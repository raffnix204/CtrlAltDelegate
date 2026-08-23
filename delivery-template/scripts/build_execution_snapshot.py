#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,datetime,argparse,sys,hashlib
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
IMPLEMENTATION_SATISFIED={'IMPLEMENTED_UNVERIFIED','VERIFYING','DONE'}; VERIFIED_SATISFIED={'DONE'}
def load(rel,default):
 try:return json.loads((R/rel).read_text(encoding='utf-8'))
 except:return default
def git(*a):
 try:return subprocess.check_output(['git',*a],cwd=R,text=True,stderr=subprocess.DEVNULL).strip()
 except:return ''
def dependencies(job):
 out=[]
 for d in job.get('dependencies') or []:
  if isinstance(d,str):out.append((d,'IMPLEMENTATION'))
  elif isinstance(d,dict) and d.get('job_id'):out.append((d['job_id'],str(d.get('gate','IMPLEMENTATION')).upper()))
 return out
def build():
 assumption=R/'planning/execution/ASSUMPTIONS.jsonl'; assumption_count=sum(1 for line in assumption.read_text(encoding='utf-8').splitlines() if line.strip()) if assumption.exists() else 0
 j=load('planning/execution/JOB-GRAPH.json',{'jobs':[]}); b=load('planning/execution/BLOCKERS.json',{'blockers':[]}); d=load('planning/execution/DEFERRED-VALIDATION.json',{'items':[]}); e=load('planning/execution/EVIDENCE-INDEX.json',{'entries':[]}); c=load('planning/execution/CONVERGENCE-MATRIX.json',{'requirements':[]}); p=load('planning/execution/PROVIDER-ATTESTATIONS.json',{'providers':{}}); pre=load('planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json',{}); drift=load('planning/execution/PRODUCT-DRIFT-REVIEW.json',{}); claims=load('planning/execution/WORKER-CLAIMS.json',{'claims':{}}); att=load('planning/execution/ATTEMPT-STATE.json',{'attempts':{},'active_by_job':{}}); control=load('planning/execution/CONTROL-STATE.json',{})
 try:
  import yaml; journeys=yaml.safe_load((R/'planning/acceptance/USER-JOURNEY-ORACLES.yaml').read_text(encoding='utf-8')) or {}
 except: journeys={}
 jobs=[x for x in j.get('jobs') or [] if isinstance(x,dict)]; by={x.get('id'):x for x in jobs if x.get('id')}; counts={}
 for x in jobs: counts[x.get('status') or 'UNKNOWN']=counts.get(x.get('status') or 'UNKNOWN',0)+1
 blockers=b.get('blockers') or []; unresolved=[x for x in blockers if isinstance(x,dict) and x.get('status') not in {'RESOLVED','WAIVED'}]; pending=[x for x in d.get('items') or [] if isinstance(x,dict) and x.get('status') not in {'PASS','RESOLVED','WAIVED'}]
 js=journeys.get('journeys') or []; mandatory=[x for x in js if isinstance(x,dict) and x.get('mandatory')]; ready=[]
 for x in jobs:
  if not x.get('required',True) or x.get('status') not in {'PLANNED','BLOCKED','READY'}: continue
  jid=x.get('id'); exec_blocked=any(z.get('class')=='EXECUTION_BLOCKER' and (z.get('scope')=='GLOBAL' or jid in (z.get('affected_job_ids') or [])) for z in unresolved)
  if exec_blocked: continue
  okay=True
  for did,gate in dependencies(x):
   ds=(by.get(did) or {}).get('status'); sat=VERIFIED_SATISFIED if gate=='VERIFIED' else IMPLEMENTATION_SATISFIED
   if ds not in sat: okay=False; break
  if okay: ready.append(jid)
 global_exec=any(x.get('class')=='EXECUTION_BLOCKER' and x.get('scope')=='GLOBAL' for x in unresolved)
 if not jobs and not (c.get('requirements') or []): next_state='PLANNING_REQUIRED'
 elif ready: next_state='CONTINUE_OTHER_WORK' if unresolved or pending else 'CONTINUE'
 elif global_exec: next_state='EXECUTION_BLOCKED'
 elif pending or counts.get('IMPLEMENTED_UNVERIFIED',0): next_state='VALIDATION_PENDING_EXTERNAL'
 else: next_state='VERIFY_COMPLETION'
 active_claims=[x for x in (claims.get('claims') or {}).values() if isinstance(x,dict) and x.get('status')=='ACTIVE']; active_attempts=[x for x in (att.get('attempts') or {}).values() if isinstance(x,dict) and x.get('status')=='RUNNING']
 return {'version':'5.9','generated':True,'status':'CURRENT','candidate_sha':c.get('candidate_sha') or e.get('candidate_sha') or git('rev-parse','HEAD'),'git_head':git('rev-parse','HEAD'),'control_revision':control.get('revision'),'jobs':{'total':len(jobs),'by_status':counts,'derived_ready':ready},'workers':{'active_claims':len(active_claims),'active_attempts':len(active_attempts)},'blockers':{'unresolved':len(unresolved),'execution':sum(1 for x in unresolved if x.get('class')=='EXECUTION_BLOCKER'),'verification':sum(1 for x in unresolved if x.get('class')=='VERIFICATION_BLOCKER')},'validation':{'pending':len(pending)},'assumptions':{'count':assumption_count},'next_state':next_state,'evidence':{'entries':len(e.get('entries') or []),'status':e.get('status')},'convergence':{'requirements':len(c.get('requirements') or []),'status':c.get('status')},'journeys':{'total':len(js),'mandatory':len(mandatory),'mandatory_pass':sum(1 for x in mandatory if x.get('status')=='PASS')},'providers':{'count':len(p.get('providers') or {}),'consumer_verified':sum(1 for x in (p.get('providers') or {}).values() if isinstance(x,dict) and x.get('status')=='CONSUMER_VERIFIED')},'runtime_preflight':pre.get('status'),'product_drift':drift.get('status'),'updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--write-state-md',action='store_true'); ap.add_argument('--no-seal',action='store_true'); a=ap.parse_args(); snap=build(); cs.atomic_json('planning/execution/EXECUTION-SNAPSHOT.json',snap)
 if a.write_state_md:
  lines=['# Execution State — generated','',f"Candidate SHA: `{snap['candidate_sha'] or 'UNSET'}`",f"Control revision: {snap['control_revision']}",f"Jobs: {snap['jobs']['total']} — {snap['jobs']['by_status']}",f"Derived ready jobs: {', '.join(snap['jobs']['derived_ready']) or 'NONE'}",f"Active claims/attempts: {snap['workers']['active_claims']}/{snap['workers']['active_attempts']}",f"Unresolved blockers: {snap['blockers']['unresolved']} (execution {snap['blockers']['execution']}, verification {snap['blockers']['verification']})",f"Deferred validation pending: {snap['validation']['pending']}",f"Mandatory journeys passed: {snap['journeys']['mandatory_pass']}/{snap['journeys']['mandatory']}",f"Runtime preflight: {snap['runtime_preflight']}",f"Product drift review: {snap['product_drift']}",f"Next state: {snap['next_state']}",'','Do not edit this file manually; regenerate it.','']; (R/'planning/execution/STATE.md').write_text('\n'.join(lines),encoding='utf-8')
 if not a.no_seal: cs.seal('REGENERATE_EXECUTION_SNAPSHOT',actor='orchestrator',paths=['planning/execution/EXECUTION-SNAPSHOT.json'],event={'type':'EXECUTION_SNAPSHOT_REGENERATED'})
 print(json.dumps(snap,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
