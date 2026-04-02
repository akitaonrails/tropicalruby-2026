---
marp: true
theme: tropical-ruby
paginate: true
html: true
title: Tropical Ruby 2026 - Agile Vibe Coding
author: Fabio Akita
description: Keynote em pt-BR sobre agile vibe coding, agentes de IA, engenharia e o pós-bolha da programação.
---

<!-- _class: title -->
![bg right:41% cover](../assets/opening-right-portrait.jpg)
<div class="eyebrow">Tropical Ruby 2026 Keynote</div>

# Agile Vibe Coding
## IA substitui
## programador ruim.
## Não engenharia.

<!--
Tempo sugerido: ~0:45

- Eu quero abrir cravando a tese, porque o resto da palestra existe só pra sustentar isso.
- Sim, IA está substituindo gente em software.
- Mas não do jeito raso que o pânico de internet adora vender.
- O que ela pega primeiro é produtividade fake, senioridade fake e aquela engenharia porca que sobreviveu durante anos porque o mercado aceitava jogar dinheiro fora.
-->
---

<!-- _class: center tone-moss -->
# Fabio Akita

<div class="stats">
  <div class="card"><strong>Codeminer 42</strong><span class="mini">cofundador, hoje no conselho</span></div>
  <div class="card"><strong>RubyConf Brasil</strong><span class="mini">fundador e organizador até 2016</span></div>
  <div class="card"><strong>@akitando</strong><span class="mini">500 mil+ seguidores</span></div>
  <div class="card"><strong>Flow + Inteligência Ltda</strong><span class="mini">alcance além da bolha tech</span></div>
</div>


<!--
Tempo sugerido: ~0:40

- Pra quem só me conhece por um pedaço da internet: fui cofundador da Codeminer 42 e hoje estou no conselho.
- Fundei e organizei a RubyConf Brasil até 2016.
- Passei anos no YouTube com o Akitando.
- E também fui parar fora da bolha tech, em programas como Flow e Inteligência Ltda.
-->
---

