# Command Code First-Class Preview — V5.8.2

Command Code is a `FIRST_CLASS_PREVIEW` harness target. Promotion to `FIRST_CLASS` requires the runtime conformance lane because the public GitHub repository does not expose the complete CLI implementation.

## Native fit
CtrlAltDelegate maps canonical `AGENTS.md` and `.agents/skills` directly. Detect actual support for project memory, progressive skill loading, isolated/parallel/background subagents, persistent dependency-aware tasks, headless structured output, session resume/continue, MCP, hooks, permission enforcement and worktrees from the installed client rather than assuming documentation equals runtime.

## Source of truth
CtrlAltDelegate `JOB-GRAPH.json`, surface policy, requirements, evidence and planning state remain authoritative. Native Command Code tasks may mirror ready jobs for execution but must not silently replace or override the control graph. Taste/preferences may influence implementation style only within explicit requirements/architecture/policy.

## Permissions and hooks
Where supported, translate CtrlAltDelegate protected surfaces and worker authority into native `ALLOW/ASK/DENY`/hook enforcement. `INSTRUCTIONS != ENFORCEMENT`: a prompt prohibition is not equivalent to a native permission boundary.

## Caching/model economics
The core methodology does not route or pin models. Command Code may exploit its own model/provider/cache behavior, but CtrlAltDelegate only specifies worker capability/assurance requirements. Pricing, model availability and cache rules are drift-prone and must not be hardcoded into the release.

## Conformance
The lane verifies: instructions, `.agents/skills`, headless structured output, session resume, scoped file/shell/Git access, deny enforcement, subagent isolation/parallelism, task mapping, MCP registration, hooks, worktree behavior and CtrlAltDelegate handoff/resume. Missing optional features reduce the effective capability attestation; missing required job capability triggers reroute/fail-loud.
