---
name: consent-privacy-cookie-auditor
description: Use to audit website cookies, consent flows, analytics/marketing tags, embedded third parties, forms collecting personal data, and privacy disclosures without pretending to provide jurisdiction-specific legal certification.
---

# Consent Privacy Cookie Auditor

## Core rule

**Technical privacy review is not legal compliance certification. Identify observable data flows and consent behavior, then mark legal interpretation `BLOCKED` when applicable rules/counsel are unavailable.**

Inspect where evidence allows: cookies/storage before and after consent, analytics/tag managers, advertising pixels, embedded maps/video/chat, forms and PII fields, privacy/cookie links, consent categories, reject/withdraw behavior, script blocking, retention/configuration evidence, and third-party destinations.

Use browser/network evidence for runtime claims. Do not submit real sensitive personal data for routine QA. Do not claim GDPR/CCPA/other legal compliance solely from technical checks.

Report `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN` per technical control and identify the policy/legal source required for final compliance review.