#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / 'adapters' / 'chatgpt' / 'devmesh-chatgpt'
CORE = ROOT / 'plugins' / 'devmesh' / 'skills'

skill = (ADAPTER / 'SKILL.md').read_text(encoding='utf-8')
assert skill.startswith('---\n')
assert 'name: devmesh-chatgpt' in skill
assert 'Agent Skills format' in skill
assert 'Do not assume a local shell' in skill
assert 'Public web browsing is not Browser QA' in skill
assert 'connected GitHub' in skill
assert '`PASS`' in skill and '`BLOCKED`' in skill and '`NOT RUN`' in skill

for name in ['tool-adaptation.md', 'evidence-boundaries.md', 'invocation-examples.md']:
    assert (ADAPTER / 'references' / name).is_file(), name

with tempfile.TemporaryDirectory(prefix='devmesh-adapter-test-') as tmp:
    out = Path(tmp) / 'devmesh-chatgpt.zip'
    subprocess.run(
        [sys.executable, str(ROOT / 'scripts' / 'build_chatgpt_adapter.py'), '--output', str(out)],
        check=True,
        cwd=ROOT,
    )
    assert out.is_file()
    with zipfile.ZipFile(out) as zf:
        names = set(zf.namelist())
        assert 'SKILL.md' in names
        assert 'VERSION' in names
        assert 'PLAYBOOKS.md' in names
        assert 'references/tool-adaptation.md' in names
        bundled = {n for n in names if n.startswith('playbooks/') and n.endswith('.md')}
        core = {f'playbooks/{p.parent.name}.md' for p in CORE.glob('*/SKILL.md')}
        assert bundled == core
        assert zf.read('VERSION').decode().strip() == '0.6.0'

print('OK: ChatGPT adapter source and portable upload bundle validated')
