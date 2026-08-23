#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,json,sys,uuid
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--subject',required=True); ap.add_argument('--decision',required=True); ap.add_argument('--why',required=True); ap.add_argument('--cost-if-wrong',required=True); ap.add_argument('--evidence',action='append',default=[]); ap.add_argument('--job'); a=ap.parse_args(); row={'version':'5.9','ruling_id':'RUL-'+uuid.uuid4().hex[:12],'subject':a.subject,'decision':a.decision,'why':a.why,'cost_if_wrong':a.cost_if_wrong,'evidence':a.evidence,'job_id':a.job,'at':datetime.datetime.now(datetime.timezone.utc).isoformat()}; cs.append_jsonl('planning/execution/RULINGS.jsonl',row); cs.append_jsonl('planning/execution/CONTROL-EVENTS.jsonl',{'version':'5.9','event_id':row['ruling_id'],'type':'RULING_RECORDED','job_id':a.job,'at':row['at']}); print(json.dumps(row,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
