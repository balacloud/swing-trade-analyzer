# Data source audit: truth-free checks (2026-11-19)

Plan: `docs/claude/design/DATA_SOURCE_TESTING_PLAN_DAY126.md` step 1. Script: `backend/backtest/audit_data_sources.py`.
Checks C2 fresh, C4 integrity, C5 jumps, C6 history, C8 tab honest, C9 cross-source. **Not yet checked (needs IBKR, step 2): identity, close accuracy vs broker, volume vs broker.**
"STA uses" = the first source in the real chain that returned data. ✅ pass ⚠️ warn ❌ fail — not applicable.

## Matrix

| Class | Ticker | STA uses | Bars | C2 | C4 | C5 | C6 | C8 | C9 |
|---|---|---|---|---|---|---|---|---|---|
| US stock | `CAT` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `BRK-B` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `GOOGL` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `JPM` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `JNJ` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA stock | `RY.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA stock | `CNR.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA stock | `ATD.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA stock | `CNQ.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CSU.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA ETF | `HXQ.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA ETF | `VFV.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA ETF | `XEQT.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA ETF | `XCHP.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA ETF | `FINN.NE` | yfinance | 503 | ⚠️ | ❌ | ✅ | ✅ | ❌ | — |
| CDR | `WDC.TO` | yfinance | 135 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | — |
| US stock | `GEV` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `TSM` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `ETN` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `VRT` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA stock | `CCO.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CDR | `ASML.TO` | yfinance | 280 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CDR | `ANET.TO` | yfinance | 229 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | — |
| US stock | `CEG` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `ALAB` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `NVDA` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `AVGO` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `KEYS` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CDR | `MU.TO` | yfinance | 277 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA stock | `GIB-A.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| US stock | `MRVL` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `ONTO` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `CAMT` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `AMD` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `ORCL` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| US stock | `FCX` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `QCOM` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CDR | `SNDK.TO` | yfinance | 135 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CDR | `GEV.TO` | yfinance | 229 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | — |
| CDR | `AVGO.TO` | yfinance | 229 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CDR | `AMD.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA ETF | `HURA.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XGD.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `MTRX.TO` | yfinance | 211 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | — |
| CA ETF | `ORBX.TO` | yfinance | 141 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | — |
| CA ETF | `RBOT.TO` | yfinance | 502 | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | — |
| CA ETF | `XDRV.TO` | yfinance | 503 | ⚠️ | ❌ | ✅ | ✅ | ❌ | — |
| CA ETF | `CARS.TO` | yfinance | 502 | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | — |
| CA ETF | `COPP.TO` | yfinance | 503 | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | — |
| US ETF | `UFO` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `QTUM` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US ETF | `BOTZ` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `DRIV` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `GDX` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `DRAM` | yfinance | 161 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA ETF | `XETM.TO` | yfinance | 210 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | — |
| US ETF | `SETM` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `SMH` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `GRID` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `URA` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `AIPO` | yfinance | 334 | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| US ETF | `COPX` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `SOXX` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA ETF | `SGRD.TO` | yfinance | 148 | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ | — |
| US leveraged | `SOXL` | yfinance | 502 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| CA leveraged | `SOXL.NE` | yfinance | 315 | ⚠️ | ❌ | ⚠️ | ✅ | ❌ | ✅ |
| CA stock | `MDA.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `NTR.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `ASTL.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `BDT.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `PNG.V` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CGY.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | — |
| US leveraged | `QPUX` | yfinance | 325 | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ | ❌ |
| US leveraged | `DRAL` | yfinance | 104 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ❌ |
| US leveraged | `SPCL` | yfinance | 158 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `URAA` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `UBOT` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `COPZ` | twelvedata | 193 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CA leveraged | `GDXU.TO` | yfinance | 503 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US stock | `AAPL` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `MSFT` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `META` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `NFLX` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `AMZN` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `TSLA` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `HD` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `V` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `LLY` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `ABBV` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `WMT` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `COST` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `PG` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `XOM` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `CVX` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| US stock | `COP` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `LIN` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `NEM` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `GE` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `RTX` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `NEE` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `SO` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `DUK` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `WELL` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `PLD` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `EQIX` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `NVDL` | twelvedata | 504 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `AAPU` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `MSFU` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `METU` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `GGLL` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `NFXL` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `AMZU` | yfinance | 502 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `TSLL` | yfinance | 502 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `BRKU` | yfinance | 487 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `ELIL` | yfinance | 416 | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| US leveraged | `COTG` | yfinance | 296 | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| US leveraged | `AVGC` | yfinance | 101 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |

