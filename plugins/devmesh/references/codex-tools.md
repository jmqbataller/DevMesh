# Codex Environment Notes

Codex execution capabilities differ across the app, CLI, workspaces, sandboxes, plugin versions, and enabled feature flags. Detect capabilities instead of assuming them.

## Plugin surfaces used by DevMesh

The Codex adapter uses:

- `.codex-plugin/plugin.json` for plugin metadata and skill discovery
- `.mcp.json` for the bundled Playwright MCP server
- `skills/` for provider-neutral DevMesh workflows

The browser MCP configuration launches:

```text
npx -y @playwright/mcp@latest --isolated
```

If the MCP server cannot start, `browser-engine`/`browser-qa` must report the gate as blocked/partial instead of fabricating browser evidence.

## Git environment detection

Useful read-only commands when Git is available:

```bash
git status -sb
git branch --show-current
git rev-parse --show-toplevel
git remote -v
```

Before modifying a repository with existing local work, inspect the diff and preserve unrelated changes.

## Risk and approvals

Use the DevMesh `risk-engine` before mutation. Sandbox approval prompts and DevMesh risk classification are complementary: a host allowing a command does not automatically make the command low-risk.

## Browser tools

Prefer the plugin-provided Playwright MCP browser for exploratory/runtime QA. Keep browser sessions isolated unless the user explicitly authorizes testing with existing authenticated state.

Browser evidence may include:

- accessibility/DOM snapshots
- rendered text/state
- clicks/typing/navigation
- viewport changes
- console/runtime observations
- network evidence when exposed by the tool
- screenshots/artifacts

Do not assume every MCP release exposes every artifact type. Report missing trace/screenshot/network capabilities accurately.

## Native subagents

Codex versions may expose native multi-agent tools such as agent spawning/waiting/closing. `multi-agent-review` should detect availability at runtime.

Good reviewer boundaries:

- spec/correctness
- code quality
- security
- browser/UX/accessibility/performance

Reviewers should remain read-only against the shared working tree. One lead/implementer applies fixes and performs retesting.

If native subagents are unavailable, execute the same reviewer briefs sequentially and state the limitation.

## Detached worktrees / restricted Git environments

When Codex runs inside an externally managed or detached worktree, branch/push/PR operations may be restricted even though file edits/tests work. In that case:

- finish code and verification
- preserve clean Git scope
- provide the branch/commit/PR handoff information the user needs
- do not claim a push/PR happened when the environment blocked it

## Windows notes

Node installations on Windows may expose `npm.cmd`/`npx.cmd` while PowerShell execution policy blocks `npm.ps1`/`npx.ps1`. DevMesh uses `npx` in the cross-platform MCP config; if manual troubleshooting is required on Windows, `npx.cmd` is a useful diagnostic equivalent.
