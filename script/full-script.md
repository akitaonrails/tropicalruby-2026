# Canal 3 Expo 2026 - Roteiro Completo

Este roteiro acompanha a versão em PT-BR do deck em `slides/tropical-ruby-2026.md`.

## Slide 1 - Retrogame na era das IAs
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

## Slide 5 - SpaceX abriu capital
Restam: ~55:20 (25s)

Enquanto isso, o dinheiro grande foi pra bolsa. Até a SpaceX abriu capital. IPO precificado a 135 dólares por ação, cerca de 75 bilhões de dólares levantados, valuation perto de 1 trilhão e 770 bilhões no IPO segundo a CNBC. No primeiro dia, fechou a 160 dólares e 95 centavos, alta de 19,2 por cento. O ponto pra mim não é oba-oba de ação. É capital público correndo atrás de infraestrutura física. Quando até foguete, satélite e rede entram nessa escala, fica claro que 2026 virou uma briga de infraestrutura. Não é só software.

## Slide 6 - Anthropic abriu capital
Restam: ~54:55 (25s)

E em 19 de novembro foi a vez da Anthropic, a dona do Claude. Precificou o IPO a 83 dólares por ação, acima da faixa que ela mesma tinha anunciado, e levantou 81 bilhões e 300 milhões de dólares. Só a oferta base já passa a da SpaceX. Abriu na Nasdaq a 111 dólares e meio, alta de 34 por cento, valendo perto de 2 trilhões de dólares. E a receita cresceu 1.200 por cento em um ano: uns 33 bilhões de dólares só nos nove meses até setembro. A empresa que faz o modelo que eu uso todo dia agora joga no mesmo campeonato da SpaceX. Essa corrida também é de capital.

## Slide 7 - Top 20 do benchmark (outubro/2026)
Restam: ~54:30 (40s)

E falando em Anthropic, olha o placar mais recente do meu benchmark, a versão 4, de 28 de outubro. Top 20. Oito modelos fecharam com nota 100: Gemini 4 Argon, GPT-6 Astra, Opus 5, Fable 5, Opus 5.5, e os GPTs 5.6 e 5.5. Então a nota sozinha já não separa ninguém. O que separa é custo e tempo. O Opus 5.5 tirou 100 gastando 16 dólares em uma hora. O GPT-6.1 Terra tirou quase 97 com menos de 2 dólares, em 21 minutos. E lá embaixo do top 20 tem DeepSeek e Kimi passando de 92. Nota alta virou commodity. A briga agora é custo, velocidade e quota.

## Slide 8 - Tier list não é benchmark
Restam: ~53:50 (25s)

E aí, enquanto eu rodo teste, a internet faz tier list. Essa circulou no X essa semana. Olha o Sonnet 5.5 lá em SSS: no meu teste, num projeto longo de verdade, ele tirou 88 e ficou fora do top 20. O GPT-5.6 Terra está em B: no meu teste tirou 100, gastando nove dólares e meio. Às vezes bate, como o Gemini 4 Argon no topo. Mas tier list é opinião em formato de ranking. É barato fazer. Medir dá trabalho, e é por isso que eu meço.

## Slide 9 - Quanto custa ser competente
Restam: ~53:25 (40s)

E aí vem a pergunta que interessa: quanto custa? Saiu hoje o meu benchmark v5. Mesma tarefa pra todo mundo, um app Rails de chat completo, testado e rodando em Docker. Os dezesseis modelos que terminaram passaram de primeira. A diferença está no bolso: do GPT-6 Luna, que fez tudo por quinze centavos de dólar, até o Grok, que custou mais de catorze. Quase cem vezes. E o preço por milhão de tokens na tabela engana: com cache, a conta cai de setenta a noventa por cento, e modelo que fala demais gasta mais que modelo caro que vai direto ao ponto. Competente o suficiente já é barato. A pergunta agora é quanto você paga por rodada.


## Slide 10 - Não era exponencial
Restam: ~52:45 (55s)

Aqui é só o desenho mental. A corrida de treino parecia exponencial porque a gente estava olhando o miolo da curva S. Mas nada é exponencial pra sempre. Desde 2024, o retorno marginal ficou muito pior. Pra ganhar mais uma ordem de grandeza, a conta de capital, energia e compute explode. Então o foco natural muda: otimização, produto e agentes.