## Verdict per class

- **US stock** (47): no failures; warnings: CAT C2, CAT C6, BRK-B C2, BRK-B C6, BRK-B C8, GOOGL C2, GOOGL C6, GOOGL C8, JPM C2, JPM C6, JPM C8, JNJ C2, JNJ C6, JNJ C8, GEV C2, GEV C6, TSM C2, TSM C6, ETN C2, ETN C6, VRT C2, VRT C6, VRT C8, CEG C2, CEG C6, ALAB C2, ALAB C6, ALAB C8, NVDA C2, NVDA C6, NVDA C8, AVGO C2, AVGO C6, AVGO C8, KEYS C2, KEYS C6, KEYS C8, MRVL C2, MRVL C6, MRVL C8, ONTO C2, ONTO C6, CAMT C2, CAMT C6, AMD C2, AMD C6, ORCL C2, ORCL C6, ORCL C9, FCX C2, FCX C6, FCX C8, QCOM C2, QCOM C6, QCOM C8, AAPL C2, AAPL C6, AAPL C8, MSFT C2, MSFT C6, MSFT C8, META C2, META C6, META C8, NFLX C2, NFLX C6, AMZN C2, AMZN C6, TSLA C2, TSLA C6, HD C2, HD C6, HD C8, V C2, V C6, V C8, LLY C2, LLY C6, LLY C8, ABBV C2, ABBV C6, ABBV C8, WMT C2, WMT C6, WMT C8, COST C2, COST C6, PG C2, PG C6, PG C8, XOM C2, XOM C6, CVX C2, CVX C6, CVX C9, COP C2, COP C6, LIN C2, LIN C6, NEM C2, NEM C6, GE C2, GE C6, RTX C2, RTX C6, NEE C2, NEE C6, NEE C8, SO C2, SO C6, SO C8, DUK C2, DUK C6, DUK C8, WELL C2, WELL C6, WELL C8, PLD C2, PLD C6, EQIX C2, EQIX C6
- **CA stock** (13): no failures; warnings: RY.TO C2, CNR.TO C2, ATD.TO C2, CNQ.TO C2, CSU.TO C2, CCO.TO C2, GIB-A.TO C2, MDA.TO C2, NTR.TO C2, ASTL.TO C2, BDT.TO C2, PNG.V C2, CGY.TO C2
- **CA ETF** (15): FAILS: FINN.NE C4, FINN.NE C8, XDRV.TO C4, XDRV.TO C8; warnings: HXQ.TO C2, VFV.TO C2, XEQT.TO C2, XCHP.TO C2, FINN.NE C2, HURA.TO C2, XGD.TO C2, MTRX.TO C2, MTRX.TO C6, ORBX.TO C2, ORBX.TO C6, RBOT.TO C2, RBOT.TO C4, XDRV.TO C2, CARS.TO C2, CARS.TO C4, COPP.TO C2, COPP.TO C4, XETM.TO C2, XETM.TO C6, SGRD.TO C2, SGRD.TO C4, SGRD.TO C6
- **CDR** (8): no failures; warnings: WDC.TO C2, WDC.TO C6, ASML.TO C2, ANET.TO C2, ANET.TO C6, MU.TO C2, SNDK.TO C2, SNDK.TO C6, GEV.TO C2, GEV.TO C6, AVGO.TO C2, AVGO.TO C6, AMD.TO C2
- **US ETF** (13): no failures; warnings: UFO C2, UFO C6, UFO C8, QTUM C2, QTUM C6, QTUM C9, QTUM C8, BOTZ C2, BOTZ C6, BOTZ C8, DRIV C2, DRIV C6, DRIV C8, GDX C2, GDX C6, GDX C8, DRAM C2, DRAM C6, DRAM C8, SETM C2, SETM C6, SETM C8, SMH C2, SMH C6, GRID C2, GRID C6, URA C2, URA C6, AIPO C2, AIPO C8, COPX C2, COPX C6, COPX C8, SOXX C2, SOXX C6, SOXX C8
- **US leveraged** (19): FAILS: QPUX C9, DRAL C9; warnings: SOXL C2, SOXL C5, SOXL C6, SOXL C9, SOXL C8, QPUX C2, QPUX C5, QPUX C8, DRAL C2, DRAL C6, DRAL C8, SPCL C2, SPCL C5, SPCL C6, SPCL C8, URAA C2, URAA C6, URAA C8, UBOT C2, UBOT C6, COPZ C2, COPZ C6, NVDL C2, NVDL C6, AAPU C2, AAPU C6, AAPU C9, AAPU C8, MSFU C2, MSFU C6, MSFU C8, METU C2, METU C6, METU C9, METU C8, GGLL C2, GGLL C6, GGLL C9, GGLL C8, NFXL C2, NFXL C6, NFXL C8, AMZU C2, AMZU C6, AMZU C9, AMZU C8, TSLL C2, TSLL C5, TSLL C6, TSLL C9, TSLL C8, BRKU C2, BRKU C4, BRKU C6, BRKU C9, BRKU C8, ELIL C2, ELIL C8, COTG C2, COTG C8, AVGC C2, AVGC C6, AVGC C8
- **CA leveraged** (2): FAILS: SOXL.NE C4, SOXL.NE C8; warnings: SOXL.NE C2, SOXL.NE C5, GDXU.TO C2

