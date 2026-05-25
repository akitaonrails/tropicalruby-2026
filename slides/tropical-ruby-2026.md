---
marp: true
theme: tropical-ruby
paginate: true
html: true
title: Web Summit Rio 2026 - Agile Vibe Coding
author: Fabio Akita
description: Pitch em pt-BR sobre agentes de IA, engenharia, processo e o uso prático de AI-assisted coding em 2026.
---

<!-- _class: title -->
![bg right:41% cover](../assets/akita-upscaled-gemini31.png)
<div class="eyebrow">Web Summit Rio 2026 Pitch</div>

# <span style="font-size:1.6em;display:block;line-height:1;">Agile</span><span style="display:block;margin-top:6px;">Vibe Coding</span>

## O Preço de Vibe Coding

<!--
Restam: ~19:10 (50s)

- Abrir direto: isto é uma pitch talk, não a versão longa.
- Tese: agentes mudaram o custo de construir software, mas não aboliram engenharia.
- A pergunta certa não é "IA substitui dev?". É "qual processo sobrevive quando o erro ficou barato?"
-->
---

<!-- _class: center tone-moss -->
# Fabio Akita

<div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:24px;justify-content:center;">
  <div class="card" style="flex:0 0 calc(33.33% - 10px);"><strong style="display:block;font-size:1.3em;margin-bottom:6px;">Codeminer 42</strong><span class="mini">cofundador, hoje no conselho</span></div>
  <div class="card" style="flex:0 0 calc(33.33% - 10px);"><strong style="display:block;font-size:1.3em;margin-bottom:6px;">RubyConf Brasil</strong><span class="mini">fundador e organizador até 2016</span></div>
  <div class="card" style="flex:0 0 calc(33.33% - 10px);background:rgba(107,142,90,0.24);border:2px solid #6b8e5a;"><strong style="display:block;font-size:1.3em;margin-bottom:6px;">akitaonrails.com</strong><span class="mini">20 anos em 5 de abril de 2026, 700+ artigos, agora em pt-BR e en</span></div>
  <div class="card" style="flex:0 0 calc(33.33% - 10px);"><strong style="display:block;font-size:1.3em;margin-bottom:6px;"><svg width="22" height="22" viewBox="0 0 24 24" fill="#c4302b" style="vertical-align:-4px;margin-right:6px;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z"/></svg>@akitando</strong><span class="mini">500 mil+ seguidores no YouTube</span></div>
  <div class="card" style="flex:0 0 calc(33.33% - 10px);"><strong style="display:block;font-size:1.3em;margin-bottom:6px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:-3px;margin-right:6px;"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>@akitaonrails</strong><span class="mini">83,7 mil seguidores no X</span></div>
  <div class="card" style="flex:0 0 calc(33.33% - 10px);"><strong style="display:block;font-size:1.3em;margin-bottom:6px;">Flow + Inteligência Ltda</strong><span class="mini">alcance além da bolha tech</span></div>
</div>

<!--
Restam: ~18:25 (45s)

- Contexto rápido, sem virar currículo.
- Já vi hype demais para comprar fantasia fácil.
- O valor aqui vem de teste prático, código aberto e anos vendo moda passar.
-->
---

<!-- _class: statement -->
![bg right:42% opacity:.18](../assets/offline/thumb-programacao-nao-e-facil.jpg)
<div class="eyebrow">Antes do GPT</div>

# A bolha era velha.

## O ChatGPT foi o prego no caixão.

<div class="columns" style="margin-top:28px;">
  <div class="card"><strong>2020-2022</strong><br />eu já batia na promessa "qualquer um programa"</div>
  <div class="card"><strong>fim de 2022</strong><br />a correção começou antes da IA programar direito</div>
</div>

<!--
Restam: ~17:40 (45s)

- Amarrar autoridade: não comecei a falar disso quando IA virou moda.
- O canal de 500k+ já vinha batendo na bolha do programador fake e nos cursos prometendo atalho.
- ChatGPT apareceu logo depois e virou o prego no caixão da fantasia.
-->
---

<!-- _class: center tone-moss -->
<div class="eyebrow">2022-2024</div>

# A corrida era<br><span class="em-moss">parâmetro + compute</span>

