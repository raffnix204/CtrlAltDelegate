# Oh My Pi First-Class Adapter — V5.9.3

Oh My Pi (`omp`) is a Pi-derived coding-agent harness with its own first-class task/subagent, model-role, LSP/DAP, worktree, structured-output and review surfaces. CtrlAltDelegate reuses the Pi behavioral methodology but treats OMP as a separate `FIRST_CLASS` harness so these native capabilities can be used deliberately rather than merely tolerated through generic Pi compatibility.

## Native surfaces used

- root `AGENTS.md` and canonical `.agents/skills/` discovery;
- `task` batch fan-out for independent ready jobs;
- per-subagent model selection/overrides;
- structured output schemas for Worker Result contracts;
- isolated worktrees/patch metadata for parallel writers;
- background task execution and typed result metadata;
- optional advisor/review capabilities as supplemental evidence.

## Critical model-routing caveat

OMP's generic task `effort: hi` means the highest reasoning level supported by the resolved model. That can exceed `high`. CtrlAltDelegate therefore never uses generic `hi` for an OpenAI FRONTIER/Sol worker. Resolve the exact Sol selector and bind `:high`; `xhigh` and `max` remain forbidden by `config/MODEL-ROUTING-POLICY.yaml`.

## Authority

OMP scheduler/session success is not CtrlAltDelegate completion. `JOB-GRAPH`, attempt state, exact change-set, parent re-verification, independent review, integration nodes and convergence remain authoritative.
