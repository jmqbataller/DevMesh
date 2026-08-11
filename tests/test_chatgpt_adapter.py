#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / 'adapters' / 'chatgpt' / 'devmesh-chatgpt'
CORE = ROOT / 'plugins' / 'devmesh' / 'skills'
MANIFEST = ROOT / 'plugins' / 'devmesh' / '.codex-plugin' / 'plugin.json'
VERSION = json.loads(MANIFEST.read_text(encoding='utf-8'))['version']

skill = (ADAPTER / 'SKILL.md').read_text(encoding='utf-8')
assert skill.startswith('---\n')
assert 'name: devmesh-chatgpt' in skill
assert 'Agent Skills format' in skill
assert f'v{VERSION}' in skill
assert 'Do not assume a local shell' in skill
assert 'Public web browsing is not Browser QA' in skill
assert 'mission-control' in skill
assert 'real-estate-idx-mls' in skill
assert 'wordpress-real-estate-specialist' in skill
assert 'wordpress-site-doctor' in skill
assert 'idx-provider-detector' in skill
assert 'idx-search-qa' in skill
assert 'wordpress-lead-flow-qa' in skill
assert 'parallel execution: BLOCKED' in skill
assert 'judge independence: unavailable' in skill
assert '`PASS`' in skill and '`BLOCKED`' in skill and '`NOT RUN`' in skill

for name in ['tool-adaptation.md', 'evidence-boundaries.md', 'invocation-examples.md']:
    assert (ADAPTER / 'references' / name).is_file(), name

with tempfile.TemporaryDirectory(prefix='devmesh-adapter-test-') as tmp:
    out = Path(tmp) / 'devmesh-chatgpt.zip'
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'build_chatgpt_adapter.py'), '--output', str(out)], check=True, cwd=ROOT)
    assert out.is_file()
    with zipfile.ZipFile(out) as zf:
        names = set(zf.namelist())
        assert {'SKILL.md','VERSION','PLAYBOOKS.md','references/tool-adaptation.md'} <= names
        bundled = {n for n in names if n.startswith('playbooks/') and n.endswith('.md')}
        core = {f'playbooks/{p.parent.name}.md' for p in CORE.glob('*/SKILL.md')}
        assert bundled == core
        assert zf.read('VERSION').decode().strip() == VERSION
        for playbook in [
            'mission-control','devmesh-judge','incident-commander',
            'real-estate-idx-mls','reso-web-api','listing-sync-search','idx-compliance-review',
            'wordpress-real-estate-specialist','wordpress-site-doctor','wordpress-plugin-conflict-detective',
            'wordpress-safe-update-manager','wp-cli-operator','wordpress-rest-api-integrator',
            'idx-provider-detector','wordpress-idx-bridge','idx-search-qa','listing-freshness-monitor',
            'idx-compliance-monitor','idx-vow-mode-detector','wordpress-performance-doctor',
            'wordpress-security-specialist','wordpress-lead-flow-qa','wordpress-client-handover']:
            assert f'playbooks/{playbook}.md' in names

print(f'OK: ChatGPT adapter v{VERSION} source and portable WordPress real-estate upload bundle validated')
