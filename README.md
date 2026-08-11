# DevMesh

**DevMesh** is an evidence-based AI software-engineering, website-operations, and agency-operations orchestration framework for ChatGPT, Codex, and future adapters. It helps agents inspect, plan, build, diagnose, operate, monitor, verify, judge, recover, and deliver without turning assumptions into fake passes.

Developer: **John Mark Bataller**

DevMesh ships with:
- **Codex adapter** — plugin + Playwright MCP for coding-environment execution
- **ChatGPT adapter** — portable Agent Skills bundle that adapts to tools available in normal ChatGPT

## Download DevMesh for ChatGPT

[**Download `devmesh-chatgpt-v1.1.0.zip`**](https://github.com/jmqbataller/DevMesh/releases/download/v1.1.0/devmesh-chatgpt-v1.1.0.zip)

On a ChatGPT account/surface that supports uploaded Skills: open **Plugins → Skills → Create → Upload from your computer**, upload the ZIP, then start a new chat.

# DevMesh v1.1 — Agency Operations Control Center

v1.1 contains **102 composable skills** and extends v1.0 Website Operations into multi-client / multi-site agency operations.

## Agency command

```text
DevMesh Agency Deep:
Review all client websites.

Prioritize outages, SSL/domain expiry, WordPress errors,
security, failed backups, stale IDX/MLS feeds,
broken lead flows, CRM failures, SEO/accessibility issues,
and renewal risks.

Create a site-specific maintenance queue with evidence,
SLAs, blockers, and client-ready reporting.
```

Typical agency loop:

```text
client onboarding + access inventory
→ multi-site fleet health
→ scheduled checks
→ domain / SSL expiry
→ tickets + SLA priority
→ site-specific Website/WordPress/IDX specialists
→ staged update waves / staging→production
→ change + screenshot history
→ plugin vulnerability maintenance watch
→ license/subscription renewals
→ lead SLA + CRM + MLS provider health
→ privacy/cookies + accessibility + content QA
→ client monthly reporting
→ safe client offboarding when needed
```

## New v1.1 skills

- `agency-operations-control-center` — top-level multi-client agency orchestrator
- `multi-site-fleet-manager` — site-specific portfolio health and maintenance prioritization
- `scheduled-site-health-monitor` — daily/weekly/monthly monitoring contracts and execution evidence
- `domain-ssl-expiry-monitor` — registrar/domain and TLS expiry/change monitoring
- `wordpress-update-wave-manager` — canary/staging update waves with stop-on-failure rollout
- `staging-production-manager` — safe environment comparison and production promotion
- `website-change-timeline` — evidence-backed change/deploy/update history
- `visual-history-screenshot-timeline` — timestamped browser snapshots and visual change history
- `plugin-vulnerability-maintenance-watch` — verified advisory + fleet exposure + update planning
- `license-subscription-tracker` — renewal/entitlement tracking without storing credentials/payment secrets
- `client-access-inventory` — operational capability/role inventory without secret values
- `ticket-request-intake-agent` — structured client request intake without inventing root cause
- `sla-priority-engine` — P1/P2/P3/P4 impact routing using actual client SLA when available
- `lead-sla-monitor` — lead handoff latency from site through email/webhook/CRM where observable
- `real-estate-crm-integration-specialist` — vendor-neutral CRM/webhook/API/email lead integration diagnosis
- `mls-provider-health-monitor` — upstream provider vs local IDX/MLS failure separation
- `consent-privacy-cookie-auditor` — technical consent/cookie/data-flow audit without false legal certification
- `accessibility-continuous-monitor` — release-by-release accessibility regression tracking
- `content-qa-agent` — placeholder/contact/CTA/content consistency QA with authoritative-source safeguards
- `client-onboarding-agent` — secret-free client baseline, access gaps, stack map and initial queue
- `client-offboarding-agent` — ownership-preserving handover/revocation/transfer workflow

See [`docs/AGENCY_OPERATIONS.md`](docs/AGENCY_OPERATIONS.md).

# DevMesh v1.0 — Website Operations Specialist

The v1.0 Website Operations stack remains available:

- `website-operations-specialist`
- `hosting-dns-ssl-doctor`
- `wordpress-migration-specialist`
- `backup-restore-drill`
- `seo-search-console-specialist`
- `real-estate-seo-specialist`
- `core-web-vitals-diagnoser`
- `analytics-conversion-qa`
- `email-deliverability-doctor`
- `broken-link-redirect-manager`
- `plugin-theme-risk-intelligence`
- `wp-cron-reliability-doctor`
- `reso-schema-drift-detector`
- `reso-provider-capability-inspector`
- `client-monthly-website-report`
- `website-emergency-recovery`

See [`docs/WEBSITE_OPERATIONS.md`](docs/WEBSITE_OPERATIONS.md).

## WordPress Real Estate Specialist

DevMesh retains Site Health, plugin/theme conflict isolation, safe updates, WP-CLI, WordPress REST, IDX provider detection, WordPress↔MLS bridging, search/map QA, listing freshness, IDX/VOW/compliance monitoring, performance/security, lead-flow QA, and client handover.

## Real Estate IDX / MLS / RESO

DevMesh distinguishes IDX, VOW, participant feeds, syndication, and internal uses. RESO provides standards rather than MLS listing credentials. The applicable MLS/provider license remains authoritative for permitted fields, refresh requirements, attribution/disclaimers, and display restrictions.

The real-estate stack includes `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, `idx-compliance-review`, `reso-schema-drift-detector`, `reso-provider-capability-inspector`, and v1.1 `mls-provider-health-monitor`.

DevMesh will not claim local IDX compliance if current applicable MLS/provider rules were not reviewed; that evidence remains `BLOCKED`.

See [`docs/REAL_ESTATE_IDX_MLS.md`](docs/REAL_ESTATE_IDX_MLS.md) and [`docs/WORDPRESS_REAL_ESTATE.md`](docs/WORDPRESS_REAL_ESTATE.md).

## Client onboarding example

```text
DevMesh Agency:
Onboard this client website.

Create a secret-free inventory of hosting, DNS, WordPress,
backups, analytics, Search Console, forms/email, IDX/MLS,
CRM, renewals, current issues, access gaps,
baseline screenshots, and an initial maintenance queue.
```

## Fleet monitoring example

```text
DevMesh Agency:
Monitor this WordPress real-estate fleet for:
- uptime and HTTPS
- domain/SSL expiry
- plugin/theme risk
- backups
- IDX/MLS freshness and provider health
- lead delivery and CRM latency
- accessibility/content regressions
- license renewals

Do not claim a monitor is running unless a real scheduler exists.
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

## One prompt → working product

```text
Use DevMesh.
Build a working quotation website.
```

“Working” means integrated behavior when required: frontend, backend/server logic, API/server actions, persistence/migrations, validation/error states, auth boundaries when needed, and end-to-end evidence.

## Depth + resource modes

```text
DevMesh Quick + Eco
DevMesh Standard + Balanced   # defaults
DevMesh Deep + Max
```

Quick/Standard/Deep control engineering depth. Eco/Balanced/Max control orchestration resource intensity. Neither can bypass safety/evidence requirements.

## ChatGPT Adapter

The ChatGPT adapter lives at `adapters/chatgpt/devmesh-chatgpt/`. It does not assume normal ChatGPT has a shell, localhost, Git CLI, WP-CLI, WordPress admin, hosting/DNS/registrar dashboards, Search Console, analytics, SMTP/CRM visibility, backup systems, monitoring telemetry, Playwright, sub-agents, MLS credentials, or deployment credentials. Missing evidence remains `BLOCKED`/`NOT RUN`.

Build locally:

```bash
python scripts/build_chatgpt_adapter.py
```

Output: `dist/devmesh-chatgpt-v1.1.0.zip`.

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

DevMesh uses `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. Fleet health, monitoring, renewals, access, SLA, CRM/lead delivery, MLS-provider health, privacy/legal claims, WordPress, browser, CI and production status require corresponding evidence.

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
| Codex | **v1.1 supported** |
| ChatGPT | **v1.1 portable Agent Skills adapter** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

## License

MIT
