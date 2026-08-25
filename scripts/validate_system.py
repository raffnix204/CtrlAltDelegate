#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml, json

R=Path(__file__).resolve().parents[1]
errors=[]
skill_root=R/'.agents/skills'
skills={p.parent.name:p for p in skill_root.glob('*/SKILL.md')}

def norm(s):
    s=re.sub(r'^\d+\.\s*','',s.strip())
    return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()

def heading_regions(body):
    hs=list(re.finditer(r'^(#{2,3})\s+(.+?)\s*$',body,re.M))
    for i,h in enumerate(hs):
        level=len(h.group(1)); end=len(body)
        for nxt in hs[i+1:]:
            if len(nxt.group(1))<=level:
                end=nxt.start(); break
        yield h, body[h.end():end]

try:
    catalog=yaml.safe_load((skill_root/'CATALOG.yaml').read_text(encoding='utf-8'))
except Exception as e:
    errors.append(f'catalog parse: {e}'); catalog={}
entries=[x for x in catalog.get('skills',[]) if isinstance(x,dict)]
ids={x.get('id') for x in entries}
if str(catalog.get('version'))!='5.9': errors.append('catalog version mismatch')
if catalog.get('library')!='software-planning-lead-v5.9': errors.append('catalog library mismatch')
if (catalog.get('policy') or {}).get('skill_schema')!='5.7.1-domain-expertise+planning-registry': errors.append('catalog skill_schema mismatch')
if catalog.get('library_count') != len(skills): errors.append(f"catalog library_count={catalog.get('library_count')} actual={len(skills)}")
if ids != set(skills): errors.append(f'catalog/file mismatch missing_files={sorted(ids-set(skills))} missing_catalog={sorted(set(skills)-ids)}')

for sid,p in sorted(skills.items()):
    t=p.read_text(encoding='utf-8')
    if not t.startswith('---\n'):
        errors.append(f'{sid}: missing frontmatter'); continue
    end=t.find('\n---\n',4)
    try: fm=yaml.safe_load(t[4:end])
    except Exception as e: errors.append(f'{sid}: yaml {e}'); continue
    if fm.get('name') != sid: errors.append(f'{sid}: frontmatter name mismatch')
    if not str(fm.get('description','')).strip(): errors.append(f'{sid}: missing description')
    if len(t) < 1200: errors.append(f'{sid}: skill entrypoint too thin ({len(t)} chars)')
    if 'For autonomous execution, convert this concern into an explicit design or implementation decision' in t: errors.append(f'{sid}: legacy templated boilerplate remains')
    if re.search(r'^## V5\.[0-9.]+ Autonomous Research & Routing Contract\s*$',t,re.M): errors.append(f'{sid}: duplicated global execution contract remains')
    h2=[ln[3:].strip() for ln in t.splitlines() if ln.startswith('## ') and not ln.startswith('### ')]
    metadata_only={'Purpose','Purpose / Ownership','Profiles','Typical roles','Progressive References','Companion Skills','Related'}
    if len([h for h in h2 if h not in metadata_only]) < 3: errors.append(f'{sid}: insufficient domain decision/workflow surface')

    body=t[end+5:] if end>=0 else t
    # EMPTY_SECTION_GATE: leaf H2/H3 must have body; H2 with child H3 is a valid container.
    for h,region in heading_regions(body):
        level=len(h.group(1)); child=bool(re.search(r'^#{%d,3}\s+'%(level+1),region,re.M)) if level<3 else False
        if not child and not region.strip(): errors.append(f'{sid}: empty leaf section {h.group(1)} {h.group(2)}')
    # Expert Decision points need substantive body and must not merely repeat the heading.
    m=re.search(r'^## Expert Decision Model\s*$([\s\S]*?)(?=^## |\Z)',body,re.M)
    if m:
        sec=m.group(1); hs=list(re.finditer(r'^###\s+(.+?)\s*$',sec,re.M))
        for i,h in enumerate(hs):
            b=sec[h.end():hs[i+1].start() if i+1<len(hs) else len(sec)].strip()
            if not b: errors.append(f'{sid}: empty Expert Decision point {h.group(1)}'); continue
            plain=' '.join(x.strip() for x in b.splitlines() if x.strip() and not x.lstrip().startswith(('-', '*', '`')))
            if len(re.sub(r'\s+',' ',plain)) < 40: errors.append(f'{sid}: Expert Decision body too thin: {h.group(1)}')
            first_para=b.split('\n\n',1)[0].strip().strip('*_` ')
            if norm(first_para.rstrip('.;:')) == norm(h.group(1).rstrip('.;:')): errors.append(f'{sid}: Expert Decision repeats heading without added value: {h.group(1)}')

