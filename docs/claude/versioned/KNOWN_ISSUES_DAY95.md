# Known Issues — Day 95 (July 24, 2026)

## Changes from Day 94

**Resolved this session:**
- Paper-trading launchd job was firing at 4:30pm ET while its own comment assumed 4:30pm CT (machine's actual local timezone is America/Toronto/Eastern, confirmed via `/etc/localtime`) — silently shrinking the intended ~90-minute post-close settling buffer to ~30 minutes. Fixed: schedule shifted to 17:30 ET, comment corrected, launchd reloaded. See Golden Rule 33 and `PROJECT_STATUS_DAY95_SHORT.md`.

**Added this session:** none.

**Freeze status:** unchanged — forward-testing accumulation remains the user's sole stated priority. Today's plist fix is scheduling/ops-only and does not touch the verdict engine or paper-trading gate.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg.
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.
**Fix:** Parked behind the paper-trading focus.

### Low / Info: Volume confirmation missing from the decision engine (carried from Day 92)
**Severity:** Low
**Description:** Neither the Full Analysis verdict tree (`determineVerdict()`) nor the Simple Checklist's 9 criteria check whether a price move is confirmed by rising volume (accumulation) vs. thin volume. The Simple Checklist's "Volume" criterion is a liquidity gate, not a price/volume-confirmation signal.
**Fix:** Deferred — touches the frozen, already-backtested verdict logic and needs a fresh re-backtest before shipping. Tracked as ROADMAP.md Priority #11. Parked until the 100-trade paper-trading gate clears.

### Low / Info: MR's ADX docstring doesn't match its code (carried from Day 92)
**Severity:** Low
**Description:** `mean_reversion.py`'s module docstring claims MR is "only active when ADX < 20 (range-bound)," but `detect_mr_signal()`'s actual `signal` condition never checks ADX. Likely a doc-accuracy issue, not a logic bug.
**Fix:** Deferred alongside the volume-confirmation item, ROADMAP.md Priority #11.

### Low / Info: Session 28 audit's remaining lower-priority findings (carried from Day 91)
**Severity:** Low
**Description:** Value tab's ROE thresholds badged "Buffett/Damodaran" when the code comment says "ChatGPT research validated"; Validate/Data Sources tabs show "live"/"healthy" status without probing real fetch success; Forward Testing's momentum-path trades store identical net/gross P&L and per-position fetch failures are silently dropped. Plus the audit's general polish list.
**Fix:** Tracked as ROADMAP.md Priority #10 — batchable, not urgent, parked behind paper-trading focus.

### Low / Info: Sector Rotation Monitor has no fallback on its own OHLCV fetch (carried from Day 94)
**Severity:** Low
**Description:** Unlike most of the app, `get_sector_rotation()` calls `yf.download()` directly rather than going through the `TwelveData → yfinance → Tradier` provider chain — a single yfinance failure now surfaces correctly (per the Day 94 fix) instead of hanging silently, but there's still no automatic fallback to try another provider before failing.
**Fix:** Not actioned — low probability event, no fallback currently wired in. Log-only per Day 94's own judgment.

### Low / Info: Paper-trading launchd log doesn't capture manual/force-run activity (new, found Day 95, not actioned)
**Severity:** Low
**Description:** `daily_job.log`'s `StandardOutPath` only captures stdout from launchd-triggered invocations. Several recent days showed "already ran today — skipping" in that log with no matching completion line, while the `job_runs` DB table confirms real activity happened those days — meaning a manual/force run (terminal-invoked) likely did the actual work before the scheduled fire, and that manual run's output isn't preserved anywhere.
**Fix:** Not actioned — data currency isn't in question (the ledger itself is authoritative), just log completeness. Worth a look if it becomes important to know exactly which invocation path produced a given day's trades.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal watchlist Name/Market Cap N/A by choice, a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable per the documented point-in-time limitation). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
