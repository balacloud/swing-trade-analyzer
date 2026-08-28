# Known Issues — Day 103 (August 7, 2026)

## Changes from Day 102

**Resolved this session:** Forward Test tab's closed-trades display truncation (MR/HUB-65 silently showed only 20 of 71/28 closed trades, with no indication — both the table and the "Show tickers (N)" button count were affected). Fixed with a visible truncation note and corrected total-count math.

**Added this session:** `fetchSectorRotation()` whitelist-reconstruction risk (see below) — found while investigating the Sectors tab's data-sourcing at the user's request, not from a symptom.

**Freeze status:** unchanged — forward-testing accumulation remains the sole stated priority across all four live tracks. MR (broad) is now past 70% of its 100-trade bar (71/100 closed).

**Not an STA issue, tracked separately:** SRPS (Sector Rotation Pullback System) was fully investigated this session as a potential 5th automated track — its own Gate 0 (signal frequency) passed, Gate 1 (full backtest) failed (34.1% win rate vs. required 45%, PF 1.177 vs. required 1.2). Per its own design doc, it does not get built as a live track. Not logged as an STA bug/issue since the backtest worked correctly and gave an honest answer — see `PROJECT_STATUS_DAY103_SHORT.md` for full detail. The pivot (a discretionary Sector Pullback Screener) is a new, working feature, not an issue.

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

### Low / Info: Sector Rotation's original 11-sector endpoint has no provider fallback (carried from Day 94, scope clarified Day 103)
**Severity:** Low / Info
**Description:** `get_sector_rotation()` (`/api/sectors/rotation`) calls `yf.download()` directly rather than going through the multi-provider orchestrator — a single point of failure (a clean 500 if yfinance is down, no Tradier/TwelveData fallback). Its two newer siblings (`/api/sectors/sub-industry`, Day 101; `/api/sectors/pullback-screen`, Day 103) both use the full orchestrator chain — this is now the only one of the three sector-related endpoints without it.
**Fix:** Not actioned — low probability event, log-only per Day 94's own judgment. A contained fix (swap to the orchestrator, matching the two newer siblings) was offered to the user Day 103 but not requested.

### Low / Info: `fetchSectorRotation()` is a whitelisted reconstruction, not a pass-through (found Day 103)
**Severity:** Low / Info
**Description:** `frontend/src/services/api.js`'s `fetchSectorRotation()` manually lists which backend fields survive to the frontend, rather than passing the response through directly. This is the exact pattern that already caused a real bug once (Day 92: a new `macro_alignment` field was added to the backend and silently never reached the UI until noticed). The two newer sibling fetch functions (`fetchSubIndustryRotation`, `fetchSrpsPullbackScreen`) were both explicitly built as pass-throughs, citing that lesson — this older function was never migrated. Hasn't recurred only because no new field has been added to `/api/sectors/rotation`'s response since Day 93.
**Fix:** Not actioned this session (investigation only, at user's request). A contained fix — convert to pass-through, matching the established newer convention — was offered but not requested.

### Low / Info: MR and momentum's automated entry gates have no regime/sector-correlation awareness (carried from Day 100, not a bug)
**Severity:** Low / Info
**Description:** `detect_mr_signal()` (MR, both broad and HUB-65) checks exactly 4 things — RSI(2), price vs. its own 200-day SMA, price floor, 20-day dollar volume — with no VIX, sector, or cross-ticker correlation check at all. Momentum's verdict engine has some regime awareness (VIX + SPY vs. its 200-day average) but nothing sector-specific either. **Materialized concretely Day 103**: 4 of Path A's recent losses were a correlated batch (FRT+SKT both REITs; PAGP+PAA literally the same company's two securities), contributing to a real win-rate drop this session — confirmed as this known gap playing out, not a new bug, via direct trade-level and exit-mechanics verification.
**Fix:** Not actionable mid-freeze — would be a re-tune of a frozen entry condition. Logged so the real statistical power of "100 trades" is understood accurately when the bar is eventually evaluated.

### Low / Info: HUB-65 backtest is selection-biased by construction (carried from Day 98, not a bug)
**Severity:** Low / Info
**Description:** `backtest_hub_mr.py`'s clean-looking headline numbers (PF 1.2574, Sharpe 1.5278) are NOT comparable to the project's own survivorship-free baseline (PF 1.16). The caveat is stated everywhere the number appears.
**Fix:** Not actionable — the forward-test track (own 100-trade bar, now 28/100) is the real test.

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

### Low / Info: SRPS's Rule 6 (earnings exclusion) not applied in either backtest gate (new, Day 103, not a bug)
**Severity:** Low / Info
**Description:** Neither `srps_gate0_signal_count.py` nor `srps_gate1_backtest.py` applies the design doc's Rule 6 (skip candidates with earnings within 21 days) — no cheap historical earnings-date source exists across ~400-500 tickers x multi-year windows. Both scripts' results are documented as an upper bound. The live discretionary screener (`/api/sectors/pullback-screen`) DOES apply it, since live earnings-calendar data actually exists per-ticker.
**Fix:** Moot — SRPS failed Gate 1 on win rate/PF grounds independent of this gap; not worth resolving unless the rules themselves get redesigned and re-tested.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal/HUB-65 watchlist Name/Market Cap N/A by choice, a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable per the documented point-in-time limitation). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
