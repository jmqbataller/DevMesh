---
name: email-deliverability-doctor
description: Use for WordPress/site email delivery, SMTP, form notifications, SPF, DKIM, DMARC, From/Reply-To alignment, bounces, spam placement, CRM notifications, and downstream lead-email verification.
---

# Email Deliverability Doctor

## Core rule

**A form saying “sent” does not prove the message reached the intended mailbox or CRM. Trace the delivery chain.**

Map:
`browser submit → application/form plugin → WordPress mail/SMTP provider → provider acceptance → recipient/CRM → user-visible confirmation`

Inspect when evidence exists:
- SMTP/provider configuration and authentication boundaries
- sender domain and From/Reply-To behavior
- SPF/DKIM/DMARC records and alignment
- provider response/message IDs without exposing secrets
- bounce/rejection/rate-limit evidence
- spam/junk placement reports when accessible
- form notification routing and CRM/webhook handoff
- duplicate or missing notifications

Never expose SMTP passwords/API keys. DNS changes require `risk-engine`. Do not claim inbox delivery from application success alone.

Completion reports each boundary as `PASS`, `FAIL`, `FIXED`, `BLOCKED`, or `NOT RUN`, plus the proven failure point and retest evidence.
