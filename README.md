# Tropical Ruby 2026 Keynote

This workspace contains a first executable pass of the `Tropical Ruby 2026` keynote in a declarative slide format.

## Why Marp

I chose **Marp** as the primary authoring tool for this pass.

- It is Markdown-native and fast to iterate on.
- `marp-cli` can export to **HTML, PDF, and PPTX**.
- Its PPTX output can be opened by **Google Slides**.
- The default HTML deck supports simple browser transitions.
- It fits the requested `Presentation Zen` style better than a heavier slide framework.

Runner-up: **Slidev** is also strong and more app-like, especially for web-native interactions, but it is heavier than needed for this talk.

## Files

- `slides/tropical-ruby-2026.md`: main Marp slide deck
- `themes/tropical-ruby.css`: custom theme
- `script/full-script.md`: speaker script matched to the slides
- `research/sources.md`: source notes, tool choice rationale, factual anchors
- `.marprc.yml`: Marp configuration

## Preview And Build

This repo has been tested in this environment with the wrapper scripts in `bin/`.

### Preview slides in browser

```bash
bin/serve-slides
```

Then open:

```text
http://localhost:8080/slides/tropical-ruby-2026.md
```

If you want the raw Marp wrapper instead:

```bash
bin/marp --server .
```

### Export all slide formats

```bash
bin/build-slides
```

Artifacts are written to `build/`.

### Preview the speaker script

Open `script/full-script.md` in any Markdown editor, or inspect it in terminal:

```bash
sed -n '1,260p' script/full-script.md
```

## Environment Notes

- `@marp-team/marp-cli` currently fails under the local `Node.js v25.7.0`.
- The wrapper uses `Node 22`, which was tested successfully here.
- PDF/PPTX export also needs Chromium launched with `--no-sandbox` in this environment, which is handled by `bin/chromium-no-sandbox`.
- This first pass intentionally uses mostly **remote image URLs** for speed.
- For a conference-final deck, I would recommend freezing those assets locally before export.
- Embedded video is best handled in the final HTML deck or by re-embedding the clip directly inside Google Slides after PPTX import.
