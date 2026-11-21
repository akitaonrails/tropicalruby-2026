#!/usr/bin/env python3
"""Measure where each <video class="deck-video"> sits on its slide in the rendered deck.

Marp's PPTX export bakes every slide into one flat background image, so the video
overlay has nothing to snap to. This renders the deck with Marp's bare template
(every slide laid out at once), loads it in headless Chrome and prints JSON:
{"<slide number>": {"left": f, "top": f, "width": f, "height": f}}, each a
fraction of the slide, for the first deck video on that slide.

usage: measure_videos.py SLIDES_MD > rects.json
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROBE = """<script>
window.addEventListener('load', () => setTimeout(() => {
  const out = {};
  document.querySelectorAll('section[id]').forEach(s => {
    const v = s.querySelector('video.deck-video');
    if (!v) return;
    const S = s.getBoundingClientRect(), V = v.getBoundingClientRect();
    out[s.id] = {left: (V.left - S.left) / S.width, top: (V.top - S.top) / S.height,
                 width: V.width / S.width, height: V.height / S.height};
  });
  const pre = document.createElement('pre');
  pre.id = 'video-rects';
  pre.textContent = JSON.stringify(out);
  document.body.appendChild(pre);
}, 500));
</script>"""


def main(deck: str) -> int:
    # Next to the deck so its relative ../assets paths still resolve.
    fd, name = tempfile.mkstemp(prefix=".measure-", suffix=".html", dir=Path(deck).resolve().parent)
    os.close(fd)
    page = Path(name)
    try:
        subprocess.run([str(ROOT / "bin/marp"), deck, "--html", "--template", "bare", "-o", str(page)],
                       check=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        page.write_text(page.read_text().replace("</body>", PROBE + "</body>"))
        dom = subprocess.run([str(ROOT / "bin/chromium-no-sandbox"), "--headless=new", "--disable-gpu",
                              "--allow-file-access-from-files", "--window-size=1280,720",
                              "--virtual-time-budget=15000", "--dump-dom", page.as_uri()],
                             check=True, capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout
    finally:
        page.unlink(missing_ok=True)
    m = re.search(r'<pre id="video-rects">(.*?)</pre>', dom, re.S)
    if not m:
        raise SystemExit("measure_videos: the probe did not report any video positions")
    print(m.group(1))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: measure_videos.py SLIDES_MD > rects.json")
    raise SystemExit(main(sys.argv[1]))
