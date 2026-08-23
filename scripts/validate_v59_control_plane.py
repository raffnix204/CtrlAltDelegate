#!/usr/bin/env python3
from pathlib import Path
import json,shutil,subprocess,sys,tempfile,time,yaml
R=Path(__file__).resolve().parents[1]; errors=[]
required=[
'config/EXECUTION-CONTROL-POLICY.yaml','config/STATE-RECONCILIATION.yaml','config/PLANNING-CONVERGENCE-POLICY.yaml','config/REVIEW-VERDICT-POLICY.yaml','config/CONTROL-EFFECTIVENESS-POLICY.yaml','config/SKILL-DISCOVERY-POLICY.yaml',
'planning/execution/CONTROL-STATE.json','planning/execution/CONTROL-MUTATION-LOG.jsonl','planning/execution/CONTROL-EVENTS.jsonl','planning/execution/WORKER-CLAIMS.json','planning/execution/JOB-ATTEMPTS.jsonl','planning/execution/ATTEMPT-STATE.json','planning/execution/RECOVERY-ACTIONS.jsonl','planning/execution/RECONCILIATION-LOG.jsonl','planning/execution/REVIEW-VERDICTS.json','planning/execution/VERIFICATION-BASELINES.json','planning/execution/PLANNING-CONVERGENCE.json','planning/architecture/PLANNING-ARTIFACT-GRAPH.yaml',
'docs/schemas/WORKER-RESULT.schema.json','docs/templates/WORKER-RESULT.template.json','scripts/control_state.py','scripts/validate_control_mutation.py','scripts/claim_job.py','scripts/heartbeat_job.py','scripts/start_job_attempt.py','scripts/settle_job_attempt.py','scripts/reconcile_execution_state.py','scripts/record_recovery_action.py','scripts/validate_worker_result.py','scripts/record_verification_baseline.py','scripts/classify_verification_delta.py','scripts/validate_planning_convergence.py','scripts/record_review_verdict.py','scripts/execution_stop_gate.py','scripts/validate_oracle_integrity.py','scripts/validate_decision_coverage.py','scripts/validate_planning_artifact_graph.py','scripts/validate_skill_discovery.py','scripts/record_control_insight.py','scripts/planning_probe.py']
for x in required:
 if not (R/x).exists(): errors.append('missing '+x)
try:
 p=yaml.safe_load((R/'config/EXECUTION-CONTROL-POLICY.yaml').read_text()) or {}
 if str(p.get('version'))!='5.9': errors.append('execution control policy version')
 if not p.get('state_revision',{}).get('compare_and_set_required'): errors.append('compare-and-set missing')
 if not p.get('claim',{}).get('one_active_claim_per_job'): errors.append('claim exclusivity missing')
except Exception as e: errors.append(str(e))
try:
 s=yaml.safe_load((R/'config/SURFACE-POLICY.yaml').read_text()) or {}; classes=s.get('classes') or {}
 for c in ['LOCKED','CONTROLLER_MUTATED','DERIVED','APPEND_ONLY']:
  if classes.get(c,{}).get('enforcement')!='ENFORCED': errors.append(c+' not ENFORCED')
except Exception as e: errors.append(str(e))

def run(root,*args,expect=None):
 cp=subprocess.run([sys.executable,*map(str,args)],cwd=root,text=True,capture_output=True)
 if expect is not None and cp.returncode not in expect: errors.append(f"{' '.join(map(str,args))}: rc={cp.returncode} out={cp.stdout.strip()} err={cp.stderr.strip()}")
 return cp
