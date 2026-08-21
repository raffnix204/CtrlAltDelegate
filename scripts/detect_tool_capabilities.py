#!/usr/bin/env python3
from pathlib import Path
import argparse, json, shutil, subprocess, os
R=Path(__file__).resolve().parents[1]

def local_binary(cmd):
    base=(R/'tools' if R.name=='.ctrlaltdelegate' else R/'.ctrlaltdelegate-runtime/tools')
    hits=list(base.rglob(cmd))+list(base.rglob(cmd+'.exe')) if base.exists() else []
    return str(hits[0]) if hits else None

def cmd_version(cmd,args=('--version',)):
    p=shutil.which(cmd) or local_binary(cmd)
    if not p: return None
    try:
        r=subprocess.run([p,*args],capture_output=True,text=True,timeout=5)
        out=(r.stdout or r.stderr).strip().splitlines()
        return {'path':p,'version':out[0][:200] if out else 'UNKNOWN','exit':r.returncode}
    except Exception as e: return {'path':p,'version':'UNKNOWN','error':str(e)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--json',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    tools={k:cmd_version(v) for k,v in {'crw':'crw','obscura':'obscura','node':'node','npm':'npm','npx':'npx','git':'git','gh':'gh','codex':'codex','claude':'claude','opencode':'opencode','command_code':'cmd','pi':'pi','deepseek_harness':'dsh'}.items()}
    tools={k:v for k,v in tools.items() if v}
    caps={}
    if 'crw' in tools:
        for c in ['web.scrape','web.map','web.crawl','web.extract']: caps[c]={'provider':'crw','status':'DETECTED_NOT_SMOKE_TESTED'}
    if 'obscura' in tools:
        for c in ['browser.javascript','browser.dom','browser.interaction','browser.screenshot','browser.pdf','browser.mcp']: caps[c]={'provider':'obscura','status':'DETECTED_NOT_SMOKE_TESTED'}
    state={'version':'5.8.1','status':'INVENTORIED','tools':tools,'capabilities':caps,'note':'Detection is not capability proof; run verify_tool_capability.py for required capabilities.'}
    if a.write:
        p=R/'planning/execution/CAPABILITY-STATE.json'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(state,indent=2)+'\n')
    print(json.dumps(state,indent=2) if a.json or True else state)
    return 0
if __name__=='__main__': raise SystemExit(main())
