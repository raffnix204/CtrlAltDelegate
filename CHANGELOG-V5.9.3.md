# CtrlAltDelegate V5.9.3

<!-- VERIFIED-RELEASE-CLAIMS: release/RELEASE-CLAIMS.yaml -->

Release date: 2026-08-30
Base release: V5.9.2
Public main baseline observed: `4e44a3a54a8d7be64dad5ef02a26316db373cee5`

## Summary

V5.9.3 is a harness/code-intelligence patch. It keeps the V5.9.2 feasibility, Planning Compiler, parent re-verification, hierarchical model-routing and Sol-`high` ceiling controls, while adding **Oh My Pi** as an explicit first-class Pi-derived harness and **Graphify** as the preferred persistent code-intelligence provider for non-trivial codebases.

Canonical skills: **154 -> 154**. Added canonical skills: **none**. OMP is implemented as a harness adapter and Graphify remains an external provider, so no canonical skill is added or duplicated.

## Oh My Pi first-class harness

- adds `oh-my-pi` as `FIRST_CLASS` in harness conformance;
- reuses root `AGENTS.md` and canonical `.agents/skills` rather than creating an OMP-specific skill copy;
- maps CtrlAltDelegate ready jobs to OMP native `task` batches when dependency/write ownership permits;
- uses structured `outputSchema` worker results and isolated worktrees/patch metadata when attested;
- records OMP task/model/result metadata while keeping CtrlAltDelegate controller state authoritative;
- ships a small `.omp/RULES.md` sticky hard-rule layer instead of duplicating the full system instructions.

### OMP/Sol effort safety

OMP `task` `effort: hi` means the highest supported effort for the resolved model and can therefore map above `high`. CtrlAltDelegate **must not** use generic OMP `hi` for OpenAI FRONTIER/Sol workers. Resolve the exact Sol selector and bind `:high`. The existing Sol `xhigh`/`max` prohibition remains unchanged.

## Graphify code intelligence

V5.9.3 adds a `CODE_INTELLIGENCE_PREFLIGHT` to every project.

For non-trivial code projects, when Graphify is available/approved:

`GRAPH BUILD/UPDATE -> query/path/explain -> targeted source/LSP -> implementation -> real verification`

Graphify is used for navigation, architecture/dependency tracing, read-first resolution and context compression. It is **not** an acceptance oracle; material claims still require source, tests, compiler, runtime/provider/browser/network evidence as applicable.

### Host install consent

Graphify host installation is a deliberate exception to the normal project-local tool rule:

- missing + no stored preference -> ask once: `HOST_ALWAYS | PROJECT_ONLY | NEVER`;
- `HOST_ALWAYS` may install the verified user-scope tool and generic Agent Skills integration without sudo/admin;
- `PROJECT_ONLY` keeps the executable under CtrlAltDelegate runtime/control storage;
- `NEVER` uses fallback navigation and suppresses repeat prompts on that host.

The reviewed baseline is `graphifyy==0.9.53` / Apache-2.0. Future upgrades require drift verification and a fresh smoke test.

## Graph lifecycle

- existing current `graphify-out/graph.json` is query-first and is not rebuilt per worker;
- multi-wave coding may use incremental update/watch;
- code-only structural refresh remains LLM-free when supported by Graphify;
- generated `graphify-out/` is ignored by Git by default;
- inferred/ambiguous graph relationships must be confirmed in source before consequential decisions.

## New control surfaces

- `adapters/oh-my-pi/*`
- `.omp/RULES.md`
- `docs/system/OH-MY-PI-FIRST-CLASS-HARNESS.md`
- `config/CODE-INTELLIGENCE-POLICY.yaml`
- `docs/system/CODE-INTELLIGENCE-AND-GRAPHIFY.md`
- `planning/execution/CODE-INTELLIGENCE-STATE.yaml`
- `docs/templates/CODE-INTELLIGENCE-STATE.template.yaml`
- `scripts/graphify_ctl.py`
- `scripts/validate_v593_integration.py`

## Preserved V5.9.2 controls

- recurring research and critical feasibility proof/spikes;
- Planning Compiler, Plan Checker and cold-start implementability;
- zero-context Job Contracts and pre-authored verification oracles;
- exact baseline/candidate review targets and fail-closed scope;
- worker claims -> parent re-verification -> fresh independent review;
- integration/seam nodes and Research Drift scoped replanning;
- `FRONTIER | BALANCED | EFFICIENT` model routing;
- OpenAI reference mapping Sol / Terra / Luna at `high`;
- Sol never above `high`;
- controller-owned execution state and convergence/evidence gates.
