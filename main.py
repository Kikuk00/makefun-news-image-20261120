"""Entry point for the news-image bounty.

Copies the pre-rendered entry.png sitting next to this script into the
output directory requested by MAKEFUN_OUTPUT_DIR (default /output).
Standard library only.
"""

import os
import sys
from pathlib import Path


def locate_source() -> Path:
    here = Path(__file__).resolve().parent
    return here / "entry.png"


def resolve_output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(raw)


def main() -> int:
    source = locate_source()
    if not source.is_file():
        print(f"error: source image missing: {source}", file=sys.stderr)
        return 1

    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)

    image_bytes = source.read_bytes()
    target = output_dir / "entry.png"
    target.write_bytes(image_bytes)
    print(f"wrote {target} ({len(image_bytes)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
