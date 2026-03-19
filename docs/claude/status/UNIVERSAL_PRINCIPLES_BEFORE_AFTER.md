# STA Universal Principles Evolution — Before vs After

> **Date:** March 19, 2026 (Day 69-70)
> **Source:** 4-LLM audit (Grok 3, Gemini 2.5 Pro, Perplexity Pro, Claude Opus 4.6) — 35 claims, 5 domains
> **Core finding:** STA was ~70% universal already. Evolution was surgical, not a rebuild.
> **Synthesis:** `docs/research/UNIVERSAL_PRINCIPLES_SYNTHESIS.md`
> **Implementation plan:** `docs/research/UNIVERSAL_PRINCIPLES_IMPLEMENTATION_PLAN.md`

---

## 1. Stop Loss Logic

| | Before | After |
|--|--------|-------|
| **Primary stop** | Fixed 7% from entry | **ATR x 2** (volatility-adaptive) |
| **7% role** | The stop | **Max cap only** — stop never exceeds 7% even if 2x ATR is higher |
| **Simple checklist** | Flat 7% for all cap sizes | **7% large / 9% mid / 10% small** |
| **Evidence** | Convention | VERIFIED 3/4 LLMs (Claim 4.2). ATR analysis: 7% = only 1.4x ATR for small caps (below 2x noise floor) |
| **Files** | `riskRewardCalc.js`, `trade_simulator.py`, `simplifiedScoring.js` | Same files, logic inverted (ATR first, % cap second) |

---

## 2. Position Sizing

| | Before | After |
|--|--------|-------|
| **Sizing model** | Fixed % risk (Van Tharp 2%) — VIX-blind | **VIX-scaled**: 100% at VIX<20, 75% at VIX 20-30, 50% at VIX>30 |
| **Evidence** | N/A | PLAUSIBLE 3/4 — Moreira & Muir (2017): position sizing is the #1 regime lever |
| **Files** | `positionSizing.js` | Same file + `App.jsx` VIX passthrough |

---

## 3. Sentiment in Verdict

| | Before | After |
|--|--------|-------|
| **Verdict formula** | T + F + **S** → 2+ Strong = BUY | T + F → 2 Strong = BUY. **Sentiment = informational only** |
| **Sentiment display** | Full card, same weight as others | "(info)" label, **reduced opacity** |
| **BottomLineCard** | Referenced F&G in "What's Good" / "What's Risky" | **All sentiment references removed** |
| **Risk/Macro gate** | Unfavorable → HOLD | **Unchanged** — validated by backtest (bear WR 55.6%→71.4%) |
| **Evidence** | Backtest hardcoded sentiment='Neutral' — never validated | Removing aligns live system with backtest evidence |
| **Files** | `categoricalAssessment.js`, `categorical_engine.py`, `BottomLineCard.jsx` | Same files, frontend+backend parity |

---

## 4. Momentum Measurement

