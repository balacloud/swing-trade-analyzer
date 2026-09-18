# Project Status — Day 118

> **Consolidated close.** No formal `/sta-end` ran between Day 112 and this one — Days 113,
> 116, 117, and 118 each shipped real, committed, live-verified work, but only informally
> (docs updated inline as work happened, no session-close pass). This file closes all four at
> once. Days 114-115 produced planning documents only (`SR_PIVOT_FIX_PLAN_DAY112.md`'s Phase
> 3-4 re-verification, `MTF_VCP_FIX_PLAN_DAY115.md`), no code shipped those days.

**Version:** App v4.62, Backend v2.51, Frontend v4.59 (was v4.61 / v2.49 / v4.56 at Day 112 close)

---

## What Happened (Day 113 → 118)

### Day 113 — Paper-trading program discontinued (user's explicit direction)
User: *"I don't want to paper trade... I want to use Claude and STA as analysis engine and
recommendation, I will take care of stuff myself."* Confirmed scope (full stop, graceful
wind-down) via one clarifying question before touching the live system.

| File | Change |
|---|---|
| `backend/paper_trading/daily_job.py` | New `PROGRAM_DISCONTINUED` flag gates only Step 3 (new-signal generation); existing positions still wind down by their own exit rules. Verified live via `--force` run: 0 new signals, 2 positions closed normally. |
| `backend/paper_trading/live_signals.py` | Path B's `B_revised_rr` gate + `check_sr_gate()` call removed from signal generation (retired, docstring warns re-validate before any successor). |
| `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` | Top-of-file discontinuation notice + final Change Log row. |
| `frontend/src/components/AutomatedPaperTradingPanel.jsx` | Discontinuation banner; "Force Run Now" relabeled "Check for closes". |
| `docs/claude/stable/ROADMAP.md`, `CLAUDE_CONTEXT.md` | Priority #1 → DISCONTINUED, #13 (IBKR) → DECLINED not parked. Freeze lifted. |

MR (broad) — 194+ closed, PF ~2.5 — stands as the program's one confirmed result.

### Day 116 — Volume effort-vs-result: OBV sign bug + partial-bar RVOL fix + new same-day read
Opus-planned (`docs/claude/design/VOLUME_EFFORT_VS_RESULT_PLAN_DAY116.md`), 3 commits.

- **`calculate_obv()`'s `trend` sign bug fixed** (`backend.py`) — was biased toward `'rising'`
  when cumulative OBV is negative (a `*1.02`/`*0.98` comparison inverts sign for negative
  numbers). Sign-safe `±2%·abs(obv_sma)` band. Measured: 5/150 tickers flip (all
  `rising`→`flat`), zero `rising`↔`falling` flips — proven the live ⚠️ DIST badge can't be
  affected (fires only on `falling`).
- **The existing 20-day OBV divergence sentence** (live since Day 49, previously hover-only)
  surfaced as visible text on the Volume card (`getObvHorizonRead()`, new
  `frontend/src/utils/volumeThresholds.js` function).
- **New finding, fixed same session:** `meta.rvol` read the still-forming intraday bar with no
  partial-bar guard — mid-session read ~half its true value. New `meta.candle.barComplete` +
  `meta.prevBar` fields (backend), wired into the Volume card, the ⚠️ DIST badge, and
  `priceStructureNarrative.js`'s breakout-watch line (broadened beyond the original plan's
  scope, at the user's direction).
- **New same-day effort-vs-result read** — today's RVOL crossed against today's price move in
  ATR units (`getEffortVsResultRead()`), the one genuinely new signal; explicitly disclosed as
  unbacktested/first-principles in its own copy.
- Verified live on NVDA + RIVN (browser); found and fixed one wording bug during that check
  ("Today lean:" → "Lean:").

### Day 117 — Absolute-momentum informational read (dual momentum's 2nd leg)
Opus-planned (`docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md`), 1 commit.

- New `frontend/src/utils/absoluteMomentum.js` — a stock's own trailing ~1-year return read
  against a 5% cash proxy (the real Day 107 backtest constant, `backtest_holistic.py:108`, not
  an invented number). Zero backend changes — both display surfaces already had the number.
