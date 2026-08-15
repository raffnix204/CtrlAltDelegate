# Extension Security, Lifecycle & Messaging

Map each execution context: web page, injected page script, content script, extension page, background/service worker. Record what each can access and which messages cross boundaries.

Validate message schema and sender/origin/tab context where security decisions depend on it. Never expose a generic privileged RPC from page-controlled data without an allowlist and authorization checks.

Persist resumable state before relying on later background execution. Event listeners should reconstruct required state from storage when awakened.
