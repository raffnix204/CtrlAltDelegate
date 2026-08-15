# Git, Local Runtime and Recovery Playbook

## 1. Planner → repository handoff

The Planning GPT finishes first and exports a complete ZIP.

The user then manually:
1. creates/selects a GitHub repository;
2. extracts/adds the planning package;
3. commits and pushes it;
4. opens the repository with the coding agent;
5. starts the master Autopilot Goal.

The Planning GPT normally does not know the repository URL. Project files should use placeholders such as:

`Repository URL: DISCOVER_FROM_GIT_REMOTE_AT_EXECUTION`

The coding orchestrator resolves:
- `git remote get-url origin`;
- default branch;
- current `main` SHA;
- repository policy/branch protection where discoverable.

It records the real URL in `planning/execution/STATE.md`.

## 2. Repository gate

Before implementation:

- valid Git repository exists;
- planning package is present;
- plan is committed/pushed;
- remote can be resolved;
- working tree is understood;
- default branch policy is known;
- required skills/tools preflight passes or installs safely;
- local runtime strategy is feasible.

No need to return to the planner if repository metadata differs; execution adapts within project constraints.

## 3. Branch/worktree model

Never develop feature work directly on `main`.

For each wave:

`agent/wave-XX-<name>`

This is the wave integration branch, created from latest validated `main`.

Parallel write jobs use isolated worktrees/branches, e.g.:

`agent/job-JOB-012-auth-api`

Each job branch starts from the wave's agreed baseline.

The orchestrator:
- dispatches jobs;
- reviews actual diffs;
- integrates accepted commits into the wave integration branch;
- resolves conflicts centrally;
- validates the combined wave.

Do not allow two workers to independently redesign the same schema/public contract.

## 4. Automatic checkpoint to main

Default V4 policy favors autonomous progress with stable checkpoints.

After a wave has passed all required gates:

1. ensure wave integration branch is clean and pushed;
2. run required integrated validations;
3. integrate the wave into `main`;
4. push/update remote `main`;
5. rebuild/restart and runtime-test latest `main`;
6. record checkpoint evidence;
7. begin next wave from that latest `main`.

If repository policy requires PRs/checks:
- create PR targeting `main`;
- attach evidence;
- wait/poll for automated checks where tooling permits;
- enable/perform auto-merge if explicitly authorized and repository policy allows;
- if mandatory human approval is technically required, mark a genuine external blocker.

Do not weaken branch protection to gain autonomy.

## 5. Commit discipline

Use logical commits.

Commit messages should communicate intent.

Do not:
- commit secrets;
- mix unrelated refactors;
- silently weaken tests;
- commit transient logs/build artifacts unless required.

Before accepting a job:
- inspect `git status`;
- inspect diff;
- verify intended files;
- verify no accidental debris.

## 6. Runtime contract

Every executable project exports `LOCAL-RUNTIME.md`.

It must describe, once the stack is selected:

- prerequisites;
- environment variables;
- local dependencies;
- build procedure;
- migration procedure;
- restart/recreate procedure;
- health/readiness endpoints;
- smoke tests;
- canonical user-reachable URL strategy.

Prefer an explicit configuration such as:

`LOCAL_TEST_BASE_URL`

Examples are illustrative only:
- `http://devbox.local:3000`
- `http://192.168.1.50:3000`

Never invent the project's address.

## 7. Post-wave local deployment gate

After every wave merged/checkpointed on `main`:

1. update/check out latest `main`;
2. rebuild all affected application/services;
3. rebuild container images when required;
4. apply migrations safely;
5. recreate/restart services/workers;
6. verify health/readiness;
7. run wave smoke tests against the running system;
8. repair and repeat if failure is in scope;
9. determine the actual user-reachable URL;
10. record URL and runtime SHA in STATE;
11. continue automatically.

A wave is not a successful checkpoint until the running local system represents the merged code.

## 8. Host URL rules

Report a URL using this priority:

1. explicit `LOCAL_TEST_BASE_URL`;
2. configured DNS hostname;
3. configured mDNS hostname;
4. known reverse-proxy hostname;
5. non-loopback host IP + published port.

