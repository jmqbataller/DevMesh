---
name: reso-web-api
description: Use when integrating, migrating, debugging, or reviewing a RESO Web API/OData MLS feed, including metadata discovery, Data Dictionary mapping, authentication, queries, pagination, and provider extensions.
---

# RESO Web API

Use this skill for the transport/data-contract layer of MLS integrations.

## Core rule

**Discover the provider's actual metadata and licensed capabilities before generating queries or field mappings.**

RESO defines standards; the MLS/data provider supplies listing data and credentials.

## Current standard posture

Prefer RESO Web API for modern integrations. Treat RETS as deprecated legacy transport unless maintaining an existing provider integration that still requires it.

The RESO Web API is based on HTTP, JSON and OData conventions. Provider-specific capabilities and extensions still require discovery from the actual service.

## Workflow

1. identify MLS/provider and licensed use
2. obtain authorized endpoint/auth documentation without exposing secrets
3. inspect service document and `$metadata`
4. identify available resources such as Property, Member, Office, Media or provider extensions
5. map standard fields/lookups through the RESO Data Dictionary
6. preserve local/custom fields explicitly rather than pretending they are standard
7. design `$select`, `$filter`, `$orderby`, paging and incremental queries around actual provider support
8. keep auth tokens/client credentials server-side
9. validate response types, pagination and error behavior
10. add contract/integration tests around representative provider responses

## Authentication

Use only the auth method authorized by the provider. Never invent or scrape credentials.

- keep bearer tokens/client credentials out of browser code
- rotate/refresh tokens according to provider documentation
- never log token values
- separate development/test credentials from production when the provider supports it

## Metadata and mapping

Do not assume every MLS exposes identical fields.

For each consumed field record:
- provider field name
- RESO standard mapping when applicable
- data type
- lookup/enumeration meaning
- nullable/required behavior
- local extension status
- display/license sensitivity

Reject silent field coercion that can corrupt prices, dates, coordinates, statuses, identifiers, room counts or boolean/list semantics.

## Query safety

- validate/allowlist user-driven filter fields and sort options
- escape/build OData expressions correctly rather than string-concatenating untrusted input
- cap page sizes to provider and product limits
- handle next-page/continuation semantics
- handle throttling, transient failure and provider timeout without retry storms
- avoid downloading fields/media the product does not need

## Verification

When credentials and a test endpoint are available, verify:
- auth success/failure behavior
- metadata parse
- representative Property query
- filters and sort semantics
- pagination
- local field handling
- changed-data/incremental marker behavior when supported
- 401/403/429/5xx handling

If no provider credentials are available, generated queries/mappings remain `NOT RUN` and provider compatibility is `BLOCKED`.