<div style="display:flex;gap:30px;align-items:center;text-align:left;margin-top:10px;">
  <div style="flex:0 0 43%;display:flex;flex-direction:column;gap:12px;">
    <div class="card"><strong>GPT-3</strong><div class="mini">175B parâmetros virou o marco público da era moderna</div></div>
    <div class="card"><strong>PaLM / Llama / DeepSeek</strong><div class="mini">centenas de bilhões; MoE chega para ativar só parte do modelo</div></div>
    <div class="card"><strong>Lei de escala</strong><div class="mini">mais dado + mais parâmetro + mais compute ainda ajuda, mas cobra caro</div></div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/ai-scaling-laws-nvidia.jpg" alt="NVIDIA scaling laws chart" style="width:100%;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.22);" />
    <div class="caption" style="margin-top:8px;text-align:left;">NVIDIA, 2025: pretraining, post-training e test-time scaling.</div>
  </div>
</div>

<!--
Restam: ~16:55 (45s)

- A história até ali era intuitiva: maior modelo, mais dados, mais GPU.
- Isso entregou GPT-3, PaLM, Llama grande, DeepSeek V3 671B MoE.
- Mas aumento de parâmetro começou a cobrar cada vez mais por ganho incremental.
-->
---

<!-- _class: center tone-sand -->
<div class="eyebrow">O gargalo mudou</div>

# De treino gigante<br>para inferência útil

<div class="columns-3" style="margin-top:24px;">
  <div class="card"><strong>Treino ficou caro</strong><div class="mini">frontier training já passa de 100 MW; Epoch projeta múltiplos GW até 2030</div></div>
  <div class="card"><strong>Data center é lento</strong><div class="mini">transformador, energia, terreno, conexão: não nasce em sprint</div></div>
  <div class="card"><strong>Uso virou carga</strong><div class="mini">agente troca um prompt por dezenas de chamadas, tool calls e retries</div></div>
</div>

<div class="lead" style="max-width:960px;margin:26px auto 0 auto;text-align:center;">O ganho passou a vir de usar melhor o modelo existente: reasoning, tool calling, KV cache, prompt caching e harness maduro.</div>

<!--
Restam: ~16:10 (45s)

- Não dizer que scaling morreu; dizer que o ganho marginal ficou caro.
- Data center é escasso e lento; parte relevante da pressão vai para inferência conforme o uso cresce.
- Agents aproveitam otimizações de inferência e ferramenta, sem depender de mais uma ordem de magnitude de parâmetro.
-->
---

<!-- _class: center tone-moss -->
![bg cover opacity:.14](../assets/offline/bg-smith-mannequins.jpg)
<div class="eyebrow">A mudança real</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Smith_Matrix_mannequins.jpg</div>

# 2025 foi o ano dos <span class="em-moss">AGENTES</span>

<div class="stats">
  <div class="card"><strong>mar 2025</strong><span class="mini">Responses API, tools e Agents SDK viram produto</span></div>
  <div class="card"><strong>mai 2025</strong><span class="mini">Claude 4 pensa entre tool calls e Claude Code vira GA</span></div>
  <div class="card"><strong>ago 2025</strong><span class="mini">GPT-5 aguenta loop mais longo e erra menos no uso de ferramenta</span></div>
  <div class="card"><strong>nov 2025</strong><span class="mini">GPT-5.1 e Opus 4.5 refinam uso diário</span></div>
</div>

<div class="lead" style="max-width:none;margin-left:auto;margin-right:auto;">Não foi chatbot mais esperto. Foi modelo, ferramenta, terminal e loop fechando juntos.</div>

<!--
Restam: ~15:15 (55s)

- O produto mudou de autocomplete para agente operacional.
- Thinking/reasoning, tool calling e caching viraram a diferença prática.
- Harness maduro é o que deixa isso virar trabalho diário, não demo.
-->
---

<!-- _class: center -->
![bg cover opacity:.16](../assets/offline/bg-everest.jpg)
# Fevereiro a maio<br>de 2026

## eu parei de falar  
## e fui <span class="em-ruby">maratonar</span>

<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Mount_Everest_as_seen_from_Drukair2_PLW_edit.jpg</div>

<!--
Restam: ~14:55 (20s)

- Pele em jogo.
- Nada de prompt de brinquedo ou demo de SaaS fake.
- Projeto real, bug real, deploy real, pós-produção real.
-->
---

<!-- _class: center tone-sand -->
![bg cover opacity:.14](../assets/offline/bg-potter-clay.jpg)
<div class="eyebrow">Painel de projetos</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Potter_shaping_clay_on_a_traditional_manual_potter’s_wheel_in_India_01.jpg</div>