Never report as the user's test URL:
- `localhost`;
- `127.0.0.1`;
- `0.0.0.0`;
- `::1`;
- Docker service name;
- container ID;
- container-only bridge IP;
- internal Kubernetes service DNS;
- unverified guessed address.

Services may bind internally to `0.0.0.0`; the **reported** URL must still use a reachable host address.

Verify the URL with an actual request/health check where possible.

## 9. Runtime safety

Autonomous rebuild/restart must not:
- delete production/shared data;
- reset persistent volumes without plan authorization;
- expose private dev services publicly;
- disable auth/firewall protections;
- overwrite secrets;
- run destructive migrations casually.

Distinguish local development/test data from production data.

## 10. Execution recovery

Export these modes.

### RESUME
Read STATE/ledger/git; continue from first incomplete dependency-ready job.

### FORENSICS
Investigate why progress stopped:
- failing command;
- last good SHA;
- current branch;
- runtime health;
- dependency state;
- changed files;
- missing access.

### ROLLBACK
Return to the latest verified wave checkpoint when continued repair is unsafe.

Prefer Git revert/known checkpoint semantics appropriate to repository policy rather than destructive history rewriting.

## 11. Interruption recovery procedure

On resumed Autopilot:

1. inspect Git repository and remote;
2. read canonical job/dependency status and `STATE.md`;
3. verify current `main` SHA;
4. inspect unfinished branches/worktrees;
5. confirm completed ledger evidence;
6. verify runtime state;
7. run deterministic status reconciliation;
8. repair derived state when evidence is clear;
9. stop with `STATE_INCONSISTENT` if canonical evidence conflicts;
10. resume the first valid incomplete dependency-ready work.

Completed work must not be repeated merely because a chat/session restarted.

## 12. Wave checkpoint record

Persist after each successful wave:

- wave ID/name;
- integrated jobs;
- resulting `main` SHA;
- review verdicts;
- validation commands/results;
- runtime build/restart result;
- verified test URL;
- deviations;
- technical debt;
- next ready wave.

This makes long autonomous runs inspectable and recoverable.


## Existing-repository safety
Inspect branch/HEAD/status before work. Preserve all uncommitted/untracked user work; never reset/clean/overwrite/drop it. Prefer isolated worktree from committed baseline when appropriate. Record baseline SHA + dirty state. Git history/diff/bisect may support debugging only when user work remains safe.

## Harness bootstrap safety

Prefer project-local configuration, exact pins and verified capability evidence. Merge existing harness config rather than overwrite it. Never commit credentials, bypass managed policy or mutate global user config when project-local setup works. Executable extensions are supply-chain trust boundaries.

## GitHub bootstrap and continuous sync

`REMOTE_POLICY = REUSE_EXISTING_ELSE_CREATE` by default.

1. inspect Git and existing remote;
2. valid existing `origin` wins;
3. if absent, identify authenticated GitHub account using available safe tooling;
4. create planned repository, PRIVATE by default unless PUBLIC explicitly approved;
5. set/push `main` baseline;
6. push completed job/wave branches at meaningful checkpoints;
7. integrate validated waves through allowed direct/PR path;
8. push and verify final `main`.

Do not create a second repo when a valid origin already exists. Do not bypass branch protection/required checks. Do not print tokens/credentials.

### Hybrid planning Git policy

Commit shared execution truth: requirements, architecture, ADRs, selected skills, AUTOPILOT goal, state/ledger/findings/repository maps and safe harness adapters.

Ignore transient/private/bulky evidence: delivery bundle, `planning/private/`, `planning/**/raw/`, `tmp/`, `logs/`, caches, local dumps, secrets and large replaceable browser/crawl artifacts.


## Commit/push documentation guard
Install `.githooks` through `scripts/install_git_guards.py` when no conflicting hook system exists. If an existing hook path exists, preserve it and integrate `python3 scripts/docs_freshness_gate.py --staged` and the pre-push check into that system. Each code/config commit updates affected docs or carries a matching staged-diff `NONE` attestation. Never bypass the guard to make progress.
