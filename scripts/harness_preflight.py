#!/usr/bin/env python3
"""V5.6.3 filesystem/harness readiness helper. No third-party package is installed here.
The active agent may research and install a required missing capability according to policy.
"""
from pathlib import Path
import argparse, json, shutil, os
ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--json',action='store_true'); args=ap.parse_args()
    skills=list((ROOT/'.agents/skills').glob('*/SKILL.md'))
    result={
      'agents_md':(ROOT/'AGENTS.md').is_file(),
      'handoff':(ROOT/'CODING-AGENT-HANDOFF.md').is_file(),
      'autopilot_goal':(ROOT/'planning/execution/AUTOPILOT-GOAL.md').is_file(),
      'stack_manifest':(ROOT/'planning/architecture/STACK-MANIFEST.yaml').is_file(),
      'skills_manifest':(ROOT/'planning/execution/SKILLS-MANIFEST.yaml').is_file(),
      'documentation_state':(ROOT/'planning/execution/DOCUMENTATION-STATE.yaml').is_file(),
      'context_state':(ROOT/'planning/execution/CONTEXT-STATE.yaml').is_file(),
      'parallelism_state':(ROOT/'planning/execution/PARALLELISM-STATE.yaml').is_file(),
      'execution_profile':(ROOT/'planning/execution/EXECUTION-PROFILE.yaml').is_file(),
      'worker_checkpoint_helper':(ROOT/'scripts/worker_checkpoint.py').is_file(),
      'convergence_matrix':(ROOT/'planning/execution/CONVERGENCE-MATRIX.json').is_file(),
      'evidence_index':(ROOT/'planning/execution/EVIDENCE-INDEX.json').is_file(),
      'docs_precommit_guard':(ROOT/'.githooks/pre-commit').is_file(),
      'docs_prepush_guard':(ROOT/'.githooks/pre-push').is_file(),
      'canonical_skills':len(skills),
      'git':bool(shutil.which('git')),
      'github_cli':bool(shutil.which('gh')),
      'pi':bool(shutil.which('pi')),
      'codex':bool(shutil.which('codex')),
      'claude':bool(shutil.which('claude')),
      'opencode':bool(shutil.which('opencode')),
      'policy':'capability_first_no_static_third_party_pin',
      'harness_contract':'pi_reference_codex_first_class_same_behavioral_contract',
    }
    result['filesystem_ready']=all(result[k] for k in ['agents_md','handoff','autopilot_goal','stack_manifest','skills_manifest','documentation_state','context_state','parallelism_state','execution_profile','worker_checkpoint_helper','convergence_matrix','evidence_index','docs_precommit_guard','docs_prepush_guard']) and result['canonical_skills']>0 and result['git']
    print(json.dumps(result,indent=2) if args.json else '\n'.join(f'{k}: {v}' for k,v in result.items()))
    return 0 if result['filesystem_ready'] else 2
if __name__=='__main__': raise SystemExit(main())
