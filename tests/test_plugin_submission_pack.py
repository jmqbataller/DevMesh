#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'docs' / 'plugin-submission'
required = {'LISTING.md','PRIVACY.md','TERMS.md','TEST_CASES.md','RELEASE_NOTES.md','SUBMISSION_CHECKLIST.md'}
found = {p.name for p in PACK.glob('*.md')}
assert not (required-found), f'missing submission files: {sorted(required-found)}'

listing=(PACK/'LISTING.md').read_text(encoding='utf-8')
for phrase in ['Submission type: **Skills only**','## Plugin name','## Short description','## Long description','## Website','## Support URL','## Privacy policy URL','## Terms URL','## Starter prompts','Mission Control','Incident Commander']:
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
assert 'DevMesh v0.7.0' in release and 'Mission Control' in release and 'DevMesh Judge' in release
checklist=(PACK/'SUBMISSION_CHECKLIST.md').read_text(encoding='utf-8')
for phrase in ['Apps Management: Write','individual verification','business verification','Skills only','Submit for Review','devmesh-chatgpt-v0.7.0.zip']:
    assert phrase in checklist, phrase
print('OK: public OpenAI Plugin Directory v0.7 submission pack validated')
