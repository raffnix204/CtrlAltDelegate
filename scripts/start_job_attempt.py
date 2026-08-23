#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,sys,uuid
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('job_id'); ap.add_argument('--worker',required=True); ap.add_argument('--claim-token',required=True); ap.add_argument('--brief-sha256',required=True); ap.add_argument('--base-sha',required=True); ap.add_argument('--attempt-id'); ap.add_argument('--expected-revision',type=int); a=ap.parse_args()
 try: cs.assert_revision(a.expected_revision)
 except Exception as e: print('ATTEMPT_START_DENIED',e); return 3
 claims=cs.load_json('planning/execution/WORKER-CLAIMS.json'); c=(claims.get('claims') or {}).get(a.job_id); th=hashlib.sha256(a.claim_token.encode()).hexdigest()
 if not c or c.get('status')!='ACTIVE' or c.get('worker_id')!=a.worker or c.get('token_hash')!=th: print('ATTEMPT_START_DENIED_CLAIM_MISMATCH'); return 2
 st=cs.load_json('planning/execution/ATTEMPT-STATE.json'); active=(st.get('active_by_job') or {}).get(a.job_id)
 if active: print('ATTEMPT_START_DENIED_ALREADY_ACTIVE '+active); return 2
 aid=a.attempt_id or ('ATT-'+a.job_id+'-'+uuid.uuid4().hex[:8]); ts=datetime.datetime.now(datetime.timezone.utc).isoformat()
 att={'attempt_id':aid,'job_id':a.job_id,'worker_id':a.worker,'claim_token_hash':th,'brief_sha256':a.brief_sha256,'base_sha':a.base_sha,'status':'RUNNING','started_at':ts,'settled_at':None,'result_path':None}
 st.setdefault('attempts',{})[aid]=att; st.setdefault('active_by_job',{})[a.job_id]=aid; st['version']='5.9'; st['updated_at']=ts; cs.atomic_json('planning/execution/ATTEMPT-STATE.json',st)
 cs.append_jsonl('planning/execution/JOB-ATTEMPTS.jsonl',{'version':'5.9','event':'ATTEMPT_STARTED',**att})
 g=cs.load_json('planning/execution/JOB-GRAPH.json'); job=next((x for x in g.get('jobs',[]) if x.get('id')==a.job_id),None)
 if not job: print('ATTEMPT_START_DENIED_JOB_NOT_FOUND'); return 2
 job['status']='RUNNING'; job['active_attempt_id']=aid; job['updated_at']=ts; g['updated_at']=ts; g['state_revision']=int(g.get('state_revision') or 0)+1; cs.atomic_json('planning/execution/JOB-GRAPH.json',g)
 rec=cs.seal('START_JOB_ATTEMPT',actor=a.worker,paths=['planning/execution/ATTEMPT-STATE.json','planning/execution/JOB-GRAPH.json'],event={'type':'ATTEMPT_STARTED','job_id':a.job_id,'attempt_id':aid,'worker_id':a.worker})
 print(json.dumps({'status':'ATTEMPT_RUNNING','attempt_id':aid,'control_revision':rec['revision']},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
