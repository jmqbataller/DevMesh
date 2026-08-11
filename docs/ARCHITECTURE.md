# Architecture

DevMesh is a **provider-neutral engineering workflow layer** for AI coding agents, not a separate model.

The host agent supplies reasoning and execution. DevMesh supplies task routing, risk control, browser automation integration, engineering methodology, quality gates, review orchestration, project memory, and evidence requirements. **Codex is the first supported adapter.**

## v0.3 request lifecycle

```text
User request
   ↓
using-devmesh
   ├── classify task
   ├── codebase-intelligence
   ├── project-memory (opt-in/existing)
   └── risk-engine before mutation
   ↓
Requirements / plan when needed
   ↓
Implementation or systematic debugging
   ↓
Relevant gates selected by surface/risk
   ├── regression-testing
   ├── browser-engine → browser-qa
   ├── ui-ux-review
   ├── accessibility-review
   ├── security-review
   ├── performance-review
   └── multi-agent-review
   ↓
qa-verification
   ↓
code-review
   ↓
qa-reporting / git-delivery
```

The router selects the **minimum safe and evidence-producing workflow**. Installing every skill does not mean executing every skill on every task.

## Codex adapter

```text
plugins/devmesh/
├── .codex-plugin/plugin.json
├── .mcp.json                    # Playwright MCP
├── assets/
├── skills/
├── references/
└── scripts/
```

The Codex plugin manifest exposes DevMesh skills and a companion MCP configuration. The bundled Playwright server is a local stdio MCP process started with `npx`; the browser methodology remains provider-neutral so future adapters can map an equivalent browser engine.

## Skill groups

### Orchestration

| Skill | Responsibility |
|---|---|
| using-devmesh | classify task and select workflow |
| risk-engine | action-risk classification and approval behavior |
| project-memory | opt-in persistent non-secret project context |
| multi-agent-review | independent reviewer orchestration / sequential fallback |
| qa-reporting | evidence matrix and artifact/report persistence |

### Discovery and implementation

| Skill | Responsibility |
|---|---|
| codebase-intelligence | understand current repository/stack/config/test/Git state |
| brainstorming-requirements | freeze scope, constraints, acceptance criteria |
| writing-plans | executable implementation plan |
| implementation | intentional scoped code changes |
| systematic-debugging | reproduce/trace/prove root cause |
| regression-testing | preserve bug fixes/behavior contracts |

### Browser and experience

| Skill | Responsibility |
|---|---|
| browser-engine | actual browser execution and evidence transport |
| browser-qa | rendered functional/responsive/runtime QA and fix/retest loop |
| ui-ux-review | product/UI design quality |
| accessibility-review | keyboard, semantics, focus, forms, contrast, motion |
| performance-review | loading/runtime/resource evidence and optimization |

### Verification and delivery

| Skill | Responsibility |
|---|---|
| security-review | auth/data/secrets/API/security boundaries |
| qa-verification | project-native automated/static verification |
| code-review | correctness/maintainability/regression review |
| git-delivery | branch/commit/PR/handoff discipline |

## Browser architecture

`browser-qa` owns the verification contract; `browser-engine` owns browser control.

```text
browser-qa
    ↓
browser-engine
    ↓
Playwright MCP (Codex v0.3 adapter)
    ↓
real page/session
```

If the host cannot provide a real browser engine, Browser QA must report the gate as blocked/partial rather than pretending source inspection proves rendered behavior.

## Fix/retest architecture

Verification skills may route defects back to implementation:

```text
Observed defect
   ↓
prove root cause
   ↓
implementation
   ↓
rerun exact failed scenario
   ↓
regression-testing when practical
```

Browser QA caps autonomous fix/retest at three rounds. Multi-agent review caps itself to an initial review, one fix round, and one focused re-review.

## Project memory boundary

Persistent memory is deliberately opt-in:

```text
.devmesh/
├── project.json
├── decisions.md
├── qa-baseline.json
└── reports/
```

Current source/config always outranks stored memory. Secrets and sensitive personal data are forbidden from DevMesh memory and QA artifacts.

## Multi-agent model

DevMesh does not require multi-agent support. When native subagents exist, reviewers are independent/read-only and the lead/implementer owns edits. When native subagents do not exist, reviewer roles execute sequentially using the same contracts.

This preserves compatibility across providers while allowing Codex to use native agent tooling where available.

## Adapter roadmap

Future adapters should map native capabilities to the same contracts rather than fork the methodology:

- Claude Code
- Gemini CLI
- Cursor
- GitHub Copilot
- other coding-agent environments

A future adapter may use a different browser tool, subagent mechanism, or plugin format while preserving DevMesh's evidence boundaries and workflow semantics.
