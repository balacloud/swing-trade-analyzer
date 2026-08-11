# Known Issues — Day 97 (July 24, 2026)

## Changes from Day 96

**Resolved this session:** none — pure research/planning session, no code touched.

**Added this session:** none new to the Open Issues list — the IBKR paper-execution work is a *planned, not-started* feature, tracked as ROADMAP Priority #13 and `docs/claude/design/IBKR_PAPER_EXECUTION_PLAN.md`, not a bug or gap in the existing system.

**Freeze status:** unchanged — forward-testing accumulation remains the user's sole stated priority for Path A/MR. The IBKR plan is explicitly parked pending further user research/review before Phase 1 begins.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg (Path A and Path B, and would carry through to any future IBKR execution too, since it shares the same verdict step).
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.
**Fix:** Parked behind the paper-trading focus.

### Low / Info: Momentum's stop/target formula design — deeper redesign still open (carried from Day 95/96)
**Severity:** Low
**Description:** `compute_entry_levels()`'s flat+8% target vs. ATR-clamped stop remains the exit-management formula for both Path A and Path B (confirmed intentional, matches the historical backtest's own exit simulation). The deeper design critique (stop is structural, target is flat) still stands as a legitimate longer-term design question.
**Fix:** Not urgent — revisit only if Path B's own results suggest the exit side needs attention too, post-freeze.

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

### Low / Info: IBKR paper-execution CIRO question — one loose end before implementation (new, Day 97, not a bug)
**Severity:** Low / Info
**Description:** The IBKR paper-execution design plan (`IBKR_PAPER_EXECUTION_PLAN.md`, ROADMAP Priority #13) reasons that CIRO Rule 3200's automated-order restriction doesn't extend to a pure paper-trading account (no real security trades, no real marketplace access) — but this is Claude's own reasoned interpretation of the rule's stated purpose, not something CIRO states explicitly about paper accounts.
**Fix:** Not actioned — feature is parked pending the user's own additional research/review. A support ticket to IBKR confirming this directly would remove all doubt before Phase 1 begins.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal watchlist Name/Market Cap N/A by choice, a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable per the documented point-in-time limitation). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
