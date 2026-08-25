#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys
root=Path(__file__).resolve().parents[1]
required=['README.md','AGENTS.md','CHANGELOG-V5.9.1.md','RELEASE-METADATA.json','release-handoff/UPDATE-PUBLIC-GITHUB-REPO.md']
errs=[f'missing {p}' for p in required if not (root/p).exists()]
if (root/'RELEASE-METADATA.json').exists():
    import json
    m=json.loads((root/'RELEASE-METADATA.json').read_text())
    if m.get('version') not in {'5.9.1','5.9.2'}: errs.append('metadata version mismatch')
if len(list((root/'.agents/skills').glob('*/SKILL.md')))!=154: errs.append('skill count mismatch')
if errs:
 print('RELEASE CLAIMS FAILED'); [print('-',e) for e in errs]; sys.exit(1)
print('V5.9.1 CONTROL SURFACES OK')
