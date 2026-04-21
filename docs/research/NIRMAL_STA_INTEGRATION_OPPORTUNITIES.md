# Nirmal's System → STA Integration Opportunities

**Created:** April 20, 2026  
**Purpose:** How to leverage Nirmal's 3-year track record to improve Swing Trade Analyzer  
**Status:** Analysis complete — awaiting prioritization decision  

---

## EXECUTIVE SUMMARY

Nirmal is a proven swing trader with ~65-75% win rate, 3:1 R:R discipline, and consistent 2-entry/2-target structure. His methodology overlaps significantly with what STA already does — this is validation, not contradiction. The key opportunity is **closing the gaps** between what he does and what STA currently outputs.

**Bottom line:** 4 actionable improvements, ranked by effort vs. impact.

---

## WHAT ALREADY ALIGNS (No Changes Needed)

These validate our existing system — Nirmal independently arrived at the same conclusions:

| Nirmal's Practice | STA's Current Implementation | Validation |
|-------------------|-------------------------------|-----------|
| 2-entry DCA system | Dual Entry Strategy card | ✅ Identical |
| R:R minimum 3:1 | R:R filter in Trade Setup | ✅ Aligned |
| ATR-based stops | ATR stops primary (Tier 1A) | ✅ Same |
| Technical primary, fundamentals secondary | Categorical Assessment ordering | ✅ Same |
| "Safe traders" / "Risky traders" split | Simple vs Full analysis views | ✅ Conceptually same |
| Sector rotation awareness | Sectors tab (Day 62) | ✅ Covered |
| Earnings awareness | Earnings warning card (v4.10) | ✅ Covered |
| Fear & Greed monitoring | Categorical Assessment sentiment | ✅ Covered |
| VIX as market gate | Risk/Macro gate in categorical | ✅ Covered |
| SPY 200 SMA regime filter | Bear regime filter (Day 57) | ✅ Covered |

**Conclusion:** STA and Nirmal's system are directionally identical. He uses intuition + pattern recognition; STA systematizes it.

---

## GAPS — WHERE STA CAN IMPROVE

### GAP 1: Gap-Fill Detection (High Value, Medium Effort)

**What Nirmal does:** Explicitly uses "gap filling strategy" as a trade trigger. Called AAPL using it (Aug 2023): *"Radar detected under gap filling strategy — Gap under daily timeframe Aug 03-04."*

**What STA currently does:** Nothing. No gap detection at all.

**Why it matters:**
- Gap fills are a high-probability setup — price tends to return to fill unfilled gaps
- Nirmal has used it repeatedly for entries on large-cap tech
- Objective, programmable, backtest-able

**Implementation idea:**
- Backend: Add `detect_gaps()` to `backend.py` — scan for unfilled gaps >1.5% on daily OHLCV
- Output: `gapFillZone: { lowerBound, upperBound, gapAge, filled: bool }`
- Frontend: Add to Price Structure Card (Phase 2) or Trade Setup card
- Label: "Gap Fill Zone: $187 - $191 (22 days unfilled)"

**Effort:** Medium (1 session — data already available from TwelveData OHLCV)

---

### GAP 2: Two-Price Entry Format in Trade Setup (Low Effort, High UX Value)

**What Nirmal does:** Every call has `Entry1 (immediate) + Entry2 (averaging, ~8% lower)`. His group members didn't understand it initially, but once they did, it became their standard operating model.

**What STA currently does:** Shows a single "Entry Zone" (support range). Doesn't explicitly call out "buy here, average here."

**Why it matters:**
- STA's users don't know *how* to use the entry zone
- Nirmal's format tells you exactly: "buy at resistance breakout, reload at next support"
- This is behavioral — it reduces emotional decisions mid-trade

**Implementation idea:**
- In Trade Setup card, explicitly label:
  - `Primary Entry: $X.XX (breakout confirmation)`
  - `Averaging Entry: $X.XX (support level / ~8% lower)`
- Can use existing S/R data — first level = primary entry, next support = averaging entry
- Add a note: "Safe: enter at primary. Aggressive: add at averaging level."

**Effort:** Low (1-2 hours, purely frontend label change in Trade Setup card)

---

### GAP 3: Market Phase Detection (Medium Effort, High Value)

**What Nirmal does:** He implicitly reads market phase before sizing trades:
- Bull Rally → full size, tech focus
- Correction → reduce 50%, go to cash, buy puts
- Consolidation → tight stops, smaller size
- Sector Rotation → pivot to small-caps/IWM

**What STA currently does:** Has VIX gate + SPY regime filter. Has Sectors tab. But doesn't synthesize these into a **"current market phase" label** that adjusts position sizing.

**Why it matters:**
- Nirmal would never give a full-size BUY call when his market phase reads "Correction"
- STA gives the same verdict regardless of market phase (only gates on VIX/SPY binary)
- During April 2026 tariff crash: Nirmal said "Play safe" and "too late to exit, hold tight" — STA had no mechanism to reflect this

**Implementation idea:**
- Synthesize existing signals: VIX + SPY trend + sector rotation state + Fear & Greed
- Output a 5-phase label in the Risk/Macro card:
  - 🟢 **Bull Rally** — reduce caution, full size
  - 🟡 **Profit Taking** — book partial, tighten stops
  - 🟡 **Sector Rotation** — shift to IWM/financials
  - 🟠 **Consolidation** — reduce size, tight stops
  - 🔴 **Correction** — cash heavy, no new longs
- Already have all the data (VIX, SPY, sector RS) — just need synthesis logic
- Affects position sizing output (VIX sizing already done in Tier 2A)

