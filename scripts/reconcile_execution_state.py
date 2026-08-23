#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,json,subprocess,sys
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs

def log(row): cs.append_jsonl('planning/execution/RECONCILIATION-LOG.jsonl',{'version':'5.9','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),**row})
def parse_exp(s):
 try:return datetime.datetime.fromisoformat(s)
 except:return None
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--pre-dispatch',action='store_true'); a=ap.parse_args(); detected=[]; repaired=[]; blockers=[]
 # 1. Integrity: derived snapshot may be safely rebuilt; authority/controller state may not.
 drift=cs.verify_seal()
 snapshot_only=bool(drift) and all('planning/execution/EXECUTION-SNAPSHOT.json' in x for x in drift)
 if drift and not snapshot_only:
  blockers.extend(drift); detected.extend({'kind':'CONTROL_SURFACE_DRIFT','detail':x} for x in drift)
  log({'status':'BLOCKED','detected':detected,'repaired':[],'blockers':blockers}); print('RECONCILIATION_BLOCKED'); [print('-',x) for x in blockers]; return 2
 if snapshot_only:
  subprocess.run([sys.executable,str(R/'scripts/build_execution_snapshot.py'),'--no-seal'],cwd=R,text=True,capture_output=True)
  rec=cs.seal('RECONCILE_DERIVED_SNAPSHOT',actor='reconciler',paths=['planning/execution/EXECUTION-SNAPSHOT.json'],event={'type':'RECONCILIATION_REPAIR','kind':'SNAPSHOT_DRIFT'}); repaired.append({'kind':'SNAPSHOT_DRIFT','revision':rec['revision']})
 # 2. Claims/attempts: expired claim is safely releasable only after time expiry.
 claims=cs.load_json('planning/execution/WORKER-CLAIMS.json'); att=cs.load_json('planning/execution/ATTEMPT-STATE.json'); g=cs.load_json('planning/execution/JOB-GRAPH.json'); now=datetime.datetime.now(datetime.timezone.utc); changed=False
 for jid,c in list((claims.get('claims') or {}).items()):
  if not isinstance(c,dict) or c.get('status')!='ACTIVE': continue
  exp=parse_exp(c.get('lease_expires_at'))
  if exp and exp<=now:
   detected.append({'kind':'EXPIRED_CLAIM','job_id':jid,'worker_id':c.get('worker_id')}); c['status']='EXPIRED'; c['expired_at']=now.isoformat(); changed=True
   aid=(att.get('active_by_job') or {}).pop(jid,None)
   if aid and aid in (att.get('attempts') or {}): att['attempts'][aid]['status']='INTERRUPTED'; att['attempts'][aid]['settled_at']=now.isoformat(); cs.append_jsonl('planning/execution/JOB-ATTEMPTS.jsonl',{'version':'5.9','event':'ATTEMPT_INTERRUPTED','attempt_id':aid,'job_id':jid,'reason':'lease_expired','at':now.isoformat()})
   job=next((x for x in g.get('jobs',[]) if isinstance(x,dict) and x.get('id')==jid),None)
   if job and job.get('status') in {'CLAIMED','RUNNING'}: job['status']='READY'; job.pop('active_attempt_id',None); job['updated_at']=now.isoformat()
   repaired.append({'kind':'EXPIRED_CLAIM','job_id':jid})
 # orphan active attempt with no active matching claim
 for jid,aid in list((att.get('active_by_job') or {}).items()):
  c=(claims.get('claims') or {}).get(jid); aa=(att.get('attempts') or {}).get(aid)
  if aa and aa.get('status')=='RUNNING' and (not c or c.get('status')!='ACTIVE' or c.get('worker_id')!=aa.get('worker_id')):
   detected.append({'kind':'ORPHAN_ATTEMPT','job_id':jid,'attempt_id':aid}); aa['status']='INTERRUPTED'; aa['settled_at']=now.isoformat(); att['active_by_job'].pop(jid,None); changed=True; repaired.append({'kind':'ORPHAN_ATTEMPT','job_id':jid,'attempt_id':aid})
 if changed:
  claims['updated_at']=now.isoformat(); att['updated_at']=now.isoformat(); g['updated_at']=now.isoformat(); g['state_revision']=int(g.get('state_revision') or 0)+1; cs.atomic_json('planning/execution/WORKER-CLAIMS.json',claims); cs.atomic_json('planning/execution/ATTEMPT-STATE.json',att); cs.atomic_json('planning/execution/JOB-GRAPH.json',g); cs.seal('RECONCILE_EXECUTION_OWNERSHIP',actor='reconciler',paths=['planning/execution/WORKER-CLAIMS.json','planning/execution/ATTEMPT-STATE.json','planning/execution/JOB-GRAPH.json'],event={'type':'RECONCILIATION_REPAIR','kinds':[x['kind'] for x in repaired]})
 # 3. Revalidate every DONE job through transition controller without trusting status.
 # Invalid DONE is a safe-repairable projection error: demote it, never preserve a false completion claim.
 done_repaired=[]
 g=cs.load_json('planning/execution/JOB-GRAPH.json')
 for job in [x for x in g.get('jobs',[]) if isinstance(x,dict) and x.get('status')=='DONE']:
  cp=subprocess.run([sys.executable,str(R/'scripts/transition_job.py'),job['id'],'DONE','--revalidate-only'],cwd=R,text=True,capture_output=True)
  if cp.returncode!=0:
   detected.append({'kind':'DONE_INVARIANT_VIOLATION','job_id':job['id']})
   target='IMPLEMENTED_UNVERIFIED' if (job.get('implementation_complete') is True or job.get('implementation_status')=='COMPLETE') else 'READY'
   job['status']=target; job['verification_status']='PENDING' if target=='IMPLEMENTED_UNVERIFIED' else 'NOT_STARTED'; job['reconciliation_reason']='DONE_INVARIANT_VIOLATION'; job['updated_at']=now.isoformat(); done_repaired.append({'kind':'DONE_INVARIANT_VIOLATION','job_id':job['id'],'to':target})
 if done_repaired:
  g['state_revision']=int(g.get('state_revision') or 0)+1; g['updated_at']=now.isoformat(); cs.atomic_json('planning/execution/JOB-GRAPH.json',g); cs.seal('RECONCILE_FALSE_DONE',actor='reconciler',paths=['planning/execution/JOB-GRAPH.json'],event={'type':'RECONCILIATION_REPAIR','kind':'DONE_INVARIANT_VIOLATION','jobs':[x['job_id'] for x in done_repaired]}); repaired.extend(done_repaired)
 # 4. Rebuild derived snapshot after safe repairs.
 if not blockers:
  subprocess.run([sys.executable,str(R/'scripts/build_execution_snapshot.py')],cwd=R,text=True,capture_output=True)
 status='PASS' if not blockers else 'BLOCKED'; log({'status':status,'pre_dispatch':a.pre_dispatch,'detected':detected,'repaired':repaired,'blockers':blockers})
 if blockers: print('RECONCILIATION_BLOCKED'); [print('-',x) for x in blockers]; return 2
 print(json.dumps({'status':'RECONCILIATION_PASS','detected':detected,'repaired':repaired,'pre_dispatch':a.pre_dispatch},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
