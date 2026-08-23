#!/usr/bin/env python3
from pathlib import Path
import json,sys,yaml,subprocess
R=Path(__file__).resolve().parents[1]
def jl(rel): return json.loads((R/rel).read_text(encoding='utf-8'))
def main():
    errors=[]; pending=[]
    q=subprocess.run([sys.executable,str(R/'scripts/quality_gate.py'),'--validate','--json'],cwd=R,text=True,capture_output=True)
    try:qj=json.loads(q.stdout)
    except Exception:qj={}
    if q.returncode not in {0,3}: errors.append('quality_gate failed: '+(q.stdout.strip() or q.stderr.strip()))
    c=jl('planning/execution/CONVERGENCE-MATRIX.json'); ev=jl('planning/execution/EVIDENCE-INDEX.json'); g=jl('planning/execution/JOB-GRAPH.json'); b=jl('planning/execution/BLOCKERS.json'); d=jl('planning/execution/DEFERRED-VALIDATION.json'); p=jl('planning/execution/PROVIDER-ATTESTATIONS.json'); drift=jl('planning/execution/PRODUCT-DRIFT-REVIEW.json'); pre=jl('planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json')
    journeys=yaml.safe_load((R/'planning/acceptance/USER-JOURNEY-ORACLES.yaml').read_text(encoding='utf-8')) or {}; contract=yaml.safe_load((R/'planning/product/PRODUCT-CONTRACT.yaml').read_text(encoding='utf-8')) or {}; policy=yaml.safe_load((R/'config/PRODUCT-COMPLETION-POLICY.yaml').read_text(encoding='utf-8')) or {}
    candidate=c.get('candidate_sha') or ev.get('candidate_sha'); em={x.get('id'):x for x in ev.get('entries',[]) if isinstance(x,dict) and x.get('id')}
    real_types=set(policy.get('real_evidence_types') or []); consumer_types={'INTEGRATION_REAL','RUNTIME_REAL','BROWSER_REAL','NATIVE_RUNTIME_REAL','NETWORK_REAL','USER_JOURNEY_REAL'}
    blockers={x.get('id'):x for x in b.get('blockers') or [] if isinstance(x,dict) and x.get('id')}; active=[x for x in blockers.values() if x.get('status') not in {'RESOLVED','WAIVED'}]
    deferred=[x for x in d.get('items') or [] if isinstance(x,dict) and x.get('required_for_completion',True) and x.get('status') not in {'PASS','RESOLVED','WAIVED'}]
    deferred_req={rid for x in deferred for rid in (x.get('requirement_ids') or [])}; deferred_jobs={jid for x in deferred for jid in (x.get('job_ids') or [])}
    verification_job={jid for x in active if x.get('class')=='VERIFICATION_BLOCKER' for jid in (x.get('affected_job_ids') or [])}; verification_req={rid for x in active if x.get('class')=='VERIFICATION_BLOCKER' for rid in (x.get('requirement_ids') or [])}
    def fresh_pass(eid):
        x=em.get(eid)
        return bool(x and x.get('status')=='PASS' and (not candidate or x.get('sha')==candidate or x.get('scope_independent_after_sha',False)))
    if not candidate: errors.append('candidate_sha missing')
    for r in c.get('requirements') or []:
        if not isinstance(r,dict) or not r.get('mandatory',True): continue
        rid=r.get('id','<unnamed>'); st=r.get('status')
        if st=='IMPLEMENTED_UNVERIFIED':
            if rid in deferred_req or rid in verification_req: pending.append(f'requirement {rid}')
            else: errors.append(f'{rid}: IMPLEMENTED_UNVERIFIED without declared verification blocker/deferred validation')
            continue
        if st!='CONVERGED': errors.append(f'{rid}: not CONVERGED'); continue
        got={em[eid].get('type') for eid in r.get('evidence_ids') or [] if eid in em and fresh_pass(eid)}; need=set(r.get('required_evidence_types') or [])
        if not need.issubset(got): errors.append(f'{rid}: missing evidence types {sorted(need-got)}')
    for x in journeys.get('journeys') or []:
        if not isinstance(x,dict) or not x.get('mandatory'): continue
        jid=x.get('id','<unnamed>'); st=x.get('status')
        if st=='DEFERRED_VALIDATION':
            bx=blockers.get(x.get('blocker_id')) if x.get('blocker_id') else None
            linked=bool(bx and bx.get('class')=='VERIFICATION_BLOCKER' and bx.get('status') not in {'RESOLVED','WAIVED'}) or any(jid in (z.get('journey_ids') or []) for z in deferred)
            if linked: pending.append(f'journey {jid}')
            else: errors.append(f'journey {jid}: deferred without verification blocker')
            continue
        if st!='PASS': errors.append(f'journey {jid}: {st}'); continue
        got={em[eid].get('type') for eid in x.get('evidence_ids') or [] if eid in em and fresh_pass(eid)}; need=set(x.get('required_evidence_types') or [])
        if x.get('final_real_required') and not need: need={'USER_JOURNEY_REAL'}
        if not need.issubset(got): errors.append(f'journey {jid}: missing typed evidence {sorted(need-got)}')
        if x.get('final_real_required') and not (got & real_types): errors.append(f'journey {jid}: no real-runtime evidence')
    for pid,x in (p.get('providers') or {}).items():
        if not isinstance(x,dict) or not x.get('required_for_completion'): continue
        st=x.get('status')
        if st!='CONSUMER_VERIFIED':
            bx=blockers.get(x.get('blocker_id')) if x.get('blocker_id') else None
            if bx and bx.get('class')=='VERIFICATION_BLOCKER' and bx.get('status') not in {'RESOLVED','WAIVED'}: pending.append(f'provider {pid}')
            else: errors.append(f'provider {pid}: {st}')
            continue
        ids=x.get('evidence_ids') or []; got={em[eid].get('type') for eid in ids if eid in em and fresh_pass(eid)}
        if 'PROVIDER_REAL' not in got: errors.append(f'provider {pid}: CONSUMER_VERIFIED lacks PROVIDER_REAL evidence')
        if not (got & consumer_types): errors.append(f'provider {pid}: CONSUMER_VERIFIED lacks real consumer/runtime evidence')
        for eid in ids:
            if not fresh_pass(eid): errors.append(f'provider {pid}: invalid/stale evidence {eid}')
    if contract.get('status') not in {'READY','APPROVED','NOT_APPLICABLE'}: errors.append('product contract not READY/APPROVED/N/A')
    if contract.get('status')!='NOT_APPLICABLE':
        if drift.get('status')!='PASS': errors.append('product drift review not PASS')
        if candidate and drift.get('candidate_sha')!=candidate: errors.append('product drift review stale')
        if not (drift.get('reviewer') or {}).get('independent'): errors.append('product drift reviewer not independent')
        drift_types={em[eid].get('type') for eid in drift.get('evidence_ids') or [] if eid in em and fresh_pass(eid)}
        if 'PRODUCT_DRIFT_REVIEW' not in drift_types: errors.append('product drift review lacks PRODUCT_DRIFT_REVIEW evidence')
    elif drift.get('status') not in {'NOT_APPLICABLE','PASS'}: errors.append('product drift review invalid for N/A contract')
    pre_status=pre.get('status')
    if pre_status in {'READY_WITH_DEFERRED_VALIDATION'}: pending.append('product runtime preflight deferred validation')
    elif pre_status not in {'PASS','READY','COMPLETE'}: errors.append('product runtime preflight not complete')
    for chk in pre.get('checks') or []:
        if not isinstance(chk,dict) or not chk.get('required',True): continue
        st=chk.get('status')
        if st in {'READY','PASS','AVAILABLE','NOT_APPLICABLE'}: continue
        if st=='DEFERRED_VERIFICATION' and chk.get('blocker_class')=='VERIFICATION_BLOCKER': pending.append('runtime prerequisite '+str(chk.get('id','<unnamed>')))
        else: errors.append('runtime prerequisite not ready: '+str(chk.get('id','<unnamed>'))+'='+str(st))
    for x in active:
        if x.get('class')=='EXECUTION_BLOCKER' and x.get('scope')=='GLOBAL': errors.append('global execution blocker unresolved: '+str(x.get('id')))
    for x in deferred: pending.append('deferred validation '+str(x.get('id')))
    for x in g.get('jobs') or []:
        if not isinstance(x,dict) or not x.get('required',True): continue
        jid=x.get('id'); st=x.get('status')
        if st=='DONE': continue
        if st in {'IMPLEMENTED_UNVERIFIED','VERIFYING'} and (jid in deferred_jobs or jid in verification_job): pending.append(f'job {jid}')
        else: errors.append(f'job {jid}: {st}')
    if q.returncode==3:
        if pending: pending.extend('quality gate: '+x for x in qj.get('pending',[]) or [])
        else: errors.append('quality gate pending without declared external/deferred validation')
    if errors:
        print('PRODUCT_COMPLETION_GATE_FAIL'); [print('-',x) for x in errors]; return 2
    if pending:
        print('PRODUCT_COMPLETION_GATE_VALIDATION_PENDING_EXTERNAL'); [print('-',x) for x in sorted(set(pending))]; return 3
    print('PRODUCT_COMPLETION_GATE_PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
