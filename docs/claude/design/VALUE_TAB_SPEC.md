# Design Spec: Value Investing Tab

> **Status:** Draft v1 — Post 4-LLM research synthesis
> **Author:** Claude (Day 75 design session)
> **Date:** May 15, 2026
> **Research source:** `docs/research/VALUE_INVESTING_RESEARCH_PROMPT.md` (4 LLMs: Perplexity, ChatGPT, Gemini, Claude Opus)
> **Depends on:** Feature freeze lift after paper trading validation
> **Priority:** MEDIUM — build after Gate 5 + behavioral test + paper trading + N4

---

## 0. First Principles — Why This Tab Must Exist

STA is a swing trading tool. Its categorical assessment, Trade Setup card, and verdict are all designed for 5–30 day holds. But the same data pipeline (fundamentals, price, sector) contains everything needed to answer a completely different question:

> **"Is this a quality business available at a fair or undervalued price for a 3–5 year hold?"**

This is a different lens. It doesn't replace the swing verdict. It doesn't compete with it. It answers a question the swing trader sometimes asks *after* a BUY signal: "Is this also a business I'd want to hold through a correction?"

**The tab exists because:**
1. STA already fetches ROE, D/E, revenue growth, EPS — the raw materials are free
2. Buffett/Graham/Lynch/Greenblatt/Damodaran frameworks are well-validated over decades
3. A swing entry into a quality business is better than a swing entry into a mediocre one — same technical setup, different downside floor

---

## 1. Tab Identity

| Field | Value |
|-------|-------|
| **Tab Name** | 💎 Value |
| **Route/key** | `valueTab` |
| **Position** | After Context tab, before Forward Test tab |
| **Scope** | Read-only analysis. Zero wiring to swing verdict, categorical assessment, or Trade Setup |
| **API endpoint** | `/api/value/<ticker>` (new) |
| **Trigger** | On-demand when tab is opened (not part of parallel fetch on Analyze page) |

---

## 2. What This Tab IS and IS NOT

| This tab IS | This tab IS NOT |
|-------------|-----------------|
| A separate value investing lens | A replacement or override for the swing verdict |
| Based on validated primary sources (Graham, Damodaran, Lynch, Greenblatt, Buffett) | Based on folklore thresholds (D/E < 0.5, FCF yield > 5%, Rev growth > 10%) |
| Cap-size and sector-aware | A universal screener with fixed thresholds |
| Honest about data limitations (N/A ≠ red) | A false-precision machine (no point estimates without uncertainty) |
| Built on existing STA data pipeline + 2 new calls | A new data pipeline requiring new providers |
| Suitable for 3–5 year investment horizon | A timing tool for entry/exit decisions |

**Critical constraint:** No output from this tab affects `determineVerdict()`, `categoricalAssessment.js`, or any other STA scoring function. Complete isolation.

---

## 3. Validated Metric Set (4-LLM consensus)

### 3.1 Core Metrics (universal — all 5 investors agree on the principle)

| Metric | Source attribution | Formula | Threshold | Guard |
|--------|-------------------|---------|-----------|-------|
| **ROIC** | Damodaran (VERIFIED) — "value creation = ROIC > WACC" | Finnhub `roicTTM` (direct). Fallback: `NOPAT / InvestedCapital` | Green: ROIC > WACC; Yellow: within 2% of WACC; Red: ROIC < WACC | If null + fallback fails → N/A. Don't show red. |
| **ROE (5-yr median)** | Buffett (PLAUSIBLE) — high ROE with low leverage | Finnhub `roeTTM` + AV history for 5-yr median | Cap-size adjusted (see §4) | Always pair with Net Income trend. Flag: rising ROE + flat NI = buyback distortion |
| **Earnings Stability** | Graham (VERIFIED) — "no earnings deficit in past 10 years" | AV `annualReports[].netIncome` — count profitable years of last 5 (10 if available) | Green: 5/5 (or 10/10); Yellow: 4/5; Red: ≤ 3/5 | Most reliable AV field. Low missing data risk. |
| **Balance Sheet Strength** | Graham (VERIFIED) — current ratio ≥ 2, LTD ≤ NCA | Net Debt/EBITDA (primary) + Interest Coverage (secondary) | Cap-size adjusted (see §4). Sector exclusions (see §5) | If interestExpense ≈ 0 → "N/A (no debt)" — NOT an error. Not red. |
| **Relative P/E vs Sector** | Graham (VERIFIED, P/E ≤ 15 on 3-yr avg), Damodaran | yfinance `trailingPE` vs sector median from STA's existing sector rotation data | Small: ≤ 0.80× sector median; Mid: ≤ 0.90×; Large: ≤ 1.00× | If P/E negative (loss) → N/A. Don't show red. |
| **Margin of Safety** | Damodaran (VERIFIED) — `(IntrinsicValue − Price) / IntrinsicValue` | Derived from DCF Lite (see §3.2) | Green: MOS ≥ cap-size threshold; Yellow: 10–threshold; Red: < 10% or negative | Only compute if DCF Lite is computable. Otherwise N/A. |

