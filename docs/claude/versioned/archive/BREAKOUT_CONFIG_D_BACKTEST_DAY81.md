# Breakout Enhancement Plan — Task 0.1/0.2 Results (Day 81, July 10, 2026)

> **Source:** `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` Phase 0
> **Command run (exactly as specified in the plan's acceptance criteria):**
> `python backend/backtest/backtest_holistic.py --configs C D E --walk-forward`
> **Universe:** default 60-ticker `BACKTEST_TICKERS` (hand-picked, same universe as the original Config C headline numbers — appropriate here since this is a *relative* comparison of C/D/E on identical tickers/period, not a new absolute-PF claim; survivorship bias affects all three configs equally and does not affect the internal comparison)
> **Period:** walk-forward IS 2020-01-01–2023-06-30, OOS 2023-07-01–2025-12-31
> **Prerequisite verified before running:** gap-aware fills present in `trade_simulator.py` (`open_day <= stop_price` / `open_day >= target_price` checks) — confirmed via grep before starting, per the plan's explicit instruction.

---

## What Was Built

Config D and E added to `check_entry_signals()` in `backend/backtest/backtest_holistic.py`, sharing the same `detect_patterns()` call and priority-ordered scan (vcp → cup_handle → flat_base) as Config B, so no extra pattern-detection cost:

- **Config D** (confirmed-only): Config A + pattern status == `broken_out` **and** `breakout.volume_confirmed == True` + viable + R:R ≥ 1.2
- **Config E** (anticipatory-only): Config A + pattern status in `(at_pivot, forming)` + viable + R:R ≥ 1.2 — the complement of D within B's status set (leaves `complete` as B/C-only, matching neither D nor E)

**Config C's own gating was verified byte-for-byte unchanged** before running the real comparison: quick-test (5 tickers) run on the pre-edit code and post-edit code produced identical results (4 trades, 75.0% WR, PF 2.0782, avg R 0.2269, Sharpe 0.0602, block bootstrap p=0.232) — confirmed via `git stash`/`git stash pop` diff testing. The frozen canonical Config C number is untouched.

---

## Results

| Config | Period | Trades | Win Rate | Avg Return | Profit Factor | Avg R | Sharpe |
|--------|--------|--------|----------|------------|----------------|-------|--------|
| **C** (mixed, existing) | IS | 29 | 55.17% | 1.50% | 2.01 | 0.23 | 0.68 |
| **C** (mixed, existing) | OOS | 42 | 52.38% | 1.33% | 1.64 | 0.24 | 0.74 |
| **D** (confirmed-only, new) | IS | **0** | — | — | — | — | — |
| **D** (confirmed-only, new) | OOS | **0** | — | — | — | — | — |
| **E** (anticipatory-only, new) | IS | 24 | 50.00% | 0.97% | 1.54 | 0.16 | 0.25 |
| **E** (anticipatory-only, new) | OOS | 38 | 47.37% | 0.88% | 1.38 | 0.19 | 0.38 |

Config E alone captures 24/29 (83%) of C's IS trades and 38/42 (90%) of C's OOS trades — the large majority of Config C's edge already comes from anticipatory (`at_pivot`/`forming`) entries, not confirmed breakouts. The remaining ~5–9% comes from `complete` status (cup_handle only), which is neither D nor E.

## Config D: Zero Trades — Root Cause (Not a Bug)

Verified this is a genuine, well-explained result, not a defect in the Day 81 implementation. Diagnostic: ran `pattern_detection.detect_patterns()` at **daily granularity** across the **full 2019–2025 range** on AAPL, MSFT, and META (all three high-signal tickers with multiple real Config C trades) and counted every pattern with confidence ≥ 60 by status, across all three pattern types (VCP, cup & handle, flat base):

```
AAPL: at_pivot=146, cup_formed=115, forming=29, complete=8, broken_out=0
MSFT: at_pivot=153, forming=48, cup_formed=20, complete=14, broken_out=0
META: cup_formed=22, forming=23, at_pivot=37, complete=1, broken_out=0
```

**`broken_out` status at confidence ≥ 60 occurred zero times across ~4,000+ sampled daily checks on three of the market's most actively-patterned large caps.** This traces to how `pattern_detection.py` computes confidence: for VCP, confidence is built from base-quality signals (contraction count, decreasing contraction depth, volatility contraction, base tightness, volume dry-up) — properties of the **pre-breakout consolidation phase**. The moment price actually closes above the pivot (`status='broken_out'`), the trailing lookback window that feeds the confidence calculation now includes the breakout's own expansion in volatility and range, which is structurally the opposite of what the confidence score rewards. Cup & handle's confidence (cup depth/shape, handle formation) has the same character. So a pattern reaching `broken_out` status while *still* holding ≥60% confidence is a narrow-to-nonexistent intersection by construction, not a data or threshold artifact — confirmed by checking `check_breakout_quality()`'s volume-confirmation window too (`lookback_days=5`, searches for the first close-above-pivot day in that window): for a stock that's been above pivot for a while, this window no longer even contains the true breakout day, compounding the rarity.

**Important scope note:** this backtest tests `pattern_detection.py`'s 3-status lifecycle (the system Config C actually uses), *not* the newer, richer 8-state `breakout_detection.py` engine wired in Phase 1.5 (`BREAKOUT_CONFIRMED`, `RETEST_ENTRY`, etc.). That engine uses different, more sophisticated gates (candle quality, RS-vs-benchmark, ATR contraction) and has never been backtested — this result says nothing about whether *that* engine's confirmed-breakout state would behave differently. Per the plan's own gap analysis (G4), these are explicitly two different systems.

---

## Verdict Against Pre-Committed Interpretation Criteria (Task 0.2)

The plan pre-committed three branches before results existed:

> - D meaningfully beats C → confirmation adds edge → emphasize `broken_out`+confirmed states.
> - D ≈ C → confirmation is neutral → surface both equally.
> - **D worse OR trade count collapses (<40% of C) → confirmation costs more than it saves → keep current mixed logic, emphasize `at_pivot` (early) candidates instead.**

**Verdict: third branch, decisively.** 0 trades is a more extreme case of "trade count collapses" than the criteria anticipated (0% of C's count, not just <40%). Combined with the root-cause finding above, this isn't merely "confirmation costs more than it saves" — within `pattern_detection.py`'s existing confidence methodology, waiting for `broken_out` status essentially **never** fires as an actionable, high-confidence signal at all. Config E (anticipatory-only) is a much closer proxy for "what Config C's edge actually is" than Config D could ever be under this pattern-detection design.

**Change to the live/frozen system: none**, per the plan's explicit rule. This is a backtest-only finding about which trade population the frozen system's edge already lives in.

## Implication for Phases 2–3

Per this verdict, **Phase 2 (breakout state badges) and Phase 3 (`/breakout-watch` skill) should emphasize `at_pivot`/`BREAKOUT_WATCH`/anticipatory states as the actionable candidates**, not treat `BREAKOUT_CONFIRMED` as the primary signal — consistent with what Config E's trade share already shows. Note Phase 2/3 consume the *separate* `breakout_detection.py` 8-state engine (not `pattern_detection.py`), so this is directional guidance (anticipatory > confirmed, based on the pattern-detection system's evidence) rather than a literal state-mapping — the 8-state engine's own `BREAKOUT_CONFIRMED` accuracy is still unvalidated and a separate question.
