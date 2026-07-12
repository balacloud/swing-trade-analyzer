# Known Issues — Day 81 (July 10, 2026)

> **Day 82 update (July 12):** Breakout Plan Phase 0 and Phases 2–3 (both
> flagged "not yet run" / "ready" below) are now DONE — see ROADMAP.md's
> "COMPLETE — Breakout Enhancement Plan" sections and
> `docs/claude/versioned/BREAKOUT_CONFIG_D_BACKTEST_DAY81.md`. Also: a
> Fable process/hygiene audit ran Day 82
> (`docs/claude/design/FABLE_AUDIT_DAY82_PROCESS_AND_DECLUTTER.md`) — fixed
> 2 real git risk items (untracked production provider, tracked
> node_modules), deleted ~20 dead/orphaned files, this doc was one of the
> stale-doc findings that prompted this note. This file's body below is
> otherwise left as the Day 81 snapshot; see ROADMAP for current status.

## Changes from Day 80

**Resolved this session:**
- ✅ Live MR Detector Missing Liquidity Gate — `mean_reversion.py`'s `detect_mr_signal()` now uses price>$10 + 20-day avg dollar volume>$25M (was price>$5 + 500K share-volume), matching the backtest's Day 79 liquidity re-test exactly. Live MR signals now reflect the config that was actually validated (PF 1.16).

**New:**
- ✅ Automated paper trading engine built and live (`backend/paper_trading/`) — see Info entry below. This was not a planned roadmap item; built in response to a same-session user request to automate signal capture instead of relying on manual Forward Test logging.
- ⚠️ Catch-up limitation (by design, not a bug): the daily job's TradingView-driven momentum scan and MR scan both reflect *today's* live market only. If the scheduled run is missed (machine asleep), the job correctly resolves exits/state for already-open positions via full historical replay, but cannot retroactively reconstruct what would have signaled on the missed day — those entry signals are simply not generated. Keep the launchd job running close to daily for the cleanest OOS record.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver.
**Fix:** Mitigation choice still a pending user decision: (a) align live to SimFin's annualized-quarterly method, or (b) re-run the backtest with TTM-style fundamentals. **Now also relevant to the automated paper-trading engine**, since `live_signals.py`'s momentum leg pulls live fundamentals the same way the Analyze page does.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Low: SimFin API Key Rotation Unconfirmed (carried from Day 79)
**Severity:** Low
**Description:** Key moved to `backend/.env` (Task 1.1), but the OLD key is still in git history and was never confirmed rotated at simfin.com. A new key was shared in conversation Day 79 but not yet confirmed as the intended replacement or applied.
**Fix:** User to confirm rotation status.

### Low: Defeat Beta Import Still Present (carried)
**Severity:** Low (no functional impact)

### Info: Automated Paper Trading Engine — Built and Live (Day 81)
**Severity:** Info (milestone)
**Description:** `backend/paper_trading/` (`ledger.py`, `live_signals.py`, `daily_job.py`) runs unattended once per weekday via a macOS launchd agent (`~/Library/LaunchAgents/com.sta.papertrading.daily.plist`, weekdays 16:30 CT, ~90min after close). Every qualifying signal from the frozen config (`PAPER_TRADING_PREREGISTRATION.md`) is taken automatically — no human filtering — making this the primary, selection-bias-free source for the 50-trade confirmation bar, ahead of the manual Forward Test tab.
- Momentum candidates: the exact TradingView query `/api/scan/tradingview?strategy=best` uses (factored into shared `backend/scan_queries.py` so the scan route and the paper-trading engine can't drift), filtered through the live categorical assessment engine (`categorical_engine.run_assessment`) + R:R >= 1.2 check.
- MR candidates: `detect_mr_signal()` (now with the Day 81 liquidity fix) over the shared `mean_reversion.DEFAULT_MR_UNIVERSE`.
- Exit logic: `trade_simulator.py`/`mr_simulator.py` gained a `live_mode` parameter (verified byte-for-byte identical to the batch backtest on 40 synthetic trades) so live positions replay the *exact* backtested exit rules — one implementation, not a second one prone to drift.
- First live run (2026-07-10): 0 momentum signals (2 candidates found, correctly rejected on fundamentals/R:R), 2 MR signals queued (GOOGL, ABBV) — cross-checked against `/api/mr/scan` directly.
- Check progress: `cd backend && venv/bin/python paper_trading/daily_job.py --report`. Disable: `launchctl unload ~/Library/LaunchAgents/com.sta.papertrading.daily.plist`.
- Not yet done: no UI surfacing of this ledger (separate SQLite db from the manual Forward Test tab's localStorage) — deferred until trades accumulate.

### Info: Backtest Universe Survivorship Bias (carried from Day 79/80 — historical context)
**Severity:** Info (resolved via Phase 4 re-validation, kept for history)
**Description:** Canonical numbers are now the survivorship-free 400-ticker sample (Config C PF 1.40, MR liquidity-restricted PF 1.16). See ROADMAP.md.

### Info: Breakout Plan Phase 0 — DONE (Day 81, was "not yet run")
**Severity:** Info (milestone)
**Description:** Config D (confirmed-breakout-only) got 0 trades — a genuine, root-caused finding (pattern confidence structurally can't coexist with `broken_out` status), not a bug. Config E (anticipatory-only) captures 83–90% of Config C's real trades. See `docs/claude/versioned/BREAKOUT_CONFIG_D_BACKTEST_DAY81.md`.

### Info: Breakout Plan Phases 2–3 — DONE (Day 81, was "ready, not started")
**Severity:** Info (milestone)
**Description:** `/api/breakout/batch` endpoint, Scan tab badge column, and `/breakout-watch` skill all built and verified (real browser session for the badge column, live backend for the skill). Only Phase 1 (scan preset) remains, gated on explicit user approval.

### Info: IBKR Filter #8 — 52W High Proximity Availability Unverified (carried from Day 77)
**Severity:** Info (verify before building `/ibkr-scan`)

### Info: N4 Market Phase Synthesis — Research Done, Not Yet Built (carried from Day 76)
**Severity:** Info (planned — queued behind paper trading)

### Info: /ibkr-scan Skill — Design Complete, Not Yet Built (carried from Day 77)
**Severity:** Info (planned)

### Info: Price Structure Card — Phase 1 Only (carried from Day 72)
**Severity:** Info (known limitation)

### Info: Value Tab — ROIC Null on Finnhub Free Tier (carried from Day 75)
**Severity:** Info (Phase 1 limitation)

### Info: Value Tab Phase 2 Deferred (carried from Day 75)
**Severity:** Info (planned)

### Info: Gate 5 Combined Sharpe Measurement Artifact (carried from Day 75)
**Severity:** Info (methodological note)

### Info: Sentiment Removed from Verdict (carried from Day 70)
**Severity:** Info (architectural decision)

### Info: Blended RS Degrades Verdict Quality (carried)
**Severity:** Info (by design)

### Info: Backtest Max Drawdown — Reported Two Ways (carried from Day 79)
**Severity:** Info (methodological improvement)

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated (carried)
**Severity:** Info

### Info: FOMC Dates Hardcoded through 2027 (carried)
**Severity:** Info (maintenance reminder)

### Info: Parameter Stability — rsi_low and stop_atr_multiple Fragile (carried)
**Severity:** Info (documented, current values validated)
