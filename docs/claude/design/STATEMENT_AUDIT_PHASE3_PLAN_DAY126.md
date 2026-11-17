# Statement Audit, phase 3 (Day 126): Fundamentals, Market backdrop, Mean-Reversion Read, Data Sources — PLAN v1

Phases 1-2 are done (Technical Read, gauge/ladder, header price + badges, Trade Setup + key levels, Breakout, Price Data, Relative Strength: 0 WRONG on 7 tickers).
Phase 3 covers the remaining Analyze-page cards, then the Data Sources tab. Same protocol (MASTER_AUDIT_FRAMEWORK Part 7: S1-S5, verdicts PASS / WRONG / MISLEADING / UNVERIFIED,
every number token claimed or listed). New cards go in NEW modules importing the phase-1/2 machinery (`audit_cards.py` style), so earlier behaviour cannot regress; the frozen
phase-1 baseline gate stays. Nothing is called covered that is not.

## 1. Statements seen on the live cards (AAPL and SOXL.NE dumps) and how each is checked
### Market backdrop (`card-market-backdrop`, RegimeRead.jsx, marketBackdrop.js)
| Statement | Source | S2 / S3 |
|---|---|---|
| "S&P 500 / Nasdaq-100 (QQQ): Long-term (200-day) ↑ above +1.1% · Short-term (50-day) ↓ below -3.1%" | `/api/market/spy` and `/api/market/index/QQQ` `trend` facts (index_trend.py) | recompute 200/50-day averages and the % from an INDEPENDENT second source (fresh yfinance 2y SPY/QQQ, an S4 check, not the app's bars); arrows/words above/below vs the sign |
| "Biggest 1-day drop, last 10 sessions: -4.4% on Nov 5 (largest since Apr 4, 2025)" and QQQ "(largest in data back to Nov 13, 2024)" | index_trend.py | recompute the worst close-to-close change in the last 10 completed sessions, its date, and the "largest since <date>" / "in data back to" claims over the same history; words "last 10 sessions" = 10 bars; the data start date |
| "VIX 25.5 · high (latest quote)" | `/api/market/vix`, `vix_bands.py` | band word vs the number and the band table; "latest quote" vs the quote's timestamp |
| "Index figures as of Nov 16 close" | last completed bar | equals the last completed index bar (not a forming one) |
| Header "NEVER GATES THIS PAGE" etc. copy | copy | exempt list |
### Fundamentals (`card-fundamentals`, FundamentalsRead.jsx)
Sales growth %, ROE %, D/E (shown with their flag cutoffs: falling 10%+, below 0%, above 2.0), the "No red flags / N flags / Not applicable (ETF)" headline and "All 3 checks ran", "Next earnings · Last date in the feed: <date> (N days ago)",
sources line, the "disagrees with STA's backtest data about 40% of the time" claim. Checks: payload -> text arithmetic and format; the flag words vs the numbers and cutoffs (a tripped flag must show ✗, ETF = Not applicable); "N days ago" = calendar days
from the earnings date (S3 calendar vs trading); S5: the earnings date equals the header earnings badge and `/api/earnings`; ETF detection vs `quoteType`. S2 recompute is not possible for provider fields (Finnhub/Alpha Vantage): UNVERIFIED with the
reason, plus an S4 outside check against Yahoo `info` (revenueGrowth, returnOnEquity, debtToEquity) with a stated tolerance and unit conversion (decimal vs percent). The "40%" claim is traced to its source document or marked UNVERIFIED.
### Mean-Reversion Read (`card-mr-read`, MRRead.jsx, mrReadRows.js, mean_reversion.py)
"2-day RSI 33 needs under 10", "16.9% above its 200-day average", "$352.78 needs above $10", "$16.5B traded on an average day needs above $25M (average of the last 20 days)", the "Blocked by:" sentence, "No signal", "Checked on the <date> close".
Recompute from bars: RSI(2) per mean_reversion.py's definition (Connors), 200-day SMA and % distance, close, 20-day average dollar volume (shares x close, on the stated window); the four pass/fail marks vs the thresholds (10 / 200-day / $10 / $25M) and the
"No signal" headline = all four must pass; "Blocked by" lists exactly the failing rules; zero-volume funds show "not checked", never a fake $0 (SOXL.NE); "Checked on" = the last completed bar (the page says "today's bar is still forming" mid-session).
S5: the "% above/below its 200-day average" equals the Technical Read's 200-day row (same claim, same number); close equals "Last close".
### Data Sources tab (page checker A11 covers page = API)
Statements: per-source freshness ("7.9h ago"), provider chain lines, quality PASS/WARN/FAIL rows, indicator table rows, split notes, "Data from <provider>". S2/S3: freshness "Xh ago" vs the provider timestamp and now; calendar vs hours words; "rows" counts vs the cache (C8 provenance honesty is already checked); indicator table windows vs the code (Indicator Formula audit catalog). S4 stays the data-source audit's (C3/C9, `backend/reference/data_audit_latest.json`); this audit reads its result and reports UNVERIFIED where a ticker is not in it.

## 2. Build
- Dump script: capture `card-fundamentals`, `card-market-backdrop`, `card-mr-read` text (done in the exploratory run) and, for the tab, switch to Data Sources and read its text; payloads: `/api/fundamentals`, `/api/mr/signal`, `/api/market/index/QQQ`, `/api/market/vix`, `/api/provenance`.
- `backend/audit_cards2.py` (Market backdrop, Fundamentals, MR) importing `audit_cards.CardAudit`; `audit_tabs.py` for Data Sources. Independent index data for the backdrop is fetched by the audit itself (yfinance, cached to the report folder so a rerun is reproducible).
- Tests: planted wrong number / wrong word / unclaimed number per card, boundary cases (RSI(2) exactly 10, price exactly $10, $25M, D/E exactly 2.0, sales exactly -10%), ETF, zero-volume, missing-feed ("Not available" states must be said, never blank).
- Report: one coverage table across all phases (card, statements, tokens claimed, tokens unverified, recomputed / arithmetic-only / structural / UNVERIFIED, branches not reached). Ledger rows. Tickers: the existing 7 plus a bank (D/E "weaker signal"), an ETF with volume (SMH exists), a name with negative ROE, and one with earnings inside 7 days.

## 3. Questions for the review
1. Missing statements, copy and tooltips on these cards (grep the real JSX), incl. the "40%" and "weaker signal for banks" claims and anything that overstates.
2. Is a second-source (yfinance) recompute for the market backdrop the right S2/S4 split, and how should data start dates ("in data back to Nov 13, 2024") be verified?
3. RSI(2) and dollar-volume definitions in mean_reversion.py vs what the card says (window, smoothing, which bar); forming-bar handling.
4. Real bugs you can already see on these cards (labels, windows, live vs completed bars, rounding, verdict words against Day-126 facts-not-verdicts, silent failures).
5. Ways a wrong number could pass; regression risk to phases 1-2.

## 4. Process
Plan -> Opus review -> build -> run on 9+ tickers -> fix findings (own tests) or log -> three passes -> Known Issues, ledger, framework history -> commit.

## 5. Review result (v2) — Opus: GO WITH CHANGES, applied
- **Scope split.** Phase 3a (this build): Market backdrop, Fundamentals, MR Read on the Analyze page. Phase 3b (next): the Data Sources TAB, whose real statements differ from §1 (identity "inferred: <basis>", cache state, "Checked N bars (period P) · cached <time> · last bar D, N sessions behind", split note, "Last audit (date, N days old)", "Fundamentals from X, N days old / today", "N calls left today", coverage chips "as tested on <date>", cache tiles, "4pm ET + 30 min / 7 days"); needs `/api/health`, `/api/data-sources/coverage`, cache status. "7.9h ago" is the Analyze header (covered).
- **Real bugs to fix now:** MR "2-day RSI 10 needs under 10 ✗" (rounded to 0 dp; 10.24 shows 10) -> one decimal; stale/dead MR copy ("Forward Test tab" is hidden, "can be Strong there" no longer exists); blocker "the 2-day drop is too small" also shown after a RISE -> "2-day RSI is 10 or higher"; Fundamentals "disagrees about 40% of the time" (a 6-of-15 Day-78 label comparison about a label the card no longer shows) -> cut; "Debt is heavy" verdict word; O'Neil "A" is earnings growth not sales; ROE tooltip "the company lost money" is false for a profitable negative-equity company; cache tiles show "0 KB / 0%" for missing values (`?? 0`) -> dash; indicator catalog still says "Includes today's bar" / "RVOL reads low mid-session" (stale since the forming-bar fix).
- **Logged, not fixed:** RSI(2) is ewm smoothing (last 2 changes ~75% weight), "scores the last 2 days" is approximate; dollar-volume/price cutoff display rounding ($9.995, $24.95M); VIX band from 2-dp value vs 1-dp display; VIX has no quote timestamp so "latest quote" is UNVERIFIED; D/E and ROE definitions differ between Finnhub, Alpha Vantage and Yahoo, so the S4 check grades "same side of the cutoff" and reports the ratio as INFO; "weaker signal for banks" has no code branch (reviewed copy); "Buy the dip" / "The plan, as tested" advice-style headlines; "FORWARD-TESTED" badge is a claim.
- **Design:** parse by testid / data attributes, not flat text; per-card exempt lists with reasons (phase-1 EXEMPT swallows "20 days"/"200-day"); MR `asOf` must equal the stock's newest date; second source for the backdrop matched to the app's actual provider and anchored to `searchedFrom`; near-ties under 0.05 pp are UNVERIFIED-borderline; planted-payload branch tests through Playwright `page.route` where the card copy itself must be rendered; freeze the phase-2 dumps too (identical rows).

## 6. Result (Day 126, phase 3a)
Built per §5 for the three Analyze-page cards: 238 PASS / 0 WRONG / 7 UNVERIFIED (VIX has no quote time). Phases 1-2 unchanged (266 / 256 PASS, 0 WRONG). Real bugs fixed: MR RSI rounding at the cutoff, MR blocker after a rise, dead/stale MR copy,
unsupported Fundamentals claim and verdict word, false ROE tooltip, fake-zero cache tiles, stale catalog rows. Deferred to 3b: the Data Sources tab (its real statements are listed in §5) and Playwright planted-payload branch tests.
