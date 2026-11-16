"""The Bath Did This — ai-excited-01 entry.

Copies the entry image (entry.png, sitting next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png. Stdlib only.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