## Slide 11 - 2025 foi o ano dos Agentes
Restam: ~51:50 (65s)

Pra mim, 2025 foi o ano em que a pilha foi fechando. Em março, a OpenAI transformou tool support em plataforma de verdade. Em maio, a Anthropic já estava empurrando thinking com tool use e levando Claude Code pra um estado mais sério. Em agosto, GPT-5 começou a aguentar loop longo com menos tropeço. Em novembro, GPT-5.1 e Opus 4.5 deixaram isso mais redondo pra uso diário. Não foi um dia mágico. Foi o ano inteiro fechando modelo, thinking, tool support e operação.

## Slide 12 - Dezembro de 2025 foi a Virada
Restam: ~50:45 (75s)

E aí, em duas semanas de novembro de 2025, tudo alinhou. Em 13 de novembro a OpenAI lançou o GPT-5.1 pra desenvolvedores, e ao mesmo tempo o Codex CLI finalmente ficou bom o bastante pra rodar tarefa longa de verdade no terminal. Onze dias depois, em 24 de novembro, a Anthropic soltou o Opus 4.5 e o Claude Code amadureceu com thinking entre chamadas de ferramenta, execução em background, fluxo de agente sério. Não foi modelo novo isolado. Foi modelo novo mais CLI de agente madura, dos dois lados, na mesma janela. Em dezembro de 2025, dava pra começar a apostar tempo de verdade nisso. Foi por isso que janeiro de 2026 virou minha entrada na maratona.

## Slide 13 - Fevereiro a novembro de 2026
Restam: ~49:30 (42s)

Então eu parei de falar disso em abstrato e fui testar com pele em jogo. Começou em fevereiro e não parou até agora, novembro. Não com prompt de brinquedo. Não com videozinho fake de SaaS em dez minutos. Projeto real. Deploy real. Teste real. Bug real. Esse é o meu GitHub nos últimos doze meses: 14 mil contribuições, e de fevereiro pra cá quase não tem dia vazio. São 60 projetos que eu criei em 2026, todos abertos. E vale o disclaimer honesto: são todos perfeitos, modelo de excelência de código? Absolutamente não. Alguns viraram software de uso diário, outros são protótipos. O ponto era rodar o ciclo do agente em escala, de verdade.

## Slide 14 - Do zero pra software real
Restam: ~48:48 (35s)

Este slide é só a parede de projetos. FrankMD, FrankMega, Frank Sherlock, Frank Yomik, Frank FBI, Frank Karaoke e outros. O objetivo não é explicar repositório por repositório. O objetivo é mostrar volume e variedade: desktop, Rails, Rust, ferramentas, mídia, deploy, software em uso real. Se a tese estava certa, ela precisava aparecer em mais de um tipo de problema.

## Slide 15 - As únicas ferramentas pra usar agora
Restam: ~48:13 (20s)

Aproveitando que falei do mar de modelos, estes são os quatro CLIs que eu realmente usaria para agente de terminal sério em maio de 2026: Claude Code, Codex, opencode e Oh-My-Pi. Claude Code e Codex cobrem os modelos fechados de fronteira. opencode e Oh-My-Pi são bons quando você quer ser agnóstico, testar modelo chinês ou rodar via OpenRouter. O resto é orbital.

## Slide 16 - Trocar de harness sem perder controle
Restam: ~47:53 (25s)

Como eu alterno entre harnesses, acabei criando um kit pequeno para não virar bagunça. Não é orquestrador mágico. É operação básica: ai-jail para dar autonomia com cerca, ai-memory para o contexto sobreviver entre sessões e harnesses, e ai-usagebar para eu saber quando estou perto do limite e preciso trocar de cavalo.

## Slide 17 - Autonomia com cerca
Restam: ~47:28 (40s)

O ai-jail nasceu porque eu gosto de rodar Claude e Codex em modo sem freio, mas não quero dar a chave da casa. Eu tiro a fricção de confirmação dentro do harness e coloco a trava no sistema operacional. O projeto fica read-write. O resto do host fica fora, read-only, mascarado ou mapeado explicitamente. Não é VM, não é blindagem militar, mas é uma camada prática.

