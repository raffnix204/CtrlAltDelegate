#!/usr/bin/env python3
from pathlib import Path
import argparse, subprocess, hashlib, sys, datetime, yaml
R=Path(__file__).resolve().parents[1]
STATE=R/'planning/execution/DOCUMENTATION-STATE.yaml'
STATE_REL='planning/execution/DOCUMENTATION-STATE.yaml'
DOC_NAMES={'README.md','CHANGELOG.md','CHANGELOG-SYSTEM.md'}
DOC_PREFIXES=('docs/','planning/adr/','planning/execution/DOCUMENTATION-COVERAGE.md')
IMPACTS={'NONE','USER','INSTALLATION','CONFIGURATION','API','MIGRATION','OPERATOR','SECURITY','RELEASE'}

def git(*args, input_text=None, check=True):
    p=subprocess.run(['git',*args],cwd=R,text=True,input=input_text,capture_output=True)
    if check and p.returncode: raise RuntimeError(p.stderr.strip() or p.stdout.strip())
    return p.stdout

def staged_files(): return [x for x in git('diff','--cached','--name-only','--diff-filter=ACMR').splitlines() if x]
def is_doc(p): return Path(p).name in DOC_NAMES or p.startswith(DOC_PREFIXES) or p.lower().endswith(('.md','.mdx','.rst')) and (p.startswith('docs/') or Path(p).name.lower().startswith('readme'))
def fingerprint(files):
    files=[x for x in files if x != STATE_REL]
    h=hashlib.sha256()
    for f in sorted(files):
        h.update(f.encode()+b'\0')
        out=git('show',f':{f}',check=False)
        h.update(out.encode('utf-8','replace')+b'\0')
    return h.hexdigest()

def load_state():
    try:return yaml.safe_load(STATE.read_text()) or {}
    except Exception:return {}
def save_state(d): STATE.parent.mkdir(parents=True,exist_ok=True); STATE.write_text(yaml.safe_dump(d,sort_keys=False),encoding='utf-8')

def record(args):
    files=staged_files(); impacts=[x.strip().upper() for x in args.impact.split(',') if x.strip()]
    bad=set(impacts)-IMPACTS
    if bad or not impacts: raise SystemExit(f'Invalid impact: {sorted(bad) or impacts}')
    docs=[x.strip() for x in (args.docs or '').split(',') if x.strip()]
    if impacts==['NONE']:
        if len((args.reason or '').strip())<12: raise SystemExit('NONE requires a concrete reason (>=12 chars).')
    else:
        if 'NONE' in impacts: raise SystemExit('NONE cannot be combined with other impacts.')
        if not docs: raise SystemExit('Non-NONE impact requires --docs with canonical docs updated in this commit.')
        missing=[d for d in docs if d not in files]
        if missing: raise SystemExit(f'Docs must be staged before record: {missing}')
    d={'version':'5.6','status':'RECORDED','last_check':{
        'staged_fingerprint':fingerprint(files),'impact':impacts,'docs_updated':docs,'reason':args.reason,
        'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'staged_files':[x for x in files if x!=STATE_REL]},
        'final_gate':load_state().get('final_gate',{})}
    save_state(d)
    print('DOCS_FRESHNESS_RECORDED',d['last_check']['staged_fingerprint'])

def verify_staged():
    files=staged_files(); d=load_state(); lc=d.get('last_check') or {}; errors=[]
    if STATE_REL not in files: errors.append(f'{STATE_REL} must be staged for every non-doc commit.')
    non_state=[x for x in files if x!=STATE_REL]
    if not non_state: errors.append('No staged project files found.')
    fp=fingerprint(files)
    if lc.get('staged_fingerprint')!=fp: errors.append('Documentation attestation does not match current staged diff. Re-run --record after final staging.')
    impacts=lc.get('impact') or []
    if not impacts: errors.append('Missing Documentation Impact.')
    if impacts==['NONE'] and len(str(lc.get('reason') or '').strip())<12: errors.append('NONE impact lacks concrete reason.')
    if impacts and impacts!=['NONE']:
        docs=lc.get('docs_updated') or []
        if not docs: errors.append('Non-NONE impact requires docs_updated.')
        for doc in docs:
            if doc not in files: errors.append(f'Documented updated file is not staged: {doc}')
    if errors:
        print('DOCS_FRESHNESS_FAIL'); [print('-',e) for e in errors]; return 2
    print('DOCS_FRESHNESS_PASS',','.join(impacts)); return 0

def commits_between(local_sha, remote_sha):
    if local_sha=='0'*40: return []
    if remote_sha=='0'*40: spec=local_sha
    else: spec=f'{remote_sha}..{local_sha}'
    return [x for x in git('rev-list','--reverse',spec,check=False).splitlines() if x]

def verify_push(stdin_text):
    errors=[]; lines=[x for x in stdin_text.splitlines() if x.strip()]
    if not lines:
        # Manual invocation fallback: current upstream range if available.
        up=git('rev-parse','@{upstream}',check=False).strip()
        head=git('rev-parse','HEAD').strip()
        if up: lines=[f'refs/heads/main {head} refs/heads/main {up}']
    for line in lines:
        parts=line.split()
        if len(parts)<4: continue
        _,local_sha,_,remote_sha=parts[:4]
        for c in commits_between(local_sha,remote_sha):
            names=[x for x in git('show','--pretty=','--name-only',c).splitlines() if x]
            non_docs=[x for x in names if not is_doc(x) and x!=STATE_REL]
            if non_docs and STATE_REL not in names:
                errors.append(f'{c[:12]} changes code/config without documentation freshness attestation')
    if errors:
        print('PRE_PUSH_DOCS_FAIL'); [print('-',e) for e in errors]; return 2
    print('PRE_PUSH_DOCS_PASS'); return 0

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--record',action='store_true'); ap.add_argument('--staged',action='store_true'); ap.add_argument('--pre-push',action='store_true')
    ap.add_argument('--impact',default=''); ap.add_argument('--docs'); ap.add_argument('--reason'); ap.add_argument('--stdin-file')
    a=ap.parse_args()
    try:
        if a.record: record(a); return 0
        if a.staged: return verify_staged()
        if a.pre_push:
            data=Path(a.stdin_file).read_text() if a.stdin_file else sys.stdin.read()
            return verify_push(data)
        ap.error('choose --record, --staged, or --pre-push')
    except RuntimeError as e:
        print('DOCS_FRESHNESS_ERROR',e); return 2
if __name__=='__main__': raise SystemExit(main())
