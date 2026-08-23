# Skill Evals — V5.9

V5.9 evaluates skills as behavior-changing expert context, not by file count or prose length.

## Eval classes

- **routing** — correct specialist is available/loaded; near-miss specialists remain unloaded.
- **behavior** — V5.9 specialist must improve a discriminating technical decision versus the frozen V5.5/no-specialist baseline.
- **system_regression** — proves global autonomy/evidence/rightsizing/routing behavior still applies after boilerplate was removed from individual skills.

## Baselines

Existing skills compare against their V5.5 entrypoint. New V5.9 skills compare against the global execution contract plus adjacent generic skills without the new specialist. Preserve the prompt, repository fixture and tool surface across compared runs.

## Measurements

Record pass/fail per assertion plus:

- active `SKILL.md` context tokens;
- progressive-reference tokens actually loaded;
- elapsed time/tool calls where measurable;
- repeated-run pass-rate/variance for stochastic tasks;
- cases where the specialist made the outcome worse.

An assertion that passes equally without the specialist is non-discriminating and should be replaced or demoted to system regression.

`python scripts/validate_skill_evals.py` checks structural integrity. Harness-specific runners may execute the scenarios against any supported model/provider; this pack deliberately does not hardcode one.
