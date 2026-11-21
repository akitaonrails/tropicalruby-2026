#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu


ROOT = Path(__file__).resolve().parent.parent
SLIDES_MD = ROOT / "slides" / "tropical-ruby-2026.md"


@dataclass(frozen=True)
class Placement:
    left: float
    top: float
    width: float
    height: float


@dataclass(frozen=True)
class VideoSpec:
    movie: Path
    poster: Path
    mime_type: str
    placement: Placement
    volume: float = 0.0  # 0.0 = muted; 0.25 = 25%


GAMES = ROOT / "assets" / "games"
DEFAULT_PLACEMENT = Placement(left=0.10, top=0.12, width=0.80, height=0.80)


def game_video(name: str, volume: float) -> VideoSpec:
    """A clip in assets/games/<name>.mp4 with its <name>.jpg poster."""
    return VideoSpec(
        movie=GAMES / f"{name}.mp4",
        poster=GAMES / f"{name}.jpg",
        mime_type="video/mp4",
        placement=DEFAULT_PLACEMENT,
        volume=volume,
    )


VIDEO_SPECS: dict[str, VideoSpec] = {
    "omarchy-games-menu": game_video("omarchy-games-menu", volume=0.0),
    "colin-duckstation": game_video("colin-duckstation", volume=0.25),
    "colin-launcher-default": game_video("colin-launcher-default", volume=0.25),
    "colin-launcher-4k": game_video("colin-launcher-4k", volume=0.25),
    "colin-recomp-4k": game_video("colin-recomp-4k", volume=0.25),
    "rad-mobile": game_video("rad-mobile", volume=0.25),
    "wangan-6r": game_video("wangan-6r", volume=0.25),
    "initial-d-ta5": game_video("initial-d-ta5", volume=0.25),
}


def emu(value: float, full: int) -> Emu:
    return Emu(int(full * value))


def find_marked_slides() -> dict[str, int]:
    text = SLIDES_MD.read_text()
    slides = text.split("\n---\n")
    # Marp front matter lives before the first thematic break and is not a real slide.
    if slides and slides[0].lstrip().startswith("---\nmarp:"):
        slides = slides[1:]
    markers: dict[str, int] = {}
    for index, slide in enumerate(slides, 1):
        matches = re.findall(r"<!--\s*pptx-video:\s*([a-z0-9-]+)\s*-->", slide)
        for key in matches:
            if key in markers:
                raise SystemExit(f"Duplicate pptx-video marker: {key}")
            markers[key] = index
    return markers


def main(argv: list[str]) -> int:
    rects: dict[str, dict[str, float]] = {}
    if len(argv) >= 3 and argv[1] == "--rects":
        rects = json.loads(Path(argv[2]).read_text())
        argv = [argv[0], *argv[3:]]
    if len(argv) not in (2, 3):
        print("usage: embed_videos_pptx.py [--rects RECTS_JSON] INPUT_PPTX [OUTPUT_PPTX]", file=sys.stderr)
        return 2

    input_pptx = Path(argv[1]).resolve()
    output_pptx = Path(argv[2]).resolve() if len(argv) == 3 else input_pptx

    if not input_pptx.exists():
        raise SystemExit(f"Input PPTX not found: {input_pptx}")

    markers = find_marked_slides()
    missing_markers = sorted(set(VIDEO_SPECS) - set(markers))
    if missing_markers:
        raise SystemExit(f"Missing pptx-video markers in slides markdown: {', '.join(missing_markers)}")

    for key, spec in VIDEO_SPECS.items():
        if not spec.movie.exists():
            raise SystemExit(f"Missing movie asset for {key}: {spec.movie}")
        if not spec.poster.exists():
            raise SystemExit(f"Missing poster asset for {key}: {spec.poster}")

    if output_pptx != input_pptx:
        output_pptx.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(input_pptx, output_pptx)

    prs = Presentation(str(output_pptx))
    slide_width = prs.slide_width
    slide_height = prs.slide_height

    for key, spec in VIDEO_SPECS.items():
        slide_no = markers[key]
        slide = prs.slides[slide_no - 1]

        # Marp bakes each slide (poster included) into one background image, so the
        # movie goes exactly over the poster using the box measured in the HTML.
        rect = rects.get(str(slide_no))
        if rect is not None:
            place = Placement(**rect)
        else:
            print(f"warning: no measured position for {key} (slide {slide_no}); using the default box",
                  file=sys.stderr)
            place = spec.placement
        left = emu(place.left, slide_width)
        top = emu(place.top, slide_height)
        width = emu(place.width, slide_width)
        height = emu(place.height, slide_height)

        movie = slide.shapes.add_movie(
            str(spec.movie),
            left,
            top,
            width,
            height,
            poster_frame_image=str(spec.poster),
            mime_type=spec.mime_type,
        )
        enable_autoplay(slide, movie.shape_id, spec.volume)

    prs.save(str(output_pptx))
    print(f"Embedded {len(VIDEO_SPECS)} videos into {output_pptx}")
    return 0


def enable_autoplay(slide, shape_id: int, volume: float = 0.0) -> None:
    """Flip the embedded movie timing from click-to-play to autoplay, and set volume.

    No looping: LibreOffice Impress can hang a slideshow on a repeating video (keys stop
    advancing, exit takes seconds; tdf#107368), and every clip outlasts its slide anyway.
    """
    root = slide.part._element
    videos = root.xpath(f".//p:video[p:cMediaNode/p:tgtEl/p:spTgt[@spid='{shape_id}']]")
    if not videos:
        raise SystemExit(f"Unable to find timing node for video shape {shape_id}")

    video = videos[0]
    media_node = video.xpath("./p:cMediaNode")[0]
    if volume <= 0:
        media_node.set("mute", "1")
    else:
        media_node.set("vol", str(int(round(volume * 100000))))

    cond = video.xpath("./p:cMediaNode/p:cTn/p:stCondLst/p:cond")[0]
    cond.set("delay", "0")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
