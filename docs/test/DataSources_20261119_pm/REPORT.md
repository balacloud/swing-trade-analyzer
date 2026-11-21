# Data source audit: truth-free checks (2026-11-19)

Plan: `docs/claude/design/DATA_SOURCE_TESTING_PLAN_DAY126.md` step 1. Script: `backend/backtest/audit_data_sources.py`.
Checks C2 fresh, C4 integrity, C5 jumps, C6 history, C8 tab honest, C9 cross-source. **Not yet checked (needs IBKR, step 2): identity, close accuracy vs broker, volume vs broker.**
"STA uses" = the first source in the real chain that returned data. ✅ pass ⚠️ warn ❌ fail — not applicable.

## Matrix

| Class | Ticker | STA uses | Bars | C2 | C4 | C5 | C6 | C8 | C9 |
|---|---|---|---|---|---|---|---|---|---|
| US stock | `CAT` | twelvedata | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `BRK-B` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `GOOGL` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `JPM` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `JNJ` | yfinance | 501 | ✅ | ❌ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA stock | `RY.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CNR.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `ATD.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CNQ.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CSU.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `HXQ.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `VFV.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XEQT.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XCHP.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `FINN.NE` | yfinance | 503 | ✅ | ❌ | ✅ | ✅ | ❌ | — |
| CDR | `WDC.TO` | yfinance | 135 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| US stock | `GEV` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `TSM` | yfinance | 501 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `ETN` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `VRT` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA stock | `CCO.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CDR | `ASML.TO` | yfinance | 280 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CDR | `ANET.TO` | yfinance | 229 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| US stock | `CEG` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `ALAB` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `NVDA` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `AVGO` | twelvedata | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `KEYS` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CDR | `MU.TO` | yfinance | 277 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA stock | `GIB-A.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| US stock | `MRVL` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `ONTO` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `CAMT` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `AMD` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `ORCL` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `FCX` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `QCOM` | tradier | 502 | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| CDR | `SNDK.TO` | yfinance | 135 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CDR | `GEV.TO` | yfinance | 229 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CDR | `AVGO.TO` | yfinance | 229 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CDR | `AMD.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA ETF | `HURA.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XGD.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `MTRX.TO` | yfinance | 211 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CA ETF | `ORBX.TO` | yfinance | 142 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CA ETF | `RBOT.TO` | yfinance | 503 | ✅ | ⚠️ | ✅ | ✅ | ✅ | — |
| CA ETF | `XDRV.TO` | yfinance | 503 | ✅ | ❌ | ✅ | ✅ | ❌ | — |
| CA ETF | `CARS.TO` | yfinance | 502 | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | — |
| CA ETF | `COPP.TO` | yfinance | 503 | ✅ | ⚠️ | ✅ | ✅ | ✅ | — |
| US ETF | `UFO` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `QTUM` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `BOTZ` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `DRIV` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `GDX` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `DRAM` | tradier | 161 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA ETF | `XETM.TO` | yfinance | 211 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| US ETF | `SETM` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `SMH` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `GRID` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `URA` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `AIPO` | tradier | 334 | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| US ETF | `COPX` | yfinance | 501 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US ETF | `SOXX` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA ETF | `SGRD.TO` | yfinance | 148 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | — |
| US leveraged | `SOXL` | yfinance | 501 | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| CA leveraged | `SOXL.NE` | yfinance | 315 | ✅ | ❌ | ⚠️ | ✅ | ❌ | ✅ |
| CA stock | `MDA.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `NTR.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `ASTL.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `BDT.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `PNG.V` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CGY.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| US leveraged | `QPUX` | tradier | 325 | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ |
| US leveraged | `DRAL` | yfinance | 104 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ❌ |
| US leveraged | `SPCL` | tradier | 158 | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `URAA` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `UBOT` | yfinance | 501 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `COPZ` | tradier | 192 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| CA leveraged | `GDXU.TO` | yfinance | 503 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US stock | `AAPL` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `MSFT` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `META` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `NFLX` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `AMZN` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `TSLA` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `HD` | yfinance | 501 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `V` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `LLY` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `ABBV` | yfinance | 501 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `WMT` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `COST` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `PG` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `XOM` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `CVX` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `COP` | yfinance | 501 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `LIN` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `NEM` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `GE` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `RTX` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `NEE` | tradier | 502 | ✅ | ❌ | ✅ | ⚠️ | ❌ | ✅ |
| US stock | `SO` | yfinance | 501 | ✅ | ❌ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `DUK` | tradier | 502 | ✅ | ❌ | ✅ | ⚠️ | ❌ | ⚠️ |
| US stock | `WELL` | tradier | 502 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `PLD` | yfinance | 501 | ✅ | ❌ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `EQIX` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `NVDL` | tradier | 502 | ✅ | ✅ | ❌ | ⚠️ | ❌ | ✅ |
| US leveraged | `AAPU` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `MSFU` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `METU` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `GGLL` | yfinance | 501 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `NFXL` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `AMZU` | tradier | 502 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `TSLL` | yfinance | 501 | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `BRKU` | tradier | 487 | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US leveraged | `ELIL` | tradier | 417 | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| US leveraged | `COTG` | yfinance | 296 | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| US leveraged | `AVGC` | tradier | 101 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |

## Verdict per class

- **US stock** (47): FAILS: JNJ C4, NEE C4, NEE C8, SO C4, DUK C4, DUK C8, PLD C4; warnings: CAT C4, CAT C6, BRK-B C6, BRK-B C8, GOOGL C6, GOOGL C8, JPM C6, JPM C8, JNJ C6, JNJ C8, GEV C6, GEV C8, TSM C4, TSM C6, TSM C8, ETN C6, ETN C9, ETN C8, VRT C6, VRT C8, CEG C6, CEG C8, ALAB C6, ALAB C8, NVDA C6, NVDA C9, NVDA C8, AVGO C6, KEYS C6, KEYS C8, MRVL C6, MRVL C8, ONTO C6, ONTO C8, CAMT C6, CAMT C8, AMD C6, AMD C9, AMD C8, ORCL C6, ORCL C8, FCX C6, FCX C8, QCOM C8, AAPL C6, AAPL C8, MSFT C6, MSFT C8, META C6, META C8, NFLX C6, NFLX C8, AMZN C6, AMZN C8, TSLA C6, TSLA C8, HD C4, HD C6, HD C8, V C6, V C8, LLY C6, LLY C8, ABBV C4, ABBV C6, ABBV C8, WMT C4, WMT C6, WMT C8, COST C6, COST C8, PG C6, PG C8, XOM C4, XOM C6, XOM C9, XOM C8, CVX C4, CVX C6, CVX C9, CVX C8, COP C4, COP C6, COP C9, COP C8, LIN C6, LIN C8, NEM C4, NEM C6, NEM C8, GE C6, GE C8, RTX C4, RTX C6, RTX C8, NEE C6, SO C6, SO C9, SO C8, DUK C6, DUK C9, WELL C4, WELL C6, WELL C9, WELL C8, PLD C6, PLD C8, EQIX C6, EQIX C9, EQIX C8
- **CA stock** (13): no failures
- **CA ETF** (15): FAILS: FINN.NE C4, FINN.NE C8, XDRV.TO C4, XDRV.TO C8; warnings: MTRX.TO C6, ORBX.TO C6, RBOT.TO C4, CARS.TO C2, CARS.TO C4, COPP.TO C4, XETM.TO C6, SGRD.TO C4, SGRD.TO C6
- **CDR** (8): no failures; warnings: WDC.TO C6, ANET.TO C6, SNDK.TO C6, GEV.TO C6, AVGO.TO C6
- **US ETF** (13): no failures; warnings: UFO C6, UFO C8, QTUM C6, QTUM C8, BOTZ C6, BOTZ C8, DRIV C6, DRIV C8, GDX C4, GDX C6, GDX C8, DRAM C6, DRAM C8, SETM C6, SETM C8, SMH C6, SMH C8, GRID C6, GRID C8, URA C4, URA C6, URA C8, AIPO C8, COPX C4, COPX C6, COPX C8, SOXX C6, SOXX C8
- **US leveraged** (19): FAILS: QPUX C5, QPUX C8, DRAL C9, NVDL C5, NVDL C8; warnings: SOXL C5, SOXL C6, SOXL C8, DRAL C6, DRAL C8, SPCL C5, SPCL C6, SPCL C9, SPCL C8, URAA C4, URAA C6, URAA C8, UBOT C4, UBOT C6, UBOT C8, COPZ C6, COPZ C8, NVDL C6, AAPU C6, AAPU C8, MSFU C6, MSFU C8, METU C6, METU C8, GGLL C6, GGLL C8, NFXL C6, NFXL C8, AMZU C6, AMZU C8, TSLL C5, TSLL C6, TSLL C8, BRKU C4, BRKU C6, BRKU C9, BRKU C8, ELIL C8, COTG C8, AVGC C6, AVGC C8
- **CA leveraged** (2): FAILS: SOXL.NE C4, SOXL.NE C8; warnings: SOXL.NE C5

