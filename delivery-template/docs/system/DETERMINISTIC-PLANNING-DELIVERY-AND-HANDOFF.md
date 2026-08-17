# Deterministic Planning Delivery and Coding-Agent Handoff — V5.6.4

## Purpose

A planning run is not complete merely because planning documents exist. A Custom-GPT planning run reaches `DELIVERY_READY` only when the planning package, its deterministic location, and the coding-agent start prompt are all materialized and internally consistent. Any downloadable artifact that represents implementation-ready project planning is therefore a handoff delivery and must use this closure contract; a lone final-plan file is not a valid delivery. Explicitly requested intermediate drafts may be emitted only when clearly marked `DRAFT / NOT_HANDOFF`.

This contract prevents three failure classes:

1. project-specific or drifting delivery directory names;
2. a planning ZIP that omits the coding-agent handoff/start prompt;
3. a handoff prompt that assumes the coding agent starts inside the delivery directory instead of the actual project root.

## Canonical Custom-GPT delivery topology

Custom-GPT planning exports use one fixed archive name and one fixed control-directory name:

```text
ctrlaltdelegate-delivery.zip
└── ctrlaltdelegate/
    ├── AGENTS.md
    ├── CLAUDE.md
    ├── CODING-AGENT-START-PROMPT.md
    ├── DELIVERY-MANIFEST.yaml
    ├── .agents/skills/<selected>/...
    ├── .claude/skills/<selected>/SKILL.md
    ├── config/...
    ├── scripts/...
    ├── docs/system/...
    └── planning/
        ├── PROJECT.md
        ├── REQUIREMENTS.md
        ├── discovery/...
        ├── architecture/...
        ├── research/...
        ├── context/...
        ├── repository/...            # when relevant
        ├── execution/...
        └── handoff/
            ├── HANDOFF-STATUS.yaml
            ├── CODING-AGENT-HANDOFF.md
            └── FINAL-START-PROMPT.md
```

The archive and top-level directory names are **not project-derived**. Project identity belongs in planning metadata, not filesystem topology.

## Installation model

The user extracts the ZIP and places the resulting `ctrlaltdelegate/` directory directly inside the target project's root directory.

Example:

```text
my-project/                         # coding-agent working directory / project root
├── package.json                    # existing or future application files
├── src/                            # existing or future application files
└── ctrlaltdelegate/                # fixed planning/control package
    ├── CODING-AGENT-START-PROMPT.md
    └── planning/...
```

The coding agent is started from `my-project/`, **not** from `my-project/ctrlaltdelegate/`.

## Path model

Every generated start prompt must establish these meanings before any other instruction:

```text
PROJECT_ROOT  = the coding agent's current project/repository root
CONTROL_ROOT  = ./ctrlaltdelegate
PLANNING_ROOT = ./ctrlaltdelegate/planning
SKILLS_ROOT   = ./ctrlaltdelegate/.agents/skills
```

If Git already exists, `PROJECT_ROOT` is reconciled with `git rev-parse --show-toplevel`. If Git does not yet exist, the current working directory remains the intended project root and Git initialization occurs there when appropriate.

The agent must never mistake `CONTROL_ROOT` for the application repository root. Product code belongs under `PROJECT_ROOT` using the selected stack's native conventions. CtrlAltDelegate-owned planning/state/evidence and its packaged support files remain under `CONTROL_ROOT` unless the handoff explicitly requires a safe project-root integration step.

## Mandatory start prompt

Every Custom-GPT planning delivery must contain:

```text
ctrlaltdelegate/CODING-AGENT-START-PROMPT.md
```

The planner's final user-facing response must also reproduce the same resolved start prompt text so the user can paste it directly into the coding agent. `planning/handoff/FINAL-START-PROMPT.md` must be byte-identical to `CODING-AGENT-START-PROMPT.md`; there is one canonical execution-start prompt, stored at both the convenient package root and the canonical handoff path.

The start prompt must, at minimum:

1. state that the coding agent is running from `PROJECT_ROOT`;
2. set `CONTROL_ROOT=./ctrlaltdelegate`;
3. read, in order:
   - `./ctrlaltdelegate/AGENTS.md`;
   - `./ctrlaltdelegate/planning/handoff/HANDOFF-STATUS.yaml`;
   - `./ctrlaltdelegate/planning/handoff/CODING-AGENT-HANDOFF.md`;
   - `./ctrlaltdelegate/planning/execution/STATE.md`;
