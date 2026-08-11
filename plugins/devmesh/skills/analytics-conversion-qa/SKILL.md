---
name: analytics-conversion-qa
description: Use to verify analytics and conversion tracking for page views, property search/view, phone/email clicks, lead forms, schedule-showing events, saved listings, checkout-like funnels, tags, and downstream reporting.
---

# Analytics Conversion QA

## Core rule

**A successful form submission does not prove analytics attribution, and a fired browser event does not prove downstream reporting. Verify each boundary separately.**

Map the intended funnel and events, for example:
`page_view → property_search → property_view → schedule_showing/contact_agent → form_submit → lead_received`

Inspect when tools/consent allow:
- analytics/tag-manager presence and duplicate tags
- event names/parameters and trigger conditions
- consent mode/privacy boundaries
- SPA/navigation tracking if relevant
- phone/email/map/property interactions
- form success vs validation/error/cancel states
- duplicate firing
- source/medium/campaign preservation where applicable
- downstream analytics/debug/reporting evidence

Do not fabricate GA4/Search Console/CRM access or conversion counts. Never send sensitive form contents/PII as analytics parameters unless explicitly justified and permitted.

Browser QA should prove one user action produces the intended event once. Downstream dashboard/report confirmation is a separate evidence gate and may be `BLOCKED`.
