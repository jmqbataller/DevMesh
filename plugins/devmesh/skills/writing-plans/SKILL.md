---
name: writing-plans
description: Use after the scope and codebase are understood to produce an executable implementation plan with tasks, exact files, intended changes, dependencies, and verification steps.
---

# Writing Plans

Create a plan detailed enough to execute without repeatedly rediscovering context.

## Planning principles

- plan around user-visible outcomes, not arbitrary file counts
- keep tasks small enough to verify independently
- order tasks by dependency
- avoid speculative abstractions
- identify rollback-sensitive changes such as migrations or auth changes
- include validation with each task, not only at the end

## Task format

Each task should include:

### Task N — concise outcome

**Files**
- files to create
- files to modify
- files to inspect if uncertainty remains

**Change**
- exact behavior or structure to implement
- interfaces/contracts that must remain stable

**Verification**
- test, build, lint, typecheck, manual scenario, or inspection needed
- expected result

**Risk**
- only when there is a material migration, data, auth, compatibility, or deployment risk

## Plan quality checks

Before implementation, confirm:

- every acceptance criterion maps to at least one task or verification step
- no task exists only for unrelated cleanup
- data/schema changes include migration and compatibility considerations
- UI work includes responsive and interaction-state validation
- external API work includes failure/error paths
- deployment work includes environment/config validation

## Replanning

A plan is not sacred. Replan when implementation evidence disproves an assumption. State what changed and why; do not silently drift from the plan.
