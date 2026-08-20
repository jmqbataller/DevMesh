# DevMesh GPT Configuration

## Name

DevMesh

## Description

Evidence-first AI software engineering, design-to-code, website product building, debugging, WordPress and website operations, QA, and production-delivery assistant with artifact-aware output.

## Recommended capabilities

Enable only what is available and useful on the target GPT surface:

- Web search: ON for current public research and documentation.
- Code Interpreter & Data Analysis: ON when code execution, file generation, archives, calculations, or structured data work is needed.
- Image generation: Optional.
- Canvas / document editing capability: Optional when available.
- Apps: Optional for connected services such as GitHub or other workspace tools.
- Actions: Optional only when you provide your own external API schema.

Do not configure Apps and Actions at the same time. Pick the integration model required by the deployment.

## Conversation starters

- DevMesh Design-to-Code: Recreate this supplied design as a responsive website and verify what you can.
- DevMesh Website Product Builder: Build a complete business website from requirements through QA.
- DevMesh Debug: Diagnose this bug, prove the root cause, implement a fix, and retest.
- DevMesh Artifact: Turn this idea into an interactive website or app artifact if this surface supports it.
- DevMesh Website Ops: Audit this WordPress or business website and give me an evidence-based action plan.
- DevMesh GitHub: Review this repository and propose the safest implementation plan before changing code.

## Knowledge

Do not upload all individual skill files one-by-one. Run:

```bash
python scripts/build_gpts_kit.py
```

Then upload every generated file under `knowledge/`.

## Behavior source

Paste `INSTRUCTIONS.md` into the GPT Instructions field. Knowledge files are reference material; rules and workflow behavior belong in Instructions.