<!-- _class: statement -->
![bg right:42% opacity:.18](https://img.youtube.com/vi/V7oUDL7E1g4/hqdefault.jpg)
<div class="eyebrow">Arco Longo</div>

# O pânico da IA
# caiu em cima
# de uma bolha velha.

<div class="lead">Eu já vinha batendo na economia do programador fake antes de agentes de código prestarem pra alguma coisa.</div>

<!--
Tempo sugerido: ~0:45

- Eu não comecei a falar disso quando IA virou moda.
- Eu já vinha batendo na bolha da programação, na economia do programador ruim, nas promessas de curso e bootcamp, muito antes de agente de código prestar pra alguma coisa.
- A IA não inventou essa fraqueza.
- Ela só escancarou mais rápido.
-->
---

<!-- _class: center -->
![bg cover opacity:.10](https://img.youtube.com/vi/wpPv1dJWjDs/hqdefault.jpg)
<div class="eyebrow">2019 → 2026</div>

# Mesma tese.
# Ferramenta nova.

<div class="timeline">
  <div class="card"><strong>2019</strong><span class="mini">o inverno estava chegando</span></div>
  <div class="card"><strong>2020</strong><span class="mini">programação não é fácil</span></div>
  <div class="card"><strong>2022</strong><span class="mini">a bolha estourou</span></div>
  <div class="card"><strong>2025</strong><span class="mini">LLMs são loot boxes</span></div>
  <div class="card"><strong>2026</strong><span class="mini">agentes ficaram úteis</span></div>
</div>


<!--
Tempo sugerido: ~0:50

- Tem uma linha reta aqui.
- Em 2019 eu já avisava que a bolha ia azedar.
- Em 2020 eu continuava repetindo que programação não é fácil.
- Em 2022 a bolha estourou de vez.
-->
---

<!-- _class: center -->
# A mentira antiga

## “vire engenheiro
## de software
## em 2 meses”

<div class="columns">
  <div class="card"><strong>Fim de 2022</strong><br />layoffs vieram antes da IA saber programar direito</div>
  <div class="card"><strong>ChatGPT</strong><br />foi acelerador, não causa original</div>
</div>


<!--
Tempo sugerido: ~0:55

- A mentira antiga era simples: faz um cursinho rápido, vira engenheiro de software, ganha salário alto e entra no modo easy.
- Isso sempre foi conversa mole.
- Bootcamp ensina ferramenta.
- Não comprime anos de julgamento de engenharia em poucos meses.
-->
---

<!-- _class: center -->
![bg cover opacity:.16](https://i.ytimg.com/vi/bokGdQOHGrw/hqdefault.jpg)
<div class="eyebrow">A Analogia</div>

# Mesmo medo.

## “IA vai substituir artista.”  
## “IA vai substituir programador.”

<!--
Tempo sugerido: ~0:35

- Pra explicar o pânico atual, eu quero fazer uma tangente rápida com um universo que eu acompanho por hobby: drama de VTuber e drama de arte.
- O padrão emocional é o mesmo.
- No mundo da arte dizem que IA vai substituir artista.
- No nosso dizem que IA vai substituir programador.
-->
---

<!-- _class: center tone-ruby -->
# Caso AsamiArts

<div style="display:flex;gap:32px;align-items:center;text-align:left;">
  <div style="flex:0 0 42%;">
    <div class="card">
      <strong>Isso não é só drama de internet</strong><br />
      tem mercado, comissão e renda real em volta disso
    </div>
    <div class="lead" style="max-width:none;">O ponto aqui não é fofoca. É processo falso vendido como habilidade real dentro de um mercado que vive de confiança.</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/vgen.jpg" alt="Marketplace VGen" style="width:100%;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.24);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:45

- O caso da AsamiArts me interessa não pela fofoca, mas pelo mecanismo.
- Isso não afeta só ego de artista no Twitter.
- Tem mercado real de comissão em volta disso.
- Quando processo falso entra, confiança sai.
-->
---

<!-- _class: center tone-ruby -->
# Tracing sem processo

<!-- pptx-video: asamiarts-tracing -->
<div style="display:flex;gap:32px;align-items:center;text-align:left;">
  <div style="flex:0 0 42%;">
    <ul>
      <li>não aparece construção bruta antes</li>
      <li>não aparece ida e volta de correção</li>
      <li>não aparece undo, hesitação, ajuste de proporção</li>
      <li>parece “mão firme”, mas parece firme demais</li>
    </ul>
    <div class="caption">No PPTX com vídeo: clique para reproduzir.</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/asamiarts tracing.jpg" alt="Frame do vídeo de tracing" style="width:100%;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.24);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:55

- Aqui é onde eu mostro o que um tracing falso tenta vender.
- Não tem sketch feio antes.
- Não tem correção de construção no meio.
- Sai limpo demais, reto demais, confiante demais.
-->
---

<!-- _class: center tone-ruby -->
# A camada escondida

<!-- pptx-video: tracing-hidden-layer -->
<div style="display:flex;gap:34px;align-items:center;text-align:left;">
  <div style="flex:0 0 48%;">
    <ul>
      <li>o vídeo não mostra o desenho “nascendo” de verdade</li>
      <li>minha leitura é que existe uma camada base escondida por trás</li>
      <li>o verde parece estar ali para sumir na edição</li>
      <li>sem a camada escondida, a mágica some</li>
    </ul>
    <div class="caption">Inferência a partir do vídeo: isso parece truque de gravação, não processo honesto.</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/tracing, hidden layer vertical.jpg" alt="Frame vertical mostrando a camada escondida" style="height:430px;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.24);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:55

- Esse é o pedaço mais importante.
- Minha leitura é que o vídeo esconde uma camada pronta por trás.
- O verde parece estar ali justamente para ser filtrado depois.
- O vídeo vende tracing; o truque está na composição.
-->
---

<!-- _class: center tone-ruby -->
# A evolução não bate

<div style="display:flex;gap:32px;align-items:center;text-align:left;">
  <div style="flex:0 0 45%;">
    <div class="card"><strong>em pouco tempo muda demais</strong><br />traço, rosto, acabamento e construção saltam sem continuidade</div>
    <div class="lead" style="max-width:none;">Evolução humana existe, claro. O problema é quando a “mão” parece trocar de pessoa em intervalos curtos demais.</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/asamiart inconsistent evolution.jpg" alt="Exemplo de evolução inconsistente no caso AsamiArts" style="width:100%;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.24);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:50

- Outro sinal é a inconsistência.
- Não é só “melhorou”.
- A mão muda demais em pouco tempo.
- Parece mistura de fontes diferentes, não evolução orgânica.
-->
---

<!-- _class: center tone-ruby -->
# A alucinação entrega

<div style="display:flex;gap:32px;align-items:center;text-align:left;">
  <div style="flex:0 0 42%;">
    <div class="card"><strong>o cano está do lado errado</strong><br />isso não é detalhe de estilo; é erro estrutural de entendimento</div>
    <div class="lead" style="max-width:none;">É o mesmo tipo de erro que a gente já conhece em IA: a imagem parece plausível à primeira vista, mas desmonta quando você olha a anatomia do objeto.</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/asamiarts halucination.jpg" alt="Exemplo de alucinacao em arte com arma desenhada errada" style="width:100%;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.24);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:45

- Aqui entra a alucinação mais óbvia.
- A arma parece arma até você olhar direito.
- O cano está do lado errado.
- Isso é erro de entendimento, não acabamento.
-->
---

