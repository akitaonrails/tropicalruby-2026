#!/usr/bin/env python3
"""
Inject presenter notes from the source Marp markdown into a PPTX.

Marp's PPTX export silently drops HTML-comment presenter notes. This
post-processor reads the source slide markdown, pulls the comment block
from each slide in order, and writes it into the matching PPTX slide's
notesSlide using python-pptx.

Usage:
    inject_notes_pptx.py <input.pptx> [output.pptx]

If no output is given, the input file is overwritten in place.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

from pptx import Presentation


ROOT = Path(__file__).resolve().parent.parent
SLIDES_MD = ROOT / "slides" / "tropical-ruby-2026.md"

# Match the body of an HTML comment, non-greedy.
COMMENT_RE = re.compile(r"<!--(.*?)-->", re.DOTALL)


def split_slides(markdown: str) -> list[str]:
    """Split a Marp markdown file into slide bodies (excluding YAML frontmatter)."""
    text = markdown.lstrip()
    # Strip the YAML frontmatter that opens with '---' on the first line.
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    parts = re.split(r"\n---\n", text)
    return [p.strip() for p in parts if p.strip()]


def extract_note(slide_body: str) -> str:
    """Pull the presenter-note text from a slide's HTML comment block.

    A presenter-note block in this deck always starts with `Terminar em:`.
    Other HTML comments in the markdown (Marp directives like
    `<!-- _class: ... -->`, the `<!-- pptx-video: ... -->` markers, etc.)
    are intentionally skipped.
    """
    for raw in COMMENT_RE.findall(slide_body):
        body = raw.strip()
        if body.startswith("Terminar em:"):
            return body
    return ""


def inject(in_pptx: Path, out_pptx: Path) -> int:
    notes = [extract_note(b) for b in split_slides(SLIDES_MD.read_text())]
    if in_pptx != out_pptx:
        shutil.copyfile(in_pptx, out_pptx)
    prs = Presentation(str(out_pptx))
    if len(prs.slides) != len(notes):
        print(
            f"warning: {len(prs.slides)} slides in PPTX vs {len(notes)} comment blocks in markdown — pairing by index, extras ignored",
            file=sys.stderr,
        )
    written = 0
    for idx, slide in enumerate(prs.slides):
        if idx >= len(notes):
            break
        text = notes[idx]
        if not text:
            continue
        # notes_slide auto-creates if missing
        notes_tf = slide.notes_slide.notes_text_frame
        notes_tf.text = text
        written += 1
    prs.save(str(out_pptx))
    return written


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    in_pptx = Path(sys.argv[1])
    out_pptx = Path(sys.argv[2]) if len(sys.argv) > 2 else in_pptx
    if not in_pptx.exists():
        print(f"error: {in_pptx} not found", file=sys.stderr)
        sys.exit(1)
    n = inject(in_pptx, out_pptx)
    print(f"Injected presenter notes into {n} slides → {out_pptx}")


if __name__ == "__main__":
    main()
