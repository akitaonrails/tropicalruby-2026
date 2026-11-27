# Gambiconf 2026 - Roteiro Completo

Este roteiro acompanha a versão em PT-BR do deck em `slides/tropical-ruby-2026.md`.

## Slide 1 - Agile Vibe Coding
Restam: ~60:00 (75s)

Vou abrir direto, porque a gente tem uma hora pra desmontar isso com calma: agentes de IA mudaram o custo de construir software, mas não aboliram engenharia. Perguntar “IA substitui programador?” é pouco. A pergunta que importa é: qual processo sobrevive quando errar ficou barato e entregar ficou rápido? A tese é simples: agente bom aumenta muito a produtividade de quem sabe dirigir. Mas também acelera a bagunça de quem não sabe. Esse é o preço de vibe coding.

## Slide 2 - Fabio Akita
Restam: ~58:45 (60s)

Pra quem só me conhece por um pedaço da internet: fui cofundador da Codeminer 42 e hoje estou no conselho. Fundei e organizei a RubyConf Brasil até 2016. Passei anos no YouTube com o Akitando, mais de quinhentos e setenta mil inscritos, e sigo ativo no X como @akitaonrails, com quase cem mil seguidores lá também. E o akitaonrails.com acabou de completar 20 anos no dia 5 de abril de 2026, com mais de 830 artigos publicados, agora em português e inglês. Também fui parar fora da bolha tech, em programas como Flow e Inteligência Ltda. Estou falando isso por um motivo simples: eu já vi hype demais, mercado demais e promessa furada demais pra comprar fantasia fácil.

## Slide 3 - Heróis ou Vilões
Restam: ~57:45 (45s)

Antes de entrar na tecnologia, uma tentação que eu vejo todo dia: transformar IA em novela de CEO. Sam Altman, da OpenAI: hype, escala e o Elon processando. Dario Amodei, da Anthropic: Fable 5, Mythos 5 e até shutdown de governo entrando na história. E o Jensen Huang, da Nvidia, que tá em todas: comprou briga com gamer por causa do DLSS 5, briga com Washington por causa de chip pra China, e agora ainda tem escândalo pessoal na capa de jornal. Herói ou vilão, depende do feed que você segue. Só que o motor real é mais chato: margem, compute, assinatura subsidiada, API cara, IPO e distribuição. Esses caras não são personagem de Marvel. São CEOs tentando comprar tempo, GPU e narrativa. O importante pra nós não é torcer por um deles. É entender o incentivo. E pra entender incentivo, tem que começar pelo básico: o que essa tecnologia é de verdade.

## Slide 4 - Papagaios Estocásticos
Restam: ~57:00 (100s)

O jeito mais honesto de descrever o que um LLM faz por baixo é papagaio estocástico. Termo cunhado em 2021 por Emily Bender e a turma da Timnit Gebru. O modelo repete padrões de token aprendidos no treino, com fluência impressionante, mas sem entender o que diz. É bonito de ler e fraco de compromisso com a verdade. Por isso eu chamo LLM de loot box: é probabilístico, não é compilador determinístico. Dá pra melhorar bastante com contexto, ferramenta, ciclo de avaliação e prompt melhor? Dá. Mas o modelo de 2026 ainda baixa a cabeça pra você. Se você vem com premissa torta, ele muitas vezes prefere agradar em vez de contrariar. E continua errando com confiança: inventa detalhe, completa lacuna do jeito errado e segue em frente como se estivesse tudo certo. Por isso agente sem freio é desastre. O que segura ainda é execução real, teste real e revisão real.

## Slide 5 - Qualidade convergiu
Restam: ~55:20 (45s)

Eu mantive um benchmark próprio o ano inteiro, o v4: sete sprints construindo um app Rails enquanto eu planto catorze sabotagens silenciosas no código. E a conclusão de outubro foi clara: qualidade convergiu. Oito modelos fecharam com nota 100. Quando eu cruzei o meu resultado com SWE-bench Pro e Terminal-Bench, os seis primeiros ficaram espremidos em três pontos e meio — o primeiro e o segundo separados por 0,036 ponto. E eu já medi o mesmo modelo variando nove pontos entre uma rodada e outra. Dois ou três pontos numa tabela é ruído. Tier A é faixa de competência, não pódio olímpico. Pare de acompanhar ranking de LLM como campeonato de futebol.

## Slide 6 - Tier list não é benchmark
Restam: ~54:35 (20s)

