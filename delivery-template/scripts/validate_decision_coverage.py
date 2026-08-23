#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]; P=R/'planning/execution/DECISION-LEDGER.jsonl'; allowed={'RESOLVED','DEFERRED_WITH_REASON','AUTOPILOT_OWNED'}; errs=[]; count=0
for n,line in enumerate(P.read_text(encoding='utf-8').splitlines(),1):
 if not line.strip(): continue
 count+=1
 try:x=json.loads(line)
 except Exception as e: errs.append(f'line {n}: invalid json'); continue
 if x.get('consequential',True) and x.get('status') not in allowed: errs.append(f"line {n}: consequential decision status {x.get('status')} not covered")
if errs:
 print('DECISION_COVERAGE_FAIL'); [print('-',x) for x in errs]; raise SystemExit(2)
print('DECISION_COVERAGE_PASS decisions='+str(count))
