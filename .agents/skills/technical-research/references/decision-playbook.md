# Technical Research & Evidence Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from the exact unresolved decision, existing planning/repository/runtime evidence, drift risk and the evidence threshold that will stop research.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Start from exported planning research and repository evidence

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 2. Classify research need per job as NONE, VERIFY_DRIFT, TARGETED or SPIKE and state the decision that the research must enable.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 3. Prefer official specifications/docs/repositories/releases and first-party vendor sources for behavior

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 4. Separate sourced fact, repository evidence, inference and recommendation. Date drift-prone evidence and record exact version/platform context.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 5. For uncertain implementation claims, prefer a minimal executable spike/contract test over more prose research.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 6. Once evidence is sufficient, make routine technical decisions autonomously within the authority contract, update STACK/ADR/SKILLS routing and continue.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 7. Escalate only if the researched options change product behavior/scope, risk data loss, weaken security/privacy, create material recurring cost/business lock-in, or require external credentials/approval.

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## Community evidence and reuse discovery

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.
