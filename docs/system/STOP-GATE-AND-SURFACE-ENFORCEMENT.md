# Stop Gate and Surface Enforcement — V5.9

A documented policy is not enforcement. V5.9 distinguishes `ENFORCED`, `OBSERVED` and `ADVISORY` mechanisms.

## Stop gate

Where a harness runtime actually exposes a blocking stop hook, stop may be denied only when:

- dependency-ready required work remains, and
- objective progress has occurred.

If ready work exists but progress has stalled, stopping for reconciliation/recovery is allowed; the harness must not be trapped in an infinite forced-continue loop. Harnesses without a verified blocking hook receive advisory continuation only.

## Protected surfaces

`SURFACE-POLICY.yaml` defines:

- `LOCKED`
- `CONTROLLER_MUTATED`
- `DERIVED`
- `APPEND_ONLY`
- `EDITABLE`
- `HUMAN_CONTROLLED`

Git guards run `validate_control_mutation.py` so controller-managed state cannot be silently hand-edited and still pass release/execution gates.
