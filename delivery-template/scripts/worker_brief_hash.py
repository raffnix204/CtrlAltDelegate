#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, yaml, json, sys
p=argparse.ArgumentParser(description='Bind/verify SHA-256 authority pointers and optional append-only skill-grant chain.')
p.add_argument('brief'); p.add_argument('--root',default='.'); p.add_argument('--write',action='store_true'); p.add_argument('--verify-grants',action='store_true'); p.add_argument('--grant-log',default='planning/execution/SKILL-REQUESTS.jsonl')
a=p.parse_args(); root=Path(a.root).resolve(); brief=Path(a.brief); brief=brief if brief.is_absolute() else (root/brief); d=yaml.safe_load(brief.read_text(encoding='utf-8')) or {}; errors=[]
def sha(b): return hashlib.sha256(b).hexdigest()
for item in d.get('authority_pointers') or []:
    rel=item.get('path'); target=(root/rel).resolve() if rel else None
    if not rel or not target or not target.is_file() or (root not in target.parents and target!=root): errors.append(f'invalid pointer {rel}'); continue
    actual=sha(target.read_bytes()); expected=item.get('sha256')
    if a.write: item['sha256']=actual
    elif expected!=actual: errors.append(f'STALE_BRIEF {rel} expected={expected} actual={actual}')
if a.write: brief.write_text(yaml.safe_dump(d,sort_keys=False),encoding='utf-8')
base_sha=sha(brief.read_bytes()); effective=base_sha
if a.verify_grants:
    log=(root/a.grant_log); prev=None
    if log.exists():
        for line in log.read_text(encoding='utf-8').splitlines():
            if not line.strip(): continue
            try:e=json.loads(line)
            except Exception: errors.append('invalid grant JSONL'); continue
            if e.get('base_brief_sha256')!=base_sha or e.get('decision') not in {'L0_REFERENCE_LOAD','L1_JIT_SKILL_INJECT'}: continue
            if e.get('previous_grant_sha256')!=prev: errors.append('STALE_BRIEF grant chain mismatch')
            skill=(root/e.get('canonical_skill_path',''))
            if not skill.is_file() or sha(skill.read_bytes())!=e.get('skill_sha256'): errors.append(f'STALE_BRIEF skill hash mismatch {e.get("skill_id")}')
            raw={k:v for k,v in e.items() if k not in {'event_sha256','effective_brief_sha256'}}
            ev=sha(json.dumps(raw,sort_keys=True,separators=(',',':')).encode())
            if ev!=e.get('event_sha256'): errors.append('STALE_BRIEF grant event hash mismatch')
            effective=sha((base_sha+'|'+(prev or '')+'|'+ev).encode()); prev=ev
            if effective!=e.get('effective_brief_sha256'): errors.append('STALE_BRIEF effective hash mismatch')
if errors:
    [print(x) for x in errors]; sys.exit(2)
print(f'WORKER_BRIEF_INTEGRITY_PASS effective_brief_sha256={effective}')
