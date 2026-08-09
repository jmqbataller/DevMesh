# Architecture

DevMesh is a **provider-neutral workflow layer** for AI coding agents, not a new model.

The host agent supplies reasoning and execution. DevMesh supplies reusable software-development methodology through composable skills. **Codex is the first supported adapter**, while the core skill contracts are intentionally written so future adapters can target Claude Code, Gemini CLI, Cursor, Copilot, and other coding-agent environments.

## Request lifecycle

```text
User request
   ↓
DevMesh Router / task classification
   ↓
Codebase intelligence
   ↓
Requirements (when needed)
   ↓
Plan (when needed)
   ↓
Implementation / systematic debugging
   ↓
UI/UX review (frontend work)
   ↓
QA verification
   ↓
Code review
   ↓
Git delivery (when requested/available)
```

## Core vs adapters

```text
DevMesh
├── skills/                 # provider-neutral workflow contracts
├── references/             # shared and platform-specific guidance
├── scripts/                # optional local helpers
└── .codex-plugin/          # Codex adapter / packaging metadata (v0.1)
```

The core should avoid depending on one provider's proprietary tool names. Platform-specific capabilities belong in adapter metadata or reference documents. This lets the same ten workflows evolve across multiple coding agents without duplicating the methodology.

## Why routing matters

Not every request needs every skill. A backend typo fix should not require a full redesign workflow. A repository-wide redesign should not skip requirements and responsive review.

The router selects the **minimum safe workflow**.

## Skill boundaries

| Skill | Owns |
|---|---|
| using-devmesh | classification and routing |
| brainstorming-requirements | scope and acceptance criteria |
| codebase-intelligence | repository understanding |
| writing-plans | executable task breakdown |
| implementation | intentional code changes |
| systematic-debugging | evidence-driven root-cause workflow |
| ui-ux-review | usability, responsive, accessibility, visual QA |
| qa-verification | proof before completion |
| code-review | independent correctness/security/quality pass |
| git-delivery | branch/commit/PR/handoff discipline |

## Platform roadmap

### v0.1 — Codex adapter

`.codex-plugin/plugin.json` exposes the DevMesh skills to Codex.

### Future adapters

Potential adapter targets:

- Claude Code
- Gemini CLI
- Cursor
- GitHub Copilot
- other agent environments with reusable instruction/skill systems

Adapters should map native tools and lifecycle behavior to the same DevMesh skill contracts rather than fork the core workflows.

## Multi-agent future

The architecture allows implementation and review to be split across subagents when the active coding-agent environment supports it. Multi-agent execution is deliberately not required for v0.1.0, which keeps DevMesh usable in simpler environments.
