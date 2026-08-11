# DevMesh

**DevMesh** is a provider-ready software-development agent framework that makes AI coding agents inspect, plan, build, verify, review, and report with evidence instead of jumping directly into edits.

**Codex is the first supported adapter.** The core methodology is provider-neutral so future adapters can target Claude Code, Gemini CLI, Cursor, GitHub Copilot, and other coding-agent environments.

## DevMesh v0.4

v0.4 contains **21 composable skills** plus a bundled **Playwright MCP browser engine**.

### Core engineering

1. `using-devmesh` — task router and quality-gate selection
2. `codebase-intelligence` — repository/stack/config/test/Git understanding
3. `brainstorming-requirements` — scope, constraints, acceptance criteria
4. `writing-plans` — Task → Files → Changes → Verification plans
5. `implementation` — intentional, reviewable changes
6. `systematic-debugging` — reproduce → trace → prove cause → fix
7. `risk-engine` — read-only / low / medium / high-risk action control
8. `full-stack-build` — one-prompt whole-product orchestration across frontend, backend/server logic, API, persistence, validation, and end-to-end verification when required

### Browser and product quality

9. `browser-engine` — real browser control through Playwright MCP
10. `browser-qa` — launch → render → console → viewports → interactions → screenshots → visual review → fix/retest
11. `ui-ux-review` — hierarchy, consistency, responsive UX, states, motion
12. `accessibility-review` — keyboard, focus, semantics, labels, forms, contrast, reduced motion
13. `performance-review` — bundles, images, fonts, network/runtime, measured optimization

### Correctness and safety

14. `regression-testing` — preserve confirmed bug fixes with focused automated coverage
15. `security-review` — auth, authorization, sessions, secrets, data/API/database/storage boundaries
16. `qa-verification` — tests, lint/type/build, runtime scenarios, diff verification
17. `code-review` — correctness, regressions, complexity, maintainability, test gaps
18. `multi-agent-review` — independent read-only reviewers when native subagents are available

### Memory, reporting, delivery

19. `project-memory` — opt-in `.devmesh/` project facts, decisions, QA baselines
20. `qa-reporting` — PASS/FAIL/FIXED/BLOCKED evidence and optional persistent artifacts
21. `git-delivery` — branch/commit/PR/handoff discipline

## One-prompt full-stack product build

The main v0.4 enhancement is `full-stack-build`.

A short request such as:

```text
Build a working quotation website.
```

can now trigger a product-level workflow without requiring the user to separately say:

```text
add frontend
add backend
add API
add database
connect everything
```

DevMesh treats **working** as an integrated product, not a static frontend mock.

When required by the product, it coordinates:

```text
product requirements
→ frontend
→ backend / server logic
→ API contracts
→ database / persistence
→ validation / error handling
→ auth / authorization when required
→ browser QA
→ security / accessibility / performance gates when relevant
→ end-to-end verification
→ code review / QA report
```

### Example: working quotation website

DevMesh may infer the minimum necessary capabilities such as:

- create a quotation
- add/edit/remove line items
- calculate totals
- save and load quotations
- edit existing quotations
- validate invalid/required input
- preserve data across reloads when persistence is required
- connect the UI to the real server/API/database layer

It should **not** silently invent large unrelated features such as subscriptions, payments, CRM, mass email, PDF export, or multi-company tenancy unless the request or existing product requires them.

### Greenfield behavior

When there is no existing stack and the user did not choose one, DevMesh should:

1. choose the simplest maintainable architecture supported by the environment/deployment target
2. avoid unnecessary framework duplication
3. state important defaults in the plan
4. proceed without blocking on low-impact implementation choices
5. ask only when missing information materially changes business behavior, data ownership/security, payments, destructive migrations, production integrations, or another difficult-to-reverse decision

### Completion rule

DevMesh must not call a product-level build **working** when required layers are mocked or disconnected.

Where applicable, it should exercise a real end-to-end journey similar to:

```text
open app
→ create data
→ server validates
→ persist
→ read it back
→ update it
→ reload
→ confirm persistence
```

If an external credential/service/environment is unavailable, that specific portion must be reported as `BLOCKED` or `NOT RUN` instead of being faked.

## Real Browser Engine

DevMesh bundles a Playwright MCP server:

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

When the host supports plugin MCP servers, Browser QA can use real browser automation instead of source-only inspection.

Browser QA flow:

```text
launch app
→ inspect rendered page
→ check console/runtime
→ test desktop/mobile/tablet when relevant
→ click/type/navigate
→ test forms/buttons/states
→ detect overflow/clipping/z-index issues
→ capture screenshots/artifacts
→ UI/accessibility review
→ fix real issue
→ rerun the exact failed scenario
→ add regression coverage when practical
```

Browser QA is capped at **3 autonomous fix/retest rounds** to avoid infinite loops.

## Quality gates are selected, not blindly run

DevMesh keeps the router lightweight for small tasks while deepening verification when scope/risk requires it.

