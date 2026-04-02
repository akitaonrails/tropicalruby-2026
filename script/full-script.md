# Tropical Ruby 2026 - Full Script

This script follows the deck in `slides/tropical-ruby-2026.md`.

## Slide 1 - Agile Vibe Coding

I want to start with the thesis, because everything else in this talk exists to support it. AI is absolutely replacing people in software. But not in the simplistic way the panic merchants describe. What AI is replacing first is fake productivity, fake seniority, and the whole market distortion that let weak engineering survive by just adding more cheap hands. Engineering itself is not going away. If anything, engineering matters more now.

## Slide 2 - Fabio Akita

Very quickly, for the people who only know me from one corner of the internet: I co-founded Codeminer 42 and now sit on its board. I founded and organized RubyConf Brasil until 2016. I spent years on YouTube with Akitando, and I’ve also crossed into a more mainstream audience through shows like Flow and Inteligência Ltda. I’m saying this only to make one point: I’ve spent a long time watching markets, technology waves, and how narratives fool people.

## Slide 3 - I was already arguing against the bubble before LLMs

This is important because I don’t want anyone thinking I only started saying this after AI became fashionable. I was already arguing that the software market had become inflated, distorted, and full of false promises before coding agents became usable. AI did not invent the weakness. AI only exposed it faster.

## Slide 4 - 2019 to 2026

There is a straight line here. In 2019 I was already warning about startup winter. In 2020 I was repeating that programming is not easy. In 2022 the startup bubble popped for real. In 2025 I argued that LLMs are loot boxes, meaning probabilistic systems with real limits. And in late 2025 and early 2026, agents finally became competent enough to matter in day-to-day software work. So the story is consistent. The tools changed. The underlying argument did not.

## Slide 5 - The bubble already cracked

The bubble burst before AI coding became mature. That matters. The mass layoffs started in late 2022. ChatGPT showed up in the same era, but it was not the sole cause. It was the accelerant on a system that was already unstable. A lot of weak companies were already over-hiring weak developers to feed growth theater.

## Slide 6 - The old lie

The old lie was simple: become a software engineer in a few weeks, get a huge salary, and enjoy easy money forever. That was always nonsense. A bootcamp can teach a tool. It cannot compress years of engineering judgment into a few months. The market temporarily paid as if it could. Reality corrected that fantasy.

## Slide 7 - The fear is the same

To explain the current panic, I want to take a small detour into another world I follow as a hobby: VTuber and art drama. The emotional pattern is identical. In the art world, people say AI will replace artists. In programming, people say AI will replace programmers. In both cases, the people who panic the most usually have a shallow definition of craft.

## Slide 8 - AsamiArts

The specific case I want to cite is the video “How a New AI Art Method Managed to Trick Over 100k People - The Unprecedented Case of AsamiArts.” The point is not the gossip. The point is the mechanism of deception. Surface-level observers can be fooled by output that looks smooth and convincing, even when the process behind it is fake.

## Slide 9 - Fraud looks smooth

The accusation in that case is interesting because it maps directly to bad AI programming. Fake live drawing can look very clean. No hesitation. No visible struggle. No iteration. Hidden tracing or hidden support layers can make it appear as if the artist is creating from scratch. Customers who don’t understand the process get fooled because they evaluate the performance, not the craft.

## Slide 10 - Real craft looks messy

Real artists know the process is messy. There are revisions, corrections, composition problems, consistency problems, and client-driven changes. The same is true in software. Real engineering is not a single elegant output. It is a chain of constrained decisions, tradeoffs, fixes, tests, reversions, and cleanup. If your process looks magically effortless, I immediately become suspicious.

## Slide 11 - AI exposes whether there was real craft underneath

That is the bridge back to programming. AI acts like an amplifier. If there was real craft underneath, AI multiplies it. If there was only surface imitation, AI also multiplies that. So the tool is not the real story. The operator is.

## Slide 12 - Claude Code leaked

Then came one of the funniest possible confirmations of this thesis: the March 31, 2026 Claude Code leak. The official Anthropic coding tool accidentally exposed a huge source map. Suddenly everybody could look at the internals of one of the most influential coding-agent products on the market.

