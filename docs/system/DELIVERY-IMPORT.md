# Delivery Import — V5.6.4

## Custom-GPT planning handoff

Custom-GPT planning exports are no longer project-named root overlays. The canonical archive is:

```text
ctrlaltdelegate-delivery.zip
└── ctrlaltdelegate/
```

Place the extracted `ctrlaltdelegate/` directory directly inside the target project root. Start the coding agent from the target project root and paste `ctrlaltdelegate/CODING-AGENT-START-PROMPT.md`.

The nested package intentionally avoids overwriting existing root `AGENTS.md`, `CLAUDE.md`, hooks, source files or project configuration. It carries the implementation-ready planning baseline, selected skills, execution contracts, state and handoff instructions under one deterministic control root.

Validate a package with:

```bash
python3 ctrlaltdelegate/scripts/validate_handoff_delivery.py .
```

The validator requires the fixed folder name, the canonical manifest, the start prompt, the handoff-ready marker and the expected planning paths.

## Path semantics

```text
PROJECT_ROOT  = target project / Git root
CONTROL_ROOT  = ./ctrlaltdelegate
PLANNING_ROOT = ./ctrlaltdelegate/planning
SKILLS_ROOT   = ./ctrlaltdelegate/.agents/skills
```

Product implementation belongs in `PROJECT_ROOT`. CtrlAltDelegate-owned planning/state/evidence remains under `CONTROL_ROOT` unless a deliberate safe integration step is required.

## Optional root integration

If the project benefits from root-level hooks, harness adapters or instruction-file integration, perform that as an explicit reviewed merge after the nested handoff has been validated. Never overwrite an existing project-owned agent instruction/configuration file blindly.

## GitHub-native standalone distribution

The GitHub-native release itself remains root-native. A cloned GitHub-native distribution can be used directly as the project baseline and runs the full planning + execution lifecycle without a Custom GPT.
