#!/usr/bin/env python3
"""Validate sealed control state and append-only surfaces.

`--staged` additionally inspects the Git index. Append-only control ledgers may
add lines but may not delete/rewrite existing lines in a staged change.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, yaml
sys.path.insert(0,str(Path(__file__).resolve().parent))
import control_state as cs

def validate_append_chain(rel):
    p=cs.ROOT/rel
    if not p.exists(): return [f'missing {rel}']
    errs=[]
    for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip(): continue
        try: json.loads(line)
        except Exception as e: errs.append(f'{rel}:{n}: invalid json {e}')
    if rel.endswith('CONTROL-MUTATION-LOG.jsonl'):
        prev=None
        for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
            if not line.strip(): continue
            try:x=json.loads(line)
            except Exception: continue
            if x.get('previous_receipt_hash')!=prev: errs.append(f'{rel}:{n}: receipt chain mismatch')
            copy=dict(x); got=copy.pop('receipt_hash',None)
            want=hashlib.sha256(json.dumps(copy,sort_keys=True,separators=(',',':')).encode()).hexdigest()
            if got!=want: errs.append(f'{rel}:{n}: receipt hash mismatch')
            prev=got
        if prev!=cs.state().get('last_receipt_hash'): errs.append('CONTROL-STATE last_receipt_hash mismatch')
    return errs

def append_only_paths():
    p=yaml.safe_load((cs.ROOT/'config/SURFACE-POLICY.yaml').read_text(encoding='utf-8')) or {}
    return [x for x in (((p.get('classes') or {}).get('APPEND_ONLY') or {}).get('paths') or []) if isinstance(x,str)]

def validate_staged_append_only():
    errs=[]
    try:
        cp=subprocess.run(['git','rev-parse','--is-inside-work-tree'],cwd=cs.ROOT,text=True,capture_output=True)
        if cp.returncode!=0: return []
        for rel in append_only_paths():
            d=subprocess.run(['git','diff','--cached','--numstat','--',rel],cwd=cs.ROOT,text=True,capture_output=True)
            if d.returncode!=0: errs.append(f'cannot inspect staged append-only path {rel}'); continue
            for line in d.stdout.splitlines():
                parts=line.split('\t')
                if len(parts)>=3:
                    deleted=parts[1]
                    if deleted not in {'0','-'} and int(deleted)>0:
                        errs.append(f'APPEND_ONLY_STAGED_REWRITE {rel} deleted_lines={deleted}')
    except Exception as e: errs.append('staged append-only check failed: '+str(e))
    return errs

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--initialize',action='store_true'); ap.add_argument('--staged',action='store_true'); a=ap.parse_args()
    if a.initialize:
        try: cs.initialize_seal(); print('CONTROL_MUTATION_SEAL_INITIALIZED'); return 0
        except Exception as e: print('CONTROL_MUTATION_INIT_FAIL',e); return 2
    errs=cs.verify_seal()
    for rel in append_only_paths(): errs.extend(validate_append_chain(rel))
    if a.staged: errs.extend(validate_staged_append_only())
    if errs:
        print('CONTROL_MUTATION_QA_FAIL'); [print('-',x) for x in errs]; return 2
    print('CONTROL_MUTATION_QA_PASS revision='+str(cs.state().get('revision'))); return 0
if __name__=='__main__': raise SystemExit(main())