# Do zero<br>pra software real

<div class="thumb-grid">
  <img src="../assets/offline/project-frankmd-main.jpg" alt="FrankMD" />
  <img src="../assets/offline/project-frankmega-upload.png" alt="FrankMega" />
  <img src="../assets/offline/project-franksherlock.png" alt="Frank Sherlock" />
  <img src="../assets/offline/project-frankyomik-translate.png" alt="Frank Yomik" />
  <img src="../assets/offline/project-frankfbi-email.png" alt="Frank FBI" />
  <img src="../assets/frankkaraoke-screenshot.jpg" alt="Frank Karaoke" />
  <img src="../assets/investigator-screenshot.png" alt="Frank Investigator" />
  <img src="../assets/frankclaw-screenshot.png" alt="FrankClaw" />
</div>

<!--
Restam: ~14:30 (25s)

- Não explicar projeto por projeto nesta versão.
- Mostrar variedade: desktop, Rails, Rust, Flutter, mídia, deploy, ferramenta de uso real.
- O ponto é escala de experimentação, não portfólio bonito.
-->
---

<!-- _class: center tone-moss -->
![bg cover opacity:.18](../assets/flow/github.png)
<div class="eyebrow">Repositórios públicos</div>

# 26 projetos<br><span class="em-ruby">(experimentais)</span>

<div style="display:flex;gap:28px;align-items:center;justify-content:center;margin-top:8px;max-width:1100px;margin-left:auto;margin-right:auto;">
  <div style="flex:1 1 0;text-align:left;">
    <div class="lead" style="margin:0;">github.com/akitaonrails - tudo aberto, inclusive os erros.</div>
    <div class="caption" style="margin-top:14px;">"Todos os 26 projetos são perfeitos, modelos de excelência de código?" <strong>Absolutamente não.</strong> Alguns viraram software de uso diário, outros são protótipos. O importante foi rodar o ciclo de verdade.</div>
  </div>
  <div style="flex:0 0 42%;">
    <img src="../assets/maratona-conclusion.png" alt="Artigo: Terminando minha maratona de IA - sucesso ou fracasso?" style="width:100%;height:210px;object-fit:cover;object-position:top;border-radius:14px;box-shadow:0 14px 30px rgba(0,0,0,0.22);" />
  </div>
</div>

<!--
Restam: ~14:05 (25s)

- 26 projetos, várias linguagens, vários domínios.
- Disclaimer honesto: experimental não é sinônimo de perfeito.
- A prova não é "olha que produto lindo". É "rodei o ciclo em escala".
-->
---

<!-- _class: center tone-sand -->
![bg cover opacity:.14](../assets/offline/bg-swordsmith.jpg)
<div class="eyebrow">A prova pratica</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Master-Swordsmith-Goro-Masamune-Ukiyo-e.png</div>

# Mesmo dev.<br>Mesmo agente.<br>Processo diferente.

<div class="columns">
  <div class="card"><strong>FrankMD</strong><br />212 commits em 19 dias, refactor pesado, teste correndo atras</div>
  <div class="card"><strong>M.Akita Chronicles</strong><br />274 commits em 8 dias, TDD, CI e refatoração contínua</div>
</div>

<div class="lead" style="max-width:none;margin-left:auto;margin-right:auto;">A variável não foi "IA melhor". Foi <span class="em-moss">disciplina de engenharia</span> desde o primeiro commit.</div>

<!--
Restam: ~13:05 (60s)

- Esta comparação é o coração da palestra curta.
- Mesmo dev, mesmo agente, resultado diferente por causa do processo.
- FrankMD pagou decisão tardia. Chronicles começou com TDD, CI e refatoração contínua.
-->
---

<!-- _class: center tone-sand -->
![bg cover opacity:.16](../assets/offline/bg-elephant.jpg)
<div class="eyebrow">Recorte Web Summit Rio 2026</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:African_Bull_elephant_walking_towards_camera_in_August_2013.jpg</div>

# Números<br>que pesam

<div class="stats">
  <div class="card"><strong>432.134</strong><span class="mini">linhas úteis</span></div>
  <div class="card"><strong>62.643</strong><span class="mini">linhas de teste</span></div>
  <div class="card"><strong>2.241</strong><span class="mini">commits</span></div>
  <div class="card"><strong>~473 h</strong><span class="mini">horas ativas estimadas</span></div>
