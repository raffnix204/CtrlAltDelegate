# V5.6.3 Setup

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
A V5.6.3 `<project-slug>-coding-agent-delivery/` is repo-root-ready. For greenfield, its extracted contents may become the initial working tree. For brownfield, safe-merge it. Because planning is already implementation-ready, start from `planning/handoff/FINAL-START-PROMPT.md`; this is an `EXECUTION_HANDOFF`, not a prerequisite for GitHub-native use.

## Complete distribution check
The published GitHub Native repository should contain `.agents/skills/`, `.claude/skills/`, `.pi/`, `.githooks/`, `evals/`, `scripts/`, `docs/`, `config/` and `planning/`.

Run:

```bash
python3 scripts/validate_system.py
python3 scripts/validate_skill_evals.py
python3 scripts/harness_preflight.py
```

The first two must pass for an intact release checkout. `harness_preflight.py` additionally reports local harness/tool availability.

## Pi / Codex / Claude Code / OpenCode
Pi is the reference harness; Codex CLI is an equal first-class behavioral target. Claude Code and OpenCode use the same canonical contracts when required capabilities are available. No model routing is required.

## Git guards
After repository initialization/import run `python3 scripts/install_git_guards.py`. Preserve/integrate existing custom hooks and reach `GIT_GUARDS_READY` before implementation commits.


## Language behavior
Use any supported human language when talking to the coding agent. The agent follows the user's language by default, while CtrlAltDelegate-controlled system and planning artifacts remain English. See `docs/system/LANGUAGE-AND-INTERACTION.md`.
