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
'wordpress-real-estate-specialist','wordpress-site-doctor','wordpress-plugin-conflict-detective','wordpress-safe-update-manager','wp-cli-operator','wordpress-rest-api-integrator','idx-provider-detector','wordpress-idx-bridge','idx-search-qa','listing-freshness-monitor','idx-compliance-monitor','idx-vow-mode-detector','wordpress-performance-doctor','wordpress-security-specialist','wordpress-lead-flow-qa','wordpress-client-handover',
'website-operations-specialist','hosting-dns-ssl-doctor','wordpress-migration-specialist','backup-restore-drill','seo-search-console-specialist','real-estate-seo-specialist','core-web-vitals-diagnoser','analytics-conversion-qa','email-deliverability-doctor','broken-link-redirect-manager','plugin-theme-risk-intelligence','wp-cron-reliability-doctor','reso-schema-drift-detector','reso-provider-capability-inspector','client-monthly-website-report','website-emergency-recovery',
'agency-operations-control-center','multi-site-fleet-manager','scheduled-site-health-monitor','domain-ssl-expiry-monitor','wordpress-update-wave-manager','staging-production-manager','website-change-timeline','visual-history-screenshot-timeline','plugin-vulnerability-maintenance-watch','license-subscription-tracker','client-access-inventory','ticket-request-intake-agent','sla-priority-engine','lead-sla-monitor','real-estate-crm-integration-specialist','mls-provider-health-monitor','consent-privacy-cookie-auditor','accessibility-continuous-monitor','content-qa-agent','client-onboarding-agent','client-offboarding-agent'}
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
    if manifest.get('version')!='1.1.0': fail('manifest version')
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
    require(PLUGIN/'skills/real-estate-idx-mls/SKILL.md',['RESO Web API','VOW is not IDX','server-side','local MLS/provider rules'])
    require(PLUGIN/'skills/wordpress-real-estate-specialist/SKILL.md',['wordpress-site-doctor','idx-provider-detector','wordpress-lead-flow-qa','wordpress-client-handover'])
    require(PLUGIN/'skills/website-operations-specialist/SKILL.md',['hosting-dns-ssl-doctor','backup-restore-drill','seo-search-console-specialist','client-monthly-website-report'])

    require(PLUGIN/'skills/agency-operations-control-center/SKILL.md',['multi-site-fleet-manager','scheduled-site-health-monitor','sla-priority-engine','client-offboarding-agent'])
    require(PLUGIN/'skills/multi-site-fleet-manager/SKILL.md',['independent operational boundary','Healthy','BLOCKED'])
    require(PLUGIN/'skills/scheduled-site-health-monitor/SKILL.md',['monitoring plan is not a running monitor','daily','weekly','monthly','NOT RUN'])
    require(PLUGIN/'skills/domain-ssl-expiry-monitor/SKILL.md',['certificate validity','domain renewal','30/14/7 days','BLOCKED'])
    require(PLUGIN/'skills/wordpress-update-wave-manager/SKILL.md',['representative staging/canary wave','STOP rollout','rollback'])
    require(PLUGIN/'skills/staging-production-manager/SKILL.md',['staging and production','robots/noindex','Production PASS'])
    require(PLUGIN/'skills/website-change-timeline/SKILL.md',['Correlation is a lead, not proof','recent changes','Never store secrets'])
    require(PLUGIN/'skills/visual-history-screenshot-timeline/SKILL.md',['screenshot is evidence','never replace old snapshots','browser-control','BLOCKED'])
    require(PLUGIN/'skills/plugin-vulnerability-maintenance-watch/SKILL.md',['verified advisory/vendor evidence','affected sites','mass-disable'])
    require(PLUGIN/'skills/license-subscription-tracker/SKILL.md',['entitlement metadata','auto-renew','payment secrets'])
    require(PLUGIN/'skills/client-access-inventory/SKILL.md',['Inventory capability and ownership','AVAILABLE','MISSING','raw tokens'])
    require(PLUGIN/'skills/ticket-request-intake-agent/SKILL.md',['symptom separately','acceptance criteria','sla-priority-engine'])
    require(PLUGIN/'skills/sla-priority-engine/SKILL.md',['actual SLA','`P1`','`P2`','`P3`','`P4`'])
    require(PLUGIN/'skills/lead-sla-monitor/SKILL.md',['submitted form is not a delivered lead','synthetic test leads','CRM'])
    require(PLUGIN/'skills/real-estate-crm-integration-specialist/SKILL.md',['actual integration path','Follow Up Boss','webhook','2xx'])
    require(PLUGIN/'skills/mls-provider-health-monitor/SKILL.md',['provider health from local integration health','$metadata','UPSTREAM','LOCAL'])
    require(PLUGIN/'skills/consent-privacy-cookie-auditor/SKILL.md',['not legal compliance certification','cookies/storage','GDPR/CCPA','BLOCKED'])
    require(PLUGIN/'skills/accessibility-continuous-monitor/SKILL.md',['release property','automated scans','REGRESSION','FIXED'])
    require(PLUGIN/'skills/content-qa-agent/SKILL.md',['must not invent the correct business fact','lorem','authoritative'])
    require(PLUGIN/'skills/client-onboarding-agent/SKILL.md',['verified baseline','client-access-inventory','never passwords/tokens'])
    require(PLUGIN/'skills/client-offboarding-agent/SKILL.md',['preserve client ownership','explicit authorization','TRANSFERRED','REVOKED'])

    chat_meta=frontmatter(CHATGPT/'SKILL.md')
    if chat_meta.get('name')!='devmesh-chatgpt' or not chat_meta.get('description'): fail('ChatGPT adapter metadata')
    require(CHATGPT/'SKILL.md',['Do not assume a local shell','Public web browsing is not Browser QA','mission-control','website-operations-specialist','agency-operations-control-center','multi-site-fleet-manager','scheduled-site-health-monitor','lead-sla-monitor','real-estate-crm-integration-specialist','client-onboarding-agent','client-offboarding-agent','parallel execution: BLOCKED','judge independence: unavailable','PASS','BLOCKED','NOT RUN'])
    for ref in ['tool-adaptation.md','evidence-boundaries.md','invocation-examples.md']:
        if not (CHATGPT/'references'/ref).exists(): fail(f'missing ChatGPT adapter reference {ref}')

    print(f"OK: marketplace {market['name']}")
    print(f"OK: manifest {manifest['name']} v{manifest['version']}")
    print('OK: Playwright MCP configuration validated')
    print(f'OK: {len(found)} required skills and 8 task types validated')
    print('OK: ChatGPT Agent Skills adapter contract validated')
    print('OK: v1.1 Agency Operations + v1.0 Website Operations + WordPress/IDX/MLS contracts validated')
    return 0
if __name__=='__main__': sys.exit(main())