## Slide 18 - Contexto que sobrevive ao harness
Restam: ~46:48 (40s)

O ai-memory resolve outro problema: harness esquece. Claude compacta, Codex compacta, sessão acaba, e o próximo agente não sabe por que você tomou uma decisão duas horas atrás. Ele captura prompts, chamadas de ferramenta e limites de sessão, consolida em markdown, indexa com FTS5 e expõe handoff e busca via MCP. Não substitui documentação canônica em `docs/`. Cobre o meio do caminho.

## Slide 19 - Números que pesam
Restam: ~46:08 (95s)

E aqui é onde eu boto peso na afirmação de velocidade. Recontei tudo do zero com `tokei`, de janeiro até agora, novembro. São 60 projetos. Dá uns 1,8 milhão de linhas úteis, mais uns 256 mil de teste, 13.614 commits meus e cerca de 1.540 horas ativas estimadas. Em maio eu tinha contado 30 projetos e 432 mil linhas. Em seis meses, mais que quadruplicou. A regra ficou mais rígida, não mais frouxa: só arquivo rastreado no git, sem linha em branco, sem asset, sem vendor, sem código de terceiro. Também tirei JSON, dado gerado, resultado de benchmark e fixture, porque isso infla número sem ninguém escrever nada. Nos projetos onde a comunidade contribuiu, como ai-memory, ai-usagebar e FrankMD, eu só contei a minha fatia. Fork de projeto dos outros, como o Omarchy, ficou de fora. As horas continuam conservadoras: sessões por histórico de commit, corte de 90 minutos de pausa, mais 20 minutos por sessão, teto de 8 horas. Não é tudo que eu trabalhei. É só o que dá pra defender olhando commit. Com isso na mesa, agora dá pra discutir mecanismo, não fé.

## Slide 20 - Alcançamos "Developer 10x"?
Restam: ~44:33 (90s)

Da minha experiência prática, o resumo honesto é 5x a 10x de velocidade. Não porque o modelo escreve código perfeito. Não escreve. O ganho vem porque ele atravessa aquele atrito chato que normalmente quebra foco: código repetitivo, busca, refatoração repetitiva, teste repetitivo, execução de comando, tentativa rápida. A confiança, por outro lado, só veio porque o resto continuou existindo: teste, integração contínua, refatoração, produção. E isso já aponta para a causa: a virada não foi genialidade súbita, foi loop melhor.

## Slide 21 - Competente o Suficiente
Restam: ~43:03 (40s)

E se você quiser a versão longa de tudo isso, eu juntei os artigos do ano num livro: Competente o Suficiente. Um ano colocando a IA à prova, sem medo e sem propaganda. Reorganizei tudo como uma história só, chequei os fatos de novo e ilustrei. É pra quem está ansioso ou confuso com IA: o profissional com medo de ser substituído, o pai que leu que a AGI chega em dois anos, o gerente a quem estão vendendo transformação com IA. O EPUB e o PDF são de graça e vão continuar de graça. O impresso e o Kindle saem a preço de custo, eu não ganho nada com isso. A versão 1.1 saiu em 18 de novembro, e se você achar qualquer erro, abre uma issue no GitHub.

## Slide 22 - distrobox-gaming
Restam: ~42:23 (30s)

Agora o lado pessoal da maratona: games. O distrobox-gaming é um container com todos os emuladores já configurados, do RetroArch ao RPCS3 e ao shadPS4. Já passou de 480 estrelas no GitHub. É pra quem não quer perder um fim de semana configurando emulador.

## Slide 23 - omarchy-games-menu
Restam: ~41:53 (25s)

Em cima dele eu fiz o omarchy-games-menu: um launcher pessoal em Rust com interface em QuickShell, seguindo o tema do Omarchy. Emulador, port de PC e as minhas versões customizadas, tudo num lugar só.

## Slide 24 - Menu de jogos do Omarchy (vídeo)
Restam: ~41:28 (20s)

É assim que ele fica. A coleção inteira, capa por capa, organizada por plataforma.

## Slide 25 - Quiver
Restam: ~41:08 (30s)

