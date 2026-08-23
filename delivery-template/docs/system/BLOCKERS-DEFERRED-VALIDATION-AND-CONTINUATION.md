# Blockers, Deferred Validation & Continuation — V5.8.2

## Principle

Build as far as safely possible before requesting human intervention. Missing proof blocks the affected completion claim; it does not block dependency-ready implementation. A completed implementation may enter `IMPLEMENTED_UNVERIFIED`, which satisfies ordinary `IMPLEMENTATION` dependencies while an explicitly `VERIFIED` dependency still waits for `DONE`.

## Two blocker classes

### EXECUTION_BLOCKER
Use only when the affected implementation path cannot be continued meaningfully or safely without the missing dependency/authority. Scope it to `JOB`, `SUBGRAPH` or `GLOBAL`. A global execution stop is valid only when no dependency-ready required work remains and every remaining required path depends on unresolved execution blockers.

### VERIFICATION_BLOCKER
Use when implementation can continue but final proof currently needs a credential, human action, physical device, external service/window or other unavailable validation prerequisite. Record it through `scripts/record_blocker.py` into `BLOCKERS.json` and `DEFERRED-VALIDATION.json`, record any implementation assumption, and continue ready work.

## Autonomous fallback

Unless human authority is genuinely required:

`RESEARCH → BEST-EVIDENCE IMPLEMENTATION → RECORD ASSUMPTION → DEFER UNAVAILABLE VALIDATION → CONTINUE`.

An assumption must state basis/evidence, affected requirement/job, confidence, candidate/plan reference, validation required later and whether it can invalidate implemented work.

## Batched validation wave

After feasible implementation/integration work is exhausted, execute a consolidated deferred-validation wave. Ask the user for the smallest grouped set of actions/credentials/device checks that cannot be automated. Failed deferred checks create repair jobs and re-enter normal closed-loop verification.
