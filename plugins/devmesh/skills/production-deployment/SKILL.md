---
name: production-deployment
description: Use for production release requests; validate environment, migrations, build, deployment, health, live browser/API smoke tests, rollback readiness, and post-deploy evidence.
---

# Production Deployment

Production deployment is a high-impact workflow. Use `risk-engine`; require authorization for destructive migrations, data changes, domain/DNS changes, irreversible release actions, or other high-risk operations not already authorized.

Preflight:
- clean/understood Git diff
- required CI/tests/build pass
- production env variable names/config present without printing secrets
- migrations reviewed and ordered
- security review for exposed surfaces
- rollback/forward-repair plan

Deploy using the repository's existing platform and workflow when possible.

After deploy, verify the actual production target:
- health/readiness endpoint when present
- critical API smoke checks
- open the live URL in `browser-qa`
- console/runtime/network errors
- representative desktop/mobile journeys
- auth/data boundaries when safely testable
- migration-backed create/read/update behavior when appropriate and using safe test records

Do not declare production success from a build log alone. If live environment access is unavailable, mark production verification `BLOCKED`.

Report deployment target/version, migration result, health/smoke evidence, live URL checks, remaining risks, and rollback path. Never expose production secrets in reports.