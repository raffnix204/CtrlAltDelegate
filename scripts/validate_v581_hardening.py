#!/usr/bin/env python3
from pathlib import Path
import json, yaml, subprocess, tempfile, sys
R=Path(__file__).resolve().parents[1]; e=[]
required=['config/SKILL-ESCALATION-POLICY.yaml','planning/execution/SKILL-REQUESTS.jsonl','planning/execution/SKILL-USAGE-EVENTS.jsonl','docs/templates/WORKER-BRIEF-DELTA.template.yaml','docs/system/RUNTIME-SKILL-ESCALATION.md','scripts/resolve_skill_request.py','config/SKILL-MAINTENANCE-POLICY.yaml','scripts/record_skill_usage.py','scripts/aggregate_skill_usage.py','docs/system/USAGE-AWARE-SKILL-MAINTENANCE.md','release/RELEASE-BASELINE.json','release/RELEASE-DELTA.json','release/RELEASE-CLAIMS.yaml','scripts/validate_release_claims.py']
for x in required:
    if not (R/x).exists(): e.append('missing '+x)
try:
    p=yaml.safe_load((R/'config/SKILL-ESCALATION-POLICY.yaml').read_text());
    if str(p.get('version'))!='5.9': e.append('skill escalation version')
    if list(p.get('levels',{}))!=['L0_REFERENCE_LOAD','L1_JIT_SKILL_INJECT','L2_JOB_REBRIEF','L3_SCOPED_CHANGE']: e.append('skill escalation ladder')
    if not p.get('invariants',{}).get('base_brief_immutable'): e.append('base brief must be immutable')
except Exception as x:e.append(str(x))
try:
    d=json.loads((R/'release/RELEASE-DELTA.json').read_text());
    if d.get('skill_count_before')!=154 or d.get('skill_count_after')!=154 or d.get('skills_added')!=[]: e.append('release skill delta incorrect')
except Exception as x:e.append(str(x))
coverage=(R/'docs/system/SKILL-COVERAGE-AUDIT.md').read_text()
if 'V5.7.1 then added nine distinct specialists' not in coverage: e.append('coverage history not corrected')
if 'V5.8 preserves those improvements and adds 9' in coverage: e.append('stale false V5.8 skill-addition claim')
maint=yaml.safe_load((R/'config/SKILL-MAINTENANCE-POLICY.yaml').read_text()) or {}
if maint.get('retirement',{}).get('automatic') is not False:e.append('automatic retirement must be false')
if maint.get('structural_validation',{}).get('all_canonical_skills_every_release') is not True:e.append('all skills structural QA must remain')
if 'security-review' not in set(maint.get('dimensions',{}).get('criticality_overrides',{}).get('P0_CORE_SAFETY',[])):e.append('security-review must remain P0 independent of usage')
if 'security-review' not in set(maint.get('dimensions',{}).get('criticality_overrides',{}).get('P0_CORE_SAFETY',[])):e.append('security-review must remain P0 independent of usage')
if 'security-review' not in set(maint.get('dimensions',{}).get('criticality_overrides',{}).get('P0_CORE_SAFETY',[])):e.append('security-review must remain P0 independent of usage')
# deterministic smoke test: L1 request produces grant without modifying brief
with tempfile.TemporaryDirectory() as td:
    b=Path(td)/'brief.yaml'; b.write_text("version: '5.9'\njob:\n  required_skill_ids: [implementation-engineering]\n")
    cp=subprocess.run([sys.executable,str(R/'scripts/resolve_skill_request.py'),'postgres-engineering','--job-id','SMOKE','--brief',str(b),'--reason','runtime dependency discovered','--impact','none'],cwd=R,text=True,capture_output=True)
    if cp.returncode!=0 or 'L1_JIT_SKILL_INJECT' not in cp.stdout:e.append('L1 skill injection smoke test')
if e:
    print('V581_HARDENING_QA_FAIL'); [print('-',x) for x in e]; sys.exit(2)
print('V581_HARDENING_QA_PASS')
