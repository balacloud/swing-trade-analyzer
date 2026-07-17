# Known Issues — Day 90 (July 17, 2026)

## Changes from Day 89

**This session (monitoring + investigation only, no code changes):**
- Paper-trading check-in: Momentum 2 open/0 closed; MR 9 open/4 closed (75% WR, PF 2.19, +1.49%/trade).
- Investigated "Force Run Now" button mechanics end-to-end at user's request (see Info entry below) — confirmed existing behavior is correct by design, no bug found.

**Freeze status:** unchanged — still in complete feature freeze. No code shipped this session, so no freeze-exception question applies.

---

## Open Issues

Carried forward unchanged from `KNOWN_ISSUES_DAY89.md` — no new bugs found or fixed, no trading-logic/threshold changes. See that file (and `KNOWN_ISSUES_DAY87.md` for the full Medium/Low list) for complete detail.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg.
**Fix:** Mitigation choice still a pending user decision.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Low / Info items
Unchanged — SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal watchlist Name/Market Cap N/A by choice. See `KNOWN_ISSUES_DAY87.md` for full text of each.

---

### Info: Force Run Button — Investigated, Confirmed Safe to Click Repeatedly (Day 90)
**Severity:** Info (investigation record, not a bug)
**Description:** User asked what happens on repeated "Force Run Now" clicks and why the panel shows no ticker-level detail. Traced `daily_job.py` / `ledger.py` / `live_signals.py` / `AutomatedPaperTradingPanel.jsx`:
- No duplicate trades possible — `has_active_or_cooldown()` blocks re-queuing any ticker already pending/open/in-cooldown; closed positions are permanently excluded from replay.
- `job_runs.run_date` is UNIQUE with `INSERT OR REPLACE` — a same-day re-click overwrites that day's run summary rather than accumulating it, so the panel's "Run complete" banner only ever shows the latest click's delta.
- Real (non-correctness) cost: each click re-runs a live TradingView scan + OHLCV fetches across ~150 candidates per side plus every open position — genuine load against the same shared rate-limited provider chain Golden Rule 25 already found tips over at scale. Repeated rapid clicking is the one plausible way to retrigger that cascade.
- The panel has no ticker-level display anywhere (aggregate counts only) — seeing actual open/closed tickers requires querying `paper_positions` in the SQLite ledger directly.
**Fix:** None needed — behavior is correct as designed. Optional future enhancement (not committed): add a ticker-level table to the panel. Raised but not requested as a build task this session.
