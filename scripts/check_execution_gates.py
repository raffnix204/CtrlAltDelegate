#!/usr/bin/env python3
from pathlib import Path
import argparse, subprocess, yaml, sys
ap=argparse.ArgumentParser(); ap.add_argument('ledger'); ap.add_argument('--cwd',default='.'); args=ap.parse_args()
data=yaml.safe_load(Path(args.ledger).read_text()) or {}; bad=[]
for g in data.get('gates',[]):
    if g.get('kind','RUNNABLE')=='MANUAL':
        if not g.get('evidence') or g.get('evidence')=='pending': bad.append((g.get('id'),'manual evidence pending'))
        continue
    cmd=g.get('check'); exp=g.get('expect')
    if not cmd or not exp: bad.append((g.get('id'),'malformed runnable gate')); continue
    p=subprocess.run(cmd,shell=True,cwd=args.cwd,text=True,capture_output=True)
    out=(p.stdout or '')+(p.stderr or '')
    if p.returncode!=0 or exp not in out: bad.append((g.get('id'),f'exit={p.returncode} expect_match={exp in out}'))
if bad:
    print('GATES FAILED'); [print(i,r) for i,r in bad]; sys.exit(1)
print('ALL GATES MET WITH CURRENT EXECUTION')
