This project will be very long, so I need you to properly plan in advance, then move one step at a time, check, git commit, go the next step only when the previous is completed and validated.

I need you to first research the best/popular open source tool to declaratively build presentation slides, preferrably that I can later upload to google slides for easy deployment. it must support images, video playback, simple transitions, nothing fancy. I prefer my slides to follow The Art of Presentation Zen style, japanese style of very few text on slides, just highlights and images.

The event is called Tropical Ruby 2026 - a Ruby programming centric event, all the audience will be programmers or related, I will be the keynote presenter. The motivation is because of all my current research on Agile Vibe Coding. You must research the blog posts in ~/Projects/akitaonrails-hugo/ the posts from february forward tagged #vibecoding #agile #agents talking about my AI coding methodology and my marathon creating several sustainable projects, available in ~/Projects/frank* ../FrankMD ../mila-bot/ ../easy-* ../ai-jail/ 

I probably want to start with a super short introduction of my self. Codeminer 42 co-founder, current board of directors. Former RubyConf Brasil founder and organizer until 2016. Former Youtuber at @akitando channel with more than 500k followers. Former podcast guest at important podcasts such as Flow and Inteligência Ltda (ex https://www.youtube.com/watch?v=sf4Gxf0LiKo&pp=ygUQZmFiaW8gYWtpdGEgZmxvd9IHCQnZCgGHKiGM7w%3D%3D and https://www.youtube.com/watch?v=_Hl9wiLkns4&pp=ygUdZmFiaW8gYWtpdGEgaW50ZWxpZ2VuY2lhIGx0ZHPSBwkJ2QoBhyohjO8%3D and https://www.youtube.com/watch?v=9aWa-eCmWYE&t=1s&pp=ygUSZmFiaW8gYWtpdGEgdWxyaWNo0gcJCdkKAYcqIYzv). Then started researching and posting about AI coding since at least 2 years ago and culminating this year.

Most relevant recent posts: https://akitaonrails.com/2026/02/08/rant-ia-acabou-com-programadores/ and https://akitaonrails.com/2026/02/08/rant-ia-acabou-com-programadores/ and https://akitaonrails.com/2026/02/20/do-zero-a-pos-producao-em-1-semana-como-usar-ia-em-projetos-de-verdade-bastidores-do-the-m-akita-chronicles/ and https://akitaonrails.com/2026/02/24/rant-o-akita-abriu-as-pernas-pra-ia/ and https://akitaonrails.com/2026/03/05/37-dias-de-imers%c3%a3o-em-vibe-coding-conclus%c3%a3o-quanto-a-modelos-de-neg%c3%b3cio/. Study and pick the most relevant concepts.

I want to start next with a tangent about my hobby of watching VTuber drama, quickly explain how big is Hoyoverse or Nijisanji or VShojo. But particularly this one: https://www.youtube.com/watch?v=bokGdQOHGrw

It's about what many programmers fear: AI replacing their jobs. Same thing in the arts space: AI drawing better than human artists. Study this particular case: it's about an amateur artist that was fooling customers by delivering traced or even full AI art. Explain the techniques to fool such as making live streaming showing live drawing, but it's actually using a hidden layer with the image to trace, but it's in green so OBS or other capture programs can do the same thing as in a green screen transparency. It appears that the person is drawing from scratch, but she's actually tracing. Real artists can't be fooled because no real artist draw the final lines without making any mistakes, undoing and redoing many times.

Moreover, the style is inconsistent, she's unable to adjust the drawings to the customer's requests, so she invents excuses. Then finally she was exposed by another artist that let her know that she should improve her ways but she didn't.

Then segway to the recent Claude Code leaked code: https://akitaonrails.com/2026/03/31/codigo-fonte-do-claude-code-vazou-o-que-achamos-dentro/ and how absurdly spaghetti it was. And how people were able to quickly reverse engineer its secrets and even clean room reimplement into Free Code or Open Claw.

Now study a bit of the transcripts from the videos of my YouTube channel, such as: 
https://akitaonrails.com/2023/02/14/akitando-138-meu-comeco-de-carreira-durante-a-bolha-1997-a-2002-bug-do-milenio-crash/
https://akitaonrails.com/2022/11/22/akitando-132-rant-a-bolha-de-startups-estourou/
https://akitaonrails.com/2019/06/11/akitando-50-a-bolha-de-startups-vai-estourar-winter-is-coming/ 
https://akitaonrails.com/2020/03/24/akitando-75-o-que-vem-depois-do-covid-19/
https://akitaonrails.com/2020/04/01/akitando-76-guia-definitivo-de-aprendendo-a-aprender-a-maior-bronca-da-sua-vida-rated-r/
https://akitaonrails.com/2021/01/06/akitando-90-o-que-os-cursos-nao-te-ensinam-sobre-mercados/
https://akitaonrails.com/2019/10/23/akitando-65-a-dor-de-aprender-que-cursos-livros/ill doe
https://akitaonrails.com/2019/10/09/akitando-63-nao-terceirize-suas-decisoes-a-licao-mais-importante-da-sua-vida/
https://akitaonrails.com/2023/01/05/akitando-135-chatgpt-consegue-te-substituir-entendendo-jobs-assincronos/
https://akitaonrails.com/2022/05/30/akitando-119-rant-aprendizado-na-beira-do-caos-rated-r/

I started this youtube channel at the peak of the programming bubble, where everybody wanted to become a programmer like I explained here: https://akitaonrails.com/2020/02/19/akitando-72-rant-programacao-nao-e-facil/

It was against the trends of selling online courses, bootcamps, and promising easy employment in tech companies that were hiring like there was no tomorrow.

The bubble popped in 2022 and ChatGPT first debut around the same time, cementing the myth that "anyone can become a real software engineer with little effort"

Since then LLMs evolved fast. They will never be able to code perfectly, as I explained here: https://akitaonrails.com/2025/05/02/rant-llms-sao-loot-boxes/

But that's not a problem. The frontier models were smart enough to keep improving the tool support of those LLMs so they can be used as "agents". Claude Code, Codex and OpenCode are the culmination of the agents approach: the LLMs still can't program perfectly, but now they are able to autonomously execute the code they just edited, receiving instant feedback of the errors, and then being able to adjust, step by step, like a junior human programmer would do as well, using agentic web fetch to consult online sources, etc. 

The real turning point was at the end of 2025 (confirm) when Opus 4.5 and GPT 5.1 were released. They were good enough to finally be able to code competently using agentic engineering. Now we can really use it to write software that at least executes properly, instead of the LLM trying to guess everything in hopes that it would work.

End of January I started to pay more attention (read my articles about it as I stated before, the 37 days one. Here's where we quickly advance through all the projects I did, one by one, but without explaining any of them in detail as all of them are well documented in this blog and publicly available on github.

The whole point of this explanation is this climax:
- yes, AI will replace all the jobs taken by bad programmers, those that only joined because they thought they would amass a lot of money with little to no effort: but the bubble exploded already. The promises of those fraudulent courses and bootcamps were unfulfilled, they all closed shop and disappeared. Layoffs are continuing to this day (talk about Oracle's recent 30k layoff)
- AI is a reflection of its user: it augments what you are. If you are a great senior programmer, you will produce high quality code with AI. If you are one of those bad programmer, you will create bad code even faster. AI will not transform a bad coder in a real programmer.
- Same thing with the arts example: AI doesn't replace foundational knowledge and experience. Color Theory, composition, arts history influences, consistency, coherence, etc 
- My beef with the programming bubble that exploded in 2022 is that most companies were ignoring proper engineering in favor of just hiring more cheap programmers and just accumulating absurd ammounts of technical debt. 
- I, Fabio Akita, am very happy that the bubble exploded and that AI can now replace the bad programmers, because the real key to develop real working software with AI, fast, is by using the old, battle tested, original agile techniques, particularly extreme programming. Refer to my articles about agile vibe coding.

We can go a bit technical explaining the current state of the LLM ecosystem. Anthropic and OpenAI are the best frontier platforms. It's being followed by a few competitors such as GLM, MiniMax and Kimi. The open source models are not nearly on par with them. Deepseek made waves in the news a couple of years ago, but I think the open source models doesn't even have tool support. Alibaba's Qwen3 is old and weak, but it's still one of the best open source. But again, you won't have nearly the same performance as Opus 4.6 or GPT 5.4.

Price is a concern, research the current pro, max plans for claude. I consider them cheap. Yes, on preocupation is that anthropic is heavily subsidizing these plans. I hear that the most prolific developers would have to pay upwards of 10k a month if they were paying the full cost (research). But while it's the range of 200 USD/month per developer, it's a steal. 

From my own 500+ hours of marathon at this point I can attest I was able to produce sustainable projects in a velocity 5x to 10x my normal average. I could advance way faster because the LLMs were able to bypass most of the obstacles that would make me stop and procrastinate.

Junior developers are very worried because they won't be hired anymore. I say that nothing changed. We are now in an ocean of AI Slop. Even Claude Code, done by Anthropic itself, when leaked, it's a mess of unsustainable spaghetti code. Like them, all other companies are just running fast, still ignoring proper engineering methodologies. So all of them are spaghetti. The juniors will have to learn how to start fixing all of those problems. That's how they will learn: in a small company, where the CEO tried to vibe code, and deployed a horrendous code base. Now someone needs to fix it, but he can't afford a senior developer, that's where juniors will have to start learning by experience, in a real messy project. That's how I started in my old days. 

Seniors must start teaching the juniors how to do proper engineering with the AI to avoid all that AI Slop. Seniors can now produce 5x to 10x, but they are not immortal. Seniors will change companies. Seniors will retire. Someone will have to replace them: that's the juniors they trained. In house training is the best investment for a sustainable tech business.

And now all the bad programmers will leave the industry. So only the real engineers, those who properly studied the foundations, and actually have what it takes to spend days, methodically resolving AI Slop, will survive and thrive. This is the conclusion.

---


Whenever citing my old videos (try to do that), illustrate the slides with the youtube video thumbnails. Whenever citing websites, add screenshots of those pages in the slides. You can make many slides as the intention is that I will go through them quickly, as highlights to the talk points. When presenting my frank* projects, use the images in the readme pages to illustrate. Make bold texts, short texts, easy to read, zen slides.

Also write down a full script of the presentation that matches those slides.

---

Important additions after the iterative process:

- the whole thing must be in pt-BR, slides and script. use my voice from the posts, not corporate voice, not translator voice, not conference organizer voice. it must sound like me talking on stage.
- whenever changing or adding text, run a humanizer pass. I don't want llm-sounding symmetry, fake elegance, or polished corporate filler.
- keep slides, full script and presenter notes synchronized all the time. presenter notes must be short, bullet-like, stage cues, not a second manuscript.
- presenter notes must stay shorter than the script and more focused. if slides move, script and notes must move together.

Narratively I want this to work as a proper 3-act story:
- first act: the panic is misdiagnosed
- second act: what actually changed in late 2025 / early 2026 and the proof from my marathon
- third act: what this means for engineers, juniors, seniors and the software market

In practice:
- the intro must open with the thesis directly
- then connect to my older warnings from previous years
- then use the vtuber / art fraud tangent and the claude code leak as examples of fake-looking process versus real work
- the practical proof of the marathon results must land before the explanation of the mechanism
- only after the audience buys the proof do we explain why it worked: tools, thinking, loops, xp, tdd, ci, refactoring, judgment

The asamiarts section needs to be more complete than what I first described:
- show an actual tracing clip so the audience sees what "too clean" looks like
- show the hidden layer clip so I can explain the likely green background / filtered layer trick
- show the inconsistent style evolution across a short amount of time
- show the hallucination example with the gun / barrel on the wrong side
- show the style stealing / lora example
- briefly explain what a lora is: a lightweight fine-tuning / adapter on top of a base model to push it toward a specific style or artist
- the point is not gossip, it is to show how people who don't understand the craft get fooled by fake process

The claude code / agents section also needs explicit timeline context:
- briefly explain who started the tool support / agentic evolution
- mention the important milestones that make 2025 the pivotal year
- explain that the big turning point was not that the models became perfect coders
- the big turning point was model + tool support + execution loop + feedback loop + cli tools becoming good enough together
- connect this to claude code, codex, opencode, mcp, responses api, structured tool support, computer use, etc when relevant
- make it clear that by december 2025 serious experimentation started accelerating, and that is why january 2026 triggered me to do the same

It is important to briefly explain the current state of llms:
- they still bajulate the user
- they still make mistakes confidently
- they still hallucinate
- they are still probabilistic loot boxes, never deterministic like a compiler
- but with tools and execution they became useful enough

Also explain briefly what "thinking" / reasoning means in this context:
- it is not magic, it is extra inference budget to consider intermediate steps before acting
- it is useful for tool calling because the model needs to decide if it should use a tool, which tool, in what order, with what arguments, and whether the result was enough or it needs another step
- this is why better thinking + better tool support matters for agents

On the engineering proof side, the metrics section must be stricter:
- count all the projects mentioned in the beginning, not just whatever appears in the thumbnail grid
- calculate total lines of code
- calculate total test lines of code
- total commits
- estimated active hours
- document the counting methodology so the slide does not get questioned easily
- make clear when some repo enters code volume but not commit count because it was not in a closed git repo

Also normalize the calendar honestly:
- make explicit that my marathon was 45 days, but almost 16h every day, 7 days a week
- estimate the equivalent for a normal senior working business hours only, no more than 8h a day, 5 days a week
- then estimate the same senior without AI, using the 5x to 10x slower rough range
- separate days corridos from dias uteis correctly
- this should probably be its own slide, not hidden inside another one

The xp / agile vibe coding part needs to be stronger:
- explain a bit more why xp matters specifically with agents
- tdd is not decoration, it is the guard rail when the model is wrong
- ci is not hygiene theater, it is how you catch drift and regressions immediately
- refactoring is not cleanup later, it is what keeps the code base and the agent productive over time
- reinforce the comparison between FrankMD and The M.Akita Chronicles: same developer, same agent, different process, very different sustainability and velocity

On ecosystem / market positioning:
- explain that frontier closed models are still ahead in the full coding-agent workflow
- open source is useful, but still behind in the complete tool loop
- mention the clean room reactions after the claude code leak, such as free-code / openclaw style reactions
- explain that trivial software got absurdly cheap
- add current claude pricing context, because I still think 20 / 100 / 200 USD is cheap for the leverage

Add a near-end slide about speculation on the AI economy:
- recent data center investment
- energy consumption growth
- local grid bottlenecks / energy shortage risks
- the fact that training and inference compete for finite compute, capital and electricity
- the s-curve of giant raw model improvements approaching more diminishing returns
- my speculation is that frontier labs will have to spend more effort on efficiency, inference capacity, serving, tool support and productization, not only on giant new training runs
- mention the pressure that an anthropic ipo in 2026 would add to this logic, but phrase it as speculation, not as a confirmed fact

Visually:
- use thumbnails from my old youtube videos when citing old arguments
- use screenshots from websites / articles when relevant
- use local extracted frames and clips when useful
- don't overdo visuals, but don't leave long runs of boring white slides either
- if a visual is vertical, compose the slide around that instead of forcing a bad crop
- if marp pptx cannot embed video directly, automate a post-process step to inject mp4s into the final pptx

Delivery / closing:
- after the engineering conclusion, I want a shameless ad slide for The M.Akita Chronicles
- then I want a slide exposing that the whole slide deck itself was made with AI, including highlights of the tools and processes used
- then the final slide must be a big OBRIGADO in the center, with urls at the bottom for codeminer42.com, themakitachronicles.com and the github repo of the talk

Finally:
- validate html, pdf and pptx, not just one output
- pdf may break layouts that look fine in html, so always test
- commit only after each meaningful validated milestone
- document the workflow and constraints in readme / claude.md so future iterations don't drift
