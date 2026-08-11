---
name: resource-budget
description: Use alongside Quick/Standard/Deep to choose Eco, Balanced, or Max resource intensity for agent parallelism, tool calls, replay breadth, and review depth without weakening safety or evidence requirements.
---

# Resource Budget

Resource budget is orthogonal to execution depth.

Examples:
- `DevMesh Deep + Eco` — deep required engineering gates, conservative agent/tool usage
- `DevMesh Standard + Max` — normal scope with more parallel/reviewer capacity where supported

## Modes

### Eco
- minimize parallel workers
- prefer focused searches/tests before broad scans
- reuse existing evidence safely
- smaller eval/replay sample when not release-critical

### Balanced
Default. Use proportionate tools, reviewers, browser traces, and eval breadth.

### Max
- use independent/parallel workers when genuinely useful and supported
- broader replay/verification on high-value work
- stronger reviewer diversity for consequential decisions

## Non-negotiable boundaries

Resource budget never:
- skips a safety-critical gate
- converts `BLOCKED` into `PASS`
- authorizes external spending, paid infrastructure, or destructive actions
- selects a specific model/tool that the runtime does not expose
- increases concurrency beyond runtime/workspace limits

If the host does not expose model selection, token budgets, or agent controls, treat Eco/Balanced/Max as orchestration guidance only and state what could not be controlled.
