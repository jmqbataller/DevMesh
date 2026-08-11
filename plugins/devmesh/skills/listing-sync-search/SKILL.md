---
name: listing-sync-search
description: Use for MLS listing replication, incremental synchronization, local search/indexing, listing/media reconciliation, freshness, pagination, maps, and consumer property-search performance.
---

# Listing Sync & Search

Use this skill when an IDX/MLS product copies authorized listing data into a local database/search index or needs a high-quality property-search experience.

## Core rule

**The authoritative MLS/provider controls what may be displayed; local cache state must never override current display authorization.**

## Architecture decision

Choose between:
- live provider queries
- replicated local database
- replicated database + search index
- hybrid strategy

Base the decision on provider license, query limits, freshness requirements, search UX, scale, and operational complexity.

## Replication workflow

1. identify stable listing/provider identifiers
2. identify provider modification/incremental markers when available
3. fetch pages deterministically
4. upsert idempotently
5. checkpoint only after durable success
6. reconcile removals/status/display eligibility
7. sync media with stable relationships
8. record last successful sync and lag
9. retry transient failures with bounded backoff
10. recover safely after partial runs

Never interpret a failed sync as permission to keep stale public inventory indefinitely.

## Data model

Keep provider truth separate from product/user state.

Typical separation:
- normalized listing source record
- display/search projection
- media records
- provider/source metadata
- sync/checkpoint state
- user favorites/saved searches/leads

Do not mix user-owned annotations into the authoritative listing payload in a way that makes resync destructive.

## Search

Support only filters/sorts actually backed by the provider/mapped data. Common examples include price, beds, baths, property type, status, geography and listing recency, but never assume exact field names.

- objective criteria only for IDX listing selection
- stable pagination/cursors
- deterministic sort tie-breakers
- bounded page sizes
- geospatial/map queries where coordinates are licensed/available
- explicit empty/error/stale-data states

## Media

- preserve provider media ordering/type where available
- lazy-load consumer images responsibly
- use placeholders/fallbacks for broken media
- do not copy/store media beyond the provider/license terms
- remove or stop serving media when listing display rights no longer allow it

## Observability

Track without leaking credentials/PII:
- last successful sync
- current sync lag
- records fetched/updated/removed
- page/checkpoint position
- provider errors/rate limits
- reconciliation anomalies
- media failures

## QA

Verify where executable:
- first sync
- no-op sync
- changed listing update
- removed/withheld listing
- retry after partial failure
- duplicate-page/retry idempotency
- pagination boundaries
- combined filters
- map/list result consistency
- stale-data banner/behavior if sync lag exceeds product threshold
- media failure fallback

Use `network-failure-qa`, `performance-review`, `browser-qa`, and `observability-review` when relevant.
