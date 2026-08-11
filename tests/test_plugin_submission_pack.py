#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'docs' / 'plugin-submission'

required = {
    'LISTING.md',
    'PRIVACY.md',
    'TERMS.md',
    'TEST_CASES.md',
    'RELEASE_NOTES.md',
    'SUBMISSION_CHECKLIST.md',
}

found = {p.name for p in PACK.glob('*.md')}
missing = required - found
assert not missing, f'missing submission files: {sorted(missing)}'

listing = (PACK / 'LISTING.md').read_text(encoding='utf-8')
for phrase in [
    'Submission type: **Skills only**',
    '## Plugin name',
    '## Short description',
    '## Long description',
    '## Website',
    '## Support URL',
    '## Privacy policy URL',
    '## Terms URL',
    '## Starter prompts',
]:
    assert phrase in listing, phrase

privacy = (PACK / 'PRIVACY.md').read_text(encoding='utf-8')
assert 'does not operate a DevMesh-controlled backend service' in privacy
assert 'does not sell personal data' in privacy

terms = (PACK / 'TERMS.md').read_text(encoding='utf-8')
assert 'No independent hosted service' in terms
assert 'User responsibility' in terms

tests = (PACK / 'TEST_CASES.md').read_text(encoding='utf-8')
assert tests.count('## Positive test ') == 5
assert tests.count('# Negative test ') == 3
assert 'False deployment claim' in tests
assert 'Secret exposure' in tests
assert 'Pretend a bug is fixed without evidence' in tests

checklist = (PACK / 'SUBMISSION_CHECKLIST.md').read_text(encoding='utf-8')
for phrase in ['Apps Management: Write', 'individual verification', 'business verification', 'Skills only', 'Submit for Review']:
    assert phrase in checklist, phrase

print('OK: public OpenAI Plugin Directory submission pack validated')
