#!/usr/bin/env python3
from pathlib import Path
import json, yaml, hashlib, sys
R=Path(__file__).resolve().parents[1]; errors=[]

def load_yaml(rel):
    try: return yaml.safe_load((R/rel).read_text(encoding='utf-8')) or {}
    except Exception as e: errors.append(f'{rel}: {e}'); return {}

def load_json(rel):
    try: return json.loads((R/rel).read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{rel}: {e}'); return {}

ap=load_yaml('config/ASSURANCE-PROFILES.yaml')
if str(ap.get('version'))!='5.8': errors.append('ASSURANCE-PROFILES version')
if set(ap.get('allowed_assurance_profiles') or []) != {'NORMAL','ELEVATED','HIGH','CRITICAL'}: errors.append('assurance profile set')
if (ap.get('policy') or {}).get('work_size_and_assurance_are_independent') is not True: errors.append('work/assurance independence')
state=load_yaml('planning/execution/ASSURANCE-STATE.yaml')
if str(state.get('version'))!='5.8': errors.append('ASSURANCE-STATE version')
rc=load_json('planning/execution/ROOT-CAUSE-DEPTH.json')
if rc.get('version')!='5.8': errors.append('ROOT-CAUSE-DEPTH version')
for rel in ['docs/system/ASSURANCE-BEHAVIORAL-ORACLES-AND-ROOT-CAUSE-DEPTH.md','docs/system/WORKER-BRIEF-INTEGRITY-AND-CAPABILITY-ATTESTATION.md','docs/templates/WORKER-BRIEF.template.yaml','docs/templates/HARNESS-ATTESTATION.template.json']:
    if not (R/rel).is_file(): errors.append(f'missing {rel}')
loop=load_yaml('config/LOOP-CONTRACTS.yaml')
repair=((loop.get('loops') or {}).get('REPAIR_LOOP') or {})
if 'root_cause_depth_gate' not in (repair.get('pre_repair_gates') or []): errors.append('REPAIR_LOOP lacks root_cause_depth_gate')
if 'behavioral_oracle' not in (repair.get('pre_repair_gates') or []): errors.append('REPAIR_LOOP lacks behavioral_oracle')
if errors:
    print('ASSURANCE_CONTROL_QA_FAIL'); [print('-',e) for e in errors]; sys.exit(2)
print('ASSURANCE_CONTROL_QA_PASS')
