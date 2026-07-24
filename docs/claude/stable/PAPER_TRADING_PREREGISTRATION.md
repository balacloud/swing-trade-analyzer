# Paper Trading Pre-Registration

> **Purpose:** Freeze the exact configuration BEFORE paper trades are logged, so the forward-test result is a real out-of-sample test and not another round of in-sample tuning.
> **Created:** Day 78 (July 5, 2026) — Fable Review Remediation Plan, Task 0.1
> **Frozen commit:** `933ad297ed14ca3c2aad2fb16ca453890d7c43fa` (includes Task 0.2's RS 1.0/1.2 resolution)
> **Rule (Golden Rule 18):** No threshold below may change until 100 trades are logged in the Forward Test tab (raised from 50, Day 92 — see Change Log). Any change resets the count to zero and requires a new pre-registration entry.

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

## 8b. Path B — Parallel Momentum Entry-Gate Experiment (Day 95)

**Not a change to the frozen Sections 1-8 above.** Path A (the config described in this whole document) continues completely unchanged, accumulating toward its own 100-trade bar exactly as before. Path B is a new, separately pre-registered, honestly-tracked experiment running *alongside* it — same candidate pool, same day, same regime, isolating exactly one variable.

**What prompted it:** a Day 95 live investigation found that `paper_trading/live_signals.py`'s momentum R:R check (flat +8% target, ATR-clamped stop, `compute_entry_levels()`) is **not** the same logic `backtest_holistic.py`'s actual Config C entry gate used to validate momentum's PF 1.40-1.61 — that gate computes R:R from real support/resistance levels (`risk = price - nearest_support`, `reward = nearest_resistance - price`), falling back to a flat 1.5 estimate only when no S&R levels exist. The live engine has been using the wrong piece of logic as its entry decision since Day 81 (the real S&R math was only ever the exit-management formula in the backtest, never the entry gate) — the same bug *class* as Golden Rule 19's JS/Python parity finding, just live-vs-backtest instead of JS-vs-Python.

| Rule | Path A (unchanged) | Path B (new) |
|------|---------------------|--------------|
| Trend Template / RS / fundamentals / verdict | Shared — identical computation for both | Shared — identical computation for both |
| Entry gate | `compute_entry_levels()` flat+8%/ATR-clamped-stop proxy, R:R≥1.2 (Day 81 substitute, unchanged) | Real S&R-based gate (`check_sr_gate()` in `live_signals.py`) — replicates `backtest_holistic.py`'s actual Config C gate exactly: `is_viable AND rr_ratio>=1.2` from real support/resistance, 1.5 ATR-fallback if no S&R levels |
| Exit management once entered | `compute_entry_levels()` (unchanged) | **Identical** — same function, same formula. Path B only differs in what decided the trade was worth taking, not how it's managed afterward |
| Ledger tag | `variant='A_frozen'` | `variant='B_revised_rr'` |
| Confirmation bar | 100 trades (unchanged, Section 10) | 100 trades, tracked independently |
| Cooldown/active-position tracking | Independent per variant — a ticker on cooldown in one variant doesn't block the other | Independent per variant |

**Why this isn't a Golden Rule 18 violation:** Path A's frozen thresholds and accumulated count are completely untouched. Path B is a brand-new, separately-tracked hypothesis test, pre-registered before any of its own trades exist (0 as of Day 95) — exactly the same legitimate pattern as Day 79/80's MR liquidity re-test, just running in parallel instead of sequentially.

**Note on an earlier same-day mistake:** a first attempt at "Path B" (before this section was written) tried widening `compute_entry_levels()`'s stop clamp floor from entry×0.90 to entry×0.85 — this was based on a wrong premise (that the ATR-clamp formula was the actual entry gate) and a live backtest sanity check proved it directionally backwards (widening the stop makes risk bigger, which makes R:R *worse*, not better — PF, Sharpe, and drawdown all degraded on the same 76 historical trades). That approach was fully reverted; this S&R-based design replaced it once the real backtest logic was traced. See `KNOWN_ISSUES_DAY95.md` for the full narrative.

## 9. Mean-Reversion Arm (isolated system, RSI(2))

| Rule | Value |
|------|-------|
| Entry | RSI(2) < 10 AND price > 200 SMA AND price > $10 AND 20-day avg dollar volume > $25M (updated Day 81 — see Change Log; was price > $5 AND avg volume > 500K at initial freeze) |
| Exit | RSI(2) > 70 OR 10 trading days max |
| Stop | entry × (1 − 5%) — the actual backtested/live `stop_pct=0.05` formula (`mr_simulator.py`, `paper_trading/daily_job.py`); the live *detector*'s displayed stop/target (`mean_reversion.py`'s `detect_mr_signal()`, `max(entry×0.95, entry−1.5×ATR)`) is informational/UI-only and is NOT what the paper-trading engine or backtest actually exit on — corrected Day 82, this table previously conflated the two |
| Capital allocation | 50/50 split with momentum system (Gate 5, 1.9% overlap, 0.274 P&L correlation) — ⚠️ gross-of-costs at freeze time; see Section 11 |

