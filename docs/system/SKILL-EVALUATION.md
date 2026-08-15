# Skill Evaluation — V5.6.1

The skill library is software behavior, not static prose. Release QA must test routing and behavioral effect, especially as the library grows.

## Three eval lanes
1. **Routing eval** — realistic project/job fingerprints select required skills and reject unrelated specialists.
2. **Behavior eval** — compare an agent baseline without the target skill against the same bounded task with the skill. Score observable decisions/output/evidence, not whether the agent repeats skill wording.
3. **System-evolution eval** — run sequences of dependent changes/resume/context-epoch transitions to detect state contamination, stale routing and convergence drift.

## Pressure scenarios
For critical skills include scenarios that tempt the agent to violate the skill under time/complexity pressure. Examples: security shortcut, skip docs, reuse stale test result, add a dependency unnecessarily, serialize independent jobs, or load the whole skill library.

## Skill description discipline
Catalog/description text exists for routing. Keep global autonomy/research/evidence/routing policy in `SKILL-EXECUTION-CONTRACT.md`; keep only domain-specific decision guidance in `SKILL.md`, with deep specialist material in progressive `references/`. A worker should load the canonical skill and only the references material to its job.

## Regression policy
A skill may not be considered improved merely because it is longer. Keep/change/merge/retire based on measurable routing/actionability/behavior. If a new rule measurably worsens success, remove or rework it.

## Assets
`evals/skills/scenarios.yaml` contains deterministic catalog-level cases plus prompts for behavior campaigns. `scripts/validate_skill_evals.py` validates scenario integrity without invoking a model. Model/harness campaigns remain optional release QA and must record the harness/model/provider actually used rather than hardcoding it into methodology.
