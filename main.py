#!/usr/bin/env python3
"""Write one absurd invention pitch to /output/entry.txt.

The pitch is a single sentence of at most 220 characters: a ridiculous
invention that fixes a tiny everyday annoyance, naming the annoyance,
the invention, and its silly mechanism in one tight sentence.
"""

import os

LINE = (
    "A washing machine that, on finding one red sock among the whites, "
    "convenes a tiny tribunal and sentences the sock to solitary "
    "confinement in the lint trap."
)


def check_entry(text):
    """Validate the pitch against the competition gate before writing it.

    The gate requires UTF-8 text of 1 to 220 characters, not only white
    space, as exactly one sentence: a single terminal full stop and no
    line breaks, so the file the judge reads is the sentence and nothing
    else. The checks below mirror the gate so a bad entry fails loudly
    here, on this machine, instead of silently scoring zero.
    """
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(text) > 220:
        raise ValueError("entry must be at most 220 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    if text.count(".") != 1:
        raise ValueError("entry must contain exactly one sentence")
    return text


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = check_entry(LINE.strip())
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    os.umask(0o022)
    main()
