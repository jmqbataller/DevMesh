---
name: idx-provider-detector
description: Use to identify how a WordPress or other real-estate site receives and renders IDX/MLS data, including vendor plugins, embeds, RESO Web API, legacy RETS, replication, and hosted search/detail pages.
---

# IDX Provider Detector

## Core rule

**Detect from evidence; do not guess the MLS or IDX vendor from visual appearance alone.**

Inspect as available:
- WordPress plugin/theme inventory and vendor namespaces
- page source, scripts, iframes, network hosts, REST/AJAX endpoints and cookies
- server environment/config references without exposing credentials
- database tables/options/custom post types associated with listing data
- scheduled jobs/webhooks/sync logs
- DNS/subdomains and vendor-hosted result/detail URLs
- RESO/OData service documents or legacy RETS configuration

Classify the architecture:
- vendor-hosted iframe/widget
- vendor WordPress plugin rendering
- live server-side API query
- replicated/local listing database/search index
- hybrid
- unknown

Also distinguish provider/vendor from the MLS itself. A vendor may broker access to one or more MLS feeds.

Report provider confidence, evidence, IDX/VOW/use-type clues, data transport, render location, sync model, and unresolved unknowns. Never expose tokens or credential values.