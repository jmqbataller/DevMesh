#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT/'plugins'/'devmesh'

def text(name: str) -> str:
    return (PLUGIN/'skills'/name/'SKILL.md').read_text(encoding='utf-8')

def has(name: str, *phrases: str) -> None:
    body = text(name)
    for phrase in phrases:
        assert phrase in body, f'{name} missing {phrase!r}'

mcp = json.loads((PLUGIN/'.mcp.json').read_text(encoding='utf-8'))
playwright = mcp['mcpServers']['playwright']
assert playwright['command'] in {'npx','npx.cmd'}
assert '@playwright/mcp@latest' in playwright['args']
assert '--isolated' in playwright['args']

# v0.9 WordPress Real Estate Specialist
has('wordpress-real-estate-specialist','wordpress-site-doctor','wordpress-plugin-conflict-detective','idx-provider-detector','idx-search-qa','wordpress-security-specialist','wordpress-client-handover')
has('wordpress-site-doctor','WordPress Site Health','PHP/server/database','WP-Cron','REST API','permalinks','BLOCKED')
has('wordpress-plugin-conflict-detective','Reproduce first','--skip-plugins','--skip-themes','staging','FIXED')
has('wordpress-safe-update-manager','backup/restore','staging','rollback','post-update','IDX search/detail/map/lead/freshness')
has('wp-cli-operator','wp plugin','wp cron','--ssh','--http','--skip-plugins','High-risk operations','Never print secrets')
has('wordpress-rest-api-integrator','show_in_rest','rest_api_init','permission_callback','Application Passwords','server-side')
has('idx-provider-detector','vendor-hosted iframe/widget','live server-side API query','replicated/local listing database/search index','RESO/OData','legacy RETS')
has('wordpress-idx-bridge','privileged MLS feed','server-side','cache invalidation/freshness','withheld/removed/delayed-marketing','confidential fields')
has('idx-search-qa','price min/max','map pins','back-to-results','browser-qa','Network 429/5xx/timeouts')
has('listing-freshness-monitor','last successful sync','checkpoint','WP-Cron','provider contract','stale public listing')
has('idx-compliance-monitor','Internet-display-withheld','delayed-marketing','Hiding with CSS is not removal','rule source/version','BLOCKED')
has('idx-vow-mode-detector','`IDX`','`VOW`','`HYBRID`','broker-consumer relationship','agreements')
has('wordpress-performance-doctor','Measure before optimizing','Lighthouse/Core Web Vitals','IDX vendor scripts','cache','measured result')
has('wordpress-security-specialist','risk reduction','least privilege','permission_callback','Application Password','MLS/IDX OAuth/API credentials')
has('wordpress-lead-flow-qa','success message is not proof','schedule/request showing','duplicate submit','synthetic test leads','downstream delivery')
has('wordpress-client-handover','passwords, tokens, API keys, MLS credentials','active theme/child theme','weekly/monthly/quarterly','Website Specialist')

# v0.8 real-estate IDX / MLS specialization
has('real-estate-idx-mls','RESO Web API','RETS','VOW is not IDX','seller instructions','delayed-marketing','server-side','local MLS/provider rules','BLOCKED')
has('reso-web-api','$metadata','RESO Data Dictionary','OData','RETS','server-side','401/403/429/5xx','NOT RUN')
has('listing-sync-search','authoritative MLS/provider','idempotent','checkpoint','last successful sync','objective criteria','removed/withheld listing','map/list result consistency')
has('idx-compliance-review','Local MLS/provider rules','seller-withheld','delayed-marketing','confidential','VOW distinction','hidden with CSS','BLOCKED')

# v0.7 Mission Control stack
has('mission-control','dynamic-task-graph','parallel-agent-orchestration','devmesh-judge','architecture-simulator','failure-memory','eval-replay-lab','Maximum two judge repair rounds')
has('dynamic-task-graph','acyclic','READY','acceptance criteria','critical path','Replanning')
has('parallel-agent-orchestration','actual sub-agent','sequential fallback','at most four concurrent workers','integrator')
has('devmesh-judge','Evidence outranks confidence','independence: unavailable','Critical failures','release decision')
has('confidence-engine','hypothesis ledger','HIGH','MEDIUM','LOW root-cause confidence','not proof')
has('adversarial-review','maximum of two debate rounds','single-context adversarial analysis','majority vote alone is not evidence')
has('change-impact-map','DIRECT','INDIRECT','UNKNOWN','Regression plan','blast radius')
has('failure-memory','Persistence is opt-in','verified lessons','.devmesh/knowledge','Cross-project memory','Never store secrets')
has('eval-replay-lab','repeatable cases','deterministic','cherry-pick','.devmesh/evals','self-modify')
has('architecture-simulator','Simulation is not a benchmark','concurrent edits','rollback','NEEDS MEASUREMENT')
has('resource-budget','Eco','Balanced','Max','orthogonal','safety-critical gate')
has('incident-commander','SEV1','preserve evidence','confidence-engine','risk-engine','UNPROVEN','resolved')

# Legacy contracts remain intact.
has('execution-modes','Quick','Standard','Deep','never bypass')
has('environment-doctor','runtime/toolchain','port conflicts','Do not fabricate credentials')
has('database-architect','constraints','indexes','RLS/policies','rollback')
has('api-contract','request','response','authentication and authorization','contract/integration tests')
has('issue-to-pr','read issue','reproduce/confirm','create/update a PR','Never close an issue')
has('production-deployment','Preflight','health/readiness','actual production target','rollback')
has('visual-regression','baseline','REGRESSION','silently overwrite')
has('network-failure-qa','API 4xx/5xx','timeout','offline','duplicate submit')
has('test-data-personas','synthetic','production data','deterministic')
has('observability-review','structured server logs','health/readiness','Never log passwords')
has('ci-auto-heal','read logs','root cause','make CI green')
has('architecture-guard','server-only','direct database access','circular dependencies')
has('full-stack-build','database-architect','api-contract','architecture-guard','test-data-personas','network-failure-qa','visual-regression','observability-review')
has('browser-qa','3 browser fix rounds','same browser scenario')
has('security-review','Supabase')
has('accessibility-review','prefers-reduced-motion')
has('performance-review','Do not invent Lighthouse/Core Web Vitals numbers')
has('project-memory','Do not silently add `.devmesh/`')
has('multi-agent-review','maximum four concurrent reviewers')

print('OK: v0.9 WordPress Real Estate, v0.8 IDX/MLS, Mission Control, and legacy feature contracts validated')
