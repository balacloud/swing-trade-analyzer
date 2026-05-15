# API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 75 (May 15, 2026)
> **Total API Routes:** 29 (1 new route added Day 75: `/api/value/<ticker>`)
>
> **Day 75 Changes:** NEW `GET /api/value/<ticker>` — Value investing lens (Phase 1). Isolated endpoint, no impact on existing routes. Frontend v4.34, Backend v2.35, API Service v2.11.

---

## Day 75 New Endpoint — `GET /api/value/<ticker>`

### Purpose
Standalone value investing analysis — Buffett/Damodaran/Graham/Lynch/Greenblatt lens. **Completely isolated from swing verdict and categorical assessment.**

### Response Shape

```json
{
  "ticker": "AAPL",
  "cap_size": "large",
  "market_cap": 3150000000000,
  "current_price": 211.45,
  "quality": {
    "verdict": "decent",
    "roic": {
      "value": null,
      "display": "N/A",
      "note": "Not available (Finnhub free tier)"
    },
    "roe": {
      "value": 147.3,
      "display": "147.3%",
      "score": 2,
      "flag": "leverage_driven",
      "flag_detail": "ROE/ROA ratio: 4.2x — may be leverage-driven, not operational excellence"
    },
    "fcf_yield": {
      "value": 3.8,
      "display": "3.8%",
      "score": 1
    }
  },
  "valuation": {
    "verdict": "stretched",
    "graham_number": {
      "value": 87.23,
      "display": "$87.23",
      "upside_pct": -58.8,
      "bar": {
        "current": 211.45,
        "graham": 87.23,
        "pct_above": 142.4
      }
    },
    "pe_ratio": {
      "value": 32.1,
      "display": "32.1×",
      "threshold": 20,
      "score": 0
    },
    "peg_ratio": {
      "value": 2.4,
      "display": "2.4×",
      "type": "peg",
      "score": 0
    }
  },
  "dividend": {
    "yield_pct": 0.35,
    "display": "0.35%"
  },
  "summary": "Quality business, but priced beyond Graham's comfort zone.",
  "data_sources": ["finnhub", "yfinance"],
  "phase": 1
}
```

### Cap Size Tiers
| Tier | Market Cap | ROE Threshold | FCF Yield Threshold | Graham MOS |
|------|-----------|---------------|---------------------|------------|
| large | > $10B | 15% | 3% | 20% |
| mid | $2–10B | 12% | 3.5% | 30% |
| small | < $2B | 10% | 4% | 40% |

### Null Handling Rules
- Graham Number: if EPS ≤ 0 OR BVPS ≤ 0 → `null`, display `"Not applicable — negative inputs"`, **never red**
- ROIC: if not available from Finnhub → `null`, display `"N/A"`, gray card (not red)
- PEG/PEGY: auto-switch at `div_yield_pct > 1.5%`

### Quality Verdict Logic
| Condition | Verdict |
|-----------|---------|
| ROIC > WACC AND ROE > threshold | `"strong"` |
| Either (not both) | `"decent"` |
| Neither | `"weak"` |
| Both null | `"na"` |

### Valuation Verdict Logic
| Condition | Verdict |
|-----------|---------|
| Price < Graham × 0.8 AND P/E < threshold × 0.8 | `"strong"` |
| Price < Graham AND P/E < threshold | `"fair"` |
| Price 0–30% above Graham OR P/E at threshold | `"decent"` |
| Price > Graham × 1.3 OR P/E > threshold × 1.5 | `"stretched"` |

### Data Sources (Phase 1)
| Field | Source | Notes |
|-------|--------|-------|
| `roicTTM` | Finnhub | Not available on all free-tier tickers |
| `roeTTM`, `roaTTM` | Finnhub | Used for DuPont leverage flag |
| `pegRatio`, `peTTM` | Finnhub | Pre-computed ratios |
| `trailingEps`, `bookValue` | yfinance `.info` | Graham Number inputs |
| `freeCashflow` | yfinance `.info` | Falls back to OCF-Capex from cashflow df |
| `trailingAnnualDividendYield` | yfinance `.info` | **NOT `dividendYield`** — latter is unreliable |
| `sector` | yfinance `.info` | Used for sector exclusion warnings |

### Important: Dividend Yield Field
Use `trailingAnnualDividendYield` from yfinance `.info`. **Do NOT use `dividendYield`** — this field sources from Finnhub's `dividendYieldIndicatedAnnual` after the `_pct_to_decimal` transform, resulting in values like 36.22% for AAPL (should be 0.35%).

### Frontend Consumer
- Component: `frontend/src/components/ValueTab.jsx`
- Fetch: `frontend/src/services/api.js:fetchValueData()`
- Tab: `frontend/src/App.jsx` — 💎 Value button, `activeTab === 'value'`
- Theme: amber-400 accent, amber-600 active tab

---

## Unchanged Endpoints (Day 72 reference)

See archived `API_CONTRACTS_DAY72.md` for full documentation of all 28 pre-existing endpoints. Key endpoints unchanged:

| Endpoint | Purpose |
|----------|---------|
| `GET /api/analyze/<ticker>` | Full swing analysis (verdict, categorical, patterns) |
| `GET /api/sr/<ticker>` | Support/resistance levels + `meta.levelScores` (Day 72) |
| `GET /api/context/<ticker>` | Market context (cycles, econ, news, regime) |
| `GET /api/mr/signal/<ticker>` | Mean-reversion signal |
| `GET /api/mr/scan` | MR scan across watchlist |
| `GET /api/scanner/run` | TradingView screener scan |
| `GET /api/fear-greed` | Fear & Greed index |
| `GET /api/validate/<ticker>` | Validation engine |
| `GET /api/cache/status` | Cache status |
