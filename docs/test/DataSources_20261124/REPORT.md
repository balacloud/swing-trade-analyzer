# Data source audit: truth-free checks (2026-11-24)

Plan: `docs/claude/design/DATA_SOURCE_TESTING_PLAN_DAY126.md` step 1. Script: `backend/backtest/audit_data_sources.py`.
Checks C2 fresh, C4 integrity, C5 jumps, C6 history, C8 tab honest, C9 cross-source. **Not yet checked (needs IBKR, step 2): identity, close accuracy vs broker, volume vs broker.**
"STA uses" = the first source in the real chain that returned data. ✅ pass ⚠️ warn ❌ fail — not applicable.

## Matrix

| Class | Ticker | STA uses | Bars | C2 | C4 | C5 | C6 | C8 | C9 |
|---|---|---|---|---|---|---|---|---|---|
| US stock | `CAT` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `BRK-B` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `GOOGL` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `JPM` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `JNJ` | alpaca | 504 | ✅ | ❌ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| CA stock | `RY.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CNR.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `ATD.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CNQ.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CSU.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `HXQ.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `VFV.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XEQT.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XCHP.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `FINN.NE` | yfinance | 502 | ✅ | ❌ | ✅ | ✅ | ⚠️ | — |
| CDR | `WDC.TO` | yfinance | 138 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| US stock | `GEV` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `TSM` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `ETN` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `VRT` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CA stock | `CCO.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CDR | `ASML.TO` | yfinance | 283 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CDR | `ANET.TO` | yfinance | 232 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| US stock | `CEG` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `ALAB` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `NVDA` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `AVGO` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `KEYS` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CDR | `MU.TO` | yfinance | 280 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA stock | `GIB-A.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| US stock | `MRVL` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `ONTO` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `CAMT` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `AMD` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `ORCL` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `FCX` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `QCOM` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CDR | `SNDK.TO` | yfinance | 138 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CDR | `GEV.TO` | yfinance | 232 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CDR | `AVGO.TO` | yfinance | 232 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CDR | `AMD.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CA ETF | `HURA.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `XGD.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA ETF | `MTRX.TO` | yfinance | 214 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CA ETF | `ORBX.TO` | yfinance | 145 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| CA ETF | `RBOT.TO` | yfinance | 502 | ✅ | ⚠️ | ✅ | ✅ | ✅ | — |
| CA ETF | `XDRV.TO` | yfinance | 502 | ✅ | ❌ | ✅ | ✅ | ⚠️ | — |
| CA ETF | `CARS.TO` | yfinance | 502 | ✅ | ⚠️ | ✅ | ✅ | ✅ | — |
| CA ETF | `COPP.TO` | yfinance | 502 | ✅ | ⚠️ | ✅ | ✅ | ✅ | — |
| US ETF | `UFO` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `QTUM` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `BOTZ` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `DRIV` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `GDX` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `DRAM` | alpaca | 164 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CA ETF | `XETM.TO` | yfinance | 214 | ✅ | ✅ | ✅ | ⚠️ | ✅ | — |
| US ETF | `SETM` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `SMH` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `GRID` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `URA` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `AIPO` | alpaca | 337 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US ETF | `COPX` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US ETF | `SOXX` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CA ETF | `SGRD.TO` | yfinance | 151 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | — |
| US leveraged | `SOXL` | alpaca | 504 | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ |
| CA leveraged | `SOXL.NE` | yfinance | 318 | ✅ | ❌ | ⚠️ | ✅ | ⚠️ | ✅ |
| CA stock | `MDA.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `NTR.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `ASTL.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `BDT.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `PNG.V` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| CA stock | `CGY.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| US leveraged | `QPUX` | alpaca | 328 | ✅ | ✅ | ❌ | ✅ | ⚠️ | ✅ |
| US leveraged | `DRAL` | alpaca | 107 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `SPCL` | alpaca | 161 | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ |
| US leveraged | `URAA` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `UBOT` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `COPZ` | alpaca | 194 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| CA leveraged | `GDXU.TO` | yfinance | 502 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US stock | `AAPL` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `MSFT` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `META` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `NFLX` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `AMZN` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `TSLA` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `HD` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `V` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `LLY` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `ABBV` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `WMT` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `COST` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ❌ |
| US stock | `PG` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `XOM` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| US stock | `CVX` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| US stock | `COP` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| US stock | `LIN` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `NEM` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `GE` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US stock | `RTX` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| US stock | `NEE` | alpaca | 504 | ✅ | ❌ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `SO` | alpaca | 504 | ✅ | ❌ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `DUK` | alpaca | 504 | ✅ | ❌ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| US stock | `WELL` | alpaca | 504 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| US stock | `PLD` | alpaca | 504 | ✅ | ❌ | ✅ | ⚠️ | ⚠️ | ✅ |
| US stock | `EQIX` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| US leveraged | `NVDL` | alpaca | 504 | ✅ | ✅ | ❌ | ⚠️ | ⚠️ | ✅ |
| US leveraged | `AAPU` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `MSFU` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `METU` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `GGLL` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `NFXL` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `AMZU` | alpaca | 504 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| US leveraged | `TSLL` | alpaca | 504 | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ |
| US leveraged | `BRKU` | alpaca | 490 | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| US leveraged | `ELIL` | alpaca | 420 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US leveraged | `COTG` | alpaca | 299 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| US leveraged | `AVGC` | alpaca | 104 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |

