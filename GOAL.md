# GOAL — V5.8.1

## Project mode
`AUTO`

Allowed: NEW_BUILD / EXISTING_CONTINUE / AUDIT_ONLY / AUDIT_REMEDIATE / BUGFIX / SECURITY_HARDEN / FRONTEND_UPGRADE / SEO_OPTIMIZE / WEBSITE_MODERNIZE / INFRA_NETWORK / DATA_AI

## Product / technical objective
`DESCRIBE_OR_INFER_FROM_PROJECT`

## Coding harness
`AUTO_DETECT` — Pi is preferred reference harness; Codex/Claude Code/OpenCode supported.

## GitHub
Repository slug: `AUTO_FROM_PROJECT`
Owner: `AUTHENTICATED_ACCOUNT`
Visibility: `PRIVATE_UNLESS_EXPLICITLY_PUBLIC`
Remote policy: `REUSE_EXISTING_ELSE_CREATE`
Sync policy: `COMMIT_JOB_CHECKPOINTS_PUSH_WAVES_AND_VALIDATED_MAIN`
Branch policy: `RESPECT_EXISTING_PROTECTION_AND_PR_RULES`

## Existing repository objective
Requested change/audit/bug: `AUTO/NONE`
Architecture: `PRESERVE_UNLESS_JUSTIFIED`
Known baseline failures: `UNKNOWN`

## Planning baseline
Lifecycle mode: `AUTO_DETECT_FROM_GIT_AND_PLANNING_STATE`
Existing authoritative planning: `USE_IF_PRESENT_UNLESS_REPO_RUNTIME_CONTRADICTS`
No planning baseline: `RUN_FULL_COLLABORATIVE_LIFECYCLE_FROM_INTAKE`
Partial planning: `RESUME_EARLIEST_UNRESOLVED_MATERIAL_GATE`
Custom-GPT planning/research: `OPTIONAL_AUTHORITATIVE_INPUT_WHEN_PRESENT`
Execution research: `JIT_ONLY_AFTER_REUSING_CURRENT_PLANNING_EVIDENCE`
Research modes: `NONE | VERIFY_DRIFT | TARGETED | SPIKE`
Routine technical decisions after evidence: `AUTONOMOUS`

## Web acquisition
Required capabilities: `AUTO`
Provider: `USE_EXISTING_COMPATIBLE_CAPABILITY_FIRST`
Examples: existing self-hosted Firecrawl / Firecrawl-compatible MCP/API / harness-native web tools.
Browser: `USE_FOR_INTERACTION_JS_AUTH_VISUAL_ACCEPTANCE_NOT_DEFAULT_BULK_CRAWLER`

## Data / local-first
SQLite: `FIRST_CLASS_WHEN_FIT`
SQLite vector search: `AUTO_SELECT_CURRENT_SUPPORTED_EXTENSION_AND_VERIFY`
Remote DB required: `ONLY_IF_REQUIREMENTS_JUSTIFY`

## Network / infrastructure
Network platforms: `AUTO`
Management safety: `PRESERVE_REACHABILITY_WITH_BACKUP_CANARY_ROLLBACK`
Vendor-specific specialists: `ROUTE_ONLY_WHEN_ACTUAL_PLATFORM_MATCHES`

## Execution
Run `planning/execution/AUTOPILOT-GOAL.md` autonomously until `COMPLETED`.


## Documentation / context / parallelism
Documentation policy: `EVERY_COMMIT_AND_PUSH_CONSISTENT_BEGINNER_FIRST`
README feature coverage: `ALL_MAJOR_CURRENT_USER_CAPABILITIES_DISCOVERABLE`
Context policy: `FRESH_INDEPENDENT_WORKERS_REVIEWERS_CONTEXT_EPOCHS`
Parallel policy: `MAXIMIZE_END_TO_END_THROUGHPUT_BOTTLENECK_AWARE_NO_FIXED_AGENT_COUNT`
Model policy: `USE_OPERATOR_OR_HARNESS_SELECTION_UNCHANGED`
Capability activation: `INSTALL_IF_REQUIRED_THEN_RELOAD_OR_RESTART_REQUIRED`


## V5.8.1 planning / state / execution flow
Planning root: `planning/` — persistent, versioned, never globally gitignored.
Current state: `planning/execution/STATE.md` — update after meaningful execution boundaries.
Program design: `LIGHTEST_SUFFICIENT_BEFORE_BROAD_SUBSTANTIVE_IMPLEMENTATION`
Implementation shape: `VERTICAL_SLICE_FIRST_WHEN_DEPENDENCIES_ALLOW`
Bug regression proof: `PRE_FIX_FAIL_TO_POST_FIX_PASS_WHEN_PRACTICAL`
Failure closure: `DURABLE_MINIMUM_CONTROL_AFTER_ESCAPED_OR_REPEATED_FAILURE`
Measurable outcomes: `USE_WHEN_HONEST_AND_DECISION_RELEVANT`


V5.8.1 planning baseline includes `planning/discovery/` preference/constraint state; preserve resolved constraints during execution.


## Language / interaction
Conversation: `FOLLOW_USER_LANGUAGE_UNLESS_EXPLICITLY_OVERRIDDEN`
System/planning artifacts: `ENGLISH`
Localized product content: `ONLY_WHEN_PROJECT_REQUIRES`


## V5.8.1 control surfaces
Use the canonical loop registry/state, machine-readable job graph, surface policy, decision ledger, artifact-consistency gate and harness-conformance profile. For Custom-GPT ZIP handoffs, import to `./.ctrlaltdelegate/` under `LOCAL_PRIVATE` Git visibility before execution.


## V5.8.1 skill-driven planning

Relevant specialist skills participate while planning decisions are made, not only after planning. Run an early capability scan during intake/discovery, consult the smallest complete planning skill set for the current phase, persist consultations in `planning/context/PLANNING-SKILL-STATE.yaml`, and refresh routing whenever scope, research or stack evidence changes. Use `config/PLANNING-SKILL-ROUTING.yaml` and `docs/system/SKILL-DRIVEN-PLANNING.md`. The final coding-agent skill pool continues from these decisions.

V5.8.1 runtime skill escalation: if a worker discovers missing expertise, use `config/SKILL-ESCALATION-POLICY.yaml`; L0/L1 do not imply full replanning, while semantic changes escalate to rebrief/change control.
