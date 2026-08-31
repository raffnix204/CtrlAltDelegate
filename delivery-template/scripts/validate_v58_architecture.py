#!/usr/bin/env python3
from pathlib import Path
import yaml, json, sys, hashlib
R=Path(__file__).resolve().parents[1]; e=[]
def y(rel):
    try:return yaml.safe_load((R/rel).read_text()) or {}
    except Exception as x:e.append(f'{rel}: {x}'); return {}
def j(rel):
    try:return json.loads((R/rel).read_text())
    except Exception as x:e.append(f'{rel}: {x}'); return {}
for rel in ['config/TECHNOLOGY-CAPABILITY-CATALOG.yaml','config/TECHNOLOGY-SELECTION-POLICY.yaml','config/TOOL-CAPABILITY-CATALOG.yaml','config/TOOL-SELECTION-POLICY.yaml','config/HARNESS-CONFORMANCE.yaml']:
    d=y(rel)
    if str(d.get('version')) not in {'5.9','5.9.3'}: e.append(f'{rel}: version')
tc=y('config/TECHNOLOGY-CAPABILITY-CATALOG.yaml'); caps=tc.get('capabilities') or {}
for need in ['backend_platform','api_contract','api_gateway_management','identity_iam','analytics_olap','time_series_metrics','event_streaming','durable_workflow','realtime_collaboration','mobile','desktop','commerce','iot_device_telemetry','ai_model_serving','deployment']:
    if need not in caps or len((caps.get(need) or {}).get('candidates',[]))<1:e.append(f'technology capability missing {need}')
blob=str(tc)
for token in ['Supabase','Appwrite','PocketBase','Directus','Convex','FastAPI','NestJS','Hono','Tauri','Electron','ClickHouse','DuckDB','TimescaleDB','Temporal','NATS','Qdrant','ThingsBoard','Medusa']:
    if token not in blob:e.append(f'technology candidate missing {token}')
tools=y('config/TOOL-CAPABILITY-CATALOG.yaml').get('providers') or {}
for need in ['crw','obscura','playwright_mcp']:
    if need not in tools:e.append(f'tool provider missing {need}')
if (tools.get('crw') or {}).get('auto_install') is not True:e.append('crw auto-install policy')
if (tools.get('obscura') or {}).get('auto_install') is not True:e.append('obscura auto-install policy')
h=y('config/HARNESS-CONFORMANCE.yaml'); cc=(h.get('harnesses') or {}).get('command-code') or {}
if cc.get('support')!='FIRST_CLASS_PREVIEW':e.append('Command Code support')
if cc.get('canonical_skills')!='.agents/skills':e.append('Command Code canonical skills')
for rel in ['planning/execution/CAPABILITY-STATE.json','planning/execution/TOOL-LOCK.json']:
    if j(rel).get('version')!='5.9':e.append(f'{rel}: version')
read=(R/'README.md').read_text()
for token in ['Custom GPT','does not consume tokens, credits, or API budget from the later coding-agent account','Command Code','CRW / fastCRW','Obscura','Playwright','Capability-driven technology selection']:
    if token not in read:e.append(f'README missing {token}')
hand=(R/'release-handoff/UPDATE-PUBLIC-GITHUB-REPO.md').read_text()
for token in ['software-planning-lead-v5.9.3-github-native.zip','raffnix204/CtrlAltDelegate','commit','push']:
    if token not in hand:e.append(f'release handoff missing {token}')
for rel in ['scripts/detect_tool_capabilities.py','scripts/resolve_capability_provider.py','scripts/bootstrap_tool.py','scripts/verify_tool_capability.py','adapters/command-code/HARNESS-CAPABILITIES.yaml']:
    if not (R/rel).is_file():e.append(f'missing {rel}')
if e:
    print('V58_ARCHITECTURE_QA_FAIL'); [print('-',x) for x in e]; sys.exit(2)
print(f'V58_ARCHITECTURE_QA_PASS technology_capabilities={len(caps)} tool_providers={len(tools)} command_code={cc.get("support")}')
