#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "adapters" / "gpts" / "devmesh-gpt"
CORE = ROOT / "plugins" / "devmesh" / "skills"
MANIFEST = ROOT / "plugins" / "devmesh" / ".codex-plugin" / "plugin.json"
PACK_COUNT = 10


def version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def skill_files() -> list[Path]:
    skills = sorted(CORE.glob("*/SKILL.md"))
    if not skills:
        raise SystemExit("no DevMesh core skills found")
    return skills


def split_evenly(items: list[Path], count: int) -> list[list[Path]]:
    count = max(1, min(count, len(items)))
    groups: list[list[Path]] = [[] for _ in range(count)]
    for index, item in enumerate(items):
        groups[index % count].append(item)
    return groups


def build(output: Path) -> Path:
    required = [ADAPTER / "README.md", ADAPTER / "GPT_CONFIG.md", ADAPTER / "INSTRUCTIONS.md"]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise SystemExit("missing GPT adapter files: " + ", ".join(missing))

    skills = skill_files()
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="devmesh-gpts-") as temp:
        bundle = Path(temp) / "bundle"
        bundle.mkdir(parents=True, exist_ok=True)

        for name in ["README.md", "GPT_CONFIG.md", "INSTRUCTIONS.md"]:
            shutil.copy2(ADAPTER / name, bundle / name)

        knowledge = bundle / "knowledge"
        knowledge.mkdir(parents=True, exist_ok=True)

        groups = split_evenly(skills, PACK_COUNT)
        generated: list[str] = []

        for number, group in enumerate(groups, start=1):
            filename = f"devmesh-playbooks-{number:02d}.md"
            generated.append(filename)
            lines = [
                f"# DevMesh Knowledge Pack {number:02d}",
                "",
                "Reference playbooks for DevMesh. Behavior rules live in INSTRUCTIONS.md.",
                "",
            ]
            for skill in group:
                lines.extend([
                    f"## Playbook: {skill.parent.name}",
                    "",
                    skill.read_text(encoding="utf-8").strip(),
                    "",
                ])
            (knowledge / filename).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

        (bundle / "VERSION").write_text(version() + "\n", encoding="utf-8")
        (bundle / "UPLOAD_MANIFEST.md").write_text(
            "# DevMesh GPT Upload Manifest\n\n"
            "1. Paste `INSTRUCTIONS.md` into GPT Instructions.\n"
            "2. Apply the metadata and capability recommendations in `GPT_CONFIG.md`.\n"
            "3. Upload every file below to GPT Knowledge:\n\n"
            + "\n".join(f"- `knowledge/{name}`" for name in generated)
            + "\n\n"
            f"Knowledge files: {len(generated)} (kept below the GPT limit of 20).\n",
            encoding="utf-8",
        )

        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(bundle.rglob("*")):
                if path.is_file():
                    zf.write(path, path.relative_to(bundle).as_posix())

    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the DevMesh GPT Builder knowledge/config kit.")
    parser.add_argument("--output", type=Path, help="Output ZIP path")
    args = parser.parse_args()
    output = args.output or (ROOT / "dist" / f"devmesh-gpts-kit-v{version()}.zip")
    result = build(output)
    print(f"OK: built {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
