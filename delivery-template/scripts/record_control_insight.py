#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,json,sys
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
EVENTS={'GATE_TRIGGERED','FINDING_FOUND','FALSE_POSITIVE','REPAIR_REQUIRED','REPAIR_SUCCEEDED','RETRY','JIT_SKILL_INJECTED','RECONCILIATION_REPAIR','STOP_GATE_BLOCKED','RUNTIME_FAILURE','VERIFIER_DISAGREEMENT'}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--event',choices=sorted(EVENTS),required=True); ap.add_argument('--mechanism',required=True); ap.add_argument('--job'); ap.add_argument('--detail'); a=ap.parse_args(); row={'version':'5.9','event':a.event,'mechanism':a.mechanism,'job_id':a.job,'detail':a.detail,'at':datetime.datetime.now(datetime.timezone.utc).isoformat()}; cs.append_jsonl('planning/execution/CONTROL-INSIGHTS.jsonl',row); print('CONTROL_INSIGHT_RECORDED'); return 0
if __name__=='__main__': raise SystemExit(main())
