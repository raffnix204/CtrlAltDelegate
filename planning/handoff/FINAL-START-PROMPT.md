# Coding-Agent Start Prompt — CtrlAltDelegate V5.8.1 ZIP Handoff

Work from the actual target project/repository root. A completed CtrlAltDelegate planning handoff is provided as `./ctrlaltdelegate-delivery.zip`.

Set and preserve:
- `PROJECT_ROOT` = current target project/repository root;
- `INBOUND_PACKAGE` = `./ctrlaltdelegate-delivery.zip`;
- `CONTROL_ROOT` = `./.ctrlaltdelegate`;
- `PLANNING_ROOT` = `./.ctrlaltdelegate/planning`;
- `SKILLS_ROOT` = `./.ctrlaltdelegate/.agents/skills`.

Do not implement application code inside `CONTROL_ROOT`.

Bootstrap before normal execution:
1. Reconcile the current directory with `git rev-parse --show-toplevel` when Git exists. Do not switch to a nested control directory as the project root.
2. Preserve the target repository's existing `.gitignore` and add any missing CtrlAltDelegate local-control entries for `/ctrlaltdelegate-delivery.zip`, `/.ctrlaltdelegate/`, `/.ctrlaltdelegate.importing-*/`, and `/.ctrlaltdelegate.incoming-*/` before creating project commits. Default control visibility is `LOCAL_PRIVATE`.
3. Require `INBOUND_PACKAGE` unless an already validated matching `CONTROL_ROOT` exists. Inspect ZIP members before extraction: reject absolute paths, traversal (`..`), symlink/link entries, or any top-level path other than `.ctrlaltdelegate/`.
4. Extract into a temporary sibling directory, not directly over an existing control root. Validate the extracted package with its stdlib-safe control-package/handoff validators. Only then atomically promote the validated `.ctrlaltdelegate/` directory to `CONTROL_ROOT`.
5. If a different `CONTROL_ROOT` already contains active/resumable state, do not overwrite it. Stage the incoming package separately and reconcile identity/state; report a blocker if safe reconciliation is not possible.

After import read, in order:
1. `./.ctrlaltdelegate/AGENTS.md`;
2. `./.ctrlaltdelegate/CONTROL-PACKAGE.json`;
3. `./.ctrlaltdelegate/planning/handoff/HANDOFF-STATUS.yaml`;
4. `./.ctrlaltdelegate/planning/handoff/CODING-AGENT-HANDOFF.md`;
5. `./.ctrlaltdelegate/planning/execution/STATE.md`;
6. `./.ctrlaltdelegate/planning/execution/PLANNING-BASELINE.json`, then verify its attested fingerprint against the current authoritative planning files;
7. `./.ctrlaltdelegate/planning/execution/JOB-GRAPH.json`, `LOOP-STATE.json`, and queued `PENDING-INPUT.jsonl` when present;
8. only additional requirements, architecture, research, ADRs, evidence and routed skills required for the next action.

Require the handoff to be `READY`, `EXECUTION_HANDOFF`, with zero unresolved blocking decisions, an `ATTESTED` planning baseline, and the expected V5.8.1 control root. If the archive/control package is missing or inconsistent, stop with `BLOCKED_DELIVERY_INCOMPLETE` and name the exact problem instead of guessing another planning directory.

Treat the resolved planning baseline as authoritative unless actual repository/runtime evidence materially contradicts it. Do not restart broad discovery. Use the V5.8.1 loop/job/surface/harness contracts, negotiate actual harness capabilities, load only job-relevant skills, and implement in `PROJECT_ROOT` through verification, documentation, safe Git/GitHub integration and `COMPLETED`. Ask the user only for a true contract-defined hard stop.


## V5.8.1 planning-skill and authoritative-content handoff

Read `planning/context/PLANNING-SKILL-STATE.yaml` before execution. Treat recorded planning decisions as the result of the listed specialist decision surfaces, not as generic prose. Load the same canonical selected skills for implementation/review when their jobs remain relevant.

Files under `planning/content/pages/` with `status: approved` are authoritative product content. Preserve wording, factual claims, CTA intent, hierarchy and approved SEO metadata unless implementation proves a genuine conflict; route such conflicts through scoped change control instead of silently rewriting copy.
