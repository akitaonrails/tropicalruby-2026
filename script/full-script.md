# Beyond Summit 2026 - Roteiro Completo

Este roteiro acompanha a versão em PT-BR do deck em `slides/tropical-ruby-2026.md`.

## Slide 1 - Agile Vibe Coding
Restam: ~58:45 (75s)

Vou abrir direto, porque a gente tem uma hora pra desmontar isso com calma: agentes de IA mudaram o custo de construir software, mas não aboliram engenharia. Perguntar “IA substitui programador?” é pouco. A pergunta que importa é: qual processo sobrevive quando errar ficou barato e entregar ficou rápido? A tese é simples: agente bom aumenta muito a produtividade de quem sabe dirigir. Mas também acelera a bagunça de quem não sabe. Esse é o preço de vibe coding.

## Slide 2 - Fabio Akita
Restam: ~57:45 (60s)

Pra quem só me conhece por um pedaço da internet: fui cofundador da Codeminer 42 e hoje estou no conselho. Fundei e organizei a RubyConf Brasil até 2016. Passei anos no YouTube com o Akitando, mais de quinhentos mil seguidores, e sigo ativo no X como @akitaonrails, com cerca de oitenta e três mil seguidores lá também. E o akitaonrails.com acabou de completar 20 anos no dia 5 de abril de 2026, com mais de 700 artigos publicados, agora em português e inglês. Também fui parar fora da bolha tech, em programas como Flow e Inteligência Ltda. Estou falando isso por um motivo simples: eu já vi hype demais, mercado demais e promessa furada demais pra comprar fantasia fácil.

## Slide 3 - O pânico da IA caiu em cima de uma bolha velha
Restam: ~56:50 (55s)

Eu não comecei a falar disso quando IA virou moda. Eu já vinha batendo na bolha da programação, na economia do programador ruim, nas promessas de curso e bootcamp, muito antes de agente de código prestar pra alguma coisa. A IA não inventou essa fraqueza. Ela só escancarou mais rápido.

## Slide 4 - Meio milhão de demitidos em tech desde 2022
Restam: ~56:25 (25s)

E os números do Crunchbase confirmam que a correção começou bem antes da IA pegar agente. Em 2022, mais de 93 mil demissões em tech nos EUA. 2023 foi o pico, 191 mil. 2024, 95 mil. 2025, 127 mil — Intel cortou 27 mil sozinha, Microsoft 15 mil, Verizon 15 mil, Amazon quase 15 mil. E 2026 já decolou. A Oracle demitiu entre 20 e 30 mil por e-mail em 31 de março, sem aviso prévio e com severance picado. A Meta cortou 8 mil em maio, depois de subir o capex de IA pra 145 bilhões. Só em abril foram 83 mil cortes em tech, com 21 mil já atribuídos a IA. Total acumulado desde 2022: mais de meio milhão. E isso só nos Estados Unidos.

## Slide 5 - A mentira antiga
Restam: ~55:05 (80s)

Eu já vinha batendo nessa tecla antes de IA virar pauta. A mentira antiga era simples: faz um cursinho rápido, vira engenheiro de software em dois meses, ganha salário alto e entra no modo easy. Isso sempre foi conversa mole. Bootcamp ensina ferramenta. Não comprime anos de julgamento de engenharia. E a prova é que os layoffs começaram no fim de 2022, antes da IA saber programar direito. O ChatGPT foi acelerador. Não foi a causa original.

## Slide 6 - Claude Code vazou
Restam: ~54:10 (55s)

Daí veio uma das confirmações mais engraçadas possíveis dessa tese: o vazamento do Claude Code em 31 de março de 2026. A CLI oficial da Anthropic deixou escapar um mapa enorme do código e, de repente, todo mundo pôde olhar as tripas de uma das ferramentas de agente mais importantes do mercado.

## Slide 7 - A lição não foi “uau, magia”
Restam: ~52:40 (90s)

Abriram o código. O que apareceu lá dentro? Não foi perfeição divina. Foi uma base grande, pressionada por entrega, cheia de decisão tática, remendo e complexidade operacional. O famoso espaguete de sênior. E o mais importante: quase imediatamente começaram a copiar comportamento e reimplementar partes. Esse é o ponto. Quando a mística some, sobra engenharia.

## Slide 8 - LLMs são Papagaios Estocásticos
Restam: ~52:25 (15s)

E essa é a forma mais honesta de descrever o que um LLM faz por baixo: papagaio estocástico. Termo cunhado em 2021 por Emily Bender e a turma da Timnit Gebru. O modelo repete padrões de token aprendidos no treino, com fluência impressionante, mas sem entender o que diz. É bonito de leitura e fraco de compromisso com verdade. É por isso que ele erra com confiança, alucina API e te bajula em vez de te contrariar.

