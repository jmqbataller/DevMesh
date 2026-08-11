# DevMesh

**DevMesh** is a provider-ready software-development agent framework that makes AI coding agents inspect, plan, implement, verify, review, and report with evidence instead of jumping directly into edits.

**Codex is the first supported adapter.** The core methodology is provider-neutral so future adapters can target Claude Code, Gemini CLI, Cursor, GitHub Copilot, and other coding-agent environments.

## DevMesh v0.3

v0.3 contains **20 composable skills** plus a bundled **Playwright MCP browser engine**.

### Core engineering

1. `using-devmesh` — task router and quality-gate selection
2. `codebase-intelligence` — repository/stack/config/test/Git understanding
3. `brainstorming-requirements` — scope, constraints, acceptance criteria
4. `writing-plans` — Task → Files → Changes → Verification plans
5. `implementation` — intentional, reviewable changes
6. `systematic-debugging` — reproduce → trace → prove cause → fix
7. `risk-engine` — read-only / low / medium / high-risk action control

### Browser and product quality

8. `browser-engine` — real browser control through Playwright MCP
9. `browser-qa` — launch → render → console → viewports → interactions → screenshots → visual review → fix/retest
10. `ui-ux-review` — hierarchy, consistency, responsive UX, states, motion
11. `accessibility-review` — keyboard, focus, semantics, labels, forms, contrast, reduced motion
12. `performance-review` — bundles, images, fonts, network/runtime, measured optimization

### Correctness and safety

13. `regression-testing` — preserve confirmed bug fixes with focused automated coverage
14. `security-review` — auth, authorization, sessions, secrets, data/API/database/storage boundaries
15. `qa-verification` — tests, lint/type/build, runtime scenarios, diff verification
16. `code-review` — correctness, regressions, complexity, maintainability, test gaps
17. `multi-agent-review` — independent read-only reviewers when native subagents are available

### Memory, reporting, delivery

18. `project-memory` — opt-in `.devmesh/` project facts, decisions, QA baselines
19. `qa-reporting` — PASS/FAIL/FIXED/BLOCKED evidence and optional persistent artifacts
20. `git-delivery` — branch/commit/PR/handoff discipline

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

DevMesh keeps the router lightweight for small tasks while deepening verification when risk/scope requires it.

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
Requirements / Plan (when needed)
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

Report states distinguish:

- `PASS`
- `FAIL`
- `FIXED`
- `BLOCKED`
- `NOT RUN`

Missing evidence is never converted into a pass.

## Multi-Agent Review

When the host environment exposes native subagents, DevMesh can dispatch independent read-only reviewers for:

- spec/correctness
- code quality
- security
- browser/UI/accessibility/performance

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

## Suggested v0.3 smoke test

In a disposable web project:

```text
Use DevMesh.
Build a responsive settings page with a form.
Run the relevant quality gates.
Launch the real app in the browser, test desktop and mobile, check console errors,
exercise the form, capture screenshots, fix any real issues and retest them.
Add regression coverage for bugs you discover when practical.
Do not claim a quality gate passed without evidence.
```

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
OK: manifest devmesh v0.3.0
OK: Playwright MCP companion configuration validated
OK: 20 required skills and 8 task types validated
OK: v0.3 quality-gate contracts validated
OK: routing contract validated for 8 task types and v0.3 quality gates
OK: Playwright, fix/retest, regression, security, accessibility, performance, memory, risk, reporting, and multi-agent contracts validated
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
| Codex | **v0.3 supported** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

DevMesh has no custom LLM or required backend. The active coding agent remains the execution engine; DevMesh supplies the workflow, browser integration, safety rules, quality gates, review orchestration, memory, and evidence requirements.

## License

MIT
