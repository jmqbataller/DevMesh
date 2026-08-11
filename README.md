# DevMesh

**DevMesh** is a provider-ready software-engineering workflow framework for AI coding agents. It makes agents inspect, plan, build, verify, review, repair, and deliver with evidence instead of jumping straight into edits.

DevMesh now ships with two adapters:

- **Codex adapter** — plugin + Playwright MCP for coding-environment execution
- **ChatGPT adapter** — portable Agent Skills bundle that adapts to the tools/connectors available in normal ChatGPT

## DevMesh v0.6

v0.6 keeps the 33 shared engineering playbooks from v0.5 and adds a first-class **ChatGPT Adapter**.

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

The ChatGPT adapter lives at:

```text
adapters/chatgpt/devmesh-chatgpt/
├── SKILL.md
└── references/
```

It follows the portable Agent Skills model and is packaged with generated copies of all shared DevMesh playbooks so the upload bundle is self-contained.

Build it with:

```bash
python scripts/build_chatgpt_adapter.py
```

Output:

```text
dist/devmesh-chatgpt-v0.6.0.zip
```

The adapter intentionally does **not** assume normal ChatGPT has a local shell, localhost server, Git CLI, Playwright, or deployment credentials.

Instead it detects the tools available in the current chat and adapts:

```text
GitHub connected?      → inspect/edit issue/repo/PR/CI when authorized
Files available?       → inspect real uploaded/library source
Code runtime available?→ run tests/build when possible
Browser control?       → real Browser QA
Deployment app/tool?   → production release evidence
None of the above?     → generate source/patches/plans and mark execution NOT RUN/BLOCKED
```

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
├── plugins/devmesh/                 # Codex adapter
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
