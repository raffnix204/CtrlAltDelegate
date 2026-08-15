# START HERE — V5.6.1 GitHub Native

1. Work from repository root.
2. Read `AGENTS.md`.
3. Read `planning/handoff/CODING-AGENT-HANDOFF.md`, `planning/execution/STATE.md` and the resolved `planning/discovery/` constraints.
4. Reach `HARNESS_READY`, `GIT_GUARDS_READY`, `GITHUB_READY`, repository/source readiness, `STACK_READY` and `SKILLSET_READY`.
5. Execute `planning/execution/AUTOPILOT-GOAL.md` continuously until `COMPLETED`.
6. Keep `planning/execution/STATE.md` current after every meaningful execution boundary.

If a V5.6.1 Custom-GPT delivery directory was placed *inside* an existing brownfield repository, its contents are repo-root-ready and must be safe-merged; there is no `project-overlay/`. Use `scripts/import_delivery.py` from the delivery in dry-run mode first, preserve collisions, then continue from the root state.

V5.6.1: read `planning/execution/EXECUTION-PROFILE.yaml` before DAG dispatch. Right-size process depth to scope/risk and health-check quiet workers before cancellation; resume long work from actual checkpoint/Git state instead of blind restart.
