---
name: idx-compliance-review
description: Use to review an IDX real-estate website/app against confirmed MLS/provider display rules plus general NAR IDX safeguards, including attribution, disclaimers, seller display restrictions, confidential fields, retrieval limits, and VOW distinctions.
---

# IDX Compliance Review

Use this skill for compliance-focused review of public MLS listing display.

## Core rule

**Local MLS/provider rules and the participant's data license are authoritative for the implementation. General NAR IDX policy is a baseline, not a substitute for the actual local agreement.**

Do not provide a legal-compliance guarantee. Report what was checked, the rule source, evidence, and unresolved local requirements.

## Review inputs

Collect when available:
- MLS/provider name and current rules/agreement
- authorized use type (IDX, VOW, participant feed, etc.)
- website/app URLs or source code
- fields/resources displayed
- source/agent/broker attribution requirements
- required disclaimer text/placement
- update/freshness rules
- query/download limits
- Internet-display and address-display flags
- delayed-marketing handling
- status/off-market display rules
- media restrictions

If the actual local rules are missing, mark local compliance `BLOCKED`.

## General IDX safeguards to inspect

Based on current NAR IDX policy, verify where applicable:

- participant's IDX use is within authorized display purposes
- seller-withheld Internet listings are excluded from public IDX display
- seller-withheld property addresses are not exposed
- delayed-marketing records are not publicly displayed before permitted
- listing selection uses objective criteria
- confidential broker/showing/security/seller-contact information is not exposed
- listing agent/source identity is displayed when required by the MLS
- consumer personal/non-commercial-use notice is present when required
- data reliability/disclaimer language is present when required
- result/download limits comply with the MLS rules
- the MLS can monitor the participant's IDX site where local rules require access

Do not assume every MLS adopts every optional NAR guideline identically.

## VOW distinction

If the product establishes a broker-consumer relationship and provides registered-user brokerage access, inspect the actual VOW rules separately. Do not label a VOW feature compliant solely because public IDX pages pass this review.

## Technical leak review

Inspect:
- API responses for hidden/confidential fields
- server/client boundaries for MLS credentials
- page source/JSON hydration for fields hidden only visually
- search indexes/caches that may contain non-displayable records
- sitemap/SEO pages for listings that should no longer be public
- image/CDN caches after display withdrawal

A field hidden with CSS still counts as exposed if it is delivered to the browser.

## Review output

For each finding record:
- requirement/source
- evidence
- status: `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, or `N/A`
- severity
- remediation

Never state "IDX compliant" without having the current applicable MLS/provider rules and direct evidence for the reviewed surfaces.
