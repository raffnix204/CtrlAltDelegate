# Vue Reactivity, Composables & Data

Track whether a value is a `ref`, reactive proxy, computed value or plain snapshot. Destructuring/copying can sever tracking; use the project-supported utilities/patterns when exposing reactive properties from composables.

A composable may create per-component state or intentionally shared client state. Make that lifetime explicit. In SSR, avoid module-global mutable user state.

For async data, define stable keys from inputs that truly determine the result and make mutation refresh/invalidation target the same domain identity.
