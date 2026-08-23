#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, json, hashlib, sys
EXPECTED='.ctrlaltdelegate'
REQUIRED=['AGENTS.md','CODING-AGENT-START-PROMPT.md','CONTROL-PACKAGE.json','DELIVERY-MANIFEST.yaml','TARGET-GITIGNORE.fragment','planning/handoff/HANDOFF-STATUS.yaml','planning/handoff/CODING-AGENT-HANDOFF.md','planning/handoff/FINAL-START-PROMPT.md','planning/execution/STATE.md','planning/execution/PLANNING-BASELINE.json','planning/execution/JOB-GRAPH.json','planning/execution/LOOP-STATE.json','config/PLANNING-SKILL-ROUTING.yaml','planning/context/PLANNING-SKILL-STATE.yaml','docs/system/SKILL-DRIVEN-PLANNING.md','config/LOOP-CONTRACTS.yaml','config/SURFACE-POLICY.yaml','config/HARNESS-CONFORMANCE.yaml','config/ASSURANCE-PROFILES.yaml','docs/system/ASSURANCE-BEHAVIORAL-ORACLES-AND-ROOT-CAUSE-DEPTH.md','docs/system/WORKER-BRIEF-INTEGRITY-AND-CAPABILITY-ATTESTATION.md','planning/execution/ASSURANCE-STATE.yaml','planning/execution/ROOT-CAUSE-DEPTH.json','scripts/validate_assurance_control.py','scripts/worker_brief_hash.py','config/TECHNOLOGY-CAPABILITY-CATALOG.yaml','config/TECHNOLOGY-SELECTION-POLICY.yaml','config/TOOL-CAPABILITY-CATALOG.yaml','config/TOOL-SELECTION-POLICY.yaml','planning/architecture/TECHNOLOGY-EVALUATION.yaml','planning/execution/CAPABILITY-STATE.json','planning/execution/TOOL-LOCK.json','docs/system/CAPABILITY-DRIVEN-TECHNOLOGY-SELECTION.md','docs/system/CAPABILITY-RESOLUTION-AND-TOOL-BOOTSTRAP.md','config/BLOCKER-POLICY.yaml','config/PRODUCT-COMPLETION-POLICY.yaml','planning/product/PRODUCT-CONTRACT.yaml','planning/acceptance/USER-JOURNEY-ORACLES.yaml','planning/execution/BLOCKERS.json','planning/execution/DEFERRED-VALIDATION.json','planning/execution/ASSUMPTIONS.jsonl','planning/execution/PROVIDER-ATTESTATIONS.json','planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json','planning/execution/PRODUCT-DRIFT-REVIEW.json','planning/execution/EXECUTION-SNAPSHOT.json','docs/system/PRODUCT-RUNTIME-COMPLETION.md','docs/system/BLOCKERS-DEFERRED-VALIDATION-AND-CONTINUATION.md','docs/system/EXECUTION-SNAPSHOT-AND-CONTROLLED-TRANSITIONS.md','scripts/record_blocker.py','scripts/refresh_job_readiness.py','scripts/transition_job.py','scripts/build_execution_snapshot.py','scripts/validate_product_completion.py','scripts/record_loop_attempt.py']
V59_REQUIRED=['config/EXECUTION-CONTROL-POLICY.yaml', 'config/STATE-RECONCILIATION.yaml', 'config/PLANNING-CONVERGENCE-POLICY.yaml', 'config/REVIEW-VERDICT-POLICY.yaml', 'config/CONTROL-EFFECTIVENESS-POLICY.yaml', 'config/SKILL-DISCOVERY-POLICY.yaml', 'planning/architecture/PLANNING-ARTIFACT-GRAPH.yaml', 'planning/execution/CONTROL-STATE.json', 'planning/execution/CONTROL-MUTATION-LOG.jsonl', 'planning/execution/CONTROL-EVENTS.jsonl', 'planning/execution/WORKER-CLAIMS.json', 'planning/execution/ATTEMPT-STATE.json', 'planning/execution/JOB-ATTEMPTS.jsonl', 'planning/execution/RECOVERY-ACTIONS.jsonl', 'planning/execution/RECONCILIATION-LOG.jsonl', 'planning/execution/CONTROL-INSIGHTS.jsonl', 'planning/execution/RULINGS.jsonl', 'planning/execution/REVIEW-VERDICTS.json', 'planning/execution/VERIFICATION-BASELINES.json', 'planning/execution/PLANNING-CONVERGENCE.json', 'docs/schemas/WORKER-RESULT.schema.json', 'docs/templates/WORKER-RESULT.template.json', 'scripts/control_state.py', 'scripts/validate_control_mutation.py', 'scripts/claim_job.py', 'scripts/heartbeat_job.py', 'scripts/start_job_attempt.py', 'scripts/settle_job_attempt.py', 'scripts/reconcile_execution_state.py', 'scripts/record_recovery_action.py', 'scripts/validate_worker_result.py', 'scripts/record_verification_baseline.py', 'scripts/classify_verification_delta.py', 'scripts/validate_planning_convergence.py', 'scripts/record_review_verdict.py', 'scripts/execution_stop_gate.py', 'scripts/validate_oracle_integrity.py', 'scripts/validate_decision_coverage.py', 'scripts/validate_planning_artifact_graph.py']
REQUIRED.extend(x for x in V59_REQUIRED if x not in REQUIRED)


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
        expected={'ctrlaltdelegate_version':'5.9','archive_name':'ctrlaltdelegate-delivery.zip','top_level_directory':EXPECTED,'control_root':'./.ctrlaltdelegate','control_visibility':'LOCAL_PRIVATE'}
        for k,v in expected.items():
            if cp.get(k)!=v: errors.append(f'CONTROL-PACKAGE {k} mismatch: {cp.get(k)!r} != {v!r}')
    p=root/'CODING-AGENT-START-PROMPT.md'; q=root/'planning/handoff/FINAL-START-PROMPT.md'
    if p.is_file() and q.is_file() and p.read_bytes()!=q.read_bytes(): errors.append('start prompt parity mismatch')
    if errors:
        print('CONTROL_PACKAGE_QA_FAIL'); [print('-',e) for e in errors]; return 2
    print('CONTROL_PACKAGE_QA_PASS', f'control_root={root}', f'required_files={len(REQUIRED)}')
    return 0
if __name__=='__main__': raise SystemExit(main())