## 10. Success / Failure Criteria (declared in advance)

Judgment happens only after **≥ 100 logged trades** in the Forward Test tab (raised from 50, Day 92 — user decision, not a response to any interim result: at the time of this change momentum had 0 closed trades and MR had 5, both far short of even the original 50). Before that point, any result — including a losing streak — is within expected variance and is NOT evidence the system is broken.

| Outcome | Threshold | Interpretation |
|---------|-----------|----------------|
| **Confirmed** | Live profit factor ≥ 1.2 AND positive expectancy after transaction costs, on ≥ 100 trades | System has a real, tradeable edge — continue as-is |
| **Modest but real** | PF 1.05–1.2 | Edge exists but thinner than backtest suggested (expected, per Fable review — survivorship bias + reused OOS) — continue with realistic expectations, do not abandon |
| **Broken** | PF < 0.9 after ≥ 100 trades, or expectancy consistently negative | Stop live trading, return to remediation Phase 4 (survivorship-free re-validation) before any further capital deployment |

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
| 81 | Section 9 MR entry gate updated: price>$5+500K shares → price>$10+20d ADV>$25M | Pre-committed, one-time liquidity re-test (Golden Rule 20) run Day 79/80, *before* any live MR paper trades existed — not a mid-flight re-tune, no trade count to reset. This amendment (made Day 82, per the Day 82 Fable hygiene audit) is a documentation catch-up: the live detector and paper-trading engine were correctly updated Day 81, but this doc's Section 9 table was never edited to match, so it briefly misdescribed the config the paper trades are actually being judged against. |
| 82 | Section 9 Stop row corrected | Clarified that the paper-trading engine and backtest exit on the flat 5% stop (`stop_pct=0.05`), not the ATR-based formula `mean_reversion.py`'s live *detector* displays for UI purposes — those are two different numbers that this table previously conflated. No behavior changed; documentation-only fix. |
| 88 | Candidate-pool breadth widened (not an entry/exit threshold change): momentum's per-day TradingView pre-filter raised from 50 to 150 raw candidates; MR's live universe switched from a static 54-ticker list to a dynamic ~200-300-ticker TradingView liquid-universe scan (`scan_queries.build_mr_universe_query()`), falling back to the static list if the screener is unavailable. | User asked how to reach the 50-trade confirmation bar faster. This is the legitimate lever per Golden Rule 18/20's own distinction: checking *more tickers* under the *same unchanged rule* is not re-tuning — nothing in this table's Sections 1-9 (the actual frozen thresholds) changed. Loosening RSI(2)/R:R/Config C thresholds instead would have been forbidden re-tuning and was explicitly rejected. |
| 92 | Confirmation bar raised: **50 → 100 logged trades** per system before Section 10 judgment (Sections 1-9 entry/exit thresholds themselves unchanged). | Explicit user decision to hold focus on forward-testing longer before any capital-allocation discussion. Not goalpost-moving in the Golden Rule 18 sense that decision guards against — that rule exists to stop *lowering* the bar or *changing thresholds* after a disappointing interim result to manufacture a better-looking number. Raising the trade-count bar is strictly more conservative (harder to pass, not easier), and was made with 0 momentum / 5 MR closed trades on the books — nowhere near either the old or new bar, so there was no interim result to be reacting to. |
| 95 | New Section 8b: **Path B** parallel momentum entry-gate experiment added — real S&R-based R:R gate (matches the actual historical Config C backtest logic), tracked under its own `variant='B_revised_rr'` ledger tag, own 100-trade bar. Sections 1-8/9 (Path A / MR) completely unchanged. | Live investigation found the live engine's R:R check (`compute_entry_levels()`'s flat/ATR proxy) was never the same logic the backtest actually validated — a live/backtest divergence bug, not a re-tune of a working threshold. Running as a parallel, separately-tracked experiment rather than replacing Path A preserves Path A's in-progress count entirely. |
