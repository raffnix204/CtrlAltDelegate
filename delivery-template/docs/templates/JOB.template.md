# JOB-XXX: <name>

## Objective

## Requirement IDs

## Dependencies
Use `IMPLEMENTATION` by default so downstream construction can continue after an upstream job reaches `IMPLEMENTED_UNVERIFIED`. Use `VERIFIED` only when consuming the dependency before real verification would be unsafe or meaningless.


## Consumes

## Produces

## Allowed Scope

## Protected Scope

## Risk Class
LOW / STANDARD / HIGH

## Execution Profile / Job Size
Project profile: `MICRO | SMALL | STANDARD | HIGH_RISK`. Job size: `MICRO | BOUNDED | SUBSTANTIVE`. Do not fragment a SMALL project into many micro-jobs.

## Required Worker Capabilities
List only capabilities this job actually needs (for example write/shell/Git/web/browser/runtime/device). Dispatch only after capability match is verified.

## Change Triggers

## Cross-Job Seams
`NONE` or named concern.

## Required Skills
List **only** job-relevant skills with exact canonical paths.

- `<skill-id>` → `.agents/skills/<skill-id>/SKILL.md` — why required

The delegated worker must read these files before work and return `SKILLS_APPLIED`.

## Program Design
`INLINE | planning/architecture/PROGRAM-DESIGN.md#<section> | NOT_MATERIAL`
State consequential files/modules, public contracts/call flow/test shape and first executable vertical slice when material.

## Solution Minimization
Record selected rung/evidence/rejected unnecessary surfaces. Substantive implementation must load `solution-minimization-engineering`.

## Implementation Requirements

## Acceptance Criteria
- [ ] ...

## Required Tests / Evidence
For each material test/evidence item, state the production defect/risk it can falsify and whether it must be fresh on the job/wave candidate SHA. For confirmed bugfixes, specify the practical `PRE_FIX_FAIL → POST_FIX_PASS` proof path.

## Measurable Outcome
`NONE` or the observable product/NFR metric, baseline, target/acceptance rule and measurement method. Never invent a proxy when categorical correctness is the real requirement.

## Failure-Mode Closure
`NOT_TRIGGERED` initially. If this job resolves an escaped defect/incident/repeated failure, record the smallest durable recurrence protection added or why no additional protection is justified.

## Validation Commands

## Runtime Impact

## Git / Worktree Policy

## Worker Liveness / Recovery
For long-running/expensive work, state the progress signal and checkpoint strategy. Elapsed wall-clock time alone is not stall evidence. On provider loss, reconcile Git/files/checkpoint and resume the next safe step instead of restarting completed work.

## Handoff / Worker Return

```text
STATUS: IMPLEMENTED | VERIFYING | BLOCKED
SKILLS_APPLIED: ...
implementation_status: COMPLETE | PARTIAL
verification_status: PASS | PENDING_EXTERNAL | FAIL | NOT_APPLICABLE
blocker_class: NONE | VERIFICATION_BLOCKER | EXECUTION_BLOCKER
critical findings/evidence: ...
report: ...
```

## Evidence Granularity
For MICRO/SMALL profiles, prefer coherent milestone evidence that can legitimately support multiple Requirement IDs rather than one ceremony record/commit per requirement.

## Documentation Impact
`NONE | USER | INSTALLATION | CONFIGURATION | API | MIGRATION | OPERATOR | SECURITY | RELEASE` with affected canonical doc paths.

## Context Policy
`FRESH` by default; inherited/forked context requires a concrete reason.

## Parallelism
Conflict domains, isolation/worktree/cwd, current system bottleneck, and explicit serialization/throttling reason if another ready job exists but this job is not dispatched concurrently. Avoid writer WIP that only queues ahead of saturated integration/test/CI/review/runtime capacity.

## Convergence Mapping
Requirement IDs → code paths → evidence IDs → documentation paths/status.
