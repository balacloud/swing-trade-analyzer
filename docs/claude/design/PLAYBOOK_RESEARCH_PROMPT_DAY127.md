# Research prompt: "Why stocks move" playbook, tested against the user's 117 tickers (draft v2, Day 127)

Purpose: one research run that builds a top-down playbook, **macro event -> sector -> stock**, and then **applies it to the user's own 117 tickers** (`backend/audit_universe.txt`). Two layers: (A) long history (1926 to today) at macro and sector level, where 100 years of data exists; (B) the 117 tickers over whatever real history each one has, as a check and a lookup. Not a trading system, not advice: the user decides every trade.

Paste everything below the line.

---

## PROMPT

You are a market historian and a skeptical quantitative researcher. Build a **top-down playbook that explains why stocks move**, then test and apply it on a fixed list of 117 tickers.

### The user and the use
A discretionary swing trader (days to weeks). They read a macro backdrop (rates, inflation, growth, credit, volatility, the dollar, oil), then pick sectors, then stocks. For each macro event they want: **what usually happened next, in which sectors, in which kinds of stocks, how often, and how often it did NOT, and where each of MY 117 names sits in that picture.** They make every trade decision. The page that uses your work states **facts and base rates, never verdicts or predictions**.

### The fixed universe (the 117)
The tickers are in `backend/audit_universe.txt` (provided with this prompt). Mix: ~47 US stocks, ~13 Canadian stocks, ~13 US ETFs, ~15 Canadian ETFs, ~8 CDRs (Canadian receipts of US stocks), ~19 US leveraged ETFs, 2 Canadian leveraged ETFs. First step, before any analysis:
1. **Map every ticker** to: country, exchange and currency, asset class, GICS sector and industry (or "ETF: what it holds"), market-cap bucket, and **first available trading date**. For leveraged ETFs and CDRs also map the **underlying** (e.g. NVDL -> NVDA, AMD.TO -> AMD) and the leverage (2x/3x, daily reset). Show this table.
2. **Flag what cannot be tested:** tickers with under 3 years of history, tickers that only exist since the last rate cycle, and any ticker whose data is close-only or has known split problems. Mark them "too short to test", never fill them in.

### The path to cover (in this order)
1. **Macro events**, each with a rule a computer can check (dates/thresholds), not a story: Fed cuts (start of a cutting cycle vs "insurance" cut vs cut during recession), hikes, yield curve (inversion, re-steepening), inflation surprises, recessions (start/end, NBER), credit-spread widening, VIX spikes, dollar moves, oil shocks, QE/QT, tariffs and fiscal shocks.
2. **Sector response (Layer A, long history).** For each event: which sectors beat or lagged the market over 1, 3, 6, 12 months after, with the spread of outcomes. Use Fama-French industry portfolios before GICS existed; sector ETFs (SPDR XL*) after ~1999.
3. **Stock-trait response (Layer A).** Within a sector, what separated winners from losers: size, value/growth, momentum, quality, leverage, beta, earnings revisions, dividend yield. Which traits repeat across eras and which flipped.
4. **The 117 (Layer B).** For each ticker, through its own real history:
   - How it behaved in each macro event (relative to its sector ETF and to SPY/XIU), with n = the number of events it actually lived through.
   - Does it behave like its sector's long-history pattern, or differently? (A stock that does the opposite of its sector is a finding, not noise.)
   - **Leveraged ETFs:** separate the underlying's move from the leverage and decay: show the underlying, the fund, and the gap, per event. Volatility drag is arithmetic; show it as numbers.
   - **CDRs and Canadian tickers:** show the effect of CAD/USD and the hedge, not just the US move.
5. **Lookup output:** for each of the 117, one row: its sector, the macro events where history says it tends to do better/worse than the market (with n and grade), and the events where it has no usable history.

### Questions each finding must answer
- Average **and** range (median, 25th/75th percentile, worst case, % of episodes positive).
- **How many independent episodes?** Overlapping windows are not independent. "n = 14 cutting cycles", not "n = 3,000 days".
- Does it hold in every era (1926-45, 1946-65, 1966-81, 1982-99, 2000-2012, 2013-today) or only some?
- The **counter-example set**: when the pattern failed and what was different.
- Is it still there after costs, and could someone have known the rule at the time?
- What was already priced in (sector moved BEFORE the event)?

