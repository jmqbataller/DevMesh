---
name: domain-ssl-expiry-monitor
description: Use to track domain-registration and TLS certificate expiry, nameserver/certificate changes, HTTPS validity, and renewal risk across client websites.
---

# Domain SSL Expiry Monitor

## Core rule

**Treat expiry and ownership evidence separately: certificate validity does not prove domain renewal, and a future expiry date does not prove auto-renew will succeed.**

Inspect where accessible: registrar/domain expiry, nameservers, DNSSEC state, certificate subject/SAN, issuer, validity window, hostname match, chain health, HTTPS redirect, and renewal mechanism.

Escalate configurable thresholds such as 30/14/7 days, but prefer client/provider policy when known. Detect unexpected nameserver or certificate changes as review events, not automatically malicious events.

Never expose registrar credentials or DNS API tokens. If registrar data is unavailable, report certificate evidence separately and domain-renewal status `BLOCKED`.