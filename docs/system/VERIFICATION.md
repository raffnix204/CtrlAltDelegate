# Verification System — V5.9

## Evidence before claims
Agent reports are claims. The orchestrator reproduces load-bearing checks on the exact candidate SHA/environment.

## Standard gates
Substantive jobs normally receive Spec Compliance + Code Quality plus change-triggered gates. Wave candidates then run project-level build/type/lint/test/integration checks.

## Change triggers
- API/shared schema/type → consumer + contract impact (`api-contracts`).
- DB migration → migration/data compatibility.
- Auth/security → negative authorization/security tests.
- Public UI → browser + responsive + accessibility; premium UI additionally screenshot/visual polish.
- Runtime/config → rebuild/restart/health/user-reachable URL.

## Premium UI evidence
For substantial UI, capture actual integrated render on representative mobile/laptop/wide sizes. Confirm fonts/assets, content states, navigation, overflow and console. Screenshot evidence does not replace accessibility/functional checks.

## Adversarial factual review
Use when high-risk/high-autonomy claims benefit from falsification. Never majority-vote taste/architecture judgment.

## Verdict
READY / READY_WITH_CAVEATS / NOT_READY.

Required failures cannot be hidden by skipping, weakening tests or raising thresholds without an authorized documented decision.


## Brownfield baseline verification
Persist baseline SHA and existing gate outcomes. Candidate failures are PRE_EXISTING / FIXED / NEW / ENVIRONMENT / UNKNOWN. NEW required failures block completion. Inspect enforcement-config/test changes for weakening. Audit remediation requires targeted findings to reach explicit terminal status with evidence.

## GitHub completion evidence
When GitHub sync is enabled, final evidence includes remote identity, final validated local main SHA, remote main SHA or equivalent verification, and proof required branch/PR checks were respected. Locally complete but unpushed work is incomplete.


## Documentation readiness
`DOCUMENTATION_READY` is a required final gate for distributable projects: root README is beginner-first and current, every major user-visible feature is discoverable, install/setup/config/usage examples match the candidate, affected API/migration/operator/security docs are synchronized, links/commands/paths are checked, and a fresh reviewer can follow the documented path without implementation context. Documentation must be committed/pushed with the final validated `main`.

## Context / parallel evidence
For long autonomous runs retain `CONTEXT-STATE.yaml` epoch evidence and `PARALLELISM-STATE.yaml`. When multiple independent jobs were ready, verification should explain useful concurrent dispatch or the concrete dependency/conflict/resource/bottleneck reason for serialization/throttling.


## V5.9 convergence and evidence freshness
Candidate verification is requirement-linked, not suite-count based. Maintain `CONVERGENCE-MATRIX.json` and `EVIDENCE-INDEX.json`; required evidence is bound to candidate SHA/environment/scope and becomes stale after affected changes. Before completion run `python scripts/quality_gate.py --validate` plus the routed project-native checks.

Tests must be falsifiable: name the production defect caught, derive expected results independently, and use targeted mutation reasoning for material behavior. A passing test that cannot catch a plausible bug is not useful evidence.

## Clean-room product acceptance
For a distributable/user-facing product, when safe/practical verify from a fresh checkout/container/workspace using README and linked canonical docs: prerequisites, install, setup, start, primary user flows, update/migration/uninstall as relevant. Exercise real CLI/API/browser/native/network entry points. Source-code guessing indicates documentation failure.


## Evidence attestation commit
Run product/runtime/test/documentation evidence on a committed **verified candidate SHA**. After verification, a final commit may update only canonical evidence/state attestation files. `quality_gate.py` permits this narrow post-candidate diff. Any code, configuration, test, build/runtime definition or user-facing documentation change after the verified candidate invalidates the affected evidence and requires a new candidate/reverification.


## V5.9 regression / closure / outcome evidence
For a confirmed bug with safe baseline access, preserve evidence that the focused regression check fails for the intended reason before the fix and passes after it. If `FAILURE_MODE_CLOSURE` was triggered, verify the new durable control actually detects/prevents the named failure class.

For declared measurable outcomes, compare candidate and baseline under a credible comparable method. A claimed improvement without comparable measurement is not completion evidence.

## V5.9 behavioral-oracle and independent-assurance gate
For substantive defect repair derive the acceptance oracle from authoritative observable behavior, not the proposed patch. When symptom-layer repair could hide a deeper cause, complete `ROOT_CAUSE_DEPTH_GATE` before implementation. Elevated/high assurance uses author-independent verification; high/critical assurance additionally keeps sibling assurance verdicts blind where parallel independent checks are used. Work-size and assurance profiles are independent.

## V5.9 realness and deferred validation
Verification records evidence type and realness. Mocks/simulations are useful feedback but cannot prove real provider, network, native runtime or user-journey behavior. When the final check requires a human, device, credential or external environment, queue it in `DEFERRED-VALIDATION.json`, continue independent implementation, then execute one consolidated validation/repair wave before completion.