## Slide 9 - LLMs ainda bajulam e erram
Restam: ~51:00 (85s)

Eu chamei LLMs de loot boxes porque elas são probabilísticas. Não são compiladores determinísticos. Dá pra melhorar bastante com contexto, ferramenta, ciclo de avaliação e prompt melhor? Dá. Mas o modelo de 2026 ainda baixa a cabeça pra você. Se você vem com premissa torta, ele muitas vezes prefere agradar em vez de contrariar. Ele também continua errando com confiança. Inventa detalhe, completa lacuna do jeito errado, segue em frente como se estivesse tudo certo. Por isso agente sem freio é desastre. O que segura ainda é execução real, teste real e revisão real.

## Slide 10 - Treino e inferência disputam a mesma tomada
Restam: ~49:35 (85s)

E aqui entra minha especulação sobre a economia da IA. A conta física começou a apertar de verdade. Os quatro grandes — Alphabet, Amazon, Meta e Microsoft — comprometeram cerca de 650 bilhões de dólares em capex de IA pra 2025 e 2026 juntos. Em 2024 isso era 222 bilhões. Triplicou em dois anos. Do outro lado, a IEA revisou pra cima em dezembro de 2025 e agora projeta 1.100 terawatt-hora de consumo elétrico em data centers globais em 2026 — equivalente ao Japão inteiro. Em 2024 eram 415. E tem mais um detalhe que muda a leitura: a Epoch AI mostra que inferência saiu de 33% do compute em 2023 e deve bater 67% em 2026. Não é mais só treino que consome a tomada. Agente queima muito mais inferência por usuário do que chatbot bobo. Então eu não apostaria em outro salto de ordem de grandeza no frontier tão cedo. Eu apostaria em briga por eficiência, suporte a ferramentas, custo de inferência e produto. E se a Anthropic vier mesmo pra IPO em 2026, essa pressão por margem e previsibilidade fica ainda maior.

## Slide 11 - Carro elétrico ia salvar. IA comeu a economia.
Restam: ~49:15 (20s)

Tem uma ironia que vale destacar. Carro elétrico ia ser a grande economia de energia da década. A frota global de EV hoje consome cerca de 130 terawatt-hora por ano, segundo a IEA. O crescimento de data center sozinho, entre 2024 e 2026, foi de 685 terawatt-hora. Em dois anos, IA adicionou na rede aproximadamente cinco vezes toda a eletricidade que a frota global de carro elétrico consome hoje. EV e data center disputam o mesmo megawatt — e data center está ganhando de longe.

## Slide 12 - 7 GW que não saem do papel em 2026
Restam: ~48:55 (20s)

E pra deixar a conta física concreta: dos cerca de 12 gigawatts de data center anunciados pra 2026 nos Estados Unidos, só uns 5 estão em obra de verdade. Os outros 7 atrasaram ou foram cancelados. Bloomberg confirma um intervalo de 30 a 50 por cento. O gargalo não é dinheiro, é equipamento físico: transformador de alta tensão tem fila de até 5 anos, switchgear escasso, tarifa chinesa de 15 a 25 por cento. Fila de conexão à rede leva até 5 anos. E mesmo assim os hyperscalers não recuaram o capex de 650 bilhões pra 2025 e 2026. Dólar sobra. Tomada não.

## Slide 13 - A corrida por compute acelera em 2026
Restam: ~48:40 (15s)

Mas mesmo com essa correção em curso, a corrida por compute não desacelerou. Em 2026, Anthropic e xAI fecharam contratos pesados de capacidade pra suprir treino e inferência. A fila do mercado não é mais por desenvolvedor júnior. É por GPU, energia e data center.

## Slide 14 - SpaceX abriu capital
Restam: ~48:15 (25s)

E no meio dessa corrida de infraestrutura, até a SpaceX abriu capital. IPO precificado a 135 dólares por ação, cerca de 75 bilhões de dólares levantados, valuation perto de 1 trilhão e 770 bilhões no IPO segundo a CNBC. No primeiro dia, fechou a 160 dólares e 95 centavos, alta de 19,2 por cento. O ponto pra mim não é oba-oba de ação. É capital público correndo atrás de infraestrutura física. Quando até foguete, satélite e rede entram nessa escala, fica claro que 2026 virou uma briga de infraestrutura. Não é só software.

## Slide 15 - Não era exponencial
Restam: ~47:20 (55s)

Aqui é só o desenho mental. A corrida de treino parecia exponencial porque a gente estava olhando o miolo da curva S. Mas nada é exponencial pra sempre. Desde 2024, o retorno marginal ficou muito pior. Pra ganhar mais uma ordem de grandeza, a conta de capital, energia e compute explode. Então o foco natural muda: otimização, produto e agentes.

## Slide 16 - 2025 foi o ano dos Agentes
Restam: ~46:15 (65s)