| | Before | After |
|--|--------|-------|
| **RS for verdict** | 52-week RS only | **52-week RS only** (unchanged — blended RS degrades PF 1.90→1.51) |
| **RS display** | 52-week only | **Blended RS (21d + 63d + 126d avg) shown as informational** |
| **Simple checklist RS** | RS >= 1.0 | **RS >= 1.2** |
| **Evidence** | Convention | Backtest across 20 tickers: PF 1.56→1.78, WR 49.7%→52.6%. RS 1.0 was MISLEADING per 2/2 LLMs (too permissive for Minervini/O'Neil) |
| **Files** | `rsCalculator.js`, `scoringEngine.js`, `simplifiedScoring.js` | New `calculateBlendedRS()` function added |

---

## 5. Mean-Reversion Arm (Entirely New)

| | Before | After |
|--|--------|-------|
| **Strategy** | Momentum-only (silent in choppy markets) | **Momentum + Mean-Reversion dual arm** |
| **MR entry** | Did not exist | **RSI(2) < 10** + price > 200 SMA + price > $5 + vol > 500K |
| **MR exit** | Did not exist | RSI(2) > 70 OR 10-day time exit OR 5% stop |
| **MR display** | Did not exist | `MRSignalCard.jsx` — dark theme, hidden when inactive |
| **Backtest** | N/A | Gate 4 PASSED: **520 trades, 62.9% WR, PF 1.26, avg hold 4.1 days** |
| **Evidence** | N/A | VERIFIED — Asness et al. (2013) strategy diversification. RSI(2)<10 is evidence-based (Connors). RSI(14)<30 was MISLEADING 3/4 LLMs |
| **Files** | N/A | `mean_reversion.py` (NEW), `mr_simulator.py` (NEW), `MRSignalCard.jsx` (NEW), `backend.py` (+2 endpoints), `api.js` |

---

## 6. Parameter Validation

| | Before | After |
|--|--------|-------|
| **Validation** | Walk-forward only | Walk-forward + **parameter stability analysis** |
| **Tool** | None | `parameter_stability.py` — tests ADX ±2, RS ±0.1, stop ±0.5x |
| **Findings** | Unknown | rsi_low fragile at 55 (PF 0.83), stop_atr_multiple fragile at 1.5x (PF 0.98). Current params validated as robust |
| **Evidence** | N/A | MISLEADING 4/4 that walk-forward alone is enough (Claim 5.2) |

---

## 7. Weight Optimization Principle

| | Before | After |
|--|--------|-------|
| **Category weights** | Equal (by accident — binary system treats equally) | **Equal by principle** — codified as Golden Rule #16 |
| **Evidence** | N/A | MISLEADING 4/4 — DeMiguel et al. (2009): equal weights beat optimized OOS. 238 trades is too few to optimize 4+ weights |
| **Files** | `GOLDEN_RULES.md` | Design principle, not code change |

---

## 8. UI Presentation (Simplicity Premium)

| | Before | After |
|--|--------|-------|
| **Views** | 3 views: Full, Decision Matrix, Simple | **2 views**: Full + Simple (Decision Matrix removed) |
| **Full analysis** | 12 sections flat-listed, all visible | **3-tier progressive disclosure** |
| **Tier 1 (always visible)** | Everything | Verdict, Trade Setup, Bottom Line, MR Signal, Quality Gates |
| **Tier 2 (collapsed)** | N/A | Holding Period, Price & RS, Pattern Detection, Categorical Assessment |
| **Tier 3 (hidden)** | N/A | Technical Indicators (click to show) |
| **TradingView Chart** | Present (collapsible widget) | **Removed** |
| **Volume checklist** | Flat $10M all caps | **$2M small / $5M mid / $10M large** |
| **Evidence** | N/A | VERIFIED/PLAUSIBLE 4/4 — simplicity premium is real. Fewer indicators = faster decisions = better execution |

---

## 9. Bug Fixes (Tier 0 — Pre-Work)

| Bug | Before | After |
|-----|--------|-------|
| VCP volume | Only checked overall volume decline | Per-contraction volume dry-up check (+10 confidence booster) |
| MTF "3.2x" | Hallucinated claim in docstrings | Removed — no source ever supported this |
| F&G neutral zone | 35-60 (too wide — 36 and 59 feel very different) | Narrowed to **40-55** |
| RRG normalization | Docs didn't match code | Docs corrected |

---

## What DIDN'T Change (~70% of the System)

| Module | Why It Survived |
|--------|----------------|
| **Categorical Assessment structure** (T/F/S/R) | Standard quant factor decomposition — 4 LLMs agreed |
| **Trend Template** (8 Minervini criteria) | IS the universal trend definition — not practitioner-specific |
| **S&R Engine** (Pivot → Agglomerative → KMeans → Volume Profile) | Standard quant clustering — robust |
| **Pattern Detection** (VCP, Cup & Handle, Flat Base) | Binary overlay design is correct (not a scored factor) |
| **Risk/Macro gate** (VIX + SPY > 200 SMA) | Bear filter validated by backtest (WR improvement) |
| **Backtest core** (Config C: 238 trades, PF 1.61, Sharpe 0.85) | Results unchanged — all changes are orthogonal |
| **Data pipeline** (TwelveData → Finnhub → AlphaVantage → yfinance) | Multi-source architecture is robust |
| **Context Tab** (FRED + Alpha Vantage) | Pre-flight info layer — doesn't modify verdicts |
| **Sector Rotation** (11 SPDR ETFs, RRG quadrants) | Informational layer — intact |
| **All 25 existing API endpoints** | Zero modified. 2 new MR endpoints added |

---

## Backtest Impact

**No re-run needed.** Reasoning:

1. **Sentiment removal** — backtest already hardcoded Neutral (zero impact on results)
2. **ATR stops** — backtest already used ATR for quick period (now primary everywhere)
3. **VIX sizing** — added to simulator but doesn't change historical entry/exit signals
4. **MR engine** — completely isolated, own standalone backtest (Gate 4 PASSED)
5. **Simple checklist** (RS 1.2, cap-aware) — frontend-only human tool, doesn't touch backtest engine
6. **Blended RS** — informational display only, verdict still uses rs52Week

**Outstanding:** Gate 5 (combined momentum+MR system) — tests whether both arms together improve Sharpe vs momentum-only. Future work, not a re-run.

---

## Version History

| Version | State |
|---------|-------|
| v4.30 | Before universal principles (Day 68) |
| v4.31 | After Tier 0-3 implementation (Day 70) |
| v4.32 | After simplicity premium UI + cap-aware checklist (Day 70B) |

---

*The engine that produces Config C (PF 1.61, WR 53.78%) is intact. What evolved: how the system sizes positions (VIX-aware), sets stops (ATR-primary), catches mean-reversion signals (new arm), validates parameters (stability test), and presents information (simpler, honest, cap-aware).*
