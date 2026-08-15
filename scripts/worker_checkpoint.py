#!/usr/bin/env python3
"""Small harness-neutral helper for resumable long-running worker checkpoints.

This does not implement a timeout. It only persists/reports progress state under ignored
planning/private/runs/. Prefer native harness/provider progress/session persistence when available.
"""
from pathlib import Path
import argparse, json
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]

def now(): return datetime.now(timezone.utc).isoformat()
def path_for(run_id,job_id): return ROOT/'planning/private/runs'/run_id/job_id/'worker-state.json'
def load(p):
    if not p.exists(): return {}
    return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('action',choices=['init','progress','block','done','fail','show']); ap.add_argument('--run-id',required=True); ap.add_argument('--job-id',required=True); ap.add_argument('--baseline-sha'); ap.add_argument('--step'); ap.add_argument('--note'); ap.add_argument('--file',action='append',default=[]); ap.add_argument('--completed',action='append',default=[]); args=ap.parse_args()
    p=path_for(args.run_id,args.job_id); d=load(p)
    if args.action=='show':
        if not d: print('WORKER_CHECKPOINT_MISSING',p); return 2
        print(json.dumps(d,indent=2,ensure_ascii=False)); return 0
    if not d:
        d={'version':'5.6','run_id':args.run_id,'job_id':args.job_id,'baseline_sha':args.baseline_sha,'status':'RUNNING','started_at':now(),'last_meaningful_progress_at':now(),'current_step':None,'completed_steps':[],'changed_files':[],'notes':[]}
    if args.baseline_sha: d['baseline_sha']=args.baseline_sha
    if args.step: d['current_step']=args.step
    for x in args.completed:
        if x not in d['completed_steps']: d['completed_steps'].append(x)
    for x in args.file:
        if x not in d['changed_files']: d['changed_files'].append(x)
    if args.note: d['notes'].append({'at':now(),'text':args.note})
    status={'init':'RUNNING','progress':'RUNNING','block':'BLOCKED','done':'DONE','fail':'FAILED'}[args.action]
    d['status']=status; d['updated_at']=now()
    if args.action in {'init','progress','done'}: d['last_meaningful_progress_at']=d['updated_at']
    save(p,d); print('WORKER_CHECKPOINT',status,p.relative_to(ROOT)); return 0
if __name__=='__main__': raise SystemExit(main())