```text
User Request
    ↓
Task Classification
    ↓
Codebase Intelligence
    ↓
Project Memory (only when opted in)
    ↓
Risk Engine
    ↓
Full-Stack Build (whole working products only)
    ↓
Requirements / Plan
    ↓
Implementation / Debugging
    ↓
Relevant Quality Gates
    ├── Regression Testing
    ├── Browser QA
    ├── Accessibility
    ├── Security
    ├── Performance
    └── Multi-Agent Review
    ↓
QA Verification
    ↓
Code Review
    ↓
QA Report / Git Delivery
```

Examples:

- **Whole working web app:** inspect → risk → full-stack-build → requirements → plan → implement vertical slices → Browser QA/security/accessibility/performance as relevant → QA → review
- **Tiny backend fix:** inspect → risk → implement → regression test → QA
- **Browser bug:** inspect → debug → implement → Browser QA → regression test → QA
- **Web redesign:** inspect → requirements → UI/UX → implement → Browser QA → accessibility → QA → code review
- **Auth/data feature:** inspect → risk → implement → security review → regression/QA → review
- **Release readiness:** QA → security → Browser QA → accessibility/performance when relevant → multi-agent review → report → delivery

## Risk Engine

DevMesh classifies mutating actions by blast radius:

- **Read-only** — inspect/search/diagnostics
- **Low** — scoped source/test/docs edits
- **Medium** — dependency/schema/auth/CI/env-contract/broad-refactor changes
- **High** — destructive production/data/history/external/financial/security actions

High-risk actions require explicit authorization unless that exact action was already clearly authorized in the current request.

## Project Memory

Persistent memory is **opt-in**. DevMesh never silently adds project-memory files to unrelated repositories.

When enabled:

```text
.devmesh/
├── project.json
├── decisions.md
├── qa-baseline.json
└── reports/
```

Memory stores stable non-secret project facts such as commands, architecture decisions, QA journeys, and baseline references. It must never store tokens, passwords, cookies, private keys, or `.env` contents.

## QA Reports

Substantial/release tasks can retain evidence under:

```text
.devmesh/reports/YYYY-MM-DD-HHMM-task-slug/
├── report.md
├── screenshots/
├── console.txt
├── network.md
└── artifacts/
```

Report states distinguish `PASS`, `FAIL`, `FIXED`, `BLOCKED`, and `NOT RUN`. Missing evidence is never converted into a pass.

## Multi-Agent Review

When the host environment exposes native subagents, DevMesh can dispatch independent read-only reviewers for spec/correctness, code quality, security, and browser/UI/accessibility/performance.

Reviewers do not race to edit the same working tree. The lead/implementer owns fixes. DevMesh defaults to at most four concurrent reviewers and one focused re-review round.

When subagents are unavailable, the same review briefs run sequentially.

## Install in Codex

Add the DevMesh marketplace:

```bash
codex plugin marketplace add jmqbataller/DevMesh
```

Install DevMesh:

```bash
codex plugin add devmesh@devmesh-marketplace
```

Confirm:

```bash
codex plugin list
```

After an update/reinstall, start a **new Codex thread/session** so the new skills and MCP configuration are loaded.

### Windows note

If PowerShell blocks `npm.ps1`, use `npm.cmd`/`npx.cmd` for manual Node commands. DevMesh itself declares Playwright MCP through the plugin manifest; the host plugin loader is responsible for starting it.

## Suggested v0.4 smoke test

In a disposable repository, prompt Codex with only:

```text
Use DevMesh.
Build a working quotation website.
```

Expected behavior:

- classify as a product-level `build`
- invoke `full-stack-build`
- infer the minimum required frontend/backend/API/persistence layers
- plan before implementation
- build actual integrated flows rather than frontend mocks
- run relevant Browser QA/security/accessibility/performance checks
- verify a representative persisted end-to-end journey when the environment supports it
- state clearly which external integrations or environments remain blocked

## Development validation

From the repository root:

```bash
python tests/validate_devmesh.py
python tests/test_routing_contract.py
python tests/test_feature_contracts.py
```

Expected:

```text
OK: marketplace devmesh-marketplace
OK: manifest devmesh v0.4.0
OK: Playwright MCP companion configuration validated
OK: 21 required skills and 8 task types validated
OK: one-prompt full-stack build contract validated
OK: v0.4 quality-gate contracts validated
OK: routing contract validated for 8 task types, one-prompt full-stack builds, and v0.4 quality gates
OK: full-stack build, Playwright, fix/retest, regression, security, accessibility, performance, memory, risk, reporting, and multi-agent contracts validated
```

## Repository structure

```text
DevMesh/
├── .agents/plugins/marketplace.json
├── plugins/devmesh/
│   ├── .codex-plugin/plugin.json
│   ├── .mcp.json
│   ├── assets/
│   ├── skills/
│   ├── references/
│   └── scripts/
├── tests/
├── docs/
├── AGENTS.md
├── CHANGELOG.md
└── README.md
```

## Current platform support

| Platform | Status |
|---|---|
| Codex | **v0.4 supported** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

DevMesh has no custom LLM or required backend. The active coding agent remains the execution engine; DevMesh supplies the workflow, full-stack product orchestration, browser integration, safety rules, quality gates, review orchestration, memory, and evidence requirements.

## License

MIT
