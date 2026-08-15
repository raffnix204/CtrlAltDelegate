---
name: technology-stack-selection
description: Select languages, runtimes, frameworks, rendering models, databases and deployment targets from explicit project constraints and current evidence. Use for non-trivial greenfield stack decisions or justified brownfield replatforming decisions.
---

# Technology & Stack Selection Engineering

## Purpose

Turn product and operational requirements into a defensible technology stack instead of defaulting to familiar tools. The output must explain why the selected language, runtime, framework, data store, deployment model and supporting services fit this project better than credible alternatives.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Every non-trivial NEW_BUILD before architecture is frozen.
- When a brownfield feature introduces a materially new runtime, persistence model, frontend rendering model or platform boundary.
- When the existing stack is demonstrably blocking required performance, security, deployment, maintainability or ecosystem needs.
- When the user explicitly asks which language/framework/database/hosting approach should be used.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Product type, users, workflows, latency/throughput expectations and offline/realtime needs.
- Team/maintenance constraints, delivery speed, hiring/operational realities and existing organizational expertise when known.
- Target platforms, deployment environment, hosting constraints, compliance/security requirements and budget boundaries.
- Data shape, consistency/transaction needs, integration surfaces, background work and expected scale.
- Brownfield stack, current contracts and migration tolerance when an existing repository is involved.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

### Preference and constraint authority
Before comparing stacks, read the resolved project preference/constraint artifact when present. Classify every consequential user statement as `REQUIRED`, `PREFERRED` or `AUTO`. `REQUIRED` eliminates incompatible candidates. `PREFERRED` is a weighted criterion, not an absolute rule. `AUTO` is permission to choose autonomously. Hosting/runtime, exposure model, data sensitivity, region/residency and existing infrastructure can dominate framework preference and must be known before architecture freeze.

If the user has not expressed these constraints, the planner should have run a concise technical-preferences checkpoint; do not infer a hard preference from silence.

- Apply hard constraints first: platform/runtime restrictions, native SDK requirements, compliance, supported deployment targets and required integrations.
- Score credible candidates across correctness fit, ecosystem maturity, maintenance burden, developer velocity, performance headroom, operational simplicity, portability, cost and lock-in.
- Separate language choice from framework choice and framework choice from rendering/deployment model. A good language does not make every framework or architecture appropriate.
- For web work explicitly choose among static generation, MPA, islands/partial hydration, SSR, SPA/client-heavy or hybrid rendering before naming a framework. Research current Astro/Next/Nuxt/SvelteKit/etc. capabilities only when they are real candidates.
- Prefer mature, boring defaults when requirements are ordinary; choose Rust/Go/native/distributed complexity only when concrete constraints justify it.
- For brownfield systems, continuation is the default. Replatform only with evidence that expected benefit exceeds migration and dual-system risk.
- Verify current support windows, licenses, compatibility and deployment constraints for all consequential choices before finalizing.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Frame** — Write the project workload and non-negotiable constraints in technology-neutral language.
2. **Candidate set** — Create a small credible candidate set; avoid a comparison of every technology in existence.
3. **Research** — Use authoritative current docs/releases for unstable facts, platform support and ecosystem constraints.
4. **Score** — Compare candidates using explicit project-weighted criteria and disqualifiers.
5. **Prototype risk** — For uncertain/high-risk claims, run a minimal spike or require a first execution job that proves the assumption.
6. **Decide** — Record selected stack, rejected alternatives, tradeoffs and decision confidence.
7. **Route** — Write STACK-MANIFEST and select matching stack/domain skills before execution planning.

## Expert Heuristics

- Use one primary language/runtime unless a second one buys a concrete platform or performance advantage.
- Do not choose microservices as a default scaling strategy; modular monoliths are usually easier until independent scaling/deployment is required.
- Choose database technology from access patterns, consistency and operational needs, not trend popularity.
- Framework productivity is only valuable if the team can operate and upgrade it safely.
- A static/content-oriented website and a highly interactive SaaS application should not automatically receive the same frontend stack.
- Serverless, containers and Kubernetes are deployment models with different operational costs; choose them after workload and organizational constraints are known.
- Make future migration cost visible: proprietary managed services can be excellent choices when their concrete benefit justifies lock-in.

## Edge Cases and Failure Modes

- Conflicting requirements that favor different ecosystems; isolate the true hard constraint before adding polyglot complexity.
- Unknown scale: design for credible near-term growth and preserve scale-up paths instead of prebuilding hyperscale architecture.
- Vendor SDK only supports certain runtimes; verify current support rather than assuming wrappers are equivalent.
- Existing team insists on a stack that conflicts with a hard technical constraint; document the conflict and escalate only if it changes product/business intent.
- Legacy system requires gradual strangler migration; select compatibility boundaries and coexistence period explicitly.

## Anti-Patterns

- Choosing a language because it benchmarks fastest when the workload is I/O-bound and team/ops cost dominates.
- Selecting a framework first and reverse-engineering requirements to justify it.
- Cargo-culting a previous project stack into a different workload.
- Adding queues, caches, Kubernetes, multiple databases or microservices before a requirement needs them.
- Treating current popularity as evidence of long-term project fit.

## Verification and Evidence

- STACK-MANIFEST names every material language/runtime/framework/database/deployment decision and its status.
- At least one credible alternative and its rejection reason exists for consequential decisions.
- Current-version/platform/licensing facts used by architecture have source evidence.
- Selected project skills include the matching stack specialists and domain specialists.
- No unresolved technology question remains that would materially change job boundaries or implementation approach.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `repository-onboarding`
- `frontend-architecture`
- `backend-architecture`
- `database-design`
- `deployment-readiness`
- `context-efficiency`
