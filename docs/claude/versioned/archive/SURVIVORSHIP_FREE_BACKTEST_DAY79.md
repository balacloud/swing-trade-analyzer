# Survivorship-Free Backtest Re-Validation (Day 79)

> **Source:** Fable Review Remediation Plan, Phase 4 (Task 4.1 + 4.2).
> **Script:** `backend/backtest/backtest_survivorship_free.py`
> **Run date:** Day 79, session 2 (July 6, 2026)
> **Purpose:** Test whether Config C's PF 1.61 and MR's PF 1.26 survive on a universe that wasn't hand-picked with 2026 hindsight.

---

## Method

**Original universe:** 60 tickers hand-picked in 2026, dominated by 2020–2025 mega-winners (NVDA, LLY, AVGO, PLTR, CRWD, COIN...).

**Unbiased universe:** Random sample of 400 tickers, **seed=42** (reproducible, no hand-picking), drawn from SimFin's full US coverage — **3,788 tickers** as of Day 79. Liquidity filtering (price > $5, 20-day avg dollar volume > $5M) happens **per-date inside the backtest itself**, not as a pre-selection step — pre-filtering to "currently liquid" names would just reintroduce a different flavor of hindsight bias. Same period as the original (2020-01-01 to 2025-12-31), Config C (standard holding period) and MR both run with all Phase 2 fixes already in place (transaction costs, gap-aware fills, corrected statistics).

**Residual survivorship (honest, not zero, as the plan anticipated):** 140/400 tickers (35%) had no usable OHLCV — mostly `YFTzMissingError('possibly delisted')`. This means the *true* historical universe was even messier than what could actually be tested; yfinance's own coverage gaps are a real, separate limitation layered on top of the sampling methodology. 260 tickers were processed for Config C, 263 for MR (slightly different skip counts — same download function, minor variance in which calls transiently failed).

---

## Results — Config C (Momentum, Standard Period)