- `simplifiedScoring.js`'s Momentum criterion exposes `stockReturnPct` as a **sub-field on the
  existing `momentum` object** — deliberately not a new top-level key on `results.criteria`,
  which is iterated elsewhere (`passCount`, the "missing" list, one-card-per-key render) and
  would have silently become a 10th checklist criterion. This near-miss was the Opus plan's
  main catch — see new Golden Rule 57.
- Shows on both the Simple Checklist Momentum card and the Full Analysis RS card. Verified
  live: AAPL (`above_cash`, 7/9 criteria unchanged), MSFT (`negative` branch, FAIL card renders
  the info line without implying it caused the fail, 5/9 unchanged).
- The Day 111 decision NOT to gate on this (excluded only 1 of 75 backtested trades) is
  unchanged and stays closed — only the read is new.

### Day 118 — MTF Confluence graduated score + VCP resistance-based target (Phases 3-4 of the S&R fix chain)
Opus-planned Day 112, re-verified against current code Day 115
(`docs/claude/design/MTF_VCP_FIX_PLAN_DAY115.md`), implemented and 2-commit split this session.

- **MTF Confluence's `strength` field** — was dead (computed, serialized, read by no consumer)
  — now a real graduated score blending normalized daily/weekly touch counts with proximity to
  the weekly match. Verified to reproduce the old flat 1.0/0.6 constants at full touch
  saturation via direct unit test. Surfaced as Strong/Moderate/Weak on the ★ tooltip.
- **Synthetic (ATR/Fibonacci-projected) levels** now excluded from the confluence set entirely,
  not just the denominator label — new `meta.mtf.projected_excluded`, shown in the UI badge
  rather than left silent. No live ATH candidate found in a 47-ticker sweep (rarer than
  expected under the Day 112 pivot fix), so verified via direct unit test instead, including
  the all-levels-projected division-by-zero edge case.
- **VCP's flat +15% target retired** — now the nearest real resistance above the pivot,
  falling back to the largest contraction's measured-move depth when no real resistance exists
  (or the whole ticker is ATH/ATL-flagged, in which case even a level above the pivot is
  synthetic). Returns `null`, never a fabricated %. `getActionablePatterns()` gains an `srData`
  param; `App.jsx` passes the just-fetched `data.sr`, not the async state variable, to avoid a
  stale-read race.
- Verified against CVX (the one live VCP-detected ticker found in a 58-ticker sweep — its own
  resistance sits below the pivot, so it live-exercised the fallback branch,
  `$217.78 + ($192.69-$164.78) = $245.69`); the primary-resistance and ATH-guard branches
  verified via direct logic test against real CVX data plus constructed cases.
- One live-browser visual check for MTF completed (NVDA); the browser extension disconnected
  mid-session for the VCP check, so that fix was verified at the logic level only, not visually
  click-through-confirmed.

---

## Artifacts updated this session
- "STA vs. 100 Years of Trading Principles" — row 04 (Volume) updated Day 116, row 02
  (Momentum) updated Day 117. Both stay Partial: Volume's read is informational by design;
  Momentum's absolute-return leg is now visible but still not combined into one enforced rule
  the way the source principle prescribes.

## All Gates Status
No live forward-test gates exist anymore (program discontinued Day 113). All work this
session was pure Analyze-page display/read logic — confirmed freeze-independent before
starting each piece, consistent with Golden Rule 54 discipline.

## Next Session Priorities
1. 🔴 High: per-ticker data provenance can't distinguish "never checked" from "just failed"
   (Day 108, oldest open item, no plan written yet).
2. 🟡 6 Medium findings with no plan written: VIX sizing never wired in (may now be moot —
   the engine it would wire into is discontinued, worth a quick check before planning);
   `ContextTab.jsx` bypasses the shared fetch layer; Value tab ROE attribution wording; Settings'
   risk slider allows 5%/trade against the app's own 2% ceiling; Backtest↔Live fundamentals
   mismatch; two endpoints bypass circuit-breaker protection.
3. 🧹 Cleanup batch, zero risk: 5 dead `App.jsx` functions (confirmed via build warnings —
   `cacheResult`, `getViabilityStyle`, `generateActionableRecommendation`,
   `generateScoreExplanation`, `getSubScoreInfo`), stale Data Sources "Defeat Beta API" doc
   line, Value Tab investor-name relabeling.
4. Revisit the VCP visual click-through check (browser extension disconnected mid-verification
   this session) if a doubt ever surfaces about it in practice.
