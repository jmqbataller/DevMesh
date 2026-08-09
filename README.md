# DevMesh

**DevMesh** is a provider-ready software development agent framework that routes coding work through the right engineering workflow instead of letting an AI coding agent jump directly into edits.

**Codex is the first supported adapter.** The core methodology is intentionally provider-neutral so DevMesh can expand to Claude Code, Gemini CLI, Cursor, GitHub Copilot, and other coding-agent environments.

## What DevMesh does

DevMesh v0.1.1 contains 10 core workflows:

1. **Bootstrap / Agent Router** — classify `build`, `fix`, `debug`, `redesign`, `refactor`, `review`, `deploy`, or `research` requests and select the minimum safe workflow.
2. **Brainstorm / Requirements** — turn larger or ambiguous requests into goals, constraints, acceptance criteria, and frozen scope.
3. **Codebase Intelligence** — inspect instructions, stack, architecture, config boundaries, tests, and Git state before editing.
4. **Planning Agent** — produce `Task → Files → Changes → Verification` plans.
5. **Implementation Agent** — make intentional changes in logical, reviewable units.
6. **Debug Agent** — reproduce → trace → hypothesize → prove root cause → fix → regression verify.
7. **UI/UX Agent** — review hierarchy, responsiveness, spacing, accessibility, states, motion, overflow, and consistency.
8. **QA / Verification Agent** — run targeted tests, lint/type/build checks, runtime scenarios, UI checks, and final diff inspection.
9. **Code Review Agent** — second-pass review for correctness, security, regressions, complexity, maintainability, and test gaps.
10. **Git / Delivery Agent** — protect working-tree scope and prepare intentional branches, commits, PRs, or handoffs.

## Core philosophy

```text
Inspect before editing.
Prove root cause before fixing.
Use the minimum safe workflow.
Preserve unrelated working behavior.
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
UI/UX Review (frontend work)
    ↓
QA Verification
    ↓
Code Review
    ↓
Git Delivery (when requested/available)
```

The router deliberately does **not** run all ten workflows for every request.

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

Refresh the marketplace, then reinstall DevMesh. If your Codex version exposes marketplace upgrade, use its marketplace upgrade flow; reinstalling `devmesh@devmesh-marketplace` is safe for picking up a changed plugin package.

## Smoke tests

Use a small disposable code repository for these tests.

### 1. Build routing

Prompt:

```text
Build a small settings page with a theme toggle. Inspect the repository first and tell me which DevMesh workflow you are using before editing.
```

Expected routing:

```text
codebase-intelligence
→ brainstorming-requirements
→ writing-plans
→ implementation
→ qa-verification
→ code-review
```

### 2. Debug routing

Prompt:

```text
The save button sometimes does nothing. Do not guess the fix. Find and prove the root cause, fix it, and verify the regression.
```

Expected routing:

```text
codebase-intelligence
→ systematic-debugging
→ implementation
→ qa-verification
→ code-review
```

### 3. UI/UX routing

Prompt:

```text
Redesign this page for a modern professional UI and fix mobile overflow and keyboard accessibility. Preserve existing functionality.
```

Expected routing:

```text
codebase-intelligence
→ brainstorming-requirements
→ ui-ux-review
→ writing-plans
→ implementation
→ qa-verification
→ code-review
```

## Development validation

Run from the DevMesh repository root:

```bash
python tests/validate_devmesh.py
python tests/test_routing_contract.py
```

Expected:

```text
OK: marketplace devmesh-marketplace
OK: manifest devmesh v0.1.1
OK: 10 required skills and 8 task types validated
OK: routing contract validated for 8 task types
```

## Project helper scripts

The installed Codex plugin includes optional helpers under `plugins/devmesh/scripts/`:

Linux/macOS:

```bash
./plugins/devmesh/scripts/inspect-project.sh
./plugins/devmesh/scripts/verify-project.sh
```

PowerShell:

```powershell
./plugins/devmesh/scripts/inspect-project.ps1
./plugins/devmesh/scripts/verify-project.ps1
```

The DevMesh skills do not depend on these helpers.

## Current platform support

| Platform | Status |
|---|---|
| Codex | **v0.1 supported** |
| Claude Code | Planned |
| Gemini CLI | Planned |
| Cursor | Planned |
| GitHub Copilot | Planned |

## V1 scope

DevMesh intentionally has no custom LLM, backend, database, required API key, or framework dependency. The active coding agent remains the execution engine; DevMesh supplies the engineering methodology.

## License

MIT
