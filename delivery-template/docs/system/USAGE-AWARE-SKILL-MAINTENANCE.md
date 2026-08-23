# Usage-Aware Skill Maintenance — V5.9

## Goal
The 154-skill library remains fully available and structurally validated, but expensive maintenance effort is prioritized by observed project usage plus criticality/drift risk.

## Local evidence only
CtrlAltDelegate does not add telemetry. Project runs may append non-secret events to `planning/execution/SKILL-USAGE-EVENTS.jsonl`. Maintainers can explicitly aggregate selected delivery directories/ZIPs with `scripts/aggregate_skill_usage.py`.

## Priority model
- **P0 Core/Safety**: maintained proactively regardless of observed frequency.
- **P1 Hot**: high weighted usage; proactive drift/source review and full behavior campaigns.
- **P2 Warm**: regular usage; rotating behavior campaigns and drift review when signaled.
- **P3 Cold**: structural QA every release; expensive external refresh deferred until activation/`VERIFY_DRIFT`.
- **Retirement candidate**: never automatic. Requires sustained low use, overlap evidence and behavior-eval evidence that the skill adds no unique value.

`RUNTIME_INJECTED` and especially `ROUTING_MISS` receive extra weight because they reveal weaknesses in AOT routing. Usage affects maintenance scheduling only; it never suppresses a required skill at runtime.

## Optional SkillOpt campaign
V5.9 may use Microsoft SkillOpt as an external offline optimizer for selected maintenance candidates. Usage decides where to spend optimization budget, not whether a skill remains available. SkillOpt writes only staged candidates; promotion requires CtrlAltDelegate structural QA, held-out behavior validation, no regression and risk-appropriate cross-harness evidence. Session harvesting is opt-in and is not required when abstract usage/routing events are sufficient.
