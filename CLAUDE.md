# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Marp-based keynote deck for Tropical Ruby 2026, not a generic app. Most changes touch talk structure, wording, layout, or export quality. The talk is in pt-BR, authored by Fabio Akita.

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
- The first line is `Terminar em: ~MM:SS (Ds)` — end-time on the wall clock plus current slide duration in seconds. The script file uses the same format. Both are rebuilt together whenever pacing changes.
- Total runtime target is 50:00 (last slide ends at ~50:00)
- If the script changes meaningfully, update the matching notes

## Slide and layout workflow

After slide or theme edits:

- Rebuild with `bin/build-slides`
- Check HTML, PDF, and PPTX — not just one output
- If the deck uses PPTX video overlays, also check `build/tropical-ruby-2026.with-video.pptx`
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

## PPTX video workflow

Some slides contain `<!-- pptx-video: ... -->` markers in the markdown.

- Do not remove those markers unless you also remove the matching video asset and post-process entry
- Keep poster images visible in the slide so HTML and PDF still make sense
- If you move a marked slide's layout, verify video placement in `bin/embed_videos_pptx.py`
- `bin/build-slides` produces both the raw PPTX and `build/tropical-ruby-2026.with-video.pptx`

## Narrative structure

The deck has a deliberate three-act shape — don't break it casually when moving slides:

- **Act 1**: the panic is misdiagnosed (thesis, older warnings, AsamiArts fraud case, Claude Code leak)
- **Act 2**: what actually changed and the practical proof ("2025 foi o ano dos Agentes" timeline → "Dezembro de 2025 foi a Virada" hinge → January 2026 trigger → marathon projects → metrics → Ciclo do Agente / PILOTA mechanism)
- **Act 3**: what that means for engineers and the market (XP discipline, benchmark findings, pricing economics, energy speculation, "A correção", junior/senior, engineering as the durable thing)

The ending has three layers: engineering conclusion ("Vai sobreviver quem souber fazer engenharia") → newsletter ad → meta-stinger (deck made with AI) → clean `OBRIGADO` exit.

Key structural constraints:

- The real midpoint turn is the jump from "Dezembro de 2025 foi a Virada" into "Fevereiro e março de 2026" — should feel like "parei de opinar e fui testar com pele em jogo"
- The FrankMD vs M.Akita Chronicles comparison / marathon wall / metrics / "Developer 10x?" are the proof block — opinion becomes evidence here
- The benchmark arc (slides 33–37: "Quem consegue bater o Claude Opus?" → "Não é mais só parâmetros" → "'Coder' no nome não vira coder melhor" → "IA nunca vai ser perfeita. Mas errar ficou barato" → "Assinatura ganha de pay-as-you-go") is the hard-data block grounded in the April 5 2026 benchmark article
- The closing run from "A correção" through "Vai sobreviver quem souber fazer engenharia" escalates: diagnosis → hope → responsibility → hard truth → final statement
- Prefer explicit cause-and-effect bridges between major blocks over adding new content

## Build environment caveats

- Local Node.js v25.7.0 breaks `@marp-team/marp-cli` — the `bin/marp` wrapper pins Node 22 via `npx -p node@22`
- PDF and PPTX export need Chromium with `--no-sandbox`, handled by `bin/chromium-no-sandbox`
- The PDF renderer is stricter than the browser — if layout looks fine in HTML but broken in PDF, suspect the CSS first
- Video embedding is a Python post-process step (`bin/embed_videos_pptx.py` using `python-pptx`) since Marp doesn't natively embed playable video in PPTX

## Final check before committing

- Sync script, slides, and notes
- Rebuild exports with `bin/build-slides`
- Confirm the PDF is not missing layout blocks
- Keep wording tight and human
- If the user asks for `git commit`, always rebuild first so the latest final artifacts are committed together with the source changes
