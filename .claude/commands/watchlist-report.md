# Watchlist Catalyst Report

Take a pasted broker watchlist (IBKR/TWS-style export — ticker, name, currency,
last, change%, bid/ask, volume, 52-week high/low, EMA(200)/EMA(50) ratios) and
produce a research report: what's actually moving each name, the regime/
sector context around it, any earnings-driven event risk in the next 10 days,
and a small set of risk/entry-readiness technical indicators bucketed
most-actionable-first. Publishes as a single, durable Claude Artifact — **not**
a live STA feature, no ledger, no automated signal, no buy/sell verdict.
Informational + risk-framing research only, same spirit as the Sector
Pullback Screener.

**Day 103 design decision (user-confirmed, after checking sibling-project
precedent first — Trading Intelligence Hub's Options Sieve gate pattern and
its own Sector Advisory Panel's "alerting, never deciding" rule, and STA's
own `breakout_detection.py` most-actionable-first bucketing):** "more
actionable" means giving the trader what they need to size and risk-manage a
position (PERSONA.md Core Principle 2 — position sizing/risk matters ~90%,
entry signal ~10%), not telling them what to buy. The readiness bucketing
below (Step 4) describes current technical STATE, never a verdict — same
line the Hub itself draws for its own closest analog to this tool.

**Why general web research, not STA's own regime engine:** confirmed with the
user (Day 103) — this skill is for thematic/niche ETF watchlists (uranium,
space tech, quantum, robotics, critical materials, and similar), which don't
map cleanly onto STA's 11 broad GICS sectors. STA's own Sectors tab / Market
Phase engine stays the right tool for broad-sector, single-stock work; this
skill is deliberately a separate, web-research-driven tool for this
different use case.

## Step 1: Parse the pasted watchlist

Extract, per row: ticker, full name, currency (CAD/USD — matters, several
names here are cross-listed in both, e.g. `XCHP` (CAD) and `SOXX` (USD) are
literally the same iShares Semiconductor ETF, not two different funds — call
that out explicitly if it recurs, don't silently treat them as unrelated),
last price, change %, 52-week high/low, and the Price/EMA(200) and
Price/EMA(50) ratios if present (these are a cheap, already-computed
"how extended is this" signal — a name at +20% over its 200-EMA is far
different context than one sitting flat on it).

Broker paste formats vary (tabs, multiple spaces, stray `—` for missing
fields) — be tolerant of formatting, but if a row is genuinely ambiguous
(can't confidently extract a ticker), ask rather than guess.

If fewer than ~5 rows are provided, ask if this is really the intended
watchlist before running a full report — this skill is built for a themed,
multi-ETF paste, not a single quick lookup (use the app's own Analyze/Scan
tabs for that).

## Step 2: Compute the readiness indicators (reuse STA's own functions, don't reinvent)

Four indicators, deliberately kept short (PERSONA.md's "overfitting disguised
as rigor" pitfall — more indicators isn't more diligence, it's more ways to
fool yourself):

1. **Trend vs. 200-EMA** — already in the pasted data (`Price/EMA(200)`).
2. **RSI(14)** — short-term momentum/overbought read.
3. **Relative volume** — today's volume vs. its 20-day average. **Display
   only, never a bucket gate** — see the caveat below, this metric is
   structurally unreliable while the market is still open.
4. **ATR-based stop distance** — `ATR(20) / last_close`, as a %. Not a
   recommended stop, a *distance a disciplined stop would plausibly sit at*
   — the input a trader needs to size a position (PERSONA.md Core Principle
   2), not a signal.

**Relative volume's partial-bar problem (found live-testing this exact
step, Day 103):** `volume.iloc[-1]` from a same-day yfinance fetch is
*today's volume so far*, not a completed session's — comparing it against
`rolling(20).mean()` of complete prior days is the same partial-bar
mismatch Golden Rule 39 already found and fixed in the live paper-trading
engine, just in a new shape. Live-tested against this project's real Day
103 watchlist: nearly every ticker read 0.3x-0.9x relative volume
regardless of actual conviction, simply because the fetch ran mid-session.
**Never use this metric to gate a bucket** — display it with an explicit
"as of [time], partial session" caveat, or better, compute it against
*yesterday's* completed volume vs. the 20-day average instead of today's
running total, if the report is generated during market hours.

**RSI(14) alone understates a stretched long-term trend (found live-testing
this same step):** RSI(14) is a *short-term* oscillator — a name can sit
20%+ above its 200-EMA (genuinely extended on the trend that matters for
entry timing) while RSI(14) reads neutral, if the last 14 days themselves
included a pullback. Live-tested case: SMH/SOXX sat at RSI≈50-52 (neutral)
while +21-23% above their 200-EMA, right after a real, named "stretched
valuations" selloff the catalyst research (Step 5) independently
identified — RSI(14) alone would have called these "not extended," directly
contradicting the report's own narrative. **"Extended" must check BOTH
signals**, not RSI in isolation — see Step 4's corrected bucket definition.

**Prefer IBKR MCP over yfinance when it's available (Day 103 update, found
live-testing a real IBKR-sourced re-run of this exact watchlist).** The
user's own pasted watchlist is sourced from their real IBKR/TWS account —
when the `mcp__claude_ai_Interactive_Brokers_IBKR__*` tools are connected,
use them as the primary OHLCV source, not an approximation of it:
1. `get_watchlists` → find the matching list by name/tag, get its `id`.
2. `get_watchlist` with that `id` → real `contract_id_ex` per ticker,
   matched by name against the pasted rows.