if not errors:
 with tempfile.TemporaryDirectory(prefix='cad-v59-') as td:
  T=Path(td)/'root'; shutil.copytree(R,T)
  # Build a fresh controlled fixture.
  (T/'planning/execution/CONTROL-MUTATION-LOG.jsonl').write_text(''); (T/'planning/execution/CONTROL-EVENTS.jsonl').write_text(''); (T/'planning/execution/JOB-ATTEMPTS.jsonl').write_text(''); (T/'planning/execution/RECOVERY-ACTIONS.jsonl').write_text(''); (T/'planning/execution/RECONCILIATION-LOG.jsonl').write_text('')
  (T/'planning/execution/CONTROL-STATE.json').write_text(json.dumps({'version':'5.9','revision':0,'status':'UNSEALED','sealed_hashes':{},'last_mutation_id':None,'last_receipt_hash':None,'updated_at':None},indent=2)+'\n')
  jobs={'version':'5.9','state_revision':0,'jobs':[{'id':'J1','status':'READY','required':True,'dependencies':[]},{'id':'J2','status':'PLANNED','required':True,'dependencies':[{'job_id':'J1','gate':'IMPLEMENTATION'}]}],'updated_at':None,'transition_policy':'config/PRODUCT-COMPLETION-POLICY.yaml','dependency_policy':{'default_gate':'IMPLEMENTATION','implementation_satisfied_by':['IMPLEMENTED_UNVERIFIED','VERIFYING','DONE'],'verified_satisfied_by':['DONE']}}
  (T/'planning/execution/JOB-GRAPH.json').write_text(json.dumps(jobs,indent=2)+'\n'); (T/'planning/execution/WORKER-CLAIMS.json').write_text(json.dumps({'version':'5.9','claims':{},'updated_at':None},indent=2)+'\n'); (T/'planning/execution/ATTEMPT-STATE.json').write_text(json.dumps({'version':'5.9','attempts':{},'active_by_job':{},'updated_at':None},indent=2)+'\n'); (T/'planning/execution/REVIEW-VERDICTS.json').write_text(json.dumps({'version':'5.9','verdicts':[],'updated_at':None},indent=2)+'\n')
  run(T,T/'scripts/validate_control_mutation.py','--initialize',expect={0}); run(T,T/'scripts/validate_control_mutation.py',expect={0})
  # Claim exclusivity + attempt lifecycle.
  c1=run(T,T/'scripts/claim_job.py','J1','--worker','W1','--skip-reconcile',expect={0}); token=json.loads(c1.stdout)['claim_token'] if c1.returncode==0 else 'bad'
  run(T,T/'scripts/claim_job.py','J1','--worker','W2','--skip-reconcile',expect={4})
  a1=run(T,T/'scripts/start_job_attempt.py','J1','--worker','W1','--claim-token',token,'--brief-sha256','b'*64,'--base-sha','BASE',expect={0}); aid=json.loads(a1.stdout)['attempt_id'] if a1.returncode==0 else 'bad'
  run(T,T/'scripts/heartbeat_job.py','J1','--worker','W1','--claim-token',token,expect={0})
  result={'schema_version':'5.9','job_id':'J1','attempt_id':aid,'worker_id':'W1','brief_sha256':'b'*64,'base_sha':'BASE','outcome':'IMPLEMENTED','implementation_status':'COMPLETE','verification_status':'PENDING_EXTERNAL','skills_applied':[],'changed_paths':['src/x'],'evidence_ids':[],'blockers':[],'concerns':[]}
  rp=T/'worker-result.json'; rp.write_text(json.dumps(result)); run(T,T/'scripts/validate_worker_result.py',rp,expect={0})
  # No evidence => settlement is allowed as a result claim, but DONE is not.
  run(T,T/'scripts/settle_job_attempt.py',rp,'--claim-token',token,expect={0}); run(T,T/'scripts/transition_job.py','J1','DONE','--revalidate-only',expect={2})
  run(T,T/'scripts/refresh_job_readiness.py','--write',expect={0})
  g=json.loads((T/'planning/execution/JOB-GRAPH.json').read_text()); j2=next(x for x in g['jobs'] if x['id']=='J2')
  if j2.get('status')!='READY': errors.append('IMPLEMENTED_UNVERIFIED did not release IMPLEMENTATION dependency')
  # Direct protected-state edit must be detected.
  g['jobs'][0]['status']='DONE'; (T/'planning/execution/JOB-GRAPH.json').write_text(json.dumps(g,indent=2)+'\n'); run(T,T/'scripts/validate_control_mutation.py',expect={2})
  # Tri-state review: unverifiable requires followup.
  run(T,T/'scripts/record_review_verdict.py','--requirement','REQ','--candidate-sha','SHA','--oracle','O','--verifier-profile','blind','--verdict','UNVERIFIABLE',expect={2})
  # Planning artifact graph and decision coverage structural gates.
  run(T,T/'scripts/validate_planning_artifact_graph.py',expect={0}); run(T,T/'scripts/validate_decision_coverage.py',expect={0})
if errors:
 print('V59_CONTROL_PLANE_QA_FAIL'); [print('-',x) for x in errors]; raise SystemExit(2)
print('V59_CONTROL_PLANE_QA_PASS')
