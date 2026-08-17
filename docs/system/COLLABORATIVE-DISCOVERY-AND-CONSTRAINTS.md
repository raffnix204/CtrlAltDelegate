# Collaborative Discovery & Preference/Constraint Contract — V5.6.4

## Purpose
V5.6.4 keeps autonomous planning while preventing expensive late architectural reversals. Discovery is **co-design**, not a questionnaire. The planner must actively clarify, suggest, challenge and research before freezing consequential technical decisions.

## Adaptive discovery
Do not classify a person permanently as beginner or expert. Infer only how much detail is useful **for the current decision**. Functional/product understanding remains rigorous for everyone.

Decision style for the planning session:
- `AUTOPILOT` — planner decides unspecified details autonomously and explains only consequential choices.
- `COLLABORATIVE` — planner surfaces important alternatives/trade-offs before consequential decisions.
- `DIRECTED` — user supplies more technical constraints; planner still challenges unsafe/incompatible assumptions.

Every preference/constraint is recorded with one strength:
- `REQUIRED` — hard constraint; do not override autonomously.
- `PREFERRED` — honor unless evidence shows material downside/conflict; explain deviation.
- `AUTO` — planner selects from requirements/current evidence.

## Early technical-preferences checkpoint
Before stack selection/architecture freeze, ask concise natural-language questions covering:
1. **Decision involvement** — how much the user wants to steer technical choices.
2. **Technology preferences** — languages/frameworks/databases/platforms to use or avoid; `AUTO` always valid.
3. **Runtime/hosting/environment** — cloud/provider/server/VM/container/serverless/edge/local-LAN/offline/device constraints; `AUTO` always valid.
4. **Data/security/region/exposure** — sensitivity, public vs private/LAN-only, residency/region, regulatory or high-security constraints; `AUTO`/“no special requirement” always valid when appropriate.

Ask a fifth/follow-up question only when the answers or project imply material existing systems, integrations, budget/operating constraints, hardware/network limits, accounts/providers, migration requirements or other high-impact dependencies.

Do not ask again for facts already provided. For an obvious beginner, explain choices in outcome language and recommend a default. For an experienced user, allow deeper trade-off discussion. In both cases the user may delegate any individual choice to `AUTO`.

## Collaborative discovery loop
Use repeated small rounds of 3–7 high-value questions, but do not merely interrogate:

`UNDERSTAND → CLARIFY → OPPORTUNITY_SCAN → SUGGEST/CHALLENGE → USER_OR_AUTO_DECISION → REFINE → REPEAT`

Three planner behaviors:
- **Clarify:** resolve ambiguity or missing behavior that affects acceptance/design.
- **Suggest:** surface a relevant feature/workflow/control the user may have omitted.
- **Challenge:** point out a likely worse, unsafe or unnecessarily complex choice and propose a better alternative.

Suggestions must pass relevance and YAGNI/solution-minimization tests. Do not inflate scope merely because an idea is possible. Record accepted suggestions, rejected ideas and explicit non-goals so they do not reappear later.

## Opportunity scan
As relevant, scan for overlooked concerns across:
- core workflows and user roles;
- onboarding, permissions and recovery/error states;
- search/filter/import/export/notifications/automation;
- data lifecycle, backup/restore and audit needs;
- integrations and external dependencies;
- accessibility, privacy, security and abuse boundaries;
- offline/network/device behavior;
- observability, operations, performance and scale;
- migration/upgrade paths and likely near-term constraints.

Only surface opportunities that are plausible and material for this product.

## Research before consequential architecture
For material technology/platform/hosting decisions, use current research proportional to uncertainty and consequence. Priority:
1. actual repo/runtime evidence for brownfield;
2. official docs/specs/releases/support matrices;
3. official repositories/issues when operational details matter;
4. strong independent technical evidence;
5. community evidence (for example GitHub discussions/issues, Stack Overflow, Reddit) for real-world friction, edge cases and operator experience.

Community evidence is supplementary, never the sole authority for compatibility/security/compliance. Research should also test whether an established project/library/platform capability can satisfy the need before custom implementation. Evaluate fit, license, maintenance, security, extensibility and lock-in.

## Discovery readiness / assumption freeze
Do not finalize stack/architecture while a high-impact unknown could reasonably force substantial redesign. Before `DISCOVERY_READY`, summarize:
- product intent/users/core workflows and accepted outcomes;
- material edge cases/non-goals;
- accepted/rejected planner suggestions;
- preference/constraint matrix (`REQUIRED|PREFERRED|AUTO`);
- hosting/runtime/exposure/security/data/region assumptions;
- existing systems/integrations when applicable;
- unresolved items and whether they are safe to defer.

Ask one compact confirmation only for consequential user-owned constraints. `AUTO` items do not need approval; the planner selects them with evidence and proceeds.

Lifecycle:
`INTAKE → COLLABORATIVE_DISCOVERY → PREFERENCES_CONSTRAINTS_READY → DISCOVERY_READY → RESEARCH_READY → STACK_READY → ARCHITECTURE_READY → PROGRAM_DESIGN_READY → SKILLSET_READY → EXECUTION_RIGHTSIZING_GATE → EXECUTION_DAG_READY → DELIVERY_READY`

For GitHub-native standalone operation, `DELIVERY_READY` means the repository-local planning baseline is ready to enter execution; an external Custom-GPT/ZIP transfer is not required. See `FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md`.

## Late constraint changes
A late user constraint does not automatically trigger full replanning:
`NEW_CONSTRAINT → IMPACT_ANALYSIS → INVALIDATE_ONLY_AFFECTED_ARTIFACTS/EVIDENCE → UPDATE ADR/STACK/PROGRAM_DESIGN/JOBS → RECONVERGE`

If the new constraint changes product intent, safety, business commitment or other user-owned scope, surface that decision. Otherwise update the affected technical plan autonomously.
