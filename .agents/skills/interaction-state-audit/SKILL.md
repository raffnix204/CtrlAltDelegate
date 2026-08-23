---
name: interaction-state-audit
description: "Use when the task materially involves this skill's owned domain: Trace complex interactive flows end-to-end to detect race conditions, stale state, double actions, contradictory effects and broken refresh/navigation outcomes."
---

# Interaction State & Concurrency Audit

Skill ID: `interaction-state-audit`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Trace complex interactive flows end-to-end to detect race conditions, stale state, double actions, contradictory effects and broken refresh/navigation outcomes.

## Profiles

web_app, internal_app, ecommerce

## Typical roles

state-reviewer, frontend-reviewer, integration-reviewer

## Activate when
Features include optimistic updates, autosave, search-as-you-type, concurrent mutations, multi-tab/session behavior, background refresh, cache invalidation, undo, drag/drop, complex forms or client state machines.

## Audit model
For each critical action write the transition chain:
`precondition → user event → validation → mutation/request → pending UI → response(s) → cache/store update → rendered result → refresh/navigation result`.

## Checks
### Concurrency
- double click/repeated submit;
- out-of-order responses;
- canceled request finishing late;
- two tabs editing same resource;
- background refetch overwriting optimistic/local edits;
- stale closure/effect state;
- server retries producing duplicate side effects.

### Optimistic UI
Only optimistic when rollback/reconciliation is defined and failure cost is acceptable. Pending state must be visible when ambiguity matters. Server response remains authoritative.

### Cache invalidation
Identify all surfaces representing the mutated entity/query. Verify exact invalidation/update behavior. Broad invalidate-everything may be correct initially but should not create unacceptable waterfalls.

### Navigation/refresh
After successful action, verify:
- browser refresh displays same canonical state;
- back/forward does not resurrect invalid stale state;
- URL parameters still represent filters/tab/page when intended;
- deep link opens a valid state.

### Async forms/autosave
Debounce/throttle semantics explicit. Preserve local edits. Display saving/saved/error state appropriately. Do not claim saved until durable server confirmation.

### Destructive actions
Prevent duplicate deletion and handle already-deleted/conflict responses gracefully.

## Testing
Prefer deterministic integration/browser tests with controlled delayed/out-of-order responses for high-risk races. Use fake timers only where time itself is the unit under test; do not hide real async ordering bugs.

## Anti-patterns
- `isLoading` single boolean for multiple independent requests;
- ignoring AbortController/cancellation semantics when stale responses can win;
- optimistic success toast before rollback path exists;
- cache key missing filter/tenant/user dimension;
- side effects inside render/computed logic;
- local state duplicating props/server cache without synchronization contract;
- disabling buttons as the only idempotency protection for server side effects.

## Evidence
Audit report lists critical transition chains, race scenarios exercised, resulting defects/fixes and any residual conflict policy (last-write-wins/version check/merge/reject).

## V5.6.1 Async State and Race Matrix

Audit each interaction as a small state machine: idle/loading/success/empty/error/retrying/canceled/stale plus any optimistic/pending state. Identify what happens when users click twice, navigate away, edit while saving, submit out of order, reconnect after offline state, or receive a stale response after a newer request.

Assign ownership for cancellation, request identity/versioning and optimistic rollback. Buttons disabled during work are not a complete concurrency strategy; server idempotency and stale-response suppression may still be required.

Verification should deliberately exercise rapid repeated input, slow/failing network, navigation during work, back/forward restoration and concurrent tabs/sessions when the product can encounter them.

### State ownership test
For every mutable interaction value, name its owner and lifetime: URL/server/cache/application/component/session. If two layers can write the same conceptual state, define reconciliation precedence. Test stale cache plus optimistic mutation plus server rejection where such combinations are possible. Focus/selection/scroll state may also need preservation across re-render/navigation in productivity interfaces.

### Cross-surface consistency
When the same entity can be edited from multiple panels, tabs or devices, define freshness and conflict semantics. Ensure background refresh cannot silently overwrite unsaved local edits and that optimistic updates reconcile with authoritative server versions.
