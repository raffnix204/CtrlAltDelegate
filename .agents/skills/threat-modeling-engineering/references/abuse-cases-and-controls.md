# Threat Abuse Cases & Controls
## When to read this reference

Read this reference when **abuse cases and controls** is material to the current threat modeling engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Write an abuse case with attacker prerequisite → action/path → violated asset/invariant → observable outcome. A mitigation should state where it is enforced and how failure is detected.

Prefer layered controls:
- prevent: authorization, validation, isolation, rate/quotas, signatures/idempotency;
- detect: audit/security events, anomaly/abuse metrics, integrity checks;
- recover: revocation, rollback, replay/reconciliation, credential rotation, backup/restore.

Residual risk is explicit only after controls and remaining consequence are understood.
