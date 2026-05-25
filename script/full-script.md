# Web Summit Rio 2026 - Roteiro Completo

Este roteiro acompanha a versão em PT-BR do deck em `slides/tropical-ruby-2026.md`.

## Slide 1 - Agile Vibe Coding
Restam: ~19:10 (50s)

Aqui é a versão curta, então vou direto: agentes de IA mudaram o custo de construir software, mas não aboliram engenharia. Perguntar "IA substitui programador?" é pouco. A pergunta que importa é: qual processo sobrevive quando errar ficou barato e entregar ficou rápido? O que eu vou defender é simples: agente bom aumenta muito a produtividade de quem sabe dirigir. Mas ele também acelera a bagunça de quem não sabe.

## Slide 2 - Fabio Akita
Restam: ~18:25 (45s)

Pra quem não me conhece: fui cofundador da Codeminer 42, fundei a RubyConf Brasil, mantenho o Akitando no YouTube com mais de 500 mil seguidores, e o akitaonrails.com acabou de fazer 20 anos. Estou dizendo isso por um motivo simples: eu já vi hype demais. Eu não comecei a falar da bolha do programador fake quando IA virou moda. Eu já vinha batendo nessa tecla antes.

## Slide 3 - A bolha era velha. O ChatGPT foi o prego no caixão.
Restam: ~17:40 (45s)

Antes do GPT, a indústria já vendia uma mentira confortável: qualquer um faz um cursinho, aprende uma ferramenta e vira engenheiro de software. Eu já criticava isso no canal. A correção começou em 2022, antes da IA programar direito. Aí o ChatGPT apareceu logo depois e virou o prego no caixão. Ele não criou a bolha. Ele expôs a bolha.

## Slide 4 - A corrida era parâmetro + compute
Restam: ~16:55 (45s)

De 2022 até 2024, a leitura dominante era quase sempre a mesma: modelo maior, mais dado, mais GPU. GPT-3 com 175 bilhões de parâmetros virou o marco público. Depois vieram modelos com centenas de bilhões, MoE, clusters cada vez maiores. Scaling law funciona. Não estou dizendo que morreu. O ponto é outro: cada salto começou a cobrar mais caro por ganho incremental menor.

## Slide 5 - De treino gigante para inferência útil
Restam: ~16:10 (45s)

E a conta física começou a apertar. Treino frontier já consome escala de data center sério. Construir data center é lento: energia, transformador, terreno, fibra, conexão à rede. Ao mesmo tempo, os modelos ficaram úteis o bastante para muita gente usar todo dia. A pressão sai só do treino e vai para inferência: reasoning, tool calling, cache, prompt caching, dezenas de chamadas por agente. O ganho passa a vir de usar melhor o modelo que já existe.

## Slide 6 - 2025 foi o ano dos AGENTES
Restam: ~15:15 (55s)

Por isso 2025 foi a virada. Não porque o chatbot ficou um pouco mais esperto. Foi a pilha fechando: APIs com ferramentas, CLIs de agente, thinking entre tool calls, cache, contexto maior, execução no terminal. O produto deixou de ser "me responde" e virou "trabalha comigo no projeto por uma hora". Esse detalhe muda tudo para programação.

## Slide 7 - Fevereiro a maio de 2026
Restam: ~14:55 (20s)

Então eu parei de falar disso em abstrato e fui testar com pele em jogo. De fevereiro a maio. Nada de prompt de brinquedo, nada de vídeo fake de SaaS em dez minutos. Projeto real, bug real, deploy real, pós-produção real.

## Slide 8 - Do zero pra software real
Restam: ~14:30 (25s)

Este slide é só a parede de projetos. Não vou explicar um por um aqui. A ideia é mostrar variedade: desktop, Rails, Rust, Flutter, mídia, deploy, ferramenta de uso real. Se a tese presta, ela precisa sobreviver a mais de um tipo de problema.

## Slide 9 - 26 projetos experimentais
Restam: ~14:05 (25s)

Tudo está aberto no GitHub. São 26 projetos em várias linguagens e domínios. Disclaimer honesto: não são 26 projetos perfeitos. Alguns viraram software de uso diário, outros são protótipos. O ponto não era fingir excelência. Era rodar o ciclo de agente em escala e ver onde ele quebra.

