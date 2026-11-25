#!/usr/bin/env python3
"""Make the AI Judge Laugh — office-life one-liner.

Writes a single joke about office life (one line, 1-200 chars) to
/output/entry.txt. The joke follows the judge brief in order:
concrete office scene, true observation, surprising turn, tight line,
original wording.

Entry (128 chars):
    We spent three weeks in meetings about a bug, the intern fixed it
    in ten minutes, and the meeting to thank him lasted two hours.
"""

import os

ENTRY = (
    "We spent three weeks in meetings about a bug, "
    "the intern fixed it in ten minutes, "
    "and the meeting to thank him lasted two hours."
)

MAX_CHARS = 200


def validate(text):
    """Gate: UTF-8, 1-200 chars, exactly one line, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # raises on lone surrogates / non-encodable chars
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    print("wrote /output/entry.txt (%d chars)" % len(entry))


if __name__ == "__main__":
    main()
