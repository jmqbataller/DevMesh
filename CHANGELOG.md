# Changelog

## 0.2.1 - 2026-08-11

- Added the new DevMesh neon technology logo as the Codex plugin icon and logo asset.
- Added `brandColor`, `composerIcon`, and `logo` interface metadata.
- Reduced default prompts to the Codex-supported maximum of three.

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
- Updated validation and routing contract tests for Browser QA.

## 0.1.1 - 2026-08-09

- Converted the repository into a Codex-installable marketplace layout.
- Added `.agents/plugins/marketplace.json` with `devmesh@devmesh-marketplace`.
- Moved the Codex adapter package to `plugins/devmesh/`.
- Removed the obsolete `hooks` field from the Codex plugin manifest to match the current manifest contract.
- Added marketplace/manifest/skill validation tests.
- Added routing contract tests for all eight DevMesh task types.
- Added concrete Codex CLI installation and smoke-test instructions.

## 0.1.0 - 2026-08-09

- Initial DevMesh release.
- Added ten development workflow skills.
- Added first Codex plugin manifest.
- Added project inspection and verification helpers.
