#!/usr/bin/env python3
"""Validate a deterministic nested CtrlAltDelegate planning handoff package."""
from __future__ import annotations

from pathlib import Path
import argparse
import sys
import yaml

EXPECTED_DIR = "ctrlaltdelegate"
EXPECTED_ARCHIVE = "ctrlaltdelegate-delivery.zip"
REQUIRED_FILES = [
    'AGENTS.md',
    'CLAUDE.md',
    'CODING-AGENT-START-PROMPT.md',
    'DELIVERY-MANIFEST.yaml',
    '.agents/skills/CATALOG.yaml',
    'config/SKILL-ROUTING-RULES.yaml',
    'scripts/validate_handoff_delivery.py',
    'docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md',
    'docs/system/SKILL-EXECUTION-CONTRACT.md',
    'docs/system/LANGUAGE-AND-INTERACTION.md',
    'docs/system/DETERMINISTIC-PLANNING-DELIVERY-AND-HANDOFF.md',
    'planning/PROJECT.md',
    'planning/REQUIREMENTS.md',
    'planning/discovery/DISCOVERY-STATE.md',
    'planning/discovery/TECHNICAL-PREFERENCES.yaml',
    'planning/handoff/HANDOFF-STATUS.yaml',
    'planning/handoff/CODING-AGENT-HANDOFF.md',
    'planning/handoff/FINAL-START-PROMPT.md',
    'planning/execution/STATE.md',
    'planning/execution/EXECUTION-PROFILE.yaml',
    'planning/execution/AUTOPILOT-GOAL.md',
    'planning/architecture/STACK-MANIFEST.yaml',
    'planning/architecture/PROGRAM-DESIGN.md',
    'planning/execution/SKILLS-MANIFEST.yaml',
    'planning/execution/CONVERGENCE-MATRIX.json',
    'planning/execution/EVIDENCE-INDEX.json',
    'planning/research/RESEARCH-POLICY.yaml',
]
PROMPT_REQUIRED = [
    "PROJECT_ROOT",
    "CONTROL_ROOT",
    "./ctrlaltdelegate/AGENTS.md",
    "./ctrlaltdelegate/planning/handoff/HANDOFF-STATUS.yaml",
    "./ctrlaltdelegate/planning/handoff/CODING-AGENT-HANDOFF.md",
    "./ctrlaltdelegate/planning/execution/STATE.md",
    "BLOCKED_DELIVERY_INCOMPLETE",
    "EXECUTION_HANDOFF",
]
PROMPT_FORBIDDEN = [
    "<project-slug>-coding-agent-delivery",
    "project-overlay",
]


