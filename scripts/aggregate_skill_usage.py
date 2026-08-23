#!/usr/bin/env python3
from pathlib import Path
import argparse, json, yaml, zipfile, tempfile, shutil
R=Path(__file__).resolve().parents[1]
def events_from_root(root):
    p=root/'planning/execution/SKILL-USAGE-EVENTS.jsonl'; out=[]
    if p.exists():
        for line in p.read_text(encoding='utf-8').splitlines():
            try:
                if line.strip(): out.append(json.loads(line))
            except: pass
    # Older exports still provide useful selection evidence.
    sm=root/'planning/execution/SKILLS-MANIFEST.yaml'
    if sm.exists():
        try:
            d=yaml.safe_load(sm.read_text(encoding='utf-8')) or {}
            for sid in d.get('project_selected') or []: out.append({'skill_id':sid,'event':'EXECUTION_SELECTED'})
        except: pass
    ps=root/'planning/context/PLANNING-SKILL-STATE.yaml'
    if ps.exists():
        try:
            d=yaml.safe_load(ps.read_text(encoding='utf-8')) or {}
            for item in d.get('consulted') or []:
                if isinstance(item,dict) and item.get('skill_id'): out.append({'skill_id':item['skill_id'],'event':'PLANNING_CONSULTED'})
        except: pass
    return out
def find_roots(base):
    roots=[]
    if (base/'planning').exists(): roots.append(base)
    roots += [p for p in base.rglob('*') if p.is_dir() and (p/'planning/execution').exists()]
    seen=[]
    for r in roots:
        if r not in seen: seen.append(r)
    return seen
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('inputs',nargs='+'); ap.add_argument('--output',default='maintenance/SKILL-USAGE-SUMMARY.json'); ap.add_argument('--state',default='maintenance/SKILL-MAINTENANCE-STATE.yaml'); ap.add_argument('--root',default=None)
    a=ap.parse_args(); root=Path(a.root).resolve() if a.root else R; pol=yaml.safe_load((root/'config/SKILL-MAINTENANCE-POLICY.yaml').read_text())
    weights=pol['weights']; counts={}; sources=[]; temps=[]
    try:
        for raw in a.inputs:
            p=Path(raw).resolve(); base=p
            if p.suffix.lower()=='.zip':
                td=Path(tempfile.mkdtemp(prefix='cad-usage-')); temps.append(td)
                with zipfile.ZipFile(p) as z:z.extractall(td)
                base=td
            for rr in find_roots(base):
                ev=events_from_root(rr)
                if ev: sources.append(str(p));
                for x in ev:
                    sid=x.get('skill_id'); typ=x.get('event');
                    if not sid or typ not in weights: continue
                    d=counts.setdefault(sid,{'events':{},'weighted_score':0})
                    d['events'][typ]=d['events'].get(typ,0)+1; d['weighted_score']+=weights[typ]
        p0=set(pol['dimensions']['criticality_overrides']['P0_CORE_SAFETY'])
        hot=pol['usage_tiers']['HOT']['min_weighted_events']; warm=pol['usage_tiers']['WARM']['min_weighted_events']
        all_skills=sorted(p.parent.name for p in (root/'.agents/skills').glob('*/SKILL.md'))
        for sid in all_skills: counts.setdefault(sid,{'events':{},'weighted_score':0})
        state={'version':'5.8.2','skills':{}}
        for sid,d in sorted(counts.items()):
            score=d['weighted_score']; tier='HOT' if score>=hot else ('WARM' if score>=warm else 'COLD')
            priority='P0' if sid in p0 else ('P1' if tier=='HOT' else ('P2' if tier=='WARM' else 'P3'))
            state['skills'][sid]={**d,'usage_tier':tier,'maintenance_priority':priority}
        out={'version':'5.8.2','sources':sorted(set(sources)),'skills':state['skills']}
        (root/a.output).parent.mkdir(parents=True,exist_ok=True); (root/a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
        (root/a.state).write_text(yaml.safe_dump(state,sort_keys=False))
        print(f'SKILL_USAGE_AGGREGATION_PASS skills={len(state["skills"])} sources={len(set(sources))}')
    finally:
        for td in temps: shutil.rmtree(td,ignore_errors=True)
if __name__=='__main__': main()
