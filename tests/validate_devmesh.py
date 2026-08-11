#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins' / 'devmesh'
MANIFEST = PLUGIN / '.codex-plugin' / 'plugin.json'
MARKETPLACE = ROOT / '.agents' / 'plugins' / 'marketplace.json'
MCP = PLUGIN / '.mcp.json'

REQUIRED = {
    'using-devmesh',
    'brainstorming-requirements',
    'codebase-intelligence',
    'writing-plans',
    'implementation',
    'systematic-debugging',
    'ui-ux-review',
    'browser-engine',
    'browser-qa',
    'regression-testing',
    'security-review',
    'accessibility-review',
    'performance-review',
    'project-memory',
    'risk-engine',
    'qa-verification',
    'qa-reporting',
    'code-review',
    'multi-agent-review',
    'git-delivery',
}

FM = re.compile(r'^---\n(.*?)\n---\n', re.S)


def fail(msg: str) -> None:
    print('ERROR:', msg)
    raise SystemExit(1)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding='utf-8')
    match = FM.match(text)
    if not match:
        fail(f'missing frontmatter: {path.relative_to(ROOT)}')
    out: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            out[key.strip()] = value.strip()
    return out


def require_phrases(path: Path, phrases: list[str]) -> None:
    text = path.read_text(encoding='utf-8')
    for phrase in phrases:
        if phrase not in text:
            fail(f'{path.relative_to(ROOT)} missing required phrase: {phrase}')


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    market = json.loads(MARKETPLACE.read_text(encoding='utf-8'))
    mcp = json.loads(MCP.read_text(encoding='utf-8'))

    if manifest.get('name') != 'devmesh':
        fail('manifest name must be devmesh')
    if manifest.get('version') != '0.3.0':
        fail('manifest version must be 0.3.0')
    if manifest.get('skills') != './skills/':
        fail('manifest skills must be ./skills/')
    if manifest.get('mcpServers') != './.mcp.json':
        fail('manifest must declare ./.mcp.json')
    if 'hooks' in manifest:
        fail('hooks must not be declared in plugin.json')

    interface = manifest.get('interface', {})
    if len(interface.get('defaultPrompt', [])) > 3:
        fail('defaultPrompt must contain at most 3 entries')
    for asset_field in ['composerIcon', 'logo']:
        rel = interface.get(asset_field)
        if not rel or not rel.startswith('./'):
            fail(f'{asset_field} must be a relative plugin path')
        if not (PLUGIN / rel[2:]).exists():
            fail(f'missing interface asset: {rel}')

    if market.get('name') != 'devmesh-marketplace':
        fail('unexpected marketplace name')
    entries = [p for p in market.get('plugins', []) if p.get('name') == 'devmesh']
    if len(entries) != 1:
        fail('marketplace must contain exactly one devmesh entry')
    entry = entries[0]
    if entry.get('source') != {'source': 'local', 'path': './plugins/devmesh'}:
        fail('invalid marketplace source')
    if entry.get('policy', {}).get('installation') != 'AVAILABLE':
        fail('installation policy must be AVAILABLE')
    if entry.get('policy', {}).get('authentication') not in {'ON_INSTALL', 'ON_USE'}:
        fail('invalid auth policy')

    playwright = mcp.get('mcpServers', {}).get('playwright')
    if not isinstance(playwright, dict):
        fail('missing playwright MCP server')
    if playwright.get('command') not in {'npx', 'npx.cmd'}:
        fail('playwright MCP must use npx')
    args = playwright.get('args', [])
    if '@playwright/mcp@latest' not in args:
        fail('playwright MCP package missing from args')

    found: dict[str, Path] = {}
    for path in sorted((PLUGIN / 'skills').glob('*/SKILL.md')):
        meta = frontmatter(path)
        name = meta.get('name')
        desc = meta.get('description')
        if not name or not desc:
            fail(f'missing name/description: {path.relative_to(ROOT)}')
        if path.parent.name != name:
            fail(f'directory/name mismatch: {path.relative_to(ROOT)}')
        if name in found:
            fail(f'duplicate skill: {name}')
        found[name] = path

    if set(found) != REQUIRED:
        fail(
            'skill set mismatch; '
            f'missing={sorted(REQUIRED - set(found))}, '
            f'extra={sorted(set(found) - REQUIRED)}'
        )

    router = (PLUGIN / 'skills/using-devmesh/SKILL.md').read_text(encoding='utf-8')
    for task in ['build', 'fix', 'debug', 'redesign', 'refactor', 'review', 'deploy', 'research']:
        if f'`{task}`' not in router:
            fail(f'router missing task type: {task}')
    for skill in REQUIRED - {'using-devmesh', 'browser-engine'}:
        if skill not in router:
            fail(f'router does not reference skill: {skill}')
    if 'browser-engine' not in router:
        fail('router must explain browser-engine delegation')

    require_phrases(
        PLUGIN / 'skills/browser-qa/SKILL.md',
        [
            'browser-engine',
            'Automatic fix → retest loop',
            '3 browser fix rounds',
            'Evidence boundary',
        ],
    )
    require_phrases(
        PLUGIN / 'skills/security-review/SKILL.md',
        ['Authentication and sessions', 'Authorization', 'Secrets and trust boundaries'],
    )
    require_phrases(
        PLUGIN / 'skills/accessibility-review/SKILL.md',
        ['Keyboard and focus', 'Automated checks', 'WCAG'],
    )
    require_phrases(
        PLUGIN / 'skills/performance-review/SKILL.md',
        ['Runtime review', 'Metrics', 'before/after evidence'],
    )
    require_phrases(
        PLUGIN / 'skills/regression-testing/SKILL.md',
        ['Bug-fix sequence', 'Browser regressions', 'original regression'],
    )
    require_phrases(
        PLUGIN / 'skills/project-memory/SKILL.md',
        ['.devmesh/', 'Opt-in rule', 'Never store secret values'],
    )
    require_phrases(
        PLUGIN / 'skills/risk-engine/SKILL.md',
        ['Read-only', 'Low risk', 'Medium risk', 'High risk'],
    )
    require_phrases(
        PLUGIN / 'skills/qa-reporting/SKILL.md',
        ['PASS', 'BLOCKED', '.devmesh/reports/'],
    )
    require_phrases(
        PLUGIN / 'skills/multi-agent-review/SKILL.md',
        ['read-only', 'maximum four', 'sequential fallback'],
    )

    print(f"OK: marketplace {market['name']}")
    print(f"OK: manifest {manifest['name']} v{manifest['version']}")
    print('OK: Playwright MCP companion configuration validated')
    print(f"OK: {len(found)} required skills and 8 task types validated")
    print('OK: v0.3 quality-gate contracts validated')
    return 0


if __name__ == '__main__':
    sys.exit(main())
