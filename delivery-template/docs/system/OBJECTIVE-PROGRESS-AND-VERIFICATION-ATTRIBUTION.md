# Objective Progress and Verification Attribution — V5.9

The agent no longer self-certifies progress with a boolean. `progress_signature.py` derives a work-product signature from observable repository/control-state deltas: changed-path fingerprint, job status distribution, passing evidence, converged requirements, unresolved blockers and consumer-verified providers.

`record_loop_attempt.py` compares the current signature with the previous one. Same failure + unchanged objective signature + same strategy is denied.

## Pre/post verification attribution

For risk-appropriate jobs, record the same verification command before and after the attempt:

- `CLEAN` — baseline passed and still passes.
- `REGRESSED` — baseline passed; post attempt fails.
- `BASELINE_BROKEN` — baseline already failed and still fails.
- `FIXED_BASELINE` — baseline failed; post attempt passes.

This prevents pre-existing failures from being attributed to a worker and makes regressions explicit.

## Oracle integrity

A worker must not make a red test green by weakening an acceptance/test oracle outside the job's declared allowed test paths. `validate_oracle_integrity.py` flags unexpected test/spec mutation for review.
