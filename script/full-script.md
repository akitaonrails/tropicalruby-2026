# Tropical Ruby 2026 - Full Script

This script follows the tightened deck in `slides/tropical-ruby-2026.md`.

## Slide 1 - Agile Vibe Coding

I want to start with the thesis, because everything else in this talk exists to support it. AI is replacing people in software, yes. But not in the simplistic way panic merchants describe. What AI replaces first is fake productivity, fake seniority, and the weak engineering that survived only because the market tolerated waste. Engineering itself is not going away. Engineering matters more now.

## Slide 2 - Fabio Akita

For people who only know me from one corner of the internet: I co-founded Codeminer 42 and now sit on its board. I founded and organized RubyConf Brasil until 2016. I spent years on YouTube with Akitando, and I also crossed into a more mainstream audience through shows like Flow and Inteligência Ltda. I say this only to establish that I have spent a long time watching how markets, narratives, and technology waves distort people’s expectations.

## Slide 3 - The AI panic arrived on top of an old bubble

I do not want anyone thinking I only started saying this after AI became fashionable. I was already arguing that the software market had become inflated, distorted, and full of false promises before coding agents became useful. AI did not invent the weakness. It only exposed it faster.

## Slide 4 - Same thesis. New tools.

There is a straight line here. In 2019 I was warning about startup winter. In 2020 I repeated that programming is not easy. In 2022 the bubble popped for real. In 2025 I argued that LLMs are loot boxes, meaning probabilistic systems with hard limits. In late 2025 and early 2026, agents finally became competent enough to matter in day-to-day work. The tools changed. The core argument did not.

## Slide 5 - The old lie

The old lie was simple: become a software engineer in a few weeks, get a huge salary, and enjoy easy money forever. That was always nonsense. A bootcamp can teach a tool. It cannot compress years of engineering judgment into a few months. The market temporarily paid as if it could. Reality corrected that fantasy. The bubble started cracking in late 2022, before AI coding was mature enough to take the blame.

## Slide 6 - Same fear

To explain the current panic, I want a detour into another world I follow as a hobby: VTuber and art drama. The emotional pattern is identical. In the art world, people say AI will replace artists. In programming, people say AI will replace programmers. In both cases, the loudest panic usually comes from a shallow understanding of craft.

## Slide 7 - AsamiArts

The specific case is the video about AsamiArts. The gossip itself is not the important part. The important part is the deception pattern. Surface-level observers can be fooled by output that looks smooth and convincing even when the process behind it is fake. If there is hidden tracing, hidden scaffolding, and staged performance, people who only look at the final output get tricked.

## Slide 8 - Real craft looks messy

That maps directly to software. Real craft looks messy. Real artists revise, hesitate, adapt, and correct. Real engineers do the same. The point is not elegance at first output. The point is whether the work survives revision, change requests, new constraints, and contact with reality. AI does not change this. It amplifies it.

## Slide 9 - Claude Code leaked

Then came one of the funniest confirmations of this thesis: the March 31, 2026 Claude Code leak. The official Anthropic coding tool exposed a huge source map, and suddenly everybody could inspect the internals of one of the most influential coding-agent products on the market.

## Slide 10 - The lesson was not “wow, magic”

And what did people find? Not divine perfection. Not magic. They found a large, revenue-generating, pressure-shaped production codebase with complexity, tactical compromises, and what the internet immediately called staff-engineer spaghetti. Then people started reverse engineering pieces and reimplementing behavior almost immediately. That is the point: once the mystique disappears, what remains is engineering.

## Slide 11 - AI did not remove engineering

So my central point is simple. AI did not remove the need for engineering. It removed excuses. It exposed the gap between people who know how systems survive in production and people who only know how to produce plausible-looking output.

## Slide 12 - LLMs are loot boxes

I called LLMs loot boxes because they are probabilistic. They are not deterministic compilers. They do not guarantee correctness. You can improve your odds with context, tools, evaluation loops, and better prompts, but you are still operating on probabilities. That is exactly why foundation matters. Somebody still has to judge the result.

## Slide 13 - One-shot prompt is for demos

The one-shot prompt fantasy is intellectually lazy. It assumes you can describe everything relevant up front. Real software does not work like that. Production reveals things you did not know mattered. APIs behave badly. Infrastructure fails in annoying ways. User behavior mutates requirements. That is why one-shot prompt is for demos and iteration is for production.

## Slide 14 - Late 2025 mattered