Pra mim, 2025 foi o ano em que a pilha foi fechando. Em março, a OpenAI transformou tool support em plataforma de verdade. Em maio, a Anthropic já estava empurrando thinking com tool use e levando Claude Code pra um estado mais sério. Em agosto, GPT-5 começou a aguentar loop longo com menos tropeço. Em novembro, GPT-5.1 e Opus 4.5 deixaram isso mais redondo pra uso diário. Não foi um dia mágico. Foi o ano inteiro fechando modelo, thinking, tool support e operação.

## Slide 17 - Dezembro de 2025 foi a Virada
Restam: ~45:00 (75s)

E aí, em duas semanas de novembro de 2025, tudo alinhou. Em 13 de novembro a OpenAI lançou o GPT-5.1 pra desenvolvedores, e ao mesmo tempo o Codex CLI finalmente ficou bom o bastante pra rodar tarefa longa de verdade no terminal. Onze dias depois, em 24 de novembro, a Anthropic soltou o Opus 4.5 e o Claude Code amadureceu com thinking entre chamadas de ferramenta, execução em background, fluxo de agente sério. Não foi modelo novo isolado. Foi modelo novo mais CLI de agente madura, dos dois lados, na mesma janela. Em dezembro de 2025, dava pra começar a apostar tempo de verdade nisso. Foi por isso que janeiro de 2026 virou minha entrada na maratona.

## Slide 18 - Fevereiro a maio de 2026
Restam: ~44:30 (30s)

Então eu parei de falar disso em abstrato e fui testar com pele em jogo. Foi de fevereiro até maio. Não com prompt de brinquedo. Não com videozinho fake de SaaS em dez minutos. Projeto real. Deploy real. Teste real. Bug real. Pós-produção real.

## Slide 19 - Do zero pra software real
Restam: ~43:55 (35s)

Este slide é só a parede de projetos. FrankMD, FrankMega, Frank Sherlock, Frank Yomik, Frank FBI, Frank Karaoke e outros. O objetivo não é explicar repositório por repositório. O objetivo é mostrar volume e variedade: desktop, Rails, Rust, ferramentas, mídia, deploy, software em uso real. Se a tese estava certa, ela precisava aparecer em mais de um tipo de problema.

## Slide 20 - 30 projetos (experimentais)
Restam: ~43:43 (12s)

Tudo aberto no GitHub. São 30 repositórios em várias linguagens e domínios. E aqui vale o disclaimer honesto que eu escrevi no post de fechamento da maratona: "todos os 30 são perfeitos, modelos de excelência de código?" Absolutamente não. São experimentos. Alguns viraram software de uso diário, outros são protótipos. O ponto não era entregar 30 produtos perfeitos. Era rodar o ciclo do agente em escala, de verdade.

## Slide 21 - As únicas ferramentas pra usar agora
Restam: ~43:23 (20s)

Aproveitando que falei do mar de modelos, estes são os quatro CLIs que eu realmente usaria para agente de terminal sério em maio de 2026: Claude Code, Codex, opencode e Oh-My-Pi. Claude Code e Codex cobrem os modelos fechados de fronteira. opencode e Oh-My-Pi são bons quando você quer ser agnóstico, testar modelo chinês ou rodar via OpenRouter. O resto é orbital.

## Slide 22 - Trocar de harness sem perder controle
Restam: ~42:58 (25s)

Como eu alterno entre harnesses, acabei criando um kit pequeno para não virar bagunça. Não é orquestrador mágico. É operação básica: ai-jail para dar autonomia com cerca, ai-memory para o contexto sobreviver entre sessões e harnesses, e ai-usagebar para eu saber quando estou perto do limite e preciso trocar de cavalo.

## Slide 23 - Autonomia com cerca
Restam: ~42:18 (40s)

O ai-jail nasceu porque eu gosto de rodar Claude e Codex em modo sem freio, mas não quero dar a chave da casa. Eu tiro a fricção de confirmação dentro do harness e coloco a trava no sistema operacional. O projeto fica read-write. O resto do host fica fora, read-only, mascarado ou mapeado explicitamente. Não é VM, não é blindagem militar, mas é uma camada prática.

## Slide 24 - Contexto que sobrevive ao harness
Restam: ~41:38 (40s)

O ai-memory resolve outro problema: harness esquece. Claude compacta, Codex compacta, sessão acaba, e o próximo agente não sabe por que você tomou uma decisão duas horas atrás. Ele captura prompts, chamadas de ferramenta e limites de sessão, consolida em markdown, indexa com FTS5 e expõe handoff e busca via MCP. Não substitui documentação canônica em `docs/`. Cobre o meio do caminho.

## Slide 25 - Mesmo dev. Mesmo agente. Processo diferente.
Restam: ~40:13 (85s)

