#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "adapters" / "gpts" / "devmesh-gpt"
CORE = ROOT / "plugins" / "devmesh" / "skills"
MANIFEST = ROOT / "plugins" / "devmesh" / ".codex-plugin" / "plugin.json"
VERSION = json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]

for name in ["README.md", "GPT_CONFIG.md", "INSTRUCTIONS.md"]:
    assert (ADAPTER / name).is_file(), name

instructions = (ADAPTER / "INSTRUCTIONS.md").read_text(encoding="utf-8")
for phrase in [
    "Artifact-first delivery when supported",
    "interactive website/app artifacts",
    "PASS",
    "BLOCKED",
    "NOT RUN",
    "OBSERVED",
    "INFERRED",
    "UNKNOWN",
    "Public web browsing is research",
]:
    assert phrase in instructions, phrase

config = (ADAPTER / "GPT_CONFIG.md").read_text(encoding="utf-8")
assert "Apps" in config and "Actions" in config
assert "Do not configure Apps and Actions at the same time" in config

with tempfile.TemporaryDirectory(prefix="devmesh-gpts-test-") as tmp:
    out = Path(tmp) / "devmesh-gpts.zip"
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_gpts_kit.py"), "--output", str(out)],
        check=True,
        cwd=ROOT,
    )
    assert out.is_file()

    with zipfile.ZipFile(out) as zf:
        names = set(zf.namelist())
        assert {"README.md", "GPT_CONFIG.md", "INSTRUCTIONS.md", "VERSION", "UPLOAD_MANIFEST.md"} <= names
        knowledge = sorted(n for n in names if n.startswith("knowledge/") and n.endswith(".md"))
        assert len(knowledge) == 10
        assert len(knowledge) <= 20
        assert zf.read("VERSION").decode().strip() == VERSION

        corpus = "\n".join(zf.read(name).decode("utf-8") for name in knowledge)
        core_names = sorted(path.parent.name for path in CORE.glob("*/SKILL.md"))
        for skill_name in core_names:
            assert f"## Playbook: {skill_name}" in corpus, skill_name

print(f"OK: GPT Builder adapter v{VERSION} packages all DevMesh playbooks into 10 Knowledge files")