def resolve_control_root(raw: Path) -> Path:
    raw = raw.resolve()
    if raw.name == EXPECTED_DIR:
        return raw
    child = raw / EXPECTED_DIR
    if child.is_dir():
        return child
    return raw


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=".", help="project root, extraction root, or ctrlaltdelegate directory")
    ap.add_argument("--allow-not-ready", action="store_true", help="validate templates before the final READY marker is written")
    args = ap.parse_args()

    control = resolve_control_root(Path(args.path))
    errors: list[str] = []

    if control.name != EXPECTED_DIR:
        errors.append(f"control directory must be named exactly {EXPECTED_DIR!r}; got {control.name!r}")

    for rel in REQUIRED_FILES:
        if not (control / rel).is_file():
            errors.append(f"missing required file: {rel}")

    manifest_path = control / "DELIVERY-MANIFEST.yaml"
    manifest = {}
    if manifest_path.is_file():
        try:
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        except Exception as exc:
            errors.append(f"DELIVERY-MANIFEST.yaml parse error: {exc}")
    expected_manifest = {
        "version": "5.6.4",
        "layout": "NESTED_CONTROL_ROOT",
        "archive_name": EXPECTED_ARCHIVE,
        "control_root_name": EXPECTED_DIR,
        "coding_agent_working_directory": "PROJECT_ROOT",
        "project_root_relation_from_control_root": "..",
        "start_prompt": "CODING-AGENT-START-PROMPT.md",
        "handoff_status": "planning/handoff/HANDOFF-STATUS.yaml",
        "canonical_handoff": "planning/handoff/CODING-AGENT-HANDOFF.md",
        "final_start_prompt": "planning/handoff/FINAL-START-PROMPT.md",
        "start_prompt_parity": "BYTE_IDENTICAL",
        "state": "planning/execution/STATE.md",
    }
    for key, value in expected_manifest.items():
        if manifest.get(key) != value:
            errors.append(f"manifest {key} must be {value!r}; got {manifest.get(key)!r}")
    declared_required = set(manifest.get("required_files") or [])
    missing_declared = [rel for rel in REQUIRED_FILES if rel not in declared_required]
    if missing_declared:
        errors.append(f"manifest required_files missing: {missing_declared}")

    prompt_path = control / "CODING-AGENT-START-PROMPT.md"
    if prompt_path.is_file():
        prompt = prompt_path.read_text(encoding="utf-8")
        for token in PROMPT_REQUIRED:
            if token not in prompt:
                errors.append(f"start prompt missing required token/path: {token}")
        for token in PROMPT_FORBIDDEN:
            if token in prompt:
                errors.append(f"start prompt contains forbidden legacy/project-derived path: {token}")

        final_prompt_path = control / "planning/handoff/FINAL-START-PROMPT.md"
        if final_prompt_path.is_file() and final_prompt_path.read_bytes() != prompt_path.read_bytes():
            errors.append("CODING-AGENT-START-PROMPT.md and planning/handoff/FINAL-START-PROMPT.md must be byte-identical")

    status_path = control / "planning/handoff/HANDOFF-STATUS.yaml"
    status = {}
    if status_path.is_file():
        try:
            status = yaml.safe_load(status_path.read_text(encoding="utf-8")) or {}
        except Exception as exc:
            errors.append(f"HANDOFF-STATUS.yaml parse error: {exc}")
    if status:
        expected_status = {
            "version": "5.6.4",
            "mode": "EXECUTION_HANDOFF",
            "topology": "NESTED_CONTROL_ROOT",
            "project_root": ".",
            "control_root": "./ctrlaltdelegate",
            "planning_root": "./ctrlaltdelegate/planning",
            "skills_root": "./ctrlaltdelegate/.agents/skills",
            "start_prompt": "./ctrlaltdelegate/CODING-AGENT-START-PROMPT.md",
            "canonical_handoff": "./ctrlaltdelegate/planning/handoff/CODING-AGENT-HANDOFF.md",
            "final_start_prompt": "./ctrlaltdelegate/planning/handoff/FINAL-START-PROMPT.md",
            "start_prompt_parity": "BYTE_IDENTICAL",
            "state": "./ctrlaltdelegate/planning/execution/STATE.md",
        }
        for key, value in expected_status.items():
            if status.get(key) != value:
                errors.append(f"handoff status {key} must be {value!r}; got {status.get(key)!r}")
        if not args.allow_not_ready:
            if status.get("status") != "READY":
                errors.append(f"handoff status must be READY; got {status.get('status')!r}")
            if status.get("unresolved_blocking_decisions") != 0:
                errors.append("handoff cannot be READY with unresolved blocking decisions")
            checks = status.get("closure_checks") or {}
            expected_checks = [
                "required_paths_present",
                "prompt_paths_verified",
                "planning_ready",
                "zero_blocking_decisions",
                "control_tree_verified_before_archive",
            ]
            false_checks = [key for key in expected_checks if checks.get(key) is not True]
            if false_checks:
                errors.append(f"READY handoff has incomplete closure checks: {false_checks}")

    if errors:
        print("HANDOFF_DELIVERY_QA_FAIL")
        for error in errors:
            print("-", error)
        return 2

    print(f"HANDOFF_DELIVERY_QA_PASS control_root={control} required_files={len(REQUIRED_FILES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
