# Known Issues — Day 102 (August 4, 2026)

## Changes from Day 101

**Resolved this session:** none.

**Added this session:** none — no STA code was touched. (The Questrade Flow experiment's open items — a possible `XCHP.TO` ticker-collision risk, and the daily-cap-vs-lifetime-cap gap on the buy flow — are tracked in memory as a separate, non-STA real-money exercise, not logged here since they aren't STA issues.)

**Freeze status:** unchanged — forward-testing accumulation remains the sole stated priority across all four tracks. MR (broad) crossed the halfway point (61/100 closed).

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Relevant to momentum's Path A/B (both share the same verdict step); not relevant to MR (HUB-65 included), which doesn't use the fundamentals leg.
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.
**Fix:** Parked behind the paper-trading focus.

### Low / Info: MR and momentum's automated entry gates have no regime/sector-correlation awareness (carried from Day 100, not a bug)
**Severity:** Low / Info
**Description:** `detect_mr_signal()` (MR, both broad and HUB-65) checks exactly 4 things — RSI(2), price vs. its own 200-day SMA, price floor, 20-day dollar volume — with no VIX, sector, or cross-ticker correlation check at all. Momentum's verdict engine has some regime awareness (VIX + SPY vs. its 200-day average) but nothing sector-specific either.
**Fix:** Not actionable mid-freeze — would be a re-tune of a frozen entry condition. Logged so the real statistical power of "100 trades" is understood accurately when the bar is eventually evaluated.

### Low / Info: HUB-65 backtest is selection-biased by construction (carried from Day 98, not a bug)
**Severity:** Low / Info
**Description:** `backtest_hub_mr.py`'s clean-looking headline numbers (PF 1.2574, Sharpe 1.5278) are NOT comparable to the project's own survivorship-free baseline (PF 1.16). The caveat is stated everywhere the number appears.
**Fix:** Not actionable — the forward-test track (own 100-trade bar, now 26/100) is the real test.

### Low / Info: HUB-65 and the broad MR scan are not independent samples (carried from Day 98, not a bug)
**Severity:** Low / Info
**Description:** Many HUB-65 tickers overlap the broad dynamic MR universe — the same ticker can enter both tracks on the same day as separate positions with independent cooldowns.
**Fix:** Not actionable — accepted by design.

### Low / Info: Momentum's stop/target formula design — deeper redesign still open (carried from Day 95/96)
**Severity:** Low
**Description:** `compute_entry_levels()`'s flat+8% target vs. ATR-clamped stop remains the exit-management formula for Path A and Path B (confirmed intentional, matches the historical backtest's own exit simulation).
**Fix:** Not urgent — revisit only if results suggest the exit side needs attention, post-freeze.

### Low / Info: MR's ADX docstring doesn't match its code (carried from Day 92)
**Severity:** Low
**Description:** `mean_reversion.py`'s module docstring claims MR is "only active when ADX < 20 (range-bound)," but `detect_mr_signal()`'s actual `signal` condition never checks ADX.
**Fix:** Deferred alongside the volume-confirmation item, ROADMAP.md Priority #11.

### Low / Info: Volume confirmation missing from the decision engine (carried from Day 92)
**Severity:** Low
**Description:** Neither the Full Analysis verdict tree nor the Simple Checklist's 9 criteria check whether a price move is confirmed by rising volume vs. thin volume.
**Fix:** Deferred — touches frozen verdict logic. Tracked as ROADMAP.md Priority #11. Parked until the 100-trade paper-trading gate clears.

### Low / Info: Session 28 audit's remaining lower-priority findings (carried from Day 91)
**Severity:** Low
**Description:** Value tab's ROE thresholds badged "Buffett/Damodaran" when the code comment says "ChatGPT research validated"; Validate/Data Sources tabs show "live"/"healthy" status without probing real fetch success; per-position fetch failures are silently dropped.
**Fix:** Tracked as ROADMAP.md Priority #10 — batchable, not urgent, parked behind paper-trading focus.

### Low / Info: Sector Rotation Monitor has no fallback on its own OHLCV fetch (carried from Day 94)
**Severity:** Low
**Description:** `get_sector_rotation()` calls `yf.download()` directly rather than going through the provider chain. The `/api/sectors/sub-industry` endpoint (Day 101) does NOT have this limitation.
**Fix:** Not actioned — low probability event, log-only per Day 94's own judgment.

### Low / Info: Paper-trading launchd log doesn't capture manual/force-run activity (carried from Day 95)
**Severity:** Low
**Description:** `daily_job.log`'s `StandardOutPath` only captures stdout from launchd-triggered invocations, not manual/force runs.
**Fix:** Not actioned — the ledger itself is authoritative, just log completeness.

### Low / Info: IBKR paper-execution CIRO question — one loose end before implementation (carried from Day 97, not a bug)
**Severity:** Low / Info
**Description:** The IBKR paper-execution design plan reasons CIRO Rule 3200 doesn't extend to a pure paper account — Claude's own reasoned interpretation, not something CIRO states explicitly.
**Fix:** Not actioned — feature is parked pending the user's own additional research/review.

### Low / Info: No scheduled/proactive breakout alerting (carried from Day 100, not a bug — feature gap)
**Severity:** Low / Info
**Description:** `/breakout-watch` and the Scan tab's badge column both work against any ticker list on demand, but nothing runs on a schedule or notifies unprompted.
**Fix:** Parked — see ROADMAP.md priority #15.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal/HUB-65 watchlist Name/Market Cap N/A by choice, a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable per the documented point-in-time limitation). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
