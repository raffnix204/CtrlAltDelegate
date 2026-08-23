# Planning Baseline Attestation — V5.8.2

Before `EXECUTION_HANDOFF` or consequential autonomous execution, CtrlAltDelegate may attest the accepted planning baseline. The attestation records deterministic SHA-256 hashes for authoritative planning/control artifacts and the aggregate fingerprint in `planning/execution/PLANNING-BASELINE.json`.

The fingerprint is drift evidence, not a prohibition on legitimate change. If an authoritative file changes, classify the change: expected scoped course correction, stale/uncommitted state, or unexplained drift. Update the affected artifacts, record a ruling/change record, reconverge, then issue a new attestation. Never silently overwrite an accepted baseline merely to match implementation.

Do not include volatile/private logs, raw evidence or timestamps in the hashed set. The attestation must be reproducible from the same authoritative files.
