# Harness State — V5.6.3

Lifecycle: NOT_CHECKED
Active Harness: AUTO_DETECT
Reference Harness: PI
Detected Version: UNKNOWN
Readiness: NOT_READY

| Capability | Required | Status | Provider | Resolved Version | Evidence |
|---|---:|---|---|---|---|
| Instructions | YES | UNKNOWN | | | |
| Agent Skills | YES | UNKNOWN | | | |
| Persistent Goal loop | AUTO | UNKNOWN | | | |
| General subagents | AUTO | UNKNOWN | | | |
| Fresh isolated contexts | YES for independent jobs/reviews | UNKNOWN | | | |
| Parallel delegation | YES when independent ready jobs exist | UNKNOWN | | | |
| Background delegation | AUTO | UNKNOWN | | | |
| Writer worktree/cwd isolation | AUTO for parallel writers | UNKNOWN | | | |
| Runtime reload after install | AUTO | UNKNOWN | | | |
| Independent review | YES for substantive work | UNKNOWN | | | |
| Git/GitHub | YES | UNKNOWN | | | |
| Web acquisition | project-dependent | UNKNOWN | | | |
| Browser | project-dependent | UNKNOWN | | | |
| Semantic code navigation | large-repo dependent | UNKNOWN | | | |
| Network device/API automation | network-project dependent | UNKNOWN | | | |
| SQLite vector extension | SQLite-vector project dependent | UNKNOWN | | | |
| Remote operator channel | NO | UNKNOWN | | | |

Missing capabilities are resolved current-at-runtime and recorded here. V5.6.3 prescribes capabilities and safety contracts, not third-party package versions.

Restart Required: NO
Restart Reason: NONE
Resume Action: NONE

## V5.6.3 worker-liveness capability check
Before long-running/expensive delegation, record whether the active provider exposes progress/update signals, cancellation and resumable session/checkpoint behavior. Before every delegation, verify the job-required capability set (for example web/browser/runtime/device) is actually available to that worker. A static provider timeout must not be interpreted as proof that the worker was idle.
