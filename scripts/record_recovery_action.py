#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,json,sys,uuid
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
ACTIONS={'RETRY','REPAIR','REMEDIATE','REBRIEF','REPLAN','DEFER_VALIDATION','EXTERNAL_BLOCK','ABORT'}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--job',required=True); ap.add_argument('--attempt',required=True); ap.add_argument('--failure-signature',required=True); ap.add_argument('--failure-class',required=True); ap.add_argument('--action',choices=sorted(ACTIONS),required=True); ap.add_argument('--reason',required=True); ap.add_argument('--strategy'); ap.add_argument('--expected-revision',type=int); a=ap.parse_args()
 try: cs.assert_revision(a.expected_revision)
 except Exception as e: print('RECOVERY_DENIED',e); return 3
 rows=[]; p=R/'planning/execution/RECOVERY-ACTIONS.jsonl'
 for line in p.read_text(encoding='utf-8').splitlines():
  if line.strip():
   try: rows.append(json.loads(line))
   except: pass
 same=[x for x in rows if x.get('job_id')==a.job and x.get('failure_signature')==a.failure_signature]
 if same and a.action=='RETRY' and same[-1].get('action')=='RETRY' and same[-1].get('strategy')==a.strategy:
  print('RECOVERY_DENIED_SAME_FAILURE_SAME_RETRY_STRATEGY'); return 2
 ts=datetime.datetime.now(datetime.timezone.utc).isoformat(); rid='REC-'+uuid.uuid4().hex[:12]
 row={'version':'5.9','recovery_id':rid,'job_id':a.job,'attempt_id':a.attempt,'failure_signature':a.failure_signature,'failure_class':a.failure_class,'action':a.action,'strategy':a.strategy,'reason':a.reason,'at':ts}
 cs.append_jsonl('planning/execution/RECOVERY-ACTIONS.jsonl',row); rec=cs.seal('RECORD_RECOVERY_ACTION',actor='orchestrator',paths=[],event={'type':'RECOVERY_SELECTED','job_id':a.job,'attempt_id':a.attempt,'recovery_id':rid,'action':a.action})
 print(json.dumps({**row,'control_revision':rec['revision']},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
