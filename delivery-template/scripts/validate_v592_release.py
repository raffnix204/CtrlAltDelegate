#!/usr/bin/env python3
from pathlib import Path
import json, sys
R=Path(__file__).resolve().parents[1]
required=['README.md','AGENTS.md','CHANGELOG-V5.9.2.md','RELEASE-METADATA.json','release-handoff/UPDATE-PUBLIC-GITHUB-REPO.md','config/MODEL-ROUTING-POLICY.yaml']
e=[f'missing {p}' for p in required if not (R/p).exists()]
if (R/'RELEASE-METADATA.json').exists():
 m=json.loads((R/'RELEASE-METADATA.json').read_text());
 if m.get('version')!='5.9.2': e.append('metadata version mismatch')
if len(list((R/'.agents/skills').glob('*/SKILL.md')))!=154: e.append('skill count mismatch')
if len(list((R/'.claude/skills').glob('*/SKILL.md')))!=154: e.append('claude adapter count mismatch')
if e:
 print('RELEASE CLAIMS FAILED'); [print('-',x) for x in e]; sys.exit(1)
print('RELEASE CLAIMS OK: 5.9.2')
