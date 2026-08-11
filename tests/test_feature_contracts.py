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

# Existing v0.3/v0.4 safeguards remain intact.
has('browser-qa','3 browser fix rounds','same browser scenario')
has('security-review','Supabase')
has('accessibility-review','prefers-reduced-motion')
has('performance-review','Do not invent Lighthouse/Core Web Vitals numbers')
has('project-memory','Do not silently add `.devmesh/`')
has('multi-agent-review','maximum four concurrent reviewers')

print('OK: v0.5 full-stack, environment, DB/API, Issue→PR, CI, resilience, visual, observability, architecture, modes, deployment, and legacy contracts validated')