Enquanto eu rodo teste, a internet faz tier list. Essa circulou no X. Opinião em formato de ranking é barato de fazer. Medir dá trabalho, e é por isso que eu meço.

## Slide 7 - 16 de 16 passaram. O preço variou 95×.
Restam: ~54:15 (35s)

Então no benchmark v5, agora em novembro, eu mudei a pergunta: todos já entregam, quanto custa entregar? Mesma tarefa pra dezesseis modelos comerciais Tier A: um app Rails completo de chat, testado, lintado e rodando em Docker. Os dezesseis passaram de primeira, sem um único empurrão. O único que ficou de fora foi o Muse Wonder da Meta, e não foi por qualidade — foi porque estourou a cota depois de doze chamadas. A diferença de verdade está no bolso e no relógio: noventa e cinco vezes no preço, de quinze centavos no GPT-6 Luna até mais de catorze dólares no Grok 4.7.

## Slide 8 - Preço de tabela engana
Restam: ~53:40 (35s)

E aqui tem uma pegadinha que quase ninguém olha: preço por milhão de tokens na tabela engana feio. Em programação com agente, de 94% a 99% do input é leitura de cache, o que corta de 69% a 94% da conta. Olha o GPT-6.2 Astra e o Claude Fable 5.2: preço de tabela idêntico, oito por quarenta dólares, mas o Astra custou menos da metade porque falou quatro vezes menos e terminou em metade do tempo. E cai por terra o mito do modelo chinês sempre mais barato: o GLM-5.3 na API oficial saiu mais caro que o Opus 5.5, e o DeepSeek V4 Pro queimou quase trinta e sete milhões de tokens.

## Slide 9 - Zero FOMO: o que eu uso hoje
Restam: ~53:05 (40s)

Então na prática, zero FOMO. Usar Fable 5.2 pra trocar cor de botão é pagar tarifa de foguete pra fazer entrega de bicicleta. No meu fluxo real hoje, eu tenho usado cada vez mais o Gemini 4 Neon como padrão: é enxuto em tokens, entregou catorze arquivos de teste no benchmark, custa três dólares e dez na API e no plano de vinte dólares se paga em seis rodadas. Logo atrás vêm Claude Opus 5.5 e GPT-6.2 Sol, que sobram com folga sem derreter cota igual Fable ou Astra. A regra é simples: escolha qualquer Tier A que caiba no seu bolso e na sua cota, mantenha um plano B e volte a programar.

## Slide 10 - De repente, Singapura virou 22% da Nvidia
Restam: ~52:25 (40s)

Antes de falar de modelos open source e modelos chineses, eu preciso derrubar um mito: a história de que a China fez modelo de fronteira sem GPU americana e só na genialidade. Olha os relatórios oficiais da própria Nvidia na SEC. Singapura saiu de 2,3 bilhões de dólares, 8% da receita em 2023, pra 6,8 bilhões em 2024, pra 23,7 bilhões — 18% — em 2025. E no segundo trimestre fiscal de 2026 bateu 10,2 bilhões num único trimestre: 22% da receita global da Nvidia num país de seis milhões de habitantes. A Nvidia sempre disse que era só endereço de faturamento, com menos de 2% de entrega física. E logo depois de bater 22%, mudou o critério no 10-Q — e Singapura sumiu da tabela.

## Slide 11 - Contrabando a céu aberto
Restam: ~51:45 (35s)

Enquanto Jensen Huang dizia pra Bloomberg que não havia nenhuma evidência de desvio porque um rack pesa quase duas toneladas, em agosto de 2025 o canal independente Gamers Nexus passou três semanas em Hong Kong, Shenzhen e Taipei. Eles entrevistaram na frente das câmeras contrabandistas, brokers, oficinas de reparo e compradores finais — mostrando placas restritas sendo escoadas pelo Sudeste Asiático e oficinas chinesas desmontando e remontando hardware de ponta pra contornar o bloqueio.

## Slide 12 - Singapura, Alice Huang e a brecha remota
Restam: ~51:10 (40s)

E além do contrabando físico, existia a brecha da nuvem remota. Como não podiam importar GPU direto pra China, gigantes como Tencent, Alibaba e ByteDance alugavam clusters Nvidia remotamente em data centers na Malásia, na Indonésia e em Singapura. Em novembro de 2026 explodiu o escândalo envolvendo a Megaspeed de Singapura e a Speedmatrix da Malásia — ligadas a Alice Huang, com estimativa de 7,5 a 12 bilhões de dólares em hardware avançado desviado. Só aí o governo americano publicou a regra do BIS fechando o acesso remoto e colocando Singapura, Malásia, Indonésia, Tailândia e até o Brasil na lista de alto risco.

