# Known Issues — Day 98 (July 24, 2026)

## Changes from Day 97

**Resolved this session:** none — this session added a new feature (HUB-65 curated-universe MR track), it didn't fix an existing bug.

**Added this session:** none to the Open Issues list. The HUB-65 backtest's selection bias is a known, explicitly-documented caveat (stated in the script's docstring, its JSON output, the UI caption, and `PAPER_TRADING_PREREGISTRATION.md` §9b) — not an undiscovered gap, so it's not tracked here as an issue.

**Freeze status:** unchanged — forward-testing accumulation remains the user's sole stated priority for Path A/MR/HUB-65 alike. The IBKR plan (Day 97) is still explicitly parked pending further user research/review.

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

### Low / Info: HUB-65 backtest is selection-biased by construction (new, Day 98, not a bug)
**Severity:** Low / Info
**Description:** `backtest_hub_mr.py`'s clean-looking headline numbers (PF 1.2574, Sharpe 1.5278) are NOT comparable to the project's own survivorship-free baseline (PF 1.16, random 400-ticker sample) — HUB-65 is a 2026 watchlist of names selected *because* they already look strong (semis/uranium/fintech momentum names), a milder version of the exact bias the original hand-picked-60-ticker backtest was corrected for (Day 79). The caveat is stated everywhere the number appears (script docstring, JSON `meta.caveat`, UI card caption, `PAPER_TRADING_PREREGISTRATION.md` §9b) — this entry exists so it isn't quietly forgotten, not because it's hidden anywhere.
**Fix:** Not actionable — the forward-test track (own 100-trade bar) is the real test, same philosophy as every other system in this project. No further backtest iteration planned.

### Low / Info: HUB-65 and the broad MR scan are not independent samples (new, Day 98, not a bug)
**Severity:** Low / Info
**Description:** Many HUB-65 tickers overlap the broad dynamic MR universe (liquid large-caps both scans would surface) — the same ticker can enter both tracks on the same day as separate positions with independent cooldowns. A naive PF comparison between the two tracks doesn't cleanly answer "does curation help" vs. "does curation just concentrate risk on correlated names."
**Fix:** Not actionable — accepted by design (deduping would mean shared names never accumulate HUB-65 trades). Frame any future comparison between the two tracks as "a different bet," not "a better strategy."

### Low / Info: Momentum's stop/target formula design — deeper redesign still open (carried from Day 95/96)
**Severity:** Low
**Description:** `compute_entry_levels()`'s flat+8% target vs. ATR-clamped stop remains the exit-management formula for both Path A and Path B (confirmed intentional, matches the historical backtest's own exit simulation). The deeper design critique (stop is structural, target is flat) still stands as a legitimate longer-term design question.
**Fix:** Not urgent — revisit only if Path B's own results suggest the exit side needs attention too, post-freeze.

### Low / Info: MR's ADX docstring doesn't match its code (carried from Day 92)
**Severity:** Low
**Description:** `mean_reversion.py`'s module docstring claims MR is "only active when ADX < 20 (range-bound)," but `detect_mr_signal()`'s actual `signal` condition never checks ADX. Likely a doc-accuracy issue, not a logic bug. Applies identically to the HUB-65 track (same detector function).
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

### Low / Info: IBKR paper-execution CIRO question — one loose end before implementation (carried from Day 97, not a bug)
**Severity:** Low / Info
**Description:** The IBKR paper-execution design plan (`IBKR_PAPER_EXECUTION_PLAN.md`, ROADMAP Priority #13) reasons that CIRO Rule 3200's automated-order restriction doesn't extend to a pure paper-trading account — but this is Claude's own reasoned interpretation, not something CIRO states explicitly about paper accounts.
**Fix:** Not actioned — feature is parked pending the user's own additional research/review. A support ticket to IBKR confirming this directly would remove all doubt before Phase 1 begins.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal/HUB-65 watchlist Name/Market Cap N/A by choice (same free Volume/Change fix from Day 86 applies to all three), a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable per the documented point-in-time limitation). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
