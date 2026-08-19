#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, datetime
R=Path(__file__).resolve().parents[1]
DEFAULT=[
'planning/PROJECT.md','planning/REQUIREMENTS.md','planning/discovery/DISCOVERY-STATE.md','planning/discovery/TECHNICAL-PREFERENCES.yaml',
'planning/context/PLANNING-SKILL-STATE.yaml','planning/architecture/STACK-MANIFEST.yaml','planning/architecture/PROGRAM-DESIGN.md','planning/execution/EXECUTION-PROFILE.yaml',
'planning/execution/JOB-GRAPH.json','planning/execution/SKILLS-MANIFEST.yaml','config/LOOP-CONTRACTS.yaml','config/SURFACE-POLICY.yaml','config/HARNESS-CONFORMANCE.yaml']
EXTRA_DIRS=['planning/design','planning/content','planning/seo']
def digest(b): return hashlib.sha256(b).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--verify',action='store_true'); a=ap.parse_args(); out=R/'planning/execution/PLANNING-BASELINE.json'
 files={}; errors=[]
 dynamic=list(DEFAULT)
 for drel in EXTRA_DIRS:
  base=R/drel
  if base.exists():
   for p in sorted(x for x in base.rglob('*') if x.is_file()):
    rel=p.relative_to(R).as_posix()
    if rel not in dynamic: dynamic.append(rel)
 for rel in dynamic:
  p=R/rel
  if not p.is_file(): errors.append(f'missing {rel}'); continue
  files[rel]=digest(p.read_bytes())
 agg=digest('\n'.join(f'{k}:{files[k]}' for k in sorted(files)).encode())
 if a.verify:
  try: old=json.loads(out.read_text(encoding='utf-8'))
  except Exception as e: print('PLANNING_ATTEST_FAIL',e); return 2
  if old.get('aggregate_sha256')!=agg or old.get('files')!=files:
   print('PLANNING_ATTEST_DRIFT'); return 3
  print('PLANNING_ATTEST_PASS',agg); return 0
 if errors:
  print('PLANNING_ATTEST_FAIL'); [print('-',e) for e in errors]; return 2
 old=None
 try: old=json.loads(out.read_text(encoding='utf-8')).get('aggregate_sha256')
 except: pass
 data={'version':'5.7.1','status':'ATTESTED','aggregate_sha256':agg,'files':files,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'supersedes':old}
 out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8'); print('PLANNING_ATTEST_WRITTEN',agg); return 0
if __name__=='__main__': raise SystemExit(main())
