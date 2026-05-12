# AI Agents Evolution: 2025 Timeline and Milestones

Research compiled April 13, 2026. Intended as fact-check reference for the Tropical Ruby 2026 keynote slides "2025 foi o ano dos Agentes" and "Dezembro de 2025 foi a Virada." Dates sourced from official announcements, Wikipedia, and tech press. Where a precise date is uncertain, the qualifier "(approx.)" is used.

---

## 1. Key Model Releases

### Pre-2025 foundation (late 2023 -- 2024)

- **2024-03-04** -- Anthropic releases the **Claude 3 family**: Haiku, Sonnet, and Opus. First family with vision capabilities and the Opus/Sonnet/Haiku naming convention.
- **2024-05-13** -- OpenAI releases **GPT-4o** ("omni"), a natively multimodal model with text, vision, and audio in a single architecture. Significant speed and cost improvement over GPT-4 Turbo.
- **2024-06-20** -- Anthropic releases **Claude 3.5 Sonnet**. Mid-tier model that outperformed the flagship Opus 3 on most benchmarks. An upgraded version ships **2024-10-22** alongside Claude 3.5 Haiku.
- **2024-09-12** -- OpenAI releases **o1-preview and o1-mini**, the first "reasoning" models trained with RL to generate internal chain-of-thought before answering. Available to ChatGPT Plus and Team users. Full o1 release: **2024-12-05**.
- **2024-12-20** -- OpenAI announces **o3** (successor to o1); available to researchers only until late January 2025.
- **2024-12-26 (approx.)** -- DeepSeek releases **DeepSeek-V3** (base and chat), a 671B MoE model trained on 14.8T tokens for reportedly under $6M in compute. Open-weight.

### 2025 Q1

- **2025-01-20** -- DeepSeek releases **DeepSeek-R1**, an open-weight reasoning model. Surpasses ChatGPT as most-downloaded iOS app in the US by Jan 27. Major shock to the industry on cost and open-source viability.
- **2025-01-31** -- OpenAI releases **o3-mini** (low/medium/high variants). First broadly available o3-series model.
- **2025-02-24** -- Anthropic releases **Claude 3.7 Sonnet**, the first "hybrid reasoning" model: standard mode and extended thinking mode in the same model. New SWE-bench Verified highs for Anthropic.
- **2025-02-27** -- OpenAI releases **GPT-4.5** ("Orion") as a research preview. Largest GPT model to date. $75/$150 per million tokens. Available to Pro users and developers.

### 2025 Q2

- **2025-04-05** -- Meta releases **Llama 4** family (Scout, Maverick; Behemoth still in training). First Llama generation with MoE architecture. Scout has a 10M-token context window.
- **2025-04-14** -- OpenAI releases **GPT-4.1**, GPT-4.1 mini, and GPT-4.1 nano. 1M-token context. 54.6% on SWE-bench Verified.
- **2025-04-16** -- OpenAI releases **o3** (general availability) alongside **o4-mini**. Most advanced reasoning models to date.
- **2025-04-29** -- Alibaba releases **Qwen 3** family (dense models: 0.6B--32B; MoE models: 30B-A3B and 235B-A22B). Trained on 36T tokens, 2x Qwen 2.5. Hybrid reasoning (thinking/non-thinking modes).
- **2025-05-06** -- Google releases **Gemini 2.5 Pro Preview** (I/O edition) with improved coding. Experimental version had appeared **2025-03-25**. GA on **2025-06-17**.
- **2025-05-22** -- Anthropic releases **Claude Opus 4** and **Claude Sonnet 4**. Opus 4 described as "the world's best coding model." Extended thinking with tool use (beta). 200K context. Interleaved thinking between tool calls.

### 2025 Q3

- **2025-08-05** -- Anthropic releases **Claude Opus 4.1**. Incremental improvements in software engineering and agentic reasoning over Opus 4.
- **2025-08-07** -- OpenAI releases **GPT-5**. Unified system with instant + thinking modes and an automatic router. 400K context. 74.9% on SWE-bench Verified. $1.25/$10 per million tokens (half the input cost of GPT-4o). Three API sizes: gpt-5, gpt-5-mini, gpt-5-nano. ~45% fewer hallucinations than GPT-4o; ~80% fewer with thinking enabled.

