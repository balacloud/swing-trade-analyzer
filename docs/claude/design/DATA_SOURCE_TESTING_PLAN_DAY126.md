# Data Source Testing Plan (Day 126)

**Status:** PLAN, not built. Review: three passes by Claude after the build (user, Day 126: no Fable unless asked).
**Why:** The user trades US and Canadian stocks, ETFs and leveraged ETFs and asked: "are we getting accurate
info?" and "how good is our Data Sources tab?". Day 126 research found real data faults the tab could not see
(SOXL.NE: unadjusted split, 311 of 311 bars flat with zero volume). *(Corrected Day 126: an earlier draft also listed "7 CDRs with 0–1 bars". That was the wrong symbol: the CDRs trade on Toronto (`.TO`, 131–503 clean bars); `.NE` is a secondary venue.)*
**Rule for this plan:** a source is "accurate" only when it matches an independent truth. "It loaded" is not accuracy.

---

## 1. How good is the Data Sources tab today? (evidence from Day 126)

It answers **"where did this come from, and is it cached?"** It does **not** answer **"is this right?"**

| # | Finding | Evidence |
|---|---|---|
| 1 | **No quality signal at all.** SOXL.NE shows `yfinance / just_fetched` with 311 rows, exactly like a clean stock. | Pilot (§2): flat 311/311, split −67% on 2026-05-25 unadjusted, zero volume last 5 bars. The tab said nothing. |
| 2 | **No instrument identity.** No exchange, currency (USD vs CAD) or class (stock / ETF / leveraged). US SOXL ($55.97 USD) and Canadian SOXL.NE ($14.10 CAD) look the same. | `/api/provenance` returns only `ohlcv` and `fundamentals` cache info. Golden Rule 58 trap. |
| 3 | **"Rows" without dates.** No first date, last date or "last bar is stale". | `provenance.ohlcv.rows` only. |
| 4 | **The static Data Source Map is wrong.** It lists Stooq as the last resort, but Stooq is not in the chain (dead, Day 82). Tradier (the real 3rd source) is missing. | `orchestrator.py:88,92`: chain is Twelve Data → Yahoo → Tradier. |
| 5 | **The backend's `data_sources` block is hard-coded.** Says prices come from "Yahoo Finance" (US prices come from Twelve Data) and fundamentals from "Defeat Beta API" (stale, Known Issue Day 111). | `backend.py:/api/provenance` |
| 6 | **"Active source" is global, not per ticker.** It shows the last call's source (`ohlcv: yfinance`), so a US ticker can be labelled with a Canadian lookup's source. | `/api/health` `providers.active_sources` |
| 7 | **Quota view is partial, coverage view is missing.** The live tab does show calls left for Twelve Data (797) and Alpha Vantage (17) and live circuit-breaker state (good). It does not show which source serves which class (US / Toronto / Cboe Canada), nor Tradier's or EODHD's limits. *(Corrected Day 126: an earlier draft said there was no quota view at all.)* | Live tab, AAPL, Day 126 |
| 8 | **The indicator formula table is unverified.** Its formulas (ATR, RSI, ...) were never checked against the code in this pass. | Not tested; listed so it is not trusted by default. |
| 9 | **Fundamentals line can say "cached" for a fund that has none.** SOXL.NE shows `Fundamentals: CACHED, yfinance, age 0.7 days`, yet `/api/fundamentals/SOXL.NE` returns 404. Not traced why. | Live tab + curl, Day 126 |
| 10 | **The footer and map still name Stooq** (dead) **and omit Tradier**, which served 3,592 of ~9,600 logged OHLCV fetches. | Live tab; `backend.log` |

What the tab does well: the cache numbers (entries, size, hit rate), and per-ticker source + age for plain US and Toronto
tickers (AAPL → Twelve Data, RY.TO → Yahoo were correct in the pilot).

### Grade by class (data in STA today, then what the tab tells you)

Data grade = what the pilot structure checks show. **No class has been price-checked against IBKR yet**, so none is "verified accurate". Spot checks so far: TSX and AMD.NE closes within 0.1–0.3% of IBKR; QPUX, SPCL, UBOT, GDXU.TO match the user's IBKR screen.

