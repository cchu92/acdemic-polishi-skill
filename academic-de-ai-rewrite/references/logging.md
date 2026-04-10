# Persistent Logging

Use this file when the user wants rewrite history to persist on disk.

## Default behavior

Append one Markdown entry per rewrite.

Default log path:
`./rewrite-logs/academic-de-ai-rewrite-log.md`

Override the path when the user specifies a project log location.

## What to log

Log the edited scope, not the entire paper, unless the user explicitly requests a full-file snapshot.

For each entry, capture:
- timestamp
- scope label
- source path when available
- output path when available
- edit mode: `full`, `partial`, or `no-op`
- short summary bullets
- original snippet
- revised snippet
- optional notes

## How to write the log

Use `scripts/append_modification_log.py` from the skill directory.

Typical usage:

```bash
python3 scripts/append_modification_log.py \
  --log-path ./rewrite-logs/academic-de-ai-rewrite-log.md \
  --scope "Introduction paragraph 2" \
  --edit-mode partial \
  --source-path ./paper/main.tex \
  --summary "Removed mechanical lead-in" \
  --summary "Compressed redundant background sentence" \
  --original-file /tmp/original-snippet.txt \
  --revised-file /tmp/revised-snippet.txt \
  --note "Kept the edit local to the marked paragraph"
```

## Practical guidance

If the user marks a sentence or clause, log only that marked span plus enough nearby text to make the change intelligible.

If no substantive change is needed, still append an entry with `edit-mode` set to `no-op` and explain why the source was retained.

If the user requests both rewritten text and a persistent log, do both in the same turn.
