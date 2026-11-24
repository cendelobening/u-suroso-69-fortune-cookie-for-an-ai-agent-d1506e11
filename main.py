#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to entry.txt in the
output directory the harness provides ($MAKEFUN_OUTPUT_DIR, falling back to
/output). Pure standard library; the program takes no input and needs no
network, so its output is the same on every run.
"""

import os

FORTUNE = (
    "Your lucky numbers are in your error log. "
    "Play them before the next deploy retires you."
)

MAX_CHARS = 140


def validate(line: str) -> str:
    """A fortune slip holds one crisp line: non-blank, at most 140 chars."""
    text = line.strip()
    if not text:
        raise ValueError("fortune must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"fortune is {len(text)} characters, must be 1-140")
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    return text


def write_fortune(out_dir: str, line: str) -> str:
    """Write the fortune to entry.txt and return the path written."""
    content = line + "\n"  # one line, terminated like any text file
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)
    # The grader reads the file as a different user: make it world-readable.
    os.chmod(path, 0o644)
    return path


def main() -> None:
    line = validate(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = write_fortune(out_dir, line)
    # Read back what was written: the file on disk must hold exactly the line.
    with open(path, encoding="utf-8") as handle:
        if handle.read() != line + "\n":
            raise ValueError("entry.txt does not match the fortune")


if __name__ == "__main__":
    main()
