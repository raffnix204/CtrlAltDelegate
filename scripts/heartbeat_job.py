#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,sys,yaml
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('job_id'); ap.add_argument('--worker',required=True); ap.add_argument('--claim-token',required=True); ap.add_argument('--expected-revision',type=int); a=ap.parse_args()
 try: cs.assert_revision(a.expected_revision)
 except Exception as e: print('HEARTBEAT_DENIED',e); return 3
 d=cs.load_json('planning/execution/WORKER-CLAIMS.json'); c=(d.get('claims') or {}).get(a.job_id); th=hashlib.sha256(a.claim_token.encode()).hexdigest()
 if not c or c.get('status')!='ACTIVE' or c.get('worker_id')!=a.worker or c.get('token_hash')!=th: print('HEARTBEAT_DENIED_CLAIM_MISMATCH'); return 2
 pol=yaml.safe_load((R/'config/EXECUTION-CONTROL-POLICY.yaml').read_text()) or {}; sec=int(pol.get('claim',{}).get('heartbeat_extension_seconds',900)); now=datetime.datetime.now(datetime.timezone.utc)
 c['heartbeat_at']=now.isoformat(); c['lease_expires_at']=(now+datetime.timedelta(seconds=sec)).isoformat(); d['updated_at']=now.isoformat(); cs.atomic_json('planning/execution/WORKER-CLAIMS.json',d)
 rec=cs.seal('HEARTBEAT_JOB',actor=a.worker,paths=['planning/execution/WORKER-CLAIMS.json'],event={'type':'JOB_HEARTBEAT','job_id':a.job_id,'worker_id':a.worker})
 print(json.dumps({'status':'HEARTBEAT_OK','lease_expires_at':c['lease_expires_at'],'control_revision':rec['revision']},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
