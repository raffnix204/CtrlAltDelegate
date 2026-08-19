#!/usr/bin/env python3
from pathlib import Path
import json, shutil, subprocess, sys
R=Path(__file__).resolve().parents[1]

def exists(rel): return (R/rel).exists()
def cmd(name): return shutil.which(name) is not None
checks={
 'filesystem': all(exists(x) for x in ['AGENTS.md','.agents/skills/CATALOG.yaml','planning/execution/STATE.md']),
 'loop_control': all(exists(x) for x in ['config/LOOP-CONTRACTS.yaml','planning/execution/LOOP-STATE.json']),
 'job_graph': exists('planning/execution/JOB-GRAPH.json'),
 'surface_policy': exists('config/SURFACE-POLICY.yaml'),
 'harness_conformance': exists('config/HARNESS-CONFORMANCE.yaml'),
 'handoff_validator': exists('scripts/validate_handoff_delivery.py'),
 'git': cmd('git'), 'github_cli':cmd('gh'), 'pi':cmd('pi'), 'codex':cmd('codex'), 'claude':cmd('claude'), 'opencode':cmd('opencode'),
 'deepseek_harness': cmd('dsh') or cmd('deepseek-harness'),
}
checks['core_ready']=all(checks[k] for k in ['filesystem','loop_control','job_graph','surface_policy','harness_conformance','handoff_validator','git'])
print(json.dumps(checks,indent=2)); raise SystemExit(0 if checks['core_ready'] else 2)
