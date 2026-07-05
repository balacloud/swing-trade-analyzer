# Fable Review Remediation Plan

> **Purpose:** Actionable plan to address findings from the Day 78 Fable 5 full-system review (intent, code, docs, live-market viability). Written to be executed by Claude (Sonnet) across multiple sessions with no additional context needed.
> **Source:** Fable 5 deep review, Day 78 (July 5, 2026) — backtest engine, verdict logic, MR engine, live-data path, docs.
> **Location:** `docs/claude/design/`
> **Status:** NOT STARTED
> **Last Updated:** Day 78 (July 5, 2026)

---

## How to Use This Document (instructions for executing Claude)

1. Execute phases **in order**. Within a phase, execute tasks in order unless marked independent.
2. **One task at a time.** Read the target file first, make the change, verify the acceptance criteria, then move on (Golden Rules #2, #7, #13).
3. Mark each task's Status line (`NOT STARTED → IN PROGRESS → DONE (Day N)`) as you go. Update this file directly.
4. This plan is **compatible with the feature freeze**: every task is a bug fix, validation fix, hygiene fix, or measurement task. Nothing here adds user-facing features.
5. Do NOT re-tune any strategy thresholds while executing this plan. Phase 0 freezes the config; changing thresholds afterward invalidates the paper-trading experiment.
6. At session close, follow the normal SESSION CLOSE PROTOCOL in `CLAUDE_CONTEXT.md` and record which tasks were completed.

---

## Background: Review Verdict (context for all tasks)

The Fable review concluded:

- **Strengths (keep, don't touch):** point-in-time fundamentals via SimFin Publish Date, conservative stop-before-target intraday ordering, entry cooldowns, transaction costs in the holistic backtest, self-flagging sanity warnings, regime gates, VIX sizing, equal-weight principle, filter-not-ranker philosophy.
- **Core concern:** the backtested edge (Config C: 238 trades, 53.78% WR, PF 1.61) is **likely overstated** for live trading because of (a) a survivorship-biased 60-ticker universe hand-picked in 2026, and (b) an out-of-sample window reused across ~20 tuning sessions (Days 55–75), which erodes its OOS validity. Honest live expectation: PF ~1.1–1.3, not 1.6.
- **Secondary concerns:** MR backtest has no transaction costs; stop fills ignore gap-downs; t-test/Sharpe/MaxDD have methodological weaknesses; the default (simple) view enforces RS ≥ 1.2 which the flagship backtest never validated; backtest fundamentals (SimFin) differ from live fundamentals (Finnhub); verdict logic is duplicated in JS and Python with only 5 parity vectors; repo hygiene issues (leaked API key, tracked venv, version drift, dead code).
- **Live-market outlook:** the system will likely *protect* capital (gates/stops/sizing are robust by construction). The *alpha* is unproven until paper trading produces 50+ logged trades under a frozen config.

---

## Phase 0 — Freeze & Pre-Register the Config (do FIRST, before anything else)

**Why first:** every backtest metric already suffers from iterative tuning. The paper-trading experiment is only valid if the configuration is written down *before* trades are logged and never touched mid-stream. Any threshold change after this point restarts the 50-trade clock.

### Task 0.1 — Create the pre-registration document
- **Status:** NOT STARTED
- **Effort:** 1–2 hours
- **Action:** Create `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` containing the EXACT frozen configuration:
  - Verdict logic version: file + git commit hash of `frontend/src/utils/categoricalAssessment.js` and `frontend/src/utils/simplifiedScoring.js`.
  - All thresholds in force: TT ≥ 7 Strong / ≥ 5 Decent, RSI bands, RS threshold **per view** (note Task 3.1 must be resolved BEFORE freezing — do Task 3.1 first if not done), ADX ≥ 20 gate, VIX bands (20/30), pattern confidence ≥ 60, R:R ≥ 1.2, stop rules (ATR primary + % caps), targets (+7/+8/+15 by period), trailing EMA rules, breakeven ratchet at +5%, VIX position multipliers (1.0/0.75/0.50), MR rules (RSI(2) < 10, >200 SMA, >$5, >500K vol, RSI(2) > 70 exit, 10d max, 5% stop), 50/50 momentum/MR capital split.
  - Success/failure criteria declared in advance: minimum 50 trades before judgment; system "confirmed" if live PF ≥ 1.2 and expectancy > 0 after costs; "broken" only if PF < 0.9 after 50+ trades (a 6-trade losing streak is EXPECTED variance, not failure).
  - Statement: "No threshold may change until 50 trades are logged. Changes restart the count."
- **Acceptance:** file exists, contains every threshold with its current value, and includes the frozen commit hash.

### Task 0.2 — Resolve the RS threshold contradiction (BLOCKER for 0.1)
- **Status:** NOT STARTED
- **Effort:** 30 min decision + 15 min code
- **Finding:** The default view (simple checklist, `frontend/src/utils/simplifiedScoring.js:99`) requires **RS ≥ 1.2**. The full view's Strong-Technical (`frontend/src/utils/categoricalAssessment.js:269`) requires **RS ≥ 1.0**, which is what Config C (PF 1.61) actually backtested. ROADMAP records both "RS 1.0 optimal / 1.2 breaks" (Tier 0D — on 5 and 3 trades, samples too small to mean anything) and "1.2 improves simplified backtest" (Day 70B). Two contradictory "validated" thresholds ship simultaneously, and the default screen is the unbacktested one.
- **Action:**
  1. Present the contradiction to the user and get a decision. **Recommendation: set the simple checklist to RS ≥ 1.0** so the default view matches the flagship backtested config. Rationale: Config C (238 trades) is the only adequately-sampled validation; the 1.2 value came from a different scoring script (`backend/backtest/backtest_simplified.py`) testing a different (unshipped-as-verdict) checklist.
  2. Apply the decision in `simplifiedScoring.js` (threshold + reason string) OR document explicitly in the pre-registration doc that the two views intentionally differ and why.
  3. Update ROADMAP.md with the resolution so the contradiction stops being cited both ways.
- **Acceptance:** one canonical RS story; simple checklist, full view, ROADMAP, and pre-registration doc all consistent.

---

## Phase 1 — Repo Hygiene (quick wins, zero strategy risk, one session)

All tasks independent. None affect trading logic.

### Task 1.1 — Remove hardcoded SimFin API key
- **Status:** NOT STARTED
- **Effort:** 30 min
- **Finding:** Live API key hardcoded at `backend/backtest/simfin_loader.py:20` (`_API_KEY = '38f0...'`), committed to git.
- **Action:**
  1. Move key to `.env` as `SIMFIN_API_KEY`; load via `os.environ.get('SIMFIN_API_KEY')` (match how `FRED_API_KEY` is loaded elsewhere in backend).
  2. Fail with a clear error message if missing.
  3. Tell the user to **rotate the key** at simfin.com (it is already in git history; removing it from HEAD does not un-leak it). Do not attempt history rewriting without explicit user approval.
- **Acceptance:** `grep -rn "38f09db0" backend/` returns nothing; backtest still loads SimFin data with the env key.

### Task 1.2 — Untrack backend/venv from git
- **Status:** NOT STARTED
- **Effort:** 20 min
- **Finding:** `backend/venv/` (thousands of site-packages files) is tracked in git — bloats the repo, produces noisy status, and pip upgrades show as modified source.
- **Action:**
  1. Add `backend/venv/` to `.gitignore`.
  2. `git rm -r --cached backend/venv` (leaves the directory on disk).
  3. Commit. Warn: the commit will be large (deletions only).
- **Acceptance:** `git status` shows no `backend/venv/` entries; backend still starts via `./start.sh`.

### Task 1.3 — Fix backend version string drift
- **Status:** NOT STARTED
- **Effort:** 10 min
- **Finding:** `backend/backend.py:579` reports `'version': '2.23'`; docs say Backend v2.35.
- **Action:** Update the string to the current documented backend version. Better: define `BACKEND_VERSION` once near the top of `backend.py` and reference it, then add a line to the SESSION CLOSE PROTOCOL notes that version bumps must touch this constant.
- **Acceptance:** `curl localhost:5001/api/health` reports the same version as CLAUDE_CONTEXT.md.

### Task 1.4 — Delete dead frontend code
- **Status:** NOT STARTED
- **Effort:** 30 min
- **Finding:** `frontend/src/components/DecisionMatrix.jsx` unwired since Day 70 (`App.jsx:48` comment confirms removal); `frontend/src/utils/scoringEngine_day4.js` and `scoringEngine_v2.1.js` are legacy versions.
- **Action:** For each file: `grep -rn "<name>" frontend/src/` to confirm zero imports, then delete. If any import exists, STOP and report instead of deleting.
- **Acceptance:** frontend builds and runs (`./start.sh`, load Analyze page for one ticker).

---

## Phase 2 — Backtest Integrity Fixes (the measurement must be honest before re-validation)

Do these BEFORE Phase 4, so the re-validation run uses the corrected simulator. These change *measurement*, not strategy.

### Task 2.1 — Add transaction costs to the MR backtest
- **Status:** NOT STARTED
- **Effort:** 1–2 hours
- **Finding:** `backend/backtest/mr_simulator.py` and `backend/backtest/gate5_combined.py` apply **zero** transaction costs (verified: no cost/slippage references in either file), while the momentum backtest uses `apply_transaction_costs()` from `metrics.py`. Gate 4's PF 1.26 on 4.1-day holds is gross; the edge may be materially thinner net.
- **Action:**
  1. In `mr_simulator.py`, after each trade result, apply `apply_transaction_costs(entry_price, exit_price)` (import from `backtest.metrics`) and store `pnl_pct_net`; use net in all aggregate stats.
  2. Same in `gate5_combined.py` for the MR leg (momentum leg: verify whether it already nets costs; make both legs consistent).
  3. Re-run the MR standalone backtest and Gate 5. Record new net numbers.
- **Acceptance:** re-run outputs show net-of-cost PF/WR for MR. **Report the delta honestly** — if net PF drops below ~1.10, flag to the user that the 50/50 capital split decision should be revisited (do not change the split yourself; that's a user decision under the freeze).

### Task 2.2 — Gap-aware stop fills in both simulators
- **Status:** NOT STARTED
- **Effort:** 2–3 hours
- **Finding:** Both `trade_simulator.py` (`low_day <= stop_price → exit at stop_price`) and `mr_simulator.py` (same pattern) fill stops at the exact stop price. Real gap-downs fill at the open, below the stop. This optimism is worst for MR (buying 2-period-oversold stocks — the population most prone to gap-downs).
- **Action:** In both simulators, before the intraday stop check, add a gap check:
  ```python
  open_day = stock_df['Open'].iloc[check_idx]
  if open_day <= stop_price:
      exit_price = open_day   # gapped through the stop — fill at open
  elif low_day <= stop_price:
      exit_price = stop_price # normal intraday stop
  ```
  Apply the same logic to gap-up target fills (fill at open when `open >= target` — this is favorable and keeps the model symmetric/honest).
- **Acceptance:** self-tests in both files still pass; re-run `--quick-test`; document the metric deltas vs. previous run in the results JSON/HTML. Expect WR/PF to drop slightly — that is the point.

### Task 2.3 — Fix statistical methodology in metrics.py
- **Status:** NOT STARTED
- **Effort:** 2–3 hours
- **Findings:**
  a. `_compute_t_test` assumes i.i.d. trades; trades cluster by regime and by correlated tickers, so p=0.002 is overstated.
  b. `_t_distribution_pvalue` uses a hand-rolled erf approximation with a "crude correction" — scipy is already a transitive dependency of the stack.
  c. `_compute_sharpe`/`_compute_sortino` hardcode `trades_per_year = 25` regardless of actual frequency.
  d. `_compute_max_drawdown` compounds pooled trades sequentially at 100% equity each — the reported 52.6% is a modeling artifact (neither portfolio DD nor per-trade DD).
- **Action:**
  1. Replace the p-value approximation with `scipy.stats.ttest_1samp` (fall back to current approximation only if scipy import fails).
  2. Compute `trades_per_year` from actual data: `n_trades / (span_years from first entry_date to last exit_date)`.
  3. Add a **block bootstrap** p-value alongside the t-test: resample trades in monthly blocks (group by entry month), 10,000 resamples, report the fraction of resampled means ≤ 0. Label the existing t-test output `t_pvalue_iid_assumption` so nobody mistakes it for the robust number.
  4. Relabel max drawdown as `sequential_100pct_equity_dd` and ADD a second, honest metric: DD of an equity curve where each trade risks a fixed 1R = 2% of equity (uses `return_r` × 2% per trade, compounded in entry-date order). Report both.
- **Acceptance:** `python backend/backtest/metrics.py` self-test passes; a Config C re-run reports both p-values and both DD figures; docs updated wherever "p=0.002" or "max DD 52.6%" are cited (STATUS, ROADMAP, README if present).

### Task 2.4 — Strengthen JS↔Python verdict parity testing
- **Status:** NOT STARTED
- **Effort:** 2–3 hours
- **Finding:** Verdict logic exists twice — `categoricalAssessment.js` (live truth, 900+ lines) and `categorical_engine.py` (the version that was backtested). Parity is held by only 5 hand-written vectors in `_verify_parity()`. Five vectors cannot cover a 9-rule verdict tree × 3 holding periods.
- **Action:**
  1. Write `backend/backtest/test_verdict_parity.py`: grid-generate inputs — TT ∈ {3,5,6,7,8}, RSI ∈ {25,45,55,65,75,85}, RS ∈ {0.7,0.95,1.0,1.05,1.2}, ADX ∈ {15,22,28}, VIX ∈ {15,25,35,None}, spy_above ∈ {T,F}, spy_declining ∈ {T,F}, fundamentals ∈ {strong-set, decent-set, weak-set, all-None}, holding_period ∈ {quick,standard,position} (~thousands of combos; cheap, pure functions).
  2. Run the same grid through the JS side via a small Node script that imports `categoricalAssessment.js` functions and prints verdicts as JSON (`node frontend/scripts/verdict_grid.mjs > /tmp/js_verdicts.json` style; put the script in `frontend/scripts/`).
  3. Compare. Every mismatch is a real bug in one of the two implementations — report all mismatches to the user with the differing rule before fixing anything.
- **Acceptance:** grid comparison runs clean OR every mismatch is documented with root cause and user-approved fix. Add the parity script to the pre-close checklist for any session that touches verdict logic.

---

## Phase 3 — Backtest↔Live Coherence (make the tested thing and the shipped thing the same thing)

### Task 3.1 — (moved to Phase 0 as Task 0.2 — RS threshold. Do not do twice.)

### Task 3.2 — Document and measure the fundamentals data-source mismatch
- **Status:** NOT STARTED
- **Effort:** 2 hours
- **Finding:** Backtest ROE = SimFin quarterly net income ×4 / equity (`simfin_loader.py:98`); live ROE = Finnhub TTM. YoY growth computed by different code from different sources. The same stock can be Fundamental-Strong in the backtest and Decent live → live Config C ≠ backtested Config C.
- **Action:**
  1. Write a one-off diagnostic script `backend/backtest/diag_fundamentals_mismatch.py`: for ~20 liquid tickers, fetch live Finnhub fundamentals AND SimFin-derived fundamentals for the latest available common quarter; run `assess_fundamental()` on both; report how often the categorical label (Strong/Decent/Weak) differs.
  2. If label disagreement > ~20%, flag to the user — the mitigation options (align the live computation to annualized-quarterly, or re-run the backtest with TTM-style fundamentals) are a user decision.
  3. Record the measured disagreement rate in KNOWN_ISSUES as a permanent Info entry either way.
- **Acceptance:** disagreement rate measured and documented; no silent assumption remains.

### Task 3.3 — Fix silent RS fallback in live assessment
- **Status:** NOT STARTED
- **Effort:** 15 min
- **Finding:** `categoricalAssessment.js:262` — `const rs52Week = technicalData?.rsData?.rs52Week || 1.0;` silently substitutes neutral 1.0 when RS is missing (also converts an impossible-but-defensive 0 to 1.0). Violates the project's own rule: "Return null, not a plausible fake" / "silent fallbacks are invisible lies" (Day 54).
- **Action:** When rs52Week is null/undefined, do not fabricate 1.0 — either exclude RS from the Strong check and append a visible reason ("RS unavailable — Strong rating requires RS data"), or cap Technical at Decent when RS is missing. Match whichever treatment the backtest used (`backtest_holistic.py:248` also defaults to 1.0 — if you change one side, change both and note it in the parity test of Task 2.4).
- **Acceptance:** missing RS produces a visible reason in the UI, not a silent neutral; JS and Python treat missing RS identically.

---

## Phase 4 — Survivorship-Free Re-Validation (the big one; 1–2 dedicated sessions)

### Task 4.1 — Rebuild the backtest universe without hindsight
- **Status:** NOT STARTED
- **Effort:** 1–2 sessions
- **Finding:** The 60-ticker universe (`backtest_holistic.py:55-80`) was hand-picked in 2026 and is dominated by 2020–2025 mega-winners (NVDA, LLY, AVGO, PLTR, CRWD, COIN...). A momentum-BUY filter tested on hindsight-selected momentum winners looks good almost by construction. This is the single biggest threat to PF 1.61 being real.
- **Action:**
  1. Build the universe from **SimFin's own coverage** (already local, free, point-in-time): all US tickers in the SimFin dataset (`get_available_tickers()`), filtered per-date only by criteria knowable at the time: price > $5 and 20d average dollar volume > $5M **as of each entry date** (compute from the OHLCV already being downloaded). Include tickers that later died or faded — SimFin's dataset includes delisted names; yfinance may lack OHLCV for some delisted tickers — log the count skipped for missing prices and report it as residual survivorship (it will not be zero; the goal is *much less* bias, honestly measured, not perfection).
  2. If the full universe is too slow, use a random sample of 300–500 qualifying tickers, seeded (`random.seed(42)`) for reproducibility — random selection is the point; no hand-picking.
  3. Run Config C, standard period, WITH the Phase 2 fixes (gap fills, corrected stats). Also run the MR strategy on the same universe.
  4. Use `--scan-interval 2` or 3 if runtime demands; note it in results.
- **Acceptance:** results JSON/HTML produced for the unbiased universe; skipped-ticker count reported.

### Task 4.2 — Interpret and document the re-validation honestly
- **Status:** NOT STARTED
- **Effort:** half session (with 4.1)
- **Action:** Create `docs/claude/versioned/SURVIVORSHIP_FREE_BACKTEST_DAY[N].md` comparing original vs unbiased-universe results. Interpretation guide (pre-committed so the conclusion isn't fitted to the result):
  - Net PF ≥ 1.3 with p (block bootstrap) < 0.05 → edge substantially confirmed; proceed with paper trading as planned.
  - Net PF 1.1–1.3 → edge real but modest; paper trade with expectations reset (this is still a tradeable system with 2% risk sizing).
  - Net PF < 1.1 → the filter still has defensive value, but the alpha claim is unsupported; discuss with user before allocating capital. **Do not** re-tune thresholds to fix the number — that is precisely the data-snooping failure mode this plan exists to end.
- **Acceptance:** comparison doc exists; STATUS/ROADMAP headline metrics updated to cite the unbiased numbers as canonical; old numbers kept but labeled "hindsight-universe."

---

## Phase 5 — Paper-Trading Instrumentation (measure the execution gap)

### Task 5.1 — Log signal-vs-fill slippage in the Forward Test tab
- **Status:** NOT STARTED
- **Effort:** 1–2 hours
- **Finding:** Backtest enters at the signal bar's close; a human enters manually later, possibly at a dual-entry price never modeled. For single-digit-% average winners, ~0.5% entry slippage per trade meaningfully erodes PF. No backtest can measure this — only live logging can.
- **Action:** In `frontend/src/utils/forwardTesting.js` + the Forward Test tab: when a trade is added, also record `signal_close_price` (the close price shown at analysis time) alongside the actual `entry` the user got. Add a computed `entry_slippage_pct` column and show its running average in the Van Tharp stats block. Same for exits vs. the rule-implied exit price if feasible (optional).
- **Acceptance:** new trades store both prices; stats block shows average entry slippage; CSV export includes it.

### Task 5.2 — Add regime tag to every paper trade
- **Status:** NOT STARTED
- **Effort:** 1 hour
- **Why:** 2020–2025 was one long bull + one orderly bear. Live results must be attributable by regime to know whether deviation from backtest is regime-driven or system-driven.
- **Action:** When a paper trade is logged, snapshot: VIX value, SPY vs 200 SMA, 50 SMA declining flag, and the resulting regime label (reuse existing categorical logic — do not reimplement). Store on the trade record; include in CSV export.
- **Acceptance:** every new paper trade carries a regime snapshot.

---

## Explicitly OUT of Scope (do not do these)

- **No threshold re-tuning** of any strategy parameter (RS decision in Task 0.2 is a one-time coherence fix, then frozen).
- **No new features** (Value Tab Phase 2, N4, /ibkr-scan, Price Structure Phase 2 all wait — feature freeze stands; this plan takes precedence as validation/bug work).
- **No git history rewriting** for the leaked key without explicit user approval — rotation at the provider is the real fix.
- **No changing the 50/50 momentum/MR split, exits, or sizing rules** based on re-run numbers — report findings; splits/rules are user decisions.

---

## Suggested Session Sequencing

| Session | Tasks | Outcome |
|---------|-------|---------|
| 1 | 0.2 (RS decision) → 0.1 (pre-registration) → Phase 1 (all hygiene) | Config frozen, repo clean |
| 2 | 2.1, 2.2 (MR costs + gap fills), re-run MR + Gate 5 | Honest MR/Gate numbers |
| 3 | 2.3 (stats), 2.4 (parity grid) | Honest stats, verdict parity proven |
| 4 | 3.2, 3.3 (data mismatch diag, RS fallback) | Backtest↔live coherence measured |
| 5–6 | 4.1, 4.2 (survivorship-free re-validation) | Canonical unbiased metrics |
| 7 | 5.1, 5.2 (paper-trade instrumentation) | Execution gap measurable |

Paper trading can and should **start immediately after Session 1** (freeze + pre-registration). Phases 2–5 improve measurement in parallel; they do not block logging trades.

---

## Progress Log

| Day | Tasks Completed | Notes |
|-----|-----------------|-------|
| — | — | Plan created Day 78, nothing executed yet |
