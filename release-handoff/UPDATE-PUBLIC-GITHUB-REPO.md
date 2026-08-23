# CtrlAltDelegate V5.8.2 — Public GitHub Repository Update Handoff

Update the public repository `https://github.com/raffnix204/CtrlAltDelegate` from the supplied archive **`software-planning-lead-v5.8.2-github-native.zip`**. Perform the work autonomously through validation, commit and push unless a real credential/branch-protection/human-approval boundary blocks you.

## Authority and safety

- The release archive is authoritative for CtrlAltDelegate-managed system/runtime/planning/skill/config/eval/template/adapter files and the canonical V5.8.2 `README.md`.
- The existing GitHub repository is authoritative for repository-specific branding/presentation and unrelated files.
- **Do not replace the repository wholesale.** Do not modify files whose bytes are already identical.
- Protect `assets/**`, `.github/**`, `LICENSE`, `CONTRIBUTING.md`, and `SECURITY.md` unless the release manifest explicitly marks a specific file as managed/changed. The V5.8.2 README is intentionally managed and must be updated from the release.
- Preserve unrelated local/user changes. Never `git reset --hard`, clean untracked work, or force-push to discard state.

## Procedure

1. Start from the actual CtrlAltDelegate repository root. Verify `git rev-parse --show-toplevel`, remote `origin`, current branch, `git status --short`, and fetch current remote state. If this is not `raffnix204/CtrlAltDelegate`, stop rather than updating the wrong repository.
2. Locate `software-planning-lead-v5.8.2-github-native.zip`. Validate it as a ZIP and reject unsafe members (absolute paths, `..`, symlink/path traversal). The archive must contain exactly one top-level directory named `software-planning-lead-v5.8.2-github-native/`.
3. Extract to a temporary directory **outside the repository working tree**. Do not run code from the ZIP before inspection.
4. Read `RELEASE-FILE-MANIFEST.json`, `PACKAGE-MANIFEST.md`, `CHANGELOG-V5.8.2.md`, and this handoff. Treat the merge policy in the release manifest as the ownership contract.
5. Compare the extracted release with the repository. Copy/add only managed files whose content differs. `README.md` is managed and should become the canonical V5.8.2 README. Merge `.gitignore` non-destructively; preserve existing entries. Preserve protected repo-specific files.
6. Delete an old path only when the current or previous release manifest proves it is CtrlAltDelegate-owned and V5.8.2 intentionally removes/replaces it. Otherwise leave it alone.
7. Ensure canonical `.agents/skills` and thin `.claude/skills` adapters match the release. Do not create duplicate skill libraries for Command Code or DeepSeek Harness.
8. Run at minimum:
   - `python3 scripts/validate_system.py`
   - `python3 scripts/validate_skill_evals.py`
   - `python3 scripts/validate_control_plane.py`
   - `python3 scripts/validate_assurance_control.py`
   - `python3 scripts/validate_v58_architecture.py`
   - `python3 scripts/validate_v581_hardening.py`
   - `python3 scripts/validate_v582_completion.py`
   - `python3 scripts/validate_release_claims.py --git`
   - `python3 scripts/harness_preflight.py --json` (a missing optional harness binary is not a release failure)
9. Review `git diff --check`, `git status --short`, `git diff --stat`, and the actual diff. Specifically check for accidental asset/branding changes, unrelated deletions, stale pre-V5.8.2 active-version references, and generated junk.
10. If validation passes, create one descriptive commit such as `release: update CtrlAltDelegate to v5.8.2`. Push through the repository's normal branch/PR policy. Do not weaken branch protection. If direct push is allowed by current policy, push it. If policy requires a PR, create/push the branch and open the PR instead.
11. Verify the remote commit/PR exists and report: branch, commit SHA, validation results, files changed, and any protected files intentionally preserved.

## Completion rule

Do not report success until the remote update is verifiably pushed (or a policy-required PR is verifiably opened) and all required release validators pass. A local commit alone is not completion.


V5.8.2 release-integrity requirement: run `python3 scripts/validate_release_claims.py --git` after the controlled merge and before commit/push. It must verify the real repository diff against `release/RELEASE-CLAIMS.yaml` and `release/RELEASE-DELTA.json`.
