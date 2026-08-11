---
name: license-subscription-tracker
description: Use to track non-secret operational licenses, subscriptions, renewal dates, ownership, business criticality, and expiry risk for client website services such as premium plugins, hosting, IDX, SMTP, backups, and SaaS tools.
---

# License Subscription Tracker

## Core rule

**Track entitlement metadata, not credentials or payment secrets. A recorded renewal date is not proof payment/auto-renew will succeed.**

Track where known: client/site, product/service, owner/account holder, plan, seats/domains, renewal/expiry date, billing cadence, auto-renew status if verified, business criticality, cancellation/transfer notes, and evidence source.

Typical services: hosting, domains, premium WordPress plugins/themes, IDX/MLS vendors, SMTP/email, backups, CDN/WAF, analytics/SEO tools, CRM/integration platforms.

Escalate upcoming renewals by configurable threshold and distinguish `active`, `expiring`, `expired`, `unknown`, and `BLOCKED`. Never store card numbers, passwords, API keys, recovery codes, or full private invoices unless explicitly required and safely handled.