| Class | Pilot tickers | Data (structure) | Tab honesty |
|---|---|---|---|
| US stock | AAPL, RIVN | Clean: 504 bars, no flats, no jumps (Twelve Data) | OK |
| US ETF | SPY, SMH | Clean | OK (fundamentals 404 is expected; wording untested) |
| US leveraged | TQQQ, QPUX, SOXL | Clean. Big jumps (QPUX +48%, SOXL +55%) look real; QPUX's 2026-03-23 reverse split was adjusted | OK, but no split check |
| Canada stock | RY.TO, SHOP.TO | Clean (Yahoo) | OK |
| Canada ETF | XIU.TO, XEQT.TO | Clean (Yahoo) | OK |
| Canada leveraged | GDXU.TO / **SOXL.NE** | GDXU.TO clean. **SOXL.NE bad** (see above). HSU.TO not found at all (old ticker?) | **Misleading** for `.NE`: looks fine, is not |
| Canada CDRs (use `.TO`) | AMD.TO, AVGO.TO, MU.TO, SNDK.TO, … | Clean on `.TO` (131–503 bars, no flat bars, no jumps). The `.NE` symbols have 0–1 bar | Shows `.NE` as "fetched" with 1 row, no warning |

---

## 2. Pilot already run (Day 126, 14 tickers, truth-free checks)

Bars, first and last date, flat zero-volume bars, jumps over 40%, zero volume in the last 5 bars, and what the tab says. Result: every class is
structurally clean except `.NE`. Reproduce with step 1 below.

---

## 3. The test design

### 3.1 Universe (Wave 1: exactly 24 tickers, all from the user's own IBKR watchlists)

*(Corrected Day 126: the first draft said "4 per class" but listed 28 and left two placeholders.)*

| Class | Tickers (STA symbol) | Why this one |
|---|---|---|
| **US stock** (3) | JPM, CAT, BRK-B | Large caps from `Quality_US_Canada`; BRK-B tests the dash symbol |
| **US ETF** (3) | SMH, SOXX, GDX | From `AI Supply Chain ETF`; SMH has no fundamentals (404 path) |
| **US leveraged** (4) | QPUX, DRAL, SPCL, UBOT | QPUX had a 1:3 reverse split (2026-03-23); DRAL ~100 days and SPCL ~154 days of history; UBOT is the clean control |
| **Canada stock** (4) | RY.TO, CNR.TO, ATD.TO, CSU.TO | From `Quality_US_Canada`; Toronto listings, CAD prices |
| **Canada ETF** (4) | XEQT.TO, VFV.TO, HXQ.TO, XCHP.TO | From `Long_Term_Quality_ETFs` |
| **Canada leveraged** (2) | GDXU.TO, SOXL.NE | The user's only two Canadian leveraged funds (BetaPro, 3:1 split 2026-05-25). GDXU.TO is the clean control, SOXL.NE the known-bad case |
| **CDRs, Canadian receipts of US stocks** (4) | AMD.TO, AVGO.TO, MU.TO, SNDK.TO | From `AI Supply Chain`. They trade on Toronto; the plan also checks the `.NE` mirror to confirm it should not be used |

**Wave 2:** URAA, COPZ, AVGC, GOOGL, JNJ, CNQ.TO, ATD/other CDRs (ANET, GEV, WDC, ASML), and **US SOXL (contract 73340487) as the wrong-fund control** next to the user's SOXL (805995437), since both are on one watchlist.

Symbols above are the STA/Yahoo form; the exact Yahoo symbol for BRK-B, CNR, ATD, CSU, HXQ, VFV and XCHP is **not yet verified**, so step 1 of the build resolves each one first and reports any that do not load.
Always take contract ids from the user's own watchlists, never by symbol search (Golden Rule 58), and show exchange + currency in every report row.

### 3.2 Truth sources
1. **IBKR (via Claude, MCP):** daily bars and corporate actions for the contract. Lean pull per ticker: last 10 daily bars + one year of weekly bars with `include_corporate_actions`. IBKR is split-adjusted. Note: its quotes are 15 minutes delayed, and its **volume is not comparable** to consolidated feeds (Day 122: IBKR ≈ 46–65% of Twelve Data/Yahoo), so volume is checked for plausibility, never equality.
2. **Cross-source agreement:** query every source that can serve the class (Twelve Data, Yahoo, Tradier, EODHD, Alpha Vantage) and diff the last 20 closes. Where IBKR and a source agree and another disagrees, the outlier is wrong.

### 3.3 Checks per ticker (pass / warn / fail)

| ID | Check | Pass | Fail |
|---|---|---|---|
| C1 | **Right instrument:** exchange, currency, name vs IBKR | same instrument | different fund / currency (e.g. US vs Canadian SOXL) |
| C2 | **Fresh:** last bar = last completed session (or flagged as forming) | yes | older than 1 session, or silently includes an unfinished bar |
| C3 | **Close accuracy:** last 5 closes vs IBKR | within 0.3% | over 1% |
| C4 | **OHLC integrity:** high ≥ open/close, low ≤ open/close; share of flat zero-volume bars | none / under 2% | over 20% flat |
| C5 | **Splits:** every jump over 40% matched to an IBKR corporate action, and adjusted | adjusted or real move | unadjusted split |
| C6 | **History length:** bars vs listing date; under 252 flagged | as expected | missing years |
| C7 | **Volume plausible:** nonzero, same order of magnitude as IBKR | yes | zero or wildly off |
| C8 | **Provenance honest:** the source the tab shows = the source the orchestrator actually used (trace logs) | equal | different |
| C9 | **Cross-source:** other sources' last 20 closes within 0.5% | agree | any provider disagrees: record which |
| C10 | **(Wave 2) Classification and fundamentals:** `quoteType` (EQUITY / ETF / leveraged), ETF skips fundamentals cleanly, Canadian stock fundamentals availability, earnings date | as expected | wrong class or silent gap |

