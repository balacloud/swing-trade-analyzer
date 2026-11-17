# Statement Audit phase 3a report (Market backdrop, Fundamentals, Mean-Reversion Read)

Run: 2026-11-17T16:00 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 3543 · WRONG 51 (CRITICAL) · MISLEADING 17 (per-row severity) · UNVERIFIED 138 (INFO)

Recomputed from bars: MR RSI(2), % above the 200-day, dollar volume, the four rule marks, the blocker sentence; S&P 500 200/50-day and the 10-session drop (the app's own 260 bars); QQQ and "largest since" from an independent Yahoo history (S4).
Provider fields (sales growth, ROE, debt/equity) are arithmetic and flag logic only: no recompute is possible (UNVERIFIED as to truth). NOT YET COVERED: the Data Sources tab (phase 3b), other tabs; branches these tickers do not reach (signal true, VIX band edges, no-down-day, unavailable backdrop, negative equity) are exercised by planted tests only.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| ABBV | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| ASTL.TO | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| ATD.TO | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| CCO.TO | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| CGY.TO | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| CNR.TO | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| CVX | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| ETN | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| GEV | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| GIB-A.TO | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| HD | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| LLY | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| MDA.TO | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| MRVL | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| NTR.TO | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| PG | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| PNG.V | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| V | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| VRT | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| WMT | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| XOM | FU5 | headline = the number of tripped flags | Can't check | 0 flag(s) | WRONG | CRITICAL |  |
| AAPU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 28.23% | 27.41% | WRONG | CRITICAL |  |
| AMZU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.96% | 0.20% | WRONG | CRITICAL |  |
| CARS.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average | WRONG | CRITICAL |  |
| CARS.TO | MR-row-volume | zero-volume fund: "no volume data", unchecked | Does it trade enough to get in and out? ✗ $26,790 traded on an average | no volume data | WRONG | CRITICAL |  |
| COP | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 68.24 | 52.05 | WRONG | CRITICAL |  |
| COP | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 15.33% | 13.78% | WRONG | CRITICAL |  |
| COPP.TO | MR-row-volume | Volume row found | Does it trade enough to get in and out? ✗ $790,606 traded on | row | WRONG | CRITICAL |  |
| COPX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.6% | -20.74% | WRONG | CRITICAL |  |
| COTG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,028,329 | 1,040,150 | WRONG | CRITICAL |  |
| DUK | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 94.43 | 95.68 | WRONG | CRITICAL |  |
| DUK | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 4.59% | 6.46% | WRONG | CRITICAL |  |
| EQIX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.9% | 2.46% | WRONG | CRITICAL |  |
| GGLL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -36.62% | -37.16% | WRONG | CRITICAL |  |
| GRID | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -12.28% | -12.61% | WRONG | CRITICAL |  |
| HURA.TO | MR-row-volume | Volume row found | Does it trade enough to get in and out? ✗ $507,990 traded on | row | WRONG | CRITICAL |  |
| JNJ | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13% | 13.65% | WRONG | CRITICAL |  |
| LIN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 5.32% | 5.77% | WRONG | CRITICAL |  |
| MSFU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 26.31% | 25.12% | WRONG | CRITICAL |  |
| MTRX.TO | MR-row-volume | Volume row found | Does it trade enough to get in and out? ✗ $526,345 traded on | row | WRONG | CRITICAL |  |
| NEE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -2.3% | -1.38% | WRONG | CRITICAL |  |
| RBOT.TO | MR-row-volume | Volume row found | Does it trade enough to get in and out? ✗ $117,305 traded on | row | WRONG | CRITICAL |  |
| SO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 87.14 | 82.26 | WRONG | CRITICAL |  |
| SO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 3.86% | 2.09% | WRONG | CRITICAL |  |
| TSLL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -16.67% | -17.65% | WRONG | CRITICAL |  |
| TSM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.08% | -7.39% | WRONG | CRITICAL |  |
| UBOT | MR-row-volume | Volume row found | Does it trade enough to get in and out? ✗ $325,519 traded on | row | WRONG | CRITICAL |  |
| V | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 23.14% | 22.69% | WRONG | CRITICAL |  |
| XDRV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average | WRONG | CRITICAL |  |
| XDRV.TO | MR-row-volume | zero-volume fund: "no volume data", unchecked | Does it trade enough to get in and out? ✗ $1,786 traded on an average  | no volume data | WRONG | CRITICAL |  |
| XETM.TO | MR-row-volume | Volume row found | Does it trade enough to get in and out? ✗ $203,585 traded on | row | WRONG | CRITICAL |  |
| AMZU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.0% | TR +0.2% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| CAT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -29.3% | TR -29.0% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| CVX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +11.8% | TR +10.8% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| DUK | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +4.6% | TR +6.5% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| EQIX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.9% | TR +2.5% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| GE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +0.6% | TR +0.4% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| GGLL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -36.6% | TR -37.2% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| GRID | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -12.3% | TR -12.6% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| MSFU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +26.3% | TR +25.1% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| PG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +16.8% | TR +15.4% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| QPUX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -82.5% | TR -87.4% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| QTUM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -9.8% | TR -10.1% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| RTX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +0.2% | TR -0.2% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| SO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +3.9% | TR +2.1% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| TSLL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -16.7% | TR -17.6% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| TSM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -7.1% | TR -7.4% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| V | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +23.1% | TR +22.7% | MISLEADING | LOW | the two cards divide by different roundings of the average |
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
| AMZN | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -16 5% $244.86 2026 -11 -16 $257.75 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| AMZU | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -16 5% $33.51 2026 -11 -16 $35.27 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
| NTR.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 2026 -11 -16 5% $93.69 2026 -11 -16 $98.62 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 13 unclaimed number token(s) |
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
| AAPL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-02 (15 days ago); no upcoming date listed. | 2026-11-02 days_until=-15 | PASS |  |  |
| AAPU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AAPU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ABBV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (18 days ago); no upcoming date listed. Earnin | 2026-10-30 days_until=-18 | PASS |  |  |
| AIPO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AIPO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ALAB | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +153.7% | +153.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ALAB | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ALAB | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) | Alpha Vantage | PASS |  |  |
| ALAB | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (14 days ago); no upcoming date listed. | 2026-11-03 days_until=-14 | PASS |  |  |
| AMD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.6% | 11.6% flag=False | PASS |  |  |
| AMD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.10 | 0.10 flag=False | PASS |  |  |
| AMD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AMD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| AMD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (14 days ago); no upcoming date listed. | 2026-11-03 days_until=-14 | PASS |  |  |
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
| AMZN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (19 days ago); no upcoming date listed. | 2026-10-29 days_until=-19 | PASS |  |  |
| AMZU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AMZU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ANET.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ANET.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ASML.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ASML.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ASTL.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (20 days ago); no upcoming date listed. Earnin | 2026-10-28 days_until=-20 | PASS |  |  |
| ATD.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-24 · in 7 days. Within a week: decide before then whether to hold throug | 2026-11-24 days_until=7 | PASS |  |  |
| AVGC | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AVGC | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| AVGO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +85.5% | +85.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AVGO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 43.9% | 43.9% flag=False | PASS |  |  |
| AVGO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.60 | 0.60 flag=False | PASS |  |  |
| AVGO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AVGO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| AVGO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-09 · in 22 days. If you'll still hold on that date, the price can jump e | 2026-12-09 days_until=22 | PASS |  |  |
| AVGO.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AVGO.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| BDT.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.7% | +36.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| BDT.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.6% | 16.6% flag=False | PASS |  |  |
| BDT.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.79 | 0.79 flag=False | PASS |  |  |
| BDT.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| BDT.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| BDT.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-11 (6 days ago); no upcoming date listed. | 2026-11-11 days_until=-6 | PASS |  |  |
| BOTZ | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| BOTZ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| BRK-B | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.2% | +11.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| BRK-B | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.9% | 11.9% flag=False | PASS |  |  |
| BRK-B | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| BRK-B | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| BRK-B | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| BRK-B | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-07 (10 days ago); no upcoming date listed. | 2026-11-07 days_until=-10 | PASS |  |  |
| BRKU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| BRKU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CAMT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 5.8% | 5.8% flag=False | PASS |  |  |
| CAMT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.69 | 0.69 flag=False | PASS |  |  |
| CAMT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CAMT | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| CAMT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (13 days ago); no upcoming date listed. | 2026-11-04 days_until=-13 | PASS |  |  |
| CARS.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| CARS.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CAT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +17.3% | +17.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CAT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 58.5% | 58.5% flag=False | PASS |  |  |
| CAT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 2.10 | 2.10 flag=True | PASS |  |  |
| CAT | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| CAT | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| CAT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| CAT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (19 days ago); no upcoming date listed. | 2026-10-29 days_until=-19 | PASS |  |  |
| CCO.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (18 days ago); no upcoming date listed. Earnin | 2026-10-30 days_until=-18 | PASS |  |  |
| CEG | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +45.4% | +45.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CEG | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 18.3% | 18.3% flag=False | PASS |  |  |
| CEG | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| CEG | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CEG | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CEG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-09 (8 days ago); no upcoming date listed. | 2026-11-09 days_until=-8 | PASS |  |  |
| CGY.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-30 · in 13 days. If you'll still hold on that date, the price can jump e | 2026-11-30 days_until=13 | PASS |  |  |
| CNQ.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +34.4% | +34.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CNQ.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 32.4% | 32.4% flag=False | PASS |  |  |
| CNQ.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.42 | 0.42 flag=False | PASS |  |  |
| CNQ.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CNQ.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CNQ.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (12 days ago); no upcoming date listed. | 2026-11-05 days_until=-12 | PASS |  |  |
| CNR.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-29 · in 73 days. If you'll still hold on that date, the price can jump e | 2027-01-29 days_until=73 | PASS |  |  |
| COP | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.8% | 17.8% flag=False | PASS |  |  |
| COP | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.35 | 0.35 flag=False | PASS |  |  |
| COP | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| COP | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| COP | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (12 days ago); no upcoming date listed. | 2026-11-05 days_until=-12 | PASS |  |  |
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
| COST | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-10 · in 23 days. If you'll still hold on that date, the price can jump e | 2026-12-10 days_until=23 | PASS |  |  |
| COTG | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| COTG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CSU.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +19.1% | +19.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CSU.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 24.2% | 24.2% flag=False | PASS |  |  |
| CSU.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.13 | 1.13 flag=False | PASS |  |  |
| CSU.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CSU.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CSU.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-06 (11 days ago); no upcoming date listed. | 2026-11-06 days_until=-11 | PASS |  |  |
| CVX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (18 days ago); no upcoming date listed. Earnin | 2026-10-30 days_until=-18 | PASS |  |  |
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
| DUK | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (12 days ago); no upcoming date listed. | 2026-11-05 days_until=-12 | PASS |  |  |
| ELIL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ELIL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| EQIX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.5% | 11.5% flag=False | PASS |  |  |
| EQIX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.72 | 1.72 flag=False | PASS |  |  |
| EQIX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| EQIX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| EQIX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (20 days ago); no upcoming date listed. | 2026-10-28 days_until=-20 | PASS |  |  |
| ETN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (14 days ago); no upcoming date listed. Earnin | 2026-11-03 days_until=-14 | PASS |  |  |
| FCX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 15.3% | 15.3% flag=False | PASS |  |  |
| FCX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.49 | 0.49 flag=False | PASS |  |  |
| FCX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| FCX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| FCX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (21 days ago); no upcoming date listed. | 2026-10-27 days_until=-21 | PASS |  |  |
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
| GE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (28 days ago); no upcoming date listed. | 2026-10-20 days_until=-28 | PASS |  |  |
| GEV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-27 · in 71 days. If you'll still hold on that date, the price can jump e | 2027-01-27 days_until=71 | PASS |  |  |
| GEV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GEV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GGLL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GGLL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GIB-A.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-11 (6 days ago); no upcoming date listed. Earning | 2026-11-11 days_until=-6 | PASS |  |  |
| GOOGL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 42.6% | 42.6% flag=False | PASS |  |  |
| GOOGL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.18 | 0.18 flag=False | PASS |  |  |
| GOOGL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GOOGL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| GOOGL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (20 days ago); no upcoming date listed. | 2026-10-28 days_until=-20 | PASS |  |  |
| GRID | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GRID | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| HD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-17 · today. The price can jump either way on the report. Earnings dates  | 2026-11-17 days_until=0 | PASS |  |  |
| HURA.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| HURA.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| HXQ.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| HXQ.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| JNJ | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.6% | 19.6% flag=False | PASS |  |  |
| JNJ | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.55 | 0.55 flag=False | PASS |  |  |
| JNJ | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| JNJ | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| JNJ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-26 · in 70 days. If you'll still hold on that date, the price can jump e | 2027-01-26 days_until=70 | PASS |  |  |
| JPM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +10.2% | +10.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| JPM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.9% | 17.9% flag=False | PASS |  |  |
| JPM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 3.32 | 3.32 flag=True | PASS |  |  |
| JPM | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| JPM | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| JPM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| JPM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-14 · in 58 days. If you'll still hold on that date, the price can jump e | 2027-01-14 days_until=58 | PASS |  |  |
| KEYS | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.5% | +36.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| KEYS | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 20.9% | 20.9% flag=False | PASS |  |  |
| KEYS | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.42 | 0.42 flag=False | PASS |  |  |
| KEYS | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| KEYS | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| KEYS | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-19 · in 2 days. Within a week: decide before then whether to hold throug | 2026-11-19 days_until=2 | PASS |  |  |
| LIN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 18.1% | 18.1% flag=False | PASS |  |  |
| LIN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.68 | 0.68 flag=False | PASS |  |  |
| LIN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| LIN | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| LIN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (19 days ago); no upcoming date listed. | 2026-10-29 days_until=-19 | PASS |  |  |
| LLY | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (19 days ago); no upcoming date listed. Earnin | 2026-10-29 days_until=-19 | PASS |  |  |
| MDA.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (12 days ago); no upcoming date listed. Earnin | 2026-11-05 days_until=-12 | PASS |  |  |
| META | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +26.1% | +26.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| META | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 30.3% | 30.3% flag=False | PASS |  |  |
| META | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.30 | 0.30 flag=False | PASS |  |  |
| META | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| META | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| META | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (27 days ago); no upcoming date listed. | 2026-10-21 days_until=-27 | PASS |  |  |
| METU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| METU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| MRVL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-01 · in 14 days. If you'll still hold on that date, the price can jump e | 2026-12-01 days_until=14 | PASS |  |  |
| MSFT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +18.8% | +18.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MSFT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 33.2% | 33.2% flag=False | PASS |  |  |
| MSFT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.23 | 0.23 flag=False | PASS |  |  |
| MSFT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MSFT | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| MSFT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (20 days ago); no upcoming date listed. | 2026-10-28 days_until=-20 | PASS |  |  |
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
| NEE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (27 days ago); no upcoming date listed. | 2026-10-21 days_until=-27 | PASS |  |  |
| NEM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 26.5% | 26.5% flag=False | PASS |  |  |
| NEM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.16 | 0.16 flag=False | PASS |  |  |
| NEM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NEM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| NEM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-22 (26 days ago); no upcoming date listed. | 2026-10-22 days_until=-26 | PASS |  |  |
| NFLX | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.8% | +11.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NFLX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.4% | 50.4% flag=False | PASS |  |  |
| NFLX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.52 | 0.52 flag=False | PASS |  |  |
| NFLX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NFLX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NFLX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (28 days ago); no upcoming date listed. | 2026-10-20 days_until=-28 | PASS |  |  |
| NFXL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| NFXL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| NTR.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (13 days ago); no upcoming date listed. Earnin | 2026-11-04 days_until=-13 | PASS |  |  |
| NVDA | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +105.8% | +105.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NVDA | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 110.1% | 110.1% flag=False | PASS |  |  |
| NVDA | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| NVDA | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NVDA | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NVDA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-17 · today. The price can jump either way on the report. | 2026-11-17 days_until=0 | PASS |  |  |
| NVDL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| NVDL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ONTO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 6.5% | 6.5% flag=False | PASS |  |  |
| ONTO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.77 | 0.77 flag=False | PASS |  |  |
| ONTO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ONTO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| ONTO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-09 (8 days ago); no upcoming date listed. | 2026-11-09 days_until=-8 | PASS |  |  |
| ORBX.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ORBX.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ORCL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 42.6% | 42.6% flag=False | PASS |  |  |
| ORCL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 2.01 | 2.01 flag=True | PASS |  |  |
| ORCL | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| ORCL | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| ORCL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| ORCL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-14 · in 27 days. If you'll still hold on that date, the price can jump e | 2026-12-14 days_until=27 | PASS |  |  |
| PG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-22 (26 days ago); no upcoming date listed. Earnin | 2026-10-22 days_until=-26 | PASS |  |  |
| PLD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 7.9% | 7.9% flag=False | PASS |  |  |
| PLD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.66 | 0.66 flag=False | PASS |  |  |
| PLD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PLD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| PLD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (33 days ago); no upcoming date listed. | 2026-10-15 days_until=-33 | PASS |  |  |
| PNG.V | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-24 · in 7 days. Within a week: decide before then whether to hold throug | 2026-11-24 days_until=7 | PASS |  |  |
| QCOM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.3% | 50.3% flag=False | PASS |  |  |
| QCOM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.50 | 0.50 flag=False | PASS |  |  |
| QCOM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| QCOM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| QCOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (13 days ago); no upcoming date listed. | 2026-11-04 days_until=-13 | PASS |  |  |
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
| RTX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (28 days ago); no upcoming date listed. | 2026-10-20 days_until=-28 | PASS |  |  |
| RY.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +8.9% | +8.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| RY.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.2% | 16.2% flag=False | PASS |  |  |
| RY.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 4.10 | 4.10 flag=True | PASS |  |  |
| RY.TO | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| RY.TO | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| RY.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| RY.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-03 · in 16 days. If you'll still hold on that date, the price can jump e | 2026-12-03 days_until=16 | PASS |  |  |
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
| SO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (12 days ago); no upcoming date listed. | 2026-11-05 days_until=-12 | PASS |  |  |
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
| TSLA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (27 days ago); no upcoming date listed. | 2026-10-21 days_until=-27 | PASS |  |  |
| TSLL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| TSLL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| TSM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +50.9% | +50.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| TSM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 41.9% | 41.9% flag=False | PASS |  |  |
| TSM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| TSM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| TSM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| TSM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (33 days ago); no upcoming date listed. | 2026-10-15 days_until=-33 | PASS |  |  |
| UBOT | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| UBOT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| UFO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| UFO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| URA | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| URA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| URAA | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| URAA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| V | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (21 days ago); no upcoming date listed. Earnin | 2026-10-27 days_until=-21 | PASS |  |  |
| VFV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| VFV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| VRT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (20 days ago); no upcoming date listed. Earnin | 2026-10-28 days_until=-20 | PASS |  |  |
| WDC.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| WDC.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| WELL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +38.4% | +38.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| WELL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 3.7% | 3.7% flag=False | PASS |  |  |
| WELL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.40 | 0.40 flag=False | PASS |  |  |
| WELL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| WELL | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| WELL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-26 (22 days ago); no upcoming date listed. | 2026-10-26 days_until=-22 | PASS |  |  |
| WMT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-19 · in 2 days. Within a week: decide before then whether to hold throug | 2026-11-19 days_until=2 | PASS |  |  |
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
| XOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (18 days ago); no upcoming date listed. Earnin | 2026-10-30 days_until=-18 | PASS |  |  |
| AAPL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +16.9% | TR +16.9% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AAPL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AAPL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AAPL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 16,532,614,871 | 16,532,614,789 | PASS |  |  |
| AAPL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AAPL | MR-price | price = the last completed close | 352.78 | 352.78 | PASS |  |  |
| AAPL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $352.78 needs above $10 | $352.78 needs above $10 | PASS |  |  |
| AAPL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 32.9 needs under 10 | 32.91 needs under 10 -> ✗ | PASS |  |  |
| AAPL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 16.9% above its 200-day average | 16.9% above | PASS |  |  |
| AAPL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $16.5B traded on an average day needs above $25M | $16,532,614,871 needs above $25,000,000 | PASS |  |  |
| AAPL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 32.91 | 32.91 | PASS |  |  |
| AAPL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 16.92% | 16.92% | PASS |  |  |
| AAPL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +28.2% | TR +28.2% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AAPU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AAPU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AAPU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 27,176,283 | 27,176,284 | PASS |  |  |
| AAPU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AAPU | MR-price | price = the last completed close | 48.77 | 48.77 | PASS |  |  |
| AAPU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $48.77 needs above $10 | $48.77 needs above $10 | PASS |  |  |
| AAPU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 31.2 needs under 10 | 31.19 needs under 10 -> ✗ | PASS |  |  |
| AAPU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 28.2% above its 200-day average | 28.2% above | PASS |  |  |
| AAPU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $27.2M traded on an average day needs above $25M | $27,176,283 needs above $25,000,000 | PASS |  |  |
| AAPU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 31.19 | 31.19 | PASS |  |  |
| AAPU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ABBV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +22.2% | TR +22.2% | PASS | LOW | the two cards divide by different roundings of the average |
| ABBV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ABBV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| ABBV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ABBV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,515,476,683 | 1,515,476,683 | PASS |  |  |
| ABBV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ABBV | MR-price | price = the last completed close | 294.55 | 294.55 | PASS |  |  |
| ABBV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $294.55 needs above $10 | $294.55 needs above $10 | PASS |  |  |
| ABBV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 47.5 needs under 10 | 47.49 needs under 10 -> ✗ | PASS |  |  |
| ABBV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 22.2% above its 200-day average | 22.2% above | PASS |  |  |
| ABBV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.5B traded on an average day needs above $25M | $1,515,476,683 needs above $25,000,000 | PASS |  |  |
| ABBV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 47.49 | 47.49 | PASS |  |  |
| ABBV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 22.16% | 22.16% | PASS |  |  |
| ABBV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AIPO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.4% | TR -20.4% | PASS | LOW | the two cards divide by different roundings of the average |
| AIPO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AIPO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| AIPO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AIPO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AIPO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 47,912,052 | 47,911,429 | PASS |  |  |
| AIPO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AIPO | MR-price | price = the last completed close | 22.69 | 22.69 | PASS |  |  |
| AIPO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $22.69 needs above $10 | $22.69 needs above $10 | PASS |  |  |
| AIPO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.4 needs under 10 | 11.38 needs under 10 -> ✗ | PASS |  |  |
| AIPO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.4% below its 200-day average | 20.4% below | PASS |  |  |
| AIPO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $47.9M traded on an average day needs above $25M | $47,912,052 needs above $25,000,000 | PASS |  |  |
| AIPO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.38 | 11.38 | PASS |  |  |
| AIPO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.41% | -20.41% | PASS |  |  |
| AIPO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ALAB | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -21.5% | TR -21.5% | PASS | LOW | the two cards divide by different roundings of the average |
| ALAB | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ALAB | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| ALAB | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ALAB | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ALAB | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,164,514,389 | 1,164,514,382 | PASS |  |  |
| ALAB | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ALAB | MR-price | price = the last completed close | 202.34 | 202.34 | PASS |  |  |
| ALAB | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $202.34 needs above $10 | $202.34 needs above $10 | PASS |  |  |
| ALAB | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.7 needs under 10 | 10.71 needs under 10 -> ✗ | PASS |  |  |
| ALAB | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 21.5% below its 200-day average | 21.5% below | PASS |  |  |
| ALAB | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.2B traded on an average day needs above $25M | $1,164,514,389 needs above $25,000,000 | PASS |  |  |
| ALAB | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.71 | 10.71 | PASS |  |  |
| ALAB | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -21.49% | -21.49% | PASS |  |  |
| ALAB | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +18.8% | TR +18.8% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AMD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 18,034,998,377 | 18,004,099,726 | PASS |  |  |
| AMD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD | MR-price | price = the last completed close | 504.28 | 504.28 | PASS |  |  |
| AMD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $504.28 needs above $10 | $504.28 needs above $10 | PASS |  |  |
| AMD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.0 needs under 10 | 22.01 needs under 10 -> ✗ | PASS |  |  |
| AMD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 18.8% above its 200-day average | 18.8% above | PASS |  |  |
| AMD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $18B traded on an average day needs above $25M | $18,034,998,377 needs above $25,000,000 | PASS |  |  |
| AMD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.01 | 22.01 | PASS |  |  |
| AMD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 18.81% | 18.81% | PASS |  |  |
| AMD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +25.9% | TR +25.9% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-13 | 2026-11-13 | PASS |  |  |
| AMD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 35,789,890 | 35,789,891 | PASS |  |  |
| AMD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD.TO | MR-price | price = the last completed close | 13.76 | 13.76 | PASS |  |  |
| AMD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $13.76 needs above $10 | $13.76 needs above $10 | PASS |  |  |
| AMD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 38.0 needs under 10 | 37.99 needs under 10 -> ✗ | PASS |  |  |
| AMD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 25.9% above its 200-day average | 25.9% above | PASS |  |  |
| AMD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $35.8M traded on an average day needs above $25M | $35,789,890 needs above $25,000,000 | PASS |  |  |
| AMD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 37.99 | 37.99 | PASS |  |  |
| AMD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 25.87% | 25.86% | PASS |  |  |
| AMD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMZN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +5.3% | TR +5.3% | PASS | LOW | the two cards divide by different roundings of the average |
| AMZN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AMZN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,698,663,966 | 12,698,663,966 | PASS |  |  |
| AMZN | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| AMZN | MR-price | price = the last completed close | 257.75 | 257.75 | PASS |  |  |
| AMZN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $257.75 needs above $10 | $257.75 needs above $10 | PASS |  |  |
| AMZN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.1 needs under 10 | 8.1 needs under 10 -> ✓ | PASS |  |  |
| AMZN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 5.3% above its 200-day average | 5.3% above | PASS |  |  |
| AMZN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.7B traded on an average day needs above $25M | $12,698,663,966 needs above $25,000,000 | PASS |  |  |
| AMZN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8.1 | 8.10 | PASS |  |  |
| AMZN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 5.34% | 5.34% | PASS |  |  |
| AMZN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMZU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AMZU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 66,270,505 | 66,287,930 | PASS |  |  |
| AMZU | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| AMZU | MR-price | price = the last completed close | 35.27 | 35.27 | PASS |  |  |
| AMZU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $35.27 needs above $10 | $35.27 needs above $10 | PASS |  |  |
| AMZU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.3 needs under 10 | 7.35 needs under 10 -> ✓ | PASS |  |  |
| AMZU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.0% above its 200-day average | 1.0% above | PASS |  |  |
| AMZU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $66.3M traded on an average day needs above $25M | $66,270,505 needs above $25,000,000 | PASS |  |  |
| AMZU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.35 | 7.35 | PASS |  |  |
| AMZU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ANET.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ANET.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| ANET.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ANET.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ANET.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ANET.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ANET.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,522,550 | 2,522,550 | PASS |  |  |
| ANET.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ANET.TO | MR-price | price = the last completed close | 33.41 | 33.41 | PASS |  |  |
| ANET.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $33.41 needs above $10 | $33.41 needs above $10 | PASS |  |  |
| ANET.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 23.4 needs under 10 | 23.45 needs under 10 -> ✗ | PASS |  |  |
| ANET.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 11.0% above its 200-day average | 11.0% above | PASS |  |  |
| ANET.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.5M traded on an average day needs above $25M | $2,522,550 needs above $25,000,000 | PASS |  |  |
| ANET.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 23.45 | 23.45 | PASS |  |  |
| ANET.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 11.01% | 11.01% | PASS |  |  |
| ANET.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ASML.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -7.6% | TR -7.6% | PASS | LOW | the two cards divide by different roundings of the average |
| ASML.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ASML.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| ASML.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASML.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,697,585 | 2,697,598 | PASS |  |  |
| ASML.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ASML.TO | MR-price | price = the last completed close | 41.62 | 41.62 | PASS |  |  |
| ASML.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $41.62 needs above $10 | $41.62 needs above $10 | PASS |  |  |
| ASML.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.2 needs under 10 | 11.18 needs under 10 -> ✗ | PASS |  |  |
| ASML.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 7.6% below its 200-day average | 7.6% below | PASS |  |  |
| ASML.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,697,585 needs above $25,000,000 | PASS |  |  |
| ASML.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.18 | 11.18 | PASS |  |  |
| ASML.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.63% | -7.63% | PASS |  |  |
| ASML.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ASTL.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ASTL.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; the price is under $10; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| ASTL.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASTL.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,955,659 | 5,955,660 | PASS |  |  |
| ASTL.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ASTL.TO | MR-price | price = the last completed close | 7.67 | 7.67 | PASS |  |  |
| ASTL.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $7.67 needs above $10 | $7.67 needs above $10 | PASS |  |  |
| ASTL.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.6 needs under 10 | 10.62 needs under 10 -> ✗ | PASS |  |  |
| ASTL.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 22.7% above its 200-day average | 22.7% above | PASS |  |  |
| ASTL.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $6M traded on an average day needs above $25M | $5,955,659 needs above $25,000,000 | PASS |  |  |
| ASTL.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.62 | 10.62 | PASS |  |  |
| ASTL.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 22.7% | 22.70% | PASS |  |  |
| ASTL.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ATD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.9% | TR +1.9% | PASS | LOW | the two cards divide by different roundings of the average |
| ATD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ATD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| ATD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ATD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 100,171,655 | 100,171,656 | PASS |  |  |
| ATD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ATD.TO | MR-price | price = the last completed close | 83.9 | 83.9 | PASS |  |  |
| ATD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $83.90 needs above $10 | $83.90 needs above $10 | PASS |  |  |
| ATD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 91.6 needs under 10 | 91.61 needs under 10 -> ✗ | PASS |  |  |
| ATD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.9% above its 200-day average | 1.9% above | PASS |  |  |
| ATD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $100.2M traded on an average day needs above $25M | $100,171,655 needs above $25,000,000 | PASS |  |  |
| ATD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 91.61 | 91.61 | PASS |  |  |
| ATD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.92% | 1.92% | PASS |  |  |
| ATD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AVGC | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| AVGO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -9.3% | TR -9.3% | PASS | LOW | the two cards divide by different roundings of the average |
| AVGO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AVGO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| AVGO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 8,984,213,777 | 8,984,213,800 | PASS |  |  |
| AVGO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AVGO | MR-price | price = the last completed close | 333.4 | 333.4 | PASS |  |  |
| AVGO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $333.40 needs above $10 | $333.40 needs above $10 | PASS |  |  |
| AVGO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 26.4 needs under 10 | 26.35 needs under 10 -> ✗ | PASS |  |  |
| AVGO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.3% below its 200-day average | 9.3% below | PASS |  |  |
| AVGO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $9B traded on an average day needs above $25M | $8,984,213,777 needs above $25,000,000 | PASS |  |  |
| AVGO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 26.35 | 26.35 | PASS |  |  |
| AVGO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.26% | -9.26% | PASS |  |  |
| AVGO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AVGO.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AVGO.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| AVGO.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 17,019,916 | 17,020,014 | PASS |  |  |
| AVGO.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AVGO.TO | MR-price | price = the last completed close | 12.64 | 12.64 | PASS |  |  |
| AVGO.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $12.64 needs above $10 | $12.64 needs above $10 | PASS |  |  |
| AVGO.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 26.6 needs under 10 | 26.62 needs under 10 -> ✗ | PASS |  |  |
| AVGO.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.8% below its 200-day average | 9.8% below | PASS |  |  |
| AVGO.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $17M traded on an average day needs above $25M | $17,019,916 needs above $25,000,000 | PASS |  |  |
| AVGO.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 26.62 | 26.62 | PASS |  |  |
| AVGO.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.82% | -9.82% | PASS |  |  |
| AVGO.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BDT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +28.8% | TR +28.8% | PASS | LOW | the two cards divide by different roundings of the average |
| BDT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| BDT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| BDT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BDT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 26,861,477 | 26,861,428 | PASS |  |  |
| BDT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BDT.TO | MR-price | price = the last completed close | 75.18 | 75.18 | PASS |  |  |
| BDT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $75.18 needs above $10 | $75.18 needs above $10 | PASS |  |  |
| BDT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 29.6 needs under 10 | 29.62 needs under 10 -> ✗ | PASS |  |  |
| BDT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 28.8% above its 200-day average | 28.8% above | PASS |  |  |
| BDT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $26.9M traded on an average day needs above $25M | $26,861,477 needs above $25,000,000 | PASS |  |  |
| BDT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 29.62 | 29.62 | PASS |  |  |
| BDT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 28.83% | 28.83% | PASS |  |  |
| BDT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BOTZ | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -16.9% | TR -16.9% | PASS | LOW | the two cards divide by different roundings of the average |
| BOTZ | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| BOTZ | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| BOTZ | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BOTZ | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 27,512,644 | 27,512,645 | PASS |  |  |
| BOTZ | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BOTZ | MR-price | price = the last completed close | 30.12 | 30.12 | PASS |  |  |
| BOTZ | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $30.12 needs above $10 | $30.12 needs above $10 | PASS |  |  |
| BOTZ | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.5 needs under 10 | 7.49 needs under 10 -> ✓ | PASS |  |  |
| BOTZ | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 16.9% below its 200-day average | 16.9% below | PASS |  |  |
| BOTZ | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $27.5M traded on an average day needs above $25M | $27,512,644 needs above $25,000,000 | PASS |  |  |
| BOTZ | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.49 | 7.49 | PASS |  |  |
| BOTZ | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -16.88% | -16.87% | PASS |  |  |
| BOTZ | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BRK-B | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +18.3% | TR +18.3% | PASS | LOW | the two cards divide by different roundings of the average |
| BRK-B | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| BRK-B | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| BRK-B | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BRK-B | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,931,074,274 | 2,931,074,255 | PASS |  |  |
| BRK-B | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BRK-B | MR-price | price = the last completed close | 592.85 | 592.85 | PASS |  |  |
| BRK-B | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $592.85 needs above $10 | $592.85 needs above $10 | PASS |  |  |
| BRK-B | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 95.2 needs under 10 | 95.22 needs under 10 -> ✗ | PASS |  |  |
| BRK-B | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 18.3% above its 200-day average | 18.3% above | PASS |  |  |
| BRK-B | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.9B traded on an average day needs above $25M | $2,931,074,274 needs above $25,000,000 | PASS |  |  |
| BRK-B | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 95.22 | 95.22 | PASS |  |  |
| BRK-B | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 18.33% | 18.33% | PASS |  |  |
| BRK-B | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BRKU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +33.0% | TR +33.0% | PASS | LOW | the two cards divide by different roundings of the average |
| BRKU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| BRKU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| BRKU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BRKU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BRKU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,825,783 | 2,825,777 | PASS |  |  |
| BRKU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BRKU | MR-price | price = the last completed close | 30.81 | 30.81 | PASS |  |  |
| BRKU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $30.81 needs above $10 | $30.81 needs above $10 | PASS |  |  |
| BRKU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 97.6 needs under 10 | 97.56 needs under 10 -> ✗ | PASS |  |  |
| BRKU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 33.0% above its 200-day average | 33.0% above | PASS |  |  |
| BRKU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.8M traded on an average day needs above $25M | $2,825,783 needs above $25,000,000 | PASS |  |  |
| BRKU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 97.56 | 97.56 | PASS |  |  |
| BRKU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 33.03% | 33.03% | PASS |  |  |
| BRKU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CAMT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -39.9% | TR -39.9% | PASS | LOW | the two cards divide by different roundings of the average |
| CAMT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CAMT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CAMT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAMT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 62,047,397 | 62,030,769 | PASS |  |  |
| CAMT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CAMT | MR-price | price = the last completed close | 93.25 | 93.25 | PASS |  |  |
| CAMT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $93.25 needs above $10 | $93.25 needs above $10 | PASS |  |  |
| CAMT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.9 needs under 10 | 7.89 needs under 10 -> ✓ | PASS |  |  |
| CAMT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 39.9% below its 200-day average | 39.9% below | PASS |  |  |
| CAMT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $62M traded on an average day needs above $25M | $62,047,397 needs above $25,000,000 | PASS |  |  |
| CAMT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.89 | 7.89 | PASS |  |  |
| CAMT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -39.88% | -39.88% | PASS |  |  |
| CAMT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CARS.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -27.9% | TR -27.9% | PASS | LOW | the two cards divide by different roundings of the average |
| CARS.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CARS.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CARS.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CARS.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CARS.TO | MR-cond-volume_filter | zero-volume history: the volume rule is not checked, never a fake $0 fail | False | None/unchecked | PASS |  | the card shows "no volume data" |
| CARS.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CARS.TO | MR-price | price = the last completed close | 20.19 | 20.19 | PASS |  |  |
| CARS.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $20.19 needs above $10 | $20.19 needs above $10 | PASS |  |  |
| CARS.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.3 needs under 10 | 10.29 needs under 10 -> ✗ | PASS |  |  |
| CARS.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 27.9% below its 200-day average | 27.9% below | PASS |  |  |
| CARS.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.29 | 10.29 | PASS |  |  |
| CARS.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -27.9% | -27.90% | PASS |  |  |
| CARS.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CAT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CAT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| CAT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,419,363,112 | 2,419,363,105 | PASS |  |  |
| CAT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CAT | MR-price | price = the last completed close | 570.49 | 570.49 | PASS |  |  |
| CAT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $570.49 needs above $10 | $570.49 needs above $10 | PASS |  |  |
| CAT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.6 needs under 10 | 11.59 needs under 10 -> ✗ | PASS |  |  |
| CAT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 29.3% below its 200-day average | 29.3% below | PASS |  |  |
| CAT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.4B traded on an average day needs above $25M | $2,419,363,112 needs above $25,000,000 | PASS |  |  |
| CAT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.59 | 11.59 | PASS |  |  |
| CAT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -29.31% | -29.31% | PASS |  |  |
| CAT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CCO.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -33.2% | TR -33.2% | PASS | LOW | the two cards divide by different roundings of the average |
| CCO.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CCO.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CCO.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CCO.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 153,052,704 | 153,052,704 | PASS |  |  |
| CCO.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CCO.TO | MR-price | price = the last completed close | 94.4 | 94.4 | PASS |  |  |
| CCO.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $94.40 needs above $10 | $94.40 needs above $10 | PASS |  |  |
| CCO.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.3 needs under 10 | 6.31 needs under 10 -> ✓ | PASS |  |  |
| CCO.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 33.2% below its 200-day average | 33.2% below | PASS |  |  |
| CCO.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $153.1M traded on an average day needs above $25M | $153,052,704 needs above $25,000,000 | PASS |  |  |
| CCO.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.31 | 6.31 | PASS |  |  |
| CCO.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -33.18% | -33.18% | PASS |  |  |
| CCO.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CEG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.2% | TR -0.2% | PASS | LOW | the two cards divide by different roundings of the average |
| CEG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CEG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| CEG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CEG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CEG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 997,745,312 | 997,745,313 | PASS |  |  |
| CEG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CEG | MR-price | price = the last completed close | 277.82 | 277.82 | PASS |  |  |
| CEG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $277.82 needs above $10 | $277.82 needs above $10 | PASS |  |  |
| CEG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 47.8 needs under 10 | 47.83 needs under 10 -> ✗ | PASS |  |  |
| CEG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.2% below its 200-day average | 0.2% below | PASS |  |  |
| CEG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $997.7M traded on an average day needs above $25M | $997,745,312 needs above $25,000,000 | PASS |  |  |
| CEG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 47.83 | 47.83 | PASS |  |  |
| CEG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.2% | -0.20% | PASS |  |  |
| CEG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CGY.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +9.3% | TR +9.3% | PASS | LOW | the two cards divide by different roundings of the average |
| CGY.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CGY.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| CGY.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CGY.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CGY.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,557,783 | 2,557,784 | PASS |  |  |
| CGY.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CGY.TO | MR-price | price = the last completed close | 86.08 | 86.08 | PASS |  |  |
| CGY.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $86.08 needs above $10 | $86.08 needs above $10 | PASS |  |  |
| CGY.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 35.3 needs under 10 | 35.28 needs under 10 -> ✗ | PASS |  |  |
| CGY.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 9.3% above its 200-day average | 9.3% above | PASS |  |  |
| CGY.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.6M traded on an average day needs above $25M | $2,557,783 needs above $25,000,000 | PASS |  |  |
| CGY.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 35.28 | 35.28 | PASS |  |  |
| CGY.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 9.32% | 9.32% | PASS |  |  |
| CGY.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CNQ.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +7.7% | TR +7.7% | PASS | LOW | the two cards divide by different roundings of the average |
| CNQ.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CNQ.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CNQ.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CNQ.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 526,085,323 | 526,085,317 | PASS |  |  |
| CNQ.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CNQ.TO | MR-price | price = the last completed close | 68.96 | 68.96 | PASS |  |  |
| CNQ.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $68.96 needs above $10 | $68.96 needs above $10 | PASS |  |  |
| CNQ.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 26.4 needs under 10 | 26.4 needs under 10 -> ✗ | PASS |  |  |
| CNQ.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 7.7% above its 200-day average | 7.7% above | PASS |  |  |
| CNQ.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $526.1M traded on an average day needs above $25M | $526,085,323 needs above $25,000,000 | PASS |  |  |
| CNQ.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 26.4 | 26.40 | PASS |  |  |
| CNQ.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 7.68% | 7.68% | PASS |  |  |
| CNQ.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CNR.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +13.2% | TR +13.2% | PASS | LOW | the two cards divide by different roundings of the average |
| CNR.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CNR.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CNR.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CNR.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 217,110,493 | 217,110,494 | PASS |  |  |
| CNR.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CNR.TO | MR-price | price = the last completed close | 182.77 | 182.77 | PASS |  |  |
| CNR.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $182.77 needs above $10 | $182.77 needs above $10 | PASS |  |  |
| CNR.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 84.2 needs under 10 | 84.24 needs under 10 -> ✗ | PASS |  |  |
| CNR.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 13.2% above its 200-day average | 13.2% above | PASS |  |  |
| CNR.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $217.1M traded on an average day needs above $25M | $217,110,493 needs above $25,000,000 | PASS |  |  |
| CNR.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 84.24 | 84.24 | PASS |  |  |
| CNR.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13.19% | 13.19% | PASS |  |  |
| CNR.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COP | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +15.3% | TR +15.3% | PASS | LOW | the two cards divide by different roundings of the average |
| COP | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COP | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| COP | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COP | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,023,843,018 | 1,030,145,366 | PASS |  |  |
| COP | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COP | MR-price | price = the last completed close | 140.52 | 140.52 | PASS |  |  |
| COP | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $140.52 needs above $10 | $140.52 needs above $10 | PASS |  |  |
| COP | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 68.2 needs under 10 | 68.24 needs under 10 -> ✗ | PASS |  |  |
| COP | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 15.3% above its 200-day average | 15.3% above | PASS |  |  |
| COP | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1B traded on an average day needs above $25M | $1,023,843,018 needs above $25,000,000 | PASS |  |  |
| COP | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPP.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.8% | TR -20.8% | PASS | LOW | the two cards divide by different roundings of the average |
| COPP.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COPP.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| COPP.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPP.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPP.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPP.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPP.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 790,606 | 790,606 | PASS |  |  |
| COPP.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COPP.TO | MR-price | price = the last completed close | 46.48 | 46.48 | PASS |  |  |
| COPP.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $46.48 needs above $10 | $46.48 needs above $10 | PASS |  |  |
| COPP.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.5 needs under 10 | 4.47 needs under 10 -> ✓ | PASS |  |  |
| COPP.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.8% below its 200-day average | 20.8% below | PASS |  |  |
| COPP.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.47 | 4.47 | PASS |  |  |
| COPP.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.82% | -20.82% | PASS |  |  |
| COPP.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.6% | TR -20.7% | PASS | LOW | the two cards divide by different roundings of the average |
| COPX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COPX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| COPX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 238,970,239 | 239,099,834 | PASS |  |  |
| COPX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COPX | MR-price | price = the last completed close | 65.51 | 65.51 | PASS |  |  |
| COPX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $65.51 needs above $10 | $65.51 needs above $10 | PASS |  |  |
| COPX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.0 needs under 10 | 3.95 needs under 10 -> ✓ | PASS |  |  |
| COPX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.6% below its 200-day average | 20.6% below | PASS |  |  |
| COPX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $239M traded on an average day needs above $25M | $238,970,239 needs above $25,000,000 | PASS |  |  |
| COPX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.95 | 3.95 | PASS |  |  |
| COPX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPZ | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| COST | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +14.1% | TR +14.0% | PASS | LOW | the two cards divide by different roundings of the average |
| COST | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COST | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| COST | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COST | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,513,681,139 | 2,513,681,135 | PASS |  |  |
| COST | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COST | MR-price | price = the last completed close | 1113.74 | 1113.74 | PASS |  |  |
| COST | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,113.74 needs above $10 | $1,113.74 needs above $10 | PASS |  |  |
| COST | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 98.8 needs under 10 | 98.79 needs under 10 -> ✗ | PASS |  |  |
| COST | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 14.1% above its 200-day average | 14.1% above | PASS |  |  |
| COST | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.5B traded on an average day needs above $25M | $2,513,681,139 needs above $25,000,000 | PASS |  |  |
| COST | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 98.79 | 98.79 | PASS |  |  |
| COST | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 14.05% | 14.05% | PASS |  |  |
| COST | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COTG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +22.6% | TR +22.6% | PASS | LOW | the two cards divide by different roundings of the average |
| COTG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COTG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| COTG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COTG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COTG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COTG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COTG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COTG | MR-price | price = the last completed close | 17.05 | 17.04 | PASS |  |  |
| COTG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $17.05 needs above $10 | $17.05 needs above $10 | PASS |  |  |
| COTG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 98.3 needs under 10 | 98.31 needs under 10 -> ✗ | PASS |  |  |
| COTG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 22.6% above its 200-day average | 22.6% above | PASS |  |  |
| COTG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1M traded on an average day needs above $25M | $1,028,329 needs above $25,000,000 | PASS |  |  |
| COTG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 98.31 | 98.31 | PASS |  |  |
| COTG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 22.6% | 22.57% | PASS |  |  |
| COTG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CSU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CSU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CSU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CSU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 206,472,881 | 206,472,881 | PASS |  |  |
| CSU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CSU.TO | MR-price | price = the last completed close | 3436.53 | 3436.53 | PASS |  |  |
| CSU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $3,436.53 needs above $10 | $3,436.53 needs above $10 | PASS |  |  |
| CSU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.8 needs under 10 | 21.82 needs under 10 -> ✗ | PASS |  |  |
| CSU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 22.4% above its 200-day average | 22.4% above | PASS |  |  |
| CSU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $206.5M traded on an average day needs above $25M | $206,472,881 needs above $25,000,000 | PASS |  |  |
| CSU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.82 | 21.82 | PASS |  |  |
| CSU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 22.35% | 22.35% | PASS |  |  |
| CSU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CVX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CVX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CVX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CVX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,805,389,494 | 1,805,389,486 | PASS |  |  |
| CVX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CVX | MR-price | price = the last completed close | 217.14 | 217.14 | PASS |  |  |
| CVX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $217.14 needs above $10 | $217.14 needs above $10 | PASS |  |  |
| CVX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 49.4 needs under 10 | 49.44 needs under 10 -> ✗ | PASS |  |  |
| CVX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 11.8% above its 200-day average | 11.8% above | PASS |  |  |
| CVX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.8B traded on an average day needs above $25M | $1,805,389,494 needs above $25,000,000 | PASS |  |  |
| CVX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 49.44 | 49.44 | PASS |  |  |
| CVX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 11.83% | 11.83% | PASS |  |  |
| CVX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DRAL | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| DRAM | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| DRIV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.1% | TR -20.2% | PASS | LOW | the two cards divide by different roundings of the average |
| DRIV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| DRIV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| DRIV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DRIV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DRIV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DRIV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DRIV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,140,751 | 1,141,268 | PASS |  |  |
| DRIV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DRIV | MR-price | price = the last completed close | 27.35 | 27.35 | PASS |  |  |
| DRIV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $27.35 needs above $10 | $27.35 needs above $10 | PASS |  |  |
| DRIV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.4 needs under 10 | 6.38 needs under 10 -> ✓ | PASS |  |  |
| DRIV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.1% below its 200-day average | 20.1% below | PASS |  |  |
| DRIV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.1M traded on an average day needs above $25M | $1,140,751 needs above $25,000,000 | PASS |  |  |
| DRIV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.38 | 6.39 | PASS |  |  |
| DRIV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.12% | -20.21% | PASS |  |  |
| DRIV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DUK | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| DUK | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| DUK | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DUK | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 597,326,340 | 592,945,535 | PASS |  |  |
| DUK | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DUK | MR-price | price = the last completed close | 130.59 | 130.59 | PASS |  |  |
| DUK | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $130.59 needs above $10 | $130.59 needs above $10 | PASS |  |  |
| DUK | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 94.4 needs under 10 | 94.43 needs under 10 -> ✗ | PASS |  |  |
| DUK | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 4.6% above its 200-day average | 4.6% above | PASS |  |  |
| DUK | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $597.3M traded on an average day needs above $25M | $597,326,340 needs above $25,000,000 | PASS |  |  |
| DUK | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ELIL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +52.7% | TR +52.7% | PASS | LOW | the two cards divide by different roundings of the average |
| ELIL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ELIL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| ELIL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ELIL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ELIL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,719,075 | 2,719,044 | PASS |  |  |
| ELIL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ELIL | MR-price | price = the last completed close | 41.12 | 41.12 | PASS |  |  |
| ELIL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $41.12 needs above $10 | $41.12 needs above $10 | PASS |  |  |
| ELIL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 41.1 needs under 10 | 41.07 needs under 10 -> ✗ | PASS |  |  |
| ELIL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 52.7% above its 200-day average | 52.7% above | PASS |  |  |
| ELIL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,719,075 needs above $25,000,000 | PASS |  |  |
| ELIL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 41.07 | 41.22 | PASS |  |  |
| ELIL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 52.66% | 52.68% | PASS |  |  |
| ELIL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| EQIX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| EQIX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| EQIX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| EQIX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 719,156,874 | 718,988,746 | PASS |  |  |
| EQIX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| EQIX | MR-price | price = the last completed close | 1043.06 | 1043.06 | PASS |  |  |
| EQIX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,043.06 needs above $10 | $1,043.06 needs above $10 | PASS |  |  |
| EQIX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 19.8 needs under 10 | 19.83 needs under 10 -> ✗ | PASS |  |  |
| EQIX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.9% above its 200-day average | 1.9% above | PASS |  |  |
| EQIX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $719.2M traded on an average day needs above $25M | $719,156,874 needs above $25,000,000 | PASS |  |  |
| EQIX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 19.83 | 19.83 | PASS |  |  |
| EQIX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ETN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -15.3% | TR -15.3% | PASS | LOW | the two cards divide by different roundings of the average |
| ETN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ETN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ETN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ETN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,159,606,556 | 1,159,606,557 | PASS |  |  |
| ETN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ETN | MR-price | price = the last completed close | 336.88 | 336.88 | PASS |  |  |
| ETN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $336.88 needs above $10 | $336.88 needs above $10 | PASS |  |  |
| ETN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.5 needs under 10 | 7.47 needs under 10 -> ✓ | PASS |  |  |
| ETN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 15.3% below its 200-day average | 15.3% below | PASS |  |  |
| ETN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.2B traded on an average day needs above $25M | $1,159,606,556 needs above $25,000,000 | PASS |  |  |
| ETN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.47 | 7.47 | PASS |  |  |
| ETN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -15.29% | -15.29% | PASS |  |  |
| ETN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| FCX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -15.3% | TR -15.3% | PASS | LOW | the two cards divide by different roundings of the average |
| FCX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| FCX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| FCX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FCX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 779,664,311 | 779,664,311 | PASS |  |  |
| FCX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| FCX | MR-price | price = the last completed close | 55.19 | 55.19 | PASS |  |  |
| FCX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $55.19 needs above $10 | $55.19 needs above $10 | PASS |  |  |
| FCX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.2 needs under 10 | 6.17 needs under 10 -> ✓ | PASS |  |  |
| FCX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 15.3% below its 200-day average | 15.3% below | PASS |  |  |
| FCX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $779.7M traded on an average day needs above $25M | $779,664,311 needs above $25,000,000 | PASS |  |  |
| FCX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.17 | 6.17 | PASS |  |  |
| FCX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -15.32% | -15.32% | PASS |  |  |
| FCX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| FINN.NE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +6.8% | TR +6.9% | PASS | LOW | the two cards divide by different roundings of the average |
| FINN.NE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| FINN.NE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| FINN.NE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FINN.NE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FINN.NE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FINN.NE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FINN.NE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 10,675,329 | 10,675,330 | PASS |  |  |
| FINN.NE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| FINN.NE | MR-price | price = the last completed close | 32.1 | 32.1 | PASS |  |  |
| FINN.NE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $32.10 needs above $10 | $32.10 needs above $10 | PASS |  |  |
| FINN.NE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.7 needs under 10 | 12.69 needs under 10 -> ✗ | PASS |  |  |
| FINN.NE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 6.8% above its 200-day average | 6.8% above | PASS |  |  |
| FINN.NE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $10.7M traded on an average day needs above $25M | $10,675,329 needs above $25,000,000 | PASS |  |  |
| FINN.NE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.69 | 12.69 | PASS |  |  |
| FINN.NE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 6.84% | 6.84% | PASS |  |  |
| FINN.NE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GDX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.8% | TR -11.8% | PASS | LOW | the two cards divide by different roundings of the average |
| GDX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GDX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GDX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,956,933,288 | 1,957,033,586 | PASS |  |  |
| GDX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GDX | MR-price | price = the last completed close | 78.95 | 78.95 | PASS |  |  |
| GDX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $78.95 needs above $10 | $78.95 needs above $10 | PASS |  |  |
| GDX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.4 needs under 10 | 4.38 needs under 10 -> ✓ | PASS |  |  |
| GDX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.8% below its 200-day average | 11.8% below | PASS |  |  |
| GDX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2B traded on an average day needs above $25M | $1,956,933,288 needs above $25,000,000 | PASS |  |  |
| GDX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.38 | 4.38 | PASS |  |  |
| GDX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.79% | -11.79% | PASS |  |  |
| GDX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GDXU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -32.4% | TR -32.4% | PASS | LOW | the two cards divide by different roundings of the average |
| GDXU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GDXU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| GDXU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDXU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDXU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 7,728,957 | 7,728,958 | PASS |  |  |
| GDXU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GDXU.TO | MR-price | price = the last completed close | 24.3 | 24.3 | PASS |  |  |
| GDXU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $24.30 needs above $10 | $24.30 needs above $10 | PASS |  |  |
| GDXU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.6 needs under 10 | 4.57 needs under 10 -> ✓ | PASS |  |  |
| GDXU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 32.4% below its 200-day average | 32.4% below | PASS |  |  |
| GDXU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $7.7M traded on an average day needs above $25M | $7,728,957 needs above $25,000,000 | PASS |  |  |
| GDXU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.57 | 4.57 | PASS |  |  |
| GDXU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -32.43% | -32.43% | PASS |  |  |
| GDXU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| GE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,720,552,103 | 1,720,552,098 | PASS |  |  |
| GE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GE | MR-price | price = the last completed close | 325.18 | 325.18 | PASS |  |  |
| GE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $325.18 needs above $10 | $325.18 needs above $10 | PASS |  |  |
| GE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.7 needs under 10 | 15.67 needs under 10 -> ✗ | PASS |  |  |
| GE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.6% above its 200-day average | 0.6% above | PASS |  |  |
| GE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.7B traded on an average day needs above $25M | $1,720,552,103 needs above $25,000,000 | PASS |  |  |
| GE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.67 | 15.67 | PASS |  |  |
| GE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.58% | 0.58% | PASS |  |  |
| GE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GEV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -19.8% | TR -19.8% | PASS | LOW | the two cards divide by different roundings of the average |
| GEV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GEV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GEV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,620,076,021 | 3,616,230,240 | PASS |  |  |
| GEV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GEV | MR-price | price = the last completed close | 763.57 | 763.57 | PASS |  |  |
| GEV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $763.57 needs above $10 | $763.57 needs above $10 | PASS |  |  |
| GEV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.5 needs under 10 | 10.48 needs under 10 -> ✗ | PASS |  |  |
| GEV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 19.8% below its 200-day average | 19.8% below | PASS |  |  |
| GEV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3.6B traded on an average day needs above $25M | $3,620,076,021 needs above $25,000,000 | PASS |  |  |
| GEV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.48 | 10.48 | PASS |  |  |
| GEV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -19.79% | -19.72% | PASS |  |  |
| GEV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GEV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GEV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| GEV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,604,628 | 6,604,665 | PASS |  |  |
| GEV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GEV.TO | MR-price | price = the last completed close | 51.03 | 51.03 | PASS |  |  |
| GEV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $51.03 needs above $10 | $51.03 needs above $10 | PASS |  |  |
| GEV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.4 needs under 10 | 10.38 needs under 10 -> ✗ | PASS |  |  |
| GEV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.4% below its 200-day average | 20.4% below | PASS |  |  |
| GEV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $6.6M traded on an average day needs above $25M | $6,604,628 needs above $25,000,000 | PASS |  |  |
| GEV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.38 | 10.38 | PASS |  |  |
| GEV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.36% | -20.36% | PASS |  |  |
| GEV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GGLL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GGLL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GGLL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GGLL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GGLL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 197,744,471 | 197,655,978 | PASS |  |  |
| GGLL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GGLL | MR-price | price = the last completed close | 64.83 | 64.83 | PASS |  |  |
| GGLL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $64.83 needs above $10 | $64.83 needs above $10 | PASS |  |  |
| GGLL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.8 needs under 10 | 13.84 needs under 10 -> ✗ | PASS |  |  |
| GGLL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 36.6% below its 200-day average | 36.6% below | PASS |  |  |
| GGLL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $197.7M traded on an average day needs above $25M | $197,744,471 needs above $25,000,000 | PASS |  |  |
| GGLL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.84 | 13.84 | PASS |  |  |
| GGLL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GIB-A.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +18.0% | TR +18.0% | PASS | LOW | the two cards divide by different roundings of the average |
| GIB-A.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-13 | 2026-11-13 | PASS |  |  |
| GIB-A.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| GIB-A.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GIB-A.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 76,331,030 | 76,331,030 | PASS |  |  |
| GIB-A.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GIB-A.TO | MR-price | price = the last completed close | 117.8 | 117.8 | PASS |  |  |
| GIB-A.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $117.80 needs above $10 | $117.80 needs above $10 | PASS |  |  |
| GIB-A.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 80.4 needs under 10 | 80.41 needs under 10 -> ✗ | PASS |  |  |
| GIB-A.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 18.0% above its 200-day average | 18.0% above | PASS |  |  |
| GIB-A.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $76.3M traded on an average day needs above $25M | $76,331,030 needs above $25,000,000 | PASS |  |  |
| GIB-A.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 80.41 | 80.41 | PASS |  |  |
| GIB-A.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 18.02% | 18.02% | PASS |  |  |
| GIB-A.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GOOGL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -16.0% | TR -16.0% | PASS | LOW | the two cards divide by different roundings of the average |
| GOOGL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GOOGL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GOOGL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GOOGL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GOOGL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,276,800,531 | 12,276,800,482 | PASS |  |  |
| GOOGL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GOOGL | MR-price | price = the last completed close | 283.72 | 283.72 | PASS |  |  |
| GOOGL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $283.72 needs above $10 | $283.72 needs above $10 | PASS |  |  |
| GOOGL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.2 needs under 10 | 14.17 needs under 10 -> ✗ | PASS |  |  |
| GOOGL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 16.0% below its 200-day average | 16.0% below | PASS |  |  |
| GOOGL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.3B traded on an average day needs above $25M | $12,276,800,531 needs above $25,000,000 | PASS |  |  |
| GOOGL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14.17 | 14.17 | PASS |  |  |
| GOOGL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -16.04% | -16.04% | PASS |  |  |
| GOOGL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GRID | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GRID | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GRID | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GRID | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GRID | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 111,861,140 | 111,861,141 | PASS |  |  |
| GRID | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GRID | MR-price | price = the last completed close | 156.14 | 156.14 | PASS |  |  |
| GRID | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $156.14 needs above $10 | $156.14 needs above $10 | PASS |  |  |
| GRID | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.1 needs under 10 | 11.06 needs under 10 -> ✗ | PASS |  |  |
| GRID | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 12.3% below its 200-day average | 12.3% below | PASS |  |  |
| GRID | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $111.9M traded on an average day needs above $25M | $111,861,140 needs above $25,000,000 | PASS |  |  |
| GRID | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.06 | 11.06 | PASS |  |  |
| GRID | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +4.5% | TR +4.5% | PASS | LOW | the two cards divide by different roundings of the average |
| HD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| HD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| HD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,530,681,895 | 1,530,681,896 | PASS |  |  |
| HD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HD | MR-price | price = the last completed close | 347.51 | 347.51 | PASS |  |  |
| HD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $347.51 needs above $10 | $347.51 needs above $10 | PASS |  |  |
| HD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.8 needs under 10 | 22.78 needs under 10 -> ✗ | PASS |  |  |
| HD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 4.5% above its 200-day average | 4.5% above | PASS |  |  |
| HD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.5B traded on an average day needs above $25M | $1,530,681,895 needs above $25,000,000 | PASS |  |  |
| HD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.78 | 22.78 | PASS |  |  |
| HD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 4.51% | 4.51% | PASS |  |  |
| HD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HURA.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -29.4% | TR -29.4% | PASS | LOW | the two cards divide by different roundings of the average |
| HURA.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| HURA.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| HURA.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HURA.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HURA.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HURA.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HURA.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 507,990 | 507,990 | PASS |  |  |
| HURA.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HURA.TO | MR-price | price = the last completed close | 37.54 | 37.54 | PASS |  |  |
| HURA.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $37.54 needs above $10 | $37.54 needs above $10 | PASS |  |  |
| HURA.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.9 needs under 10 | 6.9 needs under 10 -> ✓ | PASS |  |  |
| HURA.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 29.4% below its 200-day average | 29.4% below | PASS |  |  |
| HURA.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.9 | 6.90 | PASS |  |  |
| HURA.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -29.41% | -29.41% | PASS |  |  |
| HURA.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HXQ.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| HXQ.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| HXQ.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HXQ.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,310,089 | 5,310,090 | PASS |  |  |
| HXQ.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HXQ.TO | MR-price | price = the last completed close | 111.87 | 111.87 | PASS |  |  |
| HXQ.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $111.87 needs above $10 | $111.87 needs above $10 | PASS |  |  |
| HXQ.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.7 needs under 10 | 12.72 needs under 10 -> ✗ | PASS |  |  |
| HXQ.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.3% below its 200-day average | 0.3% below | PASS |  |  |
| HXQ.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $5.3M traded on an average day needs above $25M | $5,310,089 needs above $25,000,000 | PASS |  |  |
| HXQ.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.72 | 12.72 | PASS |  |  |
| HXQ.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.28% | -0.28% | PASS |  |  |
| HXQ.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| JNJ | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +13.0% | TR +13.0% | PASS | LOW | the two cards divide by different roundings of the average |
| JNJ | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| JNJ | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| JNJ | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| JNJ | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,027,970,533 | 2,027,201,458 | PASS |  |  |
| JNJ | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| JNJ | MR-price | price = the last completed close | 282.55 | 282.55 | PASS |  |  |
| JNJ | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $282.55 needs above $10 | $282.55 needs above $10 | PASS |  |  |
| JNJ | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 39.3 needs under 10 | 39.25 needs under 10 -> ✗ | PASS |  |  |
| JNJ | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 13.0% above its 200-day average | 13.0% above | PASS |  |  |
| JNJ | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2B traded on an average day needs above $25M | $2,027,970,533 needs above $25,000,000 | PASS |  |  |
| JNJ | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 39.25 | 39.25 | PASS |  |  |
| JNJ | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| JPM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +4.1% | TR +4.1% | PASS | LOW | the two cards divide by different roundings of the average |
| JPM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| JPM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| JPM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| JPM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,185,001,440 | 2,185,001,445 | PASS |  |  |
| JPM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| JPM | MR-price | price = the last completed close | 338.21 | 338.21 | PASS |  |  |
| JPM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $338.21 needs above $10 | $338.21 needs above $10 | PASS |  |  |
| JPM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 20.6 needs under 10 | 20.57 needs under 10 -> ✗ | PASS |  |  |
| JPM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 4.1% above its 200-day average | 4.1% above | PASS |  |  |
| JPM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.2B traded on an average day needs above $25M | $2,185,001,440 needs above $25,000,000 | PASS |  |  |
| JPM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 20.57 | 20.57 | PASS |  |  |
| JPM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 4.06% | 4.06% | PASS |  |  |
| JPM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| KEYS | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.0% | TR -11.0% | PASS | LOW | the two cards divide by different roundings of the average |
| KEYS | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| KEYS | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| KEYS | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| KEYS | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| KEYS | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 456,116,118 | 456,116,120 | PASS |  |  |
| KEYS | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| KEYS | MR-price | price = the last completed close | 285.63 | 285.63 | PASS |  |  |
| KEYS | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $285.63 needs above $10 | $285.63 needs above $10 | PASS |  |  |
| KEYS | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.2 needs under 10 | 14.22 needs under 10 -> ✗ | PASS |  |  |
| KEYS | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.0% below its 200-day average | 11.0% below | PASS |  |  |
| KEYS | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $456.1M traded on an average day needs above $25M | $456,116,118 needs above $25,000,000 | PASS |  |  |
| KEYS | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14.22 | 14.22 | PASS |  |  |
| KEYS | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -10.97% | -10.97% | PASS |  |  |
| KEYS | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| LIN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +5.3% | TR +5.3% | PASS | LOW | the two cards divide by different roundings of the average |
| LIN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| LIN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| LIN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| LIN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,065,816,205 | 1,065,162,015 | PASS |  |  |
| LIN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| LIN | MR-price | price = the last completed close | 523.46 | 523.46 | PASS |  |  |
| LIN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $523.46 needs above $10 | $523.46 needs above $10 | PASS |  |  |
| LIN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 41.8 needs under 10 | 41.78 needs under 10 -> ✗ | PASS |  |  |
| LIN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 5.3% above its 200-day average | 5.3% above | PASS |  |  |
| LIN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,065,816,205 needs above $25,000,000 | PASS |  |  |
| LIN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 41.78 | 41.78 | PASS |  |  |
| LIN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| LLY | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +28.8% | TR +28.8% | PASS | LOW | the two cards divide by different roundings of the average |
| LLY | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| LLY | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| LLY | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| LLY | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 4,189,339,265 | 4,189,339,265 | PASS |  |  |
| LLY | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| LLY | MR-price | price = the last completed close | 1431.67 | 1431.67 | PASS |  |  |
| LLY | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,431.67 needs above $10 | $1,431.67 needs above $10 | PASS |  |  |
| LLY | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 44.4 needs under 10 | 44.35 needs under 10 -> ✗ | PASS |  |  |
| LLY | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 28.8% above its 200-day average | 28.8% above | PASS |  |  |
| LLY | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $4.2B traded on an average day needs above $25M | $4,189,339,265 needs above $25,000,000 | PASS |  |  |
| LLY | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 44.35 | 44.35 | PASS |  |  |
| LLY | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 28.83% | 28.83% | PASS |  |  |
| LLY | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MDA.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -10.3% | TR -10.3% | PASS | LOW | the two cards divide by different roundings of the average |
| MDA.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MDA.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| MDA.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MDA.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 60,872,176 | 60,872,177 | PASS |  |  |
| MDA.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MDA.TO | MR-price | price = the last completed close | 40.08 | 40.08 | PASS |  |  |
| MDA.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $40.08 needs above $10 | $40.08 needs above $10 | PASS |  |  |
| MDA.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.6 needs under 10 | 9.57 needs under 10 -> ✓ | PASS |  |  |
| MDA.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 10.3% below its 200-day average | 10.3% below | PASS |  |  |
| MDA.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $60.9M traded on an average day needs above $25M | $60,872,176 needs above $25,000,000 | PASS |  |  |
| MDA.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.57 | 9.57 | PASS |  |  |
| MDA.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -10.32% | -10.32% | PASS |  |  |
| MDA.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| META | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.6% | TR -0.6% | PASS | LOW | the two cards divide by different roundings of the average |
| META | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| META | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| META | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| META | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| META | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,879,787,491 | 14,879,787,462 | PASS |  |  |
| META | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| META | MR-price | price = the last completed close | 626.41 | 626.41 | PASS |  |  |
| META | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $626.41 needs above $10 | $626.41 needs above $10 | PASS |  |  |
| META | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 35.6 needs under 10 | 35.63 needs under 10 -> ✗ | PASS |  |  |
| META | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.6% below its 200-day average | 0.6% below | PASS |  |  |
| META | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $14.9B traded on an average day needs above $25M | $14,879,787,491 needs above $25,000,000 | PASS |  |  |
| META | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 35.63 | 35.63 | PASS |  |  |
| META | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.62% | -0.62% | PASS |  |  |
| META | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| METU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -13.3% | TR -13.3% | PASS | LOW | the two cards divide by different roundings of the average |
| METU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| METU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| METU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| METU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| METU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 113,342,178 | 113,342,179 | PASS |  |  |
| METU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| METU | MR-price | price = the last completed close | 22.15 | 22.15 | PASS |  |  |
| METU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $22.15 needs above $10 | $22.15 needs above $10 | PASS |  |  |
| METU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 35.2 needs under 10 | 35.23 needs under 10 -> ✗ | PASS |  |  |
| METU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 13.3% below its 200-day average | 13.3% below | PASS |  |  |
| METU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $113.3M traded on an average day needs above $25M | $113,342,178 needs above $25,000,000 | PASS |  |  |
| METU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 35.23 | 35.23 | PASS |  |  |
| METU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -13.26% | -13.26% | PASS |  |  |
| METU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MRVL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -22.4% | TR -22.4% | PASS | LOW | the two cards divide by different roundings of the average |
| MRVL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MRVL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| MRVL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MRVL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MRVL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,443,865,806 | 5,443,865,806 | PASS |  |  |
| MRVL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MRVL | MR-price | price = the last completed close | 145.36 | 145.36 | PASS |  |  |
| MRVL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $145.36 needs above $10 | $145.36 needs above $10 | PASS |  |  |
| MRVL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.3 needs under 10 | 12.34 needs under 10 -> ✗ | PASS |  |  |
| MRVL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 22.4% below its 200-day average | 22.4% below | PASS |  |  |
| MRVL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.4B traded on an average day needs above $25M | $5,443,865,806 needs above $25,000,000 | PASS |  |  |
| MRVL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.34 | 12.34 | PASS |  |  |
| MRVL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -22.4% | -22.40% | PASS |  |  |
| MRVL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MSFT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +17.2% | TR +17.2% | PASS | LOW | the two cards divide by different roundings of the average |
| MSFT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MSFT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| MSFT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MSFT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,219,865,706 | 14,219,865,832 | PASS |  |  |
| MSFT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MSFT | MR-price | price = the last completed close | 517.99 | 517.99 | PASS |  |  |
| MSFT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $517.99 needs above $10 | $517.99 needs above $10 | PASS |  |  |
| MSFT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.4 needs under 10 | 15.37 needs under 10 -> ✗ | PASS |  |  |
| MSFT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 17.2% above its 200-day average | 17.2% above | PASS |  |  |
| MSFT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $14.2B traded on an average day needs above $25M | $14,219,865,706 needs above $25,000,000 | PASS |  |  |
| MSFT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.37 | 15.37 | PASS |  |  |
| MSFT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 17.23% | 17.23% | PASS |  |  |
| MSFT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MSFU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MSFU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| MSFU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MSFU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 98,765,666 | 98,866,428 | PASS |  |  |
| MSFU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MSFU | MR-price | price = the last completed close | 39.17 | 39.17 | PASS |  |  |
| MSFU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $39.17 needs above $10 | $39.17 needs above $10 | PASS |  |  |
| MSFU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.6 needs under 10 | 15.61 needs under 10 -> ✗ | PASS |  |  |
| MSFU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 26.3% above its 200-day average | 26.3% above | PASS |  |  |
| MSFU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $98.8M traded on an average day needs above $25M | $98,765,666 needs above $25,000,000 | PASS |  |  |
| MSFU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.61 | 15.61 | PASS |  |  |
| MSFU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MTRX.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MTRX.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| MTRX.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MTRX.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MTRX.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MTRX.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MTRX.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 526,345 | 526,347 | PASS |  |  |
| MTRX.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MTRX.TO | MR-price | price = the last completed close | 29.24 | 29.24 | PASS |  |  |
| MTRX.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $29.24 needs above $10 | $29.24 needs above $10 | PASS |  |  |
| MTRX.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.5 needs under 10 | 9.47 needs under 10 -> ✓ | PASS |  |  |
| MTRX.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.9% below its 200-day average | 14.9% below | PASS |  |  |
| MTRX.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.47 | 9.47 | PASS |  |  |
| MTRX.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.87% | -14.87% | PASS |  |  |
| MTRX.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -6.8% | TR -6.8% | PASS | LOW | the two cards divide by different roundings of the average |
| MU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| MU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 79,117,921 | 79,117,921 | PASS |  |  |
| MU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MU.TO | MR-price | price = the last completed close | 31.43 | 31.43 | PASS |  |  |
| MU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $31.43 needs above $10 | $31.43 needs above $10 | PASS |  |  |
| MU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.6 needs under 10 | 14.63 needs under 10 -> ✗ | PASS |  |  |
| MU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 6.8% below its 200-day average | 6.8% below | PASS |  |  |
| MU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $79.1M traded on an average day needs above $25M | $79,117,921 needs above $25,000,000 | PASS |  |  |
| MU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14.63 | 14.63 | PASS |  |  |
| MU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -6.85% | -6.85% | PASS |  |  |
| MU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NEE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -2.3% | TR -2.3% | PASS | LOW | the two cards divide by different roundings of the average |
| NEE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NEE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| NEE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,131,866,055 | 1,131,748,945 | PASS |  |  |
| NEE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NEE | MR-price | price = the last completed close | 85.34 | 85.34 | PASS |  |  |
| NEE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $85.34 needs above $10 | $85.34 needs above $10 | PASS |  |  |
| NEE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 40.0 needs under 10 | 39.97 needs under 10 -> ✗ | PASS |  |  |
| NEE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 2.3% below its 200-day average | 2.3% below | PASS |  |  |
| NEE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,131,866,055 needs above $25,000,000 | PASS |  |  |
| NEE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 39.97 | 39.97 | PASS |  |  |
| NEE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NEM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.6% | TR -1.6% | PASS | LOW | the two cards divide by different roundings of the average |
| NEM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NEM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NEM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 802,108,176 | 802,108,177 | PASS |  |  |
| NEM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NEM | MR-price | price = the last completed close | 110.31 | 110.31 | PASS |  |  |
| NEM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $110.31 needs above $10 | $110.31 needs above $10 | PASS |  |  |
| NEM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.7 needs under 10 | 8.71 needs under 10 -> ✓ | PASS |  |  |
| NEM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.6% below its 200-day average | 1.6% below | PASS |  |  |
| NEM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $802.1M traded on an average day needs above $25M | $802,108,176 needs above $25,000,000 | PASS |  |  |
| NEM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8.71 | 8.71 | PASS |  |  |
| NEM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.63% | -1.63% | PASS |  |  |
| NEM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NFLX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -24.4% | TR -24.4% | PASS | LOW | the two cards divide by different roundings of the average |
| NFLX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NFLX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NFLX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFLX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,944,852,337 | 2,944,852,337 | PASS |  |  |
| NFLX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NFLX | MR-price | price = the last completed close | 60.75 | 60.75 | PASS |  |  |
| NFLX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $60.75 needs above $10 | $60.75 needs above $10 | PASS |  |  |
| NFLX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.9 needs under 10 | 7.93 needs under 10 -> ✓ | PASS |  |  |
| NFLX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 24.4% below its 200-day average | 24.4% below | PASS |  |  |
| NFLX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.9B traded on an average day needs above $25M | $2,944,852,337 needs above $25,000,000 | PASS |  |  |
| NFLX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.93 | 7.93 | PASS |  |  |
| NFLX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -24.43% | -24.43% | PASS |  |  |
| NFLX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NFXL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -50.1% | TR -50.1% | PASS | LOW | the two cards divide by different roundings of the average |
| NFXL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NFXL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| NFXL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFXL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFXL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 21,373,234 | 21,373,234 | PASS |  |  |
| NFXL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NFXL | MR-price | price = the last completed close | 10.22 | 10.22 | PASS |  |  |
| NFXL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $10.22 needs above $10 | $10.22 needs above $10 | PASS |  |  |
| NFXL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.8 needs under 10 | 7.85 needs under 10 -> ✓ | PASS |  |  |
| NFXL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 50.1% below its 200-day average | 50.1% below | PASS |  |  |
| NFXL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $21.4M traded on an average day needs above $25M | $21,373,234 needs above $25,000,000 | PASS |  |  |
| NFXL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.85 | 7.85 | PASS |  |  |
| NFXL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -50.11% | -50.11% | PASS |  |  |
| NFXL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NTR.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NTR.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 146,082,099 | 146,082,101 | PASS |  |  |
| NTR.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| NTR.TO | MR-price | price = the last completed close | 98.62 | 98.62 | PASS |  |  |
| NTR.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $98.62 needs above $10 | $98.62 needs above $10 | PASS |  |  |
| NTR.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.1 needs under 10 | 4.06 needs under 10 -> ✓ | PASS |  |  |
| NTR.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.9% above its 200-day average | 0.9% above | PASS |  |  |
| NTR.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $146.1M traded on an average day needs above $25M | $146,082,099 needs above $25,000,000 | PASS |  |  |
| NTR.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.06 | 4.06 | PASS |  |  |
| NTR.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.92% | 0.92% | PASS |  |  |
| NTR.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.5% | TR -23.5% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NVDA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 40,055,123,308 | 40,055,122,882 | PASS |  |  |
| NVDA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDA | MR-price | price = the last completed close | 156.14 | 156.14 | PASS |  |  |
| NVDA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $156.14 needs above $10 | $156.14 needs above $10 | PASS |  |  |
| NVDA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.8 needs under 10 | 5.78 needs under 10 -> ✓ | PASS |  |  |
| NVDA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.5% below its 200-day average | 23.5% below | PASS |  |  |
| NVDA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $40.1B traded on an average day needs above $25M | $40,055,123,308 needs above $25,000,000 | PASS |  |  |
| NVDA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.78 | 5.78 | PASS |  |  |
| NVDA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.47% | -23.47% | PASS |  |  |
| NVDA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.2% | TR -23.2% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NVDL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 577,221,155 | 577,221,155 | PASS |  |  |
| NVDL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDL | MR-price | price = the last completed close | 16.35 | 16.35 | PASS |  |  |
| NVDL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $16.35 needs above $10 | $16.35 needs above $10 | PASS |  |  |
| NVDL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.9 needs under 10 | 5.91 needs under 10 -> ✓ | PASS |  |  |
| NVDL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.2% below its 200-day average | 23.2% below | PASS |  |  |
| NVDL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $577.2M traded on an average day needs above $25M | $577,221,155 needs above $25,000,000 | PASS |  |  |
| NVDL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.91 | 5.91 | PASS |  |  |
| NVDL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.22% | -23.22% | PASS |  |  |
| NVDL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ONTO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -24.3% | TR -24.3% | PASS | LOW | the two cards divide by different roundings of the average |
| ONTO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ONTO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| ONTO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ONTO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ONTO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 241,495,911 | 241,495,912 | PASS |  |  |
| ONTO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ONTO | MR-price | price = the last completed close | 196.77 | 196.77 | PASS |  |  |
| ONTO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $196.77 needs above $10 | $196.77 needs above $10 | PASS |  |  |
| ONTO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.5 needs under 10 | 22.52 needs under 10 -> ✗ | PASS |  |  |
| ONTO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 24.3% below its 200-day average | 24.3% below | PASS |  |  |
| ONTO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $241.5M traded on an average day needs above $25M | $241,495,911 needs above $25,000,000 | PASS |  |  |
| ONTO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.52 | 22.52 | PASS |  |  |
| ONTO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -24.31% | -24.31% | PASS |  |  |
| ONTO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ORBX.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| ORCL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -22.6% | TR -22.6% | PASS | LOW | the two cards divide by different roundings of the average |
| ORCL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ORCL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| ORCL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ORCL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ORCL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,282,428,391 | 5,282,428,391 | PASS |  |  |
| ORCL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ORCL | MR-price | price = the last completed close | 119.09 | 119.09 | PASS |  |  |
| ORCL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $119.09 needs above $10 | $119.09 needs above $10 | PASS |  |  |
| ORCL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.9 needs under 10 | 15.87 needs under 10 -> ✗ | PASS |  |  |
| ORCL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 22.6% below its 200-day average | 22.6% below | PASS |  |  |
| ORCL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.3B traded on an average day needs above $25M | $5,282,428,391 needs above $25,000,000 | PASS |  |  |
| ORCL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.87 | 15.87 | PASS |  |  |
| ORCL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -22.61% | -22.61% | PASS |  |  |
| ORCL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| PG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| PG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,695,604,430 | 1,695,602,953 | PASS |  |  |
| PG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PG | MR-price | price = the last completed close | 173.02 | 173.02 | PASS |  |  |
| PG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $173.02 needs above $10 | $173.02 needs above $10 | PASS |  |  |
| PG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 96.5 needs under 10 | 96.54 needs under 10 -> ✗ | PASS |  |  |
| PG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 16.8% above its 200-day average | 16.8% above | PASS |  |  |
| PG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.7B traded on an average day needs above $25M | $1,695,604,430 needs above $25,000,000 | PASS |  |  |
| PG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 96.54 | 96.54 | PASS |  |  |
| PG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 16.81% | 16.81% | PASS |  |  |
| PG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PLD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -7.4% | TR -7.4% | PASS | LOW | the two cards divide by different roundings of the average |
| PLD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| PLD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| PLD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PLD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PLD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 468,398,772 | 468,398,773 | PASS |  |  |
| PLD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PLD | MR-price | price = the last completed close | 127.6 | 127.6 | PASS |  |  |
| PLD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $127.60 needs above $10 | $127.60 needs above $10 | PASS |  |  |
| PLD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.7 needs under 10 | 10.74 needs under 10 -> ✗ | PASS |  |  |
| PLD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 7.4% below its 200-day average | 7.4% below | PASS |  |  |
| PLD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $468.4M traded on an average day needs above $25M | $468,398,772 needs above $25,000,000 | PASS |  |  |
| PLD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.74 | 10.74 | PASS |  |  |
| PLD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.41% | -7.41% | PASS |  |  |
| PLD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PNG.V | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -51.4% | TR -51.4% | PASS | LOW | the two cards divide by different roundings of the average |
| PNG.V | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| PNG.V | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| PNG.V | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PNG.V | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,630,882 | 3,630,882 | PASS |  |  |
| PNG.V | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PNG.V | MR-price | price = the last completed close | 3.22 | 3.22 | PASS |  |  |
| PNG.V | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $3.22 needs above $10 | $3.22 needs above $10 | PASS |  |  |
| PNG.V | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.1 needs under 10 | 5.1 needs under 10 -> ✓ | PASS |  |  |
| PNG.V | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 51.4% below its 200-day average | 51.4% below | PASS |  |  |
| PNG.V | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $3.6M traded on an average day needs above $25M | $3,630,882 needs above $25,000,000 | PASS |  |  |
| PNG.V | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.1 | 5.10 | PASS |  |  |
| PNG.V | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -51.41% | -51.41% | PASS |  |  |
| PNG.V | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QCOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.0% | TR -1.0% | PASS | LOW | the two cards divide by different roundings of the average |
| QCOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| QCOM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| QCOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QCOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QCOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,353,875,132 | 2,353,875,132 | PASS |  |  |
| QCOM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QCOM | MR-price | price = the last completed close | 168.52 | 168.52 | PASS |  |  |
| QCOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $168.52 needs above $10 | $168.52 needs above $10 | PASS |  |  |
| QCOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.7 needs under 10 | 13.65 needs under 10 -> ✗ | PASS |  |  |
| QCOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.0% below its 200-day average | 1.0% below | PASS |  |  |
| QCOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.4B traded on an average day needs above $25M | $2,353,875,132 needs above $25,000,000 | PASS |  |  |
| QCOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.65 | 13.65 | PASS |  |  |
| QCOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.04% | -1.04% | PASS |  |  |
| QCOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QPUX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| QPUX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| QPUX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QPUX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,593,621 | 1,593,596 | PASS |  |  |
| QPUX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QPUX | MR-price | price = the last completed close | 3.59 | 3.59 | PASS |  |  |
| QPUX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $3.59 needs above $10 | $3.59 needs above $10 | PASS |  |  |
| QPUX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.8 needs under 10 | 3.81 needs under 10 -> ✓ | PASS |  |  |
| QPUX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 82.5% below its 200-day average | 82.5% below | PASS |  |  |
| QPUX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.6M traded on an average day needs above $25M | $1,593,621 needs above $25,000,000 | PASS |  |  |
| QPUX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.81 | 3.81 | PASS |  |  |
| QPUX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -82.5% | -82.50% | PASS |  |  |
| QPUX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QTUM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| QTUM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| QTUM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QTUM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 50,004,294 | 50,004,295 | PASS |  |  |
| QTUM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QTUM | MR-price | price = the last completed close | 124.47 | 124.47 | PASS |  |  |
| QTUM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $124.47 needs above $10 | $124.47 needs above $10 | PASS |  |  |
| QTUM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.8 needs under 10 | 9.85 needs under 10 -> ✓ | PASS |  |  |
| QTUM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.8% below its 200-day average | 9.8% below | PASS |  |  |
| QTUM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $50M traded on an average day needs above $25M | $50,004,294 needs above $25,000,000 | PASS |  |  |
| QTUM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.85 | 9.85 | PASS |  |  |
| QTUM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.75% | -9.75% | PASS |  |  |
| QTUM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RBOT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| RBOT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| RBOT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RBOT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RBOT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RBOT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RBOT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 117,305 | 117,306 | PASS |  |  |
| RBOT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RBOT.TO | MR-price | price = the last completed close | 27.53 | 27.53 | PASS |  |  |
| RBOT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $27.53 needs above $10 | $27.53 needs above $10 | PASS |  |  |
| RBOT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.1 needs under 10 | 6.13 needs under 10 -> ✓ | PASS |  |  |
| RBOT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 17.4% below its 200-day average | 17.4% below | PASS |  |  |
| RBOT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.13 | 6.13 | PASS |  |  |
| RBOT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -17.41% | -17.41% | PASS |  |  |
| RBOT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RTX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| RTX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| RTX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RTX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,107,745,906 | 1,107,745,911 | PASS |  |  |
| RTX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RTX | MR-price | price = the last completed close | 194.89 | 194.89 | PASS |  |  |
| RTX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $194.89 needs above $10 | $194.89 needs above $10 | PASS |  |  |
| RTX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.4 needs under 10 | 13.43 needs under 10 -> ✗ | PASS |  |  |
| RTX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.2% above its 200-day average | 0.2% above | PASS |  |  |
| RTX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,107,745,906 needs above $25,000,000 | PASS |  |  |
| RTX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.43 | 13.43 | PASS |  |  |
| RTX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.21% | 0.21% | PASS |  |  |
| RTX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RY.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +8.6% | TR +8.6% | PASS | LOW | the two cards divide by different roundings of the average |
| RY.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| RY.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| RY.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RY.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,077,231,874 | 1,077,231,704 | PASS |  |  |
| RY.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RY.TO | MR-price | price = the last completed close | 285.69 | 285.69 | PASS |  |  |
| RY.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $285.69 needs above $10 | $285.69 needs above $10 | PASS |  |  |
| RY.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.8 needs under 10 | 11.83 needs under 10 -> ✗ | PASS |  |  |
| RY.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 8.6% above its 200-day average | 8.6% above | PASS |  |  |
| RY.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,077,231,874 needs above $25,000,000 | PASS |  |  |
| RY.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.83 | 11.83 | PASS |  |  |
| RY.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 8.62% | 8.62% | PASS |  |  |
| RY.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SETM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -31.0% | TR -31.0% | PASS | LOW | the two cards divide by different roundings of the average |
| SETM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SETM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| SETM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SETM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SETM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SETM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SETM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,488,242 | 3,488,233 | PASS |  |  |
| SETM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SETM | MR-price | price = the last completed close | 22.41 | 22.41 | PASS |  |  |
| SETM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $22.41 needs above $10 | $22.41 needs above $10 | PASS |  |  |
| SETM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.7 needs under 10 | 4.67 needs under 10 -> ✓ | PASS |  |  |
| SETM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 31.0% below its 200-day average | 31.0% below | PASS |  |  |
| SETM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $3.5M traded on an average day needs above $25M | $3,488,242 needs above $25,000,000 | PASS |  |  |
| SETM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.67 | 4.67 | PASS |  |  |
| SETM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -30.98% | -30.98% | PASS |  |  |
| SETM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SGRD.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| SMH | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.9% | TR -11.9% | PASS | LOW | the two cards divide by different roundings of the average |
| SMH | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SMH | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| SMH | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SMH | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SMH | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,959,608,377 | 5,959,608,411 | PASS |  |  |
| SMH | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SMH | MR-price | price = the last completed close | 461.9 | 461.9 | PASS |  |  |
| SMH | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $461.90 needs above $10 | $461.90 needs above $10 | PASS |  |  |
| SMH | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.2 needs under 10 | 10.24 needs under 10 -> ✗ | PASS |  |  |
| SMH | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.9% below its 200-day average | 11.9% below | PASS |  |  |
| SMH | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6B traded on an average day needs above $25M | $5,959,608,377 needs above $25,000,000 | PASS |  |  |
| SMH | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.24 | 10.24 | PASS |  |  |
| SMH | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.88% | -11.88% | PASS |  |  |
| SMH | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SNDK.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| SO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| SO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 774,983,365 | 780,927,060 | PASS |  |  |
| SO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SO | MR-price | price = the last completed close | 94.64 | 94.64 | PASS |  |  |
| SO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $94.64 needs above $10 | $94.64 needs above $10 | PASS |  |  |
| SO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 87.1 needs under 10 | 87.14 needs under 10 -> ✗ | PASS |  |  |
| SO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 3.9% above its 200-day average | 3.9% above | PASS |  |  |
| SO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $775M traded on an average day needs above $25M | $774,983,365 needs above $25,000,000 | PASS |  |  |
| SO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -60.7% | TR -60.7% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SOXL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| SOXL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,203,043,627 | 12,203,043,628 | PASS |  |  |
| SOXL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL | MR-price | price = the last completed close | 48.76 | 48.76 | PASS |  |  |
| SOXL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $48.76 needs above $10 | $48.76 needs above $10 | PASS |  |  |
| SOXL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.9 needs under 10 | 10.9 needs under 10 -> ✗ | PASS |  |  |
| SOXL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 60.7% below its 200-day average | 60.7% below | PASS |  |  |
| SOXL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.2B traded on an average day needs above $25M | $12,203,043,627 needs above $25,000,000 | PASS |  |  |
| SOXL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.9 | 10.90 | PASS |  |  |
| SOXL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -60.68% | -60.68% | PASS |  |  |
| SOXL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL.NE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -60.2% | TR -60.2% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL.NE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SOXL.NE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| SOXL.NE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL.NE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-volume_filter | zero-volume history: the volume rule is not checked, never a fake $0 fail | False | None/unchecked | PASS |  | the card shows "no volume data" |
| SOXL.NE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL.NE | MR-price | price = the last completed close | 12.3 | 12.3 | PASS |  |  |
| SOXL.NE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $12.30 needs above $10 | $12.30 needs above $10 | PASS |  |  |
| SOXL.NE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.0 needs under 10 | 10.96 needs under 10 -> ✗ | PASS |  |  |
| SOXL.NE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 60.2% below its 200-day average | 60.2% below | PASS |  |  |
| SOXL.NE | MR-row-volume | zero-volume fund: "no volume data", unchecked | Does it trade enough to get in and out? – no volume data this data sou | no volume data | PASS |  |  |
| SOXL.NE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.96 | 10.99 | PASS |  |  |
| SOXL.NE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -60.18% | -60.17% | PASS |  |  |
| SOXL.NE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -12.0% | TR -12.0% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SOXX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| SOXX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,104,691,173 | 6,104,692,110 | PASS |  |  |
| SOXX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXX | MR-price | price = the last completed close | 141.22 | 141.22 | PASS |  |  |
| SOXX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $141.22 needs above $10 | $141.22 needs above $10 | PASS |  |  |
| SOXX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.8 needs under 10 | 11.81 needs under 10 -> ✗ | PASS |  |  |
| SOXX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 12.0% below its 200-day average | 12.0% below | PASS |  |  |
| SOXX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6.1B traded on an average day needs above $25M | $6,104,691,173 needs above $25,000,000 | PASS |  |  |
| SOXX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.81 | 11.81 | PASS |  |  |
| SOXX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -12.02% | -12.02% | PASS |  |  |
| SOXX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SPCL | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| TSLA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.7% | TR -0.7% | PASS | LOW | the two cards divide by different roundings of the average |
| TSLA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| TSLA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| TSLA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,957,957,813 | 14,957,957,890 | PASS |  |  |
| TSLA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSLA | MR-price | price = the last completed close | 379.74 | 379.74 | PASS |  |  |
| TSLA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $379.74 needs above $10 | $379.74 needs above $10 | PASS |  |  |
| TSLA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.6 needs under 10 | 21.62 needs under 10 -> ✗ | PASS |  |  |
| TSLA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.7% below its 200-day average | 0.7% below | PASS |  |  |
| TSLA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $15B traded on an average day needs above $25M | $14,957,957,813 needs above $25,000,000 | PASS |  |  |
| TSLA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.62 | 21.62 | PASS |  |  |
| TSLA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.72% | -0.72% | PASS |  |  |
| TSLA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| TSLL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| TSLL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; the price is under $10 | the 2-day RSI is 10 or higher; it is below its 200-day average; the price is under $10 | PASS |  |  |
| TSLL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 506,752,940 | 506,752,837 | PASS |  |  |
| TSLL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSLL | MR-price | price = the last completed close | 9.8 | 9.8 | PASS |  |  |
| TSLL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $9.80 needs above $10 | $9.80 needs above $10 | PASS |  |  |
| TSLL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 20.6 needs under 10 | 20.63 needs under 10 -> ✗ | PASS |  |  |
| TSLL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 16.7% below its 200-day average | 16.7% below | PASS |  |  |
| TSLL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $506.8M traded on an average day needs above $25M | $506,752,940 needs above $25,000,000 | PASS |  |  |
| TSLL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 20.63 | 20.63 | PASS |  |  |
| TSLL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| TSM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| TSM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| TSM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,893,529,775 | 5,893,529,457 | PASS |  |  |
| TSM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSM | MR-price | price = the last completed close | 373.45 | 373.45 | PASS |  |  |
| TSM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $373.45 needs above $10 | $373.45 needs above $10 | PASS |  |  |
| TSM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.8 needs under 10 | 9.81 needs under 10 -> ✓ | PASS |  |  |
| TSM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 7.1% below its 200-day average | 7.1% below | PASS |  |  |
| TSM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.9B traded on an average day needs above $25M | $5,893,529,775 needs above $25,000,000 | PASS |  |  |
| TSM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.81 | 9.81 | PASS |  |  |
| TSM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| UBOT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -35.4% | TR -35.4% | PASS | LOW | the two cards divide by different roundings of the average |
| UBOT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| UBOT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| UBOT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UBOT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UBOT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UBOT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UBOT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 325,519 | 325,520 | PASS |  |  |
| UBOT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| UBOT | MR-price | price = the last completed close | 15.51 | 15.51 | PASS |  |  |
| UBOT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $15.51 needs above $10 | $15.51 needs above $10 | PASS |  |  |
| UBOT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.4 needs under 10 | 7.37 needs under 10 -> ✓ | PASS |  |  |
| UBOT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 35.4% below its 200-day average | 35.4% below | PASS |  |  |
| UBOT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.37 | 7.37 | PASS |  |  |
| UBOT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -35.41% | -35.41% | PASS |  |  |
| UBOT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| UFO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -15.9% | TR -16.0% | PASS | LOW | the two cards divide by different roundings of the average |
| UFO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| UFO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| UFO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UFO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UFO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UFO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UFO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 10,152,640 | 10,152,641 | PASS |  |  |
| UFO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| UFO | MR-price | price = the last completed close | 39.54 | 39.54 | PASS |  |  |
| UFO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $39.54 needs above $10 | $39.54 needs above $10 | PASS |  |  |
| UFO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.6 needs under 10 | 9.57 needs under 10 -> ✓ | PASS |  |  |
| UFO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 15.9% below its 200-day average | 15.9% below | PASS |  |  |
| UFO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $10.2M traded on an average day needs above $25M | $10,152,640 needs above $25,000,000 | PASS |  |  |
| UFO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.57 | 9.57 | PASS |  |  |
| UFO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -15.91% | -15.91% | PASS |  |  |
| UFO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| URA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -33.5% | TR -33.5% | PASS | LOW | the two cards divide by different roundings of the average |
| URA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| URA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| URA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 151,486,844 | 151,486,844 | PASS |  |  |
| URA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| URA | MR-price | price = the last completed close | 30.44 | 30.44 | PASS |  |  |
| URA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $30.44 needs above $10 | $30.44 needs above $10 | PASS |  |  |
| URA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.6 needs under 10 | 6.56 needs under 10 -> ✓ | PASS |  |  |
| URA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 33.5% below its 200-day average | 33.5% below | PASS |  |  |
| URA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $151.5M traded on an average day needs above $25M | $151,486,844 needs above $25,000,000 | PASS |  |  |
| URA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.56 | 6.56 | PASS |  |  |
| URA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -33.53% | -33.53% | PASS |  |  |
| URA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| URAA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -60.4% | TR -60.4% | PASS | LOW | the two cards divide by different roundings of the average |
| URAA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| URAA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| URAA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URAA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URAA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,046,256 | 1,046,256 | PASS |  |  |
| URAA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| URAA | MR-price | price = the last completed close | 11.71 | 11.71 | PASS |  |  |
| URAA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $11.71 needs above $10 | $11.71 needs above $10 | PASS |  |  |
| URAA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.9 needs under 10 | 6.88 needs under 10 -> ✓ | PASS |  |  |
| URAA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 60.4% below its 200-day average | 60.4% below | PASS |  |  |
| URAA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1M traded on an average day needs above $25M | $1,046,256 needs above $25,000,000 | PASS |  |  |
| URAA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.88 | 6.88 | PASS |  |  |
| URAA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -60.44% | -60.44% | PASS |  |  |
| URAA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| V | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| V | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| V | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| V | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,940,659,096 | 2,945,960,836 | PASS |  |  |
| V | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| V | MR-price | price = the last completed close | 426.46 | 426.46 | PASS |  |  |
| V | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $426.46 needs above $10 | $426.46 needs above $10 | PASS |  |  |
| V | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 73.1 needs under 10 | 73.09 needs under 10 -> ✗ | PASS |  |  |
| V | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 23.1% above its 200-day average | 23.1% above | PASS |  |  |
| V | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.9B traded on an average day needs above $25M | $2,940,659,096 needs above $25,000,000 | PASS |  |  |
| V | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 73.09 | 72.84 | PASS |  |  |
| V | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| VFV.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +6.0% | TR +6.1% | PASS | LOW | the two cards divide by different roundings of the average |
| VFV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-13 | 2026-11-13 | PASS |  |  |
| VFV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| VFV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VFV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 70,355,521 | 70,355,522 | PASS |  |  |
| VFV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| VFV.TO | MR-price | price = the last completed close | 191.4 | 191.4 | PASS |  |  |
| VFV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $191.40 needs above $10 | $191.40 needs above $10 | PASS |  |  |
| VFV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 53.0 needs under 10 | 52.96 needs under 10 -> ✗ | PASS |  |  |
| VFV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 6.0% above its 200-day average | 6.0% above | PASS |  |  |
| VFV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $70.4M traded on an average day needs above $25M | $70,355,521 needs above $25,000,000 | PASS |  |  |
| VFV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 52.96 | 52.96 | PASS |  |  |
| VFV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 6.05% | 6.05% | PASS |  |  |
| VFV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| VRT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -30.5% | TR -30.5% | PASS | LOW | the two cards divide by different roundings of the average |
| VRT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| VRT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| VRT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VRT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VRT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,798,863,038 | 1,798,863,039 | PASS |  |  |
| VRT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| VRT | MR-price | price = the last completed close | 188.67 | 188.67 | PASS |  |  |
| VRT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $188.67 needs above $10 | $188.67 needs above $10 | PASS |  |  |
| VRT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.3 needs under 10 | 14.3 needs under 10 -> ✗ | PASS |  |  |
| VRT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 30.5% below its 200-day average | 30.5% below | PASS |  |  |
| VRT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.8B traded on an average day needs above $25M | $1,798,863,038 needs above $25,000,000 | PASS |  |  |
| VRT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14.3 | 14.30 | PASS |  |  |
| VRT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -30.53% | -30.53% | PASS |  |  |
| VRT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| WDC.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| WELL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +10.3% | TR +10.3% | PASS | LOW | the two cards divide by different roundings of the average |
| WELL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| WELL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| WELL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| WELL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 725,106,038 | 725,106,038 | PASS |  |  |
| WELL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| WELL | MR-price | price = the last completed close | 244.65 | 244.65 | PASS |  |  |
| WELL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $244.65 needs above $10 | $244.65 needs above $10 | PASS |  |  |
| WELL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 26.1 needs under 10 | 26.1 needs under 10 -> ✗ | PASS |  |  |
| WELL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 10.3% above its 200-day average | 10.3% above | PASS |  |  |
| WELL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $725.1M traded on an average day needs above $25M | $725,106,038 needs above $25,000,000 | PASS |  |  |
| WELL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 26.1 | 26.10 | PASS |  |  |
| WELL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 10.34% | 10.34% | PASS |  |  |
| WELL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| WMT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +7.9% | TR +7.9% | PASS | LOW | the two cards divide by different roundings of the average |
| WMT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| WMT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| WMT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| WMT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,719,007,348 | 2,719,007,348 | PASS |  |  |
| WMT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| WMT | MR-price | price = the last completed close | 128.41 | 128.41 | PASS |  |  |
| WMT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $128.41 needs above $10 | $128.41 needs above $10 | PASS |  |  |
| WMT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 96.1 needs under 10 | 96.12 needs under 10 -> ✗ | PASS |  |  |
| WMT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 7.9% above its 200-day average | 7.9% above | PASS |  |  |
| WMT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.7B traded on an average day needs above $25M | $2,719,007,348 needs above $25,000,000 | PASS |  |  |
| WMT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 96.12 | 96.12 | PASS |  |  |
| WMT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 7.93% | 7.93% | PASS |  |  |
| WMT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XCHP.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -9.6% | TR -9.6% | PASS | LOW | the two cards divide by different roundings of the average |
| XCHP.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XCHP.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XCHP.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XCHP.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 7,598,142 | 7,598,142 | PASS |  |  |
| XCHP.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XCHP.TO | MR-price | price = the last completed close | 105.33 | 105.33 | PASS |  |  |
| XCHP.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $105.33 needs above $10 | $105.33 needs above $10 | PASS |  |  |
| XCHP.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.3 needs under 10 | 13.3 needs under 10 -> ✗ | PASS |  |  |
| XCHP.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.6% below its 200-day average | 9.6% below | PASS |  |  |
| XCHP.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $7.6M traded on an average day needs above $25M | $7,598,142 needs above $25,000,000 | PASS |  |  |
| XCHP.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.3 | 13.30 | PASS |  |  |
| XCHP.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.56% | -9.55% | PASS |  |  |
| XCHP.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XDRV.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -16.7% | TR -16.7% | PASS | LOW | the two cards divide by different roundings of the average |
| XDRV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XDRV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XDRV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-cond-volume_filter | zero-volume history: the volume rule is not checked, never a fake $0 fail | False | None/unchecked | PASS |  | the card shows "no volume data" |
| XDRV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XDRV.TO | MR-price | price = the last completed close | 39.69 | 39.69 | PASS |  |  |
| XDRV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $39.69 needs above $10 | $39.69 needs above $10 | PASS |  |  |
| XDRV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 16.3 needs under 10 | 16.28 needs under 10 -> ✗ | PASS |  |  |
| XDRV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 16.7% below its 200-day average | 16.7% below | PASS |  |  |
| XDRV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 16.28 | 16.28 | PASS |  |  |
| XDRV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -16.7% | -16.70% | PASS |  |  |
| XDRV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XEQT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +3.0% | TR +3.0% | PASS | LOW | the two cards divide by different roundings of the average |
| XEQT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XEQT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| XEQT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XEQT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 50,060,118 | 50,059,642 | PASS |  |  |
| XEQT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XEQT.TO | MR-price | price = the last completed close | 44.86 | 44.86 | PASS |  |  |
| XEQT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $44.86 needs above $10 | $44.86 needs above $10 | PASS |  |  |
| XEQT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 12.8 needs under 10 | 12.78 needs under 10 -> ✗ | PASS |  |  |
| XEQT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 3.0% above its 200-day average | 3.0% above | PASS |  |  |
| XEQT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $50.1M traded on an average day needs above $25M | $50,060,118 needs above $25,000,000 | PASS |  |  |
| XEQT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 12.78 | 12.79 | PASS |  |  |
| XEQT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 3.02% | 3.02% | PASS |  |  |
| XEQT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XETM.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XETM.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XETM.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XETM.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XETM.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XETM.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XETM.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 203,585 | 203,586 | PASS |  |  |
| XETM.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XETM.TO | MR-price | price = the last completed close | 61.57 | 61.57 | PASS |  |  |
| XETM.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $61.57 needs above $10 | $61.57 needs above $10 | PASS |  |  |
| XETM.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.4 needs under 10 | 4.44 needs under 10 -> ✓ | PASS |  |  |
| XETM.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.0% below its 200-day average | 23.0% below | PASS |  |  |
| XETM.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.44 | 4.44 | PASS |  |  |
| XETM.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.02% | -23.02% | PASS |  |  |
| XETM.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XGD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -7.9% | TR -7.9% | PASS | LOW | the two cards divide by different roundings of the average |
| XGD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XGD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| XGD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XGD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 33,476,373 | 33,476,374 | PASS |  |  |
| XGD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XGD.TO | MR-price | price = the last completed close | 50.8 | 50.8 | PASS |  |  |
| XGD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $50.80 needs above $10 | $50.80 needs above $10 | PASS |  |  |
| XGD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.0 needs under 10 | 4.97 needs under 10 -> ✓ | PASS |  |  |
| XGD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 7.9% below its 200-day average | 7.9% below | PASS |  |  |
| XGD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $33.5M traded on an average day needs above $25M | $33,476,373 needs above $25,000,000 | PASS |  |  |
| XGD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.97 | 4.97 | PASS |  |  |
| XGD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.9% | -7.90% | PASS |  |  |
| XGD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +8.0% | TR +8.0% | PASS | LOW | the two cards divide by different roundings of the average |
| XOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XOM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| XOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,485,090,817 | 2,485,090,528 | PASS |  |  |
| XOM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XOM | MR-price | price = the last completed close | 166.87 | 166.87 | PASS |  |  |
| XOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $166.87 needs above $10 | $166.87 needs above $10 | PASS |  |  |
| XOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 34.4 needs under 10 | 34.39 needs under 10 -> ✗ | PASS |  |  |
| XOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 8.0% above its 200-day average | 8.0% above | PASS |  |  |
| XOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.5B traded on an average day needs above $25M | $2,485,090,817 needs above $25,000,000 | PASS |  |  |
| XOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 34.39 | 34.37 | PASS |  |  |
| XOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 8.04% | 8.04% | PASS |  |  |
| XOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AAPL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AAPL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AAPL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AAPL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AAPL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AAPL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AAPL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AAPL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AAPL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AAPU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AAPU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AAPU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AAPU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AAPU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AAPU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AAPU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AAPU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AAPU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AAPU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ABBV | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ABBV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ABBV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ABBV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ABBV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ABBV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ABBV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ABBV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ABBV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ABBV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ABBV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ABBV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AIPO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AIPO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AIPO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AIPO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AIPO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AIPO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AIPO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AIPO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AIPO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AIPO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AIPO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AIPO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ALAB | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ALAB | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ALAB | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ALAB | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ALAB | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ALAB | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ALAB | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ALAB | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ALAB | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ALAB | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ALAB | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ALAB | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMD | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AMD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AMD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AMD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AMD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AMD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMD.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AMD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AMD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AMD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AMD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AMD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMZN | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMZN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMZN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AMZN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AMZN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMZN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMZN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AMZN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AMZN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMZN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AMZN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMZN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMZU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMZU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMZU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AMZU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AMZU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMZU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMZU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AMZU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AMZU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMZU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AMZU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMZU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ANET.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ANET.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ANET.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ANET.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ANET.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ANET.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ANET.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ANET.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ANET.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ANET.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ANET.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ANET.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ASML.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ASML.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ASML.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ASML.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ASML.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ASML.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ASML.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ASML.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ASML.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ASML.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ASML.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ASML.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ASTL.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ASTL.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ASTL.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ASTL.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ASTL.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ASTL.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ASTL.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ASTL.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ASTL.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ASTL.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ASTL.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ASTL.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ATD.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ATD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ATD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ATD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ATD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ATD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ATD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ATD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ATD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ATD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ATD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ATD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGC | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AVGC | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AVGC | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AVGC | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AVGC | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGC | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AVGC | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AVGC | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AVGC | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AVGC | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AVGC | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGC | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AVGO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AVGO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AVGO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AVGO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AVGO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AVGO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AVGO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AVGO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AVGO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGO.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AVGO.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AVGO.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| AVGO.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| AVGO.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGO.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AVGO.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| AVGO.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| AVGO.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AVGO.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| AVGO.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGO.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BDT.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| BDT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| BDT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| BDT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| BDT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BDT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| BDT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| BDT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| BDT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| BDT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| BDT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BDT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BOTZ | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| BOTZ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| BOTZ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| BOTZ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| BOTZ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BOTZ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| BOTZ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| BOTZ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| BOTZ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| BOTZ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| BOTZ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BOTZ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BRK-B | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| BRK-B | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| BRK-B | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| BRK-B | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| BRK-B | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BRK-B | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| BRK-B | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| BRK-B | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| BRK-B | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| BRK-B | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| BRK-B | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BRK-B | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BRKU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| BRKU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| BRKU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| BRKU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| BRKU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BRKU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| BRKU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| BRKU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| BRKU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| BRKU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| BRKU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BRKU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CAMT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CAMT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CAMT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CAMT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CAMT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CAMT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CAMT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CAMT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CAMT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CAMT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CAMT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CAMT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CARS.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CARS.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CARS.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CARS.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CARS.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CARS.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CARS.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CARS.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CARS.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CARS.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CARS.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CARS.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CAT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CAT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CAT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CAT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CAT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CAT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CAT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CAT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CAT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CAT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CAT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CAT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CCO.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CCO.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CCO.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CCO.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CCO.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CCO.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CCO.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CCO.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CCO.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CCO.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CCO.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CCO.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CEG | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CEG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CEG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CEG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CEG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CEG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CEG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CEG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CEG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CEG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CEG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CEG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CGY.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CGY.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CGY.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CGY.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CGY.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CGY.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CGY.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CGY.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CGY.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CGY.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CGY.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CGY.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CNQ.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CNQ.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CNQ.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CNQ.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CNQ.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CNQ.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CNQ.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CNQ.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CNQ.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CNQ.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CNQ.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CNQ.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CNR.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CNR.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CNR.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CNR.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CNR.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CNR.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CNR.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CNR.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CNR.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CNR.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CNR.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CNR.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COP | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COP | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COP | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| COP | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| COP | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COP | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COP | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| COP | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| COP | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COP | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| COP | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COP | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPP.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COPP.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COPP.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| COPP.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| COPP.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPP.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COPP.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| COPP.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| COPP.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COPP.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| COPP.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPP.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COPX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COPX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| COPX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| COPX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COPX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| COPX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| COPX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COPX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| COPX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPZ | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COPZ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COPZ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| COPZ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| COPZ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPZ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COPZ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| COPZ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| COPZ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COPZ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| COPZ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPZ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COST | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COST | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COST | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| COST | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| COST | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COST | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COST | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| COST | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| COST | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COST | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| COST | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COST | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COTG | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| COTG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| COTG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| COTG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| COTG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COTG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| COTG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| COTG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| COTG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| COTG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| COTG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COTG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CSU.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CSU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CSU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CSU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CSU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CSU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CSU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CSU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CSU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CSU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CSU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CSU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CVX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| CVX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| CVX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| CVX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| CVX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CVX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| CVX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| CVX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| CVX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| CVX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| CVX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CVX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRAL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DRAL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DRAL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| DRAL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| DRAL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRAL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DRAL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| DRAL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| DRAL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DRAL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| DRAL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRAL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRAM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DRAM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DRAM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| DRAM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| DRAM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRAM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DRAM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| DRAM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| DRAM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DRAM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| DRAM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRAM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRIV | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DRIV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DRIV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| DRIV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| DRIV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRIV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DRIV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| DRIV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| DRIV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DRIV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| DRIV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRIV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DUK | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DUK | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DUK | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| DUK | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| DUK | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DUK | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DUK | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| DUK | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| DUK | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DUK | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| DUK | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DUK | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ELIL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ELIL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ELIL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ELIL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ELIL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ELIL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ELIL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ELIL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ELIL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ELIL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ELIL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ELIL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| EQIX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| EQIX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| EQIX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| EQIX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| EQIX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| EQIX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| EQIX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| EQIX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| EQIX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| EQIX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| EQIX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| EQIX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ETN | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ETN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ETN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ETN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ETN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ETN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ETN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ETN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ETN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ETN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ETN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ETN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| FCX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| FCX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| FCX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| FCX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| FCX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| FCX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| FCX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| FCX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| FCX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| FCX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| FCX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| FCX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| FINN.NE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| FINN.NE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| FINN.NE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| FINN.NE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| FINN.NE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| FINN.NE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| FINN.NE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| FINN.NE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| FINN.NE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| FINN.NE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| FINN.NE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| FINN.NE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GDX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GDX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GDX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GDX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GDX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GDX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GDX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GDX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GDX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GDX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GDX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GDX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GDXU.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GDXU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GDXU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GDXU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GDXU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GDXU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GDXU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GDXU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GDXU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GDXU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GDXU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GDXU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GEV | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GEV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GEV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GEV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GEV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GEV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GEV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GEV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GEV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GEV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GEV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GEV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GEV.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GEV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GEV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GEV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GEV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GEV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GEV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GEV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GEV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GEV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GEV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GEV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GGLL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GGLL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GGLL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GGLL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GGLL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GGLL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GGLL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GGLL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GGLL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GGLL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GGLL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GGLL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GIB-A.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GIB-A.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GIB-A.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GIB-A.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GIB-A.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GIB-A.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GIB-A.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GIB-A.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GIB-A.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GIB-A.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GIB-A.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GIB-A.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GOOGL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GOOGL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GOOGL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GOOGL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GOOGL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GOOGL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GOOGL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GOOGL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GOOGL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GOOGL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GOOGL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GOOGL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GRID | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| GRID | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| GRID | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| GRID | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| GRID | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GRID | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| GRID | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| GRID | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| GRID | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| GRID | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| GRID | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GRID | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HD | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| HD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| HD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| HD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| HD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| HD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| HD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| HD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| HD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| HD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HURA.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| HURA.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| HURA.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| HURA.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| HURA.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HURA.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| HURA.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| HURA.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| HURA.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| HURA.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| HURA.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HURA.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HXQ.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| HXQ.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| HXQ.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| HXQ.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| HXQ.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HXQ.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| HXQ.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| HXQ.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| HXQ.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| HXQ.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| HXQ.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HXQ.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| JNJ | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| JNJ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| JNJ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| JNJ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| JNJ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| JNJ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| JNJ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| JNJ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| JNJ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| JNJ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| JNJ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| JNJ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| JPM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| JPM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| JPM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| JPM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| JPM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| JPM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| JPM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| JPM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| JPM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| JPM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| JPM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| JPM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| KEYS | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| KEYS | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| KEYS | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| KEYS | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| KEYS | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| KEYS | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| KEYS | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| KEYS | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| KEYS | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| KEYS | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| KEYS | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| KEYS | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| LIN | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| LIN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| LIN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| LIN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| LIN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| LIN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| LIN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| LIN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| LIN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| LIN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| LIN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| LIN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| LLY | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| LLY | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| LLY | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| LLY | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| LLY | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| LLY | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| LLY | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| LLY | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| LLY | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| LLY | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| LLY | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| LLY | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MDA.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MDA.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MDA.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| MDA.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| MDA.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MDA.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MDA.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| MDA.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| MDA.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MDA.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| MDA.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MDA.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| META | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| META | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| META | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| META | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| META | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| META | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| META | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| META | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| META | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| META | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| META | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| META | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| METU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| METU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| METU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| METU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| METU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| METU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| METU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| METU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| METU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| METU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| METU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| METU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MRVL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MRVL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MRVL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| MRVL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| MRVL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MRVL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MRVL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| MRVL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| MRVL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MRVL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| MRVL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MRVL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MSFT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MSFT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MSFT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| MSFT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| MSFT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MSFT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MSFT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| MSFT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| MSFT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MSFT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| MSFT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MSFT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MSFU | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MSFU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MSFU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| MSFU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| MSFU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MSFU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MSFU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| MSFU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| MSFU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MSFU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| MSFU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MSFU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MTRX.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MTRX.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MTRX.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| MTRX.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| MTRX.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MTRX.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MTRX.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| MTRX.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| MTRX.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MTRX.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| MTRX.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MTRX.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MU.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| MU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| MU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| MU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| MU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| MU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| MU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| MU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| MU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| MU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NEE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NEE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NEE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| NEE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| NEE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NEE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NEE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| NEE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| NEE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NEE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| NEE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NEE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NEM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NEM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NEM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| NEM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| NEM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NEM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NEM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| NEM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| NEM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NEM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| NEM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NEM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NFLX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NFLX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NFLX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| NFLX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| NFLX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NFLX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NFLX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| NFLX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| NFLX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NFLX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| NFLX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NFLX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NFXL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NFXL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NFXL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| NFXL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| NFXL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NFXL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NFXL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| NFXL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| NFXL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NFXL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| NFXL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NFXL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NTR.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NTR.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NTR.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| NTR.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| NTR.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NTR.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NTR.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| NTR.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| NTR.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NTR.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| NTR.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NTR.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NVDA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NVDA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NVDA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| NVDA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| NVDA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NVDA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| NVDA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| NVDA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NVDA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| NVDA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NVDL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NVDL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NVDL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| NVDL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| NVDL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NVDL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| NVDL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| NVDL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NVDL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| NVDL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ONTO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ONTO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ONTO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ONTO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ONTO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ONTO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ONTO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ONTO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ONTO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ONTO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ONTO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ONTO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ORBX.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ORBX.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ORBX.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ORBX.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ORBX.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ORBX.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ORBX.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ORBX.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ORBX.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ORBX.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ORBX.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ORBX.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ORCL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ORCL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ORCL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| ORCL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| ORCL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ORCL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ORCL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| ORCL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| ORCL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ORCL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| ORCL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ORCL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PG | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| PG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| PG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| PG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| PG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| PG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| PG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| PG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| PG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| PG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PLD | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| PLD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| PLD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| PLD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| PLD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PLD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| PLD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| PLD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| PLD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| PLD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| PLD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PLD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PNG.V | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| PNG.V | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| PNG.V | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| PNG.V | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| PNG.V | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PNG.V | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| PNG.V | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| PNG.V | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| PNG.V | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| PNG.V | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| PNG.V | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PNG.V | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QCOM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| QCOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| QCOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| QCOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| QCOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QCOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| QCOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| QCOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| QCOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| QCOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| QCOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QCOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QPUX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| QPUX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| QPUX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| QPUX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| QPUX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QPUX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| QPUX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| QPUX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| QPUX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| QPUX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| QPUX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QPUX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QTUM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| QTUM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| QTUM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| QTUM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| QTUM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QTUM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| QTUM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| QTUM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| QTUM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| QTUM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| QTUM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QTUM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RBOT.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| RBOT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| RBOT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| RBOT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| RBOT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RBOT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| RBOT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| RBOT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| RBOT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| RBOT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| RBOT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RBOT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RTX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| RTX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| RTX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| RTX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| RTX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RTX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| RTX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| RTX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| RTX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| RTX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| RTX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RTX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RY.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| RY.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| RY.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| RY.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| RY.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RY.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| RY.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| RY.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| RY.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| RY.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| RY.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RY.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SETM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SETM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SETM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SETM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SETM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SETM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SETM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SETM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SETM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SETM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SETM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SETM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SGRD.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SGRD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SGRD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SGRD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SGRD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SGRD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SGRD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SGRD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SGRD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SGRD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SGRD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SGRD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SMH | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SMH | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SMH | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SMH | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SMH | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SMH | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SMH | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SMH | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SMH | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SMH | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SMH | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SMH | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SNDK.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SNDK.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SNDK.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SNDK.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SNDK.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SNDK.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SNDK.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SNDK.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SNDK.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SNDK.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SNDK.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SNDK.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SOXL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SOXL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SOXL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SOXL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SOXL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SOXL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SOXL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SOXL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SOXL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXL.NE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SOXL.NE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SOXL.NE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SOXL.NE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SOXL.NE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL.NE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SOXL.NE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SOXL.NE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SOXL.NE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SOXL.NE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SOXL.NE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL.NE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SOXX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SOXX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SOXX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SOXX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SOXX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SOXX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SOXX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SOXX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SOXX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SPCL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SPCL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SPCL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| SPCL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| SPCL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SPCL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SPCL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| SPCL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| SPCL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SPCL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| SPCL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SPCL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSLA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| TSLA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| TSLA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| TSLA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| TSLA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSLA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| TSLA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| TSLA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| TSLA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| TSLA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| TSLA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSLA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSLL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| TSLL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| TSLL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| TSLL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| TSLL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSLL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| TSLL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| TSLL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| TSLL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| TSLL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| TSLL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSLL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| TSM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| TSM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| TSM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| TSM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| TSM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| TSM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| TSM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| TSM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| TSM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| UBOT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| UBOT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| UBOT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| UBOT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| UBOT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| UBOT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| UBOT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| UBOT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| UBOT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| UBOT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| UBOT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| UBOT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| UFO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| UFO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| UFO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| UFO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| UFO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| UFO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| UFO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| UFO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| UFO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| UFO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| UFO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| UFO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| URA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| URA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| URA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| URA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| URA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| URA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| URA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| URA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| URA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| URA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| URA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| URA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| URAA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| URAA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| URAA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| URAA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| URAA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| URAA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| URAA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| URAA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| URAA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| URAA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| URAA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| URAA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| V | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| V | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| V | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| V | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| V | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| V | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| V | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| V | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| V | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| V | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| V | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| V | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| VFV.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| VFV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| VFV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| VFV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| VFV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| VFV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| VFV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| VFV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| VFV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| VFV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| VFV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| VFV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| VRT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| VRT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| VRT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| VRT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| VRT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| VRT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| VRT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| VRT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| VRT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| VRT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| VRT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| VRT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WDC.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| WDC.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| WDC.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| WDC.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| WDC.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WDC.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| WDC.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| WDC.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| WDC.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| WDC.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| WDC.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WDC.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WELL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| WELL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| WELL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| WELL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| WELL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WELL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| WELL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| WELL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| WELL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| WELL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| WELL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WELL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WMT | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| WMT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| WMT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| WMT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| WMT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WMT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| WMT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| WMT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| WMT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| WMT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| WMT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WMT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XCHP.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XCHP.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XCHP.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| XCHP.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| XCHP.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XCHP.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XCHP.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| XCHP.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| XCHP.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XCHP.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| XCHP.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XCHP.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XDRV.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XDRV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XDRV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| XDRV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| XDRV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XDRV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XDRV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| XDRV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| XDRV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XDRV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| XDRV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XDRV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XEQT.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XEQT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XEQT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| XEQT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| XEQT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XEQT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XEQT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| XEQT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| XEQT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XEQT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| XEQT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XEQT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XETM.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XETM.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XETM.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| XETM.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| XETM.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XETM.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XETM.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| XETM.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| XETM.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XETM.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| XETM.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XETM.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XGD.TO | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XGD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XGD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| XGD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| XGD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XGD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XGD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| XGD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| XGD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XGD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| XGD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XGD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XOM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 13, 2024 | 2024-11-13 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| XOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| XOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.0% | ↓ below -3.0% | PASS |  |  |
| XOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -7.7% | ↓ below -7.7% | PASS |  |  |
| XOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| XOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +1.1% | ↑ above +1.1% | PASS |  |  |
| XOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -3.1% | ↓ below -3.1% | PASS |  |  |
| XOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| XOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 16 close | Nov 16 | PASS |  |  |
| XOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 26.0 | 26.0 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