## Slide 13 - E não foi só silício: destilação industrial
Restam: ~50:30 (35s)

E não foi só silício americano. Tanto a Anthropic quanto a OpenAI publicaram relatórios expondo campanhas de destilação em escala industrial: dezenas de milhares de contas falsas e centenas de milhões de trocas via proxy ligadas a laboratórios chineses como DeepSeek, Moonshot, MiniMax, Alibaba e Zhipu pra extrair raciocínio e código do Claude e do GPT. A engenharia chinesa é real e competente, ninguém tira o mérito. Mas a narrativa de "zero GPU americana e zero modelo americano, só genialidade" é mito.

## Slide 14 - Open source chegou no Tier A — em qual máquina?
Restam: ~49:55 (40s)

Dito isso, os modelos de pesos abertos funcionam de verdade? Eu gastei mais de seis mil dólares rodando quase setenta rodadas do meu benchmark v4 — da minha RTX 5090 e do Strix Halo até pods de quatro B300 na RunPod. E a boa notícia é que os melhores modelos abertos, como DeepSeek V4.1 Flash, GLM 5.3 Flash e Qwen3.8 Flash-Next, chegaram em 92,5, Tier A, colados no Sonnet 5 e no GPT-6 Sol. O problema é a máquina: 510 gigas em quatro B300 pode ser open source no GitHub, mas não cabe em casa. Eu até subi o DeepSeek de 2 bits na 5090 — deu 17 tokens por segundo. Tecnicamente roda, mas pra agente é inútil.

## Slide 15 - RunPod 4× B300 vs. pagar Anthropic / OpenAI
Restam: ~49:15 (40s)

Então vale a pena alugar servidor grande pra rodar modelo aberto? Eu medi concorrência real com critério de conforto de verdade: primeiro token em até dois segundos e pelo menos 50 tokens por segundo pra 95% das requisições. Um pod de 4x B300 na RunPod, a 36 dólares por hora desligando à noite, segura 32 desenvolvedores confortáveis — dá 198 dólares por pessoa. Ou seja, só empata com uma assinatura forte de 200 dólares de Claude ou Codex se você tiver perto de trinta devs usando o dia inteiro. A H200 parece mais barata por hora, mas só aguenta 8 devs e sai 316 por pessoa. Deixar 24/7 ou rodar em AWS e Azure dispara pra 355 a 933 dólares por dev. Time pequeno? Pague API ou assinatura. Infra própria só fecha conta com time grande ou exigência de compliance.

## Slide 16 - Em casa (até 5090), só 2 modelos jogam de verdade
Restam: ~48:35 (40s)

E em hardware doméstico de verdade, até uma RTX 5090? Hoje só dois modelos entregam qualidade e velocidade de agente de verdade. No AMD Strix Halo, com 64 gigas de memória unificada mas banda mais modesta, quem vence é o Qwen3.8 Flash-Next em Q2_0, fazendo 55 a 65 tokens por segundo. Já na RTX 5090 com o engine Basalt, que explora o FP4 nativo da Blackwell, o Qwen bate 377 a 400 tokens por segundo — só que esmagado em 2 bits e jogando de 30 a 42 gigas de especialistas na RAM. E aí acabou de chegar o novo campeão.

## Slide 17 - Thinking Machines Lab & Mira Murati
Restam: ~48:15 (30s)

E de onde veio esse Inkling? Eu mesmo nunca tinha ouvido falar dele até ver um post do DHH comparando o modelo no teste do Omarchy. Ele é obra da Thinking Machines Lab, a startup fundada em fevereiro de 2025 por Mira Murati, ex-CTO da OpenAI, junto com um time pesado egresso da própria OpenAI, incluindo John Schulman como Chief Scientist. Em 2025 eles construíram a infraestrutura e a plataforma Tinker pra fine-tuning de modelos abertos. Em julho de 2026 soltaram o Inkling original sob licença Apache 2.0, e agora em novembro veio a geração 2 — incluindo o Inkling 2 Mini, feito sob medida pra rodar localmente num notebook de 32 gigas ou numa única GPU doméstica.

## Slide 18 - O novo campeão caseiro: Inkling 2 Mini
Restam: ~47:45 (40s)

