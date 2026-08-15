# Privacy & Data Governance Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from actor/tenant boundaries, authority, sensitive state transitions, audit/reconciliation requirements and exceptional/recovery paths.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## Early data/security/region constraint capture

- **Watch for:** cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence.
- **Prove with:** positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure.
- **Safe change pattern:** define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

## 1. Inventory personal/sensitive data by source, purpose, storage, processor, retention and access rather than relying on a generic privacy statement.

- **Watch for:** silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality.
- **Prove with:** representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases.
- **Safe change pattern:** make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

## 2. Collect only data needed for defined product/operational purposes and avoid placing secrets/PII in logs, analytics, prompts or support artifacts by default.

- **Watch for:** over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts.
- **Prove with:** effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant.
- **Safe change pattern:** use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

## 3. Implement deletion/retention/export across primary databases, caches, indexes, object storage, backups and external processors with documented limitations.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 4. Treat consent/preferences and security/legal bases as product state with auditability where required, not only frontend banners.

- **Watch for:** cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence.
- **Prove with:** positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure.
- **Safe change pattern:** define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

## 5. Define roles and least-privilege access to sensitive datasets and keep production-data use in development/test exceptional and sanitized.

- **Watch for:** cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership.
- **Prove with:** positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities.
- **Safe change pattern:** centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

## 6. When laws/regulations materially constrain behavior, perform current jurisdiction-specific research and escalate genuine compliance decisions rather than encoding stale legal rules.

- **Watch for:** cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence.
- **Prove with:** positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure.
- **Safe change pattern:** define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

## 7. Include privacy checks in new integrations/AI features where data leaves the existing trust boundary.

- **Watch for:** cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence.
- **Prove with:** positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure.
- **Safe change pattern:** define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.
