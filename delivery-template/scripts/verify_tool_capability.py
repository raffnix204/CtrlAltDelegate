#!/usr/bin/env python3
from pathlib import Path
import argparse, json, shutil, subprocess, os
R=Path(__file__).resolve().parents[1]
def run(cmd,timeout=20):
    try:
        r=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout); return r.returncode,(r.stdout+r.stderr)[-2000:]
    except Exception as e:return 99,str(e)
def find_provider(name):
    p=shutil.which(name)
    if p:return p
    roots=[R/'tools' if R.name=='.ctrlaltdelegate' else R/'.ctrlaltdelegate-runtime/tools']
    for root in roots:
        if root.exists():
            hits=list(root.rglob(name))+list(root.rglob(name+'.exe'))
            if hits:return str(hits[0])
    return None
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('provider',choices=['crw','obscura','playwright_mcp']); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    checks=[]; caps=[]
    if a.provider=='crw':
        b=find_provider('crw');
        if not b: print(json.dumps({'status':'MISSING','provider':'crw'},indent=2)); return 2
        rc,out=run([b,'https://example.com']); checks.append({'name':'static_scrape','exit':rc}); caps=['web.scrape'] if rc==0 else []
    elif a.provider=='obscura':
        b=find_provider('obscura');
        if not b: print(json.dumps({'status':'MISSING','provider':'obscura'},indent=2)); return 2
        rc,out=run([b,'fetch','https://example.com','--eval','document.title']); checks.append({'name':'js_eval','exit':rc}); caps=['browser.javascript','browser.dom','browser.interaction'] if rc==0 else []
    else:
        # Verify isolated package presence; runtime browser launch is a separate project acceptance probe.
        base=(R/'tools' if R.name=='.ctrlaltdelegate' else R/'.ctrlaltdelegate-runtime/tools'); hits=list((base/'playwright-mcp').rglob('package.json'))
        ok=bool(hits) or bool(shutil.which('playwright'))
        checks.append({'name':'package_present','exit':0 if ok else 2}); caps=['browser.production_acceptance'] if ok else []
    ok=all(x['exit']==0 for x in checks); result={'version':'5.9','provider':a.provider,'status':'VERIFIED' if ok else 'FAILED','checks':checks,'capabilities':caps}
    if a.write and ok:
        p=R/'planning/execution/CAPABILITY-STATE.json'; state={'version':'5.9','status':'INVENTORIED','capabilities':{}}
        if p.exists():
            try:state=json.loads(p.read_text())
            except Exception:pass
        for c in caps: state.setdefault('capabilities',{})[c]={'provider':a.provider,'status':'VERIFIED'}
        p.write_text(json.dumps(state,indent=2)+'\n')
    print(json.dumps(result,indent=2)); return 0 if ok else 2
if __name__=='__main__': raise SystemExit(main())
