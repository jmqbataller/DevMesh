# Repository Instructions

This repository defines **DevMesh**, a provider-neutral software-engineering orchestration framework with Codex and ChatGPT adapters.

When modifying it:

1. Keep core methodology provider-neutral; provider-specific packaging/tool notes belong under adapter/plugin paths or references.
2. Keep each skill focused on one responsibility and route composition through `using-devmesh`; Mission Control orchestrates rather than duplicating specialist workflows.
3. Preserve existing public skill names unless a versioned migration is intentional.
4. Keep the Codex marketplace source at `./plugins/devmesh` and manifest at `plugins/devmesh/.codex-plugin/plugin.json`.
5. Run all validation tests in `.github/workflows/validate.yml` before claiming a release valid.
6. Update CHANGELOG, README/docs, version metadata, ChatGPT bundle expectations, release automation, and submission materials for user-visible releases.
7. Never add secrets, real customer data, tokens, cookies, credentials, production PII, or environment-specific private values.
8. New platform support must reuse DevMesh evidence/safety contracts rather than fork methodology.
9. Quick/Standard/Deep and Eco/Balanced/Max may reduce depth/resources but never truthfulness, safety-critical checks, or authorization boundaries.
10. Browser/CI/production/parallel-agent/independent-judge/benchmark claims require actual corresponding evidence; unavailable capabilities are `BLOCKED`/`NOT RUN` or explicitly labeled fallback.
11. Persistent project/failure memory is opt-in. Evals use sanitized fixtures and must not silently self-modify DevMesh core rules.
12. Production incidents prioritize stabilization/evidence and keep destructive mitigation risk-gated.
