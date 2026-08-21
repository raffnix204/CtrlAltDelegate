# Adaptive Execution & Worker Liveness — V5.8.1

## Purpose

V5.8.1 right-sizes orchestration to the actual project and prevents useful long-running subagents from being killed merely because an arbitrary wall-clock duration elapsed.

Quality requirements remain requirement/risk-driven. **Process ceremony is not a quality metric.**

## 1. Execution Rightsizing Gate

Before finalizing the implementation DAG, classify the project/run:

`DISCOVERY/STACK/PROGRAM DESIGN → EXECUTION_RIGHTSIZING_GATE → MICRO | SMALL | STANDARD | HIGH_RISK`

Use scope, coupling, number of independently testable capabilities, deployment/runtime complexity, migration/data sensitivity, security/privacy exposure, reversibility, operational blast radius and verification cost. Do not classify from requirement count, LOC guesses or skill-library breadth alone.

### MICRO
A bounded change or tiny project with low coupling/risk.
- one coherent implementation unit or milestone;
- avoid subagent fan-out unless a specialist/reviewer is materially useful;
- no branch/worktree per microtask;
- self-review + decisive targeted checks; independent review only on a risk trigger;
- one coherent commit/checkpoint where repository policy allows;
- convergence still covers all mandatory requirements, but one evidence item may support several requirements.

### SMALL
A compact product such as a small website/internal tool with a few real capabilities.
- usually 2–4 executable vertical-slice milestones rather than many micro-jobs;
- one feature/integration branch is normally enough when parallel writers are unnecessary;
- batch same-shape work; use subagents only when startup/context/isolation cost is justified by saved wall time or expertise;
- milestone evidence and targeted review; one fresh final/release review plus triggered specialist reviews;
- commit/push at coherent milestones, not after every tiny task;
- preserve full final QA, security, accessibility, documentation and runtime acceptance required by the product.

### STANDARD
Normal multi-capability application/system.
- dependency DAG and waves;
- selective parallel writers with isolation;
- job/wave evidence and fresh independent review for substantive work;
- standard convergence, documentation and runtime gates.

### HIGH_RISK
Security/data-loss/compliance/critical migration/network lockout/distributed-state or similarly high-consequence work.
- explicit rollback/recovery and risk evidence;
- stronger independent review and isolation;
- finer-grained checkpoints when they reduce blast radius;
- do not relax gates merely because the code diff is small.

Profiles are defaults, not ceilings. A SMALL project may contain one HIGH-risk job; route that job at the stricter risk level without inflating every unrelated task.

## 2. Skill Rightsizing

Project-selected skills are a routing candidate pool, not worker context.

`PROJECT-RELEVANT → JOB CHANGE/RISK TRIGGERS → SMALLEST COMPLETE JOB SET → WORKER`

Never target a fixed number of skills. A small job often needs only a handful; a complex security/network/data job may legitimately need more. Unrelated skills must not be loaded merely because they were relevant elsewhere in the project.

## 3. Delegation Capability Gate

Before dispatch, compare the job's required capabilities with the actual worker/provider surface. Examples: filesystem/write, shell, Git, web research, browser, semantic navigation, isolated cwd/worktree, runtime/device access.

`JOB REQUIRED CAPABILITIES ⊆ WORKER VERIFIED CAPABILITIES`

If not, route to a capable worker/provider or bootstrap the missing supported capability under `CAPABILITY-BOOTSTRAP.md`. Do not discover after dispatch that a researcher has no web tool.

## 4. Progress-aware worker lease

A static wall-clock duration is **not** evidence that a worker is stalled.

Worker liveness states:
- `RUNNING` — recent observable progress;
- `QUIET` — no recent progress signal, but no evidence of failure yet;
- `STALLED` — health check shows no meaningful progress and recovery action is justified;
- `BLOCKED` — worker reports an external/dependency/policy blocker;
- `DONE` — terminal success/return;
- `FAILED` — terminal worker/provider failure.

Progress may be demonstrated by provider/onUpdate events, tool completion/output, test/build output, new/modified scoped artifacts, checkpoint updates, or another harness-native signal. Merely repeating the same text/tool failure does not renew a lease indefinitely.

Policy:
1. while meaningful progress is observed, renew/continue the worker lease;
2. when progress becomes quiet, perform a health check before cancellation;
3. do not cancel solely because an arbitrary elapsed duration was reached;
4. if an external provider imposes a hard deadline, checkpoint before it when feasible and resume afterward rather than restarting blindly;
5. cancellation remains immediate for explicit user/policy/safety requests or destructive runaway behavior.

No universal numeric timeout is encoded in the methodology. Harness/provider constraints are discovered at runtime and recorded.

## 5. Checkpoint and resume

Long-running or expensive jobs should persist the smallest resumable state under ignored runtime scratch, normally:

`planning/private/runs/<RUN_ID>/<JOB_ID>/worker-state.json`

Useful fields: job/baseline SHA, status, current step, completed steps, scoped changed files, decisive tests/evidence already run, last meaningful progress, blockers and exact next step. Never store secrets or full transcripts.

On worker loss:

`READ CHECKPOINT → VERIFY GIT/FILES → RECONCILE WHAT ACTUALLY EXISTS → RESUME NEXT SAFE STEP`

Do not repeat completed research/build/test work unless evidence is stale or uncertain.

`scripts/worker_checkpoint.py` is an optional harness-neutral helper for long jobs; native provider progress/session persistence is preferred when it already supplies equivalent capability.

## 6. Stall and retry policy

A stalled worker is not automatically a failed solution.
- first determine whether it is computing, blocked on a long command, awaiting external I/O, rate-limited, deadlocked or looping;
- preserve partial useful work before termination where safe;
- resume the same job from checkpoint when the approach remains sound;
- invoke a fresh debugger/replan only after evidence shows the approach or state is bad;
- repeated identical stalls/failures trigger job resizing, capability rerouting or root-cause debugging rather than blind restart loops.

## 7. Review/evidence/commit right-sizing

For MICRO/SMALL work, avoid process-only churn:
- one evidence record may support several requirements when it genuinely proves them;
- bind/attest evidence at meaningful milestone/final candidates rather than creating a ceremony commit for every requirement;
- reviewers inspect worker evidence and actual diff, then reproduce the smallest decisive sample/risk checks instead of re-performing the entire job by default;
- full independent re-verification remains mandatory where risk/uncertainty requires it;
- documentation changes stay in the same coherent product commit when possible.

Evidence freshness and convergence semantics remain unchanged: batching evidence does not permit stale or missing proof.

## 8. Throughput rule

Optimize **time to validated user value**, not agent utilization, token consumption, number of jobs or number of commits.

Parallelize only when:
- work is dependency-ready and behaviorally independent;
- isolation is safe;
- dispatch/context overhead is smaller than expected time saved;
- the downstream bottleneck can absorb the work.

Otherwise batch or serialize deliberately and record the reason when required by the profile.

## V5.8.1 separate assurance axis
`MICRO|SMALL|STANDARD|HIGH_RISK` describes orchestration size/cost. `NORMAL|ELEVATED|HIGH|CRITICAL` describes assurance depth. A tiny but security- or data-critical change may remain SMALL while receiving HIGH assurance. Do not inflate unrelated implementation ceremony to satisfy assurance; strengthen independence and evidence instead.
