# Known Issues — Day 96 (July 24, 2026)

## Changes from Day 95

**Resolved this session:**
- Paper-trading launchd timezone bug (4:30pm ET vs. assumed 4:30pm CT) — fixed, see Golden Rule 33.
- Every data provider's circuit breaker miscounted ticker-specific data gaps as provider-health failures — fixed across all 6 providers, see Golden Rule 36.
- `.env` loading fragility (import-order side effects) — centralized in `providers/__init__.py`.
- **Momentum's live R:R gate never matched the actual backtested entry logic** — the flat+8%/ATR-clamp formula was substitute logic since Day 81, while the real Config C backtest validated a support/resistance-based R:R check. This was the true explanation for the 81% rejection rate measured earlier in the day (not the stop-clamp specifics originally suspected). See Golden Rule 35.

**Added this session:**
- **Path B** — a parallel forward-test experiment (`variant='B_revised_rr'`) using the real S&R-based entry gate, running alongside the untouched Path A. Own 100-trade bar, 0/100 as of today. See `PAPER_TRADING_PREREGISTRATION.md` §8b for full detail, including the reverted wrong first attempt (widening the stop clamp — proven directionally backwards via a quick backtest check).
- New Golden Rules 33-36 (timezone verification, persona lens, live/backtest parity, circuit-breaker failure-type distinction).
- New `docs/claude/stable/PERSONA.md` — trading-judgment lens, wired into `/sta-start`/`/sta-end`.

**Freeze status:** unchanged for Path A and MR — no frozen threshold touched. Path B is a new, separate, honestly pre-registered experiment; it doesn't reset or affect Path A's count.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg (both Path A and Path B, since both share the same fundamentals-fed verdict step).
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.
**Fix:** Parked behind the paper-trading focus.

### Low / Info: Momentum's stop/target formula design — deeper redesign still open (carried from Day 95, reframed)
**Severity:** Low
**Description:** `compute_entry_levels()`'s flat+8% target vs. ATR-clamped stop remains the EXIT-MANAGEMENT formula for both Path A and Path B (confirmed this is intentional/consistent with how the historical backtest actually simulates trades once entered — not a bug). The deeper design critique from earlier Day 95 (stop is structural, target is flat; the "standard" exit rule's 10-EMA trailing stop gives convexity the entry-time R:R snapshot doesn't see) still stands as a legitimate longer-term design question, separate from the entry-gate divergence bug that Path B now addresses.
**Fix:** Not urgent — Path B's real S&R-based entry gate is the higher-priority fix and is now live. Revisit the exit-formula design question only if Path B's own results suggest the exit side needs attention too, post-freeze.

### Low / Info: MR's ADX docstring doesn't match its code (carried from Day 92)
**Severity:** Low
**Description:** `mean_reversion.py`'s module docstring claims MR is "only active when ADX < 20 (range-bound)," but `detect_mr_signal()`'s actual `signal` condition never checks ADX. Likely a doc-accuracy issue, not a logic bug.
**Fix:** Deferred alongside the volume-confirmation item, ROADMAP.md Priority #11.

### Low / Info: Volume confirmation missing from the decision engine (carried from Day 92)
**Severity:** Low
**Description:** Neither the Full Analysis verdict tree nor the Simple Checklist's 9 criteria check whether a price move is confirmed by rising volume vs. thin volume.
**Fix:** Deferred — touches the frozen, already-backtested verdict logic. Tracked as ROADMAP.md Priority #11. Parked until the 100-trade paper-trading gate clears.

### Low / Info: Session 28 audit's remaining lower-priority findings (carried from Day 91)
**Severity:** Low
**Description:** Value tab's ROE thresholds badged "Buffett/Damodaran" when the code comment says "ChatGPT research validated"; Validate/Data Sources tabs show "live"/"healthy" status without probing real fetch success; Forward Testing's momentum-path trades store identical net/gross P&L and per-position fetch failures are silently dropped. Plus the audit's general polish list.
**Fix:** Tracked as ROADMAP.md Priority #10 — batchable, not urgent, parked behind paper-trading focus.

### Low / Info: Sector Rotation Monitor has no fallback on its own OHLCV fetch (carried from Day 94)
**Severity:** Low
**Description:** `get_sector_rotation()` calls `yf.download()` directly rather than going through the provider chain — no automatic fallback to try another provider before failing.
**Fix:** Not actioned — low probability event, log-only per Day 94's own judgment.

### Low / Info: Paper-trading launchd log doesn't capture manual/force-run activity (carried from Day 95)
**Severity:** Low
**Description:** `daily_job.log`'s `StandardOutPath` only captures stdout from launchd-triggered invocations, not manual/force runs.
**Fix:** Not actioned — data currency isn't in question (the ledger itself is authoritative), just log completeness.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal watchlist Name/Market Cap N/A by choice, a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable per the documented point-in-time limitation). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
