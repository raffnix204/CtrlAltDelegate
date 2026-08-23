#!/usr/bin/env python3
from pathlib import Path
import argparse,json,subprocess,sys,yaml
R=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--harness'); a=ap.parse_args(); g=json.loads((R/'planning/execution/JOB-GRAPH.json').read_text()); ready=[x.get('id') for x in g.get('jobs',[]) if isinstance(x,dict) and x.get('required',True) and x.get('status')=='READY']; loop=json.loads((R/'planning/execution/LOOP-STATE.json').read_text()); progress=loop.get('progress_delta')=='MEANINGFUL'
 conf=yaml.safe_load((R/'config/HARNESS-CONFORMANCE.yaml').read_text()) or {}; row=(conf.get('harnesses') or {}).get(a.harness,{}) if a.harness else {}; supported=bool(row.get('blocking_stop_hook'))
 if ready and progress:
  print(json.dumps({'decision':'BLOCK_STOP' if supported else 'ADVISORY_CONTINUE','ready_jobs':ready,'progress':True,'enforcement':'ENFORCED' if supported else 'ADVISORY'},indent=2)); return 2 if supported else 3
 if ready and not progress:
  print(json.dumps({'decision':'ALLOW_STOP_FOR_RECOVERY','ready_jobs':ready,'progress':False,'reason':'stalled_or_unproven_progress'},indent=2)); return 0
 print(json.dumps({'decision':'ALLOW_STOP','ready_jobs':ready},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
