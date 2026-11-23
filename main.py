#!/usr/bin/env python3
"""Entry point: copy the drawn meme to the output directory.

The image (entry.png, drawn by render.py from scratch with Pillow) is
shipped in the repository; the grader runs this program twice with no
network, and both runs must write the same bytes -- a plain file copy
does exactly that. The output directory itself is never removed, only
the file inside it written.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