## Verdict per class

- **US stock** (47): FAILS: JNJ C4, COST C9, NEE C4, SO C4, DUK C4, PLD C4; warnings: CAT C4, CAT C6, BRK-B C6, GOOGL C6, JPM C6, JNJ C6, JNJ C9, JNJ C8, GEV C6, TSM C4, TSM C6, ETN C6, VRT C6, CEG C6, ALAB C6, NVDA C6, AVGO C6, KEYS C6, MRVL C6, ONTO C6, CAMT C6, AMD C6, ORCL C6, FCX C6, QCOM C6, AAPL C6, MSFT C6, META C6, NFLX C6, AMZN C6, TSLA C6, HD C4, HD C6, V C6, LLY C6, ABBV C4, ABBV C6, WMT C4, WMT C6, COST C6, PG C6, XOM C4, XOM C6, XOM C9, CVX C4, CVX C6, CVX C9, COP C4, COP C6, COP C9, LIN C6, NEM C4, NEM C6, GE C6, RTX C4, RTX C6, RTX C9, NEE C6, NEE C8, SO C6, SO C9, SO C8, DUK C6, DUK C9, DUK C8, WELL C4, WELL C6, WELL C9, PLD C6, PLD C8, EQIX C6, EQIX C9
- **CA stock** (13): no failures
- **CA ETF** (15): FAILS: FINN.NE C4, XDRV.TO C4; warnings: FINN.NE C8, MTRX.TO C6, ORBX.TO C6, RBOT.TO C4, XDRV.TO C8, CARS.TO C4, COPP.TO C4, XETM.TO C6, SGRD.TO C4, SGRD.TO C6
- **CDR** (8): no failures; warnings: WDC.TO C6, ANET.TO C6, SNDK.TO C6, GEV.TO C6, AVGO.TO C6
- **US ETF** (13): no failures; warnings: UFO C6, QTUM C6, BOTZ C6, DRIV C6, GDX C4, GDX C6, DRAM C6, SETM C6, SMH C6, GRID C6, URA C4, URA C6, COPX C4, COPX C6, SOXX C6
- **US leveraged** (19): FAILS: QPUX C5, NVDL C5; warnings: SOXL C5, SOXL C6, QPUX C8, DRAL C6, SPCL C5, SPCL C6, URAA C4, URAA C6, UBOT C4, UBOT C6, COPZ C2, COPZ C6, NVDL C6, NVDL C8, AAPU C6, MSFU C6, METU C6, GGLL C6, NFXL C6, AMZU C6, TSLL C5, TSLL C6, BRKU C4, BRKU C6, BRKU C9, AVGC C6
- **CA leveraged** (2): FAILS: SOXL.NE C4; warnings: SOXL.NE C5, SOXL.NE C8

## Every finding (warn and fail), with evidence

**CAT** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**BRK-B** (US stock, dash symbol); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**GOOGL** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**JPM** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**JNJ** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 4; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.50%, volume x1.01 | alpaca vs yfinance: max close diff 0.00%, volume x1.01 | alpaca vs tradier: max close diff 0.50%, volume x1.01
- ⚠️ C8: tab says alpaca / 504 rows / cached; but another source STA can fall back to fails: tradier C4; the tab would not warn

**FINN.NE** (CA ETF); sources {'yfinance': 502}
- ❌ C4: yfinance: flat zero-volume 1%; bad OHLC rows 23; zero-volume in last 5: 0
- ⚠️ C8: tab says yfinance / 502 rows / cached and yfinance fails C4; the tab already lists: integrity