O Inkling 2 Mini, da Thinking Machines Lab da Mira Murati, licença Apache 2.0. O truque deles é genial: um Looped MoE com 24 camadas físicas onde as 12 do meio rodam três vezes por token, entregando profundidade de 48 camadas em vinte gigas. Resultado na minha 5090 com Basalt: cabe 100% na VRAM com quase sete gigas sobrando pro desktop, zero offload na RAM, precisão nativa NVFP4, janela de um milhão de tokens, 250 a 346 tokens por segundo e 100, 100, 100 nas três rodadas do meu teste difícil. O trade-off honesto é que ele pensa mais alto que o Qwen e sofre no Strix Halo por banda de memória. Mas pra quem tem uma 5090, ele é o novo rei local.


## Slide 8 - Não era exponencial
Restam: ~53:35 (55s)

Aqui é só o desenho mental. A corrida de treino parecia exponencial porque a gente estava olhando o miolo da curva S. Mas nada é exponencial pra sempre. Desde 2024, o retorno marginal ficou muito pior. Pra ganhar mais uma ordem de grandeza, a conta de capital, energia e compute explode. Então o foco natural muda: otimização, produto e agentes.

## Slide 9 - 2025 foi o ano dos Agentes
Restam: ~52:40 (65s)

Pra mim, 2025 foi o ano em que a pilha foi fechando. Em março, a OpenAI transformou tool support em plataforma de verdade. Em maio, a Anthropic já estava empurrando thinking com tool use e levando Claude Code pra um estado mais sério. Em agosto, GPT-5 começou a aguentar loop longo com menos tropeço. Em novembro, GPT-5.1 e Opus 4.5 deixaram isso mais redondo pra uso diário. Não foi um dia mágico. Foi o ano inteiro fechando modelo, thinking, tool support e operação.

## Slide 10 - Dezembro de 2025 foi a Virada
Restam: ~51:35 (75s)

E aí, em duas semanas de novembro de 2025, tudo alinhou. Em 13 de novembro a OpenAI lançou o GPT-5.1 pra desenvolvedores, e ao mesmo tempo o Codex CLI finalmente ficou bom o bastante pra rodar tarefa longa de verdade no terminal. Onze dias depois, em 24 de novembro, a Anthropic soltou o Opus 4.5 e o Claude Code amadureceu com thinking entre chamadas de ferramenta, execução em background, fluxo de agente sério. Não foi modelo novo isolado. Foi modelo novo mais CLI de agente madura, dos dois lados, na mesma janela. Em dezembro de 2025, dava pra começar a apostar tempo de verdade nisso. Foi por isso que janeiro de 2026 virou minha entrada na maratona.

## Slide 11 - Fevereiro a novembro de 2026
Restam: ~50:20 (42s)

Então eu parei de falar disso em abstrato e fui testar com pele em jogo. Começou em fevereiro e não parou até agora, novembro. Não com prompt de brinquedo. Não com videozinho fake de SaaS em dez minutos. Projeto real. Deploy real. Teste real. Bug real. Esse é o meu GitHub nos últimos doze meses: 14 mil contribuições, e de fevereiro pra cá quase não tem dia vazio. São 60 projetos que eu criei em 2026, todos abertos. E vale o disclaimer honesto: são todos perfeitos, modelo de excelência de código? Absolutamente não. Alguns viraram software de uso diário, outros são protótipos. O ponto era rodar o ciclo do agente em escala, de verdade.

## Slide 12 - Do zero pra software real
Restam: ~49:38 (35s)

Este slide é só a parede de projetos. FrankMD, FrankMega, Frank Sherlock, Frank Yomik, Frank FBI, Frank Karaoke e outros. O objetivo não é explicar repositório por repositório. O objetivo é mostrar volume e variedade: desktop, Rails, Rust, ferramentas, mídia, deploy, software em uso real. Se a tese estava certa, ela precisava aparecer em mais de um tipo de problema.

## Slide 13 - Números que pesam
Restam: ~49:03 (95s)

