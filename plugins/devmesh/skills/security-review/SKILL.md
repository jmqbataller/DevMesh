---
name: security-review
description: Use for changes that affect authentication, authorization, user data, APIs, database access, secrets, uploads, redirects, sessions, deployment boundaries, or other security-sensitive behavior, and for explicit security reviews.
---

# Security Review

Review security based on the actual architecture and data flow. Do not produce a generic checklist and call it a review.

## Scope first

Identify the security-relevant boundaries in the requested change:

- browser/client
- server/API
- authentication provider
- session/cookie/token storage
- database and row-level authorization
- file/object storage
- third-party APIs/webhooks
- deployment/environment variables
- admin-only functionality

## Review areas

### Secrets and trust boundaries

- no server secrets in client bundles
- no credentials committed to source
- environment variables used on the correct side of the boundary
- sensitive values excluded from logs, screenshots, and QA artifacts

### Authentication and sessions

- authentication state is actually verified server-side where required
- session/cookie settings match the framework and deployment model
- logout/session invalidation behavior is sane
- password reset, OAuth callbacks, and redirect destinations are constrained appropriately

### Authorization

- authenticated does not automatically mean authorized
- object/resource ownership is enforced at the trusted layer
- admin actions have explicit authorization
- Supabase projects verify RLS/policies where data access depends on them
- client-side hiding is never treated as access control

### Input and output safety

- validate untrusted input at the correct boundary
- parameterize database queries
- avoid unsafe HTML/script injection
- encode/render user content safely
- validate URLs and redirects
- constrain file uploads by type, size, destination, and access model when applicable

### Browser and request security

Check when relevant:

- CSRF exposure
- CORS configuration
- secure transport assumptions
- content security constraints
- open redirects
- insecure mixed content
- unsafe postMessage/origin handling

### API/webhook security

- authentication/signature validation
- replay/idempotency where needed
- rate/abuse controls appropriate to risk
- least-privilege API keys/scopes
- safe error messages

### Dependencies and configuration

Use available package/audit tooling when it is already supported by the project. Distinguish exploitable application risk from noisy transitive advisories.

## Severity

Report findings as:

- **Critical** — credible path to major compromise/data loss; blocks completion/release
- **High** — exploitable security defect with meaningful impact; blocks release
- **Medium** — real weakness needing planned remediation
- **Low** — hardening or defense-in-depth improvement

Do not inflate severity without an exploitation path and affected asset.

## Fix workflow

For Critical/High findings within task scope:

`security-review → systematic-debugging when cause is unclear → implementation → targeted security verification → regression-testing when feasible`

Retest the security property, not merely the code path.

## Completion report

State:

- boundaries reviewed
- findings by severity
- fixes made
- verification evidence
- assumptions and untested areas

If no findings remain, say what was reviewed and what evidence supports that conclusion. Never say a system is "secure" in absolute terms.
