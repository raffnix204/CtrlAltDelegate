# Prompt Contract Design and Evaluation

Use this reference when an LLM prompt is a durable product contract rather than an ad-hoc one-off request.

## Contract
Record: purpose, authoritative context, task, constraints, tool/authority policy, output schema/format, examples only where they improve discrimination, failure modes, fallback and evaluation cases.

## Refinement loop
`BASELINE PROMPT → REPRESENTATIVE EVALS → FAILURE CLASSIFICATION → ONE TARGETED CHANGE → RE-EVAL → REGRESSION CHECK → ACCEPT/REJECT`.

Change one material variable at a time when diagnosing prompt behavior. Version behavior-changing prompt/context/schema/model inputs with eval evidence. Do not optimize a prompt against a single favorable example or leak expected answers into the evaluation context.
