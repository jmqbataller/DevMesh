#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = (ROOT / 'plugins/devmesh/skills/using-devmesh/SKILL.md').read_text(encoding='utf-8')

EXPECTED = {
    'build': [
        'codebase-intelligence',
        'risk-engine',
        'brainstorming-requirements',
        'writing-plans',
        'implementation',
        'qa-verification',
        'code-review',
    ],
    'fix': [
        'codebase-intelligence',
        'risk-engine',
        'implementation',
        'regression-testing',
        'qa-verification',
    ],
    'debug': [
        'codebase-intelligence',
        'risk-engine',
        'systematic-debugging',
        'implementation',
        'regression-testing',
        'qa-verification',
        'code-review',
    ],
    'redesign': [
        'codebase-intelligence',
        'risk-engine',
        'brainstorming-requirements',
        'ui-ux-review',
        'writing-plans',
        'implementation',
        'browser-qa',
        'accessibility-review',
        'qa-verification',
        'code-review',
    ],
    'refactor': [
        'codebase-intelligence',
        'risk-engine',
        'writing-plans',
        'implementation',
        'qa-verification',
        'code-review',
    ],
    'review': [
        'codebase-intelligence',
        'code-review',
    ],
    'deploy': [
        'codebase-intelligence',
        'risk-engine',
        'qa-verification',
        'security-review',
        'git-delivery',
    ],
    'research': ['codebase-intelligence'],
}

lines = [
    line
    for line in ROUTER.splitlines()
    if line.startswith('| ') and not line.startswith('| Task') and not line.startswith('|---')
]
rows = {}
for line in lines:
    cols = [c.strip() for c in line.strip('|').split('|')]
    if len(cols) >= 3 and cols[0] in EXPECTED:
        rows[cols[0]] = cols[1]

for task, skills in EXPECTED.items():
    assert task in rows, f'missing routing row: {task}'
    pos = -1
    for skill in skills:
        nxt = rows[task].find(skill)
        assert nxt >= 0, f'{task}: missing {skill}'
        assert nxt > pos, f'{task}: wrong order for {skill}'
        pos = nxt

CONDITIONS = [
    'full-stack-build for whole working app/site/system',
    'browser-qa + accessibility-review for browser UI',
    'security-review for auth/data/API',
    'performance-review for substantial/public web work',
    'multi-agent-review for large/high-risk changes',
    'qa-reporting',
    'systematic-debugging when root cause is not proven',
    'browser-qa for browser defects',
    'security-review for security-sensitive fixes',
    'browser-qa for web release',
    'accessibility/performance gates for public UI',
]
for phrase in CONDITIONS:
    assert phrase in ROUTER, f'missing routing condition: {phrase}'

assert 'Invoke `full-stack-build` automatically' in ROUTER
assert 'Build a working quotation website' in ROUTER
assert 'after `risk-engine`' in ROUTER
assert 'frontend, backend, API, and database layers' in ROUTER
assert 'browser-qa` invokes `browser-engine`' in ROUTER
assert '3 fix/retest rounds' in ROUTER
assert 'Persistent `.devmesh/reports/` files are opt-in' in ROUTER
assert 'High-risk actions require explicit authorization' in ROUTER

print('OK: routing contract validated for 8 task types, one-prompt full-stack builds, and v0.4 quality gates')
