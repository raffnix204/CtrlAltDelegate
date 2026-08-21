#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, json, re
EXPECTED='.ctrlaltdelegate'
REQUIRED=['AGENTS.md','CLAUDE.md','CODING-AGENT-START-PROMPT.md','CONTROL-PACKAGE.json','DELIVERY-MANIFEST.yaml','TARGET-GITIGNORE.fragment','.agents/skills/CATALOG.yaml','config/SKILL-ROUTING-RULES.yaml','config/PLANNING-SKILL-ROUTING.yaml','docs/system/SKILL-DRIVEN-PLANNING.md','planning/context/PLANNING-SKILL-STATE.yaml','config/LOOP-CONTRACTS.yaml','config/SURFACE-POLICY.yaml','config/HARNESS-CONFORMANCE.yaml','config/ASSURANCE-PROFILES.yaml','docs/system/ASSURANCE-BEHAVIORAL-ORACLES-AND-ROOT-CAUSE-DEPTH.md','docs/system/WORKER-BRIEF-INTEGRITY-AND-CAPABILITY-ATTESTATION.md','planning/execution/ASSURANCE-STATE.yaml','planning/execution/ROOT-CAUSE-DEPTH.json','scripts/validate_assurance_control.py','scripts/worker_brief_hash.py','config/SKILL-ESCALATION-POLICY.yaml','planning/execution/SKILL-REQUESTS.jsonl','planning/execution/SKILL-USAGE-EVENTS.jsonl','docs/system/RUNTIME-SKILL-ESCALATION.md','config/SKILL-MAINTENANCE-POLICY.yaml','config/CONTROL-VISIBILITY.yaml','scripts/validate_handoff_delivery.py','scripts/validate_control_package.py','planning/PROJECT.md','planning/REQUIREMENTS.md','planning/discovery/DISCOVERY-STATE.md','planning/discovery/TECHNICAL-PREFERENCES.yaml','planning/handoff/HANDOFF-STATUS.yaml','planning/handoff/CODING-AGENT-HANDOFF.md','planning/handoff/FINAL-START-PROMPT.md','planning/execution/STATE.md','planning/execution/PLANNING-BASELINE.json','planning/execution/PENDING-INPUT.jsonl','planning/execution/ARTIFACT-CONSISTENCY.json','planning/execution/LEARNING-CANDIDATES.jsonl','planning/execution/EXECUTION-PROFILE.yaml','planning/execution/AUTOPILOT-GOAL.md','planning/execution/JOB-GRAPH.json','planning/execution/LOOP-STATE.json','planning/execution/DECISION-LEDGER.jsonl','planning/architecture/STACK-MANIFEST.yaml','planning/architecture/PROGRAM-DESIGN.md','planning/execution/SKILLS-MANIFEST.yaml','planning/execution/CONVERGENCE-MATRIX.json','planning/execution/EVIDENCE-INDEX.json','planning/research/RESEARCH-POLICY.yaml']

def scalar(text,key):
    m=re.search(rf'(?m)^\s*{re.escape(key)}:\s*[\'\"]?([^\n\'\"]+)',text); return m.group(1).strip() if m else None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path',nargs='?',default='.'); ap.add_argument('--allow-not-ready',action='store_true'); a=ap.parse_args()
    r=Path(a.path).resolve();
    if r.name!=EXPECTED and (r/EXPECTED).is_dir(): r=r/EXPECTED
    errors=[]
    if r.name!=EXPECTED: errors.append(f'control directory must be named exactly {EXPECTED}')
    for rel in REQUIRED:
        if not (r/rel).is_file(): errors.append(f'missing required file: {rel}')
    p=r/'CODING-AGENT-START-PROMPT.md'; q=r/'planning/handoff/FINAL-START-PROMPT.md'
    if p.is_file():
        txt=p.read_text(encoding='utf-8')
        for token in ['ctrlaltdelegate-delivery.zip','./.ctrlaltdelegate','PROJECT_ROOT','BLOCKED_DELIVERY_INCOMPLETE','EXECUTION_HANDOFF','LOCAL_PRIVATE']:
            if token not in txt: errors.append(f'start prompt missing {token}')
        if q.is_file() and p.read_bytes()!=q.read_bytes(): errors.append('start prompt parity mismatch')
    s=r/'planning/handoff/HANDOFF-STATUS.yaml'
    if s.is_file():
        txt=s.read_text(encoding='utf-8')
        for key,val in {'version':'5.8.1','mode':'EXECUTION_HANDOFF','topology':'ZIP_TO_HIDDEN_CONTROL_ROOT','control_root':'./.ctrlaltdelegate','control_visibility':'LOCAL_PRIVATE'}.items():
            got=scalar(txt,key)
            if got!=val: errors.append(f'handoff {key} mismatch: {got!r}')
        if not a.allow_not_ready:
            if scalar(txt,'status')!='READY': errors.append('handoff status must be READY')
            if scalar(txt,'unresolved_blocking_decisions')!='0': errors.append('blocking decisions must be zero')
            for key in ['required_paths_present','prompt_paths_verified','planning_ready','planning_baseline_attested','zero_blocking_decisions','control_tree_verified_before_archive','planning_skill_state_present','assurance_state_present']:
                if scalar(txt,key)!='true': errors.append(f'closure check not true: {key}')
    baseline=r/'planning/execution/PLANNING-BASELINE.json'
    if baseline.is_file():
        try:
            bd=json.loads(baseline.read_text(encoding='utf-8'))
            if bd.get('status')!='ATTESTED' or not bd.get('aggregate_sha256'): errors.append('planning baseline must be ATTESTED')
        except Exception as e: errors.append(f'planning baseline parse error: {e}')
    if errors:
        print('HANDOFF_DELIVERY_QA_FAIL'); [print('-',e) for e in errors]; return 2
    print('HANDOFF_DELIVERY_QA_PASS', f'control_root={r}', f'required_files={len(REQUIRED)}'); return 0
if __name__=='__main__': raise SystemExit(main())
