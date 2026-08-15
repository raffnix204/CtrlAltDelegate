---
name: multi-tenancy-engineering
description: Design tenant isolation, identity, data partitioning, authorization, quotas, migrations, observability and operational workflows for shared SaaS systems.
---

# Multi-Tenancy Engineering

## Purpose / Ownership

Design tenant isolation, identity, data partitioning, authorization, quotas, migrations, observability and operational workflows for shared SaaS systems.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **multi tenant**.
- Work contains or materially changes **tenant**.
- Work contains or materially changes **saas isolation**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Actors/roles/tenant boundaries, sensitive data or money flow, authoritative permissions and external provider/processor contracts.
- Audit, retention/deletion, reconciliation, incident/legal/compliance requirements and who has recovery/destructive authority.
- Failure/abuse cases including insider/admin actions, retries, provider partial failure and account/tenant lifecycle.
- Existing evidence sources: audit log, payment/provider records, data inventory, incident timeline and access-control tests.

## Expert Decision Model

### 1. Choose tenancy model—shared schema with tenant key/RLS, schema-per-tenant, database-per-tenant or hybrid—from isolation, scale and operations requirements.


Before committing to this point, make its ownership and failure boundary explicit and validate it with positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities. Reject an implementation that can create cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership; centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 2. Carry tenant context explicitly from authenticated request/job/event boundaries and never infer it from user-controlled object identifiers.


Treat this as an observable contract rather than a style preference. The decisive evidence is positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities; keep the design away from cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership, and centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 3. Enforce isolation at multiple appropriate layers and write negative cross-tenant tests


Enforce isolation at multiple appropriate layers and write negative cross-tenant tests; convenience filters alone are not a security boundary.

### 4. Partition caches, search/vector indexes, object storage keys and background jobs by tenant as carefully as primary database rows.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities as acceptance evidence, specifically guarding against cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership; centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 5. Design tenant-aware migrations/backfills, quotas/rate limits, billing/entitlements and deletion/export workflows.


Before committing to this point, make its ownership and failure boundary explicit and validate it with positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities. Reject an implementation that can create cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership; centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 6. Keep operator/support impersonation or cross-tenant admin paths auditable and tightly privileged.


Treat this as an observable contract rather than a style preference. The decisive evidence is positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities; keep the design away from cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership, and centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

### 7. Include tenant identity in logs/metrics safely for diagnosis without leaking one tenant's data to another.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities. If cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership remains plausible, the decision is not closed; centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

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

- `auth-architecture`
- `database-design`
- `security-review`
- `payments-billing-engineering`