### 2025 Q4

- **2025-09-29** -- Anthropic releases **Claude Sonnet 4.5**. Major coding and agentic upgrade. Ships with Claude Code checkpoints, refreshed terminal UI, and native VS Code extension.
- **2025-10-15** -- Anthropic releases **Claude Haiku 4.5**. Fast, cheap model for agent sub-tasks and high-throughput use.
- **2025-11-12** -- OpenAI releases **GPT-5.1** (Instant and Thinking variants). Adaptive reasoning: model decides when to think. Customizable personalities. Improved instruction-following and coding. Two more variants ship **2025-11-19**.
- **2025-11-24** -- Anthropic releases **Claude Opus 4.5**. "Best model in the world for coding, agents, and computer use." 96.1% SWE-bench, 95.5% Terminal-bench. $5/$25 per million tokens. Automatic conversation summarization for long sessions. Available in Claude Chat, Claude Code, API, Bedrock, Vertex AI, Azure Foundry.

### Post-2025 (context)

- **2026-02-05** -- Claude Opus 4.6 released. Agent teams, Claude in PowerPoint.
- **2026-02-17** -- Claude Sonnet 4.6 released. Adaptive thinking, interleaved thinking auto-enabled.
- GPT-5.2, GPT-5.4 follow in early 2026. GPT 5.4 is the current OpenAI flagship for coding (as of April 2026).

---

## 2. Coding Agent Tool Milestones

### Precursors (2023--2024)

- **2023-03** -- GitHub Copilot Chat launches in VS Code (preview). Chat-based code assistance on top of the existing inline completions (launched 2021/2022).
- **2023-07 (approx.)** -- **Aider** (Paul Gauthier) first released. Open-source terminal-based AI pair programmer with Git integration. Supports multi-model via LiteLLM.
- **2024-03-12** -- **Devin** (Cognition Labs) announced. Marketed as "first fully autonomous AI software engineer." 13.86% on SWE-bench (previous SOTA was 1.96%). Goes viral. Skepticism follows about real-world reliability.
- **2024-04** -- GitHub launches **Copilot Workspace** technical preview (issue-to-PR agent workflow).
- **2024-08** -- **Cursor** (Anysphere) raises $60M Series A (a16z). Introduces Composer mode for multi-file editing. Crosses 100K users.
- **2024-11 (approx.)** -- Codeium launches **Windsurf Editor**, an AI-native IDE (VS Code fork) with its "Cascade" agent system for deep codebase-aware editing.
- **2024-12** -- Cursor raises $105M Series B at $2.6B valuation (Thrive Capital). Fastest SaaS to $100M ARR (12 months). End of 2024, Cursor is the dominant AI coding editor.
- **2024-12-10** -- **Devin** reaches general availability at $500/month.

### 2025

- **2025-02-24** -- Anthropic launches **Claude Code** as a limited research preview. Terminal-based agentic coding tool: reads code, edits files, runs tests, commits to Git. Ships alongside Claude 3.7 Sonnet.
- **2025-02-06** -- GitHub announces **Copilot Agent Mode** (preview) in VS Code: Copilot iterates on its own output, runs terminal commands, auto-fixes errors.
- **2025-04-05 (approx.)** -- Cognition launches **Devin 2.0**, drops price from $500/month to $20/month.
- **2025-04-16** -- OpenAI launches **Codex CLI**, open-source terminal coding agent. Written in Rust. Runs locally. Supports macOS and Linux.
- **2025-05-19** -- GitHub announces **Copilot Coding Agent** (public preview at Build). Asynchronous agent that picks up GitHub issues, creates branches, writes code, opens PRs. Ships in VS Code and on github.com. GA in **September 2025**.
- **2025-05-22** -- Claude Code reaches **general availability**. Ships with Claude Opus 4 and Sonnet 4 support. Extended thinking between tool calls.
- **2025-05-30** -- GitHub sunsets Copilot Workspace; its architecture is folded into the Copilot Coding Agent.
- **2025-06** -- Cursor v1.0 (first "stable" release). Over $500M ARR by this point. Used by "over half of the Fortune 500."
- **2025-09-29** -- Claude Code gets checkpoints (save/rollback), refreshed terminal UI, native VS Code extension (ships with Sonnet 4.5).
- **2025-10-20** -- Anthropic launches **Claude Code on the web** (browser-based).
- **2025-11** -- Cursor crosses $1B ARR. Claude Code also reaches ~$1B ARR within ~6 months of GA.
- **2025 (ongoing)** -- **Cline** (open-source VS Code extension, agentic coding), **Aider** (continued multi-model improvements), **Amazon Q Developer** (CLI launched March 2025; formerly CodeWhisperer, GA April 2024), and **OpenCode** (open-source Go-based terminal agent, 95K+ GitHub stars by 2026) all mature as alternatives.

