#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ROUTER=(ROOT/'plugins/devmesh/skills/using-devmesh/SKILL.md').read_text(encoding='utf-8')
EXPECTED={
'build':['codebase-intelligence','brainstorming-requirements','writing-plans','implementation','qa-verification','code-review'],
'fix':['codebase-intelligence','implementation','qa-verification'],
'debug':['codebase-intelligence','systematic-debugging','implementation','qa-verification','code-review'],
'redesign':['codebase-intelligence','brainstorming-requirements','ui-ux-review','writing-plans','implementation','qa-verification','code-review'],
'refactor':['codebase-intelligence','writing-plans','implementation','qa-verification','code-review'],
'review':['codebase-intelligence','code-review'],
'deploy':['codebase-intelligence','qa-verification','git-delivery'],
'research':['codebase-intelligence'],
}
lines=[line for line in ROUTER.splitlines() if line.startswith('| ') and not line.startswith('| Task') and not line.startswith('|---')]
rows={}
for line in lines:
    cols=[c.strip() for c in line.strip('|').split('|')]
    if len(cols)>=3 and cols[0] in EXPECTED:
        rows[cols[0]]=cols[1]
for task,skills in EXPECTED.items():
    assert task in rows, f'missing routing row: {task}'
    pos=-1
    for skill in skills:
        nxt=rows[task].find(skill)
        assert nxt>=0, f'{task}: missing {skill}'
        assert nxt>pos, f'{task}: wrong order for {skill}'
        pos=nxt
print('OK: routing contract validated for 8 task types')