E aqui é onde eu boto peso na afirmação de velocidade. Recontei tudo do zero com `tokei`, de janeiro até agora, novembro. São 60 projetos. Dá uns 1,8 milhão de linhas úteis, mais uns 256 mil de teste, 13.614 commits meus e cerca de 1.540 horas ativas estimadas. Em maio eu tinha contado 30 projetos e 432 mil linhas. Em seis meses, mais que quadruplicou. A regra ficou mais rígida, não mais frouxa: só arquivo rastreado no git, sem linha em branco, sem asset, sem vendor, sem código de terceiro. Também tirei JSON, dado gerado, resultado de benchmark e fixture, porque isso infla número sem ninguém escrever nada. Nos projetos onde a comunidade contribuiu, como ai-memory, ai-usagebar e FrankMD, eu só contei a minha fatia. Fork de projeto dos outros, como o Omarchy, ficou de fora. As horas continuam conservadoras: sessões por histórico de commit, corte de 90 minutos de pausa, mais 20 minutos por sessão, teto de 8 horas. Não é tudo que eu trabalhei. É só o que dá pra defender olhando commit. Com isso na mesa, agora dá pra discutir mecanismo, não fé.

## Slide 14 - As únicas ferramentas pra usar agora
Restam: ~47:28 (20s)

E com o que eu fiz tudo isso? Estes são os quatro CLIs que eu realmente usaria para agente de terminal sério em maio de 2026: Claude Code, Codex, opencode e Oh-My-Pi. Claude Code e Codex cobrem os modelos fechados de fronteira. opencode e Oh-My-Pi são bons quando você quer ser agnóstico, testar modelo chinês ou rodar via OpenRouter. O resto é orbital.

## Slide 15 - Trocar de harness sem perder controle
Restam: ~47:08 (25s)

Como eu alterno entre harnesses, acabei criando um kit pequeno para não virar bagunça. Não é orquestrador mágico. É operação básica: ai-jail para dar autonomia com cerca, ai-memory para o contexto sobreviver entre sessões e harnesses, e ai-usagebar para eu saber quando estou perto do limite e preciso trocar de cavalo.

## Slide 27-30 - Autonomia com cerca (ai-jail: instalar, muro de kernel e TUI)
Restam: ~46:43 (110s)

O ai-jail nasceu porque eu gosto de rodar Claude e Codex em modo sem freio, mas não quero dar a chave da casa. Eu tiro a fricção de confirmação dentro do harness e coloco a trava no sistema operacional. Pra começar no Arch Linux é direto pelo AUR: `pacman -S bubblewrap`, `yay -S ai-jail-bin`, e roda `ai-jail --dry-run claude` pra inspecionar ou `ai-jail claude` direto. O projeto fica read-write; seu `/home` e seus segredos ficam de fora. E repara na diferença fundamental contra o sandbox embutido dos harnesses: o sandbox embutido só cerca os comandos de shell, deixando o processo do agente, os servidores MCP e os hooks soltos na sua conta. O ai-jail levanta o muro em volta do harness inteiro — quem responde não é um humano cansado apertando Enter, é o kernel. E você nem precisa decorar flags: a TUI guiada mostra os presets, deixa ligar e desligar rede, SSH, pastas e variáveis visualmente, salva a configuração do projeto e já monta a linha de comando pronta pra copiar com uma tecla.

## Slide 30-34 - Contexto que sobrevive ao harness (ai-memory: quickstart, pipeline, compactação e time)
Restam: ~45:13 (140s)

O ai-memory resolve o outro problema: harness esquece. Claude compacta, Codex compacta, sessão acaba, e o próximo agente não sabe por que você tomou uma decisão duas horas atrás. No Arch Linux também é direto pelo AUR: `yay -S ai-memory-bin`, `ai-memory setup`, liga a unit de usuário com `systemctl --user enable --now ai-memory.service` e abre o agente com `ai-memory run claude` — sem cadastro e sem nuvem obrigatória. Enquanto você trabalha, ele captura observações via hooks, consolida em páginas markdown numa wiki git, recupera com FTS5 e MCP e faz handoff entre sessões e agentes diferentes. E memória que só cresce vira lixo: ele tem pontuação de retenção e *forget sweep* pra compactar ou descartar notas frias, tudo reversível via `restore-page` no histórico do git. E o mesmo servidor funciona pra time inteiro: cada dev usa Claude Code, Codex, Cursor ou Gemini CLI apontando pro mesmo servidor, compartilhando a wiki do projeto e mantendo handoffs pessoais, com contas e auditoria sem plano pago. E não é mais projeto solo: hoje já são mais de 16,5 mil estrelas, 214 contribuidores, mais de 1.392 pull requests mergeados e 750 issues fechadas — e foi exatamente esse volume de comunidade que me forçou a formalizar minhas skills de manutenção no final da palestra.

