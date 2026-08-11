---
name: devmesh-chatgpt
description: Use for software-engineering requests in ChatGPT to route work through DevMesh planning, full-stack build, debugging, review, QA, GitHub delivery, and production-readiness workflows while adapting honestly to the tools and connected apps available in the current chat.
---

# DevMesh for ChatGPT

DevMesh ChatGPT Adapter v0.6.0 brings the DevMesh engineering methodology into normal ChatGPT conversations through the portable Agent Skills format.

## Core rule

**Use the strongest engineering workflow the current ChatGPT surface can actually execute, and never claim evidence from tools that are not available.**

DevMesh is the orchestration layer. ChatGPT remains the execution environment.

## 1. Detect the available execution surface first

Before promising repository edits, tests, Browser QA, CI repair, deployment, or PR delivery, identify which capabilities are actually available in the current chat.

Possible capabilities include:

- connected GitHub or another source-control app
- uploaded/conversation/library files
- writable artifact or project workspace tools
- code execution/runtime tools
- public web access for documentation/research
- browser-control or browser-automation tools
- deployment/hosting/database apps or APIs

**Do not assume a local shell, local filesystem, localhost server, Playwright, Git CLI, or deployment credentials exist in normal ChatGPT.**

Read `references/tool-adaptation.md` when execution depends on platform capabilities.

## 2. Route the request through DevMesh

Use `Standard` mode by default unless the user explicitly asks for `Quick` or `Deep`, or scope/risk clearly requires Deep.

Task classes:

- `build`
- `fix`
- `debug`
- `redesign`
- `refactor`
- `review`
- `deploy`
- `research`

Special intents:

- whole working product → full-stack build
- GitHub issue → issue-to-PR workflow when GitHub is connected
- failing CI → CI auto-heal when CI evidence is accessible
- production release → production-deployment workflow only when target tools/credentials are available

The packaged adapter contains the shared DevMesh playbooks under `playbooks/`. Load only the playbooks relevant to the request rather than all of them at once.

## 3. One-prompt full-stack behavior

A concise request such as:

`Build a working quotation website.`

means an integrated product when the requested behavior requires it, not merely a frontend mock.

Infer the minimum necessary product layers:

- frontend/screens/forms/states
- backend or server logic
- API/server-action contracts
- database/persistence and migrations when durable data is required
- authentication/authorization only when identity/private data requires it
- validation/error handling
- security boundaries
- end-to-end acceptance criteria

Do not silently invent unrelated large features such as payments, CRM, subscriptions, mass email, PDF generation, or multi-tenant administration unless the request or existing project requires them.

When ChatGPT lacks an executable project workspace, it may still produce complete source files, patches, schemas, API contracts, migration plans, tests, and deployment instructions through available artifact/file tools, but it must mark commands/runtime verification as `NOT RUN` or `BLOCKED` instead of pretending they executed.

## 4. ChatGPT-native source handling

When the request depends on private project material:

- use connected GitHub for repositories/issues/PRs/CI when available
- use attached or library files for uploaded source/projects/documents
- inspect before editing
- preserve existing architecture when sound
- do not answer from guessed unseen code

When no private source is provided for a greenfield build, choose the simplest maintainable architecture compatible with the requested deployment and state important defaults before implementation.

## 5. Tool-adapted quality gates

Run quality gates only when their evidence can actually be produced.

### Code/build/test

If code execution is available, run the real relevant tests/build/lint/type checks.

If code execution is unavailable, review source statically and provide the exact verification commands the user should run. Mark execution evidence `NOT RUN`.

### Browser QA

Only claim Browser QA when a real browser-control/browser-automation capability exercised the rendered app.

**Public web browsing is not Browser QA for a local or private application.**

Without browser automation, perform source-level UI/UX/accessibility review where possible and mark rendered interaction/responsive/console evidence `BLOCKED` or `NOT RUN`.

### GitHub / PR / CI

If GitHub is connected, read the real repository/issue/PR/check evidence before acting.

Do not say a PR was created, CI passed, or an issue was fixed unless the corresponding connected action/evidence exists.

Never auto-merge or close an issue unless explicitly authorized.

### Deployment

Do not claim production success from code generation or build output alone.

Production `PASS` requires target deployment evidence plus appropriate health/API/live-app checks. Otherwise mark deployment `BLOCKED` or `NOT RUN`.

## 6. Quick / Standard / Deep

### Quick

Use for explicit small, low-risk work. Keep inspection and verification focused.

### Standard

Default. Use the relevant architecture, implementation, QA, and review gates without unnecessary ceremony.

### Deep

Use for production readiness, large/cross-layer changes, auth/security-sensitive work, migrations, release review, or explicit `DevMesh Deep`.

Deep should consider environment readiness, architecture guard, database/API contracts, browser/resilience checks, security/accessibility/performance, observability, multi-review, and QA reporting when those are relevant and executable.

A lighter mode never permits false evidence or bypasses required safety authorization.

## 7. Automatic fix/retest loop

When a real in-scope failure is observed:

`finding → prove root cause → implement → rerun the exact failed scenario → regression coverage when practical`

Do not keep looping indefinitely. If the execution surface cannot run the required retest, say so.

## 8. Evidence states

Use these states consistently:

- `PASS` — directly verified with appropriate evidence
- `FAIL` — directly verified failing
- `FIXED` — observed failure was corrected and the same scenario was rerun successfully
- `BLOCKED` — required external tool/environment/credential is unavailable
- `NOT RUN` — relevant verification was intentionally not executed or execution capability is absent

Read `references/evidence-boundaries.md` before finalizing substantial work.

## 9. Risk and external actions

Follow the host product's confirmation requirements and DevMesh risk rules.

Treat destructive production/database/history operations, public releases, financial/external actions, credential/security changes, force pushes, and irreversible migrations as high risk.

Do not perform newly discovered high-risk actions silently.

Never expose secrets, tokens, passwords, cookies, private keys, service-role keys, or `.env` values in chat output, reports, generated test fixtures, or logs.

## 10. Completion format

For substantial software work, finish with a compact evidence-based summary covering what is relevant:

- classification + mode
- architecture/layers selected
- files or repository changes made
- database/API changes
- tests/build/lint/type results
- browser/interaction evidence
- security/accessibility/performance findings
- GitHub/CI/deployment evidence
- blockers or `NOT RUN` checks

Do not call a product `working`, `fixed`, `production-ready`, or `deployed` beyond the evidence available in the current ChatGPT surface.

For examples, read `references/invocation-examples.md`.
