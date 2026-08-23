#!/usr/bin/env python3
"""Safely import a CtrlAltDelegate V5.8.2 planning delivery ZIP into a target project.

This helper belongs to the root-native distribution. A Custom-GPT handoff can be
bootstrapped by a coding agent with equivalent standard archive operations when
this helper is not already present in the target repository.
"""
from __future__ import annotations
from pathlib import Path, PurePosixPath
import argparse, json, os, shutil, stat, sys, uuid, zipfile, re

ARCHIVE_NAME = "ctrlaltdelegate-delivery.zip"
CONTROL_NAME = ".ctrlaltdelegate"
IGNORE_LINES = [
    "/ctrlaltdelegate-delivery.zip",
    "/.ctrlaltdelegate/",
    "/.ctrlaltdelegate.importing-*/",
    "/.ctrlaltdelegate.incoming-*/",
]
REQUIRED = [
    "AGENTS.md", "CODING-AGENT-START-PROMPT.md", "CONTROL-PACKAGE.json",
    "DELIVERY-MANIFEST.yaml", "TARGET-GITIGNORE.fragment",
    "planning/handoff/HANDOFF-STATUS.yaml",
    "planning/handoff/CODING-AGENT-HANDOFF.md",
    "planning/handoff/FINAL-START-PROMPT.md",
    "planning/execution/STATE.md", "planning/execution/PLANNING-BASELINE.json", "planning/execution/JOB-GRAPH.json",
    "planning/execution/LOOP-STATE.json", "config/LOOP-CONTRACTS.yaml",
    "config/SURFACE-POLICY.yaml", "config/HARNESS-CONFORMANCE.yaml",
]

def is_link(info: zipfile.ZipInfo) -> bool:
    mode = (info.external_attr >> 16) & 0xFFFF
    return stat.S_ISLNK(mode)

def validate_members(zf: zipfile.ZipFile) -> list[str]:
    errors=[]
    for info in zf.infolist():
        raw=info.filename.replace('\\','/')
        p=PurePosixPath(raw)
        if not raw or raw.startswith('/') or p.is_absolute():
            errors.append(f"absolute/empty archive member: {raw!r}"); continue
        if any(part in {'..',''} for part in p.parts):
            errors.append(f"unsafe traversal member: {raw}"); continue
        if p.parts[0] != CONTROL_NAME:
            errors.append(f"unexpected top-level path: {raw}")
        if is_link(info): errors.append(f"link entry forbidden: {raw}")
    return errors

def yaml_scalar(text: str, key: str):
    m=re.search(rf"(?m)^\s*{re.escape(key)}:\s*['\"]?([^\n'\"]+)",text)
    return m.group(1).strip() if m else None

def validate_tree(control: Path) -> list[str]:
    errors=[]
    for rel in REQUIRED:
        if not (control/rel).is_file(): errors.append(f"missing required file: {rel}")
    try:
        cp=json.loads((control/'CONTROL-PACKAGE.json').read_text(encoding='utf-8'))
        expected={
            'ctrlaltdelegate_version':'5.8.2', 'archive_name':ARCHIVE_NAME,
            'top_level_directory':CONTROL_NAME, 'control_root':'./.ctrlaltdelegate',
            'control_visibility':'LOCAL_PRIVATE',
        }
        for k,v in expected.items():
            if cp.get(k)!=v: errors.append(f"CONTROL-PACKAGE {k} mismatch")
    except Exception as exc: errors.append(f"CONTROL-PACKAGE.json parse error: {exc}")
    p=control/'CODING-AGENT-START-PROMPT.md'; q=control/'planning/handoff/FINAL-START-PROMPT.md'
    if p.is_file() and q.is_file() and p.read_bytes()!=q.read_bytes(): errors.append('start prompt parity mismatch')
    try:
        baseline=json.loads((control/'planning/execution/PLANNING-BASELINE.json').read_text(encoding='utf-8'))
        if baseline.get('status')!='ATTESTED' or not baseline.get('aggregate_sha256'): errors.append('planning baseline is not attested')
    except Exception as exc: errors.append(f'planning baseline parse error: {exc}')
    s=control/'planning/handoff/HANDOFF-STATUS.yaml'
    if s.is_file():
        text=s.read_text(encoding='utf-8')
        for k,v in {'version':'5.8.2','status':'READY','mode':'EXECUTION_HANDOFF','topology':'ZIP_TO_HIDDEN_CONTROL_ROOT','control_root':'./.ctrlaltdelegate','control_visibility':'LOCAL_PRIVATE','unresolved_blocking_decisions':'0'}.items():
            if yaml_scalar(text,k)!=v: errors.append(f"handoff {k} mismatch")
        for k in ['required_paths_present','prompt_paths_verified','planning_ready','planning_baseline_attested','zero_blocking_decisions','control_tree_verified_before_archive','planning_skill_state_present']:
            if yaml_scalar(text,k)!='true': errors.append(f"closure check not true: {k}")
    return errors

