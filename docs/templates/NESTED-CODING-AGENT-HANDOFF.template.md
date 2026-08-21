# Coding Agent Handoff — CtrlAltDelegate V5.8.1 Imported Control Package

## Operating roots

The coding agent runs from the actual target project/repository root.

- `PROJECT_ROOT=.`
- `INBOUND_PACKAGE=./ctrlaltdelegate-delivery.zip`
- `CONTROL_ROOT=./.ctrlaltdelegate`
- `PLANNING_ROOT=./.ctrlaltdelegate/planning`
- `SKILLS_ROOT=./.ctrlaltdelegate/.agents/skills`

Application code belongs in `PROJECT_ROOT` outside `CONTROL_ROOT`. CtrlAltDelegate planning, control state, evidence indexes, selected skills and private runtime state belong under `CONTROL_ROOT`.

## Entry contract

This is an execution-ready planning handoff. Import the ZIP safely, verify `HANDOFF-STATUS.yaml` is `READY`, verify the planning baseline attestation, then continue from the exact persisted state. Do not restart broad discovery unless repository/runtime evidence invalidates a material planning assumption.

Default control visibility is `LOCAL_PRIVATE`. Preserve the target repository's `.gitignore` and ensure the inbound archive, control root and temporary import siblings remain ignored. Do not publish private/raw/runtime CtrlAltDelegate state unless the user explicitly selects a curated shared-planning policy.

## Control-plane execution

Use the V5.8.1 canonical control surfaces:

- `planning/execution/JOB-GRAPH.json` for dependency/ready/claim state;
- `planning/execution/LOOP-STATE.json` plus `config/LOOP-CONTRACTS.yaml` for closed-loop state and anti-thrashing;
- `planning/execution/DECISION-LEDGER.jsonl` for material autonomous rulings;
- `planning/execution/ARTIFACT-CONSISTENCY.json` for requirements/planning consistency findings;
- `config/SURFACE-POLICY.yaml` for instruction-versus-enforcement and protected surfaces;
- `config/HARNESS-CONFORMANCE.yaml` for capability negotiation;
- `planning/execution/PENDING-INPUT.jsonl` for mid-run user input reconciliation;
- `planning/execution/PLANNING-BASELINE.json` for accepted-plan drift detection.

Load only the exact `.agents/skills/<id>/SKILL.md` bodies and progressive references required by the active job.

## Worker and recovery contract

Delegate only when useful. Match job-required capabilities to verified harness/worker capabilities; fail loud or reroute when a required capability is unsupported. Bound each worker by allowed scope, prohibited scope, permission class, done-when conditions and evidence requirements. A worker report is a claim until integrated and verified.

Before retrying a loop, compare progress signatures. Repeated failure with no new evidence, meaningful diff or state advance requires a strategy change, fresh debugger, job resize, reroute or scoped replan rather than a blind retry.

Persist state before restart/context reset and reconstruct from disk on resume. New user input is classified at safe boundaries and invalidates only affected planning/execution state.

## Completion

Continue through implementation, targeted and acceptance verification, evidence refresh, documentation, safe Git/GitHub integration and convergence until `COMPLETED`. Do not declare completion from worker success alone. Ask the user only for a contract-defined business/product/safety/external hard stop.


## V5.8.1 specialist-planning authority
Read `$CONTROL_ROOT/planning/context/PLANNING-SKILL-STATE.yaml` before implementation. The planning baseline may contain specialist-produced design, SEO, data, security, content or other domain artifacts. Preserve their resolved decisions unless current repository/runtime evidence materially contradicts them. Approved files under `$CONTROL_ROOT/planning/content/pages/` are authoritative copy and must not be casually rewritten.

## V5.8.1 assurance and debug integrity
Read `planning/execution/ASSURANCE-STATE.yaml` and `config/ASSURANCE-PROFILES.yaml`. Work size and assurance depth are independent. For substantive bug repair, derive a behavioral oracle from authoritative observed behavior and use `planning/execution/ROOT-CAUSE-DEPTH.json` when a symptom-layer fix could hide a deeper cause. High-assurance acceptance must be author-independent; parallel assurance verdicts remain blind when required. Delegated workers verify hash-bound authority pointers and return `STALE_BRIEF` rather than executing stale planning state.
