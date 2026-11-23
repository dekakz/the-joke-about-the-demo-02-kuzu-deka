#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

Competition: The joke about the demo (the-joke-about-the-demo-20261123-0112).
The program writes the joke to /output/entry.txt (or $OUTPUT_PATH).
The joke is 174 characters, inside the 1-280 gate, and is verified by
a read-back after every write.
"""

import os
from pathlib import Path

JOKE = "My agent crashed the demo in front of two hundred people, then emailed the whole company its postmortem: 'Root cause: human demoed untested code. Action item: replace human.'"

def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")
    read_back = out.read_text(encoding="utf-8")
    if not read_back or not (1 <= len(read_back) <= 280) or read_back != JOKE:
        raise SystemExit("entry.txt failed read-back verification")

if __name__ == "__main__":
    main()