<!-- _class: center tone-ruby -->
# LoRA é estilo empacotado

<div style="display:flex;gap:32px;align-items:center;text-align:left;">
  <div style="flex:0 0 45%;">
    <ul>
      <li>LoRA é um ajuste leve em cima de um modelo base</li>
      <li>ele empurra o modelo para um traço, tema ou artista específico</li>
      <li>a comunidade treinou muita LoRA com imagem pública e zero autorização</li>
      <li>depois isso volta disfarçado de “meu estilo”</li>
    </ul>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/asamiarts lora steal.jpg" alt="Exemplo de uso e roubo de estilos com LoRA" style="width:100%;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.24);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:55

- E tem outra camada aí: LoRA.
- LoRA é um ajuste leve em cima de um modelo base para puxar um traço específico.
- O problema é que muita LoRA foi treinada com arte pública sem autorização.
- Aí o roubo de estilo volta embalado como ferramenta.
-->
---

<!-- _class: statement -->
![bg right:45% opacity:.18](https://img.youtube.com/vi/Yl-hlwhj2B0/hqdefault.jpg)
<div class="eyebrow">Mesma Regra No Código</div>

# Trabalho de verdade
# parece bagunçado.

## IA só amplifica o que já estava lá.

<!--
Tempo sugerido: ~1:00

- E é aqui que isso volta pro código.
- Trabalho de verdade parece bagunçado.
- Artista de verdade erra, corrige, revisa, ajusta composição, muda junto com o pedido do cliente.
- Engenheiro de verdade faz a mesma coisa.
-->
---

<!-- _class: center tone-ruby -->
<div class="eyebrow">31 de março de 2026</div>

# Claude Code vazou

<div class="stats">
  <div class="card"><strong>512 mil</strong><span class="mini">linhas de TypeScript</span></div>
  <div class="card"><strong>1.900</strong><span class="mini">arquivos</span></div>
  <div class="card"><strong>59,8 MB</strong><span class="mini">de mapa do código exposto</span></div>
  <div class="card"><strong>6,5/10</strong><span class="mini">o “espaguete de sênior”</span></div>
</div>


<!--
Tempo sugerido: ~0:45

- Daí veio uma das confirmações mais engraçadas possíveis dessa tese: o vazamento do Claude Code em 31 de março de 2026.
- A CLI oficial da Anthropic deixou escapar um mapa enorme do código e, de repente, todo mundo pôde olhar as tripas de uma das ferramentas de agente mais importantes do mercado.
-->
---

<!-- _class: center -->
<div class="eyebrow">A Faísca</div>

<div style="display:flex;gap:34px;align-items:center;text-align:left;">
  <div style="flex:0 0 39%;">
    <h1 style="margin:0 0 18px 0;line-height:0.95;">Não foi rumor.<br />Foi vazamento.</h1>
    <div class="lead" style="max-width:none;margin:0;">A imagem de abertura do seu artigo já conta a história inteira: source map exposto, árvore de arquivos na mão de todo mundo e a mística indo embora em tempo real.</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/claude-code-leak-tweet.png" alt="Tweet do vazamento do Claude Code" style="height:480px;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.28);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:20

- E eu quis colocar a imagem de abertura do artigo justamente por isso.
- Ela resume o clima do negócio em um frame: o tweet, o link, a árvore de arquivos aparecendo, e a internet inteira percebendo em tempo real que dava pra abrir a caixa-preta.
- A mística acabou ali.
-->
---

<!-- _class: center tone-ruby -->
# A lição não foi
# “uau, magia”

<div class="columns">
  <div class="card"><strong>Nem a Anthropic escapa</strong><br />pressão de entrega também gera código tático</div>
  <div class="card"><strong>E copiaram rápido</strong><br />free-code e reimplementações apareceram quase na hora</div>
</div>


<!--
Tempo sugerido: ~1:00

- E o que apareceu lá dentro? Não apareceu perfeição divina.
- Não apareceu magia.
- Apareceu uma base grande, pressionada por entrega, cheia de decisão tática, chave de recurso, remendo e complexidade operacional.
- O famoso espaguete de sênior.
-->
---

<!-- _class: statement -->
<div class="eyebrow">Meu Ponto</div>

# IA não eliminou
# engenharia.

## Eliminou desculpa.

<!--
Tempo sugerido: ~0:35

- Então meu ponto central é esse: IA não eliminou a necessidade de engenharia.
- Ela eliminou desculpa.
- Ela escancarou a diferença entre quem sabe fazer sistema sobreviver em produção e quem só sabe produzir resposta plausível.
-->
---

<!-- _class: center tone-sand -->
# LLMs são loot boxes