Aqui entra a comparação que eu acho mais forte de todas. FrankMD de um lado. M.Akita Chronicles do outro. Mesmo desenvolvedor. Mesmo agente. Processo diferente. No FrankMD eu ainda estava pagando várias decisões tardias: refactor pesado, teste correndo atrás, reorganização mais traumática. No M.Akita Chronicles entrou TDD, CI e refatoração contínua desde o começo. Resultado: 212 commits em 19 dias num caso, 274 commits em 8 dias no outro. A variável não foi “IA melhor”. Foi disciplina de engenharia. É aqui que a conversa deixa de ser opinião e vira evidência.

## Slide 26 - Números que pesam
Restam: ~38:38 (95s)

E aqui é onde eu boto peso na afirmação de velocidade. Esse recorte foi fechado em maio de 2026. Recontando do zero com `tokei`, agora no recorte novo da Beyond Summit, dá 432.134 linhas úteis, 62.643 linhas de teste, 2.241 commits e cerca de 473 horas ativas estimadas. Entraram 30 projetos AI-assisted: FrankMD, FrankClaw, Frank Sherlock, FrankMega, Frank Yomik, Frank FBI, Investigator, Karaoke, easy-ffmpeg, easy-subtitle, mila-bot, configs de Omarchy, homelab, shadPS4, e outros. A regra é simples: arquivo rastreado no git, sem linha em branco, sem asset, sem build, sem vendor, sem árvore de terceiro. Para software, isso é código e comentários rastreados pelo `tokei`. Para blog, docs, relatórios e conteúdo, markdown também conta, porque ali ele é o produto do trabalho. Teste continua separado por path. No `shadPS4` eu não contei o emulador inteiro; contei só a branch experimental `gamma-debug`. No site, não contei o blog inteiro; contei só o recorte AI-era. As horas continuam conservadoras: sessões por histórico de commit, corte de 90 minutos de pausa, mais 20 minutos por sessão, teto de 8 horas. Não é tudo que eu trabalhei. É só o que dá pra defender olhando commit. Com isso na mesa, agora dá pra discutir mecanismo, não fé.

## Slide 27 - Alcançamos "Developer 10x"?
Restam: ~37:08 (90s)

Da minha experiência prática, o resumo honesto é 5x a 10x de velocidade. Não porque o modelo escreve código perfeito. Não escreve. O ganho vem porque ele atravessa aquele atrito chato que normalmente quebra foco: código repetitivo, busca, refatoração repetitiva, teste repetitivo, execução de comando, tentativa rápida. A confiança, por outro lado, só veio porque o resto continuou existindo: teste, integração contínua, refatoração, produção. E isso já aponta para a causa: a virada não foi genialidade súbita, foi loop melhor.

## Slide 28 - Prompt único é pra demo
Restam: ~36:03 (65s)

A fantasia do prompt único é preguiçosa. Ela parte da ideia de que dá pra prever e especificar tudo antes. Software real não funciona assim. Produção revela coisa que você nem sabia que importava. A API vem torta. A infra falha do jeito errado. O usuário faz o que ninguém previu. O requisito muda. Prompt único serve pra demo. Produção pede iteração.

## Slide 29 - github.com/akitaonrails/llm-coding-benchmark
Restam: ~35:51 (12s)

Antes de mostrar o ranking, vale dizer que tudo isso está aberto. O repositório está em github.com/akitaonrails/llm-coding-benchmark. Quatro rodadas documentadas em abril e maio, prompt e configuração versionados, dados brutos no repo. Quem quiser reproduzir o benchmark com seus próprios modelos, é só clonar.

## Slide 30 - Benchmark Ranking (Junho/2026)
Restam: ~35:39 (12s)

O ranking agora é de junho e já tem 34 modelos scored. Eu cortei a imagem no top 8 pra caber no slide. Opus 4.7 e GPT 5.4 xHigh continuam empatados no topo, 97. GPT 5.5 vem em 96, Opus 4.8 em 95. A novidade é o miolo do Tier A: Fable 5 em 94, Gemini 3.5 Flash em 93, Kimi K2.6 e GLM 5.2 empatados em 87. E Kimi K2.7 Code ficou logo fora do corte, em 86.

## Slide 31 - Modelos fechados ainda lideram
Restam: ~34:34 (65s)

No ecossistema de modelos em junho de 2026, minha leitura prática é simples. Anthropic e OpenAI ainda lideram código sério: Opus 4.7 e GPT 5.4 empatam em 97, GPT 5.5 vem logo atrás, e Opus 4.8 quase encosta. Mas o bloco de cima apertou. Fable 5 entrou forte, Gemini 3.5 Flash surpreendeu, Kimi K2.6 continua barato e bom, e GLM 5.2 corrigiu a vergonha do GLM 5.1. Open-ish ainda não substitui o fluxo completo com agentes, mas já não dá mais pra tratar como brinquedo.