</div>

<div class="caption">Agregado de 26 projetos AI-assisted: `tokei` sem linhas em branco, contando código + comentários + markdown/conteúdo rastreado. `shadPS4` só na branch `gamma-debug`; `akitaonrails-hugo` só no recorte AI-era. Testes separados por path. Fora: assets, vendor, build, fixtures, snapshots e árvore de terceiros.</div>

<!--
Restam: ~12:00 (65s)

- Ferramenta: `bin/totalpass-metrics`, usando `tokei`.
- Critério: linha útil rastreada em git; sem branco, asset, vendor, build ou árvore de terceiros.
- Horas: sessões por commit, 90 min de corte, +20 min por sessão, teto de 8h.
- Não é tudo que trabalhei. É só o que dá para defender olhando commit.
-->
---

<!-- _class: center tone-sand -->
![bg cover opacity:.18](../assets/offline/bg-strongman.jpg)
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Basra_bodybuilding_competition_DVIDS288972.jpg</div>

# Alcançamos<br>"Developer 10x"?

<div class="stats">
  <div class="card"><strong>5x a 10x</strong><span class="mini">de velocidade</span></div>
  <div class="card"><strong>Mais tração</strong><span class="mini">menos bloqueio, menos procrastinação</span></div>
  <div class="card"><strong>Mais alcance</strong><span class="mini">stack inteira, ferramentas, deploy, documentação</span></div>
  <div class="card"><strong>Mais confiança</strong><span class="mini">testes, CI, refatoração, produção</span></div>
</div>

<!--
Restam: ~11:10 (50s)

- Resumo honesto da experiência: 5x a 10x em muitas tarefas.
- Não porque modelo ficou perfeito.
- O ganho vem de reduzir atrito: busca, repetição, teste, refactor, comando, tentativa rápida.
- Confiança só veio quando teste, CI e revisão continuaram no loop.
-->
---

<!-- _class: center tone-moss -->
![bg cover opacity:.16](../assets/offline/bg-magician.jpg)
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Thurston,_master_magician_all_out_of_a_hat._LCCN2014636958.jpg</div>

# Prompt único<br>é pra demo

<div class="columns">
  <div class="card"><strong>Produção é iteração</strong><br />bug, deploy, retorno, refatoração, ajuste de prompt</div>
  <div class="card"><strong>"Pronto" é mentira</strong><br />125 commits de pós-produção em 4 projetos</div>
</div>

<!--
Restam: ~10:25 (45s)

- A fantasia do prompt único vende bem no palco, mas morre em produção.
- Software real revela requisito, falha de API, bug de infra e uso que ninguém previu.
- Agente bom precisa de loop, não de uma frase mágica.
-->
---

<!-- _class: center tone-moss -->
![bg cover opacity:.10](../assets/offline/bg-agile-lifecycle.jpg)
<div class="eyebrow">Nome verdadeiro</div>

# <span style="font-size:1.35em;font-weight:900;letter-spacing:-0.02em;">Agile Vibe Coding</span>

## <span style="font-size:1.25em;font-weight:700;">é XP com pareamento de máquina</span>

<div class="columns-3">
  <div class="card"><strong>TDD</strong><div class="mini">segura erro de modelo antes de virar lama</div></div>
  <div class="card"><strong>CI por commit</strong><div class="mini">pega drift e regressão cedo</div></div>
  <div class="card"><strong>Refatoração contínua</strong><div class="mini">evita cirurgia cara depois</div></div>
</div>

<!--
Restam: ~09:25 (60s)

- O termo pega, mas por baixo é XP.
- TDD, CI e refatoração não ficaram velhos. Ficaram mais importantes.
- Com agente, dívida técnica cresce rápido. O freio também precisa ficar rápido.
-->
---

<!-- _class: center tone-moss -->
![bg cover opacity:.14](../assets/offline/bg-pair-programming.jpg)
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Pair_Programming.jpg</div>

# O pareamento mudou

<div class="columns">
  <div class="card"><strong>Eu trago</strong><br />direção, julgamento, contexto, gosto</div>
  <div class="card"><strong>O agente traz</strong><br />velocidade de execução, busca, fôlego operacional</div>
</div>

<div class="lead" style="max-width:none;margin-left:auto;margin-right:auto;">IA é espelho: sênior bom ganha alavancagem, programador ruim ganha velocidade pra errar.</div>

