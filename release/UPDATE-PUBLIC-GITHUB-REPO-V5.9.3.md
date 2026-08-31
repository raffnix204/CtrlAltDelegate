# Update Public CtrlAltDelegate Repository to V5.9.3

You are the release coding agent. Update `raffnix204/CtrlAltDelegate` to **V5.9.3**, validate the complete framework, commit it and push/merge it to remote `main`. Work autonomously unless a real permission, policy or destructive conflict requires the user.

## Release input

- Run from the actual checked-out CtrlAltDelegate repository root.
- Release archive: `./software-planning-lead-v5.9.3-github-native.zip` or the exact supplied path.
- V5.9.3 is a cumulative patch over V5.9.2. The public `main` observed while building this release was `4e44a3a54a8d7be64dad5ef02a26316db373cee5` (`release: CtrlAltDelegate v5.9.2`). Never reset a newer compatible repository to this observed SHA.

## Non-negotiable safety

1. Inspect `git status`, current branch, remotes and `HEAD`; preserve unrelated/dirty user work. Never `reset --hard`, `clean`, or discard unrelated changes.
2. Validate ZIP paths before extraction; reject absolute/traversal/device/unsafe-symlink members.
3. Extract outside the tracked repository and read `RELEASE-METADATA.json`, `CHANGELOG-V5.9.3.md`, `RELEASE-MANAGED-PATHS.txt`, `AGENTS.md` and this handoff first.
4. Treat `RELEASE-MANAGED-PATHS.txt` as the release overlay allow-list. Never delete repo-owned files merely because they are absent from the ZIP.
5. Preserve `.git/`, branding/assets, GitHub metadata, historical changelogs and unrelated project files.
6. For a release-managed path changed independently since the compatible baseline, diff and merge semantics; do not blindly overwrite newer compatible work.

## Required V5.9.3 semantic outcome

Retain every V5.9.2 feasibility/planning/compiler/reverification/model-routing control and additionally enforce:

### Oh My Pi first-class harness

- `oh-my-pi` / `omp` is `FIRST_CLASS`, while Pi remains the reference harness;
- OMP reuses root `AGENTS.md` and canonical `.agents/skills`; do not duplicate the 154-skill library into an OMP-specific tree;
- map independent ready jobs to OMP native `task` batching/async execution when attested and useful;
- use OMP structured output schemas and isolated worktree/patch metadata for worker contracts/parallel writers when available;
- OMP scheduler/session completion is only a worker claim; CtrlAltDelegate parent re-verification, fresh review and controller settlement remain authority;
- **do not use generic OMP `effort: hi` for OpenAI FRONTIER/Sol**. OMP can map `hi` to the model's highest supported effort. Resolve Sol explicitly at `high`; `xhigh` and `max` remain forbidden;
- the persistent main orchestrator remains normally spawn-only and never receives independent-review credit.

### Graphify code intelligence

- every project runs `CODE_INTELLIGENCE_PREFLIGHT`;
- Graphify is the preferred persistent code-intelligence provider for non-trivial codebases when approved/available;
- when a current graph exists, use `query/path/explain` before broad grep/read traversal, then confirm material findings in source/LSP;
- Graphify is navigation/context compression only and **cannot satisfy acceptance/verification by itself**;
- multi-wave work may use Graphify incremental update/watch; watcher failure is not a global blocker;
- generated `graphify-out/` stays local/ignored by default;
- missing Graphify with no stored host choice requires a one-time user decision: `HOST_ALWAYS | PROJECT_ONLY | NEVER`;
- `HOST_ALWAYS` is user-scope only, no sudo/admin/global overwrite; `PROJECT_ONLY` remains isolated under CtrlAltDelegate runtime/control storage; `NEVER` uses fallback navigation;
- reviewed/pinned baseline is `graphifyy==0.9.53` / Apache-2.0; a different version requires drift verification and smoke-test evidence.

### Preserved model routing

- `FRONTIER=gpt-5.6-sol`, `BALANCED=gpt-5.6-terra`, `EFFICIENT=gpt-5.6-luna` as OpenAI reference mapping;
- all CtrlAltDelegate-selected GPT-5.6 routes use `high`;
- Sol is never requested above `high`;
- escalation remains `EFFICIENT -> BALANCED -> FRONTIER` with fresh attempts and evidence;
- canonical skill count remains exactly 154; Claude adapter count remains 154.

## Merge

1. Verify `RELEASE-MANIFEST.sha256`.
2. Merge every release-managed path, including delivery-template mirrors, new `.omp/RULES.md`, `adapters/oh-my-pi/`, code-intelligence policy/state/docs/controller, validators and release metadata.
3. Keep `.agents/skills` canonical and `.claude/skills` as thin adapters.
4. Add `CHANGELOG-V5.9.3.md`; preserve older changelogs.
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
python3 scripts/validate_v593_integration.py
python3 scripts/validate_planning.py
python3 scripts/validate_control_plane.py
python3 scripts/validate_assurance_control.py
python3 scripts/validate_skill_evals.py
python3 scripts/validate_v58_architecture.py
python3 scripts/validate_v59_control_plane.py
python3 scripts/harness_preflight.py --json
python3 scripts/graphify_ctl.py prepare
```

Also run every other existing release/system validator that remains applicable. Do not weaken old gates merely to pass.

Verify counts:

```bash
find .agents/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
find .claude/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
```

Both must be `154`.

Explicitly verify:

- OMP is `FIRST_CLASS` in `HARNESS-CONFORMANCE.yaml`;
- `.omp/RULES.md` is a thin sticky hard-rule layer, not a second full instruction system;
- active OMP policy never maps Sol through generic `effort: hi`;
- current policy never requests Sol `xhigh`/`max`;
- `graphify_ctl.py prepare` is non-mutating and returns one of the documented actions;
- no host Graphify installation occurs during release validation;
- Graphify policy states navigation-not-proof and host consent;
- `graphify-out/` is ignored;
- source research matrix records OMP/Graphify provenance.

Historical changelogs may mention old behavior or higher effort names where clearly contextualized.

## Review before commit

- `git diff --check`
- inspect `git diff --stat` and material diffs
- confirm branding and unrelated files were not removed
- confirm OMP adapter, harness conformance, model-routing policy and `.omp/RULES.md` agree
- confirm Graphify policy, tool catalog/selection, controller, gitignore and delivery-template agree
- confirm V5.9.2 feasibility/Plan Checker/parent-reverification controls still exist
- confirm manifests/release claims match the actual diff

## Commit / push

Commit only intended release changes:

```text
release: CtrlAltDelegate v5.9.3
```

Push through the repository's permitted path. If direct `main` is protected, create a release branch/PR, satisfy checks and merge normally. Never bypass protection.

Afterward fetch remote `main` and report:

- final remote SHA;
- branch/PR path used;
- validation results;
- 154/154 skill/adapter counts;
- any reconciled post-baseline changes;
- confirmation that V5.9.3 is on remote `main`;
- confirmation that OMP is first-class, Graphify is consent-gated/query-first, and Sol remains capped at `high`.
