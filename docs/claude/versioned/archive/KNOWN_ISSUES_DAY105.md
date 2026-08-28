# Known Issues — Day 105 (August 11, 2026)

## Changes from Day 104

**Resolved this session:**
- Sectors tab staleness bug — "Refresh Session" cleared the backend cache but never told already-loaded frontend components to refetch. Fixed with a `sectorRefreshTrigger` + a new scoped in-tab Refresh button. New Golden Rule 43.
- A pre-existing instance of the same failure family: the sector-level SRPS Pullback Screener's `sectorsCappedFrom` field has been computed by the backend since Day 102 but never displayed by the frontend. Fixed alongside the new sub-industry screener's equivalent field.

**Added this session:** the SRPS screener's R:R structural gap (below) — found while cross-checking screener candidates against STA's own fuller engine, not a new bug introduced this session.

**Freeze status:** unchanged — forward-testing accumulation remains the sole stated priority across all four live tracks. MR (broad) now 83/100 closed (live-pulled 2026-08-11), closest to its 100-trade bar by a wide margin.

---

## Open Issues

### Low / Info: SRPS screener's R:R is structurally disconnected from real support/resistance (new, Day 105)
**Severity:** Low / Info
**Description:** Both the sector-level (`/api/sectors/pullback-screen`) and sub-industry-level (`/api/sectors/sub-industry-pullback-screen`) SRPS screeners compute their displayed target price as `entry + 2.5 × risk` (`SRPS_TARGET_R_MULTIPLE`) — a fixed multiple of the stop distance, never checked against where real chart resistance actually sits. Cross-checking 3 live candidates this session (CGNX, GEV, RIVN) against STA's own Full Analysis Risk/Reward check (which does measure against real support/resistance) found real R:R of 0.48:1 and 0.27:1 for GEV/RIVN — nowhere near the screener's own implied 2.5:1. This isn't specific to these 3 tickers; it's true of every candidate the screener will ever produce, since the target formula never consults resistance at all.
**Fix:** Not actioned — the screener's own disclaimer already states it's informational-only, not a signal, and this session's cross-checks are exactly the "apply your own judgment" the disclaimer asks for. A real fix (computing target against actual resistance, matching the Full Analysis engine's own method) would be a genuine, non-trivial rule change to SRPS's already-fixed, backtested-and-failed rule set — offered as a future improvement, not started.

### Low / Info: `/watchlist-report`'s published AI Supply Chain ETF Artifact — blank-render status not rechecked (carried from Day 104)
**Severity:** Info
**Description:** At Day 104's close, the AI Supply Chain ETF watchlist Artifact was rendering blank on the platform (file verified correct locally). Day 105 ran the skill on a different watchlist (AI_Leveraged) and published a separate, new Artifact URL — the original AI Supply Chain Artifact's render status was not rechecked this session.
**Fix:** Not an STA issue. Check `https://claude.ai/code/artifact/03423c12-9a9c-4334-8e32-6b2b822f418e` next time that specific watchlist is used; republish if still blank.

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
**Description:** `get_sector_rotation()` (`/api/sectors/rotation`) calls `yf.download()` directly rather than going through the multi-provider orchestrator — a single point of failure (a clean 500 if yfinance is down, no Tradier/TwelveData fallback). Its two newer siblings (`/api/sectors/sub-industry`, Day 101; `/api/sectors/pullback-screen`, Day 103) both use the full orchestrator chain — this is now the only one of the three sector-related endpoints without it. The new sub-industry pullback screener (Day 105) also uses the orchestrator, so the count of "endpoints without fallback" hasn't grown.
**Fix:** Not actioned — low probability event, log-only per Day 94's own judgment. A contained fix was offered Day 103, not requested since.

### Low / Info: `fetchSectorRotation()` is a whitelisted reconstruction, not a pass-through (found Day 103)
**Severity:** Low / Info
**Description:** `frontend/src/services/api.js`'s `fetchSectorRotation()` manually lists which backend fields survive to the frontend, rather than passing the response through directly. This is the exact pattern that already caused a real bug once (Day 92: a new `macro_alignment` field was added to the backend and silently never reached the UI until noticed). The two newer sibling fetch functions (`fetchSubIndustryRotation`, `fetchSrpsPullbackScreen`) — and now `fetchSubIndustryPullbackScreen()`, added Day 105 — were all explicitly built as pass-throughs, citing that lesson. This older function was never migrated.
**Fix:** Not actioned — offered but not requested.

### Low / Info: MR and momentum's automated entry gates have no regime/sector-correlation awareness (carried from Day 100, not a bug)
**Severity:** Low / Info
**Description:** `detect_mr_signal()` (MR, both broad and HUB-65) checks exactly 4 things — RSI(2), price vs. its own 200-day SMA, price floor, 20-day dollar volume — with no VIX, sector, or cross-ticker correlation check at all. Momentum's verdict engine has some regime awareness (VIX + SPY vs. its 200-day average) but nothing sector-specific either.
**Fix:** Not actionable mid-freeze — would be a re-tune of a frozen entry condition.

### Low / Info: HUB-65 backtest is selection-biased by construction (carried from Day 98, not a bug)
**Severity:** Low / Info
**Description:** `backtest_hub_mr.py`'s clean-looking headline numbers (PF 1.2574, Sharpe 1.5278) are NOT comparable to the project's own survivorship-free baseline (PF 1.16). The caveat is stated everywhere the number appears.
**Fix:** Not actionable — the forward-test track (own 100-trade bar, now 29/100) is the real test.

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

### Low / Info: SRPS's Rule 6 (earnings exclusion) not applied in either backtest gate (carried from Day 103, not a bug)
**Severity:** Low / Info
**Description:** Neither `srps_gate0_signal_count.py` nor `srps_gate1_backtest.py` applies the design doc's Rule 6 (skip candidates with earnings within 21 days). Both scripts' results are documented as an upper bound.
**Fix:** Moot — SRPS failed Gate 1 on win rate/PF grounds independent of this gap.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal/HUB-65 watchlist Name/Market Cap N/A by choice, a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable per the documented point-in-time limitation). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
