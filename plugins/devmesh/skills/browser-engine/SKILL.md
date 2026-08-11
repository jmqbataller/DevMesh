---
name: browser-engine
description: Use when DevMesh needs real browser control for launching a web app, navigating rendered pages, inspecting runtime evidence, interacting with UI, changing viewports, and capturing screenshots through Playwright or an equivalent browser surface.
---

# Browser Engine

This skill provides the execution layer for rendered browser evidence. `browser-qa` owns the QA methodology; `browser-engine` owns reliable browser control.

## Preferred engine

DevMesh bundles a Playwright MCP server through `.mcp.json`. Prefer the native `playwright` MCP tools when they are available.

If the MCP server is unavailable:

1. Detect whether the active environment already exposes another real browser automation surface.
2. If the project already uses Playwright tests/CLI, use that existing setup when appropriate.
3. Do not silently install unrelated browser frameworks into the target project.
4. If no browser-capable surface exists, report the missing capability to `browser-qa` and fall back to static checks only.

## Launch sequence

1. Inspect package scripts, framework config, README, and existing development commands.
2. Choose the project's intended dev/preview command instead of inventing one.
3. Start the app without blocking the agent's control loop.
4. Wait for an actual reachable URL and meaningful readiness.
5. Record the command, URL, and process details needed to stop/restart it safely.

Do not deploy to production merely to obtain browser evidence.

## Browser session rules

- Prefer an isolated browser profile for reproducible QA.
- Do not rely on the user's personal cookies/session unless the user explicitly requested testing an authenticated state and the environment safely supports it.
- Do not enter secrets into browser forms unless the user explicitly provided and authorized their use.
- Stay within the requested application/domain unless a tested user journey legitimately requires another origin.

## Core operations

Use the browser surface to perform the smallest set of operations that proves the requested behavior:

- navigate to routes
- inspect accessibility/DOM snapshots
- read visible states
- click, type, select, submit, hover, focus, and press keys
- change viewport or emulate representative device sizes when supported
- inspect console/runtime messages
- inspect failed or relevant network activity when supported
- capture screenshots
- collect additional browser artifacts such as traces when the available tooling supports them

## Viewport baseline

When responsive behavior matters, prefer representative sizes such as:

- desktop: approximately 1440x900
- tablet: approximately 768x1024 when the product has tablet behavior
- phone: approximately 390x844

These are evidence points, not a substitute for fluid-layout reasoning. Add edge widths when a defect appears near a breakpoint.

## Screenshot discipline

Capture screenshots for meaningful states, not every click. Typical evidence:

- initial desktop state
- representative mobile state
- a state related to a reported defect
- error/empty/success state when materially relevant
- before/after evidence for a visual fix when useful

Store artifacts under the QA report directory when `qa-reporting` is active.

## Runtime evidence

Distinguish:

- application console errors
- expected framework development warnings
- browser/tooling noise
- third-party errors unrelated to the requested journey

Only escalate evidence that affects the tested product or reveals a credible defect.

## Failure recovery

When the app or browser session fails:

1. Determine whether the failure belongs to the app, local server, browser engine, missing dependency, or environment.
2. Retry only when the failure is plausibly transient.
3. Do not loop indefinitely.
4. After two engine-level retries, report the blocker and continue with whatever static QA remains possible.

## Handoff to Browser QA

Return evidence containing:

- launch command and URL
- browser engine used
- routes opened
- viewport/device coverage
- interactions performed
- console/network observations
- screenshot/artifact paths when available
- engine limitations or failures

Never convert missing browser evidence into a pass.
