---
name: mls-provider-health-monitor
description: Use to distinguish website-side IDX/MLS failures from upstream provider/feed degradation by monitoring endpoint/auth/metadata/query health, rate limits, sync checkpoints, freshness, and provider status evidence.
---

# MLS Provider Health Monitor

## Core rule

**Separate provider health from local integration health. A stale site does not prove the MLS is down, and a healthy provider endpoint does not prove the local sync/search works.**

Where authorized, check: auth/token exchange, endpoint reachability, `$metadata`, representative permitted query, response latency, 401/403/429/5xx, pagination, last provider/listing modification timestamp, local sync checkpoint, media access, and provider status notices.

Classify evidence as `UPSTREAM`, `LOCAL`, `MIXED`, `UNKNOWN`, or `HEALTHY` with confidence and timestamps.

Respect query/rate limits and MLS licensing. Never expose feed credentials. Use `listing-freshness-monitor`, `reso-schema-drift-detector`, and `reso-provider-capability-inspector` for deeper analysis.