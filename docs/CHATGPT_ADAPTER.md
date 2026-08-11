# ChatGPT Adapter

DevMesh v0.6 adds a portable ChatGPT adapter using the Agent Skills format.

## Public download

GitHub Release asset:

`https://github.com/jmqbataller/DevMesh/releases/download/v0.6.0/devmesh-chatgpt-v0.6.0.zip`

The repository validation workflow builds this ZIP from source and attaches it to the `v0.6.0` GitHub Release on successful pushes to `main`.

## Install in ChatGPT

When the ChatGPT account/surface supports uploaded Personal Skills:

1. Open **Plugins**.
2. Open **Skills**.
3. Choose **Create** → **Upload from your computer**.
4. Upload `devmesh-chatgpt-v0.6.0.zip`.
5. Start a new chat and ask ChatGPT to use DevMesh.

Example:

```text
Use DevMesh.
Build a working quotation website.
```

Personal Skills availability and admin controls depend on the ChatGPT plan, workspace, role, region, and supported surface.

## Why a separate adapter?

Codex is an execution-oriented coding environment and can expose local/project tools such as shell, Git, and plugin MCP servers. Normal ChatGPT conversations may instead expose uploaded files, connected apps, artifact tools, web access, or workspace-specific capabilities.

The ChatGPT adapter keeps the same DevMesh engineering rules while refusing to assume Codex-only capabilities.

## GitHub capability boundary

A GitHub connection in ChatGPT does not automatically mean write access.

Treat repository capabilities separately:

- repository read/search may be available
- issue/PR/check reading may be available depending on the surface
- commit/push/branch/PR writes require an explicitly exposed write-capable action
- if write actions are absent, DevMesh should generate the patch/files and mark repository delivery `BLOCKED` rather than claiming a push or PR

For direct OpenAI-managed repository write/push workflows, Codex remains the dedicated coding surface when ChatGPT does not expose those actions.

## Source layout

```text
adapters/chatgpt/devmesh-chatgpt/
├── SKILL.md
└── references/
    ├── tool-adaptation.md
    ├── evidence-boundaries.md
    └── invocation-examples.md
```

The release bundle also includes generated copies of every shared DevMesh core playbook under `playbooks/` so the uploaded skill remains self-contained.

## Build the upload bundle locally

From the repository root:

```bash
python scripts/build_chatgpt_adapter.py
```

Output:

```text
dist/devmesh-chatgpt-v0.6.0.zip
```

The ZIP has `SKILL.md` at its root plus references and all generated shared playbooks.

## Tool adaptation

The adapter first detects whether the current chat can read/write a repository, execute code, control a browser, access CI, or deploy. It then runs the strongest available DevMesh workflow and labels missing evidence `BLOCKED` or `NOT RUN` rather than pretending unavailable tools exist.

## Browser QA boundary

Public web browsing is not a substitute for controlling a local/private application. The ChatGPT adapter only reports Browser QA as passed when actual browser-control/browser-automation evidence exists for the target app.

## Plugin Directory status

OpenAI's Plugin Directory is the discovery surface for plugins across ChatGPT and Codex, and plugins may contain only Skills. DevMesh is not yet published as a public Plugin Directory listing.

The current public distribution path is:

```text
GitHub repository
→ GitHub Release
→ devmesh-chatgpt-v0.6.0.zip
→ ChatGPT Skills upload on eligible accounts/surfaces
```

For future directory publication, DevMesh should follow the OpenAI plugin/app publication route available at submission time. If an app/MCP integration is added, OpenAI's Apps SDK and app submission process can be used for review and potential distribution through a plugin listing.

## Core portability rule

Shared DevMesh playbooks remain provider-neutral. The adapter changes tool invocation and evidence boundaries, not the engineering methodology.
