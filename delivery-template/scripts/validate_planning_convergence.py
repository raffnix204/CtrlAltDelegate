#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,sys,yaml
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
P='planning/execution/PLANNING-CONVERGENCE.json'
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--blockers',type=int,default=0); ap.add_argument('--warnings',type=int,default=0); ap.add_argument('--uncovered-requirements',type=int,default=0); ap.add_argument('--unresolved-decisions',type=int,default=0); ap.add_argument('--unresolved-assumptions',type=int,default=0); ap.add_argument('--missing-runtime-prerequisites',type=int,default=0); ap.add_argument('--strategy',required=True); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
 dims={'blocker_count':a.blockers,'warning_count':a.warnings,'uncovered_requirements':a.uncovered_requirements,'unresolved_decisions':a.unresolved_decisions,'unresolved_assumptions':a.unresolved_assumptions,'missing_runtime_prerequisites':a.missing_runtime_prerequisites}; sig=hashlib.sha256(json.dumps(dims,sort_keys=True).encode()).hexdigest(); d=cs.load_json(P); prev=d.get('signature'); plateau=int(d.get('plateau_count') or 0)+1 if prev==sig else 0
 pol=yaml.safe_load((R/'config/PLANNING-CONVERGENCE-POLICY.yaml').read_text()) or {}; limit=int(pol.get('plateau',{}).get('same_signature_limit',2)); status='READY' if not any(dims.values()) else 'PLATEAU' if plateau>=limit else 'IMPROVING_OR_UNRESOLVED'
 if status=='PLATEAU' and d.get('strategy')==a.strategy:
  print('PLANNING_CONVERGENCE_FAIL_STRATEGY_CHANGE_REQUIRED'); return 2
 if a.write:
  ts=datetime.datetime.now(datetime.timezone.utc).isoformat(); d.update({'version':'5.9','iteration':int(d.get('iteration') or 0)+1,'previous_signature':prev,'signature':sig,'plateau_count':plateau,'dimensions':dims,'strategy':a.strategy,'status':status,'updated_at':ts}); cs.atomic_json(P,d); cs.seal('PLANNING_CONVERGENCE_UPDATE',actor='planner',paths=[],event={'type':'PLANNING_CONVERGENCE','status':status,'signature':sig})
 print(json.dumps({'status':status,'signature':sig,'plateau_count':plateau,'dimensions':dims},indent=2)); return 0 if status!='PLATEAU' else 3
if __name__=='__main__': raise SystemExit(main())
