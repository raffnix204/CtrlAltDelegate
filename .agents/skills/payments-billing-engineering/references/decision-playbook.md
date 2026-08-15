# Payments & Billing Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from actor/tenant boundaries, authority, sensitive state transitions, audit/reconciliation requirements and exceptional/recovery paths.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Treat the payment provider as an external state machine and define which local records are authoritative for product entitlement vs financial evidence.

- **Watch for:** cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence.
- **Prove with:** positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure.
- **Safe change pattern:** define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

## 2. Use provider-hosted checkout/portals when they satisfy requirements and reduce PCI/security scope.

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

## 3. Make create/update/refund operations idempotent and persist provider object/event identifiers for reconciliation.

- **Watch for:** untrusted input crossing a trust boundary, parser/format ambiguity, partial writes, unbounded resource use, metadata/provenance loss or derived data that cannot be rebuilt.
- **Prove with:** representative valid/invalid/adversarial fixtures, round-trip/checksum/metadata invariants, bounded-resource behavior and final consumer/read-back evidence.
- **Safe change pattern:** preserve source/provenance, validate before promotion, stream/bound expensive work, write atomically or through durable staging and keep derivatives rebuildable.

## 4. Verify webhook signatures, tolerate duplicate/out-of-order delivery and process asynchronously with replay capability.

- **Watch for:** duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash.
- **Prove with:** forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants.
- **Safe change pattern:** make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

## 5. Model subscription lifecycle states, proration/trials/cancellation and entitlement timing explicitly

- **Watch for:** evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs.
- **Prove with:** frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces.
- **Safe change pattern:** version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

## 6. Separate money amounts/currencies/tax/invoice facts from display floats and test rounding.

- **Watch for:** cross-tenant leakage, privilege expansion, duplicate financial effects, irreconcilable state transitions, stale flags/policy or missing audit/reconciliation evidence.
- **Prove with:** positive/negative actor and tenant cases, lifecycle/state-transition tests, audit records and reconciliation/recovery tests for partial failure.
- **Safe change pattern:** define authority, defaults and state transitions explicitly, make high-impact changes reversible and keep exceptional paths auditable instead of silently becoming defaults.

## 7. Automate reconciliation between provider events and local state and route material recurring-cost/business-policy decisions to the user.

- **Watch for:** cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership.
- **Prove with:** positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities.
- **Safe change pattern:** centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.
