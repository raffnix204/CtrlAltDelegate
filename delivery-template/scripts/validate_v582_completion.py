#!/usr/bin/env python3
from pathlib import Path
import json,yaml,subprocess,tempfile,sys
R=Path(__file__).resolve().parents[1]; e=[]
required=['config/BLOCKER-POLICY.yaml','config/PRODUCT-COMPLETION-POLICY.yaml','planning/product/PRODUCT-CONTRACT.yaml','planning/acceptance/USER-JOURNEY-ORACLES.yaml','planning/execution/BLOCKERS.json','planning/execution/DEFERRED-VALIDATION.json','planning/execution/ASSUMPTIONS.jsonl','planning/execution/PROVIDER-ATTESTATIONS.json','planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json','planning/execution/PRODUCT-DRIFT-REVIEW.json','planning/execution/EXECUTION-SNAPSHOT.json','docs/system/PRODUCT-RUNTIME-COMPLETION.md','docs/system/BLOCKERS-DEFERRED-VALIDATION-AND-CONTINUATION.md','docs/system/EXECUTION-SNAPSHOT-AND-CONTROLLED-TRANSITIONS.md','scripts/transition_job.py','scripts/build_execution_snapshot.py','scripts/refresh_job_readiness.py','scripts/validate_product_completion.py','scripts/record_loop_attempt.py','scripts/record_blocker.py','config/SKILL-OPTIMIZATION-POLICY.yaml','docs/system/SKILLOPT-OFFLINE-SKILL-LAB.md']
for x in required:
    if not (R/x).exists(): e.append('missing '+x)
try:
    b=yaml.safe_load((R/'config/BLOCKER-POLICY.yaml').read_text())
    if str(b.get('version'))!='5.8.2': e.append('blocker policy version')
    if not b.get('continuation_rule',{}).get('verification_blocker_never_global_stop'): e.append('verification blocker must not global stop')
except Exception as x:e.append(str(x))
try:
    c=yaml.safe_load((R/'config/PRODUCT-COMPLETION-POLICY.yaml').read_text())
    for tok in ['USER_JOURNEY_REAL','PROVIDER_REAL']:
        if tok not in c.get('evidence_types',[]):e.append('missing '+tok+' evidence type')
    if c.get('project_completion',{}).get('validation_pending_state')!='VALIDATION_PENDING_EXTERNAL':e.append('missing validation pending state')
    if c.get('job_transition',{}).get('implementation_complete_state')!='IMPLEMENTED_UNVERIFIED':e.append('missing implementation-complete continuation state')
    if not c.get('dependency_gates',{}).get('verification_blocker_does_not_block_implementation_dependencies'):e.append('missing implementation dependency continuation rule')
except Exception as x:e.append(str(x))

