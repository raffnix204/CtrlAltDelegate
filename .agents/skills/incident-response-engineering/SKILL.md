---
name: incident-response-engineering
description: Prepare and execute evidence-driven incident response with detection, severity, containment, diagnosis, recovery, communication, post-incident learning and tested runbooks.
---

# Incident Response & Runbook Engineering

## Purpose / Ownership

Prepare and execute evidence-driven incident response with detection, severity, containment, diagnosis, recovery, communication, post-incident learning and tested runbooks.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **runbook**.
- Work contains or materially changes **incident**.
- Work contains or materially changes **outage**.
- Work contains or materially changes **on-call**.
- Work contains or materially changes **postmortem**.
- Work contains or materially changes **sev**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Actors/roles/tenant boundaries, sensitive data or money flow, authoritative permissions and external provider/processor contracts.
- Audit, retention/deletion, reconciliation, incident/legal/compliance requirements and who has recovery/destructive authority.
- Failure/abuse cases including insider/admin actions, retries, provider partial failure and account/tenant lifecycle.
- Existing evidence sources: audit log, payment/provider records, data inventory, incident timeline and access-control tests.

## Expert Decision Model

### 1. Define incident classes and severity from user/data/business impact, not emotion


Define incident classes and severity from user/data/business impact, not emotion; attach response expectations and escalation ownership.

### 2. Write runbooks around observable symptoms, decision trees, exact safe checks, bounded mitigation actions and verification rather than generic troubleshooting prose.


Treat this as an observable contract rather than a style preference. The decisive evidence is isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery; keep the design away from restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback, and separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

### 3. Preserve evidence while restoring service: timeline, logs, metrics, traces, deploys, configuration changes and hypotheses must remain distinguishable.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery. If restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback remains plausible, the decision is not closed; separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

### 4. Prefer reversible containment and traffic isolation over speculative invasive fixes


Prefer reversible containment and traffic isolation over speculative invasive fixes; protect data integrity and security during emergency changes.

### 5. Separate mitigation from root-cause correction


Separate mitigation from root-cause correction; once stable, reproduce and fix the causal defect with regression evidence.

### 6. Post-incident actions need owners, evidence and closure criteria


Post-incident actions need owners, evidence and closure criteria; avoid blame and avoid action lists that only say 'be more careful'.

### 7. Exercise high-value runbooks and restore/failover procedures before incidents so commands, permissions and dependencies are known to work.


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

- `reliability-observability`
- `systematic-debugging`
- `backup-disaster-recovery-engineering`
- `documentation-engineering`
