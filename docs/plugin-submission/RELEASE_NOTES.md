# DevMesh v0.6.0 — Plugin Submission Release Notes

Initial public Plugin Directory submission.

DevMesh is a skills-only software engineering workflow plugin that packages reusable workflows for planning, full-stack product construction, debugging, database/API design, QA, security/accessibility/performance review, CI diagnosis, code review, and delivery.

This initial submission includes:

- the portable ChatGPT Agent Skill adapter;
- 33 shared DevMesh engineering playbooks bundled for portable use;
- Quick, Standard, and Deep execution modes;
- one-prompt full-stack workflow behavior;
- explicit evidence states: `PASS`, `FAIL`, `FIXED`, `BLOCKED`, and `NOT RUN`;
- tool-adaptation rules so ChatGPT does not assume local shell, browser automation, Git write access, or deployment capabilities that are not actually available;
- secret-handling, risk, and false-verification safeguards.

The skills-only submission does not require an MCP server, external DevMesh account, DevMesh-hosted backend, OAuth flow, or reviewer credentials.

Reviewer note: DevMesh intentionally distinguishes workflow guidance from executed evidence. A task may be implemented while runtime, browser, CI, or deployment verification remains `NOT RUN` or `BLOCKED` when those execution surfaces are unavailable.
