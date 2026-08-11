# DevMesh v0.8.0

DevMesh v0.8 adds a **Real Estate IDX / MLS specialization** on top of Mission Control.

New capabilities include:
- `real-estate-idx-mls` for end-to-end IDX/MLS website and app orchestration
- `reso-web-api` for RESO Web API/OData metadata discovery, Data Dictionary mapping, authentication, queries, pagination, and provider extensions
- `listing-sync-search` for licensed listing replication, incremental synchronization, reconciliation, media, maps, local search, freshness, and sync observability
- `idx-compliance-review` for evidence-based review of public IDX display against confirmed local MLS/provider rules plus general NAR IDX safeguards

The specialization explicitly distinguishes IDX, VOW, participant feeds, syndication, and internal uses; treats RETS as legacy compatibility rather than the default for new integrations; keeps MLS credentials server-side; and refuses to claim provider compatibility or IDX compliance without the applicable MLS/provider evidence.

The release preserves Mission Control, one-prompt full-stack builds, Browser QA, security, accessibility, performance, observability, CI repair, production deployment, incident response, review, memory, reporting, and Git delivery.

The ChatGPT adapter bundles all new real-estate playbooks and adapts them to the tools and provider evidence actually available in the current chat.
