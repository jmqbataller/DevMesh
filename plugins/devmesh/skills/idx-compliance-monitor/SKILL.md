---
name: idx-compliance-monitor
description: Use for ongoing checks that public IDX display continues to honor MLS/provider listing restrictions, seller opt-outs, delayed marketing, removals, attribution, disclaimers, and confidential-field boundaries.
---

# IDX Compliance Monitor

## Core rule

**Monitor against the current local MLS/provider rules and licensed data use. General NAR/RESO guidance is not a substitute for the actual agreement.**

Continuously or periodically compare public display behavior with provider state/rules when tools/data are available:
- Internet-display-withheld listings
- property-address-withheld instructions
- delayed-marketing/non-public states
- withdrawn/expired/removed/non-displayable records
- confidential remarks, showing/security instructions and seller contact fields
- required source/listing-agent attribution
- required consumer-use notices/disclaimers
- authorized statuses/property classes/fields
- reasonable retrieval/download limits where applicable

When a record changes from displayable to non-displayable, ensure public search/detail/cache/index paths stop exposing it according to the applicable rule. Hiding with CSS is not removal.

Record the rule source/version used for each compliance assertion. If local rules/provider evidence are missing, mark the relevant check `BLOCKED`.

Do not automatically delete authoritative history or operational audit data merely to remove a public display. Separate public visibility from internal retention rights.