### 3.2 Investor-Specific Metrics (valid but narrower applicability)

| Metric | Investor | Formula | When to show | When to suppress |
|--------|----------|---------|--------------|------------------|
| **Graham Number** | Graham (VERIFIED, Intelligent Investor ch.14) | `sqrt(22.5 × max(EPS_ttm, 0) × max(BVPS, 0))` | Asset-backed, profitable, established companies | **`EPS ≤ 0 OR BVPS ≤ 0 → N/A ("Not applicable — negative inputs")`**. Show sector warning for tech, software, biotech. |
| **PEG / PEGY** | Lynch (PLAUSIBLE) — "a fairly priced company's P/E equals its growth rate" | PEG = `trailingPE / (5yr_EPS_CAGR × 100)`. PEGY = `trailingPE / (growth + dividendYield)` | Growth stocks and stalwarts | Suppress for: cyclicals at earnings trough, zero-growth businesses. Use PEGY when dividend yield > 1.5%. Label as "approximate" when using 1-yr fallback. |
| **DCF Lite** | Damodaran (VERIFIED) — single-stage Gordon Growth | `FCF_adjusted × (1 + g) / (r − g_terminal)` | Any company with positive FCF | FCF ≤ 0 → N/A. **Hard cap: g_terminal ≤ 2.5% (nominal GDP ceiling).** Show sensitivity: "±1% terminal growth ≈ ±18% value." Surface assumptions in UI. |
| **EV/EBIT** | Greenblatt (VERIFIED as ranking metric, not absolute threshold) | `(marketCap + totalDebt − totalCash) / EBIT_TTM` | Profitable companies in screener context | EBIT ≤ 0 → N/A. Do NOT badge as "cheap" with absolute cutoff. Show as ranking vs sector peers. |
| **FCF Yield (adjusted)** | Modern screen (NOT a primary-source metric) | `(FCF_3yr_avg − SBC_3yr_avg) / marketCap` | Secondary display only | **No pass/fail badge.** Damodaran: single-year FCF = "more noise than information." 3-yr average + SBC-adjusted only. |

### 3.3 Explicitly EXCLUDED metrics (rejected by 2+ LLMs)

| Metric | Why excluded |
|--------|-------------|
| D/E < 0.5 | Not Graham's actual rule. IFRS 16 distorts it. Replaced by Net Debt/EBITDA + ICR. |
| Revenue growth > 10% = moat | Not from any primary source. Growth destroys value when ROIC < WACC. |
| Net margin > 10% | No primary source. Varies by sector structure. Use ROIC > WACC instead. |
| FCF yield > 5% as quality badge | Modern quant screen. Single-year FCF too noisy. Demoted to secondary display. |
| EV/EBIT < 10 as hard threshold | Greenblatt uses relative ranking, not absolute cutoff. |

---

## 4. Cap-Size Thresholds Matrix

| Metric | Small < $2B | Mid $2–10B | Large > $10B |
|--------|-------------|------------|--------------|
| ROE (5-yr median) | > 10–12% | > 12–15% | > 15% |
| Net Debt / EBITDA | < 1.5× | < 2.0× | < 2.5× |
| Interest Coverage | > 4× | > 4× | > 3× |
| DCF Margin of Safety | ≥ 40% | ≥ 30% | ≥ 20–25% |
| Graham Number | Only if profitable + asset-backed. High N/A expected. | Traditional sectors (industrials, retail, financials) | Most applicable |
| P/E vs sector | ≤ 0.80× median | ≤ 0.90× median | ≤ 1.00× median |

