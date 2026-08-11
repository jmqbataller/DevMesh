---
name: full-stack-build
description: Use for product-level build requests such as “build a working quotation website/app/system” where a complete runnable outcome requires coordinated frontend, backend/server logic, APIs, persistence, validation, security boundaries, and end-to-end verification.
---

# Full-Stack Product Build

Use this skill when the user asks for a **whole working product**, not merely a page or isolated component.

Typical triggers:

- “Build a working quotation website.”
- “Build an inventory system.”
- “Create a booking web app.”
- “Make a SaaS dashboard.”
- “Build a portal/app/system that actually works.”

## Core rule

**“Working” means integrated behavior, not a frontend mock.**

When the product requires them, deliver the frontend, backend/server logic, API contracts, database/persistence, validation, error handling, security boundaries, and end-to-end verification as one coordinated build.

Do not finish with fake APIs, placeholder persistence, buttons that do nothing, or frontend-only flows unless the user explicitly asked for a prototype.

## When not to use this skill

Do not force full-stack architecture onto:

- a static landing page with no dynamic requirements
- a single UI component
- content-only pages
- a scoped frontend-only task
- a backend-only service explicitly requested as such

Use the smallest architecture that makes the requested product genuinely work.

## Decision discipline

### Prefer existing architecture

If the repository already has a stack, database, API style, auth system, deployment target, or project conventions, preserve and extend them unless they are demonstrably unsuitable for the requested outcome.

### Greenfield defaults

If the request is greenfield and the user did not choose a stack:

1. Choose the simplest maintainable architecture supported by the environment and expected deployment.
2. Avoid introducing multiple frameworks for the same responsibility.
3. State important defaults in the plan before implementation.
4. Do not block on low-impact choices that can be made safely.

Ask a clarifying question only when the missing answer materially changes business behavior, data ownership, authentication/authorization, payment behavior, destructive migration strategy, production integration, or another difficult-to-reverse decision.

### Do not invent product scope

Infer only the minimum capabilities necessary to make the requested product work.

For example, a “working quotation website” may reasonably require creating a quotation, editing line items, calculating totals, saving/loading quotations, and seeing validation/error states. Do **not** silently invent payments, CRM, email campaigns, PDF generation, multi-company tenancy, subscriptions, or other large features unless the request or existing product requires them.

## Full-stack architecture map

Before implementation, define the required layers.

### 1. Product contract

Identify:

- primary user or user roles
- core user journeys
- main data entities
- required persistence
- success/error states
- acceptance criteria

Keep assumptions explicit and minimal.

### 2. Frontend

Define and build the actual user-facing experience:

- routes/screens/components
- forms and controls
- loading/empty/error/success states
- responsive behavior
- accessible interaction states
- client-side validation where useful for UX

The final frontend must call the real application backend/API when a backend is required.

### 3. Backend / server logic

Implement the server-side responsibilities required by the product:

- domain/business logic
- authoritative validation
- calculations that must not be trusted to the client
- authentication/session handling when required
- authorization checks when users/data have access boundaries
- secret-bearing integrations on the server side only
- safe error handling and logging boundaries

Do not duplicate critical business rules independently across frontend and backend without a reason.

### 4. API contract

For every required frontend/backend boundary, define:

- operation/route/action
- request shape
- response shape
- validation behavior
- error shape/status
- authorization requirement
- idempotency/concurrency expectations when relevant

Frontend code must integrate against these real contracts rather than mock responses in the final implementation.

### 5. Database / persistence

If the product needs durable data:

- choose the repository’s existing persistence layer when available
- define schema/entities and relationships
- add migrations when the stack uses them
- enforce server-side ownership/access rules where applicable
- include created/updated timestamps or equivalent metadata when useful
- avoid storing secrets in application records

If persistence is not actually needed, do not add a database merely because this is a full-stack workflow.

### 6. Auth and authorization — conditional

Add auth only when the product requires identity or private/multi-user data.

When auth exists:

- enforce authorization server-side
- do not rely on hidden UI controls as access control
- protect private records and privileged actions
- keep session/token secrets out of client code

### 7. Integrations — conditional

For email, payments, storage, AI APIs, webhooks, third-party services, or external APIs:

- keep credentials server-side
- validate incoming/outgoing payloads
- handle retries/idempotency where the integration requires it
- make local/development behavior explicit when real credentials are unavailable
- do not claim live external integration success without evidence

## Implementation sequence

Prefer vertical slices that become usable end-to-end rather than building all frontend first and all backend last.

Recommended sequence:

1. Freeze the minimal product contract through `brainstorming-requirements`.
2. Map frontend/backend/API/database boundaries.
3. Produce a file-level plan through `writing-plans`.
4. Implement foundational schema/config/server boundaries.
5. Implement one core journey end-to-end.
6. Verify it before expanding to the next journey.
7. Complete remaining required journeys.
8. Run relevant quality gates.

For independent cross-layer work, `multi-agent-review` or native subagents may be used when available, but avoid concurrent agents editing overlapping files without coordination.

## Mandatory integration checks

For a product-level build, verify the layers connect in reality.

Where applicable, exercise at least one representative end-to-end journey such as:

`open app → create data → server validates → persist → read it back → update it → reload page → confirm persistence`

Also test relevant negative/error behavior:

- required/invalid input
- failed request handling
- unauthorized/forbidden behavior when auth exists
- empty state
- duplicate/conflict behavior when relevant

## Quality gates

A full-stack product build should route to the relevant existing DevMesh skills:

- `browser-qa` for runnable browser UI
- `accessibility-review` for substantial/public UI
- `security-review` for APIs, auth, user data, database/storage, secrets, uploads, webhooks, or integrations
- `performance-review` for substantial/public web products when runtime/loading cost matters
- `regression-testing` for defects discovered and fixed during the build when stable tests are practical
- `qa-verification` for tests/lint/type/build/runtime evidence
- `code-review` for final correctness/maintainability review
- `multi-agent-review` for large/cross-layer/high-risk builds
- `qa-reporting` for substantial/release-ready builds

Use `risk-engine` before mutating work and before any newly discovered high-risk operation.

## Completion contract

Do not call a full-stack product “working” unless the relevant evidence exists.

Report clearly:

- architecture chosen and why
- frontend implemented
- backend/server logic implemented
- API boundaries implemented
- database/persistence implemented, or why it was unnecessary
- auth/authorization implemented, or why it was unnecessary
- environment variables/configuration required without exposing secret values
- tests/build/lint/typecheck results
- end-to-end journeys actually exercised
- Browser QA evidence when browser tooling is available
- security/accessibility/performance findings when those gates ran
- remaining blocked integrations or deployment steps

If an external service, credential, database, browser, or production environment is unavailable, mark that portion `BLOCKED`/`NOT RUN`; do not downgrade the whole product into a fake implementation just to say “done.”
