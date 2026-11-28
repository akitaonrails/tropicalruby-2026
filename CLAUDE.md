# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Marp-based keynote deck for **Gambiconf 2026** (*Agile Vibe Coding — Entendendo "IA" Direito*, https://gambiconf.dev/; evolved from the Canal 3 Expo 2026 and Beyond Summit 2026 editions). Most changes touch talk structure, wording, layout, or export quality. The talk is in pt-BR, authored by Fabio Akita.

## Key files

| Purpose | Path |
|---------|------|
| Slide deck (Marp markdown) | `slides/tropical-ruby-2026.md` |
| Speaker script | `script/full-script.md` |
| Theme CSS | `themes/tropical-ruby.css` |
| Marp config | `.marprc.yml` |
| Original brief / prompt history | `IDEA.md` |
| Source links | `research/sources.md` |
| Build outputs | `build/*.html`, `build/*.pdf`, `build/*.pptx` |

## Commands

| Task | Command |
|------|---------|
| Preview in browser | `bin/serve-slides` (auto-picks free port from 8080) |
| Full rebuild (HTML + PDF + PPTX + video PPTX) | `bin/build-slides` |
| Preview script | `sed -n '1,260p' script/full-script.md` |

## Keep these files aligned

When you change the talk, sync all three:

- `slides/tropical-ruby-2026.md`
- `script/full-script.md`
- presenter notes inside `slides/tropical-ruby-2026.md`

Do not update one in isolation unless the user explicitly asks for that.

## Text workflow

- Keep visible slide text in pt-BR unless the user asks otherwise
- Preserve the direct, spoken voice already established in the deck
- Run a humanizer pass on new or changed prose so it sounds spoken, not LLM-polished
- Watch for jargon, English leftovers, and corporate phrasing

## Presenter notes

Presenter notes live as HTML comments (`<!-- ... -->`) in the slide markdown.

- Keep them shorter than the full script — short bullets, not dense prose
- Treat them as stage cues
- Notes should carry reminders the presenter won't see on the slide itself: specific numbers, dates, methodology caveats, transition cues — not a restatement of the visible content
- The first line is `Restam: ~MM:SS (Ds)` — countdown remaining time on the wall clock (starting from a 60:00 slot, counting down to 00:00) plus current slide duration in seconds. The script file uses the same format. Both are rebuilt together whenever pacing changes.
- Total slot is 60:00; deck currently lands at ~14:08 remaining (buffer for Q&A). Actual deck runtime is ~45:52 across 67 slides.
- If the script changes meaningfully, update the matching notes

## Visual language

- AI / toolkit / Agile Vibe Coding slides (`ai ai-wine|ai-umber|ai-olive`) use the **Gambiconf 2026** dark hacker-workshop identity: carbon-flame (`#f34b21`), workbench-tangerine (`#ff8915`), and terminal-lime (`#9ee36a`) with a blueprint dot-grid and a 4px top gradient ribbon. Defined at the end of `themes/tropical-ruby.css`.
- Retro block slides (slides 35–48) use `tone-extra-dark rg rg-<chapter>`: cool night grounds with faint CRT scanlines, one ground + accent per chapter (`--ruby` is overridden per chapter): `rg-linux`, `rg-rally`, `rg-arcade`, `rg-street`, `rg-dossier`. New retro slides take their chapter's class.
- Keep the two families distinct; do not reuse the light `tone-moss/ruby/sand` paper tones for new slides in either block.
- Background photos in `section.ai` slides use `![bg cover opacity:.15 blur:7px]` so they never compete with the text.
- The title slide uses `assets/akita-portrait-cutout.png` (transparent background) and `assets/gambiconf-logo.png`.

## Slide and layout workflow

After slide or theme edits:

- Rebuild with `bin/build-slides`
- Check HTML, PDF, and PPTX — not just one output
- If the deck uses PPTX video overlays, also check `build/<branch>.with-video.pptx`
- If PDF breaks while HTML looks fine, trust the PDF problem and simplify the layout
- Keep the latest final build artifacts committed in the repo
- Do not keep temporary preview images or scratch subfolders inside `build/`

Prefer:

- Flex layouts for raw HTML blocks
- Conservative CSS for metric cards, grids, and slide furniture
- Local files in `assets/` for images and media instead of remote URLs

Avoid:

- CSS grid layouts in raw HTML blocks (fragile in Marp export)
- Visual tricks that render in browser preview but disappear in PDF

## HTML video workflow

