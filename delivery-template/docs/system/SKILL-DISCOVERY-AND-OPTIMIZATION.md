# Skill Discovery and Optimization — V5.9

Skill quality has two independent concerns:

1. **Discovery** — does the harness/router load the right skill at the right time?
2. **Behavior** — after the skill is loaded and read, does agent behavior improve?

V5.9 treats skill descriptions as activation metadata. Trigger-first wording (`Use when ...`) is preferred because descriptions should help selection rather than serve as a shortcut for the full workflow in `SKILL.md`.

Bulk semantic description rewrites require A/B evaluation rather than blind formatting. Measure selection recall/precision, whether the skill body was actually read, behavioral compliance and false-positive activation.

For new or materially changed P0/P1 skills, prefer skill-TDD evidence:

`no-skill baseline -> with-skill run -> pressure/adversarial case -> held-out/no-regression validation`.

SkillOpt remains optional offline maintainer tooling. It may optimize staged candidates but cannot directly mutate canonical skills or auto-promote them.