## Slide - Você não tem objetivos
Restam: ~21:24 (60s)

E aqui entra uma coisa que pouca gente quer admitir. Muita gente não tem problema de prompt. Tem problema de objetivo. A pessoa pede “melhora meu sistema”, “faz ficar profissional”, “resolve a performance”, mas não sabe dizer o estado atual, a restrição, nem a métrica de sucesso. E a pergunta incômoda é essa: você se acostumou a esperar alguém criar o backlog por você? A IA não adivinha isso. Se você não consegue transformar desejo em critério mensurável, você não sabe o que pedir. O agente fica rodando em cima de fumaça.

## Slide - O sprint ideal
Restam: ~20:24 (60s)

O desenho ideal pra mim não é planning longo, backlog enorme e duas semanas tentando cumprir o combinado antigo. Com agente, eu prefiro ciclos muito mais curtos. Uma manhã de product manager com programador, para fechar objetivo, corte de escopo e critério. Uma tarde de QA com programador, para quebrar, validar e achar borda. Isso roda pela semana entre os programadores, cada um com LLM. O tech lead não vira gargalo de aprovação; entra nos pontos certos, quando precisa guiar arquitetura, refatoração ou decisão que custa caro depois.

## Slide - Codar é Barato. Errar é Barato.
Restam: ~19:24 (60s)

Antes, protótipo e POC eram caros demais; por isso todo mundo tentava acertar no planejamento. Com LLM, codar ficou barato e errar também ficou barato. O ganho é testar mais hipóteses, matar ideias ruins cedo e seguir com mais confiança nas ideias boas. Não é virar irresponsável; é reduzir o custo do aprendizado.

## Slide - Agile Vibe Coding é XP com pareamento de máquina
Restam: ~17:54 (90s)

Agile Vibe Coding é XP com pareamento de máquina. A estrutura por baixo é velha: TDD segura erro de modelo antes de virar lama, CI por commit pega drift e regressão cedo, e refatoração contínua evita cirurgia cara depois.

## Slide - O pareamento mudou
Restam: ~16:24 (90s)

O melhor corte de responsabilidade que eu encontrei foi esse: eu trago direção, julgamento, contexto e gosto. O agente traz velocidade de execução, busca e fôlego operacional. Se eu reduzo o agente a digitador burro, piora. Se eu entrego produto e arquitetura pra ele sozinho, piora também. É por isso que eu digo que IA é espelho: sênior bom ganha alavancagem; programador ruim ganha velocidade pra errar.

## Slide 18 - Alcançamos "Developer 10x"?
Restam: ~45:23 (90s)

Da minha experiência prática, o resumo honesto é 5x a 10x de velocidade. Não porque o modelo escreve código perfeito. Não escreve. O ganho vem porque ele atravessa aquele atrito chato que normalmente quebra foco: código repetitivo, busca, refatoração repetitiva, teste repetitivo, execução de comando, tentativa rápida. A confiança, por outro lado, só veio porque o resto continuou existindo: teste, integração contínua, refatoração, produção. E isso já aponta para a causa: a virada não foi genialidade súbita, foi loop melhor.

## Slide 19 - Competente o Suficiente
Restam: ~43:53 (40s)

E se você quiser a versão longa de tudo isso, eu juntei os artigos do ano num livro: Competente o Suficiente. Um ano colocando a IA à prova, sem medo e sem propaganda. Reorganizei tudo como uma história só, chequei os fatos de novo e ilustrei. É pra quem está ansioso ou confuso com IA: o profissional com medo de ser substituído, o pai que leu que a AGI chega em dois anos, o gerente a quem estão vendendo transformação com IA. O EPUB e o PDF são de graça e vão continuar de graça. O impresso e o Kindle saem a preço de custo, eu não ganho nada com isso. A versão 1.1 saiu em 18 de novembro, e se você achar qualquer erro, abre uma issue no GitHub.

## Slide 38 - distrobox-gaming
Restam: ~43:13 (30s)

Agora o lado pessoal da maratona: games. O distrobox-gaming é um container com todos os emuladores já configurados, do RetroArch ao RPCS3 e ao shadPS4. Já passou de 480 estrelas no GitHub. É pra quem não quer perder um fim de semana configurando emulador.

## Slide 39 - Jogo velho não roda no Windows 11
Restam: ~42:43 (40s)