## Every finding (warn and fail), with evidence

**CAT** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': "ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) ("}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**BRK-B** (US stock, dash symbol); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': "ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) ("}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**GOOGL** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 502}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open || tradier: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars) || tradier: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**JPM** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': "ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) ("}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**JNJ** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': "ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) ("}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**RY.TO** (CA stock); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**CNR.TO** (CA stock); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**ATD.TO** (CA stock); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**CNQ.TO** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**CSU.TO** (CA stock, CAD 3,000+); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**HXQ.TO** (CA ETF); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**VFV.TO** (CA ETF); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**XEQT.TO** (CA ETF); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**XCHP.TO** (CA ETF); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**FINN.NE** (CA ETF); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ❌ C4: yfinance: flat zero-volume 1%; bad OHLC rows 22; zero-volume in last 5: 0
- ❌ C8: tab says yfinance / 503 rows / cached but yfinance fails C4: the tab shows no warning

**WDC.TO** (CDR); sources {'yfinance': 135}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 134 bars from 2026-05-08

**GEV** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': "ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) ("}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**TSM** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**ETN** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**VRT** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**CCO.TO** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**ASML.TO** (CDR); sources {'yfinance': 280}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**ANET.TO** (CDR); sources {'yfinance': 229}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 228 bars from 2025-12-22