entry_map={e['id']:e for e in entries if e.get('id')}
actual_ref_count=0
for sid,e in entry_map.items():
    declared=set(e.get('references',[]) or [])
    actual={str(p.relative_to(skill_root/sid)).replace('\\','/') for p in (skill_root/sid/'references').rglob('*') if p.is_file()} if (skill_root/sid/'references').exists() else set()
    actual_ref_count += len(actual)
    if declared != actual: errors.append(f'{sid}: catalog/reference mismatch declared_only={sorted(declared-actual)} actual_only={sorted(actual-declared)}')
    for ref in actual:
        rt=(skill_root/sid/ref).read_text(encoding='utf-8')
        if len(rt)<300: errors.append(f'{sid}: progressive reference too thin {ref}')
        if not re.search(r'(?i)when|use this reference|read this',rt): errors.append(f'{sid}: reference lacks loading guidance {ref}')

wrappers={p.parent.name:p for p in (R/'.claude/skills').glob('*/SKILL.md')}
if set(wrappers) != set(skills): errors.append('Claude wrapper set does not match canonical skills')
for sid,p in wrappers.items():
    wt=p.read_text(encoding='utf-8')
    if f'../../../.agents/skills/{sid}/SKILL.md' not in wt: errors.append(f'{sid}: bad Claude adapter')

required=[
'config/BLOCKER-POLICY.yaml','config/PRODUCT-COMPLETION-POLICY.yaml','planning/product/PRODUCT-CONTRACT.yaml','planning/acceptance/USER-JOURNEY-ORACLES.yaml','planning/execution/BLOCKERS.json','planning/execution/DEFERRED-VALIDATION.json','planning/execution/PROVIDER-ATTESTATIONS.json','planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json','planning/execution/PRODUCT-DRIFT-REVIEW.json','planning/execution/EXECUTION-SNAPSHOT.json','scripts/transition_job.py','scripts/build_execution_snapshot.py','scripts/refresh_job_readiness.py','scripts/validate_product_completion.py','scripts/record_loop_attempt.py','scripts/record_blocker.py','config/SKILL-OPTIMIZATION-POLICY.yaml','docs/system/SKILLOPT-OFFLINE-SKILL-LAB.md','scripts/validate_v582_completion.py','docs/system/ASSURANCE-BEHAVIORAL-ORACLES-AND-ROOT-CAUSE-DEPTH.md','docs/system/WORKER-BRIEF-INTEGRITY-AND-CAPABILITY-ATTESTATION.md','config/ASSURANCE-PROFILES.yaml','planning/execution/ASSURANCE-STATE.yaml','planning/execution/ROOT-CAUSE-DEPTH.json','docs/templates/WORKER-BRIEF.template.yaml','docs/templates/HARNESS-ATTESTATION.template.json','scripts/validate_assurance_control.py','scripts/worker_brief_hash.py','planning/execution/SKILLS-MANIFEST.yaml','planning/architecture/STACK-MANIFEST.yaml','planning/research/RESEARCH-POLICY.yaml','planning/research/RESEARCH-REGISTER.md','planning/execution/DOCUMENTATION-STATE.yaml','planning/execution/DOCUMENTATION-COVERAGE.md','planning/execution/CONTEXT-STATE.yaml','planning/execution/PARALLELISM-STATE.yaml','planning/execution/EXECUTION-PROFILE.yaml','delivery-template/planning/execution/EXECUTION-PROFILE.yaml','config/DOCUMENTATION-RULES.yaml','docs/system/DOCUMENTATION-LIFECYCLE.md','docs/system/CONTEXT-AND-PARALLELISM.md','docs/system/CAPABILITY-BOOTSTRAP.md','.githooks/pre-commit','.githooks/pre-push','scripts/docs_freshness_gate.py','scripts/install_git_guards.py','config/STACK-SIGNALS.yaml','config/SKILL-ROUTING-RULES.yaml','planning/execution/CONVERGENCE-MATRIX.json','planning/execution/EVIDENCE-INDEX.json','planning/repository/REPO-CONTEXT-MAP.md','docs/system/QUALITY-EFFICIENCY-HARDENING.md','docs/system/CONVERGENCE-AND-EVIDENCE.md','docs/system/SKILL-EVALUATION.md','docs/system/SKILL-EXECUTION-CONTRACT.md','docs/system/SKILL-SCHEMA-V5.6.1.md','docs/system/SKILL-SCHEMA-V5.7.1.md','docs/system/SKILL-LIBRARY-QUALITY-AUDIT-V5.6.1.md','.agents/skills/SOURCE-RESEARCH-MATRIX.yaml','docs/system/CODEX-FIRST-CLASS-HARNESS.md','docs/system/GITHUB-DIRECT-HANDOFF.md','docs/system/PROGRAM-DESIGN-AND-VERTICAL-SLICES.md','docs/system/REPOSITORY-LAYOUT-AND-STATE.md','docs/system/COLLABORATIVE-DISCOVERY-AND-CONSTRAINTS.md','docs/system/ADAPTIVE-EXECUTION-AND-WORKER-LIVENESS.md','docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md','docs/system/LANGUAGE-AND-INTERACTION.md','docs/system/DETERMINISTIC-PLANNING-DELIVERY-AND-HANDOFF.md','docs/templates/NESTED-CODING-AGENT-START-PROMPT.template.md','docs/templates/NESTED-DELIVERY-MANIFEST.template.yaml','docs/templates/HANDOFF-STATUS.template.yaml','scripts/validate_handoff_delivery.py','planning/discovery/TECHNICAL-PREFERENCES.yaml','planning/discovery/DISCOVERY-STATE.md','planning/architecture/PROGRAM-DESIGN.md','planning/context/PROJECT-CONTEXT.md','planning/handoff/START-HERE.md','planning/handoff/CODING-AGENT-HANDOFF.md','planning/handoff/FINAL-START-PROMPT.md','planning/handoff/DELIVERY-MANIFEST.yaml','scripts/quality_gate.py','scripts/worker_checkpoint.py','scripts/validate_skill_evals.py','evals/skills/scenarios.yaml','docs/system/CAPABILITY-DRIVEN-TECHNOLOGY-SELECTION.md','config/TECHNOLOGY-CAPABILITY-CATALOG.yaml','config/TECHNOLOGY-SELECTION-POLICY.yaml','docs/system/CAPABILITY-RESOLUTION-AND-TOOL-BOOTSTRAP.md','config/TOOL-CAPABILITY-CATALOG.yaml','config/TOOL-SELECTION-POLICY.yaml','planning/architecture/TECHNOLOGY-EVALUATION.yaml','planning/execution/CAPABILITY-STATE.json','planning/execution/TOOL-LOCK.json','docs/system/COMMAND-CODE-FIRST-CLASS-PREVIEW.md','adapters/command-code/HARNESS-CAPABILITIES.yaml','scripts/detect_tool_capabilities.py','scripts/resolve_capability_provider.py','scripts/bootstrap_tool.py','scripts/verify_tool_capability.py','release-handoff/UPDATE-PUBLIC-GITHUB-REPO.md','README.md','config/SKILL-ESCALATION-POLICY.yaml','planning/execution/SKILL-REQUESTS.jsonl','planning/execution/SKILL-USAGE-EVENTS.jsonl','docs/system/RUNTIME-SKILL-ESCALATION.md','scripts/resolve_skill_request.py','config/SKILL-MAINTENANCE-POLICY.yaml','scripts/aggregate_skill_usage.py','docs/system/USAGE-AWARE-SKILL-MAINTENANCE.md','release/RELEASE-BASELINE.json','release/RELEASE-DELTA.json','release/RELEASE-CLAIMS.yaml','scripts/validate_release_claims.py']
for x in required:
    if not (R/x).exists(): errors.append(f'missing {x}')

