---
name: api-contract
description: Use when frontend/backend/services communicate through APIs or server actions; define and verify request, response, error, auth, pagination, concurrency, and compatibility contracts before integration.
---

# API Contract

Treat the API boundary as an explicit product contract, not an implementation accident.

For each operation define:
- method/action and route/name
- request parameters/body schema
- response schema
- validation and normalization
- error/status shape
- authentication and authorization
- pagination/filter/sort when relevant
- idempotency/concurrency semantics when relevant
- rate/size limits when relevant

Prefer existing repository conventions. Keep business-critical validation authoritative on the server.

Generate or update contract/schema types from one source of truth when the stack supports it. Add focused contract/integration tests so frontend and backend cannot silently drift.

Do not expose internal stack traces, secret-bearing errors, or privileged fields. Do not return a successful response for failed persistence merely to keep the UI moving.

Verification should exercise at least one valid request and relevant invalid/unauthorized/conflict paths against the real server boundary when available.

Report the operations changed, compatibility impact, tests/evidence, and remaining external blockers.