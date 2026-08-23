#!/usr/bin/env python3
from pathlib import Path
import argparse,json,shutil,socket,subprocess
R=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='kind',required=True)
 p=sub.add_parser('path'); p.add_argument('value')
 p=sub.add_parser('command'); p.add_argument('value')
 p=sub.add_parser('port'); p.add_argument('value',type=int)
 a=ap.parse_args(); out={'kind':a.kind,'value':a.value}
 if a.kind=='path':
  x=(R/a.value) if not Path(a.value).is_absolute() else Path(a.value); out['status']='exists' if x.exists() else 'missing'; out['resolved']=str(x)
 elif a.kind=='command': out['status']='available' if shutil.which(a.value) else 'missing'; out['resolved']=shutil.which(a.value)
 else:
  s=socket.socket(); s.settimeout(.2)
  try:s.bind(('127.0.0.1',a.value)); out['status']='free'
  except OSError: out['status']='in_use'
  finally:s.close()
 print(json.dumps(out,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