**WDC.TO** (CDR); sources {'yfinance': 138}
- ⚠️ C6: yfinance: 138 bars from 2026-05-08

**GEV** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**TSM** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**ETN** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**VRT** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**ANET.TO** (CDR); sources {'yfinance': 232}
- ⚠️ C6: yfinance: 232 bars from 2025-12-22

**CEG** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**ALAB** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**NVDA** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**AVGO** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**KEYS** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**MRVL** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**ONTO** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**CAMT** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**AMD** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**ORCL** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**FCX** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**QCOM** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**SNDK.TO** (CDR, short history); sources {'yfinance': 138, 'eodhd': 139}
- ⚠️ C6: yfinance: 138 bars from 2026-05-08

**GEV.TO** (CDR); sources {'yfinance': 232}
- ⚠️ C6: yfinance: 232 bars from 2025-12-22

**AVGO.TO** (CDR); sources {'yfinance': 232}
- ⚠️ C6: yfinance: 232 bars from 2025-12-22

**MTRX.TO** (CA ETF); sources {'yfinance': 214}
- ⚠️ C6: yfinance: 214 bars from 2026-01-20

**ORBX.TO** (CA ETF); sources {'yfinance': 145}
- ⚠️ C6: yfinance: 145 bars from 2026-04-29

**RBOT.TO** (CA ETF); sources {'yfinance': 502}
- ⚠️ C4: yfinance: flat zero-volume 2%; bad OHLC rows 0; zero-volume in last 5: 0

**XDRV.TO** (CA ETF); sources {'yfinance': 502}
- ❌ C4: yfinance: flat zero-volume 82%; bad OHLC rows 0; zero-volume in last 5: 3
- ⚠️ C8: tab says yfinance / 501 rows / cached and yfinance fails C4; the tab already lists: integrity

**CARS.TO** (CA ETF); sources {'yfinance': 502}
- ⚠️ C4: yfinance: flat zero-volume 12%; bad OHLC rows 0; zero-volume in last 5: 1

**COPP.TO** (CA ETF); sources {'yfinance': 502}
- ⚠️ C4: yfinance: flat zero-volume 2%; bad OHLC rows 0; zero-volume in last 5: 0

**UFO** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**QTUM** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**BOTZ** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**DRIV** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**GDX** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**DRAM** (US ETF); sources {'alpaca': 164, 'twelvedata': 164, 'yfinance': 164, 'tradier': 164}
- ⚠️ C6: alpaca: 164 bars from 2026-04-02 || twelvedata: 164 bars from 2026-04-02 || yfinance: 164 bars from 2026-04-02 || tradier: 164 bars from 2026-04-02

**XETM.TO** (CA ETF); sources {'yfinance': 214}
- ⚠️ C6: yfinance: 214 bars from 2026-01-20

**SETM** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**SMH** (US ETF, no fundamentals); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**GRID** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**URA** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 2; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**COPX** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 2; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**SOXX** (US ETF); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**SGRD.TO** (CA ETF); sources {'yfinance': 151}
- ⚠️ C4: yfinance: flat zero-volume 3%; bad OHLC rows 0; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 151 bars from 2026-04-21

