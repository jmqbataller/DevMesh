#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins' / 'devmesh'
MANIFEST = PLUGIN / '.codex-plugin' / 'plugin.json'
MARKETPLACE = ROOT / '.agents' / 'plugins' / 'marketplace.json'
MCP = PLUGIN / '.mcp.json'
CHATGPT = ROOT / 'adapters' / 'chatgpt' / 'devmesh-chatgpt'
REQUIRED = {
'using-devmesh','execution-modes','brainstorming-requirements','codebase-intelligence','environment-doctor','writing-plans','implementation','systematic-debugging','risk-engine','full-stack-build','database-architect','api-contract','architecture-guard','browser-engine','browser-qa','network-failure-qa','visual-regression','ui-ux-review','accessibility-review','performance-review','test-data-personas','regression-testing','security-review','observability-review','qa-verification','qa-reporting','code-review','multi-agent-review','ci-auto-heal','issue-to-pr','production-deployment','project-memory','git-delivery',
'mission-control','dynamic-task-graph','parallel-agent-orchestration','devmesh-judge','confidence-engine','adversarial-review','change-impact-map','failure-memory','eval-replay-lab','architecture-simulator','resource-budget','incident-commander'}
FM = re.compile(r'^---\n(.*?)\n---\n', re.S)

def fail(msg): print('ERROR:',msg); raise SystemExit(1)
def frontmatter(path):
    m=FM.match(path.read_text(encoding='utf-8'))
    if not m: fail(f'missing frontmatter: {path.relative_to(ROOT)}')
    out={}
    for line in m.group(1).splitlines():
        if ':' in line:
            k,v=line.split(':',1); out[k.strip()]=v.strip()
    return out
def require(path, phrases):
    body=path.read_text(encoding='utf-8')
    for p in phrases:
        if p not in body: fail(f'{path.relative_to(ROOT)} missing: {p}')

def main():
    manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
    market=json.loads(MARKETPLACE.read_text(encoding='utf-8'))
    mcp=json.loads(MCP.read_text(encoding='utf-8'))
    if manifest.get('name')!='devmesh': fail('manifest name')
    if manifest.get('version')!='0.7.0': fail('manifest version')
    if manifest.get('skills')!='./skills/': fail('skills path')
    if manifest.get('mcpServers')!='./.mcp.json': fail('mcp path')
    if 'hooks' in manifest: fail('hooks must not be in plugin.json')
    interface=manifest.get('interface',{})
    if len(interface.get('defaultPrompt',[]))>3: fail('defaultPrompt max 3')
    for field in ('composerIcon','logo'):
        rel=interface.get(field)
        if not rel or not rel.startswith('./') or not (PLUGIN/rel[2:]).exists(): fail(f'invalid asset {field}')
    if market.get('name')!='devmesh-marketplace': fail('marketplace name')
    entries=[p for p in market.get('plugins',[]) if p.get('name')=='devmesh']
    if len(entries)!=1 or entries[0].get('source')!={'source':'local','path':'./plugins/devmesh'}: fail('marketplace entry')
    pw=mcp.get('mcpServers',{}).get('playwright',{})
    if pw.get('command') not in {'npx','npx.cmd'}: fail('playwright command')
    if '@playwright/mcp@latest' not in pw.get('args',[]) or '--isolated' not in pw.get('args',[]): fail('playwright args')
    found={}
    for path in sorted((PLUGIN/'skills').glob('*/SKILL.md')):
        meta=frontmatter(path); name=meta.get('name')
        if not name or not meta.get('description'): fail(f'metadata {path}')
        if name!=path.parent.name or name in found: fail(f'skill identity {path}')
        found[name]=path
    if set(found)!=REQUIRED: fail(f'skill set mismatch missing={sorted(REQUIRED-set(found))} extra={sorted(set(found)-REQUIRED)}')
    router=(PLUGIN/'skills/using-devmesh/SKILL.md').read_text(encoding='utf-8')
    for task in ['build','fix','debug','redesign','refactor','review','deploy','research']:
        if f'`{task}`' not in router: fail(f'router task {task}')
    for skill in REQUIRED-{'using-devmesh'}:
        if skill not in router: fail(f'router skill {skill}')
    require(PLUGIN/'skills/mission-control/SKILL.md',['dynamic-task-graph','parallel-agent-orchestration','devmesh-judge','Maximum two judge repair rounds'])
    require(PLUGIN/'skills/dynamic-task-graph/SKILL.md',['acyclic','READY','acceptance criteria','critical path'])
    require(PLUGIN/'skills/parallel-agent-orchestration/SKILL.md',['actual sub-agent','sequential fallback','four concurrent','integrator'])
    require(PLUGIN/'skills/devmesh-judge/SKILL.md',['Evidence outranks confidence','independence: unavailable','Critical failures','BLOCKED'])
    require(PLUGIN/'skills/confidence-engine/SKILL.md',['hypothesis ledger','LOW root-cause confidence','Confidence controls','FIXED'])
    require(PLUGIN/'skills/adversarial-review/SKILL.md',['maximum of two debate rounds','single-context adversarial analysis','majority vote'])
    require(PLUGIN/'skills/change-impact-map/SKILL.md',['DIRECT','INDIRECT','UNKNOWN','Regression plan'])
    require(PLUGIN/'skills/failure-memory/SKILL.md',['Persistence is opt-in','verified fix','.devmesh/knowledge','Cross-project memory'])
    require(PLUGIN/'skills/eval-replay-lab/SKILL.md',['deterministic','cherry-pick','.devmesh/evals','NOT RUN'])
    require(PLUGIN/'skills/architecture-simulator/SKILL.md',['Simulation is not a benchmark','NEEDS MEASUREMENT','rollback'])
    require(PLUGIN/'skills/resource-budget/SKILL.md',['Eco','Balanced','Max','never'])
    require(PLUGIN/'skills/incident-commander/SKILL.md',['SEV1','preserve evidence','risk-engine','UNPROVEN','BLOCKED'])
    chat_meta=frontmatter(CHATGPT/'SKILL.md')
    if chat_meta.get('name')!='devmesh-chatgpt' or not chat_meta.get('description'): fail('ChatGPT adapter metadata')
    require(CHATGPT/'SKILL.md',['Do not assume a local shell','Public web browsing is not Browser QA','mission-control','parallel execution: BLOCKED','judge independence: unavailable','PASS','BLOCKED','NOT RUN'])
    for ref in ['tool-adaptation.md','evidence-boundaries.md','invocation-examples.md']:
        if not (CHATGPT/'references'/ref).exists(): fail(f'missing ChatGPT adapter reference {ref}')
    print(f"OK: marketplace {market['name']}")
    print(f"OK: manifest {manifest['name']} v{manifest['version']}")
    print('OK: Playwright MCP configuration validated')
    print(f'OK: {len(found)} required skills and 8 task types validated')
    print('OK: ChatGPT Agent Skills adapter contract validated')
    print('OK: v0.7 Mission Control contracts validated')
    return 0
if __name__=='__main__': sys.exit(main())
