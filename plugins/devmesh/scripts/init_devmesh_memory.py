#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def detect(root: Path) -> dict:
    data = {
        "schemaVersion": 1,
        "commands": {},
        "paths": {},
    }

    package_json = root / "package.json"
    if package_json.exists():
        try:
            pkg = json.loads(package_json.read_text(encoding="utf-8"))
        except Exception:
            pkg = {}
        data["packageManager"] = (
            "pnpm" if (root / "pnpm-lock.yaml").exists()
            else "yarn" if (root / "yarn.lock").exists()
            else "npm"
        )
        scripts = pkg.get("scripts", {}) if isinstance(pkg, dict) else {}
        pm = data["packageManager"]
        prefix = "pnpm" if pm == "pnpm" else "yarn" if pm == "yarn" else "npm run"
        for key in ["dev", "build", "test", "lint", "typecheck"]:
            if key in scripts:
                data["commands"][key] = f"{prefix} {key}"
        deps = {}
        if isinstance(pkg, dict):
            deps.update(pkg.get("dependencies", {}) or {})
            deps.update(pkg.get("devDependencies", {}) or {})
        if "next" in deps:
            data["projectType"] = "nextjs"
        elif "react" in deps:
            data["projectType"] = "react"
        elif "vue" in deps:
            data["projectType"] = "vue"
        elif "svelte" in deps or "@sveltejs/kit" in deps:
            data["projectType"] = "svelte"
        else:
            data["projectType"] = "node"
        data["browserFacing"] = any(k in deps for k in ["next", "react", "vue", "svelte", "@sveltejs/kit", "vite"])

    if (root / "composer.json").exists():
        data.setdefault("projectType", "php")
    if (root / "wp-config.php").exists() or (root / "wp-content").exists():
        data["projectType"] = "wordpress"
        data["browserFacing"] = True

    source_candidates = [p for p in ["src", "app", "pages", "lib"] if (root / p).exists()]
    test_candidates = [p for p in ["tests", "test", "__tests__", "e2e"] if (root / p).exists()]
    if source_candidates:
        data["paths"]["source"] = source_candidates
    if test_candidates:
        data["paths"]["tests"] = test_candidates

    if (root / "supabase").exists():
        data["database"] = "supabase"
    if (root / "vercel.json").exists():
        data["deployment"] = "vercel"

    data["commands"] = {k: v for k, v in data["commands"].items() if v}
    data["paths"] = {k: v for k, v in data["paths"].items() if v}
    return {k: v for k, v in data.items() if v not in ({}, [], None, "")}


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize opt-in .devmesh project memory without reading secrets.")
    parser.add_argument("path", nargs="?", default=".", help="Target project directory")
    parser.add_argument("--force", action="store_true", help="Replace existing project.json only")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    memory = root / ".devmesh"
    reports = memory / "reports"
    memory.mkdir(exist_ok=True)
    reports.mkdir(exist_ok=True)

    project_file = memory / "project.json"
    if not project_file.exists() or args.force:
        project_file.write_text(json.dumps(detect(root), indent=2) + "\n", encoding="utf-8")

    decisions = memory / "decisions.md"
    if not decisions.exists():
        decisions.write_text("# DevMesh Decisions\n\nRecord durable non-secret architecture/product decisions here.\n", encoding="utf-8")

    baseline = memory / "qa-baseline.json"
    if not baseline.exists():
        baseline.write_text(json.dumps({"schemaVersion": 1, "commands": [], "browser": {"routes": [], "viewports": []}, "acceptedWarnings": []}, indent=2) + "\n", encoding="utf-8")

    print(f"Initialized DevMesh memory at {memory}")
    print("No .env files, credentials, cookies, or secret values were read.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
