---
name: architecture-simulator
description: Use before consequential architecture decisions to stress the proposed design against realistic growth, concurrency, latency, failure, authorization, migration, rollback, and operational scenarios without confusing scenario analysis with measured benchmarks.
---

# Architecture Simulator

## Core rule

**Expose failure modes before code makes them expensive. Simulation is not a benchmark.**

## Scenario matrix

Select scenarios relevant to the product, such as:
- empty/new account
- normal expected workload
- data growth / pagination pressure
- concurrent edits / duplicate requests
- slow database or API
- downstream 4xx/5xx/timeouts
- expired/unauthorized session
- partial network failure
- background job retry/idempotency
- migration forward failure
- rollback/repair
- region/service outage
- stale cache or eventual consistency

For each scenario document:
- expected invariant
- likely failure mode
- detection signal
- mitigation/design requirement
- verification method after implementation

## Capacity claims

Do not invent statements like “supports 100k users” from design inspection. Numeric capacity/performance claims require measured load/benchmark evidence. Scenario analysis should use labels such as `DESIGN OK`, `RISK`, `UNKNOWN`, `NEEDS MEASUREMENT`.

## Output

Turn discovered risks into architecture requirements, task-graph nodes, tests, observability signals, or rollback steps. Prefer the simplest mitigation proportional to the actual risk.
