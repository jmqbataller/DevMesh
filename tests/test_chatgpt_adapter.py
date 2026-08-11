#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / 'adapters' / 'chatgpt' / 'devmesh-chatgpt'
CORE = ROOT / 'plugins' / 'devmesh' / 'skills'
MANIFEST = ROOT / 'plugins' / 'devmesh' / '.codex-plugin' / 'plugin.json'
VERSION = json.loads(MANIFEST.read_text(encoding='utf-8'))['version']

skill = (ADAPTER / 'SKILL.md').read_text(encoding='utf-8')
assert skill.startswith('---\n')
assert 'name: devmesh-chatgpt' in skill
assert 'Agent Skills format' in skill
assert f'v{VERSION}' in skill
assert 'Do not assume a local shell' in skill
assert 'Public web browsing is not Browser QA' in skill
for phrase in [
    'mission-control','real-estate-idx-mls','wordpress-real-estate-specialist',
    'website-operations-specialist','agency-operations-control-center','multi-site-fleet-manager',
    'scheduled-site-health-monitor','domain-ssl-expiry-monitor','wordpress-update-wave-manager',
    'staging-production-manager','website-change-timeline','visual-history-screenshot-timeline',
    'plugin-vulnerability-maintenance-watch','license-subscription-tracker','client-access-inventory',
    'ticket-request-intake-agent','sla-priority-engine','lead-sla-monitor',
    'real-estate-crm-integration-specialist','mls-provider-health-monitor',
    'consent-privacy-cookie-auditor','accessibility-continuous-monitor','content-qa-agent',
    'client-onboarding-agent','client-offboarding-agent',
    'hosting-dns-ssl-doctor','backup-restore-drill','seo-search-console-specialist',
    'analytics-conversion-qa','email-deliverability-doctor','website-emergency-recovery',
    'parallel execution: BLOCKED','judge independence: unavailable']:
    assert phrase in skill, phrase
assert '`PASS`' in skill and '`BLOCKED`' in skill and '`NOT RUN`' in skill

for name in ['tool-adaptation.md', 'evidence-boundaries.md', 'invocation-examples.md']:
    assert (ADAPTER / 'references' / name).is_file(), name

with tempfile.TemporaryDirectory(prefix='devmesh-adapter-test-') as tmp:
    out = Path(tmp) / 'devmesh-chatgpt.zip'
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'build_chatgpt_adapter.py'), '--output', str(out)], check=True, cwd=ROOT)
    assert out.is_file()
    with zipfile.ZipFile(out) as zf:
        names = set(zf.namelist())
        assert {'SKILL.md','VERSION','PLAYBOOKS.md','references/tool-adaptation.md'} <= names
        bundled = {n for n in names if n.startswith('playbooks/') and n.endswith('.md')}
        core = {f'playbooks/{p.parent.name}.md' for p in CORE.glob('*/SKILL.md')}
        assert bundled == core
        assert zf.read('VERSION').decode().strip() == VERSION
        for playbook in [
            'mission-control','devmesh-judge','incident-commander',
            'real-estate-idx-mls','reso-web-api','listing-sync-search','idx-compliance-review',
            'wordpress-real-estate-specialist','wordpress-site-doctor','wordpress-plugin-conflict-detective',
            'wordpress-safe-update-manager','wp-cli-operator','wordpress-rest-api-integrator',
            'idx-provider-detector','wordpress-idx-bridge','idx-search-qa','listing-freshness-monitor',
            'idx-compliance-monitor','idx-vow-mode-detector','wordpress-performance-doctor',
            'wordpress-security-specialist','wordpress-lead-flow-qa','wordpress-client-handover',
            'website-operations-specialist','hosting-dns-ssl-doctor','wordpress-migration-specialist',
            'backup-restore-drill','seo-search-console-specialist','real-estate-seo-specialist',
            'core-web-vitals-diagnoser','analytics-conversion-qa','email-deliverability-doctor',
            'broken-link-redirect-manager','plugin-theme-risk-intelligence','wp-cron-reliability-doctor',
            'reso-schema-drift-detector','reso-provider-capability-inspector',
            'client-monthly-website-report','website-emergency-recovery',
            'agency-operations-control-center','multi-site-fleet-manager','scheduled-site-health-monitor',
            'domain-ssl-expiry-monitor','wordpress-update-wave-manager','staging-production-manager',
            'website-change-timeline','visual-history-screenshot-timeline',
            'plugin-vulnerability-maintenance-watch','license-subscription-tracker','client-access-inventory',
            'ticket-request-intake-agent','sla-priority-engine','lead-sla-monitor',
            'real-estate-crm-integration-specialist','mls-provider-health-monitor',
            'consent-privacy-cookie-auditor','accessibility-continuous-monitor','content-qa-agent',
            'client-onboarding-agent','client-offboarding-agent']:
            assert f'playbooks/{playbook}.md' in names

print(f'OK: ChatGPT adapter v{VERSION} source and portable Agency Operations bundle validated')
