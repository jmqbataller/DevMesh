# DevMesh GPT Builder Adapter

This adapter packages DevMesh for a Custom GPT / GPT Builder style setup.

It complements, rather than replaces, the portable ChatGPT Agent Skill adapter at
`adapters/chatgpt/devmesh-chatgpt/`.

## What this adapter provides

- `INSTRUCTIONS.md` — ready-to-paste GPT instructions.
- `GPT_CONFIG.md` — recommended name, description, capabilities, and conversation starters.
- `scripts/build_gpts_kit.py` — builds a GPT-friendly ZIP with DevMesh playbooks grouped into a small number of Knowledge files.
- Artifact-aware behavior — when the current ChatGPT surface exposes a native interactive or file artifact capability, DevMesh should create the deliverable there instead of only describing it.
- Evidence-first fallback — when a surface cannot render, execute, deploy, browse, or write, DevMesh produces the strongest source/specification it can and marks verification as `NOT RUN` or `BLOCKED`.

## Build

```bash
python scripts/build_gpts_kit.py
```

Default output:

```text
dist/devmesh-gpts-kit-v<version>.zip
```

## Install in GPT Builder

1. Open the GPT editor available to your account/workspace.
2. Set the Name and Description from `GPT_CONFIG.md`.
3. Paste `INSTRUCTIONS.md` into the GPT Instructions field.
4. Run `python scripts/build_gpts_kit.py`.
5. Extract the generated ZIP.
6. Upload every file under `knowledge/` as GPT Knowledge.
7. Enable only the capabilities you actually want the GPT to use.
8. If you use connected Apps, do not configure Actions at the same time. If you need your own API, use Actions instead and provide a valid OpenAPI schema.
9. Test the conversation starters in Preview and verify tool behavior before publishing or sharing.

The generated package intentionally stays below the GPT Knowledge file-count ceiling by combining the individual DevMesh playbooks into grouped text-forward reference files.
