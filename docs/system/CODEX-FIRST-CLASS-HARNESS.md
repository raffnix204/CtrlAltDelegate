# Codex First-Class Harness — V5.8.2

Pi remains the reference/golden-path harness, while Codex CLI is a **first-class equal behavioral target**. V5.8.2 defines one canonical execution contract; harness adapters translate capabilities without creating separate methodologies.

## Shared canonical surfaces
- root `AGENTS.md` and project handoff/goal/state;
- `.agents/skills/<id>/SKILL.md` canonical skills;
- exact per-job skill routing;
- Git/worktree/isolation policy;
- research, documentation, convergence, evidence and verification gates;
- autonomous continuation and hard-stop semantics.

## Codex preflight
When active harness is Codex:
1. verify the current Codex client/session can read repository instructions and canonical skills;
2. inventory file/search/shell/Git, sandbox/approval mode, network/web/browser/MCP/tool surfaces actually available;
3. inventory isolated delegation/parallel execution capabilities exposed by the current Codex surface or installed compatible extension/plugin;
4. prefer native capabilities; bootstrap only genuinely required missing capabilities using current official OpenAI/plugin documentation and provenance checks;
5. after install/config changes, reload/restart if required, persist state, re-inventory and smoke test;
6. never assume Pi-specific Goal/packages exist and never install them into Codex.

## Parallelism
Do not claim Codex CLI itself has a specific fixed native agent fan-out capability unless the current session proves it. If isolated parallel delegation is required by the ready DAG and absent, resolve a current compatible capability through the generic bootstrap policy. If unavailable, record the constraint and continue with the best safe concurrency rather than weakening correctness.

## Sandbox/approvals
Respect the active Codex sandbox and approval policy. Do not disable protections merely to reach autonomy. If a required safe operation cannot proceed under policy, use the standard hard-stop/fallback mechanism.

## Model neutrality
Do not choose or route models. Use the operator/harness-selected model unchanged. Record it only as runtime evidence when useful for reproducibility/evals.

## Compatibility QA
V5.8.2 release QA verifies that every canonical skill is exposed through the shared `.agents/skills` surface and that no Pi-only operational instruction is required for Codex execution. Project-specific adapters may be added only when the current Codex capability contract requires them.
