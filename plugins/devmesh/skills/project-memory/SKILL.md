---
name: project-memory
description: Use when a repository has opted into DevMesh memory or the user asks DevMesh to remember project commands, architecture decisions, QA baselines, or stable project facts across sessions without storing secrets.
---

# Project Memory

DevMesh project memory is repository-local, human-readable, and non-secret. It reduces repeated rediscovery while keeping the source of truth visible to developers.

## Opt-in rule

Do not silently add `.devmesh/` files to an unrelated repository merely because DevMesh is installed.

Use persistent project memory when any of these are true:

- `.devmesh/` already exists
- the user asks to initialize/enable DevMesh memory
- repository instructions explicitly opt into it

Otherwise keep discovered context in the current session only.

## Recommended structure

```text
.devmesh/
├── project.json
├── decisions.md
├── qa-baseline.json
└── reports/
```

### `project.json`

Store stable operational facts such as:

- project/framework type
- package manager
- install/dev/build/test/lint/typecheck commands
- key source/test directories
- browser-facing flag
- database/provider names
- deployment provider
- public/local preview conventions

Never store secret values, access tokens, passwords, private keys, cookies, or full `.env` contents.

### `decisions.md`

Record concise decisions that materially affect future work:

- architecture conventions
- intentionally chosen tradeoffs
- compatibility constraints
- design-system conventions
- known non-obvious boundaries

Do not turn this into a transcript or duplicate the README.

### `qa-baseline.json`

Store stable QA expectations, not fabricated measurements. Examples:

- key routes/journeys
- representative viewports
- required test commands
- known accepted warnings with rationale
- last verified baseline artifact references

Numeric performance baselines belong here only when they were actually measured and the context is recorded.

## Read workflow

After `codebase-intelligence`, read existing `.devmesh` memory and validate it against the repository. Treat stale memory as a hint, never as higher authority than current source/config.

If a stored command no longer exists, update memory only when persistent memory is enabled and the correct command is proven.

## Write workflow

When updating memory:

1. change only facts learned or decisions made in the current task
2. keep diffs small
3. avoid volatile details
4. do not store secrets
5. mention memory-file changes in the final task summary

## Security boundary

Before writing memory, scan candidate content for credentials or sensitive personal data. If uncertain, omit the value and record only the non-secret structural fact.

## Portability

Keep core memory provider-neutral. Platform-specific details may be named as values (for example `deployment: vercel`) but the schema must not require one coding-agent vendor.