v59_required=['CHANGELOG-V5.9.md','config/EXECUTION-CONTROL-POLICY.yaml','config/STATE-RECONCILIATION.yaml','config/PLANNING-CONVERGENCE-POLICY.yaml','config/REVIEW-VERDICT-POLICY.yaml','config/CONTROL-EFFECTIVENESS-POLICY.yaml','config/SKILL-DISCOVERY-POLICY.yaml','planning/execution/CONTROL-STATE.json','planning/execution/WORKER-CLAIMS.json','planning/execution/ATTEMPT-STATE.json','planning/execution/JOB-ATTEMPTS.jsonl','planning/execution/RECOVERY-ACTIONS.jsonl','planning/execution/RECONCILIATION-LOG.jsonl','planning/execution/REVIEW-VERDICTS.json','planning/architecture/PLANNING-ARTIFACT-GRAPH.yaml','docs/schemas/WORKER-RESULT.schema.json','scripts/validate_control_mutation.py','scripts/claim_job.py','scripts/start_job_attempt.py','scripts/settle_job_attempt.py','scripts/reconcile_execution_state.py','scripts/validate_worker_result.py','scripts/validate_planning_convergence.py','scripts/validate_skill_discovery.py','scripts/validate_v59_control_plane.py']
for x in v59_required:
    if not (R/x).exists(): errors.append(f'missing V5.9 surface {x}')

for path,key in [('planning/execution/SKILLS-MANIFEST.yaml','library_count')]:
    try:
        d=yaml.safe_load((R/path).read_text(encoding='utf-8'))
        if str(d.get('version'))!='5.9': errors.append(f'{path} version mismatch')
        if key and d.get(key)!=len(skills): errors.append(f'{path} {key} mismatch')
    except Exception as e: errors.append(f'{path} parse: {e}')
