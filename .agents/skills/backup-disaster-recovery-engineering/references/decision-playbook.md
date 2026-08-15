# Backup & Disaster Recovery Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from independent failure domains, protected data/config/key dependencies, RPO/RTO, restore authority and the last independently proven recovery exercise.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Define data classes and required RPO/RTO before selecting backup mechanisms

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 2. Backups must live outside the primary failure domain and be encrypted/access-controlled independently where appropriate.

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 3. Capture application data, object/file storage, configuration, encryption-key dependencies and infrastructure state needed for real recovery.

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 4. Continuously or periodically verify backup integrity and perform restore drills into isolated environments

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 5. Document point-in-time vs snapshot semantics, consistency coordination and quiescing requirements for multi-store applications.

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 6. Design ransomware/credential-compromise resilience using immutable/offline/limited-deletion copies where risk warrants.

- **Watch for:** over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts.
- **Prove with:** effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant.
- **Safe change pattern:** use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

## 7. Recovery runbooks name ordering, DNS/network changes, secret/key restoration, health checks and authority to fail over/fail back.

- **Watch for:** over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts.
- **Prove with:** effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant.
- **Safe change pattern:** use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.
