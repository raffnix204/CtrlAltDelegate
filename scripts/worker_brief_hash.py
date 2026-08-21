#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, yaml, sys
p=argparse.ArgumentParser(description='Bind or verify SHA-256 authority pointers in a CtrlAltDelegate worker brief.')
p.add_argument('brief'); p.add_argument('--root',default='.'); p.add_argument('--write',action='store_true')
a=p.parse_args(); root=Path(a.root).resolve(); brief=Path(a.brief)
d=yaml.safe_load(brief.read_text(encoding='utf-8')) or {}; errors=[]
for item in d.get('authority_pointers') or []:
    rel=item.get('path'); target=(root/rel).resolve() if rel else None
    if not rel or not target or not target.is_file() or root not in target.parents and target!=root:
        errors.append(f'invalid pointer {rel}'); continue
    actual=hashlib.sha256(target.read_bytes()).hexdigest()
    expected=item.get('sha256')
    if a.write: item['sha256']=actual
    elif expected!=actual: errors.append(f'STALE_BRIEF {rel} expected={expected} actual={actual}')
if a.write: brief.write_text(yaml.safe_dump(d,sort_keys=False),encoding='utf-8')
if errors:
    [print(x) for x in errors]; sys.exit(2)
print('WORKER_BRIEF_INTEGRITY_PASS')
