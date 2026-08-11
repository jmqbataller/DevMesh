#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ROUTER=(ROOT/'plugins/devmesh/skills/using-devmesh/SKILL.md').read_text(encoding='utf-8')
EXPECTED={
'build':['codebase-intelligence','risk-engine','brainstorming-requirements','writing-plans','implementation','qa-verification','code-review'],
'fix':['codebase-intelligence','risk-engine','implementation','regression-testing','qa-verification'],
'debug':['codebase-intelligence','risk-engine','systematic-debugging','implementation','regression-testing','qa-verification','code-review'],
'redesign':['codebase-intelligence','risk-engine','brainstorming-requirements','ui-ux-review','writing-plans','implementation','browser-qa','accessibility-review','qa-verification','code-review'],
'refactor':['codebase-intelligence','risk-engine','writing-plans','implementation','qa-verification','code-review'],
'review':['codebase-intelligence','code-review'],
'deploy':['codebase-intelligence','risk-engine','qa-verification','security-review','production-deployment','git-delivery'],
'research':['codebase-intelligence']}
rows={}
for line in ROUTER.splitlines():
    if line.startswith('| ') and not line.startswith('| Task') and not line.startswith('|---'):
        cols=[c.strip() for c in line.strip('|').split('|')]
        if len(cols)>=3 and cols[0] in EXPECTED: rows[cols[0]]=cols[1]
for task,skills in EXPECTED.items():
    assert task in rows, f'missing {task}'
    pos=-1
    for skill in skills:
        nxt=rows[task].find(skill)
        assert nxt>=0, f'{task} missing {skill}'
        assert nxt>pos, f'{task} order {skill}'
        pos=nxt
for phrase in ['Quick','Standard','Deep','Eco','Balanced','Max','mission-control','dynamic-task-graph','parallel-agent-orchestration','devmesh-judge','confidence-engine','adversarial-review','change-impact-map','failure-memory','eval-replay-lab','architecture-simulator','resource-budget','incident-commander','environment-doctor','full-stack-build','database-architect','api-contract','issue-to-pr','ci-auto-heal','production-deployment','Read the real issue','Never auto-merge','Build logs alone are not production verification','Never overwrite a baseline','PASS','BLOCKED','NOT RUN']:
    assert phrase in ROUTER, f'missing router contract {phrase}'
assert '3 fix/retest rounds' in ROUTER
assert '2 repair/rejudge rounds' in ROUTER
assert 'High-risk/destructive operations require explicit authorization' in ROUTER
assert 'full-stack product working while required layers are mocked/disconnected' in ROUTER
assert 'parallel execution: BLOCKED / sequential fallback' in ROUTER
assert 'same-context fallback' in ROUTER
print('OK: routing contract validated for 8 task types and v0.7 Mission Control orchestration')
