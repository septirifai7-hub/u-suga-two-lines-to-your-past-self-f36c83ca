#!/usr/bin/env python3
"""Two Lines to Your Past Self - make.fun bounty entry.

Writes a two-line warning to my past self about one specific moment
(the 2am email to my boss) and one sentence on why it mattered,
to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "Don't hit send on that 2am email to your boss \u2014 you wrote it angry, sleepless, and shaking.\nIt cost you the job you loved, and it taught you to never answer anger before breakfast."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
