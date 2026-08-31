# V5.9.3 Setup

## GitHub-native direct use — full lifecycle
The GitHub Native Edition is standalone. Clone/fork the complete distribution, open repository root in a compatible coding agent, and use the prompt in `START-HERE.md`. No Custom GPT is required.

A fresh checkout selects `FULL_LIFECYCLE` and starts collaborative discovery. Partial planning selects `RESUME_PLANNING`; an implementation-ready delivery selects `EXECUTION_HANDOFF`; interrupted work selects `RESUME_EXECUTION`.

## Existing repository
Preserve dirty/untracked user work and existing instruction/harness files. Safe-merge CtrlAltDelegate rather than blindly replacing project-owned policy. Run repository onboarding before broad changes.

For a generated delivery, inspect collisions with:

```bash
python3 scripts/import_delivery.py /path/to/delivery
```

then use `--apply` after review.

## Optional Custom-GPT delivery
A V5.9 Custom-GPT handoff is `ctrlaltdelegate-delivery.zip`. Copy the ZIP into the target project root, start the coding agent from that root, and paste the generated start prompt. The agent safely imports the single `.ctrlaltdelegate/` package, keeps it `LOCAL_PRIVATE` by default, validates it, and continues as `EXECUTION_HANDOFF`; GitHub-native standalone use remains independent of it.

## Complete distribution check
The published GitHub Native repository should contain `.agents/skills/`, `.claude/skills/`, `.pi/`, `.githooks/`, `evals/`, `scripts/`, `docs/`, `config/` and `planning/`.

Run:

```bash
python3 scripts/validate_system.py
python3 scripts/validate_skill_evals.py
python3 scripts/harness_preflight.py
```

The first two must pass for an intact release checkout. `harness_preflight.py` additionally reports local harness/tool availability.

## Oh My Pi / Pi / Codex / Claude Code / OpenCode
Oh My Pi is first-class and reuses Pi methodology while using OMP-native `task`, structured results, model roles and worktree isolation when attested. Pi remains the reference harness; Codex CLI is an equal first-class behavioral target. Claude Code and OpenCode use the same canonical contracts when required capabilities are available. Per-subagent model routing is used when supported; otherwise the same role/context contract runs on the active inherited model.

For Graphify, run `python3 scripts/graphify_ctl.py prepare`. If it returns `ASK_USER`, record one of `HOST_ALWAYS | PROJECT_ONLY | NEVER`; host installation requires explicit consent and uses `uv tool`/`pipx`, never sudo/system pip.

## Git guards
After repository initialization/import run `python3 scripts/install_git_guards.py`. Preserve/integrate existing custom hooks and reach `GIT_GUARDS_READY` before implementation commits.


## Language behavior
Use any supported human language when talking to the coding agent. The agent follows the user's language by default, while CtrlAltDelegate-controlled system and planning artifacts remain English. See `docs/system/LANGUAGE-AND-INTERACTION.md`.
