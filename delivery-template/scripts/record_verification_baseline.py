#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,subprocess,sys,uuid
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
P='planning/execution/VERIFICATION-BASELINES.json'
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--job',required=True); ap.add_argument('--phase',choices=['PRE','POST'],required=True); ap.add_argument('--command',required=True); ap.add_argument('--expected-revision',type=int); a=ap.parse_args()
 try: cs.assert_revision(a.expected_revision)
 except Exception as e: print('VERIFICATION_BASELINE_DENIED',e); return 3
 cp=subprocess.run(a.command,shell=True,cwd=R,text=True,capture_output=True); raw=(cp.stdout or '')+'\n'+(cp.stderr or ''); ts=datetime.datetime.now(datetime.timezone.utc).isoformat(); head=None
 try: head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True,stderr=subprocess.DEVNULL).strip()
 except: pass
 d=cs.load_json(P); item={'id':'VER-'+uuid.uuid4().hex[:12],'job_id':a.job,'phase':a.phase,'command':a.command,'exit_code':cp.returncode,'output_sha256':hashlib.sha256(raw.encode()).hexdigest(),'git_head':head,'at':ts}; d.setdefault('baselines',{}).setdefault(a.job,{})[a.phase]=item; d['updated_at']=ts; cs.atomic_json(P,d); cs.seal('RECORD_VERIFICATION_BASELINE',actor='verifier',paths=[],event={'type':'VERIFICATION_BASELINE_RECORDED','job_id':a.job,'phase':a.phase,'exit_code':cp.returncode}); print(json.dumps(item,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
