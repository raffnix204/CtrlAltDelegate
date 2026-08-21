# Skill Schema V5.7.2

## Purpose

V5.7.2 keeps each canonical `SKILL.md` focused on domain expertise while making planning participation explicit through a centralized registry. A specialist can influence Custom-GPT planning, coding-agent execution, or both without duplicating global planning/governance prose across every skill.

## Canonical skill directory

```text
.agents/skills/<skill-id>/
├── SKILL.md
└── references/        # optional progressive material
```

`SKILL.md` remains the canonical decision surface. Progressive references are loaded only when their topic is material.

## Required domain decision surface

A substantive skill must provide unique decision value for its responsibility, including the relevant combination of:

- activation context and boundaries;
- domain invariants and implementation decisions;
- failure modes and drift-sensitive assumptions;
- verification/evidence expectations;
- links to progressive references when deeper material is useful.

Generic autonomy, research, evidence, routing, loop and escalation policy belongs in the system contracts and must not be copied into every skill.

## Planning participation metadata

Every canonical skill must have exactly one entry in `config/PLANNING-SKILL-ROUTING.yaml`. The registry defines:

- whether participation is conditional or not applicable for planning;
- applicable planning phases;
- planning roles;
- artifacts/decisions the skill informs or produces;
- positive activation signals;
- negative triggers that prevent unnecessary loading;
- whether the selected skill is handed to execution when a job remains relevant.

The registry is the authority for planning routing. Do not add repetitive planning-role boilerplate to all `SKILL.md` files merely to restate the registry. A skill body may contain planning-specific domain guidance when that guidance itself is substantive.

## Planning roles

Supported roles include:

- `DISCOVERY_ADVISOR`
- `RESEARCH_ADVISOR`
- `REQUIREMENTS_ADVISOR`
- `ARCHITECTURE_ADVISOR`
- `PROGRAM_DESIGN_ADVISOR`
- `CONTENT_OR_DESIGN_PRODUCER`
- `VERIFICATION_ADVISOR`
- `EXECUTION_SPECIALIST`

## Routing invariant

For every planning phase:

```text
project evidence + resolved constraints
→ candidate specialists
→ smallest complete relevant set
→ consult canonical skill decision surfaces
→ persist material decisions/artifacts
→ refresh routing after material changes
```

The full library is never preloaded. Project profiles are routing hints, not ceilings. Any specialist may participate when evidence makes it relevant.

## Cross-edition invariant

The Custom GPT and GitHub-native editions must use the same canonical skill IDs, skill bodies, progressive references and planning-capability registry. The Custom GPT uses them during planning; the coding-agent handoff carries the job-relevant selected specialists forward to implementation and verification.
