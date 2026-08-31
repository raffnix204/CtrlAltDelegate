#!/usr/bin/env python3
from pathlib import Path
import argparse, json, shutil, subprocess
R=Path(__file__).resolve().parents[1]
def has(x): return bool(shutil.which(x))
def version(cmd):
    if not has(cmd): return None
    for args in ([cmd,"--version"],[cmd,"version"]):
        try:
            r=subprocess.run(args,capture_output=True,text=True,timeout=5)
            out=(r.stdout or r.stderr or "").strip()
            if r.returncode==0 and out: return out.splitlines()[0]
        except Exception: pass
    return None
def main():
    a=argparse.ArgumentParser(); a.add_argument('--json',action='store_true'); args=a.parse_args()
    skills=list((R/'.agents/skills').glob('*/SKILL.md'))
    r={
      'version':'5.9.3','canonical_skills':len(skills),'git':has('git'),'gh':has('gh'),
      'pi':has('pi'),'oh_my_pi':has('omp'),'oh_my_pi_version':version('omp'),'codex':has('codex'),
      'command_code':has('cmd'),'claude':has('claude'),'opencode':has('opencode'),
      'deepseek_harness':has('dsh') or has('deepseek-harness'),'crw':has('crw'),'obscura':has('obscura'),
      'graphify':has('graphify'),'graphify_version':version('graphify'),
      'conformance_file':(R/'config/HARNESS-CONFORMANCE.yaml').is_file(),
      'tool_catalog':(R/'config/TOOL-CAPABILITY-CATALOG.yaml').is_file(),
      'technology_catalog':(R/'config/TECHNOLOGY-CAPABILITY-CATALOG.yaml').is_file(),
      'loop_control':(R/'config/LOOP-CONTRACTS.yaml').is_file(),
      'job_graph':(R/'planning/execution/JOB-GRAPH.json').is_file(),
      'surface_policy':(R/'config/SURFACE-POLICY.yaml').is_file(),
      'assurance_control':(R/'config/ASSURANCE-PROFILES.yaml').is_file(),
      'model_routing_policy':(R/'config/MODEL-ROUTING-POLICY.yaml').is_file(),
      'code_intelligence_policy':(R/'config/CODE-INTELLIGENCE-POLICY.yaml').is_file(),
      'policy':'capability_class_adaptive_model_routing_plus_graph_query_first_code_intelligence'
    }
    r['filesystem_ready']=r['canonical_skills']>0 and r['git'] and all(r[k] for k in ['conformance_file','tool_catalog','technology_catalog','loop_control','job_graph','surface_policy','model_routing_policy','code_intelligence_policy'])
    print(json.dumps(r,indent=2) if args.json else '\n'.join(f'{k}: {v}' for k,v in r.items())); return 0 if r['filesystem_ready'] else 2
if __name__=='__main__': raise SystemExit(main())