## Every finding (warn and fail), with evidence

**CAT** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**BRK-B** (US stock, dash symbol); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**GOOGL** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**JPM** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**JNJ** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 4; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters); a source later in the chain fails: tradier C4

**FINN.NE** (CA ETF); sources {'yfinance': 503}
- ❌ C4: yfinance: flat zero-volume 1%; bad OHLC rows 22; zero-volume in last 5: 0
- ❌ C8: tab says yfinance / 503 rows / just_fetched but yfinance fails C4: the tab shows no warning

**WDC.TO** (CDR); sources {'yfinance': 135}
- ⚠️ C6: yfinance: 135 bars from 2026-05-08

**GEV** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**TSM** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**ETN** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: tradier vs twelvedata: max close diff 0.31%, volume x0.96 | tradier vs yfinance: max close diff 0.31%, volume x1.00
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**VRT** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**ANET.TO** (CDR); sources {'yfinance': 229}
- ⚠️ C6: yfinance: 229 bars from 2025-12-22

**CEG** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**ALAB** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**NVDA** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.01%, volume x0.70 (volume ratio outside 0.8-1.25) | yfinance vs tradier: max close diff 0.00%, volume x1.00
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**AVGO** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)

**KEYS** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**MRVL** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**ONTO** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**CAMT** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**AMD** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: tradier vs twelvedata: max close diff 0.01%, volume x0.69 (volume ratio outside 0.8-1.25) | tradier vs yfinance: max close diff 0.00%, volume x1.00
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**ORCL** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**FCX** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**QCOM** (US stock); sources {'twelvedata': 'ERROR: [twelvedata] HTTP 429 - rate limited (ticker=QCOM)', 'yfinance': 501, 'tradier': 502}
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says yfinance first, so STA fell through to tradier (every source in the chain matters)

**SNDK.TO** (CDR, short history); sources {'yfinance': 135, 'eodhd': 135}
- ⚠️ C6: yfinance: 135 bars from 2026-05-08

**GEV.TO** (CDR); sources {'yfinance': 229}
- ⚠️ C6: yfinance: 229 bars from 2025-12-22

**AVGO.TO** (CDR); sources {'yfinance': 229}
- ⚠️ C6: yfinance: 229 bars from 2025-12-22

**MTRX.TO** (CA ETF); sources {'yfinance': 211}
- ⚠️ C6: yfinance: 211 bars from 2026-01-20

**ORBX.TO** (CA ETF); sources {'yfinance': 142}
- ⚠️ C6: yfinance: 142 bars from 2026-04-29

**RBOT.TO** (CA ETF); sources {'yfinance': 503}
- ⚠️ C4: yfinance: flat zero-volume 2%; bad OHLC rows 0; zero-volume in last 5: 0

**XDRV.TO** (CA ETF); sources {'yfinance': 503}
- ❌ C4: yfinance: flat zero-volume 82%; bad OHLC rows 0; zero-volume in last 5: 2
- ❌ C8: tab says yfinance / 503 rows / just_fetched but yfinance fails C4: the tab shows no warning

**CARS.TO** (CA ETF); sources {'yfinance': 502}
- ⚠️ C2: yfinance: last bar 2026-11-18, expected 2026-11-19 (1 session behind)
- ⚠️ C4: yfinance: flat zero-volume 12%; bad OHLC rows 0; zero-volume in last 5: 1

**COPP.TO** (CA ETF); sources {'yfinance': 503}
- ⚠️ C4: yfinance: flat zero-volume 2%; bad OHLC rows 0; zero-volume in last 5: 0

**UFO** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**QTUM** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**BOTZ** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**DRIV** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**GDX** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**DRAM** (US ETF); sources {'twelvedata': 161, 'yfinance': 161, 'tradier': 161}
- ⚠️ C6: twelvedata: 161 bars from 2026-04-02 || yfinance: 161 bars from 2026-04-02 || tradier: 161 bars from 2026-04-02
- ⚠️ C8: tab says tradier / 161 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**XETM.TO** (CA ETF); sources {'yfinance': 211}
- ⚠️ C6: yfinance: 211 bars from 2026-01-20

