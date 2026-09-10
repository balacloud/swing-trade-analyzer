# Full System Audit — Running Findings Log

> **Purpose:** Running findings log for the 10-group full-system audit scoped Day 107 (plan: `/Users/balajik/.claude/plans/polished-watching-thacker.md`, tracked as Tasks #1-11).
> **Policy (confirmed by user, Day 107):** A finding gets fixed immediately if it's isolated from the 4 live paper-trading forward-test tracks (Momentum Path A/B, MR broad/HUB-65). A finding gets **parked here** — not fixed — if applying it would change behavior those tracks are relying on mid-accumulation (Golden Rule 18: no frozen threshold changes until 100 trades/track; a change resets that track's count to zero). Parked items get actioned once the relevant track(s) clear their bar, or sooner if the user explicitly decides a reset is worth it.
> **Format:** Each entry: Group / Finding / Severity / Disposition (Fixed | Parked-post-freeze | Logged-info, no action needed).

---

## Group 1 — S&R / Pattern / Market-Structure Engine (COMPLETE, Day 107)

### Finding 1 — MTF Confluence weekly levels computed on fabricated dates
**Severity:** CRITICAL
**Disposition:** **FIXED (Day 107)**
**Detail:** `backend.py`'s `/api/sr/<ticker>` route rebuilt its DataFrame from raw `.values` arrays, dropping the real `DatetimeIndex`. `support_resistance.py`'s `_resample_to_weekly()` then fabricated dates via `pd.date_range(freq='D')` (including fake weekends) whenever no real DatetimeIndex was present, producing "weekly" S&R levels from 7-day calendar buckets instead of real 5-day trading weeks. User-visible on the Analyze page's "MTF Confluence: X%" badge and "Weekly Levels" section.
**Why safe to fix now:** Confirmed via grep that `live_signals.py` (the live paper-trading engine) never reads `meta.mtf` at all — display-only, zero impact on any of the 4 live tracks.
**Fix:** `backend.py`, `/api/sr/<ticker>` route — pass `index=hist_data.index` when reconstructing the DataFrame, preserving the real dates. Matches the pattern `live_signals.py` already uses correctly (`.rename()`, not values-reconstruction).
**Verification:** Isolated unit test confirmed the mechanism directly — real business-day DatetimeIndex → 52 weekly bars (correct); the old fake-date fallback → 38 (wrong). Backend auto-reloaded and served a live AAPL request successfully post-fix.

