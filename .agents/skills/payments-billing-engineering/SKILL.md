---
name: payments-billing-engineering
description: Engineer checkout, subscriptions, invoices, entitlements, refunds and payment-provider integrations with idempotency, webhook verification, ledger clarity and reconciliation.
---

# Payments & Billing Engineering

## Purpose / Ownership

Engineer checkout, subscriptions, invoices, entitlements, refunds and payment-provider integrations with idempotency, webhook verification, ledger clarity and reconciliation.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **stripe**.
- Work contains or materially changes **payment**.
- Work contains or materially changes **billing**.
- Work contains or materially changes **subscription**.
- Work contains or materially changes **checkout**.
- Work contains or materially changes **invoice**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Actors/roles/tenant boundaries, sensitive data or money flow, authoritative permissions and external provider/processor contracts.
- Audit, retention/deletion, reconciliation, incident/legal/compliance requirements and who has recovery/destructive authority.
- Failure/abuse cases including insider/admin actions, retries, provider partial failure and account/tenant lifecycle.
- Existing evidence sources: audit log, payment/provider records, data inventory, incident timeline and access-control tests.

## Expert Decision Model

### 1. Treat the payment provider as an external state machine and define which local records are authoritative for product entitlement vs financial evidence.


Before committing to this point, make its ownership and failure boundary explicit and validate it with positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure. Reject an implementation that can create cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence; define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

### 2. Use provider-hosted checkout/portals when they satisfy requirements and reduce PCI/security scope.


Treat this as an observable contract rather than a style preference. The decisive evidence is detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations; keep the design away from version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target, and bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

### 3. Make create/update/refund operations idempotent and persist provider object/event identifiers for reconciliation.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence. If untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt remains plausible, the decision is not closed; preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

### 4. Verify webhook signatures, tolerate duplicate/out-of-order delivery and process asynchronously with replay capability.


Acceptance requires negative authorization tests, audit trails, reconciliation, retention/deletion checks, incident timelines and recovery rehearsal appropriate to the domain; a happy-path command or sample is insufficient on its own.

### 5. Model subscription lifecycle states, proration/trials/cancellation and entitlement timing explicitly


Model subscription lifecycle states, proration/trials/cancellation and entitlement timing explicitly; never infer active access from one payment boolean.

### 6. Separate money amounts/currencies/tax/invoice facts from display floats and test rounding.


Treat this as an observable contract rather than a style preference. The decisive evidence is positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure; keep the design away from cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence, and define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

### 7. Automate reconciliation between provider events and local state and route material recurring-cost/business-policy decisions to the user.


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

- `integration-engineering`
- `security-review`
- `background-job-engineering`
