# V5.6.1 Skill Authoring Schema

## Design objective

Skills encode expert decisions, not generic orchestration. A mid-level engineer familiar with the base language should gain concrete domain-specific judgment from a skill.

## Required frontmatter

```yaml
---
name: <stable-skill-id>
description: <what the skill owns and the concrete contexts that should trigger it>
---
```

Descriptions are routing surfaces. Include distinguishing trigger language and avoid descriptions so broad that the skill fires for adjacent work.

## Recommended body

```text
# Title
## Purpose / Ownership
## Activation & Negative Triggers
## Context To Inspect
## Expert Decision Model
## Critical Invariants
## Failure Modes / Sharp Edges
## Version / Drift Triggers
## Domain-Specific Verification
## Progressive References
## Companion Skills
```

Not every section requires equal size. Omit empty sections rather than filling them with generic boilerplate.

## Progressive references

Use `references/` for material that is:

- useful only for a subset of jobs;
- detailed enough to crowd out the decision model;
- version/provider/runtime-specific;
- a troubleshooting playbook, migration table or protocol deep dive.

Every reference pointer in `SKILL.md` says **when to read it**. Do not create reference files with no routing condition.

## Scripts

Bundle a script only when it replaces deterministic/repeated work that workers would otherwise recreate. Scripts must be inspectable, safe by default and independently testable. Never hide consequential decisions inside opaque automation.

## Source adaptation

External skills, documentation and repositories are research inputs. Extract the underlying decision/failure/verification concept, confirm material technical claims against current first-party sources where appropriate, then rewrite it to fit this system. Do not preserve upstream branding, workflow assumptions, hardcoded model/provider choices or arbitrary prescriptions unless they are genuinely required by the domain.

## Eval requirement

New or materially changed skills require:

1. routing-positive prompts;
2. routing-negative/near-miss prompts;
3. behavior scenarios where the skill should improve a decision over baseline;
4. system-regression checks proving global execution behavior still applies after boilerplate removal.

Prefer discriminating assertions. An assertion that passes equally with and without the skill does not demonstrate skill value.

## V5.6.1 structural completion gates

- **Empty-section gate:** a leaf H2/H3 must contain substantive instructions/evidence guidance; an H2 may delegate detail to child headings but empty numbered Expert Decision points are invalid.
- **Heading/body duplication gate:** a numbered Expert Decision point may not merely repeat its heading as its body.
- **Progressive-reference gate:** every cataloged reference must exist; every reference must state when it is useful and must add decision/failure/verification value beyond the entrypoint.
- **Global-contract gate:** global autonomy, escalation, research, evidence and routing policy remains in `docs/system/SKILL-EXECUTION-CONTRACT.md`, not copied back into specialist skills.