## Slide 32 - Quem consegue bater o Claude Opus?
Restam: ~32:59 (95s)

Pra não ficar só na opinião, montei um benchmark automatizado que agora tem 34 modelos scored. Open source locais numa RTX 5090 e num servidor AMD com 128 GB de memória unificada, comerciais via API pelo OpenRouter, todos no mesmo runner, mesmas condições. A rubrica continua com 8 dimensões: completude do deliverable, RubyLLM correto, qualidade dos testes, error handling, persistência, Hotwire de verdade, arquitetura e prod-ready. Score 0 a 100, Tier A, B, C, D. Resultado: o topo ainda é fechado, mas ficou mais cheio. Opus 4.7 e GPT 5.4 xHigh empatam em 97. GPT 5.5 vem em 96. Opus 4.8 em 95. Fable 5 em 94. Gemini 3.5 Flash em 93. Kimi K2.6 e GLM 5.2 empatam em 87. Kimi K2.7 Code ficou logo atrás, 86. O ponto não mudou: tamanho virou commodity. O que separa quem aguenta agente real é infraestrutura — thinking, tool calling e prompt caching casados.

## Slide 33 - Não é mais só parâmetros
Restam: ~31:34 (85s)

Aí vem a pergunta óbvia quando alguém olha esse benchmark: por que só esses quatro? E a resposta curta é que tamanho de modelo não é mais o que separa os bons dos ruins. Tamanho virou commodity. O que separa quem aguenta um agente real de verdade são três coisas que precisam estar casadas. Tem que ter prompt caching. Sem KV cache decente, cada turno do agente relê o contexto inteiro, e o custo do loop explode. Você não consegue segurar uma sessão longa de Claude Code rodando se a infraestrutura não cacheia direito. Tem que ter tool calling de verdade. O modelo precisa escolher qual ferramenta chamar, montar os argumentos corretamente, receber resultado de volta e usar isso pro próximo passo. Muito modelo open source fala que faz tool calling, mas na prática ou trava ou inventa método que não existe. E tem que ter reasoning, ou thinking, como a Anthropic chama. Que é basicamente um budget extra de inferência pra planejar antes de agir em vez de chutar a primeira resposta que vem. Sem esses três casados, não tem agente que funcione na prática. Poucos modelos passam porque poucos fecham essas três coisas juntas. Não é falta de parâmetro, é falta de infraestrutura completa. O DeepSeek é o exemplo mais gritante disso hoje. O modelo em si não é ruim. Mas ele falha no fluxo de agente justamente porque não fecha essas três condições juntas.

## Slide 34 - "Coder" no nome não vira coder melhor
Restam: ~30:14 (80s)

E tem outra surpresa do benchmark que vale a pena destacar, porque vai contra o consenso. A intuição de quase todo mundo é que modelos com "Coder" no nome são os melhores pra programação, afinal foram fine-tunados especificamente em código. Mas no benchmark deu o oposto. Dos três Qwen Coder dedicados, dois falharam catastroficamente: o Qwen 3 Coder 30B devolveu uma string mockada hardcoded em vez de chamar a API, e o Qwen 2.5 Coder 32B rodou 90 minutos de timeout sem escrever um único arquivo. O terceiro nem rodou direito. Enquanto isso, as versões gerais do Qwen se saíram melhor que as Coder dedicadas. O Qwen 3.5 35B-A3B, que é MoE geral, rodou Rails na RTX 5090 e as alucinações que apareceram eram resolvíveis em um ou dois follow-ups. Foi o menos ruim da família. Ou seja, versão geral bateu as Coder dedicadas. E mais: eu coloquei no benchmark o Qwen 3.5 27B distilado direto do Claude 4.6 Opus, exatamente pra testar a promessa de "Claude em casa". Rodou Rails, mas alucinou a API toda. Distilação não foi o atalho. E pra não sair nenhum mal-entendido: se alguém insistir em testar Qwen pra código, a única variação que ainda vale gastar tempo avaliando é o Qwen 3.5 35B-A3B MoE geral — e mesmo ele fica bem atrás de Claude, GPT 5.4 e GLM 5.1. A lição amarra direto com o slide anterior: marketing label não substitui as três condições — prompt caching, tool calling e reasoning casados. Sem essas três, não importa quantas vezes você ponha "Coder" no nome do modelo.

## Slide 35 - IA nunca vai ser perfeita. Mas errar ficou barato.
Restam: ~28:44 (90s)

