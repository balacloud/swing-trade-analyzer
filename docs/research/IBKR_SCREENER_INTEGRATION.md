# IBKR 2.0 Market Screener — Integration with STA

> **Purpose:** Document IBKR screener capabilities and define a maximally-leveraged filter set that pre-qualifies candidates before STA deep analysis. Every filter uses data IBKR has in real-time that STA cannot easily provide at market-wide scale.
> **Created:** Day 76 (May 18, 2026)
> **Status:** Research / Design — skill not yet built

---

## The Core Idea

Two-stage pipeline. IBKR does the wide funnel (7,000+ → ~50) using real-time data and factors STA doesn't have. STA does the deep funnel (50 → 5–10) using Trend Template, S/R levels, patterns, trade setups, and verdicts.

```
IBKR Screener (7,000+ stocks, real-time)
    ↓  14 filters — 3 tiers (see below)
    ↓  ~30–80 survivors
User pastes screenshot(s) → /ibkr-scan skill
    ↓  Claude parses tickers + visible column data
    ↓  calls STA API for each (analyze + SR + MR)
    ↓  ranks by verdict + R:R + pattern
Top 5–10 high-conviction candidates
```

---

## Filter Design Principles

### What IBKR has that STA cannot provide at scale
| IBKR Capability | Why It Matters | STA Gap |
|----------------|----------------|---------|
| Real-time price vs EMA(20/50/200) | Minervini Trend Template at scale, instantly | STA computes TT per-ticker only after you request it |
| EarnGrw% | Earnings acceleration = institutional buying fuel | STA has revenue growth, not earnings growth separately |
| Inst. Percent Held | Minervini sponsorship requirement | STA never checks institutional ownership |
| Quick Ratio | Financial health tighter than D/E | STA uses D/E only |
| Analyst Target/Price Disparity % | Analyst-confirmed upside = catalyst validation | STA has no analyst data |
| MACD Histogram | Real-time momentum confirmation | STA checks MACD but only per-ticker after request |
| Average Option Volume + 52W IV Rank | OptionsIQ eligibility pre-check | STA has no options data |
| Fee Rate + Utilization | Short squeeze fuel quantified | STA has no short metrics |
| Change % (live) | Positive on the day = money flowing in now | STA's OHLCV is cached, not live |

### What IBKR cannot do that STA does
| STA Capability | Why It's Irreplaceable |
|---------------|----------------------|
| RS vs SPY (52-week) | IBKR has no direct RS ratio — Price/EMA(50) is a proxy only |
| RSI (14) | Not available as an IBKR factor |
| S/R levels + touch counts | Unique to STA's clustering engine |
| Pattern detection (VCP, Cup & Handle) | Unique to STA |
| Trade setup (entry, stop, target, R:R) | Unique to STA |
| Earnings proximity warning | IBKR has no earnings date filter |
| Mean reversion signal | Unique to STA |
| Position sizing (VIX-adjusted) | Unique to STA |

**Implication:** IBKR filters for everything it knows. STA validates what IBKR cannot see. Zero overlap = zero redundancy.

---

## Complete Filter Configuration

### Tier 1 — Structure Gates (eliminates ~80% of market)
*These establish the basic quality and trend structure. ALL must pass.*

| # | Factor | Operator | Value | Rationale |
|---|--------|----------|-------|-----------|
| 1 | Market Cap | Greater Than | 1B | Cap-aware: avoids micro-caps where STA stops are unreliable and institutional data is noisy |
| 2 | Average Volume ($) | Greater Than | 5,000,000 | STA liquidity floor. Below this, spreads widen, stops slip, patterns are unreliable |
| 3 | Last | Greater Than | 10 | No penny stocks. STA MR engine requires >$5; swing trades need price stability |
| 4 | Price/EMA(200) | Greater Than | 1.05 | Trend Template #1: above 200 EMA with 5% buffer. Buffer ensures EMA is rising, not just touched |
| 5 | Price/EMA(50) | Greater Than | 1.0 | Trend Template #4: above 50 EMA. Combined with #4 this implies 50 EMA > 200 EMA (Stage 2) |
| 6 | Price/EMA(20) | Greater Than | 1.0 | Trend Template #7: above 20 EMA. Short-term trend intact = stock is actively being accumulated, not consolidating below short MA |

**After Tier 1: ~300–500 survivors**

---

