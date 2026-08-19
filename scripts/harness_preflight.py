#!/usr/bin/env python3
from pathlib import Path
import argparse, json, shutil
R=Path(__file__).resolve().parents[1]
def has(x): return bool(shutil.which(x))
def main():
    a=argparse.ArgumentParser(); a.add_argument('--json',action='store_true'); args=a.parse_args()
    skills=list((R/'.agents/skills').glob('*/SKILL.md'))
    r={'version':'5.7.1','canonical_skills':len(skills),'git':has('git'),'gh':has('gh'),'pi':has('pi'),'codex':has('codex'),'claude':has('claude'),'opencode':has('opencode'),'deepseek_harness':has('dsh') or has('deepseek-harness'),'conformance_file':(R/'config/HARNESS-CONFORMANCE.yaml').is_file(),'loop_control':(R/'config/LOOP-CONTRACTS.yaml').is_file(),'job_graph':(R/'planning/execution/JOB-GRAPH.json').is_file(),'surface_policy':(R/'config/SURFACE-POLICY.yaml').is_file(),'policy':'capability_negotiation_no_model_routing'}
    r['filesystem_ready']=r['canonical_skills']>0 and r['git'] and all(r[k] for k in ['conformance_file','loop_control','job_graph','surface_policy'])
    print(json.dumps(r,indent=2) if args.json else '\n'.join(f'{k}: {v}' for k,v in r.items())); return 0 if r['filesystem_ready'] else 2
if __name__=='__main__': raise SystemExit(main())