try:
    pref=yaml.safe_load((R/'planning/discovery/TECHNICAL-PREFERENCES.yaml').read_text(encoding='utf-8'))
    if str(pref.get('version'))!='5.9': errors.append('TECHNICAL-PREFERENCES version mismatch')
    if pref.get('decision_style') not in {'AUTO','AUTOPILOT','COLLABORATIVE','DIRECTED'}: errors.append('TECHNICAL-PREFERENCES invalid decision_style')
    required_items={'technology','runtime_hosting','data_security_region','existing_environment'}
    if not required_items.issubset(set((pref.get('items') or {}).keys())): errors.append('TECHNICAL-PREFERENCES missing required item groups')
    for key,val in (pref.get('items') or {}).items():
        if isinstance(val,dict) and val.get('strength') not in {'REQUIRED','PREFERRED','AUTO'}: errors.append(f'TECHNICAL-PREFERENCES invalid strength for {key}')
except Exception as e: errors.append(f'TECHNICAL-PREFERENCES parse: {e}')
try:
    ep=yaml.safe_load((R/'planning/execution/EXECUTION-PROFILE.yaml').read_text(encoding='utf-8'))
    if str(ep.get('version'))!='5.9': errors.append('EXECUTION-PROFILE version mismatch')
    if ep.get('profile') not in {'AUTO','MICRO','SMALL','STANDARD','HIGH_RISK'}: errors.append('EXECUTION-PROFILE invalid profile')
    if set(ep.get('allowed_assurance_profiles') or []) != {'NORMAL','ELEVATED','HIGH','CRITICAL'}: errors.append('EXECUTION-PROFILE invalid assurance profiles')
    if (ep.get('policy') or {}).get('work_size_and_assurance_are_independent') is not True: errors.append('EXECUTION-PROFILE must separate work size and assurance')
    wl=ep.get('worker_liveness') or {}
    if wl.get('static_wall_clock_timeout_is_stall_evidence') is not False: errors.append('EXECUTION-PROFILE must reject static wall-clock timeout as stall evidence')
    if wl.get('resume_from_checkpoint_instead_of_blind_restart') is not True: errors.append('EXECUTION-PROFILE must require checkpoint resume')
except Exception as e: errors.append(f'EXECUTION-PROFILE parse: {e}')
try:
    dm=yaml.safe_load((R/'planning/handoff/DELIVERY-MANIFEST.yaml').read_text(encoding='utf-8'))
    if 'planning/execution/EXECUTION-PROFILE.yaml' not in (dm.get('required_files') or []): errors.append('DELIVERY-MANIFEST must require EXECUTION-PROFILE')
except Exception as e: errors.append(f'DELIVERY-MANIFEST parse: {e}')

patterns=[r'\.agent/skills/',r'planning/execution/skills/',r'pi-subagents@\d',r'delivery_version:\s*[\'\"]?(?:4\.[0-9]+)',r'expected 60 canonical skills',r'\*\*60-skill\*\*']
exempt={'PACKAGE-MANIFEST.md','validate_system.py','CREDITS-AND-PROVENANCE.md','PROVENANCE.md','CHANGELOG-SYSTEM.md'}
for p in R.rglob('*'):
    if not p.is_file() or p.name in exempt or '.git' in p.parts or p.suffix.lower() not in {'.md','.yaml','.yml','.json','.py','.toml','.txt'}: continue
    try:t=p.read_text(encoding='utf-8')
    except: continue
    for pat in patterns:
        if re.search(pat,t): errors.append(f'{p.relative_to(R)}: stale pattern {pat}')

legacy_re=re.compile(r'(?i)\bV(?:4\.\d+|5\.[0-4])(?:\.\d+)?\b|(?<![0-9.])(?:4\.[0-9]+|5\.[0-4])(?:\.[0-9]+)?(?![0-9.])')
for p in R.rglob('*'):
    if not p.is_file() or '.git' in p.parts or p.name in {'PACKAGE-MANIFEST.md','validate_system.py','CHANGELOG-SYSTEM.md','CREDITS-AND-PROVENANCE.md','PROVENANCE.md'}: continue
    if p.suffix.lower() not in {'.md','.yaml','.yml','.json','.py','.toml','.txt','.sh'}: continue
    try:t=p.read_text(encoding='utf-8')
    except: continue
    if legacy_re.search(t): errors.append(f'{p.relative_to(R)}: legacy version remnant')


