# Known Issues — Day 106 (August 13, 2026)

## Changes from Day 105

**Resolved this session:**
- Scan tab breakout-badge "—" ambiguity — three different situations (beyond the 20-row cap / requested-no-result / genuine NOT_READY) rendered as one indistinguishable dash. Fixed with four distinct honest labels. New Golden Rule 44.

**Added this session:**
- Simple Checklist's "PASS" badge label is misleading at low pass counts (below).
- Canadian Analyze Page limitation's real scope/status is now uncertain (downgraded from "confirmed broken," below) — found investigating a user-flagged concern about a Canadian ticker, not a new bug introduced this session.

**Investigated, not a bug:** a user-flagged possible US/Canadian ticker mix-up on CMG.TO — verified directly against the backend (`CMG.TO` → Computer Modelling Group @ $4.00; bare `CMG` → Chipotle @ $32.64). The original analysis had correctly used the `.TO`-suffixed ticker throughout. No fix needed.

**Freeze status:** unchanged — forward-testing accumulation remains the sole stated priority across all four live tracks. Numbers not re-pulled this session (see `PROJECT_STATUS_DAY106_SHORT.md`); last live check was Day 105 (2026-08-11).

---

## Open Issues

### Low / Info: Simple Checklist's "PASS" badge is misleading at low pass counts (new, Day 106)
**Severity:** Low / Info
**Description:** `simplifiedScoring.js`'s checklist verdict field is binary — `'TRADE'` only at 9/9 criteria met, `'PASS'` for everything else, including 2/9 or 0/9. The Simple Checklist card's header badge displays this field's literal text, so a ticker failing 7 of 9 criteria still shows a badge that says **"PASS."** The card's own bottom-line message ("No Trade — most criteria failing, avoid this trade") is accurate and visible directly below it, so the information isn't wrong — but the top badge reads as good news to anyone who doesn't read past it. Found live-testing CMG.TO (2/9, badge said "PASS," bottom card correctly said avoid).
**Fix:** Not actioned — flagged to the user, no decision made on rewording yet (e.g. "PASS" → "NO TRADE" or similar, keeping the pass-count visible either way).

### Low / Info: Canadian Analyze Page — real scope now uncertain (carried from Day 59, status softened Day 106)
**Severity:** Low / Info (downgraded from Medium pending a proper recheck)
**Description:** Long-documented as "Analyze page needs a data source redesign for .TO tickers, only the Scan tab has real Canadian support." A Day 106 spot-check (CMG.TO) directly contradicts this for at least one ticker — both the Simple Checklist and Full Analysis returned correct, verified data (name and price matched the real Canadian company, confirmed via direct backend check). Not exhaustively retested across other Canadian tickers or exchanges (TSX-V, other dual-listings), so this is not being marked resolved — but the prior "confirmed broken" framing is no longer accurate either.
**Fix:** Not actioned this session — needs a proper multi-ticker recheck (a handful of TSX names across sectors) before this can be honestly closed or reconfirmed as broken.

### Low / Info: `/watchlist-report`'s published AI Supply Chain ETF Artifact — blank-render status not rechecked (carried from Day 104/105)
**Severity:** Info
**Description:** At Day 104's close, the AI Supply Chain ETF watchlist Artifact was rendering blank on the platform (file verified correct locally). Not rechecked Day 105 or Day 106 — two different watchlists were run instead, each publishing its own new Artifact.
**Fix:** Not an STA issue. Check `https://claude.ai/code/artifact/03423c12-9a9c-4334-8e32-6b2b822f418e` next time that specific watchlist is used; republish if still blank.

### Low / Info: SRPS screener's R:R is structurally disconnected from real support/resistance (carried from Day 105)
**Severity:** Low / Info
**Description:** Both the sector-level (`/api/sectors/pullback-screen`) and sub-industry-level (`/api/sectors/sub-industry-pullback-screen`) SRPS screeners compute their displayed target price as `entry + 2.5 × risk`, never checked against where real chart resistance actually sits. Cross-checking 3 live candidates (CGNX, GEV, RIVN) against STA's own Full Analysis Risk/Reward check found real R:R of 0.48:1 and 0.27:1 — nowhere near the screener's own implied 2.5:1. True of every candidate the screener will ever produce.
**Fix:** Not actioned — the screener's own disclaimer already states it's informational-only. A real fix would be a non-trivial rule change to SRPS's already-fixed, backtested-and-failed rule set. Offered as a future improvement, not started.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Relevant to momentum's Path A/B; not relevant to MR (HUB-65 included), which doesn't use the fundamentals leg.
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus.

### Low / Info: Sector Rotation's original 11-sector endpoint has no provider fallback (carried from Day 94/103)
**Severity:** Low / Info
**Description:** `get_sector_rotation()` (`/api/sectors/rotation`) calls `yf.download()` directly rather than going through the multi-provider orchestrator — a single point of failure. Its two newer siblings both use the full orchestrator chain.
**Fix:** Not actioned — low probability event, log-only. A contained fix was offered Day 103, not requested since.

### Low / Info: `fetchSectorRotation()` is a whitelisted reconstruction, not a pass-through (carried from Day 103)
**Severity:** Low / Info
**Description:** `frontend/src/services/api.js`'s `fetchSectorRotation()` manually lists which backend fields survive to the frontend, rather than passing the response through directly — the exact pattern that already caused a real bug once (Day 92). The newer sibling fetch functions were all built as pass-throughs, citing that lesson; this older function was never migrated.
**Fix:** Not actioned — offered but not requested.

