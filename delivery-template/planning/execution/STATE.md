# Execution State

Status: NOT_STARTED
Lifecycle Stage: BOOTSTRAP
Lifecycle Mode: AUTO_DETECT
Planning Source: AUTO_DETECT
Last Updated: UNKNOWN

Harness: AUTO_DETECT
Harness Readiness: NOT_READY
Git Guards Readiness: NOT_READY
Documentation Readiness: NOT_READY
Context Epoch: 1
Parallelism Readiness: NOT_MEASURED
Execution Profile: AUTO / NOT_CLASSIFIED
Worker Liveness: IDLE
Current Bottleneck: UNKNOWN
Restart Required: NO

Project Mode: AUTO
Repository Intake: NOT_STARTED
Repository Baseline SHA: UNKNOWN
Repository Readiness: NOT_READY
Preferences / Constraints Readiness: NOT_READY
Discovery Readiness: NOT_READY
Planning Skill Readiness: NOT_READY
Research Readiness: NOT_READY
Stack Readiness: NOT_READY
Architecture Readiness: NOT_READY
Program Design Readiness: NOT_EVALUATED
Skillset Readiness: NOT_READY
Execution DAG Readiness: NOT_READY
Execution Handoff Readiness: NOT_READY

Repository URL: DISCOVER_FROM_GIT_REMOTE
Current Branch: UNKNOWN
Main SHA: UNKNOWN
Candidate SHA: UNKNOWN
Runtime SHA: UNKNOWN
User-Reachable Test URL: UNKNOWN

Current Wave: NONE
Active Jobs: NONE
Completed Jobs: NONE
Blocked Jobs: NONE
Convergence Status: NOT_EVALUATED
Evidence Status: NOT_EVALUATED

## Next action
Read `AGENTS.md`, inspect actual Git/repository state and this persisted planning tree, then run lifecycle mode detection. If discovery is `NOT_READY`, enter `FULL_LIFECYCLE` and run the early capability scan, load relevant planning specialists, then start/resume collaborative discovery before consequential architecture or implementation. If planning or execution already progressed, resume the earliest unresolved material gate or exact persisted execution action without repeating completed work. Read `planning/handoff/CODING-AGENT-HANDOFF.md` as the primary execution entry only when an execution-ready handoff exists.

## Persistence rule
Update this compact snapshot after every meaningful planning gate, job, integrated wave, material commit/push, runtime apply, blocker/hard-stop, restart/resume, context epoch and convergence/evidence verdict. Put detailed history in `execution-ledger.md`, not here.

- Loop State: `planning/execution/LOOP-STATE.json`
- Job Graph: `planning/execution/JOB-GRAPH.json`
- Surface Policy: `config/SURFACE-POLICY.yaml`
- Planning Skill State: `planning/context/PLANNING-SKILL-STATE.yaml`
- Harness Conformance: `config/HARNESS-CONFORMANCE.yaml`
