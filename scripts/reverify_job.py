#!/usr/bin/env python3
import argparse, subprocess, sys
ap=argparse.ArgumentParser(); ap.add_argument('ledger'); ap.add_argument('--baseline',required=True); ap.add_argument('--candidate',required=True); ap.add_argument('--cwd',default='.'); a=ap.parse_args()
if not a.baseline.strip() or not a.candidate.strip(): sys.exit('explicit baseline/candidate required')
print(f'REVIEW_TARGET {a.baseline}..{a.candidate}')
r=subprocess.run([sys.executable,'scripts/check_execution_gates.py',a.ledger,'--cwd',a.cwd])
sys.exit(r.returncode)
