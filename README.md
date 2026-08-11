# DevMesh

**DevMesh** is a provider-ready software-engineering workflow framework for AI coding agents. It makes agents inspect, plan, build, verify, review, repair, and deliver with evidence instead of jumping straight into edits.

DevMesh ships with two adapters:

- **Codex adapter** — plugin + Playwright MCP for coding-environment execution
- **ChatGPT adapter** — portable Agent Skills bundle that adapts to the tools/connectors available in normal ChatGPT

## Download DevMesh for ChatGPT

[**Download `devmesh-chatgpt-v0.6.0.zip`**](https://github.com/jmqbataller/DevMesh/releases/download/v0.6.0/devmesh-chatgpt-v0.6.0.zip)

The GitHub Actions validation workflow builds the ChatGPT bundle from source and publishes it as the `v0.6.0` GitHub Release asset, so users do not need to clone the repository or run the build script themselves.

### Install in ChatGPT

On a ChatGPT account/surface that supports uploaded Skills:

1. Open **Plugins** in ChatGPT.
2. Open the **Skills** tab.
3. Choose **Create** → **Upload from your computer**.
4. Upload `devmesh-chatgpt-v0.6.0.zip`.
5. Start a new chat and prompt:

```text
Use DevMesh.
Build a working quotation website.
```

Skill availability and installation depend on the ChatGPT plan, workspace settings, role, region, and supported surface.

## DevMesh v0.6

v0.6 keeps the **33 shared engineering playbooks** from v0.5 and adds a first-class ChatGPT adapter.

### Shared engineering stack

- routing + Quick / Standard / Deep modes
- codebase intelligence + environment doctor
- one-prompt full-stack product build
- database architect + API contract
- architecture guard
- implementation + systematic debugging
- Browser QA + network failure QA + visual regression
- UI/UX + accessibility + performance
- synthetic test data/personas
- regression testing + security + observability
- QA verification + QA reporting + code review + multi-agent review
- CI auto-heal
- Issue → PR
- production deployment
- project memory + Git delivery

## One prompt → working product

A prompt can be as short as:

```text
Use DevMesh.
Build a working quotation website.
```

DevMesh treats **working** as an integrated product when the behavior requires multiple layers:

```text
inspect source/environment
→ select execution mode
→ risk assessment
→ full-stack product contract
→ database architecture when required
→ API contract when required
→ frontend + backend/server + persistence
→ vertical-slice integration
→ relevant QA/security/accessibility/performance
→ review/report/delivery
```

It does not silently invent unrelated large scope such as payments, subscriptions, CRM, PDF export, or multi-company tenancy unless requested or required.

## ChatGPT Adapter

Source:

```text
adapters/chatgpt/devmesh-chatgpt/
├── SKILL.md
└── references/
```

The portable upload bundle contains `SKILL.md`, supporting references, and generated copies of all shared DevMesh playbooks.

Developers can also build the bundle locally:

```bash
python scripts/build_chatgpt_adapter.py
```

Output:

```text
dist/devmesh-chatgpt-v0.6.0.zip
```

The adapter intentionally does **not** assume normal ChatGPT has a local shell, localhost server, Git CLI, Playwright, deployment credentials, or GitHub write access.

Instead it detects the capabilities available in the current chat:

```text
GitHub readable?       → inspect real repository/issue/PR/CI evidence
GitHub writable?       → write only if an explicit write action is exposed and authorized
Files available?       → inspect real uploaded/library source
Code runtime available?→ run tests/build when possible
Browser control?       → real Browser QA
Deployment app/tool?   → production release evidence
None of the above?     → generate source/patches/plans and mark execution NOT RUN/BLOCKED
```

The standard ChatGPT GitHub app may be read-only. DevMesh never assumes commit/push/PR-write capability just because GitHub is connected; Codex remains the appropriate OpenAI coding surface for direct repository write/push workflows when those actions are not exposed in ChatGPT.

**Public web browsing is not treated as Browser QA for a local/private application.** Missing execution evidence is never converted into a pass.

See [`docs/CHATGPT_ADAPTER.md`](docs/CHATGPT_ADAPTER.md).

## Codex Adapter

Codex remains the deepest execution adapter because the plugin can expose project/runtime tools and bundled Playwright MCP.

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

Start a new Codex thread/session after reinstall so updated skills/MCP tools load.

## Execution modes

```text
DevMesh Quick
→ small low-risk task
→ focused evidence

DevMesh Standard   # default
→ normal routing and relevant quality gates

DevMesh Deep
→ environment doctor
→ architecture/database/API review
→ full relevant test/build checks
→ browser/resilience QA where executable
→ accessibility/security/performance
→ observability + deep review
→ QA report
```

Modes control depth, not truthfulness. Quick never bypasses a required safety/evidence boundary.

## Evidence states

DevMesh uses:

- `PASS`
- `FAIL`
- `FIXED`
- `BLOCKED`
- `NOT RUN`

A whole-product implementation may be complete while live Browser QA or deployment remains `BLOCKED`; DevMesh reports that boundary instead of faking success.

## Public distribution status

- **GitHub source:** public
- **GitHub Release ZIP:** automated for v0.6.0
- **Manual ChatGPT Skill upload:** supported on eligible ChatGPT accounts/surfaces
- **ChatGPT Plugin Directory listing:** not yet published

OpenAI's Plugin Directory can contain skill-only plugins, but public directory availability and publication are controlled by OpenAI. If DevMesh later adds an app/MCP integration for ChatGPT, the OpenAI Apps SDK/app submission flow can also be used as part of a public plugin listing.

## Smoke tests

ChatGPT / Codex product build:

```text
Use DevMesh.
Build a working quotation website.
```

Deep production review:

```text
DevMesh Deep: prepare this application for production.
```

GitHub delivery:

```text
Use DevMesh to fix GitHub issue #42 and prepare a PR. Do not merge it.
```

## Development validation

```bash
python tests/validate_devmesh.py
python tests/test_routing_contract.py
python tests/test_feature_contracts.py
python tests/test_chatgpt_adapter.py
```

## Current platform support

| Platform | Status |
|---|---|
| Codex | **v0.6 supported** |
| ChatGPT | **v0.6 portable Agent Skills adapter** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

## Repository structure

```text
DevMesh/
├── .agents/plugins/marketplace.json
├── plugins/devmesh/                  # Codex adapter
├── adapters/chatgpt/devmesh-chatgpt/ # ChatGPT Agent Skill source
├── scripts/build_chatgpt_adapter.py
├── tests/
├── docs/
├── AGENTS.md
├── CHANGELOG.md
└── README.md
```

## License

MIT
