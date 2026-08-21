#!/usr/bin/env python3
from pathlib import Path
import argparse, yaml, json, shutil
R=Path(__file__).resolve().parents[1]
ALIASES={'browser.interactive':'browser.interaction','web.search':'web.search','web.scrape':'web.scrape','web.map':'web.map','web.crawl':'web.crawl','web.extract':'web.extract','browser.production_acceptance':'browser.production_acceptance'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('capability'); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    pol=yaml.safe_load((R/'config/TOOL-SELECTION-POLICY.yaml').read_text())
    cat=yaml.safe_load((R/'config/TOOL-CAPABILITY-CATALOG.yaml').read_text())
    state={}
    p=R/'planning/execution/CAPABILITY-STATE.json'
    if p.exists():
        try: state=json.loads(p.read_text())
        except Exception: pass
    requested=ALIASES.get(a.capability,a.capability)
    verified=[]
    for cap,v in (state.get('capabilities') or {}).items():
        if cap==requested and isinstance(v,dict) and v.get('status')=='VERIFIED': verified.append(v.get('provider'))
    if verified:
        out={'capability':a.capability,'decision':'REUSE','provider':verified[0],'reason':'verified capability already exists'}
    else:
        prefs=(pol.get('provider_preferences') or {}).get(a.capability) or []
        normalized=[]
        for x in prefs:
            if x in {'existing_verified','existing_project_playwright','existing_verified_browser_mcp','project_native_real_browser_e2e','lightweight_http_when_static'}: continue
            normalized.append(x)
        provider=next((x for x in normalized if x in (cat.get('providers') or {})),None)
        out={'capability':a.capability,'decision':'INSTALL_OR_CONFIGURE' if provider else 'RESEARCH_REQUIRED','provider':provider,'candidates':normalized,'reason':'no verified equivalent recorded'}
    print(json.dumps(out,indent=2))
    return 0 if out['provider'] or out['decision']=='REUSE' else 2
if __name__=='__main__': raise SystemExit(main())
