---
name: real-estate-idx-mls
description: Use for real-estate website/app work involving IDX, MLS feeds, RESO Web API/OData, listing display, search, attribution, seller display restrictions, VOW distinctions, listing freshness, or MLS-provider integration.
---

# Real Estate IDX / MLS

Use this skill whenever a task involves an MLS data feed, IDX property display/search, a RESO Web API, or an existing real-estate website that consumes listing data.

## Core rule

**Treat MLS data as licensed data with provider-specific rules. Never invent credentials, access rights, fields, attribution requirements, refresh intervals, or display permissions.**

RESO defines interoperability standards; it does not provide MLS listing data. Access credentials and permitted uses come from the relevant MLS/data provider after the participant/data recipient satisfies that provider's licensing and onboarding requirements.

For new integrations, prefer the RESO Web API when available. Treat RETS as legacy compatibility only.

## 1. Classify the real-estate integration

Determine which situation applies:

- IDX public display/search
- participant/broker-owned listing feed
- VOW / registered-consumer brokerage experience
- back-office/internal MLS use
- syndication or another separately licensed channel
- migration from RETS/vendor-specific feed to RESO Web API

Do not treat these as interchangeable. Their display/access rules can differ.

## 2. Inspect the actual MLS/provider contract

Before implementation or compliance claims, identify when available:

- MLS/data-provider name
- participant/broker relationship
- approved data-use type such as IDX or VOW
- API endpoint and authentication method
- authorized resources/fields
- local display rules
- attribution/disclaimer requirements
- refresh/update obligations
- consumer-download/query limits
- rules for off-market, withdrawn, expired, delayed-marketing, address-withheld or Internet-display-withheld listings
- photo/media rules
- branding and source-identification requirements

If these are unavailable, mark local-rule compliance `BLOCKED` and build only against confirmed general requirements plus provider documentation.

## 3. RESO Web API integration

When the source is a RESO Web API:

- inspect the OData service document and `$metadata` before hard-coding resource/field assumptions
- map provider fields through the RESO Data Dictionary while preserving provider/local extensions
- support JSON payloads and provider-supported OData filtering/query options
- keep OAuth2/API credentials server-side
- validate pagination and provider result limits
- handle throttling/retries conservatively
- record source identifiers needed for attribution and reconciliation
- distinguish live-query architecture from replicated/local-search architecture

Do not expose MLS bearer tokens, client secrets, API keys, service credentials, or unrestricted feed endpoints in browser JavaScript.

## 4. Listing synchronization and freshness

For replicated/local-search architectures:

- use stable provider/listing identifiers for upsert/reconciliation
- track modification timestamps or provider-supported incremental markers
- make sync idempotent
- handle pagination/checkpointing
- process changed, removed, withheld, expired or withdrawn records according to the licensed feed/rules
- reconcile media independently when needed
- avoid duplicate records across retries
- keep a last-successful-sync signal and actionable failure logs
- test recovery after partial sync failure

Never keep a listing publicly visible merely because it remains in the local database when the authoritative source no longer permits its display.

## 5. IDX display contract

For public IDX experiences, confirm the actual local MLS rules. General safeguards include:

- display only listing content authorized for IDX
- respect seller instructions that withhold the listing or property address from Internet display
- respect delayed-marketing restrictions before public IDX display
- use objective listing-selection/filtering criteria
- provide required listing-agent/source attribution where the MLS requires it
- provide required consumer-use notices and accuracy/disclaimer text where required
- do not expose confidential broker-only/showing/security/seller-contact fields
- respect MLS-imposed reasonable retrieval/download limits
- provide the MLS access needed for compliance monitoring when the participant's local rules require it

Do not transform general NAR policy into a claim that every local MLS uses identical wording or requirements.

## 6. VOW is not IDX

If the requested product establishes a broker-consumer relationship and exposes data through a Virtual Office Website, route through the actual VOW agreement/rules. Do not assume an IDX approval automatically authorizes VOW behavior or vice versa.

## 7. Search/product architecture

When building the consumer experience, compose with `full-stack-build`, `database-architect`, `api-contract`, `security-review`, `browser-qa`, `accessibility-review`, and `performance-review` as relevant.

Typical features when requested:

- property search and objective filters
- pagination/result limits
- property detail pages
- responsive listing cards and image galleries
- map/list synchronization
- favorites/saved searches for authenticated users
- lead/contact forms
- SEO-safe public pages where permitted
- loading, empty, error and stale-data states

Do not silently invent paid lead-routing, CRM, mortgage, valuation, transaction or agent-management systems.

## 8. Security and privacy

- keep MLS credentials and privileged feed access server-side
- authorize user-specific favorites/leads/saved searches
- rate-limit expensive or abuse-prone public search endpoints where appropriate
- validate and constrain query/filter inputs
- avoid logging feed credentials or sensitive consumer data
- minimize stored consumer PII
- do not publish confidential MLS fields

## 9. QA scenarios

For a real working IDX site, test where executable:

1. listing search returns authorized records
2. objective filters combine correctly
3. pagination does not duplicate/skip records unexpectedly
4. property detail links resolve to the correct listing
5. media failures degrade safely
6. withheld/removed listing behavior follows provider rules
7. delayed-marketing/non-display records do not leak into public search
8. attribution/disclaimer appears where required
9. mobile search/cards/gallery/map remain usable
10. API timeout/429/5xx produces a controlled user state
11. credentials never appear in browser bundles/network responses
12. local cache/search catches up after a sync retry

Browser claims require actual browser evidence.

## 10. Completion evidence

Report:

- MLS/provider and authorized use type, if known
- RESO Web API vs legacy/provider-specific transport
- auth location/server boundary
- resources and field mappings
- sync/live-query strategy
- display restriction handling
- attribution/disclaimer implementation
- tests and Browser QA evidence
- local MLS rules reviewed vs `BLOCKED`
- unresolved licensing/provider questions

Do not call an IDX/MLS integration compliant solely because the code matches general NAR/RESO guidance; local MLS/provider rules and the actual license remain authoritative for that integration.
