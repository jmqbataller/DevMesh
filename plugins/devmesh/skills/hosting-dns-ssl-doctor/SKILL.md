---
name: hosting-dns-ssl-doctor
description: Use for website availability, hosting, DNS, nameserver, SSL/TLS, HTTPS, redirect, CDN/cache, origin connectivity, propagation, and mixed-content diagnosis.
---

# Hosting DNS SSL Doctor

## Core rule

**Do not blame WordPress until the network/hosting path is proven healthy. Diagnose from DNS to origin to application.**

Inspect when evidence/tools allow:
- authoritative nameservers and DNS records
- A/AAAA/CNAME and mail-related records when relevant
- apex vs `www` behavior
- certificate validity, hostname coverage, chain and expiry
- HTTP→HTTPS and canonical-host redirects
- redirect loops/chains
- CDN/proxy/cache behavior
- origin reachability and HTTP status
- mixed-content requests
- propagation/stale resolver symptoms

Typical outage path:
`DNS → TLS → CDN/proxy → origin/hosting → web server/PHP → WordPress/application`

Never invent propagation status, certificate validity, hosting incidents, or origin responses. DNS or production changes require `risk-engine` and rollback-aware planning.

Completion reports observed records/status, likely fault domain, evidence, safe fix, verification, and unresolved provider access as `BLOCKED`/`NOT RUN`.
