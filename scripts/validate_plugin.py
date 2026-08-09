#!/usr/bin/env python3
"""Static structural validation for DevMesh."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
REQUIRED_SKILLS = {
    "using-devmesh",
    "brainstorming-requirements",
    "codebase-intelligence",
    "writing-plans",
    "implementation",
    "systematic-debugging",
    "ui-ux-review",
    "qa-verification",
    "code-review",
    "git-delivery",
}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        fail(f"Missing YAML-like frontmatter: {path.relative_to(ROOT)}")
    result: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def main() -> int:
    if not MANIFEST.exists():
        fail("Missing .codex-plugin/plugin.json")

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid plugin.json: {exc}")

    for key in ("name", "version", "description", "skills"):
        if not manifest.get(key):
            fail(f"Manifest is missing required field: {key}")

    if manifest["skills"] != "./skills/":
        fail("Manifest skills path must be ./skills/")

    skills_root = ROOT / "skills"
    discovered: dict[str, Path] = {}
    for skill_file in sorted(skills_root.glob("*/SKILL.md")):
        meta = parse_frontmatter(skill_file)
        name = meta.get("name")
        description = meta.get("description")
        if not name or not description:
            fail(f"Skill needs name and description: {skill_file.relative_to(ROOT)}")
        if name in discovered:
            fail(f"Duplicate skill name: {name}")
        if skill_file.parent.name != name:
            fail(
                f"Skill directory '{skill_file.parent.name}' does not match frontmatter name '{name}'"
            )
        discovered[name] = skill_file

    missing = REQUIRED_SKILLS - discovered.keys()
    extra = discovered.keys() - REQUIRED_SKILLS
    if missing:
        fail(f"Missing required skills: {', '.join(sorted(missing))}")
    if extra:
        fail(f"Unexpected skills: {', '.join(sorted(extra))}")

    print(f"OK: manifest '{manifest['name']}' v{manifest['version']}")
    print(f"OK: {len(discovered)} required skills validated")
    print("OK: skill names, directories, descriptions, and manifest path are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
