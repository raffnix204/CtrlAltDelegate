#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,subprocess,sys
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('result_file'); ap.add_argument('--claim-token',required=True); ap.add_argument('--expected-revision',type=int); a=ap.parse_args(); rp=Path(a.result_file)
 vr=subprocess.run([sys.executable,str(R/'scripts/validate_worker_result.py'),str(rp)],cwd=R,text=True,capture_output=True)
 if vr.returncode!=0: print(vr.stdout.strip()); return 2
 d=json.loads(rp.read_text(encoding='utf-8')); jid=d['job_id']; aid=d['attempt_id']; wid=d['worker_id']; th=hashlib.sha256(a.claim_token.encode()).hexdigest()
 try: cs.assert_revision(a.expected_revision)
 except Exception as e: print('ATTEMPT_SETTLE_DENIED',e); return 3
 claims=cs.load_json('planning/execution/WORKER-CLAIMS.json'); c=(claims.get('claims') or {}).get(jid)
 if not c or c.get('status')!='ACTIVE' or c.get('worker_id')!=wid or c.get('token_hash')!=th: print('ATTEMPT_SETTLE_DENIED_CLAIM_MISMATCH'); return 2
 st=cs.load_json('planning/execution/ATTEMPT-STATE.json'); att=(st.get('attempts') or {}).get(aid)
 if not att or att.get('status')!='RUNNING' or att.get('job_id')!=jid or att.get('worker_id')!=wid or att.get('claim_token_hash')!=th: print('ATTEMPT_SETTLE_DENIED_ATTEMPT_MISMATCH'); return 2
 if att.get('brief_sha256')!=d.get('brief_sha256') or att.get('base_sha')!=d.get('base_sha'): print('ATTEMPT_SETTLE_DENIED_AUTHORITY_MISMATCH'); return 2
 ts=datetime.datetime.now(datetime.timezone.utc).isoformat(); out=d['outcome']
 att.update({'status':'SETTLED','settled_at':ts,'outcome':out,'result_path':str(rp),'worker_result':d}); st.get('active_by_job',{}).pop(jid,None); st['updated_at']=ts; cs.atomic_json('planning/execution/ATTEMPT-STATE.json',st)
 cs.append_jsonl('planning/execution/JOB-ATTEMPTS.jsonl',{'version':'5.9','event':'ATTEMPT_SETTLED','attempt_id':aid,'job_id':jid,'worker_id':wid,'outcome':out,'verification_status':d.get('verification_status'),'at':ts})
 c['status']='RELEASED'; c['released_at']=ts; claims['updated_at']=ts; cs.atomic_json('planning/execution/WORKER-CLAIMS.json',claims)
 g=cs.load_json('planning/execution/JOB-GRAPH.json'); job=next((x for x in g.get('jobs',[]) if x.get('id')==jid),None)
 if not job: print('ATTEMPT_SETTLE_DENIED_JOB_NOT_FOUND'); return 2
 job.pop('active_attempt_id',None); job['last_attempt_id']=aid; job['updated_at']=ts
 if d.get('implementation_status')=='COMPLETE':
  job['implementation_complete']=True; job['implementation_status']='COMPLETE'; job['implementation_evidence_ids']=d.get('evidence_ids') or []
  job['status']='VERIFYING' if d.get('verification_status')=='PASS' else 'IMPLEMENTED_UNVERIFIED'
 elif out in {'FAILED','BLOCKED'}: job['status']='BLOCKED' if out=='BLOCKED' else 'FAILED'
 else: job['status']='READY'
 g['updated_at']=ts; g['state_revision']=int(g.get('state_revision') or 0)+1; cs.atomic_json('planning/execution/JOB-GRAPH.json',g)
 rec=cs.seal('SETTLE_JOB_ATTEMPT',actor=wid,paths=['planning/execution/ATTEMPT-STATE.json','planning/execution/WORKER-CLAIMS.json','planning/execution/JOB-GRAPH.json'],event={'type':'ATTEMPT_SETTLED','job_id':jid,'attempt_id':aid,'outcome':out})
 print(json.dumps({'status':'ATTEMPT_SETTLED','job_id':jid,'attempt_id':aid,'job_status':job['status'],'control_revision':rec['revision']},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
