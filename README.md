# DevMesh

**DevMesh** is a provider-ready software development agent framework that routes coding work through the right engineering workflow instead of letting an AI agent jump directly into edits.

**Codex is the first supported adapter**, but the core methodology is intentionally provider-neutral so DevMesh can expand to Claude Code, Gemini CLI, Cursor, GitHub Copilot, and other coding-agent environments.

## What it does

DevMesh v0.1.0 contains 10 core workflows:

1. **Bootstrap / Agent Router** — classify `build`, `fix`, `debug`, `redesign`, `refactor`, `review`, `deploy`, or `research` requests and choose the minimum safe workflow.
2. **Brainstorm / Requirements** — turn larger or ambiguous requests into goals, constraints, acceptance criteria, and a frozen scope.
3. **Codebase Intelligence** — inspect local instructions, stack, architecture, configuration boundaries, tests, and Git state before editing.
4. **Planning Agent** — produce `Task → Files → Changes → Verification` execution plans.
5. **Implementation Agent** — make intentional changes in logical, reviewable units.
6. **Debug Agent** — reproduce → trace → hypothesize → prove root cause → fix → regression verify.
7. **UI/UX Agent** — review hierarchy, responsive behavior, spacing, accessibility, states, motion, overflow, and consistency.
8. **QA / Verification Agent** — run targeted tests, lint/type/build checks, runtime scenarios, responsive checks, and final diff inspection.
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

The router deliberately does **not** run all ten skills for every request.

### Example: backend bug

```text
"Fix why quotations are not saving"

Router
→ Codebase Intelligence
→ Systematic Debugging
→ Implementation
→ QA Verification
→ Code Review
→ Git Delivery
```

### Example: portfolio redesign

```text
"Redesign my portfolio and fix the responsive issues"

Router
→ Codebase Intelligence
→ Brainstorm / Requirements
→ UI/UX Review
→ Writing Plans
→ Implementation
→ QA Verification
→ Code Review
→ Git Delivery
```

## Repository structure

```text
DevMesh/
├── .codex-plugin/              # first platform adapter
│   └── plugin.json
├── skills/                     # provider-neutral core workflows
│   ├── using-devmesh/
│   ├── brainstorming-requirements/
│   ├── codebase-intelligence/
│   ├── writing-plans/
│   ├── implementation/
│   ├── systematic-debugging/
│   ├── ui-ux-review/
│   ├── qa-verification/
│   ├── code-review/
│   └── git-delivery/
├── references/
├── scripts/
├── docs/
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Current platform support

| Platform | Status | Notes |
|---|---|---|
| Codex | **Supported first** | `.codex-plugin/plugin.json` exposes the shared skills |
| Claude Code | Planned | Future adapter should reuse the same core skills |
| Gemini CLI | Planned | Future adapter should reuse the same core skills |
| Cursor | Planned | Adapter design TBD |
| GitHub Copilot | Planned | Adapter design TBD |

## Validate the Codex adapter

Python 3:

```bash
python scripts/validate_plugin.py
```

Expected output:

```text
OK: manifest 'devmesh' v0.1.0
OK: 10 required skills validated
OK: skill names, directories, descriptions, and manifest path are consistent
```

## Optional project helpers

Linux/macOS:

```bash
./scripts/inspect-project.sh
./scripts/verify-project.sh
```

PowerShell:

```powershell
./scripts/inspect-project.ps1
./scripts/verify-project.ps1
```

These helpers are convenience tools only; the skills do not depend on them.

## Codex installation / use

The first adapter is structured as a Codex plugin with `.codex-plugin/plugin.json` pointing to the shared `./skills/` directory.

Install/add the repository through the plugin workflow available in your Codex environment, then start a software-development request normally. The `using-devmesh` router skill is designed to select the relevant specialized workflows automatically.

## V1 scope

V1 intentionally has:

- no custom LLM
- no external backend
- no database
- no required API key
- no required multi-agent runtime
- no dependency on a specific web framework
- one initial platform adapter: Codex

The active coding agent remains the execution engine; DevMesh supplies the development methodology.

## Planned follow-ups

Platform expansion:

- Claude Code adapter
- Gemini CLI adapter
- Cursor adapter
- GitHub Copilot adapter

Specialized capabilities:

- security specialist
- database/Supabase specialist
- Vercel deployment specialist
- WordPress/PHP specialist
- performance specialist
- browser QA
- dependency upgrades
- documentation generation
- optional multi-agent implementer/reviewer orchestration

## License

MIT