## Slide 10 - Mesmo dev. Mesmo agente. Processo diferente.
Restam: ~13:05 (60s)

Esta comparação é o coração da palestra curta. Mesmo dev, mesmo agente, processo diferente. No FrankMD, eu paguei várias decisões tardias: refactor pesado, teste correndo atrás, organização mais traumática. No M.Akita Chronicles, entrei desde o começo com TDD, CI e refatoração contínua. Resultado: 212 commits em 19 dias de um lado, 274 commits em 8 dias do outro. A variável não foi uma IA melhor. Foi disciplina de engenharia.

## Slide 11 - Números que pesam
Restam: ~12:00 (65s)

Recontando tudo com `tokei`, no recorte da maratona, deu 432.134 linhas úteis, 62.643 linhas de teste, 2.241 commits e cerca de 473 horas ativas estimadas. O critério foi conservador: arquivo rastreado em git, sem linha em branco, sem asset, sem build, sem vendor, sem árvore de terceiro. As horas também são defensáveis: sessões agrupadas por commit, corte de pausa, teto diário. Não é tudo que eu trabalhei. É só o que dá para defender olhando commit.

## Slide 12 - Alcançamos "Developer 10x"?
Restam: ~11:10 (50s)

Minha resposta honesta: em muita coisa, sim, 5x a 10x de velocidade. Não porque o modelo escreve código perfeito. Ele não escreve. O ganho vem porque ele atravessa atrito: busca, boilerplate, refactor repetitivo, teste repetitivo, comando, tentativa rápida. Mas a confiança só veio porque o resto continuou existindo: teste, CI, revisão e produção.

## Slide 13 - Prompt único é pra demo
Restam: ~10:25 (45s)

A fantasia do prompt único vende bem no palco, mas morre em produção. Software real revela coisa que você não previu. A API vem torta, a infra falha do jeito errado, o usuário faz o que ninguém imaginou, o requisito muda. Prompt único serve para demo. Produto precisa de iteração.

## Slide 14 - Agile Vibe Coding
Restam: ~09:25 (60s)

Eu chamo de Agile Vibe Coding porque pega. Mas por baixo não tem misticismo: é Extreme Programming com pareamento de máquina. TDD, CI por commit e refatoração contínua não ficaram velhos. Ficaram mais importantes. O modelo erra. TDD segura parte desse erro antes de virar lama. CI pega drift e regressão cedo. Refatoração contínua impede o agente de afundar em dívida técnica em poucos dias.

## Slide 15 - O pareamento mudou
Restam: ~08:35 (50s)

A melhor divisão de responsabilidade que encontrei foi esta: eu trago direção, julgamento, contexto e gosto. O agente traz velocidade de execução, busca e fôlego operacional. Se eu reduzo o agente a digitador burro, desperdiço a ferramenta. Se eu entrego produto e arquitetura para ele sozinho, piora. A alavancagem está no par, não na terceirização da cabeça.

## Slide 16 - github.com/akitaonrails/llm-coding-benchmark
Restam: ~08:20 (15s)

Para não ficar só na minha opinião, também abri o benchmark. Prompt, runner, configuração e resultados estão no GitHub. Quatro rodadas entre abril e maio. Quem quiser reproduzir, pode clonar.

## Slide 17 - Benchmark Ranking (Maio/2026)
Restam: ~07:30 (50s)

O ranking consolidado tem 24 modelos, mesma tarefa e score de 0 a 100. Opus 4.7 e GPT 5.4 empatam no topo. GPT 5.5 chega praticamente junto e mais barato. DeepSeek V4 Pro e Kimi K2.6 mostram que o gap fechou, mas só quando o harness aguenta. A leitura prática é: escolher modelo importa, claro. Mas o fluxo importa mais.

## Slide 18 - Não é mais só parâmetro
Restam: ~06:35 (55s)

O que separa modelo que aguenta agente real não é só tamanho. Parâmetro virou commodity. Tier A depende de infraestrutura de inferência: prompt caching, tool calling e reasoning. Sem cache, o custo do loop explode. Sem tool calling decente, o modelo chama coisa errada ou inventa método. Sem reasoning, ele chuta antes de planejar. Poucos passam porque poucos fecham as três coisas juntas.

