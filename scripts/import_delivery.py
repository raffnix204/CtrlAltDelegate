#!/usr/bin/env python3
"""Safely merge an explicit root-overlay delivery into a repository.

V5.6.4 Custom-GPT planning handoffs normally use the nested ctrlaltdelegate/ topology and do not require this importer.

Greenfield delivery contents are already a repository baseline and normally need no import.
For brownfield/local nested delivery use this script. Default is dry-run. --apply copies
new files, preserves byte-identical files, stages true collisions under
planning/import-conflicts/, and never blindly overwrites user-owned content.
"""
from pathlib import Path
import argparse, hashlib, re, shutil

VERSION = "5.6"
MANIFEST = Path("planning/handoff/DELIVERY-MANIFEST.yaml")


def parse_scalar(text: str, key: str):
    m = re.search(rf"(?m)^{re.escape(key)}:\s*['\"]?([^'\"\n#]+)", text)
    return m.group(1).strip() if m else None


def parse_list(text: str, key: str):
    lines=text.splitlines(); out=[]; active=False; indent=None
    for line in lines:
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            active=True; indent=None; continue
        if not active: continue
        m=re.match(r"(\s*)-\s*['\"]?(.+?)['\"]?\s*$", line)
        if m:
            if indent is None: indent=len(m.group(1))
            out.append(m.group(2).strip().strip('"').strip("'")); continue
        if line.strip() and not line.startswith(' '): break
    return out


def same_file(a: Path, b: Path):
    if a.stat().st_size != b.stat().st_size: return False
    return hashlib.sha256(a.read_bytes()).digest() == hashlib.sha256(b.read_bytes()).digest()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('delivery', type=Path)
    ap.add_argument('--root', type=Path, default=Path.cwd())
    ap.add_argument('--apply', action='store_true')
    args=ap.parse_args()
    delivery=args.delivery.resolve(); root=args.root.resolve()
    manifest=delivery/MANIFEST
    if not manifest.is_file():
        print(f'INVALID_DELIVERY: missing {MANIFEST}'); return 2
    text=manifest.read_text(encoding='utf-8',errors='replace')
    if parse_scalar(text,'delivery_version') != VERSION:
        print(f'INVALID_DELIVERY: expected delivery_version {VERSION}'); return 2
    if parse_scalar(text,'layout') != 'REPO_ROOT_READY':
        print('INVALID_DELIVERY: expected layout REPO_ROOT_READY'); return 2
    required=parse_list(text,'required_files')
    missing=[x for x in required if not (delivery/x).is_file()]
    if missing:
        print('INVALID_DELIVERY: required files missing:', ', '.join(missing)); return 2
    if delivery == root or root.is_relative_to(delivery):
        print('INVALID_TARGET: --root must be the destination repository, not inside delivery'); return 2
    for p in delivery.rglob('*'):
        if p.is_symlink():
            print('INVALID_DELIVERY: symlink not allowed:', p.relative_to(delivery)); return 2
    copies=[]; unchanged=[]; collisions=[]
    for src in sorted(delivery.rglob('*')):
        if not src.is_file() or '.git' in src.relative_to(delivery).parts: continue
        rel=src.relative_to(delivery); dst=root/rel
        if not dst.exists(): copies.append((src,dst,rel))
        elif dst.is_file() and same_file(src,dst): unchanged.append(rel)
        else: collisions.append((src,dst,rel))
    print(f'copy_new={len(copies)} unchanged={len(unchanged)} collisions={len(collisions)} apply={args.apply}')
    for _,_,rel in collisions[:100]: print('COLLISION', rel)
    if not args.apply: return 3 if collisions else 0
    for src,dst,_ in copies:
        dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst)
    conflict_root=root/'planning/import-conflicts'/delivery.name
    for src,_,rel in collisions:
        target=conflict_root/rel; target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,target)
    # If the delivery folder itself lives inside the repo root, ignore exactly that transient nested package.
    try:
        rel_delivery=delivery.relative_to(root)
        if rel_delivery.parts:
            gi=root/'.gitignore'; current=gi.read_text(encoding='utf-8') if gi.exists() else ''
            entry='/' + rel_delivery.as_posix().rstrip('/') + '/'
            if entry not in current.splitlines():
                if current and not current.endswith('\n'): current+='\n'
                gi.write_text(current + entry + '\n', encoding='utf-8')
    except ValueError:
        pass
    print('DELIVERY_IMPORTED', f'new={len(copies)} collisions_staged={len(collisions)}')
    return 4 if collisions else 0

if __name__=='__main__': raise SystemExit(main())
