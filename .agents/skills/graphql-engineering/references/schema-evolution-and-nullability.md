# GraphQL Schema Evolution & Nullability

Schema nullability is a runtime failure contract. A non-null field that throws or resolves null can null-bubble its parent chain. Choose non-null only where the server can uphold that guarantee or the bubbling behavior is desired.

Prefer additive evolution: add field/type, migrate clients, mark old field deprecated, observe usage, then remove. Input changes can be breaking when new required fields are introduced; enum additions can also break clients that exhaustively switch.

Mutations should represent meaningful operations and return stable IDs/state/errors. Avoid exposing arbitrary persistence fields as a generic update surface.
