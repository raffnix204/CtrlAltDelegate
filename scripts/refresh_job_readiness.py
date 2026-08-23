#!/usr/bin/env python3
from pathlib import Path
import argparse,json,datetime,sys
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
IMPLEMENTATION_SATISFIED={'IMPLEMENTED_UNVERIFIED','VERIFYING','DONE'}
VERIFIED_SATISFIED={'DONE'}
TERMINAL_OR_ACTIVE={'CLAIMED','RUNNING','IMPLEMENTED_UNVERIFIED','VERIFYING','DONE','FAILED','CANCELLED'}
def deps(job):
 out=[]
 for d in job.get('dependencies') or []:
  if isinstance(d,str): out.append((d,'IMPLEMENTATION'))
  elif isinstance(d,dict) and d.get('job_id'): out.append((d['job_id'],str(d.get('gate','IMPLEMENTATION')).upper()))
 return out
def derive(g,b):
 jobs=[x for x in g.get('jobs',[]) if isinstance(x,dict)]; by={x.get('id'):x for x in jobs if x.get('id')}; blockers=[x for x in b.get('blockers',[]) if isinstance(x,dict) and x.get('status') not in {'RESOLVED','WAIVED'}]; changed=[]; ready=[]
 for j in jobs:
  jid=j.get('id'); cur=j.get('status','PLANNED')
  if not jid or cur in TERMINAL_OR_ACTIVE: continue
  exec_blocked=any(x.get('class')=='EXECUTION_BLOCKER' and (x.get('scope')=='GLOBAL' or jid in (x.get('affected_job_ids') or [])) for x in blockers)
  dep_block=[]
  for did,gate in deps(j):
   d=by.get(did); ds=(d or {}).get('status'); sat=VERIFIED_SATISFIED if gate=='VERIFIED' else IMPLEMENTATION_SATISFIED
   if not d or ds not in sat: dep_block.append({'job_id':did,'gate':gate,'status':ds or 'MISSING'})
  new='BLOCKED' if exec_blocked or dep_block else 'READY'
  if new=='READY': ready.append(jid)
  if new!=cur: changed.append({'job_id':jid,'from':cur,'to':new,'dependency_blockers':dep_block,'execution_blocked':exec_blocked})
 return ready,changed
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); ap.add_argument('--expected-revision',type=int); a=ap.parse_args()
 if cs.verify_seal(): print('READINESS_DENIED_CONTROL_DRIFT'); return 2
 try: cs.assert_revision(a.expected_revision)
 except Exception as e: print('READINESS_DENIED',e); return 3
 g=cs.load_json('planning/execution/JOB-GRAPH.json'); b=cs.load_json('planning/execution/BLOCKERS.json'); ready,changed=derive(g,b)
 if a.write and changed:
  ts=datetime.datetime.now(datetime.timezone.utc).isoformat(); by={x.get('id'):x for x in g.get('jobs',[]) if isinstance(x,dict)}
  for c in changed:
   j=by[c['job_id']]; j['status']=c['to']; j['readiness_reason']='EXECUTION_BLOCKER' if c['execution_blocked'] else ('DEPENDENCY_WAIT' if c['dependency_blockers'] else 'DEPENDENCIES_SATISFIED'); j['updated_at']=ts
  g['version']='5.9'; g['state_revision']=int(g.get('state_revision') or 0)+1; g['updated_at']=ts; cs.atomic_json('planning/execution/JOB-GRAPH.json',g); rec=cs.seal('REFRESH_JOB_READINESS',actor='orchestrator',paths=['planning/execution/JOB-GRAPH.json'],event={'type':'READINESS_REFRESHED','ready_jobs':ready})
 else: rec={'revision':cs.state().get('revision')}
 print(json.dumps({'status':'PASS','derived_ready':ready,'changes':changed,'written':bool(a.write and changed),'control_revision':rec['revision']},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