### Finding 2 — Pivot S&R method selects extreme levels, not nearest
**Severity:** HIGH
**Disposition:** **PARKED — revisit after Path B clears its 100-trade bar (currently 44/100)**
**Detail:** `support_resistance.py`'s `_pivot_sr()` — confirmed to be the actual primary/first-attempted S&R method, not a rare fallback — truncates to the 5 most extreme highs/lows (`highs[-5:]`, `lows[:5]`) *before* filtering for proximity to current price. So "nearest support/resistance" can silently mean "the most extreme level within range," not the genuinely closest one.
**Why parked, not fixed:** Confirmed via grep that both `backtest_holistic.py` (the script that produced Path B's validated PF 1.47) and `live_signals.py` (the live engine) call the exact same `compute_sr_levels()` function — this behavior is baked identically into the validated backtest AND the live, mid-accumulating track. It is NOT a live/backtest divergence (unlike the bug that originally created Path B) — live results are consistent with what was actually tested. But changing it now would alter validated behavior while Path B is still accumulating trades, which needs a decision, not a quiet patch.
**Next step when revisited:** Decide whether "true nearest S&R" is worth a fresh backtest + potential new parallel track (same pattern as Path B itself), or whether the extremity-based selection is actually fine/intentional once examined properly.

### Lower-severity items (not urgent, no live-track overlap — batch whenever convenient)
- `SRConfig.mtf_daily_weight`/`mtf_weekly_weight` — dead config fields, never read anywhere; the real confluence "strength" score is a hardcoded `1.0`/`0.6`. Same bug class as the already-fixed Golden Rule 0A hallucinated multiplier. **Severity: MEDIUM.**
- `backend.py`'s `/api/sr/<ticker>` docstring lists a stale 3-method chain, omitting Agglomerative Clustering (added Day 30) and misstating KMeans's position. **Severity: MEDIUM.**
- `level_scores` (touch counts) only populated by the agglomerative method, silently `{}` for pivot — frontend degrades gracefully, no crash, but touch-count data silently absent for a common case. **Severity: LOW.**
- Several thresholds (`volatility_threshold=0.08`, `merge_percent=0.02`, `zigzag_percent_delta=0.05`, `touch_threshold=0.005`, `ath_threshold=0.05`) have no inline citation, unlike other thresholds in the same file. Likely already priced into existing backtest numbers, not a live regression. **Severity: LOW.**

---

## Group 2 — Core Verdict Engine (COMPLETE, Day 107)

Overall: strong result. Every pre-registered threshold (Technical/Fundamental/Risk-Macro, all 12 verdict-priority steps, signal weights by holding period) verified byte-for-byte identical between `categoricalAssessment.js` and `categorical_engine.py`. The JS/Python parity test (`test_verdict_parity.py`, the exact test that caught the original Golden Rule 19 bug) was actually run live: **86,400/86,400 combinations match, 0 mismatches.**

### Finding 1 — Stale RS threshold in file-header docstring
**Severity:** MEDIUM | **Disposition:** FIXED (Day 107)
`simplifiedScoring.js`'s top-of-file criteria list said "RS >= 1.2," but the actual code (verified directly) implements `rsRatio >= 1.0` — the correct, Day-78-reverted, pre-registered value. Pure comment drift, zero behavior impact, zero freeze overlap. Fixed the docstring to match.

### Finding 2 — Equal-weight docstring no longer matches the Day-70 verdict logic
**Severity:** MEDIUM | **Disposition:** FIXED (Day 107)
`categoricalAssessment.js`'s "EQUAL-WEIGHT PRINCIPLE" header claimed "All 4 categories carry equal weight... Verdict logic: count of Strong categories" — but `determineVerdict()`'s actual `strongCount` (confirmed directly) only counts Technical + Fundamental; Sentiment was explicitly excluded at Day 70, Risk-Macro acts as a gate not a counted vote. Pure comment drift (the code itself already has an accurate inline comment explaining this at the point of use) — fixed the header to match.

### Lower-severity items (not urgent, no live-track overlap)
- Pre-registration doc's §5 step 11 wording ("Favorable" only) omits that the code (both langs, matching each other) also allows "Neutral" — a doc-completeness gap, not a code bug. **LOW.**
- Pre-registration doc's §5 step 3 wording is a simplified paraphrase of a 3-branch condition both languages implement identically. **LOW.**
- Pattern target multipliers (1.15/1.20/1.12 for VCP/Cup&Handle/Flat Base) have qualitative but not quantitative backtest citations, unlike the pattern-actionability threshold nearby. **LOW.**

### Confirmed clean
- `liquidityThresholds.js` is genuinely the sole source of truth — no orphaned hardcoded liquidity numbers found elsewhere in the frontend.
- 3 R:R minimums confirmed exact in code: `simplifiedScoring.js` ≥2.0 (Simple Checklist TRADE/PASS), `riskRewardCalc.js` ≥1.0 (App.jsx Trade Setup display badge), pre-reg §6 ≥1.2 (live paper-trading gate, audited in Group 3). No inconsistency bug — three genuinely different UI surfaces with three intentionally different purposes, just no single doc stating all three together until now.

---

## Group 3 — FWD-Testing Frozen-Rules Audit (COMPLETE, Day 107)

Claim Audit against `PAPER_TRADING_PREREGISTRATION.md` Sections 1-11. Strong result on everything entry/exit/cooldown-related: R:R≥1.2 (both Path A and Path B, traced to the same `MIN_RR` constant), Standard holding-period exit management (target/stop/EMA-trail/breakeven-ratchet — all confirmed implemented, not just the headline target/stop), Path B's real S&R gate, MR's entry/exit gate and the Day-82 two-different-stops distinction (still holds correctly), HUB-65's byte-identical gate with only the universe swapped, and per-variant cooldown independence — all **VERIFIED** with direct code tracing, no drift found.

### Finding 1 — Section 8 (VIX position sizing) was never wired into the live engine
**Severity:** initially assessed HIGH, **downgraded to MEDIUM after independent verification of real-world impact** (see below)
**Disposition:** LOGGED — no urgency, no track-reset needed, ties naturally into the already-parked IBKR real-capital execution plan rather than needing its own fix or new track
**Detail:** `get_vix_multiplier()` (the exact, byte-correct 1.0/0.75/0.50 implementation) exists in `trade_simulator.py` but has **zero callers anywhere in the backend** — confirmed independently via grep. The ledger schema (`paper_positions` table, read directly) has no `shares`/`quantity`/`position_size` column at all — only price levels and %/R-multiple outcome fields. `regime_snapshot` records VIX at entry but nothing reads it back. All 4 live tracks enter every trade at implicit full/fixed size regardless of VIX.
**Why this doesn't need urgent action:** Independently confirmed `backend/backtest/metrics.py`'s `compute_metrics()` — the function computing every number the Section 10 Confirmed/Modest/Broken judgment depends on (win rate, profit factor, expectancy) — operates purely on `return_pct`/`return_r` (percentage return and R-multiple). Both are **position-size-invariant**: the same trade at any position size produces the identical % return and R-multiple. So this gap does not corrupt, bias, or affect any of the statistics the 4 tracks are currently being judged on. It only matters once real dollar capital is at stake — i.e., exactly the already-parked IBKR paper-execution plan (Priority #2 in the parked backlog), which will need real share-count sizing wired in before it starts. Recommend folding this into that plan's scope rather than treating it as a standalone fix.

### Confirmed clean / no action needed
- ADX docstring mismatch (`mean_reversion.py`) — confirmed still open, exactly as already tracked in `KNOWN_ISSUES_DAY107.md`. No drift in tracking, nothing to update.
- **Caught and corrected a sub-agent error during my own verification pass**: the audit initially reported `HUB_UNIVERSE` contains 65 tickers vs. the doc's documented 64, flagging a numeric drift. Independently recounted directly (regex extraction + manual line count): **64 tickers, exactly matching the doc.** No drift exists — the sub-agent's count was wrong, not the codebase. Reported here as a reminder that even structured audit output needs spot-verification before being logged as fact.

---

## Group 4b — Analyze Tab, Coherence half (COMPLETE, Day 107)

App.jsx-wide grep sweep for hardcoded-threshold drift (seeded by the Fear & Greed finding). Result: the Fear & Greed bug was NOT an isolated incident, but it is the most severe of a small handful — most of App.jsx's ~50 threshold sites (VIX bands, trend-template bands, rvol bands, R:R bands, MR signal labels, fundamental sub-scores) are correctly synced with their canonical source.

### Finding 1 — Fear & Greed gauge threshold bands (correction to earlier session claim)
**Severity:** MEDIUM | **Disposition:** FIXED (Day 107, this pass)
**Detail:** Earlier in this session this was described as "already fixed" — that was **wrong**. It was found and logged as a Known Issue Day 107 but never actually patched until now. Independently re-verified still stale (60/35 bands) before fixing. Realigned `App.jsx`'s sentiment gauge (both the text-color badge and the 5-tier progress bar) to `categoricalAssessment.js`'s current 55/50/40 bands. Pure display fix, verdict logic itself was never affected (categoricalAssessment.js already had the right bands).

### Finding 2 — `rs52Week` colored with two different band sets 27 lines apart
**Severity:** LOW-MEDIUM | **Disposition:** FIXED (Day 107)
**Detail:** The RS-ratio value badge used stale 1.2/1.0 bands (pre-Day-78-revert) while the RS Interpretation text 27 lines below correctly used 1.0/0.8 — the same `rs52Week` number could render green in one spot and yellow in the other. Ironically inside a block whose own Day-83 comment explicitly warned against exactly this kind of drift. Realigned the first badge to match the already-correct 1.0/0.8 bands (which also match the frozen pre-registration spec's Strong≥1.0/Weak<0.8).

### Finding 3 — ADX "no-trend" cutoff differs between two files (15 vs 20)
**Severity:** LOW | **Disposition:** LOGGED, not fixed — genuinely ambiguous, needs a product decision
**Detail:** `priceStructureNarrative.js`'s Rule 11 uses `ADX < 15` to choose "Choppy — no clear trend" vs. "Downtrend" (only reached after trend-template is already confirmed weak, TT<4). `categoricalAssessment.js` uses `ADX < 20` as a verdict-downgrade gate at a different decision point entirely. Checked directly: these aren't necessarily the same claim — one is a trading-decision gate, the other a narrative-label choice after a different condition already fired. Not confident enough this is actually wrong (vs. intentionally different) to fix unilaterally; needs a human call on whether they should be unified.

### Other findings — all LOW, no action needed
Stale docstrings on 2 backend routes describing pre-Day-51 caching (code itself correct, description just outdated); an RSI color/reasoning philosophy mismatch on an advanced-toggle-only display (bullish-green vs. cautionary-text for the same RSI<30, low exposure); dead code re-implementing a deprecated 75-point verdict scale (`generateScoreExplanation()`, confirmed unused, exactly the pattern Day 83 tried to eliminate but never deleted); several operational thresholds (VIX regime bands, freshness windows, earnings-warning tiers) with no cited research basis, but none are trade-decision-affecting.

### Confirmed clean
Breakout engine (8-state, priority order, field mapping) still coherent — no phantom paths. Price Structure's 12-rule tree fully intact, correctly ordered. `/api/data/freshness` genuinely computes real cache-age, not hardcoded/always-fresh.

## Group 4a — Analyze Tab, Behavioral half (COMPLETE, Day 107)

Live curl + in-browser testing against 7 tickers (AAPL, NVDA, F, SMCI, SPY, CMG.TO, RY.TO) across all 8 Analyze-pipeline endpoints, plus full browser verification (screenshots + console) for SPY/CMG.TO/RY.TO.

### Canadian ticker question — RESOLVED
**The long-carried "Canadian Analyze page — real scope now uncertain" backlog item is now closed.** CMG.TO (small-cap software) and RY.TO (large-cap bank — deliberately a different profile than the earlier Day-106 spot-check) both passed every endpoint, every render path, and full live in-browser verification: correct verdicts, sectors, S&R levels, pattern detection, breakout badges, and MR-signal handling. This is broader coverage than the Day-106 check (which never touched breakout/patterns/mr-signal). No remaining gap found.

### Finding 1 — ETF "Data Source Status Banner" shows a factually wrong message
**Severity:** MEDIUM | **Disposition:** FIXED (Day 107)
**Detail:** Live-reproduced for SPY. `scoringEngine.js` correctly gives ETF tickers `dataQuality: 'N/A'` (a legitimate third state, distinct from `'unavailable'`/`'fallback'`), but `App.jsx`'s banner only checked for `'unavailable'` (red) vs. else (yellow "Using Backup Data Source — Primary providers unavailable... using fallback source") — so every ETF fell into the yellow branch and displayed a message that's simply untrue: no fallback was attempted, ETFs structurally don't have this data category. The correct, calm "F:N/A" messaging already exists and renders correctly elsewhere (`categoricalAssessment.js`'s ETF handling, confirmed separately working). Fixed by excluding `dataQuality === 'N/A'` from triggering this banner at all — the accurate messaging already shown elsewhere covers it.

### Finding 2 — Two falsy-zero risks (React `{value && <div>}` renders "0")
**Severity:** MEDIUM (code-confirmed; not reproduced live today — no ticker happened to hit exactly 0) | **Disposition:** FIXED (Day 107)
**Detail:** `srData.meta?.rvol && (...)` and `srData.meta.tradeViability.risk_reward_context && (...)` both guard numeric fields the backend can legitimately compute as exactly `0.0` (`rvol` when volume is 0; `risk_reward_context` when price sits exactly at a detected resistance level) — this project has hit this exact bug class before (documented React gotcha). A repo-wide sweep found this pattern has otherwise been cleaned up (only 5 instances of `{X && <...}` total in App.jsx, these 2 were the only ones touching numeric fields). Fixed both to `!= null` checks, matching the pattern already used correctly elsewhere in the same file (e.g. `dataFreshness.sources[].ageMinutes`, `breakoutData.rvol`).

### Confirmed clean
No true phantom paths found anywhere in the Analyze pipeline (17+ distinct `srData.meta.*` dotted paths, all `patternsData`/`breakoutData`/`mrData` paths) — every field the frontend reads traces to a real API field. The Day-71-class `stockData.fundamentals.marketCap` bug specifically re-checked and confirmed still fixed. ETF fundamentals handling (`categoricalAssessment.js`'s separate path) confirmed correct — the bug was isolated to the one banner, not systemic.

---

## Group 5 — Scan Tab (COMPLETE, Day 107)

Clean result — no CRITICAL/HIGH/MEDIUM findings, nothing fixed, no regressions. All 5 checklist items verified live with real data, not just code-read:
- Golden Rule 44's breakout-badge fix (4 distinct outcomes) still intact.
- The Day-106 "STA Verdict" column still correctly gated to Retest Entry/Building Base only, still calls the real verdict pipeline (confirmed byte-identical call shape to the Analyze tab's own pipeline) — live-confirmed reachable (RETEST_ENTRY rows actually appeared in a live 10-ticker sample).
- Scan tab and the paper-trading engine (Group 3) confirmed to call the exact same `scan_queries.build_best_query()` — the Day-82/83 candidate-set-divergence bug's fix holds.
- All 3 watchlist presets (Nirmal's, Master Framework, HUB-65) still route through the shared `fetchWatchlistCandidates()` helper, no bespoke-logic drift.

### LOW-severity items only, none fixed (harmless/cosmetic)
- 4 of 6 scan strategy presets (reddit/minervini/momentum/value) have uncited numeric thresholds — only `best` (Config C backtest) is properly grounded.
- `breakout_routes.py`'s 80-bar minimum has no stated rationale.
- `fetchScanStrategies()` in `api.js` maps two fields (`tradingview_available`, `notes`) that don't exist in the real backend response (verified live via curl) — but nothing anywhere reads them, so it's dead code with zero live impact, not a bug worth fixing.

---

## Group 6a — Sectors Tab (COMPLETE, Day 107)

Both Coherence and Behavioral treatment, required given this tab's history of a real bug on every audit pass since Day 93. Result this time: mostly clean, but one real, root-cause-level finding.

### Finding 1 — Golden Rule 30's fix was never applied to the function it's named after
**Severity:** MEDIUM | **Disposition:** FIXED (Day 107)
**Detail:** `fetchSectorRotation()` in `api.js` — the exact function Golden Rule 30 (Day 92) is about — was still a manual whitelist-reconstruction, not a genuine pass-through. It had already silently dropped fields this way *twice before* (`size_rotation`/`size_signal` Day 67, `macro_alignment` Day 92), each time "fixed" by extending the whitelist rather than removing it. Every sibling function built *after* Day 92 (`fetchSubIndustryRotation`, `fetchSrpsPullbackScreen`, `fetchSubIndustryPullbackScreen`) correctly switched to `return response.json()` and cites GR30 in their comments — this one function was left un-migrated, the root cause never actually closed. Live-proven still dropping something today: the backend returns a `cached` field (already displayed elsewhere in the app, e.g. `MarketPhaseBanner.jsx`) that the whitelist had no entry for.
**Fix:** Converted to a genuine pass-through, matching its siblings. Verified live via curl — `cached` and all other fields now reach the frontend. Also added optional chaining at the one unguarded consumer (`App.jsx`'s `getSectorContext()`) that had implicitly relied on the old whitelist's `|| []`/`|| {}` defaults — confirmed the backend's error paths already return non-200 (caught earlier in the fetch chain) so this was extra safety, not covering a real gap, but now consistent with how the rest of the codebase handles pass-through data.

### Confirmed clean (all live-verified, not just code-read)
- The Day-105 Refresh-button fix (Golden Rule 43) still wired correctly end-to-end through all 3 lazy-loaded sub-sections.
- The Day-105 SRPS R:R gap (2.5×risk, never checked against real resistance) confirmed still present as documented — live-computed from real returned candidates (STLD, TRP), not just read from a comment.
- Both fan-out caps (`LIVE_CANDIDATE_LIMIT`, `MAX_CLUSTERS_PER_REQUEST`) confirmed present AND live-triggered today (a real 9→8 cluster cap fired during testing, not hypothetical).
- Both `sectorsCappedFrom`/`clustersCappedFrom` UI displays confirmed rendering.
- No phantom paths in any of the 4 endpoints' frontend consumption.

### Lower-severity items (not urgent)
- `size_signal`'s ±2 RS-Ratio-point threshold has no cited research/backtest basis. **LOW.**

---

## Group 6b — Context Tab (COMPLETE, Day 107)

### Finding 1 — `ContextTab.jsx` bypasses `api.js`, and it was a genuine oversight, not a legitimate divergence
**Severity:** HIGH (architectural) | **Disposition:** LOGGED, not migrated — real fix is a small project (needs `api.js`'s dead Context functions fixed to throw-not-swallow first), not a quick patch
**Detail:** Confirmed via git history: `api.js` gained `fetchContextFull`/`fetchContextNews`/`fetchCycles`/`fetchEcon` in the *same commit* that created `ContextTab.jsx` (Day 62), and `fetchMarketPhase` arrived in `api.js` the same day `ContextTab.jsx` got `loadMarketPhase()` (Day 87) — the component was simply never wired to its own sibling functions, which have sat as 100% dead code (zero callers) ever since. Migrating now isn't a one-line swap: `api.js`'s versions all swallow errors to `null` instead of throwing, which would silently break every visible error banner/retry button this tab already correctly has. Logged as a real, scoped follow-up project, not attempted here.

### Finding 2 — Alpha Vantage news quota wasted on a placeholder ticker + redundant double-fetch
**Severity:** HIGH | **Disposition:** FIXED (Day 107)
**Detail:** `ContextTab.jsx`'s `loadCyclesEcon()` always called the combined `/api/context/<ticker||'SPY'>` endpoint, which backend always internally fetches news for — even when no real ticker was selected (wasting a credit on discarded SPY news), and redundantly a second time via the separate `loadNews(ticker)` call whenever a ticker *was* selected. This exact failure pattern was already self-diagnosed and avoided elsewhere in the same file (a Day 92 comment near `get_sector_rotation()` describes and avoids precisely this) — just never applied to the original call site it was describing.
**Fix:** Added an additive `skip_news` query param to `/api/context/<ticker>` (backend, backward-compatible, defaults to current behavior). `ContextTab.jsx` now always passes `skip_news=true` and relies solely on `loadNews()` for news — eliminates both the wasted-quota case and the double-fetch race in one change. Verified: frontend recompiled clean.

### Finding 3 — PMI/Business-Cycle cards not covered by the Day-91 date-alignment fix
**Severity:** MEDIUM-HIGH | **Disposition:** LOGGED, not fixed — needs porting the existing `_at_months_ago()` fix to 2 more call sites, a contained backend change worth its own session
**Detail:** The Day-91 fix (Golden Rule 26) only patched `_cpi_card()`'s use of `_yoy()`. `_pmi_card()` and `_business_cycle_card()` compute their own raw two-point MoM directly (`data[0][1]` vs `data[1][1]`, `limit=3`), with no date-matching — exposed to the identical failure mode (FRED withholding an observation silently shifts the comparison onto the wrong month) that Day 91 fixed for CPI specifically. `_unemployment_card()` is confirmed safe (already uses `_at_months_ago()`).

### Finding 4 — `ConflictCheck`'s "Cycles FAVORABLE" mislabels the combined 10-indicator regime
**Severity:** LOW-MEDIUM | **Disposition:** FIXED (Day 107)
**Detail:** `ContextTab.jsx` passes the combined cycles+econ `overall_regime` into a prop literally named `cyclesRegime`, and the rendered text said "Cycles FAVORABLE"/"Adverse cycles" — implying a cycles-only read it isn't. Renamed the prop to `overallRegime` and updated the message text to "Macro Regime"/"macro regime," matching `RegimeBanner.jsx`'s already-established "OVERALL MACRO REGIME" terminology.

### Finding 5 — `MarketPhaseBanner` silently disappears on error, unlike every other error state on the same tab
**Severity:** MEDIUM | **Disposition:** FIXED (Day 107)
**Detail:** Returned `null` on any error (explicit comment: "fail silent, don't block the tab"), while `cyclesError`/`newsError` both show a visible red banner + Retry. Directly contradicts this project's own standing UI principle (visible muted state over hiding). Fixed to show a calm, muted gray banner ("Market phase unavailable") instead of vanishing — deliberately not red/alarming, since this is a genuinely lower-stakes informational feature, unlike cycles/econ.

### Confirmed clean
No whitelist-reconstruction bug in `ContextTab.jsx`'s bypass (genuine pass-through end to end, unlike the Sectors-tab bug found earlier this session). Day 92 macro_alignment connection and Day 93 phase/regime reconciliation both verified working live. Day 93 Seasonal Regime fix confirmed no regression. No phantom paths across all 5 endpoints.

### Lower-severity items (not urgent)
Several historical-return figures in cycles/econ cards (Yield Curve, Fed Funds, CPI regime, Presidential Year, Seasonal) have no citable source beyond a vague "Historical macro factor analysis" tag — PMI already got an honest "proxy" disclaimer Day 91, the others didn't. News aggregate sentiment counts vs. displayed article list draw from different-sized populations by design, uncommunicated to the user. Both **LOW**, informational-only, not trade-decision-affecting.

---

## Group 7 — Value Tab (COMPLETE, Day 107)

### Claim Audit — the ROE "Buffett" vs. "ChatGPT research validated" tension (Session 28, Day 91)
**Resolution:** **MISLEADING, not HALLUCINATED and not cleanly VERIFIED.** The project's own Day-75 design spec (`VALUE_TAB_SPEC.md`) already did the honest version of this analysis and labeled the ROE/Buffett link **PLAUSIBLE** (one tier below ROIC/Damodaran's VERIFIED) — that nuance never survived into the UI, which shows a flat, unqualified "Buffett" badge implying a specific source for a 3-tier numeric threshold (15/12/10) Buffett never published. The code comment "ChatGPT research validated" turns out to be the *more* accurate label — the spec's own citation confirms those specific numbers came from a ChatGPT Deep Research synthesis, not from Buffett or Damodaran. Both labels are answering different questions ("whose general principle" vs. "where did these numbers come from"); neither is fabricated, but the UI overstates certainty the project's own research explicitly declined to claim.
**Disposition:** LOGGED — a wording decision, not a code bug; needs the user's call on replacement copy (e.g. "Quality heuristic (Buffett-associated)" vs. keeping "Buffett" with a tooltip caveat), same treatment as the still-open Simple Checklist "PASS" wording question from Day 106.

### Finding 1 — FCF Yield's "negative" verdict has no matching UI style, silently shows "N/A"
**Severity:** HIGH (live-reproduced) | **Disposition:** FIXED (Day 107)
**Detail:** Confirmed live on RIVN (`value: -6.9%, verdict: "negative"`) and F (`value: -13.9%, verdict: "negative"`) — both showed the correct negative number but a gray "N/A" badge instead of a red "Weak"/negative indicator, because `VERDICT_STYLES` in `ValueTab.jsx` had no `negative` key and silently fell back to `.na`.
**Fix:** Added a `negative` style entry (red/rose, labeled "Negative"). Frontend recompiled clean.

### Finding 2 — FCF Yield badged "Damodaran" when the design spec cites him as a critic of exactly this metric
**Severity:** MEDIUM | **Disposition:** LOGGED, same wording-decision family as the ROE finding above
**Detail:** `VALUE_TAB_SPEC.md` explicitly frames single-year FCF yield as "NOT a primary-source metric" and quotes Damodaran calling it "more noise than information" — yet the UI badges it "Damodaran" as if he endorses it. Worse version of the same badge-overclaim pattern as the ROE finding.

### Finding 3 — Single-year FCF Yield gets a pass/fail badge despite the spec explicitly saying it shouldn't
**Severity:** MEDIUM | **Disposition:** LOGGED, needs a product decision (remove the badge vs. compute a real 3-yr average per the spec's own requirement)
**Detail:** `VALUE_TAB_SPEC.md` explicitly says FCF Yield should have "No pass/fail badge" and require a 3-year average, citing single-year FCF as noisy — the actual code computes single-year FCF (correctly labeled as such) but still assigns a colored verdict badge anyway, contradicting its own spec's explicit guard.

### Confirmed clean
Tab correctly stays scoped to Phase 1 only, no Phase 2/3 capability overclaimed anywhere. Graham Number formula and the P/E <15 boundary both trace cleanly to cited sources. `roa` is computed and returned but never rendered — dead field, zero risk, not a bug.

### Lower-severity items (not urgent)
ROIC's "decent" band (0-5pt spread) drifted from the spec's ~±2pt "yellow" band with no stated reason; P/E's "<25 fair" cutoff and PEG's "<1.5 stretched" cutoff are both uncited magic numbers. All **LOW**.

---

## Group 8 — Validate + Data Sources Tabs (COMPLETE, Day 107)

### Main deliverable — the Day-91 "shows healthy without probing" finding: SPLIT, not one fact
**Settled with a live natural experiment**, not just a code read: TwelveData's circuit breaker happened to be genuinely OPEN in production during this audit (confirmed via `/api/health`'s real `circuit_breakers.twelvedata.state: "open"`), giving a real failure to test against.

| Signal | Still broken? |
|---|---|
| Data Sources tab's per-provider "Data Source Map" | **Fixed** (at some point after Day 91, undocumented) — live-confirmed correctly showing TwelveData red/"circuit open — skipped" and yfinance as the active fallback, both via API and a live screenshot. |
| Header "● Backend Connected" indicator (every tab) | **Still the Day-91 bug** — `/api/health`'s `status` was a hardcoded `'healthy'` literal, incapable of ever reflecting anything. |
| Per-ticker Provenance panel | **Still the Day-91 bug, and the sharper original complaint** — live-tested: a genuine 404 fetch failure (`ZZZZZINVALID`) produced byte-identical provenance output before and after. No code path anywhere records "this fetch just failed" vs. "never attempted." |

### Finding 1 — `/api/health`'s `status` field was a hardcoded literal
**Severity:** MEDIUM | **Disposition:** FIXED (Day 107)
**Detail:** Never conditional on anything — a pure liveness check ("is Flask running") mislabeled as a health check, driving the header's connection dot across every tab.
**Fix:** Now derived from whether the app's own core subsystems actually loaded (`SR_ENGINE_AVAILABLE`, `DATA_PROVIDER_AVAILABLE`, `SQLITE_CACHE_AVAILABLE`) — deliberately NOT tied to individual provider circuit-breaker state, since a single provider being circuit-broken is normal, self-healing, by-design behavior (already correctly shown on its own in the Data Sources tab) and shouldn't flip a global indicator red for expected operation. Verified live — status stays `'healthy'` under today's actual (fully-loaded) conditions, only differs in a genuinely-degraded case.

### Finding 2 — Per-ticker provenance can't distinguish "never fetched" from "just failed"
**Severity:** HIGH | **Disposition:** LOGGED, not fixed — needs a genuinely new piece of state (a failure-attempt record, keyed by ticker, wired into every fetch failure path), not a quick patch. This is the real, still-open core of the original Day-91 complaint.

### Confirmed clean / no action
Both dead validation routes (`/api/validation/results`, `/api/validation/history`) reconfirmed genuinely unreachable, no hidden callers. `/api/validation/run` confirmed doing genuine live web-scrape cross-validation (a real 29-second call, real AAPL variance data) — entirely unrelated to the health-check finding. `validation.py` import resolves cleanly, was never actually a mystery.

### Lower-severity items (not urgent)
`/api/cache/status`'s own hardcoded `status: 'healthy'` — same pattern as Finding 1, but confirmed genuinely unused by the frontend as a health signal, so left as-is (LOW, decorative only). `cache_manager.py`'s TTL constants (24h OHLCV, 7-day fundamentals, 6h cycles/econ, 4h news) remain uncited. README documents the 2 dead validation routes without noting they're orphaned.

---

## Group 9 — Providers Package, scoped (COMPLETE, Day 107)

Deliberately scoped re-verification, not a fresh-exhaustive pass, per the plan's own stated exception (justified by real recent audit density here — Day 83, Day 95-96).

### Golden Rule 22 (shared cross-process SQLite state) — VERIFIED, fully intact
Both `rate_limiter.py` and `circuit_breaker.py` still persist exclusively to `backend/data/provider_state.db` under atomic `BEGIN IMMEDIATE` transactions. No fallback to in-memory-only state exists.

### Golden Rule 36 (circuit breaker vs. ticker-not-found conflation) — VERIFIED across all 7 provider files, zero regressions
Checked file-by-file, not sampled: yfinance, twelvedata, finnhub, fmp, alphavantage, tradier, stooq all correctly exempt `DataNotFoundError`/`InsufficientDataError` from tripping the breaker. Notably `fmp_provider.py` was never even touched by the original Day-96 fix commit — it was already built compliant.

### Findings — all LOW/INFO, 3 fixed (trivial doc corrections), rest logged
- **FIXED:** `orchestrator.py` had 2 stale per-method docstrings still listing "Stooq" (removed Day 82) instead of "Tradier" (added Day 83) — the correct chain was already right in the same file's module-level docstring, just not the two method-level ones. Corrected both.
- **FIXED:** `exceptions.py`'s `InsufficientDataError` docstring said "e.g., < 150 bars" — every real call site actually uses `< 10`. Corrected.
- **LOGGED, not fixed:** `backtest_adapter.py` has a real latent logic gap (MEDIUM) — for short-span historical backtest windows outside the trailing-2-years-from-today, `dp.get_ohlcv()` is called with a hardcoded `'2y'` period regardless of the actual requested date range, which could silently return an empty/wrong DataFrame for an old, short window. Not currently triggered (the one real in-repo caller uses a multi-year range that avoids this path), but worth a proper look before this function gets a new caller. Backtest-adjacent code, treated with the same care as anything touching the pre-registration-validated tooling.
- **LOGGED, not fixed (inert):** `get_provider_status()` hardcodes FMP's daily quota as unlimited (`-1`) instead of reading the real 250/day limit — harmless since FMP isn't in any active fallback chain today.
- Two INFO-level items (a dead `roa`/ROTA field substitution in `field_maps.py`, an uncited-but-self-documented growth-value heuristic) — no action needed.

---

## Group 10 — Forward Tab + Settings (COMPLETE, Day 107 — final group)

### `variant` disambiguation (Golden Rule 38) — VERIFIED, no bug found
The UI correctly never conflates momentum's gate-experiment axis with MR's universe axis. "Path A"/"Path B" labels are reserved for momentum only; MR shows plainly as "Mean-Reversion" and "Mean-Reversion (HUB-65)" with a deliberately different badge color and an explicit caption ("a different bet, not a better strategy"). The raw `variant` string values never even reach the frontend — the backend resolves them into 4 independently-labeled objects server-side. Well-executed.

### Finding 1 — Settings risk slider allows up to 5%, against the app's own documented 2% Van Tharp ceiling
**Severity:** MEDIUM | **Disposition:** LOGGED — a genuine product decision (should the ceiling be hard-capped at 2%, or is 2-5% an intentional range with 2% as the recommended floor?), not something to silently pick a side on
**Detail:** The Settings tab's "Risk Per Trade" slider ranges 2%-5%, labeling 2% "Conservative" — implying it's a floor, not the ceiling — directly under a "Van Tharp Principle" banner, while the project's own documentation elsewhere states "Never risk more than 2% per trade (Van Tharp)." Same tension as the ROE attribution and PASS-badge-wording items — needs your call, not a unilateral fix.

### Finding 2 — Manual journal and automated panel both label a stat "Expectancy," but they're different formulas
**Severity:** MEDIUM | **Disposition:** FIXED (Day 107)
**Detail:** The automated Forward Test panel's "Expectancy" is mean %-return per trade; the manual journal's "Expectancy" (same tab) is the Van Tharp R-multiple formula. Both were technically distinguishable via the inline %/R suffix on the number itself, but the label carried no disambiguation, inviting a direct "my journal vs. the automated ledger" comparison that isn't actually apples-to-apples.
**Fix:** Relabeled to "Expectancy (%)" (automated panel) and "Expectancy (R)" (manual journal).

### Confirmed clean
No data leakage between the automated (backend-API-driven) and manual (pure localStorage) systems — separate storage, visually distinct styling, deliberate separation per the automated panel's own top-of-file comment. Settings persistence (`loadSettings`/`saveSettings`) verified working correctly. No phantom paths in `/api/paper-trading/status` consumption. The "runs every weekday at 17:30 ET" UI claim matches the real launchd schedule exactly.

### Lower-severity items (not urgent)
Manual journal computes SQN but not Profit Factor; automated ledger computes Profit Factor but not SQN — asymmetric stat surfaces (not wrong, just not directly comparable either way). `positionSizing.js` has 2 dead config fields (`minRiskPercent`/`maxRiskPercent`) never read anywhere — the slider's actual 2-5 bounds are separate hardcoded literals that happen to currently match. Both **LOW**.

---

## Full audit — all 10 groups complete (Day 107)
