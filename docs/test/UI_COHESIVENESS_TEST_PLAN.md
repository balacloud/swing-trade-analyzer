# UI Cohesiveness Test Plan

**Created:** Day 49 (February 9, 2026). **Rewritten:** Day 124 (Analyze Page Redesign Step 8).
**Purpose:** Check that the Analyze page is coherent: every card shows real data or says
plainly why it can't, and nothing contradicts anything else.

The old Day 49 checklist (BUY/HOLD/AVOID verdict, Holding Period weight notes, momentum vs
pullback entry cards, Position Size banner, VIABLE badge) tested elements removed on
Day 123. It is replaced below. The old version is in git history.

---

## 1. Automated checks — `frontend/scripts/ui-verify-checklist.js`

Run with both servers up: `cd frontend && node scripts/ui-verify-checklist.js [TICKERS...]`.
Default tickers: AAPL, NVDA, SMH (ETF), JPM (bank), RIVN (negative ROE). The script compares
the screen with the exact JSON the page received, so a live VIX tick can't cause a false fail.
Exit code 1 on any failure; report in `docs/test/UI_Verify_<date-time>/REPORT.md`.

| ID | Check |
|----|-------|
| A1 | Market backdrop is the first card; then the stock header, Technical Read, Mean-Reversion Read, Trade Setup, Fundamentals, in that order |
| A2 | Removed elements are absent: BUY/HOLD/AVOID badge, T:/F:/S:/R: chips, "Holding Period", Favorable/Neutral/Unfavorable market label, "Position Size:" banner, VIABLE badge, "Stock not recommended" (the Trade Setup's "BUY $x" price label is allowed) |
| A3 | Every Market backdrop figure (S&P 500 and QQQ trend vs 200-day and 50-day, biggest drop and its date, VIX and its band word) equals the API payload |
| A4 | The classification line never says "Unknown"; an ETF says "Exchange-traded fund (ETF)" |
| A5 | Earnings: header badge only when an earnings date is within the warning window; if the feed failed, Fundamentals says "Couldn't check the earnings calendar." |
| A6 | No blank cards (a card folded closed by design must still show its status word) |
| A8 | Simple view badge: "✅ TRADE" only at 9/9, otherwise "⏸️ No Trade", never "PASS" |
| A9 | No card is wider than its box at 390px (phone width). Page-level overflow from the tab bar is a Known Issue, reported but not failed |

(A7 "data source shown" was dropped: the app header shows it on every tab, so it could never fail.)

The checks are unit-tested in `frontend/scripts/test_analyze_checks.mjs`: the current page
passes every check, and an old-page or broken fixture fails each one.

## 2. Manual review — `frontend/scripts/ui-cohesiveness-test.js`

Saves a full-page PDF per ticker plus `TEST_REPORT.md` with this checklist:

- [ ] Market backdrop is the first card and shows facts only (no Favorable/Unfavorable label)
- [ ] No BUY/HOLD/AVOID verdict anywhere; the Simple view says TRADE or No Trade
- [ ] Each card says what its read is based on (rules, data source, dates)
- [ ] Anything that could not load says so plainly; no blank or made-up values
- [ ] An ETF says "Exchange-traded fund (ETF)", never "Unknown"
- [ ] Earnings date (Fundamentals) and header badge agree
- [ ] Trade Setup stop/target come from real support/resistance, or the card says why not

## 3. After testing

Log anything wrong in the current `KNOWN_ISSUES_DAY*.md`, fix one issue at a time, and re-run
section 1.
