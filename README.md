# DevMesh

**DevMesh** is an evidence-based AI software-engineering orchestration framework for ChatGPT, Codex, and future adapters. It helps agents inspect, plan, build, delegate, verify, judge, repair, and deliver without turning assumptions into fake passes.

DevMesh ships with:
- **Codex adapter** — plugin + Playwright MCP for coding-environment execution
- **ChatGPT adapter** — portable Agent Skills bundle that adapts to tools available in normal ChatGPT

## Download DevMesh for ChatGPT

[**Download `devmesh-chatgpt-v0.7.0.zip`**](https://github.com/jmqbataller/DevMesh/releases/download/v0.7.0/devmesh-chatgpt-v0.7.0.zip)

On a ChatGPT account/surface that supports uploaded Skills: open **Plugins → Skills → Create → Upload from your computer**, upload the ZIP, then start a new chat.

## DevMesh v0.7 — Mission Control

v0.7 contains **45 composable skills**. The new Mission Control stack adds:

- `mission-control` — top-level dependency-aware orchestration
- `dynamic-task-graph` — DAG, readiness, acceptance/evidence contracts
- `parallel-agent-orchestration` — real delegation when the runtime supports sub-agents; explicit sequential fallback otherwise
- `devmesh-judge` — evidence-first final release gate
- `confidence-engine` — hypothesis/evidence confidence routing
- `adversarial-review` — bounded architecture/design debate
- `change-impact-map` — blast radius + regression scope
- `failure-memory` — opt-in verified failure lessons
- `eval-replay-lab` — repeatable regression/benchmark cases
- `architecture-simulator` — failure-mode scenario simulation before implementation
- `resource-budget` — Eco / Balanced / Max orchestration intensity
- `incident-commander` — production incident stabilization and recovery verification

Existing full-stack, database/API, Browser QA, security, accessibility, performance, CI, deployment, observability, code review, project memory, reporting, and Git delivery workflows remain available.

## Mission Control example

```text
DevMesh Mission Control:
Build a production-ready quotation SaaS.
```

Conceptually:

```text
inspect source/environment
→ choose Quick/Standard/Deep + Eco/Balanced/Max
→ risk + change-impact map
→ dynamic task graph
→ architecture simulation/adversarial review when relevant
→ parallel READY nodes when real sub-agents exist
   (sequential fallback otherwise)
→ integrate frontend/backend/API/database
→ Browser QA + relevant quality gates
→ DevMesh Judge
→ fix exact failed gates + re-judge (bounded)
→ QA report / delivery
```

Mission Control never claims parallel execution or an independent Judge if the runtime did not actually provide them.

## One prompt → working product

```text
Use DevMesh.
Build a working quotation website.
```

“Working” means integrated behavior when required: frontend, backend/server logic, API/server actions, persistence/migrations, validation/error states, auth boundaries when needed, and end-to-end evidence. DevMesh does not silently invent unrelated scope such as payments, CRM, subscriptions, PDF export, or multi-company tenancy.

## Depth + resource modes

```text
DevMesh Quick + Eco
DevMesh Standard + Balanced   # defaults
DevMesh Deep + Max
```

Quick/Standard/Deep control engineering depth. Eco/Balanced/Max control resource intensity. Neither can bypass safety/evidence requirements.

## DevMesh Judge

For substantial missions the Judge evaluates relevant dimensions such as functionality, tests/build, data/API integrity, architecture, security, accessibility, browser behavior, performance, regression risk, and operations. Critical failed gates veto release. Missing required evidence remains `BLOCKED`/`NOT RUN` rather than being averaged away.

## Incident Commander

```text
DevMesh Incident Commander:
Production quotations stopped saving.
```

The incident workflow prioritizes stabilization, evidence preservation, blast-radius analysis, recent-change inspection, confidence-aware root-cause testing, risk-gated mitigation, exact recovery verification, monitoring, and a post-incident report.

## Eval / Replay Lab

Representative tasks and proven failures can become reusable `.devmesh/evals/` cases. DevMesh prefers deterministic graders and identical fixtures across versions, then reports regressions/improvements without silently changing expected outcomes.

## ChatGPT Adapter

The ChatGPT adapter lives at `adapters/chatgpt/devmesh-chatgpt/`. It does not assume normal ChatGPT has a shell, localhost, Git CLI, Playwright, sub-agents, persistent memory, or deployment credentials. Missing execution capabilities remain `BLOCKED`/`NOT RUN`.

Developers can build the upload bundle locally:

```bash
python scripts/build_chatgpt_adapter.py
```

Output: `dist/devmesh-chatgpt-v0.7.0.zip`.

## Codex Adapter

Install:

```bash
codex plugin marketplace add jmqbataller/DevMesh
codex plugin add devmesh@devmesh-marketplace
```

Update:

```bash
codex plugin marketplace upgrade devmesh-marketplace
codex plugin add devmesh@devmesh-marketplace
codex plugin list
```

Start a new Codex thread/session after reinstall.

## Evidence states

DevMesh uses `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A` where appropriate. Browser/CI/production/parallel-agent/independent-judge/benchmark claims require corresponding evidence.

## Public distribution status

- GitHub source: public
- GitHub Release ZIP: automated
- Manual ChatGPT Skill upload: available on eligible ChatGPT accounts/surfaces
- OpenAI Plugin Directory listing: submission package prepared; publication still requires publisher verification, OpenAI review, approval, and Publish

See `docs/plugin-submission/` for the submission pack.

## Development validation

```bash
python tests/validate_devmesh.py
python tests/test_routing_contract.py
python tests/test_feature_contracts.py
python tests/test_chatgpt_adapter.py
python tests/test_plugin_submission_pack.py
```

## Current platform support

| Platform | Status |
|---|---|
| Codex | **v0.7 supported** |
| ChatGPT | **v0.7 portable Agent Skills adapter** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

## License

MIT
