# Repository Instructions

This repository defines **DevMesh**, a provider-neutral software-engineering workflow framework with Codex as the first supported adapter.

When modifying it:

1. Keep core methodology provider-neutral; provider-specific packaging/tool notes belong under adapter/plugin paths or references.
2. Keep each skill focused on one responsibility and route composition through `using-devmesh`.
3. Do not duplicate whole workflows across skills; orchestrators delegate to specialized skills.
4. Preserve existing public skill names unless a versioned migration is intentional.
5. Keep the Codex marketplace source at `./plugins/devmesh` and manifest at `plugins/devmesh/.codex-plugin/plugin.json`.
6. Run `python tests/validate_devmesh.py`, `python tests/test_routing_contract.py`, and `python tests/test_feature_contracts.py` before claiming the adapter valid.
7. Update `CHANGELOG.md`, README, version metadata, and tests for user-visible behavior changes.
8. Never add secrets, real customer data, tokens, cookies, credentials, or environment-specific private values.
9. New platform support should reuse DevMesh evidence/safety contracts rather than fork the methodology.
10. Execution modes may reduce depth but must never reduce truthfulness, required safety checks, or high-risk authorization boundaries.
11. Browser/CI/production/visual-regression passes require actual corresponding evidence; unavailable capabilities must be `BLOCKED`/`NOT RUN`.
