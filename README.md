# Software Planning Lead V5.6.1 — GitHub Native Edition

Autonomous software planning and delivery system with Pi as the reference harness and portable support for Codex, Claude Code and OpenCode.

## V5.6.1 highlights

- **145 canonical expert skills** in this release; the library has no conceptual size cap.
- **Global rules once:** autonomy/research/evidence/routing live in one execution contract instead of being repeated across specialist skills.
- **Domain depth progressively loaded:** 136 reference files provide framework/platform/database/security depth without preloading it into every worker context.
- New specialists: MongoDB, Terraform, Cloudflare platform, WordPress, threat modeling and property-based testing.
- Skill changes are release-tested through routing, behavior and system-regression eval classes against frozen baselines.
- Progressive routing: full library → project-selected → exact job-required skills → optional reference files.
- Framework specialists for major web/backend/mobile stacks plus language specialists.
- First-class SQLite and SQLite vector-search engineering.
- First-class network/infrastructure automation including UniFi/Ubiquiti, OpenWrt and OPNsense specialists.
- Autonomous execution-time research that reuses planner research and only closes remaining/current evidence gaps.
- Capability-based Pi bootstrap: existing Goal/subagent/MCP/browser/operator tools are reused; no static third-party plugin versions.
- Provider-neutral web acquisition: existing Firecrawl-compatible MCP/API or harness-native capabilities first.
- GitHub bootstrap/sync integrated into completion.
- Repo-root-ready Custom-GPT project delivery with a persistent versioned `planning/` tree and canonical clone/start handoff.

## Direct start

Read `AGENTS.md`, `planning/handoff/CODING-AGENT-HANDOFF.md` and `planning/execution/STATE.md`, then execute `planning/execution/AUTOPILOT-GOAL.md` through `COMPLETED`. A greenfield Custom-GPT delivery is already repo-root-ready; brownfield deliveries are safe-merged.

## Skill architecture

Canonical project skills live under `.agents/skills/<id>/`. Each skill's `SKILL.md` is the entrypoint. Some skills include `references/` for progressive deep reads.

`config/STACK-SIGNALS.yaml` detects repository evidence.
`config/SKILL-ROUTING-RULES.yaml` maps stack/capability/risk changes to specialists.
`.agents/skills/CATALOG.yaml` is the library index.

A generated project does **not** receive all 145 skills. It receives only project-relevant skill directories, and each worker reads only the subset required by its job.

## Research architecture

The Custom GPT performs broad planning and research. Coding execution starts from that evidence and performs only `NONE | VERIFY_DRIFT | TARGETED | SPIKE` research needed for implementation. Current official docs and executable spikes settle drift/compatibility questions. Routine technical decisions are autonomous.

## GitHub

Reuse an existing valid origin. Otherwise create the planned repository under the authenticated account, PRIVATE by default unless the plan explicitly requires PUBLIC. Commit/push meaningful checkpoints and keep validated `main` synchronized without bypassing branch protection.

## Pi

See `docs/system/PI-REFERENCE-HARNESS.md`. V5.6.1 specifies required capabilities, not package names. Goal persistence, general subagents, independent review, remote operator, MCP/web acquisition, browser, code navigation and project-specific execution capabilities are detected independently.

## Validation

Run:

```bash
python3 scripts/validate_system.py
python3 scripts/harness_preflight.py
```


## V5.6.1 hard autonomy guarantees
- **Docs are commit-consistent:** every code/config commit records documentation impact; affected README/docs update in the same commit and pre-push history is checked.
- **Beginner documentation:** README covers every major user-visible feature directly or through clear linked guides, with tested install/setup/config/usage/troubleshooting.
- **Context-rot resistance:** fresh workers/reviewers, durable Git/state truth and context epochs replace long-lived transcript dependence.
- **Bottleneck-aware parallelism:** every wave maximizes useful independent work without building writer WIP in front of saturated integration/test/CI/review/runtime capacity; no fixed agent count or model routing.
- **Capability bootstrap:** missing Pi capabilities are researched/installed only when required, reloaded/reverified where possible, or produce `RESTART_REQUIRED` with exact resume instructions.


## V5.6.1 system guides
- `docs/system/DOCUMENTATION-LIFECYCLE.md` — commit/push freshness, beginner README and final fresh-user review.
- `docs/system/CONTEXT-AND-PARALLELISM.md` — context epochs, fresh agents and maximum safe wave concurrency.
- `docs/system/CAPABILITY-BOOTSTRAP.md` — capability detection, safe install, reload/restart/resume.
- `docs/system/STACK-AND-SKILL-ROUTING.md` — broad library with smallest-complete job routing.
- `docs/system/PROGRAM-DESIGN-AND-VERTICAL-SLICES.md` — early structural decisions, executable slices and re-steering.
- `docs/system/REPOSITORY-LAYOUT-AND-STATE.md` — persistent `planning/`, live state and repo-root-ready delivery.
- `docs/system/GITHUB-DIRECT-HANDOFF.md` — optional write-capable planner→GitHub publish with ZIP fallback.


## V5.6.1 Program Design, State & Flow
V5.6.1 combines lean-solution/convergence/evidence/skill-eval hardening with Program Design Gate, vertical-slice-first execution, pre-fix/post-fix bug evidence, Failure-Mode Closure, measurable outcome backpressure, bottleneck-aware WIP control, persistent `planning/` state and repo-root-ready delivery. Pi remains the reference harness and Codex CLI a first-class equal behavioral target using the same canonical `.agents/skills` and execution contract.


## V5.6.1 planning discovery
Planning now uses adaptive collaborative discovery plus explicit `REQUIRED | PREFERRED | AUTO` technical preferences before consequential stack/architecture decisions. See `docs/system/COLLABORATIVE-DISCOVERY-AND-CONSTRAINTS.md`.

## V5.6.1 adaptive execution
V5.6.1 retains the `EXECUTION_RIGHTSIZING_GATE` (`MICRO | SMALL | STANDARD | HIGH_RISK`) plus progress-aware worker liveness/checkpoint-resume. Small projects keep full product quality while avoiding micro-job, branch, review, evidence and commit ceremony that adds no value. Long-running subagents continue while they make meaningful progress; static elapsed time alone is not a stall signal.
