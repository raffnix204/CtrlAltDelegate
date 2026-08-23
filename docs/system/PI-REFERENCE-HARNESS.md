# Pi Reference Harness — V5.8.2

Pi is V5.8's golden-path harness, while the core planning/skills remain portable.

## Philosophy

Pi core is intentionally minimal. V5.8.2 does not mandate package names or versions. It asks: **does the required capability exist in the active session?**

## Capability inventory

Core when routed:
- persistent Goal/run loop;
- isolated general worker delegation;
- parallel delegation for dependency-ready work;
- independent reviewer/verifier;
- file/search/bash/edit/write;
- Git/worktrees;
- project Agent Skills.

Conditional:
- remote operator channel such as Telegram;
- WEB_ACQUISITION/MCP;
- browser automation;
- semantic code navigation for large repositories;
- container/database/platform tooling.

A Goal extension may provide persistence and/or a verifier but not general worker delegation. Detect separately.

## Resolution

`NATIVE → EXISTING HOST/PROJECT → RESEARCH CURRENT PROVIDER → SAFE INSTALL → VERIFY → RECORD`.

When installing:
- prefer Pi's supported package mechanism and project-local scope when project-specific;
- verify current package identity/source/license/maintenance/compatibility;
- do not use a stale version from V5.8.2 docs;
- record the actually resolved version/provider in `HARNESS-STATE.md` for reproducibility;
- do not overwrite global settings or duplicate an equivalent installed capability;
- project trust/policy is authoritative.

## Goal integration

If persistent Goal mode exists, use it as the **outer persistence loop** for `AUTOPILOT-GOAL.md`. The V5.8.2 orchestrator still controls jobs/waves/gates/continuation. Do not stack another looping extension merely to keep the run alive.

## Remote operator

Telegram or another remote operator channel is optional host infrastructure. Reuse it if present; never install it as a project requirement unless the project/user explicitly wants remote operations.

Project `.pi/prompts/autopilot.md` exposes `/autopilot` in Pi after project trust. Remote-control plugins may surface Pi prompt templates if they support that capability.

## Model selection

V5.8.2 does not route, rank, pin, or switch models. Use the model/provider configured by the operator or active harness. Delegation, context freshness, research and verification must work without changing that selection.

## Restart/reload handling
Capability selection is dynamic and model-neutral. If isolated fresh-context or parallel delegation is required but absent, research a current trusted Pi-compatible provider at runtime and install through supported Pi mechanisms, preferring project scope where appropriate. Do not encode a permanent package/version/model in this system. After installation, use a supported `/reload`/reload mechanism when possible and smoke-test again. If the current process cannot activate the capability, persist state and set `RESTART_REQUIRED`; the operator only needs to restart/resume Pi, after which preflight resumes from disk. Never bypass Project Trust.

## Parallel proof
When a wave has independent ready work, general subagents are not enough: verify actual parallel fan-out with isolated child contexts. Record effective concurrency, background capability and worktree/cwd isolation in `PARALLELISM-STATE.yaml`; scheduler uses the discovered capacity rather than a fixed number.