### 3.4 Deliverables
- `backend/backtest/audit_data_sources.py`: runs C2, C4–C6, C8, C9 with no truth needed (cheap, repeatable, safe to run weekly). Takes a `--truth <folder>` option for C1, C3, C5, C7 once IBKR truth files exist.
- IBKR truth folder (`backend/validation_results/data_truth_YYYYMMDD/<ticker>.json`), written by Claude from the MCP calls.
- Report: `docs/test/DataSources_YYYYMMDD/REPORT.md`, a ticker × check matrix grouped by class, plus a one-line verdict per class.
- A **coverage matrix**: class × source → works / partial / no, built from C9 (this is the "which free source serves what" table).

### 3.5 Budget (rate limits, Golden Rule 25)
Twelve Data: free credits (a US ticker is cached by the app). Yahoo: unlimited but throttles. EODHD free: **20 calls a day, 1 year** (use only for the 6 Canada tickers in C9, split over two days if needed). Alpha Vantage free: 25 a day, 1 a second (the Toronto tickers only). IBKR: about 48 light calls, done in one session. All results cached on disk so a re-run costs nothing.

---

## 4. Order of work (each step: build, three review passes, show the result)

1. **Build `audit_data_sources.py` (truth-free) and run it on the 24.** Output: the first matrix. No app changes.
2. **IBKR truth capture** for the 24, then run C1, C3, C5, C7. This is the first time any class is called "verified accurate", or not.
3. **Decide routing from the matrix** (examples, not decisions): `.NE` → EODHD fallback and/or IBKR bars; known-split list for `.NE`; refuse levels when over 20% of bars are flat.
4. **Data Sources tab v2** (only after 1–3): per-ticker quality panel (exchange, currency, class, first/last bar, flat %, split check, cross-check result, source used), live source chain from the orchestrator (drop Stooq and Defeat Beta), per-class coverage matrix, provider quotas. Every element backed by a real field (engineering standard).
5. **Repeat monthly** (truth-free weekly via the script; truth checks on demand).

## 5. Out of scope
Paid sources (named, not tested). Fundamentals accuracy against filings. Intraday (4H RSI) feed accuracy. Changing any trading rule.

## 6. Decisions needed from the user
1. Is the 24-ticker Wave 1 list in §3.1 right (swap any)?
2. OK to spend about 48 IBKR calls and about 20 EODHD calls on it?
3. After the matrix: do we fix routing first (step 3) or the tab first (step 4)? Recommendation: routing first, because a nicer tab on wrong data helps nobody.

---

## 7. Tradier findings (Day 126, asked by the user: "is Tradier underused for US stocks?")

- **Not underused.** It is the 3rd source on paper (Twelve Data → Yahoo → Tradier) but `backend.log` shows it served **3,592** OHLCV fetches, vs 4,510 Yahoo and 1,482 Twelve Data. Twelve Data's free plan keeps hitting its limit, so Tradier does the work.
- **Quality on US names is good:** 0.2 s a call, production brokerage token, about 120 requests a minute, 501 clean days, no flat bars, volume within 0.1–2% of Yahoo, closes identical to the cent on 12 US stocks, ETFs and leveraged funds. Not dividend-adjusted (docstring), so old closes can sit 1–4% off Yahoo.
- **Forward splits are right** (ORLY 15:1, IBKR 4:1, FAST 2:1, TSCO 5:1: no break).
- **Reverse split is wrong.** QPUX (1-for-3, 2026-03-23): before 2026-03-20 Tradier's prices are exactly **3× too high** (171.87 vs 57.29 on one day), with a false −69% jump. Yahoo, Twelve Data and IBKR are continuous. A silent error in a source that serves about a third of fetches.
- **Gaps:** `BRK-B` and `BRK.B` return nothing (Tradier wants `BRK/B`); no Canada; only history and quotes are wired (intraday timesales exists at Tradier, untested here).
- **Decision for the audit:** promoting Tradier to first choice for US names is reasonable only with a guard: any result with a one-day move over 40% is cross-checked against the next source before it is accepted.

