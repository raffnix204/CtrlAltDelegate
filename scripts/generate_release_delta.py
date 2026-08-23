#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json
SKIP={'PACKAGE-MANIFEST.md','RELEASE-FILE-MANIFEST.json','release/RELEASE-DELTA.json'}
def files(root):
    d={}
    for p in root.rglob('*'):
        if p.is_file():
            r=str(p.relative_to(root)).replace('\\','/')
            if r in SKIP: continue
            d[r]=hashlib.sha256(p.read_bytes()).hexdigest()
    return d
def skills(root): return sorted(p.parent.name for p in (root/'.agents/skills').glob('*/SKILL.md'))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('head'); ap.add_argument('--output',required=True); a=ap.parse_args(); b=Path(a.base); h=Path(a.head); bf=files(b); hf=files(h); bs=skills(b); hs=skills(h)
    out={'version':'5.9','files_added':sorted(set(hf)-set(bf)),'files_removed':sorted(set(bf)-set(hf)),'files_modified':sorted(k for k in set(bf)&set(hf) if bf[k]!=hf[k]),'skill_count_before':len(bs),'skill_count_after':len(hs),'skills_added':sorted(set(hs)-set(bs)),'skills_removed':sorted(set(bs)-set(hs))}
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n'); print(f'RELEASE_DELTA_GENERATED added={len(out["files_added"])} modified={len(out["files_modified"])} skills={len(bs)}->{len(hs)}')
if __name__=='__main__': main()