# V5.9.2 HIERARCHICAL_MODEL_ROUTING_GATE
try:
    mr=yaml.safe_load((R/'config/MODEL-ROUTING-POLICY.yaml').read_text(encoding='utf-8'))
    if str(mr.get('patch_release'))!='5.9.2': errors.append('MODEL-ROUTING-POLICY patch release mismatch')
    if (mr.get('roles') or {}).get('main_orchestrator',{}).get('class')!='FRONTIER': errors.append('main orchestrator must route FRONTIER')
    if (mr.get('roles') or {}).get('standard_implementation_worker',{}).get('class')!='EFFICIENT': errors.append('standard implementation worker must default EFFICIENT')
    om=mr.get('openai_mapping') or {}
    if (om.get('FRONTIER') or {}).get('model')!='gpt-5.6-sol': errors.append('OpenAI FRONTIER mapping must be gpt-5.6-sol')
    if (om.get('BALANCED') or {}).get('model')!='gpt-5.6-terra': errors.append('OpenAI BALANCED mapping must be gpt-5.6-terra')
    if (om.get('EFFICIENT') or {}).get('model')!='gpt-5.6-luna': errors.append('OpenAI EFFICIENT mapping must be gpt-5.6-luna')
    fr=om.get('FRONTIER') or {}
    if fr.get('reasoning_effort_ceiling')!='high': errors.append('Sol reasoning ceiling must be high')
    if not {'xhigh','max'}.issubset(set(fr.get('forbidden_efforts') or [])): errors.append('Sol xhigh/max must be explicitly forbidden')
    if (mr.get('review_independence') or {}).get('orchestrator_role')!='ADJUDICATE_INTEGRATE_REBRIEF': errors.append('main orchestrator must not satisfy independent review')
except Exception as e: errors.append(f'MODEL-ROUTING-POLICY parse: {e}')
for rel in ['docs/system/MODEL-ROUTING-AND-HIERARCHICAL-ORCHESTRATION.md','planning/execution/MODEL-ROUTING-STATE.yaml']:
    if not (R/rel).exists(): errors.append(f'missing V5.9.2 model-routing surface {rel}')
try:
    mrs=yaml.safe_load((R/'planning/execution/MODEL-ROUTING-STATE.yaml').read_text(encoding='utf-8'))
    if str(mrs.get('version'))!='5.9.2' or mrs.get('frontier_reasoning_effort_ceiling')!='high': errors.append('MODEL-ROUTING-STATE invalid baseline')
except Exception as e: errors.append(f'MODEL-ROUTING-STATE parse: {e}')

# V5.9 FULL_LIFECYCLE_ENTRY_GATE: GitHub Native must be standalone and must not require Custom GPT planning.
forbidden_prereq = re.compile(r'(?i)custom\s*-?gpt\s+(?:should|must|needs?\s+to)\s+(?:already\s+)?(?:have\s+)?completed')
for rel in ['AGENTS.md','GOAL.md','planning/execution/AUTOPILOT-GOAL.md','START-HERE.md']:
    t=(R/rel).read_text(encoding='utf-8')
    if forbidden_prereq.search(t): errors.append(f'{rel}: Custom GPT is still phrased as a prerequisite')
mode_doc=(R/'docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md').read_text(encoding='utf-8')
for mode in ['FULL_LIFECYCLE','RESUME_PLANNING','EXECUTION_HANDOFF','RESUME_EXECUTION']:
    if mode not in mode_doc: errors.append(f'full-lifecycle contract missing mode {mode}')
start=(R/'START-HERE.md').read_text(encoding='utf-8')
if 'Custom GPT is optional' not in start and 'Custom GPT remains an optional' not in start: errors.append('START-HERE must state Custom GPT is optional')
if 'FULL_LIFECYCLE' not in start: errors.append('START-HERE missing standalone full-lifecycle entry')
state_text=(R/'planning/execution/STATE.md').read_text(encoding='utf-8')
for required_state in ['Lifecycle Mode: AUTO_DETECT','Discovery Readiness: NOT_READY','run lifecycle mode detection','collaborative discovery']:
    if required_state not in state_text: errors.append(f'initial STATE missing standalone entry signal: {required_state}')
auto=(R/'planning/execution/AUTOPILOT-GOAL.md').read_text(encoding='utf-8')
for token in ['MODE_DETECTION','FULL_LIFECYCLE','RESUME_PLANNING','EXECUTION_HANDOFF','RESUME_EXECUTION','COLLABORATIVE_DISCOVERY']:
    if token not in auto: errors.append(f'AUTOPILOT-GOAL missing full-lifecycle token {token}')
# Template/initial-state parity: project initialization must preserve full-lifecycle semantics.
for rel, tokens in {
    'docs/templates/AUTOPILOT-GOAL.template.md':['MODE_DETECTION','FULL_LIFECYCLE','RESUME_PLANNING','EXECUTION_HANDOFF','RESUME_EXECUTION'],
    'docs/templates/STATE.template.md':['Lifecycle Mode: AUTO_DETECT','Discovery Readiness: NOT_READY','run lifecycle mode detection'],
    'delivery-template/planning/execution/AUTOPILOT-GOAL.md':['MODE_DETECTION','FULL_LIFECYCLE','RESUME_PLANNING','EXECUTION_HANDOFF','RESUME_EXECUTION'],
    'delivery-template/planning/execution/STATE.md':['Lifecycle Mode: AUTO_DETECT','Discovery Readiness: NOT_READY','run lifecycle mode detection'],
}.items():
    tt=(R/rel).read_text(encoding='utf-8')
    for tok in tokens:
        if tok not in tt: errors.append(f'{rel}: missing full-lifecycle template token {tok}')