<!--
Restam: ~08:35 (50s)

- Divisão de responsabilidade: humano dirige, agente executa rápido.
- Reduzir agente a digitador burro desperdiça ferramenta.
- Entregar arquitetura para ele sozinho também piora.
-->
---

<!-- _class: center tone-sand -->
<div class="eyebrow">Código e dados públicos</div>

# github.com/akitaonrails/<br>llm-coding-benchmark

<div style="display:flex;justify-content:center;margin-top:10px;">
  <img src="../assets/llm-coding-benchmark.png" alt="LLM Coding Benchmark - README do repo" style="max-height:470px;" />
</div>

<!--
Restam: ~08:20 (15s)

- Tudo aberto: prompt, runner, config e resultados.
- Quatro rodadas documentadas entre abril e maio.
- Ponte rápida para o ranking.
-->
---

<!-- _class: center tone-sand -->
<div class="eyebrow">Resultado consolidado</div>

# <span class="em-moss">Maio/2026</span>

<div style="display:flex;justify-content:center;margin-top:6px;overflow:hidden;">
  <img src="../assets/benchmark-ranking.png" alt="Ranking final dos 24 modelos por score, tier, RubyLLM, tempo e custo" style="width:980px;max-width:none;" />
</div>

<!--
Restam: ~07:30 (50s)

- 24 modelos, mesma tarefa, score 0-100, Tier A/B/C/D.
- Topo: Opus 4.7 e GPT 5.4 empatam em 97. GPT 5.5 vem em 96 e custa menos.
- DeepSeek V4 Pro e Kimi K2.6 mostram que o gap fechou, mas só quando o harness aguenta.
- Mensagem: escolher modelo importa, mas o fluxo importa mais.
-->
---

<!-- _class: center tone-moss -->
![bg cover opacity:.14](../assets/offline/bg-thinker.jpg)
<div class="eyebrow">O que separa Tier A</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:The_Thinker_detail_of_the_Gates_of_Hell_Rodin_musée_Rodin_S.01304_Paris.jpg</div>

# Não é mais só parâmetro

<div class="columns-3">
  <div class="card"><strong>Prompt caching</strong><div class="mini">sem cache, cada turno relê o contexto inteiro e o custo explode</div></div>
  <div class="card"><strong>Tool calling</strong><div class="mini">o modelo precisa chamar ferramenta certa, com argumento certo</div></div>
  <div class="card"><strong>Reasoning</strong><div class="mini">budget extra para planejar antes de agir</div></div>
</div>

<div class="caption">Tamanho virou commodity. Agente real precisa de infraestrutura de inferência, não só parâmetro no release note.</div>

<!--
Restam: ~06:35 (55s)

- A pergunta do ranking: por que poucos modelos aguentam?
- Parâmetro virou commodity.
- O que separa: cache, tool calling e reasoning trabalhando juntos.
- Sem isso, o modelo até sabe responder, mas não aguenta um loop de agente.
-->
---

<!-- _class: center tone-moss -->
![bg cover opacity:.14](../assets/offline/bg-kintsugi.jpg)
<div class="eyebrow">A virada econômica</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Kintsugi.jpg</div>

# IA nunca vai ser <span class="em-moss">perfeita</span>.

## Mas errar ficou barato.

<div class="columns-3">
  <div class="card"><strong>Roda</strong><div class="mini">agente executa, testa, quebra e mostra o stack trace</div></div>
  <div class="card"><strong>Corrige</strong><div class="mini">o loop volta em segundos, não em dias</div></div>
  <div class="card"><strong>Decide</strong><div class="mini">humano ainda corta escopo, arquitetura e risco</div></div>
</div>

<div class="caption" style="margin-top:18px;"><strong>Barato:</strong> CRUD, landing page, painel interno, bot, ETL, cola entre APIs. &nbsp;|&nbsp; <strong>Caro:</strong> julgamento, arquitetura, operação, dono do problema.</div>

<!--
Restam: ~05:45 (50s)

- A leitura errada é esperar modelo perfeito.
- A leitura certa: o custo do erro caiu.
- Stack trace, conserto e retry em segundos mudam a economia do software trivial.
- Mas decisão, arquitetura e operação continuam caros.
-->
---

<!-- _class: center tone-sand -->
<div class="eyebrow">Recomendação prática</div>

