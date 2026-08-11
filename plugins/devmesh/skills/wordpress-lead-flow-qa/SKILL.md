---
name: wordpress-lead-flow-qa
description: Use to verify WordPress real-estate lead journeys such as contact, property inquiry, schedule showing, request information, home valuation, newsletter, saved-search, CRM/email/webhook delivery, and confirmation states.
---

# WordPress Lead Flow QA

## Core rule

**A form success message is not proof that a lead reached its intended destination. Verify the full business journey when access permits.**

Exercise relevant flows:
- contact agent
- request property information
- schedule/request showing
- home valuation request
- newsletter/registration
- saved search/favorite account flows
- general contact forms

Check:
- required/invalid input validation
- spam/honeypot/CAPTCHA behavior where configured
- consent/privacy text when required by the implementation
- listing/agent/source context carried through the submission
- duplicate submit/loading/retry behavior
- server/API response and controlled failure states
- email/CRM/webhook/database destination when accessible
- confirmation page/message and analytics event only when real evidence exists
- mobile/keyboard usability
- no sensitive data in URLs/client logs

Use synthetic test leads, not real consumer PII. Never send production leads to external recipients without authorization.

Report each journey as `PASS`, `FAIL`, `FIXED`, `BLOCKED`, or `NOT RUN`, including whether downstream delivery was actually observed.