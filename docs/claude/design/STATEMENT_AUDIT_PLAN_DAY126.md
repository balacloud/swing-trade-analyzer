# Statement Audit (Day 126) — PLAN v1

Why: the Technical Read said "+1.5% from a month ago" for the 200-day average. The number was real (30 trading days) but the words were wrong
(a month is about 21 trading days: +0.5%). It sat there from Day 123 to Day 126 because every automated check proves "page = API", never
"API = truth" or "words = number". Same family as the Day 71 phantom path and the Day 68 fabricated claim.
Goal: a repeatable audit of EVERY statement (number plus its words) on the Analyze page, with an independent recompute, and a place in
`MASTER_AUDIT_FRAMEWORK.md` so it is run after each card change.

## 1. What a "statement" is
Any text on a card that makes a factual claim: a number, a percent, a date, a window word ("a month", "1-year", "200-day", "past year", "last close"),
a comparison ("below", "above", "rising"), a count ("3 / 8"). Not advice, not design copy.

## 2. Four checks per statement (the framework's Layer S1-S4)
- **S1 Source:** which field/function produces it (file:line, API field). Recorded in the registry; no phantom paths (Day 71).
- **S2 Recompute:** rebuild the number from raw daily bars in a separate reference implementation that imports NO app indicator code
  (Python/pandas: SMA, EMA, Wilder RSI/ATR/ADX, returns, highs/lows). Tolerance per statement (rounding only).
- **S3 Words match the number:** each statement declares the window its words claim; the audit checks the computed window against a fixed
  dictionary: "a month" = 20-23 bars, "a week" = 5, "a quarter/13-week" = 63, "a year/1-year/52-week" = 250-253, "N-day" = N bars, "last close" = the
  last COMPLETED bar and its date, "now"/"live" = the quote. This is the check that would have caught today's bug.
- **S4 Outside reference (where one exists):** closes vs a second provider (the Data Sources tab C8 audit already does this; the statement audit
  reads its latest result instead of repeating it), prices vs the live quote, and a manual-ticker list vs IBKR for a human spot check (reported, never pass/fail).

## 3. Exhaustive, not a sample (Day 50 lesson)
The page text of each audited card is scanned for EVERY number pattern (`$x`, `x%`, dates, `n / m`, day-counts). Each match must be claimed by a registry
statement or sit on a short, reviewed EXEMPT list (e.g. "rule of thumb 7+", copy text). An unclaimed number = a finding ("UNCLAIMED"). So a new number added to a card
later cannot slip past silently.

## 4. Build
- `frontend/scripts/dump_page_statements.js` (node/puppeteer, reuses the checker's page driver): per ticker writes JSON {ticker, cards:{id:text}, testids:{...}, api:{stock,sr,patterns,quote}} to the report folder.
- `backend/audit_statements.py` + `backend/audit_statements_registry.py`: registry (id, card, regex to extract the displayed value, S1 source, S2 recompute fn, tolerance, window claim),
  reference indicators, window dictionary, unclaimed-number scan, report writer `docs/test/Statement_Audit_<date>/REPORT.md` (matrix: ticker x statement -> PASS/FAIL/UNCLAIMED + notes).
- `backend/test_audit_statements.py`: self-tests of the reference indicators against hand-computed values, the window dictionary (the "a month = 30 bars" case must FAIL), the unclaimed scan.
- Scope of the FIRST run (cards with numbers the user reads before a trade): header (price, change, last close, date), Technical Read (3 tiles, ADX line, 4 trend rows,
  gauge + ladder, volume line), Market backdrop band. Tickers: AAPL, NVDA, SOXL.NE, RIVN, F (sideways), plus SPY for RS. Cards not yet in the registry (Trade Setup,
  Breakout, S&R levels, Fundamentals, Data Sources) are listed as "NOT YET COVERED" in the report and the ledger, each with its statement count. Nothing is called covered that is not.

## 5. Framework + ledger
- `MASTER_AUDIT_FRAMEWORK.md`: add **Statement Audit** as a 6th audit type (table row, Part 7 protocol with S1-S4, Quick Reference line, Part 6 history row Day 126 with the "month" finding, anti-pattern "the page matches the API, so it's true").
  Update "5 distinct audit types" to 6.
- `AUDIT_COVERAGE_LEDGER.md`: new rows per card with date, depth (S1-S4), result.
- Trigger rule: run after any change to a card's text or numbers (add to the three-pass skill's pass 3 as "Statement Audit on touched cards" once it exists).

