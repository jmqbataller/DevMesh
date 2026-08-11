---
name: dynamic-task-graph
description: Use to convert a substantial engineering request into an acyclic dependency graph with explicit owners, acceptance criteria, evidence requirements, risk, and readiness states.
---

# Dynamic Task Graph

## Core rule

**Parallelize dependencies, not guesses.** A task graph exists to make ordering and evidence explicit, not to create unnecessary micro-tasks.

## Node contract

Each meaningful node should have:
- `id`
- objective
- dependencies
- inputs/source of truth
- expected outputs
- acceptance criteria
- evidence required
- risk level
- suggested owner role/skill
- affected surfaces when known
- status

Example:

```text
DB-SCHEMA
objective: persist quotations and line items
requires: REQUIREMENTS
produces: migration + constraints + ownership rules
acceptance: schema supports create/read/update/delete invariants
evidence: migration review + executable migration/test when available
```

## Graph rules

1. The graph must be acyclic. Detect and resolve circular dependencies before execution.
2. Nodes are `READY` only when all required dependencies have satisfied their contracts.
3. Keep independently executable nodes separate enough to run concurrently, but do not split cohesive edits solely to manufacture parallelism.
4. Put integration nodes after producers whose outputs must connect.
5. Put verification nodes after the behavior they verify.
6. High-risk nodes include their authorization boundary.
7. Unknown dependencies are explicit; they are not silently assumed away.

## Replanning

New evidence may change the graph. Replan when:
- a dependency assumption is disproven
- a root cause changes
- an API/schema contract changes materially
- an unexpected blast radius appears
- a required capability is blocked

Preserve completed evidence and invalidate only nodes actually affected by the replan.

## Output

Report the critical path, ready parallel groups, blocked nodes, and required integration points. Do not claim a ready parallel group ran in parallel unless `parallel-agent-orchestration` had actual runtime support.