# Complete release distribution, not a documentation-only snapshot.
for rel in ['.agents/skills/CATALOG.yaml','.claude/skills','.pi','.githooks','evals/skills/scenarios.yaml','docs/system/CAPABILITY-DRIVEN-TECHNOLOGY-SELECTION.md','config/TECHNOLOGY-CAPABILITY-CATALOG.yaml','config/TECHNOLOGY-SELECTION-POLICY.yaml','docs/system/CAPABILITY-RESOLUTION-AND-TOOL-BOOTSTRAP.md','config/TOOL-CAPABILITY-CATALOG.yaml','config/TOOL-SELECTION-POLICY.yaml','planning/architecture/TECHNOLOGY-EVALUATION.yaml','planning/execution/CAPABILITY-STATE.json','planning/execution/TOOL-LOCK.json','docs/system/COMMAND-CODE-FIRST-CLASS-PREVIEW.md','adapters/command-code/HARNESS-CAPABILITIES.yaml','scripts/detect_tool_capabilities.py','scripts/resolve_capability_provider.py','scripts/bootstrap_tool.py','scripts/verify_tool_capability.py','release-handoff/UPDATE-PUBLIC-GITHUB-REPO.md','README.md','config/SKILL-ESCALATION-POLICY.yaml','planning/execution/SKILL-REQUESTS.jsonl','planning/execution/SKILL-USAGE-EVENTS.jsonl','docs/system/RUNTIME-SKILL-ESCALATION.md','scripts/resolve_skill_request.py','config/SKILL-MAINTENANCE-POLICY.yaml','scripts/aggregate_skill_usage.py','docs/system/USAGE-AWARE-SKILL-MAINTENANCE.md','release/RELEASE-BASELINE.json','release/RELEASE-DELTA.json','release/RELEASE-CLAIMS.yaml','scripts/validate_release_claims.py']:
    if not (R/rel).exists(): errors.append(f'incomplete GitHub-native distribution: missing {rel}')

# INTERNATIONALIZATION_GATE: canonical shipped system text must remain English while conversation can adapt to the user.
german_chars=re.compile('[\\u00e4\\u00f6\\u00fc\\u00c4\\u00d6\\u00dc\\u00df]')
framework_roots=[R/'docs/system',R/'.agents/skills',R/'.claude/skills',R/'.pi',R/'config',R/'scripts']
framework_files=[R/'AGENTS.md',R/'CLAUDE.md',R/'START-HERE.md',R/'GOAL.md',R/'CODING-AGENT-HANDOFF.md']
scan_files=list(framework_files)
for base in framework_roots:
    if base.exists(): scan_files.extend(x for x in base.rglob('*') if x.is_file())
for p in scan_files:
    if p.suffix.lower() not in {'.md','.yaml','.yml','.json','.py','.toml','.txt','.sh'} and p.name not in {'pre-commit','pre-push'}: continue
    try: txt=p.read_text(encoding='utf-8')
    except: continue
    if german_chars.search(txt): errors.append(f'{p.relative_to(R)}: non-English character remnant in canonical framework text')
try:
    lang=(R/'docs/system/LANGUAGE-AND-INTERACTION.md').read_text(encoding='utf-8')
    if "Reply in the user's language by default" not in lang: errors.append('language contract missing adaptive conversation rule')
    if 'artifacts are English by default' not in lang: errors.append('language contract missing English artifact rule')
except Exception as e: errors.append(f'language contract read: {e}')