<div class="columns-3">
  <div class="card"><strong>Probabilísticas</strong><div class="mini">nunca 100% confiáveis</div></div>
  <div class="card"><strong>Dependem de contexto</strong><div class="mini">qualidade depende do que você dá e do que você checa</div></div>
  <div class="card"><strong>Gastam loop</strong><div class="mini">o ecossistema inteiro te incentiva a gastar mais tokens</div></div>
</div>


<!--
Tempo sugerido: ~0:55

- Eu chamei LLMs de loot boxes porque elas são probabilísticas.
- Não são compiladores determinísticos.
- Não existe garantia de correção.
- Dá pra melhorar bastante as chances com contexto, ferramenta, ciclo de avaliação e prompt melhor? Dá.
-->
---

<!-- _class: center tone-sand -->
<div class="eyebrow">2026 Ainda</div>

# Modelo ainda
# bajula e erra

<div class="columns-3">
  <div class="card"><strong>Bajula você</strong><div class="mini">muitas vezes responde o que você quer ouvir</div></div>
  <div class="card"><strong>Erra confiante</strong><div class="mini">inventa detalhe e segue como se estivesse certo</div></div>
  <div class="card"><strong>Precisa de freio</strong><div class="mini">execução, teste e revisão continuam obrigatórios</div></div>
</div>


<!--
Tempo sugerido: ~0:45

- E eu quero deixar uma coisa bem explícita: o modelo de 2026 ainda baixa a cabeça pra você.
- Se você vier com premissa torta, ele muitas vezes prefere te agradar em vez de te contrariar.
- Ele também continua errando com confiança.
- Inventa detalhe, completa lacuna do jeito errado, segue em frente como se estivesse tudo certo.
-->
---

<!-- _class: center tone-moss -->
<div class="eyebrow">Virada</div>

# Fim de 2025
# foi diferente

<div class="columns">
  <div class="card"><strong>13 nov 2025</strong><br />GPT-5.1 saiu para desenvolvedores</div>
  <div class="card"><strong>24 nov 2025</strong><br />Claude Opus 4.5 saiu</div>
</div>

<div class="lead" style="max-width:none;margin-left:auto;margin-right:auto;">A virada não foi “virou gênio”. Foi modelo + ferramenta + execução no loop ficando bons o bastante pra trabalho diário.</div>


<!--
Tempo sugerido: ~0:50

- uma coisa realmente mudou.
- OpenAI lançou GPT-5.1 pra desenvolvedores em 13 de novembro de 2025.
- Anthropic lançou Claude Opus 4.5 em 24 de novembro de 2025.
- Esse período importa porque foi quando o conjunto modelo mais ferramentas mais execução no loop ficou bom o bastante pra deixar de ser só chatice e começar a virar alavanca diária.
-->
---

<!-- _class: statement -->
<div class="eyebrow">O Pulo Do Gato</div>

# Não foi QI.
# Foi ferramenta.

<div class="columns-3">
  <div class="card"><strong>Shell e editor</strong><div class="mini">o modelo parou de só sugerir e passou a operar</div></div>
  <div class="card"><strong>Teste e execução</strong><div class="mini">erro voltou como feedback em segundos</div></div>
  <div class="card"><strong>Busca e contexto</strong><div class="mini">documentação e código viraram parte do loop</div></div>
</div>


<!--
Tempo sugerido: ~0:40

- Eu quero martelar isso porque muita gente ainda fala como se 2026 fosse sobre um salto mágico de inteligência.
- Não foi.
- O pulo do gato foi ferramenta.
- Shell, editor, execução, teste, busca, documentação, leitura de código, tudo isso entrando no loop.
-->
---

<!-- _class: statement tone-moss -->
<div class="eyebrow">Ciclo do Agente</div>

# Planeja.
# Investiga.
# Lapida.
# Opera.
# Testa.
# Ajusta.

<!--
Tempo sugerido: ~0:35

- E reparem como é o ciclo útil de verdade.
- Eu até brinquei no slide pra formar um acróstico de “PILOTA”: planeja, investiga, lapida, opera, testa, ajusta.
- Não tem nada de místico nisso.
- É compressão de retorno de engenharia.
-->
---

<!-- _class: center tone-moss -->
# Prompt único
# é pra demo

<div class="columns">
  <div class="card"><strong>Produção é iteração</strong><br />bug, deploy, retorno, refatoração, ajuste de prompt</div>
  <div class="card"><strong>“Pronto” é mentira</strong><br />125 commits de pós-produção em 4 projetos</div>
</div>


<!--
Tempo sugerido: ~0:55

- A fantasia do prompt único é preguiçosa.
- Ela parte da ideia de que dá pra prever e especificar tudo antes.
- Software real não funciona assim.
- Produção revela coisa que você nem sabia que importava.
-->
---

<!-- _class: center -->
<div class="eyebrow">Akita Antigo Continua Certo</div>