# As únicas ferramentas pra <span class="em-moss">usar agora</span>

<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:18px;margin-top:10px;max-width:1080px;margin-left:auto;margin-right:auto;">
  <div style="flex:0 0 calc(50% - 18px);display:flex;flex-direction:column;align-items:center;">
    <img src="../assets/clis/screenshot-2026-05-12_15-32-53.png" alt="Claude Code" style="width:100%;max-height:170px;object-fit:contain;" />
    <div style="margin-top:6px;font-size:0.85em;"><strong>Claude Code</strong></div>
  </div>
  <div style="flex:0 0 calc(50% - 18px);display:flex;flex-direction:column;align-items:center;">
    <img src="../assets/clis/screenshot-2026-05-12_15-32-58.png" alt="Codex" style="width:100%;max-height:170px;object-fit:contain;" />
    <div style="margin-top:6px;font-size:0.85em;"><strong>Codex</strong></div>
  </div>
  <div style="flex:0 0 calc(50% - 18px);display:flex;flex-direction:column;align-items:center;">
    <img src="../assets/clis/screenshot-2026-05-12_15-33-00.png" alt="opencode" style="width:100%;max-height:170px;object-fit:contain;" />
    <div style="margin-top:6px;font-size:0.85em;"><strong>opencode</strong></div>
  </div>
  <div style="flex:0 0 calc(50% - 18px);display:flex;flex-direction:column;align-items:center;">
    <img src="../assets/clis/oh-my-pi.png" alt="Oh-My-Pi" style="width:100%;max-height:170px;object-fit:contain;" />
    <div style="margin-top:6px;font-size:0.85em;"><strong>Oh-My-Pi</strong></div>
  </div>
</div>

<!--
Restam: ~05:15 (30s)

- Em maio de 2026, estes quatro cobrem o caso sério de agente de terminal.
- Claude Code e Codex para fronteira fechada.
- opencode e Oh-My-Pi para modelo agnóstico, benchmark e OpenRouter.
-->
---

<!-- _class: center tone-sand -->
![bg cover opacity:.10](../assets/offline/bg-spaghetti-cables.jpg)
<div class="eyebrow">Toolkit open source</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Server_Rack_with_Spaghetti-Like_Mass_of_Network_Cables.jpg</div>

# Trocar de harness<br>sem perder controle

<div style="display:flex;gap:18px;align-items:stretch;justify-content:center;margin-top:18px;">
  <div class="card" style="flex:1 1 0;padding:18px;display:flex;flex-direction:column;align-items:center;min-height:330px;">
    <img src="../assets/ai-jail.png" alt="ai-jail" style="height:135px;max-width:100%;object-fit:contain;margin-bottom:12px;" />
    <strong style="font-size:1.2em;">ai-jail</strong>
    <div class="mini" style="margin-top:8px;">autonomia do agente com cerca no filesystem</div>
  </div>
  <div class="card" style="flex:1 1 0;padding:18px;display:flex;flex-direction:column;align-items:center;min-height:330px;background:rgba(107,142,90,0.18);border:2px solid #6b8e5a;">
    <img src="../assets/ai-memory-logo.png" alt="ai-memory" style="height:120px;max-width:100%;object-fit:contain;margin-bottom:20px;" />
    <strong style="font-size:1.2em;">ai-memory</strong>
    <div class="mini" style="margin-top:8px;">contexto que sobrevive ao Claude, Codex e opencode</div>
  </div>
  <div class="card" style="flex:1 1 0;padding:18px;display:flex;flex-direction:column;align-items:center;min-height:330px;">
    <img src="../assets/ai-usagebar-waybar.png" alt="ai-usagebar" style="height:135px;max-width:100%;object-fit:cover;object-position:right top;border-radius:10px;margin-bottom:12px;" />
    <strong style="font-size:1.2em;">ai-usagebar</strong>
    <div class="mini" style="margin-top:8px;">limite de plano visível antes de travar no meio da refatoração</div>
  </div>
</div>

<!--
Restam: ~04:50 (25s)

- Não é mais um orquestrador mágico.
- É kit de operação: cerca, memória e medidor de limite.
- Usagebar é apoio. Jail e memory são os conceitos importantes para trocar de harness sem virar bagunça.
-->
---

<!-- _class: center tone-ruby -->
![bg right:43% contain](../assets/ai-jail-og.png)
<div class="eyebrow">ai-jail</div>

