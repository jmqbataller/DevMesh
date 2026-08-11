---
name: database-architect
description: Use when a build/change requires durable relational or document data; design schema, migrations, constraints, indexes, ownership rules, seed strategy, and rollback/verification evidence.
---

# Database Architect

Use the repository's existing database and migration system when sound. Do not add a database when persistence is unnecessary.

Before schema changes, define:
- entities and relationships
- ownership/tenant boundaries
- required vs optional fields
- identifiers and timestamps
- uniqueness/check/foreign-key constraints
- indexes justified by access patterns
- deletion/cascade/archive behavior
- concurrency/idempotency needs

For migrations:
1. inspect current schema and migration history
2. design the smallest forward migration
3. identify compatibility/data-backfill risk
4. define rollback or forward-repair strategy
5. apply in a safe environment when authorized
6. verify schema and representative reads/writes

For Supabase/Postgres, explicitly review RLS/policies when private user data exists. Never expose service-role or database secrets to client code.

Seed/test data must be synthetic and safe. Avoid production data copying unless explicitly authorized and appropriately protected.

Report migration files, schema deltas, constraints/indexes, policy changes, apply/rollback evidence, and blockers.