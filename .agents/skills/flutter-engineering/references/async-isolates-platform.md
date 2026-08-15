# Flutter Async, Isolates & Platform Integration

`async` I/O does not block the UI isolate while awaiting the underlying asynchronous operation. CPU-bound parsing/encoding/search can still monopolize the UI isolate and may need `Isolate.run`, `compute` or a long-lived isolate design depending on workload/version.

Plugin/platform channels are external capability boundaries. Define typed request/response/error semantics, thread/lifecycle expectations and what unsupported platforms do. Pigeon/code generation can reduce manual mismatch when it fits the project, but is not mandatory for every tiny integration.
