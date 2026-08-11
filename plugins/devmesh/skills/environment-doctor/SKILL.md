---
name: environment-doctor
description: Use before builds, debugging, or deployment when runtime prerequisites may block progress; detect and repair local project setup issues without exposing secrets.
---

# Environment Doctor

Goal: make the repository runnable before blaming application code.

Inspect read-only first:
- runtime/toolchain versions (Node/npm/pnpm/yarn/Python/etc.)
- Git availability and repository state
- package manager + lockfile
- install state and missing dependencies
- required scripts (`dev`, `build`, `test`, `lint`, migrations)
- `.env.example` / documented variable names without reading or printing secret values
- database/service prerequisites
- required ports and port conflicts
- browser/MCP availability when Browser QA is expected
- migration status and generated clients when applicable

Classify findings as `READY`, `MISSING`, `MISCONFIGURED`, `BLOCKED`, or `UNKNOWN`.

Safe auto-fixes may include scoped dependency install, generated client refresh, local config scaffolding, `.env.example` maintenance, and documented setup commands when allowed by `risk-engine`.

Do not fabricate credentials or silently change production configuration. If a real external secret/service is required, report the exact missing capability and continue on independent work where possible.

Completion evidence should include commands run, detected versions, resolved blockers, remaining blockers, and the canonical run/test/build commands.