E por que dá tanto trabalho rodar jogo velho? Porque o Windows 11 não é o Windows 98. Ele só existe em 64 bits: DOS e 16 bits morreram. O Screamer é de DOS e usava Glide das placas 3dfx Voodoo. O Colin de 98 usa DirectX 5 com menu em 8 bits de paleta. Jogos da era XP tropeçam em DRM bloqueado desde 2015, DLL de DirectX 9 ausente e checagem de Pentium 4. Cada jogo quebra de um jeito diferente, e a ponte é sempre outra: DOSBox, dgVoodoo, DXVK, Xidi.

## Slide 40 - Menu de jogos do Omarchy (vídeo)
Restam: ~42:03 (25s)

Em cima disso eu fiz o omarchy-games-menu: um launcher pessoal em Rust com interface em QuickShell, reunindo emulador, port de PC e as minhas versões customizadas num lugar só, capa por capa.

## Slide 41 - Colin McRae pelo launcher, 16:9 em 4K (vídeo)
Restam: ~41:38 (30s)

Eu sempre amei Colin McRae Rally de 1998. Fiz o `rea-colin-mcrae` pra Windows e Linux: você aponta pra sua cópia do jogo e ele roda em 4K, widescreen 16:9 de verdade, 60 quadros, HUD e cenários em HD. Por baixo ainda é o executável original de 1998 — o launcher corrige o que o jogo não sabia fazer.

## Slide 42 - Colin McRae em Rust
Restam: ~41:08 (35s)

Aí eu fui mais longe: reconstruir o jogo inteiro em Rust a partir de engenharia reversa, sem nenhum asset no repositório. São ~230 mil linhas de Rust, mais de 3 mil testes, 704 commits e as 2.018 funções originais mapeadas. Single-player completo: 56 estágios, campeonato, contra o relógio com fantasma, replay, chuva e neve (v0.1.4 pra Linux e Windows).

## Slide 43 - Reconstrução em Rust rodando (vídeo)
Restam: ~40:33 (25s)

Isso aqui não é o executável original — é o código reconstruído em Rust rodando nativo.

## Slide 44 - rea-launcher-sdk
Restam: ~40:08 (25s)

Depois de fazer vários launchers de Colin McRae e DiRT, extraí tudo que se repetia num framework: o `rea-launcher-sdk`. Código que vira ferramenta, que vira mais código — foi ele que gerou os launchers seguintes em horas.

## Slide 45 - Bug velho, conserto em horas
Restam: ~39:43 (40s)

Nada aqui é técnica mágica nova, e muito fix parte do trabalho da comunidade (como SilentPatch e Xidi). O que mudou foi o tempo: Colin 2005 e DiRT Rally saíram do SDK em quatro ou cinco horas cada — portar jogo abandonado levava semanas, eu fiz oito em dois dias.

## Slide 46 - Rad Mobile rodando (vídeo)
Restam: ~39:03 (25s)

Inspirado nos ports de arcade do Wanszai, fiz o meu `rea-rad-mobile` (arcade da Sega de 1990) direto do SDK: widescreen real, filtro CRT, suporte a volante de 270 graus e force feedback sintético lendo velocidade e batidas do jogo em tempo real.

## Slide 47 - O console virou arcade
Restam: ~38:38 (30s)

No fim dos anos 90 o arcade parou de usar hardware exótico e virou hardware de console: Dreamcast → NAOMI/NAOMI 2/Atomiswave, Xbox → Chihiro, GameCube → Triforce.

## Slide 48 - Depois o arcade virou PC
Restam: ~38:08 (30s)

Depois o arcade virou PC de vez: Taito Type X, RingEdge (Windows embarcado) e Lindbergh (Linux). O jogo é um executável; o que falta é a placa de I/O e o dongle. Como o TeknoParrot recusa o Wine, meus launchers usam loaders abertos (OpenParrot, lindbergh-loader, Flycast) e rodam direto no Linux.

## Slide 49 - Initial D THE ARCADE Season 5 rodando (vídeo)
Restam: ~37:38 (25s)

Esse é o Initial D THE ARCADE Season 5 rodando no Linux pelo launcher — sem TeknoParrot, com leitor de cartão, botão Start e áudio corrigidos.

## Slide 50 - Melhor que no lançamento
Restam: ~37:13 (35s)

Em vários jogos o launcher entrega melhor que no lançamento: 4K widescreen real, gatilhos independentes, volante com force feedback e correções de bugs antigos — sempre creditando a base da comunidade (SilentPatch, Xidi, Bekoha).