E se você quiser um lugar só pra achar tudo isso, tem o Quiver. É um catálogo com mais de dois mil projetos da comunidade: recomps, source ports, recriações e emuladores, e um launcher grátis pra Windows, Mac, Linux e Android que instala e atualiza tudo. Ele não distribui jogo nenhum, você traz a sua cópia. E tem até um filtro pra esconder os projetos feitos com IA, o que eu acho justo: quem quiser, escolhe.


## Slide 26 - Eu sempre amei Colin McRae
Restam: ~40:38 (30s)

E aqui vai uma confissão: eu sempre amei Colin McRae Rally, desde o PlayStation. Esse é o Colin 2.0 no DuckStation, do jeito que era: 4:3, polígono tremendo, textura borrada. E eu fiquei pensando: dá pra jogar a versão de PC num computador moderno, do jeito certo?

## Slide 27 - Launcher do Colin McRae Rally
Restam: ~40:08 (30s)

Deu. Esse é o rea-colin-mcrae, um launcher pro Colin McRae Rally original de PC, de 1998. Você aponta pra pasta do jogo e escolhe o visual: o original de 1998, o Enhanced na resolução da sua tela, ou um perfil pra Steam Deck. Roda em Windows e Linux.

## Slide 28 - Colin McRae pelo launcher, look original
Restam: ~39:38 (25s)

Primeiro o visual original, em 4:3, como saiu em 1998. Já roda liso num PC de hoje, sem gambiarra de compatibilidade.

## Slide 29 - Colin McRae pelo launcher, 16:9 em alta resolução
Restam: ~39:13 (25s)

Agora o mesmo jogo no modo Enhanced: widescreen, alta resolução, HUD e placas redesenhados em HD. Por baixo é o mesmo executável de 1998. O launcher só corrige o que o jogo não sabia fazer.

## Slide 30 - Cenários de fundo em HD
Restam: ~38:48 (25s)

E olha o detalhe do fundo. O céu, as nuvens e as montanhas eram texturas borradas de 1998. Agora são cenários em HD, e numa tela larga dá pra ver a diferença de longe.


## Slide 31 - rea-colin-mcrae-recomp
Restam: ~38:23 (25s)

Aí eu fui mais longe. Em vez de remendar o executável, tentar reconstruir o jogo inteiro em Rust, a partir de engenharia reversa. Sem nenhum asset do jogo no repositório: você aponta pra sua cópia.

## Slide 32 - Colin McRae em Rust (WIP)
Restam: ~37:58 (40s)

E os números assustam. São uns 223 mil linhas de Rust, quase 3 mil testes, 12 crates e 662 commits em 12 dias. E eu vou repetir: é trabalho em andamento. Não está pronto. Tem uma branch de preservação, que tenta ser idêntica ao executável de 1998, e uma branch moderna, com 4K, widescreen e 144 quadros por segundo.

## Slide 33 - Reconstrução em Rust rodando
Restam: ~37:18 (25s)

E isso aqui não é o executável original. É o código reconstruído em Rust rodando nativo. Ainda tem diferença e ainda tem bug, mas já dá pra correr um estágio inteiro.

## Slide 34 - Colin 04, Colin 2005, DiRT e DiRT Rally
Restam: ~36:53 (35s)

E depois do primeiro eu fui com tudo. Fiz launcher pro Colin McRae Rally 04, pro Colin 2005, pro DiRT e pro DiRT Rally. Mesmo padrão: escolhe a pasta, escolhe o visual, joga em widescreen e alta resolução. No DiRT ainda tinha um crash ao carregar corrida em processador moderno, e isso foi corrigido.

## Slide 35 - rea-launcher-sdk
Restam: ~36:18 (25s)

E quando eu já tinha cinco launchers, extraí o que se repetia num framework: o rea-launcher-sdk. É ele que já gerou os launchers de TeknoParrot e de Rad Mobile. Código que vira ferramenta, que vira mais código.

## Slide 36 - Bug velho, conserto em horas
Restam: ~35:53 (45s)

