#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, yaml, sys
R=Path(__file__).resolve().parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def canonical_event_hash(d):
    x={k:v for k,v in d.items() if k not in {'event_sha256','effective_brief_sha256'}}
    return sha(json.dumps(x,sort_keys=True,separators=(',',':')).encode())
def append_jsonl(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('a',encoding='utf-8') as f:f.write(json.dumps(obj,sort_keys=True)+'\n')
def last_event_hash(path,brief_sha):
    prev=None
    if path.exists():
        for line in path.read_text(encoding='utf-8').splitlines():
            if not line.strip(): continue
            try:e=json.loads(line)
            except: continue
            if e.get('base_brief_sha256')==brief_sha and e.get('decision') in {'L0_REFERENCE_LOAD','L1_JIT_SKILL_INJECT'}: prev=e.get('event_sha256')
    return prev
def main():
    ap=argparse.ArgumentParser(description='Resolve one runtime skill/reference request without unnecessary project replanning.')
    ap.add_argument('skill_id'); ap.add_argument('--job-id',required=True); ap.add_argument('--brief',required=True); ap.add_argument('--reason',required=True)
    ap.add_argument('--reference'); ap.add_argument('--impact',default='none',choices=['none','job_capability','job_scope','acceptance','requirements','architecture','shared_contract','security','privacy','data_loss','compliance','material_cost'])
    ap.add_argument('--record',action='store_true'); ap.add_argument('--root',default=None)
    a=ap.parse_args(); root=Path(a.root).resolve() if a.root else R
    brief=(root/a.brief).resolve() if not Path(a.brief).is_absolute() else Path(a.brief).resolve()
    if not brief.is_file(): print('SKILL_REQUEST_FAIL missing brief'); return 2
    bdata=yaml.safe_load(brief.read_text(encoding='utf-8')) or {}; bsha=sha(brief.read_bytes())
    skill=root/'.agents/skills'/a.skill_id/'SKILL.md'
    if not skill.is_file(): print(json.dumps({'decision':'L3_SCOPED_CHANGE','reason':'requested skill is not canonical; targeted research/new-specialist decision required'},indent=2)); return 3
    selected=set(((bdata.get('job') or {}).get('required_skill_ids') or [])); skillsha=sha(skill.read_bytes())
    refrel=None
    if a.reference:
        ref=(skill.parent/a.reference).resolve()
        if skill.parent not in ref.parents or not ref.is_file(): print('SKILL_REQUEST_FAIL invalid reference'); return 2
        refrel=str(ref.relative_to(root)).replace('\\','/')
    if a.reference and a.skill_id in selected and a.impact=='none': decision='L0_REFERENCE_LOAD'
    elif a.impact=='none' and not a.reference: decision='L1_JIT_SKILL_INJECT' if a.skill_id not in selected else 'L0_REFERENCE_LOAD'
    elif a.impact in {'job_capability','job_scope','acceptance'}: decision='L2_JOB_REBRIEF'
    else: decision='L3_SCOPED_CHANGE'
    log=root/'planning/execution/SKILL-REQUESTS.jsonl'; prev=last_event_hash(log,bsha)
    event={'version':'5.9','job_id':a.job_id,'base_brief_path':str(brief.relative_to(root)).replace('\\','/') if root in brief.parents else str(brief),'base_brief_sha256':bsha,'previous_grant_sha256':prev,'skill_id':a.skill_id,'canonical_skill_path':str(skill.relative_to(root)).replace('\\','/'),'skill_sha256':skillsha,'reference':refrel,'reason':a.reason,'impact':a.impact,'decision':decision}
    event['event_sha256']=canonical_event_hash(event)
    event['effective_brief_sha256']=sha((bsha+'|'+(prev or '')+'|'+event['event_sha256']).encode())
    if a.record:
        append_jsonl(log,event)
        if decision in {'L0_REFERENCE_LOAD','L1_JIT_SKILL_INJECT'}:
            ddir=root/'planning/execution/brief-deltas'; ddir.mkdir(parents=True,exist_ok=True)
            idx=sum(1 for x in log.read_text(encoding='utf-8').splitlines() if x.strip())
            (ddir/f'{a.job_id}.{idx:04d}.{a.skill_id}.yaml').write_text(yaml.safe_dump(event,sort_keys=False),encoding='utf-8')
            usage={'version':'5.9','skill_id':a.skill_id,'event':'REFERENCE_LOADED' if decision=='L0_REFERENCE_LOAD' else 'RUNTIME_INJECTED','job_id':a.job_id,'repo_sha':None,'skill_sha256':skillsha,'source_event_sha256':event['event_sha256']}
            usage_log=root/'planning/execution/SKILL-USAGE-EVENTS.jsonl'
            append_jsonl(usage_log,usage)
            if decision=='L1_JIT_SKILL_INJECT':
                miss={**usage,'event':'ROUTING_MISS'}
                append_jsonl(usage_log,miss)
    print(json.dumps(event,indent=2)); return 0 if decision in {'L0_REFERENCE_LOAD','L1_JIT_SKILL_INJECT'} else (4 if decision=='L2_JOB_REBRIEF' else 5)
if __name__=='__main__': raise SystemExit(main())
