---
name: wordpress-idx-bridge
description: Use to design or repair the server-side boundary between WordPress and an IDX/MLS/RESO provider, including listing search, property details, cache/sync, and secure credential handling.
---

# WordPress IDX Bridge

## Core rule

**WordPress must never turn a privileged MLS feed into an unrestricted public API. Expose only the data and operations authorized for the intended IDX/VOW use.**

Choose the simplest licensed architecture:
- vendor plugin/widget when it satisfies requirements
- server-side live RESO/provider query
- replicated/local search when the agreement permits it
- hybrid cache/search architecture

Define:
- provider authentication stored server-side
- RESO/provider resource and field mapping
- WordPress REST/server endpoints and permission boundaries
- listing IDs, canonical URLs and source attribution
- cache invalidation/freshness strategy
- media handling
- pagination/query limits
- withheld/removed/delayed-marketing behavior
- failure states and observability

Avoid duplicating provider data into WordPress posts unless that representation is useful, licensed, and maintainable. If custom post types are used, distinguish public content from authoritative feed state.

Compose with `reso-web-api`, `listing-sync-search`, `wordpress-rest-api-integrator`, `idx-compliance-review`, `security-review`, and `idx-search-qa` as relevant.

Completion requires evidence that search/detail data flows through the intended server boundary and that MLS credentials/confidential fields are absent from public responses.