# Update Public CtrlAltDelegate Repository to V5.9.1

You are the release coding agent. Update the existing public repository `raffnix204/CtrlAltDelegate` from its current compatible V5.9 baseline to **V5.9.1**, validate it, commit it and push it to GitHub. Work autonomously unless a true permission/policy/destructive blocker occurs.

## Compatibility
This V5.9.1 package supersedes the prior `software-planning-lead-v5.9-github-native.zip`; do not downgrade or reset to that archive.

## Inputs
- Run from the actual checked-out repository root.
- Release archive: `./software-planning-lead-v5.9.1-github-native.zip` (or the exact supplied V5.9.1 GitHub-native ZIP path).
- Expected observed upstream baseline when this package was built: `a9927f84dad25f55f827c48ae3268fcf8b8bec6d`. A newer compatible `main` is not a reason to reset; reconcile it.

## Non-negotiable safety
1. Inspect `git status`, branch, remotes and current `HEAD`. Never reset/clean/discard unrelated work.
2. If the tree contains unrelated user changes, preserve them. Do not absorb them into the release commit unless they are already intentional release work.
3. Validate ZIP members before extraction: reject absolute paths, `..` traversal, device files and unsafe symlinks.
4. Extract the release to a sibling/temp directory, **not directly over the repository**.
5. Read `RELEASE-METADATA.json`, `CHANGELOG-V5.9.1.md`, `AGENTS.md` and this handoff from the extracted release before merging.
6. Treat the release archive as an allow-list overlay. Update/create only paths present in `RELEASE-MANAGED-PATHS.txt`. Never delete repository files merely because they are absent from the ZIP.
7. Preserve repository-owned/branding/history assets not explicitly release-managed, especially `.git/`, `assets/branding/`, old release changelogs, GitHub metadata and unrelated project files.
8. Do not replace an existing file blindly if current `main` contains a post-baseline change. Diff it, preserve compatible newer work, then integrate V5.9.1 semantics.

## Required semantic outcome
The repository must expose and enforce V5.9.1 hardening:
- recurring domain/feasibility/stack/adversarial/freshness research;
- fail-closed feasibility for critical capabilities (`UNPROVEN` -> proof/spike before broad dependent implementation);
- planning compilation to zero-context Job Contracts;
- independent Plan Checker + cold-start implementability gate;
- pre-authored observable verification gates;
- exact baseline/candidate review target + parent re-verification;
- fail-closed write scope;
- explicit integration/seam nodes;
- bounded expert-reread/defect-hunt loop and no-progress strategy change;
- execution Research Drift -> scoped replan/rebrief when strategic assumptions are refuted;
- unchanged canonical skill count of 154 and no core model routing.

## Merge procedure
1. Create a temporary extraction directory outside the tracked repo tree if practical.
2. Verify `RELEASE-MANIFEST.sha256` inside the extracted release.
3. Compare every release-managed file against the working repository.
4. Merge the release overlay. Preserve executable bits for `scripts/*.py` where supported.
5. Ensure `.agents/skills` remains canonical and exactly 154 `*/SKILL.md` entrypoints; `.claude/skills` remains thin adapters.
6. Keep old release changelogs; add `CHANGELOG-V5.9.1.md`. Update `CHANGELOG-SYSTEM.md` only if the repository's existing format requires an index entry; do not erase history.
7. Keep branding/logo references intact.

## Validation
Run at minimum:
```bash
python3 scripts/validate_system.py
python3 scripts/validate_release_claims.py
python3 scripts/validate_v591_release.py
python3 scripts/validate_planning.py
```
`validate_planning.py` must pass framework/template structure; an untouched package may report `PLANNING TEMPLATE OK (NOT_STARTED/NOT_READY)`. Also verify:
```bash
find .agents/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
find .claude/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
```
Both counts must be 154.

Run any existing V5.9 repository validators that remain present (`validate_control_plane.py`, `validate_assurance_control.py`, skill eval/release validators, etc.). Do not weaken/delete old tests merely to make the patch green. If an existing validator conflicts with the intended V5.9.1 contract, update the validator and corresponding docs consistently, then rerun.

## Review before commit
- Inspect `git diff --check` and `git diff --stat`.
- Confirm no unrelated files/branding were removed.
- Search release-controlled files for stale user-facing `V5.9` current-version claims; historical changelogs/provenance may retain historical references.
- Confirm the new research/feasibility and parent-reverification rules appear in both root/runtime guidance and machine-readable config/templates.
- Confirm no Custom-GPT Knowledge files were published into the GitHub-native repo.

## Commit and push
Commit only the intended release changes using:
```text
release: CtrlAltDelegate v5.9.1
```
Then push to the repository's normal `main` path when repository policy and credentials allow it. If branch protection requires a PR, create a release branch, push it, open the PR, satisfy required checks, merge through the permitted path, then verify remote `main`. Never bypass protection.

After push/merge, fetch/verify remote `main` and report:
- final remote commit SHA;
- validation commands and results;
- skill/adaptor counts;
- any preserved post-baseline merge decisions;
- exact GitHub branch/PR path used;
- confirmation that V5.9.1 is on remote `main`.
