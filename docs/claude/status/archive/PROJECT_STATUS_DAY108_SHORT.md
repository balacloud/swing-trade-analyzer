# Project Status — Day 108 (August 14, 2026)

## Version: v4.58 → v4.59 (Backend v2.46 → v2.47, Frontend v4.53 → v4.54)

---

## What Happened Today

A full 10-group system audit, scoped and executed in one session via Plan Mode + 11 parallel/sequential background sub-agents, using the project's own `MASTER_AUDIT_FRAMEWORK.md`. Initial scoping was corrected mid-flight after the user caught two real gaps (Validate/Data Sources tabs missing from the plan; the FWD-testing engine wrongly treated as "recently audited"). Policy applied throughout, per the user's explicit instruction: fix immediately if a finding is isolated from the 4 live paper-trading tracks, park (log, don't touch) if it overlaps with their frozen logic. Full findings log: `docs/claude/versioned/FULL_AUDIT_FINDINGS_DAY107.md`.

**27 items checked across all 9 tabs + the core verdict engine + the FWD-testing engine + the data-provider package. 15 fixed, 8 parked (need a human decision or bigger scope), 4 came back clean.**

### 1. S&R / Pattern engine (Group 1)
- **Fixed — CRITICAL:** The Analyze page's "MTF Confluence" weekly support/resistance levels were silently computed from fabricated calendar dates, not real trading weeks. `backend.py`'s `/api/sr/<ticker>` route rebuilt its DataFrame from raw `.values` arrays, dropping the real date index; the resampler then fabricated one via `pd.date_range(freq='D')` (including fake weekends), bucketing 7 calendar days per "week" instead of 5 real trading days. Fixed by preserving the real index. Verified directly: 52 weekly bars (correct) vs. 38 (the old bug) on identical input.
- **Parked:** The pivot support/resistance method picks the most price-extreme levels, not the ones nearest the current price. Confirmed this exact behavior is baked identically into both the validated backtest and the live Momentum Path B track (44/100 closed) — not a live/backtest divergence, so not urgent, but changing it now would alter validated behavior mid-accumulation.

### 2. Core verdict engine (Group 2)
- **Fixed:** Two stale docstrings (`simplifiedScoring.js`'s RS threshold said 1.2, code correctly uses 1.0; `categoricalAssessment.js`'s "equal-weight" header claimed all 4 pillars are counted when only Technical+Fundamental are). Comment-only, zero behavior change.
- **Confirmed clean:** Ran the JS/Python parity test live — 86,400/86,400 combinations match. Every pre-registered threshold verified exact.

### 3. FWD-testing engine vs. its frozen rulebook (Group 3)
- **Parked — real finding, verified harmless today:** Section 8's VIX-based position-size multiplier (reduce trade size when the market is risky) was never wired into the live automated engine — `get_vix_multiplier()` exists and is correct but has zero callers; the ledger schema has no position-size field at all. Verified this does NOT affect any of the 4 tracks' current win-rate/profit-factor/expectancy numbers (all computed from %-return/R-multiple, which are position-size-invariant) — only matters once real capital is deployed. Ties into the already-parked IBKR execution plan.
- **Confirmed clean:** Every other rule (R:R≥1.2 both paths, full exit management, Path B's real S&R gate, MR's entry/exit + the Day-82 two-different-stops distinction, HUB-65's universe-only variant, per-track cooldown independence) verified exact against the live code.

### 4. Analyze tab (Group 4)
- **Resolved, not a bug:** The long-uncertain "Canadian Analyze page" question is now closed. CMG.TO and RY.TO (deliberately different profiles) both passed all 8 endpoints and full live browser verification — broader coverage than the earlier Day-106 spot-check.
- **Fixed:** ETFs (SPY, QQQ, etc.) showed a factually wrong "using fallback data source" banner; two React falsy-zero risks (`rvol`, `risk_reward_context` could legitimately be `0` and would render a stray "0" instead of hiding).

### 5. Scan tab (Group 5)
- **Confirmed clean.** Golden Rule 44's badge fix, the Day-106 STA Verdict column, candidate-set consistency with the paper-trading engine, and all 3 watchlist presets all verified intact and correct, live-tested.

### 6. Sectors tab (Group 6a)
- **Fixed:** Golden Rule 30 (Day 92) was supposed to fix a whitelist-reconstruction bug that silently drops backend fields — but the fix was applied by extending the whitelist each time (twice, historically), never by removing it. `fetchSectorRotation()` itself — the function the rule is named after — was still doing exactly what it was named for stopping, live-proven to be dropping a `cached` field. Converted to a genuine pass-through, matching every sibling function built since.
- **Confirmed clean:** Refresh-button fix, fan-out caps, capped-count displays all verified live, not just read.

### 7. Context tab (Group 6b)
- **Fixed:** The tab was burning a real Alpha Vantage news credit on a placeholder ticker every time it loaded with nothing selected, plus double-fetching news when a ticker was selected — added a `skip_news` param to `/api/context/<ticker>` (additive, backward-compatible). A mislabeled banner ("Cycles FAVORABLE" when it meant the combined 10-indicator regime) and a silently-vanishing error state (inconsistent with the rest of the tab) were also fixed.
- **Parked:** The tab bypasses the app's shared fetch layer (`api.js`) entirely with its own local fetcher — confirmed a genuine oversight (not a legitimate divergence), but migrating it properly requires fixing `api.js`'s already-dead Context functions first (they swallow errors instead of throwing) — a real, scoped follow-up, not a quick patch.

### 8. Value tab (Group 7)
- **Fixed:** Negative FCF Yield (confirmed live on RIVN, F) showed a gray "N/A" instead of a red "Weak" badge — a missing style entry.
- **Parked — resolved honestly, needs a wording decision:** The long-open "Buffett" ROE attribution question (Session 28, Day 91) resolved as genuinely overclaimed — the code's "ChatGPT research validated" comment turns out to be the more accurate label. Not a bug, a copy decision.

### 9. Validate + Data Sources tabs (Group 8)
- **Fixed:** `/api/health`'s status field was a hardcoded literal, incapable of ever reflecting anything — now derived from real core-subsystem availability.
- **Settled with a live test, not just a read:** The years-old "shows healthy without probing" question turned out to be split — the per-provider health map is genuinely fixed (tested against a real, live TwelveData outage), but the per-ticker provenance panel still can't distinguish "never checked" from "just failed." Parked — needs new failure-tracking state, a real scoped project.

### 10. Providers package (Group 9, scoped re-verification)
- **Confirmed clean:** Golden Rule 22 (shared cross-process state) and Golden Rule 36 (circuit breaker vs. ticker-not-found), checked file-by-file across all 7 providers — zero regressions.
- **Fixed:** 3 trivial stale docstrings (2× Stooq→Tradier references, 1× wrong bar-count example).

### 11. Forward Test + Settings tabs (Group 10)
- **Confirmed clean:** The ledger's `variant` column dual-meaning (Golden Rule 38) is correctly disambiguated everywhere in the UI — no mix-up between momentum's gate-experiment axis and MR's universe axis.
- **Fixed:** Two different stats on the same tab were both labeled "Expectancy" (one is %-return, one is R-multiple) — relabeled both.
- **Parked:** Settings' risk slider allows up to 5%/trade against the app's own documented 2% Van Tharp ceiling — needs a product decision.

---

## Files Changed

| File | Change |
|---|---|
| `backend/backend.py` | S&R DatetimeIndex fix, `/api/context/<ticker>` `skip_news` param, `/api/health` status derivation, `BACKEND_VERSION` bump |
| `backend/providers/exceptions.py` | Stale docstring fix |
| `backend/providers/orchestrator.py` | 2 stale docstring fixes (Stooq→Tradier) |
| `frontend/src/App.jsx` | Fear&Greed gauge bands, RS badge bands, ETF banner fix, 2 falsy-zero fixes, `getSectorContext` optional chaining, Expectancy(R) label, version string bump |
| `frontend/src/components/AutomatedPaperTradingPanel.jsx` | Expectancy(%) label |
| `frontend/src/components/ConflictCheck.jsx` | Prop rename + message text fix |
| `frontend/src/components/ContextTab.jsx` | `skip_news` param usage |
| `frontend/src/components/MarketPhaseBanner.jsx` | Visible muted error state instead of silent `null` |
| `frontend/src/components/ValueTab.jsx` | Added missing `negative` verdict style |
| `frontend/src/services/api.js` | `fetchSectorRotation()` converted to genuine pass-through |
| `frontend/src/utils/categoricalAssessment.js` | Stale docstring fix |
| `frontend/src/utils/simplifiedScoring.js` | Stale docstring fix |
| `docs/claude/versioned/FULL_AUDIT_FINDINGS_DAY107.md` | New — full audit findings log, all 10 groups |

No changes to any of the 4 live forward-test tracks' frozen entry/exit logic.

---

## All Gates Status

Unchanged for the 4 live forward-test tracks — this session's audit found and fixed real bugs elsewhere in the app, but zero findings required touching any live track's frozen logic (per the user's explicit policy). Numbers pulled live at session close (2026-08-14, job last ran same day): **Path A** 34 open/30 closed (43.33% WR, PF 1.28); **Path B** 81 open/44 closed (59.09% WR, PF 1.41); **MR broad** 6 open/**90 closed (76.67% WR, PF 2.78)** — closest to its 100-trade bar, very likely clears it within the next session or two; **MR HUB-65** 2 open/30 closed (53.33% WR, PF 1.60).

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS.** MR (broad) at 90/100, plausibly clears its bar within the next session or two.
2. **Data-freshness blind spot (Validate/Data Sources)** — the highest-priority parked audit finding. The provenance panel can't distinguish "never checked" from "just failed" for a specific ticker. Needs a new failure-tracking mechanism, scoped as its own session.
3. **3 wording/product decisions parked from the audit, whenever convenient:** Value tab's ROE "Buffett" attribution copy, Settings' 2-5% risk slider vs. the documented 2% ceiling, FCF Yield's pass/fail badge (spec says it shouldn't have one).
4. **ContextTab → api.js migration** — real architectural fix, needs `api.js`'s dead Context functions fixed to throw-not-swallow first.
5. Everything else remains parked behind the freeze: IBKR paper-execution plan (now also owns the VIX position-sizing gap), fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation redesign, `/ibkr-scan`, PMI/Business-Cycle date-alignment fix (same class as the already-fixed Day-91 CPI bug), `backtest_adapter.py`'s short-span logic gap, SRPS R:R-vs-resistance gap, pivot S&R extremity-vs-nearest redesign.
