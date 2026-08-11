# DevMesh

**DevMesh** is a provider-ready software-engineering workflow framework for AI coding agents. It makes agents inspect, plan, build, verify, review, repair, and deliver with evidence instead of jumping straight into edits.

**Codex is the first supported adapter.** The methodology is provider-neutral for future Claude Code, Gemini CLI, Cursor, Copilot, and other adapters.

## DevMesh v0.5

v0.5 contains **33 composable skills** plus a bundled **Playwright MCP browser engine**.

### Core/product engineering
- `using-devmesh` — router
- `execution-modes` — Quick / Standard / Deep
- `codebase-intelligence`
- `environment-doctor`
- `brainstorming-requirements`
- `writing-plans`
- `risk-engine`
- `full-stack-build`
- `database-architect`
- `api-contract`
- `architecture-guard`
- `implementation`
- `systematic-debugging`

### Browser/product quality
- `browser-engine`
- `browser-qa`
- `network-failure-qa`
- `visual-regression`
- `ui-ux-review`
- `accessibility-review`
- `performance-review`
- `test-data-personas`

### Correctness, security, operations
- `regression-testing`
- `security-review`
- `observability-review`
- `qa-verification`
- `code-review`
- `multi-agent-review`
- `ci-auto-heal`

### Delivery/memory
- `issue-to-pr`
- `production-deployment`
- `project-memory`
- `qa-reporting`
- `git-delivery`

## One prompt → working product

A prompt can be as short as:

```text
Use DevMesh.
Build a working quotation website.
```

DevMesh can infer the minimum required product layers instead of returning a pretty frontend mock:

```text
inspect repository/environment
→ select Standard mode (unless Quick/Deep specified)
→ risk assessment
→ full-stack product contract
→ database architecture when required
→ API contract when required
→ frontend + backend/server + persistence
→ vertical-slice integration
→ synthetic test personas when useful
→ Browser QA
→ network failure QA when relevant
→ security/accessibility/performance
→ architecture/observability review when relevant
→ QA + code review
→ report/delivery
```

It does **not** silently invent unrelated scope such as payments, subscriptions, CRM, PDF export, or multi-company tenancy unless requested or required by the existing product.

## Execution modes

```text
DevMesh Quick
→ small low-risk task
→ focused evidence

DevMesh Standard   # default
→ normal routing and relevant quality gates

DevMesh Deep
→ environment doctor
→ architecture guard
→ full relevant tests/build/lint/type checks
→ browser + network failure QA
→ accessibility/security/performance
→ visual regression when relevant
→ observability
→ multi-agent review
→ QA report
```

Modes control depth, not truthfulness. Quick mode never bypasses a safety-critical gate or high-risk authorization.

## Environment Doctor

Before blaming app code, DevMesh can detect runtime/toolchain problems, missing dependencies, package scripts, env-variable names, ports, database prerequisites, migrations, and browser/MCP availability. It never fabricates credentials or prints secret values.

## Database + API architecture

For data-backed products:

```text
requirements
→ entities/relationships/ownership
→ constraints/indexes/policies
→ migration + rollback/repair plan
→ API request/response/error/auth contract
→ contract/integration tests
→ frontend/backend integration
```

Supabase/Postgres private-data projects explicitly review RLS/policies. Service-role/database secrets stay server-side.

## Browser, resilience, and visual regression

DevMesh bundles Playwright MCP:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--isolated"]
    }
  }
}
```

Browser QA can launch the real app, inspect desktop/mobile/tablet states, click/type/navigate, inspect console/network, capture screenshots, fix real defects, and retest.

`network-failure-qa` can exercise API 4xx/5xx, timeouts, offline/slow states, malformed responses, duplicate submissions, and recovery behavior.

`visual-regression` compares stable current screenshots against approved baselines and never silently overwrites a baseline just to hide a failure.

## Issue → Working PR

When asked to solve a real GitHub issue:

```text
read actual issue/comments
→ inspect
→ reproduce/confirm
→ branch/worktree when useful
→ implement
→ regression/Browser QA
→ code review
→ commit
→ PR when authorized
```

DevMesh never auto-merges or closes the issue without explicit authorization.

## CI Auto-Heal

For failing CI:

```text
read failed workflow/job/logs
→ classify infra vs code/test/config
→ reproduce
→ prove root cause
→ fix
→ focused rerun
→ full required CI
```

It does not disable legitimate tests, weaken assertions, or add `continue-on-error` simply to make CI green.

## Production Deployment

For real release intent:

```text
preflight QA/security
→ env/migration review
→ deploy
→ health/API smoke
→ open production URL
→ live Browser QA
→ post-deploy evidence
→ rollback readiness
```

A build log alone is not a production pass. Unavailable live environments are marked `BLOCKED` rather than faked.

## Architecture + observability

`architecture-guard` detects server/client secret leaks, inappropriate direct DB access, duplicated domain logic, circular/cross-layer coupling, architecture drift, and unnecessary framework duplication while respecting small/simple codebases.

`observability-review` adds proportionate logs, error boundaries, health signals, correlation, and operational context without logging tokens, cookies, passwords, authorization headers, or sensitive payloads.

## Project memory + reports

Persistent project memory remains **opt-in**:

```text
.devmesh/
├── project.json
├── decisions.md
├── qa-baseline.json
└── reports/
```

Report states are `PASS`, `FAIL`, `FIXED`, `BLOCKED`, and `NOT RUN`. Missing evidence is never turned into a pass.

## Install / update in Codex

Initial marketplace:

```bash
codex plugin marketplace add jmqbataller/DevMesh
codex plugin add devmesh@devmesh-marketplace
```

Update an existing installation:

```bash
codex plugin marketplace upgrade devmesh-marketplace
codex plugin add devmesh@devmesh-marketplace
codex plugin list
```

Start a **new Codex thread/session** after reinstall so updated skills/MCP tools load.

## Smoke tests

Full product:
```text
Use DevMesh.
Build a working quotation website.
```

Deep production readiness:
```text
DevMesh Deep: prepare this application for production.
```

GitHub delivery:
```text
Use DevMesh to fix GitHub issue #42 and prepare a PR. Do not merge it.
```

## Development validation

```bash
python tests/validate_devmesh.py
python tests/test_routing_contract.py
python tests/test_feature_contracts.py
```

## Current platform support

| Platform | Status |
|---|---|
| Codex | **v0.5 supported** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

## License

MIT
