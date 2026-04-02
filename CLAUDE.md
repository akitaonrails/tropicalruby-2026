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
- keep the latest final build artifacts committed in the repo:
  - `build/tropical-ruby-2026.html`
  - `build/tropical-ruby-2026.pdf`
  - `build/tropical-ruby-2026.pptx`
  - `build/tropical-ruby-2026.with-video.pptx`
- do not keep temporary preview images or scratch subfolders inside `build/`

For this repo, prefer:

- flex layouts for raw HTML blocks
- conservative CSS for metric cards, grids, and slide furniture
- local files in `assets/` for images and media whenever practical, instead of third-party remote URLs

Avoid:

- fragile CSS grid layouts in raw HTML blocks
- visual tricks that render in browser preview but disappear in PDF

## PPTX video workflow

Some slides contain `<!-- pptx-video: ... -->` markers in the markdown.

Rules:

- do not remove those markers unless you also remove the matching video asset and post-process entry
- keep poster images visible in the slide itself so HTML and PDF still make sense
- if you move the layout of a marked slide, verify the video placement in `bin/embed_videos_pptx.py`
- `bin/build-slides` should produce both the raw PPTX and `build/tropical-ruby-2026.with-video.pptx`

## Practical commands

- preview server: `bin/serve-slides`
- full rebuild: `bin/build-slides`
- script preview: `sed -n '1,260p' script/full-script.md`

## Tutorial: build and run

If you are starting from a cold repo state, the safe flow is:

1. preview the deck in the browser with `bin/serve-slides`
2. open `http://localhost:8080/slides/tropical-ruby-2026.md`
3. if `8080` is busy, run `PORT=8081 bin/serve-slides` and open that port instead
4. preview the script separately with `sed -n '1,260p' script/full-script.md`
5. when you want final artifacts, run `bin/build-slides`
6. check all outputs in `build/`:
   - `tropical-ruby-2026.html`
   - `tropical-ruby-2026.pdf`
   - `tropical-ruby-2026.pptx`
   - `tropical-ruby-2026.with-video.pptx`

If something looks right in HTML but wrong in PDF, trust the PDF problem and simplify the layout.
If a PPTX video slide changed, always inspect the `.with-video.pptx`, not only the raw `.pptx`.

## Final check before committing

Before closing a meaningful edit:

- sync script, slides, and notes
- rebuild exports
- confirm the PDF is not missing layout blocks
- keep wording tight and human
- if the user asks for `git commit`, always rebuild first so the latest final artifacts are committed together with the source changes