# Preserve every mutable state touched by behavioral smoke tests.
rels=['planning/execution/JOB-GRAPH.json','planning/execution/BLOCKERS.json','planning/execution/DEFERRED-VALIDATION.json','planning/execution/EVIDENCE-INDEX.json','planning/execution/CONVERGENCE-MATRIX.json','planning/execution/PROVIDER-ATTESTATIONS.json','planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json','planning/execution/PRODUCT-DRIFT-REVIEW.json','planning/execution/LOOP-STATE.json','planning/execution/EXECUTION-SNAPSHOT.json','planning/execution/STATE.md','planning/product/PRODUCT-CONTRACT.yaml','planning/acceptance/USER-JOURNEY-ORACLES.yaml']
before={rel:(R/rel).read_text(encoding='utf-8') for rel in rels}
def jwrite(rel,obj): (R/rel).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def ywrite(rel,obj): (R/rel).write_text(yaml.safe_dump(obj,sort_keys=False),encoding='utf-8')
try:
    # Baseline completion must fail closed.
    cp=subprocess.run([sys.executable,str(R/'scripts/validate_product_completion.py')],cwd=R,text=True,capture_output=True)
    if cp.returncode==0:e.append('empty baseline completion must fail closed')

    # No-progress same-strategy retry must be denied.
    subprocess.run([sys.executable,str(R/'scripts/record_loop_attempt.py'),'--loop','REPAIR_LOOP','--strategy','same','--failure-signature','F','--progress','NO'],cwd=R,text=True,capture_output=True)
    cp=subprocess.run([sys.executable,str(R/'scripts/record_loop_attempt.py'),'--loop','REPAIR_LOOP','--strategy','same','--failure-signature','F','--progress','NO'],cwd=R,text=True,capture_output=True)
    if cp.returncode==0:e.append('same failure/no-progress strategy reuse must be denied')
    (R/'planning/execution/LOOP-STATE.json').write_text(before['planning/execution/LOOP-STATE.json'],encoding='utf-8')

    # Verification blocker creates deferred validation but does not globally stop.
    cp=subprocess.run([sys.executable,str(R/'scripts/record_blocker.py'),'SMOKE-V','--class','VERIFICATION_BLOCKER','--scope','JOB','--reason','physical device later','--jobs','JX','--requirements','REQ-X','--validation','run on device'],cwd=R,text=True,capture_output=True)
    if cp.returncode!=0 or 'CONTINUE_READY_WORK' not in cp.stdout:e.append('verification blocker smoke failed')
    (R/'planning/execution/BLOCKERS.json').write_text(before['planning/execution/BLOCKERS.json'],encoding='utf-8'); (R/'planning/execution/DEFERRED-VALIDATION.json').write_text(before['planning/execution/DEFERRED-VALIDATION.json'],encoding='utf-8')

    # Dependency semantics: IMPLEMENTED_UNVERIFIED unlocks IMPLEMENTATION but not VERIFIED dependencies.
    jwrite('planning/execution/JOB-GRAPH.json',{'version':'5.8.2','jobs':[{'id':'A','status':'IMPLEMENTED_UNVERIFIED','required':True},{'id':'B','status':'PLANNED','required':True,'dependencies':[{'job_id':'A','gate':'IMPLEMENTATION'}]},{'id':'C','status':'PLANNED','required':True,'dependencies':[{'job_id':'A','gate':'VERIFIED'}]}],'claims':{},'updated_at':None})
    cp=subprocess.run([sys.executable,str(R/'scripts/refresh_job_readiness.py')],cwd=R,text=True,capture_output=True)
    try: rr=json.loads(cp.stdout)
    except Exception: rr={}
    if cp.returncode!=0 or 'B' not in rr.get('derived_ready',[]) or 'C' in rr.get('derived_ready',[]):e.append('dependency-ready continuation semantics failed')
    cp=subprocess.run([sys.executable,str(R/'scripts/record_blocker.py'),'SMOKE-G','--class','EXECUTION_BLOCKER','--scope','GLOBAL','--reason','should be denied while B is ready','--jobs','C'],cwd=R,text=True,capture_output=True)
    if cp.returncode==0:e.append('global execution blocker must be denied while derived-ready work exists')

    # Controlled transition: implementation progress may be recorded, DONE needs real journey/provider evidence.
    sha='SMOKE_SHA'
    jwrite('planning/execution/BLOCKERS.json',{'version':'5.8.2','blockers':[],'updated_at':None}); jwrite('planning/execution/DEFERRED-VALIDATION.json',{'version':'5.8.2','items':[],'status':'EMPTY','updated_at':None})
    entries=[{'id':'E-UNIT','type':'UNIT','realness':'SIMULATED','status':'PASS','sha':sha},{'id':'E-J','type':'USER_JOURNEY_REAL','realness':'REAL','status':'PASS','sha':sha},{'id':'E-P','type':'PROVIDER_REAL','realness':'REAL','status':'PASS','sha':sha},{'id':'E-R','type':'RUNTIME_REAL','realness':'REAL','status':'PASS','sha':sha}]
    jwrite('planning/execution/EVIDENCE-INDEX.json',{'version':'5.8.2','candidate_sha':sha,'entries':entries,'status':'PASS','evidence_type_policy':'config/PRODUCT-COMPLETION-POLICY.yaml'}); jwrite('planning/execution/CONVERGENCE-MATRIX.json',{'version':'5.8.2','candidate_sha':sha,'requirements':[],'status':'NOT_EVALUATED','completion_policy':'config/PRODUCT-COMPLETION-POLICY.yaml'})
    job={'id':'J1','status':'RUNNING','required':True,'implementation_complete':True,'implementation_evidence_ids':['E-UNIT'],'acceptance':[{'status':'PASS'}],'evidence_ids':['E-UNIT'],'required_evidence_types':['UNIT'],'required_journey_ids':['JOURNEY-1'],'required_provider_ids':['P1']}
    jwrite('planning/execution/JOB-GRAPH.json',{'version':'5.8.2','jobs':[job],'claims':{},'updated_at':None})
    ywrite('planning/acceptance/USER-JOURNEY-ORACLES.yaml',{'version':'5.8.2','status':'READY','journeys':[{'id':'JOURNEY-1','mandatory':True,'final_real_required':True,'required_evidence_types':['USER_JOURNEY_REAL'],'status':'NOT_RUN','evidence_ids':[]}]})
    jwrite('planning/execution/PROVIDER-ATTESTATIONS.json',{'version':'5.8.2','providers':{'P1':{'required_for_completion':True,'status':'IMPLEMENTED','evidence_ids':[]}},'updated_at':None})
    cp=subprocess.run([sys.executable,str(R/'scripts/transition_job.py'),'J1','IMPLEMENTED_UNVERIFIED'],cwd=R,text=True,capture_output=True)
    if cp.returncode!=0:e.append('IMPLEMENTED_UNVERIFIED transition should be allowed with implementation evidence')
    cp=subprocess.run([sys.executable,str(R/'scripts/transition_job.py'),'J1','DONE'],cwd=R,text=True,capture_output=True)
    if cp.returncode==0:e.append('DONE must be denied without real journey/provider verification')
    ywrite('planning/acceptance/USER-JOURNEY-ORACLES.yaml',{'version':'5.8.2','status':'READY','journeys':[{'id':'JOURNEY-1','mandatory':True,'final_real_required':True,'required_evidence_types':['USER_JOURNEY_REAL'],'status':'PASS','evidence_ids':['E-J']}]})
    jwrite('planning/execution/PROVIDER-ATTESTATIONS.json',{'version':'5.8.2','providers':{'P1':{'required_for_completion':True,'status':'CONSUMER_VERIFIED','evidence_ids':['E-P','E-R']}},'updated_at':None})
    cp=subprocess.run([sys.executable,str(R/'scripts/transition_job.py'),'J1','DONE'],cwd=R,text=True,capture_output=True)
    if cp.returncode!=0:e.append('DONE should pass after typed real journey/provider evidence')

    # Project completion with all feasible code present but declared external proof missing returns PENDING, not hard FAIL.
    jwrite('planning/execution/JOB-GRAPH.json',{'version':'5.8.2','jobs':[{'id':'J1','status':'IMPLEMENTED_UNVERIFIED','required':True}],'claims':{},'updated_at':None})
    jwrite('planning/execution/BLOCKERS.json',{'version':'5.8.2','blockers':[{'id':'VB','class':'VERIFICATION_BLOCKER','scope':'JOB','status':'OPEN','affected_job_ids':['J1'],'requirement_ids':['REQ-1']}],'updated_at':None})
    jwrite('planning/execution/DEFERRED-VALIDATION.json',{'version':'5.8.2','items':[{'id':'VAL-VB','blocker_id':'VB','requirement_ids':['REQ-1'],'job_ids':['J1'],'required_for_completion':True,'status':'PENDING'}],'status':'PENDING','updated_at':None})
    jwrite('planning/execution/CONVERGENCE-MATRIX.json',{'version':'5.8.2','candidate_sha':sha,'requirements':[{'id':'REQ-1','mandatory':True,'status':'IMPLEMENTED_UNVERIFIED','code_paths':['src/example'],'implementation_evidence_ids':['E-UNIT'],'documentation':{'impact':'NONE'}}],'status':'PENDING','completion_policy':'config/PRODUCT-COMPLETION-POLICY.yaml'})
    jwrite('planning/execution/EVIDENCE-INDEX.json',{'version':'5.8.2','candidate_sha':sha,'entries':[entries[0]],'status':'PENDING','evidence_type_policy':'config/PRODUCT-COMPLETION-POLICY.yaml'})
    ywrite('planning/product/PRODUCT-CONTRACT.yaml',{'version':'5.8.2','status':'NOT_APPLICABLE','product_type':None,'primary_users':[],'primary_journeys':[],'product_outcomes':[],'ux_constraints':{'required':[],'prohibited':[]},'non_goals':[],'source_requirements':[]})
    ywrite('planning/acceptance/USER-JOURNEY-ORACLES.yaml',{'version':'5.8.2','status':'NOT_APPLICABLE','journeys':[]})
    jwrite('planning/execution/PROVIDER-ATTESTATIONS.json',{'version':'5.8.2','providers':{},'updated_at':None}); jwrite('planning/execution/PRODUCT-DRIFT-REVIEW.json',{'version':'5.8.2','candidate_sha':'','status':'NOT_APPLICABLE','checks':[],'evidence_ids':[],'reviewer':{},'updated_at':None}); jwrite('planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json',{'version':'5.8.2','status':'READY_WITH_DEFERRED_VALIDATION','candidate_sha':sha,'checks':[{'id':'DEVICE','required':True,'status':'DEFERRED_VERIFICATION','blocker_class':'VERIFICATION_BLOCKER'}],'updated_at':None})
    cp=subprocess.run([sys.executable,str(R/'scripts/validate_product_completion.py')],cwd=R,text=True,capture_output=True)
    if cp.returncode!=3 or 'VALIDATION_PENDING_EXTERNAL' not in cp.stdout:e.append('deferred external verification must yield VALIDATION_PENDING_EXTERNAL, not hard failure')
finally:
    for rel,text in before.items(): (R/rel).write_text(text,encoding='utf-8')

opt=yaml.safe_load((R/'config/SKILL-OPTIMIZATION-POLICY.yaml').read_text()) or {}
if opt.get('runtime_dependency') is not False or opt.get('promotion',{}).get('automatic') is not False:e.append('SkillOpt must remain optional/no auto promotion')
if e:
    print('V582_COMPLETION_QA_FAIL'); [print('-',x) for x in e]; sys.exit(2)
print('V582_COMPLETION_QA_PASS')
