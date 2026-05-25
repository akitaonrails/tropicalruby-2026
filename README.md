# Web Summit Rio 2026 Keynote

**[View the presentation live](https://akitaonrails.github.io/tropicalruby-2026/)**

> **Branch note:** this branch (`web-summit-rio-2026`) is a condensed technology pitch prepared for **Web Summit Rio 2026**. The TotalPass 2026 lecture version lives on `totalpass2026`, and the original Tropical Ruby 2026 deck lives on [`master`](https://github.com/akitaonrails/tropicalruby-2026/tree/master).

This repo holds the working deck for the `Web Summit Rio 2026` pitch cut.
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

- `build/totalpass-2026.pptx`: raw Marp export
- `build/totalpass-2026.with-video.pptx`: post-processed PPTX; embeds local MP4s when the deck has `pptx-video` markers

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
- keep them as speaking cues, not a second full manuscript
- carry reminders that aren't visible on the slide itself (numbers, methodology, transition beats), not a restatement of what the audience is already reading
- the first line is `Restam: ~MM:SS (Ds)` — countdown remaining time on the wall clock plus duration of the current slide, in both the slide notes and the matching script section. The talk slot is 20:00, counting down to 00:00; the deck currently lands at ~01:00 of buffer remaining.

If you add or rewrite visible text, do a cleanup pass so it still sounds human and spoken, not like generated copy.

If you move or redesign a slide that contains an embedded PPTX video:

- keep the `<!-- pptx-video: ... -->` marker in the matching slide
- keep the poster image in the slide so HTML/PDF still have a visible placeholder
- rebuild the `.with-video.pptx` and verify the movie overlay still lands in the right place

## Narrative structure

This branch is a 20-minute pitch, not the full TotalPass lecture. Keep the spine tight:

- what changed: agents, not chatbots
- what was tested: 26 real projects, open code, measured commits/LOC/time
- what worked: Agile Vibe Coding as XP with machine pairing
- what the data says: model choice matters, but process and harness matter more
- what supports the workflow: ai-jail, ai-memory, and ai-usagebar keep multi-harness work controlled
- what to do now: disciplined AI engineering, not prompt theater

The TotalPass lecture blocks were intentionally cut. Do not re-expand layoffs, bootcamp fraud, Claude Code leak, AsamiArts/art analogy, China/geopolitics, or data-center energy unless explicitly asked.

Keep the ending lean: engineering conclusion, quick YouTube/newsletter plugs, deck-made-with-AI meta-stinger, clean `OBRIGADO` exit.

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
