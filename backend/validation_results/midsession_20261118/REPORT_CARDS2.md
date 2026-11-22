# Statement Audit phase 3a report (Market backdrop, Fundamentals, Mean-Reversion Read)

Run: 2026-11-18T10:13 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 3687 · WRONG 0 (CRITICAL) · MISLEADING 1 (per-row severity) · UNVERIFIED 146 (INFO)

Recomputed from bars: MR RSI(2), % above the 200-day, dollar volume, the four rule marks, the blocker sentence; S&P 500 200/50-day and the 10-session drop (the app's own 260 bars); QQQ and "largest since" from an independent Yahoo history (S4).
Provider fields (sales growth, ROE, debt/equity) are arithmetic and flag logic only: no recompute is possible (UNVERIFIED as to truth). NOT YET COVERED: the Data Sources tab (phase 3b), other tabs; branches these tickers do not reach (signal true, VIX band edges, no-down-day, unavailable backdrop, negative equity) are exercised by planted tests only.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| COTG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 69.38 | 68.91 | MISLEADING | LOW | within 0.8: the MR route smooths over its own frame length |
| ABBV | U-FU | numbers on the card no statement claimed (exhaustive scan) | -17.65 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ALAB | U-FU | numbers on the card no statement claimed (exhaustive scan) | 1 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AMD | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| CAMT | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| COP | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| DUK | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| EQIX | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| FCX | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| GE | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| GOOGL | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| JNJ | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| LIN | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| NEE | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| NEM | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ONTO | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| PLD | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| QCOM | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| RTX | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| SO | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AMZU | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $33.49 2026 -11 -17 $35.25 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| BDT.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $67.57 2026 -11 -17 $71.13 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| CSU.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $3,151.08 2026 -11 -17 $3,316.93 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| HD | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $322.06 2026 -11 -17 $339.01 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| JPM | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $313.46 2026 -11 -17 $329.96 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| MSFT | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $480.93 2026 -11 -17 $506.24 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| MSFU | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $35.47 2026 -11 -17 $37.34 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| RY.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $266.94 2026 -11 -17 $280.99 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| VFV.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $176.83 2026 -11 -17 $186.14 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| XEQT.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -17 5% $42.12 2026 -11 -17 $44.34 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| AAPL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AAPU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ABBV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AIPO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ALAB | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMZN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMZU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ANET.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ASML.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ASTL.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ATD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGC | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGO.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BDT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BOTZ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BRK-B | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BRKU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CAMT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CARS.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CAT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CCO.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CEG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CGY.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CNQ.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CNR.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COP | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPP.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPZ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COST | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COTG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CSU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CVX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRAL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRAM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRIV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DUK | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ELIL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| EQIX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ETN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| FCX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| FINN.NE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GDX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GDXU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GEV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GEV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GGLL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GIB-A.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GOOGL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GRID | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HURA.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HXQ.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| JNJ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| JPM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| KEYS | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| LIN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| LLY | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MDA.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| META | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| METU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MRVL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MSFT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MSFU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MTRX.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NEE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NEM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NFLX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NFXL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NTR.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NVDA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NVDL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ONTO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ORBX.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ORCL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PLD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PNG.V | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QCOM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QPUX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QTUM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RBOT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RTX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RY.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SETM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SGRD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SMH | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SNDK.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXL.NE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SPCL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSLA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSLL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| UBOT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| UFO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| URA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| URAA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| V | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| VFV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| VRT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WDC.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WELL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WMT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XCHP.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XDRV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XEQT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XETM.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XGD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XOM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AAPL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.7% | +11.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AAPL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 127.6% | 127.6% flag=False | PASS |  |  |
| AAPL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| AAPL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AAPL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| AAPL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-02 (16 days ago); no upcoming date listed. | 2026-11-02 days_until=-16 | PASS |  |  |
| AAPU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AAPU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ABBV | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +10.3% | +10.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ABBV | FU3 | ROE: value (1 dp) and the flag at < 0% | ⚑ Return on equity ROE -92.0% | -92.0% flag=True | PASS |  |  |
| ABBV | FU4 | negative D/E -> "ratio not meaningful", unchecked | says so | not meaningful | PASS |  |  |
| ABBV | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| ABBV | FU5w | one plain sentence per tripped flag | Return on equity is negative. | 1 sentence(s) | PASS |  |  |
| ABBV | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| ABBV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (19 days ago); no upcoming date listed. | 2026-10-30 days_until=-19 | PASS |  |  |
| AIPO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AIPO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ALAB | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +153.7% | +153.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ALAB | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ALAB | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) | Alpha Vantage | PASS |  |  |
| ALAB | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (15 days ago); no upcoming date listed. | 2026-11-03 days_until=-15 | PASS |  |  |
| AMD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.6% | 11.6% flag=False | PASS |  |  |
| AMD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.10 | 0.10 flag=False | PASS |  |  |
| AMD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AMD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| AMD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (15 days ago); no upcoming date listed. | 2026-11-03 days_until=-15 | PASS |  |  |
| AMD.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +44.7% | +44.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AMD.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 12.0% | 12.0% flag=False | PASS |  |  |
| AMD.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.13 | 0.13 flag=False | PASS |  |  |
| AMD.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AMD.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| AMD.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| AMZN | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +12.1% | +12.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AMZN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 27.4% | 27.4% flag=False | PASS |  |  |
| AMZN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.50 | 0.50 flag=False | PASS |  |  |
| AMZN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AMZN | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| AMZN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (20 days ago); no upcoming date listed. | 2026-10-29 days_until=-20 | PASS |  |  |
| AMZU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AMZU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ANET.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ANET.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ASML.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ASML.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ASTL.TO | FU0 | the fundamentals feed answered 404 / error: the card says "Can't check", never "No red flags" | Can't check | Can't check | PASS |  | provider outcome (None); not a card bug |
| ATD.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +25.1% | +25.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ATD.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.6% | 19.6% flag=False | PASS |  |  |
| ATD.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.92 | 0.92 flag=False | PASS |  |  |
| ATD.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ATD.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| ATD.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-24 · in 6 days. Within a week: decide before then whether to hold throug | 2026-11-24 days_until=6 | PASS |  |  |
| AVGC | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AVGC | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| AVGO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +85.5% | +85.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AVGO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 43.9% | 43.9% flag=False | PASS |  |  |
| AVGO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.60 | 0.60 flag=False | PASS |  |  |
| AVGO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AVGO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| AVGO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-09 · in 21 days. If you'll still hold on that date, the price can jump e | 2026-12-09 days_until=21 | PASS |  |  |
| AVGO.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AVGO.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| BDT.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.7% | +36.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| BDT.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.6% | 16.6% flag=False | PASS |  |  |
| BDT.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.79 | 0.79 flag=False | PASS |  |  |
| BDT.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| BDT.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| BDT.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-11 (7 days ago); no upcoming date listed. | 2026-11-11 days_until=-7 | PASS |  |  |
| BOTZ | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| BOTZ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| BRK-B | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.2% | +11.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| BRK-B | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.9% | 11.9% flag=False | PASS |  |  |
| BRK-B | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| BRK-B | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| BRK-B | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| BRK-B | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-07 (11 days ago); no upcoming date listed. | 2026-11-07 days_until=-11 | PASS |  |  |
| BRKU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| BRKU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CAMT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 5.8% | 5.8% flag=False | PASS |  |  |
| CAMT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.69 | 0.69 flag=False | PASS |  |  |
| CAMT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CAMT | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| CAMT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (14 days ago); no upcoming date listed. | 2026-11-04 days_until=-14 | PASS |  |  |
| CARS.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| CARS.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CAT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +17.3% | +17.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CAT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 58.5% | 58.5% flag=False | PASS |  |  |
| CAT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 2.10 | 2.10 flag=True | PASS |  |  |
| CAT | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| CAT | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| CAT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| CAT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (20 days ago); no upcoming date listed. | 2026-10-29 days_until=-20 | PASS |  |  |
| CCO.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +0.7% | +0.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CCO.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 5.7% | 5.7% flag=False | PASS |  |  |
| CCO.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.14 | 0.14 flag=False | PASS |  |  |
| CCO.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CCO.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CCO.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (19 days ago); no upcoming date listed. | 2026-10-30 days_until=-19 | PASS |  |  |
| CEG | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +45.4% | +45.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CEG | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 18.3% | 18.3% flag=False | PASS |  |  |
| CEG | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| CEG | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CEG | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CEG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-09 (9 days ago); no upcoming date listed. | 2026-11-09 days_until=-9 | PASS |  |  |
| CGY.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +19.9% | +19.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CGY.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 12.0% | 12.0% flag=False | PASS |  |  |
| CGY.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.54 | 0.54 flag=False | PASS |  |  |
| CGY.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CGY.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CGY.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-30 · in 12 days. If you'll still hold on that date, the price can jump e | 2026-11-30 days_until=12 | PASS |  |  |
| CNQ.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +34.4% | +34.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CNQ.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 32.4% | 32.4% flag=False | PASS |  |  |
| CNQ.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.42 | 0.42 flag=False | PASS |  |  |
| CNQ.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CNQ.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CNQ.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (13 days ago); no upcoming date listed. | 2026-11-05 days_until=-13 | PASS |  |  |
| CNR.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +14.6% | +14.6% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CNR.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 22.4% | 22.4% flag=False | PASS |  |  |
| CNR.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.09 | 1.09 flag=False | PASS |  |  |
| CNR.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CNR.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CNR.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-29 · in 72 days. If you'll still hold on that date, the price can jump e | 2027-01-29 days_until=72 | PASS |  |  |
| COP | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.8% | 17.8% flag=False | PASS |  |  |
| COP | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.35 | 0.35 flag=False | PASS |  |  |
| COP | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| COP | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| COP | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (13 days ago); no upcoming date listed. | 2026-11-05 days_until=-13 | PASS |  |  |
| COPP.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| COPP.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| COPX | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| COPX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| COPZ | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| COPZ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| COST | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.1% | +11.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| COST | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 28.0% | 28.0% flag=False | PASS |  |  |
| COST | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| COST | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| COST | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| COST | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-10 · in 22 days. If you'll still hold on that date, the price can jump e | 2026-12-10 days_until=22 | PASS |  |  |
| COTG | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| COTG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CSU.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +19.1% | +19.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CSU.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 24.2% | 24.2% flag=False | PASS |  |  |
| CSU.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.13 | 1.13 flag=False | PASS |  |  |
| CSU.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CSU.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CSU.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-06 (12 days ago); no upcoming date listed. | 2026-11-06 days_until=-12 | PASS |  |  |
| CVX | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +34.8% | +34.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CVX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 13.9% | 13.9% flag=False | PASS |  |  |
| CVX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| CVX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CVX | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CVX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (19 days ago); no upcoming date listed. | 2026-10-30 days_until=-19 | PASS |  |  |
| DRAL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| DRAL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| DRAM | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| DRAM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| DRIV | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| DRIV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| DUK | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 10.0% | 10.0% flag=False | PASS |  |  |
| DUK | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.68 | 1.68 flag=False | PASS |  |  |
| DUK | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| DUK | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| DUK | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (13 days ago); no upcoming date listed. | 2026-11-05 days_until=-13 | PASS |  |  |
| ELIL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ELIL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| EQIX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.5% | 11.5% flag=False | PASS |  |  |
| EQIX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.72 | 1.72 flag=False | PASS |  |  |
| EQIX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| EQIX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| EQIX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (21 days ago); no upcoming date listed. | 2026-10-28 days_until=-21 | PASS |  |  |
| ETN | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +28.0% | +28.0% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ETN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.5% | 19.5% flag=False | PASS |  |  |
| ETN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.00 | 1.00 flag=False | PASS |  |  |
| ETN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ETN | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| ETN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (15 days ago); no upcoming date listed. | 2026-11-03 days_until=-15 | PASS |  |  |
| FCX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 15.3% | 15.3% flag=False | PASS |  |  |
| FCX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.49 | 0.49 flag=False | PASS |  |  |
| FCX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| FCX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| FCX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (22 days ago); no upcoming date listed. | 2026-10-27 days_until=-22 | PASS |  |  |
| FINN.NE | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| FINN.NE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GDX | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GDX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GDXU.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GDXU.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GE | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.6% | 50.6% flag=False | PASS |  |  |
| GE | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.10 | 1.10 flag=False | PASS |  |  |
| GE | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GE | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| GE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (29 days ago); no upcoming date listed. | 2026-10-20 days_until=-29 | PASS |  |  |
| GEV | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +26.8% | +26.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| GEV | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 93.0% | 93.0% flag=False | PASS |  |  |
| GEV | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.30 | 0.30 flag=False | PASS |  |  |
| GEV | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GEV | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| GEV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-27 · in 70 days. If you'll still hold on that date, the price can jump e | 2027-01-27 days_until=70 | PASS |  |  |
| GEV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GEV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GGLL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GGLL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GIB-A.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +3.3% | +3.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| GIB-A.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.5% | 17.5% flag=False | PASS |  |  |
| GIB-A.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.39 | 0.39 flag=False | PASS |  |  |
| GIB-A.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GIB-A.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| GIB-A.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-11 (7 days ago); no upcoming date listed. | 2026-11-11 days_until=-7 | PASS |  |  |
| GOOGL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 42.6% | 42.6% flag=False | PASS |  |  |
| GOOGL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.18 | 0.18 flag=False | PASS |  |  |
| GOOGL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GOOGL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| GOOGL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (21 days ago); no upcoming date listed. | 2026-10-28 days_until=-21 | PASS |  |  |
| GRID | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GRID | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| HD | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +5.7% | +5.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| HD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 102.7% | 102.7% flag=False | PASS |  |  |
| HD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 3.18 | 3.18 flag=True | PASS |  |  |
| HD | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| HD | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| HD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| HD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-17 (1 day ago); no upcoming date listed. | 2026-11-17 days_until=-1 | PASS |  |  |
| HURA.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| HURA.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| HXQ.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| HXQ.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| JNJ | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.6% | 19.6% flag=False | PASS |  |  |
| JNJ | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.55 | 0.55 flag=False | PASS |  |  |
| JNJ | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| JNJ | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| JNJ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-26 · in 69 days. If you'll still hold on that date, the price can jump e | 2027-01-26 days_until=69 | PASS |  |  |
| JPM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +10.2% | +10.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| JPM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.9% | 17.9% flag=False | PASS |  |  |
| JPM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 3.32 | 3.32 flag=True | PASS |  |  |
| JPM | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| JPM | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| JPM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| JPM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-14 · in 57 days. If you'll still hold on that date, the price can jump e | 2027-01-14 days_until=57 | PASS |  |  |
| KEYS | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.5% | +36.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| KEYS | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 20.9% | 20.9% flag=False | PASS |  |  |
| KEYS | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.42 | 0.42 flag=False | PASS |  |  |
| KEYS | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| KEYS | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| KEYS | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-19 · in 1 day. Within a week: decide before then whether to hold through | 2026-11-19 days_until=1 | PASS |  |  |
| LIN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 18.1% | 18.1% flag=False | PASS |  |  |
| LIN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.68 | 0.68 flag=False | PASS |  |  |
| LIN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| LIN | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| LIN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (20 days ago); no upcoming date listed. | 2026-10-29 days_until=-20 | PASS |  |  |
| LLY | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +38.6% | +38.6% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| LLY | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 83.7% | 83.7% flag=False | PASS |  |  |
| LLY | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.23 | 1.23 flag=False | PASS |  |  |
| LLY | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| LLY | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| LLY | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (20 days ago); no upcoming date listed. | 2026-10-29 days_until=-20 | PASS |  |  |
| MDA.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +21.5% | +21.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MDA.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 4.9% | 4.9% flag=False | PASS |  |  |
| MDA.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.31 | 0.31 flag=False | PASS |  |  |
| MDA.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MDA.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| MDA.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (13 days ago); no upcoming date listed. | 2026-11-05 days_until=-13 | PASS |  |  |
| META | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +26.1% | +26.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| META | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 30.3% | 30.3% flag=False | PASS |  |  |
| META | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.30 | 0.30 flag=False | PASS |  |  |
| META | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| META | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| META | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (28 days ago); no upcoming date listed. | 2026-10-21 days_until=-28 | PASS |  |  |
| METU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| METU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| MRVL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.5% | +36.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MRVL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.5% | 16.5% flag=False | PASS |  |  |
| MRVL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.29 | 0.29 flag=False | PASS |  |  |
| MRVL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MRVL | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| MRVL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-01 · in 13 days. If you'll still hold on that date, the price can jump e | 2026-12-01 days_until=13 | PASS |  |  |
| MSFT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +18.8% | +18.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MSFT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 33.2% | 33.2% flag=False | PASS |  |  |
| MSFT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.23 | 0.23 flag=False | PASS |  |  |
| MSFT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MSFT | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| MSFT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (21 days ago); no upcoming date listed. | 2026-10-28 days_until=-21 | PASS |  |  |
| MSFU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| MSFU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| MTRX.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| MTRX.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| MU.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| MU.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| NEE | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 20.4% | 20.4% flag=False | PASS |  |  |
| NEE | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.85 | 1.85 flag=False | PASS |  |  |
| NEE | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NEE | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| NEE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (28 days ago); no upcoming date listed. | 2026-10-21 days_until=-28 | PASS |  |  |
| NEM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 26.5% | 26.5% flag=False | PASS |  |  |
| NEM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.16 | 0.16 flag=False | PASS |  |  |
| NEM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NEM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| NEM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-22 (27 days ago); no upcoming date listed. | 2026-10-22 days_until=-27 | PASS |  |  |
| NFLX | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.8% | +11.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NFLX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.4% | 50.4% flag=False | PASS |  |  |
| NFLX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.52 | 0.52 flag=False | PASS |  |  |
| NFLX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NFLX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NFLX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (29 days ago); no upcoming date listed. | 2026-10-20 days_until=-29 | PASS |  |  |
| NFXL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| NFXL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| NTR.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +1.2% | +1.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NTR.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 8.8% | 8.8% flag=False | PASS |  |  |
| NTR.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.55 | 0.55 flag=False | PASS |  |  |
| NTR.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NTR.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| NTR.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (14 days ago); no upcoming date listed. | 2026-11-04 days_until=-14 | PASS |  |  |
| NVDA | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +105.8% | +105.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NVDA | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 110.1% | 110.1% flag=False | PASS |  |  |
| NVDA | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| NVDA | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NVDA | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NVDA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-17 (1 day ago); no upcoming date listed. | 2026-11-17 days_until=-1 | PASS |  |  |
| NVDL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| NVDL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ONTO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 6.5% | 6.5% flag=False | PASS |  |  |
| ONTO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.77 | 0.77 flag=False | PASS |  |  |
| ONTO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ONTO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| ONTO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-09 (9 days ago); no upcoming date listed. | 2026-11-09 days_until=-9 | PASS |  |  |
| ORBX.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ORBX.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ORCL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 42.6% | 42.6% flag=False | PASS |  |  |
| ORCL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 2.01 | 2.01 flag=True | PASS |  |  |
| ORCL | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| ORCL | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| ORCL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| ORCL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-14 · in 26 days. If you'll still hold on that date, the price can jump e | 2026-12-14 days_until=26 | PASS |  |  |
| PG | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +4.0% | +4.0% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| PG | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 29.6% | 29.6% flag=False | PASS |  |  |
| PG | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.70 | 0.70 flag=False | PASS |  |  |
| PG | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PG | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · yfinance (ROE, debt) | Alpha Vantage, yfinance | PASS |  |  |
| PG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-22 (27 days ago); no upcoming date listed. | 2026-10-22 days_until=-27 | PASS |  |  |
| PLD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 7.9% | 7.9% flag=False | PASS |  |  |
| PLD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.66 | 0.66 flag=False | PASS |  |  |
| PLD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PLD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| PLD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (34 days ago); no upcoming date listed. | 2026-10-15 days_until=-34 | PASS |  |  |
| PNG.V | FU0 | the fundamentals feed answered 404 / error: the card says "Can't check", never "No red flags" | Can't check | Can't check | PASS |  | provider outcome (Could not get fundamentals for PNG.V); not a card bug |
| QCOM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.3% | 50.3% flag=False | PASS |  |  |
| QCOM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.50 | 0.50 flag=False | PASS |  |  |
| QCOM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| QCOM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| QCOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (14 days ago); no upcoming date listed. | 2026-11-04 days_until=-14 | PASS |  |  |
| QPUX | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| QPUX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| QTUM | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| QTUM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| RBOT.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| RBOT.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| RTX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 12.6% | 12.6% flag=False | PASS |  |  |
| RTX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.54 | 0.54 flag=False | PASS |  |  |
| RTX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| RTX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| RTX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (29 days ago); no upcoming date listed. | 2026-10-20 days_until=-29 | PASS |  |  |
| RY.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +8.9% | +8.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| RY.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.2% | 16.2% flag=False | PASS |  |  |
| RY.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 4.10 | 4.10 flag=True | PASS |  |  |
| RY.TO | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| RY.TO | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| RY.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| RY.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-03 · in 15 days. If you'll still hold on that date, the price can jump e | 2026-12-03 days_until=15 | PASS |  |  |
| SETM | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SETM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| SGRD.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SGRD.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| SMH | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SMH | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| SNDK.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SNDK.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| SO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 12.9% | 12.9% flag=False | PASS |  |  |
| SO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.76 | 1.76 flag=False | PASS |  |  |
| SO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| SO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| SO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (13 days ago); no upcoming date listed. | 2026-11-05 days_until=-13 | PASS |  |  |
| SOXL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SOXL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| SOXL.NE | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SOXL.NE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| SOXX | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SOXX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| SPCL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SPCL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| TSLA | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales -0.2% | -0.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| TSLA | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 3.8% | 3.8% flag=False | PASS |  |  |
| TSLA | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.11 | 0.11 flag=False | PASS |  |  |
| TSLA | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| TSLA | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| TSLA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (28 days ago); no upcoming date listed. | 2026-10-21 days_until=-28 | PASS |  |  |
| TSLL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| TSLL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| TSM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +50.9% | +50.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| TSM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 41.9% | 41.9% flag=False | PASS |  |  |
| TSM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| TSM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| TSM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| TSM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (34 days ago); no upcoming date listed. | 2026-10-15 days_until=-34 | PASS |  |  |
| UBOT | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| UBOT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| UFO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| UFO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| URA | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| URA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| URAA | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| URAA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| V | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +13.2% | +13.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| V | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 64.5% | 64.5% flag=False | PASS |  |  |
| V | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.61 | 0.61 flag=False | PASS |  |  |
| V | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| V | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| V | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (22 days ago); no upcoming date listed. | 2026-10-27 days_until=-22 | PASS |  |  |
| VFV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| VFV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| VRT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +61.2% | +61.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| VRT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 46.6% | 46.6% flag=False | PASS |  |  |
| VRT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.61 | 0.61 flag=False | PASS |  |  |
| VRT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| VRT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| VRT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (21 days ago); no upcoming date listed. | 2026-10-28 days_until=-21 | PASS |  |  |
| WDC.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| WDC.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| WELL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +38.4% | +38.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| WELL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 3.7% | 3.7% flag=False | PASS |  |  |
| WELL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.40 | 0.40 flag=False | PASS |  |  |
| WELL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| WELL | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| WELL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-26 (23 days ago); no upcoming date listed. | 2026-10-26 days_until=-23 | PASS |  |  |
| WMT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +5.9% | +5.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| WMT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 22.3% | 22.3% flag=False | PASS |  |  |
| WMT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.72 | 0.72 flag=False | PASS |  |  |
| WMT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| WMT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| WMT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-19 · in 1 day. Within a week: decide before then whether to hold through | 2026-11-19 days_until=1 | PASS |  |  |
| XCHP.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| XCHP.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| XDRV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| XDRV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| XEQT.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| XEQT.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| XETM.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| XETM.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| XGD.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| XGD.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| XOM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +32.6% | +32.6% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| XOM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 15.5% | 15.5% flag=False | PASS |  |  |
| XOM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.13 | 0.13 flag=False | PASS |  |  |
| XOM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| XOM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| XOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (19 days ago); no upcoming date listed. | 2026-10-30 days_until=-19 | PASS |  |  |
| AAPL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +16.7% | TR +16.7% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AAPL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AAPL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AAPL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 16,628,022,962 | 16,628,048,373 | PASS |  |  |
| AAPL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AAPL | MR-price | price = the last completed close | 351.91 | 351.91 | PASS |  |  |
| AAPL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $351.91 needs above $10 | $351.91 needs above $10 | PASS |  |  |
| AAPL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 25.6 needs under 10 | 25.55 needs under 10 -> ✗ | PASS |  |  |
| AAPL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 16.7% above its 200-day average | 16.7% above | PASS |  |  |
| AAPL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $16.6B traded on an average day needs above $25M | $16,628,022,962 needs above $25,000,000 | PASS |  |  |
| AAPL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 25.55 | 25.55 | PASS |  |  |
| AAPL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 16.66% | 16.66% | PASS |  |  |
| AAPL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +27.2% | TR +27.2% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AAPU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AAPU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AAPU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 27,133,972 | 27,133,972 | PASS |  |  |
| AAPU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AAPU | MR-price | price = the last completed close | 48.49 | 48.49 | PASS |  |  |
| AAPU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $48.49 needs above $10 | $48.49 needs above $10 | PASS |  |  |
| AAPU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 23.4 needs under 10 | 23.36 needs under 10 -> ✗ | PASS |  |  |
| AAPU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 27.2% above its 200-day average | 27.2% above | PASS |  |  |
| AAPU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $27.1M traded on an average day needs above $25M | $27,133,972 needs above $25,000,000 | PASS |  |  |
| AAPU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 23.36 | 23.36 | PASS |  |  |
| AAPU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 27.22% | 27.22% | PASS |  |  |
| AAPU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ABBV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +22.6% | TR +22.6% | PASS | LOW | the two cards divide by different roundings of the average |
| ABBV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ABBV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| ABBV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ABBV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,497,755,339 | 1,497,755,342 | PASS |  |  |
| ABBV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ABBV | MR-price | price = the last completed close | 292.82 | 292.82 | PASS |  |  |
| ABBV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $292.82 needs above $10 | $292.82 needs above $10 | PASS |  |  |
| ABBV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.9 needs under 10 | 12.87 needs under 10 -> ✗ | PASS |  |  |
| ABBV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 22.6% above its 200-day average | 22.6% above | PASS |  |  |
| ABBV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.5B traded on an average day needs above $25M | $1,497,755,339 needs above $25,000,000 | PASS |  |  |
| ABBV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.87 | 12.87 | PASS |  |  |
| ABBV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 22.56% | 22.56% | PASS |  |  |
| ABBV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AIPO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.6% | TR -20.6% | PASS | LOW | the two cards divide by different roundings of the average |
| AIPO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AIPO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| AIPO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AIPO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AIPO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 46,714,696 | 46,715,321 | PASS |  |  |
| AIPO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AIPO | MR-price | price = the last completed close | 22.63 | 22.63 | PASS |  |  |
| AIPO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $22.63 needs above $10 | $22.63 needs above $10 | PASS |  |  |
| AIPO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.5 needs under 10 | 10.52 needs under 10 -> ✗ | PASS |  |  |
| AIPO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.6% below its 200-day average | 20.6% below | PASS |  |  |
| AIPO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $46.7M traded on an average day needs above $25M | $46,714,696 needs above $25,000,000 | PASS |  |  |
| AIPO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.52 | 10.52 | PASS |  |  |
| AIPO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.59% | -20.59% | PASS |  |  |
| AIPO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ALAB | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -18.0% | TR -18.0% | PASS | LOW | the two cards divide by different roundings of the average |
| ALAB | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ALAB | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| ALAB | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ALAB | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ALAB | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,188,661,804 | 1,188,661,795 | PASS |  |  |
| ALAB | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ALAB | MR-price | price = the last completed close | 211.6 | 211.6 | PASS |  |  |
| ALAB | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $211.60 needs above $10 | $211.60 needs above $10 | PASS |  |  |
| ALAB | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 47.4 needs under 10 | 47.39 needs under 10 -> ✗ | PASS |  |  |
| ALAB | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.0% below its 200-day average | 18.0% below | PASS |  |  |
| ALAB | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.2B traded on an average day needs above $25M | $1,188,661,804 needs above $25,000,000 | PASS |  |  |
| ALAB | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 47.39 | 47.39 | PASS |  |  |
| ALAB | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.99% | -17.99% | PASS |  |  |
| ALAB | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +18.2% | TR +18.2% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AMD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 18,509,288,047 | 18,509,288,086 | PASS |  |  |
| AMD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD | MR-price | price = the last completed close | 503.41 | 503.41 | PASS |  |  |
| AMD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $503.41 needs above $10 | $503.41 needs above $10 | PASS |  |  |
| AMD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.5 needs under 10 | 21.49 needs under 10 -> ✗ | PASS |  |  |
| AMD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 18.2% above its 200-day average | 18.2% above | PASS |  |  |
| AMD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $18.5B traded on an average day needs above $25M | $18,509,288,047 needs above $25,000,000 | PASS |  |  |
| AMD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.49 | 21.49 | PASS |  |  |
| AMD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 18.24% | 18.24% | PASS |  |  |
| AMD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +17.8% | TR +17.7% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AMD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 37,487,351 | 37,487,352 | PASS |  |  |
| AMD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD.TO | MR-price | price = the last completed close | 12.95 | 12.95 | PASS |  |  |
| AMD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $12.95 needs above $10 | $12.95 needs above $10 | PASS |  |  |
| AMD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.4 needs under 10 | 21.4 needs under 10 -> ✗ | PASS |  |  |
| AMD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 17.8% above its 200-day average | 17.8% above | PASS |  |  |
| AMD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $37.5M traded on an average day needs above $25M | $37,487,351 needs above $25,000,000 | PASS |  |  |
| AMD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.4 | 21.40 | PASS |  |  |
| AMD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 17.75% | 17.75% | PASS |  |  |
| AMD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMZN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +5.4% | TR +5.4% | PASS | LOW | the two cards divide by different roundings of the average |
| AMZN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AMZN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMZN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMZN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,718,377,505 | 12,718,377,498 | PASS |  |  |
| AMZN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMZN | MR-price | price = the last completed close | 257.89 | 257.89 | PASS |  |  |
| AMZN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $257.89 needs above $10 | $257.89 needs above $10 | PASS |  |  |
| AMZN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.4 needs under 10 | 10.42 needs under 10 -> ✗ | PASS |  |  |
| AMZN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 5.4% above its 200-day average | 5.4% above | PASS |  |  |
| AMZN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.7B traded on an average day needs above $25M | $12,718,377,505 needs above $25,000,000 | PASS |  |  |
| AMZN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.42 | 10.42 | PASS |  |  |
| AMZN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 5.36% | 5.36% | PASS |  |  |
| AMZN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMZU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +0.9% | TR +0.9% | PASS | LOW | the two cards divide by different roundings of the average |
| AMZU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AMZU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 65,943,620 | 65,943,620 | PASS |  |  |
| AMZU | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| AMZU | MR-price | price = the last completed close | 35.25 | 35.25 | PASS |  |  |
| AMZU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $35.25 needs above $10 | $35.25 needs above $10 | PASS |  |  |
| AMZU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.3 needs under 10 | 7.26 needs under 10 -> ✓ | PASS |  |  |
| AMZU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.9% above its 200-day average | 0.9% above | PASS |  |  |
| AMZU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $65.9M traded on an average day needs above $25M | $65,943,620 needs above $25,000,000 | PASS |  |  |
| AMZU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.26 | 7.26 | PASS |  |  |
| AMZU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.94% | 0.94% | PASS |  |  |
| AMZU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ANET.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ANET.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| ANET.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ANET.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ANET.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ANET.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ANET.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,552,640 | 2,552,641 | PASS |  |  |
| ANET.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ANET.TO | MR-price | price = the last completed close | 33.32 | 33.32 | PASS |  |  |
| ANET.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $33.32 needs above $10 | $33.32 needs above $10 | PASS |  |  |
| ANET.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.3 needs under 10 | 22.33 needs under 10 -> ✗ | PASS |  |  |
| ANET.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 10.6% above its 200-day average | 10.6% above | PASS |  |  |
| ANET.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.6M traded on an average day needs above $25M | $2,552,640 needs above $25,000,000 | PASS |  |  |
| ANET.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.33 | 22.33 | PASS |  |  |
| ANET.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 10.57% | 10.57% | PASS |  |  |
| ANET.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ASML.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -9.5% | TR -9.5% | PASS | LOW | the two cards divide by different roundings of the average |
| ASML.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ASML.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| ASML.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASML.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASML.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,747,418 | 2,747,429 | PASS |  |  |
| ASML.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ASML.TO | MR-price | price = the last completed close | 40.8 | 40.8 | PASS |  |  |
| ASML.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $40.80 needs above $10 | $40.80 needs above $10 | PASS |  |  |
| ASML.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.5 needs under 10 | 7.47 needs under 10 -> ✓ | PASS |  |  |
| ASML.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.5% below its 200-day average | 9.5% below | PASS |  |  |
| ASML.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,747,418 needs above $25,000,000 | PASS |  |  |
| ASML.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.47 | 7.47 | PASS |  |  |
| ASML.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.48% | -9.48% | PASS |  |  |
| ASML.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ASTL.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +15.8% | TR +15.8% | PASS | LOW | the two cards divide by different roundings of the average |
| ASTL.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ASTL.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the price is under $10; it does not trade enough dollars a day | the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| ASTL.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASTL.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASTL.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,114,991 | 6,114,992 | PASS |  |  |
| ASTL.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ASTL.TO | MR-price | price = the last completed close | 7.25 | 7.25 | PASS |  |  |
| ASTL.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $7.25 needs above $10 | $7.25 needs above $10 | PASS |  |  |
| ASTL.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.9 needs under 10 | 2.9 needs under 10 -> ✓ | PASS |  |  |
| ASTL.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 15.8% above its 200-day average | 15.8% above | PASS |  |  |
| ASTL.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $6.1M traded on an average day needs above $25M | $6,114,991 needs above $25,000,000 | PASS |  |  |
| ASTL.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.9 | 2.90 | PASS |  |  |
| ASTL.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 15.83% | 15.83% | PASS |  |  |
| ASTL.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ATD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.5% | TR +1.5% | PASS | LOW | the two cards divide by different roundings of the average |
| ATD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ATD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| ATD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ATD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 102,201,958 | 102,201,959 | PASS |  |  |
| ATD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ATD.TO | MR-price | price = the last completed close | 83.65 | 83.65 | PASS |  |  |
| ATD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $83.65 needs above $10 | $83.65 needs above $10 | PASS |  |  |
| ATD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 68.4 needs under 10 | 68.44 needs under 10 -> ✗ | PASS |  |  |
| ATD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.5% above its 200-day average | 1.5% above | PASS |  |  |
| ATD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $102.2M traded on an average day needs above $25M | $102,201,958 needs above $25,000,000 | PASS |  |  |
| ATD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 68.44 | 68.44 | PASS |  |  |
| ATD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.54% | 1.54% | PASS |  |  |
| ATD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AVGC | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| AVGO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -6.8% | TR -6.8% | PASS | LOW | the two cards divide by different roundings of the average |
| AVGO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AVGO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| AVGO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 9,173,137,260 | 9,173,137,272 | PASS |  |  |
| AVGO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AVGO | MR-price | price = the last completed close | 341.6 | 341.6 | PASS |  |  |
| AVGO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $341.60 needs above $10 | $341.60 needs above $10 | PASS |  |  |
| AVGO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 52.0 needs under 10 | 52.01 needs under 10 -> ✗ | PASS |  |  |
| AVGO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 6.8% below its 200-day average | 6.8% below | PASS |  |  |
| AVGO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $9.2B traded on an average day needs above $25M | $9,173,137,260 needs above $25,000,000 | PASS |  |  |
| AVGO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 52.01 | 52.01 | PASS |  |  |
| AVGO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -6.81% | -6.81% | PASS |  |  |
| AVGO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AVGO.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AVGO.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| AVGO.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 17,426,848 | 17,426,946 | PASS |  |  |
| AVGO.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AVGO.TO | MR-price | price = the last completed close | 12.94 | 12.94 | PASS |  |  |
| AVGO.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $12.94 needs above $10 | $12.94 needs above $10 | PASS |  |  |
| AVGO.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 52.0 needs under 10 | 52.02 needs under 10 -> ✗ | PASS |  |  |
| AVGO.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 7.7% below its 200-day average | 7.7% below | PASS |  |  |
| AVGO.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $17.4M traded on an average day needs above $25M | $17,426,848 needs above $25,000,000 | PASS |  |  |
| AVGO.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 52.02 | 52.02 | PASS |  |  |
| AVGO.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.69% | -7.68% | PASS |  |  |
| AVGO.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BDT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +21.5% | TR +21.5% | PASS | LOW | the two cards divide by different roundings of the average |
| BDT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| BDT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 28,898,177 | 28,898,170 | PASS |  |  |
| BDT.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| BDT.TO | MR-price | price = the last completed close | 71.13 | 71.13 | PASS |  |  |
| BDT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $71.13 needs above $10 | $71.13 needs above $10 | PASS |  |  |
| BDT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.6 needs under 10 | 6.59 needs under 10 -> ✓ | PASS |  |  |
| BDT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 21.5% above its 200-day average | 21.5% above | PASS |  |  |
| BDT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $28.9M traded on an average day needs above $25M | $28,898,177 needs above $25,000,000 | PASS |  |  |
| BDT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.59 | 6.59 | PASS |  |  |
| BDT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 21.46% | 21.46% | PASS |  |  |
| BDT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BOTZ | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -17.9% | TR -17.9% | PASS | LOW | the two cards divide by different roundings of the average |
| BOTZ | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| BOTZ | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| BOTZ | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BOTZ | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 28,612,117 | 28,612,118 | PASS |  |  |
| BOTZ | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BOTZ | MR-price | price = the last completed close | 29.71 | 29.71 | PASS |  |  |
| BOTZ | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $29.71 needs above $10 | $29.71 needs above $10 | PASS |  |  |
| BOTZ | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.9 needs under 10 | 4.91 needs under 10 -> ✓ | PASS |  |  |
| BOTZ | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 17.9% below its 200-day average | 17.9% below | PASS |  |  |
| BOTZ | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $28.6M traded on an average day needs above $25M | $28,612,117 needs above $25,000,000 | PASS |  |  |
| BOTZ | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.91 | 4.91 | PASS |  |  |
| BOTZ | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.93% | -17.92% | PASS |  |  |
| BOTZ | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BRK-B | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +17.0% | TR +17.0% | PASS | LOW | the two cards divide by different roundings of the average |
| BRK-B | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| BRK-B | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| BRK-B | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BRK-B | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,936,577,255 | 2,936,577,235 | PASS |  |  |
| BRK-B | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BRK-B | MR-price | price = the last completed close | 586.76 | 586.76 | PASS |  |  |
| BRK-B | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $586.76 needs above $10 | $586.76 needs above $10 | PASS |  |  |
| BRK-B | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.1 needs under 10 | 21.14 needs under 10 -> ✗ | PASS |  |  |
| BRK-B | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 17.0% above its 200-day average | 17.0% above | PASS |  |  |
| BRK-B | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.9B traded on an average day needs above $25M | $2,936,577,255 needs above $25,000,000 | PASS |  |  |
| BRK-B | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.14 | 21.14 | PASS |  |  |
| BRK-B | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 17% | 17.00% | PASS |  |  |
| BRK-B | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BRKU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +31.1% | TR +31.1% | PASS | LOW | the two cards divide by different roundings of the average |
| BRKU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| BRKU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| BRKU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BRKU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BRKU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,797,802 | 2,797,757 | PASS |  |  |
| BRKU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BRKU | MR-price | price = the last completed close | 30.19 | 30.19 | PASS |  |  |
| BRKU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $30.19 needs above $10 | $30.19 needs above $10 | PASS |  |  |
| BRKU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.6 needs under 10 | 21.57 needs under 10 -> ✗ | PASS |  |  |
| BRKU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 31.1% above its 200-day average | 31.1% above | PASS |  |  |
| BRKU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.8M traded on an average day needs above $25M | $2,797,802 needs above $25,000,000 | PASS |  |  |
| BRKU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.57 | 21.57 | PASS |  |  |
| BRKU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 31.08% | 31.08% | PASS |  |  |
| BRKU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CAMT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -38.7% | TR -38.7% | PASS | LOW | the two cards divide by different roundings of the average |
| CAMT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CAMT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| CAMT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAMT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAMT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 60,923,308 | 60,923,309 | PASS |  |  |
| CAMT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CAMT | MR-price | price = the last completed close | 94.96 | 94.96 | PASS |  |  |
| CAMT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $94.96 needs above $10 | $94.96 needs above $10 | PASS |  |  |
| CAMT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 28.3 needs under 10 | 28.34 needs under 10 -> ✗ | PASS |  |  |
| CAMT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 38.7% below its 200-day average | 38.7% below | PASS |  |  |
| CAMT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $60.9M traded on an average day needs above $25M | $60,923,308 needs above $25,000,000 | PASS |  |  |
| CAMT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 28.34 | 28.34 | PASS |  |  |
| CAMT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -38.68% | -38.68% | PASS |  |  |
| CAMT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CARS.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -28.9% | TR -28.9% | PASS | LOW | the two cards divide by different roundings of the average |
| CARS.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CARS.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| CARS.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CARS.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CARS.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CARS.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CARS.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 27,666 | 27,668 | PASS |  |  |
| CARS.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CARS.TO | MR-price | price = the last completed close | 19.88 | 19.88 | PASS |  |  |
| CARS.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $19.88 needs above $10 | $19.88 needs above $10 | PASS |  |  |
| CARS.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.4 needs under 10 | 7.41 needs under 10 -> ✓ | PASS |  |  |
| CARS.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 28.9% below its 200-day average | 28.9% below | PASS |  |  |
| CARS.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $27,666 traded on an average day needs above $25M | $27,666 needs above $25,000,000 | PASS |  |  |
| CARS.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.41 | 7.41 | PASS |  |  |
| CARS.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -28.92% | -28.92% | PASS |  |  |
| CARS.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CAT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -28.9% | TR -29.0% | PASS | LOW | the two cards divide by different roundings of the average |
| CAT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CAT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| CAT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,406,848,332 | 2,406,847,993 | PASS |  |  |
| CAT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CAT | MR-price | price = the last completed close | 570.79 | 570.79 | PASS |  |  |
| CAT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $570.79 needs above $10 | $570.79 needs above $10 | PASS |  |  |
| CAT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.0 needs under 10 | 12.96 needs under 10 -> ✗ | PASS |  |  |
| CAT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 28.9% below its 200-day average | 28.9% below | PASS |  |  |
| CAT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.4B traded on an average day needs above $25M | $2,406,848,332 needs above $25,000,000 | PASS |  |  |
| CAT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.96 | 12.96 | PASS |  |  |
| CAT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -28.95% | -28.95% | PASS |  |  |
| CAT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CCO.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -34.6% | TR -34.6% | PASS | LOW | the two cards divide by different roundings of the average |
| CCO.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CCO.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CCO.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CCO.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 154,249,560 | 154,249,560 | PASS |  |  |
| CCO.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CCO.TO | MR-price | price = the last completed close | 92.16 | 92.16 | PASS |  |  |
| CCO.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $92.16 needs above $10 | $92.16 needs above $10 | PASS |  |  |
| CCO.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.2 needs under 10 | 4.19 needs under 10 -> ✓ | PASS |  |  |
| CCO.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 34.6% below its 200-day average | 34.6% below | PASS |  |  |
| CCO.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $154.2M traded on an average day needs above $25M | $154,249,560 needs above $25,000,000 | PASS |  |  |
| CCO.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.19 | 4.19 | PASS |  |  |
| CCO.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -34.59% | -34.59% | PASS |  |  |
| CCO.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CEG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -3.4% | TR -3.4% | PASS | LOW | the two cards divide by different roundings of the average |
| CEG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CEG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| CEG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CEG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CEG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 994,361,912 | 994,363,771 | PASS |  |  |
| CEG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CEG | MR-price | price = the last completed close | 268.07 | 268.07 | PASS |  |  |
| CEG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $268.07 needs above $10 | $268.07 needs above $10 | PASS |  |  |
| CEG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.0 needs under 10 | 14 needs under 10 -> ✗ | PASS |  |  |
| CEG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 3.4% below its 200-day average | 3.4% below | PASS |  |  |
| CEG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $994.4M traded on an average day needs above $25M | $994,361,912 needs above $25,000,000 | PASS |  |  |
| CEG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14 | 14.00 | PASS |  |  |
| CEG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -3.38% | -3.38% | PASS |  |  |
| CEG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CGY.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +6.9% | TR +6.9% | PASS | LOW | the two cards divide by different roundings of the average |
| CGY.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CGY.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| CGY.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CGY.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CGY.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,530,340 | 2,530,340 | PASS |  |  |
| CGY.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CGY.TO | MR-price | price = the last completed close | 84.3 | 84.3 | PASS |  |  |
| CGY.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $84.30 needs above $10 | $84.30 needs above $10 | PASS |  |  |
| CGY.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.7 needs under 10 | 12.69 needs under 10 -> ✗ | PASS |  |  |
| CGY.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 6.9% above its 200-day average | 6.9% above | PASS |  |  |
| CGY.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.5M traded on an average day needs above $25M | $2,530,340 needs above $25,000,000 | PASS |  |  |
| CGY.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.69 | 12.69 | PASS |  |  |
| CGY.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 6.94% | 6.94% | PASS |  |  |
| CGY.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CNQ.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +6.5% | TR +6.5% | PASS | LOW | the two cards divide by different roundings of the average |
| CNQ.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CNQ.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CNQ.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CNQ.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 575,667,725 | 575,667,720 | PASS |  |  |
| CNQ.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CNQ.TO | MR-price | price = the last completed close | 68.29 | 68.29 | PASS |  |  |
| CNQ.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $68.29 needs above $10 | $68.29 needs above $10 | PASS |  |  |
| CNQ.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 17.7 needs under 10 | 17.69 needs under 10 -> ✗ | PASS |  |  |
| CNQ.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 6.5% above its 200-day average | 6.5% above | PASS |  |  |
| CNQ.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $575.7M traded on an average day needs above $25M | $575,667,725 needs above $25,000,000 | PASS |  |  |
| CNQ.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 17.69 | 17.69 | PASS |  |  |
| CNQ.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 6.48% | 6.48% | PASS |  |  |
| CNQ.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CNR.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +11.6% | TR +11.6% | PASS | LOW | the two cards divide by different roundings of the average |
| CNR.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CNR.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CNR.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CNR.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 216,751,150 | 216,751,151 | PASS |  |  |
| CNR.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CNR.TO | MR-price | price = the last completed close | 180.54 | 180.54 | PASS |  |  |
| CNR.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $180.54 needs above $10 | $180.54 needs above $10 | PASS |  |  |
| CNR.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 28.7 needs under 10 | 28.7 needs under 10 -> ✗ | PASS |  |  |
| CNR.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 11.6% above its 200-day average | 11.6% above | PASS |  |  |
| CNR.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $216.8M traded on an average day needs above $25M | $216,751,150 needs above $25,000,000 | PASS |  |  |
| CNR.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 28.7 | 28.70 | PASS |  |  |
| CNR.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 11.63% | 11.63% | PASS |  |  |
| CNR.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COP | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +14.3% | TR +14.3% | PASS | LOW | the two cards divide by different roundings of the average |
| COP | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| COP | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| COP | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COP | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,038,668,164 | 1,038,661,109 | PASS |  |  |
| COP | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COP | MR-price | price = the last completed close | 139.48 | 139.48 | PASS |  |  |
| COP | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $139.48 needs above $10 | $139.48 needs above $10 | PASS |  |  |
| COP | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 40.0 needs under 10 | 40.04 needs under 10 -> ✗ | PASS |  |  |
| COP | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 14.3% above its 200-day average | 14.3% above | PASS |  |  |
| COP | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1B traded on an average day needs above $25M | $1,038,668,164 needs above $25,000,000 | PASS |  |  |
| COP | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 40.04 | 40.06 | PASS |  |  |
| COP | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 14.29% | 14.29% | PASS |  |  |
| COP | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPP.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.8% | TR -20.8% | PASS | LOW | the two cards divide by different roundings of the average |
| COPP.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| COPP.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| COPP.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPP.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPP.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPP.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPP.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 793,339 | 793,339 | PASS |  |  |
| COPP.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COPP.TO | MR-price | price = the last completed close | 46.42 | 46.42 | PASS |  |  |
| COPP.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $46.42 needs above $10 | $46.42 needs above $10 | PASS |  |  |
| COPP.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.3 needs under 10 | 4.35 needs under 10 -> ✓ | PASS |  |  |
| COPP.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.8% below its 200-day average | 20.8% below | PASS |  |  |
| COPP.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $793,339 traded on an average day needs above $25M | $793,339 needs above $25,000,000 | PASS |  |  |
| COPP.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.35 | 4.35 | PASS |  |  |
| COPP.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.83% | -20.83% | PASS |  |  |
| COPP.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.8% | TR -20.7% | PASS | LOW | the two cards divide by different roundings of the average |
| COPX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| COPX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| COPX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 247,928,227 | 247,928,228 | PASS |  |  |
| COPX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COPX | MR-price | price = the last completed close | 65.31 | 65.31 | PASS |  |  |
| COPX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $65.31 needs above $10 | $65.31 needs above $10 | PASS |  |  |
| COPX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.7 needs under 10 | 3.69 needs under 10 -> ✓ | PASS |  |  |
| COPX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.8% below its 200-day average | 20.8% below | PASS |  |  |
| COPX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $247.9M traded on an average day needs above $25M | $247,928,227 needs above $25,000,000 | PASS |  |  |
| COPX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.69 | 3.69 | PASS |  |  |
| COPX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.75% | -20.75% | PASS |  |  |
| COPX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPZ | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| COST | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +13.9% | TR +13.9% | PASS | LOW | the two cards divide by different roundings of the average |
| COST | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| COST | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| COST | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COST | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,569,096,398 | 2,569,098,018 | PASS |  |  |
| COST | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COST | MR-price | price = the last completed close | 1110.08 | 1110.08 | PASS |  |  |
| COST | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,110.08 needs above $10 | $1,110.08 needs above $10 | PASS |  |  |
| COST | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 71.6 needs under 10 | 71.61 needs under 10 -> ✗ | PASS |  |  |
| COST | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 13.9% above its 200-day average | 13.9% above | PASS |  |  |
| COST | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.6B traded on an average day needs above $25M | $2,569,096,398 needs above $25,000,000 | PASS |  |  |
| COST | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 71.61 | 71.61 | PASS |  |  |
| COST | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13.91% | 13.91% | PASS |  |  |
| COST | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COTG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +21.6% | TR +21.6% | PASS | LOW | the two cards divide by different roundings of the average |
| COTG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| COTG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| COTG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COTG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COTG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COTG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COTG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,037,444 | 1,037,565 | PASS |  |  |
| COTG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COTG | MR-price | price = the last completed close | 16.93 | 16.93 | PASS |  |  |
| COTG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $16.93 needs above $10 | $16.93 needs above $10 | PASS |  |  |
| COTG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 69.4 needs under 10 | 69.38 needs under 10 -> ✗ | PASS |  |  |
| COTG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 21.6% above its 200-day average | 21.6% above | PASS |  |  |
| COTG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1M traded on an average day needs above $25M | $1,037,444 needs above $25,000,000 | PASS |  |  |
| COTG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 21.65% | 21.66% | PASS |  |  |
| COTG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CSU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +17.9% | TR +17.9% | PASS | LOW | the two cards divide by different roundings of the average |
| CSU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CSU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 209,829,865 | 209,829,865 | PASS |  |  |
| CSU.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| CSU.TO | MR-price | price = the last completed close | 3316.93 | 3316.93 | PASS |  |  |
| CSU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $3,316.93 needs above $10 | $3,316.93 needs above $10 | PASS |  |  |
| CSU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.5 needs under 10 | 5.45 needs under 10 -> ✓ | PASS |  |  |
| CSU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 17.9% above its 200-day average | 17.9% above | PASS |  |  |
| CSU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $209.8M traded on an average day needs above $25M | $209,829,865 needs above $25,000,000 | PASS |  |  |
| CSU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.45 | 5.45 | PASS |  |  |
| CSU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 17.92% | 17.92% | PASS |  |  |
| CSU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CVX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +11.2% | TR +11.2% | PASS | LOW | the two cards divide by different roundings of the average |
| CVX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| CVX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CVX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CVX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,805,763,454 | 1,805,763,447 | PASS |  |  |
| CVX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CVX | MR-price | price = the last completed close | 216.13 | 216.13 | PASS |  |  |
| CVX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $216.13 needs above $10 | $216.13 needs above $10 | PASS |  |  |
| CVX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 36.5 needs under 10 | 36.53 needs under 10 -> ✗ | PASS |  |  |
| CVX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 11.2% above its 200-day average | 11.2% above | PASS |  |  |
| CVX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.8B traded on an average day needs above $25M | $1,805,763,454 needs above $25,000,000 | PASS |  |  |
| CVX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 36.53 | 36.53 | PASS |  |  |
| CVX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 11.18% | 11.18% | PASS |  |  |
| CVX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DRAL | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| DRAM | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| DRIV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -21.1% | TR -21.1% | PASS | LOW | the two cards divide by different roundings of the average |
| DRIV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| DRIV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| DRIV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DRIV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DRIV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DRIV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DRIV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,144,380 | 1,144,358 | PASS |  |  |
| DRIV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DRIV | MR-price | price = the last completed close | 27 | 27 | PASS |  |  |
| DRIV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $27.00 needs above $10 | $27.00 needs above $10 | PASS |  |  |
| DRIV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.4 needs under 10 | 4.44 needs under 10 -> ✓ | PASS |  |  |
| DRIV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 21.1% below its 200-day average | 21.1% below | PASS |  |  |
| DRIV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.1M traded on an average day needs above $25M | $1,144,380 needs above $25,000,000 | PASS |  |  |
| DRIV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.44 | 4.48 | PASS |  |  |
| DRIV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -21.1% | -21.09% | PASS |  |  |
| DRIV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DUK | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +5.8% | TR +5.8% | PASS | LOW | the two cards divide by different roundings of the average |
| DUK | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| DUK | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| DUK | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DUK | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 612,423,376 | 612,423,814 | PASS |  |  |
| DUK | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DUK | MR-price | price = the last completed close | 129.84 | 129.84 | PASS |  |  |
| DUK | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $129.84 needs above $10 | $129.84 needs above $10 | PASS |  |  |
| DUK | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 59.3 needs under 10 | 59.29 needs under 10 -> ✗ | PASS |  |  |
| DUK | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 5.8% above its 200-day average | 5.8% above | PASS |  |  |
| DUK | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $612.4M traded on an average day needs above $25M | $612,423,376 needs above $25,000,000 | PASS |  |  |
| DUK | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 59.29 | 59.30 | PASS |  |  |
| DUK | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 5.79% | 5.79% | PASS |  |  |
| DUK | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ELIL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +49.0% | TR +49.1% | PASS | LOW | the two cards divide by different roundings of the average |
| ELIL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ELIL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| ELIL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ELIL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ELIL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,705,003 | 2,704,980 | PASS |  |  |
| ELIL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ELIL | MR-price | price = the last completed close | 40.25 | 40.25 | PASS |  |  |
| ELIL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $40.25 needs above $10 | $40.25 needs above $10 | PASS |  |  |
| ELIL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 18.6 needs under 10 | 18.59 needs under 10 -> ✗ | PASS |  |  |
| ELIL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 49.0% above its 200-day average | 49.0% above | PASS |  |  |
| ELIL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,705,003 needs above $25,000,000 | PASS |  |  |
| ELIL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 18.59 | 18.56 | PASS |  |  |
| ELIL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 49.05% | 49.05% | PASS |  |  |
| ELIL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| EQIX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.5% | TR +1.5% | PASS | LOW | the two cards divide by different roundings of the average |
| EQIX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| EQIX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| EQIX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| EQIX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 723,710,155 | 723,710,150 | PASS |  |  |
| EQIX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| EQIX | MR-price | price = the last completed close | 1034.83 | 1034.83 | PASS |  |  |
| EQIX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,034.83 needs above $10 | $1,034.83 needs above $10 | PASS |  |  |
| EQIX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.2 needs under 10 | 12.17 needs under 10 -> ✗ | PASS |  |  |
| EQIX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.5% above its 200-day average | 1.5% above | PASS |  |  |
| EQIX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $723.7M traded on an average day needs above $25M | $723,710,155 needs above $25,000,000 | PASS |  |  |
| EQIX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.17 | 12.17 | PASS |  |  |
| EQIX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.53% | 1.53% | PASS |  |  |
| EQIX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ETN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.7% | TR -14.7% | PASS | LOW | the two cards divide by different roundings of the average |
| ETN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ETN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ETN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ETN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,160,203,086 | 1,160,202,187 | PASS |  |  |
| ETN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ETN | MR-price | price = the last completed close | 337.11 | 337.11 | PASS |  |  |
| ETN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $337.11 needs above $10 | $337.11 needs above $10 | PASS |  |  |
| ETN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.4 needs under 10 | 9.4 needs under 10 -> ✓ | PASS |  |  |
| ETN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.7% below its 200-day average | 14.7% below | PASS |  |  |
| ETN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.2B traded on an average day needs above $25M | $1,160,203,086 needs above $25,000,000 | PASS |  |  |
| ETN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.4 | 9.40 | PASS |  |  |
| ETN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.73% | -14.73% | PASS |  |  |
| ETN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| FCX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.8% | TR -14.8% | PASS | LOW | the two cards divide by different roundings of the average |
| FCX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| FCX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| FCX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FCX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 789,799,320 | 789,799,321 | PASS |  |  |
| FCX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| FCX | MR-price | price = the last completed close | 55.3 | 55.3 | PASS |  |  |
| FCX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $55.30 needs above $10 | $55.30 needs above $10 | PASS |  |  |
| FCX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.7 needs under 10 | 9.73 needs under 10 -> ✓ | PASS |  |  |
| FCX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.8% below its 200-day average | 14.8% below | PASS |  |  |
| FCX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $789.8M traded on an average day needs above $25M | $789,799,320 needs above $25,000,000 | PASS |  |  |
| FCX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.73 | 9.73 | PASS |  |  |
| FCX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.8% | -14.80% | PASS |  |  |
| FCX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| FINN.NE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +5.6% | TR +5.6% | PASS | LOW | the two cards divide by different roundings of the average |
| FINN.NE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| FINN.NE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it does not trade enough dollars a day | it does not trade enough dollars a day | PASS |  |  |
| FINN.NE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FINN.NE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FINN.NE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FINN.NE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FINN.NE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,100,935 | 12,100,935 | PASS |  |  |
| FINN.NE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| FINN.NE | MR-price | price = the last completed close | 31.76 | 31.76 | PASS |  |  |
| FINN.NE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $31.76 needs above $10 | $31.76 needs above $10 | PASS |  |  |
| FINN.NE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.8 needs under 10 | 6.8 needs under 10 -> ✓ | PASS |  |  |
| FINN.NE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 5.6% above its 200-day average | 5.6% above | PASS |  |  |
| FINN.NE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $12.1M traded on an average day needs above $25M | $12,100,935 needs above $25,000,000 | PASS |  |  |
| FINN.NE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.8 | 6.80 | PASS |  |  |
| FINN.NE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 5.58% | 5.58% | PASS |  |  |
| FINN.NE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GDX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.0% | TR -11.0% | PASS | LOW | the two cards divide by different roundings of the average |
| GDX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GDX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GDX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,990,891,054 | 1,990,891,085 | PASS |  |  |
| GDX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GDX | MR-price | price = the last completed close | 79.57 | 79.57 | PASS |  |  |
| GDX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $79.57 needs above $10 | $79.57 needs above $10 | PASS |  |  |
| GDX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 25.8 needs under 10 | 25.79 needs under 10 -> ✗ | PASS |  |  |
| GDX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.0% below its 200-day average | 11.0% below | PASS |  |  |
| GDX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2B traded on an average day needs above $25M | $1,990,891,054 needs above $25,000,000 | PASS |  |  |
| GDX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 25.79 | 25.79 | PASS |  |  |
| GDX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.03% | -11.03% | PASS |  |  |
| GDX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GDXU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -31.4% | TR -31.4% | PASS | LOW | the two cards divide by different roundings of the average |
| GDXU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GDXU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| GDXU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDXU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 7,979,993 | 7,979,993 | PASS |  |  |
| GDXU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GDXU.TO | MR-price | price = the last completed close | 24.6 | 24.6 | PASS |  |  |
| GDXU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $24.60 needs above $10 | $24.60 needs above $10 | PASS |  |  |
| GDXU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.1 needs under 10 | 21.12 needs under 10 -> ✗ | PASS |  |  |
| GDXU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 31.4% below its 200-day average | 31.4% below | PASS |  |  |
| GDXU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $8M traded on an average day needs above $25M | $7,979,993 needs above $25,000,000 | PASS |  |  |
| GDXU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.12 | 21.12 | PASS |  |  |
| GDXU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -31.44% | -31.44% | PASS |  |  |
| GDXU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +0.9% | TR +0.9% | PASS | LOW | the two cards divide by different roundings of the average |
| GE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| GE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,643,469,536 | 1,643,469,529 | PASS |  |  |
| GE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GE | MR-price | price = the last completed close | 326.4 | 326.4 | PASS |  |  |
| GE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $326.40 needs above $10 | $326.40 needs above $10 | PASS |  |  |
| GE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 30.4 needs under 10 | 30.4 needs under 10 -> ✗ | PASS |  |  |
| GE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.9% above its 200-day average | 0.9% above | PASS |  |  |
| GE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.6B traded on an average day needs above $25M | $1,643,469,536 needs above $25,000,000 | PASS |  |  |
| GE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 30.4 | 30.40 | PASS |  |  |
| GE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.93% | 0.93% | PASS |  |  |
| GE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GEV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -18.0% | TR -18.0% | PASS | LOW | the two cards divide by different roundings of the average |
| GEV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GEV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GEV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,702,288,576 | 3,702,289,244 | PASS |  |  |
| GEV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GEV | MR-price | price = the last completed close | 779.91 | 779.91 | PASS |  |  |
| GEV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $779.91 needs above $10 | $779.91 needs above $10 | PASS |  |  |
| GEV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 43.5 needs under 10 | 43.48 needs under 10 -> ✗ | PASS |  |  |
| GEV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.0% below its 200-day average | 18.0% below | PASS |  |  |
| GEV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3.7B traded on an average day needs above $25M | $3,702,288,576 needs above $25,000,000 | PASS |  |  |
| GEV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 43.48 | 43.48 | PASS |  |  |
| GEV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -18.02% | -18.02% | PASS |  |  |
| GEV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GEV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GEV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| GEV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,573,301 | 6,573,315 | PASS |  |  |
| GEV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GEV.TO | MR-price | price = the last completed close | 52.13 | 52.13 | PASS |  |  |
| GEV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $52.13 needs above $10 | $52.13 needs above $10 | PASS |  |  |
| GEV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 43.7 needs under 10 | 43.71 needs under 10 -> ✗ | PASS |  |  |
| GEV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.7% below its 200-day average | 18.7% below | PASS |  |  |
| GEV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $6.6M traded on an average day needs above $25M | $6,573,301 needs above $25,000,000 | PASS |  |  |
| GEV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 43.71 | 43.71 | PASS |  |  |
| GEV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -18.66% | -18.66% | PASS |  |  |
| GEV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GGLL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -38.2% | TR -38.2% | PASS | LOW | the two cards divide by different roundings of the average |
| GGLL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GGLL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GGLL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GGLL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 196,868,574 | 196,868,574 | PASS |  |  |
| GGLL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GGLL | MR-price | price = the last completed close | 63.05 | 63.05 | PASS |  |  |
| GGLL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $63.05 needs above $10 | $63.05 needs above $10 | PASS |  |  |
| GGLL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.4 needs under 10 | 9.43 needs under 10 -> ✓ | PASS |  |  |
| GGLL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 38.2% below its 200-day average | 38.2% below | PASS |  |  |
| GGLL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $196.9M traded on an average day needs above $25M | $196,868,574 needs above $25,000,000 | PASS |  |  |
| GGLL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.43 | 9.43 | PASS |  |  |
| GGLL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -38.21% | -38.21% | PASS |  |  |
| GGLL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GIB-A.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +15.3% | TR +15.3% | PASS | LOW | the two cards divide by different roundings of the average |
| GIB-A.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GIB-A.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| GIB-A.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GIB-A.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 79,510,650 | 79,510,651 | PASS |  |  |
| GIB-A.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GIB-A.TO | MR-price | price = the last completed close | 115.07 | 115.07 | PASS |  |  |
| GIB-A.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $115.07 needs above $10 | $115.07 needs above $10 | PASS |  |  |
| GIB-A.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.4 needs under 10 | 10.44 needs under 10 -> ✗ | PASS |  |  |
| GIB-A.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 15.3% above its 200-day average | 15.3% above | PASS |  |  |
| GIB-A.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $79.5M traded on an average day needs above $25M | $79,510,650 needs above $25,000,000 | PASS |  |  |
| GIB-A.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.44 | 10.44 | PASS |  |  |
| GIB-A.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 15.29% | 15.29% | PASS |  |  |
| GIB-A.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GOOGL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -17.0% | TR -17.0% | PASS | LOW | the two cards divide by different roundings of the average |
| GOOGL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GOOGL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GOOGL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GOOGL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,403,335,480 | 12,403,335,411 | PASS |  |  |
| GOOGL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GOOGL | MR-price | price = the last completed close | 280.2 | 280.2 | PASS |  |  |
| GOOGL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $280.20 needs above $10 | $280.20 needs above $10 | PASS |  |  |
| GOOGL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.8 needs under 10 | 9.81 needs under 10 -> ✓ | PASS |  |  |
| GOOGL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 17.0% below its 200-day average | 17.0% below | PASS |  |  |
| GOOGL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.4B traded on an average day needs above $25M | $12,403,335,480 needs above $25,000,000 | PASS |  |  |
| GOOGL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.81 | 9.81 | PASS |  |  |
| GOOGL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.01% | -17.01% | PASS |  |  |
| GOOGL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GRID | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -12.8% | TR -12.8% | PASS | LOW | the two cards divide by different roundings of the average |
| GRID | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| GRID | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GRID | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GRID | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 110,369,653 | 110,369,654 | PASS |  |  |
| GRID | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GRID | MR-price | price = the last completed close | 155.15 | 155.15 | PASS |  |  |
| GRID | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $155.15 needs above $10 | $155.15 needs above $10 | PASS |  |  |
| GRID | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.3 needs under 10 | 8.26 needs under 10 -> ✓ | PASS |  |  |
| GRID | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 12.8% below its 200-day average | 12.8% below | PASS |  |  |
| GRID | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $110.4M traded on an average day needs above $25M | $110,369,653 needs above $25,000,000 | PASS |  |  |
| GRID | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8.26 | 8.26 | PASS |  |  |
| GRID | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -12.81% | -12.81% | PASS |  |  |
| GRID | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +3.0% | TR +3.0% | PASS | LOW | the two cards divide by different roundings of the average |
| HD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| HD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,586,965,545 | 1,586,965,530 | PASS |  |  |
| HD | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| HD | MR-price | price = the last completed close | 339.01 | 339.01 | PASS |  |  |
| HD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $339.01 needs above $10 | $339.01 needs above $10 | PASS |  |  |
| HD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.3 needs under 10 | 3.34 needs under 10 -> ✓ | PASS |  |  |
| HD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 3.0% above its 200-day average | 3.0% above | PASS |  |  |
| HD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.6B traded on an average day needs above $25M | $1,586,965,545 needs above $25,000,000 | PASS |  |  |
| HD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.34 | 3.34 | PASS |  |  |
| HD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.99% | 2.99% | PASS |  |  |
| HD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HURA.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -29.5% | TR -29.5% | PASS | LOW | the two cards divide by different roundings of the average |
| HURA.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| HURA.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| HURA.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HURA.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HURA.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HURA.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HURA.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 511,007 | 511,007 | PASS |  |  |
| HURA.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HURA.TO | MR-price | price = the last completed close | 37.39 | 37.39 | PASS |  |  |
| HURA.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $37.39 needs above $10 | $37.39 needs above $10 | PASS |  |  |
| HURA.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.1 needs under 10 | 6.13 needs under 10 -> ✓ | PASS |  |  |
| HURA.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 29.5% below its 200-day average | 29.5% below | PASS |  |  |
| HURA.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $511,007 traded on an average day needs above $25M | $511,007 needs above $25,000,000 | PASS |  |  |
| HURA.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.13 | 6.13 | PASS |  |  |
| HURA.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -29.49% | -29.49% | PASS |  |  |
| HURA.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HXQ.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.4% | TR -1.4% | PASS | LOW | the two cards divide by different roundings of the average |
| HXQ.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| HXQ.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| HXQ.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HXQ.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HXQ.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,267,104 | 5,267,104 | PASS |  |  |
| HXQ.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HXQ.TO | MR-price | price = the last completed close | 110.63 | 110.63 | PASS |  |  |
| HXQ.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $110.63 needs above $10 | $110.63 needs above $10 | PASS |  |  |
| HXQ.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.0 needs under 10 | 8.03 needs under 10 -> ✓ | PASS |  |  |
| HXQ.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.4% below its 200-day average | 1.4% below | PASS |  |  |
| HXQ.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $5.3M traded on an average day needs above $25M | $5,267,104 needs above $25,000,000 | PASS |  |  |
| HXQ.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8.03 | 8.03 | PASS |  |  |
| HXQ.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.43% | -1.43% | PASS |  |  |
| HXQ.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| JNJ | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +12.0% | TR +12.0% | PASS | LOW | the two cards divide by different roundings of the average |
| JNJ | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| JNJ | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| JNJ | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| JNJ | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,040,149,867 | 2,040,149,863 | PASS |  |  |
| JNJ | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| JNJ | MR-price | price = the last completed close | 278.7 | 278.7 | PASS |  |  |
| JNJ | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $278.70 needs above $10 | $278.70 needs above $10 | PASS |  |  |
| JNJ | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 16.4 needs under 10 | 16.44 needs under 10 -> ✗ | PASS |  |  |
| JNJ | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 12.0% above its 200-day average | 12.0% above | PASS |  |  |
| JNJ | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2B traded on an average day needs above $25M | $2,040,149,867 needs above $25,000,000 | PASS |  |  |
| JNJ | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 16.44 | 16.44 | PASS |  |  |
| JNJ | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 11.99% | 11.99% | PASS |  |  |
| JNJ | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| JPM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +2.2% | TR +2.2% | PASS | LOW | the two cards divide by different roundings of the average |
| JPM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| JPM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,215,977,880 | 2,215,977,898 | PASS |  |  |
| JPM | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| JPM | MR-price | price = the last completed close | 329.96 | 329.96 | PASS |  |  |
| JPM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $329.96 needs above $10 | $329.96 needs above $10 | PASS |  |  |
| JPM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.0 needs under 10 | 7.97 needs under 10 -> ✓ | PASS |  |  |
| JPM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 2.2% above its 200-day average | 2.2% above | PASS |  |  |
| JPM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.2B traded on an average day needs above $25M | $2,215,977,880 needs above $25,000,000 | PASS |  |  |
| JPM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.97 | 7.97 | PASS |  |  |
| JPM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.23% | 2.23% | PASS |  |  |
| JPM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| KEYS | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.4% | TR -11.4% | PASS | LOW | the two cards divide by different roundings of the average |
| KEYS | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| KEYS | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| KEYS | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| KEYS | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| KEYS | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 466,786,305 | 466,786,306 | PASS |  |  |
| KEYS | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| KEYS | MR-price | price = the last completed close | 284.45 | 284.45 | PASS |  |  |
| KEYS | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $284.45 needs above $10 | $284.45 needs above $10 | PASS |  |  |
| KEYS | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.6 needs under 10 | 12.62 needs under 10 -> ✗ | PASS |  |  |
| KEYS | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.4% below its 200-day average | 11.4% below | PASS |  |  |
| KEYS | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $466.8M traded on an average day needs above $25M | $466,786,305 needs above $25,000,000 | PASS |  |  |
| KEYS | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.62 | 12.62 | PASS |  |  |
| KEYS | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.42% | -11.42% | PASS |  |  |
| KEYS | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| LIN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +4.0% | TR +4.0% | PASS | LOW | the two cards divide by different roundings of the average |
| LIN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| LIN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| LIN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| LIN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,079,917,534 | 1,079,917,546 | PASS |  |  |
| LIN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| LIN | MR-price | price = the last completed close | 515.11 | 515.11 | PASS |  |  |
| LIN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $515.11 needs above $10 | $515.11 needs above $10 | PASS |  |  |
| LIN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.6 needs under 10 | 11.63 needs under 10 -> ✗ | PASS |  |  |
| LIN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 4.0% above its 200-day average | 4.0% above | PASS |  |  |
| LIN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,079,917,534 needs above $25,000,000 | PASS |  |  |
| LIN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.63 | 11.63 | PASS |  |  |
| LIN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 4.02% | 4.02% | PASS |  |  |
| LIN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| LLY | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +27.5% | TR +27.5% | PASS | LOW | the two cards divide by different roundings of the average |
| LLY | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| LLY | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| LLY | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| LLY | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 4,164,737,862 | 4,164,738,571 | PASS |  |  |
| LLY | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| LLY | MR-price | price = the last completed close | 1415.55 | 1415.55 | PASS |  |  |
| LLY | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,415.55 needs above $10 | $1,415.55 needs above $10 | PASS |  |  |
| LLY | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.3 needs under 10 | 21.29 needs under 10 -> ✗ | PASS |  |  |
| LLY | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 27.5% above its 200-day average | 27.5% above | PASS |  |  |
| LLY | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $4.2B traded on an average day needs above $25M | $4,164,737,862 needs above $25,000,000 | PASS |  |  |
| LLY | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.29 | 21.29 | PASS |  |  |
| LLY | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 27.51% | 27.51% | PASS |  |  |
| LLY | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MDA.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -12.2% | TR -12.3% | PASS | LOW | the two cards divide by different roundings of the average |
| MDA.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| MDA.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| MDA.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MDA.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 58,891,212 | 58,891,213 | PASS |  |  |
| MDA.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MDA.TO | MR-price | price = the last completed close | 39.22 | 39.22 | PASS |  |  |
| MDA.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $39.22 needs above $10 | $39.22 needs above $10 | PASS |  |  |
| MDA.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.4 needs under 10 | 5.41 needs under 10 -> ✓ | PASS |  |  |
| MDA.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 12.3% below its 200-day average | 12.2% below | PASS |  |  |
| MDA.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $58.9M traded on an average day needs above $25M | $58,891,212 needs above $25,000,000 | PASS |  |  |
| MDA.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.41 | 5.41 | PASS |  |  |
| MDA.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -12.25% | -12.25% | PASS |  |  |
| MDA.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| META | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.6% | TR -1.6% | PASS | LOW | the two cards divide by different roundings of the average |
| META | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| META | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| META | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| META | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| META | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,685,062,637 | 14,685,062,619 | PASS |  |  |
| META | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| META | MR-price | price = the last completed close | 618.87 | 618.87 | PASS |  |  |
| META | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $618.87 needs above $10 | $618.87 needs above $10 | PASS |  |  |
| META | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 23.3 needs under 10 | 23.31 needs under 10 -> ✗ | PASS |  |  |
| META | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.6% below its 200-day average | 1.6% below | PASS |  |  |
| META | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $14.7B traded on an average day needs above $25M | $14,685,062,637 needs above $25,000,000 | PASS |  |  |
| META | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 23.31 | 23.31 | PASS |  |  |
| META | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.63% | -1.63% | PASS |  |  |
| META | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| METU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.5% | TR -14.5% | PASS | LOW | the two cards divide by different roundings of the average |
| METU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| METU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| METU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| METU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| METU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 110,679,908 | 110,679,908 | PASS |  |  |
| METU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| METU | MR-price | price = the last completed close | 21.57 | 21.57 | PASS |  |  |
| METU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $21.57 needs above $10 | $21.57 needs above $10 | PASS |  |  |
| METU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.4 needs under 10 | 22.38 needs under 10 -> ✗ | PASS |  |  |
| METU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.5% below its 200-day average | 14.5% below | PASS |  |  |
| METU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $110.7M traded on an average day needs above $25M | $110,679,908 needs above $25,000,000 | PASS |  |  |
| METU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.38 | 22.38 | PASS |  |  |
| METU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.51% | -14.51% | PASS |  |  |
| METU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MRVL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.7% | TR -20.7% | PASS | LOW | the two cards divide by different roundings of the average |
| MRVL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| MRVL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| MRVL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MRVL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MRVL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,436,483,716 | 5,436,483,705 | PASS |  |  |
| MRVL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MRVL | MR-price | price = the last completed close | 148.74 | 148.74 | PASS |  |  |
| MRVL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $148.74 needs above $10 | $148.74 needs above $10 | PASS |  |  |
| MRVL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 35.4 needs under 10 | 35.36 needs under 10 -> ✗ | PASS |  |  |
| MRVL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.7% below its 200-day average | 20.7% below | PASS |  |  |
| MRVL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.4B traded on an average day needs above $25M | $5,436,483,716 needs above $25,000,000 | PASS |  |  |
| MRVL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 35.36 | 35.36 | PASS |  |  |
| MRVL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.72% | -20.72% | PASS |  |  |
| MRVL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MSFT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +14.7% | TR +14.7% | PASS | LOW | the two cards divide by different roundings of the average |
| MSFT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| MSFT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,522,504,700 | 14,522,504,823 | PASS |  |  |
| MSFT | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| MSFT | MR-price | price = the last completed close | 506.24 | 506.24 | PASS |  |  |
| MSFT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $506.24 needs above $10 | $506.24 needs above $10 | PASS |  |  |
| MSFT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.6 needs under 10 | 4.57 needs under 10 -> ✓ | PASS |  |  |
| MSFT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 14.7% above its 200-day average | 14.7% above | PASS |  |  |
| MSFT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $14.5B traded on an average day needs above $25M | $14,522,504,700 needs above $25,000,000 | PASS |  |  |
| MSFT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.57 | 4.57 | PASS |  |  |
| MSFT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 14.7% | 14.70% | PASS |  |  |
| MSFT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MSFU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +20.3% | TR +20.3% | PASS | LOW | the two cards divide by different roundings of the average |
| MSFU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| MSFU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 100,557,909 | 100,557,910 | PASS |  |  |
| MSFU | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| MSFU | MR-price | price = the last completed close | 37.34 | 37.34 | PASS |  |  |
| MSFU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $37.34 needs above $10 | $37.34 needs above $10 | PASS |  |  |
| MSFU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.8 needs under 10 | 4.79 needs under 10 -> ✓ | PASS |  |  |
| MSFU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 20.3% above its 200-day average | 20.3% above | PASS |  |  |
| MSFU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $100.6M traded on an average day needs above $25M | $100,557,909 needs above $25,000,000 | PASS |  |  |
| MSFU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.79 | 4.79 | PASS |  |  |
| MSFU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 20.27% | 20.27% | PASS |  |  |
| MSFU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MTRX.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| MTRX.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| MTRX.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MTRX.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MTRX.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MTRX.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MTRX.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 529,704 | 529,706 | PASS |  |  |
| MTRX.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MTRX.TO | MR-price | price = the last completed close | 29.13 | 29.13 | PASS |  |  |
| MTRX.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $29.13 needs above $10 | $29.13 needs above $10 | PASS |  |  |
| MTRX.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.6 needs under 10 | 8.55 needs under 10 -> ✓ | PASS |  |  |
| MTRX.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 15.2% below its 200-day average | 15.2% below | PASS |  |  |
| MTRX.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $529,704 traded on an average day needs above $25M | $529,704 needs above $25,000,000 | PASS |  |  |
| MTRX.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8.55 | 8.55 | PASS |  |  |
| MTRX.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -15.17% | -15.17% | PASS |  |  |
| MTRX.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -8.2% | TR -8.2% | PASS | LOW | the two cards divide by different roundings of the average |
| MU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| MU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| MU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 80,861,092 | 80,861,092 | PASS |  |  |
| MU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MU.TO | MR-price | price = the last completed close | 31.04 | 31.04 | PASS |  |  |
| MU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $31.04 needs above $10 | $31.04 needs above $10 | PASS |  |  |
| MU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.1 needs under 10 | 12.12 needs under 10 -> ✗ | PASS |  |  |
| MU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 8.2% below its 200-day average | 8.2% below | PASS |  |  |
| MU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $80.9M traded on an average day needs above $25M | $80,861,092 needs above $25,000,000 | PASS |  |  |
| MU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.12 | 12.12 | PASS |  |  |
| MU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -8.18% | -8.17% | PASS |  |  |
| MU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NEE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -2.4% | TR -2.4% | PASS | LOW | the two cards divide by different roundings of the average |
| NEE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| NEE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NEE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,123,468,110 | 1,123,468,124 | PASS |  |  |
| NEE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NEE | MR-price | price = the last completed close | 84.42 | 84.42 | PASS |  |  |
| NEE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $84.42 needs above $10 | $84.42 needs above $10 | PASS |  |  |
| NEE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.8 needs under 10 | 9.79 needs under 10 -> ✓ | PASS |  |  |
| NEE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 2.4% below its 200-day average | 2.4% below | PASS |  |  |
| NEE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,123,468,110 needs above $25,000,000 | PASS |  |  |
| NEE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.79 | 9.79 | PASS |  |  |
| NEE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -2.44% | -2.44% | PASS |  |  |
| NEE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NEM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.5% | TR -0.5% | PASS | LOW | the two cards divide by different roundings of the average |
| NEM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| NEM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| NEM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 814,719,064 | 814,719,062 | PASS |  |  |
| NEM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NEM | MR-price | price = the last completed close | 111.26 | 111.26 | PASS |  |  |
| NEM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $111.26 needs above $10 | $111.26 needs above $10 | PASS |  |  |
| NEM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 32.9 needs under 10 | 32.92 needs under 10 -> ✗ | PASS |  |  |
| NEM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.5% below its 200-day average | 0.5% below | PASS |  |  |
| NEM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $814.7M traded on an average day needs above $25M | $814,719,064 needs above $25,000,000 | PASS |  |  |
| NEM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 32.92 | 32.92 | PASS |  |  |
| NEM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.51% | -0.51% | PASS |  |  |
| NEM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NFLX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -25.6% | TR -25.7% | PASS | LOW | the two cards divide by different roundings of the average |
| NFLX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| NFLX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NFLX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFLX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,818,242,282 | 2,818,242,269 | PASS |  |  |
| NFLX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NFLX | MR-price | price = the last completed close | 59.68 | 59.68 | PASS |  |  |
| NFLX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $59.68 needs above $10 | $59.68 needs above $10 | PASS |  |  |
| NFLX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.2 needs under 10 | 4.2 needs under 10 -> ✓ | PASS |  |  |
| NFLX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 25.6% below its 200-day average | 25.6% below | PASS |  |  |
| NFLX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.8B traded on an average day needs above $25M | $2,818,242,282 needs above $25,000,000 | PASS |  |  |
| NFLX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.2 | 4.20 | PASS |  |  |
| NFLX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -25.65% | -25.65% | PASS |  |  |
| NFLX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NFXL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -51.2% | TR -51.2% | PASS | LOW | the two cards divide by different roundings of the average |
| NFXL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| NFXL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| NFXL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFXL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 19,292,788 | 19,292,788 | PASS |  |  |
| NFXL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NFXL | MR-price | price = the last completed close | 9.86 | 9.86 | PASS |  |  |
| NFXL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $9.86 needs above $10 | $9.86 needs above $10 | PASS |  |  |
| NFXL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.3 needs under 10 | 4.26 needs under 10 -> ✓ | PASS |  |  |
| NFXL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 51.2% below its 200-day average | 51.2% below | PASS |  |  |
| NFXL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $19.3M traded on an average day needs above $25M | $19,292,788 needs above $25,000,000 | PASS |  |  |
| NFXL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.26 | 4.26 | PASS |  |  |
| NFXL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -51.16% | -51.16% | PASS |  |  |
| NFXL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NTR.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.3% | TR +1.3% | PASS | LOW | the two cards divide by different roundings of the average |
| NTR.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| NTR.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| NTR.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NTR.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 139,272,665 | 139,272,666 | PASS |  |  |
| NTR.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NTR.TO | MR-price | price = the last completed close | 99.02 | 99.02 | PASS |  |  |
| NTR.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $99.02 needs above $10 | $99.02 needs above $10 | PASS |  |  |
| NTR.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.7 needs under 10 | 22.67 needs under 10 -> ✗ | PASS |  |  |
| NTR.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.3% above its 200-day average | 1.3% above | PASS |  |  |
| NTR.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $139.3M traded on an average day needs above $25M | $139,272,665 needs above $25,000,000 | PASS |  |  |
| NTR.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.67 | 22.67 | PASS |  |  |
| NTR.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.29% | 1.29% | PASS |  |  |
| NTR.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.6% | TR -23.6% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| NVDA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 42,088,882,301 | 42,088,881,875 | PASS |  |  |
| NVDA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDA | MR-price | price = the last completed close | 155.46 | 155.46 | PASS |  |  |
| NVDA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $155.46 needs above $10 | $155.46 needs above $10 | PASS |  |  |
| NVDA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.2 needs under 10 | 5.19 needs under 10 -> ✓ | PASS |  |  |
| NVDA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.6% below its 200-day average | 23.6% below | PASS |  |  |
| NVDA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $42.1B traded on an average day needs above $25M | $42,088,882,301 needs above $25,000,000 | PASS |  |  |
| NVDA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.19 | 5.19 | PASS |  |  |
| NVDA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.64% | -23.64% | PASS |  |  |
| NVDA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -48.2% | TR -48.2% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| NVDL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 612,634,816 | 612,634,823 | PASS |  |  |
| NVDL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDL | MR-price | price = the last completed close | 16.22 | 16.22 | PASS |  |  |
| NVDL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $16.22 needs above $10 | $16.22 needs above $10 | PASS |  |  |
| NVDL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.4 needs under 10 | 5.39 needs under 10 -> ✓ | PASS |  |  |
| NVDL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 48.2% below its 200-day average | 48.2% below | PASS |  |  |
| NVDL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $612.6M traded on an average day needs above $25M | $612,634,816 needs above $25,000,000 | PASS |  |  |
| NVDL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.39 | 5.39 | PASS |  |  |
| NVDL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -48.18% | -48.18% | PASS |  |  |
| NVDL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ONTO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.2% | TR -23.2% | PASS | LOW | the two cards divide by different roundings of the average |
| ONTO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ONTO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| ONTO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ONTO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ONTO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 239,113,719 | 239,113,721 | PASS |  |  |
| ONTO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ONTO | MR-price | price = the last completed close | 199.57 | 199.57 | PASS |  |  |
| ONTO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $199.57 needs above $10 | $199.57 needs above $10 | PASS |  |  |
| ONTO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 43.7 needs under 10 | 43.69 needs under 10 -> ✗ | PASS |  |  |
| ONTO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.2% below its 200-day average | 23.2% below | PASS |  |  |
| ONTO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $239.1M traded on an average day needs above $25M | $239,113,719 needs above $25,000,000 | PASS |  |  |
| ONTO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 43.69 | 43.69 | PASS |  |  |
| ONTO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.23% | -23.23% | PASS |  |  |
| ONTO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ORBX.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| ORCL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -24.7% | TR -24.7% | PASS | LOW | the two cards divide by different roundings of the average |
| ORCL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ORCL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ORCL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ORCL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,251,977,721 | 5,251,977,701 | PASS |  |  |
| ORCL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ORCL | MR-price | price = the last completed close | 115 | 115 | PASS |  |  |
| ORCL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $115.00 needs above $10 | $115.00 needs above $10 | PASS |  |  |
| ORCL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.4 needs under 10 | 8.36 needs under 10 -> ✓ | PASS |  |  |
| ORCL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 24.7% below its 200-day average | 24.7% below | PASS |  |  |
| ORCL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.3B traded on an average day needs above $25M | $5,251,977,721 needs above $25,000,000 | PASS |  |  |
| ORCL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8.36 | 8.36 | PASS |  |  |
| ORCL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -24.7% | -24.70% | PASS |  |  |
| ORCL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +15.8% | TR +15.8% | PASS | LOW | the two cards divide by different roundings of the average |
| PG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| PG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| PG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,691,523,611 | 1,691,523,228 | PASS |  |  |
| PG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PG | MR-price | price = the last completed close | 171.72 | 171.72 | PASS |  |  |
| PG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $171.72 needs above $10 | $171.72 needs above $10 | PASS |  |  |
| PG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 61.1 needs under 10 | 61.12 needs under 10 -> ✗ | PASS |  |  |
| PG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 15.8% above its 200-day average | 15.8% above | PASS |  |  |
| PG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.7B traded on an average day needs above $25M | $1,691,523,611 needs above $25,000,000 | PASS |  |  |
| PG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 61.12 | 61.12 | PASS |  |  |
| PG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 15.85% | 15.85% | PASS |  |  |
| PG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PLD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -7.9% | TR -7.9% | PASS | LOW | the two cards divide by different roundings of the average |
| PLD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| PLD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| PLD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PLD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 463,810,951 | 463,810,949 | PASS |  |  |
| PLD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PLD | MR-price | price = the last completed close | 125.56 | 125.56 | PASS |  |  |
| PLD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $125.56 needs above $10 | $125.56 needs above $10 | PASS |  |  |
| PLD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.2 needs under 10 | 3.17 needs under 10 -> ✓ | PASS |  |  |
| PLD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 7.9% below its 200-day average | 7.9% below | PASS |  |  |
| PLD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $463.8M traded on an average day needs above $25M | $463,810,951 needs above $25,000,000 | PASS |  |  |
| PLD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.17 | 3.17 | PASS |  |  |
| PLD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.91% | -7.91% | PASS |  |  |
| PLD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PNG.V | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -52.8% | TR -52.7% | PASS | LOW | the two cards divide by different roundings of the average |
| PNG.V | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| PNG.V | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| PNG.V | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PNG.V | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,741,546 | 3,741,546 | PASS |  |  |
| PNG.V | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PNG.V | MR-price | price = the last completed close | 3.12 | 3.12 | PASS |  |  |
| PNG.V | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $3.12 needs above $10 | $3.12 needs above $10 | PASS |  |  |
| PNG.V | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.7 needs under 10 | 2.74 needs under 10 -> ✓ | PASS |  |  |
| PNG.V | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 52.8% below its 200-day average | 52.8% below | PASS |  |  |
| PNG.V | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $3.7M traded on an average day needs above $25M | $3,741,546 needs above $25,000,000 | PASS |  |  |
| PNG.V | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.74 | 2.74 | PASS |  |  |
| PNG.V | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -52.75% | -52.75% | PASS |  |  |
| PNG.V | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QCOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.6% | TR -1.6% | PASS | LOW | the two cards divide by different roundings of the average |
| QCOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| QCOM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| QCOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QCOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,384,350,444 | 2,384,350,433 | PASS |  |  |
| QCOM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QCOM | MR-price | price = the last completed close | 166.67 | 166.67 | PASS |  |  |
| QCOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $166.67 needs above $10 | $166.67 needs above $10 | PASS |  |  |
| QCOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.1 needs under 10 | 9.12 needs under 10 -> ✓ | PASS |  |  |
| QCOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.6% below its 200-day average | 1.6% below | PASS |  |  |
| QCOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.4B traded on an average day needs above $25M | $2,384,350,444 needs above $25,000,000 | PASS |  |  |
| QCOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.12 | 9.12 | PASS |  |  |
| QCOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.58% | -1.58% | PASS |  |  |
| QCOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QPUX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -83.7% | TR -83.7% | PASS | LOW | the two cards divide by different roundings of the average |
| QPUX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| QPUX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| QPUX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QPUX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,610,763 | 1,610,738 | PASS |  |  |
| QPUX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QPUX | MR-price | price = the last completed close | 3.32 | 3.32 | PASS |  |  |
| QPUX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $3.32 needs above $10 | $3.32 needs above $10 | PASS |  |  |
| QPUX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.7 needs under 10 | 2.68 needs under 10 -> ✓ | PASS |  |  |
| QPUX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 83.7% below its 200-day average | 83.7% below | PASS |  |  |
| QPUX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.6M traded on an average day needs above $25M | $1,610,763 needs above $25,000,000 | PASS |  |  |
| QPUX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.68 | 2.68 | PASS |  |  |
| QPUX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -83.7% | -83.70% | PASS |  |  |
| QPUX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QTUM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.3% | TR -11.3% | PASS | LOW | the two cards divide by different roundings of the average |
| QTUM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| QTUM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| QTUM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QTUM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 49,114,018 | 49,114,018 | PASS |  |  |
| QTUM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QTUM | MR-price | price = the last completed close | 122.42 | 122.42 | PASS |  |  |
| QTUM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $122.42 needs above $10 | $122.42 needs above $10 | PASS |  |  |
| QTUM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.6 needs under 10 | 6.56 needs under 10 -> ✓ | PASS |  |  |
| QTUM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.3% below its 200-day average | 11.3% below | PASS |  |  |
| QTUM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $49.1M traded on an average day needs above $25M | $49,114,018 needs above $25,000,000 | PASS |  |  |
| QTUM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.56 | 6.56 | PASS |  |  |
| QTUM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.26% | -11.26% | PASS |  |  |
| QTUM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RBOT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -18.6% | TR -18.6% | PASS | LOW | the two cards divide by different roundings of the average |
| RBOT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| RBOT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| RBOT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RBOT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RBOT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RBOT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RBOT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 134,393 | 134,394 | PASS |  |  |
| RBOT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RBOT.TO | MR-price | price = the last completed close | 27.09 | 27.09 | PASS |  |  |
| RBOT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $27.09 needs above $10 | $27.09 needs above $10 | PASS |  |  |
| RBOT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.8 needs under 10 | 3.75 needs under 10 -> ✓ | PASS |  |  |
| RBOT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.6% below its 200-day average | 18.6% below | PASS |  |  |
| RBOT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $134,393 traded on an average day needs above $25M | $134,393 needs above $25,000,000 | PASS |  |  |
| RBOT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.75 | 3.75 | PASS |  |  |
| RBOT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -18.63% | -18.63% | PASS |  |  |
| RBOT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RTX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.8% | TR +1.8% | PASS | LOW | the two cards divide by different roundings of the average |
| RTX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| RTX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| RTX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RTX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,066,548,233 | 1,066,548,236 | PASS |  |  |
| RTX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RTX | MR-price | price = the last completed close | 198 | 198 | PASS |  |  |
| RTX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $198.00 needs above $10 | $198.00 needs above $10 | PASS |  |  |
| RTX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 60.4 needs under 10 | 60.44 needs under 10 -> ✗ | PASS |  |  |
| RTX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.8% above its 200-day average | 1.8% above | PASS |  |  |
| RTX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,066,548,233 needs above $25,000,000 | PASS |  |  |
| RTX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 60.44 | 60.44 | PASS |  |  |
| RTX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.81% | 1.81% | PASS |  |  |
| RTX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RY.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +6.7% | TR +6.7% | PASS | LOW | the two cards divide by different roundings of the average |
| RY.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| RY.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,067,141,976 | 1,067,141,811 | PASS |  |  |
| RY.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| RY.TO | MR-price | price = the last completed close | 280.99 | 280.99 | PASS |  |  |
| RY.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $280.99 needs above $10 | $280.99 needs above $10 | PASS |  |  |
| RY.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.5 needs under 10 | 3.49 needs under 10 -> ✓ | PASS |  |  |
| RY.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 6.7% above its 200-day average | 6.7% above | PASS |  |  |
| RY.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,067,141,976 needs above $25,000,000 | PASS |  |  |
| RY.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.49 | 3.49 | PASS |  |  |
| RY.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 6.72% | 6.72% | PASS |  |  |
| RY.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SETM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -31.8% | TR -31.8% | PASS | LOW | the two cards divide by different roundings of the average |
| SETM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| SETM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| SETM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SETM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SETM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SETM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SETM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,726,710 | 3,726,701 | PASS |  |  |
| SETM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SETM | MR-price | price = the last completed close | 22.11 | 22.11 | PASS |  |  |
| SETM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $22.11 needs above $10 | $22.11 needs above $10 | PASS |  |  |
| SETM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.6 needs under 10 | 3.57 needs under 10 -> ✓ | PASS |  |  |
| SETM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 31.8% below its 200-day average | 31.8% below | PASS |  |  |
| SETM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $3.7M traded on an average day needs above $25M | $3,726,710 needs above $25,000,000 | PASS |  |  |
| SETM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.57 | 3.57 | PASS |  |  |
| SETM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -31.77% | -31.77% | PASS |  |  |
| SETM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SGRD.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| SMH | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -12.3% | TR -12.3% | PASS | LOW | the two cards divide by different roundings of the average |
| SMH | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| SMH | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| SMH | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SMH | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,025,798,569 | 6,025,798,595 | PASS |  |  |
| SMH | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SMH | MR-price | price = the last completed close | 460.1 | 460.1 | PASS |  |  |
| SMH | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $460.10 needs above $10 | $460.10 needs above $10 | PASS |  |  |
| SMH | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.4 needs under 10 | 9.36 needs under 10 -> ✓ | PASS |  |  |
| SMH | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 12.3% below its 200-day average | 12.3% below | PASS |  |  |
| SMH | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6B traded on an average day needs above $25M | $6,025,798,569 needs above $25,000,000 | PASS |  |  |
| SMH | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.36 | 9.36 | PASS |  |  |
| SMH | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -12.27% | -12.27% | PASS |  |  |
| SMH | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SNDK.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| SO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +2.7% | TR +2.7% | PASS | LOW | the two cards divide by different roundings of the average |
| SO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| SO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| SO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 789,130,115 | 789,129,641 | PASS |  |  |
| SO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SO | MR-price | price = the last completed close | 93.6 | 93.6 | PASS |  |  |
| SO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $93.60 needs above $10 | $93.60 needs above $10 | PASS |  |  |
| SO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 50.0 needs under 10 | 49.96 needs under 10 -> ✗ | PASS |  |  |
| SO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 2.7% above its 200-day average | 2.7% above | PASS |  |  |
| SO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $789.1M traded on an average day needs above $25M | $789,130,115 needs above $25,000,000 | PASS |  |  |
| SO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 49.96 | 49.95 | PASS |  |  |
| SO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.67% | 2.67% | PASS |  |  |
| SO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -60.4% | TR -60.4% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| SOXL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| SOXL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,296,819,732 | 12,296,819,744 | PASS |  |  |
| SOXL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL | MR-price | price = the last completed close | 49.07 | 49.07 | PASS |  |  |
| SOXL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $49.07 needs above $10 | $49.07 needs above $10 | PASS |  |  |
| SOXL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.4 needs under 10 | 14.39 needs under 10 -> ✗ | PASS |  |  |
| SOXL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 60.4% below its 200-day average | 60.4% below | PASS |  |  |
| SOXL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.3B traded on an average day needs above $25M | $12,296,819,732 needs above $25,000,000 | PASS |  |  |
| SOXL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14.39 | 14.39 | PASS |  |  |
| SOXL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -60.38% | -60.38% | PASS |  |  |
| SOXL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL.NE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -60.0% | TR -60.0% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL.NE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| SOXL.NE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| SOXL.NE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL.NE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,697,226 | 1,697,226 | PASS |  |  |
| SOXL.NE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL.NE | MR-price | price = the last completed close | 12.36 | 12.36 | PASS |  |  |
| SOXL.NE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $12.36 needs above $10 | $12.36 needs above $10 | PASS |  |  |
| SOXL.NE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.8 needs under 10 | 13.82 needs under 10 -> ✗ | PASS |  |  |
| SOXL.NE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 60.0% below its 200-day average | 60.0% below | PASS |  |  |
| SOXL.NE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.7M traded on an average day needs above $25M | $1,697,226 needs above $25,000,000 | PASS |  |  |
| SOXL.NE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.82 | 13.69 | PASS |  |  |
| SOXL.NE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -59.96% | -59.96% | PASS |  |  |
| SOXL.NE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.9% | TR -11.9% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| SOXX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| SOXX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,115,081,151 | 6,115,082,122 | PASS |  |  |
| SOXX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXX | MR-price | price = the last completed close | 141.46 | 141.46 | PASS |  |  |
| SOXX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $141.46 needs above $10 | $141.46 needs above $10 | PASS |  |  |
| SOXX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.0 needs under 10 | 15.02 needs under 10 -> ✗ | PASS |  |  |
| SOXX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.9% below its 200-day average | 11.9% below | PASS |  |  |
| SOXX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6.1B traded on an average day needs above $25M | $6,115,081,151 needs above $25,000,000 | PASS |  |  |
| SOXX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.02 | 15.02 | PASS |  |  |
| SOXX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.87% | -11.87% | PASS |  |  |
| SOXX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SPCL | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| TSLA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.6% | TR -0.6% | PASS | LOW | the two cards divide by different roundings of the average |
| TSLA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| TSLA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| TSLA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,776,589,362 | 14,776,589,447 | PASS |  |  |
| TSLA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSLA | MR-price | price = the last completed close | 380.11 | 380.11 | PASS |  |  |
| TSLA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $380.11 needs above $10 | $380.11 needs above $10 | PASS |  |  |
| TSLA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 24.6 needs under 10 | 24.64 needs under 10 -> ✗ | PASS |  |  |
| TSLA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.6% below its 200-day average | 0.6% below | PASS |  |  |
| TSLA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $14.8B traded on an average day needs above $25M | $14,776,589,362 needs above $25,000,000 | PASS |  |  |
| TSLA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 24.64 | 24.64 | PASS |  |  |
| TSLA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.56% | -0.56% | PASS |  |  |
| TSLA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| TSLL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -16.4% | TR -16.4% | PASS | LOW | the two cards divide by different roundings of the average |
| TSLL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| TSLL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; the price is under $10 | the 2-day RSI is 10 or higher; it is below its 200-day average; the price is under $10 | PASS |  |  |
| TSLL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 495,885,337 | 495,885,328 | PASS |  |  |
| TSLL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSLL | MR-price | price = the last completed close | 9.81 | 9.81 | PASS |  |  |
| TSLL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $9.81 needs above $10 | $9.81 needs above $10 | PASS |  |  |
| TSLL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.2 needs under 10 | 22.19 needs under 10 -> ✗ | PASS |  |  |
| TSLL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 16.4% below its 200-day average | 16.4% below | PASS |  |  |
| TSLL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $495.9M traded on an average day needs above $25M | $495,885,337 needs above $25,000,000 | PASS |  |  |
| TSLL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.19 | 22.19 | PASS |  |  |
| TSLL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -16.36% | -16.36% | PASS |  |  |
| TSLL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| TSM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -10.5% | TR -10.5% | PASS | LOW | the two cards divide by different roundings of the average |
| TSM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| TSM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| TSM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,066,694,350 | 6,066,694,292 | PASS |  |  |
| TSM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSM | MR-price | price = the last completed close | 359.69 | 359.69 | PASS |  |  |
| TSM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $359.69 needs above $10 | $359.69 needs above $10 | PASS |  |  |
| TSM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.5 needs under 10 | 5.45 needs under 10 -> ✓ | PASS |  |  |
| TSM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 10.5% below its 200-day average | 10.5% below | PASS |  |  |
| TSM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6.1B traded on an average day needs above $25M | $6,066,694,350 needs above $25,000,000 | PASS |  |  |
| TSM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.45 | 5.45 | PASS |  |  |
| TSM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -10.53% | -10.53% | PASS |  |  |
| TSM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| UBOT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -37.0% | TR -37.0% | PASS | LOW | the two cards divide by different roundings of the average |
| UBOT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| UBOT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| UBOT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UBOT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UBOT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UBOT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UBOT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 332,486 | 332,487 | PASS |  |  |
| UBOT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| UBOT | MR-price | price = the last completed close | 15.04 | 15.04 | PASS |  |  |
| UBOT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $15.04 needs above $10 | $15.04 needs above $10 | PASS |  |  |
| UBOT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.7 needs under 10 | 4.72 needs under 10 -> ✓ | PASS |  |  |
| UBOT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 37.0% below its 200-day average | 37.0% below | PASS |  |  |
| UBOT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $332,486 traded on an average day needs above $25M | $332,486 needs above $25,000,000 | PASS |  |  |
| UBOT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.72 | 4.72 | PASS |  |  |
| UBOT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -36.96% | -36.96% | PASS |  |  |
| UBOT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| UFO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -16.4% | TR -16.4% | PASS | LOW | the two cards divide by different roundings of the average |
| UFO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| UFO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| UFO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UFO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UFO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UFO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UFO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 9,818,701 | 9,818,701 | PASS |  |  |
| UFO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| UFO | MR-price | price = the last completed close | 39.3 | 39.3 | PASS |  |  |
| UFO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $39.30 needs above $10 | $39.30 needs above $10 | PASS |  |  |
| UFO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.6 needs under 10 | 7.58 needs under 10 -> ✓ | PASS |  |  |
| UFO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 16.4% below its 200-day average | 16.4% below | PASS |  |  |
| UFO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $9.8M traded on an average day needs above $25M | $9,818,701 needs above $25,000,000 | PASS |  |  |
| UFO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.58 | 7.58 | PASS |  |  |
| UFO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -16.37% | -16.38% | PASS |  |  |
| UFO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| URA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -34.2% | TR -34.2% | PASS | LOW | the two cards divide by different roundings of the average |
| URA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| URA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| URA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 152,653,265 | 152,653,264 | PASS |  |  |
| URA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| URA | MR-price | price = the last completed close | 30.04 | 30.04 | PASS |  |  |
| URA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $30.04 needs above $10 | $30.04 needs above $10 | PASS |  |  |
| URA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.8 needs under 10 | 4.82 needs under 10 -> ✓ | PASS |  |  |
| URA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 34.2% below its 200-day average | 34.2% below | PASS |  |  |
| URA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $152.7M traded on an average day needs above $25M | $152,653,265 needs above $25,000,000 | PASS |  |  |
| URA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.82 | 4.82 | PASS |  |  |
| URA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -34.24% | -34.24% | PASS |  |  |
| URA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| URAA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -61.3% | TR -61.3% | PASS | LOW | the two cards divide by different roundings of the average |
| URAA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| URAA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| URAA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URAA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URAA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,047,328 | 1,047,328 | PASS |  |  |
| URAA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| URAA | MR-price | price = the last completed close | 11.38 | 11.38 | PASS |  |  |
| URAA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $11.38 needs above $10 | $11.38 needs above $10 | PASS |  |  |
| URAA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.9 needs under 10 | 4.91 needs under 10 -> ✓ | PASS |  |  |
| URAA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 61.3% below its 200-day average | 61.3% below | PASS |  |  |
| URAA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1M traded on an average day needs above $25M | $1,047,328 needs above $25,000,000 | PASS |  |  |
| URAA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.91 | 4.91 | PASS |  |  |
| URAA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -61.34% | -61.34% | PASS |  |  |
| URAA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| V | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +20.2% | TR +20.2% | PASS | LOW | the two cards divide by different roundings of the average |
| V | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| V | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| V | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| V | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,923,178,209 | 2,923,176,701 | PASS |  |  |
| V | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| V | MR-price | price = the last completed close | 416.77 | 416.77 | PASS |  |  |
| V | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $416.77 needs above $10 | $416.77 needs above $10 | PASS |  |  |
| V | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.9 needs under 10 | 15.86 needs under 10 -> ✗ | PASS |  |  |
| V | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 20.2% above its 200-day average | 20.2% above | PASS |  |  |
| V | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.9B traded on an average day needs above $25M | $2,923,178,209 needs above $25,000,000 | PASS |  |  |
| V | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.86 | 15.86 | PASS |  |  |
| V | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 20.19% | 20.19% | PASS |  |  |
| V | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| VFV.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +3.0% | TR +3.0% | PASS | LOW | the two cards divide by different roundings of the average |
| VFV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| VFV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 72,897,721 | 72,897,721 | PASS |  |  |
| VFV.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| VFV.TO | MR-price | price = the last completed close | 186.14 | 186.14 | PASS |  |  |
| VFV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $186.14 needs above $10 | $186.14 needs above $10 | PASS |  |  |
| VFV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.2 needs under 10 | 7.18 needs under 10 -> ✓ | PASS |  |  |
| VFV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 3.0% above its 200-day average | 3.0% above | PASS |  |  |
| VFV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $72.9M traded on an average day needs above $25M | $72,897,721 needs above $25,000,000 | PASS |  |  |
| VFV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.18 | 7.18 | PASS |  |  |
| VFV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 3.02% | 3.02% | PASS |  |  |
| VFV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| VRT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -29.9% | TR -29.9% | PASS | LOW | the two cards divide by different roundings of the average |
| VRT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| VRT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| VRT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VRT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VRT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,784,225,128 | 1,784,225,130 | PASS |  |  |
| VRT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| VRT | MR-price | price = the last completed close | 190.37 | 190.37 | PASS |  |  |
| VRT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $190.37 needs above $10 | $190.37 needs above $10 | PASS |  |  |
| VRT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 26.3 needs under 10 | 26.28 needs under 10 -> ✗ | PASS |  |  |
| VRT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 29.9% below its 200-day average | 29.9% below | PASS |  |  |
| VRT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.8B traded on an average day needs above $25M | $1,784,225,128 needs above $25,000,000 | PASS |  |  |
| VRT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 26.28 | 26.28 | PASS |  |  |
| VRT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -29.88% | -29.88% | PASS |  |  |
| VRT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| WDC.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| WELL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +11.5% | TR +11.5% | PASS | LOW | the two cards divide by different roundings of the average |
| WELL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| WELL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| WELL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| WELL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 739,599,079 | 739,599,158 | PASS |  |  |
| WELL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| WELL | MR-price | price = the last completed close | 245.76 | 245.76 | PASS |  |  |
| WELL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $245.76 needs above $10 | $245.76 needs above $10 | PASS |  |  |
| WELL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 74.1 needs under 10 | 74.1 needs under 10 -> ✗ | PASS |  |  |
| WELL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 11.5% above its 200-day average | 11.5% above | PASS |  |  |
| WELL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $739.6M traded on an average day needs above $25M | $739,599,079 needs above $25,000,000 | PASS |  |  |
| WELL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 74.1 | 74.10 | PASS |  |  |
| WELL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 11.47% | 11.47% | PASS |  |  |
| WELL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| WMT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +7.5% | TR +7.4% | PASS | LOW | the two cards divide by different roundings of the average |
| WMT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| WMT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| WMT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| WMT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,714,325,084 | 2,714,325,073 | PASS |  |  |
| WMT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| WMT | MR-price | price = the last completed close | 127.52 | 127.52 | PASS |  |  |
| WMT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $127.52 needs above $10 | $127.52 needs above $10 | PASS |  |  |
| WMT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 44.0 needs under 10 | 43.96 needs under 10 -> ✗ | PASS |  |  |
| WMT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 7.5% above its 200-day average | 7.5% above | PASS |  |  |
| WMT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.7B traded on an average day needs above $25M | $2,714,325,084 needs above $25,000,000 | PASS |  |  |
| WMT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 43.96 | 43.96 | PASS |  |  |
| WMT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 7.45% | 7.45% | PASS |  |  |
| WMT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XCHP.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -9.6% | TR -9.6% | PASS | LOW | the two cards divide by different roundings of the average |
| XCHP.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| XCHP.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XCHP.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XCHP.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 7,891,284 | 7,891,285 | PASS |  |  |
| XCHP.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XCHP.TO | MR-price | price = the last completed close | 105.4 | 105.4 | PASS |  |  |
| XCHP.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $105.40 needs above $10 | $105.40 needs above $10 | PASS |  |  |
| XCHP.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.6 needs under 10 | 14.6 needs under 10 -> ✗ | PASS |  |  |
| XCHP.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.6% below its 200-day average | 9.6% below | PASS |  |  |
| XCHP.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $7.9M traded on an average day needs above $25M | $7,891,284 needs above $25,000,000 | PASS |  |  |
| XCHP.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14.6 | 14.60 | PASS |  |  |
| XCHP.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.59% | -9.59% | PASS |  |  |
| XCHP.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XDRV.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -17.6% | TR -17.6% | PASS | LOW | the two cards divide by different roundings of the average |
| XDRV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| XDRV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XDRV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XDRV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,837 | 1,837 | PASS |  |  |
| XDRV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XDRV.TO | MR-price | price = the last completed close | 39.25 | 39.25 | PASS |  |  |
| XDRV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $39.25 needs above $10 | $39.25 needs above $10 | PASS |  |  |
| XDRV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.3 needs under 10 | 12.26 needs under 10 -> ✗ | PASS |  |  |
| XDRV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 17.6% below its 200-day average | 17.6% below | PASS |  |  |
| XDRV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1,837 traded on an average day needs above $25M | $1,837 needs above $25,000,000 | PASS |  |  |
| XDRV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.26 | 12.26 | PASS |  |  |
| XDRV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.59% | -17.59% | PASS |  |  |
| XDRV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XEQT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.8% | TR +1.8% | PASS | LOW | the two cards divide by different roundings of the average |
| XEQT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| XEQT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 51,252,311 | 51,251,643 | PASS |  |  |
| XEQT.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| XEQT.TO | MR-price | price = the last completed close | 44.34 | 44.34 | PASS |  |  |
| XEQT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $44.34 needs above $10 | $44.34 needs above $10 | PASS |  |  |
| XEQT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.9 needs under 10 | 5.9 needs under 10 -> ✓ | PASS |  |  |
| XEQT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.8% above its 200-day average | 1.8% above | PASS |  |  |
| XEQT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $51.3M traded on an average day needs above $25M | $51,252,311 needs above $25,000,000 | PASS |  |  |
| XEQT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.9 | 5.90 | PASS |  |  |
| XEQT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.77% | 1.77% | PASS |  |  |
| XEQT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XETM.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| XETM.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XETM.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XETM.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XETM.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XETM.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XETM.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 210,396 | 210,397 | PASS |  |  |
| XETM.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XETM.TO | MR-price | price = the last completed close | 61.17 | 61.17 | PASS |  |  |
| XETM.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $61.17 needs above $10 | $61.17 needs above $10 | PASS |  |  |
| XETM.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.9 needs under 10 | 3.89 needs under 10 -> ✓ | PASS |  |  |
| XETM.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.4% below its 200-day average | 23.4% below | PASS |  |  |
| XETM.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $210,396 traded on an average day needs above $25M | $210,396 needs above $25,000,000 | PASS |  |  |
| XETM.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.89 | 3.89 | PASS |  |  |
| XETM.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.42% | -23.42% | PASS |  |  |
| XETM.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XGD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -7.0% | TR -7.0% | PASS | LOW | the two cards divide by different roundings of the average |
| XGD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| XGD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| XGD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XGD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XGD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 33,285,953 | 33,285,953 | PASS |  |  |
| XGD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XGD.TO | MR-price | price = the last completed close | 51.28 | 51.28 | PASS |  |  |
| XGD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $51.28 needs above $10 | $51.28 needs above $10 | PASS |  |  |
| XGD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 30.6 needs under 10 | 30.63 needs under 10 -> ✗ | PASS |  |  |
| XGD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 7.0% below its 200-day average | 7.0% below | PASS |  |  |
| XGD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $33.3M traded on an average day needs above $25M | $33,285,953 needs above $25,000,000 | PASS |  |  |
| XGD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 30.63 | 30.63 | PASS |  |  |
| XGD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7% | -7.00% | PASS |  |  |
| XGD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +8.1% | TR +8.1% | PASS | LOW | the two cards divide by different roundings of the average |
| XOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| XOM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| XOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,452,797,255 | 2,452,799,932 | PASS |  |  |
| XOM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XOM | MR-price | price = the last completed close | 167.21 | 167.21 | PASS |  |  |
| XOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $167.21 needs above $10 | $167.21 needs above $10 | PASS |  |  |
| XOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 43.5 needs under 10 | 43.47 needs under 10 -> ✗ | PASS |  |  |
| XOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 8.1% above its 200-day average | 8.1% above | PASS |  |  |
| XOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.5B traded on an average day needs above $25M | $2,452,797,255 needs above $25,000,000 | PASS |  |  |
| XOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 43.47 | 43.46 | PASS |  |  |
| XOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 8.14% | 8.14% | PASS |  |  |
| XOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AAPL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AAPL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AAPL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AAPL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AAPL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AAPL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AAPL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AAPL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AAPL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AAPU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AAPU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AAPU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AAPU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AAPU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AAPU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AAPU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AAPU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AAPU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AAPU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ABBV | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ABBV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ABBV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ABBV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ABBV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ABBV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ABBV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ABBV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ABBV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ABBV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ABBV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ABBV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AIPO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AIPO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AIPO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AIPO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AIPO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AIPO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AIPO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AIPO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AIPO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AIPO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AIPO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AIPO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ALAB | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ALAB | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ALAB | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ALAB | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ALAB | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ALAB | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ALAB | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ALAB | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ALAB | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ALAB | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ALAB | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ALAB | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMD | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AMD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AMD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AMD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AMD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AMD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMD.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AMD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AMD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AMD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AMD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AMD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMZN | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMZN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMZN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AMZN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AMZN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMZN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMZN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AMZN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AMZN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMZN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AMZN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMZN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMZU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMZU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMZU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AMZU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AMZU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMZU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMZU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AMZU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AMZU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMZU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AMZU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMZU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ANET.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ANET.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ANET.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ANET.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ANET.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ANET.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ANET.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ANET.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ANET.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ANET.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ANET.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ANET.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ASML.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ASML.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ASML.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ASML.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ASML.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ASML.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ASML.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ASML.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ASML.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ASML.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ASML.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ASML.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ASTL.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ASTL.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ASTL.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ASTL.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ASTL.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ASTL.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ASTL.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ASTL.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ASTL.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ASTL.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ASTL.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ASTL.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ATD.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ATD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ATD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ATD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ATD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ATD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ATD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ATD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ATD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ATD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ATD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ATD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGC | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AVGC | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AVGC | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AVGC | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AVGC | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGC | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AVGC | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AVGC | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AVGC | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AVGC | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AVGC | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGC | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AVGO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AVGO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AVGO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AVGO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AVGO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AVGO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AVGO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AVGO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AVGO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGO.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AVGO.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AVGO.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AVGO.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AVGO.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGO.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AVGO.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AVGO.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AVGO.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AVGO.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AVGO.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGO.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BDT.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| BDT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| BDT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| BDT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| BDT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BDT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| BDT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| BDT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| BDT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| BDT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| BDT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BDT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BOTZ | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| BOTZ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| BOTZ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| BOTZ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| BOTZ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BOTZ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| BOTZ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| BOTZ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| BOTZ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| BOTZ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| BOTZ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BOTZ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BRK-B | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| BRK-B | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| BRK-B | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| BRK-B | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| BRK-B | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BRK-B | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| BRK-B | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| BRK-B | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| BRK-B | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| BRK-B | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| BRK-B | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BRK-B | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BRKU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| BRKU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| BRKU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| BRKU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| BRKU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BRKU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| BRKU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| BRKU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| BRKU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| BRKU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| BRKU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BRKU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CAMT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CAMT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CAMT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CAMT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CAMT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CAMT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CAMT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CAMT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CAMT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CAMT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CAMT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CAMT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CARS.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CARS.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CARS.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CARS.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CARS.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CARS.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CARS.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CARS.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CARS.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CARS.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CARS.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CARS.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CAT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CAT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CAT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CAT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CAT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CAT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CAT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CAT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CAT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CAT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CAT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CAT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CCO.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CCO.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CCO.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CCO.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CCO.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CCO.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CCO.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CCO.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CCO.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CCO.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CCO.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CCO.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CEG | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CEG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CEG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CEG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CEG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CEG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CEG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CEG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CEG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CEG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CEG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CEG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CGY.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CGY.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CGY.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CGY.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CGY.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CGY.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CGY.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CGY.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CGY.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CGY.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CGY.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CGY.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CNQ.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CNQ.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CNQ.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CNQ.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CNQ.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CNQ.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CNQ.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CNQ.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CNQ.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CNQ.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CNQ.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CNQ.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CNR.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CNR.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CNR.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CNR.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CNR.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CNR.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CNR.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CNR.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CNR.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CNR.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CNR.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CNR.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COP | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COP | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COP | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| COP | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| COP | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COP | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COP | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| COP | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| COP | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COP | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| COP | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COP | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPP.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COPP.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COPP.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| COPP.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| COPP.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPP.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COPP.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| COPP.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| COPP.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COPP.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| COPP.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPP.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COPX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COPX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| COPX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| COPX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COPX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| COPX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| COPX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COPX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| COPX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPZ | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COPZ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COPZ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| COPZ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| COPZ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPZ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COPZ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| COPZ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| COPZ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COPZ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| COPZ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPZ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COST | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COST | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COST | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| COST | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| COST | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COST | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COST | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| COST | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| COST | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COST | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| COST | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COST | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COTG | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COTG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COTG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| COTG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| COTG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COTG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COTG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| COTG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| COTG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COTG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| COTG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COTG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CSU.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CSU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CSU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CSU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CSU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CSU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CSU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CSU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CSU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CSU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CSU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CSU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CVX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CVX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CVX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| CVX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| CVX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CVX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CVX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| CVX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| CVX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CVX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| CVX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CVX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRAL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DRAL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DRAL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| DRAL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| DRAL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRAL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DRAL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| DRAL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| DRAL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DRAL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| DRAL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRAL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRAM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DRAM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DRAM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| DRAM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| DRAM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRAM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DRAM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| DRAM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| DRAM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DRAM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| DRAM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRAM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRIV | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DRIV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DRIV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| DRIV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| DRIV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRIV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DRIV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| DRIV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| DRIV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DRIV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| DRIV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRIV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DUK | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DUK | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DUK | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| DUK | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| DUK | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DUK | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DUK | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| DUK | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| DUK | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DUK | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| DUK | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DUK | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ELIL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ELIL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ELIL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ELIL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ELIL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ELIL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ELIL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ELIL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ELIL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ELIL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ELIL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ELIL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| EQIX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| EQIX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| EQIX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| EQIX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| EQIX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| EQIX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| EQIX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| EQIX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| EQIX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| EQIX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| EQIX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| EQIX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ETN | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ETN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ETN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ETN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ETN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ETN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ETN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ETN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ETN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ETN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ETN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ETN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| FCX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| FCX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| FCX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| FCX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| FCX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| FCX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| FCX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| FCX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| FCX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| FCX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| FCX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| FCX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| FINN.NE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| FINN.NE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| FINN.NE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| FINN.NE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| FINN.NE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| FINN.NE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| FINN.NE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| FINN.NE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| FINN.NE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| FINN.NE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| FINN.NE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| FINN.NE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GDX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GDX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GDX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GDX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GDX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GDX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GDX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GDX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GDX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GDX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GDX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GDX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GDXU.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GDXU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GDXU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GDXU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GDXU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GDXU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GDXU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GDXU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GDXU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GDXU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GDXU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GDXU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GEV | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GEV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GEV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GEV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GEV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GEV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GEV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GEV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GEV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GEV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GEV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GEV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GEV.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GEV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GEV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GEV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GEV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GEV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GEV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GEV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GEV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GEV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GEV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GEV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GGLL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GGLL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GGLL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GGLL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GGLL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GGLL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GGLL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GGLL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GGLL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GGLL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GGLL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GGLL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GIB-A.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GIB-A.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GIB-A.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GIB-A.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GIB-A.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GIB-A.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GIB-A.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GIB-A.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GIB-A.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GIB-A.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GIB-A.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GIB-A.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GOOGL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GOOGL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GOOGL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GOOGL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GOOGL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GOOGL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GOOGL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GOOGL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GOOGL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GOOGL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GOOGL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GOOGL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GRID | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GRID | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GRID | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| GRID | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| GRID | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GRID | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GRID | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| GRID | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| GRID | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GRID | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| GRID | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GRID | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HD | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| HD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| HD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| HD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| HD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| HD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| HD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| HD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| HD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| HD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HURA.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| HURA.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| HURA.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| HURA.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| HURA.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HURA.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| HURA.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| HURA.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| HURA.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| HURA.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| HURA.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HURA.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HXQ.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| HXQ.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| HXQ.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| HXQ.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| HXQ.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HXQ.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| HXQ.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| HXQ.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| HXQ.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| HXQ.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| HXQ.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HXQ.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| JNJ | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| JNJ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| JNJ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| JNJ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| JNJ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| JNJ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| JNJ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| JNJ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| JNJ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| JNJ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| JNJ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| JNJ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| JPM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| JPM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| JPM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| JPM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| JPM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| JPM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| JPM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| JPM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| JPM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| JPM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| JPM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| JPM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| KEYS | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| KEYS | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| KEYS | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| KEYS | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| KEYS | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| KEYS | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| KEYS | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| KEYS | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| KEYS | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| KEYS | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| KEYS | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| KEYS | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| LIN | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| LIN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| LIN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| LIN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| LIN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| LIN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| LIN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| LIN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| LIN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| LIN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| LIN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| LIN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| LLY | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| LLY | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| LLY | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| LLY | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| LLY | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| LLY | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| LLY | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| LLY | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| LLY | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| LLY | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| LLY | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| LLY | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MDA.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MDA.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MDA.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| MDA.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| MDA.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MDA.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MDA.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| MDA.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| MDA.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MDA.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| MDA.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MDA.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| META | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| META | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| META | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| META | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| META | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| META | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| META | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| META | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| META | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| META | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| META | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| META | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| METU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| METU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| METU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| METU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| METU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| METU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| METU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| METU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| METU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| METU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| METU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| METU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MRVL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MRVL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MRVL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| MRVL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| MRVL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MRVL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MRVL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| MRVL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| MRVL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MRVL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| MRVL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MRVL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MSFT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MSFT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MSFT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| MSFT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| MSFT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MSFT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MSFT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| MSFT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| MSFT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MSFT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| MSFT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MSFT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MSFU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MSFU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MSFU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| MSFU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| MSFU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MSFU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MSFU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| MSFU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| MSFU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MSFU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| MSFU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MSFU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MTRX.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MTRX.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MTRX.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| MTRX.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| MTRX.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MTRX.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MTRX.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| MTRX.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| MTRX.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MTRX.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| MTRX.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MTRX.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MU.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| MU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| MU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| MU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| MU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| MU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NEE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NEE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NEE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| NEE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| NEE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NEE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NEE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| NEE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| NEE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NEE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| NEE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NEE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NEM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NEM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NEM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| NEM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| NEM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NEM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NEM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| NEM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| NEM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NEM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| NEM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NEM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NFLX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NFLX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NFLX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| NFLX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| NFLX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NFLX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NFLX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| NFLX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| NFLX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NFLX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| NFLX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NFLX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NFXL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NFXL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NFXL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| NFXL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| NFXL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NFXL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NFXL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| NFXL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| NFXL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NFXL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| NFXL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NFXL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NTR.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NTR.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NTR.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| NTR.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| NTR.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NTR.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NTR.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| NTR.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| NTR.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NTR.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| NTR.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NTR.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NVDA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NVDA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NVDA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| NVDA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| NVDA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NVDA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| NVDA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| NVDA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NVDA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| NVDA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NVDL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NVDL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NVDL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| NVDL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| NVDL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NVDL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| NVDL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| NVDL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NVDL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| NVDL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ONTO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ONTO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ONTO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ONTO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ONTO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ONTO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ONTO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ONTO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ONTO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ONTO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ONTO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ONTO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ORBX.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ORBX.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ORBX.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ORBX.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ORBX.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ORBX.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ORBX.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ORBX.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ORBX.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ORBX.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ORBX.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ORBX.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ORCL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ORCL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ORCL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ORCL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ORCL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ORCL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ORCL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ORCL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ORCL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ORCL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ORCL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ORCL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PG | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| PG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| PG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| PG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| PG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| PG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| PG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| PG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| PG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| PG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PLD | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| PLD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| PLD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| PLD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| PLD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PLD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| PLD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| PLD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| PLD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| PLD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| PLD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PLD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PNG.V | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| PNG.V | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| PNG.V | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| PNG.V | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| PNG.V | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PNG.V | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| PNG.V | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| PNG.V | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| PNG.V | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| PNG.V | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| PNG.V | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PNG.V | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QCOM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| QCOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| QCOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| QCOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| QCOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QCOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| QCOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| QCOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| QCOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| QCOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| QCOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QCOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QPUX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| QPUX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| QPUX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| QPUX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| QPUX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QPUX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| QPUX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| QPUX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| QPUX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| QPUX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| QPUX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QPUX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QTUM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| QTUM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| QTUM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| QTUM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| QTUM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QTUM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| QTUM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| QTUM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| QTUM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| QTUM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| QTUM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QTUM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RBOT.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| RBOT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| RBOT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| RBOT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| RBOT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RBOT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| RBOT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| RBOT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| RBOT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| RBOT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| RBOT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RBOT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RTX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| RTX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| RTX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| RTX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| RTX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RTX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| RTX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| RTX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| RTX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| RTX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| RTX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RTX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RY.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| RY.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| RY.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| RY.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| RY.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RY.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| RY.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| RY.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| RY.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| RY.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| RY.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RY.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SETM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SETM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SETM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SETM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SETM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SETM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SETM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SETM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SETM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SETM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SETM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SETM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SGRD.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SGRD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SGRD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SGRD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SGRD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SGRD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SGRD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SGRD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SGRD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SGRD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SGRD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SGRD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SMH | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SMH | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SMH | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SMH | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SMH | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SMH | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SMH | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SMH | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SMH | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SMH | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SMH | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SMH | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SNDK.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SNDK.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SNDK.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SNDK.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SNDK.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SNDK.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SNDK.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SNDK.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SNDK.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SNDK.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SNDK.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SNDK.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SOXL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SOXL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SOXL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SOXL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SOXL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SOXL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SOXL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SOXL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SOXL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXL.NE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SOXL.NE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SOXL.NE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SOXL.NE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SOXL.NE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL.NE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SOXL.NE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SOXL.NE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SOXL.NE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SOXL.NE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SOXL.NE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL.NE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SOXX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SOXX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SOXX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SOXX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SOXX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SOXX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SOXX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SOXX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SOXX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SPCL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SPCL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SPCL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SPCL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SPCL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SPCL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SPCL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SPCL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SPCL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SPCL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SPCL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SPCL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSLA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| TSLA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| TSLA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| TSLA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| TSLA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSLA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| TSLA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| TSLA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| TSLA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| TSLA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| TSLA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSLA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSLL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| TSLL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| TSLL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| TSLL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| TSLL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSLL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| TSLL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| TSLL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| TSLL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| TSLL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| TSLL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSLL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| TSM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| TSM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| TSM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| TSM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| TSM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| TSM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| TSM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| TSM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| TSM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| UBOT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| UBOT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| UBOT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| UBOT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| UBOT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| UBOT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| UBOT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| UBOT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| UBOT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| UBOT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| UBOT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| UBOT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| UFO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| UFO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| UFO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| UFO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| UFO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| UFO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| UFO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| UFO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| UFO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| UFO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| UFO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| UFO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| URA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| URA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| URA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| URA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| URA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| URA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| URA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| URA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| URA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| URA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| URA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| URA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| URAA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| URAA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| URAA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| URAA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| URAA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| URAA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| URAA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| URAA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| URAA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| URAA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| URAA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| URAA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| V | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| V | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| V | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| V | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| V | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| V | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| V | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| V | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| V | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| V | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| V | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| V | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| VFV.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| VFV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| VFV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| VFV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| VFV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| VFV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| VFV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| VFV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| VFV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| VFV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| VFV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| VFV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| VRT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| VRT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| VRT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| VRT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| VRT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| VRT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| VRT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| VRT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| VRT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| VRT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| VRT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| VRT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WDC.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| WDC.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| WDC.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| WDC.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| WDC.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WDC.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| WDC.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| WDC.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| WDC.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| WDC.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| WDC.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WDC.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WELL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| WELL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| WELL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| WELL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| WELL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WELL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| WELL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| WELL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| WELL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| WELL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| WELL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WELL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WMT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| WMT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| WMT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| WMT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| WMT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WMT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| WMT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| WMT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| WMT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| WMT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| WMT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WMT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XCHP.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XCHP.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XCHP.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| XCHP.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| XCHP.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XCHP.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XCHP.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| XCHP.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| XCHP.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XCHP.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| XCHP.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XCHP.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XDRV.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XDRV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XDRV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| XDRV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| XDRV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XDRV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XDRV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| XDRV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| XDRV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XDRV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| XDRV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XDRV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XEQT.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XEQT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XEQT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| XEQT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| XEQT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XEQT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XEQT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| XEQT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| XEQT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XEQT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| XEQT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XEQT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XETM.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XETM.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XETM.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| XETM.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| XETM.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XETM.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XETM.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| XETM.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| XETM.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XETM.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| XETM.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XETM.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XGD.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XGD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XGD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| XGD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| XGD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XGD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XGD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| XGD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| XGD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XGD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| XGD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XGD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XOM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| XOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| XOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| XOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| XOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| XOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
