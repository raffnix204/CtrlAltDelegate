# CODING-AGENT-HANDOFF — V5.9

Canonical project handoff is `planning/handoff/CODING-AGENT-HANDOFF.md`.

From repository root read `AGENTS.md`, then that canonical handoff, then `planning/execution/STATE.md`. Do not rely on this root pointer as execution state. The versioned `planning/` tree is persistent project memory and must remain current throughout implementation.


V5.9 planning baseline includes `planning/discovery/` preference/constraint state; preserve resolved constraints during execution.

V5.9 additionally requires `planning/execution/EXECUTION-PROFILE.yaml`: right-size orchestration to project/risk and use progress-aware worker liveness/checkpoint-resume rather than treating a static elapsed duration as proof of a stalled subagent.

For a fresh standalone `NOT_STARTED` checkout, start with root `START-HERE.md`; this pointer is for execution-ready handoff/resume semantics.


## V5.9 control surfaces
Use the canonical loop registry/state, machine-readable job graph, surface policy, decision ledger, artifact-consistency gate and harness-conformance profile. For Custom-GPT ZIP handoffs, import to `./.ctrlaltdelegate/` under `LOCAL_PRIVATE` Git visibility before execution.


## V5.9 planning-skill and authoritative-content handoff

Read `planning/context/PLANNING-SKILL-STATE.yaml` before execution. Treat recorded planning decisions as the result of the listed specialist decision surfaces, not as generic prose. Load the same canonical selected skills for implementation/review when their jobs remain relevant.

Files under `planning/content/pages/` with `status: approved` are authoritative product content. Preserve wording, factual claims, CTA intent, hierarchy and approved SEO metadata unless implementation proves a genuine conflict; route such conflicts through scoped change control instead of silently rewriting copy.
## V5.9 execution-control invariant

Do not edit controller-owned execution state directly. Before dispatch, reconcile state; claim the job with a lease; start a distinct attempt; heartbeat long-running work; require a schema-valid Worker Result; then settle through controller operations. Treat `DONE` as a derived, revalidated claim rather than worker authority. `IMPLEMENTED_UNVERIFIED` may release implementation-only dependencies, but never verified dependencies. Use `UNVERIFIABLE` when current evidence cannot prove a claim, attach required follow-up evidence, and continue all safe dependency-ready work. Repeated failure without objective work-product progress requires a strategy change. Where the active harness supports a blocking stop hook, use the progress-aware stop gate; otherwise report enforcement as advisory/observed rather than pretending it is enforced.