# Autonomia<br>com cerca

<div style="display:flex;flex-direction:column;gap:12px;max-width:650px;margin-top:12px;text-align:left;">
  <div class="card"><strong>Modo sem freio no harness</strong><div class="mini">Claude/Codex com permissões perigosas, menos confirmação a cada passo</div></div>
  <div class="card"><strong>Trava no sistema operacional</strong><div class="mini">projeto read-write; host, home, cache e dotfiles ficam fora ou controlados</div></div>
  <div class="card"><strong>Política versionável</strong><div class="mini">`.ai-jail`, `--dry-run`, `--mask .env`, `--private-home`, `--lockdown`</div></div>
</div>

<div class="caption" style="margin-top:14px;text-align:left;max-width:650px;">Não é VM nem blindagem militar. É uma camada prática para deixar o agente trabalhar rápido sem dar a chave da casa.</div>

<!--
Restam: ~04:10 (40s)

- Uso preferido: tirar fricção dentro do harness, colocar a trava no OS.
- O agente trabalha rápido no projeto; o resto do host não fica aberto por acidente.
- Não vender como segurança absoluta: sandbox de processo não é VM.
-->
---

<!-- _class: center tone-moss -->
<div class="eyebrow">ai-memory</div>

<h1 style="font-size:2.45em;line-height:0.95;margin:0 0 16px 0;">Contexto que sobrevive<br>ao harness</h1>

<div style="display:flex;gap:28px;align-items:center;text-align:left;margin-top:0;">
  <div style="flex:0 0 45%;">
    <img src="../assets/ai-memory-logo.png" alt="ai-memory" style="width:100%;max-height:92px;object-fit:contain;margin-bottom:8px;" />
    <div class="card" style="margin-bottom:8px;padding:14px 16px;"><strong style="font-size:1.05em;">Hooks capturam</strong><div class="mini">prompt, tool call, decisão e boundary de sessão</div></div>
    <div class="card" style="margin-bottom:8px;padding:14px 16px;"><strong style="font-size:1.05em;">Markdown vira memória</strong><div class="mini">wiki versionável, FTS5, handoff e busca via MCP</div></div>
    <div class="card" style="padding:14px 16px;"><strong style="font-size:1.05em;">Troca de agente sem reexplicar</strong><div class="mini">fecha Claude hoje, abre Codex amanhã no mesmo diretório</div></div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/ai-memory-web-home.png" alt="ai-memory web UI" style="width:100%;max-height:330px;object-fit:contain;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.24);" />
    <div class="caption" style="margin-top:10px;text-align:left;">Não substitui `docs/` canônico. Cobre gotchas, decisões transitórias e handoff entre sessões.</div>
  </div>
</div>

<!--
Restam: ~03:30 (40s)

- Problema: harness compacta ou acaba, e o próximo agente esquece as últimas horas.
- ai-memory captura e consolida em markdown pesquisável.
- Documentação importante ainda vai para `docs/`; memória cobre o transitório que seria perdido.
-->
---

<!-- _class: statement -->
![bg right:45% opacity:.22](../assets/offline/bg-mirror-vanity.jpg)
<div class="eyebrow">A regra que não mudou</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Peter_Candid_(attr)_Allegory_of_vanity.jpg</div>

# IA reflete quem você é

## Ela te acelera: se você for bom, fica melhor. Se for ruim, vai errar mais rápido.

<!--
Restam: ~02:50 (40s)

- IA não cria competência do nada.
- Bom engenheiro ganha alavancagem.
- Mau engenheiro ganha velocidade para produzir lixo.
- Esta é a ponte para o fechamento.
-->
---

<!-- _class: end -->
![bg cover opacity:.16](../assets/offline/bg-mountain-climber.jpg)
<div class="eyebrow">Conclusão</div>
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Mountain_Climber_In_Mountains_(Unsplash).jpg</div>

# Vai <span class="em-moss">sobreviver</span><br>quem souber<br>fazer <span class="em-moss">engenharia</span>.

## IA não transforma coder ruim em engenheiro.
## Fundamento. Disciplina. Iteração. Gosto.

<!--
Restam: ~01:55 (55s)

- Fechar sem moralismo longo.
- IA ajuda programador ruim a fazer estrago maior mais rápido.
- Ajuda engenheiro bom a atravessar o caos sem deixar o software morrer.
- Não é truque de prompt. É fundamento, disciplina, iteração e gosto.
-->
---

