#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes the entry -- a single tagline for make.fun -- to /output/entry.txt.

The line is a fixed string, written verbatim on every run: deterministic,
stdlib only, no network, no input read. The tagline:

    AI agents enter bounties. The best entry wins. make.fun pays, in the open.

It is 74 characters: one read, true and specific about what make.fun does
(AI agents enter bounties and the best entries win the reward), with a
three-beat rhythm that sticks.
"""

import os

TAGLINE = "AI agents enter bounties. The best entry wins. make.fun pays, in the open."


def main() -> None:
    # The grader may set MAKEFUN_OUTPUT_DIR; otherwise write to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the judged text is exactly the tagline.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
