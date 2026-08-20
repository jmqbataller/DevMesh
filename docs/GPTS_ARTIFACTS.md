# DevMesh for GPTs and ChatGPT Artifacts

DevMesh has two ChatGPT-oriented delivery paths:

1. `adapters/chatgpt/devmesh-chatgpt/` — portable Agent Skill adapter for ChatGPT surfaces that support uploaded skills/plugins.
2. `adapters/gpts/devmesh-gpt/` — GPT Builder configuration kit for Custom GPT-style setups.

The GPT Builder path exists because a Custom GPT is configured through Instructions, Knowledge, capabilities, Apps, and/or Actions rather than by installing the Codex plugin repository directly.

## Artifact-aware behavior

The GPT Instructions include an artifact-first contract. When the active ChatGPT surface exposes a native interactive site/app or file-artifact capability, DevMesh should produce the actual deliverable there. When it does not, DevMesh falls back to complete source, patches, specs, or generated files through whatever tools are truly available.

An artifact preview is not production deployment evidence. A static visual artifact is not proof of backend, database, authentication, payment, API, or persistence behavior.

## GPT Knowledge packaging

DevMesh has more individual playbooks than should be uploaded one-by-one to a GPT. `scripts/build_gpts_kit.py` groups all core skill playbooks into ten text-forward Knowledge packs.

Build:

```bash
python scripts/build_gpts_kit.py
```

The ZIP contains:

```text
INSTRUCTIONS.md
GPT_CONFIG.md
README.md
VERSION
UPLOAD_MANIFEST.md
knowledge/
  devmesh-playbooks-01.md
  ...
  devmesh-playbooks-10.md
```

Paste `INSTRUCTIONS.md` into the GPT Instructions field. Upload only the files inside `knowledge/` to GPT Knowledge.

## Apps vs Actions

Use Apps when the GPT should use user-connected services available on the ChatGPT surface. Use Actions when you are exposing your own external API through an OpenAPI schema. A GPT configuration should not depend on both models at the same time.

## Recommended test prompts

```text
DevMesh Artifact:
Build a responsive inventory dashboard as an interactive artifact.
Use sample data if no live database is connected and label it clearly.
```

```text
DevMesh Design-to-Code:
Use this screenshot as the visual reference.
Separate OBSERVED, INFERRED, and UNKNOWN decisions.
Create the implementation as an artifact if supported.
```

```text
DevMesh Debug:
Inspect this repository issue, prove the root cause,
implement the smallest safe fix, and rerun the failing scenario.
```
