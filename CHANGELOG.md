# Changelog

## 0.8.0 - 2026-08-11

DevMesh v0.8 adds a **Real Estate IDX / MLS specialization**.

- Added `real-estate-idx-mls` for IDX/MLS website and app orchestration, including IDX vs VOW classification, provider/license discovery, display restrictions, attribution/disclaimer boundaries, server-side MLS credential handling, and evidence-aware completion.
- Added `reso-web-api` for RESO Web API/OData service discovery, `$metadata`, Data Dictionary mapping, provider extensions, auth, filtering, pagination, incremental-query verification, and RETS-as-legacy guidance.
- Added `listing-sync-search` for licensed listing replication, idempotent incremental sync, reconciliation, media, local search/maps, freshness, retry/recovery, and sync observability.
- Added `idx-compliance-review` for evidence-based public IDX review against confirmed local MLS/provider rules plus current general NAR IDX safeguards, including seller Internet/address opt-outs, delayed marketing, confidential fields, retrieval limits, attribution, disclaimers, and VOW distinctions.
- Updated the DevMesh router so build/fix/debug/redesign/refactor/review/deploy/research tasks can automatically invoke the real-estate specialization when relevant.
- Updated the ChatGPT adapter to route IDX/MLS, RESO, listing-sync, and compliance tasks without assuming MLS credentials or local-rule access.
- Expanded validation to **49 composable skills** and added IDX/MLS feature contracts.
- Updated README, real-estate documentation, release notes, manifest metadata, and automated ChatGPT release packaging for v0.8.0.

## 0.7.0 - 2026-08-11

DevMesh v0.7 introduces **Mission Control** and an evidence-aware orchestration/evaluation layer.

- Added `mission-control` for dependency-aware mission planning, delegated execution, integration, judging, and bounded repair/rejudge loops.
- Added `dynamic-task-graph` with acyclic dependencies, readiness states, acceptance/evidence contracts, critical-path reporting, and selective replanning.
- Added `parallel-agent-orchestration` with real-runtime capability detection, max-four default concurrency, isolated ownership guidance, integration checks, and explicit sequential fallback when sub-agents are unavailable.
- Added `devmesh-judge` as a final evidence gate with independent-review preference, same-context fallback disclosure, relevant quality dimensions, critical-failure vetoes, and PASS/FAIL/BLOCKED decisions.
- Added `confidence-engine` with a hypothesis ledger and LOW/MEDIUM/HIGH evidence-aware routing that never treats confidence as proof.
- Added `adversarial-review` with bounded two-round option critique and evidence-based synthesis.
- Added `change-impact-map` for direct/indirect/unknown blast-radius mapping and focused regression planning.
- Added opt-in `failure-memory` for verified root-cause/fix lessons with strict secret/PII and cross-project boundaries.
- Added `eval-replay-lab` for reproducible cases, deterministic-first grading, version/config replay, and regression/improvement measurement.
- Added `architecture-simulator` for pre-implementation failure-mode scenarios while explicitly separating simulation from measured benchmarks/capacity.
- Added `resource-budget` with Eco/Balanced/Max orchestration intensity orthogonal to Quick/Standard/Deep engineering depth.
- Added `incident-commander` for production stabilization, evidence preservation, blast-radius analysis, safe mitigation, recovery verification, and incident reporting.
- Updated the router, Codex manifest, ChatGPT adapter, validation tests, README/docs, GitHub Release workflow, and Plugin Directory submission pack for v0.7.

## 0.6.0 - 2026-08-11

DevMesh v0.6 adds the first non-Codex runtime adapter.

- Added `adapters/chatgpt/devmesh-chatgpt/SKILL.md` as a portable Agent Skills adapter for normal ChatGPT.
- Added ChatGPT-specific tool adaptation and strict evidence boundaries.
- Added a self-contained ChatGPT upload bundle builder, docs, tests, GitHub Release distribution, and Plugin Directory submission materials.

## 0.5.0 - 2026-08-11

DevMesh v0.5 expands the framework into end-to-end engineering and production orchestration with execution modes, Environment Doctor, database/API architecture, Issue→PR, deployment, visual regression, network failure QA, test personas, observability, CI auto-heal, and architecture guardrails.

## 0.4.0 - 2026-08-11

- Added one-prompt `full-stack-build` with frontend/backend/API/persistence integration and scope guardrails.

## 0.3.0 - 2026-08-11

- Added Playwright MCP Browser Engine, bounded Browser QA fix/retest, regression/security/accessibility/performance review, project memory, risk engine, QA reporting, multi-agent review, and GitHub Actions validation.

## 0.2.1 - 2026-08-11

- Added DevMesh plugin icon, composer icon/logo, and brand color.

## 0.2.0 - 2026-08-11

- Added first-class Browser QA.

## 0.1.1 - 2026-08-09

- Converted the repository into a Codex-installable marketplace layout and added validation tests.

## 0.1.0 - 2026-08-09

- Initial DevMesh release with ten development workflow skills and Codex plugin packaging.
