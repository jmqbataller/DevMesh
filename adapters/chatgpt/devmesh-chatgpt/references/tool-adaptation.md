# ChatGPT Tool Adaptation

DevMesh must adapt to capabilities actually exposed in the current ChatGPT surface.

## Capability mapping

| DevMesh need | ChatGPT-capable path | If unavailable |
|---|---|---|
| Analyze supplied visual reference | Image/PDF/file understanding for the reference actually supplied | Mark unavailable portions `BLOCKED`; do not invent unseen design details |
| Access private Figma/design source | Connected source/tool or user-supplied export/file with actual access | Work from supplied exports/screenshots only; mark private source access `BLOCKED` |
| Render/reference visual comparison | Browser-control + screenshot/render capture against the implementation plus the authoritative reference | Reference analysis may continue, but visual fidelity is `BLOCKED`/`NOT RUN` |
| Read private repository | Connected GitHub/app with read access | Ask for repo/file access or work from supplied files only |
| Edit repository | Explicitly exposed GitHub write action or writable project/artifact workspace | Generate patch/files; mark repository write `BLOCKED` |
| Read issue/PR/CI | Connected GitHub/app when that data is exposed | Do not infer private state from memory or prompt summaries |
| Run commands/tests/build | Code execution/project runtime tool | Provide exact commands and mark `NOT RUN` |
| Local dev server | Runtime/project workspace capable of starting it | Do not claim localhost execution |
| Browser QA | Browser-control/browser-automation tool that can exercise the app | Source review only; mark rendered QA `BLOCKED`/`NOT RUN` |
| Public docs/research | Web access | Use provided source material only |
| Database changes | Connected DB/app/runtime with authorized credentials | Generate schema/migration safely; mark execution `BLOCKED` |
| Production deploy | Connected hosting/deployment capability + authorization | Produce deployment plan/config; do not claim release |
| Artifact/source bundle | File/artifact creation capability | Return code/content inline where practical |

## Design-to-Code adaptation

A screenshot/mockup can be valid visual evidence when it is actually supplied, but it is not a complete behavior specification. Keep `OBSERVED`, `INFERRED`, and `UNKNOWN` separate.

Do not assume access to private Figma layers, original design tokens, exact font files, hidden frames, component definitions, hover/animation prototypes, or unseen viewport designs. A supplied export may support implementation without providing those source details.

Visual-fidelity PASS requires a real rendered implementation comparison against an authoritative reference at a matching or explicitly normalized route/state/viewport. Do not invent a numeric fidelity percentage from static reasoning.

## GitHub adaptation

Treat GitHub access as capability-detected, not automatically read/write.

In standard ChatGPT, the built-in GitHub app may expose repository reading without exposing push, commit, branch, or PR-write actions. Do not assume repository write capability merely because GitHub is connected. When a write-capable GitHub action is actually exposed in the current surface, use it only within authorization and risk boundaries. Otherwise generate the patch/files and mark repository delivery `BLOCKED` or direct the user to Codex for write/push workflows.

When GitHub tools are available:

1. Fetch the actual repository/issue/PR/check state first.
2. Preserve repository instructions and current architecture.
3. Distinguish read capability from write capability.
4. Use write actions only when they are explicitly exposed and authorized.
5. Verify the resulting ref/file/PR/check state after writes when possible.
6. Never claim a commit/PR/CI result from an intended action alone.

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
