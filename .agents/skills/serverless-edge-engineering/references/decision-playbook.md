# Serverless & Edge Runtime Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from repository/runtime ownership, current versions/capabilities, public contracts, failure semantics and representative acceptance evidence.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Verify current runtime limits, supported APIs/libraries, regions and pricing before architecture depends on them.

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

## 2. Assume instances are ephemeral and concurrent

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 3. Model cold starts, connection reuse/pooling and database fan-out

- **Watch for:** evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs.
- **Prove with:** frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces.
- **Safe change pattern:** version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

## 4. Use queues/background execution for work that exceeds request-runtime limits or needs reliable retries.

- **Watch for:** duplicate external effects, lost acknowledgements, poison work, retry storms, out-of-order state, reconnect amplification or work that cannot resume after a crash.
- **Prove with:** forced duplicate/retry/crash/out-of-order cases plus queue/worker state, correlation IDs, durable checkpoint/ack evidence and final side-effect invariants.
- **Safe change pattern:** make effect identity/idempotency and responsibility transfer explicit, acknowledge only after durable handoff, bound retry/backoff and isolate poison work.

## 5. Separate edge-friendly logic from Node/native/runtime-specific dependencies and validate actual deployment bundle compatibility.

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.

## 6. Design tracing/logging across short-lived invocations and asynchronous handoffs.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 7. Keep provider-specific services behind clear boundaries when migration risk matters, but accept lock-in where it materially reduces complexity and is documented.

- **Watch for:** version/capability mismatch, removed/renamed behavior, undocumented defaults or a client/provider assumption that differs from the deployed target.
- **Prove with:** detected runtime/server/client/provider versions, current first-party capability/schema documentation and representative success/error operations.
- **Safe change pattern:** bind behavior to discovered capabilities, isolate compatibility branches and record the verified version/capability set with the evidence.
