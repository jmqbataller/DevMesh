# DevMesh Design-to-Code Studio

DevMesh v1.3 adds a first-class **Design-to-Code Studio** for turning supplied screenshots, mockups, Figma frames/exports, PDFs, and existing rendered UI references into maintainable responsive website/application code.

The goal is not screenshot tracing. The goal is to preserve the intended visual hierarchy and product behavior while producing a real implementation that can be tested, maintained, extended, and integrated with the rest of DevMesh.

## Core workflow

```text
reference intake
→ visual-reference-analyzer
→ design-token-extractor
→ responsive-layout-inference
→ sitemap-information-architecture when route scope matters
→ ui-component-architecture
→ implementation / full-stack-build only as required
→ browser-qa
→ visual-regression + visual-fidelity-judge
→ bounded visual repair
→ accessibility / security / performance QA
→ devmesh-judge
→ production-deployment when authorized
```

## Evidence labels

Design references are incomplete product specifications. DevMesh labels material conclusions as:

- `OBSERVED` — directly visible or explicitly supplied
- `INFERRED` — an implementation decision needed to complete the product
- `UNKNOWN` — cannot be determined from the available reference

Examples:

```text
Header layout: OBSERVED
Desktop card grid: OBSERVED
Mobile menu behavior: INFERRED unless a mobile frame is supplied
Hover animation timing: UNKNOWN unless demonstrated/specified
Backend validation rules: UNKNOWN from a static screenshot
```

Static pixels never prove hidden interactions, backend/API behavior, authentication, database design, error handling, routing destinations, animation timing, or unseen responsive behavior.

## Skills

### `design-to-code-studio`

Top-level orchestrator for reference-driven implementation and verification.

### `visual-reference-analyzer`

Maps page hierarchy, layout, visual rules, components, supplied assets, visible states, and evidence gaps.

### `design-token-extractor`

Builds a maintainable semantic token system from repeated visual evidence instead of scattering arbitrary pixel values through the implementation.

### `responsive-layout-inference`

Defines explicit desktop/tablet/mobile behavior when all viewport references are not available. Unseen behavior is labeled as inferred rather than pretending the original designer specified it.

### `visual-fidelity-judge`

Compares an authoritative reference with a real rendered implementation at matching/normalized viewports. It prioritizes meaningful discrepancies and drives a maximum of **3 visual repair rounds**.

The judge never invents percentage scores. Numeric fidelity is allowed only when a repeatable measurement method actually produced it.

## Visual fidelity vs visual regression

`visual-fidelity-judge` answers:

> Does the new implementation match the supplied external design reference closely enough?

`visual-regression` answers:

> Did a previously approved implementation change unexpectedly?

Neither baseline may be silently overwritten to hide a mismatch/regression.

## Greenfield composition

When the supplied design is only part of a new product, compose Design-to-Code with `website-product-builder`:

```text
product contract
→ supplied visual reference
→ Design-to-Code Studio
→ sitemap/component architecture
→ frontend
→ backend/API/database only where required
→ SEO
→ QA
→ deployment
```

## Full-stack boundary

A beautiful match is not a working product by itself. If the request requires forms, auth, persistence, APIs, payments, CRM, IDX/MLS, admin operations, or other server behavior, route those requirements through the existing DevMesh full-stack and specialist playbooks.

Do not use fake APIs or placeholder persistence to call the result working.

## ChatGPT capability adaptation

ChatGPT can analyze images/screenshots that are actually supplied to the conversation. Access to a private Figma file, local repository, browser-controlled localhost, fonts/assets, or production environment must not be assumed.

When browser/render comparison is unavailable:

```text
Reference analysis: PASS (if the supplied reference was actually inspected)
Source implementation: PASS / BLOCKED / NOT RUN based on available writable tools
Browser QA: BLOCKED or NOT RUN
Visual fidelity: BLOCKED or NOT RUN
Deployment: BLOCKED or NOT RUN
```

Public web browsing is not equivalent to access to a private design source and is not rendered Browser QA against a local/private implementation.

## Example — screenshot to website

```text
DevMesh Design-to-Code Deep:
Use the supplied homepage screenshot as the authoritative visual reference.

Recreate it as a production-quality responsive website.
Analyze the layout, typography, spacing, colors, reusable components,
and responsive behavior.

Separate OBSERVED, INFERRED and UNKNOWN decisions.
Connect real backend/API/database behavior only where required.
Run Browser QA and compare the rendered implementation against the reference.
Fix meaningful differences without altering the reference baseline.
```

## Example — real estate design

```text
DevMesh Design-to-Code:
Implement this supplied real-estate website design.
Preserve the visual system, then integrate the authorized IDX/MLS search.
Do not expose MLS credentials or let the integration overwrite the design system.
Verify listing/search/lead behavior separately from visual fidelity.
```

## Example — existing site redesign

```text
DevMesh Design-to-Code:
Use this approved redesign as the visual target for the existing website.
Preserve working backend behavior and existing data contracts.
Replace only the necessary UI architecture and verify regressions.
```
