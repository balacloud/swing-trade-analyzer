# Verdict Parity Grid Test — Findings (Day 78)

> **Source:** Fable Review Remediation Plan, Task 2.4.
> **Script:** `backend/backtest/test_verdict_parity.py` + `frontend/scripts/verdict_grid.mjs`
> **Run date:** Day 78, session 4 (July 6, 2026)
> **Status:** Test built and run. **One confirmed bug found, reported to user, fix approved and applied.** Full grid re-run afterward: **all 86,400 combinations now match — JS and Python are in full parity.**

---

## What was tested

`categorical_engine.py` (the Python port used in the historical backtest, including Config C's PF 1.61 result) exists in parallel with `categoricalAssessment.js` (the live JS verdict logic that actually ships to users). Parity between them was previously held by only 5 hand-written test vectors — nowhere near enough to cover a 9-rule verdict tree across 3 holding periods.

This test generates a full Cartesian grid — TT ∈ {3,5,6,7,8} × RSI ∈ {25,45,55,65,75,85} × RS ∈ {0.7,0.95,1.0,1.05,1.2} × ADX ∈ {15,22,28} × VIX ∈ {15,25,35,None} × SPY-above ∈ {T,F} × SPY-declining ∈ {T,F} × fundamentals ∈ {strong,decent,weak,all-None} × holding-period ∈ {quick,standard,position} — **86,400 combinations total**. Each combo runs through both implementations' `assessTechnical`/`assess_technical`, `assessFundamental`/`assess_fundamental`, `assessRiskMacro`/`assess_risk_macro`, and `determineVerdict`/`determine_verdict`, and the four outputs are compared.

## Results

| Field | Mismatches | Rate |
|-------|-----------|------|
| technical | 0 | 0% |
| fundamental | 0 | 0% |
| risk_macro | 0 | 0% |
| **verdict** | **6,120** | **7.08%** |

All three category-assessment functions are in perfect parity. The mismatch is isolated entirely to the final verdict decision logic.

## Root cause (single, confirmed)

Every one of the 6,120 mismatches reduces to exactly **one** pattern (verified: only 2 distinct `(technical, fundamental, risk_macro, python_verdict, js_verdict)` tuples across all 6,120 rows, differing only in which non-Strong fundamental value was used):

| technical | fundamental | risk_macro | Python verdict | JS verdict |
|-----------|-------------|------------|-----------------|------------|
| Decent | Decent | Neutral | AVOID | HOLD |
| Decent | Unknown | Neutral | AVOID | HOLD |

**The bug:** in the final HOLD-fallback rule, before defaulting to AVOID:

- **`categorical_engine.py`** (Python, backtested):
  ```python
  if technical == 'Decent' and risk_macro == 'Favorable':
      return result('HOLD', 'Decent setup — consider with proper sizing')
  # Default: AVOID
  return result('AVOID', 'Insufficient strength across categories')
  ```
  Only checks `risk_macro == 'Favorable'`.

- **`categoricalAssessment.js`** (JS, live/shipped):
  ```js
  if (technical === 'Decent' && (riskMacro === 'Favorable' || riskMacro === 'Neutral')) {
    return buildResult('HOLD', 'Decent setup - wait for a strong catalyst or breakout', 'yellow');
  }
  ```
  Checks `riskMacro === 'Favorable' OR 'Neutral'`.

The Python port is missing the `'Neutral'` branch that production actually has. Whenever technical is Decent, no category is Strong, and risk/macro is Neutral (not Favorable, not Unfavorable), **live JS returns HOLD** but **the backtested Python returns AVOID**.

## Impact assessment

**Does NOT affect Config C's headline metrics (PF 1.61, 238 trades).** Both AVOID and HOLD are no-entry outcomes — the backtest never opens a trade in either case. This bug only mislabels *why* no trade was taken in the Python port; it does not change which historical trades were counted, so the walk-forward validation and all reported win rate / profit factor / Sharpe figures are unaffected by this specific bug.

**Does matter for correctness and any future extension.** If the system is ever extended to treat HOLD and AVOID differently (e.g., different UI treatment, different position-sizing behavior, or a future backtest that tracks "watched but not entered" candidates), this divergence would silently produce different behavior between what was tested and what ships.

**Validates the exercise itself.** The 5 hand-picked parity vectors in `categorical_engine.py`'s `_verify_parity()` completely missed this — none of them happened to land on (Decent, non-Strong, Neutral). A systematic grid caught it immediately. This is exactly the argument for keeping `test_verdict_parity.py` as a standing check.

## Fix — applied and verified

User approved the fix. Applied to `categorical_engine.py`'s `determine_verdict()`:

```python
# Day 78 (Fable Remediation Task 2.4): was 'Favorable' only — missing the
# 'Neutral' branch that categoricalAssessment.js has.
if technical == 'Decent' and risk_macro in ('Favorable', 'Neutral'):
    return result('HOLD', 'Decent setup — consider with proper sizing')
```

**Backtest-code-only change** — does not touch the frozen live verdict logic (`categoricalAssessment.js`) or any paper-trading config.

**Verification:**
1. `categorical_engine.py`'s own 5-vector `_verify_parity()` self-test: still all PASS.
2. Full 86,400-combo grid re-run: **0 mismatches** (was 6,120). JS and Python now fully agree on every category assessment and every verdict across the entire tested space.

As predicted, this had **zero effect on Config C's historical PF/trade-count** (AVOID and HOLD are both no-entry outcomes) — confirmed by the fact that no re-validation of Config C's headline numbers was needed to apply this fix; it only affects future backtest re-runs' internal labeling.

## Artifacts

The raw grid inputs/outputs and full mismatch list (86,400 / 6,120 rows respectively) are NOT committed — they're large (~34MB combined) and fully regenerable via:
```bash
python backend/backtest/test_verdict_parity.py
```
(Also invokes `frontend/scripts/verdict_grid.mjs` via Node automatically.) Gitignored per `.gitignore` Day 78 entry.

## Recommendation for ongoing use

Add `test_verdict_parity.py` to the pre-close checklist for any session that touches `categoricalAssessment.js` or `categorical_engine.py` — per the remediation plan's own acceptance criteria.
