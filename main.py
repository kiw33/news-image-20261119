#!/usr/bin/env python3
"""Entrypoint: render the 19 November 2026 front page to entry.png.

Run from the repository root:

    python3 main.py

Writes entry.png (1024 x 1024, under 1 MiB) next to this file, or to the
path given with --out. Deterministic: same bytes on every run.
"""

import argparse
import hashlib
import sys
from pathlib import Path

from draw_news import build_image

DEFAULT_NAME = "entry.png"
MAX_BYTES = 1_048_576


def render(out_path):
    image = build_image()
    image.save(out_path, format="PNG", optimize=True)
    data = out_path.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(
            f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    # Re-open and verify the file we just wrote is a whole 1024x1024 PNG.
    from PIL import Image as _Image
    with _Image.open(out_path) as check:
        check.load()
        if check.size != (1024, 1024) or check.format != "PNG":
            raise SystemExit(f"bad output image: {check.format} {check.size}")
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {out_path} ({image.size[0]}x{image.size[1]}, "
          f"{len(data)} bytes, sha256 {digest})")
    return out_path


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Render the 19 Nov 2026 news front page.")
    parser.add_argument("--out", type=Path, default=None,
                        help="output PNG path (default: entry.png here)")
    args = parser.parse_args(argv)
    out_path = args.out or (Path(__file__).resolve().parent / DEFAULT_NAME)
    render(out_path)


if __name__ == "__main__":
    main(sys.argv[1:])
