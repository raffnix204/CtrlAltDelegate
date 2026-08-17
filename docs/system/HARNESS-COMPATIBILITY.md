# Harness Compatibility & Capability Bootstrap — V5.6.4

Pi is the reference/golden-path harness. **Codex CLI is a first-class equal behavioral target**; Claude Code and OpenCode are supported compatible harnesses under the same contract. One methodology applies to all harnesses.

## Canonical surfaces
- `AGENTS.md`
- `.agents/skills/<id>/SKILL.md`
- project handoff/goal/state/convergence/evidence
- `planning/execution/HARNESS-STATE.md`

Claude uses `CLAUDE.md → @AGENTS.md` and thin `.claude/skills/` adapters. Codex consumes the canonical project surfaces directly when supported by its current client; add only thin adapters proven necessary by current capability detection.

## Capability-first preflight
Detect the active harness/tool surface and inventory only capabilities required by the plan. Prefer native/existing functionality. Missing required capabilities follow:
`NATIVE → EXISTING → CURRENT OFFICIAL/PRIMARY RESEARCH → SAFE SUPPORTED INSTALL → RELOAD/RESTART → VERIFY → RECORD`.

Never hardcode third-party package/plugin versions or model choices. Do not install duplicate delegation/browser/MCP frameworks.

## Pi
See `PI-REFERENCE-HARNESS.md`. Reuse host-level Goal, remote operator, MCP and subagent capabilities when present; Project Trust is a security boundary.

## Codex CLI
See `CODEX-FIRST-CLASS-HARNESS.md`. Verify current instructions/skills, shell/Git, sandbox/approval, delegation/parallelism and conditional tool surfaces from the actual session. Never assume Pi packages exist. Missing required Codex capabilities are resolved through current OpenAI/plugin mechanisms under the same provenance/restart policy.

## Claude Code / OpenCode
Use native delegation/subagent/worktree capabilities when available and the same project contract. Do not install Pi/Codex-specific components unless the active harness requires them.

## HARNESS_READY
Set only when required instructions/skills/delegation/core tools and project-selected conditional tools are available and verified, or a documented allowed fallback exists.
