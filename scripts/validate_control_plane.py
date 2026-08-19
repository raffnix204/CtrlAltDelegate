#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
R=Path(__file__).resolve().parents[1]; errors=[]
for rel in ['config/PLANNING-SKILL-ROUTING.yaml','config/LOOP-CONTRACTS.yaml','config/SURFACE-POLICY.yaml','config/HARNESS-CONFORMANCE.yaml','config/CONTROL-VISIBILITY.yaml']:
    try:
        d=yaml.safe_load((R/rel).read_text(encoding='utf-8')) or {}
        if str(d.get('version'))!='5.7.1': errors.append(f'{rel}: version')
    except Exception as e: errors.append(f'{rel}: {e}')
for rel in ['planning/execution/LOOP-STATE.json','planning/execution/JOB-GRAPH.json']:
    try:
        d=json.loads((R/rel).read_text(encoding='utf-8'))
        if d.get('version')!='5.7.1': errors.append(f'{rel}: version')
    except Exception as e: errors.append(f'{rel}: {e}')
loop=(R/'config/LOOP-CONTRACTS.yaml').read_text(encoding='utf-8')
for x in ['REPAIR_LOOP','CONVERGENCE_LOOP','WORKER_LIVENESS_LOOP']:
    if x not in loop: errors.append(f'missing loop {x}')
h=(R/'config/HARNESS-CONFORMANCE.yaml').read_text(encoding='utf-8')
for x in ['deepseek-harness','FIRST_CLASS_PREVIEW','.agents/skills']:
    if x not in h: errors.append(f'harness conformance missing {x}')
if errors:
    print('CONTROL_PLANE_QA_FAIL'); [print('-',e) for e in errors]; sys.exit(2)
print('CONTROL_PLANE_QA_PASS')
