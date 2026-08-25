#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
root=Path(__file__).resolve().parents[1]
errs=[]
def load_yaml(p):
    try:return yaml.safe_load(p.read_text()) or {}
    except Exception as e: errs.append(f'{p}: {e}'); return {}
def load_json(p):
    try:return json.loads(p.read_text())
    except Exception as e: errs.append(f'{p}: {e}'); return {}

discovery=(root/'planning/discovery/DISCOVERY-STATE.md')
disc_text=discovery.read_text() if discovery.exists() else ''
not_started=('NOT_STARTED' in disc_text or 'Status: `NOT_READY`' in disc_text)
claims=load_yaml(root/'planning/research/RESEARCH-CLAIMS.yaml')
feas=load_yaml(root/'planning/research/FEASIBILITY-LEDGER.yaml')
graph=load_json(root/'planning/execution/JOB-GRAPH.json')

# A freshly installed framework ships unresolved templates by design. Once planning starts,
# feasibility becomes fail-closed: broad implementation may not sit behind CRITICAL unknowns.
if not not_started:
    for c in feas.get('capabilities',[]):
        if c.get('criticality')=='CRITICAL' and c.get('status') in {'UNPROVEN','DISPROVEN'}:
            errs.append(f"critical capability {c.get('id')} is {c.get('status')}")

ids=set()
for n in (graph.get('nodes') or graph.get('jobs') or []):
    i=n.get('id') or n.get('job_id') or n.get('node_id')
    if not i: errs.append('job graph node missing id')
    if i in ids: errs.append(f'duplicate graph id {i}')
    ids.add(i)

if errs:
    print('PLANNING BLOCKED'); [print('-',e) for e in errs]; sys.exit(1)
print('PLANNING TEMPLATE OK (NOT_STARTED)' if not_started else 'PLANNING STRUCTURE OK')
