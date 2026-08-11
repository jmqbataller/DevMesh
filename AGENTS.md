# Repository Instructions

This repository defines **DevMesh**, a provider-neutral software-development agent framework with Codex as the first supported adapter.

When modifying it:

1. Keep the core methodology provider-neutral; provider-specific packaging belongs under the relevant adapter/plugin path.
2. Keep each skill focused on one responsibility and route between skills instead of duplicating full workflows.
3. Preserve established skill names unless a versioned migration is intentional.
4. Keep the Codex marketplace source at `./plugins/devmesh` and the manifest at `plugins/devmesh/.codex-plugin/plugin.json`.
5. Keep browser methodology provider-neutral; Codex-specific Playwright MCP packaging belongs in `plugins/devmesh/.mcp.json`.
6. Persistent project memory must remain opt-in and must never store tokens, passwords, cookies, private keys, `.env` contents, or sensitive personal data.
7. High-risk/destructive behavior must preserve explicit authorization boundaries.
8. Review subagents should be read-only by default; one lead/implementer owns fixes unless isolated worktrees are intentionally used.
9. Never report browser, accessibility, security, performance, or QA evidence that was not actually collected.
10. Run all validation tests before claiming the adapter is release-ready:

   ```bash
   python tests/validate_devmesh.py
   python tests/test_routing_contract.py
   python tests/test_feature_contracts.py
   ```

11. Update `README.md`, `docs/ARCHITECTURE.md`, and `CHANGELOG.md` when public behavior or architecture changes.
12. Never add secrets, personal tokens, or environment-specific credentials to this repository.
13. New platform adapters should reuse DevMesh skill contracts instead of forking the methodology unnecessarily.