## 6. Risks to review
1. Independence: the reference uses the same `/api/stock` bars; it proves the math and the words, not the data source (S4 covers that and says so).
2. Fragile regexes on card text: a copy change breaks extraction; the unclaimed scan must fail loudly instead of passing quietly.
3. Rounding/borderline (e.g. -26.75%): tolerance policy must be explicit (display rounding, half-up vs banker).
4. Intraday-high vs close ("1-year high"): the statement must name which one it claims.
5. Live-price statements move between dump and audit; compare to the quote captured in the same dump.
6. Runtime: puppeteer per ticker is slow; the audit reads dumps, not the page.
7. Scope creep: first run is the named cards only; do not invent coverage.

## 7. Process
Plan -> Opus review -> build -> run once -> findings fixed or logged -> Known Issues entry -> framework + ledger updated -> commit.

## 8. Review result (v2) — Opus: GO WITH CHANGES, applied
1. **Closed vocabulary + every number token.** The unclaimed scan takes EVERY number token (`-?\d[\d,]*\.?\d*`), not just $/%/dates. Word-only claims (above/below, rising/falling, ✓/✗, "near the day's high") are registered and recomputed or marked UNVERIFIED.
2. **S3 split in two.** (a) **S3-static**: a registry of phrase -> the window the code really uses (constant + file:line), run as a fast node unit test over every branch of the pure functions with made-up inputs (the "a month" = 30 bars case must FAIL); no servers; goes in /three-pass pass 3. (b) **S2-live**: the per-ticker recompute. Branches a live run never reached are reported UNVERIFIED, not PASS.
3. **Window dictionary** gets a counting rule (N-day = N bars; "N bars back" = `iloc[-(N+1)]`, so 30 trading days = `iloc[-31]`, past year = 251 bars back = ok within 250-253), per-ticker windows for young tickers (200<bars<252 uses `iloc[0]`), EMA-span wording, calendar days vs trading days, and the extra phrases found (Last N days, last 10 sessions, 52-week, Last session/Today, N min ago, ...).
4. **S4** cites C3/C9 of the data-source plan, not C8, and reports "no outside reference" (UNVERIFIED) for tickers `backend/reference/data_audit_latest.json` does not cover. It never says PASS without a reference.
5. **Extraction:** a DOM walker (details forced open, a space between elements, `title`/`aria-label` included) feeds the unclaimed scan; values for S2 come from `data-*` attributes where they exist (ladder/ticks already have `data-price`/`data-gap`) and from known testids; plain regex only as the backstop.
6. **Dump** uses the payloads the PAGE received (network capture: stock, sr, patterns, quote, spy), records the run time and market state, and checks last-bar dates agree across stock/patterns/sr/spy. S1 names the JS file:line for frontend-computed numbers (EMA21, SMA, RSI, ADX).
7. **First-run scope, stated plainly:** Technical Read (full text scan, every number claimed or UNVERIFIED), the header price lines (by testid: live price, change, last close, date), the gauge and ladder. NOT YET COVERED, listed in the report: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
8. **Cross-card check (S5):** the same claim must show the same value on every card (e.g. 1-year high: Technical Read from patterns vs Price Data from yfinance info).
9. **Tickers:** AAPL, NVDA, SOXL.NE, RIVN, F, SMCI (broken structure), SMH (ETF) + SPY reference; check which hit the young-history branches.
10. **Verdicts map to the framework labels + severity:** number wrong = CRITICAL; number right, words wrong = MISLEADING/HIGH; unclaimed or branch not reached = UNVERIFIED; no outside reference = UNVERIFIED (S4). Rounding: display uses `toFixed` (not banker's) on rounded 2-decimal inputs; the tolerance says so.
11. **Framework edits:** call them checks S1-S5 (not "Layer"); ledger depth "L3 + S1-S5"; add the protocol before Quick Reference (no renumbering of Part 6); update "5 distinct audit types", the table, Quick Reference, header dates; one ledger row "Analyze page statements"; state it is Claim + Behavioral applied to rendered text. Trigger: static S3 test in /three-pass pass 3; live audit run by hand after a card change.
12. **Reuse:** import the reference RSI/ATR/EMA from `backend/backtest/test_indicators.py` where importable; only ADX and returns are new.
