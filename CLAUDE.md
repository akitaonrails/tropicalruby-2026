# Tropical Ruby 2026 Workspace Notes

This repo is a keynote deck, not a generic app. Most changes touch talk structure, wording, layout, or export quality.

## Keep these files aligned

When you change the talk, sync all three:

- `slides/tropical-ruby-2026.md`
- `script/full-script.md`
- presenter notes inside `slides/tropical-ruby-2026.md`

Do not update one of them in isolation unless the user explicitly asks for that.

## Text workflow

When you add or rewrite text:

- keep the visible slide text in pt-BR unless the user asks otherwise
- preserve the direct, spoken voice already established in the deck
- run a humanizer pass on new or changed prose so it sounds spoken, not LLM-polished
- watch for jargon, English leftovers, and corporate phrasing the audience may not get

## Presenter notes

Presenter notes live as HTML comments in the slide markdown.

Rules:

- keep them shorter than the full script
- use short bullets, not dense prose
- treat them as stage cues
- keep the `Tempo sugerido` line roughly proportional to slide density

If the script changes meaningfully, update the matching notes.

## Slide and layout workflow

After slide or theme edits:

- rebuild with `bin/build-slides`
- check HTML, PDF, and PPTX, not just one output
- if the deck uses PPTX video overlays, also check `build/tropical-ruby-2026.with-video.pptx`
- if PDF breaks while HTML looks fine, simplify the layout

For this repo, prefer:

- flex layouts for raw HTML blocks
- conservative CSS for metric cards, grids, and slide furniture

Avoid:

- fragile CSS grid layouts in raw HTML blocks
- visual tricks that render in browser preview but disappear in PDF

## PPTX video workflow

Some slides contain `<!-- pptx-video: ... -->` markers in the markdown.

Rules:

- do not remove those markers unless you also remove the matching video asset and post-process entry
- keep poster images visible in the slide itself so HTML and PDF still make sense
- if you move the layout of a marked slide, verify the video placement in `scripts/embed_videos_pptx.py`
- `bin/build-slides` should produce both the raw PPTX and `build/tropical-ruby-2026.with-video.pptx`

## Practical commands

- preview server: `bin/serve-slides`
- full rebuild: `bin/build-slides`
- script preview: `sed -n '1,260p' script/full-script.md`

## Final check before committing

Before closing a meaningful edit:

- sync script, slides, and notes
- rebuild exports
- confirm the PDF is not missing layout blocks
- keep wording tight and human
