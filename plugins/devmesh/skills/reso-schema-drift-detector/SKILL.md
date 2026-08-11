---
name: reso-schema-drift-detector
description: Use to compare RESO Web API/OData metadata snapshots and detect provider schema/lookup/resource drift that can break MLS mapping, sync, filters, search, property details, or local indexes.
---

# RESO Schema Drift Detector

## Core rule

**Provider metadata is the contract. Detect drift before silently coercing or dropping changed fields.**

When authorized, capture/compare `$metadata`, service resources, field types, enum/lookups and provider/local extensions across known-good vs current snapshots.

Detect and classify:
- field added/removed/renamed
- type/nullability/collection changes
- resource/entity-set changes
- lookup/value changes
- provider extension changes
- relationship/navigation changes

Map change impact to:
`ingestion mapper → database schema → sync checkpoints → API contract → search/filter index → UI/property details → tests`

Do not assume a standard RESO field name proves the provider currently exposes it. Do not auto-migrate production data for ambiguous changes. Use `change-impact-map`, `database-architect`, `api-contract`, and `risk-engine` where relevant.

Output an evidence-based drift report with breaking/non-breaking/unknown classification, affected code/data paths, migration/retest plan, and `NOT RUN` if no comparable metadata snapshots exist.
