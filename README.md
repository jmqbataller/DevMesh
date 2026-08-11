# DevMesh

**DevMesh** is an evidence-based AI software-engineering and website-operations orchestration framework for ChatGPT, Codex, and future adapters. It helps agents inspect, plan, build, diagnose, operate, verify, judge, recover, and deliver without turning assumptions into fake passes.

Developer: **John Mark Bataller**

DevMesh ships with:
- **Codex adapter** — plugin + Playwright MCP for coding-environment execution
- **ChatGPT adapter** — portable Agent Skills bundle that adapts to tools available in normal ChatGPT

## Download DevMesh for ChatGPT

[**Download `devmesh-chatgpt-v1.0.0.zip`**](https://github.com/jmqbataller/DevMesh/releases/download/v1.0.0/devmesh-chatgpt-v1.0.0.zip)

On a ChatGPT account/surface that supports uploaded Skills: open **Plugins → Skills → Create → Upload from your computer**, upload the ZIP, then start a new chat.

# DevMesh v1.0 — Website Operations Specialist

v1.0 contains **81 composable skills** and turns DevMesh into a broader Website Specialist / Site Operations framework.

## Client Site Autopilot

```text
DevMesh Website Specialist:
Take over this client website.

Audit hosting, DNS, SSL, WordPress, backups, security,
performance, SEO, analytics, forms/email, IDX/MLS/RESO,
listing freshness, leads and operational reliability.

Fix safe issues, verify affected journeys,
and prepare a professional client report.
```

Typical flow:

```text
inventory
→ hosting / DNS / SSL
→ WordPress Site Health
→ backup / restore readiness
→ plugin/theme risk
→ safe updates when authorized
→ security
→ performance / Core Web Vitals
→ SEO / Search Console
→ analytics / conversions
→ forms / email delivery
→ broken links / redirects
→ IDX / MLS / RESO when present
→ WP-Cron reliability
→ Browser QA / lead QA
→ client monthly report
```

## New v1.0 skills

- `website-operations-specialist` — Client Site Autopilot and broad Website Specialist orchestration
- `hosting-dns-ssl-doctor` — nameservers, DNS, SSL/TLS, HTTPS, redirects, CDN/proxy and origin diagnosis
- `wordpress-migration-specialist` — hosting/domain/staging migrations with rollback and Browser QA
- `backup-restore-drill` — backup completeness plus safe restore verification
- `seo-search-console-specialist` — technical SEO, crawl/index and Search Console evidence
- `real-estate-seo-specialist` — IDX/listing/community URL architecture and thin/duplicate controls
- `core-web-vitals-diagnoser` — measured LCP/INP/CLS diagnosis
- `analytics-conversion-qa` — event and downstream conversion verification
- `email-deliverability-doctor` — SMTP/SPF/DKIM/DMARC/form/CRM delivery-chain diagnosis
- `broken-link-redirect-manager` — 404/link integrity and safe redirects
- `plugin-theme-risk-intelligence` — plugin/theme criticality, compatibility and removal risk
- `wp-cron-reliability-doctor` — missed/duplicate/stuck WordPress scheduled jobs
- `reso-schema-drift-detector` — RESO/OData metadata/resource/field/lookup drift detection
- `reso-provider-capability-inspector` — provider capability evidence vs licensed data-use rights
- `client-monthly-website-report` — evidence-based client-facing operational reports
- `website-emergency-recovery` — outage triage from DNS/SSL through hosting/runtime/WordPress and verified recovery

See [`docs/WEBSITE_OPERATIONS.md`](docs/WEBSITE_OPERATIONS.md).

## WordPress Real Estate Specialist

The v0.9 stack remains available:

- `wordpress-real-estate-specialist`
- `wordpress-site-doctor`
- `wordpress-plugin-conflict-detective`
- `wordpress-safe-update-manager`
- `wp-cli-operator`
- `wordpress-rest-api-integrator`
- `idx-provider-detector`
- `wordpress-idx-bridge`
- `idx-search-qa`
- `listing-freshness-monitor`
- `idx-compliance-monitor`
- `idx-vow-mode-detector`
- `wordpress-performance-doctor`
- `wordpress-security-specialist`
- `wordpress-lead-flow-qa`
- `wordpress-client-handover`

## Real Estate IDX / MLS / RESO

DevMesh distinguishes IDX, VOW, participant feeds, syndication, and internal uses. RESO provides standards rather than MLS listing credentials. The applicable MLS/provider license remains authoritative for permitted fields, refresh requirements, attribution/disclaimers, and display restrictions.

The real-estate stack includes `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, `idx-compliance-review`, plus v1.0 `reso-schema-drift-detector` and `reso-provider-capability-inspector`.

DevMesh will not claim local IDX compliance if current applicable MLS/provider rules were not reviewed; that evidence remains `BLOCKED`.

See [`docs/REAL_ESTATE_IDX_MLS.md`](docs/REAL_ESTATE_IDX_MLS.md) and [`docs/WORDPRESS_REAL_ESTATE.md`](docs/WORDPRESS_REAL_ESTATE.md).

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

```text
DevMesh Mission Control:
Build a production-ready product and judge the integrated result.
```

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

The ChatGPT adapter lives at `adapters/chatgpt/devmesh-chatgpt/`. It does not assume normal ChatGPT has a shell, localhost, Git CLI, WP-CLI, WordPress admin, hosting/DNS dashboards, Search Console, analytics, SMTP/CRM visibility, backup systems, Playwright, sub-agents, MLS credentials, or deployment credentials. Missing evidence remains `BLOCKED`/`NOT RUN`.

Build locally:

```bash
python scripts/build_chatgpt_adapter.py
```

Output: `dist/devmesh-chatgpt-v1.0.0.zip`.

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

DevMesh uses `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. Hosting, restore, SEO/index, analytics, email delivery, WordPress, browser, CI, production, lead-delivery, parallel-agent, independent-judge and IDX-compliance claims require corresponding evidence.

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
| Codex | **v1.0 supported** |
| ChatGPT | **v1.0 portable Agent Skills adapter** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

## License

MIT
