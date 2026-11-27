# Gambiconf 2026: Agile Vibe Coding

**[View the presentation live](https://akitaonrails.github.io/tropicalruby-2026/)**

## Event editions

| Event | Branch | Notes |
| --- | --- | --- |
| Tropical Ruby 2026 | [`master`](https://github.com/akitaonrails/tropicalruby-2026/tree/master) | Original keynote deck |
| TotalPass 2026 | [`totalpass2026`](https://github.com/akitaonrails/tropicalruby-2026/tree/totalpass2026) | Longer lecture version |
| Beyond Summit 2026 | [`beyondsummitey`](https://github.com/akitaonrails/tropicalruby-2026/tree/beyondsummitey) | Beyond Summit edition |
| Web Summit Rio 2026 | [`web-summit-rio-2026`](https://github.com/akitaonrails/tropicalruby-2026/tree/web-summit-rio-2026) | Condensed 20-minute technology pitch |
| Canal 3 Expo 2026 | [`c3-expo-2026`](https://github.com/akitaonrails/tropicalruby-2026/tree/c3-expo-2026) | Retro-gaming event edition: AI half + retro launchers half |
| Gambiconf 2026 | [`gambiconf-2026`](https://github.com/akitaonrails/tropicalruby-2026/tree/gambiconf-2026) | Keynote edition: Agile Vibe Coding, LLM benchmarks (commercial + open-weight), `ai-jail`/`ai-memory`, condensed retro launchers, and `my-skills` (current live deck) |

This branch holds the keynote deck for [Gambiconf 2026](https://gambiconf.dev/) (*Agile Vibe Coding — Entendendo "IA" Direito*). It is the edition published at the live link above (GitHub Pages deploys from `gambiconf-2026`).
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

Artifacts are written to `build/`, named after the current git branch (`bin/deck-name`; override with `DECK_NAME=...`). On this branch:

- `build/gambiconf-2026.html`: the deck served on GitHub Pages (`index.html` redirects to it; the build updates the redirect)
- `build/gambiconf-2026.pdf`
- `build/gambiconf-2026.pptx`: raw Marp export, with presenter notes
- `build/gambiconf-2026.with-video.pptx`: the same PPTX with the 5 game clips embedded in the file (autoplay, no loop: looping video can hang LibreOffice's slideshow)

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
- the first line is `Restam: ~MM:SS (Ds)` — countdown remaining time on the wall clock plus duration of the current slide, in both the slide notes and the matching script section. The talk slot is 60:00, counting down to 00:00; the deck currently runs ~35:07 and lands at ~24:53 remaining, left for Q&A.

If you add or rewrite visible text, do a cleanup pass so it still sounds human and spoken, not like generated copy.

If you move or redesign a slide that contains an embedded PPTX video:

- keep the `<!-- pptx-video: ... -->` marker in the matching slide
- keep the poster image in the slide so HTML/PDF still have a visible placeholder
- rebuild the `.with-video.pptx`: the build measures each video's position in the rendered HTML (`bin/measure_videos.py`) and places the movie exactly over the poster baked into the slide image

## Narrative structure

This edition has 64 slides organized into four main blocks and a closing:

- **AI & Benchmarks (slides 1–19)**: Gambiconf 2026 title, speaker bio, "Heróis ou Vilões", "Papagaios Estocásticos", LLM Benchmark v4/v5 convergence & cost arc ("Qualidade convergiu", X tier list, "16 de 16 passaram / 95×", "Preço de tabela engana", "Zero FOMO: Gemini 4 Neon / Opus 5.5 / GPT-6.2 Sol"), China/hardware caveats (Nvidia 10-K/10-Q Singapore 22% surge, Gamers Nexus smuggling, Alice Huang / Megaspeed & Malaysia/Indonesia remote cloud loophole, Anthropic/OpenAI distillation), open-weight benchmarks (4× B300 vs. Anthropic/OpenAI economics, Strix Halo vs. RTX 5090 + Basalt, Thinking Machines Lab / Mira Murati, Inkling 2 Mini Looped MoE), and "Não era exponencial"
- **Agents & Toolkit (slides 20–34)**: 2025 agents timeline, December 2025 turn, 2026 GitHub marathon wall, CLI tools, `ai-jail` (Arch AUR install, kernel wall vs. built-in sandbox, guided TUI), `ai-memory` (Arch AUR install, Capture→Consolidate→Recall→Handoff, retention/compaction + Git `restore-page`, multi-agent team server, 214-contributor community mosaic)
- **Condensed Retro / REA Proof (slides 35–49)**: 14-slide streamlined retro block (`distrobox-gaming`, Windows 11 legacy diagram, Omarchy games menu video, Colin McRae 4K launcher & Rust recompilation stats + video, `rea-launcher-sdk`, "Bug velho, conserto em horas", Rad Mobile video, console→arcade→PC diagrams, Initial D S5 video, "Melhor que no lançamento", 14 `rea-*` launchers summary, AI Lair games page)
- **Lessons Learned & Agile Vibe Coding (slides 50–61)**: `github.com/akitaonrails/my-skills` intro, symlinked skill architecture, 5-skill maintenance pipeline (`pr-audit`, `iss-audit`, `github-resolution`, `pr-post-audit`, `release`), Trust Boundary & Hard Quality Bar, "O que é Agile Vibe Coding de verdade", "Números que pesam", "Você não tem objetivos", "O sprint ideal", "Codar é Barato. Errar é Barato.", "Agile Vibe Coding é XP com pareamento de máquina", "O pareamento mudou", and "Alcançamos 'Developer 10x'?"
- **Ending (slides 62–64)**: *Competente o Suficiente* book, `OBRIGADO`, and the *The M.Akita Chronicles* newsletter QR slide (left up during Q&A)

Visual language: the AI / toolkit / Agile Vibe Coding slides use the **Gambiconf 2026** dark hacker-workshop identity (`ai ai-wine|ai-umber|ai-olive` — carbon-flame `#f34b21`, workbench-tangerine `#ff8915`, terminal-lime `#9ee36a`, blueprint dot-grid, and a 4px top gradient ribbon); the retro block keeps cool night grounds with scanlines (`rg-linux`, `rg-rally`, `rg-arcade`, `rg-street`, `rg-dossier`). Both are defined at the end of `themes/tropical-ruby.css`.

The highlight slides about the launchers carry credit caveats in their notes: several fixes build on community work, so do not claim "nobody fixed it before".

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

- Images and media are local files under `assets/`.
- Game clips live in `assets/games/*.mp4` (H.264 1080p30, ~45 s) and are stored with Git LFS; the Pages workflow checks out with `lfs: true`.
- Embedded video for PowerPoint is now handled as a post-process step after Marp export, because Marp itself does not embed playable video in PPTX.