## Slide 19 - IA nunca vai ser perfeita. Mas errar ficou barato.
Restam: ~05:45 (50s)

Muita gente ainda espera o modelo perfeito. Eu acho que essa leitura está errada. LLM vai continuar errando. A virada foi outra: o custo do erro caiu. O agente roda, quebra, recebe stack trace, corrige e tenta de novo em segundos. Isso muda a economia do software trivial. Julgamento, arquitetura e operação continuam caros.

## Slide 20 - As únicas ferramentas pra usar agora
Restam: ~05:15 (30s)

Em maio de 2026, estes são os quatro CLIs que eu realmente usaria para agente de terminal sério: Claude Code, Codex, opencode e Oh-My-Pi. Claude Code e Codex cobrem os modelos fechados de fronteira. opencode e Oh-My-Pi são bons quando você quer ser agnóstico, testar modelo chinês ou rodar via OpenRouter.

## Slide 21 - Trocar de harness sem perder controle
Restam: ~04:50 (25s)

Como eu alterno entre harnesses, acabei criando um kit pequeno para não virar bagunça. Não é orquestrador mágico. É operação básica: ai-jail para dar autonomia com cerca, ai-memory para o contexto sobreviver entre sessões e harnesses, e ai-usagebar para eu saber quando estou perto do limite e preciso trocar de cavalo.

## Slide 22 - ai-jail: autonomia com cerca
Restam: ~04:10 (40s)

O ai-jail nasceu porque eu gosto de rodar Claude e Codex em modo sem freio, mas não quero dar a chave da casa. Eu tiro a fricção de confirmação dentro do harness e coloco a trava no sistema operacional. O projeto fica read-write. O resto do host fica fora, read-only, mascarado ou mapeado explicitamente. Não é VM, não é blindagem militar, mas é uma camada prática.

## Slide 23 - ai-memory: contexto que sobrevive ao harness
Restam: ~03:30 (40s)

O ai-memory resolve outro problema: harness esquece. Claude compacta, Codex compacta, sessão acaba, e o próximo agente não sabe por que você tomou uma decisão duas horas atrás. Ele captura prompts, tool calls e boundaries de sessão, consolida em markdown, indexa com FTS5 e expõe handoff e busca via MCP. Não substitui documentação canônica em `docs/`. Cobre o meio do caminho.

## Slide 24 - IA reflete quem você é
Restam: ~02:50 (40s)

E aqui está a regra que não mudou: IA não cria competência do nada. Ela reflete quem você é. Se você é bom engenheiro, ela te faz produzir mais, mais rápido. Se você é ruim, ela te ajuda a produzir lixo numa velocidade que você nunca conseguiria sozinho.

## Slide 25 - Vai sobreviver quem souber fazer engenharia
Restam: ~01:55 (55s)

Então eu fecho assim: IA não transforma coder ruim em engenheiro. Ela ajuda coder ruim a fazer estrago maior, mais rápido. E ajuda engenheiro bom a atravessar o caos sem deixar o software morrer. Não vai sobreviver quem decorou truque de prompt. Vai sobreviver quem tem fundamento, disciplina, iteração e gosto.

## Slide 26 - O canal também virou inglês
Restam: ~01:45 (10s)

Dois merchans rápidos antes de sair. O Akitando também virou inglês: mais de 150 vídeos traduzidos e legendados com agente, além do blog bilingue. Se quiser mandar meu conteúdo pra alguém de fora do Brasil, começa por youtube.com/@Akitando.

## Slide 27 - Assine The M.Akita Chronicles
Restam: ~01:35 (10s)

E o acompanhamento semanal fica no The M.Akita Chronicles: notícias de tecnologia, opinião, código aberto e bastidor de projeto real. Sem verniz. themakitachronicles.com.

## Slide 28 - Sim, este deck inteiro foi feito com IA
Restam: ~01:05 (30s)

E sim, este deck também foi feito com IA. Pesquisa, estrutura, roteiro, presenter notes, cortes, build e acabamento vieram do mesmo fluxo: agente no terminal, Marp, scripts e iteração curta. Então não é discurso abstrato. Eu usei a pilha para fazer a própria palestra.

## Slide 29 - Obrigado
Restam: ~01:00 (5s)

Obrigado. Os links estão no rodapé.