---

## 5. Sector Exclusions

Some sectors break standard value metrics structurally. These sectors need a different evaluation approach, not a red badge:

| Sector | What breaks | What to do |
|--------|------------|-----------|
| **Banks / Insurance** | D/E meaningless (structural leverage). Graham Number's P/B cap ignores ROTCE. | Use P/TBV + ROE vs peers instead. Skip Net Debt/EBITDA. |
| **Utilities / Pipelines / REITs / Telecoms** | High D/E by design (stable contracted cash flows). | Use Interest Coverage only. Skip Net Debt/EBITDA. Tag: "Sector carries structural leverage." |
| **Biotech / Pre-profit tech** | Negative EPS → Graham Number undefined. DCF unreliable (no FCF). | Suppress Graham Number + DCF. Show only ROIC, stability score, balance sheet. |
| **Software / Intangible-heavy** | BVPS massively understated (R&D expensed, not capitalized). P/B meaningless. | Suppress Graham Number. Add note: "Book value understates economic value for this sector." |

---

## 6. Null Handling Rules

These are non-negotiable. Wrong null handling produces misleading results (Gemini: "both EPS and BVPS negative → nonsensical positive Graham Number").

```
Graham Number:
  if EPS <= 0 OR BVPS <= 0:
    display "N/A — Not applicable (negative inputs)"
    # NOT red. NOT "data missing". Different meaning.
  if sector in [SOFTWARE, BIOTECH, PLATFORM]:
    display value + warning: "Book value may understate economic value"

DCF Lite:
  if FCF_adjusted <= 0:
    display "N/A — Requires positive free cash flow"
  always show: terminal_g assumption, discount_rate assumption, sensitivity band

PEG:
  if earnings_growth <= 0:
    display "N/A — Negative/zero growth breaks PEG math"
  if dividend_yield > 1.5%:
    use PEGY = PE / (growth + dividend_yield), label as "PEGY"
  if sector is cyclical AND earnings near trough:
    display "N/A — PEG unreliable near earnings trough"
  if 5yr CAGR unavailable:
    fallback to yfinance earningsGrowth (1yr), label "(approximate)"

Interest Coverage:
  if interestExpense ≈ 0:
    display "N/A (no debt)" — NOT an error, NOT red

ROE:
  if netIncome <= 0 OR shareholderEquity <= 0:
    display "N/A"
  if ROE rising AND NetIncome flat/declining (3-yr trend):
    flag: "⚠️ ROE increase may reflect share buybacks, not operational improvement"

EV/EBIT:
  if EBIT <= 0:
    display "N/A — Company not yet profitable on EBIT basis"
```

---

## 7. Data Source Architecture

```
LIVE TIER (every /api/value/<ticker> request):
  yfinance:
    - trailingEps, bookValue (BVPS)     → Graham Number
    - trailingPE                         → Relative P/E, PEG
    - freeCashflow, marketCap            → FCF Yield
    - totalDebt, totalCash               → EV components, Net Debt
    - earningsGrowth (1yr fallback)      → PEG fallback
    - dividendYield                      → PEGY calculation

DAILY CACHE TIER (Finnhub, ~unlimited rate, cache 24h):
  /stock/metric?metric=all:
    - roicTTM                            → ROIC (primary, pre-computed)
    - roeTTM                             → ROE TTM
    - roaTTM                             → DuPont cross-check
    - pfcfTTM                            → Price/FCF cross-check
    - currentEv                          → EV for EV/EBIT

NIGHTLY BATCH TIER (Alpha Vantage, 25 req/day, cache 24h):
  INCOME_STATEMENT (annual):
    - netIncome × 5–10 years            → Earnings Consistency, PEG CAGR
    - ebit                              → EV/EBIT, Interest Coverage
    - interestExpense                   → Interest Coverage
    - incomeTaxExpense, incomeBeforeTax → Tax rate for ROIC fallback
  BALANCE_SHEET (annual):
    - commonStockSharesOutstanding      → EPS computation cross-check
    - totalStockholderEquity            → ROIC fallback, ROE history
  CASH_FLOW (annual):
    - operatingCashflow, capitalExpenditures → FCF fallback computation
    - stockBasedCompensation            → FCF SBC adjustment
```

