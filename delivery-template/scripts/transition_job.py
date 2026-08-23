#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys,datetime,yaml
R=Path(__file__).resolve().parents[1]
ALLOWED={'PLANNED','BLOCKED','READY','CLAIMED','RUNNING','IMPLEMENTED_UNVERIFIED','VERIFYING','DONE','FAILED','CANCELLED'}
def load(rel): return json.loads((R/rel).read_text(encoding='utf-8'))
def main():
    ap=argparse.ArgumentParser(description='Controlled CtrlAltDelegate job transition. DONE is fail-closed; implementation-complete work may remain IMPLEMENTED_UNVERIFIED while external proof is deferred.')
    ap.add_argument('job_id'); ap.add_argument('status',choices=sorted(ALLOWED)); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    g=load('planning/execution/JOB-GRAPH.json'); ev=load('planning/execution/EVIDENCE-INDEX.json'); conv=load('planning/execution/CONVERGENCE-MATRIX.json'); bl=load('planning/execution/BLOCKERS.json'); pr=load('planning/execution/PROVIDER-ATTESTATIONS.json')
    journeys=yaml.safe_load((R/'planning/acceptance/USER-JOURNEY-ORACLES.yaml').read_text(encoding='utf-8')) or {}
    policy=yaml.safe_load((R/'config/PRODUCT-COMPLETION-POLICY.yaml').read_text(encoding='utf-8')) or {}
    real_types=set(policy.get('real_evidence_types') or [])
    jobs=[x for x in g.get('jobs',[]) if isinstance(x,dict) and x.get('id')==a.job_id]
    if not jobs: print('JOB_NOT_FOUND'); return 2
    j=jobs[0]; target=a.status; errs=[]; candidate=conv.get('candidate_sha') or ev.get('candidate_sha')
    em={x.get('id'):x for x in ev.get('entries',[]) if isinstance(x,dict) and x.get('id')}
    active_blockers=[b for b in bl.get('blockers') or [] if isinstance(b,dict) and b.get('status') not in {'RESOLVED','WAIVED'}]
    exec_blocked=[b for b in active_blockers if b.get('class')=='EXECUTION_BLOCKER' and (b.get('scope')=='GLOBAL' or a.job_id in (b.get('affected_job_ids') or []))]
    verification_blocked=[b for b in active_blockers if b.get('class')=='VERIFICATION_BLOCKER' and a.job_id in (b.get('affected_job_ids') or [])]
    def check_evidence(ids, required_types=()):
        got=set(); local=[]
        for eid in ids or []:
            x=em.get(eid)
            if not x or x.get('status')!='PASS': local.append(f'evidence not PASS: {eid}'); continue
            if candidate and x.get('sha')!=candidate and not x.get('scope_independent_after_sha',False): local.append(f'evidence stale: {eid}')
            if x.get('type'): got.add(x.get('type'))
        missing=set(required_types or [])-got
        if missing: local.append('missing evidence types: '+','.join(sorted(missing)))
        return local,got
    if target in {'IMPLEMENTED_UNVERIFIED','VERIFYING','DONE'} and exec_blocked:
        errs.extend('execution blocker unresolved: '+str(x.get('id')) for x in exec_blocked)
    if target=='IMPLEMENTED_UNVERIFIED':
        if not (j.get('implementation_complete') is True or j.get('implementation_status')=='COMPLETE'):
            errs.append('implementation_complete/implementation_status COMPLETE required')
        ids=j.get('implementation_evidence_ids') or j.get('evidence_ids') or []
        if not (ids or j.get('implementation_evidence_not_applicable_reason') or j.get('evidence_not_applicable_reason')):
            errs.append('implementation evidence missing without N/A reason')
        ee,_=check_evidence(ids); errs.extend(ee)
    if target=='DONE':
        acceptance=j.get('acceptance') or []
        if not acceptance: errs.append('acceptance missing')
        if any(isinstance(x,dict) and x.get('status') not in {'PASS','SATISFIED'} for x in acceptance): errs.append('acceptance incomplete')
        ids=j.get('evidence_ids') or []
        if not (ids or j.get('evidence_not_applicable_reason')): errs.append('evidence missing without N/A reason')
        ee,_=check_evidence(ids,j.get('required_evidence_types') or []); errs.extend(ee)
        jm={x.get('id'):x for x in journeys.get('journeys',[]) if isinstance(x,dict) and x.get('id')}
        for jid in j.get('required_journey_ids') or []:
            x=jm.get(jid)
            if not x or x.get('status')!='PASS': errs.append('journey not PASS: '+jid); continue
            need=set(x.get('required_evidence_types') or [])
            if x.get('final_real_required') and not need: need={'USER_JOURNEY_REAL'}
            je,jgot=check_evidence(x.get('evidence_ids') or [],need); errs.extend(f'journey {jid}: {z}' for z in je)
            if x.get('final_real_required') and not (jgot & real_types): errs.append('journey lacks real evidence: '+jid)
        providers=pr.get('providers') or {}
        consumer_types={'INTEGRATION_REAL','RUNTIME_REAL','BROWSER_REAL','NATIVE_RUNTIME_REAL','NETWORK_REAL','USER_JOURNEY_REAL'}
        for pid in j.get('required_provider_ids') or []:
            x=providers.get(pid) or {}
            if x.get('status')!='CONSUMER_VERIFIED': errs.append('provider not CONSUMER_VERIFIED: '+pid); continue
            pe,pgot=check_evidence(x.get('evidence_ids') or [],{'PROVIDER_REAL'}); errs.extend(f'provider {pid}: {z}' for z in pe)
            if not (pgot & consumer_types): errs.append('provider lacks consumer-runtime evidence: '+pid)
        if verification_blocked: errs.extend('verification blocker unresolved: '+str(x.get('id')) for x in verification_blocked)
    if errs:
        print('JOB_TRANSITION_DENIED'); [print('-',x) for x in errs]; return 2
    if a.write:
        now=datetime.datetime.now(datetime.timezone.utc).isoformat(); j['status']=target; j['updated_at']=now
        if target=='IMPLEMENTED_UNVERIFIED':
            j['implementation_status']='COMPLETE'; j['verification_status']='PENDING_EXTERNAL' if verification_blocked else j.get('verification_status','PENDING')
        elif target=='DONE':
            j['implementation_status']='COMPLETE'; j['verification_status']='PASS'
        g['updated_at']=now; (R/'planning/execution/JOB-GRAPH.json').write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
    print('JOB_TRANSITION_ALLOWED'+(' AND WRITTEN' if a.write else '')); return 0
if __name__=='__main__': raise SystemExit(main())
