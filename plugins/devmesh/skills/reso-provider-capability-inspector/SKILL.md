---
name: reso-provider-capability-inspector
description: Use to inspect an MLS/data provider’s documented RESO/transport capabilities, metadata, resources, query support, provider extensions, legacy RETS exposure, and evidence needed for integration planning.
---

# RESO Provider Capability Inspector

## Core rule

**Describe only capabilities proven by the provider endpoint, metadata, documentation, certification evidence, or license. Never infer access rights from RESO terminology alone.**

Inspect when available:
- RESO Web API/OData endpoint and version evidence
- service document and `$metadata`
- resources/entity sets exposed
- standard vs local/provider extensions
- authentication method
- supported query/filter/pagination behavior
- media/resource strategy
- replication/incremental sync affordances
- rate/result limits when documented
- legacy RETS compatibility if still used
- IDX/VOW/participant-feed authorization from the actual agreement

Distinguish:
`technical capability` from `licensed permission` from `local display rule`.

Do not call a provider “RESO certified,” “IDX enabled,” or compatible with a specific implementation unless current evidence supports that claim.

Output a capability matrix, unknowns, required credentials/docs, integration risks, and next verification steps. Use `reso-web-api`, `idx-provider-detector`, and `reso-schema-drift-detector` as needed.