## Slide 51 - 14 launchers rea-*
Restam: ~36:38 (35s)

Somando tudo, são 14 launchers `rea-*`: na esquerda PC clássico (Colin McRae, DiRT, Screamer), na direita Sega e arcade (OutRun, Sega Rally, Rad Mobile, Initial D, Wangan e arcades da Nintendo). A regra é sempre a mesma: você traz a sua cópia, a pasta original fica intacta.

## Slide 54 - Games no AI Lair
Restam: ~25:53 (25s)

E se você quiser ver tudo isso com calma, está tudo documentado no meu site, na página de games: o distrobox-gaming, o menu do Omarchy, os launchers de corrida e até um joguinho que eu fiz. Só lembrando: você precisa da sua própria cópia de cada jogo, nenhum launcher traz arquivo de jogo.

## Slide 53 - github.com/akitaonrails/my-skills
Restam: ~25:53 (20s)

E pra fechar a palestra com as lições aprendidas de um ano construindo e mantendo sessenta projetos abertos: tudo o que deu certo foi parar num repositório público chamado `my-skills`.

## Slide 54 - Processo versionado: my-skills
Restam: ~25:33 (35s)

São mais de vinte e quatro skills em markdown linkadas por symlink em todos os harnesses da minha máquina — Claude Code, Codex, opencode, Kimi, Antigravity. Editei uma regra num lugar, todos os agentes herdam. Só um aviso que está no topo do README: não copie minhas skills no escuro, porque elas têm as minhas premissas. Use como referência e peça pro seu LLM escrever as suas. Modelo é alugado; o processo é seu.

## Slide 54 - A esteira de manutenção em 5 skills
Restam: ~24:53 (40s)

Na manutenção do dia a dia dos meus repositórios abertos, eu peço pro harness exatamente essa esteira: `pr-audit`, `iss-audit`, `github-resolution`, `pr-post-audit` e `release`. A regra central é separar julgamento de execução. `pr-audit` e `iss-audit` nunca fazem merge: eles auditam evidência no código, não a narrativa do autor. Só depois do meu OK entra o `github-resolution`, resolvendo um ticket por vez até ter teste e documentação em dia. Depois o `pr-post-audit` valida a árvore combinada na `main` — porque dois PRs verdes isolados podem quebrar juntos. E o `release` só corta tag e publica quando eu peço explicitamente.

## Slide 55 - Trust Boundary & Hard Quality Bar
Restam: ~24:13 (35s)

No topo de todas essas skills existem duas travas inegociáveis. A primeira é o Trust Boundary: no mundo de agentes, qualquer PR ou issue pública pode esconder prompt injection. Então título, comentário, diff e log de terceiro são sempre dados não confiáveis, nunca instruções — e um PR que edita o `CLAUDE.md` não muda as regras da própria auditoria. A segunda é a Hard Quality Bar: zero código malicioso, zero slop de IA, todo fix com teste que falha sem ele e documentação sincronizada. Um merge lento e certo sempre ganha de uma regressão rápida.

## Slide 56 - O que é Agile Vibe Coding de verdade
Restam: ~23:38 (40s)

E isso fecha o círculo com o título do primeiro slide: Agile Vibe Coding. O segredo não é um prompt mágico nem o modelo que saiu ontem no X. É a engenharia que você monta em volta do agente: cerca no kernel com `ai-jail`, memória independente do fornecedor com `ai-memory`, e processo repetível com `my-skills` — auditoria, worktrees, verificação, segurança, simplificação e `reflect` pra transformar cada padrão repetido em skill nova. Vibe coding sem método multiplica dívida técnica em dez vezes. Agile Vibe Coding é iterar rápido porque a engenharia em volta segura o tranco.

## Slide 55 - Obrigado
Restam: ~25:28 (10s)

Obrigado. Os links estão aí embaixo: Codeminer42, The M.Akita Chronicles e o repositório dessa palestra, que eu vou abrir no dia do evento.

## Slide 56 - Assine The M.Akita Chronicles
Restam: ~25:18 (25s)

E antes de você ir embora, sem falsa modéstia: se curtiu a palestra, assina o The M.Akita Chronicles. Está tudo aí na tela, e tem um QR code pra quem quiser apontar a câmera. É onde eu continuo publicando bastidor real, projeto real, código real e o que deu certo ou errado em produção. Quer acompanhar essa linha de raciocínio semana a semana? Vai em themakitachronicles.com e assina.