- Game videos live in `assets/games/` (H.264 1080p30, ~45s clips, Git LFS via `.gitattributes`), each with a `.jpg` poster
- Use `<video class="deck-video" ... playsinline>` with no `loop`: no video loops, in HTML or PPTX (a looping video hangs LibreOffice's slideshow). Add `data-volume="0.25"` for sound, or `muted autoplay` for silent clips
- Slide 14 (CLI tools) shows screenshots as `.term` terminal windows (theme CSS), not bare images
- A small `<script>` on the first game slide plays only the active slide's video and pauses the rest; browsers keep the first video muted until a key press or click
- Keep the matching `VideoSpec` (with `volume`) in `bin/embed_videos_pptx.py`
- The Pages workflow checks out with `lfs: true`; without it the videos would be LFS pointer files

## PPTX video workflow

Some slides contain `<!-- pptx-video: ... -->` markers in the markdown.

- Do not remove those markers unless you also remove the matching video asset and post-process entry
- Keep poster images visible in the slide so HTML and PDF still make sense
- Video placement is automatic: Marp bakes each PPTX slide into one flat image, so `bin/measure_videos.py` renders the deck (bare template) in headless Chrome and records each `video.deck-video` box; `bin/embed-videos-pptx` passes those boxes to `bin/embed_videos_pptx.py`, which lays the movie exactly over the baked poster. A video that overflows its slide in HTML overflows in PPTX too, so keep video slides inside 720px
- `bin/build-slides` produces `build/<branch>.{html,pdf,pptx,with-video.pptx}`; the name comes from `bin/deck-name` (git branch, or `DECK_NAME`), and the build rewrites the `index.html` redirect to match

## Narrative structure

The deck has a deliberate three-act shape — don't break it casually when moving slides:

- **Act 1**: "Heróis ou Vilões" (CEO controversy: Altman, Amodei, Huang) as the hook, then what LLMs really are and what they cost (stochastic parrots, sycophancy, October benchmark top 20, "Não era exponencial")
- **Act 2**: what actually changed and the practical proof ("2025 foi o ano dos Agentes" timeline → "Dezembro de 2025 foi a Virada" hinge → January 2026 trigger → marathon projects → metrics → CLI tools / ai-jail / ai-memory → Ciclo do Agente / PILOTA mechanism)
- **Act 3**: currently cut — the deck goes from "Developer 10x?" to the "Competente o Suficiente" book slide and then the ending (China/compute, market correction, junior/senior and the engineering conclusion were removed)

The ending: "Competente o Suficiente" book → retro-gaming block (slides 20–53: distrobox-gaming, the AI-generated "Jogo velho não roda no Windows 11" diagram (DOS/Glide, Win9x/WinG/DirectX 5, XP/DX9/DRM → Windows 11 64-bit), omarchy-games-menu + video, Quiver catalog screenshot (quiverlauncher.com), Colin McRae on DuckStation, rea-colin-mcrae launcher + default/4k videos, HD backgrounds slide (two stacked wide screenshots), rea-colin-mcrae-recomp + v0.1.4 status stats (single-player complete) + video, Colin 04/2005/DiRT/DiRT Rally launcher grid, rea-launcher-sdk, "Bug velho, conserto em horas" fixes slide, Sega Rally Revo + OutRun 2006 launchers (`.lgrid` two-up), Wanszai YouTube + GitHub as the inspiration, rea-rad-mobile repo + launcher menu + video, then two AI-composited diagrams: "O console virou arcade" (Dreamcast→NAOMI/NAOMI 2/Atomiswave, Xbox→Chihiro, GameCube→Triforce) and "Depois o arcade virou PC" (Lindbergh/Type X/RingEdge → TeknoParrot, OpenParrot, Lindbergh Loader), Azimuth (azimuthforza.com), Wangan Midnight launcher + 6R video, Initial D launcher + THE ARCADE S5 video, Sega + Nintendo arcade launchers (`.lgrid` two-up), "Melhor que no lançamento" (`.upg-*` before→after rows: resolution on the left, pads and wheels on the right; caption credits SilentPatch, Xidi, Bekoha), two highlight slides: "Achados de verdade" (PC launchers: Screamer, DiRT Rally, Sega Rally Revo) and "Arcade no Linux, sem TeknoParrot" (Initial D 4, Wangan, Nintendo, Sega), whose notes carry the credit caveats (do not claim "nobody fixed it before"), then a two-column table of the 14 rea-* launchers as the summary) → AI Lair games page screenshot (ailair.akitaonrails.com/pt-br/games) → `OBRIGADO` → newsletter ad as the last slide (left up during Q&A).

Key structural constraints:

- The real midpoint turn is the jump from "Dezembro de 2025 foi a Virada" into "Fevereiro a novembro de 2026" — should feel like "parei de opinar e fui testar com pele em jogo"
- The marathon wall / "60 projetos" GitHub activity / metrics (slide 13, right after the wall) / CLI tools, ai-jail and ai-memory sites / "Developer 10x?" are the proof block — opinion becomes evidence here
- Hard benchmark data now lives in the "Top 20 de outubro" table (slide 5, right after "Papagaios Estocásticos"), followed by the internet tier-list image as contrast and the "Quanto custa ser competente" cost bar chart (slide 7, real API cost of the 16 models from the Nov 20 2026 v5 benchmark post); the old April benchmark arc was cut
- Prefer explicit cause-and-effect bridges between major blocks over adding new content

## Build environment caveats

- Local Node.js v25.7.0 breaks `@marp-team/marp-cli` — the `bin/marp` wrapper pins Node 22 via `npx -p node@22`
- PDF and PPTX export need Chromium with `--no-sandbox`, handled by `bin/chromium-no-sandbox`
- The PDF renderer is stricter than the browser — if layout looks fine in HTML but broken in PDF, suspect the CSS first
- Video embedding is a Python post-process step (`bin/embed_videos_pptx.py` using `python-pptx`) since Marp doesn't natively embed playable video in PPTX. System Python has no `python-pptx`: run the build with a venv that has it first on `PATH`

## Final check before committing

- Sync script, slides, and notes
- Rebuild exports with `bin/build-slides`
- Confirm the PDF is not missing layout blocks
- Keep wording tight and human
- If the user asks for `git commit`, always rebuild first so the latest final artifacts are committed together with the source changes
