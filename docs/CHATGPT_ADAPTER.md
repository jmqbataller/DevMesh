# ChatGPT Adapter

DevMesh v0.7 provides a portable ChatGPT Agent Skills adapter with all 45 shared playbooks, including Mission Control.

## Download

GitHub Release asset:

`devmesh-chatgpt-v0.7.0.zip`

## Build locally

```bash
python scripts/build_chatgpt_adapter.py
```

Output: `dist/devmesh-chatgpt-v0.7.0.zip`.

## Install

When the ChatGPT account/surface supports uploaded Skills:
1. Open Plugins → Skills.
2. Choose Create → Upload from your computer.
3. Upload `devmesh-chatgpt-v0.7.0.zip`.
4. Start a new chat.

## Mission Control in ChatGPT

```text
DevMesh Mission Control:
Build a production-ready quotation SaaS.
```

The adapter detects whether the current chat can read/write a repository, execute code, control a browser, run actual sub-agents, access CI, persist project memory, or deploy. It then runs the strongest executable path.

If sub-agents are unavailable, Mission Control uses the same dynamic task graph but executes ready nodes sequentially. If an independent reviewer context is unavailable, the Judge is labeled a same-context fallback. Public web browsing is not Browser QA for a local/private app.

## Evidence

Missing capabilities remain `BLOCKED`/`NOT RUN`. Scenario simulation is not a measured benchmark. Failure memory is opt-in and never stores secrets/PII. Production incidents are not marked resolved without production evidence.