**SOXL** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C5: alpaca: 2025-04-09 +55%: also in twelvedata,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || twelvedata: 2025-04-09 +55%: also in alpaca,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2025-04-09 +55%: also in alpaca,twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2025-04-09 +55%: also in alpaca,twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**SOXL.NE** (CA leveraged, known bad: Cboe Canada only); sources {'yfinance': 318, 'eodhd': 251}
- ❌ C4: yfinance: flat zero-volume 100%; bad OHLC rows 0; zero-volume in last 5: 5
- ⚠️ C5: yfinance: 2026-05-25 -67%: also in eodhd (real move, or unadjusted everywhere: needs IBKR) | 2026-11-23 +41%: also in eodhd (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C8: tab says yfinance / 318 rows / cached and yfinance fails C4; the tab already lists: integrity

**QPUX** (US leveraged, 1:3 reverse split 2026-03-23); sources {'alpaca': 328, 'twelvedata': 328, 'yfinance': 328, 'tradier': 328}
- ❌ C5: alpaca: 2026-05-21 +48%: also in twelvedata,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || twelvedata: 2026-05-21 +48%: also in alpaca,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-05-21 +48%: also in alpaca,twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2026-03-20 -69%: ONLY here; alpaca,twelvedata,yfinance are continuous -> tradier has a split error | 2026-05-21 +48%: also in alpaca,twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C8: tab says alpaca / 328 rows / cached; but another source STA can fall back to fails: tradier C5; the tab would not warn

**DRAL** (US leveraged, ~100 days); sources {'alpaca': 107, 'twelvedata': 107, 'yfinance': 107, 'tradier': 107}
- ⚠️ C6: alpaca: 107 bars from 2026-06-25 || twelvedata: 107 bars from 2026-06-25 || yfinance: 107 bars from 2026-06-25 || tradier: 107 bars from 2026-06-25

**SPCL** (US leveraged, ~154 days); sources {'alpaca': 161, 'twelvedata': 157, 'yfinance': 161, 'tradier': 161}
- ⚠️ C5: alpaca: 2026-06-12 +57%: also in twelvedata,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || twelvedata: 2026-06-12 +57%: also in alpaca,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-06-12 +57%: also in alpaca,twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2026-06-12 +57%: also in alpaca,twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: alpaca: 161 bars from 2026-04-08 || twelvedata: 157 bars from 2026-04-14; starts 6 days after alpaca (2026-04-08, 161 bars); starts 6 days after yfinance (2026-04-08, 161 bars); starts 6 days after tradier (2026-04-08, 161 bars) || yfinance: 161 bars from 2026-04-08 || tradier: 161 bars from 2026-04-08

**URAA** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**UBOT** (US leveraged, control); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**COPZ** (US leveraged); sources {'alpaca': 194, 'twelvedata': 196, 'yfinance': 194, 'tradier': 194}
- ⚠️ C2: alpaca: last bar 2026-11-23, expected 2026-11-24 (1 session behind) || twelvedata: last bar 2026-11-23, expected 2026-11-24 (1 session behind) || yfinance: last bar 2026-11-23, expected 2026-11-24 (1 session behind) || tradier: last bar 2026-11-23, expected 2026-11-24 (1 session behind)
- ⚠️ C6: alpaca: 194 bars from 2026-02-18; starts 588 days after twelvedata (2024-07-10, 196 bars) || twelvedata: 196 bars from 2024-07-10 || yfinance: 194 bars from 2026-02-18; starts 588 days after twelvedata (2024-07-10, 196 bars) || tradier: 194 bars from 2026-02-18; starts 588 days after twelvedata (2024-07-10, 196 bars)

**AAPL** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**MSFT** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**META** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**NFLX** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**AMZN** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**TSLA** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**HD** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**V** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**LLY** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**ABBV** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**WMT** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**COST** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ❌ C9: alpaca vs twelvedata: max close diff 0.10%, volume x1.01 | alpaca vs yfinance: max close diff 0.00%, volume x1.01 | alpaca vs tradier: max close diff 2.88%, volume x1.01

**PG** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**XOM** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.01%, volume x1.00 | alpaca vs yfinance: max close diff 0.00%, volume x1.00 | alpaca vs tradier: max close diff 0.63%, volume x1.00

**CVX** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.01%, volume x1.00 | alpaca vs yfinance: max close diff 0.00%, volume x1.00 | alpaca vs tradier: max close diff 0.83%, volume x1.00

**COP** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 3; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.01%, volume x1.00 | alpaca vs yfinance: max close diff 0.00%, volume x1.00 | alpaca vs tradier: max close diff 0.66%, volume x1.00

**LIN** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**NEM** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**GE** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**RTX** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 2; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.00%, volume x1.00 | alpaca vs yfinance: max close diff 0.00%, volume x1.00 | alpaca vs tradier: max close diff 0.38%, volume x1.00

**NEE** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 4; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C8: tab says alpaca / 504 rows / cached; but another source STA can fall back to fails: tradier C4; the tab would not warn

**SO** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 4; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.01%, volume x1.00 | alpaca vs yfinance: max close diff 0.01%, volume x1.00 | alpaca vs tradier: max close diff 0.82%, volume x1.00
- ⚠️ C8: tab says alpaca / 504 rows / cached; but another source STA can fall back to fails: tradier C4; the tab would not warn

**DUK** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 5; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.01%, volume x1.00 | alpaca vs yfinance: max close diff 0.00%, volume x1.00 | alpaca vs tradier: max close diff 0.85%, volume x1.00
- ⚠️ C8: tab says alpaca / 504 rows / cached; but another source STA can fall back to fails: tradier C4; the tab would not warn

**WELL** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C4: tradier: flat zero-volume 0%; bad OHLC rows 1; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.00%, volume x1.00 | alpaca vs yfinance: max close diff 0.00%, volume x1.00 | alpaca vs tradier: max close diff 0.35%, volume x1.00

**PLD** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ❌ C4: tradier: flat zero-volume 0%; bad OHLC rows 4; zero-volume in last 5: 0
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C8: tab says alpaca / 504 rows / cached; but another source STA can fall back to fails: tradier C4; the tab would not warn

**EQIX** (US stock); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.01%, volume x1.00 | alpaca vs yfinance: max close diff 0.00%, volume x1.00 | alpaca vs tradier: max close diff 0.50%, volume x1.00

**NVDL** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ❌ C5: alpaca: 2026-11-23 +62%: also in twelvedata,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || twelvedata: 2026-11-23 +62%: also in alpaca,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2026-11-23 +62%: also in alpaca,twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2026-06-25 +191%: ONLY here; alpaca,twelvedata,yfinance are continuous -> tradier has a split error | 2026-11-23 +62%: also in alpaca,twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)
- ⚠️ C8: tab says alpaca / 504 rows / cached; but another source STA can fall back to fails: tradier C5; the tab would not warn

