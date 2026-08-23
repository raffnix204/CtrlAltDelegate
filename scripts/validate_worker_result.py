#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys
R=Path(__file__).resolve().parents[1]
try:
 import jsonschema
except Exception:
 jsonschema=None
REQUIRED=['schema_version','job_id','attempt_id','worker_id','brief_sha256','base_sha','outcome','implementation_status','verification_status','skills_applied','changed_paths','evidence_ids','blockers','concerns']

def validate(d):
 errs=[]
 for k in REQUIRED:
  if k not in d: errs.append('missing '+k)
 if d.get('schema_version')!='5.9': errs.append('schema_version must be 5.9')
 if d.get('outcome') not in {'IMPLEMENTED','NEEDS_VERIFICATION','BLOCKED','FAILED','CANCELLED'}: errs.append('invalid outcome')
 if d.get('implementation_status') not in {'COMPLETE','PARTIAL','NOT_STARTED'}: errs.append('invalid implementation_status')
 if d.get('verification_status') not in {'PASS','PENDING','PENDING_EXTERNAL','FAIL','NOT_APPLICABLE'}: errs.append('invalid verification_status')
 for k in ['skills_applied','changed_paths','evidence_ids','blockers','concerns']:
  if not isinstance(d.get(k),list): errs.append(k+' must be list')
 if jsonschema:
  try: jsonschema.validate(d,json.loads((R/'docs/schemas/WORKER-RESULT.schema.json').read_text()))
  except Exception as e: errs.append('schema: '+str(e).splitlines()[0])
 return errs

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('file'); a=ap.parse_args()
 try:d=json.loads(Path(a.file).read_text(encoding='utf-8'))
 except Exception as e: print('WORKER_RESULT_QA_FAIL',e); return 2
 errs=validate(d)
 if errs:
  print('WORKER_RESULT_QA_FAIL'); [print('-',x) for x in errs]; return 2
 print('WORKER_RESULT_QA_PASS job='+d['job_id']+' attempt='+d['attempt_id']); return 0
if __name__=='__main__': raise SystemExit(main())
