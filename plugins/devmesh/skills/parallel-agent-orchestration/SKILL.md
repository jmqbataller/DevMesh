---
name: parallel-agent-orchestration
description: Use when a runtime exposes real sub-agent or parallel execution and Mission Control has independent ready tasks that can be delegated safely with clear ownership and integration contracts.
---

# Parallel Agent Orchestration

## Core rule

**Delegate independent work; serialize shared-state work.** Never simulate agents in prose and report that as parallel execution.

## Runtime boundary

First detect whether the host exposes actual sub-agent/background/parallel-agent tools.

- If available: delegate suitable READY nodes.
- If unavailable: execute the same graph sequentially and explicitly report `parallel execution: BLOCKED / sequential fallback used`.

Do not invent agent identities or claim separate context windows existed when they did not.

## Safe delegation

Each delegated task receives:
- narrow objective
- authoritative inputs
- allowed files/surfaces when practical
- dependencies already satisfied
- acceptance criteria
- required evidence
- prohibited destructive actions
- expected handoff format

Prefer non-overlapping file or subsystem ownership. For code-writing agents, isolated branches/worktrees are useful when the runtime supports them; they are not mandatory evidence by themselves.

## Concurrency

Default to at most four concurrent workers unless the runtime/user defines a lower safe limit. Resource budget may reduce concurrency. More workers are not automatically better.

## Integration

A designated integrator must:
1. inspect every returned diff/output rather than trusting summaries
2. resolve contract/schema/API conflicts
3. rerun affected tests/integration behavior after combining work
4. reject duplicated or contradictory implementations
5. preserve unrelated repository changes

If two workers touched shared state incompatibly, stop and reconcile deliberately instead of blindly merging.

## Reviewer separation

Implementation workers should not be the only final reviewers. Route substantial integrated work to `devmesh-judge`, preferably using an independent agent/context when available.
