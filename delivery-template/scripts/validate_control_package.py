#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, json, hashlib, sys
EXPECTED='.ctrlaltdelegate'
REQUIRED=['AGENTS.md','CODING-AGENT-START-PROMPT.md','CONTROL-PACKAGE.json','DELIVERY-MANIFEST.yaml','TARGET-GITIGNORE.fragment','planning/handoff/HANDOFF-STATUS.yaml','planning/handoff/CODING-AGENT-HANDOFF.md','planning/handoff/FINAL-START-PROMPT.md','planning/execution/STATE.md','planning/execution/PLANNING-BASELINE.json','planning/execution/JOB-GRAPH.json','planning/execution/LOOP-STATE.json','config/PLANNING-SKILL-ROUTING.yaml','planning/context/PLANNING-SKILL-STATE.yaml','docs/system/SKILL-DRIVEN-PLANNING.md','config/LOOP-CONTRACTS.yaml','config/SURFACE-POLICY.yaml','config/HARNESS-CONFORMANCE.yaml','config/ASSURANCE-PROFILES.yaml','docs/system/ASSURANCE-BEHAVIORAL-ORACLES-AND-ROOT-CAUSE-DEPTH.md','docs/system/WORKER-BRIEF-INTEGRITY-AND-CAPABILITY-ATTESTATION.md','planning/execution/ASSURANCE-STATE.yaml','planning/execution/ROOT-CAUSE-DEPTH.json','scripts/validate_assurance_control.py','scripts/worker_brief_hash.py','config/TECHNOLOGY-CAPABILITY-CATALOG.yaml','config/TECHNOLOGY-SELECTION-POLICY.yaml','config/TOOL-CAPABILITY-CATALOG.yaml','config/TOOL-SELECTION-POLICY.yaml','planning/architecture/TECHNOLOGY-EVALUATION.yaml','planning/execution/CAPABILITY-STATE.json','planning/execution/TOOL-LOCK.json','docs/system/CAPABILITY-DRIVEN-TECHNOLOGY-SELECTION.md','docs/system/CAPABILITY-RESOLUTION-AND-TOOL-BOOTSTRAP.md','config/BLOCKER-POLICY.yaml','config/PRODUCT-COMPLETION-POLICY.yaml','planning/product/PRODUCT-CONTRACT.yaml','planning/acceptance/USER-JOURNEY-ORACLES.yaml','planning/execution/BLOCKERS.json','planning/execution/DEFERRED-VALIDATION.json','planning/execution/ASSUMPTIONS.jsonl','planning/execution/PROVIDER-ATTESTATIONS.json','planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json','planning/execution/PRODUCT-DRIFT-REVIEW.json','planning/execution/EXECUTION-SNAPSHOT.json','docs/system/PRODUCT-RUNTIME-COMPLETION.md','docs/system/BLOCKERS-DEFERRED-VALIDATION-AND-CONTINUATION.md','docs/system/EXECUTION-SNAPSHOT-AND-CONTROLLED-TRANSITIONS.md','scripts/record_blocker.py','scripts/refresh_job_readiness.py','scripts/transition_job.py','scripts/build_execution_snapshot.py','scripts/validate_product_completion.py','scripts/record_loop_attempt.py']

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path',nargs='?',default='.'); args=ap.parse_args()
    root=Path(args.path).resolve();
    if root.name!=EXPECTED and (root/EXPECTED).is_dir(): root=root/EXPECTED
    errors=[]
    if root.name!=EXPECTED: errors.append(f'control directory must be {EXPECTED}')
    for rel in REQUIRED:
        if not (root/rel).is_file(): errors.append(f'missing required file: {rel}')
    cp={}
    try: cp=json.loads((root/'CONTROL-PACKAGE.json').read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'CONTROL-PACKAGE.json parse error: {e}')
    if cp:
        expected={'ctrlaltdelegate_version':'5.8.2','archive_name':'ctrlaltdelegate-delivery.zip','top_level_directory':EXPECTED,'control_root':'./.ctrlaltdelegate','control_visibility':'LOCAL_PRIVATE'}
        for k,v in expected.items():
            if cp.get(k)!=v: errors.append(f'CONTROL-PACKAGE {k} mismatch: {cp.get(k)!r} != {v!r}')
    p=root/'CODING-AGENT-START-PROMPT.md'; q=root/'planning/handoff/FINAL-START-PROMPT.md'
    if p.is_file() and q.is_file() and p.read_bytes()!=q.read_bytes(): errors.append('start prompt parity mismatch')
    if errors:
        print('CONTROL_PACKAGE_QA_FAIL'); [print('-',e) for e in errors]; return 2
    print('CONTROL_PACKAGE_QA_PASS', f'control_root={root}', f'required_files={len(REQUIRED)}')
    return 0
if __name__=='__main__': raise SystemExit(main())
