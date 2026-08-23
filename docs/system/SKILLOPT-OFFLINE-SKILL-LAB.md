# SkillOpt Offline Skill Lab — V5.9

Microsoft SkillOpt is an optional maintainer-side optimization provider, not a normal project runtime dependency and never a self-modifying authority.

Use it only for explicit offline skill-maintenance campaigns selected from usage/eval evidence, especially P0/P1 skills, repeated `ROUTING_MISS`, repeated `EXECUTION_LAPSE`, incidents or behavior regressions. Candidate edits are staged outside `.agents/skills/` and may be promoted only after CtrlAltDelegate structural QA, held-out behavior validation, no-regression checks and risk-appropriate cross-harness verification.

Recommended split: `TRAIN` may inform optimization, `VALIDATION` gates candidate acceptance, and untouched `TEST` verifies final generalization. Never optimize on the final test set. Preserve baseline skill SHA, candidate SHA, SkillOpt version/source commit, optimizer/target backend/model, dataset IDs, scores and promotion decision.

Failure analysis should distinguish at least `SKILL_DEFECT`, `ROUTING_MISS`, `EXECUTION_LAPSE`, `HARNESS_FAILURE`, `MODEL_CAPABILITY_LIMIT`, `STALE_KNOWLEDGE` and `INSUFFICIENT_REFERENCE`; a failed run is not automatically evidence that skill prose is defective.

SkillOpt-Sleep/session harvesting is opt-in only. Full transcripts may contain sensitive project information and real backends may send derived content to an external provider. Prefer CtrlAltDelegate's abstracted usage/routing/failure events when they are sufficient. No automatic scheduled adoption of canonical skills.

Reviewed upstream: `microsoft/SkillOpt` main at commit `bdfdc30a8e17309c06cdbe8449f01bdecc120203` (2026-08-21); MIT-licensed repository. Re-verify current upstream behavior before a maintenance campaign.
