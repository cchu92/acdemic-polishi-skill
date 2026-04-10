#!/usr/bin/env python3

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from typing import Iterable


DEFAULT_LOG_PATH = Path("rewrite-logs/academic-de-ai-rewrite-log.md")


def read_text_argument(text: str | None, file_path: str | None) -> str:
    if text is not None:
        return text.strip("\n")
    if file_path is not None:
        return Path(file_path).read_text(encoding="utf-8").strip("\n")
    return ""


def format_bullets(items: Iterable[str]) -> str:
    values = [item.strip() for item in items if item and item.strip()]
    if not values:
        return "- None provided"
    return "\n".join(f"- {value}" for value in values)


def fenced_block(text: str) -> str:
    body = text if text else "[empty]"
    return f"```text\n{body}\n```"


def build_entry(args: argparse.Namespace) -> str:
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    original = read_text_argument(args.original_text, args.original_file)
    revised = read_text_argument(args.revised_text, args.revised_file)
    notes = format_bullets(args.note)
    summaries = format_bullets(args.summary)
    source_path = args.source_path or "[not provided]"
    output_path = args.output_path or "[not provided]"

    return "\n".join(
        [
            f"## {timestamp} | {args.scope}",
            "",
            f"- Edit mode: `{args.edit_mode}`",
            f"- Source path: `{source_path}`",
            f"- Output path: `{output_path}`",
            "",
            "### Summary",
            summaries,
            "",
            "### Original",
            fenced_block(original),
            "",
            "### Revised",
            fenced_block(revised),
            "",
            "### Notes",
            notes,
            "",
        ]
    )


def ensure_header(path: Path) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    header = "\n".join(
        [
            "# Academic De-AI Rewrite Log",
            "",
            "Persistent log for academic rewrite operations.",
            "",
        ]
    )
    path.write_text(header, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append a persistent Markdown log entry for an academic rewrite."
    )
    parser.add_argument(
        "--log-path",
        default=str(DEFAULT_LOG_PATH),
        help="Markdown log path. Defaults to rewrite-logs/academic-de-ai-rewrite-log.md",
    )
    parser.add_argument("--scope", required=True, help="Short label for the edited scope")
    parser.add_argument(
        "--edit-mode",
        choices=("full", "partial", "no-op"),
        default="partial",
        help="Whether the rewrite covered a full unit, a local span, or no substantive change",
    )
    parser.add_argument("--source-path", help="Original file path when available")
    parser.add_argument("--output-path", help="Updated file path when available")
    parser.add_argument(
        "--summary",
        action="append",
        default=[],
        help="Summary bullet. Repeat this flag for multiple bullets.",
    )
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        help="Optional note bullet. Repeat this flag for multiple notes.",
    )

    original_group = parser.add_mutually_exclusive_group()
    original_group.add_argument("--original-text", help="Original edited text")
    original_group.add_argument("--original-file", help="Path to file containing original edited text")

    revised_group = parser.add_mutually_exclusive_group()
    revised_group.add_argument("--revised-text", help="Revised edited text")
    revised_group.add_argument("--revised-file", help="Path to file containing revised edited text")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    log_path = Path(args.log_path)
    ensure_header(log_path)
    entry = build_entry(args)

    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(entry)

    print(log_path.resolve())


if __name__ == "__main__":
    main()
