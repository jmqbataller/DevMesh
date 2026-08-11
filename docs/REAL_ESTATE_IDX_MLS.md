# DevMesh Real Estate IDX / MLS Specialization

DevMesh v0.8 adds a real-estate website specialization for IDX and MLS work.

## What it covers

- IDX website/display planning and implementation
- MLS data-access discovery and provider onboarding boundaries
- RESO Web API / OData integration
- RESO Data Dictionary field/resource mapping
- listing replication/sync and live-query strategies
- property search, filters, pagination, maps, listing detail pages, media, favorites and lead capture when requested
- attribution, disclaimer and data-source display requirements
- seller Internet-display opt-outs and delayed-marketing restrictions
- VOW vs IDX distinction
- server-side credential handling and cache/index architecture
- listing freshness, deletion/withdrawal handling and sync observability
- accessibility, performance, security and Browser QA for real-estate search experiences

## Important boundaries

DevMesh does not invent MLS credentials or imply that RESO itself provides listing data. MLS data access must come from an authorized MLS/data provider under the applicable participant/license agreement.

RETS is treated as legacy compatibility only. New integrations should prefer the RESO Web API when the MLS/provider offers it.

Local MLS rules can be stricter or more specific than general NAR IDX policy, so an implementation must inspect the actual MLS/provider agreement and rules before claiming compliance.

## Example prompts

```text
Use DevMesh.
Build a working real-estate website with IDX property search using my MLS provider.
```

```text
DevMesh Deep:
Audit this IDX website for MLS/IDX compliance, RESO mapping, listing freshness, search UX, security, accessibility and performance.
```

```text
Use DevMesh.
Integrate this RESO Web API feed and build property search, property details and saved listings without exposing MLS credentials to the browser.
```