---

## 3. Agentic Infrastructure Milestones

### Tool use and function calling evolution

- **2023-06-13** -- OpenAI introduces **function calling** in the API (GPT-3.5-turbo and GPT-4). Models can return structured JSON to invoke developer-defined functions. Foundation of all agent tool use.
- **2023-11-06** -- OpenAI DevDay: **Assistants API** (beta), **parallel function calling**, GPT-4 Turbo with 128K context. Assistants API bundles code interpreter, retrieval, and function calling into a stateful agent framework.
- **2024 (mid)** -- Anthropic makes **Claude tool use** generally available across Claude API, Bedrock, and Vertex AI.
- **2024-06** -- OpenAI introduces **Structured Outputs** (`strict: true` in function definitions). Guarantees schema-conforming JSON from function calls.

### Chain-of-thought and reasoning breakthroughs

- **2024-09-12** -- OpenAI's **o1** introduces "reasoning tokens": hidden chain-of-thought before the final answer. First commercial model explicitly trained for multi-step reasoning via RL.
- **2025-02-24** -- Anthropic's **Claude 3.7 Sonnet** ships **extended thinking**: configurable token budget for step-by-step reasoning before responding. First "hybrid" model (instant + thinking in one model).
- **2025-05-22** -- **Claude Opus 4** ships **extended thinking with tool use** (beta): the model thinks between tool calls, reasons about tool results, and decides next steps. This is the key capability for agentic loops.
- **2025-08-07** -- **GPT-5** ships with an integrated thinking/instant router. Model decides when to reason and when to answer directly.
- **2025-11** -- Both GPT-5.1 (adaptive reasoning) and Opus 4.5 (extended thinking + conversation summarization) reach production maturity.

### MCP and protocol-level standards

- **2024-11-25** -- Anthropic announces **MCP (Model Context Protocol)**, an open standard for connecting AI assistants to external tools and data sources. SDKs for Python, TypeScript, C#, Java. Pre-built servers for GitHub, Slack, Google Drive, Postgres, Puppeteer, etc.
- **2025-03-11** -- OpenAI releases the **Responses API** (replaces both Chat Completions and Assistants API for new projects), the open-source **Agents SDK** (successor to Swarm), and built-in tools (web search, file search, **computer use**) directly in the API. Agents SDK is model-agnostic. Assistants API scheduled for sunset H1 2026.
- **2025 (throughout)** -- MCP gains broad adoption. By its first anniversary (Nov 2025), MCP is described as an "industry standard." GitHub Copilot, Cursor, Windsurf, Claude Code, and other tools add MCP support.

### Computer use

- **2024-10-22** -- Anthropic releases **computer use** in public beta with Claude 3.5 Sonnet (new). First frontier model to control a computer via screen reading + keyboard/mouse simulation.
- **2025-01-23** -- OpenAI releases **Operator** (powered by CUA -- Computer-Using Agent). GPT-4o + RL for GUI interaction. 38.1% on OSWorld, 87% on WebVoyager. Available to ChatGPT Pro users.
- **2025-03-11** -- OpenAI makes computer use available as a built-in tool in the Responses API.

---

## 4. The "December 2025 Turning Point"

