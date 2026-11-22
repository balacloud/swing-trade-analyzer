# Statement Audit phase 3a report (Market backdrop, Fundamentals, Mean-Reversion Read)

Run: 2026-11-20T19:53 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 3440 · WRONG 11 (CRITICAL) · MISLEADING 6 (per-row severity) · UNVERIFIED 383 (INFO)

Recomputed from bars: MR RSI(2), % above the 200-day, dollar volume, the four rule marks, the blocker sentence; S&P 500 200/50-day and the 10-session drop (the app's own 260 bars); QQQ and "largest since" from an independent Yahoo history (S4).
Provider fields (sales growth, ROE, debt/equity) are arithmetic and flag logic only: no recompute is possible (UNVERIFIED as to truth). NOT YET COVERED: the Data Sources tab (phase 3b), other tabs; branches these tickers do not reach (signal true, VIX band edges, no-down-day, unavailable backdrop, negative equity) are exercised by planted tests only.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AVGO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.04% | -17.24% | WRONG | CRITICAL |  |
| BOTZ | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 33,350,600 | 30,338,814 | WRONG | CRITICAL |  |
| BOTZ | MR-price | price = the last completed close | 27.28 | 27.34 | WRONG | CRITICAL |  |
| BOTZ | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -24.4% | -24.23% | WRONG | CRITICAL |  |
| ETN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -21.16% | -21.60% | WRONG | CRITICAL |  |
| FCX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 973,414,542 | 885,855,147 | WRONG | CRITICAL |  |
| GDX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,304,889,317 | 2,196,747,760 | WRONG | CRITICAL |  |
| GE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -4.31% | -4.50% | WRONG | CRITICAL |  |
| NEM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 889,545,737 | 844,331,490 | WRONG | CRITICAL |  |
| ORCL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,520,590,290 | 5,215,243,796 | WRONG | CRITICAL |  |
| TSM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.77% | -21.02% | WRONG | CRITICAL |  |
| AVGO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -17.0% | TR -17.2% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| BOTZ | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -24.4% | TR -24.2% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| COTG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 64.33 | 63.83 | MISLEADING | LOW | within 0.8: the MR route smooths over its own frame length |
| ETN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -21.2% | TR -21.6% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| GE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -4.3% | TR -4.5% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| TSM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.8% | TR -21.0% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| ABBV | U-FU | numbers on the card no statement claimed (exhaustive scan) | -17.65 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ALAB | U-FU | numbers on the card no statement claimed (exhaustive scan) | 1 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AMD | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AVGO | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
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
| NFLX | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ONTO | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| PLD | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| QCOM | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| RTX | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| SO | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AAPL | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $325.43 2026 -11 -20 $342.56 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| AAPU | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $43.61 2026 -11 -20 $45.91 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| BRK-B | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $541.50 2026 -11 -20 $570.00 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| CNR.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $166.61 2026 -11 -20 $175.38 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| CSU.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% 941.20 2026 -11 -20 $3,096.00 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| LIN | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $477.69 2026 -11 -20 $502.83 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| LLY | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $1,279.75 2026 -11 -20 $1,347.11 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| MSFT | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $460.29 2026 -11 -20 $484.52 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| MSFU | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $32.52 2026 -11 -20 $34.23 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| V | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $381.78 2026 -11 -20 $401.87 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| WELL | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $228.32 2026 -11 -20 $240.34 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| AAPL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AAPL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AAPL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AAPU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AAPU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AAPU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ABBV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ABBV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ABBV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AIPO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AIPO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AIPO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ALAB | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ALAB | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ALAB | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AMD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AMD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AMD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AMD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMZN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AMZN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AMZN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMZU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AMZU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AMZU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ANET.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ANET.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ANET.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ASML.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ASML.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ASML.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ASTL.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ASTL.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ASTL.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ATD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ATD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ATD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGC | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AVGC | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AVGC | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AVGO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AVGO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGO.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| AVGO.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| AVGO.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BDT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| BDT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| BDT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BOTZ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| BOTZ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| BOTZ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BRK-B | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| BRK-B | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| BRK-B | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BRKU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| BRKU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| BRKU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CAMT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CAMT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CAMT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CARS.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CARS.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CARS.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CAT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CAT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CAT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CCO.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CCO.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CCO.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CEG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CEG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CEG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CGY.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CGY.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CGY.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CNQ.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CNQ.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CNQ.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CNR.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CNR.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CNR.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COP | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| COP | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| COP | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPP.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| COPP.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| COPP.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| COPX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| COPX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPZ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| COPZ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| COPZ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COST | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| COST | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| COST | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COTG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| COTG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| COTG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CSU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CSU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CSU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CVX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| CVX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| CVX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRAL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| DRAL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| DRAL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRAM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| DRAM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| DRAM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRIV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| DRIV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| DRIV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DUK | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| DUK | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| DUK | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ELIL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ELIL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ELIL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| EQIX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| EQIX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| EQIX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ETN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ETN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ETN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| FCX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| FCX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| FCX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| FINN.NE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| FINN.NE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| FINN.NE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GDX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GDX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GDX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GDXU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GDXU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GDXU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GEV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GEV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GEV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GEV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GEV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GEV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GGLL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GGLL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GGLL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GIB-A.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GIB-A.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GIB-A.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GOOGL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GOOGL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GOOGL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GRID | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| GRID | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| GRID | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| HD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| HD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HURA.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| HURA.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| HURA.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HXQ.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| HXQ.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| HXQ.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| JNJ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| JNJ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| JNJ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| JPM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| JPM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| JPM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| KEYS | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| KEYS | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| KEYS | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| LIN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| LIN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| LIN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| LLY | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| LLY | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| LLY | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MDA.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| MDA.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| MDA.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| META | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| META | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| META | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| METU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| METU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| METU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MRVL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| MRVL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| MRVL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MSFT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| MSFT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| MSFT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MSFU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| MSFU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| MSFU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MTRX.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| MTRX.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| MTRX.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| MU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| MU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NEE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| NEE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| NEE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NEM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| NEM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| NEM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NFLX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| NFLX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| NFLX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NFXL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| NFXL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| NFXL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NTR.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| NTR.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| NTR.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NVDA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| NVDA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| NVDA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NVDL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| NVDL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| NVDL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ONTO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ONTO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ONTO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ORBX.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ORBX.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ORBX.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ORCL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| ORCL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| ORCL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| PG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| PG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PLD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| PLD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| PLD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PNG.V | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| PNG.V | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| PNG.V | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QCOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| QCOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| QCOM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QPUX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| QPUX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| QPUX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QTUM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| QTUM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| QTUM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RBOT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| RBOT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| RBOT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RTX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| RTX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| RTX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RY.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| RY.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| RY.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SETM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SETM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SETM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SGRD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SGRD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SGRD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SMH | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SMH | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SMH | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SNDK.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SNDK.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SNDK.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SOXL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SOXL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXL.NE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SOXL.NE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SOXL.NE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SOXX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SOXX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SPCL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| SPCL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| SPCL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSLA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| TSLA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| TSLA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSLL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| TSLL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| TSLL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| TSM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| TSM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| UBOT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| UBOT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| UBOT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| UFO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| UFO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| UFO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| URA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| URA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| URA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| URAA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| URAA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| URAA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| V | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| V | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| V | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| VFV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| VFV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| VFV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| VRT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| VRT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| VRT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WDC.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| WDC.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| WDC.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WELL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| WELL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| WELL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WMT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| WMT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| WMT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XCHP.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| XCHP.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| XCHP.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XDRV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| XDRV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| XDRV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XEQT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| XEQT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| XEQT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XETM.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| XETM.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| XETM.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XGD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| XGD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| XGD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -5.4% on Nov 20 | -5.67% on Nov 20 | UNVERIFIED | INFO |  |
| XOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -14.2% | ↓ below -14.4% | UNVERIFIED | INFO | within provider tolerance but not exact |
| XOM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AAPL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.7% | +11.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AAPL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 127.6% | 127.6% flag=False | PASS |  |  |
| AAPL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| AAPL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AAPL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| AAPL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-02 (18 days ago); no upcoming date listed. | 2026-11-02 days_until=-18 | PASS |  |  |
| AAPU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AAPU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ABBV | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +10.3% | +10.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ABBV | FU3 | ROE: value (1 dp) and the flag at < 0% | ⚑ Return on equity ROE -92.0% | -92.0% flag=True | PASS |  |  |
| ABBV | FU4 | negative D/E -> "ratio not meaningful", unchecked | says so | not meaningful | PASS |  |  |
| ABBV | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| ABBV | FU5w | one plain sentence per tripped flag | Return on equity is negative. | 1 sentence(s) | PASS |  |  |
| ABBV | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| ABBV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (21 days ago); no upcoming date listed. | 2026-10-30 days_until=-21 | PASS |  |  |
| AIPO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AIPO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ALAB | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +153.7% | +153.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ALAB | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ALAB | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) | Alpha Vantage | PASS |  |  |
| ALAB | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (17 days ago); no upcoming date listed. | 2026-11-03 days_until=-17 | PASS |  |  |
| AMD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.6% | 11.6% flag=False | PASS |  |  |
| AMD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.10 | 0.10 flag=False | PASS |  |  |
| AMD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AMD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| AMD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (17 days ago); no upcoming date listed. | 2026-11-03 days_until=-17 | PASS |  |  |
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
| AMZN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (22 days ago); no upcoming date listed. | 2026-10-29 days_until=-22 | PASS |  |  |
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
| ATD.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-24 · in 4 days. Within a week: decide before then whether to hold throug | 2026-11-24 days_until=4 | PASS |  |  |
| AVGC | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AVGC | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| AVGO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 43.9% | 43.9% flag=False | PASS |  |  |
| AVGO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.60 | 0.60 flag=False | PASS |  |  |
| AVGO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AVGO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| AVGO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-09 · in 19 days. If you'll still hold on that date, the price can jump e | 2026-12-09 days_until=19 | PASS |  |  |
| AVGO.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AVGO.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| BDT.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.7% | +36.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| BDT.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.6% | 16.6% flag=False | PASS |  |  |
| BDT.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.79 | 0.79 flag=False | PASS |  |  |
| BDT.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| BDT.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| BDT.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-11 (9 days ago); no upcoming date listed. | 2026-11-11 days_until=-9 | PASS |  |  |
| BOTZ | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| BOTZ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| BRK-B | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.2% | +11.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| BRK-B | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.9% | 11.9% flag=False | PASS |  |  |
| BRK-B | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| BRK-B | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| BRK-B | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| BRK-B | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-07 (13 days ago); no upcoming date listed. | 2026-11-07 days_until=-13 | PASS |  |  |
| BRKU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| BRKU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CAMT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 5.8% | 5.8% flag=False | PASS |  |  |
| CAMT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.69 | 0.69 flag=False | PASS |  |  |
| CAMT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CAMT | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| CAMT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (16 days ago); no upcoming date listed. | 2026-11-04 days_until=-16 | PASS |  |  |
| CARS.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| CARS.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CAT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +17.3% | +17.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CAT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 58.5% | 58.5% flag=False | PASS |  |  |
| CAT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 2.10 | 2.10 flag=True | PASS |  |  |
| CAT | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| CAT | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| CAT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| CAT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (22 days ago); no upcoming date listed. | 2026-10-29 days_until=-22 | PASS |  |  |
| CCO.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +0.7% | +0.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CCO.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 5.7% | 5.7% flag=False | PASS |  |  |
| CCO.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.14 | 0.14 flag=False | PASS |  |  |
| CCO.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CCO.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CCO.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (21 days ago); no upcoming date listed. | 2026-10-30 days_until=-21 | PASS |  |  |
| CEG | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +45.4% | +45.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CEG | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 18.3% | 18.3% flag=False | PASS |  |  |
| CEG | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| CEG | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CEG | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CEG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-09 (11 days ago); no upcoming date listed. | 2026-11-09 days_until=-11 | PASS |  |  |
| CGY.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +19.9% | +19.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CGY.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 12.0% | 12.0% flag=False | PASS |  |  |
| CGY.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.54 | 0.54 flag=False | PASS |  |  |
| CGY.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CGY.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CGY.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-30 · in 10 days. If you'll still hold on that date, the price can jump e | 2026-11-30 days_until=10 | PASS |  |  |
| CNQ.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +34.4% | +34.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CNQ.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 32.4% | 32.4% flag=False | PASS |  |  |
| CNQ.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.42 | 0.42 flag=False | PASS |  |  |
| CNQ.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CNQ.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CNQ.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (15 days ago); no upcoming date listed. | 2026-11-05 days_until=-15 | PASS |  |  |
| CNR.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +14.6% | +14.6% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CNR.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 22.4% | 22.4% flag=False | PASS |  |  |
| CNR.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.09 | 1.09 flag=False | PASS |  |  |
| CNR.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CNR.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CNR.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-29 · in 70 days. If you'll still hold on that date, the price can jump e | 2027-01-29 days_until=70 | PASS |  |  |
| COP | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.8% | 17.8% flag=False | PASS |  |  |
| COP | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.35 | 0.35 flag=False | PASS |  |  |
| COP | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| COP | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| COP | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (15 days ago); no upcoming date listed. | 2026-11-05 days_until=-15 | PASS |  |  |
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
| COST | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-10 · in 20 days. If you'll still hold on that date, the price can jump e | 2026-12-10 days_until=20 | PASS |  |  |
| COTG | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| COTG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CSU.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +19.1% | +19.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CSU.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 24.2% | 24.2% flag=False | PASS |  |  |
| CSU.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.13 | 1.13 flag=False | PASS |  |  |
| CSU.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CSU.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CSU.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-06 (14 days ago); no upcoming date listed. | 2026-11-06 days_until=-14 | PASS |  |  |
| CVX | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +34.8% | +34.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CVX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 13.9% | 13.9% flag=False | PASS |  |  |
| CVX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| CVX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CVX | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CVX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (21 days ago); no upcoming date listed. | 2026-10-30 days_until=-21 | PASS |  |  |
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
| DUK | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (15 days ago); no upcoming date listed. | 2026-11-05 days_until=-15 | PASS |  |  |
| ELIL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ELIL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| EQIX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.5% | 11.5% flag=False | PASS |  |  |
| EQIX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.72 | 1.72 flag=False | PASS |  |  |
| EQIX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| EQIX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| EQIX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (23 days ago); no upcoming date listed. | 2026-10-28 days_until=-23 | PASS |  |  |
| ETN | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +28.0% | +28.0% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ETN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.5% | 19.5% flag=False | PASS |  |  |
| ETN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.00 | 1.00 flag=False | PASS |  |  |
| ETN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ETN | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| ETN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (17 days ago); no upcoming date listed. | 2026-11-03 days_until=-17 | PASS |  |  |
| FCX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 15.3% | 15.3% flag=False | PASS |  |  |
| FCX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.49 | 0.49 flag=False | PASS |  |  |
| FCX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| FCX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| FCX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (24 days ago); no upcoming date listed. | 2026-10-27 days_until=-24 | PASS |  |  |
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
| GE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (31 days ago); no upcoming date listed. | 2026-10-20 days_until=-31 | PASS |  |  |
| GEV | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +26.8% | +26.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| GEV | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 93.0% | 93.0% flag=False | PASS |  |  |
| GEV | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.30 | 0.30 flag=False | PASS |  |  |
| GEV | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GEV | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| GEV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-27 · in 68 days. If you'll still hold on that date, the price can jump e | 2027-01-27 days_until=68 | PASS |  |  |
| GEV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GEV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GGLL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GGLL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GIB-A.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +3.3% | +3.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| GIB-A.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.5% | 17.5% flag=False | PASS |  |  |
| GIB-A.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.39 | 0.39 flag=False | PASS |  |  |
| GIB-A.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GIB-A.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| GIB-A.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-11 (9 days ago); no upcoming date listed. | 2026-11-11 days_until=-9 | PASS |  |  |
| GOOGL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 42.6% | 42.6% flag=False | PASS |  |  |
| GOOGL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.18 | 0.18 flag=False | PASS |  |  |
| GOOGL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GOOGL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| GOOGL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (23 days ago); no upcoming date listed. | 2026-10-28 days_until=-23 | PASS |  |  |
| GRID | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GRID | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| HD | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +5.7% | +5.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| HD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 102.7% | 102.7% flag=False | PASS |  |  |
| HD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 3.18 | 3.18 flag=True | PASS |  |  |
| HD | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| HD | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| HD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| HD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-17 (3 days ago); no upcoming date listed. | 2026-11-17 days_until=-3 | PASS |  |  |
| HURA.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| HURA.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| HXQ.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| HXQ.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| JNJ | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.6% | 19.6% flag=False | PASS |  |  |
| JNJ | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.55 | 0.55 flag=False | PASS |  |  |
| JNJ | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| JNJ | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| JNJ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-26 · in 67 days. If you'll still hold on that date, the price can jump e | 2027-01-26 days_until=67 | PASS |  |  |
| JPM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +10.2% | +10.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| JPM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.9% | 17.9% flag=False | PASS |  |  |
| JPM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 3.32 | 3.32 flag=True | PASS |  |  |
| JPM | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| JPM | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| JPM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| JPM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-14 · in 55 days. If you'll still hold on that date, the price can jump e | 2027-01-14 days_until=55 | PASS |  |  |
| KEYS | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.5% | +36.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| KEYS | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 20.9% | 20.9% flag=False | PASS |  |  |
| KEYS | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.42 | 0.42 flag=False | PASS |  |  |
| KEYS | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| KEYS | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| KEYS | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-19 (1 day ago); no upcoming date listed. | 2026-11-19 days_until=-1 | PASS |  |  |
| LIN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 18.1% | 18.1% flag=False | PASS |  |  |
| LIN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.68 | 0.68 flag=False | PASS |  |  |
| LIN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| LIN | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| LIN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (22 days ago); no upcoming date listed. | 2026-10-29 days_until=-22 | PASS |  |  |
| LLY | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +38.6% | +38.6% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| LLY | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 83.7% | 83.7% flag=False | PASS |  |  |
| LLY | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.23 | 1.23 flag=False | PASS |  |  |
| LLY | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| LLY | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| LLY | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (22 days ago); no upcoming date listed. | 2026-10-29 days_until=-22 | PASS |  |  |
| MDA.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +21.5% | +21.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MDA.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 4.9% | 4.9% flag=False | PASS |  |  |
| MDA.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.31 | 0.31 flag=False | PASS |  |  |
| MDA.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MDA.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| MDA.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (15 days ago); no upcoming date listed. | 2026-11-05 days_until=-15 | PASS |  |  |
| META | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +26.1% | +26.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| META | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 30.3% | 30.3% flag=False | PASS |  |  |
| META | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.30 | 0.30 flag=False | PASS |  |  |
| META | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| META | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| META | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (30 days ago); no upcoming date listed. | 2026-10-21 days_until=-30 | PASS |  |  |
| METU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| METU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| MRVL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.5% | +36.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MRVL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.5% | 16.5% flag=False | PASS |  |  |
| MRVL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.29 | 0.29 flag=False | PASS |  |  |
| MRVL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MRVL | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| MRVL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-01 · in 11 days. If you'll still hold on that date, the price can jump e | 2026-12-01 days_until=11 | PASS |  |  |
| MSFT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +18.8% | +18.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MSFT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 33.2% | 33.2% flag=False | PASS |  |  |
| MSFT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.23 | 0.23 flag=False | PASS |  |  |
| MSFT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MSFT | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| MSFT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (23 days ago); no upcoming date listed. | 2026-10-28 days_until=-23 | PASS |  |  |
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
| NEE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (30 days ago); no upcoming date listed. | 2026-10-21 days_until=-30 | PASS |  |  |
| NEM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 26.5% | 26.5% flag=False | PASS |  |  |
| NEM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.16 | 0.16 flag=False | PASS |  |  |
| NEM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NEM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| NEM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-22 (29 days ago); no upcoming date listed. | 2026-10-22 days_until=-29 | PASS |  |  |
| NFLX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.4% | 50.4% flag=False | PASS |  |  |
| NFLX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.52 | 0.52 flag=False | PASS |  |  |
| NFLX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NFLX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| NFLX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (31 days ago); no upcoming date listed. | 2026-10-20 days_until=-31 | PASS |  |  |
| NFXL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| NFXL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| NTR.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +1.2% | +1.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NTR.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 8.8% | 8.8% flag=False | PASS |  |  |
| NTR.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.55 | 0.55 flag=False | PASS |  |  |
| NTR.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NTR.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| NTR.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (16 days ago); no upcoming date listed. | 2026-11-04 days_until=-16 | PASS |  |  |
| NVDA | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +105.8% | +105.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NVDA | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 110.1% | 110.1% flag=False | PASS |  |  |
| NVDA | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| NVDA | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NVDA | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NVDA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-17 (3 days ago); no upcoming date listed. | 2026-11-17 days_until=-3 | PASS |  |  |
| NVDL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| NVDL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ONTO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 6.5% | 6.5% flag=False | PASS |  |  |
| ONTO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.77 | 0.77 flag=False | PASS |  |  |
| ONTO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ONTO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| ONTO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-09 (11 days ago); no upcoming date listed. | 2026-11-09 days_until=-11 | PASS |  |  |
| ORBX.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ORBX.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ORCL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 42.6% | 42.6% flag=False | PASS |  |  |
| ORCL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 2.01 | 2.01 flag=True | PASS |  |  |
| ORCL | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| ORCL | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| ORCL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| ORCL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-14 · in 24 days. If you'll still hold on that date, the price can jump e | 2026-12-14 days_until=24 | PASS |  |  |
| PG | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +4.0% | +4.0% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| PG | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 29.6% | 29.6% flag=False | PASS |  |  |
| PG | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.70 | 0.70 flag=False | PASS |  |  |
| PG | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PG | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · yfinance (ROE, debt) | Alpha Vantage, yfinance | PASS |  |  |
| PG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-22 (29 days ago); no upcoming date listed. | 2026-10-22 days_until=-29 | PASS |  |  |
| PLD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 7.9% | 7.9% flag=False | PASS |  |  |
| PLD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.66 | 0.66 flag=False | PASS |  |  |
| PLD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PLD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| PLD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (36 days ago); no upcoming date listed. | 2026-10-15 days_until=-36 | PASS |  |  |
| PNG.V | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +3.5% | +3.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| PNG.V | FU3 | ROE: value (1 dp) and the flag at < 0% | ⚑ Return on equity ROE -4.3% | -4.3% flag=True | PASS |  |  |
| PNG.V | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| PNG.V | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| PNG.V | FU5w | one plain sentence per tripped flag | Return on equity is negative. | 1 sentence(s) | PASS |  |  |
| PNG.V | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| PNG.V | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-24 · in 4 days. Within a week: decide before then whether to hold throug | 2026-11-24 days_until=4 | PASS |  |  |
| QCOM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.3% | 50.3% flag=False | PASS |  |  |
| QCOM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.50 | 0.50 flag=False | PASS |  |  |
| QCOM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| QCOM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| QCOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (16 days ago); no upcoming date listed. | 2026-11-04 days_until=-16 | PASS |  |  |
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
| RTX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (31 days ago); no upcoming date listed. | 2026-10-20 days_until=-31 | PASS |  |  |
| RY.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +8.9% | +8.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| RY.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.2% | 16.2% flag=False | PASS |  |  |
| RY.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 4.10 | 4.10 flag=True | PASS |  |  |
| RY.TO | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| RY.TO | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| RY.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| RY.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-03 · in 13 days. If you'll still hold on that date, the price can jump e | 2026-12-03 days_until=13 | PASS |  |  |
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
| SO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (15 days ago); no upcoming date listed. | 2026-11-05 days_until=-15 | PASS |  |  |
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
| TSLA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (30 days ago); no upcoming date listed. | 2026-10-21 days_until=-30 | PASS |  |  |
| TSLL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| TSLL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| TSM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +50.9% | +50.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| TSM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 41.9% | 41.9% flag=False | PASS |  |  |
| TSM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| TSM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| TSM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| TSM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (36 days ago); no upcoming date listed. | 2026-10-15 days_until=-36 | PASS |  |  |
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
| V | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (24 days ago); no upcoming date listed. | 2026-10-27 days_until=-24 | PASS |  |  |
| VFV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| VFV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| VRT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +61.2% | +61.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| VRT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 46.6% | 46.6% flag=False | PASS |  |  |
| VRT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.61 | 0.61 flag=False | PASS |  |  |
| VRT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| VRT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| VRT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (23 days ago); no upcoming date listed. | 2026-10-28 days_until=-23 | PASS |  |  |
| WDC.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| WDC.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| WELL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +38.4% | +38.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| WELL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 3.7% | 3.7% flag=False | PASS |  |  |
| WELL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.40 | 0.40 flag=False | PASS |  |  |
| WELL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| WELL | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| WELL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-26 (25 days ago); no upcoming date listed. | 2026-10-26 days_until=-25 | PASS |  |  |
| WMT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +5.9% | +5.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| WMT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 22.3% | 22.3% flag=False | PASS |  |  |
| WMT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.72 | 0.72 flag=False | PASS |  |  |
| WMT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| WMT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| WMT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-02-18 · in 90 days. If you'll still hold on that date, the price can jump e | 2027-02-18 days_until=90 | PASS |  |  |
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
| XOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (21 days ago); no upcoming date listed. | 2026-10-30 days_until=-21 | PASS |  |  |
| AAPL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +13.1% | TR +13.1% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AAPL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 17,228,527,554 | 17,228,532,717 | PASS |  |  |
| AAPL | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| AAPL | MR-price | price = the last completed close | 342.56 | 342.56 | PASS |  |  |
| AAPL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $342.56 needs above $10 | $342.56 needs above $10 | PASS |  |  |
| AAPL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.9 needs under 10 | 2.87 needs under 10 -> ✓ | PASS |  |  |
| AAPL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 13.1% above its 200-day average | 13.1% above | PASS |  |  |
| AAPL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $17.2B traded on an average day needs above $25M | $17,228,527,554 needs above $25,000,000 | PASS |  |  |
| AAPL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.87 | 2.87 | PASS |  |  |
| AAPL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13.14% | 13.14% | PASS |  |  |
| AAPL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +19.8% | TR +19.8% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AAPU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 26,700,155 | 26,700,156 | PASS |  |  |
| AAPU | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| AAPU | MR-price | price = the last completed close | 45.91 | 45.91 | PASS |  |  |
| AAPU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $45.91 needs above $10 | $45.91 needs above $10 | PASS |  |  |
| AAPU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.4 needs under 10 | 2.41 needs under 10 -> ✓ | PASS |  |  |
| AAPU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 19.8% above its 200-day average | 19.8% above | PASS |  |  |
| AAPU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $26.7M traded on an average day needs above $25M | $26,700,155 needs above $25,000,000 | PASS |  |  |
| AAPU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.41 | 2.41 | PASS |  |  |
| AAPU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 19.78% | 19.78% | PASS |  |  |
| AAPU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ABBV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +19.3% | TR +19.3% | PASS | LOW | the two cards divide by different roundings of the average |
| ABBV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ABBV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| ABBV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ABBV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,547,374,483 | 1,547,374,478 | PASS |  |  |
| ABBV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ABBV | MR-price | price = the last completed close | 286.2 | 286.2 | PASS |  |  |
| ABBV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $286.20 needs above $10 | $286.20 needs above $10 | PASS |  |  |
| ABBV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 45.8 needs under 10 | 45.78 needs under 10 -> ✗ | PASS |  |  |
| ABBV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 19.3% above its 200-day average | 19.3% above | PASS |  |  |
| ABBV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.5B traded on an average day needs above $25M | $1,547,374,483 needs above $25,000,000 | PASS |  |  |
| ABBV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 45.78 | 45.78 | PASS |  |  |
| ABBV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 19.27% | 19.27% | PASS |  |  |
| ABBV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AIPO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -28.2% | TR -28.2% | PASS | LOW | the two cards divide by different roundings of the average |
| AIPO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AIPO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| AIPO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AIPO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 46,401,441 | 46,402,066 | PASS |  |  |
| AIPO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AIPO | MR-price | price = the last completed close | 20.43 | 20.43 | PASS |  |  |
| AIPO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $20.43 needs above $10 | $20.43 needs above $10 | PASS |  |  |
| AIPO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.2 needs under 10 | 1.23 needs under 10 -> ✓ | PASS |  |  |
| AIPO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 28.2% below its 200-day average | 28.2% below | PASS |  |  |
| AIPO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $46.4M traded on an average day needs above $25M | $46,401,441 needs above $25,000,000 | PASS |  |  |
| AIPO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.23 | 1.23 | PASS |  |  |
| AIPO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -28.22% | -28.22% | PASS |  |  |
| AIPO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ALAB | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -30.3% | TR -30.3% | PASS | LOW | the two cards divide by different roundings of the average |
| ALAB | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ALAB | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ALAB | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ALAB | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,219,785,018 | 1,219,785,007 | PASS |  |  |
| ALAB | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ALAB | MR-price | price = the last completed close | 180.35 | 180.35 | PASS |  |  |
| ALAB | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $180.35 needs above $10 | $180.35 needs above $10 | PASS |  |  |
| ALAB | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.9 needs under 10 | 6.91 needs under 10 -> ✓ | PASS |  |  |
| ALAB | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 30.3% below its 200-day average | 30.3% below | PASS |  |  |
| ALAB | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.2B traded on an average day needs above $25M | $1,219,785,018 needs above $25,000,000 | PASS |  |  |
| ALAB | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.91 | 6.91 | PASS |  |  |
| ALAB | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -30.32% | -30.32% | PASS |  |  |
| ALAB | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.3% | TR -1.3% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AMD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| AMD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 21,081,457,527 | 21,081,457,428 | PASS |  |  |
| AMD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD | MR-price | price = the last completed close | 424.39 | 424.39 | PASS |  |  |
| AMD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $424.39 needs above $10 | $424.39 needs above $10 | PASS |  |  |
| AMD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.0 needs under 10 | 7.95 needs under 10 -> ✓ | PASS |  |  |
| AMD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.3% below its 200-day average | 1.3% below | PASS |  |  |
| AMD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $21.1B traded on an average day needs above $25M | $21,081,457,527 needs above $25,000,000 | PASS |  |  |
| AMD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.95 | 7.95 | PASS |  |  |
| AMD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.26% | -1.26% | PASS |  |  |
| AMD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.5% | TR -1.4% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AMD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| AMD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 43,649,290 | 43,649,290 | PASS |  |  |
| AMD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD.TO | MR-price | price = the last completed close | 10.93 | 10.93 | PASS |  |  |
| AMD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $10.93 needs above $10 | $10.93 needs above $10 | PASS |  |  |
| AMD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.8 needs under 10 | 7.84 needs under 10 -> ✓ | PASS |  |  |
| AMD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.5% below its 200-day average | 1.5% below | PASS |  |  |
| AMD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $43.6M traded on an average day needs above $25M | $43,649,290 needs above $25,000,000 | PASS |  |  |
| AMD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.84 | 7.84 | PASS |  |  |
| AMD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.47% | -1.47% | PASS |  |  |
| AMD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMZN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +0.7% | TR +0.7% | PASS | LOW | the two cards divide by different roundings of the average |
| AMZN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AMZN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMZN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMZN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 13,552,035,804 | 13,552,485,132 | PASS |  |  |
| AMZN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMZN | MR-price | price = the last completed close | 246.82 | 246.82 | PASS |  |  |
| AMZN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $246.82 needs above $10 | $246.82 needs above $10 | PASS |  |  |
| AMZN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.4 needs under 10 | 13.42 needs under 10 -> ✗ | PASS |  |  |
| AMZN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.7% above its 200-day average | 0.7% above | PASS |  |  |
| AMZN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $13.6B traded on an average day needs above $25M | $13,552,035,804 needs above $25,000,000 | PASS |  |  |
| AMZN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.42 | 13.42 | PASS |  |  |
| AMZN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.68% | 0.68% | PASS |  |  |
| AMZN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMZU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -8.0% | TR -8.0% | PASS | LOW | the two cards divide by different roundings of the average |
| AMZU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AMZU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| AMZU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMZU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMZU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 66,860,097 | 66,860,098 | PASS |  |  |
| AMZU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMZU | MR-price | price = the last completed close | 32.16 | 32.16 | PASS |  |  |
| AMZU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $32.16 needs above $10 | $32.16 needs above $10 | PASS |  |  |
| AMZU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.2 needs under 10 | 13.24 needs under 10 -> ✗ | PASS |  |  |
| AMZU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 8.0% below its 200-day average | 8.0% below | PASS |  |  |
| AMZU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $66.9M traded on an average day needs above $25M | $66,860,097 needs above $25,000,000 | PASS |  |  |
| AMZU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.24 | 13.24 | PASS |  |  |
| AMZU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.95% | -7.95% | PASS |  |  |
| AMZU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ANET.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ANET.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| ANET.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ANET.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ANET.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ANET.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ANET.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,854,655 | 2,854,655 | PASS |  |  |
| ANET.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ANET.TO | MR-price | price = the last completed close | 29.87 | 29.87 | PASS |  |  |
| ANET.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $29.87 needs above $10 | $29.87 needs above $10 | PASS |  |  |
| ANET.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.8 needs under 10 | 7.78 needs under 10 -> ✓ | PASS |  |  |
| ANET.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.3% below its 200-day average | 1.3% below | PASS |  |  |
| ANET.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.9M traded on an average day needs above $25M | $2,854,655 needs above $25,000,000 | PASS |  |  |
| ANET.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.78 | 7.78 | PASS |  |  |
| ANET.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.27% | -1.27% | PASS |  |  |
| ANET.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ASML.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -13.6% | TR -13.6% | PASS | LOW | the two cards divide by different roundings of the average |
| ASML.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ASML.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| ASML.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASML.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASML.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,732,946 | 2,732,947 | PASS |  |  |
| ASML.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ASML.TO | MR-price | price = the last completed close | 38.95 | 38.95 | PASS |  |  |
| ASML.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $38.95 needs above $10 | $38.95 needs above $10 | PASS |  |  |
| ASML.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.4 needs under 10 | 6.36 needs under 10 -> ✓ | PASS |  |  |
| ASML.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 13.6% below its 200-day average | 13.6% below | PASS |  |  |
| ASML.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,732,946 needs above $25,000,000 | PASS |  |  |
| ASML.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.36 | 6.36 | PASS |  |  |
| ASML.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -13.64% | -13.64% | PASS |  |  |
| ASML.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ASTL.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.9% | TR -1.9% | PASS | LOW | the two cards divide by different roundings of the average |
| ASTL.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ASTL.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| ASTL.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASTL.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,710,006 | 5,710,007 | PASS |  |  |
| ASTL.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ASTL.TO | MR-price | price = the last completed close | 6.15 | 6.15 | PASS |  |  |
| ASTL.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $6.15 needs above $10 | $6.15 needs above $10 | PASS |  |  |
| ASTL.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.2 needs under 10 | 0.23 needs under 10 -> ✓ | PASS |  |  |
| ASTL.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.9% below its 200-day average | 1.9% below | PASS |  |  |
| ASTL.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $5.7M traded on an average day needs above $25M | $5,710,006 needs above $25,000,000 | PASS |  |  |
| ASTL.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.23 | 0.23 | PASS |  |  |
| ASTL.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.88% | -1.88% | PASS |  |  |
| ASTL.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ATD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.9% | TR -0.9% | PASS | LOW | the two cards divide by different roundings of the average |
| ATD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ATD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| ATD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ATD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ATD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 109,034,629 | 109,034,630 | PASS |  |  |
| ATD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ATD.TO | MR-price | price = the last completed close | 81.72 | 81.72 | PASS |  |  |
| ATD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $81.72 needs above $10 | $81.72 needs above $10 | PASS |  |  |
| ATD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 50.5 needs under 10 | 50.5 needs under 10 -> ✗ | PASS |  |  |
| ATD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.9% below its 200-day average | 0.9% below | PASS |  |  |
| ATD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $109M traded on an average day needs above $25M | $109,034,629 needs above $25,000,000 | PASS |  |  |
| ATD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 50.5 | 50.50 | PASS |  |  |
| ATD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.91% | -0.91% | PASS |  |  |
| ATD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AVGC | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| AVGO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AVGO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| AVGO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 10,001,456,286 | 10,002,553,118 | PASS |  |  |
| AVGO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AVGO | MR-price | price = the last completed close | 304.41 | 304.41 | PASS |  |  |
| AVGO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $304.41 needs above $10 | $304.41 needs above $10 | PASS |  |  |
| AVGO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.9 needs under 10 | 8.93 needs under 10 -> ✓ | PASS |  |  |
| AVGO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 17.0% below its 200-day average | 17.0% below | PASS |  |  |
| AVGO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $10B traded on an average day needs above $25M | $10,001,456,286 needs above $25,000,000 | PASS |  |  |
| AVGO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8.93 | 8.93 | PASS |  |  |
| AVGO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AVGO.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| AVGO.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| AVGO.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 21,248,811 | 21,248,909 | PASS |  |  |
| AVGO.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AVGO.TO | MR-price | price = the last completed close | 11.53 | 11.53 | PASS |  |  |
| AVGO.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $11.53 needs above $10 | $11.53 needs above $10 | PASS |  |  |
| AVGO.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.7 needs under 10 | 8.66 needs under 10 -> ✓ | PASS |  |  |
| AVGO.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 17.8% below its 200-day average | 17.8% below | PASS |  |  |
| AVGO.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $21.2M traded on an average day needs above $25M | $21,248,811 needs above $25,000,000 | PASS |  |  |
| AVGO.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8.66 | 8.66 | PASS |  |  |
| AVGO.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.78% | -17.78% | PASS |  |  |
| AVGO.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BDT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +17.4% | TR +17.4% | PASS | LOW | the two cards divide by different roundings of the average |
| BDT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| BDT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| BDT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BDT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 30,095,283 | 30,095,181 | PASS |  |  |
| BDT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BDT.TO | MR-price | price = the last completed close | 69.45 | 69.45 | PASS |  |  |
| BDT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $69.45 needs above $10 | $69.45 needs above $10 | PASS |  |  |
| BDT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.3 needs under 10 | 13.35 needs under 10 -> ✗ | PASS |  |  |
| BDT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 17.4% above its 200-day average | 17.4% above | PASS |  |  |
| BDT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $30.1M traded on an average day needs above $25M | $30,095,283 needs above $25,000,000 | PASS |  |  |
| BDT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.35 | 13.35 | PASS |  |  |
| BDT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 17.37% | 17.37% | PASS |  |  |
| BDT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BOTZ | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| BOTZ | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| BOTZ | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BOTZ | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BOTZ | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $27.28 needs above $10 | $27.28 needs above $10 | PASS |  |  |
| BOTZ | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.33 needs under 10 -> ✓ | PASS |  |  |
| BOTZ | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 24.4% below its 200-day average | 24.4% below | PASS |  |  |
| BOTZ | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $33.4M traded on an average day needs above $25M | $33,350,600 needs above $25,000,000 | PASS |  |  |
| BOTZ | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.33 | 0.34 | PASS |  |  |
| BOTZ | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BRK-B | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +13.4% | TR +13.4% | PASS | LOW | the two cards divide by different roundings of the average |
| BRK-B | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| BRK-B | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,035,020,091 | 3,035,020,068 | PASS |  |  |
| BRK-B | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| BRK-B | MR-price | price = the last completed close | 570 | 570 | PASS |  |  |
| BRK-B | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $570.00 needs above $10 | $570.00 needs above $10 | PASS |  |  |
| BRK-B | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.82 needs under 10 -> ✓ | PASS |  |  |
| BRK-B | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 13.4% above its 200-day average | 13.4% above | PASS |  |  |
| BRK-B | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3B traded on an average day needs above $25M | $3,035,020,091 needs above $25,000,000 | PASS |  |  |
| BRK-B | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.82 | 2.82 | PASS |  |  |
| BRK-B | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13.42% | 13.42% | PASS |  |  |
| BRK-B | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BRKU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +23.1% | TR +23.2% | PASS | LOW | the two cards divide by different roundings of the average |
| BRKU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| BRKU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it does not trade enough dollars a day | it does not trade enough dollars a day | PASS |  |  |
| BRKU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BRKU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,723,156 | 2,723,127 | PASS |  |  |
| BRKU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BRKU | MR-price | price = the last completed close | 28.45 | 28.45 | PASS |  |  |
| BRKU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $28.45 needs above $10 | $28.45 needs above $10 | PASS |  |  |
| BRKU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.1 needs under 10 | 3.13 needs under 10 -> ✓ | PASS |  |  |
| BRKU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 23.1% above its 200-day average | 23.1% above | PASS |  |  |
| BRKU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,723,156 needs above $25,000,000 | PASS |  |  |
| BRKU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.13 | 3.13 | PASS |  |  |
| BRKU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 23.15% | 23.15% | PASS |  |  |
| BRKU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CAMT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -42.2% | TR -42.2% | PASS | LOW | the two cards divide by different roundings of the average |
| CAMT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CAMT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| CAMT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAMT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAMT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 58,667,010 | 58,667,010 | PASS |  |  |
| CAMT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CAMT | MR-price | price = the last completed close | 89.2 | 89.2 | PASS |  |  |
| CAMT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $89.20 needs above $10 | $89.20 needs above $10 | PASS |  |  |
| CAMT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.6 needs under 10 | 10.61 needs under 10 -> ✗ | PASS |  |  |
| CAMT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 42.2% below its 200-day average | 42.2% below | PASS |  |  |
| CAMT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $58.7M traded on an average day needs above $25M | $58,667,010 needs above $25,000,000 | PASS |  |  |
| CAMT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.61 | 10.61 | PASS |  |  |
| CAMT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -42.16% | -42.16% | PASS |  |  |
| CAMT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CARS.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -35.1% | TR -35.1% | PASS | LOW | the two cards divide by different roundings of the average |
| CARS.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CARS.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| CARS.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CARS.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CARS.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CARS.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CARS.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 28,453 | 28,455 | PASS |  |  |
| CARS.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CARS.TO | MR-price | price = the last completed close | 18.07 | 18.07 | PASS |  |  |
| CARS.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $18.07 needs above $10 | $18.07 needs above $10 | PASS |  |  |
| CARS.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.0 needs under 10 | 1.02 needs under 10 -> ✓ | PASS |  |  |
| CARS.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 35.1% below its 200-day average | 35.1% below | PASS |  |  |
| CARS.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $28,453 traded on an average day needs above $25M | $28,453 needs above $25,000,000 | PASS |  |  |
| CARS.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.02 | 1.02 | PASS |  |  |
| CARS.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -35.15% | -35.15% | PASS |  |  |
| CARS.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CAT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -36.3% | TR -36.3% | PASS | LOW | the two cards divide by different roundings of the average |
| CAT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CAT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CAT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,548,809,956 | 2,548,809,948 | PASS |  |  |
| CAT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CAT | MR-price | price = the last completed close | 510.63 | 510.63 | PASS |  |  |
| CAT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $510.63 needs above $10 | $510.63 needs above $10 | PASS |  |  |
| CAT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.7 needs under 10 | 0.73 needs under 10 -> ✓ | PASS |  |  |
| CAT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 36.3% below its 200-day average | 36.3% below | PASS |  |  |
| CAT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.5B traded on an average day needs above $25M | $2,548,809,956 needs above $25,000,000 | PASS |  |  |
| CAT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.73 | 0.73 | PASS |  |  |
| CAT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -36.26% | -36.26% | PASS |  |  |
| CAT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CCO.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -40.5% | TR -40.5% | PASS | LOW | the two cards divide by different roundings of the average |
| CCO.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CCO.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CCO.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CCO.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 156,048,700 | 156,048,699 | PASS |  |  |
| CCO.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CCO.TO | MR-price | price = the last completed close | 83.11 | 83.11 | PASS |  |  |
| CCO.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $83.11 needs above $10 | $83.11 needs above $10 | PASS |  |  |
| CCO.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.5 needs under 10 | 0.49 needs under 10 -> ✓ | PASS |  |  |
| CCO.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 40.5% below its 200-day average | 40.5% below | PASS |  |  |
| CCO.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $156M traded on an average day needs above $25M | $156,048,700 needs above $25,000,000 | PASS |  |  |
| CCO.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.49 | 0.49 | PASS |  |  |
| CCO.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -40.52% | -40.52% | PASS |  |  |
| CCO.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CEG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.4% | TR -14.4% | PASS | LOW | the two cards divide by different roundings of the average |
| CEG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CEG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CEG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CEG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,013,934,628 | 1,013,936,881 | PASS |  |  |
| CEG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CEG | MR-price | price = the last completed close | 237.41 | 237.41 | PASS |  |  |
| CEG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $237.41 needs above $10 | $237.41 needs above $10 | PASS |  |  |
| CEG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.0 needs under 10 | 1.03 needs under 10 -> ✓ | PASS |  |  |
| CEG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.4% below its 200-day average | 14.4% below | PASS |  |  |
| CEG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1B traded on an average day needs above $25M | $1,013,934,628 needs above $25,000,000 | PASS |  |  |
| CEG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.03 | 1.03 | PASS |  |  |
| CEG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.42% | -14.42% | PASS |  |  |
| CEG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CGY.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.4% | TR -0.4% | PASS | LOW | the two cards divide by different roundings of the average |
| CGY.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CGY.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| CGY.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CGY.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CGY.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,515,282 | 2,515,282 | PASS |  |  |
| CGY.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CGY.TO | MR-price | price = the last completed close | 78.75 | 78.75 | PASS |  |  |
| CGY.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $78.75 needs above $10 | $78.75 needs above $10 | PASS |  |  |
| CGY.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.0 needs under 10 | 0.98 needs under 10 -> ✓ | PASS |  |  |
| CGY.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.4% below its 200-day average | 0.4% below | PASS |  |  |
| CGY.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.5M traded on an average day needs above $25M | $2,515,282 needs above $25,000,000 | PASS |  |  |
| CGY.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.98 | 0.98 | PASS |  |  |
| CGY.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.41% | -0.41% | PASS |  |  |
| CGY.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CNQ.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.9% | TR -0.9% | PASS | LOW | the two cards divide by different roundings of the average |
| CNQ.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CNQ.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CNQ.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CNQ.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 693,613,394 | 693,613,387 | PASS |  |  |
| CNQ.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CNQ.TO | MR-price | price = the last completed close | 63.74 | 63.74 | PASS |  |  |
| CNQ.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $63.74 needs above $10 | $63.74 needs above $10 | PASS |  |  |
| CNQ.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.3 needs under 10 | 2.3 needs under 10 -> ✓ | PASS |  |  |
| CNQ.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.9% below its 200-day average | 0.9% below | PASS |  |  |
| CNQ.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $693.6M traded on an average day needs above $25M | $693,613,394 needs above $25,000,000 | PASS |  |  |
| CNQ.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.3 | 2.30 | PASS |  |  |
| CNQ.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.95% | -0.95% | PASS |  |  |
| CNQ.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CNR.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +8.0% | TR +8.0% | PASS | LOW | the two cards divide by different roundings of the average |
| CNR.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CNR.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 224,747,436 | 224,747,435 | PASS |  |  |
| CNR.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| CNR.TO | MR-price | price = the last completed close | 175.38 | 175.38 | PASS |  |  |
| CNR.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $175.38 needs above $10 | $175.38 needs above $10 | PASS |  |  |
| CNR.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.79 needs under 10 -> ✓ | PASS |  |  |
| CNR.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 8.0% above its 200-day average | 8.0% above | PASS |  |  |
| CNR.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $224.7M traded on an average day needs above $25M | $224,747,436 needs above $25,000,000 | PASS |  |  |
| CNR.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.79 | 2.79 | PASS |  |  |
| CNR.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 7.96% | 7.96% | PASS |  |  |
| CNR.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COP | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +11.1% | TR +11.1% | PASS | LOW | the two cards divide by different roundings of the average |
| COP | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| COP | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| COP | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COP | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,043,055,063 | 1,043,048,365 | PASS |  |  |
| COP | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COP | MR-price | price = the last completed close | 136.12 | 136.12 | PASS |  |  |
| COP | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $136.12 needs above $10 | $136.12 needs above $10 | PASS |  |  |
| COP | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 51.5 needs under 10 | 51.53 needs under 10 -> ✗ | PASS |  |  |
| COP | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 11.1% above its 200-day average | 11.1% above | PASS |  |  |
| COP | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1B traded on an average day needs above $25M | $1,043,055,063 needs above $25,000,000 | PASS |  |  |
| COP | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 51.53 | 51.54 | PASS |  |  |
| COP | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 11.09% | 11.09% | PASS |  |  |
| COP | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPP.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -32.3% | TR -32.3% | PASS | LOW | the two cards divide by different roundings of the average |
| COPP.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| COPP.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| COPP.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPP.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPP.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPP.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPP.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 904,915 | 904,916 | PASS |  |  |
| COPP.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COPP.TO | MR-price | price = the last completed close | 39.49 | 39.49 | PASS |  |  |
| COPP.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $39.49 needs above $10 | $39.49 needs above $10 | PASS |  |  |
| COPP.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.3 needs under 10 -> ✓ | PASS |  |  |
| COPP.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 32.3% below its 200-day average | 32.3% below | PASS |  |  |
| COPP.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $904,915 traded on an average day needs above $25M | $904,915 needs above $25,000,000 | PASS |  |  |
| COPP.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.3 | 0.30 | PASS |  |  |
| COPP.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -32.28% | -32.28% | PASS |  |  |
| COPP.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -31.3% | TR -31.3% | PASS | LOW | the two cards divide by different roundings of the average |
| COPX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| COPX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| COPX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 274,578,091 | 274,578,091 | PASS |  |  |
| COPX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COPX | MR-price | price = the last completed close | 56.33 | 56.33 | PASS |  |  |
| COPX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $56.33 needs above $10 | $56.33 needs above $10 | PASS |  |  |
| COPX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.26 needs under 10 -> ✓ | PASS |  |  |
| COPX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 31.3% below its 200-day average | 31.3% below | PASS |  |  |
| COPX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $274.6M traded on an average day needs above $25M | $274,578,091 needs above $25,000,000 | PASS |  |  |
| COPX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.26 | 0.26 | PASS |  |  |
| COPX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -31.31% | -31.31% | PASS |  |  |
| COPX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPZ | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| COST | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +12.6% | TR +12.6% | PASS | LOW | the two cards divide by different roundings of the average |
| COST | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| COST | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| COST | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COST | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,712,283,498 | 2,712,283,499 | PASS |  |  |
| COST | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COST | MR-price | price = the last completed close | 1102.15 | 1102.15 | PASS |  |  |
| COST | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,102.15 needs above $10 | $1,102.15 needs above $10 | PASS |  |  |
| COST | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 64.5 needs under 10 | 64.51 needs under 10 -> ✗ | PASS |  |  |
| COST | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 12.6% above its 200-day average | 12.6% above | PASS |  |  |
| COST | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.7B traded on an average day needs above $25M | $2,712,283,498 needs above $25,000,000 | PASS |  |  |
| COST | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 64.51 | 64.51 | PASS |  |  |
| COST | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 12.58% | 12.58% | PASS |  |  |
| COST | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COTG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +19.8% | TR +19.7% | PASS | LOW | the two cards divide by different roundings of the average |
| COTG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| COTG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| COTG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COTG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COTG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COTG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COTG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,089,471 | 1,089,557 | PASS |  |  |
| COTG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COTG | MR-price | price = the last completed close | 16.69 | 16.69 | PASS |  |  |
| COTG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $16.69 needs above $10 | $16.69 needs above $10 | PASS |  |  |
| COTG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 64.3 needs under 10 | 64.33 needs under 10 -> ✗ | PASS |  |  |
| COTG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 19.8% above its 200-day average | 19.8% above | PASS |  |  |
| COTG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.1M traded on an average day needs above $25M | $1,089,471 needs above $25,000,000 | PASS |  |  |
| COTG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 19.75% | 19.71% | PASS |  |  |
| COTG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CSU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +9.6% | TR +9.6% | PASS | LOW | the two cards divide by different roundings of the average |
| CSU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CSU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 206,518,858 | 206,518,858 | PASS |  |  |
| CSU.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| CSU.TO | MR-price | price = the last completed close | 3096 | 3096 | PASS |  |  |
| CSU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $3,096.00 needs above $10 | $3,096.00 needs above $10 | PASS |  |  |
| CSU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.5 needs under 10 | 1.49 needs under 10 -> ✓ | PASS |  |  |
| CSU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 9.6% above its 200-day average | 9.6% above | PASS |  |  |
| CSU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $206.5M traded on an average day needs above $25M | $206,518,858 needs above $25,000,000 | PASS |  |  |
| CSU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.49 | 1.49 | PASS |  |  |
| CSU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 9.6% | 9.60% | PASS |  |  |
| CSU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CVX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +7.8% | TR +7.8% | PASS | LOW | the two cards divide by different roundings of the average |
| CVX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| CVX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CVX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CVX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,847,382,198 | 1,847,374,703 | PASS |  |  |
| CVX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CVX | MR-price | price = the last completed close | 208.37 | 208.37 | PASS |  |  |
| CVX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $208.37 needs above $10 | $208.37 needs above $10 | PASS |  |  |
| CVX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 49.3 needs under 10 | 49.3 needs under 10 -> ✗ | PASS |  |  |
| CVX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 7.8% above its 200-day average | 7.8% above | PASS |  |  |
| CVX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.8B traded on an average day needs above $25M | $1,847,382,198 needs above $25,000,000 | PASS |  |  |
| CVX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 49.3 | 49.30 | PASS |  |  |
| CVX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 7.79% | 7.79% | PASS |  |  |
| CVX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DRAL | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| DRAM | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| DRIV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -27.9% | TR -28.0% | PASS | LOW | the two cards divide by different roundings of the average |
| DRIV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| DRIV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| DRIV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DRIV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DRIV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DRIV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DRIV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,080,521 | 1,080,507 | PASS |  |  |
| DRIV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DRIV | MR-price | price = the last completed close | 24.59 | 24.59 | PASS |  |  |
| DRIV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $24.59 needs above $10 | $24.59 needs above $10 | PASS |  |  |
| DRIV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.3 needs under 10 -> ✓ | PASS |  |  |
| DRIV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 27.9% below its 200-day average | 27.9% below | PASS |  |  |
| DRIV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.1M traded on an average day needs above $25M | $1,080,521 needs above $25,000,000 | PASS |  |  |
| DRIV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.3 | 0.31 | PASS |  |  |
| DRIV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -27.94% | -27.94% | PASS |  |  |
| DRIV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DUK | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +5.6% | TR +5.6% | PASS | LOW | the two cards divide by different roundings of the average |
| DUK | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| DUK | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| DUK | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DUK | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 664,794,034 | 664,794,503 | PASS |  |  |
| DUK | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DUK | MR-price | price = the last completed close | 129.78 | 129.78 | PASS |  |  |
| DUK | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $129.78 needs above $10 | $129.78 needs above $10 | PASS |  |  |
| DUK | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 61.7 needs under 10 | 61.67 needs under 10 -> ✗ | PASS |  |  |
| DUK | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 5.6% above its 200-day average | 5.6% above | PASS |  |  |
| DUK | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $664.8M traded on an average day needs above $25M | $664,794,034 needs above $25,000,000 | PASS |  |  |
| DUK | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 61.67 | 61.67 | PASS |  |  |
| DUK | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 5.59% | 5.59% | PASS |  |  |
| DUK | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ELIL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +34.0% | TR +34.0% | PASS | LOW | the two cards divide by different roundings of the average |
| ELIL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ELIL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it does not trade enough dollars a day | it does not trade enough dollars a day | PASS |  |  |
| ELIL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ELIL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,718,066 | 2,718,041 | PASS |  |  |
| ELIL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ELIL | MR-price | price = the last completed close | 36.41 | 36.41 | PASS |  |  |
| ELIL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $36.41 needs above $10 | $36.41 needs above $10 | PASS |  |  |
| ELIL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.1 needs under 10 | 2.15 needs under 10 -> ✓ | PASS |  |  |
| ELIL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 34.0% above its 200-day average | 34.0% above | PASS |  |  |
| ELIL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,718,066 needs above $25,000,000 | PASS |  |  |
| ELIL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.15 | 2.15 | PASS |  |  |
| ELIL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 33.99% | 33.99% | PASS |  |  |
| ELIL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| EQIX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -4.8% | TR -4.8% | PASS | LOW | the two cards divide by different roundings of the average |
| EQIX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| EQIX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| EQIX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| EQIX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 815,531,941 | 815,532,734 | PASS |  |  |
| EQIX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| EQIX | MR-price | price = the last completed close | 968.44 | 968.44 | PASS |  |  |
| EQIX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $968.44 needs above $10 | $968.44 needs above $10 | PASS |  |  |
| EQIX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.3 needs under 10 | 3.25 needs under 10 -> ✓ | PASS |  |  |
| EQIX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 4.8% below its 200-day average | 4.8% below | PASS |  |  |
| EQIX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $815.5M traded on an average day needs above $25M | $815,531,941 needs above $25,000,000 | PASS |  |  |
| EQIX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.25 | 3.25 | PASS |  |  |
| EQIX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -4.8% | -4.80% | PASS |  |  |
| EQIX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ETN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ETN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ETN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ETN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,174,576,302 | 1,177,477,414 | PASS |  |  |
| ETN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ETN | MR-price | price = the last completed close | 311.33 | 311.33 | PASS |  |  |
| ETN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $311.33 needs above $10 | $311.33 needs above $10 | PASS |  |  |
| ETN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.8 needs under 10 | 1.76 needs under 10 -> ✓ | PASS |  |  |
| ETN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 21.2% below its 200-day average | 21.2% below | PASS |  |  |
| ETN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.2B traded on an average day needs above $25M | $1,174,576,302 needs above $25,000,000 | PASS |  |  |
| ETN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.76 | 1.77 | PASS |  |  |
| ETN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| FCX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -28.9% | TR -28.9% | PASS | LOW | the two cards divide by different roundings of the average |
| FCX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| FCX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| FCX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FCX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| FCX | MR-price | price = the last completed close | 45.99 | 45.99 | PASS |  |  |
| FCX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $45.99 needs above $10 | $45.99 needs above $10 | PASS |  |  |
| FCX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.6 needs under 10 | 0.63 needs under 10 -> ✓ | PASS |  |  |
| FCX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 28.9% below its 200-day average | 28.9% below | PASS |  |  |
| FCX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $973.4M traded on an average day needs above $25M | $973,414,542 needs above $25,000,000 | PASS |  |  |
| FCX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.63 | 0.63 | PASS |  |  |
| FCX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -28.93% | -28.94% | PASS |  |  |
| FCX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| FINN.NE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +0.6% | TR +0.6% | PASS | LOW | the two cards divide by different roundings of the average |
| FINN.NE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| FINN.NE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it does not trade enough dollars a day | it does not trade enough dollars a day | PASS |  |  |
| FINN.NE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FINN.NE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FINN.NE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FINN.NE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FINN.NE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 11,868,791 | 11,868,792 | PASS |  |  |
| FINN.NE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| FINN.NE | MR-price | price = the last completed close | 30.38 | 30.38 | PASS |  |  |
| FINN.NE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $30.38 needs above $10 | $30.38 needs above $10 | PASS |  |  |
| FINN.NE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.4 needs under 10 | 3.39 needs under 10 -> ✓ | PASS |  |  |
| FINN.NE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.6% above its 200-day average | 0.6% above | PASS |  |  |
| FINN.NE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $11.9M traded on an average day needs above $25M | $11,868,791 needs above $25,000,000 | PASS |  |  |
| FINN.NE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.39 | 3.39 | PASS |  |  |
| FINN.NE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.63% | 0.63% | PASS |  |  |
| FINN.NE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GDX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.2% | TR -23.2% | PASS | LOW | the two cards divide by different roundings of the average |
| GDX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GDX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GDX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GDX | MR-price | price = the last completed close | 68.41 | 68.4 | PASS |  |  |
| GDX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $68.41 needs above $10 | $68.41 needs above $10 | PASS |  |  |
| GDX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.4 needs under 10 | 1.37 needs under 10 -> ✓ | PASS |  |  |
| GDX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.2% below its 200-day average | 23.2% below | PASS |  |  |
| GDX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.3B traded on an average day needs above $25M | $2,304,889,317 needs above $25,000,000 | PASS |  |  |
| GDX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.37 | 1.36 | PASS |  |  |
| GDX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.19% | -23.20% | PASS |  |  |
| GDX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GDXU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -48.8% | TR -48.8% | PASS | LOW | the two cards divide by different roundings of the average |
| GDXU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GDXU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| GDXU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDXU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDXU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 8,874,822 | 8,874,823 | PASS |  |  |
| GDXU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GDXU.TO | MR-price | price = the last completed close | 18.2 | 18.2 | PASS |  |  |
| GDXU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $18.20 needs above $10 | $18.20 needs above $10 | PASS |  |  |
| GDXU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.2 needs under 10 | 1.2 needs under 10 -> ✓ | PASS |  |  |
| GDXU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 48.8% below its 200-day average | 48.8% below | PASS |  |  |
| GDXU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $8.9M traded on an average day needs above $25M | $8,874,822 needs above $25,000,000 | PASS |  |  |
| GDXU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.2 | 1.20 | PASS |  |  |
| GDXU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -48.77% | -48.77% | PASS |  |  |
| GDXU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,570,389,062 | 1,571,061,906 | PASS |  |  |
| GE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GE | MR-price | price = the last completed close | 309.62 | 309.62 | PASS |  |  |
| GE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $309.62 needs above $10 | $309.62 needs above $10 | PASS |  |  |
| GE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.5 needs under 10 | 4.55 needs under 10 -> ✓ | PASS |  |  |
| GE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 4.3% below its 200-day average | 4.3% below | PASS |  |  |
| GE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.6B traded on an average day needs above $25M | $1,570,389,062 needs above $25,000,000 | PASS |  |  |
| GE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.55 | 4.55 | PASS |  |  |
| GE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GEV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -26.5% | TR -26.5% | PASS | LOW | the two cards divide by different roundings of the average |
| GEV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GEV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GEV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,624,589,382 | 3,628,088,302 | PASS |  |  |
| GEV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GEV | MR-price | price = the last completed close | 699.33 | 699.33 | PASS |  |  |
| GEV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $699.33 needs above $10 | $699.33 needs above $10 | PASS |  |  |
| GEV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.3 needs under 10 | 3.33 needs under 10 -> ✓ | PASS |  |  |
| GEV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 26.5% below its 200-day average | 26.5% below | PASS |  |  |
| GEV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3.6B traded on an average day needs above $25M | $3,624,589,382 needs above $25,000,000 | PASS |  |  |
| GEV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.33 | 3.33 | PASS |  |  |
| GEV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -26.47% | -26.53% | PASS |  |  |
| GEV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GEV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GEV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| GEV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,745,464 | 6,745,470 | PASS |  |  |
| GEV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GEV.TO | MR-price | price = the last completed close | 46.48 | 46.48 | PASS |  |  |
| GEV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $46.48 needs above $10 | $46.48 needs above $10 | PASS |  |  |
| GEV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.1 needs under 10 | 3.15 needs under 10 -> ✓ | PASS |  |  |
| GEV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 27.4% below its 200-day average | 27.4% below | PASS |  |  |
| GEV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $6.7M traded on an average day needs above $25M | $6,745,464 needs above $25,000,000 | PASS |  |  |
| GEV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.15 | 3.15 | PASS |  |  |
| GEV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -27.44% | -27.44% | PASS |  |  |
| GEV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GGLL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -44.6% | TR -44.6% | PASS | LOW | the two cards divide by different roundings of the average |
| GGLL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GGLL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GGLL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GGLL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 195,249,803 | 195,249,804 | PASS |  |  |
| GGLL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GGLL | MR-price | price = the last completed close | 56.59 | 56.59 | PASS |  |  |
| GGLL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $56.59 needs above $10 | $56.59 needs above $10 | PASS |  |  |
| GGLL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.4 needs under 10 | 5.42 needs under 10 -> ✓ | PASS |  |  |
| GGLL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 44.6% below its 200-day average | 44.6% below | PASS |  |  |
| GGLL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $195.2M traded on an average day needs above $25M | $195,249,803 needs above $25,000,000 | PASS |  |  |
| GGLL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.42 | 5.42 | PASS |  |  |
| GGLL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -44.6% | -44.60% | PASS |  |  |
| GGLL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GIB-A.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +14.0% | TR +14.0% | PASS | LOW | the two cards divide by different roundings of the average |
| GIB-A.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GIB-A.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| GIB-A.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GIB-A.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 78,059,662 | 78,059,663 | PASS |  |  |
| GIB-A.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GIB-A.TO | MR-price | price = the last completed close | 113.76 | 113.76 | PASS |  |  |
| GIB-A.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $113.76 needs above $10 | $113.76 needs above $10 | PASS |  |  |
| GIB-A.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 46.8 needs under 10 | 46.79 needs under 10 -> ✗ | PASS |  |  |
| GIB-A.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 14.0% above its 200-day average | 14.0% above | PASS |  |  |
| GIB-A.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $78.1M traded on an average day needs above $25M | $78,059,662 needs above $25,000,000 | PASS |  |  |
| GIB-A.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 46.79 | 46.79 | PASS |  |  |
| GIB-A.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13.96% | 13.96% | PASS |  |  |
| GIB-A.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GOOGL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -21.2% | TR -21.2% | PASS | LOW | the two cards divide by different roundings of the average |
| GOOGL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GOOGL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GOOGL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GOOGL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 13,019,281,670 | 13,019,281,572 | PASS |  |  |
| GOOGL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GOOGL | MR-price | price = the last completed close | 265.29 | 265.29 | PASS |  |  |
| GOOGL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $265.29 needs above $10 | $265.29 needs above $10 | PASS |  |  |
| GOOGL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.9 needs under 10 | 4.92 needs under 10 -> ✓ | PASS |  |  |
| GOOGL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 21.2% below its 200-day average | 21.2% below | PASS |  |  |
| GOOGL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $13B traded on an average day needs above $25M | $13,019,281,670 needs above $25,000,000 | PASS |  |  |
| GOOGL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.92 | 4.92 | PASS |  |  |
| GOOGL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -21.21% | -21.21% | PASS |  |  |
| GOOGL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GRID | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -18.2% | TR -18.2% | PASS | LOW | the two cards divide by different roundings of the average |
| GRID | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| GRID | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GRID | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GRID | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 108,426,684 | 108,426,686 | PASS |  |  |
| GRID | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GRID | MR-price | price = the last completed close | 145.44 | 145.44 | PASS |  |  |
| GRID | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $145.44 needs above $10 | $145.44 needs above $10 | PASS |  |  |
| GRID | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.5 needs under 10 | 0.54 needs under 10 -> ✓ | PASS |  |  |
| GRID | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.2% below its 200-day average | 18.2% below | PASS |  |  |
| GRID | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $108.4M traded on an average day needs above $25M | $108,426,684 needs above $25,000,000 | PASS |  |  |
| GRID | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.54 | 0.54 | PASS |  |  |
| GRID | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -18.17% | -18.17% | PASS |  |  |
| GRID | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +3.2% | TR +3.2% | PASS | LOW | the two cards divide by different roundings of the average |
| HD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| HD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| HD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,845,930,509 | 1,845,930,488 | PASS |  |  |
| HD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HD | MR-price | price = the last completed close | 339.1 | 339.1 | PASS |  |  |
| HD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $339.10 needs above $10 | $339.10 needs above $10 | PASS |  |  |
| HD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 54.9 needs under 10 | 54.86 needs under 10 -> ✗ | PASS |  |  |
| HD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 3.2% above its 200-day average | 3.2% above | PASS |  |  |
| HD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.8B traded on an average day needs above $25M | $1,845,930,509 needs above $25,000,000 | PASS |  |  |
| HD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 54.86 | 54.86 | PASS |  |  |
| HD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 3.19% | 3.19% | PASS |  |  |
| HD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HURA.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -35.6% | TR -35.6% | PASS | LOW | the two cards divide by different roundings of the average |
| HURA.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| HURA.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| HURA.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HURA.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HURA.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HURA.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HURA.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 527,078 | 527,078 | PASS |  |  |
| HURA.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HURA.TO | MR-price | price = the last completed close | 33.89 | 33.89 | PASS |  |  |
| HURA.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $33.89 needs above $10 | $33.89 needs above $10 | PASS |  |  |
| HURA.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.4 needs under 10 | 0.38 needs under 10 -> ✓ | PASS |  |  |
| HURA.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 35.6% below its 200-day average | 35.6% below | PASS |  |  |
| HURA.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $527,078 traded on an average day needs above $25M | $527,078 needs above $25,000,000 | PASS |  |  |
| HURA.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.38 | 0.38 | PASS |  |  |
| HURA.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -35.56% | -35.56% | PASS |  |  |
| HURA.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HXQ.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -8.0% | TR -8.0% | PASS | LOW | the two cards divide by different roundings of the average |
| HXQ.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| HXQ.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| HXQ.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HXQ.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HXQ.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,404,940 | 5,404,940 | PASS |  |  |
| HXQ.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HXQ.TO | MR-price | price = the last completed close | 103.4 | 103.4 | PASS |  |  |
| HXQ.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $103.40 needs above $10 | $103.40 needs above $10 | PASS |  |  |
| HXQ.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.1 needs under 10 | 4.1 needs under 10 -> ✓ | PASS |  |  |
| HXQ.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 8.0% below its 200-day average | 8.0% below | PASS |  |  |
| HXQ.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $5.4M traded on an average day needs above $25M | $5,404,940 needs above $25,000,000 | PASS |  |  |
| HXQ.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.1 | 4.10 | PASS |  |  |
| HXQ.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.98% | -7.98% | PASS |  |  |
| HXQ.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| JNJ | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +8.4% | TR +8.4% | PASS | LOW | the two cards divide by different roundings of the average |
| JNJ | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| JNJ | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| JNJ | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| JNJ | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,163,632,257 | 2,163,632,231 | PASS |  |  |
| JNJ | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| JNJ | MR-price | price = the last completed close | 270.47 | 270.47 | PASS |  |  |
| JNJ | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $270.47 needs above $10 | $270.47 needs above $10 | PASS |  |  |
| JNJ | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 41.1 needs under 10 | 41.08 needs under 10 -> ✗ | PASS |  |  |
| JNJ | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 8.4% above its 200-day average | 8.4% above | PASS |  |  |
| JNJ | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.2B traded on an average day needs above $25M | $2,163,632,257 needs above $25,000,000 | PASS |  |  |
| JNJ | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 41.08 | 41.08 | PASS |  |  |
| JNJ | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 8.43% | 8.43% | PASS |  |  |
| JNJ | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| JPM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -3.8% | TR -3.8% | PASS | LOW | the two cards divide by different roundings of the average |
| JPM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| JPM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| JPM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| JPM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,352,889,034 | 2,352,889,057 | PASS |  |  |
| JPM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| JPM | MR-price | price = the last completed close | 310.53 | 310.53 | PASS |  |  |
| JPM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $310.53 needs above $10 | $310.53 needs above $10 | PASS |  |  |
| JPM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.9 needs under 10 | 0.91 needs under 10 -> ✓ | PASS |  |  |
| JPM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 3.8% below its 200-day average | 3.8% below | PASS |  |  |
| JPM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.4B traded on an average day needs above $25M | $2,352,889,034 needs above $25,000,000 | PASS |  |  |
| JPM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.91 | 0.91 | PASS |  |  |
| JPM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -3.83% | -3.83% | PASS |  |  |
| JPM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| KEYS | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -18.8% | TR -18.8% | PASS | LOW | the two cards divide by different roundings of the average |
| KEYS | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| KEYS | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| KEYS | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| KEYS | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 490,440,363 | 490,552,530 | PASS |  |  |
| KEYS | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| KEYS | MR-price | price = the last completed close | 261.51 | 261.51 | PASS |  |  |
| KEYS | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $261.51 needs above $10 | $261.51 needs above $10 | PASS |  |  |
| KEYS | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.6 needs under 10 | 2.6 needs under 10 -> ✓ | PASS |  |  |
| KEYS | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.8% below its 200-day average | 18.8% below | PASS |  |  |
| KEYS | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $490.4M traded on an average day needs above $25M | $490,440,363 needs above $25,000,000 | PASS |  |  |
| KEYS | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.6 | 2.60 | PASS |  |  |
| KEYS | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -18.76% | -18.76% | PASS |  |  |
| KEYS | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| LIN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.4% | TR +1.4% | PASS | LOW | the two cards divide by different roundings of the average |
| LIN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| LIN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,140,261,315 | 1,140,261,331 | PASS |  |  |
| LIN | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| LIN | MR-price | price = the last completed close | 502.83 | 502.83 | PASS |  |  |
| LIN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $502.83 needs above $10 | $502.83 needs above $10 | PASS |  |  |
| LIN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.6 needs under 10 | 1.6 needs under 10 -> ✓ | PASS |  |  |
| LIN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.4% above its 200-day average | 1.4% above | PASS |  |  |
| LIN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,140,261,315 needs above $25,000,000 | PASS |  |  |
| LIN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.6 | 1.60 | PASS |  |  |
| LIN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.39% | 1.39% | PASS |  |  |
| LIN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| LLY | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +20.8% | TR +20.8% | PASS | LOW | the two cards divide by different roundings of the average |
| LLY | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| LLY | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 4,392,842,792 | 4,392,842,546 | PASS |  |  |
| LLY | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| LLY | MR-price | price = the last completed close | 1347.11 | 1347.11 | PASS |  |  |
| LLY | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,347.11 needs above $10 | $1,347.11 needs above $10 | PASS |  |  |
| LLY | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.5 needs under 10 | 2.51 needs under 10 -> ✓ | PASS |  |  |
| LLY | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 20.8% above its 200-day average | 20.8% above | PASS |  |  |
| LLY | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $4.4B traded on an average day needs above $25M | $4,392,842,792 needs above $25,000,000 | PASS |  |  |
| LLY | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.51 | 2.51 | PASS |  |  |
| LLY | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 20.82% | 20.82% | PASS |  |  |
| LLY | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MDA.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -17.5% | TR -17.5% | PASS | LOW | the two cards divide by different roundings of the average |
| MDA.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| MDA.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| MDA.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MDA.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 56,056,611 | 56,056,612 | PASS |  |  |
| MDA.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MDA.TO | MR-price | price = the last completed close | 36.88 | 36.88 | PASS |  |  |
| MDA.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $36.88 needs above $10 | $36.88 needs above $10 | PASS |  |  |
| MDA.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.3 needs under 10 | 7.35 needs under 10 -> ✓ | PASS |  |  |
| MDA.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 17.5% below its 200-day average | 17.5% below | PASS |  |  |
| MDA.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $56.1M traded on an average day needs above $25M | $56,056,611 needs above $25,000,000 | PASS |  |  |
| MDA.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.35 | 7.35 | PASS |  |  |
| MDA.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.49% | -17.49% | PASS |  |  |
| MDA.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| META | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -10.7% | TR -10.7% | PASS | LOW | the two cards divide by different roundings of the average |
| META | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| META | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| META | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| META | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 13,377,320,218 | 13,377,320,160 | PASS |  |  |
| META | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| META | MR-price | price = the last completed close | 560.84 | 560.84 | PASS |  |  |
| META | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $560.84 needs above $10 | $560.84 needs above $10 | PASS |  |  |
| META | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.3 needs under 10 | 1.3 needs under 10 -> ✓ | PASS |  |  |
| META | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 10.7% below its 200-day average | 10.7% below | PASS |  |  |
| META | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $13.4B traded on an average day needs above $25M | $13,377,320,218 needs above $25,000,000 | PASS |  |  |
| META | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.3 | 1.30 | PASS |  |  |
| META | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -10.68% | -10.68% | PASS |  |  |
| META | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| METU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -29.7% | TR -29.7% | PASS | LOW | the two cards divide by different roundings of the average |
| METU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| METU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| METU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| METU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 81,887,506 | 81,887,506 | PASS |  |  |
| METU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| METU | MR-price | price = the last completed close | 17.61 | 17.61 | PASS |  |  |
| METU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $17.61 needs above $10 | $17.61 needs above $10 | PASS |  |  |
| METU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.3 needs under 10 | 1.34 needs under 10 -> ✓ | PASS |  |  |
| METU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 29.7% below its 200-day average | 29.7% below | PASS |  |  |
| METU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $81.9M traded on an average day needs above $25M | $81,887,506 needs above $25,000,000 | PASS |  |  |
| METU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.34 | 1.34 | PASS |  |  |
| METU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -29.68% | -29.68% | PASS |  |  |
| METU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MRVL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -35.1% | TR -35.1% | PASS | LOW | the two cards divide by different roundings of the average |
| MRVL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| MRVL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| MRVL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MRVL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,436,763,618 | 5,436,763,608 | PASS |  |  |
| MRVL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MRVL | MR-price | price = the last completed close | 122.28 | 122.28 | PASS |  |  |
| MRVL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $122.28 needs above $10 | $122.28 needs above $10 | PASS |  |  |
| MRVL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.6 needs under 10 | 2.57 needs under 10 -> ✓ | PASS |  |  |
| MRVL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 35.1% below its 200-day average | 35.1% below | PASS |  |  |
| MRVL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.4B traded on an average day needs above $25M | $5,436,763,618 needs above $25,000,000 | PASS |  |  |
| MRVL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.57 | 2.57 | PASS |  |  |
| MRVL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -35.14% | -35.14% | PASS |  |  |
| MRVL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MSFT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +9.6% | TR +9.6% | PASS | LOW | the two cards divide by different roundings of the average |
| MSFT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| MSFT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 15,663,842,723 | 15,663,859,615 | PASS |  |  |
| MSFT | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| MSFT | MR-price | price = the last completed close | 484.52 | 484.52 | PASS |  |  |
| MSFT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $484.52 needs above $10 | $484.52 needs above $10 | PASS |  |  |
| MSFT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.9 needs under 10 | 2.91 needs under 10 -> ✓ | PASS |  |  |
| MSFT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 9.6% above its 200-day average | 9.6% above | PASS |  |  |
| MSFT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $15.7B traded on an average day needs above $25M | $15,663,842,723 needs above $25,000,000 | PASS |  |  |
| MSFT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.91 | 2.91 | PASS |  |  |
| MSFT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 9.64% | 9.64% | PASS |  |  |
| MSFT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MSFU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +9.8% | TR +9.8% | PASS | LOW | the two cards divide by different roundings of the average |
| MSFU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| MSFU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 106,597,845 | 106,597,846 | PASS |  |  |
| MSFU | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| MSFU | MR-price | price = the last completed close | 34.23 | 34.23 | PASS |  |  |
| MSFU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $34.23 needs above $10 | $34.23 needs above $10 | PASS |  |  |
| MSFU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.7 needs under 10 | 2.67 needs under 10 -> ✓ | PASS |  |  |
| MSFU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 9.8% above its 200-day average | 9.8% above | PASS |  |  |
| MSFU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $106.6M traded on an average day needs above $25M | $106,597,845 needs above $25,000,000 | PASS |  |  |
| MSFU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.67 | 2.67 | PASS |  |  |
| MSFU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 9.82% | 9.82% | PASS |  |  |
| MSFU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MTRX.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| MTRX.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| MTRX.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MTRX.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MTRX.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MTRX.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MTRX.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 528,026 | 528,027 | PASS |  |  |
| MTRX.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MTRX.TO | MR-price | price = the last completed close | 28.17 | 28.17 | PASS |  |  |
| MTRX.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $28.17 needs above $10 | $28.17 needs above $10 | PASS |  |  |
| MTRX.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.2 needs under 10 | 2.23 needs under 10 -> ✓ | PASS |  |  |
| MTRX.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 17.9% below its 200-day average | 17.9% below | PASS |  |  |
| MTRX.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $528,026 traded on an average day needs above $25M | $528,026 needs above $25,000,000 | PASS |  |  |
| MTRX.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.23 | 2.23 | PASS |  |  |
| MTRX.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.9% | -17.90% | PASS |  |  |
| MTRX.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.5% | TR -23.5% | PASS | LOW | the two cards divide by different roundings of the average |
| MU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| MU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| MU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 87,041,229 | 87,041,230 | PASS |  |  |
| MU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MU.TO | MR-price | price = the last completed close | 25.97 | 25.97 | PASS |  |  |
| MU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $25.97 needs above $10 | $25.97 needs above $10 | PASS |  |  |
| MU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.7 needs under 10 | 0.71 needs under 10 -> ✓ | PASS |  |  |
| MU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.5% below its 200-day average | 23.5% below | PASS |  |  |
| MU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $87M traded on an average day needs above $25M | $87,041,229 needs above $25,000,000 | PASS |  |  |
| MU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.71 | 0.71 | PASS |  |  |
| MU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.53% | -23.53% | PASS |  |  |
| MU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NEE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -3.5% | TR -3.5% | PASS | LOW | the two cards divide by different roundings of the average |
| NEE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| NEE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NEE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,090,815,330 | 1,090,815,345 | PASS |  |  |
| NEE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NEE | MR-price | price = the last completed close | 83.45 | 83.45 | PASS |  |  |
| NEE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $83.45 needs above $10 | $83.45 needs above $10 | PASS |  |  |
| NEE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.7 needs under 10 | 9.74 needs under 10 -> ✓ | PASS |  |  |
| NEE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 3.5% below its 200-day average | 3.5% below | PASS |  |  |
| NEE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,090,815,330 needs above $25,000,000 | PASS |  |  |
| NEE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.74 | 9.74 | PASS |  |  |
| NEE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -3.51% | -3.51% | PASS |  |  |
| NEE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NEM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -15.2% | TR -15.2% | PASS | LOW | the two cards divide by different roundings of the average |
| NEM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| NEM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NEM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NEM | MR-price | price = the last completed close | 94.69 | 94.68 | PASS |  |  |
| NEM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $94.69 needs above $10 | $94.69 needs above $10 | PASS |  |  |
| NEM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.5 needs under 10 | 1.51 needs under 10 -> ✓ | PASS |  |  |
| NEM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 15.2% below its 200-day average | 15.2% below | PASS |  |  |
| NEM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $889.5M traded on an average day needs above $25M | $889,545,737 needs above $25,000,000 | PASS |  |  |
| NEM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.51 | 1.51 | PASS |  |  |
| NEM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -15.18% | -15.18% | PASS |  |  |
| NEM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NFLX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -29.0% | TR -29.0% | PASS | LOW | the two cards divide by different roundings of the average |
| NFLX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| NFLX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NFLX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFLX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,552,464,363 | 2,552,652,939 | PASS |  |  |
| NFLX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NFLX | MR-price | price = the last completed close | 56.73 | 56.73 | PASS |  |  |
| NFLX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $56.73 needs above $10 | $56.73 needs above $10 | PASS |  |  |
| NFLX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.7 needs under 10 | 1.72 needs under 10 -> ✓ | PASS |  |  |
| NFLX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 29.0% below its 200-day average | 29.0% below | PASS |  |  |
| NFLX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.6B traded on an average day needs above $25M | $2,552,464,363 needs above $25,000,000 | PASS |  |  |
| NFLX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.72 | 1.72 | PASS |  |  |
| NFLX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -29.03% | -29.03% | PASS |  |  |
| NFLX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NFXL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -55.5% | TR -55.5% | PASS | LOW | the two cards divide by different roundings of the average |
| NFXL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| NFXL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| NFXL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFXL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 16,727,300 | 16,727,300 | PASS |  |  |
| NFXL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NFXL | MR-price | price = the last completed close | 8.9 | 8.9 | PASS |  |  |
| NFXL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $8.90 needs above $10 | $8.90 needs above $10 | PASS |  |  |
| NFXL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.1 needs under 10 | 1.06 needs under 10 -> ✓ | PASS |  |  |
| NFXL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 55.5% below its 200-day average | 55.5% below | PASS |  |  |
| NFXL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $16.7M traded on an average day needs above $25M | $16,727,300 needs above $25,000,000 | PASS |  |  |
| NFXL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.06 | 1.06 | PASS |  |  |
| NFXL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -55.51% | -55.51% | PASS |  |  |
| NFXL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NTR.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -6.2% | TR -6.2% | PASS | LOW | the two cards divide by different roundings of the average |
| NTR.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| NTR.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NTR.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NTR.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 129,319,325 | 129,319,327 | PASS |  |  |
| NTR.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NTR.TO | MR-price | price = the last completed close | 91.71 | 91.71 | PASS |  |  |
| NTR.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $91.71 needs above $10 | $91.71 needs above $10 | PASS |  |  |
| NTR.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.5 needs under 10 | 1.49 needs under 10 -> ✓ | PASS |  |  |
| NTR.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 6.2% below its 200-day average | 6.2% below | PASS |  |  |
| NTR.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $129.3M traded on an average day needs above $25M | $129,319,325 needs above $25,000,000 | PASS |  |  |
| NTR.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.49 | 1.49 | PASS |  |  |
| NTR.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -6.19% | -6.19% | PASS |  |  |
| NTR.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -38.2% | TR -38.3% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| NVDA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 48,161,015,455 | 48,169,707,070 | PASS |  |  |
| NVDA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDA | MR-price | price = the last completed close | 125.53 | 125.53 | PASS |  |  |
| NVDA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $125.53 needs above $10 | $125.53 needs above $10 | PASS |  |  |
| NVDA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.2 needs under 10 | 0.17 needs under 10 -> ✓ | PASS |  |  |
| NVDA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 38.2% below its 200-day average | 38.2% below | PASS |  |  |
| NVDA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $48.2B traded on an average day needs above $25M | $48,161,015,455 needs above $25,000,000 | PASS |  |  |
| NVDA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.17 | 0.17 | PASS |  |  |
| NVDA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -38.19% | -38.27% | PASS |  |  |
| NVDA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -66.8% | TR -66.8% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| NVDL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 708,996,823 | 708,996,831 | PASS |  |  |
| NVDL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDL | MR-price | price = the last completed close | 10.33 | 10.33 | PASS |  |  |
| NVDL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $10.33 needs above $10 | $10.33 needs above $10 | PASS |  |  |
| NVDL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.2 needs under 10 | 0.21 needs under 10 -> ✓ | PASS |  |  |
| NVDL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 66.8% below its 200-day average | 66.8% below | PASS |  |  |
| NVDL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $709M traded on an average day needs above $25M | $708,996,823 needs above $25,000,000 | PASS |  |  |
| NVDL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.21 | 0.21 | PASS |  |  |
| NVDL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -66.8% | -66.80% | PASS |  |  |
| NVDL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ONTO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -34.5% | TR -34.5% | PASS | LOW | the two cards divide by different roundings of the average |
| ONTO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ONTO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ONTO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ONTO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 234,976,100 | 234,976,100 | PASS |  |  |
| ONTO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ONTO | MR-price | price = the last completed close | 170.16 | 170.16 | PASS |  |  |
| ONTO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $170.16 needs above $10 | $170.16 needs above $10 | PASS |  |  |
| ONTO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.1 needs under 10 | 3.08 needs under 10 -> ✓ | PASS |  |  |
| ONTO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 34.5% below its 200-day average | 34.5% below | PASS |  |  |
| ONTO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $235M traded on an average day needs above $25M | $234,976,100 needs above $25,000,000 | PASS |  |  |
| ONTO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.08 | 3.08 | PASS |  |  |
| ONTO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -34.53% | -34.53% | PASS |  |  |
| ONTO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ORBX.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| ORCL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -33.5% | TR -33.5% | PASS | LOW | the two cards divide by different roundings of the average |
| ORCL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| ORCL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ORCL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ORCL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ORCL | MR-price | price = the last completed close | 101.18 | 101.19 | PASS |  |  |
| ORCL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $101.18 needs above $10 | $101.18 needs above $10 | PASS |  |  |
| ORCL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.7 needs under 10 | 0.73 needs under 10 -> ✓ | PASS |  |  |
| ORCL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 33.5% below its 200-day average | 33.5% below | PASS |  |  |
| ORCL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.5B traded on an average day needs above $25M | $5,520,590,290 needs above $25,000,000 | PASS |  |  |
| ORCL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.73 | 0.73 | PASS |  |  |
| ORCL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -33.52% | -33.51% | PASS |  |  |
| ORCL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +14.1% | TR +14.1% | PASS | LOW | the two cards divide by different roundings of the average |
| PG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| PG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| PG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,707,246,461 | 1,707,246,429 | PASS |  |  |
| PG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PG | MR-price | price = the last completed close | 169.46 | 169.46 | PASS |  |  |
| PG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $169.46 needs above $10 | $169.46 needs above $10 | PASS |  |  |
| PG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 51.8 needs under 10 | 51.8 needs under 10 -> ✗ | PASS |  |  |
| PG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 14.1% above its 200-day average | 14.1% above | PASS |  |  |
| PG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.7B traded on an average day needs above $25M | $1,707,246,461 needs above $25,000,000 | PASS |  |  |
| PG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 51.8 | 51.80 | PASS |  |  |
| PG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 14.14% | 14.14% | PASS |  |  |
| PG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PLD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -10.1% | TR -10.1% | PASS | LOW | the two cards divide by different roundings of the average |
| PLD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| PLD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| PLD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PLD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 471,934,741 | 471,934,738 | PASS |  |  |
| PLD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PLD | MR-price | price = the last completed close | 122.5 | 122.5 | PASS |  |  |
| PLD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $122.50 needs above $10 | $122.50 needs above $10 | PASS |  |  |
| PLD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.5 needs under 10 | 0.51 needs under 10 -> ✓ | PASS |  |  |
| PLD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 10.1% below its 200-day average | 10.1% below | PASS |  |  |
| PLD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $471.9M traded on an average day needs above $25M | $471,934,741 needs above $25,000,000 | PASS |  |  |
| PLD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.51 | 0.51 | PASS |  |  |
| PLD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -10.08% | -10.08% | PASS |  |  |
| PLD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PNG.V | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -57.2% | TR -57.3% | PASS | LOW | the two cards divide by different roundings of the average |
| PNG.V | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| PNG.V | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| PNG.V | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PNG.V | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 4,130,257 | 4,130,257 | PASS |  |  |
| PNG.V | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PNG.V | MR-price | price = the last completed close | 2.79 | 2.79 | PASS |  |  |
| PNG.V | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $2.79 needs above $10 | $2.79 needs above $10 | PASS |  |  |
| PNG.V | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.4 needs under 10 | 0.36 needs under 10 -> ✓ | PASS |  |  |
| PNG.V | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 57.3% below its 200-day average | 57.2% below | PASS |  |  |
| PNG.V | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $4.1M traded on an average day needs above $25M | $4,130,257 needs above $25,000,000 | PASS |  |  |
| PNG.V | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.36 | 0.36 | PASS |  |  |
| PNG.V | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -57.25% | -57.25% | PASS |  |  |
| PNG.V | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QCOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.6% | TR -11.6% | PASS | LOW | the two cards divide by different roundings of the average |
| QCOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| QCOM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| QCOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QCOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,475,498,116 | 2,475,498,112 | PASS |  |  |
| QCOM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QCOM | MR-price | price = the last completed close | 149.94 | 149.94 | PASS |  |  |
| QCOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $149.94 needs above $10 | $149.94 needs above $10 | PASS |  |  |
| QCOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.5 needs under 10 | 7.47 needs under 10 -> ✓ | PASS |  |  |
| QCOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.6% below its 200-day average | 11.6% below | PASS |  |  |
| QCOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.5B traded on an average day needs above $25M | $2,475,498,116 needs above $25,000,000 | PASS |  |  |
| QCOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.47 | 7.47 | PASS |  |  |
| QCOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.58% | -11.58% | PASS |  |  |
| QCOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QPUX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -87.6% | TR -87.6% | PASS | LOW | the two cards divide by different roundings of the average |
| QPUX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| QPUX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| QPUX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QPUX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,583,149 | 1,583,124 | PASS |  |  |
| QPUX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QPUX | MR-price | price = the last completed close | 2.47 | 2.47 | PASS |  |  |
| QPUX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $2.47 needs above $10 | $2.47 needs above $10 | PASS |  |  |
| QPUX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.4 needs under 10 | 0.44 needs under 10 -> ✓ | PASS |  |  |
| QPUX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 87.6% below its 200-day average | 87.6% below | PASS |  |  |
| QPUX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.6M traded on an average day needs above $25M | $1,583,149 needs above $25,000,000 | PASS |  |  |
| QPUX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.44 | 0.44 | PASS |  |  |
| QPUX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -87.64% | -87.64% | PASS |  |  |
| QPUX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QTUM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -19.3% | TR -19.3% | PASS | LOW | the two cards divide by different roundings of the average |
| QTUM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| QTUM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| QTUM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QTUM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 51,393,165 | 51,393,166 | PASS |  |  |
| QTUM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QTUM | MR-price | price = the last completed close | 111.43 | 111.43 | PASS |  |  |
| QTUM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $111.43 needs above $10 | $111.43 needs above $10 | PASS |  |  |
| QTUM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.7 needs under 10 | 1.69 needs under 10 -> ✓ | PASS |  |  |
| QTUM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 19.3% below its 200-day average | 19.3% below | PASS |  |  |
| QTUM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $51.4M traded on an average day needs above $25M | $51,393,165 needs above $25,000,000 | PASS |  |  |
| QTUM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.69 | 1.69 | PASS |  |  |
| QTUM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -19.28% | -19.28% | PASS |  |  |
| QTUM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RBOT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -24.6% | TR -24.6% | PASS | LOW | the two cards divide by different roundings of the average |
| RBOT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| RBOT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| RBOT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RBOT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RBOT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RBOT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RBOT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 132,432 | 132,432 | PASS |  |  |
| RBOT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RBOT.TO | MR-price | price = the last completed close | 25 | 25 | PASS |  |  |
| RBOT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $25.00 needs above $10 | $25.00 needs above $10 | PASS |  |  |
| RBOT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.27 needs under 10 -> ✓ | PASS |  |  |
| RBOT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 24.6% below its 200-day average | 24.6% below | PASS |  |  |
| RBOT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $132,432 traded on an average day needs above $25M | $132,432 needs above $25,000,000 | PASS |  |  |
| RBOT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.27 | 0.27 | PASS |  |  |
| RBOT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -24.64% | -24.64% | PASS |  |  |
| RBOT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RTX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -2.2% | TR -2.2% | PASS | LOW | the two cards divide by different roundings of the average |
| RTX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| RTX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| RTX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RTX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,041,784,499 | 1,041,784,506 | PASS |  |  |
| RTX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RTX | MR-price | price = the last completed close | 190.17 | 190.17 | PASS |  |  |
| RTX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $190.17 needs above $10 | $190.17 needs above $10 | PASS |  |  |
| RTX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.1 needs under 10 | 7.06 needs under 10 -> ✓ | PASS |  |  |
| RTX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 2.2% below its 200-day average | 2.2% below | PASS |  |  |
| RTX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1B traded on an average day needs above $25M | $1,041,784,499 needs above $25,000,000 | PASS |  |  |
| RTX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.06 | 7.06 | PASS |  |  |
| RTX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -2.2% | -2.20% | PASS |  |  |
| RTX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RY.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.3% | TR -0.3% | PASS | LOW | the two cards divide by different roundings of the average |
| RY.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| RY.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| RY.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RY.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 999,908,707 | 999,908,709 | PASS |  |  |
| RY.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RY.TO | MR-price | price = the last completed close | 263.05 | 263.05 | PASS |  |  |
| RY.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $263.05 needs above $10 | $263.05 needs above $10 | PASS |  |  |
| RY.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.27 needs under 10 -> ✓ | PASS |  |  |
| RY.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.3% below its 200-day average | 0.3% below | PASS |  |  |
| RY.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $999.9M traded on an average day needs above $25M | $999,908,707 needs above $25,000,000 | PASS |  |  |
| RY.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.27 | 0.27 | PASS |  |  |
| RY.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.33% | -0.33% | PASS |  |  |
| RY.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SETM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -39.3% | TR -39.3% | PASS | LOW | the two cards divide by different roundings of the average |
| SETM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| SETM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| SETM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SETM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SETM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SETM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SETM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 4,315,882 | 4,315,874 | PASS |  |  |
| SETM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SETM | MR-price | price = the last completed close | 19.53 | 19.53 | PASS |  |  |
| SETM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $19.53 needs above $10 | $19.53 needs above $10 | PASS |  |  |
| SETM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.31 needs under 10 -> ✓ | PASS |  |  |
| SETM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 39.3% below its 200-day average | 39.3% below | PASS |  |  |
| SETM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $4.3M traded on an average day needs above $25M | $4,315,882 needs above $25,000,000 | PASS |  |  |
| SETM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.31 | 0.31 | PASS |  |  |
| SETM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -39.33% | -39.33% | PASS |  |  |
| SETM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SGRD.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| SMH | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.9% | TR -23.9% | PASS | LOW | the two cards divide by different roundings of the average |
| SMH | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| SMH | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| SMH | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SMH | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,929,574,677 | 6,929,574,659 | PASS |  |  |
| SMH | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SMH | MR-price | price = the last completed close | 399.51 | 399.51 | PASS |  |  |
| SMH | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $399.51 needs above $10 | $399.51 needs above $10 | PASS |  |  |
| SMH | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.4 needs under 10 | 0.43 needs under 10 -> ✓ | PASS |  |  |
| SMH | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.9% below its 200-day average | 23.9% below | PASS |  |  |
| SMH | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6.9B traded on an average day needs above $25M | $6,929,574,677 needs above $25,000,000 | PASS |  |  |
| SMH | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.43 | 0.43 | PASS |  |  |
| SMH | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.93% | -23.93% | PASS |  |  |
| SMH | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SNDK.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| SO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +2.0% | TR +2.0% | PASS | LOW | the two cards divide by different roundings of the average |
| SO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| SO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| SO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 800,319,222 | 800,315,949 | PASS |  |  |
| SO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SO | MR-price | price = the last completed close | 93.13 | 93.13 | PASS |  |  |
| SO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $93.13 needs above $10 | $93.13 needs above $10 | PASS |  |  |
| SO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 28.9 needs under 10 | 28.9 needs under 10 -> ✗ | PASS |  |  |
| SO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 2.0% above its 200-day average | 2.0% above | PASS |  |  |
| SO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $800.3M traded on an average day needs above $25M | $800,319,222 needs above $25,000,000 | PASS |  |  |
| SO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 28.9 | 28.90 | PASS |  |  |
| SO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.05% | 2.05% | PASS |  |  |
| SO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -75.0% | TR -75.0% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| SOXL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| SOXL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,917,876,260 | 12,917,876,310 | PASS |  |  |
| SOXL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL | MR-price | price = the last completed close | 30.88 | 30.88 | PASS |  |  |
| SOXL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $30.88 needs above $10 | $30.88 needs above $10 | PASS |  |  |
| SOXL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.1 needs under 10 | 1.09 needs under 10 -> ✓ | PASS |  |  |
| SOXL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 75.0% below its 200-day average | 75.0% below | PASS |  |  |
| SOXL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.9B traded on an average day needs above $25M | $12,917,876,260 needs above $25,000,000 | PASS |  |  |
| SOXL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.09 | 1.09 | PASS |  |  |
| SOXL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -75.03% | -75.03% | PASS |  |  |
| SOXL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL.NE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -74.5% | TR -74.5% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL.NE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| SOXL.NE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| SOXL.NE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL.NE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,580,820 | 2,580,820 | PASS |  |  |
| SOXL.NE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL.NE | MR-price | price = the last completed close | 7.85 | 7.85 | PASS |  |  |
| SOXL.NE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $7.85 needs above $10 | $7.85 needs above $10 | PASS |  |  |
| SOXL.NE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.3 needs under 10 | 1.33 needs under 10 -> ✓ | PASS |  |  |
| SOXL.NE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 74.5% below its 200-day average | 74.5% below | PASS |  |  |
| SOXL.NE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.6M traded on an average day needs above $25M | $2,580,820 needs above $25,000,000 | PASS |  |  |
| SOXL.NE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.33 | 1.32 | PASS |  |  |
| SOXL.NE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -74.51% | -74.51% | PASS |  |  |
| SOXL.NE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.3% | TR -23.3% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| SOXX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| SOXX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,403,847,038 | 6,403,855,514 | PASS |  |  |
| SOXX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXX | MR-price | price = the last completed close | 123.4 | 123.4 | PASS |  |  |
| SOXX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $123.40 needs above $10 | $123.40 needs above $10 | PASS |  |  |
| SOXX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.3 needs under 10 | 1.27 needs under 10 -> ✓ | PASS |  |  |
| SOXX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.3% below its 200-day average | 23.3% below | PASS |  |  |
| SOXX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6.4B traded on an average day needs above $25M | $6,403,847,038 needs above $25,000,000 | PASS |  |  |
| SOXX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.27 | 1.27 | PASS |  |  |
| SOXX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.29% | -23.29% | PASS |  |  |
| SOXX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SPCL | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| TSLA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -9.4% | TR -9.4% | PASS | LOW | the two cards divide by different roundings of the average |
| TSLA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| TSLA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| TSLA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,032,701,565 | 14,033,775,471 | PASS |  |  |
| TSLA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSLA | MR-price | price = the last completed close | 345.82 | 345.82 | PASS |  |  |
| TSLA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $345.82 needs above $10 | $345.82 needs above $10 | PASS |  |  |
| TSLA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.4 needs under 10 | 3.39 needs under 10 -> ✓ | PASS |  |  |
| TSLA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.4% below its 200-day average | 9.4% below | PASS |  |  |
| TSLA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $14B traded on an average day needs above $25M | $14,032,701,565 needs above $25,000,000 | PASS |  |  |
| TSLA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.39 | 3.39 | PASS |  |  |
| TSLA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.39% | -9.39% | PASS |  |  |
| TSLA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| TSLL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -30.7% | TR -30.7% | PASS | LOW | the two cards divide by different roundings of the average |
| TSLL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| TSLL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10 | it is below its 200-day average; the price is under $10 | PASS |  |  |
| TSLL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 439,171,523 | 439,171,519 | PASS |  |  |
| TSLL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSLL | MR-price | price = the last completed close | 8.07 | 8.07 | PASS |  |  |
| TSLL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $8.07 needs above $10 | $8.07 needs above $10 | PASS |  |  |
| TSLL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.4 needs under 10 | 3.41 needs under 10 -> ✓ | PASS |  |  |
| TSLL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 30.7% below its 200-day average | 30.7% below | PASS |  |  |
| TSLL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $439.2M traded on an average day needs above $25M | $439,171,523 needs above $25,000,000 | PASS |  |  |
| TSLL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.41 | 3.41 | PASS |  |  |
| TSLL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -30.68% | -30.68% | PASS |  |  |
| TSLL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| TSM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| TSM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| TSM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,440,282,145 | 6,440,596,150 | PASS |  |  |
| TSM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSM | MR-price | price = the last completed close | 318.71 | 318.71 | PASS |  |  |
| TSM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $318.71 needs above $10 | $318.71 needs above $10 | PASS |  |  |
| TSM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.2 needs under 10 | 2.18 needs under 10 -> ✓ | PASS |  |  |
| TSM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.8% below its 200-day average | 20.8% below | PASS |  |  |
| TSM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6.4B traded on an average day needs above $25M | $6,440,282,145 needs above $25,000,000 | PASS |  |  |
| TSM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.18 | 2.18 | PASS |  |  |
| TSM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| UBOT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -46.4% | TR -46.4% | PASS | LOW | the two cards divide by different roundings of the average |
| UBOT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| UBOT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| UBOT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UBOT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UBOT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UBOT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UBOT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 338,263 | 338,264 | PASS |  |  |
| UBOT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| UBOT | MR-price | price = the last completed close | 12.74 | 12.74 | PASS |  |  |
| UBOT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $12.74 needs above $10 | $12.74 needs above $10 | PASS |  |  |
| UBOT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.7 needs under 10 | 0.71 needs under 10 -> ✓ | PASS |  |  |
| UBOT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 46.4% below its 200-day average | 46.4% below | PASS |  |  |
| UBOT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $338,263 traded on an average day needs above $25M | $338,263 needs above $25,000,000 | PASS |  |  |
| UBOT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.71 | 0.71 | PASS |  |  |
| UBOT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -46.44% | -46.44% | PASS |  |  |
| UBOT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| UFO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.5% | TR -23.5% | PASS | LOW | the two cards divide by different roundings of the average |
| UFO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| UFO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| UFO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UFO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UFO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UFO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UFO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 9,681,752 | 9,681,752 | PASS |  |  |
| UFO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| UFO | MR-price | price = the last completed close | 35.87 | 35.87 | PASS |  |  |
| UFO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $35.87 needs above $10 | $35.87 needs above $10 | PASS |  |  |
| UFO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.4 needs under 10 | 0.38 needs under 10 -> ✓ | PASS |  |  |
| UFO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.5% below its 200-day average | 23.5% below | PASS |  |  |
| UFO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $9.7M traded on an average day needs above $25M | $9,681,752 needs above $25,000,000 | PASS |  |  |
| UFO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.38 | 0.38 | PASS |  |  |
| UFO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.53% | -23.53% | PASS |  |  |
| UFO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| URA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -40.8% | TR -40.8% | PASS | LOW | the two cards divide by different roundings of the average |
| URA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| URA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| URA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 182,556,317 | 182,556,317 | PASS |  |  |
| URA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| URA | MR-price | price = the last completed close | 26.82 | 26.82 | PASS |  |  |
| URA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $26.82 needs above $10 | $26.82 needs above $10 | PASS |  |  |
| URA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.35 needs under 10 -> ✓ | PASS |  |  |
| URA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 40.8% below its 200-day average | 40.8% below | PASS |  |  |
| URA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $182.6M traded on an average day needs above $25M | $182,556,317 needs above $25,000,000 | PASS |  |  |
| URA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.35 | 0.35 | PASS |  |  |
| URA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -40.82% | -40.82% | PASS |  |  |
| URA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| URAA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -68.6% | TR -68.6% | PASS | LOW | the two cards divide by different roundings of the average |
| URAA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| URAA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| URAA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URAA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,157,507 | 1,157,508 | PASS |  |  |
| URAA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| URAA | MR-price | price = the last completed close | 9.08 | 9.08 | PASS |  |  |
| URAA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $9.08 needs above $10 | $9.08 needs above $10 | PASS |  |  |
| URAA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.4 needs under 10 | 0.38 needs under 10 -> ✓ | PASS |  |  |
| URAA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 68.6% below its 200-day average | 68.6% below | PASS |  |  |
| URAA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.2M traded on an average day needs above $25M | $1,157,507 needs above $25,000,000 | PASS |  |  |
| URAA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.38 | 0.38 | PASS |  |  |
| URAA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -68.61% | -68.61% | PASS |  |  |
| URAA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| V | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +15.5% | TR +15.5% | PASS | LOW | the two cards divide by different roundings of the average |
| V | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| V | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,046,671,495 | 3,046,669,680 | PASS |  |  |
| V | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| V | MR-price | price = the last completed close | 401.87 | 401.87 | PASS |  |  |
| V | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $401.87 needs above $10 | $401.87 needs above $10 | PASS |  |  |
| V | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.79 needs under 10 -> ✓ | PASS |  |  |
| V | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 15.5% above its 200-day average | 15.5% above | PASS |  |  |
| V | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3B traded on an average day needs above $25M | $3,046,671,495 needs above $25,000,000 | PASS |  |  |
| V | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.79 | 2.79 | PASS |  |  |
| V | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 15.5% | 15.50% | PASS |  |  |
| V | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| VFV.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -2.6% | TR -2.6% | PASS | LOW | the two cards divide by different roundings of the average |
| VFV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| VFV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| VFV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VFV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 79,010,327 | 79,010,328 | PASS |  |  |
| VFV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| VFV.TO | MR-price | price = the last completed close | 176.29 | 176.29 | PASS |  |  |
| VFV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $176.29 needs above $10 | $176.29 needs above $10 | PASS |  |  |
| VFV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.6 needs under 10 | 0.6 needs under 10 -> ✓ | PASS |  |  |
| VFV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 2.6% below its 200-day average | 2.6% below | PASS |  |  |
| VFV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $79M traded on an average day needs above $25M | $79,010,327 needs above $25,000,000 | PASS |  |  |
| VFV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.6 | 0.60 | PASS |  |  |
| VFV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -2.56% | -2.56% | PASS |  |  |
| VFV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| VRT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -38.8% | TR -38.8% | PASS | LOW | the two cards divide by different roundings of the average |
| VRT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| VRT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| VRT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VRT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,773,091,310 | 1,773,091,307 | PASS |  |  |
| VRT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| VRT | MR-price | price = the last completed close | 166.24 | 166.24 | PASS |  |  |
| VRT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $166.24 needs above $10 | $166.24 needs above $10 | PASS |  |  |
| VRT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.5 needs under 10 | 5.48 needs under 10 -> ✓ | PASS |  |  |
| VRT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 38.8% below its 200-day average | 38.8% below | PASS |  |  |
| VRT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.8B traded on an average day needs above $25M | $1,773,091,310 needs above $25,000,000 | PASS |  |  |
| VRT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.48 | 5.48 | PASS |  |  |
| VRT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -38.77% | -38.77% | PASS |  |  |
| VRT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| WDC.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| WELL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +8.6% | TR +8.6% | PASS | LOW | the two cards divide by different roundings of the average |
| WELL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| WELL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 801,838,631 | 801,839,292 | PASS |  |  |
| WELL | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| WELL | MR-price | price = the last completed close | 240.34 | 240.34 | PASS |  |  |
| WELL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $240.34 needs above $10 | $240.34 needs above $10 | PASS |  |  |
| WELL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.8 needs under 10 | 9.77 needs under 10 -> ✓ | PASS |  |  |
| WELL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 8.6% above its 200-day average | 8.6% above | PASS |  |  |
| WELL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $801.8M traded on an average day needs above $25M | $801,838,631 needs above $25,000,000 | PASS |  |  |
| WELL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.77 | 9.77 | PASS |  |  |
| WELL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 8.58% | 8.58% | PASS |  |  |
| WELL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| WMT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +7.8% | TR +7.8% | PASS | LOW | the two cards divide by different roundings of the average |
| WMT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| WMT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| WMT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| WMT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,982,138,163 | 2,982,138,162 | PASS |  |  |
| WMT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| WMT | MR-price | price = the last completed close | 127.95 | 127.95 | PASS |  |  |
| WMT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $127.95 needs above $10 | $127.95 needs above $10 | PASS |  |  |
| WMT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 71.0 needs under 10 | 71.05 needs under 10 -> ✗ | PASS |  |  |
| WMT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 7.8% above its 200-day average | 7.8% above | PASS |  |  |
| WMT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3B traded on an average day needs above $25M | $2,982,138,163 needs above $25,000,000 | PASS |  |  |
| WMT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 71.05 | 71.05 | PASS |  |  |
| WMT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 7.81% | 7.81% | PASS |  |  |
| WMT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XCHP.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -21.3% | TR -21.3% | PASS | LOW | the two cards divide by different roundings of the average |
| XCHP.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| XCHP.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XCHP.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XCHP.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XCHP.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 8,074,524 | 8,074,525 | PASS |  |  |
| XCHP.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XCHP.TO | MR-price | price = the last completed close | 91.94 | 91.94 | PASS |  |  |
| XCHP.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $91.94 needs above $10 | $91.94 needs above $10 | PASS |  |  |
| XCHP.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.5 needs under 10 | 1.47 needs under 10 -> ✓ | PASS |  |  |
| XCHP.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 21.3% below its 200-day average | 21.3% below | PASS |  |  |
| XCHP.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $8.1M traded on an average day needs above $25M | $8,074,524 needs above $25,000,000 | PASS |  |  |
| XCHP.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.47 | 1.47 | PASS |  |  |
| XCHP.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -21.33% | -21.33% | PASS |  |  |
| XCHP.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XDRV.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.6% | TR -23.7% | PASS | LOW | the two cards divide by different roundings of the average |
| XDRV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| XDRV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XDRV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XDRV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XDRV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 4,329 | 4,330 | PASS |  |  |
| XDRV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XDRV.TO | MR-price | price = the last completed close | 36.31 | 36.31 | PASS |  |  |
| XDRV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $36.31 needs above $10 | $36.31 needs above $10 | PASS |  |  |
| XDRV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.8 needs under 10 | 9.75 needs under 10 -> ✓ | PASS |  |  |
| XDRV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.6% below its 200-day average | 23.6% below | PASS |  |  |
| XDRV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $4,329 traded on an average day needs above $25M | $4,329 needs above $25,000,000 | PASS |  |  |
| XDRV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.75 | 9.75 | PASS |  |  |
| XDRV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.65% | -23.65% | PASS |  |  |
| XDRV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XEQT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -3.8% | TR -3.8% | PASS | LOW | the two cards divide by different roundings of the average |
| XEQT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| XEQT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| XEQT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XEQT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 57,713,983 | 57,713,479 | PASS |  |  |
| XEQT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XEQT.TO | MR-price | price = the last completed close | 41.97 | 41.97 | PASS |  |  |
| XEQT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $41.97 needs above $10 | $41.97 needs above $10 | PASS |  |  |
| XEQT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.4 needs under 10 | 0.38 needs under 10 -> ✓ | PASS |  |  |
| XEQT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 3.8% below its 200-day average | 3.8% below | PASS |  |  |
| XEQT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $57.7M traded on an average day needs above $25M | $57,713,983 needs above $25,000,000 | PASS |  |  |
| XEQT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.38 | 0.38 | PASS |  |  |
| XEQT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -3.75% | -3.75% | PASS |  |  |
| XEQT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XETM.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| XETM.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XETM.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XETM.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XETM.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XETM.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XETM.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 246,607 | 246,608 | PASS |  |  |
| XETM.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XETM.TO | MR-price | price = the last completed close | 53.16 | 53.16 | PASS |  |  |
| XETM.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $53.16 needs above $10 | $53.16 needs above $10 | PASS |  |  |
| XETM.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.3 needs under 10 | 0.31 needs under 10 -> ✓ | PASS |  |  |
| XETM.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 33.1% below its 200-day average | 33.1% below | PASS |  |  |
| XETM.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $246,607 traded on an average day needs above $25M | $246,607 needs above $25,000,000 | PASS |  |  |
| XETM.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.31 | 0.31 | PASS |  |  |
| XETM.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -33.08% | -33.08% | PASS |  |  |
| XETM.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XGD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -19.3% | TR -19.3% | PASS | LOW | the two cards divide by different roundings of the average |
| XGD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| XGD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| XGD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XGD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 32,943,163 | 32,943,164 | PASS |  |  |
| XGD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XGD.TO | MR-price | price = the last completed close | 44.38 | 44.38 | PASS |  |  |
| XGD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $44.38 needs above $10 | $44.38 needs above $10 | PASS |  |  |
| XGD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.6 needs under 10 | 1.63 needs under 10 -> ✓ | PASS |  |  |
| XGD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 19.3% below its 200-day average | 19.3% below | PASS |  |  |
| XGD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $32.9M traded on an average day needs above $25M | $32,943,163 needs above $25,000,000 | PASS |  |  |
| XGD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.63 | 1.63 | PASS |  |  |
| XGD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -19.27% | -19.27% | PASS |  |  |
| XGD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +3.3% | TR +3.3% | PASS | LOW | the two cards divide by different roundings of the average |
| XOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-20 | 2026-11-20 | PASS |  |  |
| XOM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| XOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,761,920,541 | 2,761,912,532 | PASS |  |  |
| XOM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XOM | MR-price | price = the last completed close | 159.97 | 159.97 | PASS |  |  |
| XOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $159.97 needs above $10 | $159.97 needs above $10 | PASS |  |  |
| XOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 30.6 needs under 10 | 30.64 needs under 10 -> ✗ | PASS |  |  |
| XOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 3.3% above its 200-day average | 3.3% above | PASS |  |  |
| XOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.8B traded on an average day needs above $25M | $2,761,920,541 needs above $25,000,000 | PASS |  |  |
| XOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 30.64 | 30.64 | PASS |  |  |
| XOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 3.28% | 3.28% | PASS |  |  |
| XOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AAPL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AAPL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AAPL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AAPL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AAPL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AAPL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AAPL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AAPU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AAPU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AAPU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AAPU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AAPU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AAPU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AAPU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AAPU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ABBV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ABBV | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ABBV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ABBV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ABBV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ABBV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ABBV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ABBV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ABBV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ABBV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AIPO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AIPO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AIPO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AIPO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AIPO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AIPO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AIPO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AIPO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AIPO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AIPO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ALAB | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ALAB | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ALAB | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ALAB | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ALAB | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ALAB | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ALAB | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ALAB | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ALAB | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ALAB | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AMD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AMD | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AMD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AMD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AMD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AMD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AMD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AMD.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AMD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AMD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AMD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AMD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AMZN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AMZN | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMZN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMZN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AMZN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AMZN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AMZN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMZN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AMZN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMZN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AMZU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AMZU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMZU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMZU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AMZU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AMZU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AMZU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMZU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AMZU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMZU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ANET.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ANET.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ANET.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ANET.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ANET.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ANET.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ANET.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ANET.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ANET.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ANET.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ASML.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ASML.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ASML.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ASML.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ASML.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ASML.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ASML.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ASML.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ASML.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ASML.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ASTL.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ASTL.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ASTL.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ASTL.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ASTL.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ASTL.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ASTL.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ASTL.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ASTL.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ASTL.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ATD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ATD.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ATD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ATD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ATD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ATD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ATD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ATD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ATD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ATD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AVGC | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AVGC | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGC | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGC | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AVGC | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AVGC | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AVGC | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGC | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AVGC | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGC | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AVGO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AVGO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AVGO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AVGO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AVGO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AVGO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| AVGO.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| AVGO.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGO.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGO.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| AVGO.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AVGO.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| AVGO.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGO.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| AVGO.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGO.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| BDT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| BDT.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BDT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BDT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| BDT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| BDT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| BDT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BDT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| BDT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BDT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| BOTZ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| BOTZ | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BOTZ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BOTZ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| BOTZ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| BOTZ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| BOTZ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BOTZ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| BOTZ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BOTZ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| BRK-B | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| BRK-B | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BRK-B | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BRK-B | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| BRK-B | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| BRK-B | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| BRK-B | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BRK-B | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| BRK-B | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BRK-B | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| BRKU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| BRKU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BRKU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BRKU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| BRKU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| BRKU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| BRKU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BRKU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| BRKU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BRKU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CAMT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CAMT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CAMT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CAMT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CAMT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CAMT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CAMT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CAMT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CAMT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CAMT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CARS.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CARS.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CARS.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CARS.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CARS.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CARS.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CARS.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CARS.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CARS.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CARS.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CAT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CAT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CAT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CAT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CAT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CAT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CAT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CAT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CAT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CAT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CCO.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CCO.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CCO.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CCO.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CCO.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CCO.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CCO.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CCO.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CCO.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CCO.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CEG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CEG | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CEG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CEG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CEG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CEG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CEG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CEG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CEG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CEG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CGY.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CGY.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CGY.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CGY.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CGY.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CGY.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CGY.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CGY.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CGY.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CGY.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CNQ.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CNQ.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CNQ.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CNQ.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CNQ.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CNQ.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CNQ.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CNQ.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CNQ.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CNQ.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CNR.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CNR.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CNR.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CNR.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CNR.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CNR.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CNR.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CNR.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CNR.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CNR.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| COP | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| COP | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COP | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COP | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| COP | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COP | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| COP | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COP | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| COP | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COP | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| COPP.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| COPP.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPP.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPP.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| COPP.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COPP.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| COPP.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPP.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| COPP.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPP.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| COPX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| COPX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| COPX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COPX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| COPX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| COPX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| COPZ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| COPZ | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPZ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPZ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| COPZ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COPZ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| COPZ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPZ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| COPZ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPZ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| COST | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| COST | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COST | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COST | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| COST | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COST | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| COST | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COST | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| COST | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COST | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| COTG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| COTG | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COTG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COTG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| COTG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COTG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| COTG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COTG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| COTG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COTG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CSU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CSU.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CSU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CSU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CSU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CSU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CSU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CSU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CSU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CSU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| CVX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| CVX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CVX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CVX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| CVX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CVX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| CVX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CVX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| CVX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CVX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| DRAL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| DRAL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRAL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRAL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| DRAL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| DRAL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| DRAL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRAL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| DRAL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRAL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| DRAM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| DRAM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRAM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRAM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| DRAM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| DRAM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| DRAM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRAM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| DRAM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRAM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| DRIV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| DRIV | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRIV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRIV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| DRIV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| DRIV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| DRIV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRIV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| DRIV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRIV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| DUK | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| DUK | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DUK | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DUK | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| DUK | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| DUK | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| DUK | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DUK | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| DUK | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DUK | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ELIL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ELIL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ELIL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ELIL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ELIL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ELIL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ELIL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ELIL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ELIL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ELIL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| EQIX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| EQIX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| EQIX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| EQIX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| EQIX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| EQIX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| EQIX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| EQIX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| EQIX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| EQIX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ETN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ETN | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ETN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ETN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ETN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ETN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ETN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ETN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ETN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ETN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| FCX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| FCX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| FCX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| FCX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| FCX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| FCX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| FCX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| FCX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| FCX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| FCX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| FINN.NE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| FINN.NE | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| FINN.NE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| FINN.NE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| FINN.NE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| FINN.NE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| FINN.NE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| FINN.NE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| FINN.NE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| FINN.NE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GDX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GDX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GDX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GDX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GDX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GDX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GDX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GDX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GDX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GDX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GDXU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GDXU.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GDXU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GDXU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GDXU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GDXU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GDXU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GDXU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GDXU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GDXU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GE | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GEV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GEV | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GEV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GEV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GEV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GEV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GEV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GEV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GEV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GEV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GEV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GEV.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GEV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GEV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GEV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GEV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GEV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GEV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GEV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GEV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GGLL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GGLL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GGLL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GGLL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GGLL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GGLL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GGLL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GGLL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GGLL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GGLL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GIB-A.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GIB-A.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GIB-A.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GIB-A.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GIB-A.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GIB-A.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GIB-A.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GIB-A.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GIB-A.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GIB-A.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GOOGL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GOOGL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GOOGL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GOOGL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GOOGL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GOOGL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GOOGL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GOOGL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GOOGL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GOOGL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| GRID | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| GRID | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GRID | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GRID | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| GRID | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GRID | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| GRID | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GRID | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| GRID | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GRID | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| HD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| HD | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| HD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| HD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| HD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| HD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| HURA.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| HURA.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HURA.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HURA.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| HURA.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| HURA.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| HURA.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HURA.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| HURA.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HURA.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| HXQ.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| HXQ.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HXQ.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HXQ.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| HXQ.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| HXQ.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| HXQ.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HXQ.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| HXQ.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HXQ.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| JNJ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| JNJ | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| JNJ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| JNJ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| JNJ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| JNJ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| JNJ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| JNJ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| JNJ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| JNJ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| JPM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| JPM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| JPM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| JPM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| JPM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| JPM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| JPM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| JPM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| JPM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| JPM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| KEYS | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| KEYS | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| KEYS | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| KEYS | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| KEYS | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| KEYS | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| KEYS | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| KEYS | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| KEYS | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| KEYS | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| LIN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| LIN | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| LIN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| LIN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| LIN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| LIN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| LIN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| LIN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| LIN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| LIN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| LLY | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| LLY | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| LLY | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| LLY | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| LLY | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| LLY | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| LLY | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| LLY | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| LLY | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| LLY | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| MDA.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| MDA.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MDA.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MDA.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| MDA.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MDA.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| MDA.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MDA.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| MDA.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MDA.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| META | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| META | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| META | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| META | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| META | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| META | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| META | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| META | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| META | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| META | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| METU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| METU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| METU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| METU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| METU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| METU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| METU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| METU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| METU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| METU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| MRVL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| MRVL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MRVL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MRVL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| MRVL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MRVL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| MRVL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MRVL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| MRVL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MRVL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| MSFT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| MSFT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MSFT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MSFT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| MSFT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MSFT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| MSFT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MSFT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| MSFT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MSFT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| MSFU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| MSFU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MSFU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MSFU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| MSFU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MSFU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| MSFU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MSFU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| MSFU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MSFU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| MTRX.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| MTRX.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MTRX.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MTRX.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| MTRX.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MTRX.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| MTRX.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MTRX.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| MTRX.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MTRX.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| MU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| MU.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| MU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| MU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| MU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| NEE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| NEE | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NEE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NEE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| NEE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NEE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| NEE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NEE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| NEE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NEE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| NEM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| NEM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NEM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NEM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| NEM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NEM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| NEM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NEM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| NEM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NEM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| NFLX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| NFLX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NFLX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NFLX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| NFLX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NFLX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| NFLX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NFLX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| NFLX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NFLX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| NFXL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| NFXL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NFXL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NFXL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| NFXL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NFXL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| NFXL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NFXL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| NFXL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NFXL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| NTR.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| NTR.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NTR.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NTR.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| NTR.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NTR.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| NTR.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NTR.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| NTR.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NTR.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| NVDA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| NVDA | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NVDA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| NVDA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NVDA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| NVDA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NVDA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| NVDA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| NVDL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| NVDL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NVDL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| NVDL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NVDL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| NVDL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NVDL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| NVDL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ONTO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ONTO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ONTO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ONTO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ONTO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ONTO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ONTO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ONTO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ONTO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ONTO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ORBX.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ORBX.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ORBX.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ORBX.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ORBX.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ORBX.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ORBX.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ORBX.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ORBX.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ORBX.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| ORCL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| ORCL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ORCL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ORCL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| ORCL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ORCL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| ORCL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ORCL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| ORCL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ORCL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| PG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| PG | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| PG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| PG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| PG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| PG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| PLD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| PLD | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PLD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PLD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| PLD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| PLD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| PLD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PLD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| PLD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PLD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| PNG.V | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| PNG.V | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PNG.V | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PNG.V | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| PNG.V | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| PNG.V | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| PNG.V | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PNG.V | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| PNG.V | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PNG.V | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| QCOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| QCOM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QCOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QCOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| QCOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| QCOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| QCOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QCOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| QCOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QCOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| QPUX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| QPUX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QPUX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QPUX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| QPUX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| QPUX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| QPUX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QPUX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| QPUX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QPUX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| QTUM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| QTUM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QTUM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QTUM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| QTUM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| QTUM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| QTUM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QTUM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| QTUM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QTUM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| RBOT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| RBOT.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RBOT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RBOT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| RBOT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| RBOT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| RBOT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RBOT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| RBOT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RBOT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| RTX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| RTX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RTX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RTX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| RTX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| RTX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| RTX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RTX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| RTX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RTX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| RY.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| RY.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RY.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RY.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| RY.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| RY.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| RY.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RY.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| RY.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RY.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SETM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SETM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SETM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SETM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SETM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SETM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SETM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SETM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SETM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SETM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SGRD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SGRD.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SGRD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SGRD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SGRD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SGRD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SGRD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SGRD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SGRD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SGRD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SMH | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SMH | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SMH | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SMH | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SMH | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SMH | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SMH | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SMH | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SMH | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SMH | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SNDK.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SNDK.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SNDK.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SNDK.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SNDK.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SNDK.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SNDK.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SNDK.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SNDK.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SNDK.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SOXL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SOXL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SOXL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SOXL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SOXL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SOXL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SOXL.NE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SOXL.NE | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXL.NE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL.NE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SOXL.NE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SOXL.NE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SOXL.NE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXL.NE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SOXL.NE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL.NE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SOXX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SOXX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SOXX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SOXX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SOXX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SOXX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| SPCL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| SPCL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SPCL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SPCL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| SPCL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SPCL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| SPCL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SPCL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| SPCL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SPCL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| TSLA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| TSLA | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSLA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSLA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| TSLA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| TSLA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| TSLA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSLA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| TSLA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSLA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| TSLL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| TSLL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSLL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSLL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| TSLL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| TSLL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| TSLL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSLL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| TSLL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSLL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| TSM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| TSM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| TSM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| TSM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| TSM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| TSM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| UBOT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| UBOT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| UBOT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| UBOT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| UBOT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| UBOT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| UBOT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| UBOT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| UBOT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| UBOT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| UFO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| UFO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| UFO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| UFO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| UFO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| UFO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| UFO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| UFO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| UFO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| UFO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| URA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| URA | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| URA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| URA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| URA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| URA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| URA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| URA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| URA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| URA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| URAA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| URAA | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| URAA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| URAA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| URAA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| URAA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| URAA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| URAA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| URAA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| URAA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| V | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| V | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| V | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| V | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| V | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| V | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| V | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| V | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| V | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| V | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| VFV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| VFV.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| VFV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| VFV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| VFV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| VFV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| VFV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| VFV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| VFV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| VFV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| VRT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| VRT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| VRT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| VRT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| VRT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| VRT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| VRT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| VRT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| VRT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| VRT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| WDC.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| WDC.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WDC.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WDC.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| WDC.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| WDC.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| WDC.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WDC.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| WDC.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WDC.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| WELL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| WELL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WELL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WELL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| WELL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| WELL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| WELL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WELL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| WELL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WELL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| WMT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| WMT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WMT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WMT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| WMT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| WMT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| WMT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WMT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| WMT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WMT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| XCHP.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| XCHP.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XCHP.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XCHP.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| XCHP.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XCHP.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| XCHP.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XCHP.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| XCHP.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XCHP.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| XDRV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| XDRV.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XDRV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XDRV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| XDRV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XDRV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| XDRV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XDRV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| XDRV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XDRV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| XEQT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| XEQT.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XEQT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XEQT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| XEQT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XEQT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| XEQT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XEQT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| XEQT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XEQT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| XETM.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| XETM.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XETM.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XETM.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| XETM.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XETM.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| XETM.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XETM.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| XETM.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XETM.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| XGD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| XGD.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XGD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XGD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| XGD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XGD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| XGD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XGD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| XGD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XGD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
| XOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -10.6% | ↓ below -10.8% | PASS |  |  |
| XOM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -3.5% on Nov 20 | -3.49% on Nov 20 | PASS |  |  |
| XOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -9.1% | ↓ below -9.1% | PASS |  |  |
| XOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 20 close | Nov 20 | PASS |  |  |
| XOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 35.9 | 35.9 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | extreme | extreme | PASS |  |  |
