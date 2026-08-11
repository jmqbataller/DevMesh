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
'mission-control','dynamic-task-graph','parallel-agent-orchestration','devmesh-judge','confidence-engine','adversarial-review','change-impact-map','failure-memory','eval-replay-lab','architecture-simulator','resource-budget','incident-commander',
'real-estate-idx-mls','reso-web-api','listing-sync-search','idx-compliance-review',
'wordpress-real-estate-specialist','wordpress-site-doctor','wordpress-plugin-conflict-detective','wordpress-safe-update-manager','wp-cli-operator','wordpress-rest-api-integrator','idx-provider-detector','wordpress-idx-bridge','idx-search-qa','listing-freshness-monitor','idx-compliance-monitor','idx-vow-mode-detector','wordpress-performance-doctor','wordpress-security-specialist','wordpress-lead-flow-qa','wordpress-client-handover'}
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
    if manifest.get('version')!='0.9.0': fail('manifest version')
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
    require(PLUGIN/'skills/real-estate-idx-mls/SKILL.md',['RESO Web API','VOW is not IDX','delayed-marketing','server-side','local MLS/provider rules'])
    require(PLUGIN/'skills/reso-web-api/SKILL.md',['$metadata','RESO Data Dictionary','RETS','server-side','NOT RUN'])
    require(PLUGIN/'skills/listing-sync-search/SKILL.md',['idempotent','last successful sync','objective criteria','removed/withheld listing'])
    require(PLUGIN/'skills/idx-compliance-review/SKILL.md',['Local MLS/provider rules','seller-withheld','delayed-marketing','hidden with CSS','BLOCKED'])

    require(PLUGIN/'skills/wordpress-real-estate-specialist/SKILL.md',['wordpress-site-doctor','idx-provider-detector','wordpress-lead-flow-qa','wordpress-client-handover'])
    require(PLUGIN/'skills/wordpress-site-doctor/SKILL.md',['WordPress Site Health','WP-Cron','REST API','BLOCKED'])
    require(PLUGIN/'skills/wordpress-plugin-conflict-detective/SKILL.md',['Reproduce first','--skip-plugins','staging','FIXED'])
    require(PLUGIN/'skills/wordpress-safe-update-manager/SKILL.md',['backup/restore','staging','rollback','post-update'])
    require(PLUGIN/'skills/wp-cli-operator/SKILL.md',['--ssh','--skip-plugins','High-risk operations','Never print secrets'])
    require(PLUGIN/'skills/wordpress-rest-api-integrator/SKILL.md',['show_in_rest','rest_api_init','permission_callback','Application Passwords'])
    require(PLUGIN/'skills/idx-provider-detector/SKILL.md',['vendor-hosted iframe/widget','RESO/OData','legacy RETS','confidence'])
    require(PLUGIN/'skills/wordpress-idx-bridge/SKILL.md',['privileged MLS feed','server-side','cache invalidation/freshness','confidential fields'])
    require(PLUGIN/'skills/idx-search-qa/SKILL.md',['map pins','back-to-results','browser-qa','BLOCKED'])
    require(PLUGIN/'skills/listing-freshness-monitor/SKILL.md',['last successful sync','WP-Cron','provider contract','stale'])
    require(PLUGIN/'skills/idx-compliance-monitor/SKILL.md',['Hiding with CSS is not removal','delayed-marketing','local MLS/provider rules','BLOCKED'])
    require(PLUGIN/'skills/idx-vow-mode-detector/SKILL.md',['`IDX`','`VOW`','`HYBRID`','agreements'])
    require(PLUGIN/'skills/wordpress-performance-doctor/SKILL.md',['Measure before optimizing','Lighthouse/Core Web Vitals','IDX vendor scripts','measured result'])
    require(PLUGIN/'skills/wordpress-security-specialist/SKILL.md',['risk reduction','Application Password','MLS/IDX OAuth/API credentials','least privilege'])
    require(PLUGIN/'skills/wordpress-lead-flow-qa/SKILL.md',['success message is not proof','synthetic test leads','downstream delivery','BLOCKED'])
    require(PLUGIN/'skills/wordpress-client-handover/SKILL.md',['passwords, tokens, API keys, MLS credentials','weekly/monthly/quarterly','Website Specialist'])

    chat_meta=frontmatter(CHATGPT/'SKILL.md')
    if chat_meta.get('name')!='devmesh-chatgpt' or not chat_meta.get('description'): fail('ChatGPT adapter metadata')
    require(CHATGPT/'SKILL.md',['Do not assume a local shell','Public web browsing is not Browser QA','mission-control','real-estate-idx-mls','wordpress-real-estate-specialist','wordpress-site-doctor','idx-search-qa','wordpress-lead-flow-qa','parallel execution: BLOCKED','judge independence: unavailable','PASS','BLOCKED','NOT RUN'])
    for ref in ['tool-adaptation.md','evidence-boundaries.md','invocation-examples.md']:
        if not (CHATGPT/'references'/ref).exists(): fail(f'missing ChatGPT adapter reference {ref}')

    print(f"OK: marketplace {market['name']}")
    print(f"OK: manifest {manifest['name']} v{manifest['version']}")
    print('OK: Playwright MCP configuration validated')
    print(f'OK: {len(found)} required skills and 8 task types validated')
    print('OK: ChatGPT Agent Skills adapter contract validated')
    print('OK: v0.9 WordPress Real Estate + IDX/MLS + Mission Control contracts validated')
    return 0
if __name__=='__main__': sys.exit(main())
