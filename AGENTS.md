# Repository Instructions

This repository defines **DevMesh**, a provider-neutral development-workflow framework with Codex as the first supported adapter.

When modifying it:

1. Keep the core methodology provider-neutral; provider-specific packaging belongs under the relevant adapter/plugin path.
2. Keep each skill focused on one responsibility.
3. Do not duplicate entire workflows across multiple skills; link responsibilities through routing instead.
4. Preserve the 10 core v1 skill names unless a versioned migration is intentional.
5. Keep the Codex marketplace source at `./plugins/devmesh` and the Codex manifest at `plugins/devmesh/.codex-plugin/plugin.json`.
6. Run `python tests/validate_devmesh.py` and `python tests/test_routing_contract.py` before claiming the Codex adapter is valid.
7. Update `CHANGELOG.md` for user-visible behavior changes.
8. Never add secrets, personal tokens, or environment-specific credentials.
9. New platform support should reuse the DevMesh methodology wherever possible instead of forking behavior unnecessarily.