### Tier 2 — Fundamental Quality Gates (eliminates another ~60%)
*These ensure earnings and institutional backing — what drives sustained Stage 2 moves.*

| # | Factor | Operator | Value | Rationale |
|---|--------|----------|-------|-----------|
| 7 | ROE | Greater Than | 15 | STA fundamental Strong threshold. Buffett/Minervini minimum for capital efficiency |
| 8 | EarnGrw% | Greater Than | 10 | Earnings acceleration is what brings institutional buyers in. Revenue growth alone is insufficient — earnings are what actually move stock prices in Stage 2 |
| 9 | Inst. Percent Held | Greater Than | 25 | Minervini's explicit sponsorship requirement. <25% = no institutional accumulation phase. STA never checks this — IBKR is the only place we get it |
| 10 | Quick Ratio | Greater Than | 1.0 | Financial health: current liquid assets cover current liabilities. Filters out companies that look good on earnings but are one credit crunch away from trouble. STA's D/E misses this |

**After Tier 2: ~80–150 survivors**

---

### Tier 3 — Momentum Confirmation Gates (narrows to final ~30–80)
*These confirm the stock is moving NOW, analysts back it, and the market is participating.*

| # | Factor | Operator | Value | Rationale |
|---|--------|----------|-------|-----------|
| 11 | MACD Histogram | Greater Than | 0 | MACD histogram positive = price momentum accelerating above signal line. Confirms Stage 2 is active right now, not just on the chart historically |
| 12 | Analyst Target/Price Disparity % | Greater Than | 10 | Analysts see >10% upside to consensus target. This is not a primary signal but it validates: smart money with full 10-K access also sees value. Eliminates stocks that have already been fully priced in |
| 13 | Change % | Greater Than | -2 | Falling knife filter. Stocks dropping >2% today are showing distribution — counter to accumulation thesis. Allows slight pullbacks (good entry) while eliminating active selling |
| 14 | Average Option Volume | Greater Than | 100 | Minimum options market liquidity. Required for OptionsIQ auto-flagging. Also signals: institutions use options to hedge positions, so option volume > 100 avg implies institutional participation |

**After Tier 3: ~30–80 survivors (target)**

---

### MultiSort Configuration (rank survivors by quality)
*Applied to all survivors — top of list = highest conviction.*

| Priority | Factor | Direction | Why |
|----------|--------|-----------|-----|
| 1st | Price/EMA(50) | Higher Values | Best proxy for RS vs SPY available in IBKR. High = outperforming the index. STA validates exact RS later. |
| 2nd | EarnGrw% | Higher Values | Earnings acceleration magnitude — higher = bigger institutional catalyst |
| 3rd | Inst. Percent Held | Higher Values | More institutional ownership = more accumulation-phase conviction |
| 4th | Average Volume ($) | Higher Values | Larger dollar volume = bigger institutional footprint |

---

### Recommended Columns to Display in IBKR Output
*These don't filter but give Claude more signal when parsing the screenshot.*

| Column | What It Tells Claude |
|--------|---------------------|
| Market Cap | Cap-size tier for STA (large/mid/small thresholds) |
| Change % | Today's price action — positive = momentum today |
| Average Volume ($) | Claude computes RVOL ratio if Volume ($) also shown |
| Volume ($) | Today's dollar volume — vs average = real-time RVOL proxy |
| 52 Week High | Claude checks proximity (within 25% of high = Minervini TT criterion 5) |
| 52 Week IV Rank | OptionsIQ eligibility flag: IV Rank < 30 = cheap options |
| EarnGrw% | Already a filter but showing value helps Claude prioritize |
| Inst. Percent Held | Same — visible in output helps ranking |
| Price/EMA(50) | Confirms momentum tier |
| Analyst Target/Price Disparity % | Upside visibility for ranking |

---

### Optional Overlay: Short Squeeze Candidates
*Save as a separate IBKR screener — run alongside the main one.*

| Factor | Operator | Value | Reason |
|--------|----------|-------|--------|
| Fee Rate | Greater Than | 10 | High borrow cost = heavy short interest |
| Utilization | Greater Than | 80 | >80% of available shares borrowed = supply exhaustion |
| Average Volume ($) | Greater Than | 10,000,000 | Squeezes need high liquidity to sustain |
| Price/EMA(200) | Greater Than | 1.0 | Squeeze into uptrend (not catching falling knives) |

---

## What the 14-Filter Setup Produces

