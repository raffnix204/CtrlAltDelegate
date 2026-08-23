# CtrlAltDelegate V5.9 — Public GitHub Repository Update Handoff

Update `https://github.com/raffnix204/CtrlAltDelegate` from **`software-planning-lead-v5.9-github-native.zip`**. Complete the work autonomously through validation, commit and remote push/PR unless a genuine credential, branch-protection or human-approval boundary prevents it.

## Safety and authority

- Verify the actual Git repository root, `origin`, branch and status before any write. Stop rather than modify the wrong repository.
- Validate the archive before extraction; reject absolute paths, traversal, links/symlinks or unexpected topology. It must contain exactly one top-level directory: `software-planning-lead-v5.9-github-native/`.
- Extract outside the repository working tree.
- Treat release-managed CtrlAltDelegate files as authoritative, but perform a **controlled merge**, never delete-and-replace.
- Preserve unrelated repository material and protect `.github/**`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md` and unrelated branding/assets unless the release manifest explicitly manages a changed path.
- Merge `.gitignore` non-destructively. Never use `git reset --hard`, destructive `git clean` or force-push to discard state.

## Required inspection and merge

Read `RELEASE-FILE-MANIFEST.json`, `PACKAGE-MANIFEST.md`, `CHANGELOG-V5.9.md`, `release/RELEASE-CLAIMS.yaml`, `release/RELEASE-DELTA.json`, and this handoff. Add/update only release-managed files whose bytes differ. Remove an obsolete path only when ownership and the V5.9 release delta prove intentional removal.

Verify the V5.9 control-plane surfaces are present, including revisioned mutation state/receipts, worker claims/leases, attempt state/history, recovery/reconciliation logs, planning convergence/artifact graph, structured Worker Result schema, review verdicts, objective verification attribution, stop/surface enforcement, control-effectiveness state, and trigger-first skill discovery QA.

Canonical library must remain 154 skills with 154 thin Claude adapters and 147 progressive references unless the release evidence explicitly proves otherwise.

## Mandatory QA after merge

Run at minimum:

```bash
python3 scripts/validate_system.py
python3 scripts/validate_skill_evals.py
python3 scripts/validate_skill_discovery.py
python3 scripts/validate_control_plane.py
python3 scripts/validate_assurance_control.py
python3 scripts/validate_v58_architecture.py
python3 scripts/validate_v581_hardening.py
python3 scripts/validate_v582_completion.py
python3 scripts/validate_v59_control_plane.py
python3 scripts/validate_control_mutation.py
python3 scripts/validate_release_claims.py --git
python3 scripts/harness_preflight.py --json
```

A missing optional harness executable is not by itself a release failure. Then run `git diff --check`, inspect `git status --short`, `git diff --stat`, and the complete diff. Check for unrelated deletions, protected-file drift, stale active-version references, generated junk, and release claims inconsistent with the real Git diff.

Do not proceed with a mandatory validator failure. Correct safe release-integration problems, rerun the affected checks, then rerun the complete final gate.

When green, create one descriptive commit such as:

`release: update CtrlAltDelegate to v5.9`

Push under the repository's normal branch policy. If direct push is permitted, push it; if protection requires a PR, create/push a release branch and open the PR without weakening protection. Verify the remote commit/PR actually exists.

## Completion report

Report only after remote verification: branch, final remote commit SHA (or PR/merge identity), validation results, changed-file summary, confirmation that protected/unrelated files were preserved, and any genuine remaining external blocker. A local commit is not completion.
