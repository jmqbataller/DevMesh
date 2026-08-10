# DevMesh

**DevMesh** is a provider-ready software development agent framework that routes coding work through the right engineering workflow instead of letting an AI coding agent jump directly into edits.

**Codex is the first supported adapter.** The core methodology is intentionally provider-neutral so DevMesh can expand to Claude Code, Gemini CLI, Cursor, GitHub Copilot, and other coding-agent environments.

## What DevMesh does

DevMesh v0.2.0 contains 11 core workflows:

1. **Bootstrap / Agent Router** — classify `build`, `fix`, `debug`, `redesign`, `refactor`, `review`, `deploy`, or `research` requests and select the minimum safe workflow.
2. **Brainstorm / Requirements** — turn larger or ambiguous requests into goals, constraints, acceptance criteria, and frozen scope.
3. **Codebase Intelligence** — inspect instructions, stack, architecture, config boundaries, tests, and Git state before editing.
4. **Planning Agent** — produce `Task → Files → Changes → Verification` plans.
5. **Implementation Agent** — make intentional changes in logical, reviewable units.
6. **Debug Agent** — reproduce → trace → hypothesize → prove root cause → fix → regression verify.
7. **UI/UX Agent** — review hierarchy, responsiveness, spacing, accessibility, states, motion, overflow, and consistency.
8. **Browser QA Agent** — launch the app → inspect the rendered page → check console/runtime errors → test desktop/mobile → click interactions → detect overflow → test forms/buttons → capture screenshots → perform visual review → report/fix/retest real issues.
9. **QA / Verification Agent** — run targeted tests, lint/type/build checks, runtime scenarios, UI checks, and final diff inspection.
10. **Code Review Agent** — second-pass review for correctness, security, regressions, complexity, maintainability, and test gaps.
11. **Git / Delivery Agent** — protect working-tree scope and prepare intentional branches, commits, PRs, or handoffs.

## Browser QA evidence rule

DevMesh does not treat source-code inspection as browser verification.

When browser capability is available, `browser-qa` should gather rendered evidence from the actual app. When the active agent cannot launch or control a browser, it must say so explicitly and must **not** claim that responsive layout, interactions, console state, screenshots, or visual QA passed.

The Browser QA flow is:

```text
launch app
→ inspect rendered page
→ check console errors
→ test desktop/mobile
→ click interactions
→ detect overflow
→ test forms/buttons
→ take screenshots
→ visual review
→ report/fix issues
→ retest affected scenarios
```

## Core philosophy

```text
Inspect before editing.
Prove root cause before fixing.
Use the minimum safe workflow.
Preserve unrelated working behavior.
Rendered browser claims require browser evidence.
Verify before claiming completion.
```

## Request routing

```text
User Request
    ↓
DevMesh Router
    ↓
Codebase Intelligence
    ↓
Requirements / Planning (when needed)
    ↓
Implementation or Systematic Debugging
    ↓
UI/UX Review (frontend/design work)
    ↓
Browser QA (runnable browser-facing work)
    ↓
QA Verification
    ↓
Code Review
    ↓
Git Delivery (when requested/available)
```

The router deliberately does **not** run all workflows for every request. Browser QA is required for redesigns with a runnable browser surface and is conditionally selected for other browser-facing build, fix, debug, review, refactor, and deployment work.

## Repository structure

```text
DevMesh/
├── .agents/
│   └── plugins/
│       └── marketplace.json       # Codex marketplace catalog
├── plugins/
│   └── devmesh/                   # Codex adapter package
│       ├── .codex-plugin/
│       │   └── plugin.json
│       ├── skills/
│       │   ├── browser-qa/
│       │   └── ...
│       ├── references/
│       └── scripts/
├── tests/
│   ├── validate_devmesh.py
│   └── test_routing_contract.py
├── docs/
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Install in Codex CLI

Install the DevMesh GitHub repository as a marketplace:

```bash
codex plugin marketplace add jmqbataller/DevMesh
```

Then install DevMesh from that marketplace:

```bash
codex plugin add devmesh@devmesh-marketplace
```

Confirm Codex sees it:

```bash
codex plugin list
```

After installing or updating DevMesh, **start a new Codex thread/session** before testing so the installed skills are included in the newly rendered prompt.

### Updating DevMesh

Refresh/re-add the marketplace if needed, then reinstall DevMesh. The exact update command can vary by Codex CLI version; `codex plugin list` should show the installed DevMesh version after refresh/reinstall.

## Smoke tests

Use a small disposable code repository for these tests.

### 1. Build routing

```text
Build a small settings page with a theme toggle. Inspect the repository first and tell me which DevMesh workflow you are using before editing.
```

For browser-facing implementations, Browser QA should be included when the environment can actually launch and inspect the app.

### 2. Debug routing

```text
The save button sometimes does nothing. Do not guess the fix. Find and prove the root cause, fix it, and verify the regression.
```

Expected core path:

```text
codebase-intelligence
→ systematic-debugging
→ implementation
→ qa-verification
→ code-review
```

Add `browser-qa` when the failure is browser-facing and a runnable browser surface exists.

### 3. UI/UX + Browser QA routing

```text
Redesign this page for a modern professional UI and fix mobile overflow and keyboard accessibility. Preserve existing functionality. Launch the app and verify the result in the browser before completion.
```

Expected path:

```text
codebase-intelligence
→ brainstorming-requirements
→ ui-ux-review
→ writing-plans
→ implementation
→ browser-qa
→ qa-verification
→ code-review
```

## Development validation

Run from the DevMesh repository root:

```bash
python tests/validate_devmesh.py
python tests/test_routing_contract.py
```

Expected for v0.2.0:

```text
OK: marketplace devmesh-marketplace
OK: manifest devmesh v0.2.0
OK: 11 required skills and 8 task types validated
OK: Browser QA workflow contract validated
OK: routing contract validated for 8 task types including Browser QA conditions
```

## Project helper scripts

The installed Codex plugin includes optional helpers under `plugins/devmesh/scripts/`.

The DevMesh skills do not depend on these helpers.

## Current platform support

| Platform | Status |
|---|---|
| Codex | **v0.2 supported** |
| Claude Code | Planned |
| Gemini CLI | Planned |
| Cursor | Planned |
| GitHub Copilot | Planned |

## Current scope

DevMesh intentionally has no custom LLM, backend, database, required API key, or framework dependency. The active coding agent remains the execution engine; DevMesh supplies the engineering methodology and evidence requirements.

## License

MIT