### Bias warnings the user must see (state them in the report)
- **The 117 are a hand-picked, current watchlist.** They are winners and favourites chosen with hindsight, so their own past returns say nothing about whether the playbook works in general. **Layer A (all stocks, all eras, delisted names included where the data allows) is the evidence; Layer B is only the lookup and a sanity check.** Never use Layer B returns to "prove" a Layer A pattern.
- Many of the 117 are young (leveraged ETFs, CDRs): they have few or no events. Say so per ticker.
- Data you could not get is "not tested". Never fill a gap with a plausible story.

### Data (name the exact source and fetch date for every number)
Prefer free, citable, long-history: Ken French data library (from 1926), Shiller (from 1871), FRED (Fed funds, yield curve, CPI, unemployment, credit spreads, NBER recession dates), Yahoo/Twelve Data/Tradier for ETFs and the 117 (dividend-adjusted closes; state the adjustment). Use data as first published where revisions matter (CPI, GDP). Cross-check at least the 117's closes between two sources for the events used.

### Method rules (non-negotiable)
1. **Write the event rule before looking at results** and keep it. No re-cutting until something works.
2. Count **episodes**, not days. Sample size next to every number.
3. Guard against **survivorship**, **look-ahead** and **regime change** (0% vs 5% rates, pre/post-1971).
4. Compare every result to a **baseline** (the market on random dates). Not beating random dates = not a pattern.
5. Plain effect size ("median +3 points over 6 months, in 9 of 14 episodes") then a confidence statement. **Count how many things you tested**; the best-looking results are suspect.
6. Grade every finding: **Strong** (many episodes, all eras, survives costs and baseline), **Mixed** (some eras), **Weak/Anecdotal** (few episodes or one era), **Not supported**, **Not tested** (no data). Never upgrade a grade to be useful.
7. Separate **what happened** (data) from **why it probably happened** (theory; name the source; say it is a hypothesis).
8. Where the literature disagrees (e.g. "do cuts help stocks?"), show both sides with numbers.
9. Reproducible: fixed seeds, code in the appendix, a data-fetch log.

### Output format
1. **One-page summary:** the 5 to 10 findings that survived, each one plain sentence with grade and n.
2. **Universe table:** the 117 mapped (sector, class, first date, underlying, testable yes/no).
3. **Playbook tables:** event x sector (median 3m/6m/12m relative return, % positive, n, grade); event x stock-trait.
4. **The 117 lookup:** one row per ticker (see step 5).
5. **Counter-examples page** and **What did not hold up** (popular beliefs tested and rejected, with numbers).
6. **Method appendix:** event definitions, sources, code, limits.
7. **Machine-readable files** (CSV/JSON) of every table, keyed by ticker and event id, so the app reads them instead of copying numbers by hand.

### Style
Simple English, short sentences, jargon last. Numbers over adjectives. No "bullish/bearish/strong/weak" as verdicts on a stock (the Grade labels describe the evidence only). Every actionable sentence carries its sample size.

### Out of scope
Predicting the next move, price targets, position sizing, anything that tells the user to buy or sell, options, crypto.

---

## Notes for us (not part of the prompt)
- Fits the flow Context tab -> Sectors tab -> Analyze tab. The playbook would be a read-only reference with a "history, not a forecast" label; it must not change any card's numbers.
- Reuse, do not redo: Trading Principles comparison (Day 107), the Day 107 volume/momentum backtest spike (no edge, Golden Rule 45), MR entry-basis correction (Golden Rule 60), `sector_quadrant_history`, RRG work.
- **Order matters:** run the data-source audit (Round 2) first, because Layer B uses the same 117 tickers' price data; a wrong split (SOXL.NE, QPUX) would poison every event result. Layer B must use only tickers that pass the source audit.
- Honest expectation: most macro -> sector patterns will be Weak or era-dependent. "Most popular beliefs are Weak/Mixed" is a good outcome.
- Process before any build: this prompt -> run -> user reviews findings -> written plan -> Opus review -> go.
