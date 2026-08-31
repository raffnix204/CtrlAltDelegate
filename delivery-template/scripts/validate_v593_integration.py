#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys, yaml
R=Path(__file__).resolve().parents[1]
e=[]
required=[
 'README.md','AGENTS.md','CHANGELOG-V5.9.3.md','RELEASE-METADATA.json',
 'config/MODEL-ROUTING-POLICY.yaml','config/CODE-INTELLIGENCE-POLICY.yaml',
 'docs/system/OH-MY-PI-FIRST-CLASS-HARNESS.md','docs/system/CODE-INTELLIGENCE-AND-GRAPHIFY.md',
 'adapters/oh-my-pi/HARNESS-CAPABILITIES.yaml','adapters/oh-my-pi/MODEL-ROUTING-MAPPING.yaml',
 'adapters/oh-my-pi/TASK-MAPPING.yaml','.omp/RULES.md','scripts/graphify_ctl.py',
 'planning/execution/CODE-INTELLIGENCE-STATE.yaml','planning/execution/MODEL-ROUTING-STATE.yaml'
]
for rel in required:
    if not (R/rel).exists(): e.append(f'missing {rel}')
try:
    m=json.loads((R/'RELEASE-METADATA.json').read_text())
    if m.get('version')!='5.9.3': e.append('metadata version mismatch')
    if m.get('canonical_skill_count')!=154: e.append('metadata skill count mismatch')
except Exception as ex: e.append(f'metadata parse: {ex}')
if len(list((R/'.agents/skills').glob('*/SKILL.md')))!=154: e.append('canonical skill count != 154')
if len(list((R/'.claude/skills').glob('*/SKILL.md')))!=154: e.append('claude adapter count != 154')
try:
    hc=yaml.safe_load((R/'config/HARNESS-CONFORMANCE.yaml').read_text())
    omp=hc['harnesses']['oh-my-pi']
    if omp.get('support')!='FIRST_CLASS': e.append('OMP not FIRST_CLASS')
    if omp.get('canonical_skills')!='.agents/skills': e.append('OMP canonical skill root mismatch')
    if not omp.get('per_subagent_model_selection'): e.append('OMP model selection not enabled')
except Exception as ex: e.append(f'harness parse: {ex}')
try:
    mr=yaml.safe_load((R/'config/MODEL-ROUTING-POLICY.yaml').read_text())
    if str(mr.get('patch_release'))!='5.9.3': e.append('model routing patch release mismatch')
    fr=mr['openai_mapping']['FRONTIER']
    if fr.get('model')!='gpt-5.6-sol' or fr.get('reasoning_effort_ceiling')!='high': e.append('Sol high mapping mismatch')
    if not {'xhigh','max'}.issubset(set(fr.get('forbidden_efforts') or [])): e.append('Sol forbidden effort set incomplete')
    om=mr.get('oh_my_pi_mapping') or {}
    if om.get('generic_effort_hi_for_frontier')!='FORBIDDEN': e.append('OMP generic hi not forbidden for FRONTIER')
except Exception as ex: e.append(f'model policy parse: {ex}')
try:
    ci=yaml.safe_load((R/'config/CODE-INTELLIGENCE-POLICY.yaml').read_text())
    gp=ci['providers']['graphify']
    if gp.get('verified_version')!='0.9.53': e.append('Graphify pinned baseline mismatch')
    if gp.get('install_preference')!='HOST_USER_SCOPE_WITH_EXPLICIT_ONCE_PER_HOST_CONSENT': e.append('Graphify host-consent policy mismatch')
    pr=ci.get('principles') or {}
    if not pr.get('code_intelligence_is_navigation_not_proof'): e.append('Graphify navigation-not-proof missing')
    if not pr.get('all_projects_run_code_intelligence_preflight'): e.append('code intelligence preflight not universal')
except Exception as ex: e.append(f'code intelligence parse: {ex}')
# Static OMP Sol safety check
for rel in ['.omp/RULES.md','adapters/oh-my-pi/MODEL-ROUTING-MAPPING.yaml','docs/system/OH-MY-PI-FIRST-CLASS-HARNESS.md']:
    s=(R/rel).read_text().lower()
    if 'effort: hi' not in s or 'high' not in s: e.append(f'{rel}: OMP Sol effort caveat missing')
# Graphify wrapper prepare must be non-mutating and machine-readable
try:
    cp=subprocess.run([sys.executable,str(R/'scripts/graphify_ctl.py'),'prepare'],cwd=R,capture_output=True,text=True,timeout=15)
    if cp.returncode!=0: e.append('graphify_ctl prepare failed')
    else:
        out=json.loads(cp.stdout)
        if out.get('action') not in {'REUSE_AND_VERIFY','INSTALL_HOST_WITH_RECORDED_CONSENT','INSTALL_PROJECT_LOCAL','USE_FALLBACK','ASK_USER'}:
            e.append('graphify_ctl prepare action invalid')
except Exception as ex: e.append(f'graphify_ctl prepare: {ex}')
if '/graphify-out/' not in (R/'.gitignore').read_text(): e.append('graphify-out not ignored')
pre=(R/'scripts/harness_preflight.py').read_text()
if 'capability_negotiation_no_model_routing' in pre: e.append('stale no-model-routing preflight policy')
if "'oh_my_pi'" not in pre or "'graphify'" not in pre: e.append('preflight lacks OMP/Graphify detection')
if e:
    print('V5.9.3 INTEGRATION FAILED')
    for x in e: print('-',x)
    sys.exit(1)
print('V5.9.3 INTEGRATION OK')
