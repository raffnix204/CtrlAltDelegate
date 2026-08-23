#!/usr/bin/env python3
from pathlib import Path
import re,sys,yaml
R=Path(__file__).resolve().parents[1]; errs=[]; skills=[]
for p in sorted((R/'.agents/skills').glob('*/SKILL.md')):
    txt=p.read_text(encoding='utf-8'); m=re.match(r'^---\n(.*?)\n---\n',txt,re.S)
    if not m: errs.append(f'{p.parent.name}: missing YAML frontmatter'); continue
    try: fm=yaml.safe_load(m.group(1)) or {}
    except Exception as e: errs.append(f'{p.parent.name}: invalid frontmatter {e}'); continue
    d=str(fm.get('description') or '').strip(); skills.append(p.parent.name)
    if not d.startswith('Use when '): errs.append(f'{p.parent.name}: description must be activation-trigger-first (Use when ...)')
    if len(d)>420: errs.append(f'{p.parent.name}: description too long for discovery metadata ({len(d)})')
    if not fm.get('name'): errs.append(f'{p.parent.name}: missing name')
policy=yaml.safe_load((R/'config/SKILL-DISCOVERY-POLICY.yaml').read_text(encoding='utf-8')) or {}
if str(policy.get('version'))!='5.9': errs.append('SKILL-DISCOVERY-POLICY version mismatch')
if policy.get('description_style')!='ACTIVATION_TRIGGER_FIRST': errs.append('discovery policy must require activation-trigger-first descriptions')
if not policy.get('a_b_evaluation_required_for_bulk_semantic_rewrite'): errs.append('semantic bulk rewrites must require A/B evaluation')
if errs:
 print('SKILL_DISCOVERY_QA_FAIL'); [print('-',x) for x in errs]; sys.exit(2)
print(f'SKILL_DISCOVERY_QA_PASS skills={len(skills)} trigger_first={len(skills)}')
