#!/usr/bin/env python3
from pathlib import Path
import argparse,json,datetime,sys
R=Path(__file__).resolve().parents[1]; P=R/'planning/execution/LOOP-STATE.json'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--loop',required=True); ap.add_argument('--strategy',required=True); ap.add_argument('--failure-signature'); ap.add_argument('--progress',choices=['YES','NO'],required=True); a=ap.parse_args()
    d=json.loads(P.read_text()); hist=d.get('strategy_history') or []
    same_failure=a.failure_signature and a.failure_signature==d.get('failure_signature')
    last_strategy=d.get('strategy')
    if a.progress=='NO' and same_failure and last_strategy==a.strategy:
        print('NO_PROGRESS_SAME_STRATEGY_FORBIDDEN'); return 2
    hist.append({'loop':a.loop,'strategy':a.strategy,'failure_signature':a.failure_signature,'progress':a.progress,'at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    d.update({'version':'5.8.2','active_loop':a.loop,'attempt':int(d.get('attempt') or 0)+1,'strategy':a.strategy,'failure_signature':a.failure_signature,'progress_delta':'MEANINGFUL' if a.progress=='YES' else 'NO_PROGRESS','same_strategy_allowed':not (a.progress=='NO'),'strategy_history':hist[-20:],'updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    P.write_text(json.dumps(d,indent=2)+'\n'); print('LOOP_ATTEMPT_RECORDED'); return 0
if __name__=='__main__': raise SystemExit(main())
