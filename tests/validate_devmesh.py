#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/'plugins'/'devmesh'
MANIFEST=PLUGIN/'.codex-plugin'/'plugin.json'
MARKETPLACE=ROOT/'.agents'/'plugins'/'marketplace.json'
REQUIRED={
'using-devmesh','brainstorming-requirements','codebase-intelligence','writing-plans','implementation',
'systematic-debugging','ui-ux-review','browser-qa','qa-verification','code-review','git-delivery'}
FM=re.compile(r'^---\n(.*?)\n---\n', re.S)

def fail(msg):
    print('ERROR:',msg); raise SystemExit(1)

def frontmatter(path):
    text=path.read_text(encoding='utf-8'); m=FM.match(text)
    if not m: fail(f'missing frontmatter: {path.relative_to(ROOT)}')
    out={}
    for line in m.group(1).splitlines():
        if ':' in line:
            k,v=line.split(':',1); out[k.strip()]=v.strip()
    return out

def main():
    manifest=json.loads(MANIFEST.read_text())
    market=json.loads(MARKETPLACE.read_text())
    if manifest.get('name')!='devmesh': fail('manifest name must be devmesh')
    if manifest.get('skills')!='./skills/': fail('manifest skills must be ./skills/')
    if 'hooks' in manifest: fail('hooks must not be declared in plugin.json')
    if market.get('name')!='devmesh-marketplace': fail('unexpected marketplace name')
    entries=[p for p in market.get('plugins',[]) if p.get('name')=='devmesh']
    if len(entries)!=1: fail('marketplace must contain exactly one devmesh entry')
    entry=entries[0]
    if entry.get('source')!={'source':'local','path':'./plugins/devmesh'}: fail('invalid marketplace source')
    if entry.get('policy',{}).get('installation')!='AVAILABLE': fail('installation policy must be AVAILABLE')
    if entry.get('policy',{}).get('authentication') not in {'ON_INSTALL','ON_USE'}: fail('invalid auth policy')
    found={}
    for p in sorted((PLUGIN/'skills').glob('*/SKILL.md')):
        meta=frontmatter(p); name=meta.get('name'); desc=meta.get('description')
        if not name or not desc: fail(f'missing name/description: {p.relative_to(ROOT)}')
        if p.parent.name!=name: fail(f'directory/name mismatch: {p.relative_to(ROOT)}')
        if name in found: fail(f'duplicate skill: {name}')
        found[name]=p
    if set(found)!=REQUIRED:
        fail(f'skill set mismatch; missing={sorted(REQUIRED-set(found))}, extra={sorted(set(found)-REQUIRED)}')
    router=(PLUGIN/'skills/using-devmesh/SKILL.md').read_text()
    for task in ['build','fix','debug','redesign','refactor','review','deploy','research']:
        if f'`{task}`' not in router: fail(f'router missing task type: {task}')
    for skill in REQUIRED-{'using-devmesh'}:
        if skill not in router: fail(f'router does not reference skill: {skill}')
    browser=(PLUGIN/'skills/browser-qa/SKILL.md').read_text()
    for phrase in ['Launch the application','Check browser runtime errors','Test desktop and mobile layouts','Exercise interactions','Test forms and inputs','Detect overflow and visual defects','Capture screenshots','Visual review','Report and fix real issues','Evidence boundary']:
        if phrase not in browser: fail(f'browser-qa missing required section: {phrase}')
    print(f"OK: marketplace {market['name']}")
    print(f"OK: manifest {manifest['name']} v{manifest['version']}")
    print(f"OK: {len(found)} required skills and 8 task types validated")
    print('OK: Browser QA workflow contract validated')
    return 0
if __name__=='__main__': sys.exit(main())
