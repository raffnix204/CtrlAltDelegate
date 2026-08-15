# Start Here — V5.6.3 GitHub Native

CtrlAltDelegate GitHub Native is a **complete planning + execution system**. You do not need the Custom GPT first. Open this repository with a capable coding agent and start from your actual project state.

The Custom GPT remains an optional planning-focused UI that can hand an implementation-ready baseline to the same system.

## Fastest path: start directly in the coding agent

1. Clone/fork this complete repository for a new project, or merge it safely into an existing repository.
2. Open the repository root with Pi, Codex CLI, Claude Code, OpenCode, or another compatible coding-agent harness with file/shell/Git access.
3. Paste this, filling in the project sentence:

> Read `AGENTS.md` first, then inspect Git and `planning/execution/STATE.md`.
>
> This is [a new project / an existing project]: [briefly describe what you want built, changed, fixed, audited, or improved].
>
> Determine the lifecycle mode from persisted repository state:
> - if discovery/planning has not started, run the full lifecycle from `INTAKE`;
> - if planning is partial, resume the earliest unresolved gate;
> - if planning is execution-ready, validate the baseline and begin execution;
> - if execution was already in progress, resume the exact persisted next action.
>
> For a new or incompletely planned project, perform collaborative discovery with me before consequential architecture or implementation. Do not repeat facts or decisions already persisted. The Custom GPT is optional and is not a prerequisite.
>
> Use the canonical CtrlAltDelegate contracts, routed specialist skills and progressive references. Keep project state on disk, make routine technical decisions autonomously within recorded authority, and continue through planning, implementation, verification, documentation and Git/GitHub until `COMPLETED`. Ask me only for a true product/business/safety/external hard stop defined by the contract.

That is the standalone entry point.

A fresh checkout begins in `FULL_LIFECYCLE`: collaborative discovery → constraints → research → stack/architecture → program design → skill routing → right-sized execution plan → implementation → verification → documentation/Git → `COMPLETED`.

## Automatic lifecycle modes

The agent must select from persisted evidence, not from assumptions:

- `FULL_LIFECYCLE` — no meaningful planning yet; start discovery.
- `RESUME_PLANNING` — planning is partial; resume the earliest unresolved material gate.
- `EXECUTION_HANDOFF` — implementation-ready planning exists; validate it and execute.
- `RESUME_EXECUTION` — execution already progressed; reconcile Git/runtime/evidence and resume the exact next action.

Canonical rules: `docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md`.

## Optional Custom GPT handoff

If you prefer to plan in ChatGPT first, use the CtrlAltDelegate Custom GPT. Its delivery is an `EXECUTION_HANDOFF` input to the same GitHub-native runtime. In that case, use `planning/handoff/FINAL-START-PROMPT.md`; that prompt intentionally tells the coding agent not to re-plan a completed baseline.

Do **not** use the execution-handoff prompt as the primary start for a fresh `NOT_STARTED` standalone checkout.

## Existing codebase / brownfield

Never blindly overwrite existing application or agent-instruction files. If importing a CtrlAltDelegate delivery into an existing repo, inspect collisions first:

```bash
python3 scripts/import_delivery.py /path/to/project-coding-agent-delivery
```

The command is dry-run by default. Re-run with `--apply` only after reviewing the plan. Collisions are staged under `planning/import-conflicts/` for explicit resolution.

Then the agent performs repository onboarding, protects dirty/untracked work, records the baseline SHA, detects the actual stack and resumes the appropriate lifecycle gate.

## Verify this checkout before publishing/using it

A complete V5.6.3 GitHub Native distribution includes the canonical skill library, Claude adapters, Pi prompt, Git guards, evals, scripts, system docs and persistent planning templates.

Run:

```bash
python3 scripts/validate_system.py
python3 scripts/validate_skill_evals.py
python3 scripts/harness_preflight.py
```

`validate_system.py` and `validate_skill_evals.py` must pass for the release distribution. `harness_preflight.py` additionally checks capabilities of the local checkout/environment and can report missing local tools even when the package itself is valid.

## Resume later / switch coding agents

Do not re-explain the project from conversation history. Start from Git and `planning/execution/STATE.md`. The versioned `planning/` tree is durable project memory; chat history is disposable.

## Language

Talk to the coding agent in the language you prefer. It should answer in that language by default while keeping CtrlAltDelegate system/planning artifacts in English. Localized product content remains allowed when the project requires it. See `docs/system/LANGUAGE-AND-INTERACTION.md`.
