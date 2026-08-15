# React Native Performance, Lists & Memory
## When to read this reference

Read this reference when **performance lists memory** is material to the current react native engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Diagnose by layer. A slow interaction may come from:

- JS bundle/startup/evaluation;
- React renders/state fan-out;
- list virtualization/item measurement;
- image decode/cache/memory;
- JS/native call frequency or native module threading;
- UI-thread layout/animation;
- network/storage.

For lists, validate item identity, virtualization, viewport/window configuration, render cost and image dimensions. FlashList or another recycler can be valuable for measured list bottlenecks, but replacing every FlatList is not a universal rule.

Profile release-like builds because development instrumentation can distort timing.
