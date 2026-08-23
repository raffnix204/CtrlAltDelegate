#!/usr/bin/env python3
from pathlib import Path
import argparse,fnmatch,json,subprocess
R=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('job_id'); ap.add_argument('--base'); a=ap.parse_args(); g=json.loads((R/'planning/execution/JOB-GRAPH.json').read_text()); j=next((x for x in g.get('jobs',[]) if isinstance(x,dict) and x.get('id')==a.job_id),None)
 if not j: print('ORACLE_INTEGRITY_FAIL job not found'); return 2
 cmd=['git','diff','--name-only'];
 if a.base: cmd.append(a.base+'...HEAD')
 try: paths=subprocess.check_output(cmd,cwd=R,text=True,stderr=subprocess.DEVNULL).splitlines()
 except: paths=[]
 testish=[p for p in paths if any(tok in p.lower() for tok in ['/test','/spec','tests/','specs/','.test.','.spec.'])]
 policy=j.get('oracle_policy') or {}; allowed=policy.get('allowed_test_paths') or []; allow_all=bool(policy.get('allow_test_changes'))
 denied=[] if allow_all else [p for p in testish if not any(fnmatch.fnmatch(p,pat) for pat in allowed)]
 if denied: print('ORACLE_INTEGRITY_FAIL unexpected test/oracle mutation'); [print('-',p) for p in denied]; return 2
 print('ORACLE_INTEGRITY_PASS changed_test_paths='+str(len(testish))); return 0
if __name__=='__main__': raise SystemExit(main())
