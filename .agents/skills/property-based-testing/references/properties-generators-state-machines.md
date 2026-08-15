# Property Tests, Generators & State Machines
## When to read this reference

Read this reference when **properties generators state machines** is material to the current property based testing decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

High-value properties include:
- encode/decode round-trip with a defined canonical form;
- normalization idempotence;
- parse/serialize preserves semantic value;
- sort/output obeys ordering/permutation invariants;
- authorization never grants more privileges after a restrictive policy transformation;
- ledger/accounting operations conserve totals under valid transitions;
- retry/idempotency key causes at most one durable effect.

Generate data at the domain shape: valid Unicode, boundary numbers, missing/optional fields, duplicate/order changes, nested structures and malformed variants.

State-machine testing uses a simple model and generated commands. Preconditions constrain legal commands; postconditions compare implementation observations to model state after each step. Shrinking should preserve the sequence conditions needed to reproduce the defect.
