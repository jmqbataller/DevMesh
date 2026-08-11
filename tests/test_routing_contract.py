#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ROUTER=(ROOT/'plugins/devmesh/skills/using-devmesh/SKILL.md').read_text(encoding='utf-8')
ROUTER_LOWER=ROUTER.lower()
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

for phrase in [
'Quick','Standard','Deep','Eco','Balanced','Max','website-product-builder','design-system-architect','sitemap-information-architecture','ui-component-architecture','mission-control','dynamic-task-graph','parallel-agent-orchestration','devmesh-judge','confidence-engine','adversarial-review','change-impact-map','failure-memory','eval-replay-lab','architecture-simulator','resource-budget','incident-commander','environment-doctor','full-stack-build','database-architect','api-contract','issue-to-pr','ci-auto-heal','production-deployment',
'wordpress-real-estate-specialist','website-operations-specialist','hosting-dns-ssl-doctor','wordpress-migration-specialist','backup-restore-drill','seo-search-console-specialist','real-estate-seo-specialist','core-web-vitals-diagnoser','analytics-conversion-qa','email-deliverability-doctor','broken-link-redirect-manager','plugin-theme-risk-intelligence','wp-cron-reliability-doctor','reso-schema-drift-detector','reso-provider-capability-inspector','client-monthly-website-report','website-emergency-recovery',
'agency-operations-control-center','multi-site-fleet-manager','scheduled-site-health-monitor','domain-ssl-expiry-monitor','wordpress-update-wave-manager','staging-production-manager','website-change-timeline','visual-history-screenshot-timeline','plugin-vulnerability-maintenance-watch','license-subscription-tracker','client-access-inventory','ticket-request-intake-agent','sla-priority-engine','lead-sla-monitor','real-estate-crm-integration-specialist','mls-provider-health-monitor','consent-privacy-cookie-auditor','accessibility-continuous-monitor','content-qa-agent','client-onboarding-agent','client-offboarding-agent',
'read the real issue','never auto-merge','build logs alone are not production verification','never overwrite a baseline','PASS','BLOCKED','NOT RUN']:
    assert phrase.lower() in ROUTER_LOWER, f'missing router contract {phrase}'
for phrase in [
'3 fix/retest rounds','2 repair/rejudge rounds','high-risk/destructive operations require explicit authorization',
'full-stack product working while required layers are mocked/disconnected','fall back sequentially','same-context fallback',
'frontend-only marketing/static sites must not get an unnecessary database or api','production completion requires real target evidence',
'backup existence is not restore proof','success ui is not inbox proof','stop rollout','technical audit is not legal certification',
'form submission is not downstream lead delivery','revocation/deletion/ownership changes require explicit authorization']:
    assert phrase.lower() in ROUTER_LOWER, f'missing router contract {phrase}'
print('OK: routing contract validated for 8 task types and v1.2 Website Product Builder + Agency Operations orchestration')