def update_gitignore(project: Path) -> None:
    path=project/'.gitignore'
    existing=path.read_text(encoding='utf-8') if path.exists() else ''
    missing=[line for line in IGNORE_LINES if line not in existing.splitlines()]
    if not missing: return
    suffix='\n' if existing and not existing.endswith('\n') else ''
    block='\n# CtrlAltDelegate local control plane\n'+'\n'.join(missing)+'\n'
    path.write_text(existing+suffix+block,encoding='utf-8')

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--project-root', default='.')
    ap.add_argument('--archive', default=ARCHIVE_NAME)
    ap.add_argument('--replace-existing', action='store_true', help='replace an existing control root only after the incoming package validates')
    args=ap.parse_args()
    project=Path(args.project_root).resolve(); archive=(project/args.archive).resolve() if not Path(args.archive).is_absolute() else Path(args.archive).resolve()
    if not archive.is_file(): print('BLOCKED_DELIVERY_INCOMPLETE: missing',archive); return 2
    update_gitignore(project)
    temp=project/f"{CONTROL_NAME}.importing-{uuid.uuid4().hex[:10]}"
    control=project/CONTROL_NAME
    try:
        with zipfile.ZipFile(archive,'r') as zf:
            errors=validate_members(zf)
            if errors:
                print('BLOCKED_DELIVERY_INCOMPLETE'); [print('-',e) for e in errors]; return 2
            temp.mkdir(parents=False,exist_ok=False)
            zf.extractall(temp)
        incoming=temp/CONTROL_NAME
        errors=validate_tree(incoming)
        if errors:
            print('BLOCKED_DELIVERY_INCOMPLETE'); [print('-',e) for e in errors]; return 2
        if control.exists():
            if not args.replace_existing:
                print(f'BLOCKED_DELIVERY_INCOMPLETE: {control} already exists; reconcile existing state or rerun with explicit --replace-existing only when safe')
                return 2
            backup=project/f"{CONTROL_NAME}.incoming-{uuid.uuid4().hex[:10]}"
            control.rename(backup)
            try: incoming.rename(control)
            except Exception:
                backup.rename(control); raise
        else:
            incoming.rename(control)
        # The root-level ZIP is transport, not durable product-tree content.
        # Retain it under the ignored control root when it originated from the project root.
        try:
            if archive.parent == project and archive.name == ARCHIVE_NAME:
                inbox = control / 'inbox'
                inbox.mkdir(parents=True, exist_ok=True)
                retained = inbox / ARCHIVE_NAME
                if retained.exists():
                    retained.unlink()
                archive.replace(retained)
        except Exception as exc:
            print(f'CONTROL_PACKAGE_IMPORT_WARNING: could not move inbound archive into control inbox: {exc}')
        print('CONTROL_PACKAGE_IMPORT_PASS')
        print('PROJECT_ROOT=',project)
        print('CONTROL_ROOT=',control)
        return 0
    finally:
        if temp.exists(): shutil.rmtree(temp,ignore_errors=True)
if __name__=='__main__': raise SystemExit(main())