The deck frames "Dezembro de 2025" as the moment agents went from interesting experiments to production-ready tools. Here is what converged:

### What shipped in the Nov 13 -- Nov 24 window

1. **GPT-5.1 (Nov 12--19)** -- Adaptive reasoning, better instruction-following, improved coding benchmarks. Codex CLI by this point had months of refinement since its April launch and could run sustained multi-step tasks.
2. **Claude Opus 4.5 (Nov 24)** -- 96.1% SWE-bench Verified. Extended thinking with tool use now mature. Automatic conversation summarization for long sessions. Claude Code by this point had: checkpoints, background execution, VS Code extension, web interface, and ~8 months of post-GA iteration.

### Why "December" specifically

- Both flagship models and their CLI agents shipped within **11 days of each other** (Nov 13 and Nov 24).
- By December, early adopters had both tools running on production codebases. The combination of model quality + mature CLI tooling made it possible to run multi-hour autonomous coding sessions with meaningful output for the first time.
- The convergence was not just model intelligence. It was the **full stack maturing together**: model reasoning + tool calling + execution sandbox + feedback loops + session persistence + error recovery. Neither side alone would have been enough.

### What made December different from August

- GPT-5 (August) was a capability jump, but Codex CLI was still young (4 months old) and GPT-5 did not yet have the adaptive reasoning refinements of 5.1.
- Claude Opus 4.1 (August) improved on Opus 4 but Sonnet 4.5 (September) and the Claude Code checkpoints/VS Code extension had not shipped yet.
- By December, both ecosystems had their **second or third iteration** of the 2025-generation stack. The rough edges from the summer launches were smoothed out.

### The "January 2026 trigger" narrative

The presenter (Akita) frames January 2026 as when he personally entered the marathon, having watched December's early adopters demonstrate that sustained agent-driven development was viable. The proof block in the talk (FrankMD, M.Akita Chronicles, etc.) comes from his January--March 2026 hands-on experiments.

---

## 5. Benchmark and Capability Progression

### SWE-bench Verified (agentic coding -- resolve real GitHub issues)

| Date | Agent/Model | Score | Notes |
|------|-------------|-------|-------|
| 2024-03 | Devin (Cognition) | 13.86% | Previous SOTA was 1.96% |
| 2024-10 | Claude 3.5 Sonnet (new) | ~49% | Massive jump |
| 2024-12 | Best submission | ~62% | End-of-year SOTA |
| 2025-05 | Tools + Claude Opus 4 | 73.2% | |
| 2025-08 | GPT-5 | 74.9% | |
| 2025-11 | Claude Opus 4.5 | 96.1% | Near-saturation |
| 2026 Q1 | Best agentic systems | 76--80%+ (various) | Benchmark showing saturation; SWE-bench Pro introduced |

### Aider Polyglot (multi-language coding, 225 exercises, 6 languages)

| Date | Model | Score | Notes |
|------|-------|-------|-------|
| 2024-12 | Benchmark launched | -- | Paul Gauthier introduces polyglot leaderboard |
| 2025-08 | GPT-5 | 88% | |

### Other notable benchmarks

- **GPT-5** (Aug 2025): AIME 2025 math 94.6% (no tools), MMMU 84.2%, HealthBench Hard 46.2%, tool calling 96.7% on tau2-bench
- **Claude Opus 4.5** (Nov 2025): 95.5% Terminal-bench
- **SWE-bench Pro** (introduced late 2025): best models (GPT-5, Opus 4.1) score only ~23%, showing limits of current agents on long-horizon tasks

### The "before vs after" capability picture

- **March 2024**: Devin's 13.86% SWE-bench was revolutionary. Agents could fix simple, isolated bugs.
- **End of 2024**: ~62% SWE-bench Verified. Agents could handle moderately complex single-file and small multi-file issues.
- **End of 2025**: ~96% SWE-bench Verified. Agents can resolve the vast majority of curated GitHub issues. But SWE-bench Pro (~23%) shows they still struggle with long-horizon, multi-step engineering tasks requiring deep codebase understanding.
- **The real shift**: Not just benchmark numbers, but the ability to run sustained multi-step loops (edit -> test -> read error -> fix -> re-test) reliably enough for real project work. This is what thinking + tool use + CLI maturity enabled.

