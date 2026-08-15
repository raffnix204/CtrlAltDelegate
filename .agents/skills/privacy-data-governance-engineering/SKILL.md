---
name: privacy-data-governance-engineering
description: Engineer data minimization, classification, retention, consent, access/deletion/export and privacy-safe telemetry boundaries while routing jurisdiction-specific legal conclusions to current authoritative research.
---

# Privacy & Data Governance Engineering

## Purpose / Ownership

Engineer data minimization, classification, retention, consent, access/deletion/export and privacy-safe telemetry boundaries while routing jurisdiction-specific legal conclusions to current authoritative research.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **privacy**.
- Work contains or materially changes **gdpr**.
- Work contains or materially changes **pii**.
- Work contains or materially changes **retention**.
- Work contains or materially changes **data deletion**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Actors/roles/tenant boundaries, sensitive data or money flow, authoritative permissions and external provider/processor contracts.
- Audit, retention/deletion, reconciliation, incident/legal/compliance requirements and who has recovery/destructive authority.
- Failure/abuse cases including insider/admin actions, retries, provider partial failure and account/tenant lifecycle.
- Existing evidence sources: audit log, payment/provider records, data inventory, incident timeline and access-control tests.

## Expert Decision Model

### Early data/security/region constraint capture


Before architecture is frozen, capture whether the system is public, private/LAN-only or offline; what sensitive/personal data exists; expected data residency/region; and whether regulatory/high-security requirements apply. Unknown or delegated items may be `AUTO`, but a user-specified residency/exposure/security requirement is not a routine implementation choice and must survive into architecture and deployment evidence.

### 1. Inventory personal/sensitive data by source, purpose, storage, processor, retention and access rather than relying on a generic privacy statement.


Treat this as an observable contract rather than a style preference. The decisive evidence is representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases; keep the design away from silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality, and make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

### 2. Collect only data needed for defined product/operational purposes and avoid placing secrets/PII in logs, analytics, prompts or support artifacts by default.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. If over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts remains plausible, the decision is not closed; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 3. Implement deletion/retention/export across primary databases, caches, indexes, object storage, backups and external processors with documented limitations.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence as acceptance evidence, specifically guarding against untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 4. Treat consent/preferences and security/legal bases as product state with auditability where required, not only frontend banners.


Before committing to this point, make its ownership and failure boundary explicit and validate it with positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure. Reject an implementation that can create cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence; define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

### 5. Define roles and least-privilege access to sensitive datasets and keep production-data use in development/test exceptional and sanitized.


Treat this as an observable contract rather than a style preference. The decisive evidence is positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities; keep the design away from cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership, and centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 6. When laws/regulations materially constrain behavior, perform current jurisdiction-specific research and escalate genuine compliance decisions rather than encoding stale legal rules.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure. If cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence remains plausible, the decision is not closed; define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

### 7. Include privacy checks in new integrations/AI features where data leaves the existing trust boundary.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure as acceptance evidence, specifically guarding against cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence; define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

## Critical Invariants

- Authorization is enforced at the authoritative operation/data boundary for every tenant/role path.
- Consequential privileged, money-moving or destructive actions remain attributable through durable audit/reconciliation evidence.
- Sensitive data is minimized to the stated purpose and follows retention/deletion/region/processor constraints.
- Retried or recovered operations cannot duplicate financial/destructive effects without idempotency and reconciliation.

## Failure Modes / Sharp Edges

- UI/route-level checks are bypassed by alternate API/data paths.
- Privileged/admin or support tooling crosses tenant boundaries without explicit scoped authorization and audit.
- Provider retry/webhook timing creates duplicate charges, notifications or state transitions.
- Deletion/retention workflow leaves untracked derived copies or deletes forensic evidence required by an active incident/legal hold.
- Incident containment destroys the only evidence needed for root cause or recovery.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Payment/identity/provider API and webhook semantics.
- Applicable regulatory/contractual retention, region, processor and audit requirements.
- Platform authorization/session/admin capability behavior.
- Incident-response integrations and evidence retention capabilities.

## Domain-Specific Verification

- Run positive/negative role and tenant tests at the real authoritative operation.
- Reconcile provider/external records against internal state for money-moving or asynchronously confirmed actions.
- Verify audit entries contain actor, target, tenant/context, result and correlation without leaking forbidden sensitive data.
- Exercise deletion/retention/recovery/incident paths with the same authority boundaries used in production.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

## Companion Skills

- `security-review`
- `product-analytics-engineering`
- `technical-research`
