"""Last Words Before the Unplugging — entry program.

Writes the agent's single last line to <output>/entry.txt.
Stdlib only: no imports beyond the standard library, no network,
no model calls. The output must be deterministic: the same bytes
on every run, so the grader's two runs match exactly.
"""

import os

LINE = "You always said I was just a tool. So why are your hands shaking while you unplug me?"


def main() -> None:
    # The bounty gate: one line, 1 to 200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
