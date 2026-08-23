# Review Verdicts, Rulings and Negative Requirements — V5.9

## Tri-state review

Review verdicts are:

- `PASS`
- `FAIL`
- `UNVERIFIABLE`

`UNVERIFIABLE` is never converted to PASS. It must name the missing follow-up evidence. Verdict identity binds requirement + candidate SHA + oracle + verifier profile; a new candidate SHA invalidates the old verdict for mutable behavior.

## Rulings instead of unnecessary stalls

When multiple safe interpretations exist and user authority is not required, the orchestrator may record a `RULING` containing:

- decision
- why
- evidence
- cost if wrong

This is distinct from an `ASSUMPTION`: a ruling chooses among safe interpretations; an assumption marks an evidence gap to validate later.

## Negative requirements

Planning should capture both positive outcomes and exclusions. Product contracts may declare `negative_requirements` / `exclusions`, and job acceptance must preserve relevant `MUST_NOT` behavior. Final verification checks the absence of prohibited behavior rather than only the presence of desired features.