E o que esses launchers consertam? No Colin de 1998, a corrida parava em 800 por 600. Agora vai a 4K, em widescreen de verdade, a 60 quadros, e ainda ganhou vibração nos gatilhos que o jogo nunca teve. No Colin 04, o patch de widescreen da comunidade deixava os carros 25 por cento mais estreitos, e a engenharia reversa achou o porquê. No Colin 2005, as partículas avançadas só liberavam num Pentium 4 com Hyper-Threading. Agora liberam em qualquer processador. Mas eu não vou fingir que inventei a roda. Nada aqui é técnica nova, e muito fix veio da comunidade. O que mudou foi o tempo. O Colin 2005 e o DiRT Rally saíram do SDK em umas quatro, cinco horas cada. Portar jogo abandonado levava semanas, por isso quase ninguém fazia. Eu fiz oito em uns dois dias.

## Slide 37 - Wanszai no GitHub
Restam: ~35:08 (25s)

E aqui eu preciso dar crédito pra uma inspiração. Faz tempo que eu sigo e uso os ports de arcade do Wanszai: Sega Rally Championship, Ridge Racer, Scud Race, Virtua Racing. Arcade clássico rodando em PC, num download só, do jeito certo.

## Slide 38 - Wanszai no YouTube
Restam: ~34:43 (25s)

Ele mostra tudo no canal dele, e agora está mexendo em Daytona 2. E eu sempre quis um Rad Mobile feito por ele. Só que não existia. Então eu fiz o meu, inspirado nos launchers dele, e com a coisa que eu mais queria: suporte de volante de verdade.

## Slide 39 - rea-rad-mobile
Restam: ~34:18 (25s)

Esse é o meu Rad Mobile, um arcade da Sega de 1990, saído direto do SDK. Ele já vem com um MAME empacotado e com patch, roda em Windows e Linux, e você só precisa da sua ROM.

## Slide 40 - Launcher do Rad Mobile
Restam: ~33:53 (30s)

E o menu você dirige com o volante. O arcade original tinha volante de 270 graus, dois pedais e nenhum motor. O launcher lê o meu volante, ajusta pra 270 graus e ainda inventa o force feedback que o gabinete nunca teve: ele lê a velocidade e as batidas do jogo rodando e gera as forças no volante.

## Slide 41 - Rad Mobile rodando
Restam: ~33:23 (25s)

E é isso aqui: um arcade de 1990 em widescreen de verdade, com volante e force feedback. Até o limpador de para-brisa e o farol, que no MAME puro só funcionavam no teclado, agora funcionam no volante.

## Slide 42 - O console virou arcade
Restam: ~32:58 (35s)

Uma coisa que pouca gente sabe: no fim dos anos 90 o arcade parou de usar hardware exótico e começou a usar hardware de console. O Dreamcast virou NAOMI, depois NAOMI 2, e a Sammy fez o Atomiswave na mesma base. O Xbox virou o Chihiro da Sega, que roda OutRun 2. O GameCube virou o Triforce, uma parceria da Namco, da Sega e da Nintendo. Pra quem emula, isso é ótimo: quem emula o console chega perto de emular o arcade.

## Slide 43 - Depois o arcade virou PC
Restam: ~32:23 (35s)

Depois o arcade virou PC mesmo. O Taito Type X e o RingEdge da Sega rodam Windows embarcado, e o Lindbergh da Sega é um Pentium 4 com GeForce rodando Linux. O jogo é só um executável; o que falta é a placa de I/O, o dongle e a rede do gabinete. O TeknoParrot emula essas peças no Windows, o OpenParrot é a parte de código aberto, e o Lindbergh Loader roda esses jogos direto no Linux. Só que o TeknoParrot é Windows e recusa o Wine, então meus launchers trocam ele pelos loaders abertos e rodam tudo direto no Linux.

## Slide 44 - Azimuth
Restam: ~31:48 (30s)

E a mesma história continua uma geração depois. O Xbox One é praticamente um PC, e o Azimuth roda as versões de Xbox One do Forza Horizon 2 e 3 e do Forza Motorsport 5 e 6 no Windows e no Linux. Não é emulador: o jogo roda nativo, e o wrapper só traduz as chamadas de sistema e de gráfico.

## Slide 45 - Launcher do Wangan Midnight
Restam: ~31:18 (30s)

