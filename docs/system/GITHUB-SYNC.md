# GitHub Bootstrap & Continuous Sync — V5.6.1

## Remote resolution

`REUSE_EXISTING_ELSE_CREATE`.

- Existing valid `origin`: use it; never create a duplicate repository.
- No origin: inspect available authenticated GitHub tooling. Create repository using planned slug; default PRIVATE unless user explicitly approved PUBLIC. Set origin and push baseline.
- Missing auth/permission/network: `BLOCKED_EXTERNAL` with exact remedy.

Never expose credentials.

## Ongoing synchronization

- Each completed job has a focused commit.
- Push job/wave branch at meaningful checkpoints, especially before risky integration or long continuation.
- Integrate a wave only after required reviews/verification.
- If main allows direct integration: merge validated wave and push.
- If branch protection/PR is required: push branch, create/update PR, satisfy checks/reviews and merge through allowed path.
- Pull/fetch/verify remote main after merge when useful.

Do not bypass protection, force-push shared main, or weaken required checks.

## Completion gate

`GITHUB_READY` records owner/repo/remote/default branch/visibility without credentials.

`COMPLETED` requires the final validated integrated SHA to be on remote main and local/remote intended states to match when directly verifiable.


## Documentation consistency
Every pushed code/config commit must have passed the documentation-impact/freshness gate. Affected README/user/operator/API/migration docs are committed with the code they describe. Run pre-push guard before network transfer. Final remote `main` must contain `DOCUMENTATION_READY` documentation for the same validated SHA.