# Fundamento primeiro

<div class="thumb-grid">
  <img src="https://img.youtube.com/vi/L0hTOY5n9G8/hqdefault.jpg" alt="O que os cursos não te ensinam sobre mercados" />
  <img src="https://img.youtube.com/vi/oUPaJxk6TZ0/hqdefault.jpg" alt="Aprendendo a aprender" />
  <img src="https://img.youtube.com/vi/V7oUDL7E1g4/hqdefault.jpg" alt="Programação não é fácil" />
  <img src="https://img.youtube.com/vi/am-FQ86mKV0/hqdefault.jpg" alt="Aprendizado na beira do caos" />
</div>

<!--
Tempo sugerido: ~0:50

- É por isso que o Akita antigo continua valendo.
- Não terceirize sua decisão.
- Aprenda a aprender.
- Entenda que programação não é fácil.
-->
---

<!-- _class: center -->
![bg cover opacity:.12](https://img.youtube.com/vi/D3L8IOncLkg/hqdefault.jpg)
# Não terceirize
# seu julgamento

## nem pra guru  
## nem pra bootcamp  
## nem pro modelo

<div class="lead" style="max-width:none;margin-left:auto;margin-right:auto;">A lógica continua a mesma: experimento pequeno, feedback rápido, correção contínua.</div>

<!--
Tempo sugerido: ~0:45

- O mais difícil de ensinar pra iniciante é isso: julgamento não é uma coisa que você baixa pronta.
- Não vem de influencer, não vem de bootcamp, não vem de modelo.
- O modelo mental continua o mesmo: experimento pequeno na beira do caos, erro cedo, retorno rápido, correção contínua.
-->
---

<!-- _class: center -->
# Fevereiro e março
# de 2026

## eu parei de falar  
## e fui maratonar

<!--
Tempo sugerido: ~0:25

- Então eu parei de falar disso em abstrato e fui maratonar.
- Não com prompt de brinquedo.
- Não com videozinho fake de SaaS em dez minutos.
- Projeto real.
-->
---

<!-- _class: center -->
<div class="eyebrow">Painel de Projetos</div>

# Do zero
# pra software real

<div class="thumb-grid">
  <img src="https://new-uploads-akitaonrails.s3.us-east-2.amazonaws.com/frankmd/2026/02/screenshot-2026-02-01_15-16-29.jpg" alt="FrankMD" />
  <img src="https://raw.githubusercontent.com/akitaonrails/FrankMega/master/docs/upload_screen.png" alt="FrankMega" />
  <img src="https://raw.githubusercontent.com/akitaonrails/FrankSherlock/master/docs/frank_sherlock.png" alt="Frank Sherlock" />
  <img src="https://raw.githubusercontent.com/akitaonrails/FrankYomik/master/docs/sample_translate.png" alt="Frank Yomik" />
  <img src="https://raw.githubusercontent.com/akitaonrails/frank_fbi/master/docs/suspect-email.png" alt="Frank FBI" />
  <img src="https://raw.githubusercontent.com/akitaonrails/FrankYomik/master/docs/sample_furigana.png" alt="Frank Yomik Furigana" />
  <img src="https://new-uploads-akitaonrails.s3.us-east-2.amazonaws.com/frankmd/2026/02/screenshot-2026-02-01_14-22-28.jpg" alt="FrankMD IA" />
  <img src="https://new-uploads-akitaonrails.s3.us-east-2.amazonaws.com/frankmd/2026/02/screenshot-2026-02-01_14-39-53.jpg" alt="FrankMD Hugo" />
</div>

<!--
Tempo sugerido: ~0:35

- Este slide é só a parede de projetos.
- FrankMD, FrankMega, Frank Sherlock, Frank Yomik, Frank FBI e outros.
- O objetivo não é explicar repositório por repositório.
- O objetivo é mostrar volume e variedade: desktop, Rails, Rust, ferramentas, mídia, deploy, software em uso real.
-->
---

<!-- _class: center -->
<div class="eyebrow">A Prova Prática</div>

# Mesmo dev.
# Mesmo agente.
# Processo diferente.

<div class="columns">
  <div class="card"><strong>FrankMD</strong><br />212 commits em 19 dias, refactor pesado, teste correndo atrás</div>
  <div class="card"><strong>M.Akita Chronicles</strong><br />274 commits em 8 dias, TDD, CI e refatoração contínua</div>
</div>

<div class="lead" style="max-width:none;margin-left:auto;margin-right:auto;">A variável não foi “IA melhor”. Foi disciplina de engenharia desde o primeiro commit.</div>


<!--
Tempo sugerido: ~0:55

- Aqui entra a comparação que eu acho mais forte de todas.
- FrankMD de um lado.
- M.Akita Chronicles do outro.
- Mesmo desenvolvedor.
-->
---

<!-- _class: center tone-sand -->
<div class="eyebrow">No Conjunto Completo Dos Projetos Citados</div>

# Números
# que pesam

<div class="stats">
  <div class="card"><strong>723.935</strong><span class="mini">linhas de código</span></div>
  <div class="card"><strong>199.250</strong><span class="mini">linhas de teste</span></div>
  <div class="card"><strong>1.116</strong><span class="mini">commits</span></div>
  <div class="card"><strong>~194 h</strong><span class="mini">horas ativas estimadas</span></div>
</div>

<div class="caption">Agregado dos projetos citados no começo da palestra, com o mesmo critério em produção e teste: só código próprio, excluindo documentação, fixtures, snapshots e árvores importadas de terceiros.</div>


<!--
Tempo sugerido: ~1:05

- E aqui é onde eu boto peso na afirmação de velocidade.
- Se eu agrego o conjunto de projetos citado no começo da palestra, dá 723.935 linhas de código, 199.250 linhas de teste, 1.116 commits e cerca de 194 horas ativas estimadas.
- E essa conta está fechada com o mesmo critério dos dois lados: só arquivo de código próprio, separando produção de teste pelo path, e excluindo documentação, fixtures, snapshots e árvore importada de terceiros.
- Então não tem README, arquivo auxiliar ou biblioteca de terceiro inflando número.
-->
---

<!-- _class: center tone-sand -->
# O que eu ganhei
# de verdade

<div class="stats">
  <div class="card"><strong>5x a 10x</strong><span class="mini">de velocidade</span></div>
  <div class="card"><strong>Mais tração</strong><span class="mini">menos bloqueio, menos procrastinação</span></div>
  <div class="card"><strong>Mais alcance</strong><span class="mini">stack inteira, ferramentas, deploy, documentação</span></div>
  <div class="card"><strong>Mais confiança</strong><span class="mini">testes, integração contínua, refatoração, produção</span></div>
</div>


<!--
Tempo sugerido: ~1:00

- Da minha experiência prática, o resumo honesto é 5x a 10x de velocidade.
- Não porque o modelo escreve código perfeito.
- Não escreve.
- O ganho vem porque ele atravessa aquele atrito chato que normalmente quebra foco: código repetitivo, busca, refatoração repetitiva, teste repetitivo, execução de comando, tentativa rápida.
-->
---

<!-- _class: center tone-sand -->
<div class="eyebrow">Normalizando o Ritmo</div>

# 45 dias de maratona
# não são 45 dias normais

<div class="stats">
  <div class="card"><strong>45 dias corridos</strong><span class="mini">quase 16h por dia, 7 dias por semana</span></div>
  <div class="card"><strong>~126 dias corridos</strong><span class="mini">algo perto de 4 meses e 1 semana</span></div>
  <div class="card"><strong>~630 a 1.260 dias corridos</strong><span class="mini">o mesmo sênior sem IA</span></div>
  <div class="card"><strong>~21 a 42 meses</strong><span class="mini">ou cerca de 1,8 a 3,5 anos</span></div>
</div>

<div class="caption">Estimativa linear em calendário real de trabalho: 8h por dia, só em dias úteis.</div>


<!--
Tempo sugerido: ~0:55

- Aqui eu preciso fazer a conta honesta, senão parece truque de palco.
- Isso foi entregue em 45 dias corridos, sim.
- Mas em ritmo de maratona: quase 16 horas por dia, 7 dias por semana.
- Se você converte isso para um sênior trabalhando num ritmo sustentável, no máximo 8 horas por dia e só em dias úteis, essa mesma entrega com IA vira algo como 126 dias corridos, perto de 4 meses e 1 semana.
-->
---

<!-- _class: center -->
![bg cover opacity:.10](https://new-uploads-akitaonrails.s3.us-east-2.amazonaws.com/frankmd/2026/02/agile-lifecycle-development-process-diagram-vector-31188796.jpg)
<div class="eyebrow">Nome Verdadeiro</div>

# Agile Vibe Coding

## é XP com pareamento
## programming de máquina

<!--
Tempo sugerido: ~0:45

- É por isso que eu uso o termo Agile Vibe Coding, mas também faço questão de desmistificar.
- A estrutura de verdade por baixo é velha.
- É Extreme Programming.
- O pareamento mudou porque agora meu par é uma máquina.
-->
---

<!-- _class: center tone-moss -->
# XP não é
# perfumaria

<div class="columns-3">
  <div class="card"><strong>TDD</strong><div class="mini">segura erro de modelo antes de virar lama</div></div>
  <div class="card"><strong>CI por commit</strong><div class="mini">pega drift e regressão cedo</div></div>
  <div class="card"><strong>Refatoração contínua</strong><div class="mini">evita cirurgia cara depois</div></div>
</div>


<!--
Tempo sugerido: ~0:45

- E aqui vale separar uma coisa importante.
- TDD não é perfumaria.
- CI não é perfumaria.
- Refatoração contínua não é perfumaria.
-->
---

<!-- _class: center tone-moss -->
# O pareamento mudou

<div class="columns">
  <div class="card"><strong>Eu trago</strong><br />direção, julgamento, contexto, gosto</div>
  <div class="card"><strong>O agente traz</strong><br />velocidade de execução, busca, fôlego operacional</div>
</div>

<div class="lead" style="max-width:none;margin-left:auto;margin-right:auto;">IA é espelho: sênior bom ganha alavancagem, programador ruim ganha velocidade pra errar.</div>


<!--
Tempo sugerido: ~1:00

- O melhor corte de responsabilidade que eu encontrei foi esse: eu trago direção, julgamento, contexto e gosto.
- O agente traz velocidade de execução, busca e fôlego operacional.
- Se eu reduzo o agente a digitador burro, piora.
- Se eu entrego produto e arquitetura pra ele sozinho, piora também.
-->
---

<!-- _class: center tone-moss -->
<div class="eyebrow">Estado dos Modelos, 1 de abril de 2026</div>

# Modelos fechados
# ainda lideram

<div class="columns-3">
  <div class="card"><strong>Anthropic</strong><div class="mini">continua no topo pra agentes de código</div></div>
  <div class="card"><strong>OpenAI</strong><div class="mini">GPT-5.1 virou modelo forte pra código e agentes</div></div>
  <div class="card"><strong>Seguidores</strong><div class="mini">GLM, MiniMax, Kimi; open source ainda corre atrás</div></div>
</div>


<!--
Tempo sugerido: ~0:55

- No ecossistema de modelos em 1 de abril de 2026, minha leitura prática é simples.
- Anthropic e OpenAI continuam sendo as plataformas de ponta que mais importam pra código sério.
- Existem seguidores relevantes, como GLM, MiniMax e Kimi.
- Open source é útil, mas ainda não empatou no fluxo completo com agentes.
-->
---

<!-- _class: center -->
# Open source é útil

## mas ainda não é ponta

<div style="display:flex;gap:32px;align-items:center;text-align:left;">
  <div style="flex:0 0 45%;">
    <div class="card" style="margin-bottom:12px;"><strong>clone clean-room em menos de 24h</strong><br />o leak já estava gerando reimplementação no dia seguinte</div>
    <div class="card" style="margin-bottom:12px;"><strong>free-code sem guarda-corpo</strong><br />telemetria e travas arrancadas quase na hora</div>
    <div class="card"><strong>OpenClaw mostra o terreno pronto</strong><br />o lado open source já estava maduro pra correr em cima</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/openclaw-repo-page-cropped.png" alt="Projeto OpenClaw no GitHub" style="height:430px;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.28);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:45

- Isso não significa que código aberto seja inútil.
- Significa só que expectativa precisa ser calibrada.
- Dá pra fazer coisa real? Dá.
- Mas se você quer o melhor comportamento atual de agente de código, os modelos fechados de ponta ainda estão na frente.
-->
---

<!-- _class: center -->
# E o preço
# ficou ridículo

<div style="display:flex;gap:32px;align-items:center;text-align:left;">
  <div style="flex:0 0 45%;">
    <div class="lead" style="max-width:none;margin:0 0 14px 0;">CRUD, landing page, painel interno, bot, ETL, cola entre APIs: software trivial virou commodity.</div>
    <div class="card" style="margin-bottom:12px;"><strong>Claude Pro</strong><br />US$ 20 por mês</div>
    <div class="card" style="margin-bottom:12px;"><strong>Max 5x</strong><br />US$ 100 por mês</div>
    <div class="card"><strong>Max 20x</strong><br />US$ 200 por mês</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/anthropic-claude-plan-help.png" alt="Planos Claude na Anthropic" style="height:430px;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.20);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:45

