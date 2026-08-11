#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / 'adapters' / 'chatgpt' / 'devmesh-chatgpt'
CORE = ROOT / 'plugins' / 'devmesh' / 'skills'
MANIFEST = ROOT / 'plugins' / 'devmesh' / '.codex-plugin' / 'plugin.json'


def version() -> str:
    return json.loads(MANIFEST.read_text(encoding='utf-8'))['version']


def build(output: Path) -> Path:
    if not (ADAPTER / 'SKILL.md').exists():
        raise SystemExit('missing ChatGPT adapter SKILL.md')

    skills = sorted(CORE.glob('*/SKILL.md'))
    if not skills:
        raise SystemExit('no DevMesh core skills found')

    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix='devmesh-chatgpt-') as temp:
        bundle = Path(temp) / 'bundle'
        shutil.copytree(ADAPTER, bundle)
        playbooks = bundle / 'playbooks'
        playbooks.mkdir(parents=True, exist_ok=True)

        for skill in skills:
            shutil.copy2(skill, playbooks / f'{skill.parent.name}.md')

        (bundle / 'VERSION').write_text(version() + '\n', encoding='utf-8')
        (bundle / 'PLAYBOOKS.md').write_text(
            '# Bundled DevMesh playbooks\n\n'
            + '\n'.join(f'- `playbooks/{p.parent.name}.md`' for p in skills)
            + '\n',
            encoding='utf-8',
        )

        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(bundle.rglob('*')):
                if path.is_file():
                    zf.write(path, path.relative_to(bundle).as_posix())

    return output


def main() -> int:
    parser = argparse.ArgumentParser(description='Build the portable DevMesh ChatGPT Agent Skill bundle.')
    parser.add_argument('--output', type=Path, help='Output ZIP path')
    args = parser.parse_args()
    output = args.output or (ROOT / 'dist' / f'devmesh-chatgpt-v{version()}.zip')
    result = build(output)
    print(f'OK: built {result}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