**SETM** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**SMH** (US ETF, no fundamentals); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**GRID** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**URA** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 2; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**AIPO** (US ETF); sources {'twelvedata': 334, 'yfinance': 334, 'tradier': 334}
- ⚠️ C8: tab says tradier / 334 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**COPX** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 2; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SOXX** (US ETF); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**SGRD.TO** (CA ETF); sources {'yfinance': 148}
- ⚠️ C4: yfinance: flat zero-volume 3%; bad OHLC rows 0; zero-volume in last 5: 1
- ⚠️ C6: yfinance: 148 bars from 2026-04-21

**SOXL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C5: twelvedata: 2025-04-09 +55%: also in yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2025-04-09 +55%: also in twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2025-04-09 +55%: also in twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SOXL.NE** (CA leveraged, known bad: Cboe Canada only); sources {'yfinance': 315, 'eodhd': 251}
- ❌ C4: yfinance: flat zero-volume 100%; bad OHLC rows 0; zero-volume in last 5: 4
- ⚠️ C5: yfinance: 2026-05-25 -67%: also in eodhd (real move, or unadjusted everywhere: needs IBKR)
- ❌ C8: tab says yfinance / 314 rows / live but yfinance fails C4: the tab shows no warning

**QPUX** (US leveraged, 1:3 reverse split 2026-03-23); sources {'twelvedata': 325, 'yfinance': 325, 'tradier': 325}
- ❌ C5: twelvedata: 2026-05-21 +48%: also in yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-05-21 +48%: also in twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2026-03-20 -69%: ONLY here; twelvedata,yfinance are continuous -> tradier has a split error | 2026-05-21 +48%: also in twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ❌ C8: tab says tradier / 325 rows / just_fetched but tradier fails C5: the tab shows no warning

**DRAL** (US leveraged, ~100 days); sources {'twelvedata': 104, 'yfinance': 104, 'tradier': 104}
- ⚠️ C6: twelvedata: 104 bars from 2026-06-25 || yfinance: 104 bars from 2026-06-25 || tradier: 104 bars from 2026-06-25
- ❌ C9: yfinance vs twelvedata: max close diff 2.21%, volume x1.15 | yfinance vs tradier: max close diff 0.12%, volume x0.99
- ⚠️ C8: tab says yfinance / 104 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**SPCL** (US leveraged, ~154 days); sources {'twelvedata': 154, 'yfinance': 158, 'tradier': 158}
- ⚠️ C5: twelvedata: 2026-06-12 +57%: also in yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-06-12 +57%: also in twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2026-06-12 +57%: also in twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: twelvedata: 154 bars from 2026-04-14; starts 6 days after yfinance (2026-04-08, 158 bars); starts 6 days after tradier (2026-04-08, 158 bars) || yfinance: 158 bars from 2026-04-08 || tradier: 158 bars from 2026-04-08
- ⚠️ C9: tradier vs twelvedata: max close diff 0.62%, volume x1.08 | tradier vs yfinance: max close diff 0.06%, volume x1.02
- ⚠️ C8: tab says tradier / 158 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**URAA** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**UBOT** (US leveraged, control); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**COPZ** (US leveraged); sources {'twelvedata': 194, 'yfinance': 192, 'tradier': 192}
- ⚠️ C6: twelvedata: 194 bars from 2024-07-10 || yfinance: 192 bars from 2026-02-18; starts 588 days after twelvedata (2024-07-10, 194 bars) || tradier: 192 bars from 2026-02-18; starts 588 days after twelvedata (2024-07-10, 194 bars)
- ⚠️ C8: tab says tradier / 192 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**AAPL** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**MSFT** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**META** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**NFLX** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**AMZN** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**TSLA** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**HD** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**V** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**LLY** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**ABBV** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**WMT** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**COST** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**PG** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**XOM** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: tradier vs twelvedata: max close diff 0.63%, volume x0.96 | tradier vs yfinance: max close diff 0.63%, volume x1.00
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**CVX** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: tradier vs twelvedata: max close diff 0.03%, volume x0.93 | tradier vs yfinance: max close diff 0.83%, volume x1.00
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**COP** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.01%, volume x0.98 | yfinance vs tradier: max close diff 0.65%, volume x1.00
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**LIN** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**NEM** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**GE** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**RTX** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 2; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**NEE** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 4; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ❌ C8: tab says tradier / 502 rows / just_fetched but tradier fails C4: the tab shows no warning

**SO** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 4; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: yfinance vs twelvedata: max close diff 0.01%, volume x0.96 | yfinance vs tradier: max close diff 0.81%, volume x1.00
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters); a source later in the chain fails: tradier C4

