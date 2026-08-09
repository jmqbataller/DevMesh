# Repository Instructions

This repository defines **DevMesh**, a provider-neutral development-workflow framework with Codex as the first supported adapter.

When modifying it:

1. Keep the core framework provider-neutral; platform-specific behavior belongs in adapters or references.
2. Keep each skill focused on one responsibility.
3. Do not duplicate entire workflows across multiple skills; link responsibilities through routing instead.
4. Preserve the 10 core v1 skill names unless a versioned migration is intentional.
5. Run `python scripts/validate_plugin.py` before claiming the current adapter structure is valid.
6. Update `CHANGELOG.md` for user-visible behavior changes.
7. Never add secrets, personal tokens, or environment-specific credentials.
8. New platform support should reuse the core skills wherever possible instead of forking them.
