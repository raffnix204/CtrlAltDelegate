# Model Routing & Hierarchical Orchestration — V5.9.2

## Purpose

V5.9.2 turns the existing spawn-only orchestrator into an explicit hierarchical execution model: a frontier lead owns the objective and control plane, while bounded implementation/research/validation work is delegated to cheaper fresh-context workers whenever the active harness can select a model per subagent.

The deterministic CtrlAltDelegate state machine remains authority. Model quality is a routing resource, not a substitute for job contracts, evidence, scopes, verification or controller-owned state.

## Core topology

```text
FRONTIER MAIN ORCHESTRATOR
  classify → compile brief → select class → dispatch → monitor
       │
       ├── EFFICIENT implementation/research/validator workers
       ├── BALANCED complex implementation/reviewer/debugger workers
       └── FRONTIER critical implementation/reviewer/debug escalation

worker result
  → exact change-set freeze
  → parent re-verification
  → fresh independent review
  → orchestrator adjudication/integration/rebrief
```

When suitable delegation exists, the main orchestrator does not implement feature jobs. It may make controller/state edits, prepare briefs, inspect diffs/evidence, adjudicate findings, integrate validated results and perform unavoidable tiny bootstrap edits. This preserves its context for global reasoning and prevents long implementation traces from becoming project memory.

## Model classes

CtrlAltDelegate routes abstract capability classes, not permanent vendor names:

- `FRONTIER` — global orchestration, architecture-sensitive judgment, critical review and final debugging escalation.
- `BALANCED` — complex implementation, semantic code review, integration reasoning and debugging.
- `EFFICIENT` — default bounded coding, targeted research, mechanical validation, routine docs/Git work.

`config/MODEL-ROUTING-POLICY.yaml` is canonical. A job records its minimum/requested class in the Job Contract and Worker Brief. The runtime resolves that class against the active harness.

## OpenAI GPT-5.6 mapping

As researched on 2026-08-25 from current OpenAI model guidance:

- `FRONTIER` → `gpt-5.6-sol`, reasoning `high`.
- `BALANCED` → `gpt-5.6-terra`, reasoning `high`.
- `EFFICIENT` → `gpt-5.6-luna`, reasoning `high`.

**CtrlAltDelegate must never request Sol above `high`.** `xhigh` and `max` are explicitly forbidden for Sol even if the API/harness supports them. This is a methodology ceiling, not a statement about model capability.

For another provider/harness, resolve current equivalents at runtime. Never guess a model ID. If per-subagent model choice is unsupported, inherit the active model while preserving separate roles, fresh contexts, independent review and all control-plane gates.

## Default coding route

A complete, bounded zero-context Job Contract should normally start on `EFFICIENT`. This is deliberate: detailed planning transfers architectural interpretation out of the worker and into the contract.

Promote to `BALANCED` before dispatch when material cross-layer reasoning, public-contract integration or other complexity is intrinsic to the job. Promote to `FRONTIER` only when frontier judgment is genuinely required or lower classes have failed to make objective progress.

Do not route a weakly specified job to a stronger model as a substitute for fixing the plan. A material contract gap returns to planning/rebrief.

## Escalation

```text
EFFICIENT
  ↓ failed attempt / no objective progress / complexity evidence
BALANCED
  ↓ unresolved critical reasoning / repeated failure
FRONTIER
```

Escalation creates a fresh attempt. Preserve the same objective, acceptance criteria, scope and authority unless scoped change control explicitly changes them. Attach the previous attempt's failing evidence; do not make the stronger worker rediscover history from chat.

A model swap inside a running attempt is not allowed because it destroys attempt attribution.

## Review independence

The main orchestrator is not an independent reviewer of work whose plan/brief it authored.

For standard substantive work:

```text
EFFICIENT/BALANCED IMPLEMENTER
        ↓
EFFICIENT MECHANICAL VALIDATOR
        +
BALANCED FRESH SEMANTIC REVIEWER
        ↓
FRONTIER ORCHESTRATOR adjudicates and integrates
```

For critical work, require a fresh `FRONTIER` reviewer. That reviewer must be a distinct agent/context from both the implementer and persistent main orchestrator.

The main orchestrator may inspect everything and reject work, but its own inspection does not satisfy an independent-review gate.

## Routing decision factors

Select a class from the job, not from a generic project label alone. Consider:

- completeness of the Job Contract and acceptance oracles;
- architecture/public-interface judgment still required inside implementation;
- reversibility and blast radius;
- security/privacy/data-loss consequences;
- cross-layer and seam complexity;
- prior attempt evidence and no-progress signals;
- whether the task is synthesis/judgment versus mechanical checking.

Cost may break ties between classes that satisfy the quality floor. Cost must never lower the required assurance class.

## Planning/Handoff responsibilities

The Custom GPT and GitHub-native planner compile into every material job:

- `minimum_model_class`;
- `requested_model_class`;
- reasoning effort (`high` max for CtrlAltDelegate-selected GPT-5.6 routes);
- promotion triggers;
- independent reviewer class;
- why the selected class is sufficient.

The plan therefore determines not only **what** a worker does, but also the minimum reasoning tier appropriate to the remaining ambiguity/risk.

## Runtime state and evaluation

Persist actual class/model resolution and per-attempt outcomes in `planning/execution/MODEL-ROUTING-STATE.yaml`. When the harness exposes usage, record tokens/cost/time together with first-pass acceptance, repair rounds, scope violations and review findings.

Routing policy should evolve from held-out evaluation and real project evidence. Do not optimize solely for cheapest successful demo runs; regressions in correctness, scope or repair rate block a down-route.

## Invariants

1. Deterministic control state outranks model self-report.
2. Main orchestrator is normally spawn-only.
3. Default bounded implementation is `EFFICIENT`.
4. Complex implementation/review can route `BALANCED`.
5. Critical judgment/review/debugging can route `FRONTIER`.
6. Sol reasoning effort is never above `high`.
7. Independent review always uses a fresh agent/context.
8. Main orchestrator never receives independent-review credit.
9. A routing escalation is a new attributable attempt.
10. Unsupported per-agent model routing degrades to inherited-model role separation, not broken execution.
