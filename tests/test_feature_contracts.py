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

# Previous contracts remain intact.
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

print('OK: v0.8 IDX/MLS, v0.7 Mission Control, and legacy feature contracts validated')