| Market Condition | Expected Survivors |
|-----------------|-------------------|
| Bull Trend (like current May 2026) | 50–80 stocks |
| Late Bull / Distribution | 30–50 stocks |
| Correction / Bear | 5–20 stocks (fewer survivors = fewer trades = right behaviour) |
| Recovery | 20–40 stocks (expanding) |

The filter is **self-calibrating** — in a bad market, fewer stocks pass, so fewer trades are taken. This is the correct behaviour for a swing system.

---

## Skill Design: `/ibkr-scan`

### Input
User pastes one or more IBKR screener screenshots directly into the Claude conversation, then types `/ibkr-scan`.

### What Claude does

**Step 1 — Parse screenshots**
Read all pasted screenshots. Extract:
- Every ticker symbol visible
- Any visible column values (Market Cap, Change %, Volume ($), Average Volume ($), EarnGrw%, Inst. Held, 52W High, IV Rank, etc.)
- Note how many tickers total across all screenshots

**Step 2 — Confirm STA is running**
Check `curl http://localhost:5001/api/cache/status` — if backend is down, stop and tell user to run `./start.sh`.

**Step 3 — Run STA API for each ticker**
For each parsed ticker, call in parallel:
- `GET /api/analyze/<ticker>` → verdict, categorical assessment, trade setup, R:R
- `GET /api/sr/<ticker>` → S/R levels, pattern detection, ATR, RS52W
- `GET /api/mr/signal/<ticker>` → mean reversion signal

**Step 4 — Score and rank**

| Signal | Points |
|--------|--------|
| Verdict: BUY | 3 pts |
| Verdict: HOLD | 2 pts |
| Verdict: AVOID | Eliminated |
| Technical category: Strong | +1 pt |
| Fundamental category: Strong | +1 pt |
| Pattern detected ≥ 80% | +1 pt |
| R:R ≥ 3:1 | +1 pt |
| MR signal active | +1 pt |
| 52W IV Rank < 30 (from IBKR screenshot) | +1 pt (OptionsIQ flag) |
| **Max score** | **9 pts** |

**Step 5 — Output top 5–10**

```
# IBKR Scan — [date]
## [N] tickers parsed → [M] passed STA filter → Top [K] shown

---
### #1 TICKER (score: X/9) — BUY
Technical: Strong | Fundamental: Strong | Risk: Favorable
Entry: $XX.XX (avg: $XX.XX) | Stop: $XX.XX | Target: $XX.XX | R:R: X.X:1
Pattern: VCP 92% formed — trigger above $XX.XX on >1.5x volume
MR: inactive
⚡ OptionsIQ candidate — IV Rank low (from IBKR)
[IBKR data: EarnGrw% +28%, Inst. Held 42%, Mkt Cap $8.2B]

### #2 TICKER (score: X/9) — BUY
...

---
## Watchlist — monitor for entry (HOLD)
TICKER1 (score 4), TICKER2 (score 4), TICKER3 (score 3)

## Eliminated (AVOID or data error)
[list with reason: "AVOID verdict", "R:R < 2:1", "API error"]

## ⚠️ Earnings warning
[Any ticker with earnings < 7 days — STA flags these]
```

---

## The Compounded Edge

| Stage | What Gets Eliminated | Surviving Signal |
|-------|---------------------|-----------------|
| IBKR Tier 1 (structure) | Downtrends, sideways, illiquid | Above all 3 EMAs, liquid |
| IBKR Tier 2 (fundamentals) | Weak earnings, no institutional backing | Profitable, growing, sponsored |
| IBKR Tier 3 (momentum) | Stalled, analyst-priced-in, falling | Active accumulation today |
| STA filter | No pattern, bad R:R, overbought RSI | Actionable setup with defined risk |

A stock that survives all 4 stages has passed:
- Real-time structure check (IBKR)
- Fundamental quality check (IBKR)
- Momentum confirmation (IBKR)
- Pattern + trade setup + R:R validation (STA)

This is Minervini's full process automated into a 15-minute morning workflow.

---

## Open Questions

1. **Survivor count** — paste the first screenshot after applying all 14 filters. That tells us if thresholds need adjusting.
2. **Which columns** are visible in your IBKR output? The skill parses whatever it sees — more columns = richer output.
3. **Multiple pages** — if survivors > 50, paste multiple screenshots and the skill handles them sequentially.
4. **Squeeze screener** — want to save that as a second IBKR screener save alongside the main one?