---

## 6. Supplementary: Complete Anthropic Claude Model Timeline

| Date | Model | Key capability |
|------|-------|---------------|
| 2024-03-04 | Claude 3 (Haiku, Sonnet, Opus) | Vision, 200K context |
| 2024-06-20 | Claude 3.5 Sonnet | Beat Opus 3 on most benchmarks |
| 2024-10-22 | Claude 3.5 Sonnet (new) + Haiku 3.5 | Computer use beta |
| 2025-02-24 | Claude 3.7 Sonnet | Extended thinking, hybrid reasoning |
| 2025-05-22 | Claude Opus 4 + Sonnet 4 | Thinking with tool use, 200K ctx |
| 2025-08-05 | Claude Opus 4.1 | Agentic improvements |
| 2025-09-29 | Claude Sonnet 4.5 | Best coding Sonnet yet |
| 2025-10-15 | Claude Haiku 4.5 | Fast/cheap agent subtasks |
| 2025-11-24 | Claude Opus 4.5 | 96.1% SWE-bench, conversation summarization |
| 2026-02-05 | Claude Opus 4.6 | Agent teams |
| 2026-02-17 | Claude Sonnet 4.6 | Adaptive thinking |

## 7. Supplementary: Complete OpenAI GPT/o-series Timeline

| Date | Model | Key capability |
|------|-------|---------------|
| 2024-05-13 | GPT-4o | Natively multimodal |
| 2024-09-12 | o1-preview, o1-mini | Reasoning via chain-of-thought |
| 2024-12-05 | o1 (full) | Full reasoning model |
| 2024-12-20 | o3 (announced) | Next-gen reasoning (researchers only) |
| 2025-01-31 | o3-mini | Broadly available reasoning |
| 2025-02-27 | GPT-4.5 | Research preview, largest GPT |
| 2025-04-14 | GPT-4.1 (+ mini, nano) | 1M context, 54.6% SWE-bench |
| 2025-04-16 | o3 + o4-mini (GA) | Best reasoning models |
| 2025-08-07 | GPT-5 (+ mini, nano) | Unified thinking/instant, 400K ctx |
| 2025-11-12 | GPT-5.1 (Instant + Thinking) | Adaptive reasoning |
| 2025-11-19 | GPT-5.1 (two more variants) | Expanded rollout |

---

## What the Timeline Tells Us

The story of 2025 is not about any single model release. It is about three layers maturing at the same time and finally clicking together. The first layer was raw model intelligence: reasoning tokens, extended thinking, hybrid instant-and-thinking modes. Models learned to pause, plan, and revise their own work mid-task. The second layer was tool infrastructure: function calling became reliable, MCP gave agents a universal plug for external systems, and computer use turned the screen itself into an API. The third layer was the CLI harness around those models — Claude Code, Codex CLI, Cursor's Composer — that could hold a multi-step loop open long enough to edit, test, read the error, fix, and re-test without human babysitting.

## Why Agents Care About Caches and Thinking, Not Just Bigger Models

The intuitive assumption is that smarter AI means bigger models with more parameters. That was roughly true from GPT-2 (1.5B) through GPT-4 (rumored ~1.8T). But the agent era broke that pattern. The capabilities that actually made agents viable in 2025 were not about scale — they were about how models use compute at inference time, and how cheaply they can revisit context they have already seen.

### KV cache (key-value cache)

Every transformer model, when processing a conversation, builds an internal representation of each token it has seen — a pair of key and value vectors per attention layer. That is the KV cache. Without it, every time the model generates the next token it would need to recompute attention over the entire conversation from scratch, which is quadratic in cost. With a KV cache, previous tokens are computed once and reused. For a single-shot chatbot reply this is a minor optimization. For an agent that runs 50 or 100 tool-call turns in a loop — reading files, editing, running tests, reading errors, fixing — the KV cache is the difference between a session that costs a few dollars and one that costs hundreds. It is also what makes long-context models (200K, 400K, 1M tokens) practical at all: without the cache, a 200K-token conversation would recompute attention over 200K tokens at every single generation step.

