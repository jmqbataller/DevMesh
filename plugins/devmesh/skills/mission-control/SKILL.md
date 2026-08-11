---
name: mission-control
description: Use for large, cross-layer, high-risk, or explicitly requested DevMesh missions that benefit from dependency-aware task decomposition, delegated execution, integration, independent judging, and bounded repair loops.
---

# DevMesh Mission Control

Mission Control is the top-level orchestrator for substantial engineering missions.

## Core rule

**Decompose by dependency, delegate only when the runtime can really delegate, integrate deliberately, and release only against evidence.**

Mission Control must never pretend parallel agents, independent judges, benchmarks, or production checks ran when the host environment did not execute them.

## Trigger

Use Mission Control when one or more apply:
- explicit `DevMesh Mission Control`
- `DevMesh Deep` on a substantial cross-layer task
- whole-product work spanning frontend/backend/API/database/deployment
- architecture decisions with multiple credible approaches
- broad refactors with meaningful blast radius
- production incidents or high-risk migrations
- eval/replay work across multiple cases

Do not add Mission Control overhead to a tiny Quick task unless risk requires it.

## Mission workflow

1. Inspect the real repository/environment and user constraints.
2. Select `Quick` / `Standard` / `Deep` plus `Eco` / `Balanced` / `Max` resource budget.
3. Invoke `dynamic-task-graph` to create dependency-aware nodes with acceptance criteria and evidence requirements.
4. Invoke `change-impact-map` before significant mutations when an existing codebase is involved.
5. Use `confidence-engine` for uncertain diagnoses, assumptions, and architecture hypotheses.
6. Invoke `architecture-simulator` before expensive or hard-to-reverse architecture decisions when relevant.
7. Use `adversarial-review` for consequential choices with genuinely different viable options.
8. Invoke `parallel-agent-orchestration` only when the runtime exposes real sub-agent/parallel execution. Otherwise execute ready nodes sequentially and state that parallelism was unavailable.
9. Integrate node outputs; resolve conflicts against source, tests, contracts, and user requirements.
10. Run relevant DevMesh quality gates.
11. Invoke `devmesh-judge` after substantial missions. Prefer a separate reviewer/agent/context when the runtime supports it.
12. If the judge fails a fixable in-scope gate, route the finding to the owning node, fix, rerun the exact evidence, and re-judge. Maximum two judge repair rounds unless the user explicitly expands it.
13. Store a proven reusable lesson through `failure-memory` only when persistence is opted in and the failure/root cause/fix are verified.
14. Add or replay cases through `eval-replay-lab` when the task changes DevMesh itself or when regression benchmarking is useful.
15. Report mission state, evidence, blocked nodes, judge result, and unresolved risk.

## Mission node states

Use: `PLANNED`, `READY`, `RUNNING`, `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `SKIPPED`.

A downstream node cannot be `READY` until required dependencies satisfy their acceptance/evidence contracts.

## Release gate

A Mission Control release is not `PASS` merely because implementation completed. Critical required gates must be either verified `PASS` or explicitly accepted by the user when policy/risk allows acceptance. Missing production/browser/CI evidence remains `BLOCKED` or `NOT RUN`.

## Incident routing

If the mission is an active production outage/degradation, invoke `incident-commander` first. Stabilization and evidence preservation take priority over architecture cleanup.

## Evidence boundary

Record whether execution was:
- real parallel agents
- sequential fallback
- independent judge
- same-context fallback review
- measured benchmark
- scenario simulation only

Never collapse these into the same claim.
