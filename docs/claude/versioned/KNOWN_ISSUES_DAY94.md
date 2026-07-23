# Known Issues — Day 94 (July 23, 2026)

## Changes from Day 93

**Resolved this session:**
- Sector Rotation Monitor failed silently on a data-fetch error (stuck loading spinner, no indication anything broke) — fixed with a visible error banner + Retry, verified not to cascade into breaking the Analyze Stock page (2nd-pass finding), and verified not to leave a stale error banner masking later-arriving good data (3rd-pass finding). See Golden Rule 32.
- `README.md` was substantially stale/wrong (never fully audited before) — a full Coherence Audit found and fixed ~50 real issues: 3 fictional API endpoints removed, ~10 real endpoints documented for the first time (including the entire paper-trading and breakout engines), self-contradicting version/date claims fixed, Stooq/Tradier corrected throughout, Project Structure tree rebuilt against the real filesystem. Full detail in `PROJECT_STATUS_DAY94_SHORT.md`.

**Added this session:** none — no new bugs found beyond the Sector Rotation silent-failure gap, which is fixed above.

**Freeze status:** unchanged — forward-testing accumulation remains the user's sole stated priority. Today's Sector Rotation fix and README audit are independently verified to not touch the frozen verdict engine or paper-trading gate.

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

### Low / Info: Sector Rotation Monitor has no fallback on its own OHLCV fetch (new, found Day 94, not yet fixed)
**Severity:** Low
**Description:** Unlike most of the app, `get_sector_rotation()` calls `yf.download()` directly rather than going through the `TwelveData → yfinance → Tradier` provider chain — a single yfinance failure now surfaces correctly (per today's fix) instead of hanging silently, but there's still no automatic fallback to try another provider before failing.
**Fix:** Not actioned — low probability event, no fallback currently wired in. Log-only per this session's own judgment (see `PROJECT_STATUS_DAY94_SHORT.md`).

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal watchlist Name/Market Cap N/A by choice, a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable per the documented point-in-time limitation). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
