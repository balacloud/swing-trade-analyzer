# Known Issues — Day 108 (August 14, 2026)

## Changes from Day 107

**Resolved this session (full 10-group system audit — see `docs/claude/versioned/FULL_AUDIT_FINDINGS_DAY107.md` for complete detail):**
- Fear & Greed gauge's 3rd stale threshold copy — fixed (App.jsx realigned to the correct 55/50/40 bands).
- Canadian Analyze Page — confirmed fully working end-to-end (CMG.TO + RY.TO, all 8 endpoints, full live browser check). Closing this out; no longer "uncertain."
- The 3-different-R:R-minimums item — clarified, not a bug: `simplifiedScoring.js` ≥2.0 (Simple Checklist), live paper-trading gate ≥1.2 (out of this session's scope, in `PAPER_TRADING_PREREGISTRATION.md`), `riskRewardCalc.js` ≥1.0 (display-only badge). Three genuinely different UI surfaces, three different purposes — no inconsistency, just needed documenting in one place. Closing.
- `fetchSectorRotation()`'s whitelist-reconstruction pattern (Day 103 carried item) — fixed, converted to a genuine pass-through.
- Session 28 audit's ROE attribution question (Value tab) — resolved honestly (MISLEADING, not fabricated) — see new item below for the resulting wording decision.
- Session 28 audit's Validate/Data Sources "status without probing" finding — partially fixed. `/api/health`'s hardcoded-always-healthy status is fixed; the per-ticker provenance gap is still open (see new item below, this is the sharper, still-live half of the original finding).

**New issues found this session, added below:** VIX position-sizing gap, pivot S&R extremity-vs-nearest selection, ContextTab's `api.js` bypass, provenance can't distinguish never-checked-vs-failed, PMI/Business-Cycle date-alignment gap, Settings risk slider ceiling, Value tab FCF Yield badge-vs-spec mismatch, a latent `backtest_adapter.py` logic gap, FMP's hardcoded quota display.

**Freeze status:** unchanged — forward-testing accumulation remains the sole stated priority. Live numbers pulled at session close (2026-08-14): Path A 34 open/30 closed, Path B 81 open/44 closed, MR broad 6 open/**90 closed** (closest to its 100-trade bar), MR HUB-65 2 open/30 closed.

---

## Open Issues

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (new, Day 108 — the surviving core of the Day-91 finding)
**Severity:** High
**Description:** `GET /api/provenance/<ticker>` produced byte-identical output for a ticker before and after a real, confirmed fetch failure (live-tested against a genuine 404). There's no code path anywhere that records "the last fetch attempt for this ticker failed" vs. "never attempted" — both currently look identical to the UI. The per-provider health map (Data Sources tab's "Data Source Map") was separately confirmed genuinely fixed and doesn't have this problem — this is specifically the per-ticker panel.
**Fix:** Needs a new piece of state (a failure-attempt record, keyed by ticker, wired into every fetch failure path) — a real, scoped project, not a quick patch.

### Medium: VIX position-sizing was never wired into the automated paper-trading engine (new, Day 108)
**Severity:** Medium (verified zero impact on current live-track statistics — see below)
**Description:** `PAPER_TRADING_PREREGISTRATION.md` Section 8's VIX-based position-size multiplier (1.0/0.75/0.50 for VIX <20/20-30/>30) has zero callers anywhere in the backend; the ledger schema has no share-count/position-size field at all. All 4 live tracks enter every trade at implicit full size regardless of VIX, since inception.
**Verified not urgent:** `compute_metrics()` — the function computing every stat the tracks are judged on — operates purely on %-return and R-multiple, both position-size-invariant. This gap doesn't corrupt or bias any current result.
**Fix:** Ties naturally into the already-parked IBKR real-capital execution plan, which will need real share-count sizing wired in before it starts anyway.

### Medium: Pivot support/resistance method selects extreme levels, not nearest (new, Day 108)
**Severity:** Medium
**Description:** `support_resistance.py`'s `_pivot_sr()` — confirmed the actual primary method, not a rare fallback — truncates to the 5 most price-extreme highs/lows before filtering for proximity, so "nearest support/resistance" can silently mean "the most extreme level within range."
**Why not fixed:** Confirmed this exact behavior is baked identically into both the backtest that validated Momentum Path B (PF 1.47) and the live engine itself — not a live/backtest divergence, so live results are consistent with what was tested. Changing it now would alter validated behavior while Path B is still accumulating (44/100).
**Fix:** Revisit once the freeze lifts — decide whether "true nearest S&R" is worth a fresh backtest + potential new parallel track.

### Medium: `ContextTab.jsx` bypasses the app's shared fetch layer (new, Day 108)
**Severity:** Medium
**Description:** Confirmed a genuine oversight, not a legitimate architectural divergence — `api.js` gained matching Context-tab functions in the same commits that added the features to `ContextTab.jsx`, but the component was never wired to them; those 5 functions are 100% dead code.
**Fix:** Not a quick patch — `api.js`'s versions swallow errors to `null` instead of throwing, which would silently break this tab's existing visible error/retry banners if adopted as-is. Needs both fixed together, a real scoped follow-up.

### Medium: Value tab's "Buffett" ROE attribution overstates certainty (new, Day 108, resolves the Session 28/Day 91 finding)
**Severity:** Medium
**Description:** The project's own Day-75 design spec already labeled the ROE/Buffett link PLAUSIBLE (one tier below ROIC/Damodaran's VERIFIED) — that nuance never reached the UI, which shows a flat "Buffett" badge for a 3-tier numeric threshold (15/12/10) that traces back to a ChatGPT research synthesis, not to Buffett or Damodaran specifically. The code's "ChatGPT research validated" comment is, in that narrow sense, the more accurate label. FCF Yield has the same pattern, worse — badged "Damodaran" when the design spec quotes him as a critic of exactly that simplified metric.
**Fix:** A wording decision, not a code bug — needs the user's call on replacement copy (e.g., "Quality heuristic (Buffett-associated)").

### Medium: Settings' risk slider allows up to 5%/trade against the app's own documented 2% Van Tharp ceiling (new, Day 108)
**Severity:** Medium
**Description:** The slider ranges 2%-5%, labeling 2% "Conservative" (implying a floor) directly under a "Van Tharp Principle" banner, while project documentation elsewhere states "Never risk more than 2% per trade (Van Tharp)."
**Fix:** Needs a product decision — hard-cap at 2%, or keep the range with clearer framing that 2% is the recommended ceiling, not the floor.

### Low-Medium: PMI/Business-Cycle econ cards not covered by the Day-91 date-alignment fix (new, Day 108)
**Severity:** Low-Medium
**Description:** The Day-91 fix (Golden Rule 26) only patched `_cpi_card()`'s use of `_yoy()`/`_at_months_ago()`. `_pmi_card()` and `_business_cycle_card()` compute a raw two-point MoM directly with no date-matching — exposed to the identical failure mode (FRED withholding an observation silently shifts the comparison onto the wrong month) Day 91 already fixed for CPI specifically. `_unemployment_card()` confirmed safe.
**Fix:** Port the existing `_at_months_ago()` fix to the 2 remaining call sites — a small, contained backend change.

### Low: Value tab's FCF Yield gets a pass/fail badge despite the design spec saying it shouldn't (new, Day 108)
**Severity:** Low
**Description:** `VALUE_TAB_SPEC.md` explicitly says single-year FCF Yield should have "No pass/fail badge" (citing it as noisy, requiring a 3-year average) — the actual code computes single-year FCF (correctly labeled as such) but still assigns a colored verdict badge anyway.
**Fix:** Needs a product decision — remove the badge, or compute a real 3-year average per the spec's own requirement.

### Low: `backtest_adapter.py` has a latent short-date-range logic gap (new, Day 108)
**Severity:** Low
**Description:** For a short historical backtest window outside the trailing-2-years-from-today, `dp.get_ohlcv()` is called with a hardcoded `'2y'` period regardless of the actual requested date range — could silently return an empty/wrong DataFrame. Not currently triggered (the one real in-repo caller uses a multi-year range that avoids this path).
**Fix:** Worth a proper look before this function gets a new caller. Backtest-adjacent, treat with the same care as anything touching pre-registration-validated tooling.

### Low / Info: Volume confirmation — first design tested, too restrictive as implemented (carried from Day 107)
**Severity:** Low / Info
**Description:** Backtest-only research spike tested requiring entry-day volume ≥1.5x the 50-day average — cut trades from 75 to 5, too strict to evaluate.
**Fix:** Not actioned — needs a genuinely different design before another backtest is worth running. Still gated behind the freeze regardless.

### Low / Info: Dual/absolute momentum — tested clean, near-inert in practice (carried from Day 107)
**Severity:** Low / Info
**Fix:** Not actioned — low priority, cheap to add whenever the freeze lifts.

### Low / Info: SimFin ticker-universe drift affects seed-based backtest reproducibility (carried from Day 107)
**Severity:** Low / Info
**Fix:** Not actionable — informational.

### Low / Info: Simple Checklist's "PASS" badge is misleading at low pass counts (carried from Day 106)
**Severity:** Low / Info
**Fix:** Not actioned — flagged to the user, no decision made on rewording yet.

### Low / Info: SRPS screener's R:R is structurally disconnected from real support/resistance (carried from Day 105)
**Severity:** Low / Info
**Fix:** Not actioned — informational screen, disclaimer already covers this. Related to (but distinct from) the new pivot-S&R finding above — SRPS's issue is its fixed 2.5x multiplier never checking real resistance; the pivot finding is about which S&R levels get selected as candidates in the first place.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus.

### Low / Info items (carried forward, unchanged)
`mean_reversion.py`'s ADX docstring doesn't match its code (Day 92); Sector Rotation's original endpoint has no provider fallback (Day 94/103); MR/momentum entry gates have no regime/sector-correlation awareness (Day 100, accepted design tradeoff); HUB-65 backtest is selection-biased by construction (Day 98); HUB-65 and broad MR aren't independent samples (Day 98); momentum's stop/target formula redesign still open (Day 95/96); paper-trading launchd log doesn't capture manual/force-run activity (Day 95); IBKR paper-execution CIRO question (Day 97); no scheduled/proactive breakout alerting (Day 100); SRPS's Rule 6 earnings exclusion not applied in either backtest gate (Day 103, moot — SRPS already failed Gate 1); SimFin key rotation unconfirmed; Defeat Beta import present; Master Framework/Nirmal/HUB-65 watchlist Name/Market Cap N/A by choice; a genuinely missed paper-trading job run on 2026-07-14 (confirmed, not recoverable); FMP's `get_provider_status()` hardcodes its daily quota as unlimited (`-1`) instead of the real 250/day limit — inert since FMP isn't in any active fallback chain (new, Day 108, LOW).
