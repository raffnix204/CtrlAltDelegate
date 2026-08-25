#!/usr/bin/env python3
from pathlib import Path
import yaml, sys, re
R=Path(__file__).resolve().parents[1]
e=[]
req=['config/MODEL-ROUTING-POLICY.yaml','docs/system/MODEL-ROUTING-AND-HIERARCHICAL-ORCHESTRATION.md','planning/execution/MODEL-ROUTING-STATE.yaml','CHANGELOG-V5.9.2.md']
for x in req:
    if not (R/x).exists(): e.append(f'missing {x}')
try:
    p=yaml.safe_load((R/'config/MODEL-ROUTING-POLICY.yaml').read_text())
    om=p['openai_mapping']
    checks=[
      (p['roles']['main_orchestrator']['class']=='FRONTIER','main orchestrator not FRONTIER'),
      (p['roles']['main_orchestrator']['product_code_write']=='FORBIDDEN_WHEN_SUITABLE_DELEGATION_EXISTS','orchestrator not spawn-only'),
      (p['roles']['standard_implementation_worker']['class']=='EFFICIENT','standard worker not EFFICIENT'),
      (p['roles']['semantic_reviewer']['class']=='BALANCED','semantic reviewer not BALANCED'),
      (p['roles']['critical_reviewer']['class']=='FRONTIER','critical reviewer not FRONTIER'),
      (om['FRONTIER']['model']=='gpt-5.6-sol','Sol mapping missing'),
      (om['BALANCED']['model']=='gpt-5.6-terra','Terra mapping missing'),
      (om['EFFICIENT']['model']=='gpt-5.6-luna','Luna mapping missing'),
      (om['FRONTIER']['reasoning_effort']=='high','Sol effort is not high'),
      (om['FRONTIER']['reasoning_effort_ceiling']=='high','Sol ceiling is not high'),
      ('xhigh' in om['FRONTIER']['forbidden_efforts'] and 'max' in om['FRONTIER']['forbidden_efforts'],'Sol forbidden efforts incomplete'),
      (p['review_independence']['critical']=='IMPLEMENTER_NE_REVIEWER_AND_REVIEWER_NE_MAIN_ORCHESTRATOR','critical reviewer independence missing'),
    ]
    e += [msg for ok,msg in checks if not ok]
except Exception as ex: e.append(f'policy parse: {ex}')
for rel in ['AGENTS.md','docs/templates/JOB.template.md','docs/templates/JOB-CONTRACT.template.yaml','docs/templates/WORKER-BRIEF.template.yaml']:
    s=(R/rel).read_text()
    for tok in ['EFFICIENT','BALANCED','FRONTIER']:
        if tok not in s: e.append(f'{rel} missing {tok}')
for rel in ['AGENTS.md','docs/system/MODEL-ROUTING-AND-HIERARCHICAL-ORCHESTRATION.md','config/MODEL-ROUTING-POLICY.yaml']:
    s=(R/rel).read_text().lower()
    if 'sol' not in s or 'high' not in s: e.append(f'{rel} missing Sol high rule')
    if rel!='config/MODEL-ROUTING-POLICY.yaml' and not ('xhigh' in s and 'max' in s): e.append(f'{rel} missing Sol >high prohibition')
if e:
    print('V5.9.2 MODEL ROUTING FAILED'); [print('-',x) for x in e]; sys.exit(1)
print('V5.9.2 MODEL ROUTING OK')
