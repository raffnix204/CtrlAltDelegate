# CODING-AGENT-HANDOFF — V5.6.4

Canonical project handoff is `planning/handoff/CODING-AGENT-HANDOFF.md`.

From repository root read `AGENTS.md`, then that canonical handoff, then `planning/execution/STATE.md`. Do not rely on this root pointer as execution state. The versioned `planning/` tree is persistent project memory and must remain current throughout implementation.


V5.6.4 planning baseline includes `planning/discovery/` preference/constraint state; preserve resolved constraints during execution.

V5.6.4 additionally requires `planning/execution/EXECUTION-PROFILE.yaml`: right-size orchestration to project/risk and use progress-aware worker liveness/checkpoint-resume rather than treating a static elapsed duration as proof of a stalled subagent.

For a fresh standalone `NOT_STARTED` checkout, start with root `START-HERE.md`; this pointer is for execution-ready handoff/resume semantics.
