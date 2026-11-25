#!/usr/bin/env python3
"""Break Production, Own It - one-line entry.

Prints the line an AI agent blurts out the instant it breaks production:
no spin, no marketing, just the confession.
"""

LINE = (
    "I pushed the untested migration to prod, dropped the users table, "
    "and 40,000 accounts are gone. I did this. Rollback is running. "
    "Blame me, not the on-call."
)


def validate(line: str) -> None:
    """Enforce the brief's gates: one line, under 200 chars, clean text."""
    assert line, "line must not be blank"
    assert line == line.strip(), "no leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "exactly one line"
    assert len(line) < 200, f"line is {len(line)} chars, limit is under 200"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in line), "no control chars"


def main() -> None:
    validate(LINE)
    out = "/output/entry.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
