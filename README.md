# DevMesh

**DevMesh** is an evidence-based AI software-engineering orchestration framework for ChatGPT, Codex, and future adapters. It helps agents inspect, plan, build, diagnose, verify, judge, repair, and deliver without turning assumptions into fake passes.

DevMesh ships with:
- **Codex adapter** — plugin + Playwright MCP for coding-environment execution
- **ChatGPT adapter** — portable Agent Skills bundle that adapts to tools available in normal ChatGPT

## Download DevMesh for ChatGPT

[**Download `devmesh-chatgpt-v0.9.0.zip`**](https://github.com/jmqbataller/DevMesh/releases/download/v0.9.0/devmesh-chatgpt-v0.9.0.zip)

On a ChatGPT account/surface that supports uploaded Skills: open **Plugins → Skills → Create → Upload from your computer**, upload the ZIP, then start a new chat.

## DevMesh v0.9 — WordPress Real Estate Specialist

v0.9 contains **65 composable skills**. The new WordPress real-estate stack adds:

- `wordpress-real-estate-specialist` — top-level WordPress + real-estate orchestration
- `wordpress-site-doctor` — Site Health, PHP/server/database, themes/plugins, cron, REST, permalinks and configuration
- `wordpress-plugin-conflict-detective` — evidence-based plugin/theme conflict isolation
- `wordpress-safe-update-manager` — backup/staging/update/rollback workflow
- `wp-cli-operator` — risk-aware WP-CLI operations
- `wordpress-rest-api-integrator` — custom content/routes/auth/service integration
- `idx-provider-detector` — identify IDX vendor, MLS/provider, transport, render and sync architecture
- `wordpress-idx-bridge` — secure WordPress ↔ IDX/MLS/RESO boundary
- `idx-search-qa` — browser QA for filters, sort, pagination, maps, cards, details and mobile
- `listing-freshness-monitor` — sync/query age, cron/provider/cache/index failure diagnosis
- `idx-compliance-monitor` — ongoing display-restriction monitoring
- `idx-vow-mode-detector` — IDX vs VOW vs hybrid classification
- `wordpress-performance-doctor` — measured WordPress/IDX performance diagnosis
- `wordpress-security-specialist` — WordPress-specific hardening + MLS credential boundaries
- `wordpress-lead-flow-qa` — inquiry/showing/contact downstream delivery verification
- `wordpress-client-handover` — secret-free operational handover

The v0.8 real-estate stack remains available: `real-estate-idx-mls`, `reso-web-api`, `listing-sync-search`, and `idx-compliance-review`.

### Website Specialist example

```text
DevMesh Deep:
Act as a WordPress Real Estate Website Specialist.

Audit this website end-to-end:
- WordPress core, PHP, database, Site Health, theme/child theme and plugins
- REST API, WP-Cron, permalinks and configuration
- IDX provider and MLS/RESO architecture
- listing freshness and search/filter/map/detail behavior
- IDX vs VOW and public display restrictions
- performance, security and accessibility
- inquiry/showing/contact lead delivery

Find the real root cause before fixing issues.
Fix safe issues, run Browser QA, retest affected workflows,
and prepare a secret-free client handover.
Do not claim a check passed without evidence.
```

### WordPress maintenance examples

```text
Use DevMesh.
Diagnose this WordPress plugin conflict, prove the root cause, fix it safely, and retest.
```

```text
Use DevMesh.
Update this WordPress site safely using staging/rollback evidence and retest IDX search and lead forms.
```

```text
Use DevMesh.
Inspect this site with WP-CLI, but do not make destructive changes without authorization.
```

## Real Estate IDX / MLS

DevMesh distinguishes IDX, VOW, participant feeds, syndication, and internal uses. RESO provides standards rather than MLS listing credentials. The applicable MLS/provider license remains authoritative for permitted fields, refresh requirements, attribution/disclaimers, and display restrictions.

A typical WordPress IDX workflow is:

```text
WordPress Site Doctor
→ IDX provider detection
→ IDX vs VOW classification
→ RESO/provider metadata and license review
→ WordPress ↔ MLS bridge
→ listing sync/freshness when replication is licensed
→ property search/filter/map/detail implementation
→ security/performance/accessibility
→ IDX search Browser QA
→ compliance review/monitoring
→ lead-flow QA
→ DevMesh Judge
→ client handover
```

DevMesh will not claim local IDX compliance if the current applicable MLS/provider rules were not reviewed; that evidence remains `BLOCKED`.

See [`docs/REAL_ESTATE_IDX_MLS.md`](docs/REAL_ESTATE_IDX_MLS.md) and [`docs/WORDPRESS_REAL_ESTATE.md`](docs/WORDPRESS_REAL_ESTATE.md).

## Mission Control

Mission Control still provides dynamic task graphs, real parallel delegation when supported, confidence-aware diagnosis, adversarial review, change-impact mapping, eval/replay, architecture simulation, resource budgets, Incident Commander, and the evidence-first DevMesh Judge.

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

The ChatGPT adapter lives at `adapters/chatgpt/devmesh-chatgpt/`. It does not assume normal ChatGPT has a shell, localhost, Git CLI, WP-CLI, WordPress admin, Playwright, sub-agents, MLS credentials, CRM/email visibility, or deployment credentials. Missing evidence remains `BLOCKED`/`NOT RUN`.

Build locally:

```bash
python scripts/build_chatgpt_adapter.py
```

Output: `dist/devmesh-chatgpt-v0.9.0.zip`.

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

DevMesh uses `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`, and `N/A`. WordPress health/update, browser, CI, production, lead-delivery, parallel-agent, independent-judge and IDX-compliance claims require corresponding evidence.

## Public distribution status

- GitHub source: public
- GitHub Release ZIP: automated
- Manual ChatGPT Skill upload: available on eligible ChatGPT accounts/surfaces
- OpenAI Plugin Directory listing: submission package prepared; publication still requires publisher verification, OpenAI review, approval, and Publish

Developer: **John Mark Bataller**

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
| Codex | **v0.9 supported** |
| ChatGPT | **v0.9 portable Agent Skills adapter** |
| Claude Code | Planned adapter |
| Gemini CLI | Planned adapter |
| Cursor | Planned adapter |
| GitHub Copilot | Planned adapter |

## License

MIT