# V5.9 CLOSED_LOOP_AND_ZIP_HANDOFF_GATE
required_v57=[
'config/LOOP-CONTRACTS.yaml','config/SURFACE-POLICY.yaml','config/HARNESS-CONFORMANCE.yaml','config/CONTROL-VISIBILITY.yaml',
'planning/execution/LOOP-STATE.json','planning/execution/JOB-GRAPH.json','planning/execution/DECISION-LEDGER.jsonl',
'docs/system/LOOP-ARCHITECTURE.md','docs/system/JOB-GRAPH-AND-DECISION-LEDGER.md','docs/system/SURFACE-POLICY-AND-ENFORCEMENT.md',
'docs/system/ARTIFACT-CONSISTENCY-AND-REQUIREMENTS-QUALITY.md','docs/system/HARNESS-CONFORMANCE.md',
'docs/system/DEEPSEEK-HARNESS-FIRST-CLASS-PREVIEW.md','docs/system/MODEL-VISIBLE-RECONSTRUCTABILITY.md',
'docs/system/CONTROL-PACKAGE-IMPORT-AND-GIT-HYGIENE.md','scripts/ctrlaltdelegate_doctor.py','scripts/validate_control_plane.py',
'scripts/validate_control_package.py','scripts/import_delivery.py','scripts/planning_attest.py','scripts/progress_signature.py','.agents/skills/MECHANISM-REGISTRY.yaml','docs/templates/CONTROL-PACKAGE.template.json',
'docs/templates/TARGET-GITIGNORE.fragment','docs/templates/NESTED-CODING-AGENT-HANDOFF.template.md','docs/templates/CONTROL-AGENTS.template.md','docs/templates/CONTROL-CLAUDE.template.md','docs/templates/JOB-GRAPH.template.json','docs/templates/LOOP-STATE.template.json','docs/templates/PLANNING-BASELINE.template.json','docs/templates/WORKER-CONTRACT.template.yaml','docs/templates/CHANGE.template.yaml','planning/execution/PLANNING-BASELINE.json','planning/execution/PENDING-INPUT.jsonl','planning/execution/LEARNING-CANDIDATES.jsonl','planning/execution/ARTIFACT-CONSISTENCY.json','docs/system/PLANNING-BASELINE-ATTESTATION.md','docs/system/CHANGE-CONTROL-AND-RETROSPECTIVE.md','docs/system/WORKER-CONTRACTS-AND-MIDRUN-INPUT.md']
for rel in required_v57:
    if not (R/rel).exists(): errors.append(f'missing V5.9 control surface {rel}')
loop=(R/'config/LOOP-CONTRACTS.yaml').read_text(encoding='utf-8')
for tok in ['REPAIR_LOOP','WORKER_LIVENESS_LOOP','CONVERGENCE_LOOP','no_progress_action']:
    if tok not in loop: errors.append(f'loop registry missing {tok}')
surface=(R/'config/SURFACE-POLICY.yaml').read_text(encoding='utf-8')
for tok in ['LOCKED','EDITABLE','APPEND_ONLY','HUMAN_CONTROLLED','instructions_are_not_enforcement']:
    if tok not in surface: errors.append(f'surface policy missing {tok}')
harness=(R/'config/HARNESS-CONFORMANCE.yaml').read_text(encoding='utf-8')
for tok in ['deepseek-harness','command-code','FIRST_CLASS_PREVIEW','.agents/skills','duplicate_dsh_skill_copy: false','CAPABILITY_CLASS_ADAPTIVE','imported_control_skills']:
    if tok not in harness: errors.append(f'harness conformance missing {tok}')
start_tpl=(R/'docs/templates/NESTED-CODING-AGENT-START-PROMPT.template.md').read_text(encoding='utf-8')
for token in ['ctrlaltdelegate-delivery.zip','./.ctrlaltdelegate','/.ctrlaltdelegate/','LOCAL_PRIVATE','BLOCKED_DELIVERY_INCOMPLETE','ZIP members']:
    if token not in start_tpl: errors.append(f'V5.9 ZIP start prompt template missing {token}')
if './ctrlaltdelegate/' in start_tpl: errors.append('V5.9 ZIP start prompt still references legacy visible control root')
delivery_doc=(R/'docs/system/DETERMINISTIC-PLANNING-DELIVERY-AND-HANDOFF.md').read_text(encoding='utf-8')
for token in ['ctrlaltdelegate-delivery.zip','.ctrlaltdelegate/','ZIP contains exactly one top-level directory','LOCAL_PRIVATE','atomically promote']:
    if token not in delivery_doc: errors.append(f'V5.9 deterministic delivery contract missing {token}')
gitignore=(R/'.gitignore').read_text(encoding='utf-8')
for token in ['/ctrlaltdelegate-delivery.zip','/.ctrlaltdelegate/','/.ctrlaltdelegate.importing-*/','/.ctrlaltdelegate.incoming-*/']:
    if token not in gitignore: errors.append(f'root .gitignore missing V5.9 control hygiene {token}')
try:
    js=json.loads((R/'planning/execution/JOB-GRAPH.json').read_text(encoding='utf-8'))
    if str(js.get('version'))!='5.9' or not isinstance(js.get('jobs'),list): errors.append('JOB-GRAPH invalid baseline')
    ls=json.loads((R/'planning/execution/LOOP-STATE.json').read_text(encoding='utf-8'))
    if str(ls.get('version'))!='5.9' or 'progress_delta' not in ls: errors.append('LOOP-STATE invalid baseline')
except Exception as e: errors.append(f'V5.9 control JSON parse: {e}')