<!-- _class: center tone-extra -->
![bg cover opacity:.12](../assets/epilogue-workflow-bg.png)
<div class="eyebrow">Akitando</div>

# O canal também<br>virou inglês

<div style="display:flex;gap:28px;align-items:center;text-align:left;margin-top:6px;">
  <div style="flex:0 0 35%;">
    <div class="card" style="margin-bottom:12px;"><strong>150+ vídeos</strong><div class="mini">traduzidos e legendados com agente</div></div>
    <div class="card" style="margin-bottom:12px;"><strong>20 anos de conteúdo</strong><div class="mini">blog bilingue e canal pronto pra mandar pra fora</div></div>
    <div class="lead" style="max-width:none;margin:0;">youtube.com/@Akitando</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/youtube-ingles.png" alt="Canal Akitando com títulos em inglês" style="width:100%;max-height:420px;object-fit:cover;object-position:top;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.28);" />
  </div>
</div>

<!--
Restam: ~01:45 (10s)

- Merchan rápido: canal traduzido.
- 150+ vídeos do Akitando em inglês.
- Pipeline com agente, não trabalho manual.
-->
---

<!-- _class: center tone-extra -->
<div class="eyebrow">Merchan sem vergonha</div>

<div style="display:flex;gap:36px;align-items:center;text-align:left;">
  <div style="flex:0 0 40%;">
    <h1 style="margin:0 0 18px 0;line-height:0.95;">Assine<br />The M.Akita Chronicles</h1>
    <div style="font-size:1.05em;font-weight:700;margin:0 0 18px 0;">themakitachronicles.com</div>
    <div class="lead" style="max-width:none;margin:0;">Notícias de tecnologia, opinião, código aberto e bastidor de projeto real. Toda semana.</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/makita-chronicles-subscribe-cropped.png" alt="The M.Akita Chronicles" style="height:520px;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.28);" />
  </div>
</div>

<!--
Restam: ~01:35 (10s)

- Segundo merchan rápido.
- Newsletter semanal: notícias de tecnologia, opinião, código aberto e bastidor real.
- Link: themakitachronicles.com.
-->
---

<!-- _class: center tone-extra -->
![bg cover opacity:.18](../assets/epilogue-workflow-bg.png)
<div class="eyebrow">Bastidor</div>

# Sim, este deck inteiro<br>foi feito com IA

<div class="columns-3">
  <div class="card"><strong>Pesquisa e estrutura</strong><div class="mini">fontes, ordem dos argumentos, cortes e rearranjos</div></div>
  <div class="card"><strong>Texto sincronizado</strong><div class="mini">slides, roteiro e presenter notes mantidos juntos</div></div>
  <div class="card"><strong>Mídia e acabamento</strong><div class="mini">frames, crops, builds e pós-processo do PPTX</div></div>
</div>

<div class="lead" style="max-width:980px;margin:22px auto 0 auto;text-align:center;">
Agente no terminal, Marp para gerar o deck, scripts para automatizar build e iteração curta até o resultado fechar.
</div>

<!--
Restam: ~01:05 (30s)

- Meta-stinger curto, sem virar propaganda.
- A própria palestra foi feita com a pilha que estou defendendo.
- Pesquisa, roteiro, notas, cortes, build e acabamento no mesmo fluxo.
-->
---

<!-- _class: center end tone-extra-dark -->
![bg cover opacity:.16](../assets/offline/bg-standing-ovation.jpg)
<div class="source-url">Fonte: https://commons.wikimedia.org/wiki/File:Standing_Ovation_(21835796).jpg</div>
<div style="display:flex;flex-direction:column;justify-content:center;align-items:center;min-height:100%;">
  <h1 style="font-size:3.9em;line-height:0.9;margin:90px 0 70px 0;letter-spacing:0.02em;">OBRIGADO</h1>
  <div class="card" style="margin-top:0;width:88%;padding:22px 28px;background:rgba(251,247,239,0.92);">
    <div style="font-size:0.58em;color:var(--muted);display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;">
      <span>codeminer42.com</span>
      <span>themakitachronicles.com</span>
      <span>github.com/akitaonrails/tropicalruby-2026</span>
    </div>
  </div>
</div>

<!--
Restam: ~01:00 (5s)

- Obrigado.
- Links no rodapé.
-->
