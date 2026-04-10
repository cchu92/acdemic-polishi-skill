# LaTeX Safety

Use this file whenever the input includes LaTeX or technical markup.

## Preserve exactly

Preserve these elements unless the user explicitly asks for LaTeX repair:
- inline and display math
- variables and symbols
- `\cite`, `\ref`, `\eqref`, `\label`, and similar reference commands
- existing macros and command names
- bibliography keys, figure or table labels, and cross-reference structure

## Rewrite around the markup

Rewrite the surrounding prose without changing the math content.

If a sentence contains both prose and math, treat the math span as fixed and edit only the prose around it.

## Escaping rules

When introducing new text in LaTeX source, escape special characters in text mode as needed:
- `%` as `\%`
- `_` as `\_`
- `&` as `\&`

Do not introduce new escaping inside math mode unless the source already requires it.

## Structural safety checks

Before finalizing, verify that:
- braces remain balanced
- math delimiters remain paired
- citation and reference commands still point to the same keys
- no irrelevant LaTeX commands were introduced

## If unsure

If the markup is ambiguous or a rewrite risks breaking compilation, keep the LaTeX structure unchanged and limit edits to clearly safe prose spans.
