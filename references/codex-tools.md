# Codex Environment Notes

Codex execution capabilities differ across the app, CLI, workspaces, sandboxes, and connected tools.

## Principles

- Detect capabilities instead of assuming them.
- Treat sandbox restrictions as environment facts, not reasons to fake completion.
- Use read-only inspection before write operations.
- Respect approval/confirmation boundaries for external actions.
- If subagent tools exist, they may be used for independent implementation/review work; the core workflow must still work without them.

## Git environment detection

Useful read-only commands when Git is available:

```bash
git status -sb
git branch --show-current
git rev-parse --show-toplevel
git remote -v
```

Before modifying a repository with existing local work, inspect the diff and preserve unrelated changes.

## Subagents

Multi-agent execution is an optimization, not a dependency of DevMesh v1.

Good subagent boundaries:

- independent repository investigation
- implementation of non-overlapping tasks
- second-pass code review
- UI/UX review separate from implementation

Do not dispatch several agents to modify overlapping files without a merge strategy.
