# Data source audit vs IBKR truth (20261114)

Script `backend/backtest/audit_vs_ibkr.py`. Truth: IBKR (user's own contracts), last 5 daily closes and volumes, three month-end closes (split-adjusted) and corporate actions. Sources graded: every source step 1 fetched (Twelve Data, Yahoo, Tradier for US; Yahoo for Canada; EODHD where the free quota allowed).
**C3** close accuracy (last 5 days), **C5** history level vs IBKR month-ends (catches unadjusted splits), **C7** volume plausibility. Volume is not expected to equal IBKR's (it counts a subset of trades); only zero or wildly off volume is flagged.

## Matrix (worst result across the sources that can serve the ticker)

| Class | Ticker | IBKR splits in the last year | Source | C3 close | C5 level | C7 volume |
|---|---|---|---|---|---|---|
| US stock | `BRK-B` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| US stock | `CAT` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| US stock | `JPM` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| US ETF | `GDX` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| US ETF | `SMH` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| US ETF | `SOXX` | 2026-11-05 ×3 | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| US leveraged | `DRAL` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| US leveraged | `QPUX` | 2026-03-23 ×0.333333 | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ❌ | ✅ |
| US leveraged | `SPCL` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| US leveraged | `UBOT` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
|  |  |  | tradier | ✅ | ✅ | ✅ |
| CA stock | `ATD.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `CNR.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `CSU.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `RY.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA ETF | `HXQ.TO` | — | yfinance | ✅ | ✅ | ⚠️ |
| CA ETF | `VFV.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA ETF | `XCHP.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA ETF | `XEQT.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA leveraged | `GDXU.TO` | 2026-05-25 ×3 | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA leveraged | `SOXL.NE` | 2026-05-25 ×3 | yfinance | ⚠️ | ✅ | ❌ |
|  |  |  | eodhd | ⚠️ | ✅ | ✅ |
| CDR | `AMD.TO` | 2026-10-16 ×7 | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CDR | `AVGO.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CDR | `MU.TO` | 2026-03-10 ×5 | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CDR | `SNDK.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |

## Findings (warn and fail), with evidence

**QPUX** (US leveraged; IBKR contract 866508540, DFINC 2X D LNG PURE QUNT ETF)
- ❌ tradier C5: 2025-11: tradier 178.83 vs IBKR 59.61 (x3.00) | IBKR splits in range: 2026-03-23 x0.333333

**SOXL.NE** (CA leveraged; IBKR contract 805995437, BETAPRO 3X SC DAILY LEV BA (CAD))
- ⚠️ yfinance C3: max close diff 0.34% over the 4 settled days; last day 4.22% (IBKR final history bar can be 15 min stale)
- ❌ yfinance C7: source volume is zero
- ⚠️ eodhd C3: max close diff 0.34% over the 4 settled days; last day 4.40% (IBKR final history bar can be 15 min stale)

**HXQ.TO** (CA ETF; IBKR contract 700079680, GLOBAL X NASDAQ-100 INDEX (CAD))
- ⚠️ yfinance C7: volume yfinance/IBKR x0.78

## Volume ratios (source ÷ IBKR, last 5 sessions)

| Class | Ticker | twelvedata | yfinance | tradier | eodhd |
|---|---|---|---|---|---|
| US stock | `JPM` | 2.09 | 2.09 | 2.09 | — |
| US stock | `CAT` | 1.68 | 1.68 | 1.68 | — |
| US stock | `BRK-B` | 1.80 | 1.80 | 1.80 | — |
| US ETF | `SMH` | 1.45 | 1.45 | 1.45 | — |
| US ETF | `SOXX` | 1.40 | 1.40 | 1.40 | — |
| US ETF | `GDX` | 1.68 | 1.68 | 1.68 | — |
| US leveraged | `DRAL` | 1.15 | 1.15 | 1.16 | — |
| US leveraged | `SPCL` | 1.62 | 1.62 | 1.64 | — |
| US leveraged | `UBOT` | 1.21 | 1.21 | 1.21 | — |
| US leveraged | `QPUX` | 1.18 | 1.18 | 1.19 | — |
| CA stock | `RY.TO` | — | 3.01 | — | — |
| CA stock | `CNR.TO` | — | 1.83 | — | — |
| CA stock | `ATD.TO` | — | 1.27 | — | — |
| CA stock | `CSU.TO` | — | 1.38 | — | — |
| CA leveraged | `SOXL.NE` | — | — | — | 0.95 |
| CA ETF | `XEQT.TO` | — | 0.88 | — | — |
| CA ETF | `VFV.TO` | — | 0.86 | — | — |
| CA ETF | `HXQ.TO` | — | 0.78 | — | — |
| CA ETF | `XCHP.TO` | — | 0.83 | — | — |
| CA leveraged | `GDXU.TO` | — | 0.86 | — | 0.86 |
| CDR | `AMD.TO` | — | 0.94 | — | 0.94 |
| CDR | `AVGO.TO` | — | 0.92 | — | — |
| CDR | `MU.TO` | — | 0.93 | — | 0.93 |
| CDR | `SNDK.TO` | — | 0.94 | — | 0.94 |
