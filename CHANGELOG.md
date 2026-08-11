# Changelog

## 0.5.0 - 2026-08-11

DevMesh v0.5 expands the framework into end-to-end engineering and production orchestration.

- Added `execution-modes` with Quick, Standard (default), and Deep verification depth while preserving safety/evidence requirements.
- Added `environment-doctor` for runtimes, package managers, dependencies, scripts, env-variable contracts, ports, database prerequisites, migrations, and browser/MCP readiness.
- Added `database-architect` for entities/relationships, constraints, indexes, migrations, rollback/repair planning, ownership, and Supabase/Postgres RLS/policies.
- Added `api-contract` for request/response/error/auth/pagination/concurrency contracts and focused contract/integration testing.
- Added `issue-to-pr` for issue context → reproduction → implementation → verification → review → commit → PR delivery when authorized.
- Added `production-deployment` for preflight, migrations, deployment, health/API smoke tests, live Browser QA, post-deploy evidence, and rollback readiness.
- Added `visual-regression` for deterministic screenshot baselines/diffs without silently overwriting failures.
- Added `network-failure-qa` for 4xx/5xx, timeout, offline/slow, malformed response, failed resource, duplicate submit, and recovery behavior.
- Added `test-data-personas` for safe deterministic synthetic users/fixtures/edge cases without production PII.
- Added `observability-review` for structured logs, error boundaries, health/readiness, correlation, and safe operational signals without secret logging.
- Added `ci-auto-heal` for actual failing workflow/job/log inspection, root-cause repair, rerun, and anti-test-bypass rules.
- Added `architecture-guard` for server/client boundaries, secret/data access, domain-rule duplication, circular dependencies, architecture drift, and unnecessary framework duplication.
- Updated `full-stack-build` to orchestrate environment, database, API, architecture, personas, resilience, visual regression, and observability when relevant.
- Updated the router so all v0.5 capabilities are selected by intent, risk, execution mode, and evidence needs rather than run blindly.
- Expanded validation contracts to all 33 skills and v0.5 orchestration rules.

## 0.4.0 - 2026-08-11

- Added `full-stack-build` for one-prompt working product requests across frontend, backend/server logic, API, persistence, validation, auth boundaries, and end-to-end verification.
- Added product-level build detection to the router.
- Added scope guardrails to avoid inventing unrelated large features.
- Added full-stack contract tests and v0.4 documentation.

## 0.3.0 - 2026-08-11

- Added bundled Playwright MCP configuration and `browser-engine`.
- Added evidence-based Browser QA fix/retest loop capped at three rounds.
- Added regression testing, security review, accessibility review, performance review, project memory, risk engine, QA reporting, and multi-agent review.
- Added GitHub Actions validation and expanded routing/feature contracts.

## 0.2.1 - 2026-08-11

- Added DevMesh plugin icon, `composerIcon`, `logo`, and brand color.

## 0.2.0 - 2026-08-11

- Added first-class `browser-qa` with rendered-page, console, responsive, interaction, overflow, screenshot, visual review, and evidence-boundary rules.

## 0.1.1 - 2026-08-09

- Converted the repository into a Codex-installable marketplace layout and added validation tests.

## 0.1.0 - 2026-08-09

- Initial DevMesh release with ten development workflow skills and Codex plugin packaging.
