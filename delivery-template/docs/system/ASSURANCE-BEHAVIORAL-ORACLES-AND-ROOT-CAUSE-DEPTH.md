# Assurance, Behavioral Oracles & Root-Cause Depth — V5.8

## Purpose

V5.8 strengthens debugging and verification without imposing one testing style on every domain. The core rule is: **verify the behavior independently, diagnose the deepest responsible boundary before repair, and do not let the author grade its own work.**

## 1. Behavioral oracle

For a confirmed defect or behavior-changing requirement, derive the acceptance oracle from observable behavior, requirements, issue text, protocol/specification, or other authoritative evidence — not from the proposed patch.

`BEHAVIORAL_ORACLE != IMPLEMENTATION_ORACLE`

A regression check should remain valid if the implementation strategy changes. Tests that merely assert the proposed mechanism exists are insufficient unless that mechanism is itself the public contract.

Persist, when applicable:
- authoritative behavior statement;
- minimal reproducible input/state;
- expected result;
- actual baseline result;
- exact runner/command/environment;
- oracle authority and evidence pointer.

## 2. Root-cause depth gate

For substantive bug repair, run `ROOT_CAUSE_DEPTH_GATE` before implementation when a symptom-layer patch could plausibly hide a deeper defect.

Record:
1. `behavior_home` — where the behavior is actually decided;
2. `input_state_classes` — relevant branches/states/invariants, including the failure-revealing class;
3. `deepest_responsible_cause` — the deepest boundary whose correction resolves the class, not merely the visible symptom;
4. `behavioral_oracle` — independently derived and, where safe/practical, demonstrated failing on the baseline;
5. `proposed_fix_boundary`;
6. `depth_match` — whether the proposed repair acts at the responsible boundary or has a justified safer boundary.

A `depth_match: false` result blocks implementation until the diagnosis is repaired, narrowed, or a documented exception proves why the deeper boundary must not be changed.

Do not force this ceremony onto trivial typo/config/content fixes with no plausible deeper execution cause.

## 3. Independent assurance

Assurance has independent dimensions:
- `author_independent`: reviewer/verifier did not author the candidate;
- `sibling_verdict_blind`: concurrent assurance workers do not receive one another's verdicts before reporting;
- `candidate_claims_untrusted`: author success claims are context, never proof;
- `raw_evidence_first`: verifier can inspect the candidate, authoritative requirements and raw execution evidence directly.

High-assurance work should use fresh isolated context where the harness supports it. A worker that authored a change must never be the sole acceptance authority for that change.

## 4. Separate work size from assurance depth

Execution size and assurance depth are independent axes.

Work size remains `MICRO | SMALL | STANDARD | HIGH_RISK` for orchestration cost. Assurance is `NORMAL | ELEVATED | HIGH | CRITICAL` and is derived from consequence, reversibility, security/privacy/data impact, hidden-state/concurrency risk, migration blast radius, external contract exposure and evidence difficulty.

A tiny diff in authentication, authorization, money movement, destructive data logic or network lockout may be `SMALL` work with `HIGH` or `CRITICAL` assurance.

Assurance depth changes verification independence and evidence strength; it does not authorize unnecessary implementation ceremony.

## 5. Scoped assurance repair

On an assurance failure:
- preserve accepted evidence that is still bound to unchanged artifacts/state;
- invalidate only affected claims/evidence and downstream dependents;
- repair the named defect or diagnosis;
- regenerate stale evidence;
- do not restart an entire successful wave unless the failure invalidates its shared premise.

## 6. Completion

A bug-fix claim is complete only when the behavior oracle passes on the candidate and the relevant baseline/failure evidence is credible. For root-cause-gated work, the recorded cause/fix boundary must reconcile. For elevated assurance, all required independent verdicts must be collected before acceptance.
