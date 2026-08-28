# Project Status — Day 103 (August 7, 2026)

## Version: v4.56 (Backend v2.44 → v2.45, Frontend v4.30 → v4.51 — see version-drift note below)

---

## What Happened Today

### 1. SRPS (Sector Rotation Pullback System) — investigated end-to-end as a potential 5th forward-test track, FAILED its own backtest, pivoted to a discretionary screener
User brought a fully-specified design doc (v1.2) for a new mechanical strategy: buy strong stocks in recovering sectors as they pull back to their 21-EMA, asymmetric exits. Ran it through the doc's own two-gate process before any live build:

- **Gate 0 (signal frequency)** — built `backend/backtest/sector_quadrant_history.py` (historical sector-quadrant replay) and extended `scan_queries.py` with `build_sector_query()`/`rank_candidates_by_rs()` (live sector-filtered, RS-ranked candidate sourcing). Found and fixed two real TradingView-taxonomy bugs along the way: Real Estate (XLRE) — TradingView buckets all REITs under "Finance," fixed via the finer `industry` field; Communication Services (XLC) — no field-based fix exists at all (GOOGL/META/NFLX genuinely share TradingView's `Technology Services` bucket with real Tech names), fixed via a hand-curated, live-verified 17-ticker override (`XLC_OVERRIDE_TICKERS`). Result: ~143 signal-days/year — **passed** the doc's own 60/year bar comfortably.
- **Gate 1 (full backtest)** — built `backend/backtest/srps_gate1_backtest.py`, a genuine day-by-day portfolio simulator (400-ticker survivorship-free universe, 2020-2025, Rules 1-5, max-6-concurrent-position cap) — the first code in this project with that shape; existing MR/momentum backtests run each ticker independently with no concurrency cap. Found and fixed three real bugs during this build: (1) a rule-interaction whipsaw — Rule 3's entry band overlaps Rule 5's trail-exit trigger, so many entries exited within 1 day; fixed with a 5-day trail activation delay, matching this project's own existing EMA-trail convention (`trade_simulator.py`); (2) a universe-construction bias — sector-tagging before checking price-history availability silently dropped real historical bankruptcies (ITT Educational Services, BurgerFi, Alta Mesa Holdings) that a survivorship-free test exists to capture; fixed by reordering the pipeline; (3) a near-zero stop-distance bug that produced a 331,408 R-multiple artifact on one trade, corrupting the average; fixed with a minimum stop-distance floor (`STOP_MIN_PCT`, new `srps_constants.py`).
- **Real result**: 411 closed trades, **34.1% win rate** (needed >45%), **PF 1.177** (needed >1.2, missed by a hair), **FAIL**. Internally consistent with the design doc's own corrected expectancy math, not a surprising/broken number. Per the doc's own rule, SRPS does not get built as a live automated forward-test track.
- **Pivot**: same rule logic repurposed as a pure discretionary screener — new `GET /api/sectors/pullback-screen` endpoint + new collapsible "🎯 Sector Pullback Screener" section on the Sectors tab. Shows candidates matching the mechanical criteria for the user's own judgment (regime/news/catalysts), with a permanent disclaimer stating the backtest failed and this is not a signal. No ledger, no automated entry/exit, freeze-independent.
- Sub-industry expansion (design doc's own Phase 2) explicitly **not built** — Phase 1 never passed its own backtest, so there's nothing to expand from, and the failure was about the rules, not the universe.

### 2. Golden Rule 41 — escalating three-pass review, adopted from the Trading Intelligence Hub
User asked for a Hub-style review of today's work and to bake the process into `GOLDEN_RULES.md` for all future fixes. Rule 32 (Day 94) already required three passes but used three fixed, parallel lenses; the Hub's version is stricter — each pass must be strictly more critical than the last (Pass 2 assumes Pass 1 missed something, Pass 3 assumes Pass 2 missed something too), reviewed through a 30-year veteran engineer persona distinct from PERSONA.md's trading-judgment lens. Added as Rule 41, explicitly superseding Rule 32. First real run of it (on the SRPS screener) found two real bugs neither of Rule 32's three lenses alone would have caught: a tz-normalization fix applied to a throwaway copy that never reached the data actually used, and an unbounded per-sector data-fetch loop that a live 12-month check confirmed was a real risk (8-9 sectors simultaneously Improving on 9 separate days this year), not hypothetical.

### 3. Forward Test tab — found and fixed a real display bug (user-reported)
User noticed the Mean-Reversion card's per-ticker table looked incomplete. Root cause: `backend.py`'s `/api/paper-trading/status` caps the closed-trades list at the 20 most recent per system (deliberate response-size guard) — fine for Path A (16 closed) and Path B (15 closed), which never hit the cap, but silently truncated MR (71 closed → 20 shown) and HUB-65 (28 closed → 20 shown) with zero indication anything was hidden. The aggregate stats (win rate, PF, expectancy) were always correct — computed from the full ledger, unaffected. Fixed: added a visible "Showing the 20 most recent closed trades of N total" footer note (matching the Scan tab's own existing 20-row-cap precedent, Day 83) whenever truncated. A second pass (per the new Rule 41) caught a second instance of the same root bug: the "Show tickers (N)" button label was also computed from the capped array length, not the true total — fixed in the same pass.

### 4. Forward Test data investigation (user-reported "I think it's off")
Investigated Path A's real win-rate drop (55.6%→37.5% in 3 days) at the user's request. Confirmed the display itself was correct (my own first diagnostic script had missed the `momentumPathB` key by omission — corrected before concluding anything). The real drop traces to 4 correlated losses from one entry batch: FRT+SKT (both REITs) and PAGP+PAA (literally the general-partner and limited-partner units of the same pipeline company, not two independent trades). This is a live, concrete instance of the already-logged Known Issue (no sector/instrument-correlation awareness in the entry gate, Day 100) — not a new bug, and not actionable mid-freeze. Exit mechanics (entry/stop/exit price consistency) verified clean, no Day-99-style partial-bar contamination.

### 5. Sector Rotation data-sourcing review (user-requested, investigation only — no code changed)
Confirmed `/api/sectors/rotation` (the original 11-sector endpoint) still calls `yf.download()` directly — no multi-provider orchestrator, no Tradier/TwelveData fallback — unlike its two newer siblings (`/api/sectors/sub-industry`, Day 101; `/api/sectors/pullback-screen`, today), both of which use the full orchestrator chain. Already a known, accepted issue (Day 94, Low/Info). Additionally found: `fetchSectorRotation()` in `api.js` is still a whitelisted object reconstruction, not a pass-through — the exact pattern that already caused one real bug (Day 92's `macro_alignment` field silently dropped). The two newer sibling fetch functions both explicitly switched to pass-through citing that lesson; this one was never migrated. Logged as a new Known Issue, not fixed — offered to the user as a contained future fix, not started this session.

### 6. Version-drift correction
`backend.py`'s `BACKEND_VERSION` constant was stuck at `'2.44'` (4 versions behind CLAUDE_CONTEXT's claimed v2.48) and the frontend footer hardcoded `"v4.30"` (20 versions behind the claimed v4.50) — both pre-existing, not from today. Same drift pattern already caught at Days 84/93/96/101. Corrected both source strings as part of this close.

---

## Files Changed

| File | Change |
|---|---|
| `backend/backtest/sector_quadrant_history.py` | New — historical sector-quadrant replay (Gate 0 prereq) |
| `backend/backtest/srps_gate0_signal_count.py` | New — Gate 0 signal-frequency count |
| `backend/backtest/srps_gate1_backtest.py` | New — Gate 1 full portfolio backtest |
| `backend/srps_constants.py` | New — shared SRPS rule constants (backend.py + backtest scripts) |
| `backend/scan_queries.py` | Added `build_sector_query()`, `rank_candidates_by_rs()`, `REAL_ESTATE_TV_INDUSTRY_VALUES`, `XLC_OVERRIDE_TICKERS` |
| `backend/backend.py` | New `GET /api/sectors/pullback-screen` endpoint; `BACKEND_VERSION` corrected 2.44→2.45 |
| `frontend/src/services/api.js` | New `fetchSrpsPullbackScreen()` |
| `frontend/src/components/SectorRotationTab.jsx` | New `SrpsPullbackScreenSection` (collapsible, lazy-loaded) |
| `frontend/src/components/AutomatedPaperTradingPanel.jsx` | Fixed closed-trades truncation display bug (2 instances) |
| `frontend/src/App.jsx` | Footer version string corrected v4.30→v4.51 |
| `docs/claude/stable/GOLDEN_RULES.md` | New Rule 41 (escalating 3-pass review, supersedes Rule 32) |

---

## All Gates Status

Unchanged for the 4 live forward-test tracks. No entry/exit gate, threshold, or frozen config was touched this session. SRPS's own Gate 0/Gate 1 (a new, separate, non-live system) — Gate 0 PASS, Gate 1 FAIL, not proceeding to a live gate.

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority for the 4 live tracks.

---

## Paper Trading Status (live-pulled via `daily_job.py --report`, 2026-08-07)

| Track | Open | Closed | Win Rate | Profit Factor | Notes |
|---|---|---|---|---|---|
| Momentum Path A | 39 | 16 | 37.5% | 0.8827 | Recent drop traced to a correlated 4-trade cluster (FRT/SKT REITs, PAGP/PAA same company) — known correlation gap, not a new bug |
| Momentum Path B | 69 | 15 | 53.33% | 1.5871 | |
| MR (broad) | 19 | 71 | 76.06% | 4.1386 | Past 70% of its 100-trade bar |
| MR (HUB-65) | 1 | 28 | 50.0% | 1.3668 | |

Last job run: 2026-08-06.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS for STA itself**, across all four tracks. MR (broad) is closest to its 100-trade bar at 71/100.
2. Everything else remains parked: IBKR paper-execution plan, fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap, `/ibkr-scan`, Session 28 audit remainder, breakout-alert watcher (ROADMAP #15).
3. *(Optional, offered not requested)* Sector Rotation's original 11-sector endpoint could be brought up to the same standard as its two newer siblings — multi-provider orchestrator + pass-through frontend fetch — a contained, freeze-independent fix if the user wants it.
4. SRPS's backtest infrastructure (`sector_quadrant_history.py`, `srps_gate0_signal_count.py`, `srps_gate1_backtest.py`) stays as reusable tooling — only worth revisiting if the user wants to redesign the entry/exit rules themselves (not the universe) and re-run Gate 1.
