# CODING-AGENT-HANDOFF — V5.8.1

Canonical project handoff is `planning/handoff/CODING-AGENT-HANDOFF.md`.

From repository root read `AGENTS.md`, then that canonical handoff, then `planning/execution/STATE.md`. Do not rely on this root pointer as execution state. The versioned `planning/` tree is persistent project memory and must remain current throughout implementation.


V5.8.1 planning baseline includes `planning/discovery/` preference/constraint state; preserve resolved constraints during execution.

V5.8.1 additionally requires `planning/execution/EXECUTION-PROFILE.yaml`: right-size orchestration to project/risk and use progress-aware worker liveness/checkpoint-resume rather than treating a static elapsed duration as proof of a stalled subagent.

For a fresh standalone `NOT_STARTED` checkout, start with root `START-HERE.md`; this pointer is for execution-ready handoff/resume semantics.


## V5.8.1 control surfaces
Use the canonical loop registry/state, machine-readable job graph, surface policy, decision ledger, artifact-consistency gate and harness-conformance profile. For Custom-GPT ZIP handoffs, import to `./.ctrlaltdelegate/` under `LOCAL_PRIVATE` Git visibility before execution.


## V5.8.1 planning-skill and authoritative-content handoff

Read `planning/context/PLANNING-SKILL-STATE.yaml` before execution. Treat recorded planning decisions as the result of the listed specialist decision surfaces, not as generic prose. Load the same canonical selected skills for implementation/review when their jobs remain relevant.

Files under `planning/content/pages/` with `status: approved` are authoritative product content. Preserve wording, factual claims, CTA intent, hierarchy and approved SEO metadata unless implementation proves a genuine conflict; route such conflicts through scoped change control instead of silently rewriting copy.
