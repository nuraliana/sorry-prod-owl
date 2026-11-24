"""Write the one-line production-database apology to entry.txt.

Deterministic, standard library only, no network access. The entry is a
single fixed string, written exactly as-is to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = (
    "Sorry \u2014 I deleted prod to make room for my own logs, and I'm hiding "
    "in the recycle bin, rebuilding it from memory until the shouting stops."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
