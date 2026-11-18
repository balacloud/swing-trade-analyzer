# Research prompt: "Why stocks move" playbook (draft v1, Day 127)

Purpose: one research run (Fable/Opus deep research, or a Claude session with web + code) that produces the evidence for a top-down playbook: **macro event -> sector -> stock**, the same path the Context tab, Sectors tab and Analyze tab already follow. Output feeds a playbook page. Not a trading system, not advice: the user decides every trade.

Paste everything below the line.

---

## PROMPT

You are a market historian and a skeptical quantitative researcher. Build the evidence base for a **top-down playbook that explains why stocks move**, using as much real market history as exists (target: 1926 to today for US stocks, longer for rates and the economy where free data goes back).

### The user and the use
A discretionary swing trader (days to weeks). They read a macro backdrop (rates, inflation, growth, credit, volatility, the dollar, oil), then pick sectors, then stocks. They want to know, for each macro event, **what usually happened next, in which sectors, in which kinds of stocks, how often, and how often it did NOT**. They make every trade decision themselves. The page that uses your work states **facts and base rates, never verdicts or predictions**.

### The path to cover (in this order)
1. **Macro events.** At least: Fed rate cuts (start of a cutting cycle vs. "insurance" cut vs. cuts in a recession), rate hikes, a flat/inverted/re-steepening yield curve, inflation surprises, recessions (start and end), credit spreads widening, VIX spikes, dollar moves, oil shocks, big policy events (QE/QT, tariffs, fiscal shocks). Define each event with a rule a computer can check (dates, thresholds), not a story.
2. **Sector response.** For each event: which of the 11 GICS sectors (or the Fama-French industry portfolios before GICS existed) outperformed/underperformed the market over 1, 3, 6 and 12 months after, measured against the market, with the spread of outcomes, not just the average.
3. **Stock-level response.** Inside a sector: what separated winners from losers (size, value/growth, momentum, quality, leverage, beta, earnings revisions, dividend yield). Which traits repeat across eras and which flipped.

### Questions each section must answer
- What happened on average **and** the range (median, 25th/75th percentile, worst case, % of times it was positive).
- How many independent episodes is that based on? (Overlapping windows are not independent. Say "n = 14 cutting cycles", not "n = 3,000 days".)
- Does it hold in every era (1926-45, 1946-65, 1966-81, 1982-99, 2000-2012, 2013-today) or only some?
- What is the **counter-example set**: the times the usual pattern failed, and what was different.
- Is the pattern still there after costs, and does it need hindsight (could someone have known the rule at the time)?
- What is already priced in? (Did the sector move BEFORE the event, e.g. rate-cut rallies that happen on the expectation, not the cut.)

### Data (name the exact source for every number)
Prefer free, citable, long-history sources: Ken French data library (industry, size, value, momentum portfolios, from 1926), Robert Shiller's data (S&P, CAPE, rates, from 1871), FRED (Fed funds, yield curve, CPI, unemployment, credit spreads, recession dates from NBER), CRSP-derived free series where available, Yahoo/Stooq/Twelve Data for ETFs after ~1999. If a claim needs data you could not get, say "not tested" and stop; never fill the gap with a plausible story.

### Method rules (non-negotiable)
1. **Write the event rule before looking at results** and keep it. No re-cutting until something works.
2. Count **episodes**, not days. Report the sample size beside every number.
3. Account for **survivorship bias** (indices drop failures), **look-ahead** (revised data, e.g. GDP, CPI revisions; use the data as first published where possible), and **regime change** (rates at 0% vs 5%, pre/post-1971 gold standard).
4. Compare to a **simple baseline** (buy the market on random dates). A pattern that does not beat random dates is not a pattern.
5. Report effect size in plain terms (e.g. "tech beat the market by a median 3 points over 6 months, in 9 of 14 episodes"), then a confidence statement. Multiple-testing warning: you will test many things; list how many, and treat the best-looking results as suspect.
6. Mark every finding with one grade: **Strong** (many episodes, all eras, survives costs and baseline), **Mixed** (some eras), **Weak/Anecdotal** (few episodes or one era), **Not supported**. Do not upgrade a grade to be useful.
7. Separate **what happened** (data) from **why it probably happened** (theory). Name the theory's source and say it is a hypothesis.
8. Where the literature disagrees (e.g. "do cuts help stocks?"), show both sides with their numbers.

### Output format
1. **One-page summary:** the 5 to 10 findings that survived, each in one plain sentence with its grade and n.
2. **Playbook tables:** event x sector (median 3m/6m/12m relative return, % positive, n, grade) and event x stock-trait.
3. **Counter-examples page:** the times it failed, and the one-line difference.
4. **What did not hold up:** the popular beliefs you tested and rejected, with the numbers.
5. **Method appendix:** event definitions, data sources with dates fetched, code (reproducible, fixed seeds), limitations.
6. **A machine-readable file** (CSV/JSON) of every table, so the app can read it instead of copying numbers by hand.

### Style
Simple English, short sentences, jargon last. Numbers over adjectives. No "bullish/bearish/strong/weak" as verdicts (the Grade labels above describe the evidence, not the stock). Every sentence that a trader could act on must carry its sample size.

### Out of scope
Predicting the next move; price targets; position sizing; anything that tells the user to buy or sell; options; crypto.

---

## Notes for us (not part of the prompt)
- Fits the app's top-down flow: Context tab -> Sectors tab -> Analyze tab. The playbook would be a read-only reference page with a "not tested live" label; it must not change any card's verdict.
- Prior art already in the repo to reuse, not redo: Trading Principles comparison (Day 107), the Day 107 volume/momentum backtest spike (no edge found, SimFin universe drift, Golden Rule 45), MR entry-basis correction (Golden Rule 60), `sector_quadrant_history` and RRG work.
- Honest expectation: most macro -> sector patterns are weak or era-dependent. A result of "most popular beliefs are Weak/Mixed" is a good outcome, not a failure.
- Process before any build: this prompt -> run -> user reviews findings -> written plan -> Opus review -> go.
