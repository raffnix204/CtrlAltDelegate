# Angular Reactivity, DI & Forms

## Reactivity selection

Use the simplest primitive matching the temporal model:

- plain value: non-reactive local computation;
- signal/computed: synchronous state and derived values consumed by Angular rendering;
- RxJS: cancellation, multi-event asynchronous composition, backpressure/time operators, external observable APIs.

Avoid subscriptions inside subscriptions. Prefer operator composition or explicit conversion at one boundary. Any explicit subscription needs an owner and teardown path.

## DI scope

Before `providedIn: root`, ask whether the state/resource is truly application-lifetime. Route/feature/component scoped providers can prevent accidental cross-feature state retention and simplify cleanup.

## Forms

Model server errors separately from client validation when they have different lifecycle. Do not clear server errors on unrelated value changes unless the product semantics require it. Preserve labels, described-by error relationships and focus/error-summary behavior.