**AV quota management:** 3 calls per stock = ~8 stocks/day. Batch-prefetch for active watchlist only. Never call AV on-demand. Backend should check AV cache before making any AV request.

**FCF small-cap fallback:** If `yfinance.freeCashflow = None` (expected 20–35% of small-caps):
```python
fcf = operating_cashflow - capital_expenditure  # from yfinance cashflow dataframe
# raises coverage from ~70% to ~85–90%
```

---

## 8. UI Design

### 8.1 Layout

```
┌─────────────────────────────────────────────────────┐
│  💎 Value Analysis — AAPL                            │
│  "Quality at a fair price (3–5yr lens)"              │
│  ⚠️ This analysis does not affect the swing verdict  │
└─────────────────────────────────────────────────────┘

┌─────────────────────┐  ┌─────────────────────────────┐
│  QUALITY             │  │  VALUATION                  │
│                      │  │                             │
│  ROIC: 35.2%         │  │  Graham Number: $142        │
│  ✅ Well above WACC  │  │  Current: $189              │
│                      │  │  ⚠️ Above ceiling           │
│  ROE (5yr med): 28%  │  │                             │
│  ✅ Strong (large)   │  │  DCF Lite: $165             │
│  ⚠️ Buyback note     │  │  MOS: -13% (overvalued)    │
│                      │  │  Assumptions: g=2.5%, r=9% │
│  Earnings: 5/5 yrs   │  │  Sensitivity: ±1% g = ±18% │
│  profitable          │  │                             │
│                      │  │  P/E: 28× vs sector 24×    │
│  Interest Coverage:  │  │  Premium to sector: +17%   │
│  N/A (no debt)       │  │                             │
└─────────────────────┘  │  PEG: 1.8 (approximate)    │
                          │  PEGY: N/A                  │
┌─────────────────────┐  └─────────────────────────────┘
│  BALANCE SHEET       │
│                      │  ┌─────────────────────────────┐
│  Net Debt/EBITDA:    │  │  OVERALL VALUE VERDICT       │
│  Net Cash position   │  │                             │
│  ✅ Excellent        │  │  QUALITY: Strong ✅          │
│                      │  │  VALUATION: Stretched ⚠️    │
│  D/E: N/A (net cash) │  │                             │
│                      │  │  "High quality business.    │
└─────────────────────┘  │   Currently trading above    │
                          │   conservative value         │
                          │   estimates."                │
                          └─────────────────────────────┘
```

### 8.2 Color coding
- **Green (✅):** Metric clearly passes threshold
- **Yellow (⚠️):** Near threshold, or caveat applies
- **Red (❌):** Clearly fails threshold
- **Gray (N/A):** Not applicable — data or math precondition not met. Never red.

### 8.3 Overall Value Verdict (2 components, never one number)
1. **Quality verdict:** ROIC, ROE, Earnings Stability → Strong / Decent / Weak
2. **Valuation verdict:** Graham Number, DCF MOS, Relative P/E → Attractive / Fair / Stretched

These never combine into a single score (Gemini: "composite scoring decay — Magic Formula edge is gone after publication"). Display as 2 separate signals.

### 8.4 Disclosures (always visible)
- "This analysis uses 3–5yr valuation frameworks. Not a swing trade signal."
- "DCF Lite uses simplified assumptions. See sensitivity range."
- Where source is AV-derived (nightly batch), show: "Data as of: [cache timestamp]"

---

## 9. API Design

### `GET /api/value/<ticker>`

