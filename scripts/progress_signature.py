#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,datetime
R=Path(__file__).resolve().parents[1]
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
def git(*args):
 try:return subprocess.check_output(['git',*args],cwd=R,text=True,stderr=subprocess.DEVNULL).strip()
 except:return None
data={'version':'5.8.2','git_head':git('rev-parse','HEAD'),'git_diff':git('diff','--stat'),'job_graph_sha256':h(R/'planning/execution/JOB-GRAPH.json'),'evidence_sha256':h(R/'planning/execution/EVIDENCE-INDEX.json'),'convergence_sha256':h(R/'planning/execution/CONVERGENCE-MATRIX.json')}
raw=json.dumps(data,sort_keys=True,separators=(',',':')).encode(); data['signature']=hashlib.sha256(raw).hexdigest(); data['observed_at']=datetime.datetime.now(datetime.timezone.utc).isoformat(); print(json.dumps(data,indent=2))
