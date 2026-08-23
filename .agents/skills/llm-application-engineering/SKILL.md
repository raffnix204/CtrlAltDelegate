---
name: llm-application-engineering
description: "Use when the task materially involves this skill's owned domain: Build non-agentic and agentic LLM features with structured outputs, provider/model abstraction, context construction, caching, batching, cost/latency controls, deterministic fallbacks and safe failure handling."
---

# LLM Application Engineering

## Purpose / Ownership

Build non-agentic and agentic LLM features with structured outputs, provider/model abstraction, context construction, caching, batching, cost/latency controls, deterministic fallbacks and safe failure handling.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **llm**.
- Work contains or materially changes **openai**.
- Work contains or materially changes **anthropic**.
- Work contains or materially changes **gemini**.
- Work contains or materially changes **structured output**.
- Work contains or materially changes **prompt**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Exact model/runtime/SDK version, prompt/tool/retrieval contract and model/provider capability limits.
- Versioned evaluation dataset, expected failure classes, safety/privacy/tool-access boundary and rollback baseline.
- Latency/token/cost/resource budget plus concurrency/rate-limit behavior at representative inputs.
- Training/inference data provenance, reproducibility controls and deployment/export format when applicable.

## Expert Decision Model

### 1. Define the model's exact task and evaluation before prompt/provider choice


Define the model's exact task and evaluation before prompt/provider choice; use deterministic code/rules/search for well-structured problems where it is cheaper and more reliable.

### 2. Keep provider/model identifiers and capabilities configurable and verify current limits/features instead of hardcoding stale assumptions.


Treat this as an observable contract rather than a style preference. The decisive evidence is frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces; keep the design away from evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs, and version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 3. Use schemas/structured outputs and validation for machine-consumed responses


Use schemas/structured outputs and validation for machine-consumed responses; parse failures belong in explicit repair/fallback paths.

### 4. Build context from authoritative minimal sources, preserving provenance and authorization


Build context from authoritative minimal sources, preserving provenance and authorization; larger prompts are not automatically better prompts.

### 5. Batch/cache stable work where semantics permit, track token/cost/latency and route simple vs complex requests to adequate capability rather than one expensive model.


Before committing to this point, make its ownership and failure boundary explicit and validate it with effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant. Reject an implementation that can create over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts; use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

### 6. Retry only transient failures and bound repair loops


Retry only transient failures and bound repair loops; authentication, policy and invalid-input failures should fail fast or use planned fallback.

### 7. Test stochastic behavior with eval datasets/repeated runs and retain deterministic unit tests around preprocessing, routing and parsers.


Acceptance requires versioned representative evals, held-out/negative cases, latency/token/resource distributions, traces/tool-call evidence and comparison against the prior candidate; a happy-path command or sample is insufficient on its own.

## Critical Invariants

- Model/prompt/data/retrieval versions that can change behavior are recorded with the evaluation result.
- Tool/data access remains explicitly authorized and validated; model output never grants authority by itself.
- Quality claims are based on representative evals, not one favorable example or model self-assessment.
- Rollout preserves a known-good fallback or comparison path when model/provider drift can materially change product behavior.

## Failure Modes / Sharp Edges

- Evaluation/training leakage or a non-representative benchmark hides real product regressions.
- Prompt/model/provider change improves one metric while degrading safety, latency, cost or another user segment.
- Retrieval/tool failure is misdiagnosed as generation quality and prompts are changed to compensate for bad context.
- Async/concurrent inference or training pipeline loses cancellation/checkpoint state and repeats expensive work.
- Provider/model behavior changes without a versioned eval and silently alters production outputs.

## Version / Drift Triggers

Re-verify current first-party documentation/runtime evidence when any of these materially affect the job:
- Model/API/SDK/tool-calling/structured-output capability and provider limits/pricing.
- Embedding/retrieval model behavior and index compatibility.
- ML framework/accelerator/export/quantization runtime behavior.
- Safety/usage policy or data-processing capability material to the product contract.

## Domain-Specific Verification

- Run versioned representative, negative and held-out evals and compare to the previous accepted candidate.
- Track latency/token/cost/resource distributions and provider/rate-limit failure paths, not only average quality.
- Inspect retrieval/tool traces separately from final generation to localize failures.
- For training/inference changes, verify checkpoint/restart and exported/compiled model outputs against reference behavior where applicable.

## Progressive References

- Read `references/decision-playbook.md` when a material decision, failure path, rollout, recovery or production-verification question needs deeper domain probes.

- Read `references/prompt-contract-design-and-evaluation.md` when prompts are durable product behavior that need structured iteration/evaluation.

## Companion Skills

- `ai-evaluation`
- `agent-application-engineering`
- `search-retrieval-rag-engineering`
- `context-efficiency`
