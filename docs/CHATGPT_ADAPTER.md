# ChatGPT Adapter

DevMesh v0.6 adds a portable ChatGPT adapter using the Agent Skills format.

## Why a separate adapter?

Codex is an execution-oriented coding environment and can expose local/project tools such as shell, Git, and plugin MCP servers. Normal ChatGPT conversations may instead expose uploaded files, connected apps such as GitHub, artifact tools, web access, or other workspace-specific capabilities.

The ChatGPT adapter keeps the same DevMesh engineering rules while refusing to assume Codex-only capabilities.

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

## Build the upload bundle

From the repository root:

```bash
python scripts/build_chatgpt_adapter.py
```

Output:

```text
dist/devmesh-chatgpt-v0.6.0.zip
```

The ZIP has `SKILL.md` at its root plus references and the generated shared playbooks.

## Install in ChatGPT

When the ChatGPT account/surface supports uploaded Personal Skills:

1. Open ChatGPT Skills/Plugins.
2. Choose Create.
3. Choose Upload from your computer.
4. Upload the generated `devmesh-chatgpt-v0.6.0.zip` bundle.
5. Start a new chat and ask ChatGPT to use DevMesh.

Personal Skills availability and admin controls depend on the ChatGPT plan/workspace/surface. The adapter can exist in the repository even when a specific account does not currently expose skill upload.

## Example

```text
Use DevMesh.
Build a working quotation website.
```

The adapter will first detect whether the current chat can read/write a repository, execute code, control a browser, access GitHub CI, or deploy. It then runs the strongest available DevMesh workflow and labels missing evidence `BLOCKED` or `NOT RUN` rather than pretending Codex tools exist.

## GitHub-connected example

```text
Use DevMesh to fix GitHub issue #42 and prepare a PR. Do not merge it.
```

If the GitHub app is connected with the necessary permissions, DevMesh can inspect the actual issue/repository and use those actions. Otherwise it prepares the patch/plan and reports PR delivery as blocked.

## Browser QA boundary

Public web browsing is not a substitute for controlling a local/private application. The ChatGPT adapter only reports Browser QA as passed when actual browser-control/browser-automation evidence exists for the target app.

## Core portability rule

Shared DevMesh playbooks remain provider-neutral. The adapter changes tool invocation and evidence boundaries, not the engineering methodology.
