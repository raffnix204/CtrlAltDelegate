# Final Coding-Agent Start Prompt — V5.8.1

Work from the root of this cloned repository. This prompt assumes an execution-ready planning handoff. Do not re-plan the project from scratch. For a fresh standalone `NOT_STARTED` checkout, use root `START-HERE.md` instead.

Read `AGENTS.md`, then `planning/handoff/CODING-AGENT-HANDOFF.md`, then `planning/execution/STATE.md`. Treat Git plus the versioned `planning/` tree as persistent project memory. Read only the additional requirements/architecture/jobs/skills required for the immediate next action.

Reach `HARNESS_READY`, `GIT_GUARDS_READY`, `GITHUB_READY`, repository/source readiness, `STACK_READY` and `SKILLSET_READY` using the active harness capabilities. Pi is the reference/golden-path harness, Codex CLI is first-class, and DeepSeek Harness is first-class preview while its actual capabilities must be detected. Do not route/switch/pin models. Reuse existing healthy capabilities; bootstrap only genuinely missing required capabilities with current supported mechanisms and persist `RESTART_REQUIRED` before any necessary harness restart.

Execute `planning/execution/AUTOPILOT-GOAL.md` autonomously until `COMPLETED`. Keep `planning/execution/STATE.md` concise and current after every meaningful job, integrated wave, material commit/push, runtime apply, blocker/hard-stop, restart/resume, context epoch and convergence/evidence verdict. Before a restart/context reset, persist the authoritative branch/SHA/runtime/evidence state and exact next action; resume from disk afterward.

For substantive work: satisfy the lightest sufficient `PROGRAM_DESIGN_GATE`, then `SOLUTION_MINIMIZATION_GATE`. Prefer repo reuse → stdlib/runtime → native platform/framework/DB → existing dependency → direct implementation → only then justified new dependency/abstraction. Prefer testable vertical slices over broad horizontal layer batches when dependencies allow: establish a minimal end-to-end path, verify it, then extend rules/edge cases incrementally. Re-steer after the first high-impact slice if actual code/runtime diverges from program design.

For confirmed bugfixes, when practical prove the regression with `PRE_FIX_FAIL → POST_FIX_PASS`. Tests must be falsifiable and expectations independently derived. After defects/incidents/repeated repairs, perform `FAILURE_MODE_CLOSURE`: add only the smallest durable protection that prevents the same class escaping again.

Before DAG execution, read `planning/execution/EXECUTION-PROFILE.yaml` and enforce `EXECUTION_RIGHTSIZING_GATE`: small/low-risk work gets fewer, larger coherent milestones and less branch/review/evidence ceremony; standard/high-risk work gets the depth it needs. Never reduce quality floors. Before delegation verify the worker actually has every required capability. For long-running workers, use progress-aware leases: meaningful progress keeps them alive; quiet requires a health check; elapsed wall-clock time alone is not stall evidence; checkpoint/resume before known provider deadlines or after worker loss instead of blindly restarting completed work.

At every wave perform bottleneck-aware parallel planning. Maximize safe concurrency only while it increases end-to-end throughput; do not create writer WIP in front of a slower integration/test/CI/review/runtime bottleneck. Batch tiny same-shape work, parallelize substantive independent jobs with safe isolation, and record any required serialization reason.

Maintain `planning/execution/CONVERGENCE-MATRIX.json` and SHA-bound `EVIDENCE-INDEX.json`. Use measurable product/NFR outcomes as execution backpressure wherever meaningful, without substituting proxy metrics for correctness/security/accessibility. Keep README and all affected canonical docs accurate for every commit/push; final user-facing deliverables require clean-room/fresh-user acceptance when practical.

Continue automatically between jobs/subagents/waves while dependency-ready work exists. Ask me only for a true product/business/safety/external hard stop defined by the project contract.


## Language continuity
Continue the conversation in the user's language unless explicitly requested otherwise. Keep CtrlAltDelegate-controlled planning, system, handoff and execution artifacts in English; preserve localized product content only where the project requires it.