Eu fiz a mesma coisa pros arcades. Esse é o launcher da série Wangan Midnight, do R até o Maximum Tune 6RR, num programa só. Sem TeknoParrot: uso o OpenParrot compilado do código-fonte, com as minhas correções, e escrevi a minha própria placa de I/O falando o protocolo da Namco.

## Slide 46 - Wangan Midnight rodando
Restam: ~30:48 (25s)

Isso aqui é o Maximum Tune 6R rodando no Linux, pelo launcher.

## Slide 47 - Launcher do Initial D
Restam: ~30:23 (30s)

E esse é o do Initial D: do primeiro Arcade Stage, de 2002, até o THE ARCADE Season 5, de 2025. Só loader aberto, Flycast, lindbergh-loader e windowsarcadeloader, e eu corrigi o leitor de cartão, o botão Start travado e o som que crashava no Wine.

## Slide 48 - Initial D rodando
Restam: ~29:53 (25s)

E esse é o THE ARCADE Season 5 rodando pelo launcher. Repara na cena em estilo mangá no meio da corrida.

## Slide 49 - Achados de verdade
Restam: ~29:28 (45s)

E não foi só empacotar. A engenharia reversa achou coisa. No Screamer, de 1995, um jogo de DOS, consegui widescreen de verdade mexendo na matriz da câmera, e descobri por que destravar o FPS quebra o jogo: a física roda presa a 50 hertz. No Screamer 2 da GOG, o driver 3dfx que vem junto é de Windows e não funciona no DOS; com o driver do Screamer Rally, o modo 3dfx volta. O DiRT Rally de Linux crashava em todo Ryzen 5000 pra cima, porque o jogo lê uma memória que ele mesmo marcou só pra executar. E o Sega Rally Revo engasgava uma vez por segundo no Windows porque, desde o Windows 10 2004, o timer de 1 milissegundo é por processo, e o jogo nunca pedia o dele.

## Slide 50 - Arcade no Linux, sem TeknoParrot
Restam: ~28:43 (45s)

Nos arcades foi a mesma coisa, sem TeknoParrot. O Initial D 4 crashava em toda largada. Com um watchpoint de hardware achei o culpado: o leitor de cartão emulado escrevia fora do próprio objeto e apagava o objeto dos controles. O conserto foi um byte. No Wangan, a interface do TeknoParrot fazia o papel da placa de I/O do gabinete, então escrevi a minha, falando o protocolo da Namco. Os jogos da Nintendo rodam no Dolphin oficial, e os da Sega ganharam o câmbio H do gabinete e o volante de 270 graus.

## Slide 51 - 14 launchers rea-*
Restam: ~27:58 (40s)

Somando tudo, são catorze launchers. Na esquerda, jogos antigos de PC: Colin McRae, DiRT, Screamer. Na direita, Sega e arcade: OutRun, Sega Rally, Rad Mobile, Initial D, Wangan e os arcades da Nintendo. A regra é sempre a mesma: você usa a sua cópia, a pasta original só é lida, e o launcher roda de uma cópia privada.

## Slide 52 - Games no AI Lair
Restam: ~27:18 (25s)

E se você quiser ver tudo isso com calma, está tudo documentado no meu site, na página de games: o distrobox-gaming, o menu do Omarchy, os launchers de corrida e até um joguinho que eu fiz. Só lembrando: você precisa da sua própria cópia de cada jogo, nenhum launcher traz arquivo de jogo.

## Slide 53 - Obrigado
Restam: ~26:53 (10s)

Obrigado. Os links estão aí embaixo: Codeminer42, The M.Akita Chronicles e o repositório dessa palestra, que eu vou abrir no dia do evento.

## Slide 54 - Assine The M.Akita Chronicles
Restam: ~26:43 (25s)

E antes de você ir embora, sem falsa modéstia: se curtiu a palestra, assina o The M.Akita Chronicles. Está tudo aí na tela, e tem um QR code pra quem quiser apontar a câmera. É onde eu continuo publicando bastidor real, projeto real, código real e o que deu certo ou errado em produção. Quer acompanhar essa linha de raciocínio semana a semana? Vai em themakitachronicles.com e assina.
