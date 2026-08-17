# Coding-Agent Start Prompt — Nested CtrlAltDelegate Handoff

Work from the target project's root directory. The completed CtrlAltDelegate planning/control package is installed at `./ctrlaltdelegate/`.

Set and preserve these path meanings:
- `PROJECT_ROOT` = the current target project/repository root;
- `CONTROL_ROOT` = `./ctrlaltdelegate`;
- `PLANNING_ROOT` = `./ctrlaltdelegate/planning`;
- `SKILLS_ROOT` = `./ctrlaltdelegate/.agents/skills`.

Do not treat `CONTROL_ROOT` as the application repository root. Implement product code in `PROJECT_ROOT` according to the approved plan and selected stack. Keep CtrlAltDelegate-owned planning/state/evidence under `CONTROL_ROOT` unless an explicit safe integration step says otherwise.

Read in this order:
1. `./ctrlaltdelegate/AGENTS.md`;
2. `./ctrlaltdelegate/planning/handoff/HANDOFF-STATUS.yaml`;
3. `./ctrlaltdelegate/planning/handoff/CODING-AGENT-HANDOFF.md`;
4. `./ctrlaltdelegate/planning/execution/STATE.md`;
5. only the additional requirements, architecture, jobs, ADRs, research and routed skills needed for the immediate next action.

Require `HANDOFF-STATUS.yaml` to report `status: READY`, `mode: EXECUTION_HANDOFF`, `control_root: ./ctrlaltdelegate`, and zero unresolved blocking decisions. If the package is missing, incomplete, or internally inconsistent, stop with `BLOCKED_DELIVERY_INCOMPLETE` and report the exact missing/inconsistent path instead of guessing a different directory layout.

Treat the completed planning baseline as authoritative unless actual repository/runtime evidence materially contradicts it. Do not restart broad discovery or planning from scratch. Preserve resolved `REQUIRED` constraints and honor `PREFERRED` choices unless evidence justifies a recorded deviation.

Reconcile the real project Git state from `PROJECT_ROOT`, run the required harness/capability preflight, load only the job-relevant skills from `SKILLS_ROOT`, and execute the approved plan through implementation, verification, documentation, Git/GitHub and `COMPLETED`. Continue automatically between dependency-ready jobs/waves. Ask the user only for a hard stop defined by the contract.
