# Update Public CtrlAltDelegate Repository to V5.9.2

You are the release coding agent. Update `raffnix204/CtrlAltDelegate` to **V5.9.2**, validate the complete framework, commit it and push/merge it to remote `main`. Work autonomously unless a real permission, policy or destructive conflict requires the user.

## Release input

- Run from the actual checked-out CtrlAltDelegate repository root.
- Release archive: `./software-planning-lead-v5.9.2-github-native.zip` or the exact supplied path.
- The package is cumulative over V5.9.1 and can be safely reconciled against the currently published V5.9 baseline or an already-applied V5.9.1 working baseline. Never reset a newer compatible repository to the observed old SHA.

## Non-negotiable safety

1. Inspect `git status`, current branch, remotes and `HEAD`; preserve unrelated/dirty user work. Never `reset --hard`, `clean`, or discard unrelated changes.
2. Validate ZIP paths before extraction; reject absolute/traversal/device/unsafe-symlink members.
3. Extract outside the tracked repository and read `RELEASE-METADATA.json`, `CHANGELOG-V5.9.2.md`, `RELEASE-MANAGED-PATHS.txt`, `AGENTS.md` and this handoff first.
4. Treat `RELEASE-MANAGED-PATHS.txt` as the release overlay allow-list. Never delete repo-owned files merely because they are absent from the ZIP.
5. Preserve `.git/`, branding/assets, GitHub metadata, historical changelogs and unrelated project files.
6. For a release-managed path changed independently since the compatible baseline, diff and merge semantics; do not blindly overwrite newer compatible work.

## Required V5.9.2 semantic outcome

The resulting repository must retain all V5.9.1 research/feasibility/planning-compiler/execution gates and additionally enforce:

- one persistent **FRONTIER main orchestrator** that is normally spawn-only;
- `EFFICIENT` as default bounded implementation/research/mechanical-validation worker class;
- `BALANCED` for complex implementation, semantic review and first debugger escalation;
- `FRONTIER` for intrinsic critical judgment, critical fresh review and final debugger escalation;
- OpenAI reference mapping `FRONTIER=gpt-5.6-sol`, `BALANCED=gpt-5.6-terra`, `EFFICIENT=gpt-5.6-luna`;
- all CtrlAltDelegate-selected GPT-5.6 routes use reasoning `high`;
- **Sol MUST NEVER be requested above `high`; `xhigh` and `max` are forbidden**;
- persistent main orchestrator does **not** satisfy independent-review gates;
- standard substantive work gets a fresh semantic reviewer, normally BALANCED; critical work gets a fresh FRONTIER reviewer distinct from implementer and main orchestrator;
- model escalation `EFFICIENT → BALANCED → FRONTIER` creates a fresh attempt with failure evidence, never an invisible mid-attempt switch;
- unsupported per-subagent model selection falls back to inherited model while preserving role/context separation and every quality gate;
- canonical skill count stays exactly 154.

## Merge

1. Verify `RELEASE-MANIFEST.sha256`.
2. Merge all release-managed paths, including the delivery-template mirrors.
3. Keep `.agents/skills` canonical and `.claude/skills` as thin adapters.
4. Add `CHANGELOG-V5.9.2.md`; preserve older changelogs.
5. Preserve executable bits for Python/hooks where applicable.
6. Confirm no Custom-GPT Knowledge bundle is published into GitHub Native.

## Required validation

Run at minimum:

```bash
python3 scripts/validate_system.py
python3 scripts/validate_release_claims.py
python3 scripts/validate_v591_release.py
python3 scripts/validate_v592_model_routing.py
python3 scripts/validate_v592_release.py
python3 scripts/validate_planning.py
python3 scripts/validate_control_plane.py
python3 scripts/validate_assurance_control.py
python3 scripts/validate_skill_evals.py
python3 scripts/validate_v58_architecture.py
python3 scripts/validate_v59_control_plane.py
```

Also run all other existing release/system validators that remain applicable. Do not weaken an old gate merely to pass. If an old validator intentionally prohibited model routing, update it consistently with the V5.9.2 capability-class contract and rerun.

Verify counts:

```bash
find .agents/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
find .claude/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
```

Both must be `154`.

Explicitly grep release-controlled current-policy files to prove there is no instruction that requests Sol `xhigh` or `max`. Historical research/changelog text may mention those API-supported effort names only when it clearly states they are forbidden by CtrlAltDelegate.

## Review before commit

- `git diff --check`
- inspect `git diff --stat` and material diffs
- confirm branding and unrelated files were not removed
- confirm `MODEL-ROUTING-POLICY.yaml`, Worker/Job templates, AGENTS and delivery-template agree
- confirm the main orchestrator cannot receive independent-review credit
- confirm V5.9.1 feasibility/Plan Checker/parent-reverification controls still exist
- confirm manifests and release claims match the actual diff

## Commit / push

Commit only intended release changes:

```text
release: CtrlAltDelegate v5.9.2
```

Push through the repository's permitted path. If direct `main` is protected, create a release branch/PR, satisfy checks and merge normally. Never bypass protection.

Afterward fetch remote `main` and report:
- final remote SHA;
- branch/PR path used;
- validation results;
- 154/154 skill/adapter counts;
- any reconciled post-baseline changes;
- confirmation that V5.9.2 is on remote `main` and Sol is capped at `high`.
