#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

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
if catalog.get('version')!='5.6.4': errors.append('catalog version mismatch')
if catalog.get('library')!='software-planning-lead-v5.6.4': errors.append('catalog library mismatch')
if (catalog.get('policy') or {}).get('skill_schema')!='5.6.1-domain-expertise': errors.append('catalog skill_schema mismatch')
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
'planning/execution/SKILLS-MANIFEST.yaml','planning/architecture/STACK-MANIFEST.yaml','planning/research/RESEARCH-POLICY.yaml','planning/research/RESEARCH-REGISTER.md','planning/execution/DOCUMENTATION-STATE.yaml','planning/execution/DOCUMENTATION-COVERAGE.md','planning/execution/CONTEXT-STATE.yaml','planning/execution/PARALLELISM-STATE.yaml','planning/execution/EXECUTION-PROFILE.yaml','delivery-template/planning/execution/EXECUTION-PROFILE.yaml','config/DOCUMENTATION-RULES.yaml','docs/system/DOCUMENTATION-LIFECYCLE.md','docs/system/CONTEXT-AND-PARALLELISM.md','docs/system/CAPABILITY-BOOTSTRAP.md','.githooks/pre-commit','.githooks/pre-push','scripts/docs_freshness_gate.py','scripts/install_git_guards.py','config/STACK-SIGNALS.yaml','config/SKILL-ROUTING-RULES.yaml','planning/execution/CONVERGENCE-MATRIX.json','planning/execution/EVIDENCE-INDEX.json','planning/repository/REPO-CONTEXT-MAP.md','docs/system/QUALITY-EFFICIENCY-HARDENING.md','docs/system/CONVERGENCE-AND-EVIDENCE.md','docs/system/SKILL-EVALUATION.md','docs/system/SKILL-EXECUTION-CONTRACT.md','docs/system/SKILL-SCHEMA-V5.6.1.md','docs/system/SKILL-LIBRARY-QUALITY-AUDIT-V5.6.1.md','.agents/skills/SOURCE-RESEARCH-MATRIX.yaml','docs/system/CODEX-FIRST-CLASS-HARNESS.md','docs/system/GITHUB-DIRECT-HANDOFF.md','docs/system/PROGRAM-DESIGN-AND-VERTICAL-SLICES.md','docs/system/REPOSITORY-LAYOUT-AND-STATE.md','docs/system/COLLABORATIVE-DISCOVERY-AND-CONSTRAINTS.md','docs/system/ADAPTIVE-EXECUTION-AND-WORKER-LIVENESS.md','docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md','docs/system/LANGUAGE-AND-INTERACTION.md','docs/system/DETERMINISTIC-PLANNING-DELIVERY-AND-HANDOFF.md','docs/templates/NESTED-CODING-AGENT-START-PROMPT.template.md','docs/templates/NESTED-DELIVERY-MANIFEST.template.yaml','docs/templates/HANDOFF-STATUS.template.yaml','scripts/validate_handoff_delivery.py','planning/discovery/TECHNICAL-PREFERENCES.yaml','planning/discovery/DISCOVERY-STATE.md','planning/architecture/PROGRAM-DESIGN.md','planning/context/PROJECT-CONTEXT.md','planning/handoff/START-HERE.md','planning/handoff/CODING-AGENT-HANDOFF.md','planning/handoff/FINAL-START-PROMPT.md','planning/handoff/DELIVERY-MANIFEST.yaml','scripts/quality_gate.py','scripts/worker_checkpoint.py','scripts/validate_skill_evals.py','evals/skills/scenarios.yaml']
for x in required:
    if not (R/x).exists(): errors.append(f'missing {x}')

for path,key in [('planning/execution/SKILLS-MANIFEST.yaml','library_count')]:
    try:
        d=yaml.safe_load((R/path).read_text(encoding='utf-8'))
        if d.get('version')!='5.6.4': errors.append(f'{path} version mismatch')
        if key and d.get(key)!=len(skills): errors.append(f'{path} {key} mismatch')
    except Exception as e: errors.append(f'{path} parse: {e}')
