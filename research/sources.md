# Research Notes and Sources

As of **April 5, 2026**.

## Slide tool choice

Chosen tool: **Marp**

Reasons:

- Markdown-native authoring fits a rapid keynote drafting loop.
- Official CLI supports export to **HTML, PDF, and PPTX**.
- Official docs explicitly state the PPTX output can open in **PowerPoint, Keynote, Google Slides, LibreOffice Impress, and so on**.
- The default `bespoke` template supports simple slide transitions.

Runner-up: **Slidev**

- Strong web-slide experience.
- Official docs show export to PDF, PPTX, and PNG.
- Heavier than needed for this deck and less aligned with the desired stripped-down zen style.

## Key factual anchors

### OpenAI

- GPT-5.1 released for developers on **November 13, 2025**.
- GPT 5.4 is the current flagship for coding and agentic tasks (as of April 2026).
- GPT 5.4 Pro charges $180/M output tokens via OpenRouter; ChatGPT Pro ($200/month) gives unlimited access.

### Anthropic

- Claude Opus 4.5 released on **November 24, 2025**.
- Claude Pro official announcement price: **$20/month**.
- Current Max pricing in Anthropic Help Center: **Max 5x $100/month**, **Max 20x $200/month**.

### Layoffs

- On **April 1, 2026**, CIO reported Oracle cutting up to **30,000** jobs globally.
- I treat this as a **reported current event**, not a timeless settled fact, so the slide language says “reportedly.”

### VTuber / art analogy

- Verified exact title of the referenced YouTube video through YouTube oEmbed:
  - `How a New AI Art Method Managed to Trick Over 100k People - The Unprecedented Case of AsamiArts`
- The detailed fraud mechanics in the script follow the user brief plus the verified video reference.
- I did not extract a full transcript in this pass.

## Local source material mined

### Recent AI / agent / vibe-coding arc

- `2026/02/08/rant-ia-acabou-com-programadores`
- `2026/02/20/do-zero-a-pos-producao-em-1-semana-como-usar-ia-em-projetos-de-verdade-bastidores-do-the-m-akita-chronicles`
- `2026/02/24/rant-o-akita-abriu-as-pernas-pra-ia`
- `2026/03/01/software-nunca-esta-pronto-4-projetos-a-vida-pos-deploy-e-por-que-one-shot-prompt-e-mito`
- `2026/03/05/37-dias-de-imersão-em-vibe-coding-conclusão-quanto-a-modelos-de-negócio`
- `2026/03/31/codigo-fonte-do-claude-code-vazou-o-que-achamos-dentro`
- `2025/05/02/rant-llms-sao-loot-boxes`
- `2026/04/05/testando-llms-open-source-e-comerciais-quem-consegue-bater-o-claude-opus`

### Older thesis / macro / learning arc

- `2019/06/11/akitando-50-a-bolha-de-startups-vai-estourar-winter-is-coming`
- `2019/10/09/akitando-63-nao-terceirize-suas-decisoes-a-licao-mais-importante-da-sua-vida`
- `2020/02/19/akitando-72-rant-programacao-nao-e-facil`
- `2020/03/24/akitando-75-o-que-vem-depois-do-covid-19`
- `2020/04/01/akitando-76-guia-definitivo-de-aprendendo-a-aprender-a-maior-bronca-da-sua-vida-rated-r`
- `2021/01/06/akitando-90-o-que-os-cursos-nao-te-ensinam-sobre-mercados`
- `2022/05/30/akitando-119-rant-aprendizado-na-beira-do-caos-rated-r`
- `2022/11/22/akitando-132-rant-a-bolha-de-startups-estourou`
- `2023/01/05/akitando-135-chatgpt-consegue-te-substituir-entendendo-jobs-assincronos`

## External sources

