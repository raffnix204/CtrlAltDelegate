# Control Package Import and Git Hygiene — V5.8

## User workflow

For a Custom-GPT planning handoff, the user copies exactly one file into the target project/repository root:

`ctrlaltdelegate-delivery.zip`

The coding agent starts from that project root. It does not require the user to pre-extract or rename the package.

## Deterministic local control root

The agent safely extracts the package into:

`.ctrlaltdelegate/`

`PROJECT_ROOT` remains the application repository root. `CONTROL_ROOT=./.ctrlaltdelegate`. Application source never belongs inside `CONTROL_ROOT`.

Working directly from the ZIP is not the default because skills, progressive references, validators and harness adapters need ordinary filesystem paths. ZIP access may be used for preflight/inspection only.

## Safe import

1. Reconcile `PROJECT_ROOT` with the Git root when Git exists.
2. Protect the inbound archive and control root from accidental project commits before implementation.
3. Inspect ZIP members and reject absolute paths, `..` traversal, links or any top-level path other than `.ctrlaltdelegate/`.
4. Extract to a temporary sibling path.
5. Validate manifest, required files, prompt parity and handoff readiness.
6. Atomically promote the validated directory to `.ctrlaltdelegate/`.
7. Never overwrite an active different control state silently. Stage/reconcile a newer package instead.

## Default Git visibility

Custom-GPT control packages default to `LOCAL_PRIVATE`:

```gitignore
/ctrlaltdelegate-delivery.zip
/.ctrlaltdelegate/
/.ctrlaltdelegate.importing-*/
/.ctrlaltdelegate.incoming-*/
```

The coding agent must preserve existing `.gitignore` content and add only missing CtrlAltDelegate lines. If the archive/control root is already tracked accidentally, do not rewrite history; remove it from the index in a normal safe commit unless the user intentionally selected `TRACKED_SHARED`.

The framework's own public GitHub-native repository is different: its root-native CtrlAltDelegate system files are part of that repository and remain tracked.

## Shared planning option

`LOCAL_PRIVATE` is the default to avoid polluting public application repositories. A team may deliberately choose `TRACKED_SHARED`; that decision must define an allowlist of durable planning artifacts and keep raw/private/log/cache/runtime material ignored. Do not switch visibility implicitly.
