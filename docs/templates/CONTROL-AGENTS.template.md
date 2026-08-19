# CtrlAltDelegate V5.7.1 — Imported Control Package Instructions

This file belongs to an imported Custom-GPT planning handoff. The coding agent runs from the real application repository root, not from this directory.

## Fixed roots
- `PROJECT_ROOT=.` — target application/Git root.
- `INBOUND_PACKAGE=./ctrlaltdelegate-delivery.zip`.
- `CONTROL_ROOT=./.ctrlaltdelegate`.
- `PLANNING_ROOT=./.ctrlaltdelegate/planning`.
- `SKILLS_ROOT=./.ctrlaltdelegate/.agents/skills`.

Application code, tests and normal project configuration belong in `PROJECT_ROOT`. CtrlAltDelegate planning/control/evidence belongs in `CONTROL_ROOT`. Do not redesign the target repository into the control directory.

## Authority and startup
1. Preserve platform/user instructions and the target repository's own applicable AGENTS/CLAUDE/project rules.
2. Validate `CONTROL-PACKAGE.json`, `planning/handoff/HANDOFF-STATUS.yaml` and `planning/execution/PLANNING-BASELINE.json`.
3. Treat the resolved planning baseline as authoritative unless real repository/runtime evidence materially contradicts it.
4. Read only job-relevant planning, ADR, research and skills progressively.

## V5.7.1 control plane
Use:
- `config/LOOP-CONTRACTS.yaml` + `planning/execution/LOOP-STATE.json`;
- `planning/execution/JOB-GRAPH.json`;
- `config/SURFACE-POLICY.yaml`;
- append-only `planning/execution/DECISION-LEDGER.jsonl`;
- `planning/execution/ARTIFACT-CONSISTENCY.json`;
- `config/HARNESS-CONFORMANCE.yaml`;
- `planning/execution/PENDING-INPUT.jsonl` at safe orchestration boundaries.

Do not blind-retry same-state/same-failure work with no new evidence. Change strategy or escalate. Fast feedback gates do not replace the final acceptance gate. Locked/human-controlled surfaces require their owning workflow/authority. Instructions are not enforcement: use native sandbox/permissions/tool filters/Git/CI when available and record partial enforcement honestly.

## Jobs and workers
Dispatch only dependency-ready jobs and only to workers/harnesses with proven required capabilities. Respect allowed/protected/prohibited scopes, single-writer surfaces and done-when/evidence requirements. Use checkpoint/resume for long work and reconcile actual files/Git/evidence after worker loss.

## Harnesses
Pi is reference; Codex is first-class; DeepSeek Harness is first-class preview; Claude Code/OpenCode are compatible. Imported handoffs keep skills under `SKILLS_ROOT`; load routed skills directly from there. When a harness supports a non-invasive session/profile custom skill directory, it may map `SKILLS_ROOT` natively. Do not copy the full library into the application tree merely for discovery.

## Git hygiene
Default control visibility is `LOCAL_PRIVATE`. After successful root-drop import, retain the source archive under `./.ctrlaltdelegate/inbox/ctrlaltdelegate-delivery.zip` rather than leaving it beside product files. Preserve the target `.gitignore` and keep the inbound ZIP, `CONTROL_ROOT` and temporary import roots out of the application repository history. Never delete or replace unrelated project ignore rules.

## Completion
Continue through implementation, verification, documentation, Git/GitHub integration and convergence until `COMPLETED`. Ask the user only for a true product/business/safety/external hard stop.
