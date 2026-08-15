# LLM Application Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from versioned model/prompt/data/index inputs, representative evals, authorization/safety boundaries, latency/cost budgets and fallback/abstention behavior.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Define the model's exact task and evaluation before prompt/provider choice

- **Watch for:** evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs.
- **Prove with:** frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces.
- **Safe change pattern:** version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

## 2. Keep provider/model identifiers and capabilities configurable and verify current limits/features instead of hardcoding stale assumptions.

- **Watch for:** evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs.
- **Prove with:** frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces.
- **Safe change pattern:** version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

## 3. Use schemas/structured outputs and validation for machine-consumed responses

- **Watch for:** silent loss/duplication, incompatible readers/writers, unbounded growth, hot partitions, lock amplification, stale derived state or access paths that collapse at realistic cardinality.
- **Prove with:** representative data volume, invariants/counts/checksums, explain/access-path evidence, latency/resource/lock metrics and retry/failure cases.
- **Safe change pattern:** make ownership/schema/consistency explicit, use backward-compatible expand/contract changes and keep backfills/rebuilds bounded, resumable and verifiable.

## 4. Build context from authoritative minimal sources, preserving provenance and authorization

- **Watch for:** cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership.
- **Prove with:** positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities.
- **Safe change pattern:** centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

## 5. Batch/cache stable work where semantics permit, track token/cost/latency and route simple vs complex requests to adequate capability rather than one expensive model.

- **Watch for:** over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts.
- **Prove with:** effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant.
- **Safe change pattern:** use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

## 6. Retry only transient failures and bound repair loops

- **Watch for:** evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs.
- **Prove with:** frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces.
- **Safe change pattern:** version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

## 7. Test stochastic behavior with eval datasets/repeated runs and retain deterministic unit tests around preprocessing, routing and parsers.

- **Watch for:** management-path loss, wrong zone/VLAN/route/NAT semantics, asymmetric return traffic, MTU/IPv6 surprises or controller/device partial convergence.
- **Prove with:** before/after topology and config, live routes/neighbors/rules, service/device health, representative bidirectional client traffic, counters/logs and packet capture when needed.
- **Safe change pattern:** preserve independent management or timed rollback, canary risky changes and widen only after live dataplane/service convergence.