## Slide 13 - Even Anthropic ships spaghetti under pressure

And what did people find? Not divine perfection. Not some magical architecture from the heavens. They found a big, revenue-generating, pressure-shaped production codebase with lots of feature flags, hidden paths, tactical complexity, and what the internet immediately called staff-engineer spaghetti. That description is funny because it is accurate. This is what high-pressure shipping often looks like.

## Slide 14 - Reverse engineered in hours

And because the implementation was visible, people immediately started analyzing it, bypassing pieces, and reimplementing the behavior. That is also the point. Once the mystique disappears, what remains is engineering. Architecture, constraints, protocol behavior, operational shortcuts, tradeoffs. No magic. Just work.

## Slide 15 - AI did not remove engineering

So my central point is that AI did not remove the need for engineering. It removed excuses. It exposed the gap between people who actually know how systems survive contact with production and people who only know how to produce plausible-looking output.

## Slide 16 - LLMs are loot boxes

I called LLMs loot boxes because they are probabilistic. They are not deterministic compilers. They do not guarantee correctness. You can improve your odds with context, tools, evaluation loops, and better prompts, but you are still operating on probabilities. That is exactly why foundation matters: you need someone who can judge the result.

## Slide 17 - One-shot prompt is for demos

The one-shot prompt fantasy is intellectually lazy. It assumes you can describe everything relevant up front. Real software does not work like that. Production reveals things you did not know mattered. Users behave differently. APIs are weird. Infrastructure fails in the wrong way. Requirements mutate. That is why one-shot prompt is for demos and iteration is for production.

## Slide 18 - “Done” is a lie

One of the clearest things from my 2026 posts is that “done” is basically a lie. I had 125 post-production commits across four projects. The M.Akita Chronicles alone kept evolving after launch. This is normal. Software that goes live and then stops changing is usually either dead or abandoned. Useful software keeps forcing new decisions.

## Slide 19 - Late 2025 mattered

Now, to be fair, something really did change. Late 2025 was a turning point. OpenAI released GPT-5.1 for developers on November 13, 2025. Anthropic released Claude Opus 4.5 on November 24, 2025. That period matters because the models finally became good enough in tool-using, agentic workflows to stop being mostly annoying and start being consistently useful.

## Slide 20 - Why not before?

Earlier models could already help, but they lost context too easily, hallucinated too aggressively, got stuck in loops too often, and required too much babysitting. The newer generation became better at running the loop: inspect, search, edit, run, fail, and correct. That is the threshold that changed my day-to-day behavior.

## Slide 21 - The agent loop

And notice what that loop looks like. It looks familiar. Plan. Search. Edit. Run. Check. Repeat. That is not mystical. It is just engineering feedback compression. The agent is fast at operating the loop. It is not inherently wise about which loop matters.

## Slide 22 - Foundations first

This is why my old channel themes still apply. Don’t outsource your decisions. Learn how to learn. Understand that programming is not easy. Work at the edge of chaos, meaning with controlled experimentation and disciplined correction. Those lessons age well because they were never tied to one framework or one era.

## Slide 23 - Don’t outsource judgment

The hardest thing to teach beginners is that judgment is not a downloadable asset. Not from an influencer, not from a bootcamp, and not from a model. Tools can compress labor. They do not compress maturity at the same rate.

## Slide 24 - Learn at the edge of chaos

My “edge of chaos” argument is especially relevant now. Too much rigidity and you stop adapting. Too much chaos and you become noise. The useful zone is iterative movement: small experiments, fast correction, and accumulation of insight. That is basically how good AI-assisted engineering works.

## Slide 25 - February and March 2026

So instead of talking in the abstract, I spent February and March actually marathoning with these tools. Not with toy prompts. Not with fake SaaS videos. With real projects, real deploys, real tests, real bugs, real post-production.

## Slide 26 - Project wall

This is the part where I flash through the projects quickly. FrankMD, FrankMega, Frank Sherlock, Frank Yomik, Frank FBI, and others. The point here is not to explain every repo in detail. The point is to show volume plus variety. Desktop app, Rails app, Rust app, language tooling, media pipelines, production systems.