E aqui é onde eu acho que muita gente ainda erra a leitura do mercado. LLM nunca vai ser determinística. Não importa qual modelo você esteja olhando, ele vai continuar errando, alucinando, baixando a cabeça pro usuário, inventando endpoint que não existe. Isso não vai sumir. O que mudou não foi a perfeição do modelo. Foi o custo de errar. O ciclo de feedback ficou tão curto que errar deixou de ser caro. O agente roda, quebra, recebe o stack trace, conserta, tenta de novo, em segundos. A gente parou de esperar o modelo perfeito e passou a usar o modelo imperfeito dentro de um loop barato. Essa é a virada que importa. E quando algo fica imperfeito mas barato, o open source corre por cima muito rápido. O claw-code apareceu como clone clean-room do Claude Code em menos de 24 horas, direto no GitHub da ultraworkers. Quase junto veio o free-code, que é um fork sem telemetria e sem as travas. E o OpenClaw, que já era um projeto maduro antes do leak, ganhou um empurrão: agora tem o memclaw plugado nele, que é um sistema de memória inspirado no do próprio Claude Code. Ou seja, não foi só copiar comportamento de fora, a galera do open source também está absorvendo os padrões internos e recriando por cima. E o corte de mercado que sai disso você já viu. O que ficou barato é software trivial. CRUD, landing page, painel interno, bot, ETL, cola entre APIs. O que continua caro é o que sempre foi. Julgamento, arquitetura, operação, manutenção e alguém disposto a ser dono do problema.

## Slide 36 - Assinatura ganha de pay-as-you-go
Restam: ~27:19 (85s)

E quando você vai olhar o preço, tem um detalhe que muita gente ignora. Pay-as-you-go via API parece mais honesto, mas sai muito caro muito rápido pra quem usa isso pra coding todo dia. Pagando GPT 5.4 Pro por token no OpenRouter, num uso moderado de uns 15 milhões de tokens de input e 3 milhões de output por mês, você bate perto de 990 dólares por mês. No benchmark, ele dá 97 pontos, mas custa uns 16 dólares por run. O GPT 5.5 quase empata, 96 pontos, por uns 10 dólares. Do lado da Anthropic, Opus 4.7 e 4.8 ficam perto de 1 dólar por run, mas Fable 5 já sobe pra algo como 11 dólares estimados. E aí o Tier A barato fica interessante: Kimi K2.6 e Kimi K2.7 Code rodam por uns 30 centavos. GLM 5.2 entra por assinatura. Então, traduzindo: se você usa coding agent sério no dia a dia, assinatura ainda ganha de pay-as-you-go. Talvez esteja subsidiado demais. Talvez não pare em pé pra sempre. Mas hoje é assim.

## Slide 37 - Heróis ou Vilões
Restam: ~26:44 (35s)

Uma tentação depois desse slide de preço é transformar tudo em novela de fundador. Sam Altman de um lado, Dario Amodei do outro. OpenAI contra Anthropic. Aceleracionista contra cauteloso. De um lado, hype, escala e Elon processando. Do outro, Fable 5, Mythos 5 e até shutdown de governo entrando na história. Herói ou vilão, dependendo do feed que você segue. Só que o motor real é mais chato: margem, compute, assinatura subsidiada, API cara, IPO na porta e distribuição. Esses caras não são personagens de Marvel. São CEOs tentando comprar tempo, GPU e narrativa. O importante pra nós não é torcer por um deles. É entender o incentivo. Quem controla custo, distribuição e hardware consegue empurrar o resto do mercado. E é por isso que agora entra a China.

## Slide 38 - China chegou perto do topo
Restam: ~26:19 (25s)

Vale um recorte separado pra um ponto novo dessa última rodada: modelos chineses continuam no Tier A do benchmark. Kimi K2.6, da Moonshot, ficou em 87 sobre 100, e é o Tier A mais barato do benchmark: 30 centavos por run, com FakeChat correto, rescue de erro e session cookie multi-worker safe. GLM 5.2 também fez 87, mas com ressalva: DI e testes fortes, persistência ainda process-local sem cap. Isso é importante porque o GLM 5.1 tinha tropeçado feio, inventando uma DSL que não existia. O 5.2 corrigiu muita coisa, mas ainda não é “resolvido”. Kimi K2.7 Code ficou logo atrás, 86. Então a leitura não é “China dominou”. Não dominou. A leitura é: o gap fechou em qualidade, preço caiu, mas ainda são poucos modelos que aguentam agente real.

## Slide 39 - China ainda bloqueia o H200?
Restam: ~26:04 (15s)

E a geopolítica entrou de cabeça nessa corrida. Em maio, os Estados Unidos liberaram a venda de Nvidia H200 pra dez empresas chinesas. Pequim disse "não, usa o que tem em casa" — Huawei Ascend, Cambricon, Biren. Forçando o ecossistema doméstico a maturar. E enquanto isso, a Nvidia bateu 5 trilhões e meio de dólares de valor de mercado, maior que o PIB de qualquer país exceto Estados Unidos e China. A briga de compute não é mais só sobre quem tem mais GPU. É sobre quem controla o silício. Kimi, GLM e DeepSeek entram nessa mesma pressão: fazer mais coisa rodar no hardware que Pequim quer ver crescendo.

