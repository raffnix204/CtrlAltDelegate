#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
R=Path(__file__).resolve().parents[1]
for hook in [R/'.githooks/pre-commit', R/'.githooks/pre-push']:
    if hook.is_file():
        hook.chmod(hook.stat().st_mode | 0o111)
def run(*args): return subprocess.run(args,cwd=R,text=True,capture_output=True)
cur=run('git','config','--get','core.hooksPath').stdout.strip()
if not cur:
    p=run('git','config','core.hooksPath','.githooks')
    if p.returncode: print(p.stderr); raise SystemExit(p.returncode)
    print('GIT_GUARDS_READY core.hooksPath=.githooks'); raise SystemExit(0)
if cur in {'.githooks',str((R/'.githooks').resolve())}:
    print('GIT_GUARDS_READY existing .githooks'); raise SystemExit(0)
print('HOOK_INTEGRATION_REQUIRED existing core.hooksPath='+cur)
print('Preserve the existing hook system. Integrate these commands before committing/pushing:')
print('  python3 scripts/docs_freshness_gate.py --staged')
print('  python3 scripts/docs_freshness_gate.py --pre-push')
raise SystemExit(2)
