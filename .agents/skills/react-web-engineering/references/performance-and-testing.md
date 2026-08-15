# React Performance & Verification
## When to read this reference

Read this reference when **performance and testing** is material to the current react web engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

## Performance order

1. profile the slow interaction;
2. identify whether time is network, JavaScript compute, render/commit, layout/paint or third-party work;
3. reduce work/ownership fan-out;
4. virtualize genuinely large rendered collections where needed;
5. only then add memoization with evidence that props are usually stable and render cost matters.

## Testing

Prefer tests that interact through roles/labels and assert product outcomes. Cover loading/error/empty/optimistic/retry states for material flows. Snapshot tests may supplement but should not be the only proof of behavior.

Accessibility checks include semantics, keyboard order, focus restoration and live status/error announcements where dynamic content requires them.
