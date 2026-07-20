# Known Issues — Day 92 (July 20, 2026)

## Changes from Day 91

**Resolved this session:**
- Paper-trading's `signal_date` was stamped from the wall clock instead of the OHLCV bar `signal_price` came from — a weekend/off-hours Force Run could permanently strand a signal in `pending_entry` with no visible error. 8 of momentum's 11 pending signals were affected; all repaired, 7 reactivated immediately. See Golden Rule 28.

**Added this session:**
- Volume-confirmation gap in the decision engine (new, see below) — found via a first-principles review, not a live bug report.
- MR's ADX/docstring mismatch (new, see below) — same review.

**Freeze status:** superseded — forward-testing accumulation is now the user's explicitly stated **sole** priority (stricter than the prior "bug fixes + monitoring" freeze). Confirmation bar raised 50 → 100 trades/system.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg.
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus per Day 92.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.
**Fix:** Parked behind the paper-trading focus per Day 92.

### Low / Info: Volume confirmation missing from the decision engine (new, Day 92)
**Severity:** Low
**Description:** Neither the Full Analysis verdict tree (`determineVerdict()`) nor the Simple Checklist's 9 criteria check whether a price move is confirmed by rising volume (accumulation) vs. thin volume. The Simple Checklist's "Volume" criterion is a liquidity gate (avg $ volume vs. cap-tier threshold), not a price/volume-confirmation signal — confirmed live against a real ticker (a screenshot showed CCO passing "Volume: PASS" on liquidity alone). OBV trend/divergence exists as a separate informational card and VCP/Cup&Handle's volume-dry-up check exists inside pattern detection, but neither feeds the verdict or the checklist pass count.
**Fix:** Deferred — adding it touches the frozen, already-backtested verdict logic and needs a fresh walk-forward/survivorship-free re-backtest before shipping. Tracked as ROADMAP.md Priority #11. Explicitly parked until the 100-trade paper-trading gate clears.

### Low / Info: MR's ADX docstring doesn't match its code (new, Day 92)
**Severity:** Low
**Description:** `mean_reversion.py`'s module docstring claims MR is "only active when ADX < 20 (range-bound)," but `detect_mr_signal()`'s actual `signal` condition never checks ADX — it's computed and returned as an informational `range_bound` flag only. May be a doc-accuracy issue rather than a bug (Connors' published RSI(2) method trades dips within an established uptrend, not specifically range-bound markets) — the PF 1.16 backtest result already reflects this exact ungated code, so nothing here invalidates prior results.
**Fix:** Deferred alongside the volume-confirmation item, ROADMAP.md Priority #11.

### Low / Info: Session 28 audit's remaining lower-priority findings (carried from Day 91)
**Severity:** Low
**Description:** Value tab's ROE thresholds badged "Buffett/Damodaran" when the code comment says "ChatGPT research validated"; Validate/Data Sources tabs show "live"/"healthy" status without probing real fetch success; Sectors tab's Rank #1 CTA bypasses the same Leading/Improving gate per-card buttons respect, plus `.toFixed(3)` false precision; Forward Testing's momentum-path trades store identical net/gross P&L and per-position fetch failures are silently dropped. Plus the audit's general polish list.
**Fix:** Tracked as ROADMAP.md Priority #10 — batchable, not urgent, parked behind paper-trading focus.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal watchlist Name/Market Cap N/A by choice, README.md version footer drift (now partially addressed Day 92 — Completed list and Current Priorities refreshed, but the file's own header/badge versioning wasn't audited line-by-line). See `KNOWN_ISSUES_DAY87.md` for full text of the pre-existing items.