Now, to be fair, something really did change. OpenAI released GPT-5.1 for developers on November 13, 2025. Anthropic released Claude Opus 4.5 on November 24, 2025. That period matters because the models finally became good enough in tool-using, agentic workflows to stop being mostly annoying and start being consistently useful.

## Slide 15 - The agent loop

And notice what the useful loop actually is: plan, search, edit, run, check, repeat. That is not mystical. It is engineering feedback compression. The agent is fast at operating the loop. It is not automatically wise about which loop matters.

## Slide 16 - Foundations first

This is why my old channel themes still apply. Don’t outsource your decisions. Learn how to learn. Understand that programming is not easy. Those lessons age well because they were never tied to one framework or one hype cycle. They are about how adults build durable judgment.

## Slide 17 - Don’t outsource judgment

The hardest thing to teach beginners is that judgment is not a downloadable asset. Not from influencers, not from bootcamps, and not from a model. The right mental model is still controlled experimentation at the edge of chaos: small experiments, fast correction, repeated learning.

## Slide 18 - February and March 2026

So instead of staying in the abstract, I spent February and March actually marathoning with these tools. Not toy prompts. Not fake SaaS demos. Real projects, real deploys, real tests, real bugs, real post-production.

## Slide 19 - From zero to real software

This is the fast project wall. FrankMD, FrankMega, Frank Sherlock, Frank Yomik, Frank FBI, and others. The point is not to explain each repo in detail. The point is to show volume plus variety across desktop, Rails, Rust, media pipelines, and production software.

## Slide 20 - What I actually got

From my own usage, the realistic headline is 5x to 10x velocity. Not because the models write perfect code. They absolutely do not. The gain came because they helped me get through the friction points that usually fragment focus: boilerplate, search, repetitive tests, refactors, command execution, and quick experimentation. The trust only came because the work still had tests, CI, refactoring, and production use behind it.

## Slide 21 - Agile Vibe Coding

This is why I call it Agile Vibe Coding, but I also insist on demystifying the term. The real structure underneath is old. It is Extreme Programming. Pair programming changed because my pair is now a machine. The core loop is still small releases, constant feedback, tests, refactoring, and attention on working software.

## Slide 22 - Pair programming changed

The cleanest division of labor I found is this: I bring judgment, direction, constraints, and taste. The agent brings typing speed, search stamina, and execution throughput. If I force the agent to be a dumb typist, it gets worse. If I let it decide product and architecture alone, it also gets worse. The leverage is in the split. That is why AI is a mirror: great seniors get amplified, bad coders get amplified too, just in the wrong direction.

## Slide 23 - Frontier closed models lead

On the model landscape as of April 1, 2026, my practical view is simple. Anthropic and OpenAI remain the two frontier platforms that matter most for serious coding work. Others like GLM, MiniMax, and Kimi are relevant followers. Open-source models are useful, but they are still not matching the best closed models in the full agentic workflow.

## Slide 24 - Open source is useful

That does not mean open source is worthless. It means expectations need calibration. You can do real things with open models, but if you want the best current coding-agent behavior, the frontier closed models are still ahead. And on pricing, Claude Pro at 20 dollars a month, and Max at 100 or 200, is still cheap compared to senior-developer leverage.

## Slide 25 - The correction

This is the part where I stop pretending to be diplomatic. I am actually happy the bad-programmer bubble is dying. The industry spent years substituting engineering discipline with cheap labor and accumulating technical debt as if it were free. AI is forcing a correction. Good.

## Slide 26 - Juniors are not dead

Juniors are worried, but I do not think the path disappeared. I think it changed shape. The world is now filling up with AI-slop systems rushed by founders and teams that skipped discipline. Somebody will need to clean that up. That is how many of us learned in the first place: on real, messy systems.

## Slide 27 - Seniors have a new duty

But this only works if seniors do their job. Seniors are not immortal. They move, burn out, retire, and change companies. If they do not train replacements, the organization becomes fragile. So the new responsibility is not only using AI well. It is teaching engineering with AI well. And the market is still correcting now, with April 1, 2026 reports describing another major Oracle layoff wave.

## Slide 28 - AI will not transform a bad coder into an engineer

So the closing argument is simple. AI will not transform a bad coder into an engineer. It will help a bad coder make bigger messes faster. It will help a real engineer move faster through the mess while keeping software alive.

## Slide 29 - The survivors will be the ones who can engineer

That is my conclusion for Tropical Ruby 2026. The survivors are not the people with the best prompt tricks. The survivors are the people with foundations, discipline, iteration habits, and taste. If you have that, AI is a force multiplier. If you do not, AI is a faster path to exposure.
