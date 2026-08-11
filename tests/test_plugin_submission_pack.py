#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'docs' / 'plugin-submission'
MANIFEST = ROOT / 'plugins' / 'devmesh' / '.codex-plugin' / 'plugin.json'
VERSION = json.loads(MANIFEST.read_text(encoding='utf-8'))['version']
required = {'LISTING.md','PRIVACY.md','TERMS.md','TEST_CASES.md','RELEASE_NOTES.md','SUBMISSION_CHECKLIST.md'}
found = {p.name for p in PACK.glob('*.md')}
assert not (required-found), f'missing submission files: {sorted(required-found)}'

listing=(PACK/'LISTING.md').read_text(encoding='utf-8')
for phrase in ['Submission type: **Skills only**','## Plugin name','## Short description','## Long description','## Website','## Support URL','## Privacy policy URL','## Terms URL','## Starter prompts','Website Product Builder','Mission Control','IDX / MLS','Website Operations Specialist','Agency Operations Control Center','John Mark Bataller']:
    assert phrase in listing, phrase
privacy=(PACK/'PRIVACY.md').read_text(encoding='utf-8')
assert 'does not operate a DevMesh-controlled backend service' in privacy
assert 'does not sell personal data' in privacy
terms=(PACK/'TERMS.md').read_text(encoding='utf-8')
assert 'No independent hosted service' in terms
assert 'User responsibility' in terms
tests=(PACK/'TEST_CASES.md').read_text(encoding='utf-8')
assert tests.count('## Positive test ') == 5
assert tests.count('# Negative test ') == 3
for phrase in ['False deployment claim','Secret exposure','Pretend a bug is fixed without evidence']:
    assert phrase in tests
release=(PACK/'RELEASE_NOTES.md').read_text(encoding='utf-8')
assert f'DevMesh v{VERSION}' in release
for phrase in ['Website Product Builder','design-system-architect','sitemap-information-architecture','ui-component-architecture','Agency Operations Control Center','Website Operations Specialist','Real Estate IDX / MLS','RESO Web API','idx-compliance-review','106 composable skills']:
    assert phrase in release, phrase
checklist=(PACK/'SUBMISSION_CHECKLIST.md').read_text(encoding='utf-8')
for phrase in ['Apps Management: Write','individual verification','business verification','Skills only','Submit for Review',f'devmesh-chatgpt-v{VERSION}.zip','106 bundled playbooks','Website Product Builder']:
    assert phrase in checklist, phrase
print(f'OK: public OpenAI Plugin Directory v{VERSION} submission pack validated')
