# Start Here — CtrlAltDelegate V5.9

CtrlAltDelegate GitHub Native is a standalone full-lifecycle planning and execution system. The Custom GPT is optional.

## Direct GitHub Native

Start the coding agent from this repository root, read `AGENTS.md`, inspect `planning/execution/STATE.md`, run lifecycle mode detection (`FULL_LIFECYCLE` for a fresh project), and continue from the earliest unresolved gate through `COMPLETED`.

## Custom-GPT planning handoff

For an existing target project, copy `ctrlaltdelegate-delivery.zip` into that project's root and start the coding agent from the project root. Paste the generated Coding-Agent Start Prompt. The agent safely extracts the package to `./.ctrlaltdelegate/`, keeps it separate from product files, adds the local-control ignore rules without replacing the project's existing `.gitignore`, validates the handoff, and then implements into the project root.

Do not manually rename the ZIP or control root. Do not commit the ZIP or `.ctrlaltdelegate/` to the target application repository under the default `LOCAL_PRIVATE` visibility policy.


## V5.9 skill-driven planning

Relevant specialist skills participate while planning decisions are made, not only after planning. Run an early capability scan during intake/discovery, consult the smallest complete planning skill set for the current phase, persist consultations in `planning/context/PLANNING-SKILL-STATE.yaml`, and refresh routing whenever scope, research or stack evidence changes. Use `config/PLANNING-SKILL-ROUTING.yaml` and `docs/system/SKILL-DRIVEN-PLANNING.md`. The final coding-agent skill pool continues from these decisions.


## V5.9.3 additions

- Oh My Pi (`omp`) is a first-class Pi-derived harness with native task batching, structured worker results, isolated worktrees and model routing.
- Run code-intelligence preflight early; when Graphify is ready, query the graph before broad source traversal. If Graphify is missing, ask once before any host-wide install.
Before architecture freeze resolve `planning/architecture/TECHNOLOGY-EVALUATION.yaml`. Before jobs requiring external acquisition/browser/tooling, inventory `CAPABILITY-STATE.json`; bootstrap only the missing verified capability.

V5.9 runtime skill escalation: if a worker discovers missing expertise, use `config/SKILL-ESCALATION-POLICY.yaml`; L0/L1 do not imply full replanning, while semantic changes escalate to rebrief/change control.
## V5.9 execution-control invariant

Do not edit controller-owned execution state directly. Before dispatch, reconcile state; claim the job with a lease; start a distinct attempt; heartbeat long-running work; require a schema-valid Worker Result; then settle through controller operations. Treat `DONE` as a derived, revalidated claim rather than worker authority. `IMPLEMENTED_UNVERIFIED` may release implementation-only dependencies, but never verified dependencies. Use `UNVERIFIABLE` when current evidence cannot prove a claim, attach required follow-up evidence, and continue all safe dependency-ready work. Repeated failure without objective work-product progress requires a strategy change. Where the active harness supports a blocking stop hook, use the progress-aware stop gate; otherwise report enforcement as advisory/observed rather than pretending it is enforced.

