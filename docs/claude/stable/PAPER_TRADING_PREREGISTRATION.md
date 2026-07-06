# Paper Trading Pre-Registration

> **Purpose:** Freeze the exact configuration BEFORE paper trades are logged, so the forward-test result is a real out-of-sample test and not another round of in-sample tuning.
> **Created:** Day 78 (July 5, 2026) — Fable Review Remediation Plan, Task 0.1
> **Frozen commit:** `933ad297ed14ca3c2aad2fb16ca453890d7c43fa` (includes Task 0.2's RS 1.0/1.2 resolution)
> **Rule (Golden Rule 18):** No threshold below may change until 50 trades are logged in the Forward Test tab. Any change resets the count to zero and requires a new pre-registration entry.

---

## 1. Verdict Logic — Frozen Files

| File | Role | Commit at freeze |
|------|------|-------------------|
| `frontend/src/utils/categoricalAssessment.js` | Live verdict engine (full view) | `933ad297` |
| `frontend/src/utils/simplifiedScoring.js` | Live 9-criteria checklist (default/simple view) | `933ad297` (RS aligned to 1.0 this session) |
| `backend/backtest/categorical_engine.py` | Backtested verdict engine (Python port) | `933ad297` |

## 2. Technical Assessment Thresholds

| Rule | Value | Source |
|------|-------|--------|
| Strong: Trend Template | ≥ 7/8 criteria | `categoricalAssessment.js` |
| Strong: RSI band | 50–70 | `categoricalAssessment.js` |
| Strong: RS (52-week vs SPY) | ≥ 1.0 | `categoricalAssessment.js`, `simplifiedScoring.js` (resolved Day 78 — was 1.2 in simple view) |
| Decent: Trend Template | ≥ 5/8 criteria | `categoricalAssessment.js` |
| Decent: RSI band | 40–80 | `categoricalAssessment.js` |
| Weak: RS | < 0.8 | `categoricalAssessment.js` |
| ADX gate — momentum entry | ≥ 25 | verdict + entry preference logic |
| ADX gate — pullback entry | 20–25 | verdict + entry preference logic |
| ADX gate — no-trend caution | < 20 (HOLD if 2+ strong) | `determine_verdict()` |

## 3. Fundamental Assessment Thresholds

| Rule | Value |
|------|-------|
| ROE Strong | > 15% |
| ROE Decent | 8–15% |
| ROE Weak | < 8% |
| Revenue Growth Strong | > 10% |
| Revenue Growth Decent | 0–10% |
| Revenue Growth Weak | < 0% |
| D/E Strong | < 1.0 |
| D/E Decent | 1.0–2.0 |
| D/E Weak | > 2.0 |
| Overall Strong | ≥ 2 strong metrics, 0 weak |
| Overall Weak | ≥ 2 weak metrics |

## 4. Risk/Macro Gate

| Rule | Value |
|------|-------|
| Favorable | VIX < 20 AND SPY > 200 SMA AND 50 SMA not declining |
| Neutral | VIX 20–30, or SPY 50 SMA declining while still > 200 SMA |
| Unfavorable | VIX > 30 OR SPY < 200 SMA → caps verdict at HOLD |

## 5. Verdict Priority Order (unchanged, `determine_verdict()`)

1. Weak Technical → AVOID (non-negotiable)
2. Unfavorable Risk → HOLD (structure override)
3. Weak Fundamental + position holding period → AVOID
4. ADX < 20 with 2+ strong → HOLD
5. Strong Tech + Strong Fund → BUY
6. 2+ Strong with Favorable/Neutral risk → BUY
7. Quick period: Strong Tech + Weak Fund + Favorable/Neutral → BUY (tech 70% weight)
8. Strong Tech + Decent Fund + Favorable (or quick+Neutral) → BUY
9. Position period: Decent Tech + Strong Fund + Favorable/Neutral → BUY (fund 70% weight)
10. 1+ Strong → HOLD
11. Decent Tech + Favorable → HOLD
12. Default → AVOID

Signal weights by holding period: Quick 70/30 (tech/fund), Standard 50/50, Position 30/70.

## 6. Pattern / Entry Thresholds

| Rule | Value |
|------|-------|
| Actionable pattern confidence | ≥ 60% |
| Actionable pattern status | `at_pivot`, `broken_out`, `complete`, or `forming` |
| Breakout volume confirmation | ≥ 1.5x 50-day average volume |
| Breakout follow-through | Price holds above pivot within 3 days |
| R:R minimum (Config C definition) | ≥ 1.2 |

## 7. Stops, Targets, Exits (by holding period)

| Holding Period | Max Hold | Target | Stop | Trailing / Ratchet |
|----------------|----------|--------|------|---------------------|
| Quick | 5 days | +7% | max(5% fixed, entry − 2×ATR) | none |
| Standard | 15 days | +8% | swing_low − 2×ATR, clamped 3–10% | 10 EMA trail (day 5+, gain ≥3%); breakeven ratchet at gain ≥5% |
| Position | 45 days | +15% | swing_low − 2×ATR, clamped 3–12% | 21 EMA trail (day 5+) |

## 8. Position Sizing — VIX Multiplier (Moreira & Muir 2017)

| VIX | Multiplier |
|-----|------------|
| < 20 | 1.0 (full size) |
| 20–30 | 0.75 |
| > 30 | 0.50 |

Max 2% risk per trade (Van Tharp). Equal-weight categories — never optimize weights (Golden Rule 16).

## 9. Mean-Reversion Arm (isolated system, RSI(2))

| Rule | Value |
|------|-------|
| Entry | RSI(2) < 10 AND price > 200 SMA AND price > $5 AND avg volume > 500K |
| Exit | RSI(2) > 70 OR 10 trading days max |
| Stop | max(entry × 0.95, entry − 1.5×ATR) |
| Capital allocation | 50/50 split with momentum system (Gate 5, 1.9% overlap, 0.274 P&L correlation) — ⚠️ gross-of-costs at freeze time; see Section 11 |

## 10. Success / Failure Criteria (declared in advance)

Judgment happens only after **≥ 50 logged trades** in the Forward Test tab. Before that point, any result — including a losing streak — is within expected variance and is NOT evidence the system is broken.

| Outcome | Threshold | Interpretation |
|---------|-----------|----------------|
| **Confirmed** | Live profit factor ≥ 1.2 AND positive expectancy after transaction costs, on ≥ 50 trades | System has a real, tradeable edge — continue as-is |
| **Modest but real** | PF 1.05–1.2 | Edge exists but thinner than backtest suggested (expected, per Fable review — survivorship bias + reused OOS) — continue with realistic expectations, do not abandon |
| **Broken** | PF < 0.9 after ≥ 50 trades, or expectancy consistently negative | Stop live trading, return to remediation Phase 4 (survivorship-free re-validation) before any further capital deployment |

A 6-trade losing streak alone is **not** sufficient evidence of failure at any point — it is statistically consistent with a PF-1.6 system (per the review's own variance analysis).

## 11. Known Caveats At Freeze Time (Day 78)

These are **not** reasons to delay freezing — they are reasons the "Confirmed" bar above is set at PF ≥ 1.2 rather than the backtested 1.61:

- Backtest universe (60 tickers) is survivorship-biased (hand-picked in 2026); true live PF is expected lower than the backtested 1.61.
- The same walk-forward OOS window was reused across ~20 tuning sessions (Days 55–75) — its "OOS outperforms IS" result no longer certifies robustness on its own.
- MR engine backtest (Gate 4, Gate 5) has **zero transaction costs modeled** — net PF may be materially below the reported 1.26.
- Stop fills in both backtest simulators ignore gap-downs — live slippage on stops will likely be worse than backtested.
- Backtest fundamentals (SimFin quarterly ×4) differ from live fundamentals (Finnhub TTM) — the live Fundamental label for a given stock may not match what the backtest scored.

Remediation Phases 2–5 address these in parallel; they do not need to complete before paper trading starts, but their outputs should be read alongside live results as they land.

---

## Change Log

| Day | Change | Reason |
|-----|--------|--------|
| 78 | Initial freeze | Fable Review Remediation Plan Task 0.1 |
