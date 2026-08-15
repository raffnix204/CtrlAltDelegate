# Flutter Upgrades & Release
## When to read this reference

Read this reference when **upgrades and release** is material to the current flutter engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

For upgrades record Flutter/Dart channel/version, package lock, platform build tools and target OS baselines. Read Flutter/Dart breaking changes and package changelogs for affected APIs, then update generated code and native project files coherently.

Run release builds for every affected platform. Verify signing/entitlements, deep links, permissions, plugins, tree-shaken assets/fonts and platform-specific packaging; debug mode is insufficient evidence.
