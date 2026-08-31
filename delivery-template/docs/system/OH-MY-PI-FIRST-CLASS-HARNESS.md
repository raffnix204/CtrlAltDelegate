# Oh My Pi First-Class Harness — V5.9.3

## Status

`Oh My Pi (OMP)` is a `FIRST_CLASS` CtrlAltDelegate harness. It inherits the Pi behavioral methodology but has its own capability adapter because OMP exposes materially richer runtime surfaces than generic Pi compatibility alone.

OMP already discovers repository `AGENTS.md` plus `.agent/.agents` skills/rules and therefore consumes the canonical CtrlAltDelegate `.agents/skills` library without a duplicate skill tree.

## Why a separate adapter exists

CtrlAltDelegate uses OMP-specific capabilities when runtime attestation confirms them:

- native `task` subagents, including batch fan-out and async/background execution;
- per-subagent model selection/overrides;
- structured output schemas for Worker Result contracts;
- isolated worktrees/patch capture for concurrent writers;
- live/persisted agent identities and typed task result metadata;
- LSP/DAP/editor-grade code surfaces where the active OMP build exposes them;
- advisor/review surfaces as supplemental independent signals.

The control plane remains CtrlAltDelegate. OMP does not replace `JOB-GRAPH.json`, attempt leases, exact change-set review targets, parent re-verification, convergence or stop gates.

## Dispatch mapping

For a ready wave, the main orchestrator compiles independent Job Contracts into OMP `task` items. Shared immutable project/job background goes in batch context; each task carries a self-contained Worker Brief, agent role, structured result schema and isolation requirement.

Use batch fan-out only when dependencies, write ownership and integration bottlenecks permit parallelism. Parallel writers should use isolated worktrees when available.

Worker/task return means **execution finished**, not `DONE`. The parent freezes the exact candidate branch/patch/SHA/file set, re-runs applicable gates, obtains fresh independent review and only then settles the CtrlAltDelegate attempt.

## Model routing

The generic CtrlAltDelegate classes remain canonical:

- `FRONTIER` — main orchestrator, critical judgment/review, final debugger escalation;
- `BALANCED` — complex implementation, semantic review, debugging;
- `EFFICIENT` — default bounded implementation/research/mechanical validation.

OMP can map roles/model selectors natively. For the OpenAI GPT-5.6 reference mapping, use Sol/Terra/Luna at `high`.

### Sol ceiling caveat

OMP's generic task `effort: hi` maps to the highest reasoning effort supported by the resolved model. That may be higher than `high`. Therefore an OpenAI `FRONTIER` dispatch must resolve the exact Sol model and explicitly bind `:high`; never use generic `effort: hi` as a substitute. `xhigh` and `max` remain forbidden for Sol.

## OMP sticky rules

The GitHub-native distribution includes `.omp/RULES.md` with only a small set of hard CtrlAltDelegate invariants. It does not duplicate the full `AGENTS.md`; OMP already discovers the root file.

## Graphify interaction

OMP and Graphify are complementary. OMP is the execution harness; Graphify is the preferred code-intelligence provider. When Graphify is ready, OMP workers should query the current graph before broad source traversal, then confirm material findings in source/LSP/tests/runtime.

## Conformance

Before relying on OMP-native behavior, attest the current binary/version and required capabilities. Missing optional capability causes scoped degradation; missing capability that a job requires triggers normal rerouting or a blocker rather than a fabricated success claim.
