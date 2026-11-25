"""The Meeting That Should Have Been an Email.

A deterministic program that writes exactly one joke — a single line about
a meeting that should have been an email — to /output/entry.txt and
prints it to stdout.

The line is 107 characters, well under the 200-character gate, a single
line with no trailing newline. The twist lands in the last words: the
meeting's only decision was to book another meeting to draft the email
the first one should have been.
"""

import os

LINE = "The meeting ended with one decision: schedule another meeting to write the email this one should have been."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: 1..200 chars, exactly one line, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip guard: the file on disk must be byte-identical to the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt round-trip mismatch"
    print(f"{len(LINE)} chars")
    print(LINE)


if __name__ == "__main__":
    main()
