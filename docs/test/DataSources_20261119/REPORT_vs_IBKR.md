# Data source audit vs IBKR truth (20261119)

Script `backend/backtest/audit_vs_ibkr.py`. Truth: IBKR (user's own contracts), last 5 daily closes and volumes, three month-end closes (split-adjusted) and corporate actions. Sources graded: every source step 1 fetched (Twelve Data, Yahoo, Tradier for US; Yahoo for Canada; EODHD where the free quota allowed).
**C3** close accuracy (last 5 days), **C5** history level vs IBKR month-ends (catches unadjusted splits), **C7** volume plausibility. Volume is not expected to equal IBKR's (it counts a subset of trades); only zero or wildly off volume is flagged.

## Matrix (worst result across the sources that can serve the ticker)

| Class | Ticker | IBKR splits in the last year | Source | C3 close | C5 level | C7 volume |
|---|---|---|---|---|---|---|
| US stock | `BRK-B` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US stock | `CAT` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US stock | `JPM` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US ETF | `GDX` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US ETF | `SMH` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US ETF | `SOXX` | 2026-11-05 ×3 | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `AAPU` | — | twelvedata | ✅ | ⚠️ | ✅ |
|  |  |  | yfinance | ✅ | ⚠️ | ✅ |
| US leveraged | `AMZU` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `AVGC` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `BRKU` | — | twelvedata | ✅ | ✅ | ❌ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `COPZ` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `COTG` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `DRAL` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `ELIL` | — | twelvedata | ✅ | ⚠️ | ✅ |
|  |  |  | yfinance | ✅ | ⚠️ | ✅ |
| US leveraged | `GGLL` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `METU` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `MSFU` | — | twelvedata | ✅ | ⚠️ | ✅ |
|  |  |  | yfinance | ✅ | ⚠️ | ✅ |
| US leveraged | `NFXL` | — | twelvedata | ✅ | ⚠️ | ✅ |
|  |  |  | yfinance | ✅ | ⚠️ | ✅ |
| US leveraged | `NVDL` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `QPUX` | 2026-03-23 ×0.333333 | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `SOXL` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `SPCL` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `TSLL` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `UBOT` | — | twelvedata | ✅ | ✅ | ✅ |
|  |  |  | yfinance | ✅ | ✅ | ✅ |
| US leveraged | `URAA` | — | twelvedata | ✅ | ⚠️ | ✅ |
|  |  |  | yfinance | ✅ | ⚠️ | ✅ |
| CA stock | `ASTL.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `ATD.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA stock | `BDT.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `CCO.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `CGY.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `CNQ.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `CNR.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA stock | `CSU.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA stock | `GIB-A.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `MDA.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `NTR.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `PNG.V` | — | yfinance | ✅ | ✅ | ✅ |
| CA stock | `RY.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA ETF | `CARS.TO` | — | yfinance | ❌ | ✅ | ✅ |
| CA ETF | `COPP.TO` | — | yfinance | ✅ | ✅ | ⚠️ |
| CA ETF | `FINN.NE` | — | yfinance | ✅ | ✅ | ✅ |
| CA ETF | `HURA.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA ETF | `HXQ.TO` | — | yfinance | ✅ | ✅ | ⚠️ |
|  |  |  | eodhd | ✅ | ✅ | ⚠️ |
| CA ETF | `MTRX.TO` | — | yfinance | ⚠️ | ✅ | ✅ |
| CA ETF | `ORBX.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA ETF | `RBOT.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA ETF | `SGRD.TO` | — | yfinance | ⚠️ | ✅ | ⚠️ |
| CA ETF | `VFV.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA ETF | `XCHP.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA ETF | `XDRV.TO` | — | yfinance | ❌ | ✅ | ⚠️ |
| CA ETF | `XEQT.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA ETF | `XETM.TO` | — | yfinance | ✅ | ✅ | ⚠️ |
| CA ETF | `XGD.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CA leveraged | `GDXU.TO` | 2026-05-25 ×3 | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CA leveraged | `SOXL.NE` | 2026-05-25 ×3 | yfinance | ⚠️ | ✅ | ❌ |
|  |  |  | eodhd | ⚠️ | ✅ | ✅ |
| CDR | `AMD.TO` | 2026-10-16 ×7 | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CDR | `ANET.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CDR | `ASML.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CDR | `AVGO.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CDR | `GEV.TO` | — | yfinance | ✅ | ✅ | ✅ |
| CDR | `MU.TO` | 2026-03-10 ×5 | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CDR | `SNDK.TO` | — | yfinance | ✅ | ✅ | ✅ |
|  |  |  | eodhd | ✅ | ✅ | ✅ |
| CDR | `WDC.TO` | — | yfinance | ✅ | ✅ | ✅ |

## Findings (warn and fail), with evidence

**SOXL.NE** (CA leveraged; IBKR contract 805995437, BETAPRO 3X SC DAILY LEV BA (CAD))
- ⚠️ yfinance C3: max close diff 0.34% over the 4 settled days; last day 4.22% (IBKR final history bar can be 15 min stale)
- ❌ yfinance C7: source volume is zero
- ⚠️ eodhd C3: max close diff 0.34% over the 4 settled days; last day 4.22% (IBKR final history bar can be 15 min stale)

**HXQ.TO** (CA ETF; IBKR contract 700079680, GLOBAL X NASDAQ-100 INDEX (CAD))
- ⚠️ yfinance C7: volume yfinance/IBKR x0.78
- ⚠️ eodhd C7: volume eodhd/IBKR x0.78

**MTRX.TO** (CA ETF; IBKR contract 762280434, MTRX)
- ⚠️ yfinance C3: max close diff 0.61% over the 4 settled days; last day 0.00% (IBKR final history bar can be 15 min stale)

**XDRV.TO** (CA ETF; IBKR contract 613363675, XDRV)
- ❌ yfinance C3: max close diff 2.15% over the 4 settled days; last day 0.41% (IBKR final history bar can be 15 min stale)
- ⚠️ yfinance C7: volume yfinance/IBKR x0.75

**CARS.TO** (CA ETF; IBKR contract 290879740, CARS)
- ❌ yfinance C3: max close diff 2.64% over the 4 settled days; last day 0.10% (IBKR final history bar can be 15 min stale)

**COPP.TO** (CA ETF; IBKR contract 700079802, COPP)
- ⚠️ yfinance C7: volume yfinance/IBKR x0.66

**XETM.TO** (CA ETF; IBKR contract 653041473, XETM)
- ⚠️ yfinance C7: volume yfinance/IBKR x0.76

**URAA** (US leveraged; IBKR contract 712146384, URAA)
- ⚠️ twelvedata C5: 2025-11: twelvedata 32.38 vs IBKR 35.15 (x0.92)
- ⚠️ yfinance C5: 2025-11: yfinance 32.25 vs IBKR 35.15 (x0.92)

**AAPU** (US leveraged; IBKR contract 578561419, AAPU)
- ⚠️ twelvedata C5: 2025-11: twelvedata 35.22 vs IBKR 38.08 (x0.93)
- ⚠️ yfinance C5: 2025-11: yfinance 35.10 vs IBKR 38.08 (x0.92)

**MSFU** (US leveraged; IBKR contract 583996502, MSFU)
- ⚠️ twelvedata C5: 2025-11: twelvedata 42.82 vs IBKR 46.15 (x0.93)
- ⚠️ yfinance C5: 2025-11: yfinance 42.70 vs IBKR 46.15 (x0.93)

**NFXL** (US leveraged; IBKR contract 733168177, NFXL)
- ⚠️ twelvedata C5: 2025-11: twelvedata 40.39 vs IBKR 43.03 (x0.94)
- ⚠️ yfinance C5: 2025-11: yfinance 40.32 vs IBKR 43.03 (x0.94)

**BRKU** (US leveraged; IBKR contract 747569063, BRKU)
- ❌ twelvedata C7: source volume is zero

**ELIL** (US leveraged; IBKR contract 771551303, ELIL)
- ⚠️ twelvedata C5: 2025-11: twelvedata 28.55 vs IBKR 31.99 (x0.89)
- ⚠️ yfinance C5: 2025-11: yfinance 28.24 vs IBKR 31.99 (x0.88)

**SGRD.TO** (CA ETF; IBKR contract 875271486, SGRD)
- ⚠️ yfinance C3: max close diff 0.65% over the 4 settled days; last day 0.00% (IBKR final history bar can be 15 min stale)
- ⚠️ yfinance C7: volume yfinance/IBKR x0.62

## Volume ratios (source ÷ IBKR, last 5 sessions)

| Class | Ticker | twelvedata | yfinance | tradier | eodhd |
|---|---|---|---|---|---|
| US stock | `JPM` | 2.09 | 2.09 | — | — |
| US stock | `CAT` | 1.68 | 1.68 | — | — |
| US stock | `BRK-B` | 1.80 | 1.80 | — | — |
| US ETF | `SMH` | 1.45 | 1.45 | — | — |
| US ETF | `SOXX` | 1.40 | 1.40 | — | — |
| US ETF | `GDX` | 1.68 | 1.68 | — | — |
| US leveraged | `DRAL` | 1.15 | 1.15 | — | — |
| US leveraged | `SPCL` | 1.62 | 1.62 | — | — |
| US leveraged | `UBOT` | 1.21 | 1.21 | — | — |
| US leveraged | `QPUX` | 1.18 | 1.18 | — | — |
| CA stock | `RY.TO` | — | 3.01 | — | 3.01 |
| CA stock | `CNR.TO` | — | 1.83 | — | 1.83 |
| CA stock | `ATD.TO` | — | 1.27 | — | 1.27 |
| CA stock | `CSU.TO` | — | 1.38 | — | 1.38 |
| CA leveraged | `SOXL.NE` | — | — | — | 0.95 |
| CA ETF | `XEQT.TO` | — | 0.88 | — | 0.88 |
| CA ETF | `VFV.TO` | — | 0.86 | — | 0.86 |
| CA ETF | `HXQ.TO` | — | 0.78 | — | 0.78 |
| CA ETF | `XCHP.TO` | — | 0.83 | — | 0.83 |
| CA leveraged | `GDXU.TO` | — | 0.86 | — | 0.86 |
| CDR | `AMD.TO` | — | 0.94 | — | 0.94 |
| CDR | `AVGO.TO` | — | 0.92 | — | 0.92 |
| CDR | `MU.TO` | — | 0.93 | — | 0.93 |
| CDR | `SNDK.TO` | — | 0.94 | — | 0.94 |
| CA ETF | `FINN.NE` | — | 2.12 | — | — |
| CA stock | `CNQ.TO` | — | 3.11 | — | — |
| CDR | `WDC.TO` | — | 0.88 | — | — |
| CA stock | `CCO.TO` | — | 1.17 | — | — |
| CDR | `ASML.TO` | — | 1.00 | — | — |
| CDR | `ANET.TO` | — | 0.83 | — | — |
| CA stock | `GIB-A.TO` | — | 1.41 | — | — |
| CDR | `GEV.TO` | — | 0.85 | — | — |
| CA ETF | `HURA.TO` | — | 0.94 | — | — |
| CA ETF | `XGD.TO` | — | 0.85 | — | — |
| CA ETF | `MTRX.TO` | — | 0.89 | — | — |
| CA ETF | `RBOT.TO` | — | 0.94 | — | — |
| CA ETF | `XDRV.TO` | — | 0.75 | — | — |
| CA ETF | `CARS.TO` | — | 0.95 | — | — |
| CA ETF | `COPP.TO` | — | 0.66 | — | — |
| CA ETF | `XETM.TO` | — | 0.76 | — | — |
| CA stock | `MDA.TO` | — | 1.37 | — | — |
| CA stock | `NTR.TO` | — | 1.55 | — | — |
| CA stock | `ASTL.TO` | — | 1.01 | — | — |
| CA stock | `BDT.TO` | — | 0.99 | — | — |
| CA stock | `PNG.V` | — | 0.86 | — | — |
| CA stock | `CGY.TO` | — | 0.99 | — | — |
| CA ETF | `ORBX.TO` | — | 1.00 | — | — |
| US leveraged | `SOXL` | 1.60 | 1.60 | — | — |
| US leveraged | `URAA` | 1.15 | 1.15 | — | — |
| US leveraged | `COPZ` | 1.22 | 1.22 | — | — |
| US leveraged | `NVDL` | 1.36 | 1.36 | — | — |
| US leveraged | `AAPU` | 1.23 | 1.23 | — | — |
| US leveraged | `MSFU` | 1.28 | 1.28 | — | — |
| US leveraged | `METU` | 1.26 | 1.26 | — | — |
| US leveraged | `GGLL` | 1.40 | 1.40 | — | — |
| US leveraged | `NFXL` | 1.09 | 1.09 | — | — |
| US leveraged | `AMZU` | 1.23 | 1.23 | — | — |
| US leveraged | `TSLL` | 1.10 | 1.10 | — | — |
| US leveraged | `BRKU` | — | 1.54 | — | — |
| US leveraged | `ELIL` | 1.28 | 1.28 | — | — |
| US leveraged | `COTG` | 1.15 | 1.15 | — | — |
| US leveraged | `AVGC` | 1.28 | 1.28 | — | — |
| CA ETF | `SGRD.TO` | — | 0.62 | — | — |