**CEG** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**ALAB** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**NVDA** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**AVGO** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**KEYS** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**MU.TO** (CDR); sources {'yfinance': 277, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**GIB-A.TO** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**MRVL** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**ONTO** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**CAMT** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**AMD** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**ORCL** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: twelvedata vs yfinance: max close diff 0.32%, volume x0.99

**FCX** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**QCOM** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SNDK.TO** (CDR, short history); sources {'yfinance': 135, 'eodhd': 135}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 134 bars from 2026-05-08

**GEV.TO** (CDR); sources {'yfinance': 229}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 228 bars from 2025-12-22

**AVGO.TO** (CDR); sources {'yfinance': 229, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 228 bars from 2025-12-22; starts 33 days after eodhd (2025-11-19, 251 bars)

**AMD.TO** (CDR); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**HURA.TO** (CA ETF); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**XGD.TO** (CA ETF); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**MTRX.TO** (CA ETF); sources {'yfinance': 211}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 210 bars from 2026-01-20

**ORBX.TO** (CA ETF); sources {'yfinance': 141}
- ⚠️ C2: yfinance: last bar 2026-11-18, expected 2026-11-19 (1 session behind)
- ⚠️ C6: yfinance: 141 bars from 2026-04-29

**RBOT.TO** (CA ETF); sources {'yfinance': 502}
- ⚠️ C2: yfinance: last bar 2026-11-18, expected 2026-11-19 (1 session behind)
- ⚠️ C4: yfinance: flat zero-volume 2%; bad OHLC rows 0; zero-volume in last 5: 0

**XDRV.TO** (CA ETF); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ❌ C4: yfinance: flat zero-volume 83%; bad OHLC rows 0; zero-volume in last 5: 3
- ❌ C8: tab says yfinance / 503 rows / cached but yfinance fails C4: the tab shows no warning

**CARS.TO** (CA ETF); sources {'yfinance': 502}
- ⚠️ C2: yfinance: last bar 2026-11-18, expected 2026-11-19 (1 session behind)
- ⚠️ C4: yfinance: flat zero-volume 12%; bad OHLC rows 0; zero-volume in last 5: 1

**COPP.TO** (CA ETF); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ⚠️ C4: yfinance: flat zero-volume 2%; bad OHLC rows 0; zero-volume in last 5: 0

**UFO** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**QTUM** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.37%, volume x1.01
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**BOTZ** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**DRIV** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar 2026-11-18, expected 2026-11-19 (1 session behind) || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 5 days after twelvedata (2024-11-14, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**GDX** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**DRAM** (US ETF); sources {'twelvedata': 161, 'yfinance': 161, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: twelvedata: 160 bars from 2026-04-02 || yfinance: 160 bars from 2026-04-02
- ⚠️ C8: tab says yfinance / 160 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**XETM.TO** (CA ETF); sources {'yfinance': 210}
- ⚠️ C2: yfinance: last bar 2026-11-18, expected 2026-11-19 (1 session behind)
- ⚠️ C6: yfinance: 210 bars from 2026-01-20

**SETM** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SMH** (US ETF, no fundamentals); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**GRID** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**URA** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**AIPO** (US ETF); sources {'twelvedata': 334, 'yfinance': 334, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C8: tab says yfinance / 333 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**COPX** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SOXX** (US ETF); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SGRD.TO** (CA ETF); sources {'yfinance': 148}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ⚠️ C4: yfinance: flat zero-volume 3%; bad OHLC rows 0; zero-volume in last 5: 1
- ⚠️ C6: yfinance: 147 bars from 2026-04-21

**SOXL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C5: twelvedata: 2025-04-09 +55%: also in yfinance (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2025-04-09 +55%: also in twelvedata (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.86%, volume x1.02
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SOXL.NE** (CA leveraged, known bad: Cboe Canada only); sources {'yfinance': 315, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open
- ❌ C4: yfinance: flat zero-volume 100%; bad OHLC rows 0; zero-volume in last 5: 5
- ⚠️ C5: yfinance: 2026-05-25 -67%: also in eodhd (real move, or unadjusted everywhere: needs IBKR)
- ❌ C8: tab says yfinance / 314 rows / cached but yfinance fails C4: the tab shows no warning

**MDA.TO** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**NTR.TO** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**ASTL.TO** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**BDT.TO** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**PNG.V** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**CGY.TO** (CA stock); sources {'yfinance': 503}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**QPUX** (US leveraged, 1:3 reverse split 2026-03-23); sources {'twelvedata': 325, 'yfinance': 325, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C5: twelvedata: 2026-05-21 +48%: also in yfinance (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-05-21 +48%: also in twelvedata (real move, or unadjusted everywhere: needs IBKR)
- ❌ C9: yfinance vs twelvedata: max close diff 3.98%, volume x1.02
- ⚠️ C8: tab says yfinance / 324 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**DRAL** (US leveraged, ~100 days); sources {'twelvedata': 104, 'yfinance': 104, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: twelvedata: 103 bars from 2026-06-25 || yfinance: 103 bars from 2026-06-25
- ❌ C9: yfinance vs twelvedata: max close diff 3.33%, volume x1.06
- ⚠️ C8: tab says yfinance / 103 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SPCL** (US leveraged, ~154 days); sources {'twelvedata': 153, 'yfinance': 158, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar 2026-11-18, expected 2026-11-19 (1 session behind) || yfinance: last bar is today and the session is still open
- ⚠️ C5: twelvedata: 2026-06-12 +57%: also in yfinance (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-06-12 +57%: also in twelvedata (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: twelvedata: 153 bars from 2026-04-14; starts 6 days after yfinance (2026-04-08, 158 bars) || yfinance: 157 bars from 2026-04-08
- ⚠️ C8: tab says yfinance / 157 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**URAA** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar 2026-11-18, expected 2026-11-19 (1 session behind) || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 5 days after twelvedata (2024-11-14, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**UBOT** (US leveraged, control); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar 2026-11-18, expected 2026-11-19 (1 session behind) || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 5 days after twelvedata (2024-11-14, 504 bars)

**COPZ** (US leveraged); sources {'twelvedata': 193, 'yfinance': 192, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar 2026-11-18, expected 2026-11-19 (1 session behind) || yfinance: last bar is today and the session is still open
- ⚠️ C6: twelvedata: 193 bars from 2024-07-10 || yfinance: 191 bars from 2026-02-18; starts 588 days after twelvedata (2024-07-10, 193 bars)

**GDXU.TO** (CA leveraged, control (3:1 split 2026-05-25)); sources {'yfinance': 503, 'eodhd': 251}
- ⚠️ C2: yfinance: last bar is today and the session is still open

**AAPL** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**MSFT** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**META** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**NFLX** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': "ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) ("}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**AMZN** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**TSLA** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**HD** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**V** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**LLY** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**ABBV** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**WMT** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**COST** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**PG** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**XOM** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**CVX** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: twelvedata vs yfinance: max close diff 0.83%, volume x0.99

**COP** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**LIN** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**NEM** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**GE** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**RTX** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**NEE** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SO** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 502 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**DUK** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**WELL** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**PLD** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**EQIX** (US stock); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**NVDL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**AAPU** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.45%, volume x1.01
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**MSFU** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**METU** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.64%, volume x1.01
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**GGLL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.57%, volume x1.01
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**NFXL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**AMZU** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.71%, volume x1.01
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**TSLL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 502, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C5: twelvedata: 2025-04-09 +45%: also in yfinance (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2025-04-09 +45%: also in twelvedata (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: yfinance: 501 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.50%, volume x1.01
- ⚠️ C8: tab says yfinance / 501 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**BRKU** (US leveraged); sources {'twelvedata': 492, 'yfinance': 487, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C4: twelvedata: flat zero-volume 1%; bad OHLC rows 0; zero-volume in last 5: 5
- ⚠️ C6: yfinance: 486 bars from 2024-12-11; starts 7 days after twelvedata (2024-12-04, 492 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.33%, volume xnan
- ⚠️ C8: tab says yfinance / 486 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**ELIL** (US leveraged); sources {'twelvedata': 417, 'yfinance': 416, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C8: tab says yfinance / 415 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**COTG** (US leveraged); sources {'twelvedata': 296, 'yfinance': 296, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar is today and the session is still open || yfinance: last bar is today and the session is still open
- ⚠️ C8: tab says yfinance / 295 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**AVGC** (US leveraged); sources {'twelvedata': 100, 'yfinance': 101, 'tradier': 'ERROR: [tradier] Circuit breaker OPEN'}
- ⚠️ C2: twelvedata: last bar 2026-11-18, expected 2026-11-19 (1 session behind) || yfinance: last bar is today and the session is still open
- ⚠️ C6: twelvedata: 100 bars from 2026-06-30 || yfinance: 100 bars from 2026-06-30
- ⚠️ C8: tab says yfinance / 100 rows / cached; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)


## Source errors (a source that could not serve a ticker)

- `CAT`: tradier: ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) (
- `BRK-B`: tradier: ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) (
- `JPM`: tradier: ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) (
- `JNJ`: tradier: ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) (
- `GEV`: tradier: ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) (
- `TSM`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `ETN`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `VRT`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `CEG`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `ALAB`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `NVDA`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `AVGO`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `KEYS`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `MRVL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `ONTO`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `CAMT`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `AMD`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `ORCL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `FCX`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `QCOM`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `UFO`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `QTUM`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `BOTZ`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `DRIV`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `GDX`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `DRAM`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `SETM`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `SMH`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `GRID`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `URA`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `AIPO`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `COPX`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `SOXX`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `SOXL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `QPUX`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `DRAL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `SPCL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `URAA`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `UBOT`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `COPZ`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `AAPL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `MSFT`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `META`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `NFLX`: tradier: ERROR: [tradier] HTTPSConnectionPool(host='api.tradier.com', port=443): Read timed out. (read timeout=15) (
- `AMZN`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `TSLA`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `HD`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `V`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `LLY`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `ABBV`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `WMT`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `COST`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `PG`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `XOM`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `CVX`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `COP`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `LIN`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `NEM`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `GE`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `RTX`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `NEE`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `SO`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `DUK`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `WELL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `PLD`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `EQIX`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `NVDL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `AAPU`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `MSFU`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `METU`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `GGLL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `NFXL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `AMZU`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `TSLL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `BRKU`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `ELIL`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `COTG`: tradier: ERROR: [tradier] Circuit breaker OPEN
- `AVGC`: tradier: ERROR: [tradier] Circuit breaker OPEN

## Known limits of this audit (read before trusting the matrix)

- **Agreement is not accuracy.** If two sources share the same defect they agree (SOXL.NE on Yahoo and EODHD are both close-only), so C9 passes. Only the IBKR truth step (step 2) can settle those; C5 marks them "needs IBKR".
- **"STA uses" comes from the tab.** The tab's source was read right after this script spent Twelve Data credits on the same key, so some "fell through to Yahoo" results may be partly self-inflicted. Either way, every source in the chain is graded, because any of them can serve a request.
- **Canada has one source for most tickers.** Only the tickers listed with EODHD had a second opinion (free quota: 20 calls a day). The rest show `—` in C9, which means unchecked, not clean.
- **Freshness ignores market holidays** (it uses weekdays).
- **Tradier is not dividend-adjusted**, so its old closes differ slightly from Yahoo's on ex-dividend days; the close check only looks at the last 20 sessions.
- Not run: identity/currency (C1), close accuracy vs the broker (C3), volume vs the broker (C7), fundamentals and classification (C10), Alpha Vantage.

