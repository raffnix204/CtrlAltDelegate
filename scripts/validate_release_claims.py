#!/usr/bin/env python3
from pathlib import Path
import argparse, json, subprocess, yaml, sys, re
R=Path(__file__).resolve().parents[1]
def skill_ids_from_tree(ref=None):
    if ref:
        cp=subprocess.run(['git','ls-tree','-r','--name-only',ref,'--','.agents/skills'],cwd=R,text=True,capture_output=True)
        if cp.returncode: raise RuntimeError(cp.stderr.strip())
        paths=cp.stdout.splitlines()
    else: paths=[str(p.relative_to(R)).replace('\\','/') for p in (R/'.agents/skills').glob('*/SKILL.md')]
    return sorted({p.split('/')[2] for p in paths if p.startswith('.agents/skills/') and p.endswith('/SKILL.md') and len(p.split('/'))>=4})
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--git',action='store_true'); a=ap.parse_args(); err=[]
    base=json.loads((R/'release/RELEASE-BASELINE.json').read_text()); claims=yaml.safe_load((R/'release/RELEASE-CLAIMS.yaml').read_text()) or {}; delta=json.loads((R/'release/RELEASE-DELTA.json').read_text())
    current=skill_ids_from_tree(); before_count=delta.get('skill_count_before'); after_count=delta.get('skill_count_after'); added=set(delta.get('skills_added') or [])
    if len(current)!=after_count: err.append(f'current skill count {len(current)} != release delta {after_count}')
    for c in claims.get('claims') or []:
        typ=c.get('type')
        if typ=='SKILL_COUNT' and (c.get('before')!=before_count or c.get('after')!=after_count): err.append(f'claim {c.get("id")} contradicts delta')
        if typ=='ADDED_SKILLS' and set(c.get('skills') or [])!=added: err.append(f'claim {c.get("id")} added skills contradict delta: claim={c.get("skills")} delta={sorted(added)}')
        if typ=='ADDED_PATHS':
            for p in c.get('paths') or []:
                if p not in set(delta.get('files_added') or []): err.append(f'claim {c.get("id")} says added path but delta does not: {p}')
    release_version=str(claims.get('version'))
    changelog=R/f'CHANGELOG-V{release_version}.md'
    if not changelog.is_file(): err.append(f'missing release changelog {changelog.name}')
    else:
        ct=changelog.read_text(encoding='utf-8')
        if '<!-- VERIFIED-RELEASE-CLAIMS: release/RELEASE-CLAIMS.yaml -->' not in ct: err.append('release changelog missing verified-claims marker')
        expected=f'Canonical skills: **{before_count} -> {after_count}**.'
        if expected not in ct: err.append('release changelog skill-count fact contradicts/misses structured claim')
        if not added and 'Added canonical skills: **none**.' not in ct: err.append('release changelog must state no added canonical skills')
    audit=(R/'docs/system/SKILL-COVERAGE-AUDIT.md')
    if audit.exists():
        at=audit.read_text(encoding='utf-8')
        cur='V'+release_version
        bad=re.search(rf'(?i){re.escape(cur)}[^\n]{{0,180}}adds?\s+(?:\*\*)?\d+[^\n]{{0,100}}skills?',at)
        if bad and not added: err.append('skill coverage audit claims current-release skill additions contradicted by delta')
    if a.git or (R/'.git').exists():
        b=base['base_git_sha']; cp=subprocess.run(['git','diff','--name-status',b+'..HEAD'],cwd=R,text=True,capture_output=True)
        if cp.returncode: err.append('git diff failed: '+cp.stderr.strip())
        else:
            statuses={line.split('\t',1)[1]:line.split('\t',1)[0] for line in cp.stdout.splitlines() if '\t' in line}
            for p in delta.get('files_added') or []:
                if p.startswith('release/'): continue
                if statuses.get(p)!='A': err.append(f'Git diff added-path mismatch {p}: {statuses.get(p)}')
            try:
                base_skills=skill_ids_from_tree(b); head_skills=skill_ids_from_tree('HEAD')
                if sorted(set(head_skills)-set(base_skills))!=sorted(delta.get('skills_added') or []): err.append('Git diff skill additions contradict release delta')
                if len(base_skills)!=before_count or len(head_skills)!=after_count: err.append('Git skill counts contradict release delta')
            except Exception as ex: err.append(str(ex))
    if err:
        print('RELEASE_CLAIMS_QA_FAIL'); [print('-',x) for x in err]; return 2
    print(f'RELEASE_CLAIMS_QA_PASS skills={before_count}->{after_count} added_skills={len(added)}')
    return 0
if __name__=='__main__': raise SystemExit(main())