**DUK** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 5; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: tradier vs twelvedata: max close diff 0.84%, volume x0.97 | tradier vs yfinance: max close diff 0.85%, volume x1.00
- ❌ C8: tab says tradier / 502 rows / just_fetched but tradier fails C4: the tab shows no warning

**WELL** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: tradier vs twelvedata: max close diff 0.34%, volume x0.94 | tradier vs yfinance: max close diff 0.34%, volume x1.00
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**PLD** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 4; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters); a source later in the chain fails: tradier C4

**EQIX** (US stock); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C9: tradier vs twelvedata: max close diff 0.51%, volume x0.97 | tradier vs yfinance: max close diff 0.50%, volume x1.00
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**NVDL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ❌ C5: tradier: 2026-06-25 +191%: ONLY here; twelvedata,yfinance are continuous -> tradier has a split error
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ❌ C8: tab says tradier / 502 rows / just_fetched but tradier fails C5: the tab shows no warning

**AAPU** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**MSFU** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**METU** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**GGLL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**NFXL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**AMZU** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says tradier / 502 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**TSLL** (US leveraged); sources {'twelvedata': 504, 'yfinance': 501, 'tradier': 502}
- ⚠️ C5: twelvedata: 2025-04-09 +45%: also in yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2025-04-09 +45%: also in twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2025-04-09 +45%: also in twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: yfinance: 501 bars from 2024-11-20; starts 5 days after twelvedata (2024-11-15, 504 bars) || tradier: 502 bars from 2024-11-19; starts 4 days after twelvedata (2024-11-15, 504 bars)
- ⚠️ C8: tab says yfinance / 501 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**BRKU** (US leveraged); sources {'twelvedata': 492, 'yfinance': 487, 'tradier': 487}
- ⚠️ C4: twelvedata: flat zero-volume 1%; bad OHLC rows 0; zero-volume in last 5: 5
- ⚠️ C6: yfinance: 487 bars from 2024-12-11; starts 7 days after twelvedata (2024-12-04, 492 bars) || tradier: 487 bars from 2024-12-11; starts 7 days after twelvedata (2024-12-04, 492 bars)
- ⚠️ C9: tradier vs twelvedata: max close diff 0.33%, volume xnan | tradier vs yfinance: max close diff 0.00%, volume x1.01
- ⚠️ C8: tab says tradier / 487 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**ELIL** (US leveraged); sources {'twelvedata': 417, 'yfinance': 416, 'tradier': 417}
- ⚠️ C8: tab says tradier / 417 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)

**COTG** (US leveraged); sources {'twelvedata': 296, 'yfinance': 296, 'tradier': 296}
- ⚠️ C8: tab says yfinance / 296 rows / just_fetched; the chain order says twelvedata first, so STA fell through to yfinance (every source in the chain matters)

**AVGC** (US leveraged); sources {'twelvedata': 101, 'yfinance': 101, 'tradier': 101}
- ⚠️ C6: twelvedata: 101 bars from 2026-06-30 || yfinance: 101 bars from 2026-06-30 || tradier: 101 bars from 2026-06-30
- ⚠️ C8: tab says tradier / 101 rows / just_fetched; the chain order says twelvedata first, so STA fell through to tradier (every source in the chain matters)


## Source errors (a source that could not serve a ticker)

- `QCOM`: twelvedata: ERROR: [twelvedata] HTTP 429 - rate limited (ticker=QCOM)

## Known limits of this audit (read before trusting the matrix)

- **Agreement is not accuracy.** If two sources share the same defect they agree (SOXL.NE on Yahoo and EODHD are both close-only), so C9 passes. Only the IBKR truth step (step 2) can settle those; C5 marks them "needs IBKR".
- **"STA uses" comes from the tab.** The tab's source was read right after this script spent Twelve Data credits on the same key, so some "fell through to Yahoo" results may be partly self-inflicted. Either way, every source in the chain is graded, because any of them can serve a request.
- **Canada has one source for most tickers.** Only the tickers listed with EODHD had a second opinion (free quota: 20 calls a day). The rest show `—` in C9, which means unchecked, not clean.
- **Freshness ignores market holidays** (it uses weekdays).
- **Tradier is not dividend-adjusted**, so its old closes differ slightly from Yahoo's on ex-dividend days; the close check only looks at the last 20 sessions.
- Not run: identity/currency (C1), close accuracy vs the broker (C3), volume vs the broker (C7), fundamentals and classification (C10), Alpha Vantage.

