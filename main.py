#!/usr/bin/env python3
"""Copy the front-page image to the output directory.

Stdlib only. Reads entry.png next to this file and writes it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
