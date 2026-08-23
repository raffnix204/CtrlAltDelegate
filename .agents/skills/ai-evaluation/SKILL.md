---
name: ai-evaluation
description: "Use when the task materially involves this skill's owned domain: Evaluate AI/LLM/RAG/agent features with versioned datasets, capability and regression evals, deterministic/rule/model/human graders, repeated-run stability, cost/latency tracking, and failure analysis. Use only when product behavior materially depends on stochastic AI outputs."
---

# AI Evaluation Engineering

Skill ID: `ai-evaluation`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Provide trustworthy evaluation for stochastic AI behavior that ordinary exact-output tests cannot adequately cover.

## Activation

AI/LLM features, RAG, extraction, classification, ranking, agents, tool use, generated content, model/prompt/provider changes.

Do not load for conventional deterministic software without an AI behavior surface.

## Core rule

`DEFINE TASK → DATASET → GRADERS → BASELINE → CHANGE → REPEAT → COMPARE → FAILURE ANALYSIS`

## 1. Define evaluated behavior

Separate:
- capability: new behavior must work;
- regression: existing important behavior must remain;
- safety/policy constraints where applicable;
- cost/latency/throughput constraints;
- tool-use/agent completion behavior.

Write criteria before tuning prompts/models when practical.

## 2. Evaluation dataset

Use representative, versioned examples spanning:
- common cases;
- edge/ambiguous cases;
- adversarial/noisy input where relevant;
- different lengths/languages/domains;
- historical production failures when safely available.

Keep training/tuning examples separate from held-out evaluation when overfitting is a risk.

Protect sensitive evaluation data and do not send it to unapproved providers.

## 3. Grader hierarchy

Prefer the most deterministic valid grader:
1. exact/code assertion;
2. schema/type/rule/regex/invariant;
3. reference comparison with robust normalization;
4. model-based rubric;
5. human adjudication.

Do not use an LLM judge for a property a parser/assertion can prove.

## 4. Model-based graders

When semantic judgment is necessary:
- define a narrow rubric and scoring anchors;
- isolate grader from implementation rationale when possible;
- avoid exposing expected labels that make grading trivial;
- calibrate against human examples;
- track grader model/prompt/version;
- inspect disagreement/edge cases.

A judge score is evidence, not ground truth.

## 5. Stochastic stability

Run repeated trials when randomness/model variance matters. Report distributions/failure rates rather than one lucky run.

Use project-specific reliability targets; do not copy arbitrary pass@k thresholds.

For agents, distinguish:
- task completed;
- correct final state;
- number of attempts/tool failures;
- destructive/policy violations;
- cost/latency.

## 6. RAG/retrieval surfaces

Evaluate separately where relevant:
- retrieval coverage/relevance;
- groundedness/citation correctness;
- answer correctness/usefulness;
- refusal/uncertainty behavior;
- latency/cost.

Do not blame generation for missing evidence caused by retrieval.

## 7. Change attribution

Record model/provider/prompt/retrieval/index/tool/schema versions and relevant parameters. Change one dominant variable where practical.

Compare against a stored baseline and identify improved, regressed and unchanged slices.

## 8. Failure analysis

Cluster failures by causal type:
- missing context/retrieval;
- instruction misunderstanding;
- tool selection/execution;
- hallucination/unsupported claim;
- formatting/schema;
- long-context loss;
- ambiguity;
- safety/refusal;
- evaluator error.

Repair the causal component, not only the benchmark example.

## 9. Online evidence

For production AI, complement offline evals with privacy-safe quality/latency/cost/error telemetry and sampled human feedback where appropriate. Never silently capture sensitive prompts/outputs outside approved data policy.

## 10. Release gate

A material AI change records:
- baseline dataset/version;
- grader definitions/versions;
- capability/regression results;
- repeated-run stability where needed;
- cost/latency delta;
- known failure slices;
- decision/rollback path.

## Anti-patterns

- evaluating only happy-path demos;
- tuning against the complete test set until it passes;
- using one opaque LLM judge as sole release gate;
- changing model + prompt + retrieval simultaneously with no attribution;
- exact-string assertions for legitimate variable semantic output;
- ignoring cost/latency drift while optimizing quality;
- treating benchmark score as production correctness.

## V5.6.1 Evaluation Relationship to Agent and ML Skills

Use `ai-evaluation` for nondeterministic/generative behavior: task success, groundedness, structured-output validity, tool selection, refusal/guardrail behavior, latency/cost and repeated-run stability. Pair with `agent-application-engineering` when the system has tools/memory/loops and with `machine-learning-engineering` when learned models/data pipelines require classical ML promotion/drift discipline. Prefer deterministic graders whenever they can faithfully judge the requirement.
