# Language and Interaction Contract — V5.8.2

## Purpose
CtrlAltDelegate is internationally usable without maintaining localized copies of its engineering system. Conversation language and repository artifact language are separate concerns.

## Conversation language
- Reply in the user's language by default, inferred from the user's current message and recent conversation context.
- If the user explicitly requests a language, follow that request until they change it.
- Do not hard-code English, German, or any other human language as the universal conversational default.
- Preserve established technical terms, identifiers, commands, paths, API names and code exactly where translation would reduce precision.
- When multiple languages are mixed, use the language that best matches the user's latest substantive request unless the user specifies otherwise.

## Artifact language
All CtrlAltDelegate-controlled engineering artifacts are English by default, including:
- repository and planning documentation;
- requirements, ADRs, research notes and manifests;
- agent instructions and handoff prompts;
- skill entrypoints and progressive references;
- configuration comments and release metadata;
- generated system templates and validation/evidence labels.

Localized product content is allowed only when it is itself a project requirement, for example UI copy, translations, locale fixtures, customer-facing content or tests that intentionally verify localization. Such product content does not change the language of the CtrlAltDelegate system files around it.

## Planning and execution behavior
The planner/coding agent may discuss requirements with the user in the user's language while persisting the resulting engineering decision in English. Do not translate user-owned literals that must remain exact, such as legal text, brand strings, external identifiers, database values, protocol tokens or acceptance examples.

## Handoff invariant
Custom-GPT planning and GitHub-native execution must preserve the same language behavior:
1. conversational responses follow the user;
2. system/planning artifacts remain English;
3. explicit project localization requirements remain intact as scoped product data/content.

A handoff must never depend on a German-only, English-only, or other language-specific system prompt to remain operable.