## Slide 27 - What I actually got

From my own usage, the realistic headline is 5x to 10x velocity. Not because the models write perfect code. They absolutely do not. The gain came because they helped me break through the little friction points that normally fragment focus: boilerplate, search, refactors, repetitive tests, cross-checking, command execution, quick experimentation.

## Slide 28 - The secret is boring

And what allowed that speed to become sustainable? Boring things. Tests. Refactoring. CI. Deployment. Prompt tuning. Production observation. In other words, the part the hype videos never show. If you skip that part, you can indeed generate a lot of output very quickly. What you cannot generate is trust.

## Slide 29 - Agile Vibe Coding is just XP with a machine pair

This is why I call it Agile Vibe Coding, but I also insist on demystifying the term. The real structure underneath is old. It is Extreme Programming. Pair programming changed because my pair is now a machine. But the core loop is still small releases, constant feedback, tests, refactoring, and shared attention on working software.

## Slide 30 - Pair programming changed

The cleanest division of labor I found is this: I bring judgment, direction, domain experience, and taste. The agent brings typing speed, search stamina, and execution throughput. If I force the agent to just obey exact keystroke-level instructions, it becomes worse. If I let it decide the product or architecture alone, it also becomes worse. The leverage is in the split.

## Slide 31 - AI is a mirror

That is why I say AI is a mirror. Great seniors get amplified. Weak coders get amplified too, but in the direction of faster bad decisions. AI does not launder poor thinking into good engineering.

## Slide 32 - Frontier closed models lead

On the model landscape as of April 1, 2026, my practical view is simple. Anthropic and OpenAI remain the two frontier platforms that matter most for serious coding work. Others like GLM, MiniMax, and Kimi are relevant followers. Open-source models are useful, but they are still not matching the best closed models in the full agentic coding workflow.

## Slide 33 - Open source is useful but not yet frontier

That does not mean open source is worthless. It means expectations need calibration. You can do real things with open models. But if you want the best current coding-agent behavior, especially around tools and long task execution, the frontier closed models are still ahead.

## Slide 34 - Claude pricing

This is where the economics become obvious. Claude Pro has been priced at 20 dollars a month. The current Max tiers are 100 and 200 dollars a month. At senior-developer leverage, that is extremely cheap. I understand the suspicion that this kind of usage is subsidized. I would not be surprised. But from the buyer’s perspective, at that price, the leverage is absurd.

## Slide 35 - Bad programmers will leave

This is the part where I stop pretending to be diplomatic. I am actually happy the bad-programmer bubble is dying. The industry spent years substituting engineering discipline with cheap labor and accumulating technical debt as if it were free. AI is forcing a correction. Good.

## Slide 36 - Juniors are not dead

Juniors are worried, but I don’t think the path disappeared. I think it changed shape. The world is now filling up with AI-slop systems, rushed by founders and teams that skipped engineering discipline. Somebody will need to clean that up. That is how many of us learned in the first place: in messy real systems.

## Slide 37 - Seniors have a new duty

But this only works if seniors do their job. Seniors are not immortal. They move, they burn out, they retire. If they do not train replacements, the organization becomes fragile. So the new responsibility is not only using AI well. It is teaching engineering with AI well.

## Slide 38 - Oracle and the continuing correction

And the market correction is still happening right now. On April 1, 2026, new reports described another large Oracle layoff wave. Whether the exact final count settles at 30,000 or not, the direction is clear: the market is still shedding the fantasy headcount era. We are not going back to 2021.

## Slide 39 - AI will not transform a bad coder into an engineer

So the closing argument is simple. AI will not transform a bad coder into an engineer. It will help a bad coder make bigger messes faster. It will help a real engineer move faster through the mess while keeping software alive.

## Slide 40 - The survivors will be the ones who can engineer

That is my conclusion for Tropical Ruby 2026. The survivors are not the people with the best prompt tricks. The survivors are the people with foundations, discipline, iteration habits, and taste. If you have that, AI is a force multiplier. If you do not, AI is just a faster path to exposure.
