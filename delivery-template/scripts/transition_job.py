#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys,datetime,yaml
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
ALLOWED={'PLANNED','BLOCKED','READY','CLAIMED','RUNNING','IMPLEMENTED_UNVERIFIED','VERIFYING','DONE','FAILED','CANCELLED'}
TRANSITIONS={
 'PLANNED':{'READY','BLOCKED','CANCELLED'},'BLOCKED':{'READY','CANCELLED'},'READY':{'CLAIMED','BLOCKED','CANCELLED'},'CLAIMED':{'RUNNING','READY','BLOCKED','CANCELLED'},'RUNNING':{'IMPLEMENTED_UNVERIFIED','VERIFYING','FAILED','BLOCKED','CANCELLED'},'IMPLEMENTED_UNVERIFIED':{'VERIFYING','DONE','BLOCKED','FAILED','CANCELLED'},'VERIFYING':{'DONE','IMPLEMENTED_UNVERIFIED','FAILED','BLOCKED'},'FAILED':{'READY','BLOCKED','CANCELLED'},'DONE':set(),'CANCELLED':set()}
def load(rel): return json.loads((R/rel).read_text(encoding='utf-8'))
def validate_target(j,target):
 ev=load('planning/execution/EVIDENCE-INDEX.json'); conv=load('planning/execution/CONVERGENCE-MATRIX.json'); bl=load('planning/execution/BLOCKERS.json'); pr=load('planning/execution/PROVIDER-ATTESTATIONS.json'); journeys=yaml.safe_load((R/'planning/acceptance/USER-JOURNEY-ORACLES.yaml').read_text(encoding='utf-8')) or {}; policy=yaml.safe_load((R/'config/PRODUCT-COMPLETION-POLICY.yaml').read_text(encoding='utf-8')) or {}; real_types=set(policy.get('real_evidence_types') or []); candidate=conv.get('candidate_sha') or ev.get('candidate_sha'); em={x.get('id'):x for x in ev.get('entries',[]) if isinstance(x,dict) and x.get('id')}; active=[b for b in bl.get('blockers') or [] if isinstance(b,dict) and b.get('status') not in {'RESOLVED','WAIVED'}]; jid=j.get('id'); exec_blocked=[b for b in active if b.get('class')=='EXECUTION_BLOCKER' and (b.get('scope')=='GLOBAL' or jid in (b.get('affected_job_ids') or []))]; verification_blocked=[b for b in active if b.get('class')=='VERIFICATION_BLOCKER' and jid in (b.get('affected_job_ids') or [])]; errs=[]
 def check(ids,required=()):
  got=set(); loc=[]
  for eid in ids or []:
   x=em.get(eid)
   if not x or x.get('status')!='PASS': loc.append('evidence not PASS: '+str(eid)); continue
   if candidate and x.get('sha')!=candidate and not x.get('scope_independent_after_sha',False): loc.append('evidence stale: '+str(eid))
   if x.get('type'): got.add(x.get('type'))
  miss=set(required or [])-got
  if miss: loc.append('missing evidence types: '+','.join(sorted(miss)))
  return loc,got
 if target in {'IMPLEMENTED_UNVERIFIED','VERIFYING','DONE'} and exec_blocked: errs.extend('execution blocker unresolved: '+str(x.get('id')) for x in exec_blocked)
 if target=='IMPLEMENTED_UNVERIFIED':
  if not (j.get('implementation_complete') is True or j.get('implementation_status')=='COMPLETE'): errs.append('implementation_complete/implementation_status COMPLETE required')
  ids=j.get('implementation_evidence_ids') or j.get('evidence_ids') or []
  if not (ids or j.get('implementation_evidence_not_applicable_reason') or j.get('evidence_not_applicable_reason')): errs.append('implementation evidence missing without N/A reason')
  ee,_=check(ids); errs.extend(ee)
 if target=='DONE':
  acceptance=j.get('acceptance') or []
  if not acceptance: errs.append('acceptance missing')
  if any(not isinstance(x,dict) or x.get('status') not in {'PASS','SATISFIED'} for x in acceptance): errs.append('acceptance incomplete')
  ids=j.get('evidence_ids') or []
  if not (ids or j.get('evidence_not_applicable_reason')): errs.append('evidence missing without N/A reason')
  ee,_=check(ids,j.get('required_evidence_types') or []); errs.extend(ee)
  jm={x.get('id'):x for x in journeys.get('journeys',[]) if isinstance(x,dict) and x.get('id')}
  for qid in j.get('required_journey_ids') or []:
   x=jm.get(qid)
   if not x or x.get('status')!='PASS': errs.append('journey not PASS: '+qid); continue
   need=set(x.get('required_evidence_types') or []); need=need or ({'USER_JOURNEY_REAL'} if x.get('final_real_required') else set()); je,jgot=check(x.get('evidence_ids') or [],need); errs.extend('journey '+qid+': '+z for z in je)
   if x.get('final_real_required') and not (jgot & real_types): errs.append('journey lacks real evidence: '+qid)
  consumer_types={'INTEGRATION_REAL','RUNTIME_REAL','BROWSER_REAL','NATIVE_RUNTIME_REAL','NETWORK_REAL','USER_JOURNEY_REAL'}
  for pid in j.get('required_provider_ids') or []:
   x=(pr.get('providers') or {}).get(pid) or {}
   if x.get('status')!='CONSUMER_VERIFIED': errs.append('provider not CONSUMER_VERIFIED: '+pid); continue
   pe,got=check(x.get('evidence_ids') or [],{'PROVIDER_REAL'}); errs.extend('provider '+pid+': '+z for z in pe)
   if not (got & consumer_types): errs.append('provider lacks consumer-runtime evidence: '+pid)
  if verification_blocked: errs.extend('verification blocker unresolved: '+str(x.get('id')) for x in verification_blocked)
 return errs

