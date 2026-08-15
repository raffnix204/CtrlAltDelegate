# Provenance & Maintenance

V5.3 is an independently written first-party planning/autonomous-delivery system. External repositories and standards are research inputs only; do not vendor their prompts/runtime or imply dependency unless a project explicitly selects one.

## Method inspirations reviewed
- OpenAI/Agent Skills and harness documentation for skill discovery and project instruction behavior.
- Pi official documentation for packages, extensions, Project Trust, reload/session lifecycle and extensibility.
- ECC for broad skill-coverage ideas, context budgeting, research/evaluation and workflow-quality patterns.
- Shokunin for broad engineering-domain coverage and skill-depth comparisons.
- GSD Core, Superpowers, its-magic and related public agent-method repositories for decomposition, fresh-context, verification and persistent-state ideas.

All useful concepts are normalized into the system's own portable terminology and safety model. Runtime third-party packages are capability providers, not architectural dependencies.

## Maintenance rules
- Re-research drift-prone tool/framework/provider facts when they materially affect a decision.
- Never hardcode third-party Pi package versions or model choices into methodology.
- Release QA must scan all operative files/skills/bundles for stale version/path references, validate manifests, and prove canonical skill directory parity between editions.
- Large library breadth is allowed; route only the smallest complete job-specific set.
