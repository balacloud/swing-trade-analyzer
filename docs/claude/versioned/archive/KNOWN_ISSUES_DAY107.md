# Known Issues — Day 107 (August 14, 2026)

## Changes from Day 106

**Added this session:**
- Fear & Greed gauge on the Analyze page uses a third, stale copy of the sentiment threshold bands (below) — found while three-pass verifying the "STA vs. 100 Years of Trading Principles" code audit.
- Volume confirmation and dual/absolute momentum research spike results — see the "SRPS-style informational findings" entries below; both stay parked, now with real backtest evidence behind the "not yet."

**Investigated, not a bug:** GDXU/SOXL price mismatch between yfinance and IBKR while re-running `/watchlist-report` — both funds had a genuine 3-for-1 forward split (2026-05-25); yfinance was stale/unadjusted, IBKR was correct. Not a code bug, a cross-provider data-freshness gap — resolved by sourcing those two tickers from IBKR directly.

**Freeze status:** unchanged — forward-testing accumulation remains the sole stated priority across all four live tracks. Numbers not re-pulled this session (deep-dive was on Path B's existing data). Last live check remains Day 106 (2026-08-13): Path A 35/24 closed, Path B 92/30 closed, MR broad 7/84 closed, MR HUB-65 3/29 closed.

---

## Open Issues

### Low / Info: Fear & Greed gauge uses a third, stale threshold copy (new, Day 107)
**Severity:** Low / Info
**Description:** The live verdict logic (`categoricalAssessment.js`'s `assessSentiment()`) correctly uses the post-"Bug 0G" bands (55-80 Strong / 50-55 Neutral-Optimistic / 40-50 Neutral-Cautious / else Weak). A second, already-known stale copy sits in `backend.py`'s `/api/fear-greed` endpoint (old 60-80/35-60 bands) — confirmed unread by name anywhere in the frontend, effectively dead. Found while three-pass verifying this session's trading-principles comparison audit: **a third, independent, live, user-visible copy exists in `App.jsx:2438-2439,2446-2449`** — the Analyze page's sentiment gauge bar hardcodes its own color thresholds using the same old 60/35 boundaries, completely independent of both the verdict logic and the backend's dead copy. The verdict itself is unaffected (it uses the correct bands); only the gauge's on-screen color is wrong.
**Fix:** Not actioned this session — flagged in the trading-principles Artifact's footer. A real fix would update `App.jsx`'s inline color thresholds to match `categoricalAssessment.js`'s current 55/50/40 bands (and ideally delete or fix the backend's own dead stale copy while touching this).

### Low / Info: Volume confirmation — first design tested, too restrictive as implemented (new, Day 107)
**Severity:** Low / Info
**Description:** Backtest-only research spike (`backend/backtest/research_spike_volume_momentum.py`, Config F) tested requiring entry-day volume ≥1.5x the 50-day average on top of Config C. Result: cut trades from 75 to 5 (400-ticker survivorship-free universe, 2020-2025) — too small a sample to evaluate performance either way. The finding is structural, not statistical: this specific implementation is too strict to be practical, not proven useless as a concept.
**Fix:** Not actioned — needs a genuinely different design (lower ratio, or a secondary signal rather than a hard gate) before another backtest is worth running. Still gated behind the paper-trading freeze regardless (ROADMAP Priority #11).

### Low / Info: Dual/absolute momentum — tested clean, near-inert in practice (new, Day 107)
**Severity:** Low / Info
**Description:** Same spike (Config G) tested requiring the stock's own trailing 252-day return to beat a 5% risk-free proxy, on top of Config C's existing relative-strength check. Result: only excluded 1 of Config C's 75 trades — a real, clean test, but the filter barely changes anything in practice, since Config C's existing pipeline (trend template + RS + ADX + verdict) already mostly selects stocks with positive absolute returns.
**Fix:** Not actioned — low priority, cheap to add whenever the freeze lifts, won't meaningfully change results either way.

### Low / Info: SimFin ticker-universe drift affects seed-based backtest reproducibility (new, Day 107)
**Severity:** Low / Info
**Description:** Re-running the survivorship-free backtest infrastructure today (seed=42, same parameters as the Day 79 canonical run) produced a materially different Config C baseline (PF 0.97 vs. the documented PF 1.40) — not a bug, traced to `simfin_loader.get_available_tickers()` returning 3,745 tickers today vs. 3,788 at Day 79. The same seed samples a different 400-ticker set from a changed underlying list.
**Fix:** Not actionable — informational. Anyone re-running `backtest_survivorship_free.py` later expecting to exactly reproduce PF 1.40 should expect drift for the same reason. New Golden Rule added.

### Low / Info: Simple Checklist's "PASS" badge is misleading at low pass counts (carried from Day 106)
**Severity:** Low / Info
**Description:** `simplifiedScoring.js`'s checklist verdict field is binary — `'TRADE'` only at 9/9 criteria met, `'PASS'` for everything else. The header badge displays this literal text, so a ticker failing 7 of 9 criteria still shows "PASS."
**Fix:** Not actioned — flagged to the user, no decision made on rewording yet.

### Low / Info: Canadian Analyze Page — real scope now uncertain (carried from Day 59, status softened Day 106)
**Severity:** Low / Info
**Description:** Long-documented as broken for `.TO` tickers; a Day 106 spot-check (CMG.TO) worked correctly on both Simple Checklist and Full Analysis. Not exhaustively retested across other Canadian tickers, so not marked resolved.
**Fix:** Needs a proper multi-ticker recheck before closing or reconfirming.

### Low / Info: SRPS screener's R:R is structurally disconnected from real support/resistance (carried from Day 105)
**Severity:** Low / Info
**Description:** Both sector-level and sub-industry-level SRPS screeners compute target price as `entry + 2.5×risk`, never checked against real chart resistance.
**Fix:** Not actioned — informational screen, disclaimer already covers this.

### Medium: Three different Risk/Reward minimums coexist across the app (carried context, first explicitly logged Day 106 audit)
**Severity:** Low / Info
**Description:** The Simple Checklist wants R:R ≥2.0 (`simplifiedScoring.js`), the live paper-trading gate wants ≥1.2 (`live_signals.py`), and a display-only viability badge wants ≥1.0 (`riskRewardCalc.js`). Not a bug per se — different UI surfaces, different purposes — but there's no single honest answer to "what R:R does STA require."
**Fix:** Not actioned — offered in the trading-principles Artifact's footer, not requested as a fix.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live and backtested fundamental labels.
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus.

### Low / Info items (carried forward, unchanged)
`mean_reversion.py`'s ADX docstring doesn't match its code (Day 92); volume confirmation missing from the core decision engine, now with real backtest context (see above, supersedes the Day 92 entry's "not yet tested" framing); Sector Rotation's original endpoint has no provider fallback (Day 94/103); `fetchSectorRotation()` whitelist-reconstruction pattern (Day 103); MR/momentum entry gates have no regime/sector-correlation awareness (Day 100); HUB-65 backtest is selection-biased by construction (Day 98); HUB-65 and broad MR aren't independent samples (Day 98); momentum's stop/target formula redesign still open (Day 95/96); Session 28 audit's remaining lower-priority findings (Day 91); paper-trading launchd log doesn't capture manual/force-run activity (Day 95); IBKR paper-execution CIRO question (Day 97); no scheduled/proactive breakout alerting (Day 100); SRPS's Rule 6 earnings exclusion not applied in either backtest gate (Day 103, moot — SRPS already failed Gate 1); SimFin key rotation unconfirmed; Defeat Beta import present; Master Framework/Nirmal/HUB-65 watchlist Name/Market Cap N/A by choice; a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable). See `KNOWN_ISSUES_DAY87.md` for full text of older pre-existing items.
