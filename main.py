#!/usr/bin/env python3
"""One Line, One Chill entry.

Writes a single horror sentence to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

LINE = (
    "The baby monitor played my voice reading a bedtime story in the nursery "
    "at three in the morning while I stood downstairs holding the book, "
    "still closed."
)

OUTPUT_PATH = "/output/entry.txt"


def check_entry(path):
    """Post-write self-check mirroring the gate: UTF-8, 1-200 chars, not blank."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be whitespace-only"
    return text


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    check_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