---

## 8. Step 1 result (Day 126, built and run)

`backend/backtest/audit_data_sources.py` ran on the 24 tickers; report: `docs/test/DataSources_20261114/REPORT.md`. It grades **every source in STA's chain** (not just the first, because Twelve Data's free plan is limited all day and Yahoo and Tradier serve most US fetches).

| Result | Detail |
|---|---|
| **Fails (2)** | **SOXL.NE** (100% flat zero-volume bars, unadjusted split, and the tab says nothing). **QPUX** (Tradier's reverse-split error: before 2026-03-20 prices 3× too high, false −69% jump). |
| **Clean** | US stocks and ETFs; Canadian stocks, Canadian ETFs; GDXU.TO; the CDRs on `.TO`. |
| **Warnings** | DRAL (100 bars), SPCL (154 bars; Twelve Data has only 150, starts 6 days late), AVGO.TO (225) and SNDK.TO (131) short history. Tradier has occasional bars with the close 0.2–0.3% outside the day's range (CAT, GDX, UBOT). |
| **Fall-through** | For 6 of the 10 US tickers the tab showed Yahoo, not Twelve Data (partly self-inflicted by the audit's own Twelve Data calls). |

**Review passes on the audit itself found and fixed:** (1) it assumed Twelve Data served US tickers, so it graded the wrong source; now every chain source is graded. (2) The tab-honesty check treated "a different source than expected" as fine. (3) It missed a source that starts later than another and ungraded volume ratios. (4) A one-cent rounding case caused a false warning; tolerance is now 0.1% of price. Known limits are listed at the foot of the report.

Next: step 2, IBKR truth capture for the 24 (closes, splits, volume), then the routing decision.

---

## 9. Step 2 result (Day 126): checked against IBKR

Truth: IBKR history on the user's own contracts (ids from the watchlists), 24 tickers, 47 light calls (one rate-limit retry: IBKR allows 30 a minute). Report: `docs/test/DataSources_20261114/REPORT_vs_IBKR.md`. Script: `backend/backtest/audit_vs_ibkr.py`; truth file: `backend/validation_results/ibkr_truth_20261114.json`.

- **22 of 24 pass every check on every source.** Closes match IBKR within 0.3% on settled days, history levels match at three month-ends (so splits are adjusted), and volume is plausible.
- **2 fail.** (1) **SOXL.NE** on Yahoo and EODHD: prices before 2026-05-25 are ×3.02 too high (unadjusted split); Yahoo also has zero volume. (2) **QPUX on Tradier:** ×3.00 too high before the 2026-03-23 1:3 reverse split. Both reproduce the earlier findings with the broker as the judge.
- **Splits handled correctly by every other source, including recent ones:** SOXX 3:1 on 2026-11-05, AMD CDR 7:1 on 2026-10-16, MU CDR 5:1 on 2026-03-10, GDXU 3:1 on 2026-05-25.
- **Volume is never equal across sources.** US sources (Twelve Data, Yahoo, Tradier) are identical to each other, at 1.15–2.09× IBKR. Canadian stocks: Yahoo 1.27–3.01× IBKR (RY.TO 3.01×). Canadian ETFs, CDRs and GDXU: 0.78–0.95×. Never mix or compare volume across sources.
- **A flaw in the truth, found and handled:** IBKR marks Canadian and some other contracts "delayed 900s", and its last history bar can be 15 minutes stale (SOXL.NE 2026-11-13: history bar 14.10, the user's watchlist 14.72, Yahoo 14.69, EODHD 14.72). C3 now grades the four settled days and reports the last day separately.
- **Limits:** one-day snapshot; three month-end levels per ticker; dividends not checked; Alpha Vantage not used.

**Next (step 3, routing):** SOXL.NE needs IBKR bars (or a verified split table plus a close-only warning); Tradier needs the 40%-jump cross-check before it is promoted for US names; Yahoo is good enough for Toronto names and the `.TO` CDRs, so the EODHD fallback is optional. Then the tab rebuild (step 4).

---

## 10. Step 4 status (Day 126): Data Sources tab v2 built

Built per `DATA_SOURCES_TAB_V2_PLAN_DAY126.md` after an Opus plan review. The tab now shows identity, a data-quality verdict (SOXL.NE = FAIL with the flat-bars reason; QPUX = WARN, with the audit line "tradier has a split error"), the real source chain with tested coverage, and the audit line. Routing fixes (SOXL.NE bars from IBKR, Tradier 40% guard) remain step 3 of this plan and are not built. Page checker A11 holds SOXL.NE to FAIL permanently: when SOXL.NE's data is fixed, update `KNOWN_VERDICT` in `frontend/scripts/lib/analyzeChecks.js`.

