#!/usr/bin/env python3
from pathlib import Path
import argparse,json,datetime,subprocess,sys
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
P='planning/execution/LOOP-STATE.json'
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--loop',required=True); ap.add_argument('--strategy',required=True); ap.add_argument('--failure-signature'); ap.add_argument('--progress',choices=['AUTO','YES','NO'],default='AUTO'); ap.add_argument('--expected-revision',type=int); a=ap.parse_args()
 try: cs.assert_revision(a.expected_revision)
 except Exception as e: print('LOOP_ATTEMPT_DENIED',e); return 3
 d=cs.load_json(P); hist=d.get('strategy_history') or []
 cp=subprocess.run([sys.executable,str(R/'scripts/progress_signature.py')],cwd=R,text=True,capture_output=True)
 if cp.returncode!=0: print('PROGRESS_SIGNATURE_FAIL'); return 2
 sig=json.loads(cp.stdout); cur=sig.get('signature'); prev=d.get('progress_signature'); auto_progress=(prev is None or cur!=prev)
 progress=auto_progress if a.progress=='AUTO' else a.progress=='YES'
 same_failure=bool(a.failure_signature and a.failure_signature==d.get('failure_signature')); last_strategy=d.get('strategy')
 if not progress and same_failure and last_strategy==a.strategy:
  print('NO_PROGRESS_SAME_STRATEGY_FORBIDDEN'); return 2
 ts=datetime.datetime.now(datetime.timezone.utc).isoformat(); hist.append({'loop':a.loop,'strategy':a.strategy,'failure_signature':a.failure_signature,'progress':'YES' if progress else 'NO','progress_signature':cur,'objective':sig,'at':ts})
 d.update({'version':'5.9','active_loop':a.loop,'attempt':int(d.get('attempt') or 0)+1,'strategy':a.strategy,'failure_signature':a.failure_signature,'previous_progress_signature':prev,'progress_signature':cur,'progress_delta':'MEANINGFUL' if progress else 'NO_PROGRESS','same_strategy_allowed':progress or not same_failure,'strategy_history':hist[-30:],'last_meaningful_progress':ts if progress else d.get('last_meaningful_progress'),'updated_at':ts})
 cs.atomic_json(P,d); rec=cs.seal('RECORD_LOOP_ATTEMPT',actor='orchestrator',paths=[P],event={'type':'LOOP_ATTEMPT','loop':a.loop,'strategy':a.strategy,'progress':'YES' if progress else 'NO','failure_signature':a.failure_signature})
 print(json.dumps({'status':'LOOP_ATTEMPT_RECORDED','progress':'YES' if progress else 'NO','progress_signature':cur,'control_revision':rec['revision']},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