## Slide 40 - DGX Spark: appliance, não revolução
Restam: ~25:19 (45s)

Um exemplo bom dessa mudança de foco é o DGX Spark, que a NVIDIA tinha anunciado como Project DIGITS. O marketing é bonito: GB10 Grace Blackwell, 128 giga de memória unificada, até 1 PFLOP em FP4, até 4 tera de NVMe. Mas olhando frio, a CPU é Arm, co-design com MediaTek, e o número de AI TOPS fica perto de uma RTX 5070. O valor não é ser uma máquina revolucionária de treino frontier. É appliance local pra prototipar, ajustar e rodar inferência. Parece mais um smartphone Android bombado em formato de desktop do que uma nova era de compute.

## Slide 41 - Empresas e Profissionais ruins vão sair
Restam: ~24:19 (60s)

Aqui é a parte em que eu paro de fingir diplomacia. Empresas ruins e profissionais ruins vão sair, e isso melhora a indústria. Se você é o tipo que espera alguém te dizer o que fazer, você não sabe como pedir coisas pra IA. Porque pedir bem pra IA exige a mesma coisa que trabalhar bem: entender o problema, assumir responsabilidade e saber medir o resultado. A indústria passou anos premiando quem só esperava ordem. Essa época está acabando.

## Slide 42 - Fundamento primeiro
Restam: ~23:19 (60s)

É por isso que o Akita antigo continua valendo. Não terceirize sua decisão. Aprenda a aprender. Entenda que programação não é fácil. Essas ideias envelhecem bem porque não dependem de framework, nem de hype, nem de geração de modelo. Elas falam de formação mental.

## Slide 43 - Não terceirize seu julgamento
Restam: ~22:24 (55s)

O mais difícil de ensinar pra iniciante é isso: julgamento não é uma coisa que você baixa pronta. Não vem de influencer, não vem de bootcamp, não vem de modelo. O modelo mental continua o mesmo: experimento pequeno na beira do caos, erro cedo, retorno rápido, correção contínua.

## Slide 44 - Você não tem objetivos
Restam: ~21:24 (60s)

E aqui entra uma coisa que pouca gente quer admitir. Muita gente não tem problema de prompt. Tem problema de objetivo. A pessoa pede “melhora meu sistema”, “faz ficar profissional”, “resolve a performance”, mas não sabe dizer o estado atual, a restrição, nem a métrica de sucesso. E a pergunta incômoda é essa: você se acostumou a esperar alguém criar o backlog por você? A IA não adivinha isso. Se você não consegue transformar desejo em critério mensurável, você não sabe o que pedir. O agente fica rodando em cima de fumaça.

## Slide 45 - O sprint ideal
Restam: ~20:24 (60s)

O desenho ideal pra mim não é planning longo, backlog enorme e duas semanas tentando cumprir o combinado antigo. Com agente, eu prefiro ciclos muito mais curtos. Uma manhã de product manager com programador, para fechar objetivo, corte de escopo e critério. Uma tarde de QA com programador, para quebrar, validar e achar borda. Isso roda pela semana entre os programadores, cada um com LLM. O tech lead não vira gargalo de aprovação; entra nos pontos certos, quando precisa guiar arquitetura, refatoração ou decisão que custa caro depois.

## Slide 46 - Codar é Barato. Errar é Barato
Restam: ~19:24 (60s)

Esse é o outro efeito prático. Durante muito tempo, time evitou experimento porque codar era caro. Protótipo, prova de conceito, MVP pequeno, tudo competia com o backlog oficial. Com LLM, o custo de tentar cai. E quando o custo de tentar cai, o custo de errar também cai. A oportunidade é matar ideia ruim cedo, aprender com código rodando e seguir com mais confiança.

## Slide 47 - Agile Vibe Coding
Restam: ~17:54 (90s)

Eu uso o termo Agile Vibe Coding porque pega, mas faço questão de desmistificar na hora. A estrutura de verdade por baixo é velha. É Extreme Programming. O que mudou foi o par: agora meu par é uma máquina. O resto continua igual. Entrega pequena, retorno constante, teste, refatoração, atenção obsessiva em software funcionando. E aí eu quero atacar uma coisa que alguns jovens vivem reclamando. TDD, CI por commit, refatoração contínua. Isso não é perfumaria. TDD segura o modelo quando ele viaja, e ele viaja. CI por commit pega drift e regressão cedo, antes de virar uma dor de cabeça de duas horas. E sem refatoração contínua, o agente afunda num pântano de dívida técnica em poucos dias, e aí fica improdutivo. Com agente no meio, essas três coisas ficam mais importantes. Não menos.

## Slide 48 - O pareamento mudou
Restam: ~16:24 (90s)