- E aí entra a economia da coisa.
- Software trivial ficou barato demais.
- CRUD, landing page, painel interno, bot, ETL, cola entre API, esse tipo de coisa virou commodity.
- E quando eu olho o preço oficial da Anthropic, isso fica ainda mais óbvio.
-->
---

<!-- _class: center tone-moss -->
<div class="eyebrow">Commoditização</div>

# O que ficou barato
# e o que não ficou

<div class="columns">
  <div class="card"><strong>Barato</strong><br />CRUD, landing page, painel interno, bot, ETL, cola entre APIs</div>
  <div class="card"><strong>Caro</strong><br />julgamento, arquitetura, gosto, operação, manutenção, dono do problema</div>
</div>


<!--
Tempo sugerido: ~0:40

- Esse é o corte que importa.
- O que ficou barato foi software trivial: CRUD, landing page, painel interno, bot, ETL, cola entre APIs.
- O que continua caro é o que sempre foi caro: julgamento, arquitetura, gosto, operação, manutenção e alguém disposto a ser dono do problema quando a coisa quebra de verdade.
-->
---

<!-- _class: center -->
![bg cover opacity:.10](https://www.cio.com/wp-content/uploads/2026/04/4153113-0-45250700-1775046029-shutterstock_2400351163.jpg)
<div class="eyebrow">A Correção</div>

# Programador ruim
# vai sair

## e isso melhora a indústria

<!--
Tempo sugerido: ~0:35

- Aqui é a parte em que eu paro de fingir diplomacia.
- Eu estou genuinamente feliz que a bolha do programador ruim esteja morrendo.
- A indústria passou anos trocando engenharia por braço barato e acumulando dívida técnica como se isso fosse de graça.
- A IA está forçando uma correção.
-->
---

<!-- _class: center tone-ruby -->
# Júnior não morreu

<div class="columns-3">
  <div class="card"><strong>Vai herdar a sujeira</strong><div class="mini">startup cheia de lixo de IA vai precisar de limpeza</div></div>
  <div class="card"><strong>Vai aprender no caos</strong><div class="mini">igual gerações anteriores aprenderam</div></div>
  <div class="card"><strong>Ainda precisa de sênior</strong><div class="mini">agente nenhum ensina julgamento</div></div>
</div>


<!--
Tempo sugerido: ~0:55

- Júnior está preocupado, mas eu não acho que o caminho acabou.
- Acho que ele mudou de forma.
- O mundo está enchendo de sistema feito nas coxas, cheio de lixo de IA.
- Alguém vai ter que limpar isso.
-->
---

<!-- _class: center tone-ruby -->
# Sênior tem
# nova obrigação

## ensinar engenharia com IA  
## antes do código apodrecer

<div class="lead" style="max-width:none;margin-left:auto;margin-right:auto;">E a correção continua agora. Em 1 de abril de 2026, a Oracle entrou em mais uma rodada grande de layoffs.</div>

<!--
Tempo sugerido: ~0:55

- Mas isso só funciona se sênior fizer o trabalho dele.
- Sênior não é imortal.
- Vai mudar de empresa, vai cansar, vai se aposentar.
- Se não formar substituto, a organização apodrece.
-->
---

<!-- _class: statement -->
<div class="eyebrow">Conclusão</div>

# IA não transforma
# coder ruim
# em engenheiro.

<!--
Tempo sugerido: ~0:35

- Então o fechamento é simples.
- IA não transforma programador ruim em engenheiro.
- Ela ajuda programador ruim a fazer estrago maior mais rápido.
- E ajuda engenheiro de verdade a atravessar esse caos com mais velocidade, sem deixar o software morrer.
-->
---

<!-- _class: end -->
<div class="eyebrow">Conclusão</div>

# Vai sobreviver
# quem souber
# fazer engenharia.

## Fundamento. Disciplina. Iteração. Gosto.

<!--
Tempo sugerido: ~0:40

- Essa é minha conclusão pro Tropical Ruby 2026.
- Não vai sobreviver quem decorou truquezinho de prompt.
- Vai sobreviver quem tem fundamento, disciplina, iteração e gosto.
- Se você tem isso, IA vira multiplicador.
-->
---

<!-- _class: center -->
<div class="eyebrow">Merchan Sem Vergonha</div>

<div style="display:flex;gap:36px;align-items:center;text-align:left;">
  <div style="flex:0 0 40%;">
    <h1 style="margin:0 0 18px 0;line-height:0.95;">Assine<br />The M.Akita Chronicles</h1>
    <div style="font-size:1.05em;font-weight:700;margin:0 0 18px 0;">themakitachronicles.com</div>
    <div class="lead" style="max-width:none;margin:0;">Se você curtiu essa palestra, vai lá assinar. Toda semana tem bastidor real, código real e projeto real em produção.</div>
  </div>
  <div style="flex:1 1 auto;text-align:right;">
    <img src="../assets/makita-chronicles-subscribe-cropped.png" alt="The M.Akita Chronicles" style="height:560px;border-radius:18px;box-shadow:0 18px 40px rgba(0,0,0,0.28);" />
  </div>
</div>

<!--
Tempo sugerido: ~0:20

- E já que é pra acabar sem falsa modéstia: se você curtiu essa palestra, assina o The M.Akita Chronicles.
- Está tudo aí na tela.
- É onde eu continuo publicando bastidor real, projeto real, código real e o que deu certo ou errado em produção.
- Quer acompanhar essa linha de raciocínio semana a semana? Vai em themakitachronicles.com e assina.
-->
