# Known Issues — Day 93 (July 22, 2026)

## Changes from Day 92

**Resolved this session** (full detail in `KNOWN_ISSUES_DAY92.md`'s "found and fixed in a follow-up monitoring session" addenda — carried forward here as closed):
- Cap Size Rotation banner was mid-cap-blind (both header signal and momentum note) — fixed, all 3 tiers now considered.
- Cap Size Rotation tiles' bar/number color contradicted their own quadrant label — fixed, both now track the same quadrant color.
- Sectors tab redesigned for beginner interpretability: CTA now recommends an actually-favorable sector (not just highest RS Ratio magnitude), cards grouped by quadrant, per-card ordinal rank badge removed entirely.
- `econ_engine.py`'s composite narrative box — a real Day 91 regression (stale PMI card-name lookup silently disabled 3 of 5 narrative branches) — fixed via a shared `PMI_CARD_NAME` constant; dead `unemp` variable removed.
- Seasonal Regime card's May–Oct text contradicted its own NEUTRAL badge — softened to match.
- New cross-tab connection: Sectors tab states whether the macro backdrop supports the rotation it's showing (`macro_alignment` field); Context tab's own Market Phase and Macro Regime banners now reconcile with each other too.
- Self-audit findings: a Golden Rule 21 (DRY) violation between two components' duplicated style maps, fixed via a new shared `frontend/src/utils/alignmentStyles.js`; an unverified extraction (`compute_overall_regime()`) closed by re-diffing live output; a documentation self-contradiction (a fixed finding still listed as open) corrected in this file and in `ROADMAP.md`.

**Added this session:** none — no new bugs found beyond what's listed above, all already fixed same-session.

**Freeze status:** unchanged — forward-testing accumulation remains the user's sole stated priority. All of today's Sectors/Context work is independently verified to not touch the frozen verdict engine or paper-trading gate (see `PROJECT_STATUS_DAY93_SHORT.md`'s Gates section).

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
**Description:** Value tab's ROE thresholds badged "Buffett/Damodaran" when the code comment says "ChatGPT research validated"; Validate/Data Sources tabs show "live"/"healthy" status without probing real fetch success; Sectors tab's `.toFixed(3)` false precision (the Rank #1 CTA/gate-bypass part of this same finding was fixed Day 92, not a duplicate open item — see resolved list above); Forward Testing's momentum-path trades store identical net/gross P&L and per-position fetch failures are silently dropped. Plus the audit's general polish list.
**Fix:** Tracked as ROADMAP.md Priority #10 — batchable, not urgent, parked behind paper-trading focus.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal watchlist Name/Market Cap N/A by choice, README.md version footer drift (the static "v4.30" footer string in `App.jsx` was not touched — a separate, pre-existing, already-tracked drift item, not part of today's version bump). See `KNOWN_ISSUES_DAY87.md` for full text of the pre-existing items.
