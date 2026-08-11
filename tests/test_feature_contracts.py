#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT/'plugins'/'devmesh'

def text(name: str) -> str:
    return (PLUGIN/'skills'/name/'SKILL.md').read_text(encoding='utf-8')

def has(name: str, *phrases: str) -> None:
    body = text(name)
    for phrase in phrases:
        assert phrase in body, f'{name} missing {phrase!r}'

mcp = json.loads((PLUGIN/'.mcp.json').read_text(encoding='utf-8'))
playwright = mcp['mcpServers']['playwright']
assert playwright['command'] in {'npx','npx.cmd'}
assert '@playwright/mcp@latest' in playwright['args']
assert '--isolated' in playwright['args']

# v1.3 Design-to-Code Studio
has('design-to-code-studio','visual-reference-analyzer','design-token-extractor','responsive-layout-inference','visual-fidelity-judge','OBSERVED','INFERRED','UNKNOWN','Maximum **3 visual repair rounds**','source-code similarity is not a substitute for rendered comparison')
has('visual-reference-analyzer','OBSERVED','INFERRED','UNKNOWN','static frame does not prove','exact assets','Do not claim the whole design was analyzed')
has('design-token-extractor','semantic color roles','smallest useful scale','false precision','INFERRED','accessibility-review')
has('responsive-layout-inference','implementation decision, not an observed fact','content-driven breakpoints','no horizontal overflow','touch targets','OBSERVED','INFERRED','UNKNOWN')
has('visual-fidelity-judge','authoritative visual reference','Never invent a fidelity score','Maximum **3 visual repair rounds**','NOT RUN','visual-regression','Never silently overwrite')

# v1.2 Website Product Builder
has('website-product-builder','design-system-architect','sitemap-information-architecture','ui-component-architecture','frontend implementation','backend/server logic when needed','api-contract','database-architect','seo-search-console-specialist','browser-qa','production-deployment','BLOCKED')
has('design-system-architect','typography roles','spacing/layout rhythm','color roles/tokens','focus-visible','prefers-reduced-motion','implementation-oriented design-system contract')
has('sitemap-information-architecture','page/route inventory','primary and secondary navigation','dynamic route families','indexing intent','dead ends','architecture contract')
has('ui-component-architecture','stateful vs presentational responsibilities','data-fetching/server boundaries','loading, skeleton, empty, error and success states','responsive variants','premature abstraction')

# v1.1 Agency Operations Control Center
has('agency-operations-control-center','multi-site-fleet-manager','scheduled-site-health-monitor','wordpress-update-wave-manager','ticket-request-intake-agent','sla-priority-engine','lead-sla-monitor','client-onboarding-agent','client-offboarding-agent')
has('multi-site-fleet-manager','independent operational boundary','Healthy','Warning','Critical','BLOCKED')
has('scheduled-site-health-monitor','monitoring plan is not a running monitor','daily','weekly','monthly','NOT RUN')
has('domain-ssl-expiry-monitor','certificate validity','domain renewal','30/14/7 days','registrar','BLOCKED')
has('wordpress-update-wave-manager','representative staging/canary wave','STOP rollout','rollback','per-site')
has('staging-production-manager','Staging and production','robots/noindex','analytics','Production PASS')
has('website-change-timeline','Correlation is a lead, not proof','recent changes','systematic-debugging','Never store secrets')
has('visual-history-screenshot-timeline','screenshot is evidence','never replace old snapshots','browser-control','visual-regression','BLOCKED')
has('plugin-vulnerability-maintenance-watch','verified advisory/vendor evidence','affected sites','business criticality','mass-disable')
has('license-subscription-tracker','entitlement metadata','auto-renew','payment secrets','IDX/MLS')
has('client-access-inventory','Inventory capability and ownership','AVAILABLE','MISSING','PENDING','raw tokens')
has('ticket-request-intake-agent','symptom separately','root cause','acceptance criteria','sla-priority-engine')
has('sla-priority-engine','actual SLA','`P1`','`P2`','`P3`','`P4`')
has('lead-sla-monitor','submitted form is not a delivered lead','synthetic test leads','CRM','PII')
has('real-estate-crm-integration-specialist','actual integration path','Follow Up Boss','Zapier','webhook','2xx')
has('mls-provider-health-monitor','provider health from local integration health','$metadata','UPSTREAM','LOCAL','MIXED')
has('consent-privacy-cookie-auditor','not legal compliance certification','cookies/storage','GDPR/CCPA','BLOCKED')
has('accessibility-continuous-monitor','release property','automated scans','REGRESSION','FIXED','assistive-technology')
has('content-qa-agent','must not invent the correct business fact','placeholder/lorem','authoritative')
has('client-onboarding-agent','verified baseline','client-access-inventory','never passwords/tokens','maintenance queue')
has('client-offboarding-agent','preserve client ownership','explicit authorization','TRANSFERRED','REVOKED','PENDING')