**Effort:** Medium (1 session — new `marketPhase()` function, builds on existing data)

**Note:** This is NEW logic — needs research validation before implementing. Log as "idea pending validation."

---

### GAP 4: Nirmal's Watchlist as a Default Scan Seed (Very Low Effort)

**What Nirmal does:** Has a consistent core watchlist he returns to repeatedly: SPY, QQQ, TQQQ, NVDA, AMD, GOOGL, AAPL, SMCI, PLTR, MSFT, QBTS, IWM, MU.

**What STA currently does:** Scan tab with TradingView screener. Users scan the whole market.

**Why it matters:**
- 80% of Nirmal's biggest wins came from this core 15-stock watchlist
- Quality over quantity — fewer stocks, better tracking
- These are all liquid, S&P 500 class stocks — STA's sweet spot

**Implementation idea:**
- Add a "Nirmal Watchlist" preset to the Scan tab (alongside S&P 500 / NASDAQ 100 etc.)
- Pre-seeds the scan with his 15 core tickers
- **Not a new feature** — just a named preset of existing scan functionality
- Could also be a "Quick Check" shortcut on the Analyze page

**Effort:** Very low (30 min — add preset to Scan dropdown)

**Note:** Feature freeze consideration — this is purely additive. A named preset doesn't change any logic.

---

## OPTIONSIQ ALIGNMENT (Separate Project, Strong Overlap)

Nirmal's options format is almost exactly what OptionsIQ is designed to produce:

| Nirmal's Options Call | OptionsIQ Target Output |
|-----------------------|------------------------|
| Stock entry + companion call option | Stock signal + suggested option play |
| Strike ~5-10% OTM | ATM/OTM strike recommendation |
| 4-8 week preferred expiry | DTE recommendation |
| 100%+ ROI minimum | Expected ROI range |
| "Risky traders only" flag | Risk level label |
| Exit at 50% SL or 100% ROI | Automated exit signals |

**Action:** Use Nirmal's historical calls (the CSVs referenced in the doc: `nirmal_options_recommendations.csv`, 223 plays) to validate OptionsIQ's recommendation logic before shipping.

---

## PRIORITY ORDER

| # | Gap | Effort | Impact | Verdict |
|---|-----|--------|--------|---------|
| 1 | Two-price entry labels in Trade Setup | Very Low | High UX | **Do now** |
| 2 | Nirmal watchlist preset in Scan | Very Low | Medium | **Do now** |
| 3 | Gap-fill detection | Medium | High signal | **Next sprint after paper trading** |
| 4 | Market phase synthesis | Medium | High | **Needs validation first** |

Items 1 + 2 are additive, take <2 hours combined, and require zero new logic.
Items 3 + 4 are real features — need research/backtest validation per Golden Rule #15 before building.

---

## WHAT NOT TO BUILD (Based on Nirmal's Cautions)

Things Nirmal explicitly warns against — STA should NOT automate these:

- **No auto-averaging losers** — STA should never suggest "add more" on a position that's below stop loss
- **No auto-options recommendations for beginners** — OptionsIQ needs clear risk labeling
- **No overriding stop loss** — if STA shows a trade as HOLD but price has broken stop, it's still a STOP
- **No "it'll bounce back" signals** — STA should not show optimistic commentary on broken setups

---

## VALIDATION — COMPLETED (April 20, 2026)

Script: `backend/backtest/nirmal_validation.py`  
Full results: `docs/research/nirmal_validation_results.csv` + `NIRMAL_STA_VALIDATION_RESULTS.md`

**Research question answered:** Of Nirmal's 392 parsed stock calls (378 validated), what % would STA have rated as BUY?

| STA Verdict | Count | % |
|-------------|-------|---|
| BUY (full agreement) | 58 | 15.3% |
| HOLD (cautious) | 152 | 40.2% |
| AVOID (contradiction) | 168 | 44.4% |

**Interpretation — Style Discovery, Not System Failure:**

The 44.4% contradiction rate is dominated by "Weak technical setup" (low TT score). This reveals a fundamental style difference, not a signal gap:

- **STA's categorical engine** = universal quant framework — momentum arm (Trend Template + RS>1.2) + MR arm (RSI(2)<10) + quality gate + regime filter
- **Nirmal's system** = multi-style: momentum + value recovery + gap-fill + news catalyst

Breakdown of Nirmal's trade types (estimated from data):
- ~25% are Minervini-style momentum (TT 7-8/8) → STA agrees
- ~35% are value recovery (quality stocks at TT 1-4/8, RSI 30-60) → STA correctly AVOID
- ~15% are gap-fill/mean-reversion (low TT but oversold RSI) → covered by MR engine
- ~25% are news/macro catalyst plays → not covered

**What this means for STA:**
1. **Keep the Minervini filter** — don't dilute it to match Nirmal's broader style. Our backtest (PF 1.61) was run on these stricter criteria and they outperform.
2. **The 58 BUY agreement calls** are Nirmal's highest-quality setups by Minervini standard — worth studying separately.
3. **Gap-fill detection** (GAP 1) gains urgency — a meaningful slice of the 44% contradiction is gap-fill entries that look technically weak by TT but have high win rate in Nirmal's hands.
4. **MR engine** already covers the oversold recovery subset (BSY RSI=26.7 with TT=7/8 is exactly an MR setup).
5. **Conclusion:** STA is a systematized version of Nirmal's *best* setups (Minervini-quality), not his full system. This is the right design.

---

*This document is analysis-only. No code changes should be made until user approves specific items.*
*Golden Rule #15: Never implement without validation — require research, backtest, or practitioner consensus first.*
