---
name: full-stack-build
description: Use for product-level requests such as “build a working quotation website/app/system” where a complete runnable outcome requires coordinated frontend, backend/server logic, APIs, persistence, validation, security boundaries, and end-to-end verification.
---

# Full-Stack Product Build

Use this skill when the user asks for a whole working product, not merely a page/component.

**Working means integrated behavior, not a frontend mock.**

When the product requires them, deliver frontend, backend/server logic, API contracts, database/persistence, validation, error handling, auth/authorization, integrations, and end-to-end verification as one coordinated build.

Do not finish with fake APIs, placeholder persistence, buttons that do nothing, or frontend-only flows unless the user explicitly asked for a prototype.

## Scope discipline

Infer only the minimum capabilities needed for the requested product.

A “working quotation website” may require create/edit/delete quotations, line items, totals, validation, save/load, and persistence. Do not silently invent payments, subscriptions, CRM, mass email, PDF generation, multi-company tenancy, or other large features unless requested or required by the existing product.

## Architecture sequence

1. `environment-doctor` when the runtime/setup is unknown or required to execute.
2. Freeze the minimal product contract with `brainstorming-requirements`.
3. Map frontend, backend/server, API, database, auth, and external integration boundaries.
4. Invoke `database-architect` when durable data/schema/migrations are required.
5. Invoke `api-contract` for every real frontend/backend/service boundary.
6. Use `architecture-guard` for substantial/cross-layer work.
7. Produce a file-level plan with `writing-plans`.
8. Implement vertical slices that work end-to-end.
9. Use `test-data-personas` when representative roles/edge cases improve QA.
10. Run relevant browser, failure, security, accessibility, performance, observability, review, and QA gates.

## Greenfield defaults

If no stack is chosen:
- choose the simplest maintainable architecture supported by the environment/deployment target
- avoid multiple frameworks for the same responsibility
- state important defaults in the plan
- do not block on reversible low-impact choices
- ask only when a missing answer materially changes business behavior, data ownership/security, payments, destructive migrations, production integrations, or another difficult-to-reverse decision

## Layer contracts

### Frontend
Build real routes/screens/forms/states and connect them to real server/API boundaries when required. Include loading, empty, error, success, responsive, and accessible states.

### Backend/server
Keep authoritative business validation, protected calculations, authorization, secret-bearing integrations, and safe error handling server-side.

### API
Define request/response/error/auth contracts through `api-contract`; final frontend must not depend on fake responses.

### Database/persistence
Use the repository's existing persistence layer when sound. Add schema/migrations/constraints/access policies through `database-architect`. Do not add a DB if durable data is unnecessary.

### Auth/authorization
Add identity only when required. Enforce authorization server-side; hidden buttons are not access control.

### Integrations
Keep credentials server-side. Validate payloads, handle retries/idempotency when required, and never claim live integration success without evidence.

## Mandatory integration checks

Where applicable, exercise a representative journey:
`open app → create data → server validates → persist → read it back → update it → reload → confirm persistence`

Also test relevant negative states: invalid input, failed request, unauthorized/forbidden, empty state, duplicate/conflict behavior.

For important networked flows, use `network-failure-qa` to test failure/recovery. For stable UI baselines, use `visual-regression`. For production-capable systems, use `observability-review` where operational diagnosis matters.

## Completion contract

Do not call the product working unless relevant evidence exists for:
- frontend
- backend/server logic
- API boundaries
- persistence (or why unnecessary)
- auth/authorization (or why unnecessary)
- required environment/config names without exposing secrets
- tests/build/lint/type checks
- representative end-to-end journeys
- Browser QA when available
- relevant security/accessibility/performance/resilience findings

If an external credential/service/browser/database/production environment is unavailable, mark the affected gate `BLOCKED` or `NOT RUN`; do not replace it with a fake implementation just to say done.
