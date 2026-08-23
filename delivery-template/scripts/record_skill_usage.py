#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json
R=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('skill_id'); ap.add_argument('event',choices=['PLANNING_CONSULTED','EXECUTION_SELECTED','WORKER_APPLIED','VERIFIER_APPLIED','RUNTIME_INJECTED','REFERENCE_LOADED','ROUTING_MISS','INCIDENT_RELATED']); ap.add_argument('--job-id'); ap.add_argument('--repo-sha'); ap.add_argument('--root',default=None)
    a=ap.parse_args(); root=Path(a.root).resolve() if a.root else R; skill=root/'.agents/skills'/a.skill_id/'SKILL.md'
    if not skill.is_file(): raise SystemExit('unknown canonical skill')
    obj={'version':'5.8.2','skill_id':a.skill_id,'event':a.event,'job_id':a.job_id,'repo_sha':a.repo_sha,'skill_sha256':hashlib.sha256(skill.read_bytes()).hexdigest()}
    p=root/'planning/execution/SKILL-USAGE-EVENTS.jsonl'; p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('a',encoding='utf-8') as f:f.write(json.dumps(obj,sort_keys=True)+'\n')
    print(json.dumps(obj,indent=2))
if __name__=='__main__': main()
