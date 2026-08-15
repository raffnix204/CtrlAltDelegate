# V5.6.1 Setup

## GitHub-native direct use
Place/merge these system files into the intended repository root without overwriting existing application or harness configuration blindly.

Start with the direct prompt from `README.md`.

## Existing repository
Preserve dirty user work and existing instruction/harness files. Merge V5.6.1 instructions/settings rather than replacing project-owned policy. Run repository onboarding before broad changes.

## Custom-GPT delivery
A V5.6.1 `<project-slug>-coding-agent-delivery/` is repo-root-ready. For greenfield, its extracted contents are the initial repository working tree and can be committed/pushed directly. For brownfield, safe-merge the planned files into an isolated branch/worktree; there is no nested `project-overlay/`. Start from `planning/handoff/FINAL-START-PROMPT.md`.

## Pi
Pi is the reference harness. Trust project resources when appropriate. V5.6.1 ships `.agents/skills/` and `.pi/prompts/autopilot.md` but no hardcoded third-party package install. Existing host Goal/subagent/MCP/browser/operator tools are reused. Missing required capabilities are researched/resolved at first run.

## GitHub
A valid existing origin is reused. Without one, the agent creates the planned private-by-default repository under the authenticated account when permitted. GitHub synchronization is part of completion unless explicitly disabled by the plan.


## Stack and skills
Before execution design, resolve `planning/architecture/STACK-MANIFEST.yaml` to `STACK_READY`, then select the project skill subset in `planning/execution/SKILLS-MANIFEST.yaml` to `SKILLSET_READY`. Every job must list exact skill paths; workers return `SKILLS_APPLIED`.


Run `python3 scripts/install_git_guards.py` after repository initialization/import. Existing custom hooks must be preserved and integrated. Verify `GIT_GUARDS_READY` before implementation commits.
