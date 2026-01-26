# Swing-Trading Analytics: Alignment vs Standards (Draft)

**Report Date:** 2026-01-23  
**Scope:** Compare reported industry standards to current codebase behavior  
**Status:** Draft; citations pending verification outside this repo

---

## Inputs (Provided by user)

- 52-week lookback: 252 trading days
- 13-week lookback: 63 trading days
- RS: price ratio vs benchmark, adjusted close
- Stage 2 trend: Price > 50SMA > 200SMA
- ATR/RSI defaults: 14 periods
- Volume averages: 20/50 days
- S&R: pivot highs/lows + volume profile (agglomerative clustering not standard)
- Stops: ATR-based; R:R minimum 2:1 (3:1 preferred)
- Fundamentals: EPS growth, revenue growth, ROE/ROA, D/E, margins, market cap, beta, dividend yield
- Market: SPY for RS benchmark; VIX for risk regime

---

## Alignment Table (Draft)

| Area | Reported Standard | Current Code | Alignment |
|------|-------------------|--------------|-----------|
| 52-week window | 252 trading days | 252-day anchors for RS + 52w high/low | ✅ |
| 13-week window | 63 trading days | 63-day anchors | ✅ |
| RS formula | Adjusted close ratio vs SPY | Adjusted close when available; RS return ratio + price ratio | ⚠️ Partial |
| Trend stage | Price > 50SMA > 200SMA | Checklist uses Stage 2 rule | ✅ |
| ATR/RSI | 14 periods | ATR/RSI = 14 | ✅ |
| Volume averages | 20/50 day | Added avg20/avg50 | ✅ |
| S&R methods | Pivot + volume profile | Dual output: Standard (pivot/volume) + Agglomerative | ✅ |
| Stop placement | ATR-based | Added ATR stop alongside support stop | ✅ |
| R:R threshold | 2:1 min, 3:1 preferred | Pass at 2:1; display ATR R:R | ⚠️ Partial |
| Fundamentals | Listed metrics | Added yfinance fundamentals in `/api/analyze` | ✅ |
| Market regime | VIX | Added VIX snapshot | ✅ |

---

## Implementation Notes

- RS now uses adjusted close when the source provides it; if not, falls back to raw close and logs a data-quality warning.
- S&R output includes both:
  - `supportResistanceStandard`: pivot + volume profile
  - `supportResistanceAgglomerative`: agglomerative fallback
- Trade levels expose both support-based and ATR-based stops:
  - `suggestedStop` (support)
  - `atrStop` (2 × ATR)

---

## Open Verification Items

1. Confirm the standard RS formula (price ratio vs return ratio).
2. Confirm adjusted close requirement for RS and trend filters across vendors.
3. Confirm R:R threshold preference (2:1 vs 3:1) in professional swing-trading practice.

---

## Files Updated (Day 4)

- `backend/app/main.py`
- `backend/app/services/data_provider.py`
- `backend/app/services/fundamentals.py`
- `backend/app/services/market_data.py`
- `backend/app/utils/checklist.py`
- `backend/app/utils/relative_strength.py`
- `backend/app/utils/support_resistance.py`
- `frontend/src/App.jsx`
- `frontend/src/styles.css`

