# Changelog

## 0.4.0 - 2026-08-11

DevMesh v0.4 adds one-prompt full-stack product building for concise requests such as `Build a working quotation website.`

- Added `full-stack-build` as a 21st DevMesh skill.
- Added automatic product-level build detection for whole working websites, apps, SaaS products, dashboards, portals, systems, platforms, and tools.
- Defined `working` as an integrated product rather than a frontend mock when requested behavior requires backend/server logic, APIs, persistence, auth, or integrations.
- Added cross-layer architecture mapping for frontend, backend/server logic, API contracts, database/persistence, auth/authorization, and external integrations when relevant.
- Added greenfield decision rules that prefer simple maintainable defaults and avoid unnecessary clarification for low-impact choices.
- Added scope guardrails so DevMesh infers only the minimum functionality necessary for the requested product and does not silently invent unrelated features.
- Added vertical-slice implementation guidance so core user journeys become usable end-to-end early rather than building disconnected frontend/backend halves.
- Added mandatory representative integration checks such as create → server validate → persist → read → update → reload → confirm persistence when applicable.
- Added explicit completion requirements covering frontend/backend/API/database/auth/configuration, end-to-end evidence, and blocked external services.
- Updated the router so a request like `Build a working quotation website` automatically invokes the full-stack build workflow without requiring separate frontend/backend/API/database instructions.
- Updated manifest branding/copy and default build prompt for full-stack product creation.
- Updated validators, routing tests, feature-contract tests, and README for v0.4.

## 0.3.0 - 2026-08-11

DevMesh v0.3 turns the framework from a workflow-only plugin into a deeper evidence-driven engineering system.

- Added bundled Playwright MCP configuration through `plugins/devmesh/.mcp.json`.
- Added `browser-engine` for real browser launch, navigation, interaction, viewport, console/network, screenshot, and artifact control.
- Enhanced `browser-qa` with an automatic evidence-based fix → retest loop capped at three rounds.
- Added `regression-testing` for preserving confirmed bug fixes with focused automated coverage.
- Added `security-review` for auth, authorization, sessions, secrets, data/API/database/storage, uploads, redirects, webhooks, CORS/CSRF, and security boundaries.
- Added `accessibility-review` for keyboard/focus, semantics, labels, forms, contrast, motion, responsive usability, and optional automated scanning.
- Added `performance-review` for bundles, images, fonts, network/runtime evidence, rendering cost, and measured before/after optimization.
- Added opt-in `project-memory` using `.devmesh/` for stable commands, decisions, QA baselines, and reports without secrets.
- Added `risk-engine` with read-only, low, medium, and high-risk action classification and explicit authorization requirements for destructive/high-risk operations.
- Added `qa-reporting` with PASS/FAIL/FIXED/BLOCKED/NOT RUN evidence states and optional persistent `.devmesh/reports/` artifacts.
- Added `multi-agent-review` with read-only independent reviewer roles, maximum four concurrent reviewers by default, fix/re-review limits, and sequential fallback when subagents are unavailable.
- Updated routing so features are selected by task/risk rather than forcing every quality gate onto every small change.
- Added v0.3 validator coverage for Playwright MCP, all 20 skills, quality-gate contracts, routing, and feature behavior.
- Updated architecture and documentation for the v0.3 execution model.

## 0.2.1 - 2026-08-11

- Added the DevMesh plugin icon and brand color to Codex plugin metadata.
- Added `composerIcon` and `logo` assets.
- Reduced default prompts to the supported maximum of three.

## 0.2.0 - 2026-08-11

- Added `browser-qa` as an eleventh first-class DevMesh skill.
- Added browser launch and rendered-page inspection workflow.
- Added browser console/runtime error inspection.
- Added desktop, phone, and conditional tablet responsive QA.
- Added interaction and form journey testing.
- Added overflow, clipping, z-index, spacing, focus, and responsive visual defect checks.
- Added screenshot-based QA evidence and visual review guidance.
- Added evidence-based report/fix/retest loops for browser defects.
- Added a strict evidence boundary: DevMesh must not claim browser, visual, responsive, interaction, console, or screenshot QA when browser capabilities are unavailable.
- Updated routing so redesigns require Browser QA and other browser-facing build/fix/debug/review/deploy work invokes it when relevant.

## 0.1.1 - 2026-08-09

- Converted the repository into a Codex-installable marketplace layout.
- Added `.agents/plugins/marketplace.json` with `devmesh@devmesh-marketplace`.
- Moved the Codex adapter package to `plugins/devmesh/`.
- Added marketplace/manifest/skill validation tests and routing contract tests.

## 0.1.0 - 2026-08-09

- Initial DevMesh release with ten development workflow skills and Codex plugin packaging.
