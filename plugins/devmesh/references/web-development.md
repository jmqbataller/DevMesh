# Web Development Reference

## Frontend

Prefer:

- semantic HTML
- progressive enhancement where practical
- explicit loading/error/empty states
- responsive layouts without fixed-height clipping
- accessible controls
- predictable state ownership
- minimal client-side exposure of sensitive configuration

## APIs

Validate all untrusted input server-side. Treat browser validation as UX, not security.

Use explicit status/error contracts and avoid leaking internal stack traces or secrets.

## Authentication

Authentication answers who the user is. Authorization answers what they may do. Verify both when protected data/actions are involved.

## Database

For schema changes, consider:

- migration ordering
- existing rows
- null/default behavior
- rollback or forward-fix strategy
- indexes/constraints
- row-level access rules where applicable

## Deployment

Check:

- environment variable names and exposure boundaries
- build command
- runtime version
- migrations
- redirects/rewrites
- API/serverless limits
- production-only differences
