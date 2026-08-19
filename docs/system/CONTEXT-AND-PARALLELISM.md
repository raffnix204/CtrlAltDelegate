# Context Freshness & Parallel Execution — V5.7.1

## Two independent goals
1. Prevent context rot by reconstructing truth from durable state and using fresh isolated agents.
2. Reduce wall-clock time by maximizing **safe useful concurrency** across dependency-ready independent work.

## Parallelism planning gate
For every wave, enumerate all dependency-ready jobs, identify the current end-to-end throughput bottleneck, build a conflict/seam map, partition jobs into parallel-safe groups, and dispatch safe groups concurrently **only while more work improves throughput rather than queueing in front of the bottleneck**. Serial execution of two ready behaviorally independent jobs is a scheduling defect unless justified by a recorded dependency/conflict/resource/bottleneck constraint.

Valid serialization/throttling reasons include unfinished dependency, shared contract not yet stabilized, same mutable files/state without isolation, migration ordering, exclusive runtime/device access, provider/harness concurrency cap, machine/resource pressure, saturated CI/test/review/integration/runtime capacity, or a named cross-job seam that must be resolved first.

Do not use a fixed number of agents. Determine `EFFECTIVE_CONCURRENCY` at runtime from the actual subagent provider, host resources, repository conflict graph, provider limits and workload type. Read-only research/exploration/review can fan out aggressively. Writers require isolated scopes/worktrees and non-overlapping conflict domains. Heavy build/test/device operations remain resource-aware.

## Fresh agent policy
Default every independent job/review/research task to a fresh context. The orchestrator is spawn-only where capable workers exist. Reviewers never inherit implementer reasoning. Repeated failure escalates to a fresh debugger. Recursive uncontrolled agent trees are avoided; the orchestrator owns the graph and integration.

## Context epochs
`planning/execution/CONTEXT-STATE.yaml` records the current epoch, hot surfaces and reset reason. After validated waves and other semantic boundaries persist state/evidence, increment epoch, compact/reset if supported, and reload only the minimal hot set. Goal persistence keeps the mission alive; it is not the memory store.

## Compact handoff
Workers return structured status, skill IDs applied, decisions, changed paths, tests/evidence, docs impact, commit SHA/report path and blockers. Long logs/transcripts stay on disk. The parent reads them only when evidence or a failure requires it.


## V5.7.1 Microtask batching
Parallelism is not "one agent per checkbox". Batch small same-shape jobs when they share skill set, files are easy to isolate, and a separate context would add more dispatch/review overhead than reasoning value. Keep independent substantive jobs parallel. Split a batch immediately if one item develops different risk, failure or seam behavior.

## Run-scoped scratch
Allocate a `RUN_ID` for long autonomous runs. Worker/reviewer scratch and bulky transient summaries live under ignored `planning/private/runs/<RUN_ID>/`; only compact decisions/evidence pointers are promoted to canonical STATE/ledger/convergence/evidence. New runs never trust old scratch.


## V5.7.1 Bottleneck-aware WIP control
`MAXIMIZE SAFE PARALLELISM` is subordinate to end-to-end delivery flow. Track `current_bottleneck` in `PARALLELISM-STATE.yaml` when it is material. If independent writer throughput exceeds integration/test/review/deployment throughput, cap or batch writers rather than accumulating unverified work. Reassess after the bottleneck moves.

## V5.7.1 dispatch-cost and liveness rule
Parallelism must also justify its own startup/context/integration overhead. MICRO/SMALL work may be faster and safer as one coherent worker/milestone even when theoretical fan-out exists. Parallelize only when expected end-to-end time saved exceeds dispatch/integration cost and downstream capacity can absorb results.

Worker lifetime is progress-aware, not based on a universal wall-clock timeout. Use native provider updates/session persistence where available; checkpoint expensive long work under ignored `planning/private/runs/` only when useful. Quiet is not stalled until a health check fails to find meaningful progress. Resume from actual state after provider loss instead of replaying completed work.
