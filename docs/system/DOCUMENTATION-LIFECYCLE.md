# Documentation Lifecycle — V5.9

Documentation is versioned product behavior. The repository must never intentionally push code/config newer than its affected documentation.

## Lifecycle
`STAGED CHANGE → DOCS IMPACT → UPDATE/ATTEST → DOCS_FRESHNESS_GATE → COMMIT → PRE_PUSH_GATE → PUSH → WAVE DOC REVIEW → FINAL FRESH-USER REVIEW`

## Per-commit invariant
Every commit that changes code/config/build/runtime/infrastructure either updates affected canonical docs in the same commit or records `Documentation Impact: NONE` with a concrete reason and staged-diff fingerprint in `planning/execution/DOCUMENTATION-STATE.yaml`.

Impact classes: `NONE | USER | INSTALLATION | CONFIGURATION | API | MIGRATION | OPERATOR | SECURITY | RELEASE`. Multiple classes may apply.

The canonical docs may include root README, getting-started/install/configuration/usage/API/operator/security/migration/troubleshooting guides, changelog/release notes, runbooks, and project-native equivalents. One fact has one canonical owner; other docs link instead of drifting copies.

## README contract
Root README is beginner-first and always current. It explains what the project is, what every major current user-visible feature does, prerequisites, installation, first setup, configuration, start/stop, complete major-feature usage, examples, data/network/ports where relevant, upgrade/backup/uninstall, troubleshooting, and links to deeper docs. Keep advanced detail in `docs/` but make every feature discoverable from README or its linked navigation.

Maintain `planning/execution/DOCUMENTATION-COVERAGE.md` mapping user/operator capabilities to canonical docs. User-visible feature changes update coverage in the same wave.

## Mechanical guard
Run `scripts/install_git_guards.py` once per repository. If no conflicting hooks configuration exists it activates `.githooks/pre-commit` and `.githooks/pre-push`. If an existing hook system exists, preserve it and integrate the two guard commands into that system; never overwrite unrelated hooks.

Before staging the final commit contents, record impact with `scripts/docs_freshness_gate.py --record --impact ...`. The pre-commit hook validates the attestation against the actual staged diff. The pre-push hook checks commits being pushed and blocks code/config commits that skipped the gate.

Mechanical checks are defense in depth; the agent still owns semantic truth.

## Verification
Before each validated wave is integrated, verify all docs affected by that wave. Before `COMPLETED`, spawn a fresh documentation/fresh-user reviewer that starts from README and linked docs and attempts the relevant clean install/setup/use path. `DOCUMENTATION_READY` is required for completion and the validated docs must be on remote `main` with the code they describe.
