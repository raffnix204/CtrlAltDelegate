#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,datetime,sys
R=Path(__file__).resolve().parents[1]
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
def load(rel,default):
 try:return json.loads((R/rel).read_text(encoding='utf-8'))
 except:return default
def git(*args):
 try:return subprocess.check_output(['git',*args],cwd=R,text=True,stderr=subprocess.DEVNULL).strip()
 except:return None
def main():
 g=load('planning/execution/JOB-GRAPH.json',{}); ev=load('planning/execution/EVIDENCE-INDEX.json',{}); cv=load('planning/execution/CONVERGENCE-MATRIX.json',{}); b=load('planning/execution/BLOCKERS.json',{}); p=load('planning/execution/PROVIDER-ATTESTATIONS.json',{})
 jobs=g.get('jobs') or []; by={}
 for x in jobs:
  if isinstance(x,dict): by[x.get('status','UNKNOWN')]=by.get(x.get('status','UNKNOWN'),0)+1
 entries=[x for x in ev.get('entries') or [] if isinstance(x,dict)]; passing=sum(1 for x in entries if x.get('status')=='PASS')
 reqs=[x for x in cv.get('requirements') or [] if isinstance(x,dict)]; converged=sum(1 for x in reqs if x.get('status')=='CONVERGED')
 blockers=[x for x in b.get('blockers') or [] if isinstance(x,dict) and x.get('status') not in {'RESOLVED','WAIVED'}]
 providers=p.get('providers') or {}; consumer=sum(1 for x in providers.values() if isinstance(x,dict) and x.get('status')=='CONSUMER_VERIFIED')
 diff_names=git('diff','--name-only') or ''
 data={'version':'5.9','git_head':git('rev-parse','HEAD'),'work_product_hash':hashlib.sha256(diff_names.encode()).hexdigest(),'changed_paths':len([x for x in diff_names.splitlines() if x]),'job_status_counts':by,'passing_evidence':passing,'converged_requirements':converged,'unresolved_blockers':len(blockers),'consumer_verified_providers':consumer,'job_graph_sha256':h(R/'planning/execution/JOB-GRAPH.json'),'evidence_sha256':h(R/'planning/execution/EVIDENCE-INDEX.json'),'convergence_sha256':h(R/'planning/execution/CONVERGENCE-MATRIX.json')}
 objective={k:data[k] for k in ['work_product_hash','changed_paths','job_status_counts','passing_evidence','converged_requirements','unresolved_blockers','consumer_verified_providers']}; data['signature']=hashlib.sha256(json.dumps(objective,sort_keys=True,separators=(',',':')).encode()).hexdigest(); data['observed_at']=datetime.datetime.now(datetime.timezone.utc).isoformat(); print(json.dumps(data,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