def main():
 ap=argparse.ArgumentParser(description='Fail-closed CtrlAltDelegate job transition. Direct manual status edits are non-authoritative.'); ap.add_argument('job_id'); ap.add_argument('status',choices=sorted(ALLOWED)); ap.add_argument('--write',action='store_true'); ap.add_argument('--revalidate-only',action='store_true'); ap.add_argument('--expected-revision',type=int); a=ap.parse_args()
 if not a.revalidate_only:
  drift=cs.verify_seal()
  if drift: print('JOB_TRANSITION_DENIED_CONTROL_DRIFT'); [print('-',x) for x in drift]; return 2
  try: cs.assert_revision(a.expected_revision)
  except Exception as e: print('JOB_TRANSITION_DENIED',e); return 3
 g=load('planning/execution/JOB-GRAPH.json'); jobs=[x for x in g.get('jobs',[]) if isinstance(x,dict) and x.get('id')==a.job_id]
 if not jobs: print('JOB_NOT_FOUND'); return 2
 j=jobs[0]; target=a.status; errs=[]
 if not a.revalidate_only and target!=j.get('status') and target not in TRANSITIONS.get(j.get('status'),set()): errs.append(f'illegal transition {j.get("status")} -> {target}')
 errs.extend(validate_target(j,target))
 if errs: print('JOB_TRANSITION_DENIED'); [print('-',x) for x in errs]; return 2
 if a.revalidate_only: print('JOB_REVALIDATION_PASS'); return 0
 if a.write:
  ts=datetime.datetime.now(datetime.timezone.utc).isoformat(); old=j.get('status'); j['status']=target; j['updated_at']=ts
  if target=='IMPLEMENTED_UNVERIFIED': j['implementation_status']='COMPLETE'; j['verification_status']=j.get('verification_status') or 'PENDING'
  elif target=='DONE': j['implementation_status']='COMPLETE'; j['verification_status']='PASS'
  g['version']='5.9'; g['state_revision']=int(g.get('state_revision') or 0)+1; g['updated_at']=ts; cs.atomic_json('planning/execution/JOB-GRAPH.json',g); rec=cs.seal('TRANSITION_JOB',actor='orchestrator',paths=['planning/execution/JOB-GRAPH.json'],event={'type':'JOB_TRANSITION','job_id':a.job_id,'from':old,'to':target}); print('JOB_TRANSITION_ALLOWED_AND_WRITTEN revision='+str(rec['revision']))
 else: print('JOB_TRANSITION_ALLOWED')
 return 0
if __name__=='__main__': raise SystemExit(main())
