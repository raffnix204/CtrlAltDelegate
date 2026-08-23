#!/usr/bin/env python3
from pathlib import Path
import argparse, json, subprocess, sys, yaml
R=Path(__file__).resolve().parents[1]
ALLOWED_ATTESTATION_PATHS={
 'planning/execution/EVIDENCE-INDEX.json',
 'planning/execution/CONVERGENCE-MATRIX.json',
 'planning/execution/STATE.md',
 'planning/execution/execution-ledger.md',
 'planning/execution/execution-memory.md',
 'planning/execution/GITHUB-STATE.md',
 'planning/execution/HARNESS-STATE.md',
 'planning/execution/CONTEXT-STATE.yaml',
 'planning/execution/PARALLELISM-STATE.yaml',
 'planning/execution/DOCUMENTATION-STATE.yaml',
}

def git(*args):
    try:return subprocess.check_output(['git',*args],cwd=R,text=True,stderr=subprocess.DEVNULL).strip()
    except Exception:return ''

def load(path):
    return json.loads((R/path).read_text(encoding='utf-8'))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--validate',action='store_true'); ap.add_argument('--json',action='store_true'); args=ap.parse_args()
    errs=[]; pending=[]; head=git('rev-parse','HEAD')
    try:c=load('planning/execution/CONVERGENCE-MATRIX.json')
    except Exception as e: errs.append(f'convergence parse: {e}'); c={}
    try:evid=load('planning/execution/EVIDENCE-INDEX.json')
    except Exception as e: errs.append(f'evidence parse: {e}'); evid={}
    candidate=c.get('candidate_sha') or evid.get('candidate_sha') or head
    if args.validate and not (c.get('requirements') or []): errs.append('convergence matrix has no requirements')
    if args.validate and not candidate: errs.append('candidate_sha is missing')
    if c.get('candidate_sha') and evid.get('candidate_sha') and c['candidate_sha']!=evid['candidate_sha']:
        errs.append('candidate_sha differs between convergence/evidence indexes')
    post_candidate=[]
    if head and candidate and candidate!=head:
        # Candidate may be an ancestor followed only by evidence/state attestation commits.
        rc=subprocess.run(['git','merge-base','--is-ancestor',candidate,head],cwd=R,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode
        if rc!=0:
            errs.append(f'candidate_sha {candidate} is not an ancestor of HEAD {head}')
        else:
            out=git('diff','--name-only',f'{candidate}..{head}')
            post_candidate=[x for x in out.splitlines() if x]
            illegal=[x for x in post_candidate if x not in ALLOWED_ATTESTATION_PATHS]
            if illegal: errs.append('post-candidate material changes invalidate evidence: '+', '.join(illegal))
    emap={x.get('id'):x for x in evid.get('entries',[]) if isinstance(x,dict) and x.get('id')}
    try:
        completion=yaml.safe_load((R/'config/PRODUCT-COMPLETION-POLICY.yaml').read_text(encoding='utf-8')) or {}
        allowed_types=set(completion.get('evidence_types') or [])
        real_types=set(completion.get('real_evidence_types') or [])
    except Exception as ex:
        errs.append(f'completion policy parse: {ex}'); allowed_types=set(); real_types=set()
    for x in evid.get('entries',[]) or []:
        if not isinstance(x,dict): continue
        typ=x.get('type')
        if typ and allowed_types and typ not in allowed_types: errs.append(f'evidence {x.get("id","<unnamed>")}: unknown type {typ}')
        if typ in real_types and x.get('realness') not in {'REAL',None}: errs.append(f'evidence {x.get("id","<unnamed>")}: real evidence type {typ} cannot be realness={x.get("realness")}')
    for rid,r in enumerate(c.get('requirements',[]) or [],1):
        if not isinstance(r,dict): errs.append(f'requirement row {rid} invalid'); continue
        ident=r.get('id') or f'row-{rid}'; st=r.get('status')
        if st not in {'CONVERGED','IMPLEMENTED_UNVERIFIED','WAIVED'}: errs.append(f'{ident}: status={st!r} not CONVERGED/IMPLEMENTED_UNVERIFIED/WAIVED')
        if st=='WAIVED' and not str(r.get('waiver_reason','')).strip(): errs.append(f'{ident}: WAIVED without waiver_reason')
        if st=='IMPLEMENTED_UNVERIFIED':
            pending.append(f'{ident}: implementation complete but final verification pending')
            if not (r.get('code_paths') or str(r.get('non_code_reason','')).strip()): errs.append(f'{ident}: no code_paths/non_code_reason')
            impl_ids=r.get('implementation_evidence_ids') or r.get('evidence_ids') or []
            if not (impl_ids or str(r.get('implementation_evidence_not_applicable_reason','')).strip() or str(r.get('evidence_not_applicable_reason','')).strip()): errs.append(f'{ident}: no implementation evidence/N/A reason')
            for eid in impl_ids:
                x=emap.get(eid)
                if not x: errs.append(f'{ident}: missing implementation evidence {eid}'); continue
                if x.get('status')!='PASS': errs.append(f'{ident}: implementation evidence {eid} status={x.get("status")}')
                if candidate and x.get('sha')!=candidate and not x.get('scope_independent_after_sha',False): errs.append(f'{ident}: implementation evidence {eid} stale sha={x.get("sha")} candidate={candidate}')
            doc=r.get('documentation',{}) or {}
            if not (doc.get('impact')=='NONE' or doc.get('paths')): errs.append(f'{ident}: documentation impact/paths missing')
        if st=='CONVERGED':
            if not (r.get('code_paths') or str(r.get('non_code_reason','')).strip()): errs.append(f'{ident}: no code_paths/non_code_reason')
            if not (r.get('evidence_ids') or str(r.get('evidence_not_applicable_reason','')).strip()): errs.append(f'{ident}: no evidence_ids/N/A reason')
            got_types=set()
            for eid in r.get('evidence_ids',[]) or []:
                x=emap.get(eid)
                if not x: errs.append(f'{ident}: missing evidence {eid}'); continue
                if x.get('status')!='PASS': errs.append(f'{ident}: evidence {eid} status={x.get("status")}')
                if x.get('status')=='PASS' and x.get('type'): got_types.add(x.get('type'))
                if candidate and x.get('sha')!=candidate and not x.get('scope_independent_after_sha',False): errs.append(f'{ident}: evidence {eid} stale sha={x.get("sha")} candidate={candidate}')
            required_types=set(r.get('required_evidence_types') or [])
            if not required_types.issubset(got_types): errs.append(f'{ident}: missing required evidence types {sorted(required_types-got_types)}')
            doc=r.get('documentation',{}) or {}
            if not (doc.get('impact')=='NONE' or doc.get('paths')): errs.append(f'{ident}: documentation impact/paths missing')
    for x in evid.get('entries',[]) or []:
        if not isinstance(x,dict) or not x.get('required_for_completion'): continue
        eid=x.get('id','<unnamed>'); st=x.get('status')
        if st in {'PENDING','DEFERRED','NOT_RUN'}: pending.append(f'required evidence {eid} is {st}')
        elif st!='PASS': errs.append(f'required evidence {eid} is not PASS')
        if st=='PASS' and candidate and x.get('sha')!=candidate and not x.get('scope_independent_after_sha',False): errs.append(f'required evidence {eid} stale')
    status='FAIL' if errs else ('PENDING' if pending else 'PASS')
    out={'status':status,'head':head,'candidate_sha':candidate,'post_candidate_attestation_paths':post_candidate,'requirements':len(c.get('requirements',[]) or []),'evidence':len(evid.get('entries',[]) or []),'pending':pending,'errors':errs}
    if args.json: print(json.dumps(out,indent=2))
    elif errs: print('QUALITY_GATE_FAIL\n- '+'\n- '.join(errs))
    elif pending: print('QUALITY_GATE_VALIDATION_PENDING\n- '+'\n- '.join(pending))
    else: print('QUALITY_GATE_PASS')
    return 2 if errs else (3 if pending else 0)
if __name__=='__main__': raise SystemExit(main())
