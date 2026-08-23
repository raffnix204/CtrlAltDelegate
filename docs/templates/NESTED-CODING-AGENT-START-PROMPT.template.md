# Coding-Agent Start Prompt — CtrlAltDelegate V5.8.2 ZIP Handoff

Work from the actual target project/repository root. A completed CtrlAltDelegate planning handoff is provided as `./ctrlaltdelegate-delivery.zip`.

Set and preserve:
- `PROJECT_ROOT` = current target project/repository root;
- `INBOUND_PACKAGE` = `./ctrlaltdelegate-delivery.zip`;
- `CONTROL_ROOT` = `./.ctrlaltdelegate`;
- `PLANNING_ROOT` = `./.ctrlaltdelegate/planning`;
- `SKILLS_ROOT` = `./.ctrlaltdelegate/.agents/skills`.

Do not implement application code inside `CONTROL_ROOT`.

Bootstrap before normal execution:
1. Preserve and obey any applicable target-repository instructions already present at `PROJECT_ROOT` (for example root/nested `AGENTS.md`, `CLAUDE.md` or equivalent harness-native policy). Do not overwrite them with CtrlAltDelegate control files. Reconcile the current directory with `git rev-parse --show-toplevel` when Git exists and do not switch to a nested control directory as the project root.
2. Preserve the target repository's existing `.gitignore` and add any missing CtrlAltDelegate local-control entries for `/ctrlaltdelegate-delivery.zip`, `/.ctrlaltdelegate/`, `/.ctrlaltdelegate.importing-*/`, and `/.ctrlaltdelegate.incoming-*/` before creating project commits. Default control visibility is `LOCAL_PRIVATE`.
3. Require `INBOUND_PACKAGE` unless an already validated matching `CONTROL_ROOT` exists. Inspect ZIP members before extraction: reject absolute paths, traversal (`..`), symlink/link entries, or any top-level path other than `.ctrlaltdelegate/`.
4. Extract into a temporary sibling directory, not directly over an existing control root. Validate the extracted package with its stdlib-safe control-package/handoff validators. Only then atomically promote the validated `.ctrlaltdelegate/` directory to `CONTROL_ROOT`.
5. After successful promotion, if `INBOUND_PACKAGE` came from the project root, move it to `./.ctrlaltdelegate/inbox/ctrlaltdelegate-delivery.zip`; keep the root ignore rule for bootstrap/failure safety.
6. If a different `CONTROL_ROOT` already contains active/resumable state, do not overwrite it. Stage the incoming package separately and reconcile identity/state; report a blocker if safe reconciliation is not possible.

After import read, in order:
1. `./.ctrlaltdelegate/AGENTS.md`;
2. `./.ctrlaltdelegate/CONTROL-PACKAGE.json`;
3. `./.ctrlaltdelegate/planning/handoff/HANDOFF-STATUS.yaml`;
4. `./.ctrlaltdelegate/planning/handoff/CODING-AGENT-HANDOFF.md`;
5. `./.ctrlaltdelegate/planning/execution/STATE.md`;
6. `./.ctrlaltdelegate/planning/execution/PLANNING-BASELINE.json`, then verify its attested fingerprint against the current authoritative planning files;
7. `./.ctrlaltdelegate/planning/execution/JOB-GRAPH.json`, `LOOP-STATE.json`, and queued `PENDING-INPUT.jsonl` when present;
8. only additional requirements, architecture, research, ADRs, evidence and routed skills required for the next action.

Require the handoff to be `READY`, `EXECUTION_HANDOFF`, with zero unresolved blocking decisions, an `ATTESTED` planning baseline, and the expected V5.8.2 control root. If the archive/control package is missing or inconsistent, stop with `BLOCKED_DELIVERY_INCOMPLETE` and name the exact problem instead of guessing another planning directory.

Treat the resolved planning baseline as authoritative unless actual repository/runtime evidence materially contradicts it. Do not restart broad discovery. Use the V5.8.2 loop/job/surface/harness contracts, negotiate actual harness capabilities, load only job-relevant skills, and implement in `PROJECT_ROOT` through verification, documentation, safe Git/GitHub integration and `COMPLETED`. Ask the user only for a true contract-defined hard stop.


## V5.8.2 specialist-planning authority
Read `$CONTROL_ROOT/planning/context/PLANNING-SKILL-STATE.yaml` before implementation. The planning baseline may contain specialist-produced design, SEO, data, security, content or other domain artifacts. Preserve their resolved decisions unless current repository/runtime evidence materially contradicts them. Approved files under `$CONTROL_ROOT/planning/content/pages/` are authoritative copy and must not be casually rewritten.

## V5.8.2 assurance and debug integrity
Read `planning/execution/ASSURANCE-STATE.yaml` and `config/ASSURANCE-PROFILES.yaml`. Work size and assurance depth are independent. For substantive bug repair, derive a behavioral oracle from authoritative observed behavior and use `planning/execution/ROOT-CAUSE-DEPTH.json` when a symptom-layer fix could hide a deeper cause. High-assurance acceptance must be author-independent; parallel assurance verdicts remain blind when required. Delegated workers verify hash-bound authority pointers and return `STALE_BRIEF` rather than executing stale planning state.
