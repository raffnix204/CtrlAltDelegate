# Code Intelligence & Graphify — V5.9.3

## Purpose

V5.9.3 adds a first-class code-intelligence layer so workers can query a persistent structural graph before spending context on broad file search/read cycles. Graphify is the preferred external provider for non-trivial code projects when available and approved on the host.

Graphify is **navigation/context compression**, not a verification oracle. Source, compiler/tests, runtime/provider/browser/network evidence remain authoritative.

## Lifecycle

```text
CODE_INTELLIGENCE_PREFLIGHT
  -> existing graph/provider?
  -> Graphify installed?
       yes -> verify version/capability
       no  -> resolve stored host preference
               ASK -> ask once for HOST_ALWAYS | PROJECT_ONLY | NEVER
  -> build/update graph when useful
  -> GRAPH_READY
  -> QUERY FIRST
  -> targeted source confirmation
  -> implementation/review
  -> incremental update/watch between waves when beneficial
```

Every project runs the preflight. A non-trivial codebase should use Graphify when it is ready. `MICRO` work, repositories with no supported source files, or a verified equivalent code-intelligence provider may record a justified skip.

## Installation consent

CtrlAltDelegate must never silently install a user-level host tool. If Graphify is missing and no stored choice exists, ask once:

- `HOST_ALWAYS` — install the verified Graphify package in the user's tool scope and register its generic Agent Skills integration for future projects;
- `PROJECT_ONLY` — keep Graphify isolated under the CtrlAltDelegate control/runtime root for this project;
- `NEVER` — use fallback navigation and do not ask again on that host until the preference is changed.

No `sudo`, admin elevation, global config overwrite, credentials, or paid commitment may be introduced by this bootstrap.

The verified V5.9.3 baseline is `graphifyy==0.9.53`. Before upgrading beyond the pinned baseline, use `VERIFY_DRIFT` against current upstream release/docs/license and update the lock only after a smoke test.

## Query-first rule

When `graphify-out/graph.json` is current, codebase questions should start with `graphify query`, `graphify path`, or `graphify explain`, then expand only the source slices needed to confirm the answer or make the change.

Typical flow:

```text
question/job
 -> graph query/path/explain
 -> identify files/symbols/seams
 -> targeted read/LSP
 -> implement
 -> test/runtime verify
```

Do not repeatedly rebuild a current graph merely because a new worker starts.

## Watch and incremental refresh

For active multi-job coding, Graphify may run its watcher or incremental update path between waves. Code-only updates can be rebuilt structurally without LLM semantic extraction. Debounce the watcher so parallel writers do not trigger a rebuild per file.

Watch is an optimization, not a completion gate. A watcher failure falls back to explicit `--update` or normal source navigation and is recorded in `CODE-INTELLIGENCE-STATE.yaml`.

## Trust boundary

Graphify distinguishes extracted versus inferred/ambiguous relationships. Use that distinction for navigation confidence, but verify material claims against source.

Never accept any of these solely because Graphify says so:

- an API is compatible;
- a security boundary is enforced;
- a regression is fixed;
- a call path executes at runtime;
- a migration is safe;
- a provider/browser/network journey works.

## State

Persist the active provider, install scope, version, graph fingerprint/status, last update and watch state in `planning/execution/CODE-INTELLIGENCE-STATE.yaml`. Generated `graphify-out/` is local/transient and ignored by Git by default.
