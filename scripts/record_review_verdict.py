#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,sys
R=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(R/'scripts')); import control_state as cs
P='planning/execution/REVIEW-VERDICTS.json'
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--requirement',required=True); ap.add_argument('--candidate-sha',required=True); ap.add_argument('--oracle',required=True); ap.add_argument('--verifier-profile',required=True); ap.add_argument('--verdict',choices=['PASS','FAIL','UNVERIFIABLE'],required=True); ap.add_argument('--evidence',action='append',default=[]); ap.add_argument('--followup'); a=ap.parse_args()
 if a.verdict=='UNVERIFIABLE' and not a.followup: print('VERDICT_DENIED_UNVERIFIABLE_REQUIRES_FOLLOWUP'); return 2
 identity={'requirement_id':a.requirement,'candidate_sha':a.candidate_sha,'oracle_id':a.oracle,'verifier_profile':a.verifier_profile}; vid=hashlib.sha256(json.dumps(identity,sort_keys=True).encode()).hexdigest(); ts=datetime.datetime.now(datetime.timezone.utc).isoformat(); d=cs.load_json(P); row={'verdict_id':vid,**identity,'verdict':a.verdict,'evidence_ids':a.evidence,'followup':a.followup,'at':ts}; d['verdicts']=[x for x in d.get('verdicts',[]) if x.get('verdict_id')!=vid]+[row]; d['updated_at']=ts; cs.atomic_json(P,d); cs.seal('RECORD_REVIEW_VERDICT',actor='verifier',paths=[P],event={'type':'REVIEW_VERDICT','verdict_id':vid,'verdict':a.verdict,'requirement_id':a.requirement}); print(json.dumps(row,indent=2)); return 0 if a.verdict=='PASS' else 3 if a.verdict=='UNVERIFIABLE' else 2
if __name__=='__main__': raise SystemExit(main())
