#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins' / 'devmesh'


def text(skill: str) -> str:
    return (PLUGIN / 'skills' / skill / 'SKILL.md').read_text(encoding='utf-8')

mcp = json.loads((PLUGIN / '.mcp.json').read_text(encoding='utf-8'))
playwright = mcp['mcpServers']['playwright']
assert playwright['command'] in {'npx', 'npx.cmd'}
assert '-y' in playwright['args']
assert '@playwright/mcp@latest' in playwright['args']
assert '--isolated' in playwright['args']

full_stack = text('full-stack-build')
assert 'working quotation website' in full_stack.lower()
assert 'frontend mock' in full_stack.lower()
assert 'Backend / server logic' in full_stack
assert 'API contract' in full_stack
assert 'Database / persistence' in full_stack
assert 'Mandatory integration checks' in full_stack
assert 'create data → server validates → persist → read it back → update it → reload page → confirm persistence' in full_stack
assert 'payments' in full_stack
assert 'Do not silently invent' in full_stack
assert 'fake APIs' in full_stack

assert 'Playwright MCP' in text('browser-engine')
assert 'same browser scenario' in text('browser-qa')
assert '3 browser fix rounds' in text('browser-qa')
assert 'fail before the fix' in text('regression-testing')
assert 'Supabase' in text('security-review')
assert 'prefers-reduced-motion' in text('accessibility-review')
assert 'Do not invent Lighthouse/Core Web Vitals numbers' in text('performance-review')
assert 'Do not silently add `.devmesh/`' in text('project-memory')
assert 'High risk' in text('risk-engine')
assert 'BLOCKED' in text('qa-reporting')
assert 'maximum four concurrent reviewers' in text('multi-agent-review')
assert 'reviewers should be read-only' in text('multi-agent-review').lower()

print('OK: full-stack build, Playwright, fix/retest, regression, security, accessibility, performance, memory, risk, reporting, and multi-agent contracts validated')
