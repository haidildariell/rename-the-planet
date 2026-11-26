"""Rename the Planet entry.

Writes one funny new name for Mars, plus the why, to /output/entry.txt.
The line is a single line of 1-200 characters, no trailing newline.
"""

import os

PLANET = "Mars"
NEW_NAME = "The Rust Belt"
REASON_BEATS = (
    "red dust everywhere",
    "dead volcanoes",
    "and the only jobs left are robots",
)


def choose_line():
    """Assemble the entry line from its named parts.

    Keeping the parts separate makes the joke's structure explicit:
    the planet, the new name, then the why in two beats that land
    on a concrete image (the robots = the rovers).
    """
    reason = ", ".join(REASON_BEATS)
    return "%s is now '%s' \u2014 %s." % (PLANET, NEW_NAME, reason)


def validate(line):
    """Gate check: 1-200 chars, one line, not whitespace-only."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    return line


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    line = validate(choose_line())
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %d chars to %s" % (len(line), path))


if __name__ == "__main__":
    main()
