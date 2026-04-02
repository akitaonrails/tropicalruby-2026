# Tropical Ruby 2026 Keynote

This repo holds the working deck for the `Tropical Ruby 2026` keynote.
The slides are authored in Marp, the script lives separately, and the deck is exported to HTML, PDF, and PPTX from the same source.

## Main files

- `slides/tropical-ruby-2026.md`: main Marp deck, including presenter notes in HTML comments
- `themes/tropical-ruby.css`: theme used by the deck
- `script/full-script.md`: full speaker script, in slide order, with rough timing per slide
- `research/sources.md`: factual anchors and source links
- `.marprc.yml`: Marp configuration
- `bin/serve-slides`: local preview server
- `bin/build-slides`: rebuilds HTML, PDF, and PPTX

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
- Embedded video is better handled in the final HTML deck or re-added directly in Google Slides after PPTX import.
