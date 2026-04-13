# AI Energy Usage, Power Consumption & Infrastructure Crisis

Research compiled April 2026 for Tropical Ruby 2026 keynote. Numbers sourced from IEA, Epoch AI, Gartner, Goldman Sachs, PJM Interconnection, Pew Research, Carbon Brief, and industry reporting (CNBC, Tom's Hardware, Utility Dive, etc.). Where projections diverge between sources, ranges are noted.

---

## 1. Current Power Consumption Numbers

### Global Data Center Electricity

- **2024 baseline**: ~415 TWh globally, just over 1% of global electricity demand, 0.5% of global CO2 emissions (Carbon Brief / IEA)
- **2025 estimate**: 448 TWh worldwide (Gartner); other estimates range 460-500 TWh
- **2026 projection**: IEA projects 1,100 TWh globally — equivalent to Japan's entire annual electricity consumption. This was an 18% upward revision from December 2025 estimates
- **Growth rate**: ~15% per year from 2024 to 2030, more than 4x faster than total electricity consumption growth from all other sectors (IEA)

### United States Specifically

- **2024**: US data centers consumed 183 TWh — more than 4% of US total electricity, equivalent to Pakistan's entire annual demand (Pew Research)
- **2025**: well over 200 TWh (IEA)
- **2026**: over 250 TWh, representing ~6% of total US electricity consumption (IEA / Pew)
- **2028**: 6.7% to 12% of total US electricity (various estimates)
- **2030**: 426 TWh — a 133% increase from 2024 (Pew); other estimates range to 400 TWh (IEA)
- **US share**: nearly 50% of global data center electricity consumption

### Regional Hotspots

- **Virginia**: ~26% of state electricity goes to data centers (2023), hosts over a third of the world's data centers
- **Ireland**: data centers consume 21-24% of national electricity, projected to reach 32% by 2026
- **Dublin**: 79% of local electricity consumed by data centers
- **China**: ~25% of global data center consumption
- **Europe**: ~15% of global data center consumption

### Single Facility / Single Training Run Scale

- A typical hyperscale data center draws 20-100 MW of power
- Larger facilities under construction expected to use power equivalent to 2 million households (Pew)
- Today's cutting-edge frontier training runs consume tens to hundreds of megawatts — comparable to a medium-sized power plant (Epoch AI)
- GPT-4 training consumed ~1,750 MWh (annual consumption of ~160 US homes)
- GPT-5 training estimated at ~3,500 MWh (annual consumption of ~320 US homes)
- GPT-3 (175B params) training: ~1,287 MWh (~120 US homes)

### Per-Query Energy

- ChatGPT (GPT-4o): ~0.3 Wh per simple query (Sam Altman, 2025) — roughly equal to a Google search
- The old "10x Google search" claim is outdated; efficiency gains closed the gap
- Complex queries with long documents: 2.5 Wh; 100k-token inputs: ~40 Wh
- GPT-5 inference may use 18+ Wh per output for complex responses (early estimates)

---

## 2. Data Center Buildout & Capex

### Combined 2026 Spending

- **$660-690 billion combined capex** from Microsoft, Alphabet, Amazon, Meta, and Oracle in 2026 — nearly doubling 2025 levels (CNBC, Futurum Group)
- ~75% ($450B+) directly tied to AI infrastructure (GPUs, servers, data centers), not traditional cloud (Futurum)
- Jensen Huang (NVIDIA) claims $600B in annual AI infrastructure capex is the new baseline

### Individual Company 2026 Capex

| Company | 2026 Capex (est.) | Notes |
|---------|-------------------|-------|
| Amazon | ~$200B | Largest spender; negative FCF of $17-28B projected |
| Alphabet | $175-185B | FCF projected to plummet ~90% (from $73.3B to $8.2B) |
| Meta | $115-135B | |
| Microsoft | $120B+ | |
| Oracle | ~$50B | |

### For Comparison: 2024 Capex

- Amazon $85.8B, Google $52.5B, Microsoft $44.5B, Meta $39.2B — combined ~$222B
- 2026 represents a roughly 3x increase in just two years

### Financial Stress

- Companies increasingly turning to debt markets to fund buildout
- Amazon looking at negative free cash flow of $17-28B in 2026
- Alphabet FCF projected to collapse from $73.3B (2025) to $8.2B (2026) — a 90% drop

---

## 3. Energy Shortage & Grid Strain

### PJM Interconnection (US East Coast) — The Canary in the Coal Mine

- PJM serves 65M+ people across 13 US states; it is the largest US grid operator
- **December 2025 capacity auction failed for the first time in history** — fell 6,625 MW short of reliability targets for 2027/28
- Capacity prices surged to $333.44/MW-day (up from $28.92/MW-day in 2024 — an 11x increase)
- **Summer 2027 will be the first time PJM expects to not have enough power** to reliably meet demand
- Data centers account for 94% of projected load growth in PJM territory
- Data centers add 5-7 GW annually to demand; new supply delivers only 2-3 GW
- Interconnection queue wait times now exceed 36 months

### Build Delays and Cancellations

- **Nearly half of all US data centers planned for 2026 have been delayed or canceled** (Tom's Hardware, TechRadar)
- Only ~one-third of the 12 GW of capacity expected in 2026 is under active construction
- Root cause: electrical component shortages (transformers, switchgear, batteries)
- Lead times for high-power transformers have expanded dramatically
- China supplies 40% of US battery imports and ~30% of transformer/switchgear components
- US imports of high-power transformers from China surged from <1,500 units (2022) to >8,000 units (2025)

### Electricity Price Impact on Consumers

- US residential electricity prices rose 11.5% in 2025, outpacing inflation (Goldman Sachs)
- Areas near data center clusters saw electricity prices jump 267% over five years
- 70%+ of price increase nodes are within 50 miles of significant data center activity
- Projected 40% price increase by 2030 vs. 2025 levels
- PJM market: $9.3B price increase projected for 2025-26
- Carnegie Mellon study: data centers could cause 8% average US electricity bill increase by 2030; 25%+ in Northern Virginia
- 78% of Americans are concerned data centers will raise their energy bills (Consumer Reports, Nov 2025)

---

## 4. Nuclear & Alternative Energy for AI

### Three Mile Island Restart (Microsoft)

- **20-year PPA**, 835 MW capacity, Constellation investing $1.6B to restart the dormant Unit 1 reactor (shut down 2019 for economics)
- Renamed "Crane Clean Energy Center," expected online 2028 (some sources say 2027)
- US DOE closed a $1B federal loan to Constellation (November 2025) with low-interest financing
- Demonstrated that restarting a dormant large-scale reactor is financially preferable to waiting for new technologies

### Other Major Nuclear Deals

| Company | Partner | Deal Details |
|---------|---------|-------------|
| Google | Kairos Power | First US corporate SMR fleet deal: 500 MW by 2030+, first reactor expected online 2030 |
| Amazon | X-Energy | $500M for reactor design, licensing, and TRISO fuel; 320 MWe from 4 reactor modules |
| Amazon | Susquehanna | $20B+ converting site to nuclear-powered AI data center campus |
| Meta | (RFP) | Request for proposals: 1-4 GW of new nuclear generation |

### Combined Nuclear Appetite

- Big tech signed contracts for 10+ GW of possible new nuclear capacity in the US in the past year
- This is a "nuclear arms race" among hyperscalers

### SMR (Small Modular Reactor) Progress

- NuScale 462 MW SMR received Standard Design Approval May 2025 (two months early)
- President Trump signed four Executive Orders (May 2025) to speed SMR deployment and ease NRC licensing
- Google/Kairos deal is the first US corporate SMR fleet contract
- SMRs are not expected to deliver meaningful power before 2030-2032

### Energy Source Mix for Data Centers (Current)

- Fossil fuels: ~60%
- Renewables: ~27%
- Nuclear: ~15%
- By 2035: projected 60% clean / 40% fossil (Carbon Brief)

### Gas Power Expansion

- Gas-fired power for data centers: 120 TWh (2024) projected to hit 293 TWh by 2035
- 38 GW of gas plant capacity designated for data centers (~25% of all such projects globally)

---

## 5. Training vs. Inference Power Split

### Current Split

- Historically, inference was cited as 80-90% of compute
- More recent analysis (Epoch AI) suggests current AI power demand splits **roughly equally** among training, experiments, and inference
- The shift is happening fast: inference was ~33% of compute in 2023, ~50% in 2025, projected ~67% in 2026

### Which Is Growing Faster?

- **Inference is growing faster**, driven by mass consumer/enterprise adoption
- Agents multiply inference cost per user (an agent session uses 10-100x more tokens than a simple chatbot query)
- Training compute grows 4-5x per year, but GPU efficiency improves 26-40% per year, partially offsetting power growth
- Individual frontier training runs: power doubles every ~year (2.2x annual growth rate)
- By 2030, a single frontier training run could draw 4-16 GW — approaching "small country" territory

### Inference Efficiency Gains

- NVIDIA claims 1,000,000x improvement in inference throughput per megawatt across six GPU architecture generations
- Blackwell: 15x lower cost per million tokens vs. previous generation; 10x throughput per megawatt for MoE models
- Google TPUs: 4.7x better performance-per-dollar, 67% lower power consumption vs. GPUs
- Software optimizations: 33x energy reduction per prompt achieved in 12 months
- Hardware delivers ~30% annual cost reduction and ~40% annual energy efficiency gains
- **But efficiency gains are being overwhelmed by demand growth** — total energy still rises

### Inference Spending Share

- Inference now represents 55% of AI infrastructure spending in early 2026, up from 33% in 2023

---

## 6. Cost Projections & Future Power Needs

### Near-Term (2026-2028)

- Total hyperscaler capex: $660-690B in 2026; likely $800B+ by 2028 at current trajectory
- US data center demand: may nearly double from 80 GW (2025) to 150 GW by 2028 (Bloom Energy)
- US utilities need $50B in new generation capacity just for data centers
- Global grid upgrades could cost $720B through 2030

### 2030 Projections

| Metric | Projection | Source |
|--------|-----------|--------|
| Global DC electricity | 945-1,300 TWh | IEA (base case) / IEA (2035) |
| US DC electricity | 400-426 TWh | IEA / Pew |
| Global DC share of electricity | ~3% | IEA base case |
| US DC share of electricity | 7-12% | Various |
| Total AI power capacity | >100 GW worldwide | Epoch AI |
| US AI power capacity | >50 GW | Epoch AI |
| Single frontier training run | 4-16 GW | Epoch AI |
| Residential price increase | up to 40% vs. 2025 | Goldman Sachs |

### Analyst Warnings

- **Permitting mismatch**: AI companies want GWs in 2-3 years; US/EU permitting takes 10+ years for new power plants
- Goldman Sachs models 50% demand growth to 92 GW by 2027 (base case)
- Former Google CEO Eric Schmidt testified to Congress: 29 GW additional by 2027, 67 GW more by 2030
- Energy analysts: 75-100 GW of new generation capacity needed to supply 1,000+ TWh/year by early 2030s
- Gartner: data center electricity demand to grow 16% in 2025 and **double** by 2030 (from 448 TWh to 980 TWh)

---

## 7. Environmental & Political Implications

### Carbon Footprint

- AI systems alone: 32.6 to 79.7 million tons CO2 in 2025
- By 2030: 24-44 million metric tons CO2 annually — equivalent to adding 5-10 million cars to US roads
- Data centers currently produce 0.5% of global CO2; projected to reach 1-1.4% by 2030

### Water Usage

- 2025 water footprint: 312.5-764.6 billion liters
- By 2030: 731-1,125 million cubic meters/year — equal to household water use of 6-10 million Americans
- Texas alone: 49 billion gallons (2025) potentially rising to 399 billion gallons (2030)
- Rule of thumb: 2 liters of cooling water per 1 kWh consumed
- By 2027: ~5 billion cubic meters of water annually for data centers globally

### Political Landscape

- **AI Data Center Moratorium Act of 2026** (Sanders/AOC, introduced March 25, 2026): federal moratorium on new AI data center construction until comprehensive AI safety legislation passes
- **At least 11 US states** considering legislation to temporarily ban new data centers
- Virginia delegate Irene Shin: moratorium bill until July 2028 or until interconnection queue clears
- **Bipartisan skepticism**: Bernie Sanders (left) and Ron DeSantis (right) both critical of data center boom, though with different approaches (federal ban vs. local authority)
- Most lawmakers in both parties have rejected moratorium; Sen. Fetterman called it "waving a surrender flag to China"
- Trump White House convened AI executives for a "Ratepayer Protection Pledge" — costs not to be passed to consumers
- **Ireland**: lifted its 2021 de facto moratorium on Dublin data centers in December 2025, but now requires 80% on-site renewable/battery power for new facilities

### Potential Mitigations (Per Cornell Roadmap)

- Smart siting, faster grid decarbonization, and operational efficiency could cut impacts by ~73% (CO2) and ~86% (water) vs. worst case
- Direct-to-chip and immersion cooling can significantly reduce water use
- EU exploring waste heat from data centers for water purification and carbon capture

---

## What the Numbers Tell Us

The AI industry is building the most capital-intensive infrastructure expansion since the electrification of cities, and it is doing it on a grid that was not designed for it. Hyperscalers tripled their combined capex in two years — from $222 billion in 2024 to nearly $700 billion in 2026 — and most of that money is chasing the same scarce resource: reliable electricity near fiber and water. The result is a collision. Data centers now consume more power than most countries, and the largest US grid operator failed to procure enough capacity for the first time in its history. Nearly half of the data centers planned for 2026 are delayed or canceled, not because the money ran out, but because the transformers, switchgear, and grid connections physically do not exist yet. The bottleneck is not silicon — it is copper and concrete.

The response from big tech has been to go around the grid entirely. Microsoft is restarting a nuclear reactor. Google and Amazon signed deals for small modular reactors that will not deliver power before 2030. In the meantime, gas-fired plants are filling the gap, which means the "clean AI" marketing collides with 32-to-80 million tons of CO2 per year and hundreds of billions of liters of cooling water. Residential electricity prices are already up 11.5% in a single year, with projections of 40% increases by 2030 in data-center-heavy regions. The political backlash is real: moratorium bills, bipartisan anger, and 78% of Americans worried about their power bills. The core tension for the next few years is simple — AI inference demand is growing faster than any energy source can be built, efficiency gains are real but consistently overwhelmed by usage growth, and the bill is landing on regular ratepayers who never asked for any of this.

---

## Slide Fact-Check Notes

The current slide ("Treino e inferencia disputam a mesma tomada") states:

| Slide Claim | Status | Updated Figure |
|-------------|--------|---------------|
| "US$ 500 bi investimento global em data centers em 2024" | **Conservative but defensible** — 2024 Big Four capex was ~$222B; total global DC investment (including non-hyperscaler) was roughly $500B. For 2026 the number is $660-690B for hyperscalers alone |
| "415 -> 945 TWh consumo eletrico 2024 ate 2030" | **Correct** — IEA base case. Some newer IEA revisions push 2026 alone to 1,100 TWh (includes all data centers, not just AI) |
| "20% dos projetos podem atrasar por gargalo de rede" | **Understated** — actual figure is closer to 33-50% of planned 2026 builds delayed or canceled |
| "2,5 bi/ano ritmo anual do Claude Code" | Anthropic-specific claim, not energy-related |

### Potential New Data Points for the Slide

- $660-690B hyperscaler capex in 2026 (vs. $222B in 2024 — a 3x jump in 2 years)
- PJM capacity auction failed for the first time in history (Dec 2025) — 6.6 GW short
- Nearly half of planned US data centers for 2026 delayed or canceled
- Capacity price: $28.92/MW-day (2024) to $333.44/MW-day (2025) — 11x increase
- 10+ GW of nuclear deals signed by big tech in one year
- Ireland: 32% of national electricity to data centers by 2026
- By 2030, a single frontier training run may draw 4-16 GW

---

## Key Sources

- [IEA — Energy Demand from AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [Epoch AI — Power Demands of Frontier AI Training](https://epoch.ai/blog/power-demands-of-frontier-ai-training/)
- [Epoch AI — Power Usage Trend](https://epoch.ai/data-insights/power-usage-trend)
- [Gartner — Data Center Electricity Demand to Double by 2030](https://www.gartner.com/en/newsroom/press-releases/2025-11-17-gartner-says-electricity-demand-for-data-centers-to-grow-16-percent-in-2025-and-double-by-2030)
- [Pew Research — US Data Center Energy Use](https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/)
- [Carbon Brief — Five Charts on Data Centre Energy](https://www.carbonbrief.org/ai-five-charts-that-put-data-centre-energy-use-and-emissions-into-context/)
- [CNBC — Tech AI Spending Approaches $700B in 2026](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html)
- [Futurum — AI Capex 2026: The $690B Infrastructure Sprint](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/)
- [CNBC — Sanders and DeSantis vs. Data Center Boom](https://www.cnbc.com/2026/01/01/ai-data-centers-bernie-sanders-ron-desantis-electricity-prices.html)
- [Sanders.senate.gov — AI Data Center Moratorium Act](https://www.sanders.senate.gov/press-releases/news-sanders-ocasio-cortez-announce-ai-data-center-moratorium-act/)
- [Tom's Hardware — Half of Planned US Data Center Builds Delayed](https://www.tomshardware.com/tech-industry/artificial-intelligence/half-of-planned-us-data-center-builds-have-been-delayed-or-canceled-growth-limited-by-shortages-of-power-infrastructure-and-parts-from-china-the-ai-build-out-flips-the-breakers)
- [Fortune — US Data Center Development Hit Snags](https://fortune.com/2026/03/18/power-grids-snags-electricity-limits-data-centers/)
- [PJM Inside Lines — Long-Term Load Forecast](https://insidelines.pjm.com/2025-long-term-load-forecast-report-predicts-significant-increase-in-electricity-demand/)
- [NRDC — PJM Auction Fails to Procure Supply](https://www.nrdc.org/press-releases/first-time-history-pjm-auction-fails-procure-necessary-power-supply)
- [Utility Dive — Solving PJM's Data Center Problem](https://www.utilitydive.com/news/solving-pjms-data-center-problem/805600/)
- [CNBC — Electricity Prices Rising on AI Data Center Demand](https://www.cnbc.com/2026/02/12/electricity-price-data-center-ai-inflation-goldman.html)
- [Consumer Reports — AI Data Centers Impact on Electric Bills](https://www.consumerreports.org/data-centers/ai-data-centers-impact-on-electric-bills-water-and-more-a1040338678/)
- [NPR — Three Mile Island to Reopen for Microsoft](https://www.npr.org/2024/09/20/nx-s1-5120581/three-mile-island-nuclear-power-plant-microsoft-ai)
- [IEEE Spectrum — Microsoft Powers Data Centers with TMI Nuclear](https://spectrum.ieee.org/three-mile-island)
- [Introl — Nuclear Power for AI Data Centers](https://introl.com/blog/nuclear-power-ai-data-centers-microsoft-google-amazon-2025)
- [Cornell Chronicle — Environmental Impact Roadmap](https://news.cornell.edu/stories/2025/11/roadmap-shows-environmental-impact-ai-data-center-boom)
- [Euronews — AI Data Centre Carbon Footprint](https://www.euronews.com/next/2025/12/20/ai-data-centres-could-have-a-carbon-footprint-that-matches-small-european-country-new-stud)
- [MIT Technology Review — AI Energy Footprint](https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/)
- [Deloitte — GenAI Power Consumption](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/genai-power-consumption-creates-need-for-more-sustainable-data-centers.html)
- [S&P Global — Data Center Grid-Power Demand](https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/101425-data-center-grid-power-demand-to-rise-22-in-2025-nearly-triple-by-2030)
- [Epoch AI — How Much Energy Does ChatGPT Use?](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use/)
- [Roll Call — Data Center Moratorium Bill](https://rollcall.com/2026/03/25/data-center-moratorium-pitched-as-counter-to-ai-impacts/)
- [CNBC — Who Is Footing the AI Energy Bill?](https://www.cnbc.com/2026/03/13/ai-data-centers-electricity-prices-backlash-ratepayer-protection.html)
