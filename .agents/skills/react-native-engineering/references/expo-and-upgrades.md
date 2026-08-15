# React Native Expo & Upgrade Workflow

If Expo is present, identify managed/CNG/prebuild/bare characteristics before editing native projects. Project-generated native directories may be regenerated, so put configuration in the supported source of truth.

Upgrade workflow:
1. record RN/Expo/React/Node, Xcode/Gradle/AGP/Kotlin and native dependency baseline;
2. read each relevant RN/Expo migration guide and template diff;
3. update JS dependencies coherently;
4. reconcile iOS Pods/project and Android Gradle/application changes;
5. clear generated caches only when needed, not as the primary fix;
6. build/test iOS and Android; verify native modules, deep links, notifications and release config.
