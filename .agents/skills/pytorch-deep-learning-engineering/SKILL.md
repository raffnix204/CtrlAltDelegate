---
name: pytorch-deep-learning-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer PyTorch training and inference pipelines with reproducibility, data loading, devices/dtypes, optimization, checkpoints, distributed training, evaluation and deployment correctness."
---

# PyTorch Deep Learning Engineering

## Purpose / Ownership

Engineer PyTorch training and inference pipelines with reproducibility, data loading, devices/dtypes, optimization, checkpoints, distributed training, evaluation and deployment correctness.

Own the domain-specific decisions, invariants, failure modes and verification that materially differ from generic implementation. Global autonomy, escalation, evidence, minimization and routing rules are defined by `docs/system/SKILL-EXECUTION-CONTRACT.md` and are not duplicated here.

## Activation & Negative Triggers

- Work contains or materially changes **pytorch**.
- Work contains or materially changes **torch**.
- Work contains or materially changes **deep learning**.
- Do not activate from library presence alone or for adjacent work that does not touch this responsibility.

## Context To Inspect

- Exact model/runtime/SDK version, prompt/tool/retrieval contract and model/provider capability limits.
- Versioned evaluation dataset, expected failure classes, safety/privacy/tool-access boundary and rollback baseline.
- Latency/token/cost/resource budget plus concurrency/rate-limit behavior at representative inputs.
- Training/inference data provenance, reproducibility controls and deployment/export format when applicable.

## Expert Decision Model

### 1. Version dataset/preprocessing/tokenization/model configuration with checkpoints


Version dataset/preprocessing/tokenization/model configuration with checkpoints; weights without training context are not reproducible artifacts.

### 2. Control random seeds and nondeterminism where evaluation requires repeatability while documenting performance trade-offs.


Treat this as an observable contract rather than a style preference. The decisive evidence is frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces; keep the design away from evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs, and version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 3. Handle device/dtype placement explicitly and verify mixed precision numerics, gradient scaling and overflow behavior.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces. If evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs remains plausible, the decision is not closed; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 4. Design DataLoader/input pipelines so CPU/I/O does not silently dominate accelerator utilization.


Define the before/after state and recovery semantics for this decision before changing code or configuration. Use clean-checkout canonical build/test/install, declared toolchain/lock inputs, intentional generated/artifact diffs, provenance/signature where supported and target smoke/rollback evidence as acceptance evidence, specifically guarding against non-reproducible local residue, stale caches/generated output, dependency substitution, environment-only success, compatibility breaks or artifacts not traceable to immutable source; let CI/release orchestrate repository-owned commands, separate caches from immutable artifacts, pin/record behavior-changing inputs and preserve a known-good promotion/rollback path.

### 5. Track train/validation leakage, overfitting, metrics and checkpoint selection using held-out evidence.


Acceptance requires versioned representative evals, held-out/negative cases, latency/token/resource distributions, traces/tool-call evidence and comparison against the prior candidate; a happy-path command or sample is insufficient on its own.

### 6. For distributed training, reason about effective batch size, synchronization, checkpointing and failure/restart semantics.


Treat this as an observable contract rather than a style preference. The decisive evidence is frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces; keep the design away from evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs, and version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

### 7. Benchmark inference latency/memory on the actual target and validate exported/compiled models against reference outputs.


Base the implementation on the live/repository context that governs this point, then falsify the assumption with frozen representative evals with model/prompt/corpus/index versions, retrieval/ranking or task metrics as applicable, negative/adversarial cases and latency/cost/error traces. If evaluation leakage, model/prompt/corpus/index drift, authorization loss through retrieval, hallucinated authority, unsafe tool/data access or cost/latency regressions hidden by toy inputs remains plausible, the decision is not closed; version every behavior-changing input, separate retrieval from synthesis/tool authority, gate rollout on discriminating evals and retain rollback to the last proven configuration.

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

## Companion Skills

- `machine-learning-engineering`
- `ai-evaluation`
- `performance-profiling`
