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

## Build

If you want to render locally with Marp CLI:

```bash
npx @marp-team/marp-cli@latest slides/tropical-ruby-2026.md --html --pdf --pptx
```

If you want editable PowerPoint output for final cleanup before importing into Google Slides:

```bash
npx @marp-team/marp-cli@latest slides/tropical-ruby-2026.md --pptx --pptx-editable
```

Notes:

- This first pass intentionally uses mostly **remote image URLs** for speed.
- For a conference-final deck, I would recommend freezing those assets locally before export.
- Embedded video is best handled in the final HTML deck or by re-embedding the clip directly inside Google Slides after PPTX import.
