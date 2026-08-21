# CtrlAltDelegate V5.8.1

V5.8.1 is a deterministic runtime and maintenance hardening release. It adds no canonical skills.

<!-- VERIFIED-RELEASE-CLAIMS: release/RELEASE-CLAIMS.yaml -->

## Verified release facts
- Canonical skills: **154 -> 154**.
- Added canonical skills: **none**.
- Progressive references remain **147**.

## Major changes
- Runtime skill escalation with L0 reference load, L1 single-skill JIT injection, L2 job rebrief and L3 scoped change.
- Immutable base worker briefs plus append-only SHA-bound skill grant deltas/effective-brief hashes.
- Release claims are checked against generated release-delta evidence and can be checked against the real Git diff after repository merge.
- Corrected documentation that incorrectly attributed the nine V5.7.1 specialist additions to V5.8.
- Usage-aware skill maintenance: P0 safety/core, P1 hot, P2 warm, P3 cold; no automatic retirement and no usage-based runtime suppression.
- Local/export history aggregation without network telemetry.
