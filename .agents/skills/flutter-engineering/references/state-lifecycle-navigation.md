# Flutter State, Lifecycle & Navigation

State lifetime should match the feature: widget-local transient state, feature/session state, server state or durable local data. Keep the selected library secondary to clear ownership.

Keys express identity to the element tree. Use stable domain identity for reorderable/dynamic collections and understand when a new key intentionally discards state.

Async completions can arrive after navigation/disposal. Check ownership before mutating UI state and cancel subscriptions/operations when supported.

Deep links/restoration may enter the app before auth/data bootstrap completes. Route through a state-aware gate rather than assuming a fully initialized process.
