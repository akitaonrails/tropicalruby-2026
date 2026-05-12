# Tropical Ruby 2026 Keynote

**[View the presentation live](https://akitaonrails.github.io/tropicalruby-2026/)**

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
- keep them as speaking cues, not a second full manuscript
- carry reminders that aren't visible on the slide itself (numbers, methodology, transition beats), not a restatement of what the audience is already reading
- the first line is `Restam: ~MM:SS (Ds)` — countdown remaining time on the wall clock plus duration of the current slide, in both the slide notes and the matching script section. The talk slot is 60:00, counting down to 00:00; the deck currently lands at ~08:47 of buffer remaining.

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
- the mid-section peaks around the `2025 foi o ano dos Agentes` timeline, the `Dezembro de 2025 foi a Virada` hinge, the January 2026 trigger, the marathon wall of projects, `Alcançamos "Developer 10x"?`, and the `Ciclo do Agente / PILOTA` mechanism
- the closing widens back out to XP discipline, the benchmark arc (slides 33-37), pricing economics, the energy-and-IPO speculation, market correction, juniors/seniors, and finally engineering as the durable thing

The ending currently has three layers on purpose:

- the engineering conclusion (`Vai sobreviver quem souber fazer engenharia`)
- the shameless newsletter ad
- the meta-stinger that the deck itself was made with AI, followed by a clean `OBRIGADO` exit slide

If this sequence changes, re-check not just title order but also pacing, reveal order, and whether the practical proof still lands before the mechanism explanation.

There are also a few narrative constraints from later story-tightening passes:

- the real midpoint turn is the jump from `Dezembro de 2025 foi a Virada` into `Fevereiro e março de 2026`
- that transition should feel like `parei de opinar e fui testar com pele em jogo`
- the FrankMD vs M.Akita Chronicles comparison, the marathon wall, the metrics, and the `Developer 10x?` slide are the proof block; treat them as the point where the talk stops being opinion and becomes evidence
- after the proof block, the `Ciclo do Agente` mechanism should read as an explanation of that evidence, not as abstract theory
- the benchmark arc from `Quem consegue bater o Claude Opus?` through `Assinatura ganha de pay-as-you-go` is the hard-data block; every number there is grounded in the April 5 2026 benchmark article in `research/sources.md`
- the closing run from `A correção` through `Vai sobreviver quem souber fazer engenharia` should escalate in this order:
  - diagnosis
  - hope
  - responsibility
  - hard truth
  - final statement

When editing the script or notes, prefer explicit cause-and-effect bridges between major blocks over adding new content.

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
