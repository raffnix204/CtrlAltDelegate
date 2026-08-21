# V5.7.2 — Debug Depth, Independent Assurance & Context Integrity

## Highlights

- Added behavior-derived regression oracles: acceptance tests are derived from observable requirements/defects, not from the proposed patch mechanism.
- Added `ROOT_CAUSE_DEPTH_GATE` with persisted deepest-cause / proposed-fix-boundary reconciliation for substantive debugging.
- Added explicit blind independent-assurance semantics (`author_independent`, `sibling_verdict_blind`, `candidate_claims_untrusted`).
- Split work-size orchestration from assurance depth via `NORMAL | ELEVATED | HIGH | CRITICAL`.
- Added hash-bound compact worker briefs and `STALE_BRIEF` fail-closed handling.
- Added harness capability-attestation caching bound to runtime/version/config/permissions/adapter identity.
- Added collect-persist-terminate worker lifecycle guidance.
- Added seven system-regression evals covering the new assurance/integrity behavior.
- Preserved V5.7.1's 154-skill library, Skill-Driven Planning, ZIP-drop control plane, website content planning and DeepSeek Harness support.

## Evidence boundary

The architecture was informed by `Spielewoy/autoprompt-skill`, especially its independent verification, depth-lock, pointer-brief and capability-attestation patterns. CtrlAltDelegate intentionally does **not** adopt universal strict TDD, universal >=95% coverage, fixed persona hierarchies or model routing.
