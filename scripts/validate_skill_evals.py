#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
R=Path(__file__).resolve().parents[1]
cat=yaml.safe_load((R/'.agents/skills/CATALOG.yaml').read_text(encoding='utf-8'))
ids={x['id'] for x in cat.get('skills',[]) if isinstance(x,dict) and x.get('id')}
d=yaml.safe_load((R/'evals/skills/scenarios.yaml').read_text(encoding='utf-8'))
errs=[]; seen=set(); classes=set(); behavior_targets=set()
if d.get('version') != '5.6.4': errs.append('eval version mismatch')
for s in d.get('scenarios',[]):
    sid=s.get('id'); cls=s.get('class','routing')
    if not sid or sid in seen: errs.append(f'bad/duplicate scenario id {sid}')
    seen.add(sid); classes.add(cls)
    if cls not in {'routing','behavior','system_regression'}: errs.append(f'{sid}: invalid class {cls}')
    if not str(s.get('prompt','')).strip(): errs.append(f'{sid}: missing prompt')
    for k in ('required','forbidden'):
        for x in s.get(k,[]) or []:
            if x not in ids: errs.append(f'{sid}: {k} references missing skill {x}')
    both=set(s.get('required',[]) or []) & set(s.get('forbidden',[]) or [])
    if both: errs.append(f'{sid}: both required/forbidden {sorted(both)}')
    if cls in {'behavior','system_regression'} and not s.get('assertions'):
        errs.append(f'{sid}: {cls} requires assertions')
    if cls=='behavior': behavior_targets.update(s.get('required',[]) or [])
for need in {'routing','behavior','system_regression'}:
    if need not in classes: errs.append(f'missing eval class {need}')
# V5.6.4 high-priority/new/network specialists must have at least one behavior scenario.
priority={'nextjs-engineering','react-web-engineering','angular-engineering','react-native-engineering','flutter-engineering','postgres-engineering','graphql-engineering','terraform-engineering','mongodb-engineering','cloudflare-platform-engineering','wordpress-engineering','threat-modeling-engineering','property-based-testing','unifi-network-engineering','opnsense-engineering','openwrt-engineering','network-infrastructure-engineering'}
missing=sorted(priority-behavior_targets)
if missing: errs.append(f'priority skills missing behavior eval: {missing}')
if errs:
    print('SKILL_EVAL_QA_FAIL'); [print('-',e) for e in errs]; sys.exit(2)
print(f'SKILL_EVAL_QA_PASS scenarios={len(seen)} skills={len(ids)} classes={sorted(classes)} behavior_targets={len(behavior_targets)}')