### Prompt cache (cross-request caching)

KV cache lives within a single request. Prompt cache goes further: it persists the computed KV state across multiple API requests, as long as the prefix of the conversation has not changed. Anthropic introduced prompt caching for the Claude API in mid-2024, and by 2025 it was standard across providers. This matters enormously for agents because the system prompt, the project context, and the conversation history up to the current turn are identical across consecutive tool calls. Without prompt caching, a 50-turn agent session re-processes the full system prompt and conversation history 50 times. With it, only the new tokens (the latest tool result and the model's new response) require fresh computation. The cost reduction is often 90% or more for long agentic sessions. This is what made $20/month subscription pricing viable for tools like Claude Code — the per-session compute cost dropped by an order of magnitude thanks to prefix caching.

### Tool calling (function calling)

Before tool calling, the only way to give a model access to external capabilities was to paste text instructions and hope it formatted its reply in a way your code could parse. This was fragile. Tool calling formalized the contract: the model receives a schema of available tools (name, parameters, types), and when it decides to use one, it returns a structured JSON object that the harness can execute deterministically. The harness runs the tool, feeds the result back, and the model continues. This loop — reason, call tool, observe result, reason again — is what turns a language model into an agent. The key improvements in 2025 were reliability (models stopped hallucinating tool names or malforming parameters), parallel tool calling (invoke multiple tools in one turn), and thinking between tool calls (the model can reason about the result of one tool before deciding which tool to call next). Without reliable tool calling, every other agent capability is academic.

### Deep thinking (extended thinking / reasoning tokens)

Standard language model generation is a single forward pass per token — fast, but shallow. The model commits to each token as it goes and cannot backtrack. Reasoning models (o1, o3, Claude 3.7 Sonnet's extended thinking, GPT-5's thinking mode) introduced a separate "thinking" phase: before producing the visible answer, the model generates an internal chain-of-thought that can be thousands of tokens long. This thinking is not shown to the user, but it lets the model decompose a problem, consider alternatives, catch its own mistakes, and plan multi-step strategies. For an agent, this is transformative. A coding agent that needs to decide "should I edit file A or file B, and in which order, and what test should I run after?" benefits enormously from a planning phase that happens before the first tool call. Extended thinking with tool use (introduced with Claude Opus 4 in May 2025) meant the model could also think between tool calls — after reading a test failure, it could reason about what went wrong before deciding its next edit. This is the capability that turned agents from "try something and hope" into "diagnose, plan, then act."

### Why not just add more parameters?

Scaling parameters hits diminishing returns and escalating costs simultaneously. Going from 70B to 700B parameters roughly doubles benchmark scores on some tasks, but it also requires 10x more GPU memory, 10x more training compute, and 10x more inference cost. The 2025 breakthroughs came from a different direction: keep the model at a practical size (or use Mixture-of-Experts to activate only a fraction of parameters per token, as DeepSeek V3 and Qwen 3 did), but make it smarter at inference time by letting it think longer, cache what it has already computed, and call external tools instead of trying to memorize everything in its weights. A 200B-parameter model that can think for 30 seconds, call `grep` on a codebase, read the result, and think again will outperform a 2T-parameter model that has to answer in a single pass from memory alone. The agent paradigm is fundamentally about trading raw parameter count for inference-time compute and external tool access — and that trade became decisive in 2025.

### Case study: DeepSeek — big model, missing plumbing

DeepSeek is the clearest example of why raw model size does not translate into agent capability. DeepSeek V3 has 671 billion parameters (37B active per token via MoE). DeepSeek R1 is a reasoning model trained with RL. On paper, these are frontier-class systems. In practice, they fail at the exact capabilities that matter for agentic coding.

**No prompt caching.** As of early 2026, the DeepSeek API does not offer cross-request prefix caching. In Akita's April 2026 benchmark, Claude Opus 4.6 processed 136,806 total tokens but only 830 were new — the other 135,976 were cache reads. DeepSeek V3.2 processed 115,278 tokens and every single one was recomputed from scratch: zero cache reads. The result: DeepSeek was the slowest cloud model in the benchmark at 53 tok/s (slower than locally-run Qwen 3.5 35B on an AMD Strix Halo at 46 tok/s), and the session took 60 minutes versus Claude's 16 minutes. For an agentic loop that makes 50+ round trips, resending the full context every turn is a death sentence for both speed and cost.

**Weak tool calling.** DeepSeek V3.2 supports tool calling, but in the benchmark it invented `RubyLLM::Client.new` — a class that does not exist in the gem the prompt explicitly asked it to use. The generated code crashes on the first request. This is the same hallucination pattern seen in Kimi K2.5 and MiniMax M2.7: the model tries to make the API look like the OpenAI Python SDK because that is what its training data overrepresents. Claude and GLM 5 got the API right; DeepSeek did not. Reliable tool calling is not just about emitting valid JSON — it requires the model to reason about what tool to call, with what arguments, based on actual knowledge of the target system. DeepSeek's tool calling is structurally functional but factually unreliable.

**Reasoning exists but is not integrated with tool use.** DeepSeek R1 has chain-of-thought reasoning (it emits `<think>` blocks), but it was not designed to interleave reasoning with tool calls in the way Claude Opus 4+ or GPT-5 do. R1 thinks, then answers — it does not think between tool calls. For a single-shot question, that is fine. For an agent that needs to read a test failure, reason about what went wrong, decide which file to edit, make the edit, run the test again, and reason about whether the fix worked, the thinking needs to happen between each step. DeepSeek's architecture does not support that loop natively.

**The KV cache problem at scale.** DeepSeek V3 uses Multi-Head Latent Attention (MLA), a compression technique that reduces KV cache size by projecting keys and values into a lower-dimensional latent space. This is architecturally clever and does help with memory efficiency during inference. But KV cache compression only helps within a single request. Without cross-request prompt caching, the model still recomputes the full context from scratch on every API call, which is where the real cost lives in agentic workflows. MLA makes each individual forward pass cheaper, but it does not solve the "50 round trips with the same system prompt" problem that prompt caching solves.

The bottom line: DeepSeek has the parameter count, the MoE architecture, and even a reasoning model. What it lacks is the infrastructure layer — prompt caching, reliable tool calling with factual grounding, and thinking-between-tool-calls — that turns a smart model into a functional agent. In Akita's benchmark, it landed in Tier 3 (broken code, easier to redo than fix) alongside models a fraction of its size. The 671 billion parameters did not help because the bottleneck was never raw intelligence.

**Update (May 2026):** DeepSeek V4 Pro shipped in April 2026 and partially closes the gap. With the right harness — `DeepClaude` (a shim that swaps the Claude Code endpoint to OpenRouter or DeepSeek direct) — V4 Pro reaches **Tier A at 89/100**, behind only Opus 4.7, GPT 5.4/5.5, and Kimi K2.6. In `opencode` and other `ai-sdk`-based harnesses, however, the model is still unmeasurable: the SDK strips `reasoning_content` between turns and DeepSeek's API returns 400 on turn 2. So the underlying point holds — the model itself is capable, but the tool-protocol surface still requires bespoke harness work. The 15–20 point lift from a harness change alone (Tier B 69 → Tier A 89) is the cleanest demonstration that, for agents, the harness is part of the model.

In the same April 2026 round, **Kimi K2.6** also reached Tier A (87/100) and is the cheapest Tier A model in the benchmark ($0.30/run, 3–50× cheaper than Opus 4.7 / GPT 5.4). Together they mark the first time Chinese open-weight models crossed into Tier A.

None of these layers was sufficient on its own. A brilliant model with no tool access is a chatbot. A tool-rich framework around a model that cannot reason across steps produces garbage loops. A mature CLI wired to a mediocre model just automates bad patches faster. What happened between May and November 2025 is that all three layers crossed their respective quality thresholds within months of each other. By December, when both GPT-5.1 and Claude Opus 4.5 were in the wild with battle-tested CLIs around them, early adopters started running multi-hour autonomous sessions on real codebases — and the output was genuinely useful. That is the inflection the deck calls "a virada": not a single product launch, but the moment the full stack stopped being a promising demo and became a production tool. The SWE-bench numbers (13% to 96% in twenty months) are dramatic, but the real proof is simpler — by January 2026, people were shipping real projects with agents doing the bulk of the typing, and the results held up under review.

---

## Sources

- [Anthropic Claude 3 family announcement](https://www.anthropic.com/news/claude-3-family)
- [Anthropic Claude 3.5 Sonnet announcement](https://www.anthropic.com/news/claude-3-5-sonnet)
- [Anthropic Claude 3.5 models and computer use](https://www.anthropic.com/news/3-5-models-and-computer-use)
- [Anthropic Claude 3.7 Sonnet and Claude Code](https://www.anthropic.com/news/claude-3-7-sonnet)
- [Anthropic Claude Opus 4 system card](https://www.anthropic.com/claude-4-system-card)
- [Anthropic Claude Opus 4.1](https://www.anthropic.com/news/claude-opus-4-1)
- [Anthropic Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5)
- [Anthropic Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)
- [Anthropic MCP announcement](https://www.anthropic.com/news/model-context-protocol)
- [OpenAI o1-preview announcement](https://openai.com/index/introducing-openai-o1-preview/)
- [OpenAI GPT-4.5 announcement](https://openai.com/index/introducing-gpt-4-5/)
- [OpenAI GPT-4.1 (Wikipedia)](https://en.wikipedia.org/wiki/GPT-4.1)
- [OpenAI o3 and o4-mini announcement](https://openai.com/index/introducing-o3-and-o4-mini/)
- [OpenAI GPT-5 announcement](https://openai.com/index/introducing-gpt-5/)
- [OpenAI GPT-5.1 announcement](https://openai.com/index/gpt-5-1/)
- [OpenAI Responses API and Agents SDK (InfoQ)](https://www.infoq.com/news/2025/03/openai-responses-api-agents-sdk/)
- [OpenAI Operator announcement](https://openai.com/index/introducing-operator/)
- [OpenAI Codex CLI (TechCrunch)](https://techcrunch.com/2025/04/16/openai-debuts-codex-cli-an-open-source-coding-tool-for-terminals/)
- [Cognition Devin launch](https://cognition.ai/blog/introducing-devin)
- [Cognition Devin GA](https://cognition.ai/blog/devin-generally-available)
- [DeepSeek (Wikipedia)](https://en.wikipedia.org/wiki/DeepSeek_(chatbot))
- [Qwen 3 (Alibaba Cloud blog)](https://www.alibabacloud.com/blog/alibaba-introduces-qwen3-setting-new-benchmark-in-open-source-ai-with-hybrid-reasoning_602192)
- [Gemini 2.5 Pro (Google blog)](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/)
- [Llama 4 (Meta AI blog)](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [Mistral Codestral](https://mistral.ai/news/codestral)
- [GitHub Copilot Agent Mode announcement](https://github.com/newsroom/press-releases/agent-mode)
- [GitHub Copilot Coding Agent](https://github.com/newsroom/press-releases/coding-agent-for-github-copilot)
- [Cursor statistics (DevGraphIQ)](https://devgraphiq.com/cursor-statistics/)
- [Windsurf Editor launch (Maginative)](https://www.maginative.com/article/codeium-launches-windsurf-editor-an-agentic-integrated-development-environment/)
- [Amazon Q Developer GA](https://aws.amazon.com/about-aws/whats-new/2024/04/amazon-q-developer-generally-available/)
- [SWE-bench leaderboards](https://www.swebench.com/)
- [SWE-bench Verified (Epoch AI)](https://epoch.ai/benchmarks/swe-bench-verified/)
- [Claude (Wikipedia)](https://en.wikipedia.org/wiki/Claude_(language_model))
- [GPT-5 (Wikipedia)](https://en.wikipedia.org/wiki/GPT-5)
- [GPT-5.1 (Wikipedia)](https://en.wikipedia.org/wiki/GPT-5.1)
- [OpenAI o3 (Wikipedia)](https://en.wikipedia.org/wiki/OpenAI_o3)