O melhor corte de responsabilidade que eu encontrei foi esse: eu trago direção, julgamento, contexto e gosto. O agente traz velocidade de execução, busca e fôlego operacional. Se eu reduzo o agente a digitador burro, piora. Se eu entrego produto e arquitetura pra ele sozinho, piora também. A alavancagem está nessa divisão. É por isso que eu digo que IA é espelho: sênior bom ganha potência; programador ruim ganha potência pra fazer merda mais rápido.

## Slide 49 - Eu já tinha ensinado
Restam: ~15:39 (45s)

E isso não é papo que nasceu com IA. Eu já tinha ensinado isso antes. Agilidade de verdade, organização, gestão, modelagem. O problema não começou quando apareceu o Claude Code. O que a IA fez foi tirar a desculpa. Se você não sabe modelar, não sabe organizar trabalho, não sabe quebrar problema e não sabe dizer o que quer medir, o agente só acelera sua confusão. Agora fica mais visível. Só isso.

## Slide 50 - IA reflete quem você é
Restam: ~14:09 (90s)

E é aqui que isso volta pro código. IA não cria competência do nada. Ela reflete o que você já é. Se você é um bom engenheiro, ela vai te fazer produzir mais, mais rápido, com mais qualidade. Se você é um mau engenheiro, ela vai te ajudar a produzir lixo numa velocidade que você nunca conseguiria sozinho. Isso vale pra arte, vale pro código, vale pra qualquer área onde você tente usar IA como atalho pra substituir fundação. Não existe atalho pra competência.

## Slide 51 - Júnior herda. Sênior ensina.
Restam: ~12:29 (100s)

Júnior está preocupado, mas eu não acho que o caminho acabou. Acho que ele mudou de forma. O mundo está enchendo de sistema feito nas coxas, cheio de lixo de IA, e alguém vai ter que limpar isso. Aprender ferramenta nova nunca foi o fim da profissão: binário, cartão perfurado, assembly, linguagens mais altas, framework, nuvem, agora agente. Muita gente da minha geração aprendeu exatamente assim, no projeto real, bagunçado, cheio de cicatriz. Então a virada de esperança é essa: o caminho não sumiu, ele só ficou mais caótico. Mas isso só para em pé se sênior fizer o trabalho dele. Sênior não é imortal. Vai mudar de empresa, vai cansar, vai se aposentar. Se não formar substituto, a organização apodrece. A nova obrigação do sênior não é só usar IA bem. É ensinar engenharia com IA direito, antes do código apodrecer. Agente nenhum ensina julgamento.

## Slide 52 - Vai sobreviver quem souber fazer engenharia
Restam: ~10:54 (95s)

Então vem a parte dura. IA não transforma programador ruim em engenheiro. Ela ajuda programador ruim a fazer estrago maior mais rápido. E ajuda engenheiro de verdade a atravessar esse caos com mais velocidade, sem deixar o software morrer. Então eu fecho assim. Não vai sobreviver quem decorou truquezinho de prompt. Vai sobreviver quem tem fundamento, disciplina, iteração e gosto. Se você tem isso, IA vira multiplicador. Se não tem, IA é só uma forma mais rápida de ser exposto.

## Slide 53 - Assine The M.Akita Chronicles
Restam: ~10:29 (25s)

E já que é pra acabar sem falsa modéstia: se você curtiu essa palestra, assina o The M.Akita Chronicles. Está tudo aí na tela. É onde eu continuo publicando bastidor real, projeto real, código real e o que deu certo ou errado em produção. Quer acompanhar essa linha de raciocínio semana a semana? Vai em themakitachronicles.com e assina.

## Slide 54 - O canal também virou inglês
Restam: ~10:19 (10s)

E o Akitando também virou inglês: mais de 150 vídeos traduzidos e legendados com agente, além do blog bilingue com 20 anos de conteúdo. Se quiser mandar meu conteúdo pra alguém de fora do Brasil, começa por youtube.com/@Akitando.

## Slide 55 - Sim, este deck inteiro foi feito com IA
Restam: ~09:44 (35s)

E sim, já que o assunto da palestra é esse, vale fechar com o bastidor completo. Este deck inteiro também foi feito com IA. Pesquisa, estrutura, roteiro, notas do apresentador, crops, extração de frame, build, pós-processo do PPTX com vídeo, tudo saiu do mesmo fluxo. Agente no terminal, Marp para gerar o deck, scripts para embutir vídeo e iteração curta até o negócio ficar apresentável. Então não é discurso abstrato. Eu usei essa pilha para fazer a própria palestra que vocês acabaram de ver.

## Slide 56 - Obrigado
Restam: ~09:34 (10s)

Obrigado. Os links estão aí embaixo: Codeminer42, The M.Akita Chronicles e o repositório dessa palestra, que eu vou abrir no dia do evento.