| Metric | Original (hindsight, 60 tickers) | Unbiased (400-ticker sample, 260 usable) |
|--------|-----------------------------------|---------------------------------------|
| Trades | 238 | 114 |
| Win Rate | 53.78% | 49.12% |
| Profit Factor | 1.61 | **1.3985** |
| Sharpe | 0.85 | 0.5172 |
| Avg R-Multiple | — | 0.1126 |
| Max Drawdown (sequential 100%-equity) | 52.6%* | 53.05% |
| Max Drawdown (2%-fixed-risk, honest) | — (metric didn't exist yet) | **14.06%** |
| t-statistic | — | 1.4682 |
| p-value (i.i.d. t-test) | p=0.002 (original claim) | 0.1448 |
| p-value (block bootstrap, robust) | — (didn't exist yet) | **0.0935** |

*Original 52.6% DD figure is the same sequential-100%-equity artifact metric, not a like-for-like fixed-risk comparison.

### Interpretation (pre-committed criteria applied)

The plan's three buckets:
- **PF ≥ 1.3 AND bootstrap p < 0.05** → edge substantially confirmed
- **PF 1.1–1.3** → edge real but modest
- **PF < 1.1** → alpha claim unsupported

Config C's PF (1.3985) clears the top bucket's magnitude bar, but **neither p-value clears the 0.05 significance bar** (i.i.d. 0.145, block bootstrap 0.094 — the more robust measure is actually further from significance, not closer). The criteria require **both** conditions for "substantially confirmed" — since the significance leg fails, this does not qualify for that tier even though the PF number alone looks fine. Reading the two conditions together as intended (not cherry-picking the one that passes): **this is "edge real but modest," bordering on "not yet distinguishable from chance" at only 114 trades.** The point estimate is encouraging; the sample is too small to call it confirmed.

The honest, fixed-risk drawdown (14.06%) is far more reassuring than the sequential-equity artifact (53%) — this is a genuinely useful correction from Task 2.3.

**Bottom line: Config C's momentum edge survived the hindsight test in direction (still profitable, PF > 1) but degraded from 1.61 to ~1.40, and is not yet statistically distinguishable from noise. This is consistent with the Fable review's original estimate of "honest live PF ~1.1–1.3" — if anything, 1.40 is a slightly better outcome than that estimate, though not confirmed.**

---

## Results — Mean-Reversion (MR)

| Metric | Original (hindsight, 60 tickers, Gate 4) | Unbiased (400-ticker sample, 263 usable) |
|--------|-------------------------------------------|---------------------------------------|
| Trades | 520 (original) / 1,947 (Day 79 net-of-cost re-run, same 60-ticker universe) | **6,151** |
| Win Rate | 62.9% / 63.0% | **53.03%** |
| Profit Factor | 1.26 gross / **1.23 net** | **0.9942** |
| Sharpe | — | **−0.1009** |
| Avg Return/trade | — | **−0.0116%** (net negative) |
| Max Drawdown (2%-fixed-risk) | — | 98.9%* |
| p-value (block bootstrap) | — | 0.518 (nowhere near significant — consistent with no real edge) |

*The 98.9% fixed-risk drawdown is partly inflated by sheer trade count (6,151 sequential trades compounding on one equity curve will show large swings even near breakeven) but is still a red flag consistent with PF < 1.

### Interpretation (pre-committed criteria applied)

**PF 0.9942 is below 1.0 — net losing, not just "modest."** This falls decisively into the bottom bucket ("PF < 1.1 → alpha claim unsupported") and is worse than that bucket's floor. The Sharpe is negative. The block-bootstrap p-value (0.518) confirms there is no detectable edge at any reasonable confidence level — the result is indistinguishable from a coin flip with transaction-cost drag.

**Bottom line: MR's apparent edge (PF 1.23 net on the hand-picked universe) does not survive on a representative sample of the actual tradeable universe. This is exactly the failure mode the Fable review's survivorship-bias concern was warning about, now directly confirmed for MR specifically.** Per the plan's own instruction: **do not re-tune MR's thresholds to try to recover a positive PF** — that would be the data-snooping failure mode this entire remediation exists to prevent.

### A caveat on this specific finding, stated plainly
- MR fires extremely frequently (978 trades/year-equivalent on this universe — RSI(2)<10 is a common, non-selective trigger across thousands of small/mid-cap names), so 6,151 trades is a large, well-powered sample — this result should be trusted more, not less, than Config C's thinner 114-trade sample.
- MR trades carry no regime label in the current data (100% bucketed "unknown" — `mr_simulator.py` doesn't compute one). Regime-conditioned MR performance (e.g., "does MR work better in choppy/sideways markets specifically?") cannot be assessed from this run. This is a known gap, not investigated further here.
- This does not necessarily mean RSI(2) mean-reversion is worthless as a concept — Connors' original research context, position sizing, and universe selection may differ from this implementation. It means **STA's current MR implementation, as backtested on a representative universe, does not show a positive edge net of costs.**

---

## Addendum (Day 79, session 4) — One-Time Liquidity Re-Test for MR

**User decision:** kill MR outright, OR restrict to liquid names and re-test once — whichever the data supports, with no further iteration either way.

**Rationale for one re-test, not a re-tune:** the original MR entry condition (`mr_simulator.py`) had only a `price > $5` floor — **no dollar-volume liquidity gate at all**, unlike the momentum system's existing $5M ADV gate. This is different from tuning RSI thresholds to chase a better number — it's a defensible, principled execution constraint ("a real desk could actually trade this size") decided *before* seeing the result. Connors' original RSI(2) research was also validated on liquid large-caps, not penny/shell names — several of which appeared in the unrestricted run's ticker pool (AAGH, MRDB, and similar).

**Change made:** added a liquidity gate to `backtest_mr_strategy()`'s entry condition — price > $10 (was $5) and 20-day average dollar volume > $25M (was: none). Applied once, pre-committed, not to be iterated.

**Re-run:** same universe, same seed=42, same 400-ticker sample — `--mr-only` flag added to `backtest_survivorship_free.py` to re-test MR alone without re-running the unchanged Config C leg.

| Metric | Unrestricted (Day 79, session 2) | Liquidity-Restricted (Day 79, session 4) |
|--------|-----------------------------------|---------------------------------------|
| Trades | 6,151 | **3,210** |
| Win Rate | 53.03% | **57.35%** |
| Profit Factor | 0.9942 (net losing) | **1.1602** |
| Sharpe | −0.1009 | **1.3021** |
| Avg Return/trade | −0.0116% | **+0.2697%** |
| Max Drawdown (2%-fixed-risk) | 98.9% | **78.36%** (still high) |
| t-statistic / i.i.d. p-value | −0.18 / 0.861 | **3.39 / 0.0007** (looks significant) |
| p-value (block bootstrap, robust) | 0.518 | **0.0638** (just misses 0.05) |

### Interpretation — genuinely a gray zone, reported honestly

**The liquidity restriction flipped MR from net-losing to net-positive.** PF 1.16 clears the "PF < 1.1 → dead" floor and lands in the plan's "edge real but modest" bucket (1.1–1.3) — a real, non-trivial improvement, not noise: Sharpe went from negative to 1.30, and the naive t-test now looks strong (p=0.0007).

**But the robust significance test still falls just short.** The block-bootstrap p-value (0.064) — which accounts for trade clustering, the same correction that made Config C's naive p=0.002 fall to p=0.09 — **narrowly misses the conventional 0.05 bar.** This is the exact same pattern seen with momentum: a naive test overstates confidence; the robust test says "promising, not proven."

**The fixed-risk drawdown (78%) is a genuine, separate concern.** Even with a positive PF, 3,210 trades compounding on one equity curve with clusters of consecutive losses (max 11 in a row) produced a severe drawdown under fixed 2% risk sizing. This doesn't contradict PF > 1 — thin, high-frequency edges can still have brutal variance — but it's a real risk-management flag, not just a statistics footnote.

**Verdict: this is not a clean kill, and it is not a clean confirm.** Per the pre-committed criteria (PF 1.1–1.3 → "edge real but modest, paper trade with expectations reset"), liquidity-restricted MR now qualifies for that middle tier — the same tier momentum landed in. **Recommendation: keep it alive, restricted to the $25M+ ADV / $10+ price universe, sized small, and require it to clear the same live-paper-trading bar as momentum (50+ trades, judged on the pre-registered criteria) before any capital allocation decision.** Do not treat this backtest result alone as sufficient to allocate capital — exactly as the plan intended for the momentum system.

**No further re-testing/re-tuning of MR's liquidity threshold or entry rules** — this was the one allowed re-test. Any future adjustment should be driven by live paper-trading results, not more backtest iteration on the same historical data.

---

## Recommendation (superseded for MR by the Day 79 session 4 addendum above — kept for history)

**Per the plan's explicit instruction: do not re-tune thresholds to fix these numbers.** That is the data-snooping failure mode this whole remediation plan exists to end.

1. **Config C / momentum system**: proceed to paper trading as planned. The edge is directionally real (PF > 1, positive Sharpe) but not yet statistically confirmed — treat the pre-registered "Confirmed" bar (PF ≥ 1.2 after 50+ live trades, per `PAPER_TRADING_PREREGISTRATION.md`) as the actual test; this backtest re-validation is consistent with, not a substitute for, that live test.
2. ~~**MR / mean-reversion system**: do not allocate real capital to this system as currently implemented.~~ **Superseded** — see addendum: the one-time liquidity re-test flipped MR to net-positive (PF 1.16). Current status: real-but-modest, same tier as momentum, requires live paper-trading confirmation before capital allocation — not the flat "do not allocate" verdict this section originally gave on the unrestricted-universe result.
3. ~~If MR is to be salvaged...~~ **Done** — the liquidity restriction was the one salvage attempt, per the user's explicit instruction. No further backtest iteration on MR going forward; live paper-trading data decides from here.

---

## Reproducibility

```bash
python backend/backtest/backtest_survivorship_free.py --sample-size 400 --seed 42 --scan-interval 2
```

Full results: `backend/backtest_results_holistic/survivorship_free_20260706_131040.json` (includes the full 260/263-ticker lists actually used, skip lists, and complete metrics for both systems).
