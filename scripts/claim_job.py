#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,secrets,subprocess,sys,yaml
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts'))
import control_state as cs

def iso_after(sec): return (datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(seconds=sec)).isoformat()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('job_id'); ap.add_argument('--worker',required=True); ap.add_argument('--expected-revision',type=int); ap.add_argument('--lease-seconds',type=int); ap.add_argument('--skip-reconcile',action='store_true'); a=ap.parse_args()
 if not a.skip_reconcile:
  rr=subprocess.run([sys.executable,str(R/'scripts/reconcile_execution_state.py'),'--pre-dispatch'],cwd=R,text=True,capture_output=True)
  if rr.returncode!=0: print('CLAIM_DENIED_RECONCILIATION'); print(rr.stdout.strip()); return 2
 try: cs.assert_revision(a.expected_revision)
 except Exception as e: print('CLAIM_DENIED',e); return 3
 g=cs.load_json('planning/execution/JOB-GRAPH.json'); claims=cs.load_json('planning/execution/WORKER-CLAIMS.json')
 job=next((x for x in g.get('jobs',[]) if isinstance(x,dict) and x.get('id')==a.job_id),None)
 if not job: print('CLAIM_DENIED_JOB_NOT_FOUND'); return 2
 if job.get('status') not in {'READY','CLAIMED'}: print('CLAIM_DENIED_JOB_NOT_READY',job.get('status')); return 2
 cur=(claims.get('claims') or {}).get(a.job_id)
 t=datetime.datetime.now(datetime.timezone.utc)
 if cur and cur.get('status')=='ACTIVE':
  try: exp=datetime.datetime.fromisoformat(cur['lease_expires_at'])
  except Exception: exp=t+datetime.timedelta(days=1)
  if exp>t: print('CLAIM_DENIED_ALREADY_ACTIVE worker='+str(cur.get('worker_id'))); return 4
  print('CLAIM_DENIED_STALE_CLAIM_REQUIRES_RECONCILIATION'); return 4
 pol=yaml.safe_load((R/'config/EXECUTION-CONTROL-POLICY.yaml').read_text()) or {}; sec=a.lease_seconds or int(pol.get('claim',{}).get('default_lease_seconds',900))
 token=secrets.token_urlsafe(24); token_hash=hashlib.sha256(token.encode()).hexdigest(); ts=now()
 claim={'job_id':a.job_id,'worker_id':a.worker,'token_hash':token_hash,'status':'ACTIVE','claimed_at':ts,'heartbeat_at':ts,'lease_expires_at':iso_after(sec),'control_revision':cs.state().get('revision')}
 claims.setdefault('claims',{})[a.job_id]=claim; claims['version']='5.9'; claims['updated_at']=ts; cs.atomic_json('planning/execution/WORKER-CLAIMS.json',claims)
 job['status']='CLAIMED'; job['claimed_by']=a.worker; job['updated_at']=ts; g['version']='5.9'; g['state_revision']=int(g.get('state_revision') or 0)+1; g['updated_at']=ts; cs.atomic_json('planning/execution/JOB-GRAPH.json',g)
 rec=cs.seal('CLAIM_JOB',actor=a.worker,paths=['planning/execution/WORKER-CLAIMS.json','planning/execution/JOB-GRAPH.json'],event={'type':'JOB_CLAIMED','job_id':a.job_id,'worker_id':a.worker,'token_hash':token_hash})
 print(json.dumps({'status':'CLAIMED','job_id':a.job_id,'worker_id':a.worker,'claim_token':token,'lease_expires_at':claim['lease_expires_at'],'control_revision':rec['revision']},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