**AAPU** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**MSFU** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**METU** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**GGLL** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**NFXL** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**AMZU** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**TSLL** (US leveraged); sources {'alpaca': 504, 'twelvedata': 504, 'yfinance': 501, 'tradier': 501}
- ⚠️ C5: alpaca: 2025-04-09 +45%: also in twelvedata,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || twelvedata: 2025-04-09 +45%: also in alpaca,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR) || yfinance: 2025-04-09 +45%: also in alpaca,twelvedata,tradier (real move, or unadjusted everywhere: needs IBKR) || tradier: 2025-04-09 +45%: also in alpaca,twelvedata,yfinance (real move, or unadjusted everywhere: needs IBKR)
- ⚠️ C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) || tradier: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars)

**BRKU** (US leveraged); sources {'alpaca': 490, 'twelvedata': 495, 'yfinance': 490, 'tradier': 490}
- ⚠️ C4: twelvedata: flat zero-volume 1%; bad OHLC rows 0; zero-volume in last 5: 5
- ⚠️ C6: alpaca: 490 bars from 2024-12-11; starts 7 days after twelvedata (2024-12-04, 495 bars) || yfinance: 490 bars from 2024-12-11; starts 7 days after twelvedata (2024-12-04, 495 bars) || tradier: 490 bars from 2024-12-11; starts 7 days after twelvedata (2024-12-04, 495 bars)
- ⚠️ C9: alpaca vs twelvedata: max close diff 0.33%, volume xnan | alpaca vs yfinance: max close diff 0.00%, volume x1.01 | alpaca vs tradier: max close diff 0.00%, volume x1.00

**AVGC** (US leveraged); sources {'alpaca': 104, 'twelvedata': 104, 'yfinance': 104, 'tradier': 104}
- ⚠️ C6: alpaca: 104 bars from 2026-06-30 || twelvedata: 104 bars from 2026-06-30 || yfinance: 104 bars from 2026-06-30 || tradier: 104 bars from 2026-06-30


## Source errors (a source that could not serve a ticker)


## Known limits of this audit (read before trusting the matrix)

- **Agreement is not accuracy.** If two sources share the same defect they agree (SOXL.NE on Yahoo and EODHD are both close-only), so C9 passes. Only the IBKR truth step (step 2) can settle those; C5 marks them "needs IBKR".
- **"STA uses" comes from the tab.** The tab's source was read right after this script spent Twelve Data credits on the same key, so some "fell through to Yahoo" results may be partly self-inflicted. Either way, every source in the chain is graded, because any of them can serve a request.
- **Canada has one source for most tickers.** Only the tickers listed with EODHD had a second opinion (free quota: 20 calls a day). The rest show `—` in C9, which means unchecked, not clean.
- **Freshness ignores market holidays** (it uses weekdays).
- **Tradier is not dividend-adjusted**, so its old closes differ slightly from Yahoo's on ex-dividend days; the close check only looks at the last 20 sessions.
- Not run: identity/currency (C1), close accuracy vs the broker (C3), volume vs the broker (C7), fundamentals and classification (C10), Alpha Vantage.