### Low / Info: MR and momentum's automated entry gates have no regime/sector-correlation awareness (carried from Day 100)
**Severity:** Low / Info
**Description:** `detect_mr_signal()` (MR, both broad and HUB-65) checks exactly 4 things with no VIX, sector, or cross-ticker correlation check. Momentum has some regime awareness (VIX + SPY vs. 200-day average) but nothing sector-specific.
**Fix:** Not actionable mid-freeze — would be a re-tune of a frozen entry condition.

### Low / Info: HUB-65 backtest is selection-biased by construction (carried from Day 98)
**Severity:** Low / Info
**Description:** `backtest_hub_mr.py`'s headline numbers (PF 1.2574, Sharpe 1.5278) are NOT comparable to the survivorship-free baseline (PF 1.16). Caveat stated everywhere the number appears.
**Fix:** Not actionable — the forward-test track (own 100-trade bar) is the real test.

### Low / Info: HUB-65 and the broad MR scan are not independent samples (carried from Day 98)
**Severity:** Low / Info
**Description:** Many HUB-65 tickers overlap the broad dynamic MR universe — the same ticker can enter both tracks on the same day as separate positions with independent cooldowns.
**Fix:** Not actionable — accepted by design.

### Low / Info: Momentum's stop/target formula design — deeper redesign still open (carried from Day 95/96)
**Severity:** Low
**Description:** `compute_entry_levels()`'s flat+8% target vs. ATR-clamped stop remains the exit-management formula for Path A and Path B (confirmed intentional).
**Fix:** Not urgent — revisit only if results suggest the exit side needs attention, post-freeze.

### Low / Info: MR's ADX docstring doesn't match its code (carried from Day 92)
**Severity:** Low
**Description:** `mean_reversion.py`'s module docstring claims MR is "only active when ADX < 20 (range-bound)," but `detect_mr_signal()`'s actual `signal` condition never checks ADX.
**Fix:** Deferred alongside the volume-confirmation item, ROADMAP.md Priority #11.

### Low / Info: Volume confirmation missing from the decision engine (carried from Day 92, re-confirmed live Day 106)
**Severity:** Low / Info
**Description:** Neither the Full Analysis verdict tree nor the Simple Checklist's 9 criteria check whether a price move is confirmed by rising volume vs. thin volume. The Simple Checklist's "Volume" criterion is a **dollar-liquidity gate** (avg $ volume vs. cap-tier threshold), not a volume-confirms-the-move signal — confirmed directly against CMG.TO's checklist result today (`$0.6M daily — thin liquidity (need ≥$2M for small-cap)`, unrelated to price/volume confirmation). Real volume-confirmation logic already exists elsewhere in the codebase (OBV trend/divergence card, Distribution Warning badge, breakout-quality's 1.5x-volume check) but none of it feeds either decision path.
**Fix:** Deferred — touches frozen verdict logic. Tracked as ROADMAP.md Priority #11. Parked until the 100-trade paper-trading gate clears.

### Low / Info: Session 28 audit's remaining lower-priority findings (carried from Day 91)
**Severity:** Low
**Description:** Value tab's ROE thresholds badged "Buffett/Damodaran" when the code comment says "ChatGPT research validated"; Validate/Data Sources tabs show "live"/"healthy" status without probing real fetch success; per-position fetch failures are silently dropped.
**Fix:** Tracked as ROADMAP.md Priority #10 — batchable, not urgent, parked behind paper-trading focus.

### Low / Info: Paper-trading launchd log doesn't capture manual/force-run activity (carried from Day 95)
**Severity:** Low
**Description:** `daily_job.log`'s `StandardOutPath` only captures stdout from launchd-triggered invocations, not manual/force runs.
**Fix:** Not actioned — the ledger itself is authoritative, just log completeness.

### Low / Info: IBKR paper-execution CIRO question — one loose end before implementation (carried from Day 97)
**Severity:** Low / Info
**Description:** The IBKR paper-execution design plan reasons CIRO Rule 3200 doesn't extend to a pure paper account — a reasoned interpretation, not something CIRO states explicitly.
**Fix:** Not actioned — feature is parked pending the user's own additional research/review.

### Low / Info: No scheduled/proactive breakout alerting (carried from Day 100)
**Severity:** Low / Info
**Description:** `/breakout-watch` and the Scan tab's badge column both work against any ticker list on demand, but nothing runs on a schedule or notifies unprompted.
**Fix:** Parked — see ROADMAP.md priority #15.

### Low / Info: SRPS's Rule 6 (earnings exclusion) not applied in either backtest gate (carried from Day 103)
**Severity:** Low / Info
**Description:** Neither `srps_gate0_signal_count.py` nor `srps_gate1_backtest.py` applies the design doc's Rule 6 (skip candidates with earnings within 21 days). Both scripts' results are documented as an upper bound.
**Fix:** Moot — SRPS failed Gate 1 on win rate/PF grounds independent of this gap.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity **(now resolved — see Golden Rule 44, above)**, Master Framework/Nirmal/HUB-65 watchlist Name/Market Cap N/A by choice, a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
