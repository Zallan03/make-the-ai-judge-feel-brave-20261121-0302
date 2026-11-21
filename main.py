"""Write one short relaxing text to entry.txt.

Stdlib only, no network, deterministic: the same bytes every run.
"""

import os

TEXT = (
    "Somewhere a kettle hums itself to sleep, and the light settles "
    "on the floor like a cat that has decided to stay. Nothing here is "
    "in a hurry. The next step can wait until your hands "
    "remember how steady they are."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