- Marp CLI: https://github.com/marp-team/marp-cli
- Slidev Guide: https://sli.dev/guide/
- OpenAI changelog entry for GPT-5.1: https://platform.openai.com/docs/changelog
- OpenAI GPT-5.1 docs: https://platform.openai.com/docs/models/gpt-5.1
- OpenAI GPT-5.1 announcement: https://openai.com/index/gpt-5-1-for-developers/
- Anthropic Opus 4.5 announcement: https://www.anthropic.com/news/claude-opus-4-5
- Anthropic Claude Pro announcement: https://www.anthropic.com/news/claude-pro/
- Anthropic Max pricing help article: https://support.anthropic.com/
- Oracle layoff report: https://www.cio.com/article/4153113/oracle-cuts-up-to-30000-jobs-globally-putting-enterprise-support-and-roadmaps-at-risk.html
- AsamiArts referenced video metadata: https://www.youtube.com/watch?v=bokGdQOHGrw
- IEA Energy and AI executive summary: https://www.iea.org/reports/energy-and-ai/executive-summary
- Berkeley Lab data center electricity demand report summary: https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/
- Anthropic Series G / compute capacity / Claude Code growth: https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
- NVIDIA on pretraining, post-training and test-time scaling: https://blogs.nvidia.com/blog/ai-scaling-laws/
- Anthropic IPO report carried by Reuters: https://m.economictimes.com/tech/artificial-intelligence/anthropic-plans-an-ipo-as-early-as-2026/amp_articleshow/125731426.cms
- LLM benchmark article (own, April 5, 2026): https://akitaonrails.com/2026/04/05/testando-llms-open-source-e-comerciais-quem-consegue-bater-o-claude-opus/
  - **Primary source for slides 33–37.** Published the same day akitaonrails.com turned 20 years old.
  - 22 models tested on identical runner. Only 4 produced working code: Claude Sonnet 4.6, Opus 4.6, GPT 5.4, and the GLM 5 / 5.1 pair from Z.AI.
  - GLM 5 is ~89% cheaper than Opus; GLM 5 if you need centralized OpenRouter billing, GLM 5.1 direct via Z.AI for a rounder project.
  - Per-token pricing on OpenRouter (slide 37): GPT 5.4 Pro $180/M output, Opus $25/M, GLM 5 $2.30/M, Qwen 3.6 Plus free (rate-limited).
  - Subscription vs API math for moderate coding use (~15M input + ~3M output tokens/month): GPT 5.4 Pro via API ≈ $990/mo vs ChatGPT Pro $200/mo unlimited (5× cheaper); Claude Opus via API ≈ $450/mo vs Claude Max 20x $200/mo (~220K tokens/5hr, ~half price).
  - Qwen family (slide 35): Coder-labeled models underperformed general ones. Qwen 3 Coder 30B hardcoded a mock string; Qwen 2.5 Coder 32B ran 90min timeout with zero files. The only Qwen variation still worth testing is Qwen 3.5 35B-A3B MoE general (runs Rails, hallucinations fixable in 1-2 follow-ups).
  - DeepSeek fails the agentic benchmark not because of model quality but because it doesn't close the three conditions (prompt caching + tool calling + reasoning/thinking) together.
  - Hardware behind the benchmark: RTX 5090 (32GB GDDR7) + Minisforum MS-S1 with AMD Ryzen AI Max+ 395 and 128GB unified memory. Open source via llama.cpp local, commercial via OpenRouter.
- claw-code (clean-room clone of Claude Code, <24h after leak): https://github.com/ultraworkers/claw-code
- memclaw (Claude-inspired memory system for OpenClaw): https://github.com/Felo-Inc/memclaw
- frank_karaoke (Flutter/Android, karaoke scoring app): https://github.com/akitaonrails/frank_karaoke

## What is intentionally left for a later pass

- Freezing all remote images into a local `assets/` directory for fully offline export.
- Building a final HTML/PDF/PPTX artifact in this repo.
- Replacing a few visual placeholders with literal website screenshots.
- Tightening the deck from keynote-draft length into the exact final conference runtime.
