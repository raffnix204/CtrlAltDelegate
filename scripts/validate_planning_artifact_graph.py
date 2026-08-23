#!/usr/bin/env python3
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1]; d=yaml.safe_load((R/'planning/architecture/PLANNING-ARTIFACT-GRAPH.yaml').read_text()) or {}; arts=d.get('artifacts') or []; ids={x.get('id') for x in arts if isinstance(x,dict)}; errs=[]
for x in arts:
 if not isinstance(x,dict) or not x.get('id'): errs.append('artifact missing id'); continue
 for req in x.get('requires') or []:
  if req not in ids: errs.append(f"{x['id']}: unknown dependency {req}")
 if x.get('validator') in {None,'file_exists'}: errs.append(f"{x['id']}: semantic validator required; file existence is insufficient")
# cycle detection
by={x.get('id'):x for x in arts if isinstance(x,dict) and x.get('id')}; visiting=set(); done=set()
def visit(i):
 if i in done:return
 if i in visiting: errs.append('cycle at '+i); return
 visiting.add(i)
 for q in by.get(i,{}).get('requires') or []: visit(q)
 visiting.remove(i); done.add(i)
for i in ids: visit(i)
if errs:
 print('PLANNING_ARTIFACT_GRAPH_FAIL'); [print('-',x) for x in errs]; raise SystemExit(2)
print('PLANNING_ARTIFACT_GRAPH_PASS artifacts='+str(len(arts)))
