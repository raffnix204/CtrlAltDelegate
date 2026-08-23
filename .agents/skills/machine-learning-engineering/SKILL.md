---
name: machine-learning-engineering
description: "Use when the task materially involves this skill's owned domain: Build production ML systems with explicit data contracts, reproducible training, evaluation, model artifacts, serving, monitoring, drift handling and rollback. Use for classifiers, ranking, forecasting, recommenders, embeddings or other learned models."
---

# Production Machine Learning Engineering

## Purpose

Turn model work into a production capability whose data, training, evaluation, artifact promotion, inference and monitoring are reproducible and reviewable. Optimize the product decision and error economics, not an isolated offline metric.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Supervised/unsupervised ML, recommenders, ranking, forecasting, anomaly detection or embedding pipelines.
- Notebook-to-production conversion.
- Model refresh/retraining pipelines, feature engineering or inference serving.
- Failures involving leakage, drift, stale features, train/serve skew or model artifact mismatch.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Product decision influenced by the model and cost of false positives/false negatives/abstention.
- Entity grain, labels/outcomes, feature availability time and dataset provenance.
- Serving mode: batch, online, streaming, on-device or hybrid.
- Latency/throughput/cost/privacy constraints and fallback behavior.
- Current baseline/production model and evaluation slices if existing.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Start from the downstream decision and unacceptable mistakes; choose metrics from those costs.
- Define point-in-time data/feature contracts to prevent leakage.
- Require reproducible dataset snapshot/version, code SHA, configuration and artifact identity.
- Establish a simple baseline before adding model complexity.
- Separate capability evals from regression gates and include important slices, not aggregate metrics only.
- Define promotion criteria before training results are known.
- Treat deployment as a software rollout: shadow/canary/A-B when justified, model-version observability and rollback/fallback.
- Monitor data/feature drift, serving health, latency/cost and delayed quality signals with owners and refresh criteria.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Prediction contract** — Define action, target, inputs/outputs, latency and fallback.
2. **Data contract** — Lock grain, labels, timestamps, splits, sensitive fields and snapshot.
3. **Baseline** — Create simplest credible baseline and error analysis.
4. **Pipeline** — Make feature/training/eval/inference transforms reproducible and train/serve consistent.
5. **Evaluate** — Run predeclared metrics/slices and analyze error clusters.
6. **Package** — Version model/preprocessing/config/artifact safely.
7. **Rollout** — Deploy with guardrails, monitoring and rollback.
8. **Operate** — Track drift/quality/incidents and turn failures into regressions.

## Expert Heuristics

- No feature may use information unavailable at prediction time.
- A more accurate model is not better if latency, cost, calibration or failure mode makes product behavior worse.
- Keep preprocessing with the model artifact or generated from one source to prevent train/serve skew.
- Preserve meaningful production mistakes as dataset slices/regression cases.
- Do not treat user feedback as unbiased ground truth without examining selection/lag/coverage.
- For generative/LLM components, pair with `ai-evaluation` rather than forcing classical ML metrics onto open-ended behavior.

## Edge Cases and Failure Modes

- Sparse/delayed labels.
- Distribution shift after rollout changes user behavior.
- High-impact decisions requiring human override/audit.
- GPU/nondeterministic training and reproducibility limits.
- Model/data licenses constrain deployment.
- Artifact deserialization/security and sensitive training data.

## Anti-Patterns

- Optimizing accuracy without a product decision contract.
- Random train/test split for temporal problems where future leakage occurs.
- Notebook-only hidden state.
- Promoting a model because one aggregate metric improved.
- No fallback when feature/model service is unavailable.

## Verification and Evidence

- Dataset/model/config/code identities are recorded.
- Leakage and train/serve parity checks exist.
- Promotion metrics and slices meet declared gates.
- Inference contract, fallback and latency/cost are tested.
- Monitoring/rollback/retraining criteria exist before production completion.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `ai-evaluation`
- `test-engineering`
- `performance-profiling`
- `reliability-observability`
- `security-review`
- `database-design`
