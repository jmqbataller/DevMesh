---
name: codebase-intelligence
description: Use before changing an existing repository to understand local instructions, stack, architecture, dependencies, configuration, data boundaries, tests, and Git state with read-only inspection first.
---

# Codebase Intelligence

Understand the project before modifying it.

## Read-only first pass

Start with the cheapest high-signal inspection available.

### Repository rules

Look for and read applicable instruction files such as:

- `AGENTS.md`
- `README.md`
- contributor/development docs
- framework-specific instructions
- nested instructions in the target directory

### Project identity

Inspect relevant files such as:

- `package.json`, lockfiles, workspace files
- `pyproject.toml`, `requirements*.txt`
- `composer.json`
- `go.mod`, `Cargo.toml`
- framework/config files
- deployment config

Infer the stack from evidence, not filename assumptions alone.

### Architecture

Map only what is relevant to the task:

- entry points
- routes/pages
- components/modules
- server/API layer
- database layer and migrations
- authentication/authorization
- environment variable usage
- test layout
- build/deploy pipeline

### Git state

Use read-only Git commands when available:

- current branch
- dirty/clean working tree
- recent relevant history when useful
- diff if the user already has changes

Never overwrite or stage unrelated user work during inspection.

## Environment and secret safety

It is okay to inspect **names** of environment variables and configuration wiring. Do not print or copy secret values into logs, responses, frontend code, commits, or test fixtures.

Classify variables as:

- public/client-safe
- server-only secret
- deployment-only
- unknown — treat as secret until proven otherwise

## Build a task map

Before handing off, know:

1. which files likely control the behavior
2. which dependencies or external services are involved
3. which tests/checks can validate the change
4. which files should not need modification
5. any repository state that makes editing risky

## Stop conditions

Do not begin speculative editing if:

- the relevant implementation has not been located
- the working tree contains conflicting user changes you might overwrite
- a secret would need to be exposed to achieve the proposed approach
- the requested behavior contradicts a hard repository constraint

When blocked, report the evidence and choose the safest available alternative.
