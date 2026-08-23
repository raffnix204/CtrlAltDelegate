#!/usr/bin/env python3
from pathlib import Path
import argparse, json, datetime
R=Path(__file__).resolve().parents[1]
G=R/'planning/execution/JOB-GRAPH.json'; B=R/'planning/execution/BLOCKERS.json'
IMPLEMENTATION_SATISFIED={'IMPLEMENTED_UNVERIFIED','VERIFYING','DONE'}
VERIFIED_SATISFIED={'DONE'}
TERMINAL_OR_ACTIVE={'CLAIMED','RUNNING','IMPLEMENTED_UNVERIFIED','VERIFYING','DONE','FAILED','CANCELLED'}
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def deps(job):
    out=[]
    for d in job.get('dependencies') or []:
        if isinstance(d,str): out.append((d,'IMPLEMENTATION'))
        elif isinstance(d,dict) and d.get('job_id'): out.append((d['job_id'],str(d.get('gate','IMPLEMENTATION')).upper()))
    return out
def main():
    ap=argparse.ArgumentParser(description='Derive READY/BLOCKED job states without treating verification-only blockers as execution stops.')
    ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    g=load(G); b=load(B); jobs=[x for x in g.get('jobs',[]) if isinstance(x,dict)]; by={x.get('id'):x for x in jobs if x.get('id')}
    blockers=[x for x in b.get('blockers',[]) if isinstance(x,dict) and x.get('status') not in {'RESOLVED','WAIVED'}]
    changed=[]; derived_ready=[]
    for j in jobs:
        jid=j.get('id'); cur=j.get('status','PLANNED')
        if not jid or cur in TERMINAL_OR_ACTIVE: continue
        exec_blocked=any(x.get('class')=='EXECUTION_BLOCKER' and (x.get('scope')=='GLOBAL' or jid in (x.get('affected_job_ids') or [])) for x in blockers)
        dep_block=[]
        for did,gate in deps(j):
            d=by.get(did); ds=(d or {}).get('status')
            sat=VERIFIED_SATISFIED if gate=='VERIFIED' else IMPLEMENTATION_SATISFIED
            if not d or ds not in sat: dep_block.append({'job_id':did,'gate':gate,'status':ds or 'MISSING'})
        new='BLOCKED' if exec_blocked or dep_block else 'READY'
        if new=='READY': derived_ready.append(jid)
        if new!=cur:
            changed.append({'job_id':jid,'from':cur,'to':new,'dependency_blockers':dep_block,'execution_blocked':exec_blocked})
            if a.write:
                j['status']=new; j['readiness_reason']='EXECUTION_BLOCKER' if exec_blocked else ('DEPENDENCY_WAIT' if dep_block else 'DEPENDENCIES_SATISFIED')
    if a.write and changed:
        now=datetime.datetime.now(datetime.timezone.utc).isoformat(); g['updated_at']=now; G.write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','derived_ready':derived_ready,'changes':changed,'written':bool(a.write)},indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
