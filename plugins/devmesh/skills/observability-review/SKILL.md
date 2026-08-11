---
name: observability-review
description: Use for production-capable services/apps where failures must be diagnosable; review and add proportionate logs, health signals, error boundaries, request correlation, and safe operational visibility.
---

# Observability Review

Observability should make failures diagnosable without leaking sensitive data.

Review/add only what the product needs:
- structured server logs
- consistent error boundaries/handlers
- health/readiness endpoints
- request/job correlation IDs when useful
- API failure context without secret payloads
- background job status/failure visibility
- performance timing/slow-operation signals when justified

Prefer the repository's existing logging/monitoring stack. Do not add a heavyweight vendor solely to satisfy this skill.

Never log passwords, tokens, cookies, authorization headers, secret env values, private keys, full payment data, or unnecessarily sensitive user content. Redact identifiers where appropriate.

Verification should deliberately trigger a safe failure in development/test when practical and confirm that operators receive actionable context while the user receives a safe error.

Report signals added/reviewed, sensitive-data protections, test evidence, and production integrations that remain `BLOCKED` without credentials.