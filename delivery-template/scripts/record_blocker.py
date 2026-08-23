#!/usr/bin/env python3
from pathlib import Path
import argparse,json,datetime
R=Path(__file__).resolve().parents[1]
B=R/'planning/execution/BLOCKERS.json'; D=R/'planning/execution/DEFERRED-VALIDATION.json'; G=R/'planning/execution/JOB-GRAPH.json'
IMPLEMENTATION_SATISFIED={'IMPLEMENTED_UNVERIFIED','VERIFYING','DONE'}; VERIFIED_SATISFIED={'DONE'}
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def deps(job):
    out=[]
    for d in job.get('dependencies') or []:
        if isinstance(d,str): out.append((d,'IMPLEMENTATION'))
        elif isinstance(d,dict) and d.get('job_id'): out.append((d['job_id'],str(d.get('gate','IMPLEMENTATION')).upper()))
    return out
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('id'); ap.add_argument('--class',dest='klass',choices=['EXECUTION_BLOCKER','VERIFICATION_BLOCKER'],required=True)
    ap.add_argument('--scope',choices=['JOB','SUBGRAPH','GLOBAL'],default='JOB'); ap.add_argument('--reason',required=True)
    ap.add_argument('--jobs',default=''); ap.add_argument('--requirements',default=''); ap.add_argument('--validation',default=''); ap.add_argument('--requires-user',action='store_true')
    a=ap.parse_args(); jobs=[x for x in a.jobs.split(',') if x]; reqs=[x for x in a.requirements.split(',') if x]
    b=load(B); g=load(G); now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    if any(x.get('id')==a.id and x.get('status') not in {'RESOLVED','WAIVED'} for x in b.get('blockers',[]) if isinstance(x,dict)):
        print('BLOCKER_ID_ALREADY_ACTIVE'); return 2
    if a.klass=='EXECUTION_BLOCKER' and a.scope=='GLOBAL':
        js=[x for x in g.get('jobs',[]) if isinstance(x,dict)]; by={x.get('id'):x for x in js if x.get('id')}; active=[x for x in b.get('blockers',[]) if isinstance(x,dict) and x.get('status') not in {'RESOLVED','WAIVED'}]
        ready=[]
        for x in js:
            jid=x.get('id')
            if not jid or not x.get('required',True) or jid in jobs or x.get('status') not in {'PLANNED','BLOCKED','READY'}: continue
            blocked=any(z.get('class')=='EXECUTION_BLOCKER' and (z.get('scope')=='GLOBAL' or jid in (z.get('affected_job_ids') or [])) for z in active)
            if blocked: continue
            okay=True
            for did,gate in deps(x):
                ds=(by.get(did) or {}).get('status'); sat=VERIFIED_SATISFIED if gate=='VERIFIED' else IMPLEMENTATION_SATISFIED
                if ds not in sat: okay=False; break
            if okay: ready.append(jid)
        if ready:
            print('GLOBAL_EXECUTION_BLOCKER_DENIED_READY_WORK_EXISTS '+','.join(ready)); return 2
    item={'id':a.id,'class':a.klass,'scope':a.scope,'status':'OPEN','reason':a.reason,'affected_job_ids':jobs,'requirement_ids':reqs,'requires_user':bool(a.requires_user),'created_at':now,'updated_at':now}
    b.setdefault('blockers',[]).append(item); b['updated_at']=now; B.write_text(json.dumps(b,indent=2)+'\n',encoding='utf-8')
    if a.klass=='VERIFICATION_BLOCKER':
        d=load(D); d.setdefault('items',[]).append({'id':'VAL-'+a.id,'blocker_id':a.id,'requirement_ids':reqs,'job_ids':jobs,'validation_steps':[x for x in a.validation.split('|') if x],'requires_user':bool(a.requires_user),'required_for_completion':True,'status':'PENDING','created_at':now,'updated_at':now}); d['status']='PENDING'; d['updated_at']=now; D.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
        print('VERIFICATION_BLOCKER_RECORDED_CONTINUE_READY_WORK')
    else: print('EXECUTION_BLOCKER_RECORDED_SCOPED')
    return 0
if __name__=='__main__': raise SystemExit(main())
