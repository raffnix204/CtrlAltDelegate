#!/usr/bin/env python3
from pathlib import Path
import argparse,json
R=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('job_id'); a=ap.parse_args(); d=json.loads((R/'planning/execution/VERIFICATION-BASELINES.json').read_text()); x=(d.get('baselines') or {}).get(a.job_id) or {}; pre=x.get('PRE'); post=x.get('POST')
 if not pre or not post: print('VERIFICATION_ATTRIBUTION_UNAVAILABLE'); return 3
 p=pre.get('exit_code')==0; q=post.get('exit_code')==0
 verdict='CLEAN' if p and q else 'REGRESSED' if p and not q else 'FIXED_BASELINE' if not p and q else 'BASELINE_BROKEN'
 print(json.dumps({'job_id':a.job_id,'classification':verdict,'pre_exit':pre.get('exit_code'),'post_exit':post.get('exit_code')},indent=2)); return 2 if verdict=='REGRESSED' else 0
if __name__=='__main__': raise SystemExit(main())