try:
    pref=yaml.safe_load((R/'planning/discovery/TECHNICAL-PREFERENCES.yaml').read_text(encoding='utf-8'))
    if pref.get('version')!='5.6.4': errors.append('TECHNICAL-PREFERENCES version mismatch')
    if pref.get('decision_style') not in {'AUTO','AUTOPILOT','COLLABORATIVE','DIRECTED'}: errors.append('TECHNICAL-PREFERENCES invalid decision_style')
    required_items={'technology','runtime_hosting','data_security_region','existing_environment'}
    if not required_items.issubset(set((pref.get('items') or {}).keys())): errors.append('TECHNICAL-PREFERENCES missing required item groups')
    for key,val in (pref.get('items') or {}).items():
        if isinstance(val,dict) and val.get('strength') not in {'REQUIRED','PREFERRED','AUTO'}: errors.append(f'TECHNICAL-PREFERENCES invalid strength for {key}')
except Exception as e: errors.append(f'TECHNICAL-PREFERENCES parse: {e}')
try:
    ep=yaml.safe_load((R/'planning/execution/EXECUTION-PROFILE.yaml').read_text(encoding='utf-8'))
    if ep.get('version')!='5.6.4': errors.append('EXECUTION-PROFILE version mismatch')
    if ep.get('profile') not in {'AUTO','MICRO','SMALL','STANDARD','HIGH_RISK'}: errors.append('EXECUTION-PROFILE invalid profile')
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
    if re.search(r'(?i)capability-class model routing|model_routing:\s*true',t): errors.append(f'{p.relative_to(R)}: prohibited model-routing policy')


# V5.6.4 FULL_LIFECYCLE_ENTRY_GATE: GitHub Native must be standalone and must not require Custom GPT planning.
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
for rel in ['.agents/skills/CATALOG.yaml','.claude/skills','.pi','.githooks','evals/skills/scenarios.yaml']:
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


# V5.6.4 DETERMINISTIC_HANDOFF_DELIVERY_GATE
delivery_doc=(R/'docs/system/DETERMINISTIC-PLANNING-DELIVERY-AND-HANDOFF.md').read_text(encoding='utf-8')
for token in ['ctrlaltdelegate-delivery.zip','ctrlaltdelegate/','CODING-AGENT-START-PROMPT.md','HANDOFF-STATUS.yaml','BLOCKED_DELIVERY_INCOMPLETE','PROJECT_ROOT','CONTROL_ROOT']:
    if token not in delivery_doc: errors.append(f'deterministic delivery contract missing {token}')
start_tpl=(R/'docs/templates/NESTED-CODING-AGENT-START-PROMPT.template.md').read_text(encoding='utf-8')
for token in ['./ctrlaltdelegate/AGENTS.md','./ctrlaltdelegate/planning/handoff/HANDOFF-STATUS.yaml','./ctrlaltdelegate/planning/handoff/CODING-AGENT-HANDOFF.md','./ctrlaltdelegate/planning/execution/STATE.md','BLOCKED_DELIVERY_INCOMPLETE']:
    if token not in start_tpl: errors.append(f'nested start prompt template missing {token}')
if '<project-slug>-coding-agent-delivery' in start_tpl: errors.append('nested start prompt template uses project-derived legacy directory')
manifest_tpl=(R/'docs/templates/NESTED-DELIVERY-MANIFEST.template.yaml').read_text(encoding='utf-8')
for token in ['planning/PROJECT.md','planning/REQUIREMENTS.md','docs/system/DETERMINISTIC-PLANNING-DELIVERY-AND-HANDOFF.md','docs/system/SKILL-EXECUTION-CONTRACT.md','docs/system/LANGUAGE-AND-INTERACTION.md','docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md','scripts/validate_handoff_delivery.py']:
    if token not in manifest_tpl: errors.append(f'nested delivery manifest template missing required file {token}')
status_tpl=(R/'docs/templates/HANDOFF-STATUS.template.yaml').read_text(encoding='utf-8')
for token in ['required_paths_present','prompt_paths_verified','planning_ready','zero_blocking_decisions','control_tree_verified_before_archive']:
    if token not in status_tpl: errors.append(f'handoff status template missing closure check {token}')
if 'package_reopened_and_verified' in status_tpl: errors.append('handoff status template contains self-referential final-archive verification claim')
validator=(R/'scripts/validate_handoff_delivery.py').read_text(encoding='utf-8')
for token in ['READY handoff has incomplete closure checks','CODING-AGENT-START-PROMPT.md and planning/handoff/FINAL-START-PROMPT.md must be byte-identical','manifest required_files missing']:
    if token not in validator: errors.append(f'handoff delivery validator missing enforcement: {token}')

if errors:
    print('SYSTEM_QA_FAIL')
    for e in errors: print('-',e)
    sys.exit(2)
print(f'SYSTEM_QA_PASS skills={len(skills)} claude_adapters={len(wrappers)} progressive_refs={actual_ref_count} empty_decisions=0')
