# Statement Audit phase 3a report (Market backdrop, Fundamentals, Mean-Reversion Read)

Run: 2026-11-19T18:07 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 3391 · WRONG 134 (CRITICAL) · MISLEADING 16 (per-row severity) · UNVERIFIED 268 (INFO)

Recomputed from bars: MR RSI(2), % above the 200-day, dollar volume, the four rule marks, the blocker sentence; S&P 500 200/50-day and the 10-session drop (the app's own 260 bars); QQQ and "largest since" from an independent Yahoo history (S4).
Provider fields (sales growth, ROE, debt/equity) are arithmetic and flag logic only: no recompute is possible (UNVERIFIED as to truth). NOT YET COVERED: the Data Sources tab (phase 3b), other tabs; branches these tickers do not reach (signal true, VIX band edges, no-down-day, unavailable backdrop, negative equity) are exercised by planted tests only.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| BRKU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 23.7% | 22.84% | WRONG | CRITICAL |  |
| CEG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.16% | -9.46% | WRONG | CRITICAL |  |
| COST | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 12.1% | 11.79% | WRONG | CRITICAL |  |
| CVX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 16.69 | 14.50 | WRONG | LOW | within 0.8: the MR route smooths over its own frame length |
| CVX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 6.93% | 5.12% | WRONG | CRITICAL |  |
| ETN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -16.33% | -16.80% | WRONG | CRITICAL |  |
| FCX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -24.17% | -24.45% | WRONG | CRITICAL |  |
| LIN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.93% | 2.51% | WRONG | CRITICAL |  |
| LLY | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 21.36% | 21.04% | WRONG | CRITICAL |  |
| META | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -5.13% | -5.23% | WRONG | CRITICAL |  |
| METU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.32% | -21.03% | WRONG | CRITICAL |  |
| NEE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -3.13% | -4.01% | WRONG | CRITICAL |  |
| NEM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -10.42% | -10.65% | WRONG | CRITICAL |  |
| QCOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -4.42% | -4.97% | WRONG | CRITICAL |  |
| RTX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.52% | -0.90% | WRONG | CRITICAL |  |
| V | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 15.73% | 15.33% | WRONG | CRITICAL |  |
| WMT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 6.21% | 5.93% | WRONG | CRITICAL |  |
| XOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.67% | 1.38% | WRONG | CRITICAL |  |
| AAPL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AAPU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ABBV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AIPO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ALAB | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AMD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AMD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AMZN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AMZU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ANET.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ASML.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ASTL.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ATD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AVGC | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AVGO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| AVGO.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| BDT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| BOTZ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| BRK-B | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| BRKU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CAMT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CARS.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CAT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CCO.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CEG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CGY.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CNQ.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CNR.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| COP | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| COPP.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| COPX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| COPZ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| COST | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| COTG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CSU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| CVX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| DRAL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| DRAM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| DRIV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| DUK | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ELIL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| EQIX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ETN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| FCX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GDX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GDXU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GEV | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GEV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GGLL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GIB-A.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GOOGL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| GRID | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| HD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| HURA.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| HXQ.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| JNJ | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| JPM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| KEYS | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| LIN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| LLY | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| MDA.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| META | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| METU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| MRVL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| MSFT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| MSFU | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| MTRX.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| MU.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| NEE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| NEM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| NFLX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| NFXL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| NTR.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| NVDA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| NVDL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ONTO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ORBX.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| ORCL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| PG | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| PLD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| PNG.V | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| QCOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| QPUX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| QTUM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| RBOT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| RTX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| RY.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SETM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SGRD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SMH | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SNDK.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SOXL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SOXL.NE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SOXX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| SPCL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| TSLA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| TSLL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| TSM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| UBOT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| UFO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| URA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| URAA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| V | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| VFV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| VRT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| WDC.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| WELL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| WMT | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| XCHP.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| XDRV.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| XEQT.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| XETM.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| XGD.TO | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| XOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -2.0% on Nov 19 | -1.97% on Nov 19 | WRONG | CRITICAL |  |
| BRKU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +23.7% | TR +22.8% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| CEG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -9.2% | TR -9.5% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| COST | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +12.1% | TR +11.8% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| CVX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +6.9% | TR +5.1% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| ETN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -16.3% | TR -16.8% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| FCX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -24.2% | TR -24.4% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| LIN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +2.9% | TR +2.5% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| LLY | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +21.4% | TR +21.0% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| METU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.3% | TR -21.0% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| NEE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -3.1% | TR -4.0% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| NEM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -10.4% | TR -10.7% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| QCOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -4.4% | TR -5.0% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| RTX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.5% | TR -0.9% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| V | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +15.7% | TR +15.3% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| WMT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +6.2% | TR +5.9% | MISLEADING | LOW | the two cards divide by different roundings of the average |
| XOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +2.7% | TR +1.4% | MISLEADING | LOW | the two cards divide by different roundings of the average |
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
| AAPU | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $45.30 2026 -11 -19 $47.68 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| ABBV | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $269.36 2026 -11 -19 $283.54 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| BRK-B | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $543.44 2026 -11 -19 $572.04 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| CSU.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $3,021.00 2026 -11 -19 $3,180.00 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| GIB-A.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% 6.79 2026 -11 -19 $112.41 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| HD | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $319.85 2026 -11 -19 $336.68 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| JNJ | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $253.78 2026 -11 -19 $267.14 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| LIN | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $484.70 2026 -11 -19 $510.21 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| LLY | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $1,283.56 2026 -11 -19 $1,351.12 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| MSFT | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $473.39 2026 -11 -19 $498.30 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| MSFU | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $34.48 2026 -11 -19 $36.29 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| RY.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $255.98 2026 -11 -19 $269.45 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| V | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $382.14 2026 -11 -19 $402.25 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| VFV.TO | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $173.80 2026 -11 -19 $182.95 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| WMT | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $119.74 2026 -11 -19 $126.04 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| XOM | U-MR | numbers on the card no statement claimed (exhaustive scan) | 1 5% $150.98 2026 -11 -19 $158.93 3 70 5 | each one claimed or exempt | UNVERIFIED | INFO | 10 unclaimed number token(s) |
| AAPL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AAPL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AAPU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AAPU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ABBV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ABBV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AIPO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AIPO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ALAB | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ALAB | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AMD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AMD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMZN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AMZN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMZU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AMZU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ANET.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ANET.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ASML.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ASML.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ASTL.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ASTL.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ATD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ATD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGC | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AVGC | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AVGO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AVGO.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| AVGO.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BDT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| BDT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BOTZ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| BOTZ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BRK-B | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| BRK-B | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| BRKU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| BRKU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CAMT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CAMT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CARS.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CARS.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CAT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CAT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CCO.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CCO.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CEG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CEG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CGY.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CGY.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CNQ.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CNQ.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CNR.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CNR.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COP | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| COP | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPP.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| COPP.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| COPX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COPZ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| COPZ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COST | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| COST | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| COTG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| COTG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CSU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CSU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| CVX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| CVX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRAL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| DRAL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRAM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| DRAM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DRIV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| DRIV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DUK | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| DUK | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ELIL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ELIL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| EQIX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| EQIX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ETN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ETN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| FCX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| FCX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GDX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GDX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GDXU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GDXU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GEV | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GEV | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GEV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GEV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GGLL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GGLL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GIB-A.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GIB-A.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GOOGL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GOOGL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| GRID | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| GRID | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| HD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HURA.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| HURA.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| HXQ.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| HXQ.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| JNJ | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| JNJ | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| JPM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| JPM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| KEYS | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| KEYS | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| LIN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| LIN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| LLY | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| LLY | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MDA.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| MDA.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| META | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| META | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| METU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| METU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MRVL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| MRVL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MSFT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| MSFT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MSFU | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| MSFU | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MTRX.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| MTRX.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| MU.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| MU.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NEE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| NEE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NEM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| NEM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NFLX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| NFLX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NFXL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| NFXL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NTR.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| NTR.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NVDA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| NVDA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NVDL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| NVDL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ONTO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ONTO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ORBX.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ORBX.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ORCL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| ORCL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PG | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| PG | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PLD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| PLD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PNG.V | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| PNG.V | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QCOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| QCOM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QPUX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| QPUX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QTUM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| QTUM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RBOT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| RBOT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RTX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| RTX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| RY.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| RY.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SETM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SETM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SGRD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SGRD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SMH | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SMH | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SNDK.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SNDK.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SOXL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXL.NE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SOXL.NE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SOXX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SPCL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| SPCL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSLA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| TSLA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSLL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| TSLL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| TSM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| TSM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| UBOT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| UBOT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| UFO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| UFO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| URA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| URA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| URAA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| URAA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| V | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| V | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| VFV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| VFV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| VRT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| VRT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WDC.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| WDC.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WELL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| WELL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| WMT | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| WMT | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XCHP.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| XCHP.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XDRV.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| XDRV.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XEQT.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| XEQT.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XETM.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| XETM.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XGD.TO | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| XGD.TO | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| XOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -2.7% on Nov 16 | -2.67% on Nov 16 | UNVERIFIED | INFO |  |
| XOM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| FINN.NE | X1 | cards | 0 bars | at least 60 | UNVERIFIED | INFO |  |
| AAPL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.7% | +11.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AAPL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 127.6% | 127.6% flag=False | PASS |  |  |
| AAPL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| AAPL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AAPL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| AAPL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-02 (17 days ago); no upcoming date listed. | 2026-11-02 days_until=-17 | PASS |  |  |
| AAPU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AAPU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ABBV | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +10.3% | +10.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ABBV | FU3 | ROE: value (1 dp) and the flag at < 0% | ⚑ Return on equity ROE -92.0% | -92.0% flag=True | PASS |  |  |
| ABBV | FU4 | negative D/E -> "ratio not meaningful", unchecked | says so | not meaningful | PASS |  |  |
| ABBV | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| ABBV | FU5w | one plain sentence per tripped flag | Return on equity is negative. | 1 sentence(s) | PASS |  |  |
| ABBV | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| ABBV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (20 days ago); no upcoming date listed. | 2026-10-30 days_until=-20 | PASS |  |  |
| AIPO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AIPO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ALAB | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +153.7% | +153.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ALAB | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ALAB | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) | Alpha Vantage | PASS |  |  |
| ALAB | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (16 days ago); no upcoming date listed. | 2026-11-03 days_until=-16 | PASS |  |  |
| AMD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.6% | 11.6% flag=False | PASS |  |  |
| AMD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.10 | 0.10 flag=False | PASS |  |  |
| AMD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AMD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| AMD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (16 days ago); no upcoming date listed. | 2026-11-03 days_until=-16 | PASS |  |  |
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
| AMZN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (21 days ago); no upcoming date listed. | 2026-10-29 days_until=-21 | PASS |  |  |
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
| ATD.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-24 · in 5 days. Within a week: decide before then whether to hold throug | 2026-11-24 days_until=5 | PASS |  |  |
| AVGC | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AVGC | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| AVGO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +85.5% | +85.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AVGO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 43.9% | 43.9% flag=False | PASS |  |  |
| AVGO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.60 | 0.60 flag=False | PASS |  |  |
| AVGO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AVGO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| AVGO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-09 · in 20 days. If you'll still hold on that date, the price can jump e | 2026-12-09 days_until=20 | PASS |  |  |
| AVGO.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| AVGO.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| BDT.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.7% | +36.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| BDT.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.6% | 16.6% flag=False | PASS |  |  |
| BDT.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.79 | 0.79 flag=False | PASS |  |  |
| BDT.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| BDT.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| BDT.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-11 (8 days ago); no upcoming date listed. | 2026-11-11 days_until=-8 | PASS |  |  |
| BOTZ | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| BOTZ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| BRK-B | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.2% | +11.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| BRK-B | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.9% | 11.9% flag=False | PASS |  |  |
| BRK-B | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| BRK-B | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| BRK-B | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| BRK-B | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-07 (12 days ago); no upcoming date listed. | 2026-11-07 days_until=-12 | PASS |  |  |
| BRKU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| BRKU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CAMT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 5.8% | 5.8% flag=False | PASS |  |  |
| CAMT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.69 | 0.69 flag=False | PASS |  |  |
| CAMT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CAMT | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| CAMT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (15 days ago); no upcoming date listed. | 2026-11-04 days_until=-15 | PASS |  |  |
| CARS.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| CARS.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CAT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +17.3% | +17.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CAT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 58.5% | 58.5% flag=False | PASS |  |  |
| CAT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 2.10 | 2.10 flag=True | PASS |  |  |
| CAT | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| CAT | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| CAT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| CAT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (21 days ago); no upcoming date listed. | 2026-10-29 days_until=-21 | PASS |  |  |
| CCO.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +0.7% | +0.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CCO.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 5.7% | 5.7% flag=False | PASS |  |  |
| CCO.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.14 | 0.14 flag=False | PASS |  |  |
| CCO.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CCO.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CCO.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (20 days ago); no upcoming date listed. | 2026-10-30 days_until=-20 | PASS |  |  |
| CEG | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +45.4% | +45.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CEG | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 18.3% | 18.3% flag=False | PASS |  |  |
| CEG | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| CEG | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CEG | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CEG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-09 (10 days ago); no upcoming date listed. | 2026-11-09 days_until=-10 | PASS |  |  |
| CGY.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +19.9% | +19.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CGY.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 12.0% | 12.0% flag=False | PASS |  |  |
| CGY.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.54 | 0.54 flag=False | PASS |  |  |
| CGY.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CGY.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CGY.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-30 · in 11 days. If you'll still hold on that date, the price can jump e | 2026-11-30 days_until=11 | PASS |  |  |
| CNQ.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +34.4% | +34.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CNQ.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 32.4% | 32.4% flag=False | PASS |  |  |
| CNQ.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.42 | 0.42 flag=False | PASS |  |  |
| CNQ.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CNQ.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CNQ.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (14 days ago); no upcoming date listed. | 2026-11-05 days_until=-14 | PASS |  |  |
| CNR.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +14.6% | +14.6% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CNR.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 22.4% | 22.4% flag=False | PASS |  |  |
| CNR.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.09 | 1.09 flag=False | PASS |  |  |
| CNR.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CNR.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CNR.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-29 · in 71 days. If you'll still hold on that date, the price can jump e | 2027-01-29 days_until=71 | PASS |  |  |
| COP | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.8% | 17.8% flag=False | PASS |  |  |
| COP | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.35 | 0.35 flag=False | PASS |  |  |
| COP | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| COP | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| COP | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (14 days ago); no upcoming date listed. | 2026-11-05 days_until=-14 | PASS |  |  |
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
| COST | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-10 · in 21 days. If you'll still hold on that date, the price can jump e | 2026-12-10 days_until=21 | PASS |  |  |
| COTG | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| COTG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| CSU.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +19.1% | +19.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CSU.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 24.2% | 24.2% flag=False | PASS |  |  |
| CSU.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.13 | 1.13 flag=False | PASS |  |  |
| CSU.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CSU.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CSU.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-06 (13 days ago); no upcoming date listed. | 2026-11-06 days_until=-13 | PASS |  |  |
| CVX | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +34.8% | +34.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| CVX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 13.9% | 13.9% flag=False | PASS |  |  |
| CVX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| CVX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| CVX | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| CVX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (20 days ago); no upcoming date listed. | 2026-10-30 days_until=-20 | PASS |  |  |
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
| DUK | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (14 days ago); no upcoming date listed. | 2026-11-05 days_until=-14 | PASS |  |  |
| ELIL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ELIL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| EQIX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.5% | 11.5% flag=False | PASS |  |  |
| EQIX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.72 | 1.72 flag=False | PASS |  |  |
| EQIX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| EQIX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| EQIX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (22 days ago); no upcoming date listed. | 2026-10-28 days_until=-22 | PASS |  |  |
| ETN | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +28.0% | +28.0% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ETN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.5% | 19.5% flag=False | PASS |  |  |
| ETN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.00 | 1.00 flag=False | PASS |  |  |
| ETN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ETN | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| ETN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (16 days ago); no upcoming date listed. | 2026-11-03 days_until=-16 | PASS |  |  |
| FCX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 15.3% | 15.3% flag=False | PASS |  |  |
| FCX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.49 | 0.49 flag=False | PASS |  |  |
| FCX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| FCX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| FCX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (23 days ago); no upcoming date listed. | 2026-10-27 days_until=-23 | PASS |  |  |
| GDX | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GDX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GDXU.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GDXU.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GE | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.6% | 50.6% flag=False | PASS |  |  |
| GE | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.10 | 1.10 flag=False | PASS |  |  |
| GE | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GE | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| GE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (30 days ago); no upcoming date listed. | 2026-10-20 days_until=-30 | PASS |  |  |
| GEV | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +26.8% | +26.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| GEV | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 93.0% | 93.0% flag=False | PASS |  |  |
| GEV | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.30 | 0.30 flag=False | PASS |  |  |
| GEV | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GEV | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| GEV | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-27 · in 69 days. If you'll still hold on that date, the price can jump e | 2027-01-27 days_until=69 | PASS |  |  |
| GEV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GEV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GGLL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GGLL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| GIB-A.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +3.3% | +3.3% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| GIB-A.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.5% | 17.5% flag=False | PASS |  |  |
| GIB-A.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.39 | 0.39 flag=False | PASS |  |  |
| GIB-A.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GIB-A.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| GIB-A.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-11 (8 days ago); no upcoming date listed. | 2026-11-11 days_until=-8 | PASS |  |  |
| GOOGL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 42.6% | 42.6% flag=False | PASS |  |  |
| GOOGL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.18 | 0.18 flag=False | PASS |  |  |
| GOOGL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| GOOGL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| GOOGL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (22 days ago); no upcoming date listed. | 2026-10-28 days_until=-22 | PASS |  |  |
| GRID | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| GRID | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| HD | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +5.7% | +5.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| HD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 102.7% | 102.7% flag=False | PASS |  |  |
| HD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 3.18 | 3.18 flag=True | PASS |  |  |
| HD | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| HD | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| HD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| HD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-17 (2 days ago); no upcoming date listed. | 2026-11-17 days_until=-2 | PASS |  |  |
| HURA.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| HURA.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| HXQ.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| HXQ.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| JNJ | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.6% | 19.6% flag=False | PASS |  |  |
| JNJ | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.55 | 0.55 flag=False | PASS |  |  |
| JNJ | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| JNJ | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| JNJ | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-26 · in 68 days. If you'll still hold on that date, the price can jump e | 2027-01-26 days_until=68 | PASS |  |  |
| JPM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +10.2% | +10.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| JPM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 17.9% | 17.9% flag=False | PASS |  |  |
| JPM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 3.32 | 3.32 flag=True | PASS |  |  |
| JPM | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| JPM | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| JPM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| JPM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2027-01-14 · in 56 days. If you'll still hold on that date, the price can jump e | 2027-01-14 days_until=56 | PASS |  |  |
| KEYS | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.5% | +36.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| KEYS | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 20.9% | 20.9% flag=False | PASS |  |  |
| KEYS | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.42 | 0.42 flag=False | PASS |  |  |
| KEYS | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| KEYS | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| KEYS | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-19 · today. The price can jump either way on the report. | 2026-11-19 days_until=0 | PASS |  |  |
| LIN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 18.1% | 18.1% flag=False | PASS |  |  |
| LIN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.68 | 0.68 flag=False | PASS |  |  |
| LIN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| LIN | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| LIN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (21 days ago); no upcoming date listed. | 2026-10-29 days_until=-21 | PASS |  |  |
| LLY | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +38.6% | +38.6% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| LLY | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 83.7% | 83.7% flag=False | PASS |  |  |
| LLY | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.23 | 1.23 flag=False | PASS |  |  |
| LLY | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| LLY | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| LLY | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-29 (21 days ago); no upcoming date listed. | 2026-10-29 days_until=-21 | PASS |  |  |
| MDA.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +21.5% | +21.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MDA.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 4.9% | 4.9% flag=False | PASS |  |  |
| MDA.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.31 | 0.31 flag=False | PASS |  |  |
| MDA.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MDA.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| MDA.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (14 days ago); no upcoming date listed. | 2026-11-05 days_until=-14 | PASS |  |  |
| META | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +26.1% | +26.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| META | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 30.3% | 30.3% flag=False | PASS |  |  |
| META | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.30 | 0.30 flag=False | PASS |  |  |
| META | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| META | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| META | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (29 days ago); no upcoming date listed. | 2026-10-21 days_until=-29 | PASS |  |  |
| METU | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| METU | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| MRVL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +36.5% | +36.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MRVL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.5% | 16.5% flag=False | PASS |  |  |
| MRVL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.29 | 0.29 flag=False | PASS |  |  |
| MRVL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MRVL | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| MRVL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-01 · in 12 days. If you'll still hold on that date, the price can jump e | 2026-12-01 days_until=12 | PASS |  |  |
| MSFT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +18.8% | +18.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| MSFT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 33.2% | 33.2% flag=False | PASS |  |  |
| MSFT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.23 | 0.23 flag=False | PASS |  |  |
| MSFT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| MSFT | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| MSFT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (22 days ago); no upcoming date listed. | 2026-10-28 days_until=-22 | PASS |  |  |
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
| NEE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (29 days ago); no upcoming date listed. | 2026-10-21 days_until=-29 | PASS |  |  |
| NEM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 26.5% | 26.5% flag=False | PASS |  |  |
| NEM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.16 | 0.16 flag=False | PASS |  |  |
| NEM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NEM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| NEM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-22 (28 days ago); no upcoming date listed. | 2026-10-22 days_until=-28 | PASS |  |  |
| NFLX | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.8% | +11.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NFLX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.4% | 50.4% flag=False | PASS |  |  |
| NFLX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.52 | 0.52 flag=False | PASS |  |  |
| NFLX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NFLX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NFLX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (30 days ago); no upcoming date listed. | 2026-10-20 days_until=-30 | PASS |  |  |
| NFXL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| NFXL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| NTR.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +1.2% | +1.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NTR.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 8.8% | 8.8% flag=False | PASS |  |  |
| NTR.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.55 | 0.55 flag=False | PASS |  |  |
| NTR.TO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NTR.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| NTR.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (15 days ago); no upcoming date listed. | 2026-11-04 days_until=-15 | PASS |  |  |
| NVDA | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +105.8% | +105.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NVDA | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 110.1% | 110.1% flag=False | PASS |  |  |
| NVDA | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| NVDA | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NVDA | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NVDA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-17 (2 days ago); no upcoming date listed. | 2026-11-17 days_until=-2 | PASS |  |  |
| NVDL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| NVDL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ONTO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 6.5% | 6.5% flag=False | PASS |  |  |
| ONTO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.77 | 0.77 flag=False | PASS |  |  |
| ONTO | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ONTO | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| ONTO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-09 (10 days ago); no upcoming date listed. | 2026-11-09 days_until=-10 | PASS |  |  |
| ORBX.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| ORBX.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| ORCL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 42.6% | 42.6% flag=False | PASS |  |  |
| ORCL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 2.01 | 2.01 flag=True | PASS |  |  |
| ORCL | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| ORCL | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| ORCL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| ORCL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-14 · in 25 days. If you'll still hold on that date, the price can jump e | 2026-12-14 days_until=25 | PASS |  |  |
| PG | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +4.0% | +4.0% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| PG | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 29.6% | 29.6% flag=False | PASS |  |  |
| PG | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.70 | 0.70 flag=False | PASS |  |  |
| PG | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PG | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · yfinance (ROE, debt) | Alpha Vantage, yfinance | PASS |  |  |
| PG | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-22 (28 days ago); no upcoming date listed. | 2026-10-22 days_until=-28 | PASS |  |  |
| PLD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 7.9% | 7.9% flag=False | PASS |  |  |
| PLD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.66 | 0.66 flag=False | PASS |  |  |
| PLD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PLD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| PLD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (35 days ago); no upcoming date listed. | 2026-10-15 days_until=-35 | PASS |  |  |
| PNG.V | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +3.5% | +3.5% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| PNG.V | FU3 | ROE: value (1 dp) and the flag at < 0% | ⚑ Return on equity ROE -4.3% | -4.3% flag=True | PASS |  |  |
| PNG.V | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.17 | 0.17 flag=False | PASS |  |  |
| PNG.V | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| PNG.V | FU5w | one plain sentence per tripped flag | Return on equity is negative. | 1 sentence(s) | PASS |  |  |
| PNG.V | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| PNG.V | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-24 · in 5 days. Within a week: decide before then whether to hold throug | 2026-11-24 days_until=5 | PASS |  |  |
| QCOM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.3% | 50.3% flag=False | PASS |  |  |
| QCOM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.50 | 0.50 flag=False | PASS |  |  |
| QCOM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| QCOM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| QCOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (15 days ago); no upcoming date listed. | 2026-11-04 days_until=-15 | PASS |  |  |
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
| RTX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-20 (30 days ago); no upcoming date listed. | 2026-10-20 days_until=-30 | PASS |  |  |
| RY.TO | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +8.9% | +8.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| RY.TO | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 16.2% | 16.2% flag=False | PASS |  |  |
| RY.TO | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ⚑ Debt D/E 4.10 | 4.10 flag=True | PASS |  |  |
| RY.TO | FU5 | headline = the number of tripped flags | ⚑ 1 red flag | 1 flag(s) | PASS |  |  |
| RY.TO | FU5w | one plain sentence per tripped flag | Debt to equity is above 2.0. | 1 sentence(s) | PASS |  |  |
| RY.TO | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| RY.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-12-03 · in 14 days. If you'll still hold on that date, the price can jump e | 2026-12-03 days_until=14 | PASS |  |  |
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
| SO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (14 days ago); no upcoming date listed. | 2026-11-05 days_until=-14 | PASS |  |  |
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
| TSLA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (29 days ago); no upcoming date listed. | 2026-10-21 days_until=-29 | PASS |  |  |
| TSLL | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| TSLL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| TSM | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +50.9% | +50.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| TSM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 41.9% | 41.9% flag=False | PASS |  |  |
| TSM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| TSM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| TSM | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| TSM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (35 days ago); no upcoming date listed. | 2026-10-15 days_until=-35 | PASS |  |  |
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
| V | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (23 days ago); no upcoming date listed. | 2026-10-27 days_until=-23 | PASS |  |  |
| VFV.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| VFV.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| VRT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +61.2% | +61.2% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| VRT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 46.6% | 46.6% flag=False | PASS |  |  |
| VRT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.61 | 0.61 flag=False | PASS |  |  |
| VRT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| VRT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| VRT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-28 (22 days ago); no upcoming date listed. | 2026-10-28 days_until=-22 | PASS |  |  |
| WDC.TO | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| WDC.TO | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| WELL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +38.4% | +38.4% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| WELL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 3.7% | 3.7% flag=False | PASS |  |  |
| WELL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.40 | 0.40 flag=False | PASS |  |  |
| WELL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| WELL | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales) · Finnhub (ROE, debt) | Finnhub, yfinance | PASS |  |  |
| WELL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-26 (24 days ago); no upcoming date listed. | 2026-10-26 days_until=-24 | PASS |  |  |
| WMT | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +5.9% | +5.9% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| WMT | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 22.3% | 22.3% flag=False | PASS |  |  |
| WMT | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.72 | 0.72 flag=False | PASS |  |  |
| WMT | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| WMT | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| WMT | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | 2026-11-19 · today. The price can jump either way on the report. | 2026-11-19 days_until=0 | PASS |  |  |
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
| XOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-30 (20 days ago); no upcoming date listed. | 2026-10-30 days_until=-20 | PASS |  |  |
| AAPL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +15.5% | TR +15.5% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AAPL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AAPL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AAPL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 16,519,610,897 | 16,519,623,951 | PASS |  |  |
| AAPL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AAPL | MR-price | price = the last completed close | 349.21 | 349.21 | PASS |  |  |
| AAPL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $349.21 needs above $10 | $349.21 needs above $10 | PASS |  |  |
| AAPL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.4 needs under 10 | 11.45 needs under 10 -> ✗ | PASS |  |  |
| AAPL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 15.5% above its 200-day average | 15.5% above | PASS |  |  |
| AAPL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $16.5B traded on an average day needs above $25M | $16,519,610,897 needs above $25,000,000 | PASS |  |  |
| AAPL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.45 | 11.45 | PASS |  |  |
| AAPL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 15.46% | 15.46% | PASS |  |  |
| AAPL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +24.6% | TR +24.6% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AAPU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 26,482,086 | 26,482,087 | PASS |  |  |
| AAPU | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| AAPU | MR-price | price = the last completed close | 47.68 | 47.68 | PASS |  |  |
| AAPU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $47.68 needs above $10 | $47.68 needs above $10 | PASS |  |  |
| AAPU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.3 needs under 10 | 9.3 needs under 10 -> ✓ | PASS |  |  |
| AAPU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 24.6% above its 200-day average | 24.6% above | PASS |  |  |
| AAPU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $26.5M traded on an average day needs above $25M | $26,482,086 needs above $25,000,000 | PASS |  |  |
| AAPU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.3 | 9.30 | PASS |  |  |
| AAPU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 24.59% | 24.59% | PASS |  |  |
| AAPU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ABBV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +18.3% | TR +18.3% | PASS | LOW | the two cards divide by different roundings of the average |
| ABBV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ABBV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ABBV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,487,256,025 | 1,487,256,022 | PASS |  |  |
| ABBV | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| ABBV | MR-price | price = the last completed close | 283.54 | 283.54 | PASS |  |  |
| ABBV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $283.54 needs above $10 | $283.54 needs above $10 | PASS |  |  |
| ABBV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.2 needs under 10 | 1.18 needs under 10 -> ✓ | PASS |  |  |
| ABBV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 18.3% above its 200-day average | 18.3% above | PASS |  |  |
| ABBV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.5B traded on an average day needs above $25M | $1,487,256,025 needs above $25,000,000 | PASS |  |  |
| ABBV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.18 | 1.18 | PASS |  |  |
| ABBV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 18.34% | 18.34% | PASS |  |  |
| ABBV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AIPO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -22.5% | TR -22.5% | PASS | LOW | the two cards divide by different roundings of the average |
| AIPO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AIPO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| AIPO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AIPO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AIPO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 45,903,152 | 45,902,528 | PASS |  |  |
| AIPO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AIPO | MR-price | price = the last completed close | 22.08 | 22.08 | PASS |  |  |
| AIPO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $22.08 needs above $10 | $22.08 needs above $10 | PASS |  |  |
| AIPO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.1 needs under 10 | 6.07 needs under 10 -> ✓ | PASS |  |  |
| AIPO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 22.5% below its 200-day average | 22.5% below | PASS |  |  |
| AIPO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $45.9M traded on an average day needs above $25M | $45,903,152 needs above $25,000,000 | PASS |  |  |
| AIPO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.07 | 6.07 | PASS |  |  |
| AIPO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -22.46% | -22.46% | PASS |  |  |
| AIPO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ALAB | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -18.2% | TR -18.2% | PASS | LOW | the two cards divide by different roundings of the average |
| ALAB | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ALAB | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| ALAB | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ALAB | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ALAB | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ALAB | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,179,769,649 | 1,179,769,649 | PASS |  |  |
| ALAB | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ALAB | MR-price | price = the last completed close | 211.6 | 211.6 | PASS |  |  |
| ALAB | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $211.60 needs above $10 | $211.60 needs above $10 | PASS |  |  |
| ALAB | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 39.3 needs under 10 | 39.26 needs under 10 -> ✗ | PASS |  |  |
| ALAB | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.2% below its 200-day average | 18.2% below | PASS |  |  |
| ALAB | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.2B traded on an average day needs above $25M | $1,179,769,649 needs above $25,000,000 | PASS |  |  |
| ALAB | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 39.26 | 39.26 | PASS |  |  |
| ALAB | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -18.19% | -18.19% | PASS |  |  |
| ALAB | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +14.1% | TR +14.1% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AMD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 19,968,479,097 | 19,973,663,184 | PASS |  |  |
| AMD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD | MR-price | price = the last completed close | 489.19 | 489.19 | PASS |  |  |
| AMD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $489.19 needs above $10 | $489.19 needs above $10 | PASS |  |  |
| AMD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 24.1 needs under 10 | 24.15 needs under 10 -> ✗ | PASS |  |  |
| AMD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 14.1% above its 200-day average | 14.1% above | PASS |  |  |
| AMD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $20B traded on an average day needs above $25M | $19,968,479,097 needs above $25,000,000 | PASS |  |  |
| AMD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 24.15 | 24.15 | PASS |  |  |
| AMD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 14.13% | 14.13% | PASS |  |  |
| AMD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +13.8% | TR +13.8% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AMD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 41,603,144 | 41,603,145 | PASS |  |  |
| AMD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD.TO | MR-price | price = the last completed close | 12.59 | 12.59 | PASS |  |  |
| AMD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $12.59 needs above $10 | $12.59 needs above $10 | PASS |  |  |
| AMD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 24.1 needs under 10 | 24.08 needs under 10 -> ✗ | PASS |  |  |
| AMD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 13.8% above its 200-day average | 13.8% above | PASS |  |  |
| AMD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $41.6M traded on an average day needs above $25M | $41,603,144 needs above $25,000,000 | PASS |  |  |
| AMD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 24.08 | 24.08 | PASS |  |  |
| AMD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13.79% | 13.78% | PASS |  |  |
| AMD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMZN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +5.0% | TR +5.0% | PASS | LOW | the two cards divide by different roundings of the average |
| AMZN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AMZN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMZN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMZN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,941,219,277 | 12,941,219,305 | PASS |  |  |
| AMZN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMZN | MR-price | price = the last completed close | 257.37 | 257.37 | PASS |  |  |
| AMZN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $257.37 needs above $10 | $257.37 needs above $10 | PASS |  |  |
| AMZN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 30.4 needs under 10 | 30.39 needs under 10 -> ✗ | PASS |  |  |
| AMZN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 5.0% above its 200-day average | 5.0% above | PASS |  |  |
| AMZN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.9B traded on an average day needs above $25M | $12,941,219,277 needs above $25,000,000 | PASS |  |  |
| AMZN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 30.39 | 30.39 | PASS |  |  |
| AMZN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 5.04% | 5.04% | PASS |  |  |
| AMZN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMZU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +0.1% | TR +0.1% | PASS | LOW | the two cards divide by different roundings of the average |
| AMZU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AMZU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMZU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMZU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMZU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 66,010,217 | 66,010,217 | PASS |  |  |
| AMZU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMZU | MR-price | price = the last completed close | 34.95 | 34.95 | PASS |  |  |
| AMZU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $34.95 needs above $10 | $34.95 needs above $10 | PASS |  |  |
| AMZU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 29.1 needs under 10 | 29.05 needs under 10 -> ✗ | PASS |  |  |
| AMZU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.1% above its 200-day average | 0.1% above | PASS |  |  |
| AMZU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $66M traded on an average day needs above $25M | $66,010,217 needs above $25,000,000 | PASS |  |  |
| AMZU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 29.05 | 29.05 | PASS |  |  |
| AMZU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.05% | 0.05% | PASS |  |  |
| AMZU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ANET.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ANET.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| ANET.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ANET.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ANET.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ANET.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ANET.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,644,527 | 2,644,528 | PASS |  |  |
| ANET.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ANET.TO | MR-price | price = the last completed close | 33.9 | 33.9 | PASS |  |  |
| ANET.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $33.90 needs above $10 | $33.90 needs above $10 | PASS |  |  |
| ANET.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 40.8 needs under 10 | 40.76 needs under 10 -> ✗ | PASS |  |  |
| ANET.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 12.2% above its 200-day average | 12.2% above | PASS |  |  |
| ANET.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.6M traded on an average day needs above $25M | $2,644,527 needs above $25,000,000 | PASS |  |  |
| ANET.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 40.76 | 40.76 | PASS |  |  |
| ANET.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 12.16% | 12.16% | PASS |  |  |
| ANET.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ASML.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -8.5% | TR -8.5% | PASS | LOW | the two cards divide by different roundings of the average |
| ASML.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-18 | 2026-11-18 | PASS |  |  |
| ASML.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| ASML.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASML.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASML.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,696,859 | 2,696,860 | PASS |  |  |
| ASML.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ASML.TO | MR-price | price = the last completed close | 41.25 | 41.25 | PASS |  |  |
| ASML.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $41.25 needs above $10 | $41.25 needs above $10 | PASS |  |  |
| ASML.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 32.2 needs under 10 | 32.18 needs under 10 -> ✗ | PASS |  |  |
| ASML.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 8.5% below its 200-day average | 8.5% below | PASS |  |  |
| ASML.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,696,859 needs above $25,000,000 | PASS |  |  |
| ASML.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 32.18 | 32.18 | PASS |  |  |
| ASML.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -8.5% | -8.50% | PASS |  |  |
| ASML.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ASTL.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +10.1% | TR +10.0% | PASS | LOW | the two cards divide by different roundings of the average |
| ASTL.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ASTL.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the price is under $10; it does not trade enough dollars a day | the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| ASTL.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASTL.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ASTL.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ASTL.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,813,256 | 5,813,256 | PASS |  |  |
| ASTL.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ASTL.TO | MR-price | price = the last completed close | 6.9 | 6.9 | PASS |  |  |
| ASTL.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $6.90 needs above $10 | $6.90 needs above $10 | PASS |  |  |
| ASTL.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.2 needs under 10 | 1.24 needs under 10 -> ✓ | PASS |  |  |
| ASTL.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 10.1% above its 200-day average | 10.1% above | PASS |  |  |
| ASTL.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $5.8M traded on an average day needs above $25M | $5,813,256 needs above $25,000,000 | PASS |  |  |
| ASTL.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.24 | 1.24 | PASS |  |  |
| ASTL.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 10.07% | 10.07% | PASS |  |  |
| ASTL.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ATD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -2.8% | TR -2.8% | PASS | LOW | the two cards divide by different roundings of the average |
| ATD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ATD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ATD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ATD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ATD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 103,729,707 | 103,729,708 | PASS |  |  |
| ATD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ATD.TO | MR-price | price = the last completed close | 80.14 | 80.14 | PASS |  |  |
| ATD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $80.14 needs above $10 | $80.14 needs above $10 | PASS |  |  |
| ATD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.9 needs under 10 | 4.93 needs under 10 -> ✓ | PASS |  |  |
| ATD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 2.8% below its 200-day average | 2.8% below | PASS |  |  |
| ATD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $103.7M traded on an average day needs above $25M | $103,729,707 needs above $25,000,000 | PASS |  |  |
| ATD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.93 | 4.93 | PASS |  |  |
| ATD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -2.81% | -2.81% | PASS |  |  |
| ATD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AVGC | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| AVGO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -5.6% | TR -5.6% | PASS | LOW | the two cards divide by different roundings of the average |
| AVGO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AVGO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| AVGO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 10,211,044,823 | 10,211,044,864 | PASS |  |  |
| AVGO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AVGO | MR-price | price = the last completed close | 346.55 | 346.55 | PASS |  |  |
| AVGO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $346.55 needs above $10 | $346.55 needs above $10 | PASS |  |  |
| AVGO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 47.4 needs under 10 | 47.35 needs under 10 -> ✗ | PASS |  |  |
| AVGO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 5.6% below its 200-day average | 5.6% below | PASS |  |  |
| AVGO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $10.2B traded on an average day needs above $25M | $10,211,044,823 needs above $25,000,000 | PASS |  |  |
| AVGO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 47.35 | 47.35 | PASS |  |  |
| AVGO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -5.56% | -5.56% | PASS |  |  |
| AVGO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AVGO.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| AVGO.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| AVGO.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AVGO.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AVGO.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 19,303,447 | 19,303,545 | PASS |  |  |
| AVGO.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AVGO.TO | MR-price | price = the last completed close | 13.13 | 13.13 | PASS |  |  |
| AVGO.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $13.13 needs above $10 | $13.13 needs above $10 | PASS |  |  |
| AVGO.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 48.1 needs under 10 | 48.13 needs under 10 -> ✗ | PASS |  |  |
| AVGO.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 6.4% below its 200-day average | 6.4% below | PASS |  |  |
| AVGO.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $19.3M traded on an average day needs above $25M | $19,303,447 needs above $25,000,000 | PASS |  |  |
| AVGO.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 48.13 | 48.13 | PASS |  |  |
| AVGO.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -6.38% | -6.38% | PASS |  |  |
| AVGO.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BDT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +21.1% | TR +21.1% | PASS | LOW | the two cards divide by different roundings of the average |
| BDT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| BDT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| BDT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BDT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BDT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 28,977,543 | 28,977,485 | PASS |  |  |
| BDT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BDT.TO | MR-price | price = the last completed close | 71.42 | 71.42 | PASS |  |  |
| BDT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $71.42 needs above $10 | $71.42 needs above $10 | PASS |  |  |
| BDT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 26.9 needs under 10 | 26.87 needs under 10 -> ✗ | PASS |  |  |
| BDT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 21.1% above its 200-day average | 21.1% above | PASS |  |  |
| BDT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $29M traded on an average day needs above $25M | $28,977,543 needs above $25,000,000 | PASS |  |  |
| BDT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 26.87 | 26.87 | PASS |  |  |
| BDT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 21.09% | 21.09% | PASS |  |  |
| BDT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BOTZ | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -19.7% | TR -19.7% | PASS | LOW | the two cards divide by different roundings of the average |
| BOTZ | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| BOTZ | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| BOTZ | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BOTZ | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BOTZ | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 28,119,840 | 28,119,841 | PASS |  |  |
| BOTZ | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BOTZ | MR-price | price = the last completed close | 29 | 29 | PASS |  |  |
| BOTZ | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $29.00 needs above $10 | $29.00 needs above $10 | PASS |  |  |
| BOTZ | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.4 needs under 10 | 1.45 needs under 10 -> ✓ | PASS |  |  |
| BOTZ | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 19.7% below its 200-day average | 19.7% below | PASS |  |  |
| BOTZ | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $28.1M traded on an average day needs above $25M | $28,119,840 needs above $25,000,000 | PASS |  |  |
| BOTZ | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.45 | 1.45 | PASS |  |  |
| BOTZ | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -19.74% | -19.74% | PASS |  |  |
| BOTZ | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BRK-B | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +13.9% | TR +13.9% | PASS | LOW | the two cards divide by different roundings of the average |
| BRK-B | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| BRK-B | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRK-B | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,959,326,692 | 2,959,326,669 | PASS |  |  |
| BRK-B | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| BRK-B | MR-price | price = the last completed close | 572.04 | 572.04 | PASS |  |  |
| BRK-B | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $572.04 needs above $10 | $572.04 needs above $10 | PASS |  |  |
| BRK-B | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.9 needs under 10 | 3.9 needs under 10 -> ✓ | PASS |  |  |
| BRK-B | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 13.9% above its 200-day average | 13.9% above | PASS |  |  |
| BRK-B | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3B traded on an average day needs above $25M | $2,959,326,692 needs above $25,000,000 | PASS |  |  |
| BRK-B | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.9 | 3.90 | PASS |  |  |
| BRK-B | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13.9% | 13.90% | PASS |  |  |
| BRK-B | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| BRKU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| BRKU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it does not trade enough dollars a day | it does not trade enough dollars a day | PASS |  |  |
| BRKU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| BRKU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| BRKU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,674,097 | 2,688,201 | PASS |  |  |
| BRKU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| BRKU | MR-price | price = the last completed close | 28.55 | 28.55 | PASS |  |  |
| BRKU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $28.55 needs above $10 | $28.55 needs above $10 | PASS |  |  |
| BRKU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.7 needs under 10 | 3.67 needs under 10 -> ✓ | PASS |  |  |
| BRKU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 23.7% above its 200-day average | 23.7% above | PASS |  |  |
| BRKU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.7M traded on an average day needs above $25M | $2,674,097 needs above $25,000,000 | PASS |  |  |
| BRKU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.67 | 3.67 | PASS |  |  |
| BRKU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CAMT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -36.7% | TR -36.7% | PASS | LOW | the two cards divide by different roundings of the average |
| CAMT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| CAMT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| CAMT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAMT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAMT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAMT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 58,500,270 | 58,516,829 | PASS |  |  |
| CAMT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CAMT | MR-price | price = the last completed close | 97.78 | 97.78 | PASS |  |  |
| CAMT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $97.78 needs above $10 | $97.78 needs above $10 | PASS |  |  |
| CAMT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 53.0 needs under 10 | 52.97 needs under 10 -> ✗ | PASS |  |  |
| CAMT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 36.7% below its 200-day average | 36.7% below | PASS |  |  |
| CAMT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $58.5M traded on an average day needs above $25M | $58,500,270 needs above $25,000,000 | PASS |  |  |
| CAMT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 52.97 | 52.97 | PASS |  |  |
| CAMT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -36.7% | -36.70% | PASS |  |  |
| CAMT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CARS.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -28.8% | TR -28.8% | PASS | LOW | the two cards divide by different roundings of the average |
| CARS.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-18 | 2026-11-18 | PASS |  |  |
| CARS.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| CARS.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CARS.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CARS.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CARS.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CARS.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 28,077 | 28,079 | PASS |  |  |
| CARS.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CARS.TO | MR-price | price = the last completed close | 19.88 | 19.88 | PASS |  |  |
| CARS.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $19.88 needs above $10 | $19.88 needs above $10 | PASS |  |  |
| CARS.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.4 needs under 10 | 7.41 needs under 10 -> ✓ | PASS |  |  |
| CARS.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 28.8% below its 200-day average | 28.8% below | PASS |  |  |
| CARS.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $28,077 traded on an average day needs above $25M | $28,077 needs above $25,000,000 | PASS |  |  |
| CARS.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.41 | 7.41 | PASS |  |  |
| CARS.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -28.84% | -28.84% | PASS |  |  |
| CARS.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CAT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -33.0% | TR -33.0% | PASS | LOW | the two cards divide by different roundings of the average |
| CAT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| CAT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CAT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CAT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CAT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,602,955,657 | 2,602,955,061 | PASS |  |  |
| CAT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CAT | MR-price | price = the last completed close | 537.26 | 537.26 | PASS |  |  |
| CAT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $537.26 needs above $10 | $537.26 needs above $10 | PASS |  |  |
| CAT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.9 needs under 10 | 1.93 needs under 10 -> ✓ | PASS |  |  |
| CAT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 33.0% below its 200-day average | 33.0% below | PASS |  |  |
| CAT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.6B traded on an average day needs above $25M | $2,602,955,657 needs above $25,000,000 | PASS |  |  |
| CAT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.93 | 1.93 | PASS |  |  |
| CAT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -33% | -33.00% | PASS |  |  |
| CAT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CCO.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -36.4% | TR -36.4% | PASS | LOW | the two cards divide by different roundings of the average |
| CCO.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-18 | 2026-11-18 | PASS |  |  |
| CCO.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CCO.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CCO.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CCO.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 156,688,022 | 156,688,021 | PASS |  |  |
| CCO.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CCO.TO | MR-price | price = the last completed close | 89.4 | 89.4 | PASS |  |  |
| CCO.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $89.40 needs above $10 | $89.40 needs above $10 | PASS |  |  |
| CCO.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.3 needs under 10 | 2.29 needs under 10 -> ✓ | PASS |  |  |
| CCO.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 36.4% below its 200-day average | 36.4% below | PASS |  |  |
| CCO.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $156.7M traded on an average day needs above $25M | $156,688,022 needs above $25,000,000 | PASS |  |  |
| CCO.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.29 | 2.29 | PASS |  |  |
| CCO.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -36.38% | -36.38% | PASS |  |  |
| CCO.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CEG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| CEG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CEG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CEG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CEG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 985,059,442 | 987,313,800 | PASS |  |  |
| CEG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CEG | MR-price | price = the last completed close | 252.03 | 252.03 | PASS |  |  |
| CEG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $252.03 needs above $10 | $252.03 needs above $10 | PASS |  |  |
| CEG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.82 needs under 10 -> ✓ | PASS |  |  |
| CEG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.2% below its 200-day average | 9.2% below | PASS |  |  |
| CEG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $985.1M traded on an average day needs above $25M | $985,059,442 needs above $25,000,000 | PASS |  |  |
| CEG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.82 | 2.81 | PASS |  |  |
| CEG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CGY.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +3.2% | TR +3.2% | PASS | LOW | the two cards divide by different roundings of the average |
| CGY.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| CGY.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it does not trade enough dollars a day | it does not trade enough dollars a day | PASS |  |  |
| CGY.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CGY.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CGY.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,433,863 | 2,433,863 | PASS |  |  |
| CGY.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CGY.TO | MR-price | price = the last completed close | 81.56 | 81.56 | PASS |  |  |
| CGY.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $81.56 needs above $10 | $81.56 needs above $10 | PASS |  |  |
| CGY.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.6 needs under 10 | 2.63 needs under 10 -> ✓ | PASS |  |  |
| CGY.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 3.2% above its 200-day average | 3.2% above | PASS |  |  |
| CGY.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.4M traded on an average day needs above $25M | $2,433,863 needs above $25,000,000 | PASS |  |  |
| CGY.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.63 | 2.63 | PASS |  |  |
| CGY.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 3.24% | 3.24% | PASS |  |  |
| CGY.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CNQ.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.3% | TR -0.3% | PASS | LOW | the two cards divide by different roundings of the average |
| CNQ.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| CNQ.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| CNQ.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CNQ.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNQ.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 649,274,429 | 649,274,423 | PASS |  |  |
| CNQ.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CNQ.TO | MR-price | price = the last completed close | 64.1 | 64.1 | PASS |  |  |
| CNQ.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $64.10 needs above $10 | $64.10 needs above $10 | PASS |  |  |
| CNQ.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.82 needs under 10 -> ✓ | PASS |  |  |
| CNQ.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.3% below its 200-day average | 0.3% below | PASS |  |  |
| CNQ.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $649.3M traded on an average day needs above $25M | $649,274,429 needs above $25,000,000 | PASS |  |  |
| CNQ.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.82 | 2.82 | PASS |  |  |
| CNQ.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.3% | -0.30% | PASS |  |  |
| CNQ.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CNR.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +10.1% | TR +10.1% | PASS | LOW | the two cards divide by different roundings of the average |
| CNR.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| CNR.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CNR.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CNR.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CNR.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 215,495,598 | 215,495,599 | PASS |  |  |
| CNR.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CNR.TO | MR-price | price = the last completed close | 178.66 | 178.66 | PASS |  |  |
| CNR.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $178.66 needs above $10 | $178.66 needs above $10 | PASS |  |  |
| CNR.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.4 needs under 10 | 11.36 needs under 10 -> ✗ | PASS |  |  |
| CNR.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 10.1% above its 200-day average | 10.1% above | PASS |  |  |
| CNR.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $215.5M traded on an average day needs above $25M | $215,495,598 needs above $25,000,000 | PASS |  |  |
| CNR.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.36 | 11.36 | PASS |  |  |
| CNR.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 10.13% | 10.13% | PASS |  |  |
| CNR.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COP | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +10.3% | TR +10.3% | PASS | LOW | the two cards divide by different roundings of the average |
| COP | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| COP | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| COP | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COP | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COP | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,038,691,646 | 1,038,683,382 | PASS |  |  |
| COP | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COP | MR-price | price = the last completed close | 134.99 | 134.99 | PASS |  |  |
| COP | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $134.99 needs above $10 | $134.99 needs above $10 | PASS |  |  |
| COP | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.4 needs under 10 | 22.4 needs under 10 -> ✗ | PASS |  |  |
| COP | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 10.3% above its 200-day average | 10.3% above | PASS |  |  |
| COP | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1B traded on an average day needs above $25M | $1,038,691,646 needs above $25,000,000 | PASS |  |  |
| COP | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.4 | 22.40 | PASS |  |  |
| COP | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 10.32% | 10.32% | PASS |  |  |
| COP | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPP.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -28.4% | TR -28.4% | PASS | LOW | the two cards divide by different roundings of the average |
| COPP.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| COPP.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| COPP.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPP.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPP.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPP.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPP.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 785,085 | 785,086 | PASS |  |  |
| COPP.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COPP.TO | MR-price | price = the last completed close | 41.83 | 41.83 | PASS |  |  |
| COPP.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $41.83 needs above $10 | $41.83 needs above $10 | PASS |  |  |
| COPP.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.7 needs under 10 | 0.7 needs under 10 -> ✓ | PASS |  |  |
| COPP.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 28.4% below its 200-day average | 28.4% below | PASS |  |  |
| COPP.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $785,085 traded on an average day needs above $25M | $785,085 needs above $25,000,000 | PASS |  |  |
| COPP.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.7 | 0.70 | PASS |  |  |
| COPP.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -28.41% | -28.41% | PASS |  |  |
| COPP.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -27.8% | TR -27.8% | PASS | LOW | the two cards divide by different roundings of the average |
| COPX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| COPX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| COPX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COPX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COPX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 264,547,281 | 264,547,282 | PASS |  |  |
| COPX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COPX | MR-price | price = the last completed close | 59.28 | 59.28 | PASS |  |  |
| COPX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $59.28 needs above $10 | $59.28 needs above $10 | PASS |  |  |
| COPX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.6 needs under 10 | 0.59 needs under 10 -> ✓ | PASS |  |  |
| COPX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 27.8% below its 200-day average | 27.8% below | PASS |  |  |
| COPX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $264.5M traded on an average day needs above $25M | $264,547,281 needs above $25,000,000 | PASS |  |  |
| COPX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.59 | 0.59 | PASS |  |  |
| COPX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -27.82% | -27.82% | PASS |  |  |
| COPX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COPZ | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| COST | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| COST | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| COST | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COST | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COST | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,601,282,431 | 2,605,188,157 | PASS |  |  |
| COST | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COST | MR-price | price = the last completed close | 1093.83 | 1093.83 | PASS |  |  |
| COST | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,093.83 needs above $10 | $1,093.83 needs above $10 | PASS |  |  |
| COST | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 18.5 needs under 10 | 18.54 needs under 10 -> ✗ | PASS |  |  |
| COST | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 12.1% above its 200-day average | 12.1% above | PASS |  |  |
| COST | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.6B traded on an average day needs above $25M | $2,601,282,431 needs above $25,000,000 | PASS |  |  |
| COST | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 18.54 | 18.54 | PASS |  |  |
| COST | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| COTG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +18.1% | TR +18.1% | PASS | LOW | the two cards divide by different roundings of the average |
| COTG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| COTG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it does not trade enough dollars a day | PASS |  |  |
| COTG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COTG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| COTG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COTG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| COTG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,037,509 | 1,037,613 | PASS |  |  |
| COTG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| COTG | MR-price | price = the last completed close | 16.45 | 16.45 | PASS |  |  |
| COTG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $16.45 needs above $10 | $16.45 needs above $10 | PASS |  |  |
| COTG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 18.1 needs under 10 | 18.13 needs under 10 -> ✗ | PASS |  |  |
| COTG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 18.1% above its 200-day average | 18.1% above | PASS |  |  |
| COTG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1M traded on an average day needs above $25M | $1,037,509 needs above $25,000,000 | PASS |  |  |
| COTG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 18.13 | 18.17 | PASS |  |  |
| COTG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 18.06% | 18.05% | PASS |  |  |
| COTG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CSU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +12.7% | TR +12.7% | PASS | LOW | the two cards divide by different roundings of the average |
| CSU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| CSU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CSU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 202,984,013 | 202,984,013 | PASS |  |  |
| CSU.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| CSU.TO | MR-price | price = the last completed close | 3180 | 3180 | PASS |  |  |
| CSU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $3,180.00 needs above $10 | $3,180.00 needs above $10 | PASS |  |  |
| CSU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.84 needs under 10 -> ✓ | PASS |  |  |
| CSU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 12.7% above its 200-day average | 12.7% above | PASS |  |  |
| CSU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $203M traded on an average day needs above $25M | $202,984,013 needs above $25,000,000 | PASS |  |  |
| CSU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.84 | 2.84 | PASS |  |  |
| CSU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 12.7% | 12.70% | PASS |  |  |
| CSU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| CVX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| CVX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| CVX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| CVX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| CVX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,817,549,719 | 1,831,969,276 | PASS |  |  |
| CVX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| CVX | MR-price | price = the last completed close | 206.5 | 206.5 | PASS |  |  |
| CVX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $206.50 needs above $10 | $206.50 needs above $10 | PASS |  |  |
| CVX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 16.7 needs under 10 | 16.69 needs under 10 -> ✗ | PASS |  |  |
| CVX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 6.9% above its 200-day average | 6.9% above | PASS |  |  |
| CVX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.8B traded on an average day needs above $25M | $1,817,549,719 needs above $25,000,000 | PASS |  |  |
| CVX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DRAL | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| DRAM | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| DRIV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.1% | TR -23.1% | PASS | LOW | the two cards divide by different roundings of the average |
| DRIV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| DRIV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| DRIV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DRIV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DRIV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DRIV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DRIV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,097,369 | 1,097,360 | PASS |  |  |
| DRIV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DRIV | MR-price | price = the last completed close | 26.26 | 26.26 | PASS |  |  |
| DRIV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $26.26 needs above $10 | $26.26 needs above $10 | PASS |  |  |
| DRIV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.4 needs under 10 | 1.38 needs under 10 -> ✓ | PASS |  |  |
| DRIV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.1% below its 200-day average | 23.1% below | PASS |  |  |
| DRIV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.1M traded on an average day needs above $25M | $1,097,369 needs above $25,000,000 | PASS |  |  |
| DRIV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.38 | 1.39 | PASS |  |  |
| DRIV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.13% | -23.13% | PASS |  |  |
| DRIV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DUK | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +3.1% | TR +3.1% | PASS | LOW | the two cards divide by different roundings of the average |
| DUK | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| DUK | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| DUK | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DUK | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 651,274,832 | 651,274,832 | PASS |  |  |
| DUK | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DUK | MR-price | price = the last completed close | 128.86 | 128.86 | PASS |  |  |
| DUK | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $128.86 needs above $10 | $128.86 needs above $10 | PASS |  |  |
| DUK | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 19.1 needs under 10 | 19.15 needs under 10 -> ✗ | PASS |  |  |
| DUK | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 3.1% above its 200-day average | 3.1% above | PASS |  |  |
| DUK | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $651.3M traded on an average day needs above $25M | $651,274,832 needs above $25,000,000 | PASS |  |  |
| DUK | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 19.15 | 19.15 | PASS |  |  |
| DUK | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 3.1% | 3.10% | PASS |  |  |
| DUK | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ELIL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +34.3% | TR +34.3% | PASS | LOW | the two cards divide by different roundings of the average |
| ELIL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ELIL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it does not trade enough dollars a day | it does not trade enough dollars a day | PASS |  |  |
| ELIL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ELIL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ELIL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,775,027 | 2,774,934 | PASS |  |  |
| ELIL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ELIL | MR-price | price = the last completed close | 36.57 | 36.57 | PASS |  |  |
| ELIL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $36.57 needs above $10 | $36.57 needs above $10 | PASS |  |  |
| ELIL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.4 needs under 10 | 2.38 needs under 10 -> ✓ | PASS |  |  |
| ELIL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 34.3% above its 200-day average | 34.3% above | PASS |  |  |
| ELIL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.8M traded on an average day needs above $25M | $2,775,027 needs above $25,000,000 | PASS |  |  |
| ELIL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.38 | 2.38 | PASS |  |  |
| ELIL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 34.27% | 34.26% | PASS |  |  |
| ELIL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| EQIX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +0.2% | TR +0.2% | PASS | LOW | the two cards divide by different roundings of the average |
| EQIX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| EQIX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| EQIX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| EQIX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| EQIX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 750,808,637 | 750,809,311 | PASS |  |  |
| EQIX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| EQIX | MR-price | price = the last completed close | 1018.45 | 1018.45 | PASS |  |  |
| EQIX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,018.45 needs above $10 | $1,018.45 needs above $10 | PASS |  |  |
| EQIX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.3 needs under 10 | 15.33 needs under 10 -> ✗ | PASS |  |  |
| EQIX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 0.2% above its 200-day average | 0.2% above | PASS |  |  |
| EQIX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $750.8M traded on an average day needs above $25M | $750,808,637 needs above $25,000,000 | PASS |  |  |
| EQIX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.33 | 15.33 | PASS |  |  |
| EQIX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 0.21% | 0.21% | PASS |  |  |
| EQIX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ETN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ETN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ETN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ETN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,141,442,244 | 1,144,485,504 | PASS |  |  |
| ETN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ETN | MR-price | price = the last completed close | 330.57 | 330.57 | PASS |  |  |
| ETN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $330.57 needs above $10 | $330.57 needs above $10 | PASS |  |  |
| ETN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.8 needs under 10 | 7.85 needs under 10 -> ✓ | PASS |  |  |
| ETN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 16.3% below its 200-day average | 16.3% below | PASS |  |  |
| ETN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,141,442,244 needs above $25,000,000 | PASS |  |  |
| ETN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.85 | 7.84 | PASS |  |  |
| ETN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| FCX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| FCX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| FCX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FCX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 851,545,928 | 851,700,793 | PASS |  |  |
| FCX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| FCX | MR-price | price = the last completed close | 49.12 | 49.12 | PASS |  |  |
| FCX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $49.12 needs above $10 | $49.12 needs above $10 | PASS |  |  |
| FCX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.4 needs under 10 | 1.42 needs under 10 -> ✓ | PASS |  |  |
| FCX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 24.2% below its 200-day average | 24.2% below | PASS |  |  |
| FCX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $851.5M traded on an average day needs above $25M | $851,545,928 needs above $25,000,000 | PASS |  |  |
| FCX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.42 | 1.42 | PASS |  |  |
| FCX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GDX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -19.3% | TR -19.3% | PASS | LOW | the two cards divide by different roundings of the average |
| GDX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GDX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GDX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,106,311,019 | 2,106,311,055 | PASS |  |  |
| GDX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GDX | MR-price | price = the last completed close | 72 | 72 | PASS |  |  |
| GDX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $72.00 needs above $10 | $72.00 needs above $10 | PASS |  |  |
| GDX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.0 needs under 10 | 3.03 needs under 10 -> ✓ | PASS |  |  |
| GDX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 19.3% below its 200-day average | 19.3% below | PASS |  |  |
| GDX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.1B traded on an average day needs above $25M | $2,106,311,019 needs above $25,000,000 | PASS |  |  |
| GDX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.03 | 3.03 | PASS |  |  |
| GDX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -19.27% | -19.27% | PASS |  |  |
| GDX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GDXU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -42.9% | TR -42.9% | PASS | LOW | the two cards divide by different roundings of the average |
| GDXU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GDXU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| GDXU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDXU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GDXU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GDXU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 8,455,396 | 8,455,396 | PASS |  |  |
| GDXU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GDXU.TO | MR-price | price = the last completed close | 20.35 | 20.35 | PASS |  |  |
| GDXU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $20.35 needs above $10 | $20.35 needs above $10 | PASS |  |  |
| GDXU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.77 needs under 10 -> ✓ | PASS |  |  |
| GDXU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 42.9% below its 200-day average | 42.9% below | PASS |  |  |
| GDXU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $8.5M traded on an average day needs above $25M | $8,455,396 needs above $25,000,000 | PASS |  |  |
| GDXU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.77 | 2.77 | PASS |  |  |
| GDXU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -42.93% | -42.93% | PASS |  |  |
| GDXU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.4% | TR -1.4% | PASS | LOW | the two cards divide by different roundings of the average |
| GE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,574,480,469 | 1,574,480,465 | PASS |  |  |
| GE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GE | MR-price | price = the last completed close | 318.88 | 318.88 | PASS |  |  |
| GE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $318.88 needs above $10 | $318.88 needs above $10 | PASS |  |  |
| GE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 11.7 needs under 10 | 11.69 needs under 10 -> ✗ | PASS |  |  |
| GE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.4% below its 200-day average | 1.4% below | PASS |  |  |
| GE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.6B traded on an average day needs above $25M | $1,574,480,469 needs above $25,000,000 | PASS |  |  |
| GE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 11.69 | 11.69 | PASS |  |  |
| GE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.44% | -1.44% | PASS |  |  |
| GE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GEV | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -20.5% | TR -20.5% | PASS | LOW | the two cards divide by different roundings of the average |
| GEV | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GEV | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GEV | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,564,648,181 | 3,564,647,516 | PASS |  |  |
| GEV | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GEV | MR-price | price = the last completed close | 756.28 | 756.28 | PASS |  |  |
| GEV | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $756.28 needs above $10 | $756.28 needs above $10 | PASS |  |  |
| GEV | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.6 needs under 10 | 15.61 needs under 10 -> ✗ | PASS |  |  |
| GEV | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.5% below its 200-day average | 20.5% below | PASS |  |  |
| GEV | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3.6B traded on an average day needs above $25M | $3,564,648,181 needs above $25,000,000 | PASS |  |  |
| GEV | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.61 | 15.61 | PASS |  |  |
| GEV | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -20.5% | -20.50% | PASS |  |  |
| GEV | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GEV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GEV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| GEV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GEV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GEV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,506,746 | 6,506,759 | PASS |  |  |
| GEV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GEV.TO | MR-price | price = the last completed close | 50.6 | 50.6 | PASS |  |  |
| GEV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $50.60 needs above $10 | $50.60 needs above $10 | PASS |  |  |
| GEV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.9 needs under 10 | 15.89 needs under 10 -> ✗ | PASS |  |  |
| GEV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 21.0% below its 200-day average | 21.0% below | PASS |  |  |
| GEV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $6.5M traded on an average day needs above $25M | $6,506,746 needs above $25,000,000 | PASS |  |  |
| GEV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.89 | 15.89 | PASS |  |  |
| GEV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -21.03% | -21.03% | PASS |  |  |
| GEV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GGLL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -41.2% | TR -41.2% | PASS | LOW | the two cards divide by different roundings of the average |
| GGLL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GGLL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GGLL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GGLL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GGLL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GGLL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 191,345,722 | 191,345,723 | PASS |  |  |
| GGLL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GGLL | MR-price | price = the last completed close | 59.74 | 59.74 | PASS |  |  |
| GGLL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $59.74 needs above $10 | $59.74 needs above $10 | PASS |  |  |
| GGLL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.8 needs under 10 | 10.78 needs under 10 -> ✗ | PASS |  |  |
| GGLL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 41.2% below its 200-day average | 41.2% below | PASS |  |  |
| GGLL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $191.3M traded on an average day needs above $25M | $191,345,722 needs above $25,000,000 | PASS |  |  |
| GGLL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.78 | 10.78 | PASS |  |  |
| GGLL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -41.18% | -41.18% | PASS |  |  |
| GGLL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GIB-A.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +12.6% | TR +12.6% | PASS | LOW | the two cards divide by different roundings of the average |
| GIB-A.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GIB-A.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GIB-A.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 76,785,063 | 76,785,064 | PASS |  |  |
| GIB-A.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| GIB-A.TO | MR-price | price = the last completed close | 112.41 | 112.41 | PASS |  |  |
| GIB-A.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $112.41 needs above $10 | $112.41 needs above $10 | PASS |  |  |
| GIB-A.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.5 needs under 10 | 3.53 needs under 10 -> ✓ | PASS |  |  |
| GIB-A.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 12.6% above its 200-day average | 12.6% above | PASS |  |  |
| GIB-A.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $76.8M traded on an average day needs above $25M | $76,785,063 needs above $25,000,000 | PASS |  |  |
| GIB-A.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.53 | 3.53 | PASS |  |  |
| GIB-A.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 12.61% | 12.61% | PASS |  |  |
| GIB-A.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GOOGL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -19.1% | TR -19.1% | PASS | LOW | the two cards divide by different roundings of the average |
| GOOGL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GOOGL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| GOOGL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GOOGL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GOOGL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GOOGL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,520,677,880 | 12,520,677,813 | PASS |  |  |
| GOOGL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GOOGL | MR-price | price = the last completed close | 272.66 | 272.66 | PASS |  |  |
| GOOGL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $272.66 needs above $10 | $272.66 needs above $10 | PASS |  |  |
| GOOGL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 10.2 needs under 10 | 10.18 needs under 10 -> ✗ | PASS |  |  |
| GOOGL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 19.1% below its 200-day average | 19.1% below | PASS |  |  |
| GOOGL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.5B traded on an average day needs above $25M | $12,520,677,880 needs above $25,000,000 | PASS |  |  |
| GOOGL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 10.18 | 10.18 | PASS |  |  |
| GOOGL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -19.1% | -19.10% | PASS |  |  |
| GOOGL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| GRID | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.3% | TR -14.3% | PASS | LOW | the two cards divide by different roundings of the average |
| GRID | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| GRID | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| GRID | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| GRID | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| GRID | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 105,078,663 | 105,078,665 | PASS |  |  |
| GRID | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| GRID | MR-price | price = the last completed close | 152.42 | 152.42 | PASS |  |  |
| GRID | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $152.42 needs above $10 | $152.42 needs above $10 | PASS |  |  |
| GRID | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.5 needs under 10 | 2.55 needs under 10 -> ✓ | PASS |  |  |
| GRID | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.3% below its 200-day average | 14.3% below | PASS |  |  |
| GRID | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $105.1M traded on an average day needs above $25M | $105,078,663 needs above $25,000,000 | PASS |  |  |
| GRID | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.55 | 2.55 | PASS |  |  |
| GRID | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.29% | -14.29% | PASS |  |  |
| GRID | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +2.4% | TR +2.4% | PASS | LOW | the two cards divide by different roundings of the average |
| HD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| HD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,623,436,019 | 1,623,436,001 | PASS |  |  |
| HD | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| HD | MR-price | price = the last completed close | 336.68 | 336.68 | PASS |  |  |
| HD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $336.68 needs above $10 | $336.68 needs above $10 | PASS |  |  |
| HD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.0 needs under 10 | 2.01 needs under 10 -> ✓ | PASS |  |  |
| HD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 2.4% above its 200-day average | 2.4% above | PASS |  |  |
| HD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.6B traded on an average day needs above $25M | $1,623,436,019 needs above $25,000,000 | PASS |  |  |
| HD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.01 | 2.01 | PASS |  |  |
| HD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.41% | 2.41% | PASS |  |  |
| HD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HURA.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -32.0% | TR -32.0% | PASS | LOW | the two cards divide by different roundings of the average |
| HURA.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| HURA.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| HURA.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HURA.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HURA.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HURA.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HURA.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 506,555 | 506,555 | PASS |  |  |
| HURA.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HURA.TO | MR-price | price = the last completed close | 35.85 | 35.85 | PASS |  |  |
| HURA.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $35.85 needs above $10 | $35.85 needs above $10 | PASS |  |  |
| HURA.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.4 needs under 10 | 1.37 needs under 10 -> ✓ | PASS |  |  |
| HURA.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 32.0% below its 200-day average | 32.0% below | PASS |  |  |
| HURA.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $506,555 traded on an average day needs above $25M | $506,555 needs above $25,000,000 | PASS |  |  |
| HURA.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.37 | 1.37 | PASS |  |  |
| HURA.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -32.02% | -32.02% | PASS |  |  |
| HURA.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| HXQ.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -2.4% | TR -2.4% | PASS | LOW | the two cards divide by different roundings of the average |
| HXQ.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| HXQ.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| HXQ.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| HXQ.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| HXQ.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,092,623 | 5,092,624 | PASS |  |  |
| HXQ.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| HXQ.TO | MR-price | price = the last completed close | 109.61 | 109.61 | PASS |  |  |
| HXQ.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $109.61 needs above $10 | $109.61 needs above $10 | PASS |  |  |
| HXQ.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 18.1 needs under 10 | 18.11 needs under 10 -> ✗ | PASS |  |  |
| HXQ.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 2.4% below its 200-day average | 2.4% below | PASS |  |  |
| HXQ.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $5.1M traded on an average day needs above $25M | $5,092,623 needs above $25,000,000 | PASS |  |  |
| HXQ.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 18.11 | 18.11 | PASS |  |  |
| HXQ.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -2.43% | -2.43% | PASS |  |  |
| HXQ.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| JNJ | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +7.2% | TR +7.2% | PASS | LOW | the two cards divide by different roundings of the average |
| JNJ | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| JNJ | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JNJ | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,072,332,468 | 2,072,332,444 | PASS |  |  |
| JNJ | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| JNJ | MR-price | price = the last completed close | 267.14 | 267.14 | PASS |  |  |
| JNJ | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $267.14 needs above $10 | $267.14 needs above $10 | PASS |  |  |
| JNJ | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.7 needs under 10 | 2.67 needs under 10 -> ✓ | PASS |  |  |
| JNJ | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 7.2% above its 200-day average | 7.2% above | PASS |  |  |
| JNJ | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.1B traded on an average day needs above $25M | $2,072,332,468 needs above $25,000,000 | PASS |  |  |
| JNJ | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.67 | 2.67 | PASS |  |  |
| JNJ | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 7.17% | 7.17% | PASS |  |  |
| JNJ | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| JPM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.8% | TR -0.8% | PASS | LOW | the two cards divide by different roundings of the average |
| JPM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| JPM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| JPM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| JPM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| JPM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,237,048,422 | 2,237,048,447 | PASS |  |  |
| JPM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| JPM | MR-price | price = the last completed close | 320.22 | 320.22 | PASS |  |  |
| JPM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $320.22 needs above $10 | $320.22 needs above $10 | PASS |  |  |
| JPM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.6 needs under 10 | 2.64 needs under 10 -> ✓ | PASS |  |  |
| JPM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.8% below its 200-day average | 0.8% below | PASS |  |  |
| JPM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.2B traded on an average day needs above $25M | $2,237,048,422 needs above $25,000,000 | PASS |  |  |
| JPM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.64 | 2.64 | PASS |  |  |
| JPM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.82% | -0.82% | PASS |  |  |
| JPM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| KEYS | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -12.5% | TR -12.5% | PASS | LOW | the two cards divide by different roundings of the average |
| KEYS | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| KEYS | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| KEYS | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| KEYS | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| KEYS | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| KEYS | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 471,982,614 | 472,499,456 | PASS |  |  |
| KEYS | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| KEYS | MR-price | price = the last completed close | 281.42 | 281.42 | PASS |  |  |
| KEYS | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $281.42 needs above $10 | $281.42 needs above $10 | PASS |  |  |
| KEYS | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.9 needs under 10 | 14.9 needs under 10 -> ✗ | PASS |  |  |
| KEYS | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 12.5% below its 200-day average | 12.5% below | PASS |  |  |
| KEYS | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $472M traded on an average day needs above $25M | $471,982,614 needs above $25,000,000 | PASS |  |  |
| KEYS | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14.9 | 14.90 | PASS |  |  |
| KEYS | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -12.53% | -12.53% | PASS |  |  |
| KEYS | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| LIN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| LIN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LIN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,090,797,448 | 1,095,039,561 | PASS |  |  |
| LIN | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| LIN | MR-price | price = the last completed close | 510.21 | 510.21 | PASS |  |  |
| LIN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $510.21 needs above $10 | $510.21 needs above $10 | PASS |  |  |
| LIN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.3 needs under 10 | 5.33 needs under 10 -> ✓ | PASS |  |  |
| LIN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 2.9% above its 200-day average | 2.9% above | PASS |  |  |
| LIN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,090,797,448 needs above $25,000,000 | PASS |  |  |
| LIN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.33 | 5.33 | PASS |  |  |
| LIN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| LLY | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| LLY | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| LLY | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 4,290,783,961 | 4,308,571,391 | PASS |  |  |
| LLY | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| LLY | MR-price | price = the last completed close | 1351.12 | 1351.12 | PASS |  |  |
| LLY | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $1,351.12 needs above $10 | $1,351.12 needs above $10 | PASS |  |  |
| LLY | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.9 needs under 10 | 2.87 needs under 10 -> ✓ | PASS |  |  |
| LLY | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 21.4% above its 200-day average | 21.4% above | PASS |  |  |
| LLY | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $4.3B traded on an average day needs above $25M | $4,290,783,961 needs above $25,000,000 | PASS |  |  |
| LLY | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.87 | 2.68 | PASS |  |  |
| LLY | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MDA.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.0% | TR -14.0% | PASS | LOW | the two cards divide by different roundings of the average |
| MDA.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| MDA.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| MDA.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MDA.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MDA.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MDA.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 56,311,264 | 56,311,265 | PASS |  |  |
| MDA.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MDA.TO | MR-price | price = the last completed close | 38.44 | 38.44 | PASS |  |  |
| MDA.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $38.44 needs above $10 | $38.44 needs above $10 | PASS |  |  |
| MDA.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 16.9 needs under 10 | 16.85 needs under 10 -> ✗ | PASS |  |  |
| MDA.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.0% below its 200-day average | 14.0% below | PASS |  |  |
| MDA.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $56.3M traded on an average day needs above $25M | $56,311,264 needs above $25,000,000 | PASS |  |  |
| MDA.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 16.85 | 16.85 | PASS |  |  |
| MDA.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14% | -14.00% | PASS |  |  |
| MDA.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| META | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -5.1% | TR -5.2% | PASS | LOW | the two cards divide by different roundings of the average |
| META | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| META | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| META | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| META | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 13,131,304,645 | 13,132,610,795 | PASS |  |  |
| META | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| META | MR-price | price = the last completed close | 596.22 | 596.22 | PASS |  |  |
| META | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $596.22 needs above $10 | $596.22 needs above $10 | PASS |  |  |
| META | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.7 needs under 10 | 4.73 needs under 10 -> ✓ | PASS |  |  |
| META | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 5.1% below its 200-day average | 5.1% below | PASS |  |  |
| META | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $13.1B traded on an average day needs above $25M | $13,131,304,645 needs above $25,000,000 | PASS |  |  |
| META | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.73 | 4.73 | PASS |  |  |
| META | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| METU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| METU | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| METU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| METU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| METU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 83,607,439 | 83,638,776 | PASS |  |  |
| METU | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| METU | MR-price | price = the last completed close | 20.01 | 20.01 | PASS |  |  |
| METU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $20.01 needs above $10 | $20.01 needs above $10 | PASS |  |  |
| METU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.8 needs under 10 | 4.8 needs under 10 -> ✓ | PASS |  |  |
| METU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 20.3% below its 200-day average | 20.3% below | PASS |  |  |
| METU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $83.6M traded on an average day needs above $25M | $83,607,439 needs above $25,000,000 | PASS |  |  |
| METU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.8 | 4.80 | PASS |  |  |
| METU | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MRVL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -26.5% | TR -26.5% | PASS | LOW | the two cards divide by different roundings of the average |
| MRVL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| MRVL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| MRVL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MRVL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MRVL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,335,874,549 | 5,338,084,256 | PASS |  |  |
| MRVL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MRVL | MR-price | price = the last completed close | 138.47 | 138.47 | PASS |  |  |
| MRVL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $138.47 needs above $10 | $138.47 needs above $10 | PASS |  |  |
| MRVL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.6 needs under 10 | 9.57 needs under 10 -> ✓ | PASS |  |  |
| MRVL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 26.5% below its 200-day average | 26.5% below | PASS |  |  |
| MRVL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.3B traded on an average day needs above $25M | $5,335,874,549 needs above $25,000,000 | PASS |  |  |
| MRVL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.57 | 9.57 | PASS |  |  |
| MRVL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -26.46% | -26.48% | PASS |  |  |
| MRVL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MSFT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +12.7% | TR +12.7% | PASS | LOW | the two cards divide by different roundings of the average |
| MSFT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| MSFT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,884,616,628 | 14,884,616,786 | PASS |  |  |
| MSFT | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| MSFT | MR-price | price = the last completed close | 498.3 | 498.3 | PASS |  |  |
| MSFT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $498.30 needs above $10 | $498.30 needs above $10 | PASS |  |  |
| MSFT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 8.0 needs under 10 | 8 needs under 10 -> ✓ | PASS |  |  |
| MSFT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 12.7% above its 200-day average | 12.7% above | PASS |  |  |
| MSFT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $14.9B traded on an average day needs above $25M | $14,884,616,628 needs above $25,000,000 | PASS |  |  |
| MSFT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 8 | 8.00 | PASS |  |  |
| MSFT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 12.66% | 12.66% | PASS |  |  |
| MSFT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| MSFU | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +16.6% | TR +16.6% | PASS | LOW | the two cards divide by different roundings of the average |
| MSFU | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| MSFU | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MSFU | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 101,112,208 | 101,112,208 | PASS |  |  |
| MSFU | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| MSFU | MR-price | price = the last completed close | 36.29 | 36.29 | PASS |  |  |
| MSFU | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $36.29 needs above $10 | $36.29 needs above $10 | PASS |  |  |
| MSFU | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.9 needs under 10 | 7.88 needs under 10 -> ✓ | PASS |  |  |
| MSFU | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 16.6% above its 200-day average | 16.6% above | PASS |  |  |
| MSFU | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $101.1M traded on an average day needs above $25M | $101,112,208 needs above $25,000,000 | PASS |  |  |
| MSFU | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.88 | 7.88 | PASS |  |  |
| MSFU | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 16.58% | 16.58% | PASS |  |  |
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
| MU.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.2% | TR -11.2% | PASS | LOW | the two cards divide by different roundings of the average |
| MU.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| MU.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| MU.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| MU.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| MU.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 81,710,266 | 81,710,266 | PASS |  |  |
| MU.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| MU.TO | MR-price | price = the last completed close | 30.13 | 30.13 | PASS |  |  |
| MU.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $30.13 needs above $10 | $30.13 needs above $10 | PASS |  |  |
| MU.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.1 needs under 10 | 5.14 needs under 10 -> ✓ | PASS |  |  |
| MU.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.2% below its 200-day average | 11.2% below | PASS |  |  |
| MU.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $81.7M traded on an average day needs above $25M | $81,710,266 needs above $25,000,000 | PASS |  |  |
| MU.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.14 | 5.14 | PASS |  |  |
| MU.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.17% | -11.16% | PASS |  |  |
| MU.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NEE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| NEE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| NEE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,079,838,285 | 1,080,025,354 | PASS |  |  |
| NEE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NEE | MR-price | price = the last completed close | 83.79 | 83.79 | PASS |  |  |
| NEE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $83.79 needs above $10 | $83.79 needs above $10 | PASS |  |  |
| NEE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 14.2 needs under 10 | 14.23 needs under 10 -> ✗ | PASS |  |  |
| NEE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 3.1% below its 200-day average | 3.1% below | PASS |  |  |
| NEE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.1B traded on an average day needs above $25M | $1,079,838,285 needs above $25,000,000 | PASS |  |  |
| NEE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 14.23 | 14.23 | PASS |  |  |
| NEE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NEM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| NEM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NEM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NEM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NEM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 820,476,507 | 820,757,260 | PASS |  |  |
| NEM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NEM | MR-price | price = the last completed close | 100.05 | 100.05 | PASS |  |  |
| NEM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $100.05 needs above $10 | $100.05 needs above $10 | PASS |  |  |
| NEM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.4 needs under 10 | 3.37 needs under 10 -> ✓ | PASS |  |  |
| NEM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 10.4% below its 200-day average | 10.4% below | PASS |  |  |
| NEM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $820.5M traded on an average day needs above $25M | $820,476,507 needs above $25,000,000 | PASS |  |  |
| NEM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.37 | 3.37 | PASS |  |  |
| NEM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NFLX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -27.0% | TR -27.0% | PASS | LOW | the two cards divide by different roundings of the average |
| NFLX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| NFLX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NFLX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFLX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFLX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,482,597,838 | 2,482,597,842 | PASS |  |  |
| NFLX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NFLX | MR-price | price = the last completed close | 58.46 | 58.46 | PASS |  |  |
| NFLX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $58.46 needs above $10 | $58.46 needs above $10 | PASS |  |  |
| NFLX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.7 needs under 10 | 4.7 needs under 10 -> ✓ | PASS |  |  |
| NFLX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 27.0% below its 200-day average | 27.0% below | PASS |  |  |
| NFLX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.5B traded on an average day needs above $25M | $2,482,597,838 needs above $25,000,000 | PASS |  |  |
| NFLX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.7 | 4.70 | PASS |  |  |
| NFLX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -26.98% | -26.98% | PASS |  |  |
| NFLX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NFXL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -52.9% | TR -52.9% | PASS | LOW | the two cards divide by different roundings of the average |
| NFXL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| NFXL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| NFXL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NFXL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NFXL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 16,313,473 | 16,313,474 | PASS |  |  |
| NFXL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NFXL | MR-price | price = the last completed close | 9.45 | 9.45 | PASS |  |  |
| NFXL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $9.45 needs above $10 | $9.45 needs above $10 | PASS |  |  |
| NFXL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.9 needs under 10 | 2.89 needs under 10 -> ✓ | PASS |  |  |
| NFXL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 52.9% below its 200-day average | 52.9% below | PASS |  |  |
| NFXL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $16.3M traded on an average day needs above $25M | $16,313,473 needs above $25,000,000 | PASS |  |  |
| NFXL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.89 | 2.89 | PASS |  |  |
| NFXL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -52.91% | -52.91% | PASS |  |  |
| NFXL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NTR.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -3.9% | TR -3.9% | PASS | LOW | the two cards divide by different roundings of the average |
| NTR.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| NTR.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NTR.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NTR.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NTR.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 128,552,560 | 128,552,562 | PASS |  |  |
| NTR.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NTR.TO | MR-price | price = the last completed close | 94 | 94 | PASS |  |  |
| NTR.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $94.00 needs above $10 | $94.00 needs above $10 | PASS |  |  |
| NTR.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.6 needs under 10 | 3.56 needs under 10 -> ✓ | PASS |  |  |
| NTR.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 3.9% below its 200-day average | 3.9% below | PASS |  |  |
| NTR.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $128.6M traded on an average day needs above $25M | $128,552,560 needs above $25,000,000 | PASS |  |  |
| NTR.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.56 | 3.56 | PASS |  |  |
| NTR.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -3.86% | -3.86% | PASS |  |  |
| NTR.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -28.2% | TR -28.2% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| NVDA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 44,994,733,608 | 44,994,733,166 | PASS |  |  |
| NVDA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDA | MR-price | price = the last completed close | 145.98 | 145.98 | PASS |  |  |
| NVDA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $145.98 needs above $10 | $145.98 needs above $10 | PASS |  |  |
| NVDA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.0 needs under 10 | 0.97 needs under 10 -> ✓ | PASS |  |  |
| NVDA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 28.2% below its 200-day average | 28.2% below | PASS |  |  |
| NVDA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $45B traded on an average day needs above $25M | $44,994,733,608 needs above $25,000,000 | PASS |  |  |
| NVDA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.97 | 0.97 | PASS |  |  |
| NVDA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -28.2% | -28.20% | PASS |  |  |
| NVDA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -54.3% | TR -54.3% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| NVDL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 671,719,215 | 671,719,222 | PASS |  |  |
| NVDL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDL | MR-price | price = the last completed close | 14.25 | 14.25 | PASS |  |  |
| NVDL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $14.25 needs above $10 | $14.25 needs above $10 | PASS |  |  |
| NVDL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.1 needs under 10 | 1.09 needs under 10 -> ✓ | PASS |  |  |
| NVDL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 54.3% below its 200-day average | 54.3% below | PASS |  |  |
| NVDL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $671.7M traded on an average day needs above $25M | $671,719,215 needs above $25,000,000 | PASS |  |  |
| NVDL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.09 | 1.09 | PASS |  |  |
| NVDL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -54.31% | -54.31% | PASS |  |  |
| NVDL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ONTO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -24.6% | TR -24.6% | PASS | LOW | the two cards divide by different roundings of the average |
| ONTO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ONTO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| ONTO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ONTO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ONTO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ONTO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 231,329,582 | 231,329,583 | PASS |  |  |
| ONTO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ONTO | MR-price | price = the last completed close | 195.93 | 195.93 | PASS |  |  |
| ONTO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $195.93 needs above $10 | $195.93 needs above $10 | PASS |  |  |
| ONTO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 22.0 needs under 10 | 22.02 needs under 10 -> ✗ | PASS |  |  |
| ONTO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 24.6% below its 200-day average | 24.6% below | PASS |  |  |
| ONTO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $231.3M traded on an average day needs above $25M | $231,329,582 needs above $25,000,000 | PASS |  |  |
| ONTO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 22.02 | 22.02 | PASS |  |  |
| ONTO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -24.64% | -24.64% | PASS |  |  |
| ONTO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ORBX.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| ORCL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -27.4% | TR -27.4% | PASS | LOW | the two cards divide by different roundings of the average |
| ORCL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| ORCL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ORCL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ORCL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ORCL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,091,743,970 | 5,091,743,959 | PASS |  |  |
| ORCL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ORCL | MR-price | price = the last completed close | 110.57 | 110.57 | PASS |  |  |
| ORCL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $110.57 needs above $10 | $110.57 needs above $10 | PASS |  |  |
| ORCL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.0 needs under 10 | 2.99 needs under 10 -> ✓ | PASS |  |  |
| ORCL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 27.4% below its 200-day average | 27.4% below | PASS |  |  |
| ORCL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.1B traded on an average day needs above $25M | $5,091,743,970 needs above $25,000,000 | PASS |  |  |
| ORCL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.99 | 2.99 | PASS |  |  |
| ORCL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -27.43% | -27.43% | PASS |  |  |
| ORCL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PG | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +13.1% | TR +13.1% | PASS | LOW | the two cards divide by different roundings of the average |
| PG | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| PG | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| PG | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PG | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PG | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,583,753,408 | 1,583,753,394 | PASS |  |  |
| PG | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PG | MR-price | price = the last completed close | 167.85 | 167.85 | PASS |  |  |
| PG | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $167.85 needs above $10 | $167.85 needs above $10 | PASS |  |  |
| PG | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.4 needs under 10 | 13.4 needs under 10 -> ✗ | PASS |  |  |
| PG | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 13.1% above its 200-day average | 13.1% above | PASS |  |  |
| PG | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.6B traded on an average day needs above $25M | $1,583,753,408 needs above $25,000,000 | PASS |  |  |
| PG | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.4 | 13.40 | PASS |  |  |
| PG | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 13.12% | 13.12% | PASS |  |  |
| PG | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PLD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -9.5% | TR -9.5% | PASS | LOW | the two cards divide by different roundings of the average |
| PLD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| PLD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| PLD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PLD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 458,936,676 | 458,936,674 | PASS |  |  |
| PLD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PLD | MR-price | price = the last completed close | 123.36 | 123.36 | PASS |  |  |
| PLD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $123.36 needs above $10 | $123.36 needs above $10 | PASS |  |  |
| PLD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.8 needs under 10 | 0.83 needs under 10 -> ✓ | PASS |  |  |
| PLD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 9.5% below its 200-day average | 9.5% below | PASS |  |  |
| PLD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $458.9M traded on an average day needs above $25M | $458,936,676 needs above $25,000,000 | PASS |  |  |
| PLD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.83 | 0.83 | PASS |  |  |
| PLD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -9.48% | -9.48% | PASS |  |  |
| PLD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PNG.V | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -56.0% | TR -56.0% | PASS | LOW | the two cards divide by different roundings of the average |
| PNG.V | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| PNG.V | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| PNG.V | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PNG.V | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PNG.V | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 3,750,837 | 3,750,838 | PASS |  |  |
| PNG.V | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PNG.V | MR-price | price = the last completed close | 2.88 | 2.88 | PASS |  |  |
| PNG.V | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $2.88 needs above $10 | $2.88 needs above $10 | PASS |  |  |
| PNG.V | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.7 needs under 10 | 0.65 needs under 10 -> ✓ | PASS |  |  |
| PNG.V | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 56.0% below its 200-day average | 56.0% below | PASS |  |  |
| PNG.V | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $3.8M traded on an average day needs above $25M | $3,750,837 needs above $25,000,000 | PASS |  |  |
| PNG.V | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.65 | 0.65 | PASS |  |  |
| PNG.V | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -56.03% | -56.03% | PASS |  |  |
| PNG.V | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QCOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| QCOM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| QCOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QCOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QCOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,372,403,801 | 2,372,588,562 | PASS |  |  |
| QCOM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QCOM | MR-price | price = the last completed close | 162.01 | 162.01 | PASS |  |  |
| QCOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $162.01 needs above $10 | $162.01 needs above $10 | PASS |  |  |
| QCOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 33.1 needs under 10 | 33.13 needs under 10 -> ✗ | PASS |  |  |
| QCOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 4.4% below its 200-day average | 4.4% below | PASS |  |  |
| QCOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.4B traded on an average day needs above $25M | $2,372,403,801 needs above $25,000,000 | PASS |  |  |
| QCOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 33.13 | 33.13 | PASS |  |  |
| QCOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QPUX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -85.8% | TR -85.8% | PASS | LOW | the two cards divide by different roundings of the average |
| QPUX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| QPUX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | it is below its 200-day average; the price is under $10; it does not trade enough dollars a day | PASS |  |  |
| QPUX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QPUX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QPUX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,566,326 | 1,566,301 | PASS |  |  |
| QPUX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QPUX | MR-price | price = the last completed close | 2.86 | 2.86 | PASS |  |  |
| QPUX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $2.86 needs above $10 | $2.86 needs above $10 | PASS |  |  |
| QPUX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.0 needs under 10 | 0.98 needs under 10 -> ✓ | PASS |  |  |
| QPUX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 85.8% below its 200-day average | 85.8% below | PASS |  |  |
| QPUX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.6M traded on an average day needs above $25M | $1,566,326 needs above $25,000,000 | PASS |  |  |
| QPUX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.98 | 0.98 | PASS |  |  |
| QPUX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -85.76% | -85.76% | PASS |  |  |
| QPUX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| QTUM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -13.3% | TR -13.3% | PASS | LOW | the two cards divide by different roundings of the average |
| QTUM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| QTUM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| QTUM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QTUM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QTUM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 48,747,226 | 48,747,226 | PASS |  |  |
| QTUM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QTUM | MR-price | price = the last completed close | 119.71 | 119.71 | PASS |  |  |
| QTUM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $119.71 needs above $10 | $119.71 needs above $10 | PASS |  |  |
| QTUM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.3 needs under 10 | 7.26 needs under 10 -> ✓ | PASS |  |  |
| QTUM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 13.3% below its 200-day average | 13.3% below | PASS |  |  |
| QTUM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $48.7M traded on an average day needs above $25M | $48,747,226 needs above $25,000,000 | PASS |  |  |
| QTUM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.26 | 7.26 | PASS |  |  |
| QTUM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -13.27% | -13.27% | PASS |  |  |
| QTUM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RBOT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -18.6% | TR -18.6% | PASS | LOW | the two cards divide by different roundings of the average |
| RBOT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-18 | 2026-11-18 | PASS |  |  |
| RBOT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| RBOT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RBOT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RBOT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RBOT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RBOT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 128,454 | 128,454 | PASS |  |  |
| RBOT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RBOT.TO | MR-price | price = the last completed close | 27.09 | 27.09 | PASS |  |  |
| RBOT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $27.09 needs above $10 | $27.09 needs above $10 | PASS |  |  |
| RBOT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.8 needs under 10 | 3.75 needs under 10 -> ✓ | PASS |  |  |
| RBOT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.6% below its 200-day average | 18.6% below | PASS |  |  |
| RBOT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $128,454 traded on an average day needs above $25M | $128,454 needs above $25,000,000 | PASS |  |  |
| RBOT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.75 | 3.75 | PASS |  |  |
| RBOT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -18.55% | -18.55% | PASS |  |  |
| RBOT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RTX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| RTX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| RTX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RTX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| RTX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RTX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,033,961,283 | 1,034,335,833 | PASS |  |  |
| RTX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| RTX | MR-price | price = the last completed close | 193.44 | 193.44 | PASS |  |  |
| RTX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $193.44 needs above $10 | $193.44 needs above $10 | PASS |  |  |
| RTX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 15.1 needs under 10 | 15.14 needs under 10 -> ✗ | PASS |  |  |
| RTX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.5% below its 200-day average | 0.5% below | PASS |  |  |
| RTX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1B traded on an average day needs above $25M | $1,033,961,283 needs above $25,000,000 | PASS |  |  |
| RTX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 15.14 | 15.14 | PASS |  |  |
| RTX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| RY.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +2.2% | TR +2.2% | PASS | LOW | the two cards divide by different roundings of the average |
| RY.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| RY.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| RY.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 982,581,561 | 982,581,559 | PASS |  |  |
| RY.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| RY.TO | MR-price | price = the last completed close | 269.45 | 269.45 | PASS |  |  |
| RY.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $269.45 needs above $10 | $269.45 needs above $10 | PASS |  |  |
| RY.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.7 needs under 10 | 0.66 needs under 10 -> ✓ | PASS |  |  |
| RY.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 2.2% above its 200-day average | 2.2% above | PASS |  |  |
| RY.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $982.6M traded on an average day needs above $25M | $982,581,561 needs above $25,000,000 | PASS |  |  |
| RY.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.66 | 0.66 | PASS |  |  |
| RY.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.17% | 2.17% | PASS |  |  |
| RY.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SETM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -36.0% | TR -36.0% | PASS | LOW | the two cards divide by different roundings of the average |
| SETM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| SETM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| SETM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SETM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SETM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SETM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SETM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 4,345,511 | 4,345,503 | PASS |  |  |
| SETM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SETM | MR-price | price = the last completed close | 20.64 | 20.64 | PASS |  |  |
| SETM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $20.64 needs above $10 | $20.64 needs above $10 | PASS |  |  |
| SETM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.8 needs under 10 | 0.82 needs under 10 -> ✓ | PASS |  |  |
| SETM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 36.0% below its 200-day average | 36.0% below | PASS |  |  |
| SETM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $4.3M traded on an average day needs above $25M | $4,345,511 needs above $25,000,000 | PASS |  |  |
| SETM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.82 | 0.82 | PASS |  |  |
| SETM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -36.01% | -36.01% | PASS |  |  |
| SETM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SGRD.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| SMH | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.8% | TR -14.8% | PASS | LOW | the two cards divide by different roundings of the average |
| SMH | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| SMH | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| SMH | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SMH | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SMH | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 5,816,396,184 | 5,816,396,187 | PASS |  |  |
| SMH | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SMH | MR-price | price = the last completed close | 447.48 | 447.48 | PASS |  |  |
| SMH | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $447.48 needs above $10 | $447.48 needs above $10 | PASS |  |  |
| SMH | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.79 needs under 10 -> ✓ | PASS |  |  |
| SMH | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.8% below its 200-day average | 14.8% below | PASS |  |  |
| SMH | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $5.8B traded on an average day needs above $25M | $5,816,396,184 needs above $25,000,000 | PASS |  |  |
| SMH | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.79 | 2.79 | PASS |  |  |
| SMH | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.78% | -14.78% | PASS |  |  |
| SMH | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SNDK.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| SO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +2.3% | TR +2.3% | PASS | LOW | the two cards divide by different roundings of the average |
| SO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| SO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| SO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 791,781,630 | 791,779,457 | PASS |  |  |
| SO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SO | MR-price | price = the last completed close | 93.29 | 93.29 | PASS |  |  |
| SO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $93.29 needs above $10 | $93.29 needs above $10 | PASS |  |  |
| SO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 33.2 needs under 10 | 33.24 needs under 10 -> ✗ | PASS |  |  |
| SO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 2.3% above its 200-day average | 2.3% above | PASS |  |  |
| SO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $791.8M traded on an average day needs above $25M | $791,781,630 needs above $25,000,000 | PASS |  |  |
| SO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 33.24 | 33.24 | PASS |  |  |
| SO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 2.26% | 2.26% | PASS |  |  |
| SO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -63.4% | TR -63.4% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| SOXL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| SOXL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 12,438,161,908 | 12,438,161,946 | PASS |  |  |
| SOXL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL | MR-price | price = the last completed close | 45.3 | 45.3 | PASS |  |  |
| SOXL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $45.30 needs above $10 | $45.30 needs above $10 | PASS |  |  |
| SOXL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 6.3 needs under 10 | 6.29 needs under 10 -> ✓ | PASS |  |  |
| SOXL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 63.4% below its 200-day average | 63.4% below | PASS |  |  |
| SOXL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $12.4B traded on an average day needs above $25M | $12,438,161,908 needs above $25,000,000 | PASS |  |  |
| SOXL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 6.29 | 6.29 | PASS |  |  |
| SOXL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -63.4% | -63.40% | PASS |  |  |
| SOXL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL.NE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -63.0% | TR -63.0% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL.NE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| SOXL.NE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| SOXL.NE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL.NE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL.NE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,152,504 | 2,152,505 | PASS |  |  |
| SOXL.NE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL.NE | MR-price | price = the last completed close | 11.42 | 11.42 | PASS |  |  |
| SOXL.NE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $11.42 needs above $10 | $11.42 needs above $10 | PASS |  |  |
| SOXL.NE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.3 needs under 10 | 7.34 needs under 10 -> ✓ | PASS |  |  |
| SOXL.NE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 63.0% below its 200-day average | 63.0% below | PASS |  |  |
| SOXL.NE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2.2M traded on an average day needs above $25M | $2,152,504 needs above $25,000,000 | PASS |  |  |
| SOXL.NE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.34 | 7.33 | PASS |  |  |
| SOXL.NE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -62.95% | -62.95% | PASS |  |  |
| SOXL.NE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.2% | TR -14.2% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| SOXX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| SOXX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,076,798,815 | 6,076,807,305 | PASS |  |  |
| SOXX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXX | MR-price | price = the last completed close | 137.95 | 137.95 | PASS |  |  |
| SOXX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $137.95 needs above $10 | $137.95 needs above $10 | PASS |  |  |
| SOXX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 7.7 needs under 10 | 7.71 needs under 10 -> ✓ | PASS |  |  |
| SOXX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.2% below its 200-day average | 14.2% below | PASS |  |  |
| SOXX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6.1B traded on an average day needs above $25M | $6,076,798,815 needs above $25,000,000 | PASS |  |  |
| SOXX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 7.71 | 7.71 | PASS |  |  |
| SOXX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.2% | -14.21% | PASS |  |  |
| SOXX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SPCL | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| TSLA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -2.0% | TR -2.0% | PASS | LOW | the two cards divide by different roundings of the average |
| TSLA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| TSLA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| TSLA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 13,864,736,706 | 13,881,302,954 | PASS |  |  |
| TSLA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSLA | MR-price | price = the last completed close | 374.41 | 374.41 | PASS |  |  |
| TSLA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $374.41 needs above $10 | $374.41 needs above $10 | PASS |  |  |
| TSLA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 17.7 needs under 10 | 17.73 needs under 10 -> ✗ | PASS |  |  |
| TSLA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 2.0% below its 200-day average | 2.0% below | PASS |  |  |
| TSLA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $13.9B traded on an average day needs above $25M | $13,864,736,706 needs above $25,000,000 | PASS |  |  |
| TSLA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 17.73 | 17.73 | PASS |  |  |
| TSLA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.97% | -1.97% | PASS |  |  |
| TSLA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| TSLL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -18.4% | TR -18.3% | PASS | LOW | the two cards divide by different roundings of the average |
| TSLL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| TSLL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; the price is under $10 | the 2-day RSI is 10 or higher; it is below its 200-day average; the price is under $10 | PASS |  |  |
| TSLL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSLL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSLL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 445,324,944 | 445,324,938 | PASS |  |  |
| TSLL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSLL | MR-price | price = the last completed close | 9.53 | 9.53 | PASS |  |  |
| TSLL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✗ $9.53 needs above $10 | $9.53 needs above $10 | PASS |  |  |
| TSLL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 17.8 needs under 10 | 17.8 needs under 10 -> ✗ | PASS |  |  |
| TSLL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 18.4% below its 200-day average | 18.4% below | PASS |  |  |
| TSLL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $445.3M traded on an average day needs above $25M | $445,324,944 needs above $25,000,000 | PASS |  |  |
| TSLL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 17.8 | 17.80 | PASS |  |  |
| TSLL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -18.35% | -18.35% | PASS |  |  |
| TSLL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| TSM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -12.5% | TR -12.5% | PASS | LOW | the two cards divide by different roundings of the average |
| TSM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| TSM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| TSM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| TSM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| TSM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 6,041,573,039 | 6,041,573,000 | PASS |  |  |
| TSM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| TSM | MR-price | price = the last completed close | 352.09 | 352.09 | PASS |  |  |
| TSM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $352.09 needs above $10 | $352.09 needs above $10 | PASS |  |  |
| TSM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.6 needs under 10 | 9.56 needs under 10 -> ✓ | PASS |  |  |
| TSM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 12.5% below its 200-day average | 12.5% below | PASS |  |  |
| TSM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $6B traded on an average day needs above $25M | $6,041,573,039 needs above $25,000,000 | PASS |  |  |
| TSM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.56 | 9.56 | PASS |  |  |
| TSM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -12.48% | -12.48% | PASS |  |  |
| TSM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| UBOT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -39.6% | TR -39.6% | PASS | LOW | the two cards divide by different roundings of the average |
| UBOT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| UBOT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| UBOT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UBOT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UBOT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UBOT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UBOT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 314,924 | 314,924 | PASS |  |  |
| UBOT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| UBOT | MR-price | price = the last completed close | 14.34 | 14.34 | PASS |  |  |
| UBOT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $14.34 needs above $10 | $14.34 needs above $10 | PASS |  |  |
| UBOT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.8 needs under 10 | 2.84 needs under 10 -> ✓ | PASS |  |  |
| UBOT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 39.6% below its 200-day average | 39.6% below | PASS |  |  |
| UBOT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $314,924 traded on an average day needs above $25M | $314,924 needs above $25,000,000 | PASS |  |  |
| UBOT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.84 | 2.84 | PASS |  |  |
| UBOT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -39.61% | -39.61% | PASS |  |  |
| UBOT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| UFO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -19.1% | TR -19.1% | PASS | LOW | the two cards divide by different roundings of the average |
| UFO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| UFO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| UFO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UFO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UFO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| UFO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| UFO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 9,091,807 | 9,091,808 | PASS |  |  |
| UFO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| UFO | MR-price | price = the last completed close | 37.97 | 37.97 | PASS |  |  |
| UFO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $37.97 needs above $10 | $37.97 needs above $10 | PASS |  |  |
| UFO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.4 needs under 10 | 1.44 needs under 10 -> ✓ | PASS |  |  |
| UFO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 19.1% below its 200-day average | 19.1% below | PASS |  |  |
| UFO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $9.1M traded on an average day needs above $25M | $9,091,807 needs above $25,000,000 | PASS |  |  |
| UFO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.44 | 1.44 | PASS |  |  |
| UFO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -19.1% | -19.10% | PASS |  |  |
| UFO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| URA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -36.9% | TR -36.9% | PASS | LOW | the two cards divide by different roundings of the average |
| URA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| URA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| URA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 157,674,836 | 157,674,836 | PASS |  |  |
| URA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| URA | MR-price | price = the last completed close | 28.66 | 28.66 | PASS |  |  |
| URA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $28.66 needs above $10 | $28.66 needs above $10 | PASS |  |  |
| URA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.3 needs under 10 | 1.26 needs under 10 -> ✓ | PASS |  |  |
| URA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 36.9% below its 200-day average | 36.9% below | PASS |  |  |
| URA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $157.7M traded on an average day needs above $25M | $157,674,836 needs above $25,000,000 | PASS |  |  |
| URA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.26 | 1.26 | PASS |  |  |
| URA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -36.91% | -36.91% | PASS |  |  |
| URA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| URAA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -64.3% | TR -64.3% | PASS | LOW | the two cards divide by different roundings of the average |
| URAA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| URAA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| URAA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URAA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| URAA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| URAA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,071,286 | 1,071,287 | PASS |  |  |
| URAA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| URAA | MR-price | price = the last completed close | 10.37 | 10.37 | PASS |  |  |
| URAA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $10.37 needs above $10 | $10.37 needs above $10 | PASS |  |  |
| URAA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.3 needs under 10 | 1.3 needs under 10 -> ✓ | PASS |  |  |
| URAA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 64.3% below its 200-day average | 64.3% below | PASS |  |  |
| URAA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.1M traded on an average day needs above $25M | $1,071,286 needs above $25,000,000 | PASS |  |  |
| URAA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.3 | 1.30 | PASS |  |  |
| URAA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -64.33% | -64.33% | PASS |  |  |
| URAA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| V | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| V | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| V | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,980,919,713 | 2,985,593,041 | PASS |  |  |
| V | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| V | MR-price | price = the last completed close | 402.25 | 402.25 | PASS |  |  |
| V | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $402.25 needs above $10 | $402.25 needs above $10 | PASS |  |  |
| V | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.9 needs under 10 | 2.91 needs under 10 -> ✓ | PASS |  |  |
| V | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 15.7% above its 200-day average | 15.7% above | PASS |  |  |
| V | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $3B traded on an average day needs above $25M | $2,980,919,713 needs above $25,000,000 | PASS |  |  |
| V | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.91 | 2.88 | PASS |  |  |
| V | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| VFV.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +1.1% | TR +1.2% | PASS | LOW | the two cards divide by different roundings of the average |
| VFV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| VFV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VFV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 72,453,553 | 72,453,553 | PASS |  |  |
| VFV.TO | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| VFV.TO | MR-price | price = the last completed close | 182.95 | 182.95 | PASS |  |  |
| VFV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $182.95 needs above $10 | $182.95 needs above $10 | PASS |  |  |
| VFV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 2.4 needs under 10 | 2.44 needs under 10 -> ✓ | PASS |  |  |
| VFV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 1.1% above its 200-day average | 1.1% above | PASS |  |  |
| VFV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $72.5M traded on an average day needs above $25M | $72,453,553 needs above $25,000,000 | PASS |  |  |
| VFV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 2.44 | 2.44 | PASS |  |  |
| VFV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 1.15% | 1.15% | PASS |  |  |
| VFV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| VRT | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -31.9% | TR -31.9% | PASS | LOW | the two cards divide by different roundings of the average |
| VRT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| VRT | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| VRT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VRT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| VRT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| VRT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,744,742,850 | 1,744,742,848 | PASS |  |  |
| VRT | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| VRT | MR-price | price = the last completed close | 184.99 | 184.99 | PASS |  |  |
| VRT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $184.99 needs above $10 | $184.99 needs above $10 | PASS |  |  |
| VRT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 19.6 needs under 10 | 19.57 needs under 10 -> ✗ | PASS |  |  |
| VRT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 31.9% below its 200-day average | 31.9% below | PASS |  |  |
| VRT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.7B traded on an average day needs above $25M | $1,744,742,850 needs above $25,000,000 | PASS |  |  |
| VRT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 19.57 | 19.57 | PASS |  |  |
| VRT | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -31.87% | -31.87% | PASS |  |  |
| VRT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| WDC.TO | MR0 | MR error state is said out loud | says so | says so | PASS |  |  |
| WELL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +9.2% | TR +9.2% | PASS | LOW | the two cards divide by different roundings of the average |
| WELL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| WELL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| WELL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| WELL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WELL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 789,052,819 | 789,052,820 | PASS |  |  |
| WELL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| WELL | MR-price | price = the last completed close | 243.19 | 243.19 | PASS |  |  |
| WELL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $243.19 needs above $10 | $243.19 needs above $10 | PASS |  |  |
| WELL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 20.3 needs under 10 | 20.29 needs under 10 -> ✗ | PASS |  |  |
| WELL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 9.3% above its 200-day average | 9.2% above | PASS |  |  |
| WELL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $789.1M traded on an average day needs above $25M | $789,052,819 needs above $25,000,000 | PASS |  |  |
| WELL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 20.29 | 20.29 | PASS |  |  |
| WELL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 9.25% | 9.25% | PASS |  |  |
| WELL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| WMT | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| WMT | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| WMT | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,816,189,142 | 2,820,826,488 | PASS |  |  |
| WMT | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| WMT | MR-price | price = the last completed close | 126.04 | 126.04 | PASS |  |  |
| WMT | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $126.04 needs above $10 | $126.04 needs above $10 | PASS |  |  |
| WMT | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 10.0 needs under 10 | 9.96 needs under 10 -> ✓ | PASS |  |  |
| WMT | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 6.2% above its 200-day average | 6.2% above | PASS |  |  |
| WMT | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.8B traded on an average day needs above $25M | $2,816,189,142 needs above $25,000,000 | PASS |  |  |
| WMT | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.96 | 9.96 | PASS |  |  |
| WMT | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XCHP.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -11.7% | TR -11.6% | PASS | LOW | the two cards divide by different roundings of the average |
| XCHP.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| XCHP.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XCHP.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XCHP.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XCHP.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XCHP.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 7,606,197 | 7,606,198 | PASS |  |  |
| XCHP.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XCHP.TO | MR-price | price = the last completed close | 103.19 | 103.19 | PASS |  |  |
| XCHP.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $103.19 needs above $10 | $103.19 needs above $10 | PASS |  |  |
| XCHP.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.7 needs under 10 | 9.67 needs under 10 -> ✓ | PASS |  |  |
| XCHP.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 11.7% below its 200-day average | 11.7% below | PASS |  |  |
| XCHP.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $7.6M traded on an average day needs above $25M | $7,606,197 needs above $25,000,000 | PASS |  |  |
| XCHP.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.67 | 9.67 | PASS |  |  |
| XCHP.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -11.65% | -11.65% | PASS |  |  |
| XCHP.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XDRV.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -16.9% | TR -16.9% | PASS | LOW | the two cards divide by different roundings of the average |
| XDRV.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| XDRV.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XDRV.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XDRV.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XDRV.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,759 | 2,759 | PASS |  |  |
| XDRV.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XDRV.TO | MR-price | price = the last completed close | 39.55 | 39.55 | PASS |  |  |
| XDRV.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $39.55 needs above $10 | $39.55 needs above $10 | PASS |  |  |
| XDRV.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 56.2 needs under 10 | 56.21 needs under 10 -> ✗ | PASS |  |  |
| XDRV.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 16.9% below its 200-day average | 16.9% below | PASS |  |  |
| XDRV.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $2,759 traded on an average day needs above $25M | $2,759 needs above $25,000,000 | PASS |  |  |
| XDRV.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 56.21 | 56.21 | PASS |  |  |
| XDRV.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -16.89% | -16.89% | PASS |  |  |
| XDRV.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XEQT.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -0.7% | TR -0.7% | PASS | LOW | the two cards divide by different roundings of the average |
| XEQT.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| XEQT.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| XEQT.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XEQT.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XEQT.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 53,006,413 | 53,005,909 | PASS |  |  |
| XEQT.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XEQT.TO | MR-price | price = the last completed close | 43.28 | 43.28 | PASS |  |  |
| XEQT.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $43.28 needs above $10 | $43.28 needs above $10 | PASS |  |  |
| XEQT.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 1.3 needs under 10 | 1.25 needs under 10 -> ✓ | PASS |  |  |
| XEQT.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 0.7% below its 200-day average | 0.7% below | PASS |  |  |
| XEQT.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $53M traded on an average day needs above $25M | $53,006,413 needs above $25,000,000 | PASS |  |  |
| XEQT.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 1.25 | 1.25 | PASS |  |  |
| XEQT.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -0.73% | -0.73% | PASS |  |  |
| XEQT.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XETM.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| XETM.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average; it does not trade enough dollars a day | it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| XETM.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XETM.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XETM.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XETM.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XETM.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 226,545 | 226,546 | PASS |  |  |
| XETM.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XETM.TO | MR-price | price = the last completed close | 56.19 | 56.19 | PASS |  |  |
| XETM.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $56.19 needs above $10 | $56.19 needs above $10 | PASS |  |  |
| XETM.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 0.8 needs under 10 | 0.77 needs under 10 -> ✓ | PASS |  |  |
| XETM.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 29.4% below its 200-day average | 29.4% below | PASS |  |  |
| XETM.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $226,545 traded on an average day needs above $25M | $226,545 needs above $25,000,000 | PASS |  |  |
| XETM.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 0.77 | 0.77 | PASS |  |  |
| XETM.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -29.4% | -29.40% | PASS |  |  |
| XETM.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XGD.TO | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -15.0% | TR -15.0% | PASS | LOW | the two cards divide by different roundings of the average |
| XGD.TO | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| XGD.TO | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| XGD.TO | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| XGD.TO | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XGD.TO | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 32,051,975 | 32,051,976 | PASS |  |  |
| XGD.TO | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| XGD.TO | MR-price | price = the last completed close | 46.79 | 46.79 | PASS |  |  |
| XGD.TO | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $46.79 needs above $10 | $46.79 needs above $10 | PASS |  |  |
| XGD.TO | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.9 needs under 10 | 3.87 needs under 10 -> ✓ | PASS |  |  |
| XGD.TO | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 15.0% below its 200-day average | 15.0% below | PASS |  |  |
| XGD.TO | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $32.1M traded on an average day needs above $25M | $32,051,975 needs above $25,000,000 | PASS |  |  |
| XGD.TO | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.87 | 3.87 | PASS |  |  |
| XGD.TO | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.99% | -14.99% | PASS |  |  |
| XGD.TO | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| XOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-19 | 2026-11-19 | PASS |  |  |
| XOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| XOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,499,338,338 | 2,520,508,308 | PASS |  |  |
| XOM | MR-head | headline = all four rules must pass | Signal: all 4 rules pass (payload signal=True) | all pass = True | PASS |  |  |
| XOM | MR-price | price = the last completed close | 158.93 | 158.93 | PASS |  |  |
| XOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $158.93 needs above $10 | $158.93 needs above $10 | PASS |  |  |
| XOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 4.8 needs under 10 | 4.78 needs under 10 -> ✓ | PASS |  |  |
| XOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 2.7% above its 200-day average | 2.7% above | PASS |  |  |
| XOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.5B traded on an average day needs above $25M | $2,499,338,338 needs above $25,000,000 | PASS |  |  |
| XOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 4.78 | 4.69 | PASS |  |  |
| XOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AAPL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AAPL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AAPL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AAPL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AAPL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AAPL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AAPL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AAPU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AAPU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AAPU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AAPU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AAPU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AAPU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AAPU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AAPU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ABBV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ABBV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ABBV | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ABBV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ABBV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ABBV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ABBV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ABBV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ABBV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ABBV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AIPO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AIPO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AIPO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AIPO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AIPO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AIPO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AIPO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AIPO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AIPO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AIPO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ALAB | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ALAB | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ALAB | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ALAB | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ALAB | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ALAB | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ALAB | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ALAB | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ALAB | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ALAB | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AMD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AMD | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AMD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AMD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AMD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AMD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AMD.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AMD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AMD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AMD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMZN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AMZN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AMZN | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMZN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMZN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AMZN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AMZN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMZN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AMZN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMZN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMZU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AMZU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AMZU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMZU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMZU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AMZU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AMZU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AMZU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AMZU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMZU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ANET.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ANET.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ANET.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ANET.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ANET.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ANET.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ANET.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ANET.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ANET.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ANET.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ASML.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ASML.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ASML.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ASML.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ASML.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ASML.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ASML.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ASML.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ASML.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ASML.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ASTL.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ASTL.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ASTL.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ASTL.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ASTL.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ASTL.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ASTL.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ASTL.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ASTL.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ASTL.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ATD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ATD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ATD.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ATD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ATD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ATD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ATD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ATD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ATD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ATD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGC | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AVGC | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AVGC | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGC | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGC | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AVGC | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AVGC | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGC | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AVGC | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGC | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AVGO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AVGO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AVGO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AVGO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AVGO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AVGO.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| AVGO.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| AVGO.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGO.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AVGO.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| AVGO.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| AVGO.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| AVGO.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| AVGO.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AVGO.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BDT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| BDT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| BDT.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BDT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BDT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| BDT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| BDT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BDT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| BDT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BDT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BOTZ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| BOTZ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| BOTZ | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BOTZ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BOTZ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| BOTZ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| BOTZ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BOTZ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| BOTZ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BOTZ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BRK-B | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| BRK-B | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| BRK-B | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BRK-B | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BRK-B | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| BRK-B | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| BRK-B | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BRK-B | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| BRK-B | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BRK-B | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| BRKU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| BRKU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| BRKU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BRKU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| BRKU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| BRKU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| BRKU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| BRKU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| BRKU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| BRKU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CAMT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CAMT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CAMT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CAMT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CAMT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CAMT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CAMT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CAMT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CAMT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CAMT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CARS.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CARS.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CARS.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CARS.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CARS.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CARS.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CARS.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CARS.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CARS.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CARS.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CAT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CAT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CAT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CAT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CAT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CAT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CAT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CAT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CAT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CAT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CCO.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CCO.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CCO.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CCO.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CCO.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CCO.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CCO.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CCO.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CCO.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CCO.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CEG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CEG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CEG | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CEG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CEG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CEG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CEG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CEG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CEG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CEG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CGY.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CGY.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CGY.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CGY.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CGY.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CGY.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CGY.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CGY.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CGY.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CGY.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CNQ.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CNQ.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CNQ.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CNQ.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CNQ.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CNQ.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CNQ.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CNQ.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CNQ.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CNQ.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CNR.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CNR.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CNR.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CNR.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CNR.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CNR.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CNR.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CNR.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CNR.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CNR.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COP | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COP | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| COP | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COP | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COP | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| COP | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| COP | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COP | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| COP | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COP | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPP.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COPP.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| COPP.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPP.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPP.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| COPP.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| COPP.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPP.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| COPP.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPP.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COPX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| COPX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| COPX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| COPX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| COPX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COPZ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COPZ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| COPZ | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPZ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COPZ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| COPZ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| COPZ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COPZ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| COPZ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COPZ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COST | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COST | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| COST | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COST | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COST | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| COST | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| COST | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COST | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| COST | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COST | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| COTG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| COTG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| COTG | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COTG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| COTG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| COTG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| COTG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| COTG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| COTG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| COTG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CSU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CSU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CSU.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CSU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CSU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CSU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CSU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CSU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CSU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CSU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| CVX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| CVX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| CVX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CVX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| CVX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| CVX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| CVX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| CVX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| CVX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| CVX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRAL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| DRAL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| DRAL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRAL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRAL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| DRAL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| DRAL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRAL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| DRAL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRAL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRAM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| DRAM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| DRAM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRAM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRAM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| DRAM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| DRAM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRAM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| DRAM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRAM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DRIV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| DRIV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| DRIV | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRIV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DRIV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| DRIV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| DRIV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DRIV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| DRIV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DRIV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DUK | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| DUK | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| DUK | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DUK | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DUK | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| DUK | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| DUK | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| DUK | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| DUK | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DUK | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ELIL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ELIL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ELIL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ELIL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ELIL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ELIL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ELIL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ELIL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ELIL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ELIL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| EQIX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| EQIX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| EQIX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| EQIX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| EQIX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| EQIX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| EQIX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| EQIX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| EQIX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| EQIX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ETN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ETN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ETN | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ETN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ETN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ETN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ETN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ETN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ETN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ETN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| FCX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| FCX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| FCX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| FCX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| FCX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| FCX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| FCX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| FCX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| FCX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| FCX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GDX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GDX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GDX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GDX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GDX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GDX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GDX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GDX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GDX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GDX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GDXU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GDXU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GDXU.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GDXU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GDXU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GDXU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GDXU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GDXU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GDXU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GDXU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GE | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GEV | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GEV | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GEV | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GEV | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GEV | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GEV | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GEV | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GEV | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GEV | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GEV | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GEV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GEV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GEV.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GEV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GEV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GEV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GEV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GEV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GEV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GEV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GGLL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GGLL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GGLL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GGLL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GGLL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GGLL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GGLL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GGLL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GGLL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GGLL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GIB-A.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GIB-A.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GIB-A.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GIB-A.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GIB-A.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GIB-A.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GIB-A.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GIB-A.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GIB-A.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GIB-A.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GOOGL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GOOGL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GOOGL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GOOGL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GOOGL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GOOGL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GOOGL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GOOGL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GOOGL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GOOGL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| GRID | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| GRID | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| GRID | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GRID | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| GRID | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| GRID | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| GRID | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| GRID | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| GRID | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| GRID | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| HD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| HD | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| HD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| HD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| HD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HURA.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| HURA.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| HURA.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HURA.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HURA.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| HURA.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| HURA.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HURA.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| HURA.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HURA.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| HXQ.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| HXQ.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| HXQ.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HXQ.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| HXQ.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| HXQ.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| HXQ.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| HXQ.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| HXQ.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| HXQ.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| JNJ | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| JNJ | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| JNJ | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| JNJ | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| JNJ | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| JNJ | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| JNJ | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| JNJ | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| JNJ | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| JNJ | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| JPM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| JPM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| JPM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| JPM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| JPM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| JPM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| JPM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| JPM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| JPM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| JPM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| KEYS | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| KEYS | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| KEYS | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| KEYS | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| KEYS | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| KEYS | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| KEYS | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| KEYS | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| KEYS | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| KEYS | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| LIN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| LIN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| LIN | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| LIN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| LIN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| LIN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| LIN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| LIN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| LIN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| LIN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| LLY | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| LLY | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| LLY | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| LLY | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| LLY | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| LLY | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| LLY | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| LLY | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| LLY | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| LLY | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MDA.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MDA.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| MDA.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MDA.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MDA.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| MDA.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| MDA.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MDA.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| MDA.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MDA.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| META | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| META | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| META | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| META | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| META | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| META | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| META | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| META | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| META | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| META | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| METU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| METU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| METU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| METU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| METU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| METU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| METU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| METU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| METU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| METU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MRVL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MRVL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| MRVL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MRVL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MRVL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| MRVL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| MRVL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MRVL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| MRVL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MRVL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MSFT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MSFT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| MSFT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MSFT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MSFT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| MSFT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| MSFT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MSFT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| MSFT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MSFT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MSFU | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MSFU | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| MSFU | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MSFU | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MSFU | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| MSFU | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| MSFU | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MSFU | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| MSFU | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MSFU | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MTRX.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MTRX.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| MTRX.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MTRX.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MTRX.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| MTRX.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| MTRX.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MTRX.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| MTRX.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MTRX.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| MU.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| MU.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| MU.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MU.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| MU.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| MU.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| MU.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| MU.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| MU.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| MU.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NEE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NEE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| NEE | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NEE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NEE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| NEE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| NEE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NEE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| NEE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NEE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NEM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NEM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| NEM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NEM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NEM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| NEM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| NEM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NEM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| NEM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NEM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NFLX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NFLX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| NFLX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NFLX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NFLX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| NFLX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| NFLX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NFLX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| NFLX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NFLX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NFXL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NFXL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| NFXL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NFXL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NFXL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| NFXL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| NFXL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NFXL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| NFXL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NFXL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NTR.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NTR.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| NTR.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NTR.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NTR.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| NTR.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| NTR.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NTR.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| NTR.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NTR.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NVDA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NVDA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| NVDA | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NVDA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| NVDA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| NVDA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NVDA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| NVDA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NVDL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| NVDL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| NVDL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NVDL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| NVDL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| NVDL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| NVDL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| NVDL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ONTO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ONTO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ONTO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ONTO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ONTO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ONTO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ONTO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ONTO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ONTO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ONTO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ORBX.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ORBX.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ORBX.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ORBX.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ORBX.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ORBX.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ORBX.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ORBX.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ORBX.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ORBX.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ORCL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| ORCL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| ORCL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ORCL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ORCL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| ORCL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| ORCL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| ORCL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| ORCL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ORCL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PG | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| PG | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| PG | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PG | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PG | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| PG | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| PG | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PG | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| PG | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PG | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PLD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| PLD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| PLD | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PLD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PLD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| PLD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| PLD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PLD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| PLD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PLD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PNG.V | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| PNG.V | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| PNG.V | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PNG.V | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PNG.V | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| PNG.V | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| PNG.V | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| PNG.V | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| PNG.V | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PNG.V | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QCOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| QCOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| QCOM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QCOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QCOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| QCOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| QCOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QCOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| QCOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QCOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QPUX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| QPUX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| QPUX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QPUX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QPUX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| QPUX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| QPUX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QPUX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| QPUX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QPUX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| QTUM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| QTUM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| QTUM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QTUM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QTUM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| QTUM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| QTUM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| QTUM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| QTUM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QTUM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RBOT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| RBOT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| RBOT.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RBOT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RBOT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| RBOT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| RBOT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RBOT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| RBOT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RBOT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RTX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| RTX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| RTX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RTX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RTX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| RTX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| RTX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RTX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| RTX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RTX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| RY.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| RY.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| RY.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RY.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| RY.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| RY.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| RY.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| RY.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| RY.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| RY.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SETM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SETM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SETM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SETM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SETM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SETM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SETM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SETM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SETM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SETM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SGRD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SGRD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SGRD.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SGRD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SGRD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SGRD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SGRD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SGRD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SGRD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SGRD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SMH | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SMH | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SMH | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SMH | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SMH | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SMH | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SMH | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SMH | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SMH | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SMH | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SNDK.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SNDK.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SNDK.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SNDK.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SNDK.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SNDK.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SNDK.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SNDK.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SNDK.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SNDK.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SOXL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SOXL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SOXL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SOXL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SOXL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXL.NE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SOXL.NE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SOXL.NE | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXL.NE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL.NE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SOXL.NE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SOXL.NE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXL.NE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SOXL.NE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL.NE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SOXX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SOXX | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SOXX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SOXX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SOXX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SOXX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SPCL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| SPCL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| SPCL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SPCL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SPCL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| SPCL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| SPCL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| SPCL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| SPCL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SPCL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSLA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| TSLA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| TSLA | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSLA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSLA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| TSLA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| TSLA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSLA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| TSLA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSLA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSLL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| TSLL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| TSLL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSLL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSLL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| TSLL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| TSLL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSLL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| TSLL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSLL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| TSM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| TSM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| TSM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| TSM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| TSM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| TSM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| TSM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| TSM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| TSM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| UBOT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| UBOT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| UBOT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| UBOT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| UBOT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| UBOT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| UBOT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| UBOT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| UBOT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| UBOT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| UFO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| UFO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| UFO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| UFO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| UFO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| UFO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| UFO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| UFO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| UFO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| UFO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| URA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| URA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| URA | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| URA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| URA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| URA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| URA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| URA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| URA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| URA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| URAA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| URAA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| URAA | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| URAA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| URAA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| URAA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| URAA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| URAA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| URAA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| URAA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| V | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| V | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| V | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| V | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| V | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| V | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| V | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| V | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| V | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| V | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| VFV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| VFV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| VFV.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| VFV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| VFV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| VFV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| VFV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| VFV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| VFV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| VFV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| VRT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| VRT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| VRT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| VRT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| VRT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| VRT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| VRT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| VRT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| VRT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| VRT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WDC.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| WDC.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| WDC.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WDC.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WDC.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| WDC.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| WDC.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WDC.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| WDC.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WDC.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WELL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| WELL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| WELL | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WELL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WELL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| WELL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| WELL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WELL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| WELL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WELL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| WMT | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| WMT | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| WMT | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WMT | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| WMT | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| WMT | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| WMT | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| WMT | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| WMT | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| WMT | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XCHP.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XCHP.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| XCHP.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XCHP.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XCHP.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| XCHP.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| XCHP.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XCHP.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| XCHP.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XCHP.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XDRV.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XDRV.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| XDRV.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XDRV.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XDRV.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| XDRV.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| XDRV.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XDRV.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| XDRV.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XDRV.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XEQT.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XEQT.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| XEQT.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XEQT.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XEQT.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| XEQT.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| XEQT.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XEQT.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| XEQT.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XEQT.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XETM.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XETM.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| XETM.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XETM.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XETM.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| XETM.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| XETM.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XETM.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| XETM.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XETM.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XGD.TO | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XGD.TO | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| XGD.TO | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XGD.TO | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XGD.TO | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| XGD.TO | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| XGD.TO | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XGD.TO | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| XGD.TO | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XGD.TO | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| XOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -5.4% | ↓ below -5.4% | PASS |  |  |
| XOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -9.5% | ↓ below -9.5% | PASS |  |  |
| XOM | MB-QQQ-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| XOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -2.0% | ↓ below -2.0% | PASS |  |  |
| XOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -6.0% | ↓ below -6.0% | PASS |  |  |
| XOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Nov 5, 2026 | 2026-11-05 | PASS |  |  |
| XOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 19 close | Nov 19 | PASS |  |  |
| XOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 28.4 | 28.4 | PASS |  | same-dump comparison only: VIX moves between dumps |
| XOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
