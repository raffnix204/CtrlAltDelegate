# Planning Convergence and Artifact DAG — V5.9

Planning artifacts have explicit dependencies in `planning/architecture/PLANNING-ARTIFACT-GRAPH.yaml`. File existence is never sufficient completion evidence; each artifact needs a semantic validator/readiness contract.

Planning convergence tracks:

- blockers
- warnings
- uncovered requirements
- unresolved decisions
- unresolved assumptions
- missing runtime prerequisites

If the same unresolved signature repeats at the configured plateau threshold, the same planning strategy must not repeat unchanged.

## Decision coverage

Before execution, every consequential decision must be one of:

- `RESOLVED`
- `DEFERRED_WITH_REASON`
- `AUTOPILOT_OWNED`

Load-bearing `TODO`, `maybe` or unowned `decide later` decisions are not execution-ready.

## Deterministic probes before LLM inference

Cheap machine-checkable facts should be probed directly: path existence, executable availability, port state, package/runtime presence, provider configuration and similar facts. Reasoning consumes probe results instead of guessing them.