4. reject a missing or non-ready handoff instead of improvising paths;
5. treat the package as `EXECUTION_HANDOFF` when `HANDOFF-STATUS.yaml` is `READY`;
6. preserve resolved discovery constraints and avoid broad replanning unless repository/runtime evidence invalidates them;
7. implement into `PROJECT_ROOT`, not into `CONTROL_ROOT`;
8. continue through verification, documentation, Git/GitHub and `COMPLETED` under the normal execution contract.

## Handoff status marker

`planning/handoff/HANDOFF-STATUS.yaml` is written **last**, after the other delivery files have been generated and checked.

Minimum schema:

```yaml
version: '5.6.4'
status: READY
mode: EXECUTION_HANDOFF
topology: NESTED_CONTROL_ROOT
project_root: .
control_root: ./ctrlaltdelegate
planning_root: ./ctrlaltdelegate/planning
skills_root: ./ctrlaltdelegate/.agents/skills
start_prompt: ./ctrlaltdelegate/CODING-AGENT-START-PROMPT.md
canonical_handoff: ./ctrlaltdelegate/planning/handoff/CODING-AGENT-HANDOFF.md
final_start_prompt: ./ctrlaltdelegate/planning/handoff/FINAL-START-PROMPT.md
start_prompt_parity: BYTE_IDENTICAL
state: ./ctrlaltdelegate/planning/execution/STATE.md
unresolved_blocking_decisions: 0
```

If material blockers remain, the status must not be `READY` and the planner must not claim `DELIVERY_READY`. A coding agent receiving an incomplete or inconsistent package reports `BLOCKED_DELIVERY_INCOMPLETE` and names the exact missing path instead of guessing another topology.

## Delivery closure gate

Planning-file generation and handoff generation are one atomic logical operation:

```text
PLAN READY
→ MATERIALIZE CONTROL PACKAGE
→ MATERIALIZE START PROMPT
→ MATERIALIZE CANONICAL HANDOFF
→ VERIFY REQUIRED PATHS
→ VERIFY PROMPT PATHS
→ VERIFY NO BLOCKING DECISIONS
→ WRITE HANDOFF-STATUS.yaml LAST
→ PACKAGE ZIP
→ RE-OPEN / VERIFY PACKAGE CONTENTS
→ DELIVERY_READY
```

A planning ZIP without the start prompt is invalid. A start prompt without the planning package is invalid. A prompt that references a project-specific delivery directory is invalid.

## Required delivery manifest fields

`ctrlaltdelegate/DELIVERY-MANIFEST.yaml` records at least:

```yaml
version: '5.6.4'
layout: NESTED_CONTROL_ROOT
archive_name: ctrlaltdelegate-delivery.zip
control_root_name: ctrlaltdelegate
coding_agent_working_directory: PROJECT_ROOT
project_root_relation_from_control_root: ..
start_prompt: CODING-AGENT-START-PROMPT.md
handoff_status: planning/handoff/HANDOFF-STATUS.yaml
canonical_handoff: planning/handoff/CODING-AGENT-HANDOFF.md
final_start_prompt: planning/handoff/FINAL-START-PROMPT.md
start_prompt_parity: BYTE_IDENTICAL
state: planning/execution/STATE.md
```

It also lists all mandatory planning/system files included in the concrete delivery.

## Brownfield safety

Because the Custom-GPT delivery now lives in one fixed nested directory, installing it into an existing project does not require blindly overwriting root `AGENTS.md`, `CLAUDE.md`, hooks, source files or configuration.

The coding agent may later integrate selected project-root support files only when useful and only through an explicit safe-merge step. Existing user/harness files remain authoritative unless deliberately reconciled.

## GitHub-native standalone distribution

The GitHub-native release itself remains **root-native** and fully standalone. A fresh clone of the GitHub-native distribution still runs `FULL_LIFECYCLE` from the repository root.

The nested `ctrlaltdelegate/` topology is specifically the deterministic **Custom-GPT planning handoff package** and an accepted execution-handoff input to GitHub-native methodology.

## Design provenance

This closure gate is independently written for CtrlAltDelegate. Review of the uploaded gstack 1.67.0.0 snapshot reinforced several durable ideas already compatible with this system: deterministic artifact paths, writing persistent decision/review state to disk, pre-exit verification that required planning outputs actually exist, and blocking transition when a required review/handoff marker is missing. CtrlAltDelegate does not copy gstack prompts, Claude-specific mechanics, telemetry, browser infrastructure, or its opinionated review roles.
