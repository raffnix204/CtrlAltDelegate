# Capability Bootstrap — V5.9

Pi is the reference harness. Oh My Pi is a first-class Pi-derived harness with native subagent/model/worktree capabilities when attested. V5.9.3 is capability-driven and requests abstract model classes without assuming every harness exposes per-subagent model selection. Never infer capability from a package name alone.

## Required execution capabilities
Inventory actual session/tool surfaces for instructions, Agent Skills, Git/GitHub, Goal/persistent continuation when used, isolated fresh subagents, parallel delegation when independent ready jobs exist, independent review, file/search/shell, and project-dependent web/browser/network/runtime capabilities.

## Resolution ladder
`NATIVE_VERIFIED → EXISTING_PROJECT_VERIFIED → EXISTING_EXTERNAL_VERIFIED → CURRENT RESEARCH → SAFE PROJECT-LOCAL INSTALL → REGISTER/RELOAD/RESTART IF NEEDED → SMOKE TEST → LOCK/RECORD → READY/BLOCK`

For a missing required Pi capability:
1. search current official Pi docs/package registry and inspect candidate provenance, maintenance, license, permissions and compatibility;
2. prefer project-local installation when the capability is project-specific; preserve user/global config;
3. do not hardcode a package version in the methodology; record the actually resolved package/source/version after installation;
4. remember Pi packages/extensions execute with the user's permissions and Project Trust is a deliberate security boundary;
5. after install, use a documented in-session reload mechanism if available and safe, then re-inventory/smoke-test the capability;
6. if the new capability cannot be made active in the current Pi process, persist all state and set `RESTART_REQUIRED`; output the exact restart/resume action to the operator; after restart resume from disk and rerun preflight rather than planning again.

Project Trust changes that are not active in the current process are handled the same way: do not bypass trust; request the minimal trust/restart action only when needed.

## Parallel capability proof
Presence of a Goal verifier does not prove general delegation. When parallel delegation is required, prove at least two isolated trivial read-only children can overlap and return independently, then record effective concurrency/settings exposed by the active provider. Use worktree/cwd isolation for concurrent writers where supported.


## Codex capability bootstrap
When Codex CLI is active, research current OpenAI/Codex documentation before assuming install/config/plugin details. Verify project instructions/skills, file/shell/Git, sandbox/approval, isolation, delegation/parallelism and required MCP/browser/network surfaces. Prefer Codex-native capabilities. Install a compatible extension/plugin only when a required capability is genuinely absent, then reload/restart/reverify and record provider/version. Model-class routing is part of execution capability resolution when supported; never invent an unavailable model id.

## Conditional execution isolation
Before running unfamiliar repository scripts, dependency installers, generated executables or risky integration experiments, assess whether the active harness sandbox/container/worktree can isolate the operation. Prefer existing safe isolation when material; do not impose Docker or another sandbox when risk does not justify it.

## V5.9 delegation capability matching
Capability resolution now applies **per delegated job** as well as per harness. A job declares required capabilities and the orchestrator proves the selected worker exposes them before dispatch. Long-running/expensive delegation should prefer observable progress, cancellation and resumable session/checkpoint capabilities when available. Do not pin a provider merely to obtain these; resolve current supported capability at runtime and never bypass Project Trust/security policy.


## V5.9 provider resolver
Use `config/TOOL-CAPABILITY-CATALOG.yaml`, `config/TOOL-SELECTION-POLICY.yaml`, `planning/execution/CAPABILITY-STATE.json` and `TOOL-LOCK.json`. Safe installation is autonomous when all policy conditions are satisfied; do not ask the user merely to install a project-local free tool. CRW/Obscura/Playwright mappings are provider candidates, never mandatory dependencies. Graphify is the preferred code-intelligence provider for non-trivial codebases, but host-wide installation is a special explicit-consent boundary; use `scripts/graphify_ctl.py prepare`.
