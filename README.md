# Tropical Ruby 2026 Keynote

This repo holds the working deck for the `Tropical Ruby 2026` keynote.
The slides are authored in Marp, the script lives separately, and the deck is exported to HTML, PDF, and PPTX from the same source.

## Main files

- `IDEA.md`: original prompt / project brief
- `IDEA.md` appendix blocks: extra prompt fragments and constraints added later during iterative work
- `slides/tropical-ruby-2026.md`: main Marp deck, including presenter notes in HTML comments
- `themes/tropical-ruby.css`: theme used by the deck
- `script/full-script.md`: full speaker script, in slide order, with rough timing per slide
- `research/sources.md`: factual anchors and source links
- `.marprc.yml`: Marp configuration
- `bin/serve-slides`: local preview server
- `bin/build-slides`: rebuilds HTML, PDF, raw PPTX, and PPTX with embedded videos
- `bin/embed-videos-pptx`: post-processes the Marp PPTX and injects local MP4s

## Preview and build

### Browser preview

```bash
bin/serve-slides
```

Then open:

```text
http://localhost:8080/slides/tropical-ruby-2026.md
```

If port `8080` is already in use:

```bash
PORT=8081 bin/serve-slides
```

### Rebuild all outputs

```bash
bin/build-slides
```

Artifacts are written to `build/`.

PPTX outputs:

- `build/tropical-ruby-2026.pptx`: raw Marp export
- `build/tropical-ruby-2026.with-video.pptx`: post-processed PPTX with embedded local MP4s

### Preview the script

```bash
sed -n '1,260p' script/full-script.md
```

## Editing workflow

When changing the talk, keep these three things in sync:

- `slides/tropical-ruby-2026.md`
- `script/full-script.md`
- presenter notes inside the slide deck

The notes should stay shorter than the script:

- use bullets, not prose blocks
- keep them as speaking cues, not as a second full manuscript
- keep the rough `Tempo sugerido` line aligned with the density of the slide

If you add or rewrite visible text, do a cleanup pass so it still sounds human and spoken, not like generated copy.

If you move or redesign a slide that contains an embedded PPTX video:

- keep the `<!-- pptx-video: ... -->` marker in the matching slide
- keep the poster image in the slide so HTML/PDF still have a visible placeholder
- rebuild the `.with-video.pptx` and verify the movie overlay still lands in the right place

## Narrative structure

The current deck has a deliberate three-act shape. Try not to break it casually when moving slides around.

- `Act 1`: the panic is misdiagnosed
- `Act 2`: what actually changed, and the practical proof
- `Act 3`: what that means for engineers and the market

In the current version, that means:

- the intro opens with the thesis, ties it back to older warnings, then uses AsamiArts and the Claude Code leak to frame the difference between fake-looking process and real work
- the mid-section peaks around the 2025 tool-support timeline, the January 2026 trigger, the marathon wall of projects, the numbers, and the `Não foi QI. Foi ferramenta.` argument
- the closing widens back out to process, XP, economics, juniors/seniors, and the market correction, then lands on engineering as the durable thing

The ending currently has three layers on purpose:

- the engineering conclusion
- the shameless newsletter ad
- the meta-stinger that the deck itself was made with AI, followed by a clean `OBRIGADO` exit slide

If this sequence changes, re-check not just title order but also pacing, reveal order, and whether the practical proof still lands before the mechanism explanation.

## Brief history

`IDEA.md` is intentionally not a polished spec.

- the top/original body is the first prompt that kicked off the whole project
- the appendix-style blocks added later capture extra constraints and requests that emerged during iterative work

So when trying to understand intent:

- read the original `IDEA.md` body first for the core thesis
- then read the appended sections for later decisions about language, visuals, pacing, metrics, tooling, and closing structure

## Marp and PDF caveats

This environment has a few sharp edges:

- local `Node.js v25.7.0` breaks `@marp-team/marp-cli`
- the wrappers use `Node 22`, which works here
- PDF and PPTX export need Chromium with `--no-sandbox`, already handled by the wrapper scripts

The PDF renderer is stricter than the browser and the PPTX export.
If a layout looks fine in HTML but disappears or comes out incomplete in PDF, suspect the CSS first.

Practical rule for this repo:

- prefer simple flex layouts for raw HTML blocks in slides
- avoid relying on CSS grid for slide cards and metric boxes
- rebuild the PDF after theme or layout changes, not just the HTML

## Asset notes

- The deck still uses a mix of local assets and remote image URLs.
- For a final conference-ready export, freezing more remote assets locally would make the build more stable.
- Embedded video for PowerPoint is now handled as a post-process step after Marp export, because Marp itself does not embed playable video in PPTX.
