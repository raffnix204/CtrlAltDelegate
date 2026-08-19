# Full-Lifecycle Entry & Mode Detection — V5.7.1

## Purpose

The GitHub Native Edition is a complete CtrlAltDelegate runtime. A Custom GPT handoff is optional, never a prerequisite. The same repository can start from an idea, resume partial planning, consume an execution-ready handoff, or resume interrupted implementation.

The agent must reconstruct lifecycle state from Git plus the versioned `planning/` tree instead of assuming a prior chat or planner exists.

## Startup invariant

Always begin with:

`PERSISTED_STATE_READ → MODE_DETECTION → HARNESS_READY → PROJECT/REPO/SOURCE_READY → EARLIEST_UNRESOLVED_GATE`

Do not enter broad implementation merely because `AUTOPILOT-GOAL.md` exists. Do not restart completed discovery merely because a new agent/session opened.

## Lifecycle modes

Exactly one effective mode is selected from persisted evidence.

### `FULL_LIFECYCLE`

Use when no authoritative planning baseline exists or discovery is `NOT_READY`/not meaningfully started.

Continue:

`INTAKE → COLLABORATIVE_DISCOVERY → PREFERENCES_CONSTRAINTS_READY → DISCOVERY_READY → RESEARCH_READY → STACK_READY → ARCHITECTURE_READY → PROGRAM_DESIGN_READY → SKILLSET_READY → EXECUTION_RIGHTSIZING_GATE → EXECUTION_DAG_READY → DELIVERY_READY → EXECUTION`

In GitHub-native standalone operation, `DELIVERY_READY` means the repository-local planning baseline is implementation-ready; no external ZIP or Custom GPT transfer is required.

### `RESUME_PLANNING`

Use when some planning gates are complete but the execution baseline is not ready.

Resume the earliest materially unresolved gate. Preserve resolved facts, accepted/rejected product decisions, `REQUIRED` constraints, current evidence and valid ADRs. Do not repeat discovery questions whose answers are already persisted.

### `EXECUTION_HANDOFF`

Use when an implementation-ready baseline exists, including a Custom-GPT delivery or a planning-only coding-agent session.

Validate the baseline against current Git/repository/runtime facts, invalidate only contradicted artifacts, then execute. Do not broadly re-plan an already coherent handoff.

### `RESUME_EXECUTION`

Use when persisted state shows active/completed jobs, waves, candidate/runtime SHAs, blockers, restart state or another concrete next execution action.

Reconcile actual Git/runtime/evidence with `STATE.md`; resume the exact dependency-ready action. Never restart the project from discovery unless evidence proves the planning baseline itself became materially invalid.

## Mode detection evidence

Use, in order:

1. actual Git/repository/runtime state;
2. `planning/execution/STATE.md`;
3. `planning/discovery/DISCOVERY-STATE.md` and `TECHNICAL-PREFERENCES.yaml`;
4. requirements, research register, ADRs and program design;
5. `STACK-MANIFEST.yaml`, `SKILLS-MANIFEST.yaml` and execution DAG/jobs;
6. handoff metadata when present.

Conversation history is not authoritative state.

## Decision table

| Persisted evidence | Mode | Next behavior |
|---|---|---|
| Fresh/`NOT_STARTED`; discovery `NOT_READY` | `FULL_LIFECYCLE` | start collaborative discovery before consequential architecture/code |
| Discovery/requirements partially resolved; DAG not ready | `RESUME_PLANNING` | continue earliest unresolved planning gate |
| Planning baseline complete; no execution progress | `EXECUTION_HANDOFF` | validate baseline, then enter execution |
| Jobs/waves/execution state already progressed | `RESUME_EXECUTION` | reconcile and resume exact next action |

When evidence is mixed, choose the earliest unresolved **material** gate rather than guessing from filenames alone.

## Planning invariants

- A fresh standalone checkout must not require `planning/handoff/CODING-AGENT-HANDOFF.md` to begin discovery.
- A Custom GPT is an optional planning UI and an authoritative planning input only when its artifacts are actually present.
- `REQUIRED` constraints are user-owned and cannot be silently overridden.
- `PREFERRED` constraints are strong defaults; evidence may justify deviation.
- `AUTO` explicitly delegates the decision to the planner/agent.
- Consequential stack/hosting/security decisions require current evidence proportional to uncertainty and blast radius.
- Brownfield repositories are inspected before architecture changes; proven architecture is preserved unless requirements/evidence justify change.
- Program design and execution rightsizing occur before broad implementation when material.

## Execution transition

Execution may start only after the required planning gates for the task are ready. The depth is adaptive: MICRO/SMALL work does not require large-project ceremony, but it still needs enough resolved intent, constraints, repository understanding and verification shape to avoid speculative coding.

At transition, persist at least:

- resolved product objective and acceptance;
- relevant constraints/preferences;
- repository baseline/current state;
- selected/detected stack;
- material architecture/program-design decisions;
- project-selected skills and job-level routing rules;
- execution profile and dependency-ready work;
- verification/evidence expectations.

## Handoff semantics

`planning/handoff/FINAL-START-PROMPT.md` is specifically an **execution-ready handoff prompt**. It intentionally says not to re-plan from scratch. It is correct for `EXECUTION_HANDOFF` and resume scenarios, but it is not the primary prompt for a fresh standalone `FULL_LIFECYCLE` checkout.

The human-facing standalone entry is root `START-HERE.md`.

## Completion

All four modes converge into the same execution, verification, documentation, Git/GitHub and runtime contracts. The terminal state remains `COMPLETED`; mode selection changes only where the lifecycle begins or resumes.