3. `get_price_history` per `contract_id` (`security_type="STK"`,
   `step="ONE_DAY"`, `period="THREE_MONTHS"`, `outside_rth=false`) — enough
   bars for RSI(14)/ATR(20). Still compute the actual math via STA's own
   `calculate_rsi`/`calculate_atr_series` (imported below) — only the data
   source changes, not the computation method, same DRY discipline as the
   yfinance path.

**Critical: parallel `get_price_history` calls do not reliably return
results in call order.** Confirmed live (Day 103, 24-ticker batch) — two
adjacent results came back transposed relative to their tool_use order, and
would have silently mislabeled two tickers' entire OHLCV series if trusted
positionally. Before using any batch of parallel IBKR history results,
verify each block's identity by its own last `close` value (or, for
close-clustered tickers, its `volume` scale) against a trusted reference —
the watchlist's own pasted `Last` price is sufficient. If more than ~4
contracts are batched together and any two expected last-close values are
within a few percent of each other, re-fetch that ambiguous subset in
smaller batches (or one at a time) rather than guessing from proximity
alone. Never skip this check — the failure mode is silent, not an error.

**yfinance fallback** (if IBKR MCP is unavailable, or for tickers IBKR
doesn't resolve): batch-fetch OHLCV via yfinance and reuse STA's own
already-tested indicator functions directly — do not reimplement RSI or ATR
by hand, that's exactly the "dual implementation, silent drift" failure this
project's Golden Rule 21/40 already got burned by elsewhere:

```python
import sys
sys.path.insert(0, '/Users/balajik/projects/swing-trade-analyzer/backend')
sys.path.insert(0, '/Users/balajik/projects/swing-trade-analyzer/backend/backtest')
import yfinance as yf
from backend import calculate_rsi          # backend.py — reused, not reimplemented
from trade_simulator import calculate_atr_series  # trade_simulator.py — same

data = yf.download(tickers, period='3mo', progress=False, group_by='ticker')
# per ticker: close/high/low/volume = data[t][...].dropna()
# rsi14 = calculate_rsi(close, period=14)
# atr20 = calculate_atr_series(high, low, close, period=20).iloc[-1]
# rel_vol = volume.iloc[-1] / volume.rolling(20).mean().iloc[-1]
# atr_stop_pct = atr20 / close.iloc[-1] * 100
```

One batch call, not per-ticker requests (Golden Rule 25/40 — a tight loop of
individual calls is what trips rate limiters). Note `calculate_rsi` returns
the latest float value directly, not a Series — no `.iloc[-1]` needed.

**Canadian-listed tickers** (no `.TO`-style suffix in the pasted symbol)
often won't resolve on the bare ticker via yfinance — retry with `.TO`
appended if the bare symbol returns no data, same fallback STA's own backend
already uses elsewhere for TSX names.

**Same-fund cross-currency duplicates** (e.g. `XCHP`/`SOXX`): fetch once
(prefer the USD listing — more reliably resolves on yfinance), apply the
same readings to both rows, and say so explicitly rather than fetching twice.

If a ticker's OHLCV won't resolve at all after the `.TO` retry, don't fail
the whole report — mark that row's indicators "unavailable" and continue;
say so plainly in the report rather than silently omitting the row.

## Step 3: Group by theme, not by row

Research theme-by-theme, not ticker-by-ticker — most of these watchlists
cluster into a handful of real themes (uranium, gold miners, semiconductors,
space, AI/robotics, EV/autonomous, copper/critical materials, clean-
energy grid, memory, quantum), and a single well-targeted search per theme
covers every ETF in it far more efficiently than 20+ individual per-ticker
searches. Group the parsed list into themes first (infer from fund name +
known composition — e.g. `SMH`/`SOXX`/`XCHP` → semiconductors; `HURA`/`URA` →
uranium; `XGD`/`GDX` → gold miners), then research each theme once.

For names that don't cleanly fit a theme cluster, research individually.

## Step 4: Bucket by readiness state, most-actionable-first

Using Step 2's indicators, bucket every ticker into one of four states —
same most-actionable-first convention as `breakout_detection.py`'s 8-state
engine, deliberately condensed to 4 here since these are diversified ETFs,
not single stocks with pattern-level detail to report:

- **🟢 Ready** — price above 200-EMA AND *not* extended by either measure
  below. Trend intact, room to run before either signal flags stretched.
- **🟡 Extended** — price above 200-EMA but extended: RSI(14) ≥ 65 **or**
  Price/EMA(200) ≥ +15%. Deliberately an OR, not an AND, per the RSI(14)
  caveat in Step 2 — a name can be extended on the long-term trend measure
  while its short-term RSI looks calm (or vice versa after a sharp,
  fast move), and either one alone is a real reason to flag it. Trend
  intact, but stretched — a pullback risk, not a trend-failure risk.
- **🔴 Below trend** — price below its 200-EMA, regardless of RSI. Whatever
  the catalyst narrative says, price hasn't confirmed it yet.
- **⚪ Unclassified** — no 200-EMA available (fund too new) or indicators
  didn't resolve. State this plainly; don't force a bucket.

Relative volume is never part of this bucket logic (see Step 2's caveat) —
report it in the per-ETF table as context, not as a gate.

This is a **state description, not a recommendation** — say so directly in
the report. "Ready" means "the mechanical trend/extension checks are
clear," not "buy this." A 🟢 name can still be a bad idea for other reasons
(weak catalyst, poor liquidity, doesn't fit the account's risk budget) and a
🔴 name isn't automatically avoid-forever — it's where price and story
currently disagree, which is itself the useful thing to know.

## Step 5: Per theme — catalyst + regime research (WebSearch)

For each theme cluster, search for:
1. **What's actually moved this specific group in the last few trading
   days** — a real catalyst (a rate decision, a specific company's earnings
   moving the whole sub-industry, a regulatory/policy event, a commodity
   price move), not a generic "markets were up today."
2. **Where the theme sits directionally right now** — genuinely up-trending,
   rolling over, choppy/range-bound — stated plainly, sourced from what the
   search actually returns, not inferred from the pasted price data alone
   (the EMA ratios already tell the price story; the search should add the
   *why*, not repeat the *what*).

Cross-check the search's read against the pasted data's own EMA ratios
before writing the report — if a search suggests "uranium is breaking out"
but the pasted `Price/EMA(200)` for `URA` shows -4.68% (below its 200-EMA),
say so explicitly rather than letting the two silently disagree. A
contradiction here is itself worth reporting, not smoothing over.

## Step 6: Per ETF — earnings/event risk within 10 days

For each ETF, identify its 3-5 largest underlying holdings (from known fund
composition — WebSearch if not confident) and check whether any report
earnings within the next 10 calendar days. Flag only real, large-weight risk
— a top-3 holding reporting is a real flag; an equal-weight fund's #40
holding reporting is not worth mentioning.

If an ETF has no meaningful single-company concentration (e.g. a broad,
diversified fund) or no holding reports within the window, say so plainly —
absence of risk is itself useful information, don't pad the report by
forcing a flag where none exists.

## Step 7: One market-wide regime paragraph

A single search for the current overall market regime (SPY vs. its 200-day,
VIX level, general risk sentiment) — once for the whole report, not per
ETF. This is context for reading every theme's individual result, not a
per-name data point.

## Step 8: Build the Artifact report

**Start the HTML content with `<meta charset="utf-8">` before the `<title>`
tag.** Found the hard way (Day 103, first real run of this exact step): this
report's copy is full of em-dashes, arrows, and middle-dots — without an
explicit charset declaration, the published Artifact rendered almost
completely blank (a couple of stray character fragments, nothing else),
while the same file viewed locally showed readable-but-garbled mojibake
text. Confirmed live: adding the meta tag fixed both. This isn't optional
styling — verify it's the very first thing in the file before publishing,
every time.

**After publishing, actually load the Artifact URL and look at it** — per
this project's own Golden Rule 6 ("never claim a result you haven't run")
and the dataviz skill's own "render it and look at it" step. A clean HTML
diff is not the same as a correctly rendering page.

**If the published page renders blank with no console error** (seen again
Day 103, on a re-publish of an already-working file with valid charset and
balanced HTML tags): first serve the file locally
(`python3 -m http.server` in its directory, then load
`http://localhost:<port>/<file>.html`) to confirm whether the file itself is
the problem or the platform's render of it is. If the local render is
clean, this isolates the issue to the Artifact platform, not the report —
retrying the publish once is reasonable, but don't loop on it; report the
isolated finding (file verified correct, platform render pending/broken)
rather than either claiming success or silently re-editing a file that
isn't the actual problem.

**Load the `artifact-design` skill before writing** (and `dataviz` if the
report includes any chart/color-coded visual beyond a plain table — likely,
given change% and EMA-extension data). Structure:

- Market regime paragraph at the top (Step 7)
- **Readiness buckets (Step 4) near the top, most-actionable-first** —
  🟢 Ready, 🟡 Extended, 🔴 Below trend, ⚪ Unclassified — each just a list
  of tickers, not yet the full narrative; this is the "where do I even look
  first" scan before the detail below
- Grouped by theme cluster, each with: the cluster's catalyst/regime
  narrative (Step 5), then a table of its ETFs — ticker, price, change%,
  Price/EMA(200), RSI(14), relative volume, ATR stop%, readiness bucket,
  earnings-risk flag (Step 6) if any
- Flag the `XCHP`/`SOXX`-style same-fund-different-currency duplicates
  explicitly if present, so the user doesn't read them as two independent
  data points
- A visible disclaimer: this is research/risk-framing context only, not a
  signal or recommendation — the readiness bucket is a description of
  current technical state, not a buy/sell call — matches the same framing
  convention as the Sector Pullback Screener and MR Signal Card elsewhere
  in this project

**Publish to a fixed, durable path so repeated runs update the same
Artifact URL rather than creating a new one each time** — same living-doc
convention as `docs/claude/design/HOW_STOCK_PICKING_WORKS.html`. Use
`/private/tmp/claude-501/.../scratchpad/watchlist_catalyst_report.html` (the
current session's scratchpad path) the first time, and check whether a
prior session's Artifact with this same title already exists (`Artifact`
tool, `action: "list"`) before publishing — if one does, update it via its
existing URL instead of minting a new one.

## Rules

- Never fabricate a catalyst, an earnings date, or a regime read — every
  claim in the report must trace to an actual search result. If a search
  comes back thin or ambiguous for a theme, say the read is uncertain
  rather than filling the gap with a plausible-sounding guess.
- Don't editorialize into a buy/sell recommendation for any name — report
  what's happening and why, the same "state, don't prescribe" discipline
  used elsewhere in this project (Breakout Watch's own rule, applied here).
  The readiness bucketing (Step 4) doesn't relax this — it's a mechanical
  description of trend/extension/volume state, not a verdict, and should
  read that way (see the Day 103 design decision note at the top of this
  file for why "more actionable" was scoped this way, not as a signal).
- The ATR stop% is a distance, not an instruction — never phrase it as "set
  your stop at X%," phrase it as "current ATR-based distance is X%."
- If the backend/app data would genuinely help for a *specific* name in this
  watchlist (e.g. the user also wants STA's own Analyze-page read on one of
  these), that's a separate, explicit ask — don't silently blend STA's own
  engine output into this skill's report.
