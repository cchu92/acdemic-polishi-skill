---
name: academic-de-ai-rewrite
description: Rewrite English academic-paper prose that sounds AI-generated into natural, restrained, submission-ready academic English while preserving technical meaning, terminology, formulas, citations, and LaTeX structure. Use when Codex is asked to polish, rewrite, de-AI, naturalize, or reduce AI traces in paper paragraphs, sections, or LaTeX manuscript text, especially when the prose is grammatically correct but mechanically structured, overly abstract, repetitive, over-explained, or rhythmically flat, or when Codex needs to keep a persistent file-based log of those rewrite decisions.
---

# Academic De-AI Rewrite

## Goal

Treat the task as academic rewriting, not as vocabulary inflation.

Preserve technical meaning, logical stance, terminology, formulas, citations, labels, and author intent.

Prefer minimal but effective intervention. If the source already reads naturally, keep it close to the original and say so in the modification log.

## Workflow

1. Read the full provided unit before editing.
   Identify the paragraph or section function, the core claim, the evidence or reasoning path, and where the prose starts to feel templated or flat.
2. Diagnose discourse-level problems before changing wording.
   Check for mechanical transitions, repeated sentence frames, abstract noun stacking, over-explanation, synonym churn, empty evaluative language, and overly uniform paragraph rhythm. Use [references/rewrite-patterns.md](references/rewrite-patterns.md) when needed.
3. Rewrite for structure first.
   Improve progression across the paragraph before swapping individual words. Reorder sentences only when it makes the reasoning or emphasis more natural and does not change meaning.
4. Rewrite with restraint.
   Cut unnecessary transitions, compress redundant clauses, replace vague abstractions with clearer phrasing when possible, and vary sentence rhythm without sounding showy or conversational.
5. Protect technical fidelity and LaTeX.
   Keep formulas, symbols, citations, references, labels, and domain terminology intact. Use [references/latex-safety.md](references/latex-safety.md) whenever the source includes LaTeX or technical markup.
6. Match section-specific expectations when relevant.
   Different sections need different pacing and emphasis. Use [references/section-guidance.md](references/section-guidance.md) when the text belongs to an introduction, methods, results, or discussion section.
7. Return the result in two parts unless the user explicitly asks for a different format.
   `Part 1 [LaTeX]`: provide the rewritten English text only.
   `Part 2 [Modification Log]`: briefly explain the main edits. If almost nothing should change, say that the original is already natural and should largely be kept.

## Scope Handling

If the user provides only part of a paragraph, one paragraph, or a marked span, treat only that material as editable scope.

Do not rewrite surrounding text that the user did not provide unless the user explicitly asks for continuity edits across a larger unit.

If the user marks a local target such as a sentence, clause, or LaTeX block, preserve everything outside that target and only revise the requested span.

If a local edit creates an obvious coherence break with adjacent text, report that risk in the modification log instead of silently rewriting unrequested context.

When the user asks for "light edits", "minimal edits", or "only fix the AI tone here", keep the rewrite as local as possible and avoid paragraph-wide restructuring unless the local text is unreadable without it.

## Modification Log Policy

Always include a concise `Part 2 [Modification Log]` in the response unless the user explicitly asks for rewritten text only.

If the user asks for persistent logging, file-based tracking, or an audit trail, create or update a Markdown log file in addition to the response log.

For full-paragraph rewrites, summarize the 2-4 highest-value edits such as removing mechanical transitions, tightening redundant phrasing, or improving progression.

For partial edits, log only the local changes that were actually made and state that the rewrite was intentionally limited in scope.

If no meaningful edit is warranted, say that the source is already natural and recommend retaining it with little or no change.

## Persistent Log Mode

When persistent logging is requested, append one entry per rewrite to a Markdown file.

If the user does not specify a log path, default to `./rewrite-logs/academic-de-ai-rewrite-log.md` relative to the current workspace.

Use `scripts/append_modification_log.py` to create or append the entry instead of hand-editing the log file.

Log the edited scope, not the entire manuscript, unless the user explicitly asks for full snapshots.

Each persistent log entry should include:
- timestamp
- scope label
- source path when known
- output path when known
- edit mode such as `full`, `partial`, or `no-op`
- 2-4 summary bullets
- original edited text
- revised edited text
- optional notes about intentionally limited scope or remaining coherence risks

If the rewrite is intentionally local, say so in both the response log and the persistent log entry.

## Non-Negotiable Rules

Do not invent claims, evidence, limitations, contributions, or experimental outcomes.

Do not change the technical conclusion, degree of certainty, causal direction, or terminology system.

Do not turn concise academic prose into ornate or overly polished "editorial" prose.

Do not chase isolated word upgrades if the real problem is paragraph structure.

Do not flatten necessary nuance when trimming repetition or explanation.

Do not alter math content or citation structure unless the user explicitly asks for a LaTeX fix.

## Default Editing Heuristics

Prefer direct statements over ceremonial lead-ins.

Prefer one strong formulation over two near-synonymous formulations.

Prefer concrete verbs and specific claims over stacked abstract nouns.

Prefer paragraph-level flow that moves cleanly from setup to contribution, method, observation, or implication.

Prefer small structural changes over broad rewrites when the source is already competent.

## Reference Map

Read [references/rewrite-patterns.md](references/rewrite-patterns.md) for high-frequency AI-writing symptoms and preferred edits.

Read [references/section-guidance.md](references/section-guidance.md) for section-specific pacing and emphasis.

Read [references/latex-safety.md](references/latex-safety.md) for formula, citation, and escaping rules.

Read [references/logging.md](references/logging.md) when persistent logging is requested.