# V5.9 SKILL_DRIVEN_PLANNING_GATE
required_v571=[
'docs/system/SKILL-DRIVEN-PLANNING.md','docs/system/DOMAIN-PLANNING-PROFILES.md','docs/system/WEB-PRODUCT-PLANNING-AND-CONTENT.md',
'config/PLANNING-SKILL-ROUTING.yaml','planning/context/PLANNING-SKILL-STATE.yaml',
'planning/design/DESIGN-DIRECTION.yaml','planning/design/DESIGN-SYSTEM.md','planning/design/UX-PRINCIPLES.md',
'planning/content/CONTENT-STRATEGY.md','planning/content/VOICE-GUIDE.md','planning/content/CONTENT-MANIFEST.yaml','planning/content/pages/README.md',
'planning/seo/SEO-STRATEGY.md','planning/seo/SEARCH-INTENT-MAP.yaml','planning/seo/SEO-ROUTE-MATRIX.yaml','planning/seo/STRUCTURED-DATA-PLAN.yaml','planning/seo/SEO-VERIFICATION-PLAN.md']
for rel in required_v571:
    if not (R/rel).exists(): errors.append(f'missing V5.9 planning surface {rel}')
try:
    preg=yaml.safe_load((R/'config/PLANNING-SKILL-ROUTING.yaml').read_text(encoding='utf-8')) or {}
    pskills=preg.get('skills') or {}
    if str(preg.get('version'))!='5.9': errors.append('planning skill registry version mismatch')
    if set(pskills)!=set(skills): errors.append('planning skill registry must cover every canonical skill exactly')
    for sid,meta in pskills.items():
        if not meta.get('phases') or not meta.get('roles'): errors.append(f'{sid}: incomplete planning capability metadata')
        if meta.get('execution_handoff')!='WHEN_JOB_RELEVANT': errors.append(f'{sid}: invalid planning-to-execution handoff policy')
except Exception as e: errors.append(f'planning skill registry parse: {e}')
for sid in ['seo-strategy','technical-seo-engineering','seo-content-strategy','structured-data-seo','search-experience-optimization','seo-audit-and-drift','local-commerce-seo','data-visualization-design','natural-content-editing']:
    if sid not in skills: errors.append(f'missing V5.9 specialist {sid}')
for rel in ['AGENTS.md','GOAL.md','START-HERE.md','planning/execution/AUTOPILOT-GOAL.md']:
    txt=(R/rel).read_text(encoding='utf-8')
    if 'V5.9 skill-driven planning' not in txt: errors.append(f'{rel}: missing skill-driven planning rule')


try:
    jgt=json.loads((R/'docs/templates/JOB-GRAPH.template.json').read_text(encoding='utf-8'))
    if str(jgt.get('version'))!='5.9': errors.append('JOB-GRAPH template version mismatch')
    dp=jgt.get('dependency_policy') or {}
    if 'IMPLEMENTED_UNVERIFIED' not in (dp.get('implementation_satisfied_by') or []): errors.append('JOB-GRAPH template lacks implementation-unverified dependency semantics')
except Exception as ex: errors.append(f'JOB-GRAPH template parse: {ex}')

# V5.9 PRODUCT_RUNTIME_COMPLETION_GATE
for rel in ['config/BLOCKER-POLICY.yaml','config/PRODUCT-COMPLETION-POLICY.yaml','planning/product/PRODUCT-CONTRACT.yaml','planning/acceptance/USER-JOURNEY-ORACLES.yaml','planning/execution/BLOCKERS.json','planning/execution/DEFERRED-VALIDATION.json','planning/execution/PROVIDER-ATTESTATIONS.json','planning/execution/PRODUCT-RUNTIME-PREFLIGHT.json','planning/execution/PRODUCT-DRIFT-REVIEW.json','planning/execution/EXECUTION-SNAPSHOT.json','scripts/transition_job.py','scripts/build_execution_snapshot.py','scripts/refresh_job_readiness.py','scripts/validate_product_completion.py','scripts/record_loop_attempt.py','config/SKILL-OPTIMIZATION-POLICY.yaml','docs/system/SKILLOPT-OFFLINE-SKILL-LAB.md']:
    if not (R/rel).exists(): errors.append(f'missing V5.9 completion surface {rel}')
bp=(R/'config/BLOCKER-POLICY.yaml').read_text(encoding='utf-8')
for tok in ['EXECUTION_BLOCKER','VERIFICATION_BLOCKER','verification_blocker_never_global_stop']:
    if tok not in bp: errors.append(f'blocker policy missing {tok}')
pc=(R/'config/PRODUCT-COMPLETION-POLICY.yaml').read_text(encoding='utf-8')
for tok in ['USER_JOURNEY_REAL','CONSUMER_VERIFIED','VALIDATION_PENDING_EXTERNAL','direct_manual_done_edit','IMPLEMENTED_UNVERIFIED','verification_blocker_does_not_block_implementation_dependencies']:
    if tok not in pc: errors.append(f'completion policy missing {tok}')

if errors:
    print('SYSTEM_QA_FAIL')
    for e in errors: print('-',e)
    sys.exit(2)
print(f'SYSTEM_QA_PASS skills={len(skills)} claude_adapters={len(wrappers)} progressive_refs={actual_ref_count} empty_decisions=0')
