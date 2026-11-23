# Plan: fix the two engine bugs; the MR route needs a doc correction, not code

## Context
Goal: make the first Analyze tab trustworthy. Two Medium engine bugs are open (Day 123), plus an "MR route reads Yahoo directly" note.

**Correction found while planning (measured):** the MR route is NOT bypassing the provider chain. `backend.py:3851-3910` (`/api/mr/signal`) and `:3913-3970` (`/api/mr/scan`) call `get_data_provider().get_ohlcv()` first (Alpaca -> Twelve Data -> Yahoo -> Tradier). Live check: `curl /api/mr/signal/AAPL` returned `"dataSource": "DataProvider"`. Direct Yahoo is used only if the whole chain fails, and the answer then says `dataSource: "yfinance fallback"` (and prints a warning). The Known Issues line (Day 128-130) is stale, and I repeated it earlier in this session. **No MR code change.** Only fix the note.

## Bug 1: missing RSI counts as 50 (and a real RSI of 0 becomes 50)
Where: `frontend/src/utils/categoricalAssessment.js:92` (`rsi || ... || 50`), `:766` (same), `:774` (`rsiAvailable`); Python copy `backend/backtest/categorical_engine.py:68` (`rsi if rsi is not None else 50`). Both copies must change together (Golden Rule 59).

Rule (decision): a missing RSI may never help. Missing RSI -> cannot be Strong; can be Decent if the trend checks are 5+ (same precedent as missing RS, Day 78); otherwise Weak. Reason text says "RSI unavailable". Real RSI values (including 0) are used as they are.
- JS: pick the first finite value of the passed RSI, `technicalData.indicators.rsi`; else `null`. `data.rsi = null`; `rsiAvailable` comes from the same value (one source). Branch on missing RSI FIRST, before any comparison (JS `null < 30` is true; Python `None < 30` raises), then guard every `rsiValue.toFixed`.
- Python: `None` or non-finite -> missing, same branches.
- Consumers that cope with null: `deriveTechnicalRead` (:860), `deriveStrongCriteria` (:905-909), `TechnicalRead.jsx:50,67`, `App.jsx:2001`, `forwardTesting.js:387`.
- **Must change:** `TechnicalRead.jsx:77` ("engine assumed ${rsi}, which counts as a pass") and `:281` ("RSI missing, engine assumed 50") become "RSI unavailable, so no Strong"; stale comments at `categoricalAssessment.js:441-443`, `:770-773`, `:883-884` are rewritten.
- Third copy, OUT OF SCOPE (decision at build): `parameter_stability.py:172,181` is a research script with its own overridden thresholds; its `50` only covers an out-of-range index (its RSI series is always defined). Named here, not changed.
- A missing RSI can still reach BUY (Decent technical + Strong fundamentals, position mode, `:706`); that is accepted and written here.

## Bug 2: missing SPY is described as "below its 200-day" (decision, user: stay cautious, say it honestly)
Where: JS `categoricalAssessment.js:432` (`spyData?.aboveSma200 || false`), branches `:449-483`; Python `categorical_engine.py:196-255`.

Rule: the RESULT does not change. SPY unknown -> Unfavorable, exactly as today (so no verdict moves anywhere, no BUY is allowed while the market trend is unknown). The TEXT changes: reason says "SPY trend unavailable, treated cautiously (no BUY)" instead of the false "SPY below 200 SMA (Bear regime)" and "most pullback setups fail in bear markets". If VIX > 30 the VIX reason is still shown.
- `data.spyAbove200EMA` = `null` when unknown; `data.spyAvailable` is derived from the same value (it has no consumer today). App.jsx:2001 and forwardTesting.js:387 already handle null.
- Python: test `is None` only (never `is True/False`; `is_spy_above_200sma` returns a numpy bool).
- Out of scope, named: `trade_simulator.py:121`, `backtest_holistic.py:299`, `nirmal_validation.py:366` turn missing SPY into "above" (assume bull), the opposite rule, backtest-only. `scoringEngine.js:393` spyRegime score.

## Parity and proof (Golden Rules 19, 59, hook `verdict_parity.sh`)
1. Before editing: run `backtest/test_verdict_parity.py` and save the JS and Python outputs for the existing 86,400 rows (golden).
2. Extend the grid: `RSI_VALUES` + `0` and `None`, `SPY_ABOVE_VALUES` + `None` (86,400 -> 172,800 rows). `verdict_grid.mjs` passes null through. NaN stays out of the grid (Python writes `NaN` into JSON and Node rejects it); NaN is covered in unit tests only.
3. After editing: parity must show 0 mismatches on all 151,200 rows, and the original 86,400 rows must match the saved golden BY INPUT (not row number; the nested grid reorders) on `technical`, `risk_macro` and `verdict`. SPY-None rows must give the same `risk_macro`/`verdict` as the matching SPY-False rows.
4. Mutation check: switch each fix off; the new None rows must fail.
5. Unit tests for both functions (RSI None, RSI 0, RSI NaN; SPY None with VIX 15 / 25 / 35 / None).
6. Backtest safety: the backtest always supplies RSI and SPY, so Config C should be unchanged. Check: re-run it before and after on the same day (not against the documented PF, SimFin drift, Golden Rule 45); trade count and PF must be identical. `backtest_holistic.py:279` already drops None/NaN RSI before the engine, and missing SPY never reaches it (`:299` assumes bull), so Config C cannot change; the re-run is a cheap confirmation.
7. Real page: `node scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN` (use `headless: 'shell'` if it hangs); then view a ticker with a forced-missing RSI/SPY in a unit-level render check.

## Other callers (Golden Rule 54)
`paper_trading/live_signals.py:279` (discontinued program), `backtest_holistic.py:332`, `nirmal_validation.py:390`, `parameter_stability.py:198`: `live_signals.py:281` can pass `rsi=None` (program discontinued, no impact); the others pass real values. `parameter_stability.py` also has the inline RSI copy (see above).

## Docs
Known Issues Day 131: close both Medium items; replace the stale MR-route line with the correct finding; ROADMAP/CLAUDE_CONTEXT status; new row in `ENGINEER.md` missed table ("repeated a Known Issues line without reading the code").

## Process
Plan file copy in `docs/claude/design/ENGINE_MISSING_INPUTS_PLAN_DAY131.md` -> Opus review (apply changes, tell the user) -> build -> `/three-pass` -> `three_pass_check.sh --stamp ... --plan <file>`.

## Out of scope (stays open)
`fearGreed || 50` in `assessSentiment` (informational, gates nothing); other `|| 50` at lines 92/766 are the ones covered here; Python NaN in other engines.

## Opus review (Day 131)
**Verdict: GO WITH CHANGES.** MR-route claim confirmed (`backend.py:3866-3875`, `:3940-3948`). Grid arithmetic confirmed. Applied above: (1) false "engine assumed" text in TechnicalRead.jsx:77/:281 and stale comments; (2) missing-RSI branch before comparisons; (3) third RSI copy in parameter_stability.py; (4) live_signals can pass None; (5) backtest NaN already proven by backtest_holistic.py:279, opposite-meaning SPY copies named out of scope; (6) golden matched by input on three fields; (7) RSI 0 added, NaN unit-test only; (8) `is None` only in Python; (9) SPY rule: Opus warned that "Neutral" would loosen verdicts; user chose to stay cautious (Unfavorable), text only; (10) missing RSI can still reach BUY, written down; (11) `spyAvailable` has no consumer, derived from the same value.