**Response structure:**
```json
{
  "ticker": "AAPL",
  "cap_size": "large",
  "sector": "Technology",
  "quality": {
    "roic": { "value": 35.2, "wacc_approx": 9.0, "verdict": "strong", "source": "finnhub" },
    "roe": {
      "ttm": 147.9,
      "five_yr_median": 88.2,
      "net_income_trend": "stable",
      "buyback_flag": true,
      "verdict": "strong_with_caveat",
      "source": "finnhub+av"
    },
    "earnings_stability": { "profitable_years": 5, "of_years": 5, "verdict": "strong" },
    "interest_coverage": { "value": null, "note": "no_debt", "verdict": "na" }
  },
  "valuation": {
    "graham_number": { "value": 142.3, "current_price": 189.0, "verdict": "above_ceiling", "applicable": true },
    "dcf_lite": {
      "intrinsic_value": 165.0,
      "margin_of_safety": -0.13,
      "terminal_g": 0.025,
      "discount_rate": 0.09,
      "sensitivity_pct_per_1pct_g": 18.0,
      "verdict": "overvalued",
      "fcf_source": "yfinance_adjusted"
    },
    "relative_pe": { "trailing_pe": 28.0, "sector_median_pe": 24.0, "ratio": 1.17, "verdict": "premium" },
    "peg": { "value": 1.8, "type": "peg", "approximate": true, "verdict": "fair" }
  },
  "balance_sheet": {
    "net_debt_ebitda": { "value": -0.8, "threshold": 2.5, "verdict": "strong" }
  },
  "overall": {
    "quality_verdict": "strong",
    "valuation_verdict": "stretched",
    "summary": "High quality business. Currently trading above conservative value estimates."
  },
  "data_freshness": {
    "yfinance": "2026-05-15T09:30:00",
    "finnhub": "2026-05-15T08:00:00",
    "alpha_vantage": "2026-05-15T02:00:00"
  }
}
```

---

## 10. Implementation Phases

### Phase 1 — Core tab with live-tier + Finnhub metrics (1 session)
- `/api/value/<ticker>` endpoint using yfinance + Finnhub only
- ROIC (Finnhub), ROE (Finnhub TTM), Relative P/E, Graham Number, FCF Yield
- `ValueTab.jsx` — Quality + Valuation columns, Overall Verdict
- All null guards implemented
- Cap-size detection from existing market cap data

### Phase 2 — AV-derived metrics (1 session, requires AV batch cache design)
- Earnings Consistency (AV 5-yr netIncome)
- Interest Coverage (AV EBIT / interestExpense)
- EV/EBIT (AV EBIT + yfinance EV)
- ROE 5-yr median (AV history)
- SBC-adjusted FCF Yield (AV stockBasedCompensation)

### Phase 3 — DCF Lite + PEG (1 session)
- DCF Lite with hard-capped terminal growth + sensitivity display
- PEG/PEGY with growth rate sourcing + approximate label
- 5-yr EPS CAGR from AV (with fallback to yfinance earningsGrowth)

---

## 11. What Is NOT In Scope (ever, for this tab)

- Full Damodaran 10-K DCF (multi-year income/balance/cashflow statement model)
- Moat analysis (qualitative — not automatable)
- Sector-adjusted valuation multiples (too complex for v1)
- Magic Formula screener / universe ranking (requires universe data, not per-stock)
- Canadian ticker coverage (same data source gaps as Analyze page)
- Any output that flows into swing verdict, categorical assessment, or Trade Setup

---

## 12. Research Sources

| Source | Prompt | Key findings |
|--------|--------|-------------|
| Perplexity Deep Research | Prompt 1: Core metric validation | ROIC>WACC verified. Graham Number = ceiling not signal. D/E<0.5 = misattributed. PEG = plausible for growth. FCF yield = noisy. Revenue growth > 10% = unverified. |
| ChatGPT Deep Research | Prompt 2: Cap-size adjustments | Relative P/E (not absolute 15). Net Debt/EBITDA + ICR replaces D/E. Cap-size ROE tiers. DCF MOS: 40/30/25% by cap size. Illiquidity discount = private company rule, not public equity. |
| Gemini Deep Research | Prompt 4: Failure modes | Graham Number: negative input guards critical. ROE: DuPont + buyback flag. PEG: PEGY for dividends. DCF: terminal growth hard cap. IFRS 16 breaks D/E for retailers. FCF: SBC add-back distortion. Magic Formula alpha decayed post-publication. 3 value trap case studies. |
| Claude Opus | Prompt 3: Data availability | Finnhub has roicTTM directly — use it. AV = nightly batch only (25/day = 8 stocks). Graham Number: negative EPS = #1 failure mode. FCF fallback formula (OCF − Capex) raises small-cap coverage to 85–90%. ROIC manual fallback formula provided. |

---

*This spec is research-validated and ready for implementation.*
*Golden Rule #15 satisfied: 4-LLM consensus + data availability confirmed before any code.*
*Build only after feature freeze lift (post paper trading).*
