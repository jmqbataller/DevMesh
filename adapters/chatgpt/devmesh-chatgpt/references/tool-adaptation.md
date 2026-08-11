# ChatGPT Tool Adaptation

DevMesh must adapt to capabilities actually exposed in the current ChatGPT surface.

## Capability mapping

| DevMesh need | ChatGPT-capable path | If unavailable |
|---|---|---|
| Read private repository | Connected GitHub/app | Ask for repo/file access or work from supplied files only |
| Edit repository | Connected GitHub write action or writable project/artifact workspace | Generate patch/files; mark repository write `BLOCKED` |
| Read issue/PR/CI | Connected GitHub/app | Do not infer private state from memory or prompt summaries |
| Run commands/tests/build | Code execution/project runtime tool | Provide exact commands and mark `NOT RUN` |
| Local dev server | Runtime/project workspace capable of starting it | Do not claim localhost execution |
| Browser QA | Browser-control/browser-automation tool that can exercise the app | Source review only; mark rendered QA `BLOCKED`/`NOT RUN` |
| Public docs/research | Web access | Use provided source material only |
| Database changes | Connected DB/app/runtime with authorized credentials | Generate schema/migration safely; mark execution `BLOCKED` |
| Production deploy | Connected hosting/deployment capability + authorization | Produce deployment plan/config; do not claim release |
| Artifact/source bundle | File/artifact creation capability | Return code/content inline where practical |

## GitHub adaptation

When GitHub tools are available:

1. Fetch the actual repository/issue/PR/check state first.
2. Preserve repository instructions and current architecture.
3. Use write actions only within authorization and risk boundaries.
4. Verify the resulting ref/file/PR/check state after writes when possible.
5. Never claim a commit/PR/CI result from an intended action alone.

## Browser adaptation

A normal web-search/browser-reading capability is not equivalent to controlling the application under test.

Browser QA requires evidence such as actual rendered navigation, form interactions, viewport changes, console/runtime inspection, screenshots, or equivalent automation against the target app.

If that capability is absent, ChatGPT may still review HTML/CSS/components/accessibility semantics statically, but must not report Browser QA as passed.

## Runtime adaptation

When no shell/project runtime exists:

- do not claim `npm install`, `npm test`, `npm run build`, migrations, servers, or scripts ran
- create complete source/config/test files through available file/artifact tools when possible
- provide exact setup and verification commands
- distinguish static reasoning from executed evidence

## Connected apps

Connected apps may vary by plan, workspace, role, region, and conversation. Inspect what is available rather than hard-coding a provider assumption.

App-backed actions remain governed by the app/workspace permissions and confirmation behavior. DevMesh never overrides those controls.
