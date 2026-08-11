---
name: change-impact-map
description: Use before significant edits in an existing codebase to map direct and indirect blast radius across modules, routes, APIs, schemas, UI states, tests, and deployment surfaces and derive a focused regression plan.
---

# Change Impact Map

## Core rule

**Retest what the change can actually affect, and disclose what dependency analysis cannot prove.**

## Build the map

Inspect evidence such as:
- imports/exports and call sites
- routes/server actions/controllers
- API clients and contracts
- database schema, migrations, triggers, policies
- shared domain calculations
- UI consumers and state stores
- configuration/environment boundaries
- tests/fixtures
- build/deploy entry points

Classify impact:
- `DIRECT` — explicitly depends on the changed symbol/contract/data
- `INDIRECT` — depends through a shared boundary or side effect
- `UNKNOWN` — dynamic/reflection/runtime behavior prevents confident static mapping
- `UNAFFECTED` — checked and no meaningful dependency found

## Regression plan

Map each DIRECT/INDIRECT critical surface to the smallest verification that can detect breakage. Example: changing quotation tax calculation should retest create/edit totals, API serialization, persisted totals, and any export/dashboard consumers that share the rule.

## After implementation

Compare the actual diff to the initial map. Expand tests if the change touched more surfaces than planned. Feed proven unexpected impact patterns to `failure-memory` only when persistence is opted in.

Never claim the map is exhaustive in a dynamic system when the available analysis cannot establish that.