# v1.0 Website Operations Specialist
has('website-operations-specialist','hosting-dns-ssl-doctor','wordpress-site-doctor','backup-restore-drill','seo-search-console-specialist','analytics-conversion-qa','client-monthly-website-report','PASS','BLOCKED','NOT RUN')
has('hosting-dns-ssl-doctor','DNS','SSL/TLS','redirect loops/chains','CDN/proxy/cache','origin')
has('wordpress-migration-specialist','rollback','search-replace','DNS/SSL','forms','IDX','Browser QA')
has('backup-restore-drill','backup exists','restore verified','staging','database','uploads/media')
has('seo-search-console-specialist','Search Console','robots.txt','canonical','noindex','structured data')
has('real-estate-seo-specialist','IDX filter','thin-content','canonical','expired','MLS/provider rules')
has('core-web-vitals-diagnoser','LCP','INP','CLS','Never invent Core Web Vitals numbers','field and lab')
has('analytics-conversion-qa','downstream reporting','duplicate firing','PII','form_submit')
has('email-deliverability-doctor','SPF','DKIM','DMARC','inbox delivery','CRM')
has('broken-link-redirect-manager','404','redirect chains','homepage','risk-engine')
has('plugin-theme-risk-intelligence','criticality','prove usage','staging','risk register')
has('wp-cron-reliability-doctor','WP-Cron','overdue','DISABLE_WP_CRON','system scheduler')
has('reso-schema-drift-detector','$metadata','field added/removed/renamed','change-impact-map','NOT RUN')
has('reso-provider-capability-inspector','technical capability','licensed permission','RESO Web API','legacy RETS')
has('client-monthly-website-report','never invent uptime','Not measured this period','IDX/MLS/RESO','PII')
has('website-emergency-recovery','DNS → SSL/TLS','preserve evidence','UNPROVEN','representative journeys')

# v0.9 WordPress Real Estate Specialist
has('wordpress-real-estate-specialist','wordpress-site-doctor','wordpress-plugin-conflict-detective','idx-provider-detector','idx-search-qa','wordpress-security-specialist','wordpress-client-handover')
has('wordpress-site-doctor','WordPress Site Health','PHP/server/database','WP-Cron','REST API','permalinks','BLOCKED')
has('wordpress-plugin-conflict-detective','Reproduce first','--skip-plugins','--skip-themes','staging','FIXED')
has('wordpress-safe-update-manager','backup/restore','staging','rollback','post-update','IDX search/detail/map/lead/freshness')
has('wp-cli-operator','wp plugin','wp cron','--ssh','--http','--skip-plugins','High-risk operations','Never print secrets')
has('wordpress-rest-api-integrator','show_in_rest','rest_api_init','permission_callback','Application Passwords','server-side')
has('idx-provider-detector','vendor-hosted iframe/widget','live server-side API query','replicated/local listing database/search index','RESO/OData','legacy RETS')
has('wordpress-idx-bridge','privileged MLS feed','server-side','cache invalidation/freshness','withheld/removed/delayed-marketing','confidential fields')
has('idx-search-qa','price min/max','map pins','back-to-results','browser-qa','Network 429/5xx/timeouts')
has('listing-freshness-monitor','last successful sync','checkpoint','WP-Cron','provider contract','stale public listing')
has('idx-compliance-monitor','Internet-display-withheld','delayed-marketing','Hiding with CSS is not removal','rule source/version','BLOCKED')
has('idx-vow-mode-detector','`IDX`','`VOW`','`HYBRID`','broker-consumer relationship','agreements')
has('wordpress-performance-doctor','Measure before optimizing','Lighthouse/Core Web Vitals','IDX vendor scripts','cache','measured result')
has('wordpress-security-specialist','risk reduction','least privilege','permission_callback','Application Password','MLS/IDX OAuth/API credentials')
has('wordpress-lead-flow-qa','success message is not proof','schedule/request showing','duplicate submit','synthetic test leads','downstream delivery')
has('wordpress-client-handover','passwords, tokens, API keys, MLS credentials','active theme/child theme','weekly/monthly/quarterly','Website Specialist')

# IDX/MLS + Mission Control + legacy contracts
has('real-estate-idx-mls','RESO Web API','RETS','VOW is not IDX','seller instructions','server-side','local MLS/provider rules','BLOCKED')
has('reso-web-api','$metadata','RESO Data Dictionary','OData','RETS','server-side','401/403/429/5xx','NOT RUN')
has('listing-sync-search','authoritative MLS/provider','idempotent','checkpoint','last successful sync','removed/withheld listing')
has('idx-compliance-review','Local MLS/provider rules','seller-withheld','confidential','VOW distinction','hidden with CSS','BLOCKED')
has('mission-control','dynamic-task-graph','parallel-agent-orchestration','devmesh-judge','Maximum two judge repair rounds')
has('dynamic-task-graph','acyclic','READY','acceptance criteria','critical path')
has('parallel-agent-orchestration','actual sub-agent','sequential fallback','at most four concurrent workers','integrator')
has('devmesh-judge','Evidence outranks confidence','independence: unavailable','Critical failures','release decision')
has('confidence-engine','hypothesis ledger','HIGH','MEDIUM','LOW root-cause confidence','not proof')
has('execution-modes','Quick','Standard','Deep','never bypass')
has('environment-doctor','runtime/toolchain','port conflicts','Do not fabricate credentials')
has('database-architect','constraints','indexes','RLS/policies','rollback')
has('api-contract','request','response','authentication and authorization','contract/integration tests')
has('issue-to-pr','read issue','reproduce/confirm','create/update a PR','Never close an issue')
has('production-deployment','Preflight','health/readiness','actual production target','rollback')
has('visual-regression','baseline','REGRESSION','silently overwrite')
has('network-failure-qa','API 4xx/5xx','timeout','offline','duplicate submit')
has('browser-qa','3 browser fix rounds','same browser scenario')
has('security-review','Supabase')
has('accessibility-review','prefers-reduced-motion')
has('performance-review','Do not invent Lighthouse/Core Web Vitals numbers')
has('project-memory','Do not silently add `.devmesh/`')
has('multi-agent-review','maximum four concurrent reviewers')

print('OK: v1.3 Design-to-Code, v1.2 Website Product Builder, v1.1 Agency Operations, Website Operations, WordPress Real Estate, IDX/MLS, Mission Control, and legacy feature contracts validated')