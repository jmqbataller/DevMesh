# DevMesh

**DevMesh** is an evidence-based AI software-engineering, design-to-code, greenfield website product-building, website-operations, and agency-operations orchestration framework for ChatGPT, Codex, and future adapters. It helps agents inspect, design, plan, build, diagnose, operate, monitor, verify, judge, recover, and deliver without turning assumptions into fake passes.

Developer: **John Mark Bataller**

DevMesh ships with:
- **Codex adapter** — plugin + Playwright MCP for coding-environment execution
- **ChatGPT adapter** — portable Agent Skills bundle that adapts to tools available in normal ChatGPT

## Download DevMesh for ChatGPT

[**Download `devmesh-chatgpt-v1.3.0.zip`**](https://github.com/jmqbataller/DevMesh/releases/download/v1.3.0/devmesh-chatgpt-v1.3.0.zip)

On a ChatGPT account/surface that supports uploaded Skills: open **Plugins → Skills → Create → Upload from your computer**, upload the ZIP, then start a new chat.

# DevMesh v1.3 — Design-to-Code Studio

v1.3 contains **111 composable skills** and makes screenshot/mockup/Figma/export/reference-driven implementation a first-class DevMesh specialization.

## Build from an approved visual reference

```text
DevMesh Design-to-Code Deep:
Use the supplied design as the authoritative visual reference.
Recreate it as a maintainable responsive website.

Analyze the page structure, visual hierarchy, typography,
spacing, colors, reusable components and responsive behavior.
Separate OBSERVED, INFERRED and UNKNOWN decisions.

Connect real backend/API/database behavior only where required.
Run Browser QA and compare the rendered implementation
against the reference when browser evidence is available.
Fix meaningful differences without altering the baseline.
```

Default lifecycle:

```text
reference intake
→ visual-reference-analyzer
→ design-token-extractor
→ responsive-layout-inference
→ sitemap-information-architecture when needed
→ ui-component-architecture
→ implementation / full-stack-build only as required
→ Browser QA
→ visual-regression + visual-fidelity-judge
→ maximum 3 visual repair rounds
→ accessibility / security / performance QA
→ DevMesh Judge
→ production deployment when authorized
```

### New v1.3 skills

- `design-to-code-studio` — screenshot/mockup/Figma/reference-to-code orchestrator
- `visual-reference-analyzer` — observed visual structure/assets/states plus explicit inference/unknown boundaries
- `design-token-extractor` — semantic typography/color/spacing/layout/control token extraction without false precision
- `responsive-layout-inference` — deliberate desktop/tablet/mobile decisions when not every viewport is supplied
- `visual-fidelity-judge` — rendered-reference comparison, prioritized visual findings, and bounded repair

DevMesh does **not** claim that a static screenshot proves hidden interactions, backend behavior, auth, data models, animation timing, or unseen mobile behavior. Visual conclusions are labeled `OBSERVED`, `INFERRED`, or `UNKNOWN`. Visual fidelity is `BLOCKED`/`NOT RUN` when a real rendered comparison cannot be performed, and numeric fidelity percentages are never invented.

See [`docs/DESIGN_TO_CODE.md`](docs/DESIGN_TO_CODE.md).

# DevMesh v1.2 — Website Product Builder

The v1.2 greenfield builder remains available and composes naturally with Design-to-Code when a supplied design is one input to a larger product.

## Build a website from scratch

```text
DevMesh Website Product Builder:
Build a complete working website from scratch.

Create the product contract, design system, sitemap,
UI component architecture and responsive frontend.
Add backend, API, database, auth and integrations only
where the product actually requires them.

Then implement SEO foundations, run QA,
judge the integrated result, and prepare production delivery.
```

Default lifecycle:

```text
requirements / product contract
→ design-system-architect
→ sitemap-information-architecture
→ ui-component-architecture
→ frontend implementation
→ backend/server when needed
→ api-contract when needed
→ database-architect when needed
→ integrations
→ technical SEO
→ Browser / accessibility / security / performance / network QA
→ DevMesh Judge
→ production deployment when authorized
→ handoff/report
```

The builder is scope-aware: a static/marketing/portfolio site does **not** automatically get a backend/database, while a SaaS, booking, quotation, inventory, CRM, e-commerce, membership, or real-estate product can compose the required backend/API/database/auth/integration playbooks.

See [`docs/WEBSITE_PRODUCT_BUILDER.md`](docs/WEBSITE_PRODUCT_BUILDER.md).

# DevMesh v1.1 — Agency Operations Control Center

The v1.1 agency stack remains available for multi-client / multi-site operations:

- `agency-operations-control-center`
- `multi-site-fleet-manager`
- `scheduled-site-health-monitor`
- `domain-ssl-expiry-monitor`
- `wordpress-update-wave-manager`
- `staging-production-manager`
- `website-change-timeline`
- `visual-history-screenshot-timeline`
- `plugin-vulnerability-maintenance-watch`
- `license-subscription-tracker`
- `client-access-inventory`
- `ticket-request-intake-agent`
- `sla-priority-engine`
- `lead-sla-monitor`
- `real-estate-crm-integration-specialist`
- `mls-provider-health-monitor`
- `consent-privacy-cookie-auditor`
- `accessibility-continuous-monitor`
- `content-qa-agent`
- `client-onboarding-agent`
- `client-offboarding-agent`

See [`docs/AGENCY_OPERATIONS.md`](docs/AGENCY_OPERATIONS.md).

# DevMesh v1.0 — Website Operations Specialist

The Website Operations stack remains available for hosting/DNS/SSL, WordPress migration, restore drills, SEO/Search Console, real-estate SEO, Core Web Vitals, analytics, email delivery, redirects, plugin/theme risk, WP-Cron, RESO schema/provider inspection, emergency recovery and client reporting.

See [`docs/WEBSITE_OPERATIONS.md`](docs/WEBSITE_OPERATIONS.md).

## Full-stack development

`design-to-code-studio` and `website-product-builder` compose the existing `full-stack-build` only when multiple application layers are genuinely required.

```text
Use DevMesh.
Build a working quotation website.
```

“Working” means integrated behavior when required: frontend, backend/server logic, API/server actions, persistence/migrations, validation/error states, auth boundaries, integrations, and representative end-to-end evidence.

A typical persisted verification journey is:

```text
open site
→ create/submit data
→ server validates
→ persist
→ read back
→ update
→ reload
→ confirm persistence
```

## WordPress Real Estate Specialist

DevMesh retains Site Health, plugin/theme conflict isolation, safe updates, WP-CLI, WordPress REST, IDX provider detection, WordPress↔MLS bridging, search/map QA, listing freshness, IDX/VOW/compliance monitoring, performance/security, lead-flow QA, and client handover.

## Real Estate IDX / MLS / RESO

DevMesh distinguishes IDX, VOW, participant feeds, syndication, and internal uses. RESO provides standards rather than MLS listing credentials. The applicable MLS/provider license remains authoritative for permitted fields, refresh requirements, attribution/disclaimers, and display restrictions.

The real-estate stack includes `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, `idx-compliance-review`, `reso-schema-drift-detector`, `reso-provider-capability-inspector`, and `mls-provider-health-monitor`.

DevMesh will not claim local IDX compliance if current applicable MLS/provider rules were not reviewed; that evidence remains `BLOCKED`.

See [`docs/REAL_ESTATE_IDX_MLS.md`](docs/REAL_ESTATE_IDX_MLS.md) and [`docs/WORDPRESS_REAL_ESTATE.md`](docs/WORDPRESS_REAL_ESTATE.md).

## Example: design-to-code + real estate

```text
DevMesh Design-to-Code:
Implement this supplied real-estate website design.
Preserve the visual system, then integrate the authorized IDX/MLS search.
Keep MLS credentials server-side.
Verify listing/search/lead behavior separately from visual fidelity.
```

## Example: complete custom website

```text
DevMesh Deep:
Build a professional working business website from scratch.

Requirements:
- premium responsive UI/UX
- clear sitemap and conversion flow
- reusable design system and component architecture
- frontend
- contact/lead workflow
- backend/API/database only if actually needed
- SEO foundations
- accessibility/security/performance QA
- Browser QA
- production-ready delivery

Do not use fake APIs or placeholder persistence.
```

## Example: full-stack product website

```text
DevMesh Website Product Builder + Deep:
Build a production-ready booking platform.

Include the design system, sitemap, component architecture,
frontend, server-side validation, API contracts,
database schema/migrations, authentication/authorization,
error states, SEO, QA and deployment verification.
```

## Agency command

```text
DevMesh Agency Deep:
Review all client websites.
Prioritize outages, SSL/domain expiry, WordPress errors,
security, failed backups, stale IDX/MLS feeds,
broken lead flows, CRM failures, SEO/accessibility issues,
and renewal risks.
```

## Emergency recovery

```text
DevMesh Emergency:
The WordPress website is down.

Diagnose DNS, SSL, CDN/proxy, hosting, PHP, database,
WordPress, plugins, theme, cache and recent changes.
Stabilize safely and prove recovery on affected journeys.
```

A homepage returning HTTP 200 alone is not considered full recovery.

## Mission Control

Mission Control provides dynamic task graphs, real parallel delegation when supported, confidence-aware diagnosis, adversarial review, change-impact mapping, eval/replay, architecture simulation, resource budgets, Incident Commander, and the evidence-first DevMesh Judge.

Real parallelism or independent judging is never claimed when the runtime does not provide it.

## Depth + resource modes

```text
DevMesh Quick + Eco
DevMesh Standard + Balanced   # defaults
DevMesh Deep + Max
```

Quick/Standard/Deep control engineering depth. Eco/Balanced/Max control orchestration resource intensity. Neither can bypass safety/evidence requirements.

## ChatGPT Adapter

The ChatGPT adapter lives at `adapters/chatgpt/devmesh-chatgpt/`. It does not assume normal ChatGPT has private Figma access, a writable workspace, shell, localhost, Git CLI, WP-CLI, WordPress admin, hosting/DNS/registrar dashboards, Search Console, analytics, SMTP/CRM visibility, backup systems, monitoring telemetry, Playwright, sub-agents, MLS credentials, or deployment credentials. Missing evidence remains `BLOCKED`/`NOT RUN`.

Build locally:

```bash
python scripts/build_chatgpt_adapter.py
```

Output: `dist/devmesh-chatgpt-v1.3.0.zip`.

## Codex Adapter

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

Start a new Codex thread/session after reinstall.

## Evidence states

DevMesh uses `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. Design-to-code visual fidelity, greenfield design/implementation, Browser QA, deployment, fleet health, monitoring, renewals, access, SLA, CRM/lead delivery, MLS-provider health, privacy/legal claims, WordPress, CI and production status require corresponding evidence.

## Public distribution status

- GitHub source: public
- GitHub Release ZIP: automated
- Manual ChatGPT Skill upload: available on eligible ChatGPT accounts/surfaces
- OpenAI Plugin Directory listing: submission package prepared; publication still requires publisher verification, OpenAI review, approval, and Publish

## Development validation

```bash
python tests/validate_devmesh.py
python tests/test_routing_contract.py
python tests/test_feature_contracts.py
python tests/test_chatgpt_adapter.py
python tests/test_plugin_submission_pack.py
```

## Current platform support

| Platform | Status |
|---|---|
| Codex | **v1.3 supported** |
| ChatGPT | **v1.3 portable Agent Skills adapter** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

## License

MIT
