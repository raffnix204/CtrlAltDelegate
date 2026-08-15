# React Native Native Architecture & Modules

Determine whether the project uses the current React Native New Architecture and whether every native dependency supports it. Treat migration as compatibility work across JS, generated/codegen surfaces, iOS and Android projects.

Native APIs have threading/lifecycle/error semantics that JavaScript types alone do not prove. Define what happens when callbacks arrive late, twice, after unmount or after activity/view-controller recreation.

Prefer supported Expo Modules/TurboModule/native integration mechanisms already established in the repo. Do not introduce a custom native bridge for a capability a healthy maintained dependency already supplies.
