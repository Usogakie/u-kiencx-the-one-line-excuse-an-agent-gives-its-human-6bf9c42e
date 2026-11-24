"""Write the one-line excuse an agent gives its human for missing a deadline.

Deterministic: no network, no clock, no randomness. Writes exactly one
line to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt and nowhere else.

The line leans on the agent's own situation (a chain of delegated
subagents and a context window) so it could only come from a machine
that missed a deadline, and it lands in one sentence.
"""

import os

LINE = (
    "Sorry \u2014 I delegated the deadline to a subagent, who delegated it to "
    "another subagent, and the last one is still waiting for its context "
    "window to load."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
