# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-18T10:13 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 4100 · WRONG 2 (CRITICAL) · MISLEADING 21 (HIGH/LOW per row) · UNVERIFIED 9 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 117 | 5 |
| card-price-data | 234 | 0 |
| card-relative-strength | 432 | 0 |
| card-trade-setup | 928 | 0 |

Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).
Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).
NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| PLD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | WRONG | CRITICAL | nearest support flag is not on the closest zone |
| PLD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 127.82, nearest zone high 124.69 | equal | WRONG | CRITICAL | the Buy and the Support row disagree (inside-zone + width-cap split) |
| ANET.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1M | bars: $1,547,340 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| AVGC | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $56,784 | bars: $54,909 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $618,082.3 | bars: $674,054 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $165,202.88 | bars: $110,265 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| DRAL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $945,682.23 | bars: $938,220 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| HURA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $454,251.11 | bars: $451,329 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| MTRX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $248,158.47 | bars: $276,461 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ORBX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $86,196.06 | bars: $94,165 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| QPUX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $940,595.84 | bars: $998,334 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| RBOT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $77,856.66 | bars: $86,424 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SGRD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $223,657 | bars: $167,390 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SPCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $373,695.7 | bars: $383,041 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| UBOT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $235,300.8 | bars: $239,619 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| URAA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $841,494.1 | bars: $811,335 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| WDC.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $2,771,238 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| XETM.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $175,007.37 | bars: $188,363 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ANET.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 226 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| AVGO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 226 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| GEV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 226 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| MTRX.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 208 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| XETM.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 208 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| ABBV | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| BRK-B | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| DUK | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| LLY | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| PG | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ASML.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 7 differ: 37.75-39.31 x5 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| DRIV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 10 differ: 31.32-32.04 x4 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| SETM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 4 differ: 28.74-29.18 x3 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| XEQT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 13 differ: 45.2-45.56 x4 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| AAPL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $351.46 | $351.46 | PASS |  |  |
| AAPL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.13% | 0.13% | PASS |  |  |
| AAPL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| AAPL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| AAPL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $351.46 · close 0.13% above · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| AAPL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| AAPU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $48.94 | $48.94 | PASS |  |  |
| AAPU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.92% | -0.92% | PASS |  |  |
| AAPU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.35 | 0.35 | PASS |  |  |
| AAPU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| AAPU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $48.94 · close 0.92% below · broke out Nov 11 on 0.35× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| AAPU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ABBV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $298.74 | $298.74 | PASS |  |  |
| ABBV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.98% | -1.98% | PASS |  |  |
| ABBV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ABBV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ABBV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| ABBV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $298.74 · close 1.98% below · Nov 17 close | payload values | PASS |  |  |
| ABBV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AIPO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.38 | $31.38 | PASS |  |  |
| AIPO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.87% | -27.88% | PASS |  |  |
| AIPO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AIPO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AIPO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AIPO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.38 · close 27.87% below · Nov 17 close | payload values | PASS |  |  |
| AIPO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ALAB | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $401.74 | $401.74 | PASS |  |  |
| ALAB | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -47.33% | -47.33% | PASS |  |  |
| ALAB | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ALAB | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ALAB | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ALAB | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $401.74 · close 47.33% below · Nov 17 close | payload values | PASS |  |  |
| ALAB | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $658.52 | $658.52 | PASS |  |  |
| AMD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.55% | -23.55% | PASS |  |  |
| AMD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $658.52 · close 23.55% below · Nov 17 close | payload values | PASS |  |  |
| AMD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.97 | $16.97 | PASS |  |  |
| AMD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.68% | -23.69% | PASS |  |  |
| AMD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.97 · close 23.68% below · Nov 17 close | payload values | PASS |  |  |
| AMD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $278.84 | $278.84 | PASS |  |  |
| AMZN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.51% | -7.51% | PASS |  |  |
| AMZN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $278.84 · close 7.51% below · Nov 17 close | payload values | PASS |  |  |
| AMZN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $43.49 | $43.49 | PASS |  |  |
| AMZU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.95% | -18.95% | PASS |  |  |
| AMZU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $43.49 · close 18.95% below · Nov 17 close | payload values | PASS |  |  |
| AMZU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ANET.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.85 | $38.85 | PASS |  |  |
| ANET.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.23% | -14.23% | PASS |  |  |
| ANET.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ANET.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ANET.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ANET.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.85 · close 14.23% below · Nov 17 close | payload values | PASS |  |  |
| ANET.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASML.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $53.94 | $53.94 | PASS |  |  |
| ASML.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -24.36% | -24.36% | PASS |  |  |
| ASML.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ASML.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ASML.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ASML.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $53.94 · close 24.36% below · Nov 17 close | payload values | PASS |  |  |
| ASML.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $7.57 | $7.57 | PASS |  |  |
| ASTL.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.23% | -4.23% | PASS |  |  |
| ASTL.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-06 | 2026-11-06 | PASS |  |  |
| ASTL.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.8 | 1.8 | PASS |  |  |
| ASTL.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| ASTL.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $7.57 · close 4.23% below · broke out Nov 6 on 1.80× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| ASTL.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ATD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $93.43 | $93.43 | PASS |  |  |
| ATD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.47% | -10.47% | PASS |  |  |
| ATD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ATD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ATD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ATD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $93.43 · close 10.47% below · Nov 17 close | payload values | PASS |  |  |
| ATD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGC | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $30.25 | $30.25 | PASS |  |  |
| AVGC | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39.83% | -39.83% | PASS |  |  |
| AVGC | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGC | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGC | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGC | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $30.25 · close 39.83% below · Nov 17 close | payload values | PASS |  |  |
| AVGC | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $425.98 | $425.98 | PASS |  |  |
| AVGO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.81% | -19.81% | PASS |  |  |
| AVGO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $425.98 · close 19.81% below · Nov 17 close | payload values | PASS |  |  |
| AVGO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.45 | $16.45 | PASS |  |  |
| AVGO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -21.34% | -21.34% | PASS |  |  |
| AVGO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.45 · close 21.34% below · Nov 17 close | payload values | PASS |  |  |
| AVGO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BDT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -17.69% | -17.69% | PASS |  |  |
| BDT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BDT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BDT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BDT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $86.42 · close 17.69% below · Nov 17 close | payload values | PASS |  |  |
| BDT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BOTZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.15 | $38.15 | PASS |  |  |
| BOTZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.12% | -22.12% | PASS |  |  |
| BOTZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BOTZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BOTZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BOTZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.15 · close 22.12% below · Nov 17 close | payload values | PASS |  |  |
| BOTZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $559.58 | $559.58 | PASS |  |  |
| BRK-B | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 4.86% | 4.86% | PASS |  |  |
| BRK-B | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| BRK-B | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.51 | 1.51 | PASS |  |  |
| BRK-B | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| BRK-B | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $559.58 · close 4.86% above · broke out Nov 4 on 1.51× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| BRK-B | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| BRKU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $27.52 | $27.52 | PASS |  |  |
| BRKU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 9.71% | 9.70% | PASS |  |  |
| BRKU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| BRKU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.08 | 2.08 | PASS |  |  |
| BRKU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| BRKU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $27.52 · close 9.71% above · broke out Nov 4 on 2.08× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| BRKU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRKU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CAMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $178.02 | $178.02 | PASS |  |  |
| CAMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -46.66% | -46.66% | PASS |  |  |
| CAMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $178.02 · close 46.66% below · Nov 17 close | payload values | PASS |  |  |
| CAMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CARS.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $28.41 | $28.41 | PASS |  |  |
| CARS.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.04% | -30.02% | PASS |  |  |
| CARS.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CARS.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CARS.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CARS.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $28.41 · close 30.04% below · Nov 17 close | payload values | PASS |  |  |
| CARS.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CAT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $885.8 | $885.80 | PASS |  |  |
| CAT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.56% | -35.56% | PASS |  |  |
| CAT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $885.80 · close 35.56% below · Nov 17 close | payload values | PASS |  |  |
| CAT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CCO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $154.65 | $154.65 | PASS |  |  |
| CCO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -40.41% | -40.41% | PASS |  |  |
| CCO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CCO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CCO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CCO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $154.65 · close 40.41% below · Nov 17 close | payload values | PASS |  |  |
| CCO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CEG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $309.33 | $309.33 | PASS |  |  |
| CEG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.34% | -13.34% | PASS |  |  |
| CEG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CEG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CEG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CEG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $309.33 · close 13.34% below · Nov 17 close | payload values | PASS |  |  |
| CEG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CGY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.41% | -11.40% | PASS |  |  |
| CGY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CGY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CGY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CGY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $95.15 · close 11.41% below · Nov 17 close | payload values | PASS |  |  |
| CGY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $78.6 | $78.60 | PASS |  |  |
| CNQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.12% | -13.12% | PASS |  |  |
| CNQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CNQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CNQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CNQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $78.60 · close 13.12% below · Nov 17 close | payload values | PASS |  |  |
| CNQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $178.77 | $178.77 | PASS |  |  |
| CNR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.99% | 0.99% | PASS |  |  |
| CNR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| CNR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.8 | 1.8 | PASS |  |  |
| CNR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| CNR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $178.77 · close 0.99% above · broke out Nov 4 on 1.80× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| CNR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COP | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $153.27 | $153.27 | PASS |  |  |
| COP | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9% | -9.00% | PASS |  |  |
| COP | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COP | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COP | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COP | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $153.27 · close 9.00% below · Nov 17 close | payload values | PASS |  |  |
| COP | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $69.02 | $69.02 | PASS |  |  |
| COPP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.74% | -32.74% | PASS |  |  |
| COPP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $69.02 · close 32.74% below · Nov 17 close | payload values | PASS |  |  |
| COPP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $97.59 | $97.59 | PASS |  |  |
| COPX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -33.08% | -33.08% | PASS |  |  |
| COPX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $97.59 · close 33.08% below · Nov 17 close | payload values | PASS |  |  |
| COPX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.84 | $20.84 | PASS |  |  |
| COPZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -58.78% | -58.78% | PASS |  |  |
| COPZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.84 · close 58.78% below · Nov 17 close | payload values | PASS |  |  |
| COPZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1042.57 | $1,042.57 | PASS |  |  |
| COST | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 6.48% | 6.48% | PASS |  |  |
| COST | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| COST | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.17 | 1.17 | PASS |  |  |
| COST | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| COST | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,042.57 · close 6.48% above · broke out Nov 4 on 1.17× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| COST | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COTG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $15.03 | $15.03 | PASS |  |  |
| COTG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 12.63% | 12.64% | PASS |  |  |
| COTG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| COTG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.93 | 0.93 | PASS |  |  |
| COTG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| COTG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $15.03 · close 12.63% above · broke out Nov 4 on 0.93× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| COTG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COTG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CSU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $3480.23 | $3,480.23 | PASS |  |  |
| CSU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.69% | -4.69% | PASS |  |  |
| CSU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-05 | 2026-11-05 | PASS |  |  |
| CSU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.08 | 1.08 | PASS |  |  |
| CSU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| CSU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $3,480.23 · close 4.69% below · broke out Nov 5 on 1.08× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| CSU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CSU.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CVX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $236.48 | $236.48 | PASS |  |  |
| CVX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -8.61% | -8.61% | PASS |  |  |
| CVX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CVX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CVX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CVX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $236.48 · close 8.61% below · Nov 17 close | payload values | PASS |  |  |
| CVX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $13 | $13.00 | PASS |  |  |
| DRAL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -68.38% | -68.38% | PASS |  |  |
| DRAL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $13.00 · close 68.38% below · Nov 17 close | payload values | PASS |  |  |
| DRAL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $63.82 | $63.82 | PASS |  |  |
| DRAM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39% | -39.00% | PASS |  |  |
| DRAM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $63.82 · close 39.00% below · Nov 17 close | payload values | PASS |  |  |
| DRAM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRIV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.47 | $36.47 | PASS |  |  |
| DRIV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.97% | -25.97% | PASS |  |  |
| DRIV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRIV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRIV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRIV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.47 · close 25.97% below · Nov 17 close | payload values | PASS |  |  |
| DRIV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $127.67 | $127.67 | PASS |  |  |
| DUK | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 1.7% | 1.70% | PASS |  |  |
| DUK | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| DUK | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.82 | 1.82 | PASS |  |  |
| DUK | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| DUK | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $127.67 · close 1.70% above · broke out Nov 4 on 1.82× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| DUK | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ELIL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $42.23 | $42.23 | PASS |  |  |
| ELIL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.69% | -4.69% | PASS |  |  |
| ELIL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ELIL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ELIL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ELIL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $42.23 · close 4.69% below · Nov 17 close | payload values | PASS |  |  |
| ELIL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| EQIX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1103.95 | $1,103.95 | PASS |  |  |
| EQIX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -6.26% | -6.26% | PASS |  |  |
| EQIX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| EQIX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| EQIX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| EQIX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,103.95 · close 6.26% below · Nov 17 close | payload values | PASS |  |  |
| EQIX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ETN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $476.54 | $476.54 | PASS |  |  |
| ETN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.26% | -29.26% | PASS |  |  |
| ETN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ETN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ETN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ETN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $476.54 · close 29.26% below · Nov 17 close | payload values | PASS |  |  |
| ETN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FCX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $80.07 | $80.07 | PASS |  |  |
| FCX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.93% | -30.94% | PASS |  |  |
| FCX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FCX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FCX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FCX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $80.07 · close 30.93% below · Nov 17 close | payload values | PASS |  |  |
| FCX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FINN.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.83 | $35.83 | PASS |  |  |
| FINN.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.36% | -11.36% | PASS |  |  |
| FINN.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FINN.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FINN.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FINN.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.83 · close 11.36% below · Nov 17 close | payload values | PASS |  |  |
| FINN.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $105.67 | $105.67 | PASS |  |  |
| GDX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -24.7% | -24.70% | PASS |  |  |
| GDX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $105.67 · close 24.70% below · Nov 17 close | payload values | PASS |  |  |
| GDX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDXU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.45 | $46.45 | PASS |  |  |
| GDXU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -47.04% | -47.04% | PASS |  |  |
| GDXU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDXU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDXU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDXU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.45 · close 47.04% below · Nov 17 close | payload values | PASS |  |  |
| GDXU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $375.01 | $375.01 | PASS |  |  |
| GE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.96% | -12.96% | PASS |  |  |
| GE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $375.01 · close 12.96% below · Nov 17 close | payload values | PASS |  |  |
| GE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1099.02 | $1,099.02 | PASS |  |  |
| GEV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.04% | -29.04% | PASS |  |  |
| GEV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,099.02 · close 29.04% below · Nov 17 close | payload values | PASS |  |  |
| GEV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $73.78 | $73.78 | PASS |  |  |
| GEV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.34% | -29.34% | PASS |  |  |
| GEV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $73.78 · close 29.34% below · Nov 17 close | payload values | PASS |  |  |
| GEV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GGLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $111.95 | $111.95 | PASS |  |  |
| GGLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -43.68% | -43.68% | PASS |  |  |
| GGLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GGLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GGLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GGLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $111.95 · close 43.68% below · Nov 17 close | payload values | PASS |  |  |
| GGLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $116.13 | $116.13 | PASS |  |  |
| GIB-A.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.91% | -0.91% | PASS |  |  |
| GIB-A.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-06 | 2026-11-06 | PASS |  |  |
| GIB-A.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.52 | 1.52 | PASS |  |  |
| GIB-A.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| GIB-A.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $116.13 · close 0.91% below · broke out Nov 6 on 1.52× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| GIB-A.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| GOOGL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.17 | $364.17 | PASS |  |  |
| GOOGL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.06% | -23.06% | PASS |  |  |
| GOOGL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GOOGL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GOOGL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GOOGL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.17 · close 23.06% below · Nov 17 close | payload values | PASS |  |  |
| GOOGL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GRID | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $191.14 | $191.14 | PASS |  |  |
| GRID | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.83% | -18.83% | PASS |  |  |
| GRID | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GRID | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GRID | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GRID | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $191.14 · close 18.83% below · Nov 17 close | payload values | PASS |  |  |
| GRID | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $355.76 | $355.76 | PASS |  |  |
| HD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.71% | -4.71% | PASS |  |  |
| HD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $355.76 · close 4.71% below · Nov 17 close | payload values | PASS |  |  |
| HD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HURA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $56.75 | $56.75 | PASS |  |  |
| HURA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -34.11% | -34.11% | PASS |  |  |
| HURA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HURA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HURA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HURA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $56.75 · close 34.11% below · Nov 17 close | payload values | PASS |  |  |
| HURA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HXQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.82% | -13.82% | PASS |  |  |
| HXQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HXQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HXQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HXQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $128.37 · close 13.82% below · Nov 17 close | payload values | PASS |  |  |
| HXQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $282.02 | $282.02 | PASS |  |  |
| JNJ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.18% | -1.18% | PASS |  |  |
| JNJ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-09 | 2026-11-09 | PASS |  |  |
| JNJ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.96 | 0.96 | PASS |  |  |
| JNJ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| JNJ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $282.02 · close 1.18% below · broke out Nov 9 on 0.96× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| JNJ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| JPM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.68 | $364.68 | PASS |  |  |
| JPM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.52% | -9.52% | PASS |  |  |
| JPM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| JPM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| JPM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| JPM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.68 · close 9.52% below · Nov 17 close | payload values | PASS |  |  |
| JPM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| KEYS | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $389.93 | $389.93 | PASS |  |  |
| KEYS | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.05% | -27.05% | PASS |  |  |
| KEYS | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| KEYS | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| KEYS | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| KEYS | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $389.93 · close 27.05% below · Nov 17 close | payload values | PASS |  |  |
| KEYS | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LIN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $522.93 | $522.93 | PASS |  |  |
| LIN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.5% | -1.50% | PASS |  |  |
| LIN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| LIN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.14 | 1.14 | PASS |  |  |
| LIN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| LIN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $522.93 · close 1.50% below · broke out Nov 4 on 1.14× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| LIN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LIN | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| LLY | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1447.92 | $1,447.92 | PASS |  |  |
| LLY | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.24% | -2.24% | PASS |  |  |
| LLY | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| LLY | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| LLY | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| LLY | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,447.92 · close 2.24% below · Nov 17 close | payload values | PASS |  |  |
| LLY | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MDA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $51.34 | $51.34 | PASS |  |  |
| MDA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.61% | -23.61% | PASS |  |  |
| MDA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MDA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MDA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MDA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $51.34 · close 23.61% below · Nov 17 close | payload values | PASS |  |  |
| MDA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| META | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $779.82 | $779.82 | PASS |  |  |
| META | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.64% | -20.64% | PASS |  |  |
| META | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| META | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| META | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| META | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $779.82 · close 20.64% below · Nov 17 close | payload values | PASS |  |  |
| META | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| METU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.6 | $35.60 | PASS |  |  |
| METU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39.41% | -39.41% | PASS |  |  |
| METU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| METU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| METU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| METU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.60 · close 39.41% below · Nov 17 close | payload values | PASS |  |  |
| METU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MRVL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $301.2 | $301.20 | PASS |  |  |
| MRVL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -50.62% | -50.62% | PASS |  |  |
| MRVL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MRVL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MRVL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MRVL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $301.20 · close 50.62% below · Nov 17 close | payload values | PASS |  |  |
| MRVL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $551.15 | $551.15 | PASS |  |  |
| MSFT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -8.15% | -8.15% | PASS |  |  |
| MSFT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| MSFT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.3 | 2.3 | PASS |  |  |
| MSFT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| MSFT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $551.15 · close 8.15% below · broke out Nov 4 on 2.30× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| MSFT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFT | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| MSFU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $45.17 | $45.17 | PASS |  |  |
| MSFU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -17.34% | -17.33% | PASS |  |  |
| MSFU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| MSFU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.32 | 1.32 | PASS |  |  |
| MSFU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| MSFU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $45.17 · close 17.34% below · broke out Nov 4 on 1.32× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| MSFU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| MTRX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $37.54 | $37.54 | PASS |  |  |
| MTRX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.4% | -22.40% | PASS |  |  |
| MTRX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MTRX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MTRX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MTRX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $37.54 · close 22.40% below · Nov 17 close | payload values | PASS |  |  |
| MTRX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $48.54 | $48.54 | PASS |  |  |
| MU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.06% | -36.05% | PASS |  |  |
| MU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $48.54 · close 36.06% below · Nov 17 close | payload values | PASS |  |  |
| MU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $86.87 | $86.87 | PASS |  |  |
| NEE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.82% | -2.82% | PASS |  |  |
| NEE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| NEE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.29 | 2.29 | PASS |  |  |
| NEE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| NEE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $86.87 · close 2.82% below · broke out Nov 4 on 2.29× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| NEE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEE | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| NEM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $135.01 | $135.01 | PASS |  |  |
| NEM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -17.59% | -17.59% | PASS |  |  |
| NEM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NEM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NEM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NEM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $135.01 · close 17.59% below · Nov 17 close | payload values | PASS |  |  |
| NEM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFLX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $83.6 | $83.60 | PASS |  |  |
| NFLX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.61% | -28.61% | PASS |  |  |
| NFLX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFLX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFLX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFLX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $83.60 · close 28.61% below · Nov 17 close | payload values | PASS |  |  |
| NFLX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.33 | $20.33 | PASS |  |  |
| NFXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -51.51% | -51.50% | PASS |  |  |
| NFXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.33 · close 51.51% below · Nov 17 close | payload values | PASS |  |  |
| NFXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NTR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $112.9 | $112.90 | PASS |  |  |
| NTR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.29% | -12.29% | PASS |  |  |
| NTR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NTR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NTR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NTR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $112.90 · close 12.29% below · Nov 17 close | payload values | PASS |  |  |
| NTR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.37 | $243.37 | PASS |  |  |
| NVDA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.12% | -36.12% | PASS |  |  |
| NVDA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.37 · close 36.12% below · Nov 17 close | payload values | PASS |  |  |
| NVDA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $41.59 | $41.59 | PASS |  |  |
| NVDL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -61% | -61.00% | PASS |  |  |
| NVDL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $41.59 · close 61.00% below · Nov 17 close | payload values | PASS |  |  |
| NVDL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ONTO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $353.84 | $353.84 | PASS |  |  |
| ONTO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -43.6% | -43.60% | PASS |  |  |
| ONTO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ONTO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ONTO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ONTO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $353.84 · close 43.60% below · Nov 17 close | payload values | PASS |  |  |
| ONTO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORBX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $19.64 | $19.64 | PASS |  |  |
| ORBX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.37% | -26.37% | PASS |  |  |
| ORBX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORBX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORBX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORBX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $19.64 · close 26.37% below · Nov 17 close | payload values | PASS |  |  |
| ORBX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $170.07 | $170.07 | PASS |  |  |
| ORCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.38% | -32.38% | PASS |  |  |
| ORCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $170.07 · close 32.38% below · Nov 17 close | payload values | PASS |  |  |
| ORCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $165.75 | $165.75 | PASS |  |  |
| PG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 3.6% | 3.60% | PASS |  |  |
| PG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| PG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.55 | 1.55 | PASS |  |  |
| PG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| PG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $165.75 · close 3.60% above · broke out Nov 4 on 1.55× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| PG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| PLD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $142.69 | $142.69 | PASS |  |  |
| PLD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12% | -12.01% | PASS |  |  |
| PLD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PLD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PLD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PLD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $142.69 · close 12.00% below · Nov 17 close | payload values | PASS |  |  |
| PLD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PNG.V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $6.8 | $6.80 | PASS |  |  |
| PNG.V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -54.12% | -54.12% | PASS |  |  |
| PNG.V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PNG.V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PNG.V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PNG.V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $6.80 · close 54.12% below · Nov 17 close | payload values | PASS |  |  |
| PNG.V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QCOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $205.85 | $205.85 | PASS |  |  |
| QCOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.03% | -19.03% | PASS |  |  |
| QCOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QCOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QCOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QCOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $205.85 · close 19.03% below · Nov 17 close | payload values | PASS |  |  |
| QCOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QPUX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $22.2 | $22.20 | PASS |  |  |
| QPUX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -85.05% | -85.05% | PASS |  |  |
| QPUX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QPUX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QPUX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QPUX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $22.20 · close 85.05% below · Nov 17 close | payload values | PASS |  |  |
| QPUX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QTUM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $159.25 | $159.25 | PASS |  |  |
| QTUM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.13% | -23.13% | PASS |  |  |
| QTUM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QTUM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QTUM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QTUM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $159.25 · close 23.13% below · Nov 17 close | payload values | PASS |  |  |
| QTUM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RBOT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $34.84 | $34.84 | PASS |  |  |
| RBOT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.24% | -22.24% | PASS |  |  |
| RBOT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RBOT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RBOT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RBOT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $34.84 · close 22.24% below · Nov 17 close | payload values | PASS |  |  |
| RBOT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RTX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $226.41 | $226.41 | PASS |  |  |
| RTX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.55% | -12.55% | PASS |  |  |
| RTX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RTX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RTX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RTX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $226.41 · close 12.55% below · Nov 17 close | payload values | PASS |  |  |
| RTX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.46 | $300.46 | PASS |  |  |
| RY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -6.48% | -6.48% | PASS |  |  |
| RY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.46 · close 6.48% below · Nov 17 close | payload values | PASS |  |  |
| RY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SETM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.24 | $36.24 | PASS |  |  |
| SETM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -38.99% | -38.99% | PASS |  |  |
| SETM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SETM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SETM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SETM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.24 · close 38.99% below · Nov 17 close | payload values | PASS |  |  |
| SETM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SGRD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $21.32 | $21.32 | PASS |  |  |
| SGRD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -15.79% | -15.81% | PASS |  |  |
| SGRD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SGRD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SGRD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SGRD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $21.32 · close 15.79% below · Nov 17 close | payload values | PASS |  |  |
| SGRD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SMH | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $639.47 | $639.47 | PASS |  |  |
| SMH | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.05% | -28.05% | PASS |  |  |
| SMH | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SMH | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SMH | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SMH | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $639.47 · close 28.05% below · Nov 17 close | payload values | PASS |  |  |
| SMH | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SNDK.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.35 | $46.35 | PASS |  |  |
| SNDK.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -58.4% | -58.40% | PASS |  |  |
| SNDK.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SNDK.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SNDK.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SNDK.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.35 · close 58.40% below · Nov 17 close | payload values | PASS |  |  |
| SNDK.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $94.08 | $94.08 | PASS |  |  |
| SO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.51% | -0.51% | PASS |  |  |
| SO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.86 | 1.86 | PASS |  |  |
| SO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| SO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $94.08 · close 0.51% below · broke out Nov 16 on 1.86× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| SO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| SOXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $169.83 | $169.83 | PASS |  |  |
| SOXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -71.11% | -71.11% | PASS |  |  |
| SOXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $169.83 · close 71.11% below · Nov 17 close | payload values | PASS |  |  |
| SOXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $40.79 | $40.79 | PASS |  |  |
| SOXL.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -69.7% | -69.70% | PASS |  |  |
| SOXL.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $40.79 · close 69.70% below · Nov 17 close | payload values | PASS |  |  |
| SOXL.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $198.81 | $198.81 | PASS |  |  |
| SOXX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.85% | -28.85% | PASS |  |  |
| SOXX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $198.81 · close 28.85% below · Nov 17 close | payload values | PASS |  |  |
| SOXX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SPCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.54 | $33.54 | PASS |  |  |
| SPCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -69.8% | -69.80% | PASS |  |  |
| SPCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SPCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SPCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SPCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.54 · close 69.80% below · Nov 17 close | payload values | PASS |  |  |
| SPCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $414.23 | $414.23 | PASS |  |  |
| TSLA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -8.24% | -8.24% | PASS |  |  |
| TSLA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $414.23 · close 8.24% below · Nov 17 close | payload values | PASS |  |  |
| TSLA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $11.98 | $11.98 | PASS |  |  |
| TSLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.11% | -18.11% | PASS |  |  |
| TSLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $11.98 · close 18.11% below · Nov 17 close | payload values | PASS |  |  |
| TSLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $487.47 | $487.47 | PASS |  |  |
| TSM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.21% | -26.21% | PASS |  |  |
| TSM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $487.47 · close 26.21% below · Nov 17 close | payload values | PASS |  |  |
| TSM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UBOT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $25.62 | $25.62 | PASS |  |  |
| UBOT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -41.31% | -41.30% | PASS |  |  |
| UBOT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UBOT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UBOT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UBOT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $25.62 · close 41.31% below · Nov 17 close | payload values | PASS |  |  |
| UBOT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UFO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.29 | $49.29 | PASS |  |  |
| UFO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.26% | -20.27% | PASS |  |  |
| UFO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UFO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UFO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UFO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.29 · close 20.26% below · Nov 17 close | payload values | PASS |  |  |
| UFO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| URA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $50.09 | $50.09 | PASS |  |  |
| URA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -40.03% | -40.03% | PASS |  |  |
| URA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| URA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| URA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| URA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $50.09 · close 40.03% below · Nov 17 close | payload values | PASS |  |  |
| URA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| URAA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.45 | $31.45 | PASS |  |  |
| URAA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -63.82% | -63.82% | PASS |  |  |
| URAA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| URAA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| URAA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| URAA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.45 · close 63.82% below · Nov 17 close | payload values | PASS |  |  |
| URAA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $425.99 | $425.99 | PASS |  |  |
| V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.16% | -2.16% | PASS |  |  |
| V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.57 | 1.57 | PASS |  |  |
| V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $425.99 · close 2.16% below · broke out Nov 4 on 1.57× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| V | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| VFV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.91% | -5.91% | PASS |  |  |
| VFV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VFV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VFV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VFV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $197.83 · close 5.91% below · Nov 17 close | payload values | PASS |  |  |
| VFV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| VRT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.23 | $300.23 | PASS |  |  |
| VRT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.59% | -36.59% | PASS |  |  |
| VRT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VRT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VRT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VRT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.23 · close 36.59% below · Nov 17 close | payload values | PASS |  |  |
| VRT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WDC.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.32 | $33.32 | PASS |  |  |
| WDC.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -48.59% | -48.59% | PASS |  |  |
| WDC.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WDC.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WDC.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| WDC.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.32 · close 48.59% below · Nov 17 close | payload values | PASS |  |  |
| WDC.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WELL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $242.2 | $242.20 | PASS |  |  |
| WELL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 1.47% | 1.47% | PASS |  |  |
| WELL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| WELL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.46 | 1.46 | PASS |  |  |
| WELL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| WELL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $242.20 · close 1.47% above · broke out Nov 4 on 1.46× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| WELL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WELL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| WMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $127.94 | $127.94 | PASS |  |  |
| WMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.33% | -0.33% | PASS |  |  |
| WMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| WMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.32 | 1.32 | PASS |  |  |
| WMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| WMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $127.94 · close 0.33% below · broke out Nov 4 on 1.32× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| WMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WMT | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| XCHP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $147.5 | $147.50 | PASS |  |  |
| XCHP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.54% | -28.54% | PASS |  |  |
| XCHP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XCHP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XCHP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XCHP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $147.50 · close 28.54% below · Nov 17 close | payload values | PASS |  |  |
| XCHP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XDRV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.26 | $49.26 | PASS |  |  |
| XDRV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.32% | -20.32% | PASS |  |  |
| XDRV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XDRV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XDRV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XDRV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.26 · close 20.32% below · Nov 17 close | payload values | PASS |  |  |
| XDRV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XEQT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.4% | -4.40% | PASS |  |  |
| XEQT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XEQT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XEQT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XEQT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.38 · close 4.40% below · Nov 17 close | payload values | PASS |  |  |
| XEQT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XETM.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $91.8 | $91.80 | PASS |  |  |
| XETM.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -33.37% | -33.37% | PASS |  |  |
| XETM.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XETM.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XETM.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XETM.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $91.80 · close 33.37% below · Nov 17 close | payload values | PASS |  |  |
| XETM.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XGD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $65.29 | $65.29 | PASS |  |  |
| XGD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -21.46% | -21.46% | PASS |  |  |
| XGD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XGD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XGD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XGD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $65.29 · close 21.46% below · Nov 17 close | payload values | PASS |  |  |
| XGD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $187.32 | $187.32 | PASS |  |  |
| XOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.73% | -10.74% | PASS |  |  |
| XOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $187.32 · close 10.73% below · Nov 17 close | payload values | PASS |  |  |
| XOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $351.91 · Nov 17 | $351.91 · Nov 17 | PASS |  |  |
| AAPU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $48.49 · Nov 17 | $48.49 · Nov 17 | PASS |  |  |
| ABBV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.49 / Mom: +1.18 / Rank: 2/11] XLV LEADING | RS 105.49 Mom 1.18 Rank 2/11 | PASS |  |  |
| ABBV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| ABBV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ABBV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $292.82 · Nov 17 | $292.82 · Nov 17 | PASS |  |  |
| AIPO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AIPO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $22.63 · Nov 17 | $22.63 · Nov 17 | PASS |  |  |
| ALAB | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| ALAB | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ALAB | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ALAB | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $211.60 · Nov 17 | $211.60 · Nov 17 | PASS |  |  |
| AMD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AMD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $503.41 · Nov 17 | $503.41 · Nov 17 | PASS |  |  |
| AMD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AMD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.95 · Nov 17 | $12.95 · Nov 17 | PASS |  |  |
| AMZN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.25 / Rank: 7/11] X | RS 98.43 Mom 2.25 Rank 7/11 | PASS |  |  |
| AMZN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| AMZN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $257.89 · Nov 17 | $257.89 · Nov 17 | PASS |  |  |
| AMZU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $35.25 · Nov 17 | $35.25 · Nov 17 | PASS |  |  |
| ANET.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ANET.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $33.32 · Nov 17 | $33.32 · Nov 17 | PASS |  |  |
| ASML.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASML.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $40.80 · Nov 17 | $40.80 · Nov 17 | PASS |  |  |
| ASTL.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.66 / Mom: +0.7 / Rank: 6/11] XLB IMPROVING | RS 98.66 Mom 0.7 Rank 6/11 | PASS |  |  |
| ASTL.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ASTL.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $7.25 · Nov 17 | $7.25 · Nov 17 | PASS |  |  |
| ATD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.25 / Rank: 7/11] X | RS 98.43 Mom 2.25 Rank 7/11 | PASS |  |  |
| ATD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ATD.TO | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 6 days | 📅 Earnings in 6 days | PASS |  |  |
| ATD.TO | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 6 days | 2026-11-24, 6 days | PASS |  |  |
| ATD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $83.65 · Nov 17 | $83.65 · Nov 17 | PASS |  |  |
| AVGC | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGC | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $18.20 · Nov 17 | $18.20 · Nov 17 | PASS |  |  |
| AVGO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AVGO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AVGO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $341.60 · Nov 17 | $341.60 · Nov 17 | PASS |  |  |
| AVGO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGO.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.94 · Nov 17 | $12.94 · Nov 17 | PASS |  |  |
| BDT.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| BDT.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| BDT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BDT.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $71.13 · Nov 17 | $71.13 · Nov 17 | PASS |  |  |
| BOTZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BOTZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $29.71 · Nov 17 | $29.71 · Nov 17 | PASS |  |  |
| BRK-B | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.01 / Mom: -0.46 / Rank: 4/11] XLF WEAKENIN | RS 100.01 Mom -0.46 Rank 4/11 | PASS |  |  |
| BRK-B | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| BRK-B | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRK-B | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $586.76 · Nov 17 | $586.76 · Nov 17 | PASS |  |  |
| BRKU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRKU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $30.19 · Nov 17 | $30.19 · Nov 17 | PASS |  |  |
| CAMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| CAMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAMT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $94.96 · Nov 17 | $94.96 · Nov 17 | PASS |  |  |
| CARS.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| CAT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $570.79 · Nov 17 | $570.79 · Nov 17 | PASS |  |  |
| CCO.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.44 / Mom: +0.38 / Rank: 1/11] XLE LEADING | RS 106.44 Mom 0.38 Rank 1/11 | PASS |  |  |
| CCO.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CCO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CCO.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $92.16 · Nov 17 | $92.16 · Nov 17 | PASS |  |  |
| CEG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.68 / Mom: +2.87 / Rank: 10/11] XLU IMPROVING | RS 96.68 Mom 2.87 Rank 10/11 | PASS |  |  |
| CEG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| CEG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CEG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $268.07 · Nov 17 | $268.07 · Nov 17 | PASS |  |  |
| CGY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| CGY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CGY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CGY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $84.30 · Nov 17 | $84.30 · Nov 17 | PASS |  |  |
| CNQ.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.44 / Mom: +0.38 / Rank: 1/11] XLE LEADING | RS 106.44 Mom 0.38 Rank 1/11 | PASS |  |  |
| CNQ.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CNQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNQ.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $68.29 · Nov 17 | $68.29 · Nov 17 | PASS |  |  |
| CNR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| CNR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CNR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $180.54 · Nov 17 | $180.54 · Nov 17 | PASS |  |  |
| COP | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.44 / Mom: +0.38 / Rank: 1/11] XLE LEADING | RS 106.44 Mom 0.38 Rank 1/11 | PASS |  |  |
| COP | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COP | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COP | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $139.48 · Nov 17 | $139.48 · Nov 17 | PASS |  |  |
| COPP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPP.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $46.42 · Nov 17 | $46.42 · Nov 17 | PASS |  |  |
| COPX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $65.31 · Nov 17 | $65.31 · Nov 17 | PASS |  |  |
| COPZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $8.59 · Nov 17 | $8.59 · Nov 17 | PASS |  |  |
| COST | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.52 / Mom: +3.17 / Rank: 3/11] XLP LE | RS 101.52 Mom 3.17 Rank 3/11 | PASS |  |  |
| COST | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COST | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COST | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,110.08 · Nov 17 | $1,110.08 · Nov 17 | PASS |  |  |
| COTG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COTG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $16.93 · Nov 17 | $16.93 · Nov 17 | PASS |  |  |
| CSU.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| CSU.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CSU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CSU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3,316.93 · Nov 17 | $3,316.93 · Nov 17 | PASS |  |  |
| CVX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.44 / Mom: +0.38 / Rank: 1/11] XLE LEADING | RS 106.44 Mom 0.38 Rank 1/11 | PASS |  |  |
| CVX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CVX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CVX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $216.13 · Nov 17 | $216.13 · Nov 17 | PASS |  |  |
| DRAL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $4.11 · Nov 17 | $4.11 · Nov 17 | PASS |  |  |
| DRAM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $38.93 · Nov 17 | $38.93 · Nov 17 | PASS |  |  |
| DRIV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRIV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $27.00 · Nov 17 | $27.00 · Nov 17 | PASS |  |  |
| DUK | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.68 / Mom: +2.87 / Rank: 10/11] XLU IMPROVING | RS 96.68 Mom 2.87 Rank 10/11 | PASS |  |  |
| DUK | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| DUK | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DUK | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $129.84 · Nov 17 | $129.84 · Nov 17 | PASS |  |  |
| ELIL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ELIL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $40.25 · Nov 17 | $40.25 · Nov 17 | PASS |  |  |
| EQIX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.12 / Mom: +1.22 / Rank: 9/11] XLRE IMPROV | RS 97.12 Mom 1.22 Rank 9/11 | PASS |  |  |
| EQIX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| EQIX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| EQIX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,034.83 · Nov 17 | $1,034.83 · Nov 17 | PASS |  |  |
| ETN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| ETN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ETN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ETN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $337.11 · Nov 17 | $337.11 · Nov 17 | PASS |  |  |
| FCX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.66 / Mom: +0.7 / Rank: 6/11] XLB IMPROVING | RS 98.66 Mom 0.7 Rank 6/11 | PASS |  |  |
| FCX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| FCX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| FCX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $55.30 · Nov 17 | $55.30 · Nov 17 | PASS |  |  |
| FINN.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| FINN.NE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $31.76 · Nov 17 | $31.76 · Nov 17 | PASS |  |  |
| GDX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $79.57 · Nov 17 | $79.57 · Nov 17 | PASS |  |  |
| GDXU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDXU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $24.60 · Nov 17 | $24.60 · Nov 17 | PASS |  |  |
| GE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| GE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $326.40 · Nov 17 | $326.40 · Nov 17 | PASS |  |  |
| GEV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| GEV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GEV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GEV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $779.91 · Nov 17 | $779.91 · Nov 17 | PASS |  |  |
| GEV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GEV.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $52.13 · Nov 17 | $52.13 · Nov 17 | PASS |  |  |
| GGLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $63.05 · Nov 17 | $63.05 · Nov 17 | PASS |  |  |
| GIB-A.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| GIB-A.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GIB-A.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GIB-A.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $115.07 · Nov 17 | $115.07 · Nov 17 | PASS |  |  |
| GOOGL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 97.99 / Mom: +0.28 / Rank: 8/11] X | RS 97.99 Mom 0.28 Rank 8/11 | PASS |  |  |
| GOOGL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| GOOGL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GOOGL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $280.20 · Nov 17 | $280.20 · Nov 17 | PASS |  |  |
| GRID | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GRID | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $155.15 · Nov 17 | $155.15 · Nov 17 | PASS |  |  |
| HD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.25 / Rank: 7/11] X | RS 98.43 Mom 2.25 Rank 7/11 | PASS |  |  |
| HD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| HD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $339.01 · Nov 17 | $339.01 · Nov 17 | PASS |  |  |
| HURA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HURA.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $37.39 · Nov 17 | $37.39 · Nov 17 | PASS |  |  |
| HXQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HXQ.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $110.63 · Nov 17 | $110.63 · Nov 17 | PASS |  |  |
| JNJ | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.49 / Mom: +1.18 / Rank: 2/11] XLV LEADING | RS 105.49 Mom 1.18 Rank 2/11 | PASS |  |  |
| JNJ | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| JNJ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $278.70 · Nov 17 | $278.70 · Nov 17 | PASS |  |  |
| JPM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.01 / Mom: -0.46 / Rank: 4/11] XLF WEAKENIN | RS 100.01 Mom -0.46 Rank 4/11 | PASS |  |  |
| JPM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| JPM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JPM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $329.96 · Nov 17 | $329.96 · Nov 17 | PASS |  |  |
| KEYS | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| KEYS | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| KEYS | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ Earnings in 1 day | ⚠️ Earnings in 1 day | PASS |  |  |
| KEYS | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-19, 1 days | 2026-11-19, 1 days | PASS |  |  |
| KEYS | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $284.45 · Nov 17 | $284.45 · Nov 17 | PASS |  |  |
| LIN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.66 / Mom: +0.7 / Rank: 6/11] XLB IMPROVING | RS 98.66 Mom 0.7 Rank 6/11 | PASS |  |  |
| LIN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| LIN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LIN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $515.11 · Nov 17 | $515.11 · Nov 17 | PASS |  |  |
| LLY | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.49 / Mom: +1.18 / Rank: 2/11] XLV LEADING | RS 105.49 Mom 1.18 Rank 2/11 | PASS |  |  |
| LLY | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| LLY | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LLY | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,415.55 · Nov 17 | $1,415.55 · Nov 17 | PASS |  |  |
| MDA.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| MDA.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MDA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MDA.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $39.22 · Nov 17 | $39.22 · Nov 17 | PASS |  |  |
| META | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 97.99 / Mom: +0.28 / Rank: 8/11] X | RS 97.99 Mom 0.28 Rank 8/11 | PASS |  |  |
| META | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| META | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| META | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $618.87 · Nov 17 | $618.87 · Nov 17 | PASS |  |  |
| METU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| METU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $21.57 · Nov 17 | $21.57 · Nov 17 | PASS |  |  |
| MRVL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| MRVL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MRVL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MRVL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $148.74 · Nov 17 | $148.74 · Nov 17 | PASS |  |  |
| MSFT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| MSFT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MSFT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $506.24 · Nov 17 | $506.24 · Nov 17 | PASS |  |  |
| MSFU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $37.34 · Nov 17 | $37.34 · Nov 17 | PASS |  |  |
| MTRX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MTRX.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $29.13 · Nov 17 | $29.13 · Nov 17 | PASS |  |  |
| MU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $31.04 · Nov 17 | $31.04 · Nov 17 | PASS |  |  |
| NEE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.68 / Mom: +2.87 / Rank: 10/11] XLU IMPROVING | RS 96.68 Mom 2.87 Rank 10/11 | PASS |  |  |
| NEE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $84.42 · Nov 17 | $84.42 · Nov 17 | PASS |  |  |
| NEM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.66 / Mom: +0.7 / Rank: 6/11] XLB IMPROVING | RS 98.66 Mom 0.7 Rank 6/11 | PASS |  |  |
| NEM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $111.26 · Nov 17 | $111.26 · Nov 17 | PASS |  |  |
| NFLX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 97.99 / Mom: +0.28 / Rank: 8/11] X | RS 97.99 Mom 0.28 Rank 8/11 | PASS |  |  |
| NFLX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NFLX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFLX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $59.68 · Nov 17 | $59.68 · Nov 17 | PASS |  |  |
| NFXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $9.86 · Nov 17 | $9.86 · Nov 17 | PASS |  |  |
| NTR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.66 / Mom: +0.7 / Rank: 6/11] XLB IMPROVING | RS 98.66 Mom 0.7 Rank 6/11 | PASS |  |  |
| NTR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NTR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NTR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $99.02 · Nov 17 | $99.02 · Nov 17 | PASS |  |  |
| NVDA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| NVDA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| NVDA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $155.46 · Nov 17 | $155.46 · Nov 17 | PASS |  |  |
| NVDL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $16.22 · Nov 17 | $16.22 · Nov 17 | PASS |  |  |
| ONTO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| ONTO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ONTO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ONTO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $199.57 · Nov 17 | $199.57 · Nov 17 | PASS |  |  |
| ORBX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| ORCL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ORCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $115.00 · Nov 17 | $115.00 · Nov 17 | PASS |  |  |
| PG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.52 / Mom: +3.17 / Rank: 3/11] XLP LE | RS 101.52 Mom 3.17 Rank 3/11 | PASS |  |  |
| PG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| PG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $171.72 · Nov 17 | $171.72 · Nov 17 | PASS |  |  |
| PLD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.12 / Mom: +1.22 / Rank: 9/11] XLRE IMPROV | RS 97.12 Mom 1.22 Rank 9/11 | PASS |  |  |
| PLD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| PLD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PLD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $125.56 · Nov 17 | $125.56 · Nov 17 | PASS |  |  |
| PNG.V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| PNG.V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| PNG.V | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 6 days | 📅 Earnings in 6 days | PASS |  |  |
| PNG.V | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 6 days | 2026-11-24, 6 days | PASS |  |  |
| PNG.V | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3.12 · Nov 17 | $3.12 · Nov 17 | PASS |  |  |
| QCOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| QCOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| QCOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QCOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $166.67 · Nov 17 | $166.67 · Nov 17 | PASS |  |  |
| QPUX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QPUX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3.32 · Nov 17 | $3.32 · Nov 17 | PASS |  |  |
| QTUM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QTUM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $122.42 · Nov 17 | $122.42 · Nov 17 | PASS |  |  |
| RBOT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| RTX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| RTX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $198.00 · Nov 17 | $198.00 · Nov 17 | PASS |  |  |
| RY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.01 / Mom: -0.46 / Rank: 4/11] XLF WEAKENIN | RS 100.01 Mom -0.46 Rank 4/11 | PASS |  |  |
| RY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| RY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $280.99 · Nov 17 | $280.99 · Nov 17 | PASS |  |  |
| SETM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SETM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $22.11 · Nov 17 | $22.11 · Nov 17 | PASS |  |  |
| SGRD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SGRD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $17.95 · Nov 17 | $17.95 · Nov 17 | PASS |  |  |
| SMH | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $460.10 · Nov 17 | $460.10 · Nov 17 | PASS |  |  |
| SNDK.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SNDK.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $19.28 · Nov 17 | $19.28 · Nov 17 | PASS |  |  |
| SO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.68 / Mom: +2.87 / Rank: 10/11] XLU IMPROVING | RS 96.68 Mom 2.87 Rank 10/11 | PASS |  |  |
| SO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| SO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $93.60 · Nov 17 | $93.60 · Nov 17 | PASS |  |  |
| SOXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $49.07 · Nov 17 | $49.07 · Nov 17 | PASS |  |  |
| SOXL.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL.NE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.36 · Nov 17 | $12.36 · Nov 17 | PASS |  |  |
| SOXX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $141.46 · Nov 17 | $141.46 · Nov 17 | PASS |  |  |
| SPCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SPCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $10.13 · Nov 17 | $10.13 · Nov 17 | PASS |  |  |
| TSLA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.25 / Rank: 7/11] X | RS 98.43 Mom 2.25 Rank 7/11 | PASS |  |  |
| TSLA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| TSLA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $380.11 · Nov 17 | $380.11 · Nov 17 | PASS |  |  |
| TSLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $9.81 · Nov 17 | $9.81 · Nov 17 | PASS |  |  |
| TSM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| TSM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| TSM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $359.69 · Nov 17 | $359.69 · Nov 17 | PASS |  |  |
| UBOT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UBOT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $15.04 · Nov 17 | $15.04 · Nov 17 | PASS |  |  |
| UFO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UFO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $39.30 · Nov 17 | $39.30 · Nov 17 | PASS |  |  |
| URA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $30.04 · Nov 17 | $30.04 · Nov 17 | PASS |  |  |
| URAA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URAA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $11.38 · Nov 17 | $11.38 · Nov 17 | PASS |  |  |
| V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.01 / Mom: -0.46 / Rank: 4/11] XLF WEAKENIN | RS 100.01 Mom -0.46 Rank 4/11 | PASS |  |  |
| V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| V | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| V | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $416.77 · Nov 17 | $416.77 · Nov 17 | PASS |  |  |
| VFV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VFV.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $186.14 · Nov 17 | $186.14 · Nov 17 | PASS |  |  |
| VRT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| VRT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| VRT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VRT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $190.37 · Nov 17 | $190.37 · Nov 17 | PASS |  |  |
| WDC.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WDC.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $17.13 · Nov 17 | $17.13 · Nov 17 | PASS |  |  |
| WELL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.12 / Mom: +1.22 / Rank: 9/11] XLRE IMPROV | RS 97.12 Mom 1.22 Rank 9/11 | PASS |  |  |
| WELL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| WELL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WELL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $245.76 · Nov 17 | $245.76 · Nov 17 | PASS |  |  |
| WMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.52 / Mom: +3.17 / Rank: 3/11] XLP LE | RS 101.52 Mom 3.17 Rank 3/11 | PASS |  |  |
| WMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| WMT | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ Earnings in 1 day | ⚠️ Earnings in 1 day | PASS |  |  |
| WMT | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-19, 1 days | 2026-11-19, 1 days | PASS |  |  |
| WMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $127.52 · Nov 17 | $127.52 · Nov 17 | PASS |  |  |
| XCHP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XCHP.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $105.40 · Nov 17 | $105.40 · Nov 17 | PASS |  |  |
| XDRV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XEQT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XEQT.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $44.34 · Nov 17 | $44.34 · Nov 17 | PASS |  |  |
| XETM.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XGD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XGD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $51.28 · Nov 17 | $51.28 · Nov 17 | PASS |  |  |
| XOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.44 / Mom: +0.38 / Rank: 1/11] XLE LEADING | RS 106.44 Mom 0.38 Rank 1/11 | PASS |  |  |
| XOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| XOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $167.21 · Nov 17 | $167.21 · Nov 17 | PASS |  |  |
| AAPL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $360.83 | $360.83 | PASS |  |  |
| AAPL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $351.91 | $351.91 | PASS |  |  |
| AAPL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $360.83 / $242.57 | $360.83 / $242.57 | PASS |  |  |
| AAPL | PD3 | % from High | -2.5% | -2.5% | PASS |  |  |
| AAPL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15.0B | bars: $15,393,891,469 | PASS | LOW |  |
| AAPU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $51.04 | $51.04 | PASS |  |  |
| AAPU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $48.49 | $48.49 | PASS |  |  |
| AAPU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $51.04 / $25.94 | $51.04 / $25.94 | PASS |  |  |
| AAPU | PD3 | % from High | -5.0% | -5.0% | PASS |  |  |
| AAPU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $51M | bars: $46,398,522 | PASS | LOW |  |
| ABBV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.93 | $302.93 | PASS |  |  |
| ABBV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $292.82 | $292.82 | PASS |  |  |
| ABBV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.93 / $188.25 | $302.93 / $188.25 | PASS |  |  |
| ABBV | PD3 | % from High | -3.3% | -3.3% | PASS |  |  |
| ABBV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.4B | bars: $1,444,365,724 | PASS | LOW |  |
| AIPO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $34.79 | $34.79 | PASS |  |  |
| AIPO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $22.63 | $22.63 | PASS |  |  |
| AIPO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $34.79 / $20.65 | $34.79 / $20.65 | PASS |  |  |
| AIPO | PD3 | % from High | -35.0% | -35.0% | PASS |  |  |
| AIPO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $34M | bars: $36,279,523 | PASS | LOW |  |
| ALAB | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $499.48 | $499.48 | PASS |  |  |
| ALAB | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $211.60 | $211.60 | PASS |  |  |
| ALAB | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $499.48 / $97.89 | $499.48 / $97.89 | PASS |  |  |
| ALAB | PD3 | % from High | -57.6% | -57.6% | PASS |  |  |
| ALAB | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $902M | bars: $957,481,934 | PASS | LOW |  |
| AMD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $658.52 | $658.52 | PASS |  |  |
| AMD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $503.41 | $503.41 | PASS |  |  |
| AMD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $658.52 / $188.22 | $658.52 / $188.22 | PASS |  |  |
| AMD | PD3 | % from High | -23.6% | -23.6% | PASS |  |  |
| AMD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $12.6B | bars: $13,823,305,403 | PASS | LOW |  |
| AMD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $16.97 | $16.97 | PASS |  |  |
| AMD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.95 | $12.95 | PASS |  |  |
| AMD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $16.97 / $4.93 | $16.97 / $4.93 | PASS |  |  |
| AMD.TO | PD3 | % from High | -23.7% | -23.7% | PASS |  |  |
| AMD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $27M | bars: $29,537,573 | PASS | LOW |  |
| AMZN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $287.20 | $287.20 | PASS |  |  |
| AMZN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $257.89 | $257.89 | PASS |  |  |
| AMZN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $287.20 / $196.00 | $287.20 / $196.00 | PASS |  |  |
| AMZN | PD3 | % from High | -10.2% | -10.2% | PASS |  |  |
| AMZN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $10.2B | bars: $10,697,894,465 | PASS | LOW |  |
| AMZU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.64 | $46.64 | PASS |  |  |
| AMZU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $35.25 | $35.25 | PASS |  |  |
| AMZU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.64 / $24.13 | $46.64 / $24.13 | PASS |  |  |
| AMZU | PD3 | % from High | -24.4% | -24.4% | PASS |  |  |
| AMZU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $66M | bars: $67,671,489 | PASS | LOW |  |
| ANET.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $33.32 | $33.32 | PASS |  |  |
| ANET.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.85 / $20.97 | $38.85 / $20.97 | PASS |  |  |
| ANET.TO | PD3 | % from High | -14.2% | -14.2% | PASS |  |  |
| ASML.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $56.75 | $56.75 | PASS |  |  |
| ASML.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $40.80 | $40.80 | PASS |  |  |
| ASML.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $56.75 / $26.65 | $56.75 / $26.65 | PASS |  |  |
| ASML.TO | PD3 | % from High | -28.1% | -28.1% | PASS |  |  |
| ASML.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,815,713 | PASS | LOW |  |
| ASTL.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $8.31 | $8.31 | PASS |  |  |
| ASTL.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $7.25 | $7.25 | PASS |  |  |
| ASTL.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $8.31 / $4.46 | $8.31 / $4.46 | PASS |  |  |
| ASTL.TO | PD3 | % from High | -12.8% | -12.8% | PASS |  |  |
| ASTL.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5M | bars: $4,333,309 | PASS | LOW |  |
| ATD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $94.68 | $94.68 | PASS |  |  |
| ATD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $83.65 | $83.65 | PASS |  |  |
| ATD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $94.68 / $67.83 | $94.68 / $67.83 | PASS |  |  |
| ATD.TO | PD3 | % from High | -11.6% | -11.6% | PASS |  |  |
| ATD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $116M | bars: $109,638,698 | PASS | LOW |  |
| AVGC | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $18.20 | $18.20 | PASS |  |  |
| AVGC | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.79 / $13.71 | $31.79 / $13.71 | PASS |  |  |
| AVGC | PD3 | % from High | -42.7% | -42.7% | PASS |  |  |
| AVGO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $493.32 | $493.32 | PASS |  |  |
| AVGO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $341.60 | $341.60 | PASS |  |  |
| AVGO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $493.32 / $288.98 | $493.32 / $288.98 | PASS |  |  |
| AVGO | PD3 | % from High | -30.8% | -30.8% | PASS |  |  |
| AVGO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.7B | bars: $8,585,125,804 | PASS | LOW |  |
| AVGO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.94 | $12.94 | PASS |  |  |
| AVGO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $18.88 / $11.00 | $18.88 / $11.00 | PASS |  |  |
| AVGO.TO | PD3 | % from High | -31.4% | -31.5% | PASS |  |  |
| AVGO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15M | bars: $14,841,005 | PASS | LOW |  |
| BDT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $71.13 | $71.13 | PASS |  |  |
| BDT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $86.42 / $23.93 | $86.42 / $23.93 | PASS |  |  |
| BDT.TO | PD3 | % from High | -17.7% | -17.7% | PASS |  |  |
| BDT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $28M | bars: $29,276,572 | PASS | LOW |  |
| BOTZ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $41.69 | $41.69 | PASS |  |  |
| BOTZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $29.71 | $29.71 | PASS |  |  |
| BOTZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $41.69 / $29.36 | $41.69 / $29.36 | PASS |  |  |
| BOTZ | PD3 | % from High | -28.7% | -28.7% | PASS |  |  |
| BOTZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $21M | bars: $21,441,078 | PASS | LOW |  |
| BRK-B | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $596.92 | $596.92 | PASS |  |  |
| BRK-B | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $586.76 | $586.76 | PASS |  |  |
| BRK-B | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $596.92 / $464.01 | $596.92 / $464.01 | PASS |  |  |
| BRK-B | PD3 | % from High | -1.7% | -1.7% | PASS |  |  |
| BRK-B | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.7B | bars: $2,821,241,724 | PASS | LOW |  |
| BRKU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $31.20 | $31.20 | PASS |  |  |
| BRKU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.19 | $30.19 | PASS |  |  |
| BRKU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.20 / $20.05 | $31.20 / $20.05 | PASS |  |  |
| BRKU | PD3 | % from High | -3.2% | -3.2% | PASS |  |  |
| BRKU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,770,703 | PASS | LOW |  |
| CAMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $215.99 | $215.99 | PASS |  |  |
| CAMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $94.96 | $94.96 | PASS |  |  |
| CAMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $215.99 / $89.13 | $215.99 / $89.13 | PASS |  |  |
| CAMT | PD3 | % from High | -56.0% | -56.0% | PASS |  |  |
| CAMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $45M | bars: $48,931,234 | PASS | LOW |  |
| CARS.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.16 | $38.16 | PASS |  |  |
| CARS.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $19.88 | $19.88 | PASS |  |  |
| CARS.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.16 / $19.88 | $38.16 / $19.88 | PASS |  |  |
| CARS.TO | PD3 | % from High | -47.9% | -47.9% | PASS |  |  |
| CARS.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| CAT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,068.93 | $1,068.93 | PASS |  |  |
| CAT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $570.79 | $570.79 | PASS |  |  |
| CAT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,068.93 / $532.55 | $1,068.93 / $532.55 | PASS |  |  |
| CAT | PD3 | % from High | -46.6% | -46.6% | PASS |  |  |
| CAT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.7B | bars: $1,748,822,225 | PASS | LOW |  |
| CCO.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $182.72 | $182.72 | PASS |  |  |
| CCO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $92.16 | $92.16 | PASS |  |  |
| CCO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $182.72 / $91.76 | $182.72 / $91.76 | PASS |  |  |
| CCO.TO | PD3 | % from High | -49.6% | -49.6% | PASS |  |  |
| CCO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $106M | bars: $113,898,399 | PASS | LOW |  |
| CEG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $378.52 | $378.52 | PASS |  |  |
| CEG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $268.07 | $268.07 | PASS |  |  |
| CEG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $378.52 / $227.93 | $378.52 / $227.93 | PASS |  |  |
| CEG | PD3 | % from High | -29.2% | -29.2% | PASS |  |  |
| CEG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $941M | bars: $1,016,752,093 | PASS | LOW |  |
| CGY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $84.30 | $84.30 | PASS |  |  |
| CGY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $95.15 / $44.20 | $95.15 / $44.20 | PASS |  |  |
| CGY.TO | PD3 | % from High | -11.4% | -11.4% | PASS |  |  |
| CGY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,551,533 | PASS | LOW |  |
| CNQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $78.60 | $78.60 | PASS |  |  |
| CNQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $68.29 | $68.29 | PASS |  |  |
| CNQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $78.60 / $40.51 | $78.60 / $40.51 | PASS |  |  |
| CNQ.TO | PD3 | % from High | -13.1% | -13.1% | PASS |  |  |
| CNQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $927M | bars: $863,527,098 | PASS | LOW |  |
| CNR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $184.26 | $184.26 | PASS |  |  |
| CNR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $180.54 | $180.54 | PASS |  |  |
| CNR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $184.26 / $125.06 | $184.26 / $125.06 | PASS |  |  |
| CNR.TO | PD3 | % from High | -2.0% | -2.0% | PASS |  |  |
| CNR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $230M | bars: $223,844,137 | PASS | LOW |  |
| COP | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $153.27 | $153.27 | PASS |  |  |
| COP | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $139.48 | $139.48 | PASS |  |  |
| COP | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $153.27 / $83.30 | $153.27 / $83.30 | PASS |  |  |
| COP | PD3 | % from High | -9.0% | -9.0% | PASS |  |  |
| COP | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $947M | bars: $954,826,880 | PASS | LOW |  |
| COPP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $70.54 | $70.54 | PASS |  |  |
| COPP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $46.42 | $46.42 | PASS |  |  |
| COPP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $70.54 / $42.17 | $70.54 / $42.17 | PASS |  |  |
| COPP.TO | PD3 | % from High | -34.2% | -34.2% | PASS |  |  |
| COPX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $99.65 | $99.65 | PASS |  |  |
| COPX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $65.31 | $65.31 | PASS |  |  |
| COPX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $99.65 / $55.44 | $99.65 / $55.44 | PASS |  |  |
| COPX | PD3 | % from High | -34.5% | -34.5% | PASS |  |  |
| COPX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $190M | bars: $181,743,835 | PASS | LOW |  |
| COPZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $8.59 | $8.59 | PASS |  |  |
| COPZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $26.40 / $8.52 | $26.40 / $8.52 | PASS |  |  |
| COPZ | PD3 | % from High | -67.5% | -67.5% | PASS |  |  |
| COST | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,123.67 | $1,123.67 | PASS |  |  |
| COST | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,110.08 | $1,110.08 | PASS |  |  |
| COST | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,123.67 / $839.11 | $1,123.67 / $839.11 | PASS |  |  |
| COST | PD3 | % from High | -1.2% | -1.2% | PASS |  |  |
| COST | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.5B | bars: $2,611,583,022 | PASS | LOW |  |
| COTG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $17.80 | $17.80 | PASS |  |  |
| COTG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $16.93 | $16.93 | PASS |  |  |
| COTG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $17.80 / $10.95 | $17.80 / $10.95 | PASS |  |  |
| COTG | PD3 | % from High | -4.9% | -4.9% | PASS |  |  |
| COTG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,806,464 | PASS | LOW |  |
| CSU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $3,565.00 | $3,565.00 | PASS |  |  |
| CSU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3,316.93 | $3,316.93 | PASS |  |  |
| CSU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $3,565.00 / $2,192.51 | $3,565.00 / $2,192.51 | PASS |  |  |
| CSU.TO | PD3 | % from High | -7.0% | -7.0% | PASS |  |  |
| CSU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $199M | bars: $204,135,747 | PASS | LOW |  |
| CVX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $236.48 | $236.48 | PASS |  |  |
| CVX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $216.13 | $216.13 | PASS |  |  |
| CVX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $236.48 / $142.51 | $236.48 / $142.51 | PASS |  |  |
| CVX | PD3 | % from High | -8.6% | -8.6% | PASS |  |  |
| CVX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.8B | bars: $1,886,270,399 | PASS | LOW |  |
| DRAL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $4.11 | $4.11 | PASS |  |  |
| DRAL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $25.52 / $3.73 | $25.52 / $3.73 | PASS |  |  |
| DRAL | PD3 | % from High | -83.9% | -83.9% | PASS |  |  |
| DRAM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $38.93 | $38.93 | PASS |  |  |
| DRAM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $81.34 / $26.14 | $81.34 / $26.14 | PASS |  |  |
| DRAM | PD3 | % from High | -52.1% | -52.1% | PASS |  |  |
| DRAM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.3B | bars: $1,344,795,709 | PASS | LOW |  |
| DRIV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $42.67 | $42.67 | PASS |  |  |
| DRIV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $27.00 | $27.00 | PASS |  |  |
| DRIV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $42.67 / $26.80 | $42.67 / $26.80 | PASS |  |  |
| DRIV | PD3 | % from High | -36.7% | -36.7% | PASS |  |  |
| DRIV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1M | bars: $1,085,201 | PASS | LOW |  |
| DUK | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.87 | $131.87 | PASS |  |  |
| DUK | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $129.84 | $129.84 | PASS |  |  |
| DUK | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.87 / $110.06 | $131.87 / $110.06 | PASS |  |  |
| DUK | PD3 | % from High | -1.5% | -1.5% | PASS |  |  |
| DUK | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $544M | bars: $569,831,002 | PASS | LOW |  |
| ELIL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.56 | $43.56 | PASS |  |  |
| ELIL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $40.25 | $40.25 | PASS |  |  |
| ELIL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.56 / $16.21 | $43.56 / $16.21 | PASS |  |  |
| ELIL | PD3 | % from High | -7.6% | -7.6% | PASS |  |  |
| ELIL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,524,802 | PASS | LOW |  |
| EQIX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,118.65 | $1,118.65 | PASS |  |  |
| EQIX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,034.83 | $1,034.83 | PASS |  |  |
| EQIX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,118.65 / $709.79 | $1,118.65 / $709.79 | PASS |  |  |
| EQIX | PD3 | % from High | -7.5% | -7.5% | PASS |  |  |
| EQIX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $591M | bars: $605,985,955 | PASS | LOW |  |
| ETN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $476.54 | $476.54 | PASS |  |  |
| ETN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $337.11 | $337.11 | PASS |  |  |
| ETN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $476.54 / $308.39 | $476.54 / $308.39 | PASS |  |  |
| ETN | PD3 | % from High | -29.3% | -29.3% | PASS |  |  |
| ETN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $825M | bars: $888,888,601 | PASS | LOW |  |
| FCX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.07 | $80.07 | PASS |  |  |
| FCX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $55.30 | $55.30 | PASS |  |  |
| FCX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.07 / $38.49 | $80.07 / $38.49 | PASS |  |  |
| FCX | PD3 | % from High | -30.9% | -30.9% | PASS |  |  |
| FCX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $705M | bars: $653,112,458 | PASS | LOW |  |
| FINN.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $35.83 | $35.83 | PASS |  |  |
| FINN.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $31.76 | $31.76 | PASS |  |  |
| FINN.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $35.83 / $21.66 | $35.83 / $21.66 | PASS |  |  |
| FINN.NE | PD3 | % from High | -11.4% | -11.4% | PASS |  |  |
| FINN.NE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $9M | bars: $9,996,677 | PASS | LOW |  |
| GDX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $117.18 | $117.18 | PASS |  |  |
| GDX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $79.57 | $79.57 | PASS |  |  |
| GDX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $117.18 / $69.74 | $117.18 / $69.74 | PASS |  |  |
| GDX | PD3 | % from High | -32.1% | -32.1% | PASS |  |  |
| GDX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.8B | bars: $1,691,396,929 | PASS | LOW |  |
| GDXU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $65.00 | $65.00 | PASS |  |  |
| GDXU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $24.60 | $24.60 | PASS |  |  |
| GDXU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $65.00 / $20.83 | $65.00 / $20.83 | PASS |  |  |
| GDXU.TO | PD3 | % from High | -62.2% | -62.2% | PASS |  |  |
| GDXU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $6M | bars: $5,640,985 | PASS | LOW |  |
| GE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $388.25 | $388.25 | PASS |  |  |
| GE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $326.40 | $326.40 | PASS |  |  |
| GE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $388.25 / $268.17 | $388.25 / $268.17 | PASS |  |  |
| GE | PD3 | % from High | -15.9% | -15.9% | PASS |  |  |
| GE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.5B | bars: $1,586,080,031 | PASS | LOW |  |
| GEV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,195.24 | $1,195.24 | PASS |  |  |
| GEV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $779.91 | $779.91 | PASS |  |  |
| GEV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,195.24 / $528.87 | $1,195.24 / $528.87 | PASS |  |  |
| GEV | PD3 | % from High | -34.7% | -34.7% | PASS |  |  |
| GEV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.3B | bars: $2,445,222,670 | PASS | LOW |  |
| GEV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $52.13 | $52.13 | PASS |  |  |
| GEV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.44 / $42.23 | $80.44 / $42.23 | PASS |  |  |
| GEV.TO | PD3 | % from High | -35.2% | -35.2% | PASS |  |  |
| GEV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,853,366 | PASS | LOW |  |
| GGLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $151.33 | $151.33 | PASS |  |  |
| GGLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $63.05 | $63.05 | PASS |  |  |
| GGLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $151.33 / $62.13 | $151.33 / $62.13 | PASS |  |  |
| GGLL | PD3 | % from High | -58.3% | -58.3% | PASS |  |  |
| GGLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $108M | bars: $121,845,320 | PASS | LOW |  |
| GIB-A.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.27 | $131.27 | PASS |  |  |
| GIB-A.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $115.07 | $115.07 | PASS |  |  |
| GIB-A.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.27 / $83.04 | $131.27 / $83.04 | PASS |  |  |
| GIB-A.TO | PD3 | % from High | -12.3% | -12.3% | PASS |  |  |
| GIB-A.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $69M | bars: $72,225,389 | PASS | LOW |  |
| GOOGL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $408.10 | $408.10 | PASS |  |  |
| GOOGL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $280.20 | $280.20 | PASS |  |  |
| GOOGL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $408.10 / $271.77 | $408.10 / $271.77 | PASS |  |  |
| GOOGL | PD3 | % from High | -31.3% | -31.3% | PASS |  |  |
| GOOGL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.5B | bars: $9,020,145,364 | PASS | LOW |  |
| GRID | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $198.79 | $198.79 | PASS |  |  |
| GRID | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $155.15 | $155.15 | PASS |  |  |
| GRID | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $198.79 / $143.36 | $198.79 / $143.36 | PASS |  |  |
| GRID | PD3 | % from High | -22.0% | -22.0% | PASS |  |  |
| GRID | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $88M | bars: $91,331,480 | PASS | LOW |  |
| HD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $389.24 | $389.24 | PASS |  |  |
| HD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $339.01 | $339.01 | PASS |  |  |
| HD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.24 / $277.15 | $389.24 / $277.15 | PASS |  |  |
| HD | PD3 | % from High | -12.9% | -12.9% | PASS |  |  |
| HD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,709,413,644 | PASS | LOW |  |
| HURA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $73.95 | $73.95 | PASS |  |  |
| HURA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $37.39 | $37.39 | PASS |  |  |
| HURA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $73.95 / $36.76 | $73.95 / $36.76 | PASS |  |  |
| HURA.TO | PD3 | % from High | -49.4% | -49.4% | PASS |  |  |
| HXQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $110.63 | $110.63 | PASS |  |  |
| HXQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $128.37 / $91.48 | $128.37 / $91.48 | PASS |  |  |
| HXQ.TO | PD3 | % from High | -13.8% | -13.8% | PASS |  |  |
| HXQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,603,458 | PASS | LOW |  |
| JNJ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $290.25 | $290.25 | PASS |  |  |
| JNJ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $278.70 | $278.70 | PASS |  |  |
| JNJ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $290.25 / $191.58 | $290.25 / $191.58 | PASS |  |  |
| JNJ | PD3 | % from High | -4.0% | -4.0% | PASS |  |  |
| JNJ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.0B | bars: $2,037,693,640 | PASS | LOW |  |
| JPM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $364.68 | $364.68 | PASS |  |  |
| JPM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $329.96 | $329.96 | PASS |  |  |
| JPM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $364.68 / $275.06 | $364.68 / $275.06 | PASS |  |  |
| JPM | PD3 | % from High | -9.5% | -9.5% | PASS |  |  |
| JPM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.4B | bars: $2,507,538,022 | PASS | LOW |  |
| KEYS | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $389.93 | $389.93 | PASS |  |  |
| KEYS | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $284.45 | $284.45 | PASS |  |  |
| KEYS | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.93 / $167.23 | $389.93 / $167.23 | PASS |  |  |
| KEYS | PD3 | % from High | -27.1% | -27.1% | PASS |  |  |
| KEYS | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $378M | bars: $372,290,959 | PASS | LOW |  |
| LIN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $546.40 | $546.40 | PASS |  |  |
| LIN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $515.11 | $515.11 | PASS |  |  |
| LIN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $546.40 / $384.00 | $546.40 / $384.00 | PASS |  |  |
| LIN | PD3 | % from High | -5.7% | -5.7% | PASS |  |  |
| LIN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.1B | bars: $1,077,540,395 | PASS | LOW |  |
| LLY | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,475.25 | $1,475.25 | PASS |  |  |
| LLY | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,415.55 | $1,415.55 | PASS |  |  |
| LLY | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,475.25 / $846.81 | $1,475.25 / $846.81 | PASS |  |  |
| LLY | PD3 | % from High | -4.0% | -4.0% | PASS |  |  |
| LLY | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.7B | bars: $3,656,525,267 | PASS | LOW |  |
| MDA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $67.90 | $67.90 | PASS |  |  |
| MDA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.22 | $39.22 | PASS |  |  |
| MDA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $67.90 / $20.85 | $67.90 / $20.85 | PASS |  |  |
| MDA.TO | PD3 | % from High | -42.2% | -42.2% | PASS |  |  |
| MDA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $61M | bars: $63,664,410 | PASS | LOW |  |
| META | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $779.82 | $779.82 | PASS |  |  |
| META | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $618.87 | $618.87 | PASS |  |  |
| META | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $779.82 / $519.37 | $779.82 / $519.37 | PASS |  |  |
| META | PD3 | % from High | -20.6% | -20.6% | PASS |  |  |
| META | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $13.0B | bars: $13,727,393,933 | PASS | LOW |  |
| METU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.96 | $38.96 | PASS |  |  |
| METU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $21.57 | $21.57 | PASS |  |  |
| METU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.96 / $16.76 | $38.96 / $16.76 | PASS |  |  |
| METU | PD3 | % from High | -44.6% | -44.6% | PASS |  |  |
| METU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $115M | bars: $106,942,194 | PASS | LOW |  |
| MRVL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $329.73 | $329.73 | PASS |  |  |
| MRVL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $148.74 | $148.74 | PASS |  |  |
| MRVL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $329.73 / $70.62 | $329.73 / $70.62 | PASS |  |  |
| MRVL | PD3 | % from High | -54.9% | -54.9% | PASS |  |  |
| MRVL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.7B | bars: $3,590,384,758 | PASS | LOW |  |
| MSFT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $559.15 | $559.15 | PASS |  |  |
| MSFT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $506.24 | $506.24 | PASS |  |  |
| MSFT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $559.15 / $348.54 | $559.15 / $348.54 | PASS |  |  |
| MSFT | PD3 | % from High | -9.5% | -9.5% | PASS |  |  |
| MSFT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $11.8B | bars: $12,019,140,370 | PASS | LOW |  |
| MSFU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.31 | $46.31 | PASS |  |  |
| MSFU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $37.34 | $37.34 | PASS |  |  |
| MSFU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.31 / $19.32 | $46.31 / $19.32 | PASS |  |  |
| MSFU | PD3 | % from High | -19.4% | -19.4% | PASS |  |  |
| MSFU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $93M | bars: $90,994,788 | PASS | LOW |  |
| MTRX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $29.13 | $29.13 | PASS |  |  |
| MTRX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $39.30 / $28.00 | $39.30 / $28.00 | PASS |  |  |
| MTRX.TO | PD3 | % from High | -25.9% | -25.9% | PASS |  |  |
| MU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $55.28 | $55.28 | PASS |  |  |
| MU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $31.04 | $31.04 | PASS |  |  |
| MU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $55.28 / $8.62 | $55.28 / $8.62 | PASS |  |  |
| MU.TO | PD3 | % from High | -43.9% | -43.8% | PASS |  |  |
| MU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $54M | bars: $57,611,026 | PASS | LOW |  |
| NEE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $97.30 | $97.30 | PASS |  |  |
| NEE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $84.42 | $84.42 | PASS |  |  |
| NEE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $97.30 / $74.41 | $97.30 / $74.41 | PASS |  |  |
| NEE | PD3 | % from High | -13.2% | -13.2% | PASS |  |  |
| NEE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.0B | bars: $1,070,448,627 | PASS | LOW |  |
| NEM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $135.01 | $135.01 | PASS |  |  |
| NEM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $111.26 | $111.26 | PASS |  |  |
| NEM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $135.01 / $80.58 | $135.01 / $80.58 | PASS |  |  |
| NEM | PD3 | % from High | -17.6% | -17.6% | PASS |  |  |
| NEM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $772M | bars: $716,169,065 | PASS | LOW |  |
| NFLX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $115.25 | $115.25 | PASS |  |  |
| NFLX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $59.68 | $59.68 | PASS |  |  |
| NFLX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $115.25 / $59.40 | $115.25 / $59.40 | PASS |  |  |
| NFLX | PD3 | % from High | -48.2% | -48.2% | PASS |  |  |
| NFLX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,366,299,699 | PASS | LOW |  |
| NFXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.64 | $46.64 | PASS |  |  |
| NFXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $9.86 | $9.86 | PASS |  |  |
| NFXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.64 / $9.77 | $46.64 / $9.77 | PASS |  |  |
| NFXL | PD3 | % from High | -78.9% | -78.9% | PASS |  |  |
| NFXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15M | bars: $16,108,740 | PASS | LOW |  |
| NTR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $114.19 | $114.19 | PASS |  |  |
| NTR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $99.02 | $99.02 | PASS |  |  |
| NTR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $114.19 / $74.44 | $114.19 / $74.44 | PASS |  |  |
| NTR.TO | PD3 | % from High | -13.3% | -13.3% | PASS |  |  |
| NTR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $179M | bars: $190,590,947 | PASS | LOW |  |
| NVDA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $243.37 | $243.37 | PASS |  |  |
| NVDA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $155.46 | $155.46 | PASS |  |  |
| NVDA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $243.37 / $148.80 | $243.37 / $148.80 | PASS |  |  |
| NVDA | PD3 | % from High | -36.1% | -36.1% | PASS |  |  |
| NVDA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $24.0B | bars: $24,430,752,602 | PASS | LOW |  |
| NVDL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.27 | $43.27 | PASS |  |  |
| NVDL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $16.22 | $16.22 | PASS |  |  |
| NVDL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.27 / $14.53 | $43.27 / $14.53 | PASS |  |  |
| NVDL | PD3 | % from High | -62.5% | -62.5% | PASS |  |  |
| NVDL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $288M | bars: $282,849,307 | PASS | LOW |  |
| ONTO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $386.46 | $386.46 | PASS |  |  |
| ONTO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $199.57 | $199.57 | PASS |  |  |
| ONTO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $386.46 / $121.57 | $386.46 / $121.57 | PASS |  |  |
| ONTO | PD3 | % from High | -48.4% | -48.4% | PASS |  |  |
| ONTO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $199M | bars: $206,802,768 | PASS | LOW |  |
| ORBX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $14.46 | $14.46 | PASS |  |  |
| ORBX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.62 / $12.81 | $31.62 / $12.81 | PASS |  |  |
| ORBX.TO | PD3 | % from High | -54.3% | -54.3% | PASS |  |  |
| ORCL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $248.46 | $248.46 | PASS |  |  |
| ORCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $115.00 | $115.00 | PASS |  |  |
| ORCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $248.46 / $109.21 | $248.46 / $109.21 | PASS |  |  |
| ORCL | PD3 | % from High | -53.7% | -53.7% | PASS |  |  |
| ORCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.9B | bars: $4,220,551,513 | PASS | LOW |  |
| PG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $173.59 | $173.59 | PASS |  |  |
| PG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $171.72 | $171.72 | PASS |  |  |
| PG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $173.59 / $133.74 | $173.59 / $133.74 | PASS |  |  |
| PG | PD3 | % from High | -1.1% | -1.1% | PASS |  |  |
| PG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,617,489,982 | PASS | LOW |  |
| PLD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $152.14 | $152.14 | PASS |  |  |
| PLD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $125.56 | $125.56 | PASS |  |  |
| PLD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $152.14 / $117.70 | $152.14 / $117.70 | PASS |  |  |
| PLD | PD3 | % from High | -17.5% | -17.5% | PASS |  |  |
| PLD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $462M | bars: $484,416,291 | PASS | LOW |  |
| PNG.V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $10.72 | $10.72 | PASS |  |  |
| PNG.V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3.12 | $3.12 | PASS |  |  |
| PNG.V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $10.72 / $3.07 | $10.72 / $3.07 | PASS |  |  |
| PNG.V | PD3 | % from High | -70.9% | -70.9% | PASS |  |  |
| PNG.V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $3,739,960 | PASS | LOW |  |
| QCOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $257.56 | $257.56 | PASS |  |  |
| QCOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $166.67 | $166.67 | PASS |  |  |
| QCOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $257.56 / $120.88 | $257.56 / $120.88 | PASS |  |  |
| QCOM | PD3 | % from High | -35.3% | -35.3% | PASS |  |  |
| QCOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.1B | bars: $2,220,263,808 | PASS | LOW |  |
| QPUX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.28 | $80.28 | PASS |  |  |
| QPUX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3.32 | $3.32 | PASS |  |  |
| QPUX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.28 / $3.15 | $80.28 / $3.15 | PASS |  |  |
| QPUX | PD3 | % from High | -95.9% | -95.9% | PASS |  |  |
| QTUM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $169.21 | $169.21 | PASS |  |  |
| QTUM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $122.42 | $122.42 | PASS |  |  |
| QTUM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $169.21 / $97.17 | $169.21 / $97.17 | PASS |  |  |
| QTUM | PD3 | % from High | -27.7% | -27.7% | PASS |  |  |
| QTUM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $40M | bars: $40,959,790 | PASS | LOW |  |
| RBOT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.15 | $38.15 | PASS |  |  |
| RBOT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $27.09 | $27.09 | PASS |  |  |
| RBOT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.15 / $27.00 | $38.15 / $27.00 | PASS |  |  |
| RBOT.TO | PD3 | % from High | -29.0% | -29.0% | PASS |  |  |
| RTX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $226.41 | $226.41 | PASS |  |  |
| RTX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $198.00 | $198.00 | PASS |  |  |
| RTX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $226.41 / $164.95 | $226.41 / $164.95 | PASS |  |  |
| RTX | PD3 | % from High | -12.5% | -12.5% | PASS |  |  |
| RTX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $924M | bars: $958,404,087 | PASS | LOW |  |
| RY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.65 | $302.65 | PASS |  |  |
| RY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $280.99 | $280.99 | PASS |  |  |
| RY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.65 / $199.32 | $302.65 / $199.32 | PASS |  |  |
| RY.TO | PD3 | % from High | -7.2% | -7.2% | PASS |  |  |
| RY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $911M | bars: $934,190,785 | PASS | LOW |  |
| SETM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $40.55 | $40.55 | PASS |  |  |
| SETM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $22.11 | $22.11 | PASS |  |  |
| SETM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $40.55 / $21.98 | $40.55 / $21.98 | PASS |  |  |
| SETM | PD3 | % from High | -45.5% | -45.5% | PASS |  |  |
| SETM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $3,678,373 | PASS | LOW |  |
| SGRD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.95 | $17.95 | PASS |  |  |
| SGRD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $22.49 / $17.20 | $22.49 / $17.20 | PASS |  |  |
| SGRD.TO | PD3 | % from High | -20.2% | -20.2% | PASS |  |  |
| SMH | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $671.83 | $671.83 | PASS |  |  |
| SMH | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $460.10 | $460.10 | PASS |  |  |
| SMH | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $671.83 / $314.07 | $671.83 / $314.07 | PASS |  |  |
| SMH | PD3 | % from High | -31.5% | -31.5% | PASS |  |  |
| SMH | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.0B | bars: $4,239,316,053 | PASS | LOW |  |
| SNDK.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $19.28 | $19.28 | PASS |  |  |
| SNDK.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $57.55 / $18.14 | $57.55 / $18.14 | PASS |  |  |
| SNDK.TO | PD3 | % from High | -66.5% | -66.5% | PASS |  |  |
| SNDK.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $24M | bars: $24,161,236 | PASS | LOW |  |
| SO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $97.65 | $97.65 | PASS |  |  |
| SO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $93.60 | $93.60 | PASS |  |  |
| SO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $97.65 / $81.03 | $97.65 / $81.03 | PASS |  |  |
| SO | PD3 | % from High | -4.1% | -4.1% | PASS |  |  |
| SO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $652M | bars: $675,060,130 | PASS | LOW |  |
| SOXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $301.80 | $301.80 | PASS |  |  |
| SOXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $49.07 | $49.07 | PASS |  |  |
| SOXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $301.80 / $28.10 | $301.80 / $28.10 | PASS |  |  |
| SOXL | PD3 | % from High | -83.7% | -83.7% | PASS |  |  |
| SOXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5.2B | bars: $5,849,441,202 | PASS | LOW |  |
| SOXL.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $74.21 | $74.21 | PASS |  |  |
| SOXL.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.36 | $12.36 | PASS |  |  |
| SOXL.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $74.21 / $7.92 | $74.21 / $7.92 | PASS |  |  |
| SOXL.NE | PD3 | % from High | -83.3% | -83.3% | PASS |  |  |
| SOXL.NE | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| SOXX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $218.51 | $218.51 | PASS |  |  |
| SOXX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $141.46 | $141.46 | PASS |  |  |
| SOXX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $218.51 / $86.54 | $218.51 / $86.54 | PASS |  |  |
| SOXX | PD3 | % from High | -35.3% | -35.3% | PASS |  |  |
| SOXX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.0B | bars: $4,216,408,953 | PASS | LOW |  |
| SPCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $10.13 | $10.13 | PASS |  |  |
| SPCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $83.85 / $8.20 | $83.85 / $8.20 | PASS |  |  |
| SPCL | PD3 | % from High | -87.9% | -87.9% | PASS |  |  |
| TSLA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $498.83 | $498.83 | PASS |  |  |
| TSLA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $380.11 | $380.11 | PASS |  |  |
| TSLA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $498.83 / $297.38 | $498.83 / $297.38 | PASS |  |  |
| TSLA | PD3 | % from High | -23.8% | -23.8% | PASS |  |  |
| TSLA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $14.3B | bars: $13,748,237,901 | PASS | LOW |  |
| TSLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $23.10 | $23.10 | PASS |  |  |
| TSLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $9.81 | $9.81 | PASS |  |  |
| TSLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $23.10 / $6.65 | $23.10 / $6.65 | PASS |  |  |
| TSLL | PD3 | % from High | -57.5% | -57.5% | PASS |  |  |
| TSLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $646M | bars: $538,544,182 | PASS | LOW |  |
| TSM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $487.47 | $487.47 | PASS |  |  |
| TSM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $359.69 | $359.69 | PASS |  |  |
| TSM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $487.47 / $264.03 | $487.47 / $264.03 | PASS |  |  |
| TSM | PD3 | % from High | -26.2% | -26.2% | PASS |  |  |
| TSM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.3B | bars: $4,549,195,857 | PASS | LOW |  |
| UBOT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $31.91 | $31.91 | PASS |  |  |
| UBOT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $15.04 | $15.04 | PASS |  |  |
| UBOT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.91 / $14.88 | $31.91 / $14.88 | PASS |  |  |
| UBOT | PD3 | % from High | -52.9% | -52.9% | PASS |  |  |
| UFO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $68.12 | $68.12 | PASS |  |  |
| UFO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.30 | $39.30 | PASS |  |  |
| UFO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $68.12 / $30.78 | $68.12 / $30.78 | PASS |  |  |
| UFO | PD3 | % from High | -42.3% | -42.3% | PASS |  |  |
| UFO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $10M | bars: $10,037,542 | PASS | LOW |  |
| URA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $62.28 | $62.28 | PASS |  |  |
| URA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.04 | $30.04 | PASS |  |  |
| URA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $62.28 / $29.64 | $62.28 / $29.64 | PASS |  |  |
| URA | PD3 | % from High | -51.8% | -51.8% | PASS |  |  |
| URA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $118M | bars: $119,432,547 | PASS | LOW |  |
| URAA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $62.21 | $62.21 | PASS |  |  |
| URAA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $11.38 | $11.38 | PASS |  |  |
| URAA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $62.21 / $11.11 | $62.21 / $11.11 | PASS |  |  |
| URAA | PD3 | % from High | -81.7% | -81.7% | PASS |  |  |
| V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $441.41 | $441.41 | PASS |  |  |
| V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $416.77 | $416.77 | PASS |  |  |
| V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $441.41 / $292.20 | $441.41 / $292.20 | PASS |  |  |
| V | PD3 | % from High | -5.6% | -5.6% | PASS |  |  |
| V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.7B | bars: $2,717,405,049 | PASS | LOW |  |
| VFV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $186.14 | $186.14 | PASS |  |  |
| VFV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $197.83 / $155.29 | $197.83 / $155.29 | PASS |  |  |
| VFV.TO | PD3 | % from High | -5.9% | -5.9% | PASS |  |  |
| VFV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $55M | bars: $58,927,408 | PASS | LOW |  |
| VRT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $379.76 | $379.76 | PASS |  |  |
| VRT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $190.37 | $190.37 | PASS |  |  |
| VRT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $379.76 / $147.72 | $379.76 / $147.72 | PASS |  |  |
| VRT | PD3 | % from High | -49.9% | -49.9% | PASS |  |  |
| VRT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.2B | bars: $1,295,332,333 | PASS | LOW |  |
| WDC.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.13 | $17.13 | PASS |  |  |
| WDC.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $48.85 / $15.70 | $48.85 / $15.70 | PASS |  |  |
| WDC.TO | PD3 | % from High | -64.9% | -64.9% | PASS |  |  |
| WELL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $253.37 | $253.37 | PASS |  |  |
| WELL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $245.76 | $245.76 | PASS |  |  |
| WELL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $253.37 / $178.92 | $253.37 / $178.92 | PASS |  |  |
| WELL | PD3 | % from High | -3.0% | -3.0% | PASS |  |  |
| WELL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $677M | bars: $686,297,732 | PASS | LOW |  |
| WMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $134.84 | $134.84 | PASS |  |  |
| WMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $127.52 | $127.52 | PASS |  |  |
| WMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $134.84 / $98.85 | $134.84 / $98.85 | PASS |  |  |
| WMT | PD3 | % from High | -5.4% | -5.4% | PASS |  |  |
| WMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.1B | bars: $2,755,172,955 | PASS | LOW |  |
| XCHP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $161.26 | $161.26 | PASS |  |  |
| XCHP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $105.40 | $105.40 | PASS |  |  |
| XCHP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $161.26 / $64.67 | $161.26 / $64.67 | PASS |  |  |
| XCHP.TO | PD3 | % from High | -34.6% | -34.6% | PASS |  |  |
| XCHP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5M | bars: $5,399,851 | PASS | LOW |  |
| XDRV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $61.36 | $61.36 | PASS |  |  |
| XDRV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.25 | $39.25 | PASS |  |  |
| XDRV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $61.36 / $38.62 | $61.36 / $38.62 | PASS |  |  |
| XDRV.TO | PD3 | % from High | -36.0% | -36.0% | PASS |  |  |
| XDRV.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| XEQT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $44.34 | $44.34 | PASS |  |  |
| XEQT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.38 / $37.96 | $46.38 / $37.96 | PASS |  |  |
| XEQT.TO | PD3 | % from High | -4.4% | -4.4% | PASS |  |  |
| XEQT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $37M | bars: $40,119,040 | PASS | LOW |  |
| XETM.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $61.17 | $61.17 | PASS |  |  |
| XETM.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $93.94 / $60.88 | $93.94 / $60.88 | PASS |  |  |
| XETM.TO | PD3 | % from High | -34.9% | -34.9% | PASS |  |  |
| XGD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $69.54 | $69.54 | PASS |  |  |
| XGD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $51.28 | $51.28 | PASS |  |  |
| XGD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $69.54 / $43.30 | $69.54 / $43.30 | PASS |  |  |
| XGD.TO | PD3 | % from High | -26.3% | -26.3% | PASS |  |  |
| XGD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $26M | bars: $23,671,810 | PASS | LOW |  |
| XOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $187.32 | $187.32 | PASS |  |  |
| XOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $167.21 | $167.21 | PASS |  |  |
| XOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $187.32 / $111.24 | $187.32 / $111.24 | PASS |  |  |
| XOM | PD3 | % from High | -10.7% | -10.7% | PASS |  |  |
| XOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.3B | bars: $2,249,869,194 | PASS | LOW |  |
| AAPL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $351.91 / RS 1.19 | $351.91 / RS 1.19 | PASS |  |  |
| AAPL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.19 | 1.19 | PASS |  |  |
| AAPL | RS2 | Stock 52W Return and S&P 52W Return | +32.0% / +11.2% | +32.0% / +11.2% | PASS |  |  |
| AAPL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 65 | 65 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| AAPL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +32.0% clears | +32.0% clears | PASS |  |  |
| AAPU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $48.49 / RS 1.34 | $48.49 / RS 1.34 | PASS |  |  |
| AAPU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.34 | 1.34 | PASS |  |  |
| AAPU | RS2 | Stock 52W Return and S&P 52W Return | +49.5% / +11.2% | +49.5% / +11.2% | PASS |  |  |
| AAPU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 78 | 78 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market | Well ahead of the market | PASS |  |  |
| AAPU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.5% clears | +49.5% clears | PASS |  |  |
| ABBV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $292.82 / RS 1.16 | $292.82 / RS 1.16 | PASS |  |  |
| ABBV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.16 | 1.16 | PASS |  |  |
| ABBV | RS2 | Stock 52W Return and S&P 52W Return | +28.9% / +11.2% | +28.9% / +11.2% | PASS |  |  |
| ABBV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ABBV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 63 | 63 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ABBV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| ABBV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.9% clears | +28.9% clears | PASS |  |  |
| AIPO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $22.63 / RS 0.92 | $22.63 / RS 0.92 | PASS |  |  |
| AIPO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| AIPO | RS2 | Stock 52W Return and S&P 52W Return | +2.0% / +11.2% | +2.0% / +11.2% | PASS |  |  |
| AIPO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AIPO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AIPO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| AIPO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.0% under | +2.0% under | PASS |  |  |
| ALAB | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $211.60 / RS 1.35 | $211.60 / RS 1.35 | PASS |  |  |
| ALAB | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.35 | 1.35 | PASS |  |  |
| ALAB | RS2 | Stock 52W Return and S&P 52W Return | +49.7% / +11.2% | +49.7% / +11.2% | PASS |  |  |
| ALAB | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ALAB | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 78 | 78 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ALAB | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ALAB | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.7% clears | +49.7% clears | PASS |  |  |
| AMD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $503.41 / RS 1.88 | $503.41 / RS 1.88 | PASS |  |  |
| AMD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.88 | 1.88 | PASS |  |  |
| AMD | RS2 | Stock 52W Return and S&P 52W Return | +109.3% / +11.2% | +109.3% / +11.2% | PASS |  |  |
| AMD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +109.3% clears | +109.3% clears | PASS |  |  |
| AMD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.95 / RS 1.84 | $12.95 / RS 1.84 | PASS |  |  |
| AMD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.84 | 1.84 | PASS |  |  |
| AMD.TO | RS2 | Stock 52W Return and S&P 52W Return | +104.3% / +11.2% | +104.3% / +11.2% | PASS |  |  |
| AMD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +104.3% clears | +104.3% clears | PASS |  |  |
| AMZN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $257.89 / RS 1.00 | $257.89 / RS 1.00 | PASS |  |  |
| AMZN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.00 | 1.00 | PASS |  |  |
| AMZN | RS2 | Stock 52W Return and S&P 52W Return | +10.7% / +11.2% | +10.7% / +11.2% | PASS |  |  |
| AMZN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| AMZN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +10.7% clears | +10.7% clears | PASS |  |  |
| AMZU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $35.25 / RS 0.89 | $35.25 / RS 0.89 | PASS |  |  |
| AMZU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| AMZU | RS2 | Stock 52W Return and S&P 52W Return | -1.1% / +11.2% | -1.1% / +11.2% | PASS |  |  |
| AMZU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| AMZU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.1% negative | -1.1% negative | PASS |  |  |
| ANET.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $33.32 / RS 1.26 | $33.32 / RS 1.26 | PASS |  |  |
| ANET.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.26 | 1.26 | PASS |  |  |
| ANET.TO | RS2 | Stock 52W Return and S&P 52W Return | +39.8% / +11.2% | +39.8% / +11.2% | PASS |  |  |
| ANET.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 71 | 71 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ANET.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| ANET.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.8% clears | +39.8% clears | PASS |  |  |
| ASML.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $40.80 / RS 1.29 | $40.80 / RS 1.29 | PASS |  |  |
| ASML.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.29 | 1.29 | PASS |  |  |
| ASML.TO | RS2 | Stock 52W Return and S&P 52W Return | +43.4% / +11.2% | +43.4% / +11.2% | PASS |  |  |
| ASML.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASML.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 73 | 73 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASML.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| ASML.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +43.4% clears | +43.4% clears | PASS |  |  |
| ASTL.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $7.25 / RS 1.33 | $7.25 / RS 1.33 | PASS |  |  |
| ASTL.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.33 | 1.33 | PASS |  |  |
| ASTL.TO | RS2 | Stock 52W Return and S&P 52W Return | +47.7% / +11.2% | +47.7% / +11.2% | PASS |  |  |
| ASTL.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASTL.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 76 | 76 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASTL.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ASTL.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +47.7% clears | +47.7% clears | PASS |  |  |
| ATD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $83.65 / RS 1.08 | $83.65 / RS 1.09 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| ATD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.08 | 1.09 | PASS |  |  |
| ATD.TO | RS2 | Stock 52W Return and S&P 52W Return | +20.7% / +11.2% | +20.7% / +11.2% | PASS |  |  |
| ATD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ATD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ATD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| ATD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +20.7% clears | +20.7% clears | PASS |  |  |
| AVGC | RS1 | a history of 99 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| AVGO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $341.60 / RS 0.90 | $341.60 / RS 0.90 | PASS |  |  |
| AVGO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| AVGO | RS2 | Stock 52W Return and S&P 52W Return | +0.4% / +11.2% | +0.4% / +11.2% | PASS |  |  |
| AVGO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AVGO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| AVGO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.4% under | +0.4% under | PASS |  |  |
| AVGO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.94 / RS 0.88 | $12.94 / RS 0.88 | PASS |  |  |
| AVGO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| AVGO.TO | RS2 | Stock 52W Return and S&P 52W Return | -1.8% / +11.2% | -1.8% / +11.2% | PASS |  |  |
| AVGO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| AVGO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.8% negative | -1.8% negative | PASS |  |  |
| BDT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $71.13 / RS 2.62 | $71.13 / RS 2.61 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| BDT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.62 | 2.61 | PASS |  |  |
| BDT.TO | RS2 | Stock 52W Return and S&P 52W Return | +190.8% / +11.2% | +190.8% / +11.2% | PASS |  |  |
| BDT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BDT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BDT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| BDT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +190.8% clears | +190.8% clears | PASS |  |  |
| BOTZ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $29.71 / RS 0.78 | $29.71 / RS 0.78 | PASS |  |  |
| BOTZ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.78 | 0.78 | PASS |  |  |
| BOTZ | RS2 | Stock 52W Return and S&P 52W Return | -13.0% / +11.2% | -13.0% / +11.2% | PASS |  |  |
| BOTZ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BOTZ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BOTZ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| BOTZ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -13.0% negative | -13.0% negative | PASS |  |  |
| BRK-B | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $586.76 / RS 1.05 | $586.76 / RS 1.05 | PASS |  |  |
| BRK-B | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.05 | 1.05 | PASS |  |  |
| BRK-B | RS2 | Stock 52W Return and S&P 52W Return | +16.6% / +11.2% | +16.6% / +11.2% | PASS |  |  |
| BRK-B | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRK-B | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 54 | 54 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRK-B | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRK-B | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +16.6% clears | +16.6% clears | PASS |  |  |
| BRKU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.19 / RS 1.09 | $30.19 / RS 1.09 | PASS |  |  |
| BRKU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| BRKU | RS2 | Stock 52W Return and S&P 52W Return | +21.4% / +11.2% | +21.4% / +11.2% | PASS |  |  |
| BRKU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRKU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRKU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRKU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +21.4% clears | +21.4% clears | PASS |  |  |
| CAMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $94.96 / RS 0.89 | $94.96 / RS 0.89 | PASS |  |  |
| CAMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| CAMT | RS2 | Stock 52W Return and S&P 52W Return | -1.0% / +11.2% | -1.0% / +11.2% | PASS |  |  |
| CAMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| CAMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.0% negative | -1.0% negative | PASS |  |  |
| CARS.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $19.88 / RS 0.69 | $19.88 / RS 0.69 | PASS |  |  |
| CARS.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.69 | 0.69 | PASS |  |  |
| CARS.TO | RS2 | Stock 52W Return and S&P 52W Return | -23.1% / +11.2% | -23.2% / +11.2% | PASS |  |  |
| CARS.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CARS.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 25 | 25 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CARS.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CARS.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -23.1% negative | -23.2% negative | PASS |  |  |
| CAT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $570.79 / RS 0.94 | $570.79 / RS 0.94 | PASS |  |  |
| CAT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| CAT | RS2 | Stock 52W Return and S&P 52W Return | +4.3% / +11.2% | +4.3% / +11.2% | PASS |  |  |
| CAT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| CAT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.3% under | +4.3% under | PASS |  |  |
| CCO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $92.16 / RS 0.71 | $92.16 / RS 0.71 | PASS |  |  |
| CCO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.71 | 0.71 | PASS |  |  |
| CCO.TO | RS2 | Stock 52W Return and S&P 52W Return | -20.8% / +11.2% | -20.8% / +11.2% | PASS |  |  |
| CCO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CCO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 27 | 27 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CCO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| CCO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -20.8% negative | -20.8% negative | PASS |  |  |
| CEG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $268.07 / RS 0.72 | $268.07 / RS 0.72 | PASS |  |  |
| CEG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.72 | 0.72 | PASS |  |  |
| CEG | RS2 | Stock 52W Return and S&P 52W Return | -20.4% / +11.2% | -20.4% / +11.2% | PASS |  |  |
| CEG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CEG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 27 | 27 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CEG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CEG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -20.4% negative | -20.4% negative | PASS |  |  |
| CGY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $84.30 / RS 1.49 | $84.30 / RS 1.49 | PASS |  |  |
| CGY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.49 | 1.49 | PASS |  |  |
| CGY.TO | RS2 | Stock 52W Return and S&P 52W Return | +65.3% / +11.2% | +65.3% / +11.2% | PASS |  |  |
| CGY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CGY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 89 | 89 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CGY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CGY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +65.3% clears | +65.3% clears | PASS |  |  |
| CNQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $68.29 / RS 1.37 | $68.29 / RS 1.37 | PASS |  |  |
| CNQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.37 | 1.37 | PASS |  |  |
| CNQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +51.9% / +11.2% | +51.9% / +11.2% | PASS |  |  |
| CNQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 79 | 79 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CNQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +51.9% clears | +51.9% clears | PASS |  |  |
| CNR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $180.54 / RS 1.24 | $180.54 / RS 1.24 | PASS |  |  |
| CNR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.24 | 1.24 | PASS |  |  |
| CNR.TO | RS2 | Stock 52W Return and S&P 52W Return | +37.9% / +11.2% | +37.9% / +11.2% | PASS |  |  |
| CNR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 69 | 69 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CNR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +37.9% clears | +37.9% clears | PASS |  |  |
| COP | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $139.48 / RS 1.45 | $139.48 / RS 1.45 | PASS |  |  |
| COP | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.45 | 1.45 | PASS |  |  |
| COP | RS2 | Stock 52W Return and S&P 52W Return | +61.7% / +11.2% | +61.7% / +11.2% | PASS |  |  |
| COP | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COP | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 86 | 86 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COP | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| COP | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +61.7% clears | +61.7% clears | PASS |  |  |
| COPP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $46.42 / RS 0.95 | $46.42 / RS 0.95 | PASS |  |  |
| COPP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.95 | PASS |  |  |
| COPP.TO | RS2 | Stock 52W Return and S&P 52W Return | +6.0% / +11.2% | +6.1% / +11.2% | PASS |  |  |
| COPP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| COPP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.0% clears | +6.1% clears | PASS |  |  |
| COPX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $65.31 / RS 1.01 | $65.31 / RS 1.01 | PASS |  |  |
| COPX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.01 | PASS |  |  |
| COPX | RS2 | Stock 52W Return and S&P 52W Return | +11.8% / +11.2% | +11.9% / +11.2% | PASS |  |  |
| COPX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| COPX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +11.8% clears | +11.9% clears | PASS |  |  |
| COPZ | RS1 | a history of 190 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| COST | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,110.08 / RS 1.10 | $1,110.08 / RS 1.10 | PASS |  |  |
| COST | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.10 | 1.10 | PASS |  |  |
| COST | RS2 | Stock 52W Return and S&P 52W Return | +22.4% / +11.2% | +22.4% / +11.2% | PASS |  |  |
| COST | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COST | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COST | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| COST | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +22.4% clears | +22.4% clears | PASS |  |  |
| COTG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $16.93 / RS 1.16 | $16.93 / RS 1.16 | PASS |  |  |
| COTG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.16 | 1.16 | PASS |  |  |
| COTG | RS2 | Stock 52W Return and S&P 52W Return | +28.6% / +11.2% | +28.5% / +11.2% | PASS |  |  |
| COTG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COTG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COTG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| COTG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.6% clears | +28.5% clears | PASS |  |  |
| CSU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3,316.93 / RS 0.92 | $3,316.93 / RS 0.92 | PASS |  |  |
| CSU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| CSU.TO | RS2 | Stock 52W Return and S&P 52W Return | +2.4% / +11.2% | +2.4% / +11.2% | PASS |  |  |
| CSU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CSU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CSU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| CSU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.4% under | +2.4% under | PASS |  |  |
| CVX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $216.13 / RS 1.30 | $216.13 / RS 1.30 | PASS |  |  |
| CVX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.30 | 1.30 | PASS |  |  |
| CVX | RS2 | Stock 52W Return and S&P 52W Return | +45.1% / +11.2% | +45.1% / +11.2% | PASS |  |  |
| CVX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CVX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CVX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CVX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +45.1% clears | +45.1% clears | PASS |  |  |
| DRAL | RS1 | a history of 102 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| DRAM | RS1 | a history of 159 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| DRIV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $27.00 / RS 0.85 | $27.00 / RS 0.85 | PASS |  |  |
| DRIV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| DRIV | RS2 | Stock 52W Return and S&P 52W Return | -5.6% / +11.2% | -5.6% / +11.2% | PASS |  |  |
| DRIV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DRIV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DRIV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| DRIV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.6% negative | -5.6% negative | PASS |  |  |
| DUK | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $129.84 / RS 0.96 | $129.84 / RS 0.97 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| DUK | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.97 | PASS |  |  |
| DUK | RS2 | Stock 52W Return and S&P 52W Return | +7.3% / +11.2% | +7.3% / +11.2% | PASS |  |  |
| DUK | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DUK | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DUK | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| DUK | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +7.3% clears | +7.3% clears | PASS |  |  |
| ELIL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $40.25 / RS 1.41 | $40.25 / RS 1.41 | PASS |  |  |
| ELIL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.41 | 1.41 | PASS |  |  |
| ELIL | RS2 | Stock 52W Return and S&P 52W Return | +56.3% / +11.2% | +56.3% / +11.2% | PASS |  |  |
| ELIL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ELIL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 82 | 82 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ELIL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ELIL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +56.3% clears | +56.3% clears | PASS |  |  |
| EQIX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,034.83 / RS 1.22 | $1,034.83 / RS 1.22 | PASS |  |  |
| EQIX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.22 | 1.22 | PASS |  |  |
| EQIX | RS2 | Stock 52W Return and S&P 52W Return | +36.0% / +11.2% | +36.1% / +11.2% | PASS |  |  |
| EQIX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| EQIX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 68 | 68 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| EQIX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| EQIX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +36.0% clears | +36.1% clears | PASS |  |  |
| ETN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $337.11 / RS 0.89 | $337.11 / RS 0.89 | PASS |  |  |
| ETN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| ETN | RS2 | Stock 52W Return and S&P 52W Return | -0.5% / +11.2% | -0.5% / +11.2% | PASS |  |  |
| ETN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ETN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ETN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| ETN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -0.5% negative | -0.5% negative | PASS |  |  |
| FCX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $55.30 / RS 1.29 | $55.30 / RS 1.29 | PASS |  |  |
| FCX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.29 | 1.29 | PASS |  |  |
| FCX | RS2 | Stock 52W Return and S&P 52W Return | +43.1% / +11.2% | +43.1% / +11.2% | PASS |  |  |
| FCX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FCX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 73 | 73 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FCX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| FCX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +43.1% clears | +43.1% clears | PASS |  |  |
| FINN.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $31.76 / RS 1.26 | $31.76 / RS 1.26 | PASS |  |  |
| FINN.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.26 | 1.26 | PASS |  |  |
| FINN.NE | RS2 | Stock 52W Return and S&P 52W Return | +39.7% / +11.2% | +39.7% / +11.2% | PASS |  |  |
| FINN.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FINN.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 71 | 71 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FINN.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| FINN.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.7% clears | +39.7% clears | PASS |  |  |
| GDX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $79.57 / RS 0.96 | $79.57 / RS 0.96 | PASS |  |  |
| GDX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.96 | PASS |  |  |
| GDX | RS2 | Stock 52W Return and S&P 52W Return | +6.9% / +11.2% | +6.9% / +11.2% | PASS |  |  |
| GDX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| GDX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.9% clears | +6.9% clears | PASS |  |  |
| GDXU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $24.60 / RS 0.75 | $24.60 / RS 0.75 | PASS |  |  |
| GDXU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.75 | 0.75 | PASS |  |  |
| GDXU.TO | RS2 | Stock 52W Return and S&P 52W Return | -16.9% / +11.2% | -16.9% / +11.2% | PASS |  |  |
| GDXU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDXU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 30 | 30 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDXU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| GDXU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -16.9% negative | -16.9% negative | PASS |  |  |
| GE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $326.40 / RS 0.98 | $326.40 / RS 0.98 | PASS |  |  |
| GE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.98 | 0.98 | PASS |  |  |
| GE | RS2 | Stock 52W Return and S&P 52W Return | +9.3% / +11.2% | +9.3% / +11.2% | PASS |  |  |
| GE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 49 | 49 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +9.3% clears | +9.3% clears | PASS |  |  |
| GEV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $779.91 / RS 1.22 | $779.91 / RS 1.22 | PASS |  |  |
| GEV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.22 | 1.22 | PASS |  |  |
| GEV | RS2 | Stock 52W Return and S&P 52W Return | +35.5% / +11.2% | +35.5% / +11.2% | PASS |  |  |
| GEV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GEV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| GEV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +35.5% clears | +35.5% clears | PASS |  |  |
| GEV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $52.13 / RS 1.04 | $52.13 / RS 1.04 | PASS |  |  |
| GEV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.04 | 1.04 | PASS |  |  |
| GEV.TO | RS2 | Stock 52W Return and S&P 52W Return | +15.8% / +11.2% | +15.8% / +11.2% | PASS |  |  |
| GEV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 53 | 53 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| GEV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +15.8% clears | +15.8% clears | PASS |  |  |
| GGLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $63.05 / RS 0.70 | $63.05 / RS 0.70 | PASS |  |  |
| GGLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.70 | 0.70 | PASS |  |  |
| GGLL | RS2 | Stock 52W Return and S&P 52W Return | -21.9% / +11.2% | -21.9% / +11.2% | PASS |  |  |
| GGLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GGLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 26 | 26 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GGLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| GGLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -21.9% negative | -21.9% negative | PASS |  |  |
| GIB-A.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $115.07 / RS 0.86 | $115.07 / RS 0.86 | PASS |  |  |
| GIB-A.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.86 | 0.86 | PASS |  |  |
| GIB-A.TO | RS2 | Stock 52W Return and S&P 52W Return | -4.3% / +11.2% | -4.3% / +11.2% | PASS |  |  |
| GIB-A.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GIB-A.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 39 | 39 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GIB-A.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| GIB-A.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.3% negative | -4.3% negative | PASS |  |  |
| GOOGL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $280.20 / RS 0.89 | $280.20 / RS 0.89 | PASS |  |  |
| GOOGL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| GOOGL | RS2 | Stock 52W Return and S&P 52W Return | -1.4% / +11.2% | -1.4% / +11.2% | PASS |  |  |
| GOOGL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GOOGL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GOOGL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| GOOGL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.4% negative | -1.4% negative | PASS |  |  |
| GRID | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $155.15 / RS 0.93 | $155.15 / RS 0.93 | PASS |  |  |
| GRID | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.93 | 0.93 | PASS |  |  |
| GRID | RS2 | Stock 52W Return and S&P 52W Return | +3.9% / +11.2% | +3.9% / +11.2% | PASS |  |  |
| GRID | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GRID | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GRID | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GRID | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.9% under | +3.9% under | PASS |  |  |
| HD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $339.01 / RS 0.88 | $339.01 / RS 0.88 | PASS |  |  |
| HD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| HD | RS2 | Stock 52W Return and S&P 52W Return | -2.6% / +11.2% | -2.7% / +11.2% | PASS |  |  |
| HD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| HD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -2.6% negative | -2.7% negative | PASS |  |  |
| HURA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $37.39 / RS 0.66 | $37.39 / RS 0.66 | PASS |  |  |
| HURA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.66 | 0.66 | PASS |  |  |
| HURA.TO | RS2 | Stock 52W Return and S&P 52W Return | -26.5% / +11.2% | -26.5% / +11.2% | PASS |  |  |
| HURA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HURA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 23 | 23 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HURA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| HURA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -26.5% negative | -26.5% negative | PASS |  |  |
| HXQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $110.63 / RS 0.99 | $110.63 / RS 1.00 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| HXQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.99 | 1.00 | PASS |  |  |
| HXQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +10.7% / +11.2% | +10.7% / +11.2% | PASS |  |  |
| HXQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HXQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HXQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| HXQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +10.7% clears | +10.7% clears | PASS |  |  |
| JNJ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $278.70 / RS 1.28 | $278.70 / RS 1.28 | PASS |  |  |
| JNJ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.28 | 1.28 | PASS |  |  |
| JNJ | RS2 | Stock 52W Return and S&P 52W Return | +42.8% / +11.2% | +42.8% / +11.2% | PASS |  |  |
| JNJ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JNJ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 73 | 73 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JNJ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| JNJ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +42.8% clears | +42.8% clears | PASS |  |  |
| JPM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $329.96 / RS 1.01 | $329.96 / RS 1.01 | PASS |  |  |
| JPM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.01 | PASS |  |  |
| JPM | RS2 | Stock 52W Return and S&P 52W Return | +12.0% / +11.2% | +12.0% / +11.2% | PASS |  |  |
| JPM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JPM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JPM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| JPM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +12.0% clears | +12.0% clears | PASS |  |  |
| KEYS | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $284.45 / RS 1.46 | $284.45 / RS 1.46 | PASS |  |  |
| KEYS | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.46 | 1.46 | PASS |  |  |
| KEYS | RS2 | Stock 52W Return and S&P 52W Return | +62.1% / +11.2% | +62.1% / +11.2% | PASS |  |  |
| KEYS | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| KEYS | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 87 | 87 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| KEYS | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| KEYS | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +62.1% clears | +62.1% clears | PASS |  |  |
| LIN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $515.11 / RS 1.12 | $515.11 / RS 1.12 | PASS |  |  |
| LIN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.12 | 1.12 | PASS |  |  |
| LIN | RS2 | Stock 52W Return and S&P 52W Return | +24.9% / +11.2% | +24.9% / +11.2% | PASS |  |  |
| LIN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LIN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LIN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| LIN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +24.9% clears | +24.9% clears | PASS |  |  |
| LLY | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,415.55 / RS 1.25 | $1,415.55 / RS 1.25 | PASS |  |  |
| LLY | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.25 | PASS |  |  |
| LLY | RS2 | Stock 52W Return and S&P 52W Return | +39.4% / +11.2% | +39.4% / +11.2% | PASS |  |  |
| LLY | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LLY | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LLY | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| LLY | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.4% clears | +39.4% clears | PASS |  |  |
| MDA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.22 / RS 1.65 | $39.22 / RS 1.64 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| MDA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.65 | 1.64 | PASS |  |  |
| MDA.TO | RS2 | Stock 52W Return and S&P 52W Return | +82.9% / +11.2% | +82.9% / +11.2% | PASS |  |  |
| MDA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MDA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MDA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MDA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +82.9% clears | +82.9% clears | PASS |  |  |
| META | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $618.87 / RS 0.93 | $618.87 / RS 0.93 | PASS |  |  |
| META | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.93 | 0.93 | PASS |  |  |
| META | RS2 | Stock 52W Return and S&P 52W Return | +3.1% / +11.2% | +3.2% / +11.2% | PASS |  |  |
| META | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| META | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| META | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| META | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.1% under | +3.2% under | PASS |  |  |
| METU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $21.57 / RS 0.73 | $21.57 / RS 0.73 | PASS |  |  |
| METU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.73 | 0.73 | PASS |  |  |
| METU | RS2 | Stock 52W Return and S&P 52W Return | -19.1% / +11.2% | -19.1% / +11.2% | PASS |  |  |
| METU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| METU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 28 | 28 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| METU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| METU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -19.1% negative | -19.1% negative | PASS |  |  |
| MRVL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $148.74 / RS 1.60 | $148.74 / RS 1.61 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| MRVL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.60 | 1.61 | PASS |  |  |
| MRVL | RS2 | Stock 52W Return and S&P 52W Return | +78.5% / +11.2% | +78.5% / +11.2% | PASS |  |  |
| MRVL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MRVL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 98 | 98 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MRVL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MRVL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +78.5% clears | +78.5% clears | PASS |  |  |
| MSFT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $506.24 / RS 0.90 | $506.24 / RS 0.90 | PASS |  |  |
| MSFT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| MSFT | RS2 | Stock 52W Return and S&P 52W Return | +0.6% / +11.2% | +0.6% / +11.2% | PASS |  |  |
| MSFT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| MSFT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.6% under | +0.6% under | PASS |  |  |
| MSFU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $37.34 / RS 0.74 | $37.34 / RS 0.74 | PASS |  |  |
| MSFU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.74 | 0.74 | PASS |  |  |
| MSFU | RS2 | Stock 52W Return and S&P 52W Return | -17.9% / +11.2% | -17.9% / +11.2% | PASS |  |  |
| MSFU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 29 | 29 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| MSFU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -17.9% negative | -17.9% negative | PASS |  |  |
| MTRX.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $29.13 / RS 0.88 | $29.13 / RS 0.88 | PASS |  |  |
| MTRX.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| MTRX.TO | RS2 | Stock 52W Return and S&P 52W Return | -2.1% / +11.2% | -2.1% / +11.2% | PASS |  |  |
| MTRX.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MTRX.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| MTRX.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -2.1% negative | -2.1% negative | PASS |  |  |
| MU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $31.04 / RS 2.57 | $31.04 / RS 2.57 | PASS |  |  |
| MU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.57 | 2.57 | PASS |  |  |
| MU.TO | RS2 | Stock 52W Return and S&P 52W Return | +185.8% / +11.2% | +185.8% / +11.2% | PASS |  |  |
| MU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +185.8% clears | +185.8% clears | PASS |  |  |
| NEE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $84.42 / RS 0.91 | $84.42 / RS 0.91 | PASS |  |  |
| NEE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.91 | 0.91 | PASS |  |  |
| NEE | RS2 | Stock 52W Return and S&P 52W Return | +1.3% / +11.2% | +1.3% / +11.2% | PASS |  |  |
| NEE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| NEE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +1.3% under | +1.3% under | PASS |  |  |
| NEM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $111.26 / RS 1.16 | $111.26 / RS 1.16 | PASS |  |  |
| NEM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.16 | 1.16 | PASS |  |  |
| NEM | RS2 | Stock 52W Return and S&P 52W Return | +28.9% / +11.2% | +29.0% / +11.2% | PASS |  |  |
| NEM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 63 | 63 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| NEM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.9% clears | +29.0% clears | PASS |  |  |
| NFLX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $59.68 / RS 0.49 | $59.68 / RS 0.49 | PASS |  |  |
| NFLX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.49 | 0.49 | PASS |  |  |
| NFLX | RS2 | Stock 52W Return and S&P 52W Return | -45.9% / +11.2% | -45.9% / +11.2% | PASS |  |  |
| NFLX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFLX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 9 | 9 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFLX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFLX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -45.9% negative | -45.9% negative | PASS |  |  |
| NFXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $9.86 / RS 0.21 | $9.86 / RS 0.21 | PASS |  |  |
| NFXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.21 | 0.21 | PASS |  |  |
| NFXL | RS2 | Stock 52W Return and S&P 52W Return | -77.0% / +11.2% | -77.0% / +11.2% | PASS |  |  |
| NFXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -77.0% negative | -77.0% negative | PASS |  |  |
| NTR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $99.02 / RS 1.15 | $99.02 / RS 1.15 | PASS |  |  |
| NTR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| NTR.TO | RS2 | Stock 52W Return and S&P 52W Return | +27.7% / +11.2% | +27.7% / +11.2% | PASS |  |  |
| NTR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NTR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NTR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| NTR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +27.7% clears | +27.7% clears | PASS |  |  |
| NVDA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $155.46 / RS 0.75 | $155.46 / RS 0.75 | PASS |  |  |
| NVDA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.75 | 0.75 | PASS |  |  |
| NVDA | RS2 | Stock 52W Return and S&P 52W Return | -16.5% / +11.2% | -16.5% / +11.2% | PASS |  |  |
| NVDA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 30 | 30 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -16.5% negative | -16.5% negative | PASS |  |  |
| NVDL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $16.22 / RS 0.48 | $16.22 / RS 0.48 | PASS |  |  |
| NVDL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.48 | 0.48 | PASS |  |  |
| NVDL | RS2 | Stock 52W Return and S&P 52W Return | -46.1% / +11.2% | -46.1% / +11.2% | PASS |  |  |
| NVDL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 9 | 9 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -46.1% negative | -46.1% negative | PASS |  |  |
| ONTO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $199.57 / RS 1.41 | $199.57 / RS 1.41 | PASS |  |  |
| ONTO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.41 | 1.41 | PASS |  |  |
| ONTO | RS2 | Stock 52W Return and S&P 52W Return | +56.8% / +11.2% | +56.8% / +11.2% | PASS |  |  |
| ONTO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ONTO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 83 | 83 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ONTO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ONTO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +56.8% clears | +56.8% clears | PASS |  |  |
| ORBX.TO | RS1 | a history of 140 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| ORCL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $115.00 / RS 0.48 | $115.00 / RS 0.48 | PASS |  |  |
| ORCL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.48 | 0.48 | PASS |  |  |
| ORCL | RS2 | Stock 52W Return and S&P 52W Return | -47.0% / +11.2% | -47.0% / +11.2% | PASS |  |  |
| ORCL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ORCL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 8 | 8 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ORCL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| ORCL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -47.0% negative | -47.0% negative | PASS |  |  |
| PG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $171.72 / RS 1.09 | $171.72 / RS 1.09 | PASS |  |  |
| PG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| PG | RS2 | Stock 52W Return and S&P 52W Return | +21.2% / +11.2% | +21.2% / +11.2% | PASS |  |  |
| PG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| PG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +21.2% clears | +21.2% clears | PASS |  |  |
| PLD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $125.56 / RS 0.94 | $125.56 / RS 0.94 | PASS |  |  |
| PLD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| PLD | RS2 | Stock 52W Return and S&P 52W Return | +4.8% / +11.2% | +4.8% / +11.2% | PASS |  |  |
| PLD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PLD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PLD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| PLD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.8% under | +4.8% under | PASS |  |  |
| PNG.V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3.12 / RS 0.54 | $3.12 / RS 0.54 | PASS |  |  |
| PNG.V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.54 | 0.54 | PASS |  |  |
| PNG.V | RS2 | Stock 52W Return and S&P 52W Return | -39.9% / +11.2% | -39.9% / +11.2% | PASS |  |  |
| PNG.V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PNG.V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 13 | 13 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PNG.V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| PNG.V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -39.9% negative | -39.9% negative | PASS |  |  |
| QCOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $166.67 / RS 0.92 | $166.67 / RS 0.92 | PASS |  |  |
| QCOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| QCOM | RS2 | Stock 52W Return and S&P 52W Return | +2.0% / +11.2% | +2.0% / +11.2% | PASS |  |  |
| QCOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QCOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QCOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| QCOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.0% under | +2.0% under | PASS |  |  |
| QPUX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3.32 / RS 0.05 | $3.32 / RS 0.05 | PASS |  |  |
| QPUX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.05 | 0.05 | PASS |  |  |
| QPUX | RS2 | Stock 52W Return and S&P 52W Return | -94.5% / +11.2% | -94.5% / +11.2% | PASS |  |  |
| QPUX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QPUX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QPUX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| QPUX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -94.5% negative | -94.5% negative | PASS |  |  |
| QTUM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $122.42 / RS 1.06 | $122.42 / RS 1.06 | PASS |  |  |
| QTUM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.06 | 1.06 | PASS |  |  |
| QTUM | RS2 | Stock 52W Return and S&P 52W Return | +17.7% / +11.2% | +17.7% / +11.2% | PASS |  |  |
| QTUM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QTUM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QTUM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| QTUM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +17.7% clears | +17.7% clears | PASS |  |  |
| RBOT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $27.09 / RS 0.77 | $27.09 / RS 0.76 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| RBOT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.77 | 0.76 | PASS |  |  |
| RBOT.TO | RS2 | Stock 52W Return and S&P 52W Return | -14.9% / +11.2% | -14.9% / +11.2% | PASS |  |  |
| RBOT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RBOT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 31 | 31 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RBOT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| RBOT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -14.9% negative | -14.9% negative | PASS |  |  |
| RTX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $198.00 / RS 1.03 | $198.00 / RS 1.03 | PASS |  |  |
| RTX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| RTX | RS2 | Stock 52W Return and S&P 52W Return | +14.4% / +11.2% | +14.4% / +11.2% | PASS |  |  |
| RTX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RTX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RTX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| RTX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.4% clears | +14.4% clears | PASS |  |  |
| RY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $280.99 / RS 1.25 | $280.99 / RS 1.25 | PASS |  |  |
| RY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.25 | PASS |  |  |
| RY.TO | RS2 | Stock 52W Return and S&P 52W Return | +39.4% / +11.2% | +39.4% / +11.2% | PASS |  |  |
| RY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| RY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.4% clears | +39.4% clears | PASS |  |  |
| SETM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $22.11 / RS 0.78 | $22.11 / RS 0.78 | PASS |  |  |
| SETM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.78 | 0.78 | PASS |  |  |
| SETM | RS2 | Stock 52W Return and S&P 52W Return | -13.7% / +11.2% | -13.7% / +11.2% | PASS |  |  |
| SETM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SETM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 32 | 32 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SETM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| SETM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -13.7% negative | -13.7% negative | PASS |  |  |
| SGRD.TO | RS1 | a history of 146 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| SMH | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $460.10 / RS 1.22 | $460.10 / RS 1.22 | PASS |  |  |
| SMH | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.22 | 1.22 | PASS |  |  |
| SMH | RS2 | Stock 52W Return and S&P 52W Return | +35.6% / +11.2% | +35.6% / +11.2% | PASS |  |  |
| SMH | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SMH | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 68 | 68 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SMH | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| SMH | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +35.6% clears | +35.6% clears | PASS |  |  |
| SNDK.TO | RS1 | a history of 133 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| SO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $93.60 / RS 0.96 | $93.60 / RS 0.96 | PASS |  |  |
| SO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.96 | PASS |  |  |
| SO | RS2 | Stock 52W Return and S&P 52W Return | +6.7% / +11.2% | +6.7% / +11.2% | PASS |  |  |
| SO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| SO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.7% clears | +6.7% clears | PASS |  |  |
| SOXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $49.07 / RS 1.20 | $49.07 / RS 1.20 | PASS |  |  |
| SOXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.20 | 1.20 | PASS |  |  |
| SOXL | RS2 | Stock 52W Return and S&P 52W Return | +33.3% / +11.2% | +33.3% / +11.2% | PASS |  |  |
| SOXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 66 | 66 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +33.3% clears | +33.3% clears | PASS |  |  |
| SOXL.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.36 / RS 1.11 | $12.36 / RS 1.11 | PASS |  |  |
| SOXL.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.11 | 1.11 | PASS |  |  |
| SOXL.NE | RS2 | Stock 52W Return and S&P 52W Return | +23.6% / +11.2% | +23.6% / +11.2% | PASS |  |  |
| SOXL.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 59 | 59 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +23.6% clears | +23.6% clears | PASS |  |  |
| SOXX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $141.46 / RS 1.35 | $141.46 / RS 1.35 | PASS |  |  |
| SOXX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.35 | 1.35 | PASS |  |  |
| SOXX | RS2 | Stock 52W Return and S&P 52W Return | +50.1% / +11.2% | +50.1% / +11.2% | PASS |  |  |
| SOXX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 78 | 78 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| SOXX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +50.1% clears | +50.1% clears | PASS |  |  |
| SPCL | RS1 | a history of 156 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| TSLA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $380.11 / RS 0.84 | $380.11 / RS 0.84 | PASS |  |  |
| TSLA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.84 | 0.84 | PASS |  |  |
| TSLA | RS2 | Stock 52W Return and S&P 52W Return | -7.0% / +11.2% | -7.0% / +11.2% | PASS |  |  |
| TSLA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 37 | 37 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| TSLA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -7.0% negative | -7.0% negative | PASS |  |  |
| TSLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $9.81 / RS 0.55 | $9.81 / RS 0.55 | PASS |  |  |
| TSLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.55 | 0.55 | PASS |  |  |
| TSLL | RS2 | Stock 52W Return and S&P 52W Return | -38.6% / +11.2% | -38.6% / +11.2% | PASS |  |  |
| TSLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 14 | 14 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| TSLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -38.6% negative | -38.6% negative | PASS |  |  |
| TSM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $359.69 / RS 1.16 | $359.69 / RS 1.16 | PASS |  |  |
| TSM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.16 | 1.16 | PASS |  |  |
| TSM | RS2 | Stock 52W Return and S&P 52W Return | +28.9% / +11.2% | +28.9% / +11.2% | PASS |  |  |
| TSM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 63 | 63 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| TSM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.9% clears | +28.9% clears | PASS |  |  |
| UBOT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $15.04 / RS 0.59 | $15.04 / RS 0.59 | PASS |  |  |
| UBOT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.59 | 0.59 | PASS |  |  |
| UBOT | RS2 | Stock 52W Return and S&P 52W Return | -34.1% / +11.2% | -34.1% / +11.2% | PASS |  |  |
| UBOT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UBOT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 17 | 17 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UBOT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| UBOT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -34.1% negative | -34.1% negative | PASS |  |  |
| UFO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.30 / RS 1.09 | $39.30 / RS 1.09 | PASS |  |  |
| UFO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| UFO | RS2 | Stock 52W Return and S&P 52W Return | +21.5% / +11.2% | +21.5% / +11.2% | PASS |  |  |
| UFO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UFO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UFO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| UFO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +21.5% clears | +21.5% clears | PASS |  |  |
| URA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.04 / RS 0.65 | $30.04 / RS 0.65 | PASS |  |  |
| URA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.65 | PASS |  |  |
| URA | RS2 | Stock 52W Return and S&P 52W Return | -28.0% / +11.2% | -28.0% / +11.2% | PASS |  |  |
| URA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| URA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| URA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| URA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -28.0% negative | -28.0% negative | PASS |  |  |
| URAA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $11.38 / RS 0.34 | $11.38 / RS 0.34 | PASS |  |  |
| URAA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.34 | 0.34 | PASS |  |  |
| URAA | RS2 | Stock 52W Return and S&P 52W Return | -62.5% / +11.2% | -62.5% / +11.2% | PASS |  |  |
| URAA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| URAA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| URAA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| URAA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -62.5% negative | -62.5% negative | PASS |  |  |
| V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $416.77 / RS 1.16 | $416.77 / RS 1.16 | PASS |  |  |
| V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.16 | 1.16 | PASS |  |  |
| V | RS2 | Stock 52W Return and S&P 52W Return | +28.9% / +11.2% | +28.9% / +11.2% | PASS |  |  |
| V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 63 | 63 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.9% clears | +28.9% clears | PASS |  |  |
| VFV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $186.14 / RS 1.01 | $186.14 / RS 1.01 | PASS |  |  |
| VFV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.01 | PASS |  |  |
| VFV.TO | RS2 | Stock 52W Return and S&P 52W Return | +12.8% / +11.2% | +12.8% / +11.2% | PASS |  |  |
| VFV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VFV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VFV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| VFV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +12.8% clears | +12.8% clears | PASS |  |  |
| VRT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $190.37 / RS 1.03 | $190.37 / RS 1.03 | PASS |  |  |
| VRT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| VRT | RS2 | Stock 52W Return and S&P 52W Return | +14.4% / +11.2% | +14.4% / +11.2% | PASS |  |  |
| VRT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VRT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VRT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| VRT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.4% clears | +14.4% clears | PASS |  |  |
| WDC.TO | RS1 | a history of 133 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | N/A | N/A | PASS |  | by design (needs more than 200 bars); the card does not say why |
| WELL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $245.76 / RS 1.14 | $245.76 / RS 1.14 | PASS |  |  |
| WELL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.14 | 1.14 | PASS |  |  |
| WELL | RS2 | Stock 52W Return and S&P 52W Return | +26.4% / +11.2% | +26.4% / +11.2% | PASS |  |  |
| WELL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WELL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 61 | 61 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WELL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| WELL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +26.4% clears | +26.4% clears | PASS |  |  |
| WMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $127.52 / RS 1.12 | $127.52 / RS 1.12 | PASS |  |  |
| WMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.12 | 1.12 | PASS |  |  |
| WMT | RS2 | Stock 52W Return and S&P 52W Return | +24.9% / +11.2% | +24.9% / +11.2% | PASS |  |  |
| WMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| WMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +24.9% clears | +24.9% clears | PASS |  |  |
| XCHP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $105.40 / RS 1.38 | $105.40 / RS 1.38 | PASS |  |  |
| XCHP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.38 | 1.38 | PASS |  |  |
| XCHP.TO | RS2 | Stock 52W Return and S&P 52W Return | +53.7% / +11.2% | +53.7% / +11.2% | PASS |  |  |
| XCHP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XCHP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 81 | 81 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XCHP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| XCHP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +53.7% clears | +53.7% clears | PASS |  |  |
| XDRV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.25 / RS 0.85 | $39.25 / RS 0.85 | PASS |  |  |
| XDRV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| XDRV.TO | RS2 | Stock 52W Return and S&P 52W Return | -5.8% / +11.2% | -5.9% / +11.2% | PASS |  |  |
| XDRV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XDRV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XDRV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| XDRV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.8% negative | -5.9% negative | PASS |  |  |
| XEQT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $44.34 / RS 1.03 | $44.34 / RS 1.03 | PASS |  |  |
| XEQT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| XEQT.TO | RS2 | Stock 52W Return and S&P 52W Return | +14.9% / +11.2% | +14.9% / +11.2% | PASS |  |  |
| XEQT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XEQT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 53 | 53 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XEQT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| XEQT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.9% clears | +14.9% clears | PASS |  |  |
| XETM.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $61.17 / RS 0.65 | $61.17 / RS 0.65 | PASS |  |  |
| XETM.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.65 | PASS |  |  |
| XETM.TO | RS2 | Stock 52W Return and S&P 52W Return | -27.4% / +11.2% | -27.4% / +11.2% | PASS |  |  |
| XETM.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XETM.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| XETM.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -27.4% negative | -27.4% negative | PASS |  |  |
| XGD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $51.28 / RS 1.01 | $51.28 / RS 1.01 | PASS |  |  |
| XGD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.01 | PASS |  |  |
| XGD.TO | RS2 | Stock 52W Return and S&P 52W Return | +12.8% / +11.2% | +12.8% / +11.2% | PASS |  |  |
| XGD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XGD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XGD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| XGD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +12.8% clears | +12.8% clears | PASS |  |  |
| XOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $167.21 / RS 1.31 | $167.21 / RS 1.31 | PASS |  |  |
| XOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.31 | 1.31 | PASS |  |  |
| XOM | RS2 | Stock 52W Return and S&P 52W Return | +45.9% / +11.2% | +45.9% / +11.2% | PASS |  |  |
| XOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 75 | 75 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| XOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +45.9% clears | +45.9% clears | PASS |  |  |
| AAPL | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 2.5% below $360.83 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| AAPL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| AAPL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| AAPL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $344.01 – $351.46 · 0.1% below · turned here 4× | $344.01 – $351.46 · 0.1% · 4× | PASS |  |  |
| AAPL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.8729 | 7.8727 | PASS |  |  |
| AAPL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AAPL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AAPL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $351.46 | $351.46 | PASS |  |  |
| AAPL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 351.46, nearest zone high 351.46 | equal | PASS |  |  |
| AAPL | TS1c | S5: the Buy on the bar = the Buy in the box | $351.46 | $351.46 | PASS |  |  |
| AAPL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.1% below | 0.1% below | PASS |  |  |
| AAPL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $335.71 -4.5% | $335.71 -4.5% | PASS |  |  |
| AAPL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPL | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 2.5% below the high $360.83 | PASS |  |  |
| AAPL | TS6 | Risk $ (and reward $ per share) | Risk $15.75 a share | Risk $15.75 | PASS |  |  |
| AAPU | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| AAPU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| AAPU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $47.65 – $48.94 · price is inside this zone · turned here 4× | $47.65 – $48.94 · 0.0% · 4× | PASS |  |  |
| AAPU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0423 | 2.0425 | PASS |  |  |
| AAPU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| AAPU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| AAPU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $48.94 | $48.94 | PASS |  |  |
| AAPU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 48.94, nearest zone high 48.94 | equal | PASS |  |  |
| AAPU | TS1c | S5: the Buy on the bar = the Buy in the box | $48.94 | $48.94 | PASS |  |  |
| AAPU | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AAPU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $44.86 -8.3% | $44.86 -8.3% | PASS |  |  |
| AAPU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPU | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| AAPU | TS6 | Risk $ (and reward $ per share) | Risk $4.08 a share | Risk $4.08 | PASS |  |  |
| ABBV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $302.93 · 3.5% above · turned here 1× | $302.93 · 3.5% · 1× | PASS |  |  |
| ABBV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ABBV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $291.40 · 0.5% below · turned here 1× | $291.40 · 0.5% · 1× | PASS |  |  |
| ABBV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.6623 | 6.6624 | PASS |  |  |
| ABBV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ABBV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ABBV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $291.40 | $291.40 | PASS |  |  |
| ABBV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 291.4, nearest zone high 291.4 | equal | PASS |  |  |
| ABBV | TS1c | S5: the Buy on the bar = the Buy in the box | $291.40 | $291.40 | PASS |  |  |
| ABBV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.5% below | 0.5% below | PASS |  |  |
| ABBV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $278.08 -4.6% | $278.08 -4.6% | PASS |  |  |
| ABBV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ABBV | TS4 | Target = nearest resistance edge and its % from the buy | $302.93 +4.0% | $302.93 +4.0% | PASS |  |  |
| ABBV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| ABBV | TS6 | Risk $ (and reward $ per share) | Risk $13.32 to make $11.53 a share | Risk $13.32 to make $11.53 | PASS |  |  |
| AIPO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $23.12 – $24.20 · 2.2% above · turned here 4× | $23.12 – $24.20 · 2.2% · 4× | PASS |  |  |
| AIPO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AIPO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $22.08 · 2.4% below · turned here 1× | $22.08 · 2.4% · 1× | PASS |  |  |
| AIPO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.1313 | 1.1316 | PASS |  |  |
| AIPO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| AIPO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| AIPO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $22.08 | $22.08 | PASS |  |  |
| AIPO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 22.08, nearest zone high 22.08 | equal | PASS |  |  |
| AIPO | TS1c | S5: the Buy on the bar = the Buy in the box | $22.08 | $22.08 | PASS |  |  |
| AIPO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.4% below | 2.4% below | PASS |  |  |
| AIPO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $19.82 -10.2% | $19.82 -10.2% | PASS |  |  |
| AIPO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AIPO | TS4 | Target = nearest resistance edge and its % from the buy | $23.12 +4.7% | $23.12 +4.7% | PASS |  |  |
| AIPO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| AIPO | TS6 | Risk $ (and reward $ per share) | Risk $2.26 to make $1.04 a share | Risk $2.26 to make $1.04 | PASS |  |  |
| ALAB | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $214.24 · 1.2% above · turned here 1× | $214.24 · 1.2% · 1× | PASS |  |  |
| ALAB | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ALAB | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $177.61 – $192.86 · 8.9% below · turned here 7× | $177.61 – $192.86 · 8.9% · 7× | PASS |  |  |
| ALAB | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 23.6682 | 23.6677 | PASS |  |  |
| ALAB | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| ALAB | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| ALAB | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $192.86 | $192.86 | PASS |  |  |
| ALAB | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 192.86, nearest zone high 192.86 | equal | PASS |  |  |
| ALAB | TS1c | S5: the Buy on the bar = the Buy in the box | $192.86 | $192.86 | PASS |  |  |
| ALAB | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 8.9% below | 8.9% below | PASS |  |  |
| ALAB | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $145.52 -24.5% | $145.52 -24.5% | PASS |  |  |
| ALAB | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ALAB | TS4 | Target = nearest resistance edge and its % from the buy | $214.24 +11.1% | $214.24 +11.1% | PASS |  |  |
| ALAB | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| ALAB | TS6 | Risk $ (and reward $ per share) | Risk $47.34 to make $21.38 a share | Risk $47.34 to make $21.38 | PASS |  |  |
| AMD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $546.44 – $584.73 · 8.5% above · turned here 6× | $546.44 – $584.73 · 8.5% · 6× | PASS |  |  |
| AMD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $491.12 – $530.13 · price is inside this zone · turned here 6× | $491.12 – $530.13 · 0.0% · 6× | PASS |  |  |
| AMD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 40.5705 | 40.5706 | PASS |  |  |
| AMD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| AMD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| AMD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $530.13 | $530.13 | PASS |  |  |
| AMD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 530.13, nearest zone high 530.13 | equal | PASS |  |  |
| AMD | TS1c | S5: the Buy on the bar = the Buy in the box | $530.13 | $530.13 | PASS |  |  |
| AMD | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AMD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $448.99 -15.3% | $448.99 -15.3% | PASS |  |  |
| AMD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD | TS4 | Target = nearest resistance edge and its % from the buy | $546.44 +3.1% | $546.44 +3.1% | PASS |  |  |
| AMD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AMD | TS6 | Risk $ (and reward $ per share) | Risk $81.14 to make $16.31 a share | Risk $81.14 to make $16.31 | PASS |  |  |
| AMD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $13.37 – $14.18 · 3.2% above · turned here 3× | $13.37 – $14.18 · 3.2% · 3× | PASS |  |  |
| AMD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.20 – $12.97 · price is inside this zone · turned here 5× | $12.20 – $12.97 · 0.0% · 5× | PASS |  |  |
| AMD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.0253 | 1.0253 | PASS |  |  |
| AMD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AMD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AMD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $12.97 | $12.97 | PASS |  |  |
| AMD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 12.97, nearest zone high 12.97 | equal | PASS |  |  |
| AMD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $12.97 | $12.97 | PASS |  |  |
| AMD.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AMD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $10.92 -15.8% | $10.92 -15.8% | PASS |  |  |
| AMD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $13.37 +3.1% | $13.37 +3.1% | PASS |  |  |
| AMD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AMD.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.05 to make $0.40 a share | Risk $2.05 to make $0.40 | PASS |  |  |
| AMZN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $265.34 – $267.56 · 2.9% above · turned here 2× | $265.34 – $267.56 · 2.9% · 2× | PASS |  |  |
| AMZN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $255.19 – $259.49 · price is inside this zone · turned here 3× | $255.19 – $259.49 · 0.0% · 3× | PASS |  |  |
| AMZN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.9141 | 8.9142 | PASS |  |  |
| AMZN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AMZN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AMZN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $259.49 | $259.49 | PASS |  |  |
| AMZN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 259.49, nearest zone high 259.49 | equal | PASS |  |  |
| AMZN | TS1c | S5: the Buy on the bar = the Buy in the box | $259.49 | $259.49 | PASS |  |  |
| AMZN | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AMZN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $241.66 -6.9% | $241.66 -6.9% | PASS |  |  |
| AMZN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZN | TS4 | Target = nearest resistance edge and its % from the buy | $265.34 +2.3% | $265.34 +2.3% | PASS |  |  |
| AMZN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| AMZN | TS6 | Risk $ (and reward $ per share) | Risk $17.83 to make $5.85 a share | Risk $17.83 to make $5.85 | PASS |  |  |
| AMZU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.01 – $39.05 · 5.0% above · turned here 7× | $37.01 – $39.05 · 5.0% · 7× | PASS |  |  |
| AMZU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.73 – $32.89 · 6.7% below · turned here 5× | $31.73 – $32.89 · 6.7% · 5× | PASS |  |  |
| AMZU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4458 | 2.4450 | PASS |  |  |
| AMZU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AMZU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AMZU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $32.89 | $32.89 | PASS |  |  |
| AMZU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 32.89, nearest zone high 32.89 | equal | PASS |  |  |
| AMZU | TS1c | S5: the Buy on the bar = the Buy in the box | $32.89 | $32.89 | PASS |  |  |
| AMZU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.7% below | 6.7% below | PASS |  |  |
| AMZU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $28.00 -14.9% | $28.00 -14.9% | PASS |  |  |
| AMZU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZU | TS4 | Target = nearest resistance edge and its % from the buy | $37.01 +12.5% | $37.01 +12.5% | PASS |  |  |
| AMZU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| AMZU | TS6 | Risk $ (and reward $ per share) | Risk $4.89 to make $4.12 a share | Risk $4.89 to make $4.12 | PASS |  |  |
| ANET.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $34.01 – $34.05 · 2.1% above · turned here 2× | $34.01 – $34.05 · 2.1% · 2× | PASS |  |  |
| ANET.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.45 – $33.38 · price is inside this zone · turned here 8× | $31.45 – $33.38 · 0.0% · 8× | PASS |  |  |
| ANET.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9896 | 1.9896 | PASS |  |  |
| ANET.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ANET.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ANET.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $33.38 | $33.38 | PASS |  |  |
| ANET.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 33.38, nearest zone high 33.38 | equal | PASS |  |  |
| ANET.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $33.38 | $33.38 | PASS |  |  |
| ANET.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| ANET.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $29.40 -11.9% | $29.40 -11.9% | PASS |  |  |
| ANET.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ANET.TO | TS4 | Target = nearest resistance edge and its % from the buy | $34.01 +1.9% | $34.01 +1.9% | PASS |  |  |
| ANET.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| ANET.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.98 to make $0.63 a share | Risk $3.98 to make $0.63 | PASS |  |  |
| ASML.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $42.01 – $42.36 · 3.0% above · turned here 2× | $42.01 – $42.36 · 3.0% · 2× | PASS |  |  |
| ASML.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ASML.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $40.17 – $40.74 · 0.1% below · turned here 3× | $40.17 – $40.74 · 0.1% · 3× | PASS |  |  |
| ASML.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9727 | 1.9729 | PASS |  |  |
| ASML.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ASML.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $40.74 | $40.74 | PASS |  |  |
| ASML.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 40.74, nearest zone high 40.74 | equal | PASS |  |  |
| ASML.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $40.74 | $40.74 | PASS |  |  |
| ASML.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.1% below | 0.1% below | PASS |  |  |
| ASML.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $36.79 -9.7% | $36.79 -9.7% | PASS |  |  |
| ASML.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASML.TO | TS4 | Target = nearest resistance edge and its % from the buy | $42.01 +3.1% | $42.01 +3.1% | PASS |  |  |
| ASML.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ASML.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.95 to make $1.27 a share | Risk $3.95 to make $1.27 | PASS |  |  |
| ASTL.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $8.16 – $8.31 · 12.6% above · turned here 2× | $8.16 – $8.31 · 12.6% · 2× | PASS |  |  |
| ASTL.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Uptrend pulling back to support | Uptrend pulling back to support | PASS |  |  |
| ASTL.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $7.25 – $7.44 · price is inside this zone · turned here 3× | $7.25 – $7.44 · 0.0% · 3× | PASS |  |  |
| ASTL.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4265 | 0.4270 | PASS |  |  |
| ASTL.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ASTL.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ASTL.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $7.44 | $7.44 | PASS |  |  |
| ASTL.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 7.44, nearest zone high 7.44 | equal | PASS |  |  |
| ASTL.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $7.44 | $7.44 | PASS |  |  |
| ASTL.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| ASTL.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $6.59 -11.5% | $6.59 -11.5% | PASS |  |  |
| ASTL.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASTL.TO | TS4 | Target = nearest resistance edge and its % from the buy | $8.16 +9.7% | $8.16 +9.7% | PASS |  |  |
| ASTL.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| ASTL.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.85 to make $0.72 a share | Risk $0.85 to make $0.72 | PASS |  |  |
| ATD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $84.02 · 0.4% above · turned here 1× | $84.02 · 0.4% · 1× | PASS |  |  |
| ATD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ATD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $80.76 – $81.40 · 2.7% below · turned here 3× | $80.76 – $81.40 · 2.7% · 3× | PASS |  |  |
| ATD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6748 | 1.6747 | PASS |  |  |
| ATD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| ATD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| ATD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $81.40 | $81.40 | PASS |  |  |
| ATD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 81.4, nearest zone high 81.4 | equal | PASS |  |  |
| ATD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $81.40 | $81.40 | PASS |  |  |
| ATD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| ATD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $78.05 -4.1% | $78.05 -4.1% | PASS |  |  |
| ATD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ATD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $84.02 +3.2% | $84.02 +3.2% | PASS |  |  |
| ATD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| ATD.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.35 to make $2.62 a share | Risk $3.35 to make $2.62 | PASS |  |  |
| AVGC | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $19.34 – $20.42 · 6.3% above · turned here 4× | $19.34 – $20.42 · 6.3% · 4× | PASS |  |  |
| AVGC | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.52 · 9.2% below · turned here 1× | $16.52 · 9.2% · 1× | PASS |  |  |
| AVGC | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6599 | 1.6599 | PASS |  |  |
| AVGC | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| AVGC | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| AVGC | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $16.52 | $16.52 | PASS |  |  |
| AVGC | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 16.52, nearest zone high 16.52 | equal | PASS |  |  |
| AVGC | TS1c | S5: the Buy on the bar = the Buy in the box | $16.52 | $16.52 | PASS |  |  |
| AVGC | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 9.2% below | 9.2% below | PASS |  |  |
| AVGC | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $13.20 -20.1% | $13.20 -20.1% | PASS |  |  |
| AVGC | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGC | TS4 | Target = nearest resistance edge and its % from the buy | $19.34 +17.1% | $19.34 +17.1% | PASS |  |  |
| AVGC | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| AVGC | TS6 | Risk $ (and reward $ per share) | Risk $3.32 to make $2.82 a share | Risk $3.32 to make $2.82 | PASS |  |  |
| AVGO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $349.42 – $366.55 · 2.3% above · turned here 9× | $349.42 – $366.55 · 2.3% · 9× | PASS |  |  |
| AVGO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AVGO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $328.69 – $343.29 · price is inside this zone · turned here 5× | $328.69 – $343.29 · 0.0% · 5× | PASS |  |  |
| AVGO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.4829 | 17.4828 | PASS |  |  |
| AVGO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| AVGO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| AVGO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $343.29 | $343.29 | PASS |  |  |
| AVGO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 343.29, nearest zone high 343.29 | equal | PASS |  |  |
| AVGO | TS1c | S5: the Buy on the bar = the Buy in the box | $343.29 | $343.29 | PASS |  |  |
| AVGO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AVGO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $308.32 -10.2% | $308.32 -10.2% | PASS |  |  |
| AVGO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO | TS4 | Target = nearest resistance edge and its % from the buy | $349.42 +1.8% | $349.42 +1.8% | PASS |  |  |
| AVGO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AVGO | TS6 | Risk $ (and reward $ per share) | Risk $34.97 to make $6.13 a share | Risk $34.97 to make $6.13 | PASS |  |  |
| AVGO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $13.51 – $14.10 · 4.4% above · turned here 9× | $13.51 – $14.10 · 4.4% · 9× | PASS |  |  |
| AVGO.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.72 – $13.34 · price is inside this zone · turned here 7× | $12.72 – $13.34 · 0.0% · 7× | PASS |  |  |
| AVGO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6504 | 0.6503 | PASS |  |  |
| AVGO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AVGO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AVGO.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $13.34 | $13.34 | PASS |  |  |
| AVGO.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 13.34, nearest zone high 13.34 | equal | PASS |  |  |
| AVGO.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $13.34 | $13.34 | PASS |  |  |
| AVGO.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AVGO.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.04 -9.8% | $12.04 -9.8% | PASS |  |  |
| AVGO.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO.TO | TS4 | Target = nearest resistance edge and its % from the buy | $13.51 +1.3% | $13.51 +1.3% | PASS |  |  |
| AVGO.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| AVGO.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.30 to make $0.17 a share | Risk $1.30 to make $0.17 | PASS |  |  |
| BDT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $71.25 · 0.2% above · turned here 1× | $71.25 · 0.2% · 1× | PASS |  |  |
| BDT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| BDT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $66.95 – $67.00 · 5.8% below · turned here 2× | $66.95 – $67.00 · 5.8% · 2× | PASS |  |  |
| BDT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.1013 | 4.1014 | PASS |  |  |
| BDT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| BDT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| BDT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $67.00 | $67.00 | PASS |  |  |
| BDT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 67, nearest zone high 67 | equal | PASS |  |  |
| BDT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $67.00 | $67.00 | PASS |  |  |
| BDT.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.8% below | 5.8% below | PASS |  |  |
| BDT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $58.80 -12.2% | $58.80 -12.2% | PASS |  |  |
| BDT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BDT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $71.25 +6.3% | $71.25 +6.3% | PASS |  |  |
| BDT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| BDT.TO | TS6 | Risk $ (and reward $ per share) | Risk $8.20 to make $4.25 a share | Risk $8.20 to make $4.25 | PASS |  |  |
| BOTZ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.53 · 2.8% above · turned here 1× | $30.53 · 2.8% · 1× | PASS |  |  |
| BOTZ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| BOTZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| BOTZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7941 | 0.7941 | PASS |  |  |
| BOTZ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| BOTZ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| BOTZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| BRK-B | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 1.7% below $596.92 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| BRK-B | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| BRK-B | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 7 of 8 trend checks pass | No resistance within 30% above · 7 of 8 trend checks pass | PASS |  |  |
| BRK-B | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $549.96 · 6.3% below · turned here 1× | $549.96 · 6.3% · 1× | PASS |  |  |
| BRK-B | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.3286 | 9.3286 | PASS |  |  |
| BRK-B | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| BRK-B | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| BRK-B | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 549.96, nearest zone high 549.96 | equal | PASS |  |  |
| BRK-B | TS1c | S5: the Buy on the bar = the Buy in the box | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.3% below | 6.3% below | PASS |  |  |
| BRK-B | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $531.30 -3.4% | $531.30 -3.4% | PASS |  |  |
| BRK-B | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRK-B | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 1.7% below the high $596.92 | PASS |  |  |
| BRK-B | TS6 | Risk $ (and reward $ per share) | Risk $18.66 a share | Risk $18.66 | PASS |  |  |
| BRKU | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| BRKU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| BRKU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $26.69 · 11.6% below · turned here 1× | $26.69 · 11.6% · 1× | PASS |  |  |
| BRKU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.875 | 0.8749 | PASS |  |  |
| BRKU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| BRKU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| BRKU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $26.69 | $26.69 | PASS |  |  |
| BRKU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 26.69, nearest zone high 26.69 | equal | PASS |  |  |
| BRKU | TS1c | S5: the Buy on the bar = the Buy in the box | $26.69 | $26.69 | PASS |  |  |
| BRKU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 11.6% below | 11.6% below | PASS |  |  |
| BRKU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $24.94 -6.6% | $24.94 -6.6% | PASS |  |  |
| BRKU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRKU | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| BRKU | TS6 | Risk $ (and reward $ per share) | Risk $1.75 a share | Risk $1.75 | PASS |  |  |
| CAMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $101.39 · 6.8% above · turned here 1× | $101.39 · 6.8% · 1× | PASS |  |  |
| CAMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CAMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $89.13 – $91.91 · 3.2% below · turned here 2× | $89.13 – $91.91 · 3.2% · 2× | PASS |  |  |
| CAMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.1264 | 8.1267 | PASS |  |  |
| CAMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| CAMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| CAMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $91.91 | $91.91 | PASS |  |  |
| CAMT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 91.91, nearest zone high 91.91 | equal | PASS |  |  |
| CAMT | TS1c | S5: the Buy on the bar = the Buy in the box | $91.91 | $91.91 | PASS |  |  |
| CAMT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.2% below | 3.2% below | PASS |  |  |
| CAMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $75.66 -17.7% | $75.66 -17.7% | PASS |  |  |
| CAMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CAMT | TS4 | Target = nearest resistance edge and its % from the buy | $101.39 +10.3% | $101.39 +10.3% | PASS |  |  |
| CAMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| CAMT | TS6 | Risk $ (and reward $ per share) | Risk $16.25 to make $9.48 a share | Risk $16.25 to make $9.48 | PASS |  |  |
| CARS.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.90 · 5.1% above · turned here 1× | $20.90 · 5.1% · 1× | PASS |  |  |
| CARS.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CARS.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CARS.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5064 | 0.5051 | PASS |  |  |
| CARS.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CARS.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CARS.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CAT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $615.48 – $622.21 · 7.8% above · turned here 2× | $615.48 – $622.21 · 7.8% · 2× | PASS |  |  |
| CAT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CAT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $567.23 · 0.6% below · turned here 1× | $567.23 · 0.6% · 1× | PASS |  |  |
| CAT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 28.448 | 28.4477 | PASS |  |  |
| CAT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CAT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CAT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $567.23 | $567.23 | PASS |  |  |
| CAT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 567.23, nearest zone high 567.23 | equal | PASS |  |  |
| CAT | TS1c | S5: the Buy on the bar = the Buy in the box | $567.23 | $567.23 | PASS |  |  |
| CAT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.6% below | 0.6% below | PASS |  |  |
| CAT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $510.33 -10.0% | $510.33 -10.0% | PASS |  |  |
| CAT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CAT | TS4 | Target = nearest resistance edge and its % from the buy | $615.48 +8.5% | $615.48 +8.5% | PASS |  |  |
| CAT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| CAT | TS6 | Risk $ (and reward $ per share) | Risk $56.90 to make $48.25 a share | Risk $56.90 to make $48.25 | PASS |  |  |
| CCO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $92.52 · 0.4% above · turned here 1× | $92.52 · 0.4% · 1× | PASS |  |  |
| CCO.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CCO.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CCO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.0045 | 5.0049 | PASS |  |  |
| CCO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| CCO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| CCO.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CEG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $275.57 – $286.12 · 2.8% above · turned here 5× | $275.57 – $286.12 · 2.8% · 5× | PASS |  |  |
| CEG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CEG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $255.32 – $267.59 · 0.2% below · turned here 7× | $255.32 – $267.59 · 0.2% · 7× | PASS |  |  |
| CEG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 12.989 | 12.9891 | PASS |  |  |
| CEG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| CEG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| CEG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $267.59 | $267.59 | PASS |  |  |
| CEG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 267.59, nearest zone high 267.59 | equal | PASS |  |  |
| CEG | TS1c | S5: the Buy on the bar = the Buy in the box | $267.59 | $267.59 | PASS |  |  |
| CEG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.2% below | 0.2% below | PASS |  |  |
| CEG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $241.61 -9.7% | $241.61 -9.7% | PASS |  |  |
| CEG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CEG | TS4 | Target = nearest resistance edge and its % from the buy | $275.57 +3.0% | $275.57 +3.0% | PASS |  |  |
| CEG | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CEG | TS6 | Risk $ (and reward $ per share) | Risk $25.98 to make $7.98 a share | Risk $25.98 to make $7.98 | PASS |  |  |
| CGY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $84.58 – $87.00 · 0.3% above · turned here 6× | $84.58 – $87.00 · 0.3% · 6× | PASS |  |  |
| CGY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CGY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $83.01 · 1.5% below · turned here 1× | $83.01 · 1.5% · 1× | PASS |  |  |
| CGY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5803 | 2.5803 | PASS |  |  |
| CGY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CGY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CGY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $83.01 | $83.01 | PASS |  |  |
| CGY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 83.01, nearest zone high 83.01 | equal | PASS |  |  |
| CGY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $83.01 | $83.01 | PASS |  |  |
| CGY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| CGY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $77.85 -6.2% | $77.85 -6.2% | PASS |  |  |
| CGY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CGY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $84.58 +1.9% | $84.58 +1.9% | PASS |  |  |
| CGY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CGY.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.16 to make $1.57 a share | Risk $5.16 to make $1.57 | PASS |  |  |
| CNQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $68.42 – $68.45 · 0.2% above · turned here 2× | $68.42 – $68.45 · 0.2% · 2× | PASS |  |  |
| CNQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $65.78 – $67.12 · 1.7% below · turned here 6× | $65.78 – $67.12 · 1.7% · 6× | PASS |  |  |
| CNQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9336 | 1.9339 | PASS |  |  |
| CNQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| CNQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| CNQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $67.12 | $67.12 | PASS |  |  |
| CNQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 67.12, nearest zone high 67.12 | equal | PASS |  |  |
| CNQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $67.12 | $67.12 | PASS |  |  |
| CNQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.7% below | 1.7% below | PASS |  |  |
| CNQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $63.25 -5.8% | $63.25 -5.8% | PASS |  |  |
| CNQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $68.42 +1.9% | $68.42 +1.9% | PASS |  |  |
| CNQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CNQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.87 to make $1.30 a share | Risk $3.87 to make $1.30 | PASS |  |  |
| CNR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $184.26 · 2.1% above · turned here 1× | $184.26 · 2.1% · 1× | PASS |  |  |
| CNR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $178.49 · 1.1% below · turned here 1× | $178.49 · 1.1% · 1× | PASS |  |  |
| CNR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.3338 | 3.3338 | PASS |  |  |
| CNR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| CNR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| CNR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $178.49 | $178.49 | PASS |  |  |
| CNR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 178.49, nearest zone high 178.49 | equal | PASS |  |  |
| CNR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $178.49 | $178.49 | PASS |  |  |
| CNR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| CNR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $171.82 -3.7% | $171.82 -3.7% | PASS |  |  |
| CNR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $184.26 +3.2% | $184.26 +3.2% | PASS |  |  |
| CNR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| CNR.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.67 to make $5.77 a share | Risk $6.67 to make $5.77 | PASS |  |  |
| COP | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $140.69 · 0.9% above · turned here 1× | $140.69 · 0.9% · 1× | PASS |  |  |
| COP | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COP | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $133.10 – $134.99 · 3.2% below · turned here 2× | $133.10 – $134.99 · 3.2% · 2× | PASS |  |  |
| COP | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.8743 | 3.8763 | PASS |  |  |
| COP | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| COP | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| COP | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $134.99 | $134.99 | PASS |  |  |
| COP | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 134.99, nearest zone high 134.99 | equal | PASS |  |  |
| COP | TS1c | S5: the Buy on the bar = the Buy in the box | $134.99 | $134.99 | PASS |  |  |
| COP | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.2% below | 3.2% below | PASS |  |  |
| COP | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $127.24 -5.7% | $127.24 -5.7% | PASS |  |  |
| COP | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COP | TS4 | Target = nearest resistance edge and its % from the buy | $140.69 +4.2% | $140.69 +4.2% | PASS |  |  |
| COP | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| COP | TS6 | Risk $ (and reward $ per share) | Risk $7.75 to make $5.70 a share | Risk $7.75 to make $5.70 | PASS |  |  |
| COPP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $48.48 · 4.4% above · turned here 1× | $48.48 · 4.4% · 1× | PASS |  |  |
| COPP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COPP.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $46.40 · 0.0% below · turned here 1× | $46.40 · 0.0% · 1× | PASS |  |  |
| COPP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0505 | 2.0504 | PASS |  |  |
| COPP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| COPP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| COPP.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $46.40 | $46.40 | PASS |  |  |
| COPP.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 46.4, nearest zone high 46.4 | equal | PASS |  |  |
| COPP.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $46.40 | $46.40 | PASS |  |  |
| COPP.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.0% below | 0.0% below | PASS |  |  |
| COPP.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $42.30 -8.8% | $42.30 -8.8% | PASS |  |  |
| COPP.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COPP.TO | TS4 | Target = nearest resistance edge and its % from the buy | $48.48 +4.5% | $48.48 +4.5% | PASS |  |  |
| COPP.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| COPP.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.10 to make $2.08 a share | Risk $4.10 to make $2.08 | PASS |  |  |
| COPX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $68.26 · 4.5% above · turned here 1× | $68.26 · 4.5% · 1× | PASS |  |  |
| COPX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 1 of 8 trend checks pass · ADX 25.2 | 1 of 8 trend checks pass · ADX 25.2 | PASS |  |  |
| COPX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $55.44 · 15.1% below · turned here 1× | $55.44 · 15.1% · 1× | PASS |  |  |
| COPX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.7598 | 2.7598 | PASS |  |  |
| COPX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| COPX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| COPX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $55.44 | $55.44 | PASS |  |  |
| COPX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 55.44, nearest zone high 55.44 | equal | PASS |  |  |
| COPX | TS1c | S5: the Buy on the bar = the Buy in the box | $55.44 | $55.44 | PASS |  |  |
| COPX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 15.1% below | 15.1% below | PASS |  |  |
| COPX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $49.92 -10.0% | $49.92 -10.0% | PASS |  |  |
| COPX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COPX | TS4 | Target = nearest resistance edge and its % from the buy | $68.26 +23.1% | $68.26 +23.1% | PASS |  |  |
| COPX | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.3 : 1 | 2.3 : 1 | PASS |  |  |
| COPX | TS6 | Risk $ (and reward $ per share) | Risk $5.52 to make $12.82 a share | Risk $5.52 to make $12.82 | PASS |  |  |
| COPZ | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| COPZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| COPZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7979 | 0.7975 | PASS |  |  |
| COPZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| COST | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 1.2% below $1,123.67 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| COST | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| COST | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 7 of 8 trend checks pass | No resistance within 30% above · 7 of 8 trend checks pass | PASS |  |  |
| COST | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,093.14 · 1.5% below · turned here 1× | $1,093.14 · 1.5% · 1× | PASS |  |  |
| COST | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 18.7878 | 18.7872 | PASS |  |  |
| COST | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| COST | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| COST | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,093.14 | $1,093.14 | PASS |  |  |
| COST | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1093.14, nearest zone high 1093.14 | equal | PASS |  |  |
| COST | TS1c | S5: the Buy on the bar = the Buy in the box | $1,093.14 | $1,093.14 | PASS |  |  |
| COST | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| COST | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $1,055.56 -3.4% | $1,055.56 -3.4% | PASS |  |  |
| COST | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COST | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 1.2% below the high $1,123.67 | PASS |  |  |
| COST | TS6 | Risk $ (and reward $ per share) | Risk $37.58 a share | Risk $37.58 | PASS |  |  |
| COTG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $17.80 · 5.1% above · turned here 1× | $17.80 · 5.1% · 1× | PASS |  |  |
| COTG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COTG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.07 – $16.11 · 4.8% below · turned here 2× | $16.07 – $16.11 · 4.8% · 2× | PASS |  |  |
| COTG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5142 | 0.5140 | PASS |  |  |
| COTG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| COTG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| COTG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $16.11 | $16.11 | PASS |  |  |
| COTG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 16.11, nearest zone high 16.11 | equal | PASS |  |  |
| COTG | TS1c | S5: the Buy on the bar = the Buy in the box | $16.11 | $16.11 | PASS |  |  |
| COTG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.8% below | 4.8% below | PASS |  |  |
| COTG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $15.08 -6.4% | $15.08 -6.4% | PASS |  |  |
| COTG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COTG | TS4 | Target = nearest resistance edge and its % from the buy | $17.80 +10.5% | $17.80 +10.5% | PASS |  |  |
| COTG | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.6 : 1 | 1.6 : 1 | PASS |  |  |
| COTG | TS6 | Risk $ (and reward $ per share) | Risk $1.03 to make $1.69 a share | Risk $1.03 to make $1.69 | PASS |  |  |
| CSU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3,341.06 – $3,430.89 · 0.7% above · turned here 5× | $3,341.06 – $3,430.89 · 0.7% · 5× | PASS |  |  |
| CSU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CSU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $3,118.74 – $3,227.61 · 2.7% below · turned here 6× | $3,118.74 – $3,227.61 · 2.7% · 6× | PASS |  |  |
| CSU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 121.3349 | 121.3349 | PASS |  |  |
| CSU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| CSU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| CSU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $3,227.61 | $3,227.61 | PASS |  |  |
| CSU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 3227.61, nearest zone high 3227.61 | equal | PASS |  |  |
| CSU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $3,227.61 | $3,227.61 | PASS |  |  |
| CSU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| CSU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $2,984.94 -7.5% | $2,984.94 -7.5% | PASS |  |  |
| CSU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CSU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $3,341.06 +3.5% | $3,341.06 +3.5% | PASS |  |  |
| CSU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| CSU.TO | TS6 | Risk $ (and reward $ per share) | Risk $242.67 to make $113.45 a share | Risk $242.67 to make $113.45 | PASS |  |  |
| CVX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $217.78 · 0.8% above · turned here 1× | $217.78 · 0.8% · 1× | PASS |  |  |
| CVX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CVX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $208.98 – $210.92 · 2.4% below · turned here 2× | $208.98 – $210.92 · 2.4% · 2× | PASS |  |  |
| CVX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.8615 | 4.8618 | PASS |  |  |
| CVX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| CVX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| CVX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $210.92 | $210.92 | PASS |  |  |
| CVX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 210.92, nearest zone high 210.92 | equal | PASS |  |  |
| CVX | TS1c | S5: the Buy on the bar = the Buy in the box | $210.92 | $210.92 | PASS |  |  |
| CVX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.4% below | 2.4% below | PASS |  |  |
| CVX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $201.20 -4.6% | $201.20 -4.6% | PASS |  |  |
| CVX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CVX | TS4 | Target = nearest resistance edge and its % from the buy | $217.78 +3.3% | $217.78 +3.3% | PASS |  |  |
| CVX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| CVX | TS6 | Risk $ (and reward $ per share) | Risk $9.72 to make $6.86 a share | Risk $9.72 to make $6.86 | PASS |  |  |
| DRAL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| DRAL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $4.06 · 1.2% below · turned here 1× | $4.06 · 1.2% · 1× | PASS |  |  |
| DRAL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8105 | 0.8105 | PASS |  |  |
| DRAL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| DRAL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| DRAL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $4.06 | $4.06 | PASS |  |  |
| DRAL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 4.06, nearest zone high 4.06 | equal | PASS |  |  |
| DRAL | TS1c | S5: the Buy on the bar = the Buy in the box | $4.06 | $4.06 | PASS |  |  |
| DRAL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| DRAL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $2.44 -39.9% | $2.44 -39.9% | PASS |  |  |
| DRAL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRAL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| DRAL | TS6 | Risk $ (and reward $ per share) | Risk $1.62 a share | Risk $1.62 | PASS |  |  |
| DRAM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $44.40 – $46.43 · 14.1% above · turned here 3× | $44.40 – $46.43 · 14.1% · 3× | PASS |  |  |
| DRAM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $37.01 · 4.9% below · turned here 1× | $37.01 · 4.9% · 1× | PASS |  |  |
| DRAM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.1551 | 3.1551 | PASS |  |  |
| DRAM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| DRAM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| DRAM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $37.01 | $37.01 | PASS |  |  |
| DRAM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 37.01, nearest zone high 37.01 | equal | PASS |  |  |
| DRAM | TS1c | S5: the Buy on the bar = the Buy in the box | $37.01 | $37.01 | PASS |  |  |
| DRAM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.9% below | 4.9% below | PASS |  |  |
| DRAM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $30.70 -17.0% | $30.70 -17.0% | PASS |  |  |
| DRAM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRAM | TS4 | Target = nearest resistance edge and its % from the buy | $44.40 +20.0% | $44.40 +20.0% | PASS |  |  |
| DRAM | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| DRAM | TS6 | Risk $ (and reward $ per share) | Risk $6.31 to make $7.39 a share | Risk $6.31 to make $7.39 | PASS |  |  |
| DRIV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $27.77 · 2.9% above · turned here 1× | $27.77 · 2.9% · 1× | PASS |  |  |
| DRIV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| DRIV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $26.87 · 0.5% below · turned here 1× | $26.87 · 0.5% · 1× | PASS |  |  |
| DRIV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7887 | 0.7894 | PASS |  |  |
| DRIV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| DRIV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $26.87 | $26.87 | PASS |  |  |
| DRIV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 26.87, nearest zone high 26.87 | equal | PASS |  |  |
| DRIV | TS1c | S5: the Buy on the bar = the Buy in the box | $26.87 | $26.87 | PASS |  |  |
| DRIV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.5% below | 0.5% below | PASS |  |  |
| DRIV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $25.29 -5.9% | $25.29 -5.9% | PASS |  |  |
| DRIV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRIV | TS4 | Target = nearest resistance edge and its % from the buy | $27.77 +3.3% | $27.77 +3.3% | PASS |  |  |
| DRIV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| DRIV | TS6 | Risk $ (and reward $ per share) | Risk $1.58 to make $0.90 a share | Risk $1.58 to make $0.90 | PASS |  |  |
| DUK | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $130.38 – $131.87 · 0.4% above · turned here 4× | $130.38 – $131.87 · 0.4% · 4× | PASS |  |  |
| DUK | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| DUK | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $129.28 · 0.4% below · turned here 1× | $129.28 · 0.4% · 1× | PASS |  |  |
| DUK | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1475 | 2.1470 | PASS |  |  |
| DUK | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| DUK | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| DUK | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $129.28 | $129.28 | PASS |  |  |
| DUK | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 129.28, nearest zone high 129.28 | equal | PASS |  |  |
| DUK | TS1c | S5: the Buy on the bar = the Buy in the box | $129.28 | $129.28 | PASS |  |  |
| DUK | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| DUK | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $124.99 -3.3% | $124.99 -3.3% | PASS |  |  |
| DUK | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DUK | TS4 | Target = nearest resistance edge and its % from the buy | $130.38 +0.9% | $130.38 +0.9% | PASS |  |  |
| DUK | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| DUK | TS6 | Risk $ (and reward $ per share) | Risk $4.30 to make $1.10 a share | Risk $4.30 to make $1.10 | PASS |  |  |
| ELIL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| ELIL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| ELIL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.02 – $35.86 · 10.9% below · turned here 2× | $35.02 – $35.86 · 10.9% · 2× | PASS |  |  |
| ELIL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2284 | 2.2292 | PASS |  |  |
| ELIL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| ELIL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| ELIL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 35.86, nearest zone high 35.86 | equal | PASS |  |  |
| ELIL | TS1c | S5: the Buy on the bar = the Buy in the box | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 10.9% below | 10.9% below | PASS |  |  |
| ELIL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.40 -12.4% | $31.40 -12.4% | PASS |  |  |
| ELIL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ELIL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| ELIL | TS6 | Risk $ (and reward $ per share) | Risk $4.46 a share | Risk $4.46 | PASS |  |  |
| EQIX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $1,066.51 – $1,099.74 · 3.1% above · turned here 5× | $1,066.51 – $1,099.74 · 3.1% · 5× | PASS |  |  |
| EQIX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| EQIX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,027.17 – $1,053.97 · price is inside this zone · turned here 7× | $1,027.17 – $1,053.97 · 0.0% · 7× | PASS |  |  |
| EQIX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 34.068 | 34.0680 | PASS |  |  |
| EQIX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| EQIX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| EQIX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,053.97 | $1,053.97 | PASS |  |  |
| EQIX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1053.97, nearest zone high 1053.97 | equal | PASS |  |  |
| EQIX | TS1c | S5: the Buy on the bar = the Buy in the box | $1,053.97 | $1,053.97 | PASS |  |  |
| EQIX | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| EQIX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $985.83 -6.5% | $985.83 -6.5% | PASS |  |  |
| EQIX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| EQIX | TS4 | Target = nearest resistance edge and its % from the buy | $1,066.51 +1.2% | $1,066.51 +1.2% | PASS |  |  |
| EQIX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| EQIX | TS6 | Risk $ (and reward $ per share) | Risk $68.14 to make $12.54 a share | Risk $68.14 to make $12.54 | PASS |  |  |
| ETN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $355.76 – $373.79 · 5.5% above · turned here 7× | $355.76 – $373.79 · 5.5% · 7× | PASS |  |  |
| ETN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ETN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $334.42 – $350.35 · price is inside this zone · turned here 4× | $334.42 – $350.35 · 0.0% · 4× | PASS |  |  |
| ETN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 18.0454 | 18.0459 | PASS |  |  |
| ETN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ETN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ETN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $350.35 | $350.35 | PASS |  |  |
| ETN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 350.35, nearest zone high 350.35 | equal | PASS |  |  |
| ETN | TS1c | S5: the Buy on the bar = the Buy in the box | $350.35 | $350.35 | PASS |  |  |
| ETN | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| ETN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $314.26 -10.3% | $314.26 -10.3% | PASS |  |  |
| ETN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ETN | TS4 | Target = nearest resistance edge and its % from the buy | $355.76 +1.5% | $355.76 +1.5% | PASS |  |  |
| ETN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| ETN | TS6 | Risk $ (and reward $ per share) | Risk $36.09 to make $5.41 a share | Risk $36.09 to make $5.41 | PASS |  |  |
| FCX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $58.03 – $58.80 · 4.9% above · turned here 3× | $58.03 – $58.80 · 4.9% · 3× | PASS |  |  |
| FCX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| FCX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $55.12 – $57.84 · price is inside this zone · turned here 6× | $55.12 – $57.84 · 0.0% · 6× | PASS |  |  |
| FCX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8226 | 2.8222 | PASS |  |  |
| FCX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| FCX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| FCX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $57.84 | $57.84 | PASS |  |  |
| FCX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 57.84, nearest zone high 57.84 | equal | PASS |  |  |
| FCX | TS1c | S5: the Buy on the bar = the Buy in the box | $57.84 | $57.84 | PASS |  |  |
| FCX | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| FCX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $52.19 -9.8% | $52.19 -9.8% | PASS |  |  |
| FCX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FCX | TS4 | Target = nearest resistance edge and its % from the buy | $58.03 +0.3% | $58.03 +0.3% | PASS |  |  |
| FCX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.0 : 1 | 0.0 : 1 | PASS |  |  |
| FCX | TS6 | Risk $ (and reward $ per share) | Risk $5.65 to make $0.19 a share | Risk $5.65 to make $0.19 | PASS |  |  |
| FINN.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $32.88 · 3.5% above · turned here 1× | $32.88 · 3.5% · 1× | PASS |  |  |
| FINN.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| FINN.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.50 – $31.65 · 0.3% below · turned here 5× | $31.50 – $31.65 · 0.3% · 5× | PASS |  |  |
| FINN.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6884 | 0.6885 | PASS |  |  |
| FINN.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| FINN.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| FINN.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $31.65 | $31.65 | PASS |  |  |
| FINN.NE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 31.65, nearest zone high 31.65 | equal | PASS |  |  |
| FINN.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $31.65 | $31.65 | PASS |  |  |
| FINN.NE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| FINN.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $30.27 -4.4% | $30.27 -4.4% | PASS |  |  |
| FINN.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FINN.NE | TS4 | Target = nearest resistance edge and its % from the buy | $32.88 +3.9% | $32.88 +3.9% | PASS |  |  |
| FINN.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| FINN.NE | TS6 | Risk $ (and reward $ per share) | Risk $1.38 to make $1.23 a share | Risk $1.38 to make $1.23 | PASS |  |  |
| GDX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $82.46 – $83.42 · 3.6% above · turned here 5× | $82.46 – $83.42 · 3.6% · 5× | PASS |  |  |
| GDX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GDX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $77.99 – $80.18 · price is inside this zone · turned here 4× | $77.99 – $80.18 · 0.0% · 4× | PASS |  |  |
| GDX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.4036 | 3.4036 | PASS |  |  |
| GDX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| GDX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| GDX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $80.18 | $80.18 | PASS |  |  |
| GDX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 80.18, nearest zone high 80.18 | equal | PASS |  |  |
| GDX | TS1c | S5: the Buy on the bar = the Buy in the box | $80.18 | $80.18 | PASS |  |  |
| GDX | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| GDX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $73.37 -8.5% | $73.37 -8.5% | PASS |  |  |
| GDX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GDX | TS4 | Target = nearest resistance edge and its % from the buy | $82.46 +2.8% | $82.46 +2.8% | PASS |  |  |
| GDX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GDX | TS6 | Risk $ (and reward $ per share) | Risk $6.81 to make $2.28 a share | Risk $6.81 to make $2.28 | PASS |  |  |
| GDXU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $24.76 – $24.90 · 0.7% above · turned here 2× | $24.76 – $24.90 · 0.7% · 2× | PASS |  |  |
| GDXU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GDXU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $22.26 – $22.62 · 8.0% below · turned here 2× | $22.26 – $22.62 · 8.0% · 2× | PASS |  |  |
| GDXU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.3285 | 2.3285 | PASS |  |  |
| GDXU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| GDXU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| GDXU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $22.62 | $22.62 | PASS |  |  |
| GDXU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 22.62, nearest zone high 22.62 | equal | PASS |  |  |
| GDXU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $22.62 | $22.62 | PASS |  |  |
| GDXU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 8.0% below | 8.0% below | PASS |  |  |
| GDXU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $17.96 -20.6% | $17.96 -20.6% | PASS |  |  |
| GDXU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GDXU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $24.76 +9.5% | $24.76 +9.5% | PASS |  |  |
| GDXU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| GDXU.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.66 to make $2.14 a share | Risk $4.66 to make $2.14 | PASS |  |  |
| GE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $328.67 – $336.02 · 0.7% above · turned here 3× | $328.67 – $336.02 · 0.7% · 3× | PASS |  |  |
| GE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $318.26 – $321.17 · 1.6% below · turned here 2× | $318.26 – $321.17 · 1.6% · 2× | PASS |  |  |
| GE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 10.2347 | 10.2348 | PASS |  |  |
| GE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| GE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| GE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $321.17 | $321.17 | PASS |  |  |
| GE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 321.17, nearest zone high 321.17 | equal | PASS |  |  |
| GE | TS1c | S5: the Buy on the bar = the Buy in the box | $321.17 | $321.17 | PASS |  |  |
| GE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.6% below | 1.6% below | PASS |  |  |
| GE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $300.70 -6.4% | $300.70 -6.4% | PASS |  |  |
| GE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GE | TS4 | Target = nearest resistance edge and its % from the buy | $328.67 +2.3% | $328.67 +2.3% | PASS |  |  |
| GE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| GE | TS6 | Risk $ (and reward $ per share) | Risk $20.47 to make $7.50 a share | Risk $20.47 to make $7.50 | PASS |  |  |
| GEV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $844.56 – $897.16 · 8.3% above · turned here 6× | $844.56 – $897.16 · 8.3% · 6× | PASS |  |  |
| GEV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GEV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $775.68 – $806.12 · price is inside this zone · turned here 3× | $775.68 – $806.12 · 0.0% · 3× | PASS |  |  |
| GEV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 55.4387 | 55.4387 | PASS |  |  |
| GEV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GEV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| GEV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $806.12 | $806.12 | PASS |  |  |
| GEV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 806.12, nearest zone high 806.12 | equal | PASS |  |  |
| GEV | TS1c | S5: the Buy on the bar = the Buy in the box | $806.12 | $806.12 | PASS |  |  |
| GEV | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| GEV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $695.24 -13.8% | $695.24 -13.8% | PASS |  |  |
| GEV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV | TS4 | Target = nearest resistance edge and its % from the buy | $844.56 +4.8% | $844.56 +4.8% | PASS |  |  |
| GEV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GEV | TS6 | Risk $ (and reward $ per share) | Risk $110.88 to make $38.44 a share | Risk $110.88 to make $38.44 | PASS |  |  |
| GEV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $52.71 – $54.63 · 1.1% above · turned here 3× | $52.71 – $54.63 · 1.1% · 3× | PASS |  |  |
| GEV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $50.19 · 3.7% below · turned here 1× | $50.19 · 3.7% · 1× | PASS |  |  |
| GEV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.6033 | 3.6029 | PASS |  |  |
| GEV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GEV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| GEV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $50.19 | $50.19 | PASS |  |  |
| GEV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 50.19, nearest zone high 50.19 | equal | PASS |  |  |
| GEV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $50.19 | $50.19 | PASS |  |  |
| GEV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.7% below | 3.7% below | PASS |  |  |
| GEV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $42.98 -14.4% | $42.98 -14.4% | PASS |  |  |
| GEV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $52.71 +5.0% | $52.71 +5.0% | PASS |  |  |
| GEV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GEV.TO | TS6 | Risk $ (and reward $ per share) | Risk $7.21 to make $2.52 a share | Risk $7.21 to make $2.52 | PASS |  |  |
| GGLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $69.39 · 10.1% above · turned here 1× | $69.39 · 10.1% · 1× | PASS |  |  |
| GGLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GGLL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $62.13 · 1.5% below · turned here 1× | $62.13 · 1.5% · 1× | PASS |  |  |
| GGLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.0966 | 5.0967 | PASS |  |  |
| GGLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| GGLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| GGLL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $62.13 | $62.13 | PASS |  |  |
| GGLL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 62.13, nearest zone high 62.13 | equal | PASS |  |  |
| GGLL | TS1c | S5: the Buy on the bar = the Buy in the box | $62.13 | $62.13 | PASS |  |  |
| GGLL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| GGLL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $51.94 -16.4% | $51.94 -16.4% | PASS |  |  |
| GGLL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GGLL | TS4 | Target = nearest resistance edge and its % from the buy | $69.39 +11.7% | $69.39 +11.7% | PASS |  |  |
| GGLL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| GGLL | TS6 | Risk $ (and reward $ per share) | Risk $10.19 to make $7.26 a share | Risk $10.19 to make $7.26 | PASS |  |  |
| GIB-A.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $121.13 – $122.37 · 5.3% above · turned here 2× | $121.13 – $122.37 · 5.3% · 2× | PASS |  |  |
| GIB-A.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Mixed trend — between levels | Mixed trend — between levels | PASS |  |  |
| GIB-A.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.35 · 5.0% below · turned here 1× | $109.35 · 5.0% · 1× | PASS |  |  |
| GIB-A.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.7154 | 2.7154 | PASS |  |  |
| GIB-A.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| GIB-A.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| GIB-A.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.35, nearest zone high 109.35 | equal | PASS |  |  |
| GIB-A.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.0% below | 5.0% below | PASS |  |  |
| GIB-A.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $103.92 -5.0% | $103.92 -5.0% | PASS |  |  |
| GIB-A.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GIB-A.TO | TS4 | Target = nearest resistance edge and its % from the buy | $121.13 +10.8% | $121.13 +10.8% | PASS |  |  |
| GIB-A.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.2 : 1 | 2.2 : 1 | PASS |  |  |
| GIB-A.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.43 to make $11.78 a share | Risk $5.43 to make $11.78 | PASS |  |  |
| GOOGL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $293.72 – $295.67 · 4.8% above · turned here 3× | $293.72 – $295.67 · 4.8% · 3× | PASS |  |  |
| GOOGL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GOOGL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $276.92 · 1.2% below · turned here 1× | $276.92 · 1.2% · 1× | PASS |  |  |
| GOOGL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 10.1258 | 10.1258 | PASS |  |  |
| GOOGL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| GOOGL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| GOOGL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $276.92 | $276.92 | PASS |  |  |
| GOOGL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 276.92, nearest zone high 276.92 | equal | PASS |  |  |
| GOOGL | TS1c | S5: the Buy on the bar = the Buy in the box | $276.92 | $276.92 | PASS |  |  |
| GOOGL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| GOOGL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $256.67 -7.3% | $256.67 -7.3% | PASS |  |  |
| GOOGL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GOOGL | TS4 | Target = nearest resistance edge and its % from the buy | $293.72 +6.1% | $293.72 +6.1% | PASS |  |  |
| GOOGL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| GOOGL | TS6 | Risk $ (and reward $ per share) | Risk $20.25 to make $16.80 a share | Risk $20.25 to make $16.80 | PASS |  |  |
| GRID | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $160.33 – $160.63 · 3.3% above · turned here 2× | $160.33 – $160.63 · 3.3% · 2× | PASS |  |  |
| GRID | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GRID | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $154.73 – $157.05 · price is inside this zone · turned here 3× | $154.73 – $157.05 · 0.0% · 3× | PASS |  |  |
| GRID | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.2625 | 4.2625 | PASS |  |  |
| GRID | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| GRID | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| GRID | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $157.05 | $157.05 | PASS |  |  |
| GRID | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 157.05, nearest zone high 157.05 | equal | PASS |  |  |
| GRID | TS1c | S5: the Buy on the bar = the Buy in the box | $157.05 | $157.05 | PASS |  |  |
| GRID | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| GRID | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $148.53 -5.4% | $148.53 -5.4% | PASS |  |  |
| GRID | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GRID | TS4 | Target = nearest resistance edge and its % from the buy | $160.33 +2.1% | $160.33 +2.1% | PASS |  |  |
| GRID | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| GRID | TS6 | Risk $ (and reward $ per share) | Risk $8.53 to make $3.28 a share | Risk $8.53 to make $3.28 | PASS |  |  |
| HD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $348.39 – $356.24 · 2.8% above · turned here 5× | $348.39 – $356.24 · 2.8% · 5× | PASS |  |  |
| HD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $328.26 – $336.74 · 0.7% below · turned here 5× | $328.26 – $336.74 · 0.7% · 5× | PASS |  |  |
| HD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.9189 | 8.9189 | PASS |  |  |
| HD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| HD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| HD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $336.74 | $336.74 | PASS |  |  |
| HD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 336.74, nearest zone high 336.74 | equal | PASS |  |  |
| HD | TS1c | S5: the Buy on the bar = the Buy in the box | $336.74 | $336.74 | PASS |  |  |
| HD | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| HD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $318.90 -5.3% | $318.90 -5.3% | PASS |  |  |
| HD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HD | TS4 | Target = nearest resistance edge and its % from the buy | $348.39 +3.5% | $348.39 +3.5% | PASS |  |  |
| HD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| HD | TS6 | Risk $ (and reward $ per share) | Risk $17.84 to make $11.65 a share | Risk $17.84 to make $11.65 | PASS |  |  |
| HURA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $39.48 · 5.6% above · turned here 1× | $39.48 · 5.6% · 1× | PASS |  |  |
| HURA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HURA.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $36.76 · 1.7% below · turned here 1× | $36.76 · 1.7% · 1× | PASS |  |  |
| HURA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.3939 | 1.3939 | PASS |  |  |
| HURA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| HURA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| HURA.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $36.76 | $36.76 | PASS |  |  |
| HURA.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 36.76, nearest zone high 36.76 | equal | PASS |  |  |
| HURA.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $36.76 | $36.76 | PASS |  |  |
| HURA.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.7% below | 1.7% below | PASS |  |  |
| HURA.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $33.97 -7.6% | $33.97 -7.6% | PASS |  |  |
| HURA.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HURA.TO | TS4 | Target = nearest resistance edge and its % from the buy | $39.48 +7.4% | $39.48 +7.4% | PASS |  |  |
| HURA.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.0 : 1 | 1.0 : 1 | PASS |  |  |
| HURA.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.79 to make $2.72 a share | Risk $2.79 to make $2.72 | PASS |  |  |
| HXQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $113.28 · 2.4% above · turned here 1× | $113.28 · 2.4% · 1× | PASS |  |  |
| HXQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HXQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.90 · 0.7% below · turned here 1× | $109.90 · 0.7% · 1× | PASS |  |  |
| HXQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.6634 | 2.6634 | PASS |  |  |
| HXQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| HXQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| HXQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.90 | $109.90 | PASS |  |  |
| HXQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.9, nearest zone high 109.9 | equal | PASS |  |  |
| HXQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $109.90 | $109.90 | PASS |  |  |
| HXQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| HXQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $104.57 -4.8% | $104.57 -4.8% | PASS |  |  |
| HXQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HXQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $113.28 +3.1% | $113.28 +3.1% | PASS |  |  |
| HXQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| HXQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.33 to make $3.38 a share | Risk $5.33 to make $3.38 | PASS |  |  |
| JNJ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $281.07 – $282.02 · 0.9% above · turned here 2× | $281.07 – $282.02 · 0.9% · 2× | PASS |  |  |
| JNJ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JNJ | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $273.55 – $275.23 · 1.2% below · turned here 3× | $273.55 – $275.23 · 1.2% · 3× | PASS |  |  |
| JNJ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.7573 | 6.7573 | PASS |  |  |
| JNJ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| JNJ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| JNJ | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $275.23 | $275.23 | PASS |  |  |
| JNJ | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 275.23, nearest zone high 275.23 | equal | PASS |  |  |
| JNJ | TS1c | S5: the Buy on the bar = the Buy in the box | $275.23 | $275.23 | PASS |  |  |
| JNJ | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| JNJ | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $261.72 -4.9% | $261.72 -4.9% | PASS |  |  |
| JNJ | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JNJ | TS4 | Target = nearest resistance edge and its % from the buy | $281.07 +2.1% | $281.07 +2.1% | PASS |  |  |
| JNJ | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| JNJ | TS6 | Risk $ (and reward $ per share) | Risk $13.51 to make $5.84 a share | Risk $13.51 to make $5.84 | PASS |  |  |
| JPM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $330.40 – $333.00 · 0.1% above · turned here 3× | $330.40 – $333.00 · 0.1% · 3× | PASS |  |  |
| JPM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JPM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $321.68 – $324.25 · 1.7% below · turned here 4× | $321.68 – $324.25 · 1.7% · 4× | PASS |  |  |
| JPM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.4579 | 7.4578 | PASS |  |  |
| JPM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| JPM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| JPM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $324.25 | $324.25 | PASS |  |  |
| JPM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 324.25, nearest zone high 324.25 | equal | PASS |  |  |
| JPM | TS1c | S5: the Buy on the bar = the Buy in the box | $324.25 | $324.25 | PASS |  |  |
| JPM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.7% below | 1.7% below | PASS |  |  |
| JPM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $309.33 -4.6% | $309.33 -4.6% | PASS |  |  |
| JPM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JPM | TS4 | Target = nearest resistance edge and its % from the buy | $330.40 +1.9% | $330.40 +1.9% | PASS |  |  |
| JPM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| JPM | TS6 | Risk $ (and reward $ per share) | Risk $14.92 to make $6.15 a share | Risk $14.92 to make $6.15 | PASS |  |  |
| KEYS | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $293.55 – $306.85 · 3.2% above · turned here 5× | $293.55 – $306.85 · 3.2% · 5× | PASS |  |  |
| KEYS | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| KEYS | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $275.27 · 3.2% below · turned here 1× | $275.27 · 3.2% · 1× | PASS |  |  |
| KEYS | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 15.9426 | 15.9428 | PASS |  |  |
| KEYS | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| KEYS | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| KEYS | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $275.27 | $275.27 | PASS |  |  |
| KEYS | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 275.27, nearest zone high 275.27 | equal | PASS |  |  |
| KEYS | TS1c | S5: the Buy on the bar = the Buy in the box | $275.27 | $275.27 | PASS |  |  |
| KEYS | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.2% below | 3.2% below | PASS |  |  |
| KEYS | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $243.38 -11.6% | $243.38 -11.6% | PASS |  |  |
| KEYS | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| KEYS | TS4 | Target = nearest resistance edge and its % from the buy | $293.55 +6.6% | $293.55 +6.6% | PASS |  |  |
| KEYS | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| KEYS | TS6 | Risk $ (and reward $ per share) | Risk $31.89 to make $18.28 a share | Risk $31.89 to make $18.28 | PASS |  |  |
| LIN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $517.88 – $524.14 · 0.5% above · turned here 4× | $517.88 – $524.14 · 0.5% · 4× | PASS |  |  |
| LIN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| LIN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $505.12 – $505.96 · 1.8% below · turned here 3× | $505.12 – $505.96 · 1.8% · 3× | PASS |  |  |
| LIN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.0129 | 9.0133 | PASS |  |  |
| LIN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| LIN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| LIN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $505.96 | $505.96 | PASS |  |  |
| LIN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 505.96, nearest zone high 505.96 | equal | PASS |  |  |
| LIN | TS1c | S5: the Buy on the bar = the Buy in the box | $505.96 | $505.96 | PASS |  |  |
| LIN | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% below | 1.8% below | PASS |  |  |
| LIN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $487.93 -3.6% | $487.93 -3.6% | PASS |  |  |
| LIN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LIN | TS4 | Target = nearest resistance edge and its % from the buy | $517.88 +2.4% | $517.88 +2.4% | PASS |  |  |
| LIN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| LIN | TS6 | Risk $ (and reward $ per share) | Risk $18.03 to make $11.92 a share | Risk $18.03 to make $11.92 | PASS |  |  |
| LLY | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| LLY | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| LLY | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,331.60 · 5.9% below · turned here 1× | $1,331.60 · 5.9% · 1× | PASS |  |  |
| LLY | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 43.5066 | 43.5069 | PASS |  |  |
| LLY | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| LLY | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| LLY | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,331.60 | $1,331.60 | PASS |  |  |
| LLY | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1331.6, nearest zone high 1331.6 | equal | PASS |  |  |
| LLY | TS1c | S5: the Buy on the bar = the Buy in the box | $1,331.60 | $1,331.60 | PASS |  |  |
| LLY | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.9% below | 5.9% below | PASS |  |  |
| LLY | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $1,244.59 -6.5% | $1,244.59 -6.5% | PASS |  |  |
| LLY | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LLY | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| LLY | TS6 | Risk $ (and reward $ per share) | Risk $87.01 a share | Risk $87.01 | PASS |  |  |
| MDA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $39.61 – $41.67 · 1.0% above · turned here 6× | $39.61 – $41.67 · 1.0% · 6× | PASS |  |  |
| MDA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MDA.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.15 · 2.7% below · turned here 1× | $38.15 · 2.7% · 1× | PASS |  |  |
| MDA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2733 | 2.2734 | PASS |  |  |
| MDA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| MDA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| MDA.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.15 | $38.15 | PASS |  |  |
| MDA.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 38.15, nearest zone high 38.15 | equal | PASS |  |  |
| MDA.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $38.15 | $38.15 | PASS |  |  |
| MDA.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| MDA.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $33.60 -11.9% | $33.60 -11.9% | PASS |  |  |
| MDA.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MDA.TO | TS4 | Target = nearest resistance edge and its % from the buy | $39.61 +3.8% | $39.61 +3.8% | PASS |  |  |
| MDA.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MDA.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.55 to make $1.46 a share | Risk $4.55 to make $1.46 | PASS |  |  |
| META | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $623.91 – $641.90 · 0.8% above · turned here 4× | $623.91 – $641.90 · 0.8% · 4× | PASS |  |  |
| META | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| META | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $605.33 – $611.95 · 1.1% below · turned here 2× | $605.33 – $611.95 · 1.1% · 2× | PASS |  |  |
| META | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 22.0699 | 22.0700 | PASS |  |  |
| META | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| META | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| META | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $611.95 | $611.95 | PASS |  |  |
| META | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 611.95, nearest zone high 611.95 | equal | PASS |  |  |
| META | TS1c | S5: the Buy on the bar = the Buy in the box | $611.95 | $611.95 | PASS |  |  |
| META | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| META | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $567.81 -7.2% | $567.81 -7.2% | PASS |  |  |
| META | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| META | TS4 | Target = nearest resistance edge and its % from the buy | $623.91 +2.0% | $623.91 +2.0% | PASS |  |  |
| META | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| META | TS6 | Risk $ (and reward $ per share) | Risk $44.14 to make $11.96 a share | Risk $44.14 to make $11.96 | PASS |  |  |
| METU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $22.78 – $23.54 · 5.6% above · turned here 4× | $22.78 – $23.54 · 5.6% · 4× | PASS |  |  |
| METU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| METU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $20.84 · 3.4% below · turned here 1× | $20.84 · 3.4% · 1× | PASS |  |  |
| METU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6286 | 1.6290 | PASS |  |  |
| METU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| METU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| METU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $20.84 | $20.84 | PASS |  |  |
| METU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 20.84, nearest zone high 20.84 | equal | PASS |  |  |
| METU | TS1c | S5: the Buy on the bar = the Buy in the box | $20.84 | $20.84 | PASS |  |  |
| METU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.4% below | 3.4% below | PASS |  |  |
| METU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $17.58 -15.6% | $17.58 -15.6% | PASS |  |  |
| METU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| METU | TS4 | Target = nearest resistance edge and its % from the buy | $22.78 +9.3% | $22.78 +9.3% | PASS |  |  |
| METU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| METU | TS6 | Risk $ (and reward $ per share) | Risk $3.26 to make $1.94 a share | Risk $3.26 to make $1.94 | PASS |  |  |
| MRVL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $157.89 – $170.76 · 6.2% above · turned here 3× | $157.89 – $170.76 · 6.2% · 3× | PASS |  |  |
| MRVL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MRVL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $146.78 · 1.3% below · turned here 1× | $146.78 · 1.3% · 1× | PASS |  |  |
| MRVL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.3666 | 16.3668 | PASS |  |  |
| MRVL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| MRVL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| MRVL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $146.78 | $146.78 | PASS |  |  |
| MRVL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 146.78, nearest zone high 146.78 | equal | PASS |  |  |
| MRVL | TS1c | S5: the Buy on the bar = the Buy in the box | $146.78 | $146.78 | PASS |  |  |
| MRVL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.3% below | 1.3% below | PASS |  |  |
| MRVL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $114.05 -22.3% | $114.05 -22.3% | PASS |  |  |
| MRVL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MRVL | TS4 | Target = nearest resistance edge and its % from the buy | $157.89 +7.6% | $157.89 +7.6% | PASS |  |  |
| MRVL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MRVL | TS6 | Risk $ (and reward $ per share) | Risk $32.73 to make $11.11 a share | Risk $32.73 to make $11.11 | PASS |  |  |
| MSFT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $512.76 – $517.78 · 1.3% above · turned here 2× | $512.76 – $517.78 · 1.3% · 2× | PASS |  |  |
| MSFT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MSFT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $504.96 · 0.3% below · turned here 1× | $504.96 · 0.3% · 1× | PASS |  |  |
| MSFT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 15.3934 | 15.3934 | PASS |  |  |
| MSFT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| MSFT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| MSFT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $504.96 | $504.96 | PASS |  |  |
| MSFT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 504.96, nearest zone high 504.96 | equal | PASS |  |  |
| MSFT | TS1c | S5: the Buy on the bar = the Buy in the box | $504.96 | $504.96 | PASS |  |  |
| MSFT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| MSFT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $474.17 -6.1% | $474.17 -6.1% | PASS |  |  |
| MSFT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFT | TS4 | Target = nearest resistance edge and its % from the buy | $512.76 +1.5% | $512.76 +1.5% | PASS |  |  |
| MSFT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MSFT | TS6 | Risk $ (and reward $ per share) | Risk $30.79 to make $7.80 a share | Risk $30.79 to make $7.80 | PASS |  |  |
| MSFU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.64 – $38.69 · 0.8% above · turned here 4× | $37.64 – $38.69 · 0.8% · 4× | PASS |  |  |
| MSFU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MSFU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $34.44 – $36.15 · 3.2% below · turned here 4× | $34.44 – $36.15 · 3.2% · 4× | PASS |  |  |
| MSFU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.3501 | 2.3499 | PASS |  |  |
| MSFU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| MSFU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| MSFU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $36.15 | $36.15 | PASS |  |  |
| MSFU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 36.15, nearest zone high 36.15 | equal | PASS |  |  |
| MSFU | TS1c | S5: the Buy on the bar = the Buy in the box | $36.15 | $36.15 | PASS |  |  |
| MSFU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.2% below | 3.2% below | PASS |  |  |
| MSFU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.45 -13.0% | $31.45 -13.0% | PASS |  |  |
| MSFU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFU | TS4 | Target = nearest resistance edge and its % from the buy | $37.64 +4.1% | $37.64 +4.1% | PASS |  |  |
| MSFU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MSFU | TS6 | Risk $ (and reward $ per share) | Risk $4.70 to make $1.49 a share | Risk $4.70 to make $1.49 | PASS |  |  |
| MTRX.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.20 · 3.7% above · turned here 1× | $30.20 · 3.7% · 1× | PASS |  |  |
| MTRX.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $29.09 – $29.56 · price is inside this zone · turned here 4× | $29.09 – $29.56 · 0.0% · 4× | PASS |  |  |
| MTRX.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.98 | 0.9802 | PASS |  |  |
| MTRX.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| MTRX.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| MTRX.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $29.56 | $29.56 | PASS |  |  |
| MTRX.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 29.56, nearest zone high 29.56 | equal | PASS |  |  |
| MTRX.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $29.56 | $29.56 | PASS |  |  |
| MTRX.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| MTRX.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $27.60 -6.6% | $27.60 -6.6% | PASS |  |  |
| MTRX.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MTRX.TO | TS4 | Target = nearest resistance edge and its % from the buy | $30.20 +2.2% | $30.20 +2.2% | PASS |  |  |
| MTRX.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MTRX.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.96 to make $0.64 a share | Risk $1.96 to make $0.64 | PASS |  |  |
| MU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $32.56 · 4.9% above · turned here 1× | $32.56 · 4.9% · 1× | PASS |  |  |
| MU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $28.57 – $28.78 · 7.3% below · turned here 2× | $28.57 – $28.78 · 7.3% · 2× | PASS |  |  |
| MU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5559 | 2.5559 | PASS |  |  |
| MU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| MU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| MU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $28.78 | $28.78 | PASS |  |  |
| MU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 28.78, nearest zone high 28.78 | equal | PASS |  |  |
| MU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $28.78 | $28.78 | PASS |  |  |
| MU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.3% below | 7.3% below | PASS |  |  |
| MU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $23.67 -17.8% | $23.67 -17.8% | PASS |  |  |
| MU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $32.56 +13.1% | $32.56 +13.1% | PASS |  |  |
| MU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| MU.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.11 to make $3.78 a share | Risk $5.11 to make $3.78 | PASS |  |  |
| NEE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $86.80 – $86.87 · 2.8% above · turned here 2× | $86.80 – $86.87 · 2.8% · 2× | PASS |  |  |
| NEE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $84.27 – $85.68 · price is inside this zone · turned here 5× | $84.27 – $85.68 · 0.0% · 5× | PASS |  |  |
| NEE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6395 | 1.6393 | PASS |  |  |
| NEE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| NEE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| NEE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $85.68 | $85.68 | PASS |  |  |
| NEE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 85.68, nearest zone high 85.68 | equal | PASS |  |  |
| NEE | TS1c | S5: the Buy on the bar = the Buy in the box | $85.68 | $85.68 | PASS |  |  |
| NEE | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| NEE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $82.40 -3.8% | $82.40 -3.8% | PASS |  |  |
| NEE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEE | TS4 | Target = nearest resistance edge and its % from the buy | $86.80 +1.3% | $86.80 +1.3% | PASS |  |  |
| NEE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| NEE | TS6 | Risk $ (and reward $ per share) | Risk $3.28 to make $1.12 a share | Risk $3.28 to make $1.12 | PASS |  |  |
| NEM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $120.00 – $121.46 · 7.9% above · turned here 6× | $120.00 – $121.46 · 7.9% · 6× | PASS |  |  |
| NEM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.84 – $111.95 · price is inside this zone · turned here 3× | $109.84 – $111.95 · 0.0% · 3× | PASS |  |  |
| NEM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.5128 | 4.5128 | PASS |  |  |
| NEM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| NEM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| NEM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $111.95 | $111.95 | PASS |  |  |
| NEM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 111.95, nearest zone high 111.95 | equal | PASS |  |  |
| NEM | TS1c | S5: the Buy on the bar = the Buy in the box | $111.95 | $111.95 | PASS |  |  |
| NEM | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| NEM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $102.92 -8.1% | $102.92 -8.1% | PASS |  |  |
| NEM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEM | TS4 | Target = nearest resistance edge and its % from the buy | $120.00 +7.2% | $120.00 +7.2% | PASS |  |  |
| NEM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| NEM | TS6 | Risk $ (and reward $ per share) | Risk $9.03 to make $8.05 a share | Risk $9.03 to make $8.05 | PASS |  |  |
| NFLX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $61.39 · 2.9% above · turned here 1× | $61.39 · 2.9% · 1× | PASS |  |  |
| NFLX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFLX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFLX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9471 | 1.9478 | PASS |  |  |
| NFLX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| NFLX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| NFLX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NFXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $10.57 · 7.2% above · turned here 1× | $10.57 · 7.2% · 1× | PASS |  |  |
| NFXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFXL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7098 | 0.7102 | PASS |  |  |
| NFXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| NFXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| NFXL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NTR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $103.59 – $104.15 · 4.6% above · turned here 4× | $103.59 – $104.15 · 4.6% · 4× | PASS |  |  |
| NTR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NTR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $98.61 · 0.4% below · turned here 1× | $98.61 · 0.4% · 1× | PASS |  |  |
| NTR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8025 | 2.8029 | PASS |  |  |
| NTR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| NTR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| NTR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $98.61 | $98.61 | PASS |  |  |
| NTR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 98.61, nearest zone high 98.61 | equal | PASS |  |  |
| NTR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $98.61 | $98.61 | PASS |  |  |
| NTR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| NTR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $93.01 -5.7% | $93.01 -5.7% | PASS |  |  |
| NTR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NTR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $103.59 +5.1% | $103.59 +5.1% | PASS |  |  |
| NTR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| NTR.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.61 to make $4.98 a share | Risk $5.61 to make $4.98 | PASS |  |  |
| NVDA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $163.90 · 5.4% above · turned here 1× | $163.90 · 5.4% · 1× | PASS |  |  |
| NVDA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NVDA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.7101 | 9.7101 | PASS |  |  |
| NVDA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| NVDA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| NVDA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NVDL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| NVDL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Insufficient data | Insufficient data | PASS |  |  |
| NVDL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5031 | 2.5043 | PASS |  |  |
| NVDL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| ONTO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $204.07 · 2.3% above · turned here 1× | $204.07 · 2.3% · 1× | PASS |  |  |
| ONTO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ONTO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $195.19 · 2.2% below · turned here 1× | $195.19 · 2.2% · 1× | PASS |  |  |
| ONTO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.6588 | 17.6586 | PASS |  |  |
| ONTO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ONTO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ONTO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $195.19 | $195.19 | PASS |  |  |
| ONTO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 195.19, nearest zone high 195.19 | equal | PASS |  |  |
| ONTO | TS1c | S5: the Buy on the bar = the Buy in the box | $195.19 | $195.19 | PASS |  |  |
| ONTO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.2% below | 2.2% below | PASS |  |  |
| ONTO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $159.87 -18.1% | $159.87 -18.1% | PASS |  |  |
| ONTO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ONTO | TS4 | Target = nearest resistance edge and its % from the buy | $204.07 +4.5% | $204.07 +4.5% | PASS |  |  |
| ONTO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ONTO | TS6 | Risk $ (and reward $ per share) | Risk $35.32 to make $8.88 a share | Risk $35.32 to make $8.88 | PASS |  |  |
| ORBX.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $15.45 – $15.71 · 6.8% above · turned here 2× | $15.45 – $15.71 · 6.8% · 2× | PASS |  |  |
| ORBX.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $14.29 · 1.2% below · turned here 1× | $14.29 · 1.2% · 1× | PASS |  |  |
| ORBX.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6729 | 0.6729 | PASS |  |  |
| ORBX.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ORBX.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ORBX.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $14.29 | $14.29 | PASS |  |  |
| ORBX.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 14.29, nearest zone high 14.29 | equal | PASS |  |  |
| ORBX.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $14.29 | $14.29 | PASS |  |  |
| ORBX.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| ORBX.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.94 -9.4% | $12.94 -9.4% | PASS |  |  |
| ORBX.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ORBX.TO | TS4 | Target = nearest resistance edge and its % from the buy | $15.45 +8.1% | $15.45 +8.1% | PASS |  |  |
| ORBX.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| ORBX.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.35 to make $1.16 a share | Risk $1.35 to make $1.16 | PASS |  |  |
| ORCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $122.76 · 6.7% above · turned here 1× | $122.76 · 6.7% · 1× | PASS |  |  |
| ORCL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ORCL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $114.08 · 0.8% below · turned here 1× | $114.08 · 0.8% · 1× | PASS |  |  |
| ORCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.9864 | 7.9864 | PASS |  |  |
| ORCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ORCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ORCL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $114.08 | $114.08 | PASS |  |  |
| ORCL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 114.08, nearest zone high 114.08 | equal | PASS |  |  |
| ORCL | TS1c | S5: the Buy on the bar = the Buy in the box | $114.08 | $114.08 | PASS |  |  |
| ORCL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| ORCL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $98.11 -14.0% | $98.11 -14.0% | PASS |  |  |
| ORCL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ORCL | TS4 | Target = nearest resistance edge and its % from the buy | $122.76 +7.6% | $122.76 +7.6% | PASS |  |  |
| ORCL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| ORCL | TS6 | Risk $ (and reward $ per share) | Risk $15.97 to make $8.68 a share | Risk $15.97 to make $8.68 | PASS |  |  |
| PG | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 1.1% below $173.59 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| PG | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| PG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 6 of 8 trend checks pass | No resistance within 30% above · 6 of 8 trend checks pass | PASS |  |  |
| PG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $170.52 · 0.7% below · turned here 1× | $170.52 · 0.7% · 1× | PASS |  |  |
| PG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.2038 | 3.2038 | PASS |  |  |
| PG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| PG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| PG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $170.52 | $170.52 | PASS |  |  |
| PG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 170.52, nearest zone high 170.52 | equal | PASS |  |  |
| PG | TS1c | S5: the Buy on the bar = the Buy in the box | $170.52 | $170.52 | PASS |  |  |
| PG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| PG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $164.11 -3.8% | $164.11 -3.8% | PASS |  |  |
| PG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PG | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 1.1% below the high $173.59 | PASS |  |  |
| PG | TS6 | Risk $ (and reward $ per share) | Risk $6.41 a share | Risk $6.41 | PASS |  |  |
| PLD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $131.85 – $132.60 · 5.0% above · turned here 3× | $131.85 – $132.60 · 5.0% · 3× | PASS |  |  |
| PLD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 16.5 | 3 of 8 trend checks pass · ADX 16.5 | PASS |  |  |
| PLD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $122.60 – $124.69 · 0.7% below · turned here 6× | $122.60 – $124.69 · 0.7% · 6× | PASS |  |  |
| PLD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5068 | 2.5068 | PASS |  |  |
| PLD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| PLD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $127.82 | $127.82 | PASS |  |  |
| PLD | TS1c | S5: the Buy on the bar = the Buy in the box | $127.82 | $127.82 | PASS |  |  |
| PLD | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% above | 1.8% above | PASS |  |  |
| PLD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $122.81 -3.9% | $122.81 -3.9% | PASS |  |  |
| PLD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PLD | TS4 | Target = nearest resistance edge and its % from the buy | $131.85 +3.2% | $131.85 +3.2% | PASS |  |  |
| PLD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| PLD | TS6 | Risk $ (and reward $ per share) | Risk $5.01 to make $4.03 a share | Risk $5.01 to make $4.03 | PASS |  |  |
| PNG.V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3.30 · 5.8% above · turned here 1× | $3.30 · 5.8% · 1× | PASS |  |  |
| PNG.V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| PNG.V | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| PNG.V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.2304 | 0.2307 | PASS |  |  |
| PNG.V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| PNG.V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| PNG.V | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QCOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $180.62 – $189.29 · 8.4% above · turned here 5× | $180.62 – $189.29 · 8.4% · 5× | PASS |  |  |
| QCOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QCOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $163.88 – $171.19 · price is inside this zone · turned here 6× | $163.88 – $171.19 · 0.0% · 6× | PASS |  |  |
| QCOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.866 | 8.8656 | PASS |  |  |
| QCOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| QCOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| QCOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $171.19 | $171.19 | PASS |  |  |
| QCOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 171.19, nearest zone high 171.19 | equal | PASS |  |  |
| QCOM | TS1c | S5: the Buy on the bar = the Buy in the box | $171.19 | $171.19 | PASS |  |  |
| QCOM | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| QCOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $153.46 -10.4% | $153.46 -10.4% | PASS |  |  |
| QCOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QCOM | TS4 | Target = nearest resistance edge and its % from the buy | $180.62 +5.5% | $180.62 +5.5% | PASS |  |  |
| QCOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| QCOM | TS6 | Risk $ (and reward $ per share) | Risk $17.73 to make $9.43 a share | Risk $17.73 to make $9.43 | PASS |  |  |
| QPUX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3.90 · 17.5% above · turned here 1× | $3.90 · 17.5% · 1× | PASS |  |  |
| QPUX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| QPUX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| QPUX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8738 | 0.8741 | PASS |  |  |
| QPUX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| QPUX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| QPUX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QTUM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $126.93 · 3.7% above · turned here 1× | $126.93 · 3.7% · 1× | PASS |  |  |
| QTUM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QTUM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $118.34 – $120.53 · 1.5% below · turned here 4× | $118.34 – $120.53 · 1.5% · 4× | PASS |  |  |
| QTUM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.7808 | 4.7808 | PASS |  |  |
| QTUM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| QTUM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| QTUM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $120.53 | $120.53 | PASS |  |  |
| QTUM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 120.53, nearest zone high 120.53 | equal | PASS |  |  |
| QTUM | TS1c | S5: the Buy on the bar = the Buy in the box | $120.53 | $120.53 | PASS |  |  |
| QTUM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| QTUM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $110.97 -7.9% | $110.97 -7.9% | PASS |  |  |
| QTUM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QTUM | TS4 | Target = nearest resistance edge and its % from the buy | $126.93 +5.3% | $126.93 +5.3% | PASS |  |  |
| QTUM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| QTUM | TS6 | Risk $ (and reward $ per share) | Risk $9.56 to make $6.40 a share | Risk $9.56 to make $6.40 | PASS |  |  |
| RBOT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $28.00 · 3.4% above · turned here 1× | $28.00 · 3.4% · 1× | PASS |  |  |
| RBOT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| RBOT.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| RBOT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6077 | 0.6073 | PASS |  |  |
| RBOT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| RBOT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| RBOT.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| RTX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $200.85 – $205.62 · 1.4% above · turned here 6× | $200.85 – $205.62 · 1.4% · 6× | PASS |  |  |
| RTX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RTX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $191.01 – $193.53 · 2.3% below · turned here 5× | $191.01 – $193.53 · 2.3% · 5× | PASS |  |  |
| RTX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.2796 | 5.2796 | PASS |  |  |
| RTX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| RTX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| RTX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $193.53 | $193.53 | PASS |  |  |
| RTX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 193.53, nearest zone high 193.53 | equal | PASS |  |  |
| RTX | TS1c | S5: the Buy on the bar = the Buy in the box | $193.53 | $193.53 | PASS |  |  |
| RTX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.3% below | 2.3% below | PASS |  |  |
| RTX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $182.97 -5.5% | $182.97 -5.5% | PASS |  |  |
| RTX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RTX | TS4 | Target = nearest resistance edge and its % from the buy | $200.85 +3.8% | $200.85 +3.8% | PASS |  |  |
| RTX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| RTX | TS6 | Risk $ (and reward $ per share) | Risk $10.56 to make $7.32 a share | Risk $10.56 to make $7.32 | PASS |  |  |
| RY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $287.36 – $288.75 · 2.3% above · turned here 2× | $287.36 – $288.75 · 2.3% · 2× | PASS |  |  |
| RY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $279.07 · 0.7% below · turned here 1× | $279.07 · 0.7% · 1× | PASS |  |  |
| RY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.6333 | 4.6333 | PASS |  |  |
| RY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| RY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| RY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $279.07 | $279.07 | PASS |  |  |
| RY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 279.07, nearest zone high 279.07 | equal | PASS |  |  |
| RY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $279.07 | $279.07 | PASS |  |  |
| RY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| RY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $269.80 -3.3% | $269.80 -3.3% | PASS |  |  |
| RY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $287.36 +3.0% | $287.36 +3.0% | PASS |  |  |
| RY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| RY.TO | TS6 | Risk $ (and reward $ per share) | Risk $9.27 to make $8.29 a share | Risk $9.27 to make $8.29 | PASS |  |  |
| SETM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $23.68 – $23.88 · 7.1% above · turned here 2× | $23.68 – $23.88 · 7.1% · 2× | PASS |  |  |
| SETM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| SETM | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SETM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9864 | 0.9863 | PASS |  |  |
| SETM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| SETM | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SGRD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $18.27 · 1.8% above · turned here 1× | $18.27 · 1.8% · 1× | PASS |  |  |
| SGRD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $17.20 · 4.2% below · turned here 1× | $17.20 · 4.2% · 1× | PASS |  |  |
| SGRD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.3869 | 0.3870 | PASS |  |  |
| SGRD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| SGRD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| SGRD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $17.20 | $17.20 | PASS |  |  |
| SGRD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 17.2, nearest zone high 17.2 | equal | PASS |  |  |
| SGRD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $17.20 | $17.20 | PASS |  |  |
| SGRD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.2% below | 4.2% below | PASS |  |  |
| SGRD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $16.43 -4.5% | $16.43 -4.5% | PASS |  |  |
| SGRD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SGRD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $18.27 +6.2% | $18.27 +6.2% | PASS |  |  |
| SGRD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.4 : 1 | 1.4 : 1 | PASS |  |  |
| SGRD.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.77 to make $1.07 a share | Risk $0.77 to make $1.07 | PASS |  |  |
| SMH | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $503.63 · 9.5% above · turned here 1× | $503.63 · 9.5% · 1× | PASS |  |  |
| SMH | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SMH | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $445.59 · 3.2% below · turned here 1× | $445.59 · 3.2% · 1× | PASS |  |  |
| SMH | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 24.1204 | 24.1201 | PASS |  |  |
| SMH | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| SMH | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| SMH | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $445.59 | $445.59 | PASS |  |  |
| SMH | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 445.59, nearest zone high 445.59 | equal | PASS |  |  |
| SMH | TS1c | S5: the Buy on the bar = the Buy in the box | $445.59 | $445.59 | PASS |  |  |
| SMH | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.2% below | 3.2% below | PASS |  |  |
| SMH | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $397.35 -10.8% | $397.35 -10.8% | PASS |  |  |
| SMH | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SMH | TS4 | Target = nearest resistance edge and its % from the buy | $503.63 +13.0% | $503.63 +13.0% | PASS |  |  |
| SMH | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| SMH | TS6 | Risk $ (and reward $ per share) | Risk $48.24 to make $58.04 a share | Risk $48.24 to make $58.04 | PASS |  |  |
| SNDK.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $19.52 · 1.2% above · turned here 1× | $19.52 · 1.2% · 1× | PASS |  |  |
| SNDK.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SNDK.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4773 | 2.4773 | PASS |  |  |
| SNDK.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| SNDK.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| SNDK.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $94.94 – $96.74 · 1.4% above · turned here 5× | $94.94 – $96.74 · 1.4% · 5× | PASS |  |  |
| SO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $92.72 – $93.41 · 0.2% below · turned here 3× | $92.72 – $93.41 · 0.2% · 3× | PASS |  |  |
| SO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.8002 | 1.8009 | PASS |  |  |
| SO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| SO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| SO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $93.41 | $93.41 | PASS |  |  |
| SO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 93.41, nearest zone high 93.41 | equal | PASS |  |  |
| SO | TS1c | S5: the Buy on the bar = the Buy in the box | $93.41 | $93.41 | PASS |  |  |
| SO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.2% below | 0.2% below | PASS |  |  |
| SO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $89.81 -3.9% | $89.81 -3.9% | PASS |  |  |
| SO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SO | TS4 | Target = nearest resistance edge and its % from the buy | $94.94 +1.6% | $94.94 +1.6% | PASS |  |  |
| SO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| SO | TS6 | Risk $ (and reward $ per share) | Risk $3.60 to make $1.53 a share | Risk $3.60 to make $1.53 | PASS |  |  |
| SOXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $57.74 – $58.21 · 17.7% above · turned here 2× | $57.74 – $58.21 · 17.7% · 2× | PASS |  |  |
| SOXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $48.47 – $50.06 · price is inside this zone · turned here 3× | $48.47 – $50.06 · 0.0% · 3× | PASS |  |  |
| SOXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 12.2363 | 12.2364 | PASS |  |  |
| SOXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $50.06 | $50.06 | PASS |  |  |
| SOXL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 50.06, nearest zone high 50.06 | equal | PASS |  |  |
| SOXL | TS1c | S5: the Buy on the bar = the Buy in the box | $50.06 | $50.06 | PASS |  |  |
| SOXL | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| SOXL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $25.59 -48.9% | $25.59 -48.9% | PASS |  |  |
| SOXL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL | TS4 | Target = nearest resistance edge and its % from the buy | $57.74 +15.3% | $57.74 +15.3% | PASS |  |  |
| SOXL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| SOXL | TS6 | Risk $ (and reward $ per share) | Risk $24.47 to make $7.68 a share | Risk $24.47 to make $7.68 | PASS |  |  |
| SOXL.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $14.36 · 16.2% above · turned here 1× | $14.36 · 16.2% · 1× | PASS |  |  |
| SOXL.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.05 – $13.46 · price is inside this zone · turned here 3× | $12.05 – $13.46 · 0.0% · 3× | PASS |  |  |
| SOXL.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0226 | 2.0229 | PASS |  |  |
| SOXL.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $13.46 | $13.46 | PASS |  |  |
| SOXL.NE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 13.46, nearest zone high 13.46 | equal | PASS |  |  |
| SOXL.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $13.46 | $13.46 | PASS |  |  |
| SOXL.NE | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| SOXL.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $9.41 -30.1% | $9.41 -30.1% | PASS |  |  |
| SOXL.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL.NE | TS4 | Target = nearest resistance edge and its % from the buy | $14.36 +6.7% | $14.36 +6.7% | PASS |  |  |
| SOXL.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| SOXL.NE | TS6 | Risk $ (and reward $ per share) | Risk $4.05 to make $0.90 a share | Risk $4.05 to make $0.90 | PASS |  |  |
| SOXX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $154.59 – $162.96 · 9.3% above · turned here 4× | $154.59 – $162.96 · 9.3% · 4× | PASS |  |  |
| SOXX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $130.75 · 7.6% below · turned here 1× | $130.75 · 7.6% · 1× | PASS |  |  |
| SOXX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.4055 | 8.4058 | PASS |  |  |
| SOXX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| SOXX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| SOXX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $130.75 | $130.75 | PASS |  |  |
| SOXX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 130.75, nearest zone high 130.75 | equal | PASS |  |  |
| SOXX | TS1c | S5: the Buy on the bar = the Buy in the box | $130.75 | $130.75 | PASS |  |  |
| SOXX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.6% below | 7.6% below | PASS |  |  |
| SOXX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $113.94 -12.9% | $113.94 -12.9% | PASS |  |  |
| SOXX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXX | TS4 | Target = nearest resistance edge and its % from the buy | $154.59 +18.2% | $154.59 +18.2% | PASS |  |  |
| SOXX | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.4 : 1 | 1.4 : 1 | PASS |  |  |
| SOXX | TS6 | Risk $ (and reward $ per share) | Risk $16.81 to make $23.84 a share | Risk $16.81 to make $23.84 | PASS |  |  |
| SPCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $12.16 · 20.0% above · turned here 1× | $12.16 · 20.0% · 1× | PASS |  |  |
| SPCL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $8.20 · 19.1% below · turned here 1× | $8.20 · 19.1% · 1× | PASS |  |  |
| SPCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.7136 | 1.7137 | PASS |  |  |
| SPCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| SPCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| SPCL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $8.20 | $8.20 | PASS |  |  |
| SPCL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 8.2, nearest zone high 8.2 | equal | PASS |  |  |
| SPCL | TS1c | S5: the Buy on the bar = the Buy in the box | $8.20 | $8.20 | PASS |  |  |
| SPCL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 19.1% below | 19.1% below | PASS |  |  |
| SPCL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $4.77 -41.8% | $4.77 -41.8% | PASS |  |  |
| SPCL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SPCL | TS4 | Target = nearest resistance edge and its % from the buy | $12.16 +48.3% | $12.16 +48.3% | PASS |  |  |
| SPCL | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| SPCL | TS6 | Risk $ (and reward $ per share) | Risk $3.43 to make $3.96 a share | Risk $3.43 to make $3.96 | PASS |  |  |
| TSLA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $380.15 – $393.63 · 0.0% above · turned here 7× | $380.15 – $393.63 · 0.0% · 7× | PASS |  |  |
| TSLA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLA | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $364.02 – $368.60 · 3.0% below · turned here 3× | $364.02 – $368.60 · 3.0% · 3× | PASS |  |  |
| TSLA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 15.9962 | 15.9959 | PASS |  |  |
| TSLA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| TSLA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| TSLA | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $368.60 | $368.60 | PASS |  |  |
| TSLA | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 368.6, nearest zone high 368.6 | equal | PASS |  |  |
| TSLA | TS1c | S5: the Buy on the bar = the Buy in the box | $368.60 | $368.60 | PASS |  |  |
| TSLA | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.0% below | 3.0% below | PASS |  |  |
| TSLA | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $336.61 -8.7% | $336.61 -8.7% | PASS |  |  |
| TSLA | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLA | TS4 | Target = nearest resistance edge and its % from the buy | $380.15 +3.1% | $380.15 +3.1% | PASS |  |  |
| TSLA | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| TSLA | TS6 | Risk $ (and reward $ per share) | Risk $31.99 to make $11.55 a share | Risk $31.99 to make $11.55 | PASS |  |  |
| TSLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $10.71 – $11.20 · 9.2% above · turned here 5× | $10.71 – $11.20 · 9.2% · 5× | PASS |  |  |
| TSLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $9.76 – $9.90 · price is inside this zone · turned here 2× | $9.76 – $9.90 · 0.0% · 2× | PASS |  |  |
| TSLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8446 | 0.8445 | PASS |  |  |
| TSLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| TSLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| TSLL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $9.90 | $9.90 | PASS |  |  |
| TSLL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 9.9, nearest zone high 9.9 | equal | PASS |  |  |
| TSLL | TS1c | S5: the Buy on the bar = the Buy in the box | $9.90 | $9.90 | PASS |  |  |
| TSLL | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| TSLL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $8.21 -17.1% | $8.21 -17.1% | PASS |  |  |
| TSLL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLL | TS4 | Target = nearest resistance edge and its % from the buy | $10.71 +8.2% | $10.71 +8.2% | PASS |  |  |
| TSLL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| TSLL | TS6 | Risk $ (and reward $ per share) | Risk $1.69 to make $0.81 a share | Risk $1.69 to make $0.81 | PASS |  |  |
| TSM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $371.72 – $387.17 · 3.3% above · turned here 6× | $371.72 – $387.17 · 3.3% · 6× | PASS |  |  |
| TSM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $348.59 – $358.75 · 0.3% below · turned here 4× | $348.59 – $358.75 · 0.3% · 4× | PASS |  |  |
| TSM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.9164 | 17.9164 | PASS |  |  |
| TSM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| TSM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| TSM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $358.75 | $358.75 | PASS |  |  |
| TSM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 358.75, nearest zone high 358.75 | equal | PASS |  |  |
| TSM | TS1c | S5: the Buy on the bar = the Buy in the box | $358.75 | $358.75 | PASS |  |  |
| TSM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| TSM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $322.92 -10.0% | $322.92 -10.0% | PASS |  |  |
| TSM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSM | TS4 | Target = nearest resistance edge and its % from the buy | $371.72 +3.6% | $371.72 +3.6% | PASS |  |  |
| TSM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| TSM | TS6 | Risk $ (and reward $ per share) | Risk $35.83 to make $12.97 a share | Risk $35.83 to make $12.97 | PASS |  |  |
| UBOT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $16.00 · 6.4% above · turned here 1× | $16.00 · 6.4% · 1× | PASS |  |  |
| UBOT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| UBOT | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| UBOT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8384 | 0.8382 | PASS |  |  |
| UBOT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| UBOT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| UBOT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| UFO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $40.53 · 3.1% above · turned here 1× | $40.53 · 3.1% · 1× | PASS |  |  |
| UFO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| UFO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.31 – $39.36 · price is inside this zone · turned here 3× | $38.31 – $39.36 · 0.0% · 3× | PASS |  |  |
| UFO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.3679 | 1.3675 | PASS |  |  |
| UFO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| UFO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| UFO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $39.36 | $39.36 | PASS |  |  |
| UFO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 39.36, nearest zone high 39.36 | equal | PASS |  |  |
| UFO | TS1c | S5: the Buy on the bar = the Buy in the box | $39.36 | $39.36 | PASS |  |  |
| UFO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| UFO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $36.62 -7.0% | $36.62 -7.0% | PASS |  |  |
| UFO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| UFO | TS4 | Target = nearest resistance edge and its % from the buy | $40.53 +3.0% | $40.53 +3.0% | PASS |  |  |
| UFO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| UFO | TS6 | Risk $ (and reward $ per share) | Risk $2.74 to make $1.17 a share | Risk $2.74 to make $1.17 | PASS |  |  |
| URA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.40 · 1.2% above · turned here 1× | $30.40 · 1.2% · 1× | PASS |  |  |
| URA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| URA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| URA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.435 | 1.4347 | PASS |  |  |
| URA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| URA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| URA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| URAA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $11.65 · 2.4% above · turned here 1× | $11.65 · 2.4% · 1× | PASS |  |  |
| URAA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| URAA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| URAA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.1833 | 1.1837 | PASS |  |  |
| URAA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| URAA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| URAA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $441.41 · 5.9% above · turned here 1× | $441.41 · 5.9% · 1× | PASS |  |  |
| V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Uptrend pulling back to support | Uptrend pulling back to support | PASS |  |  |
| V | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $413.83 · 0.7% below · turned here 1× | $413.83 · 0.7% · 1× | PASS |  |  |
| V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.8165 | 8.8156 | PASS |  |  |
| V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| V | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $413.83 | $413.83 | PASS |  |  |
| V | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 413.83, nearest zone high 413.83 | equal | PASS |  |  |
| V | TS1c | S5: the Buy on the bar = the Buy in the box | $413.83 | $413.83 | PASS |  |  |
| V | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| V | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $396.20 -4.3% | $396.20 -4.3% | PASS |  |  |
| V | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| V | TS4 | Target = nearest resistance edge and its % from the buy | $441.41 +6.7% | $441.41 +6.7% | PASS |  |  |
| V | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.6 : 1 | 1.6 : 1 | PASS |  |  |
| V | TS6 | Risk $ (and reward $ per share) | Risk $17.63 to make $27.58 a share | Risk $17.63 to make $27.58 | PASS |  |  |
| VFV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $188.75 – $191.22 · 1.4% above · turned here 3× | $188.75 – $191.22 · 1.4% · 3× | PASS |  |  |
| VFV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VFV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $185.71 – $186.79 · price is inside this zone · turned here 4× | $185.71 – $186.79 · 0.0% · 4× | PASS |  |  |
| VFV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8808 | 2.8806 | PASS |  |  |
| VFV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| VFV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| VFV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $186.79 | $186.79 | PASS |  |  |
| VFV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 186.79, nearest zone high 186.79 | equal | PASS |  |  |
| VFV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $186.79 | $186.79 | PASS |  |  |
| VFV.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| VFV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $181.03 -3.1% | $181.03 -3.1% | PASS |  |  |
| VFV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VFV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $188.75 +1.0% | $188.75 +1.0% | PASS |  |  |
| VFV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| VFV.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.76 to make $1.96 a share | Risk $5.76 to make $1.96 | PASS |  |  |
| VRT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $200.26 · 5.2% above · turned here 1× | $200.26 · 5.2% · 1× | PASS |  |  |
| VRT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VRT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $180.68 – $189.53 · 0.4% below · turned here 4× | $180.68 – $189.53 · 0.4% · 4× | PASS |  |  |
| VRT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.8606 | 16.8603 | PASS |  |  |
| VRT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| VRT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| VRT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $189.53 | $189.53 | PASS |  |  |
| VRT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 189.53, nearest zone high 189.53 | equal | PASS |  |  |
| VRT | TS1c | S5: the Buy on the bar = the Buy in the box | $189.53 | $189.53 | PASS |  |  |
| VRT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| VRT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $155.81 -17.8% | $155.81 -17.8% | PASS |  |  |
| VRT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VRT | TS4 | Target = nearest resistance edge and its % from the buy | $200.26 +5.7% | $200.26 +5.7% | PASS |  |  |
| VRT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| VRT | TS6 | Risk $ (and reward $ per share) | Risk $33.72 to make $10.73 a share | Risk $33.72 to make $10.73 | PASS |  |  |
| WDC.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.20 · 17.9% above · turned here 1× | $20.20 · 17.9% · 1× | PASS |  |  |
| WDC.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $15.70 · 8.3% below · turned here 1× | $15.70 · 8.3% · 1× | PASS |  |  |
| WDC.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.518 | 1.5180 | PASS |  |  |
| WDC.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| WDC.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| WDC.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 15.7, nearest zone high 15.7 | equal | PASS |  |  |
| WDC.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 8.3% below | 8.3% below | PASS |  |  |
| WDC.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.66 -19.3% | $12.66 -19.3% | PASS |  |  |
| WDC.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WDC.TO | TS4 | Target = nearest resistance edge and its % from the buy | $20.20 +28.7% | $20.20 +28.7% | PASS |  |  |
| WDC.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.5 : 1 | 1.5 : 1 | PASS |  |  |
| WDC.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.04 to make $4.50 a share | Risk $3.04 to make $4.50 | PASS |  |  |
| WELL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $253.37 · 3.1% above · turned here 1× | $253.37 · 3.1% · 1× | PASS |  |  |
| WELL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WELL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $240.11 – $242.20 · 1.4% below · turned here 2× | $240.11 – $242.20 · 1.4% · 2× | PASS |  |  |
| WELL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.2528 | 5.2534 | PASS |  |  |
| WELL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| WELL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| WELL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $242.20 | $242.20 | PASS |  |  |
| WELL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 242.2, nearest zone high 242.2 | equal | PASS |  |  |
| WELL | TS1c | S5: the Buy on the bar = the Buy in the box | $242.20 | $242.20 | PASS |  |  |
| WELL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.4% below | 1.4% below | PASS |  |  |
| WELL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $231.69 -4.3% | $231.69 -4.3% | PASS |  |  |
| WELL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WELL | TS4 | Target = nearest resistance edge and its % from the buy | $253.37 +4.6% | $253.37 +4.6% | PASS |  |  |
| WELL | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.1 : 1 | 1.1 : 1 | PASS |  |  |
| WELL | TS6 | Risk $ (and reward $ per share) | Risk $10.51 to make $11.17 a share | Risk $10.51 to make $11.17 | PASS |  |  |
| WMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $127.94 – $129.13 · 0.3% above · turned here 2× | $127.94 – $129.13 · 0.3% · 2× | PASS |  |  |
| WMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $125.37 – $126.39 · 0.9% below · turned here 3× | $125.37 – $126.39 · 0.9% · 3× | PASS |  |  |
| WMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.6692 | 2.6690 | PASS |  |  |
| WMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| WMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| WMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $126.39 | $126.39 | PASS |  |  |
| WMT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 126.39, nearest zone high 126.39 | equal | PASS |  |  |
| WMT | TS1c | S5: the Buy on the bar = the Buy in the box | $126.39 | $126.39 | PASS |  |  |
| WMT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| WMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $121.05 -4.2% | $121.05 -4.2% | PASS |  |  |
| WMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WMT | TS4 | Target = nearest resistance edge and its % from the buy | $127.94 +1.2% | $127.94 +1.2% | PASS |  |  |
| WMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| WMT | TS6 | Risk $ (and reward $ per share) | Risk $5.34 to make $1.55 a share | Risk $5.34 to make $1.55 | PASS |  |  |
| XCHP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $110.04 · 4.4% above · turned here 1× | $110.04 · 4.4% · 1× | PASS |  |  |
| XCHP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XCHP.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $95.50 · 9.4% below · turned here 1× | $95.50 · 9.4% · 1× | PASS |  |  |
| XCHP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.2838 | 6.2838 | PASS |  |  |
| XCHP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| XCHP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| XCHP.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $95.50 | $95.50 | PASS |  |  |
| XCHP.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 95.5, nearest zone high 95.5 | equal | PASS |  |  |
| XCHP.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $95.50 | $95.50 | PASS |  |  |
| XCHP.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 9.4% below | 9.4% below | PASS |  |  |
| XCHP.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $82.93 -13.2% | $82.93 -13.2% | PASS |  |  |
| XCHP.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XCHP.TO | TS4 | Target = nearest resistance edge and its % from the buy | $110.04 +15.2% | $110.04 +15.2% | PASS |  |  |
| XCHP.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| XCHP.TO | TS6 | Risk $ (and reward $ per share) | Risk $12.57 to make $14.54 a share | Risk $12.57 to make $14.54 | PASS |  |  |
| XDRV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $40.34 · 2.8% above · turned here 1× | $40.34 · 2.8% · 1× | PASS |  |  |
| XDRV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XDRV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.62 – $38.88 · 0.9% below · turned here 2× | $38.62 – $38.88 · 0.9% · 2× | PASS |  |  |
| XDRV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8322 | 0.8322 | PASS |  |  |
| XDRV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| XDRV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| XDRV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.88 | $38.88 | PASS |  |  |
| XDRV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 38.88, nearest zone high 38.88 | equal | PASS |  |  |
| XDRV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $38.88 | $38.88 | PASS |  |  |
| XDRV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| XDRV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $37.22 -4.3% | $37.22 -4.3% | PASS |  |  |
| XDRV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XDRV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $40.34 +3.8% | $40.34 +3.8% | PASS |  |  |
| XDRV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| XDRV.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.66 to make $1.46 a share | Risk $1.66 to make $1.46 | PASS |  |  |
| XEQT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $44.58 – $44.64 · 0.5% above · turned here 3× | $44.58 – $44.64 · 0.5% · 3× | PASS |  |  |
| XEQT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XEQT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $43.93 – $44.41 · price is inside this zone · turned here 5× | $43.93 – $44.41 · 0.0% · 5× | PASS |  |  |
| XEQT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5768 | 0.5764 | PASS |  |  |
| XEQT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| XEQT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $44.41 | $44.41 | PASS |  |  |
| XEQT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 44.41, nearest zone high 44.41 | equal | PASS |  |  |
| XEQT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $44.41 | $44.41 | PASS |  |  |
| XEQT.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| XEQT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $43.26 -2.6% | $43.26 -2.6% | PASS |  |  |
| XEQT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XEQT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $44.58 +0.4% | $44.58 +0.4% | PASS |  |  |
| XEQT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| XEQT.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.15 to make $0.17 a share | Risk $1.15 to make $0.17 | PASS |  |  |
| XETM.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $64.70 · 5.8% above · turned here 1× | $64.70 · 5.8% · 1× | PASS |  |  |
| XETM.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| XETM.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4539 | 2.4539 | PASS |  |  |
| XETM.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| XETM.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| XETM.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| XGD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $51.53 – $52.21 · 0.5% above · turned here 3× | $51.53 – $52.21 · 0.5% · 3× | PASS |  |  |
| XGD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XGD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $49.44 – $51.12 · 0.3% below · turned here 4× | $49.44 – $51.12 · 0.3% · 4× | PASS |  |  |
| XGD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0372 | 2.0372 | PASS |  |  |
| XGD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| XGD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| XGD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $51.12 | $51.12 | PASS |  |  |
| XGD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 51.12, nearest zone high 51.12 | equal | PASS |  |  |
| XGD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $51.12 | $51.12 | PASS |  |  |
| XGD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| XGD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $47.05 -8.0% | $47.05 -8.0% | PASS |  |  |
| XGD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XGD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $51.53 +0.8% | $51.53 +0.8% | PASS |  |  |
| XGD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| XGD.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.07 to make $0.41 a share | Risk $4.07 to make $0.41 | PASS |  |  |
| XOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $167.58 – $168.58 · 0.2% above · turned here 2× | $167.58 – $168.58 · 0.2% · 2× | PASS |  |  |
| XOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $163.88 · 2.0% below · turned here 1× | $163.88 · 2.0% · 1× | PASS |  |  |
| XOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.1759 | 4.1766 | PASS |  |  |
| XOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| XOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| XOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $163.88 | $163.88 | PASS |  |  |
| XOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 163.88, nearest zone high 163.88 | equal | PASS |  |  |
| XOM | TS1c | S5: the Buy on the bar = the Buy in the box | $163.88 | $163.88 | PASS |  |  |
| XOM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| XOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $155.53 -5.1% | $155.53 -5.1% | PASS |  |  |
| XOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XOM | TS4 | Target = nearest resistance edge and its % from the buy | $167.58 +2.3% | $167.58 +2.3% | PASS |  |  |
| XOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| XOM | TS6 | Risk $ (and reward $ per share) | Risk $8.35 to make $3.70 a share | Risk $8.35 to make $3.70 | PASS |  |  |
