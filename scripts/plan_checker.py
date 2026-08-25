#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
root=Path(__file__).resolve().parents[1]
findings=[]
graph=json.loads((root/'planning/execution/JOB-GRAPH.json').read_text())
coverage=json.loads((root/'planning/quality/CONTRACT-COVERAGE.json').read_text())
for kind in ['requirements','claims','interfaces','seams']:
    for row in coverage.get(kind,[]):
        if row.get('required',True) and (not row.get('owner') or not row.get('observer')):
            findings.append({'severity':'BLOCKER','kind':kind,'id':row.get('id'),'finding':'missing owner or observer'})
for n in graph.get('nodes',[]):
    if (n.get('type') or 'IMPLEMENTATION')=='IMPLEMENTATION':
        for k in ['objective','requirements','scope','acceptance_gates']:
            if k not in n and not n.get('contract_path'):
                findings.append({'severity':'BLOCKER','kind':'job','id':n.get('id'),'finding':f'missing {k} or contract_path'})
verdict='PASS' if not findings else 'BLOCKED'
out={'version':'5.9.1','verdict':verdict,'findings':findings,'checked_revision':graph.get('planning_revision','')}
(root/'planning/quality/PLAN-CHECKER.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2)); sys.exit(0 if verdict=='PASS' else 1)
