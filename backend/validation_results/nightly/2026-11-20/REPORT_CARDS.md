# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-20T19:53 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 4010 · WRONG 10 (CRITICAL) · MISLEADING 25 (HIGH/LOW per row) · UNVERIFIED 6 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 117 | 3 |
| card-price-data | 234 | 0 |
| card-relative-strength | 432 | 0 |
| card-trade-setup | 826 | 0 |

Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).
Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).
NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AVGC | RS1 | a history of 102 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| COPZ | RS1 | a history of 193 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| CSU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | WRONG | CRITICAL |  |
| DRAL | RS1 | a history of 105 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| DRAM | RS1 | a history of 162 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| ORBX.TO | RS1 | a history of 141 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SGRD.TO | RS1 | a history of 149 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SNDK.TO | RS1 | a history of 136 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SPCL | RS1 | a history of 159 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| WDC.TO | RS1 | a history of 136 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| AAPU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $46M | bars: $34,102,665 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ANET.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1M | bars: $1,537,718 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| AVGC | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $45,364.9 | bars: $45,586 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| BRKU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $2,687,021 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $540,855.04 | bars: $598,112 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $123,067.86 | bars: $78,923 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| DRAL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $755,269.2 | bars: $827,586 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| DRIV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $928,100.37 | bars: $991,886 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| HURA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $414,034.13 | bars: $408,277 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| MTRX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $239,557.68 | bars: $269,609 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ORBX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $85,390.26 | bars: $92,115 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| QPUX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $719,231.89 | bars: $786,281 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| RBOT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $73,200 | bars: $81,955 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SGRD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $210,091.38 | bars: $149,649 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SPCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $269,620.25 | bars: $277,197 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| UBOT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $200,030.74 | bars: $211,599 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| URA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $62.28 / $26.72 | $62.28 / $26.71 | MISLEADING | LOW | one-cent difference: the card rounds the high of the adjusted frame, the audit the 2-dp bars |
| URAA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $678,857.12 | bars: $704,674 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| WDC.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $2,695,486 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| XETM.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $158,842.08 | bars: $176,857 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ANET.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 229 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| AVGO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 229 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| GEV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 229 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| MTRX.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 210 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| XETM.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 211 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| DUK | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| SO | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| WMT | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ASML.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 8 differ: 37.75-39.31 x5 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| DRIV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 6 differ: 31.32-32.04 x4 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| GEV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 6 differ: 47.12-47.12 x1 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| AAPL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $355.11 | $355.11 | PASS |  |  |
| AAPL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.53% | -3.53% | PASS |  |  |
| AAPL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| AAPL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| AAPL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $355.11 · close 3.53% below · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| AAPL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| AAPU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.62 | $49.62 | PASS |  |  |
| AAPU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.48% | -7.48% | PASS |  |  |
| AAPU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.35 | 0.35 | PASS |  |  |
| AAPU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| AAPU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.62 · close 7.48% below · broke out Nov 11 on 0.35× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| AAPU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ABBV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $302.93 | $302.93 | PASS |  |  |
| ABBV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.52% | -5.52% | PASS |  |  |
| ABBV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ABBV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ABBV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ABBV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $302.93 · close 5.52% below · Nov 20 close | payload values | PASS |  |  |
| ABBV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AIPO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.38 | $31.38 | PASS |  |  |
| AIPO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -34.88% | -34.89% | PASS |  |  |
| AIPO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AIPO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AIPO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AIPO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.38 · close 34.88% below · Nov 20 close | payload values | PASS |  |  |
| AIPO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ALAB | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $401.74 | $401.74 | PASS |  |  |
| ALAB | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -55.11% | -55.11% | PASS |  |  |
| ALAB | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ALAB | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ALAB | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ALAB | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $401.74 · close 55.11% below · Nov 20 close | payload values | PASS |  |  |
| ALAB | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $658.52 | $658.52 | PASS |  |  |
| AMD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.55% | -35.55% | PASS |  |  |
| AMD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $658.52 · close 35.55% below · Nov 20 close | payload values | PASS |  |  |
| AMD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.97 | $16.97 | PASS |  |  |
| AMD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.59% | -35.59% | PASS |  |  |
| AMD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.97 · close 35.59% below · Nov 20 close | payload values | PASS |  |  |
| AMD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $273.23 | $273.23 | PASS |  |  |
| AMZN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.67% | -9.67% | PASS |  |  |
| AMZN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $273.23 · close 9.67% below · Nov 20 close | payload values | PASS |  |  |
| AMZN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $39.8 | $39.80 | PASS |  |  |
| AMZU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.2% | -19.20% | PASS |  |  |
| AMZU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $39.80 · close 19.20% below · Nov 20 close | payload values | PASS |  |  |
| AMZU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ANET.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.85 | $38.85 | PASS |  |  |
| ANET.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.11% | -23.11% | PASS |  |  |
| ANET.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ANET.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ANET.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ANET.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.85 · close 23.11% below · Nov 20 close | payload values | PASS |  |  |
| ANET.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASML.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $53.94 | $53.94 | PASS |  |  |
| ASML.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.79% | -27.79% | PASS |  |  |
| ASML.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ASML.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ASML.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ASML.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $53.94 · close 27.79% below · Nov 20 close | payload values | PASS |  |  |
| ASML.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $7.71 | $7.71 | PASS |  |  |
| ASTL.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.23% | -20.23% | PASS |  |  |
| ASTL.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-09 | 2026-11-09 | PASS |  |  |
| ASTL.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.67 | 2.67 | PASS |  |  |
| ASTL.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| ASTL.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $7.71 · close 20.23% below · broke out Nov 9 on 2.67× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| ASTL.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ATD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $92.89 | $92.89 | PASS |  |  |
| ATD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.02% | -12.03% | PASS |  |  |
| ATD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ATD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ATD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ATD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $92.89 · close 12.02% below · Nov 20 close | payload values | PASS |  |  |
| ATD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGC | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $27.7 | $27.70 | PASS |  |  |
| AVGC | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -48.9% | -48.92% | PASS |  |  |
| AVGC | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGC | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGC | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGC | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $27.70 · close 48.90% below · Nov 20 close | payload values | PASS |  |  |
| AVGC | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $412.5 | $412.50 | PASS |  |  |
| AVGO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.2% | -26.20% | PASS |  |  |
| AVGO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $412.50 · close 26.20% below · Nov 20 close | payload values | PASS |  |  |
| AVGO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.16 | $16.16 | PASS |  |  |
| AVGO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.65% | -28.65% | PASS |  |  |
| AVGO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.16 · close 28.65% below · Nov 20 close | payload values | PASS |  |  |
| AVGO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BDT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.64% | -19.64% | PASS |  |  |
| BDT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BDT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BDT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BDT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $86.42 · close 19.64% below · Nov 20 close | payload values | PASS |  |  |
| BDT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BOTZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.03 | $38.03 | PASS |  |  |
| BOTZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.1% | -28.11% | PASS |  |  |
| BOTZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BOTZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BOTZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BOTZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.03 · close 28.10% below · Nov 20 close | payload values | PASS |  |  |
| BOTZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $586.3 | $586.30 | PASS |  |  |
| BRK-B | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.78% | -2.78% | PASS |  |  |
| BRK-B | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| BRK-B | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.09 | 1.09 | PASS |  |  |
| BRK-B | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| BRK-B | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $586.30 · close 2.78% below · broke out Nov 11 on 1.09× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| BRK-B | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| BRKU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $30.11 | $30.11 | PASS |  |  |
| BRKU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.51% | -5.51% | PASS |  |  |
| BRKU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| BRKU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.72 | 0.72 | PASS |  |  |
| BRKU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| BRKU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $30.11 · close 5.51% below · broke out Nov 11 on 0.72× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| BRKU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRKU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CAMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $178.02 | $178.02 | PASS |  |  |
| CAMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -49.89% | -49.89% | PASS |  |  |
| CAMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $178.02 · close 49.89% below · Nov 20 close | payload values | PASS |  |  |
| CAMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CARS.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $28.41 | $28.41 | PASS |  |  |
| CARS.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.41% | -36.40% | PASS |  |  |
| CARS.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CARS.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CARS.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CARS.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $28.41 · close 36.41% below · Nov 20 close | payload values | PASS |  |  |
| CARS.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CAT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $885.81 | $885.81 | PASS |  |  |
| CAT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.35% | -42.35% | PASS |  |  |
| CAT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $885.81 · close 42.35% below · Nov 20 close | payload values | PASS |  |  |
| CAT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CCO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $154.65 | $154.65 | PASS |  |  |
| CCO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -46.26% | -46.26% | PASS |  |  |
| CCO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CCO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CCO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CCO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $154.65 · close 46.26% below · Nov 20 close | payload values | PASS |  |  |
| CCO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CEG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $309.33 | $309.33 | PASS |  |  |
| CEG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.25% | -23.25% | PASS |  |  |
| CEG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CEG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CEG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CEG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $309.33 · close 23.25% below · Nov 20 close | payload values | PASS |  |  |
| CEG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CGY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -17.24% | -17.24% | PASS |  |  |
| CGY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CGY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CGY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CGY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $95.15 · close 17.24% below · Nov 20 close | payload values | PASS |  |  |
| CGY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $78.6 | $78.60 | PASS |  |  |
| CNQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.91% | -18.91% | PASS |  |  |
| CNQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CNQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CNQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CNQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $78.60 · close 18.91% below · Nov 20 close | payload values | PASS |  |  |
| CNQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $182.06 | $182.06 | PASS |  |  |
| CNR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.67% | -3.67% | PASS |  |  |
| CNR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CNR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.18 | 1.18 | PASS |  |  |
| CNR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| CNR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $182.06 · close 3.67% below · broke out Nov 16 on 1.18× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| CNR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COP | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $153.27 | $153.27 | PASS |  |  |
| COP | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.19% | -11.19% | PASS |  |  |
| COP | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COP | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COP | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COP | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $153.27 · close 11.19% below · Nov 20 close | payload values | PASS |  |  |
| COP | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $69.02 | $69.02 | PASS |  |  |
| COPP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.78% | -42.78% | PASS |  |  |
| COPP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $69.02 · close 42.78% below · Nov 20 close | payload values | PASS |  |  |
| COPP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $97.59 | $97.59 | PASS |  |  |
| COPX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.28% | -42.28% | PASS |  |  |
| COPX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $97.59 · close 42.28% below · Nov 20 close | payload values | PASS |  |  |
| COPX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.84 | $20.84 | PASS |  |  |
| COPZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -69.62% | -69.63% | PASS |  |  |
| COPZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.84 · close 69.62% below · Nov 20 close | payload values | PASS |  |  |
| COPZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1081.55 | $1,081.55 | PASS |  |  |
| COST | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 1.9% | 1.90% | PASS |  |  |
| COST | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| COST | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.98 | 0.98 | PASS |  |  |
| COST | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_LIGHT_VOLUME | BREAKOUT_LIGHT_VOLUME | PASS |  |  |
| COST | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,081.55 · close 1.90% above · broke out Nov 11 on 0.98× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| COST | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COTG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.12 | $16.12 | PASS |  |  |
| COTG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 3.56% | 3.54% | PASS |  |  |
| COTG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| COTG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.4 | 0.4 | PASS |  |  |
| COTG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_LIGHT_VOLUME | BREAKOUT_LIGHT_VOLUME | PASS |  |  |
| COTG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.12 · close 3.56% above · broke out Nov 11 on 0.40× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| COTG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COTG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CSU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $3532.73 | $3,532.73 | PASS |  |  |
| CSU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.36% | -12.36% | PASS |  |  |
| CSU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CSU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CSU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CSU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $3,532.73 · close 12.36% below · Nov 20 close | payload values | PASS |  |  |
| CSU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CVX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $234.53 | $234.53 | PASS |  |  |
| CVX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.16% | -11.15% | PASS |  |  |
| CVX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CVX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CVX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CVX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $234.53 · close 11.16% below · Nov 20 close | payload values | PASS |  |  |
| CVX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $13 | $13.00 | PASS |  |  |
| DRAL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -76.85% | -76.85% | PASS |  |  |
| DRAL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $13.00 · close 76.85% below · Nov 20 close | payload values | PASS |  |  |
| DRAL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $63.82 | $63.82 | PASS |  |  |
| DRAM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -47.73% | -47.73% | PASS |  |  |
| DRAM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $63.82 · close 47.73% below · Nov 20 close | payload values | PASS |  |  |
| DRAM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRIV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.47 | $36.47 | PASS |  |  |
| DRIV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.57% | -32.57% | PASS |  |  |
| DRIV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRIV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRIV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRIV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.47 · close 32.57% below · Nov 20 close | payload values | PASS |  |  |
| DRIV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $131.87 | $131.87 | PASS |  |  |
| DUK | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.58% | -1.58% | PASS |  |  |
| DUK | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DUK | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DUK | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| DUK | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $131.87 · close 1.58% below · Nov 20 close | payload values | PASS |  |  |
| DUK | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ELIL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $42.5 | $42.50 | PASS |  |  |
| ELIL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.33% | -14.33% | PASS |  |  |
| ELIL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ELIL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ELIL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ELIL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $42.50 · close 14.33% below · Nov 20 close | payload values | PASS |  |  |
| ELIL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| EQIX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1098.02 | $1,098.02 | PASS |  |  |
| EQIX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.8% | -11.80% | PASS |  |  |
| EQIX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| EQIX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| EQIX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| EQIX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,098.02 · close 11.80% below · Nov 20 close | payload values | PASS |  |  |
| EQIX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ETN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $458.96 | $458.96 | PASS |  |  |
| ETN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.17% | -32.17% | PASS |  |  |
| ETN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ETN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ETN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ETN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $458.96 · close 32.17% below · Nov 20 close | payload values | PASS |  |  |
| ETN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FCX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $80.07 | $80.07 | PASS |  |  |
| FCX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.56% | -42.56% | PASS |  |  |
| FCX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FCX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FCX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FCX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $80.07 · close 42.56% below · Nov 20 close | payload values | PASS |  |  |
| FCX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FINN.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.83 | $35.83 | PASS |  |  |
| FINN.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -15.21% | -15.21% | PASS |  |  |
| FINN.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FINN.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FINN.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FINN.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.83 · close 15.21% below · Nov 20 close | payload values | PASS |  |  |
| FINN.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $105.67 | $105.67 | PASS |  |  |
| GDX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.27% | -35.27% | PASS |  |  |
| GDX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $105.67 · close 35.27% below · Nov 20 close | payload values | PASS |  |  |
| GDX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDXU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.45 | $46.45 | PASS |  |  |
| GDXU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -60.82% | -60.82% | PASS |  |  |
| GDXU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDXU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDXU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDXU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.45 · close 60.82% below · Nov 20 close | payload values | PASS |  |  |
| GDXU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $375.58 | $375.58 | PASS |  |  |
| GE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -17.56% | -17.56% | PASS |  |  |
| GE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $375.58 · close 17.56% below · Nov 20 close | payload values | PASS |  |  |
| GE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1099.66 | $1,099.66 | PASS |  |  |
| GEV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.4% | -36.40% | PASS |  |  |
| GEV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,099.66 · close 36.40% below · Nov 20 close | payload values | PASS |  |  |
| GEV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $73.78 | $73.78 | PASS |  |  |
| GEV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37% | -37.00% | PASS |  |  |
| GEV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $73.78 · close 37.00% below · Nov 20 close | payload values | PASS |  |  |
| GEV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GGLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $111.95 | $111.95 | PASS |  |  |
| GGLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -49.45% | -49.45% | PASS |  |  |
| GGLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GGLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GGLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GGLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $111.95 · close 49.45% below · Nov 20 close | payload values | PASS |  |  |
| GGLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $117.75 | $117.75 | PASS |  |  |
| GIB-A.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.39% | -3.39% | PASS |  |  |
| GIB-A.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GIB-A.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GIB-A.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GIB-A.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $117.75 · close 3.39% below · Nov 20 close | payload values | PASS |  |  |
| GIB-A.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GOOGL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.17 | $364.17 | PASS |  |  |
| GOOGL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.15% | -27.15% | PASS |  |  |
| GOOGL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GOOGL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GOOGL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GOOGL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.17 · close 27.15% below · Nov 20 close | payload values | PASS |  |  |
| GOOGL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GRID | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $189.46 | $189.46 | PASS |  |  |
| GRID | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.23% | -23.23% | PASS |  |  |
| GRID | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GRID | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GRID | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GRID | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $189.46 · close 23.23% below · Nov 20 close | payload values | PASS |  |  |
| GRID | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $362.44 | $362.44 | PASS |  |  |
| HD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -6.44% | -6.44% | PASS |  |  |
| HD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $362.44 · close 6.44% below · Nov 20 close | payload values | PASS |  |  |
| HD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HURA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $56.75 | $56.75 | PASS |  |  |
| HURA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -40.28% | -40.28% | PASS |  |  |
| HURA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HURA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HURA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HURA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $56.75 · close 40.28% below · Nov 20 close | payload values | PASS |  |  |
| HURA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HXQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.45% | -19.45% | PASS |  |  |
| HXQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HXQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HXQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HXQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $128.37 · close 19.45% below · Nov 20 close | payload values | PASS |  |  |
| HXQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $282.02 | $282.02 | PASS |  |  |
| JNJ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.1% | -4.10% | PASS |  |  |
| JNJ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-09 | 2026-11-09 | PASS |  |  |
| JNJ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.96 | 0.96 | PASS |  |  |
| JNJ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| JNJ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $282.02 · close 4.10% below · broke out Nov 9 on 0.96× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| JNJ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| JPM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.08 | $364.08 | PASS |  |  |
| JPM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.71% | -14.71% | PASS |  |  |
| JPM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| JPM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| JPM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| JPM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.08 · close 14.71% below · Nov 20 close | payload values | PASS |  |  |
| JPM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| KEYS | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $389.93 | $389.93 | PASS |  |  |
| KEYS | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.93% | -32.93% | PASS |  |  |
| KEYS | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| KEYS | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| KEYS | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| KEYS | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $389.93 · close 32.93% below · Nov 20 close | payload values | PASS |  |  |
| KEYS | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LIN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $533.39 | $533.39 | PASS |  |  |
| LIN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.73% | -5.73% | PASS |  |  |
| LIN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| LIN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| LIN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| LIN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $533.39 · close 5.73% below · Nov 20 close | payload values | PASS |  |  |
| LIN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LLY | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1451.24 | $1,451.24 | PASS |  |  |
| LLY | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.18% | -7.18% | PASS |  |  |
| LLY | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| LLY | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| LLY | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| LLY | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,451.24 · close 7.18% below · Nov 20 close | payload values | PASS |  |  |
| LLY | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MDA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $51.34 | $51.34 | PASS |  |  |
| MDA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.17% | -28.17% | PASS |  |  |
| MDA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MDA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MDA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MDA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $51.34 · close 28.17% below · Nov 20 close | payload values | PASS |  |  |
| MDA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| META | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $779.82 | $779.82 | PASS |  |  |
| META | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.08% | -28.08% | PASS |  |  |
| META | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| META | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| META | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| META | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $779.82 · close 28.08% below · Nov 20 close | payload values | PASS |  |  |
| META | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| METU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.6 | $35.60 | PASS |  |  |
| METU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -50.53% | -50.53% | PASS |  |  |
| METU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| METU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| METU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| METU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.60 · close 50.53% below · Nov 20 close | payload values | PASS |  |  |
| METU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MRVL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $301.2 | $301.20 | PASS |  |  |
| MRVL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -59.4% | -59.40% | PASS |  |  |
| MRVL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MRVL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MRVL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MRVL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $301.20 · close 59.40% below · Nov 20 close | payload values | PASS |  |  |
| MRVL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $558.07 | $558.07 | PASS |  |  |
| MSFT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.18% | -13.18% | PASS |  |  |
| MSFT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MSFT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MSFT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MSFT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $558.07 · close 13.18% below · Nov 20 close | payload values | PASS |  |  |
| MSFT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $45.88 | $45.88 | PASS |  |  |
| MSFU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.39% | -25.39% | PASS |  |  |
| MSFU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MSFU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MSFU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MSFU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $45.88 · close 25.39% below · Nov 20 close | payload values | PASS |  |  |
| MSFU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MTRX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $37.54 | $37.54 | PASS |  |  |
| MTRX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -24.96% | -24.96% | PASS |  |  |
| MTRX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MTRX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MTRX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MTRX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $37.54 · close 24.96% below · Nov 19 close | payload values | PASS |  |  |
| MTRX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $48.54 | $48.54 | PASS |  |  |
| MU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -46.5% | -46.50% | PASS |  |  |
| MU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $48.54 · close 46.50% below · Nov 20 close | payload values | PASS |  |  |
| MU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $90.04 | $90.04 | PASS |  |  |
| NEE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.32% | -7.32% | PASS |  |  |
| NEE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NEE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NEE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NEE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $90.04 · close 7.32% below · Nov 20 close | payload values | PASS |  |  |
| NEE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $135.01 | $135.01 | PASS |  |  |
| NEM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.87% | -29.87% | PASS |  |  |
| NEM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NEM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NEM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NEM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $135.01 · close 29.87% below · Nov 20 close | payload values | PASS |  |  |
| NEM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFLX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $83.6 | $83.60 | PASS |  |  |
| NFLX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.14% | -32.14% | PASS |  |  |
| NFLX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFLX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFLX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFLX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $83.60 · close 32.14% below · Nov 20 close | payload values | PASS |  |  |
| NFLX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.33 | $20.33 | PASS |  |  |
| NFXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -56.23% | -56.22% | PASS |  |  |
| NFXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.33 · close 56.23% below · Nov 20 close | payload values | PASS |  |  |
| NFXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NTR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $112.9 | $112.90 | PASS |  |  |
| NTR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.77% | -18.77% | PASS |  |  |
| NTR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NTR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NTR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NTR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $112.90 · close 18.77% below · Nov 20 close | payload values | PASS |  |  |
| NTR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.37 | $243.37 | PASS |  |  |
| NVDA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -48.42% | -48.42% | PASS |  |  |
| NVDA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.37 · close 48.42% below · Nov 20 close | payload values | PASS |  |  |
| NVDA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $41.59 | $41.59 | PASS |  |  |
| NVDL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -75.16% | -75.16% | PASS |  |  |
| NVDL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $41.59 · close 75.16% below · Nov 20 close | payload values | PASS |  |  |
| NVDL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ONTO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $353.84 | $353.84 | PASS |  |  |
| ONTO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -51.91% | -51.91% | PASS |  |  |
| ONTO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ONTO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ONTO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ONTO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $353.84 · close 51.91% below · Nov 20 close | payload values | PASS |  |  |
| ONTO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORBX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $19.64 | $19.64 | PASS |  |  |
| ORBX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.73% | -26.73% | PASS |  |  |
| ORBX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORBX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORBX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORBX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $19.64 · close 26.73% below · Nov 18 close | payload values | PASS |  |  |
| ORBX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $170.07 | $170.07 | PASS |  |  |
| ORCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -40.5% | -40.50% | PASS |  |  |
| ORCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $170.07 · close 40.50% below · Nov 20 close | payload values | PASS |  |  |
| ORCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $170.52 | $170.52 | PASS |  |  |
| PG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.62% | -0.62% | PASS |  |  |
| PG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-16 | 2026-11-16 | PASS |  |  |
| PG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.62 | 1.62 | PASS |  |  |
| PG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| PG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $170.52 · close 0.62% below · broke out Nov 16 on 1.62× its prior 50-day average volume · Nov 20 close | payload values | PASS |  |  |
| PG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| PLD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $142.69 | $142.69 | PASS |  |  |
| PLD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.15% | -14.15% | PASS |  |  |
| PLD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PLD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PLD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PLD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $142.69 · close 14.15% below · Nov 20 close | payload values | PASS |  |  |
| PLD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PNG.V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $6.8 | $6.80 | PASS |  |  |
| PNG.V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -58.97% | -58.97% | PASS |  |  |
| PNG.V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PNG.V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PNG.V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PNG.V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $6.80 · close 58.97% below · Nov 20 close | payload values | PASS |  |  |
| PNG.V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QCOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $205.85 | $205.85 | PASS |  |  |
| QCOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.16% | -27.16% | PASS |  |  |
| QCOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QCOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QCOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QCOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $205.85 · close 27.16% below · Nov 20 close | payload values | PASS |  |  |
| QCOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QPUX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $21.48 | $21.48 | PASS |  |  |
| QPUX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -88.5% | -88.50% | PASS |  |  |
| QPUX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QPUX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QPUX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QPUX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $21.48 · close 88.50% below · Nov 20 close | payload values | PASS |  |  |
| QPUX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QTUM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $159.07 | $159.07 | PASS |  |  |
| QTUM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.95% | -29.95% | PASS |  |  |
| QTUM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QTUM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QTUM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QTUM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $159.07 · close 29.95% below · Nov 20 close | payload values | PASS |  |  |
| QTUM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RBOT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $34.84 | $34.84 | PASS |  |  |
| RBOT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.24% | -28.24% | PASS |  |  |
| RBOT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RBOT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RBOT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RBOT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $34.84 · close 28.24% below · Nov 20 close | payload values | PASS |  |  |
| RBOT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RTX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $226.41 | $226.41 | PASS |  |  |
| RTX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -16.01% | -16.01% | PASS |  |  |
| RTX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RTX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RTX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RTX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $226.41 · close 16.01% below · Nov 20 close | payload values | PASS |  |  |
| RTX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.46 | $300.46 | PASS |  |  |
| RY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.45% | -12.45% | PASS |  |  |
| RY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.46 · close 12.45% below · Nov 20 close | payload values | PASS |  |  |
| RY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SETM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.24 | $36.24 | PASS |  |  |
| SETM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -46.11% | -46.11% | PASS |  |  |
| SETM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SETM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SETM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SETM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.24 · close 46.11% below · Nov 20 close | payload values | PASS |  |  |
| SETM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SGRD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $21.22 | $21.22 | PASS |  |  |
| SGRD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.77% | -20.78% | PASS |  |  |
| SGRD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SGRD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SGRD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SGRD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $21.22 · close 20.77% below · Nov 20 close | payload values | PASS |  |  |
| SGRD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SMH | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $639.47 | $639.47 | PASS |  |  |
| SMH | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.52% | -37.52% | PASS |  |  |
| SMH | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SMH | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SMH | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SMH | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $639.47 · close 37.52% below · Nov 20 close | payload values | PASS |  |  |
| SMH | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SNDK.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.35 | $46.35 | PASS |  |  |
| SNDK.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -67.06% | -67.06% | PASS |  |  |
| SNDK.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SNDK.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SNDK.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SNDK.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.35 · close 67.06% below · Nov 20 close | payload values | PASS |  |  |
| SNDK.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $94.94 | $94.94 | PASS |  |  |
| SO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.91% | -1.91% | PASS |  |  |
| SO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| SO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $94.94 · close 1.91% below · Nov 20 close | payload values | PASS |  |  |
| SO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $169.83 | $169.83 | PASS |  |  |
| SOXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -81.82% | -81.82% | PASS |  |  |
| SOXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $169.83 · close 81.82% below · Nov 20 close | payload values | PASS |  |  |
| SOXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $40.79 | $40.79 | PASS |  |  |
| SOXL.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -80.75% | -80.76% | PASS |  |  |
| SOXL.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $40.79 · close 80.75% below · Nov 20 close | payload values | PASS |  |  |
| SOXL.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $198.81 | $198.81 | PASS |  |  |
| SOXX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.93% | -37.93% | PASS |  |  |
| SOXX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $198.81 · close 37.93% below · Nov 20 close | payload values | PASS |  |  |
| SOXX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SPCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.54 | $33.54 | PASS |  |  |
| SPCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -78.38% | -78.38% | PASS |  |  |
| SPCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SPCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SPCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SPCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.54 · close 78.38% below · Nov 20 close | payload values | PASS |  |  |
| SPCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $414.23 | $414.23 | PASS |  |  |
| TSLA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -16.52% | -16.52% | PASS |  |  |
| TSLA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $414.23 · close 16.52% below · Nov 20 close | payload values | PASS |  |  |
| TSLA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $11.98 | $11.98 | PASS |  |  |
| TSLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.64% | -32.64% | PASS |  |  |
| TSLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $11.98 · close 32.64% below · Nov 20 close | payload values | PASS |  |  |
| TSLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $487.47 | $487.47 | PASS |  |  |
| TSM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -34.62% | -34.62% | PASS |  |  |
| TSM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $487.47 · close 34.62% below · Nov 20 close | payload values | PASS |  |  |
| TSM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UBOT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $25.58 | $25.58 | PASS |  |  |
| UBOT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -50.2% | -50.20% | PASS |  |  |
| UBOT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UBOT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UBOT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UBOT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $25.58 · close 50.20% below · Nov 20 close | payload values | PASS |  |  |
| UBOT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UFO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.29 | $49.29 | PASS |  |  |
| UFO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.22% | -27.23% | PASS |  |  |
| UFO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UFO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UFO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UFO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.29 · close 27.22% below · Nov 20 close | payload values | PASS |  |  |
| UFO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| URA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $50.09 | $50.09 | PASS |  |  |
| URA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -46.46% | -46.46% | PASS |  |  |
| URA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| URA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| URA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| URA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $50.09 · close 46.46% below · Nov 20 close | payload values | PASS |  |  |
| URA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| URAA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.45 | $31.45 | PASS |  |  |
| URAA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -71.13% | -71.13% | PASS |  |  |
| URAA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| URAA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| URAA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| URAA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.45 · close 71.13% below · Nov 20 close | payload values | PASS |  |  |
| URAA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $441.41 | $441.41 | PASS |  |  |
| V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -8.96% | -8.96% | PASS |  |  |
| V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $441.41 · close 8.96% below · Nov 20 close | payload values | PASS |  |  |
| V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| VFV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.89% | -10.89% | PASS |  |  |
| VFV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VFV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VFV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VFV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $197.83 · close 10.89% below · Nov 20 close | payload values | PASS |  |  |
| VFV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| VRT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.23 | $300.23 | PASS |  |  |
| VRT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -44.63% | -44.63% | PASS |  |  |
| VRT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VRT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VRT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VRT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.23 · close 44.63% below · Nov 20 close | payload values | PASS |  |  |
| VRT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WDC.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.32 | $33.32 | PASS |  |  |
| WDC.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -52.49% | -52.49% | PASS |  |  |
| WDC.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WDC.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WDC.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| WDC.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.32 · close 52.49% below · Nov 20 close | payload values | PASS |  |  |
| WDC.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WELL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $248.26 | $248.26 | PASS |  |  |
| WELL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.19% | -3.19% | PASS |  |  |
| WELL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WELL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WELL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| WELL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $248.26 · close 3.19% below · Nov 20 close | payload values | PASS |  |  |
| WELL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $131.82 | $131.82 | PASS |  |  |
| WMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.94% | -2.94% | PASS |  |  |
| WMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| WMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $131.82 · close 2.94% below · Nov 20 close | payload values | PASS |  |  |
| WMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XCHP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $147.5 | $147.50 | PASS |  |  |
| XCHP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.67% | -37.67% | PASS |  |  |
| XCHP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XCHP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XCHP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XCHP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $147.50 · close 37.67% below · Nov 20 close | payload values | PASS |  |  |
| XCHP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XDRV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.26 | $49.26 | PASS |  |  |
| XDRV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.29% | -26.29% | PASS |  |  |
| XDRV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XDRV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XDRV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XDRV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.26 · close 26.29% below · Nov 20 close | payload values | PASS |  |  |
| XDRV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XEQT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.51% | -9.51% | PASS |  |  |
| XEQT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XEQT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XEQT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XEQT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.38 · close 9.51% below · Nov 20 close | payload values | PASS |  |  |
| XEQT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XETM.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $91.8 | $91.80 | PASS |  |  |
| XETM.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.09% | -42.09% | PASS |  |  |
| XETM.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XETM.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XETM.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XETM.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $91.80 · close 42.09% below · Nov 20 close | payload values | PASS |  |  |
| XETM.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XGD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $65.29 | $65.29 | PASS |  |  |
| XGD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.03% | -32.03% | PASS |  |  |
| XGD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XGD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XGD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XGD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $65.29 · close 32.03% below · Nov 20 close | payload values | PASS |  |  |
| XGD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $187.33 | $187.33 | PASS |  |  |
| XOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.6% | -14.61% | PASS |  |  |
| XOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $187.33 · close 14.60% below · Nov 20 close | payload values | PASS |  |  |
| XOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $342.56 · Nov 20 | $342.56 · Nov 20 | PASS |  |  |
| AAPU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $45.91 · Nov 20 | $45.91 · Nov 20 | PASS |  |  |
| ABBV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.6 / Mom: +1.28 / Rank: 2/11] XLV LEADING | RS 105.6 Mom 1.28 Rank 2/11 | PASS |  |  |
| ABBV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| ABBV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ABBV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $286.20 · Nov 20 | $286.20 · Nov 20 | PASS |  |  |
| AIPO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AIPO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $20.43 · Nov 20 | $20.43 · Nov 20 | PASS |  |  |
| ALAB | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| ALAB | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ALAB | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ALAB | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $180.35 · Nov 20 | $180.35 · Nov 20 | PASS |  |  |
| AMD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| AMD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $424.39 · Nov 20 | $424.39 · Nov 20 | PASS |  |  |
| AMD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| AMD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.56 / Mom: +2.38 / Rank: 7/11] X | RS 98.56 Mom 2.38 Rank 7/11 | PASS |  |  |
| AMZN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| AMZN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $246.82 · Nov 20 | $246.82 · Nov 20 | PASS |  |  |
| AMZU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $32.16 · Nov 20 | $32.16 · Nov 20 | PASS |  |  |
| ANET.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASML.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.72 / Mom: +0.76 / Rank: 6/11] XLB IMPROVING | RS 98.72 Mom 0.76 Rank 6/11 | PASS |  |  |
| ASTL.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ASTL.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $6.15 · Nov 20 | $6.15 · Nov 20 | PASS |  |  |
| ATD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.56 / Mom: +2.38 / Rank: 7/11] X | RS 98.56 Mom 2.38 Rank 7/11 | PASS |  |  |
| ATD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ATD.TO | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 4 days | 📅 Earnings in 4 days | PASS |  |  |
| ATD.TO | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 4 days | 2026-11-24, 4 days | PASS |  |  |
| ATD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $81.72 · Nov 20 | $81.72 · Nov 20 | PASS |  |  |
| AVGC | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGC | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $14.15 · Nov 20 | $14.15 · Nov 20 | PASS |  |  |
| AVGO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| AVGO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AVGO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $304.41 · Nov 20 | $304.41 · Nov 20 | PASS |  |  |
| AVGO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BDT.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| BDT.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| BDT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BDT.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $69.45 · Nov 20 | $69.45 · Nov 20 | PASS |  |  |
| BOTZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BOTZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $27.34 · Nov 20 | $27.34 · Nov 20 | PASS |  |  |
| BRK-B | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.11 / Mom: -0.36 / Rank: 4/11] XLF WEAKENIN | RS 100.11 Mom -0.36 Rank 4/11 | PASS |  |  |
| BRK-B | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| BRK-B | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRK-B | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $570.00 · Nov 20 | $570.00 · Nov 20 | PASS |  |  |
| BRKU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRKU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $28.45 · Nov 20 | $28.45 · Nov 20 | PASS |  |  |
| CAMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| CAMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAMT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $89.20 · Nov 20 | $89.20 · Nov 20 | PASS |  |  |
| CARS.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| CAT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $510.63 · Nov 20 | $510.63 · Nov 20 | PASS |  |  |
| CCO.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.53 / Mom: +0.47 / Rank: 1/11] XLE LEADING | RS 106.53 Mom 0.47 Rank 1/11 | PASS |  |  |
| CCO.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CCO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CCO.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $83.11 · Nov 20 | $83.11 · Nov 20 | PASS |  |  |
| CEG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.97 / Mom: +3.18 / Rank: 10/11] XLU IMPROVING | RS 96.97 Mom 3.18 Rank 10/11 | PASS |  |  |
| CEG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| CEG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CEG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $237.41 · Nov 20 | $237.41 · Nov 20 | PASS |  |  |
| CGY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| CGY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CGY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CGY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $78.75 · Nov 20 | $78.75 · Nov 20 | PASS |  |  |
| CNQ.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.53 / Mom: +0.47 / Rank: 1/11] XLE LEADING | RS 106.53 Mom 0.47 Rank 1/11 | PASS |  |  |
| CNQ.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CNQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| CNR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CNR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $175.38 · Nov 20 | $175.38 · Nov 20 | PASS |  |  |
| COP | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.53 / Mom: +0.47 / Rank: 1/11] XLE LEADING | RS 106.53 Mom 0.47 Rank 1/11 | PASS |  |  |
| COP | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COP | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COP | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $136.12 · Nov 20 | $136.12 · Nov 20 | PASS |  |  |
| COPP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $56.33 · Nov 20 | $56.33 · Nov 20 | PASS |  |  |
| COPZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $6.33 · Nov 20 | $6.33 · Nov 20 | PASS |  |  |
| COST | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.86 / Mom: +3.52 / Rank: 3/11] XLP LE | RS 101.86 Mom 3.52 Rank 3/11 | PASS |  |  |
| COST | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COST | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COST | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,102.15 · Nov 20 | $1,102.15 · Nov 20 | PASS |  |  |
| COTG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COTG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $16.69 · Nov 20 | $16.69 · Nov 20 | PASS |  |  |
| CSU.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| CSU.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CSU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CSU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3,096.00 · Nov 20 | $3,096.00 · Nov 20 | PASS |  |  |
| CVX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.53 / Mom: +0.47 / Rank: 1/11] XLE LEADING | RS 106.53 Mom 0.47 Rank 1/11 | PASS |  |  |
| CVX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CVX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CVX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $208.37 · Nov 20 | $208.37 · Nov 20 | PASS |  |  |
| DRAL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3.01 · Nov 20 | $3.01 · Nov 20 | PASS |  |  |
| DRAM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $33.36 · Nov 20 | $33.36 · Nov 20 | PASS |  |  |
| DRIV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRIV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $24.59 · Nov 20 | $24.59 · Nov 20 | PASS |  |  |
| DUK | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.97 / Mom: +3.18 / Rank: 10/11] XLU IMPROVING | RS 96.97 Mom 3.18 Rank 10/11 | PASS |  |  |
| DUK | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| DUK | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DUK | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $129.78 · Nov 20 | $129.78 · Nov 20 | PASS |  |  |
| ELIL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ELIL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $36.41 · Nov 20 | $36.41 · Nov 20 | PASS |  |  |
| EQIX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.34 / Mom: +1.45 / Rank: 9/11] XLRE IMPROV | RS 97.34 Mom 1.45 Rank 9/11 | PASS |  |  |
| EQIX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| EQIX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| EQIX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $968.44 · Nov 20 | $968.44 · Nov 20 | PASS |  |  |
| ETN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| ETN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ETN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ETN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $311.33 · Nov 20 | $311.33 · Nov 20 | PASS |  |  |
| FCX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.72 / Mom: +0.76 / Rank: 6/11] XLB IMPROVING | RS 98.72 Mom 0.76 Rank 6/11 | PASS |  |  |
| FCX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| FCX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| FCX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $45.99 · Nov 20 | $45.99 · Nov 20 | PASS |  |  |
| FINN.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $68.40 · Nov 20 | $68.40 · Nov 20 | PASS |  |  |
| GDXU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| GE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $309.62 · Nov 20 | $309.62 · Nov 20 | PASS |  |  |
| GEV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| GEV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GEV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GEV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $699.33 · Nov 20 | $699.33 · Nov 20 | PASS |  |  |
| GEV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $56.59 · Nov 20 | $56.59 · Nov 20 | PASS |  |  |
| GIB-A.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| GIB-A.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GIB-A.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GIB-A.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $113.76 · Nov 20 | $113.76 · Nov 20 | PASS |  |  |
| GOOGL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.04 / Mom: +0.33 / Rank: 8/11] X | RS 98.04 Mom 0.33 Rank 8/11 | PASS |  |  |
| GOOGL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| GOOGL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GOOGL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $265.29 · Nov 20 | $265.29 · Nov 20 | PASS |  |  |
| GRID | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GRID | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $145.44 · Nov 20 | $145.44 · Nov 20 | PASS |  |  |
| HD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.56 / Mom: +2.38 / Rank: 7/11] X | RS 98.56 Mom 2.38 Rank 7/11 | PASS |  |  |
| HD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| HD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $339.10 · Nov 20 | $339.10 · Nov 20 | PASS |  |  |
| HURA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HXQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.6 / Mom: +1.28 / Rank: 2/11] XLV LEADING | RS 105.6 Mom 1.28 Rank 2/11 | PASS |  |  |
| JNJ | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| JNJ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $270.47 · Nov 20 | $270.47 · Nov 20 | PASS |  |  |
| JPM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.11 / Mom: -0.36 / Rank: 4/11] XLF WEAKENIN | RS 100.11 Mom -0.36 Rank 4/11 | PASS |  |  |
| JPM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| JPM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JPM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $310.53 · Nov 20 | $310.53 · Nov 20 | PASS |  |  |
| KEYS | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| KEYS | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| KEYS | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| KEYS | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $261.51 · Nov 20 | $261.51 · Nov 20 | PASS |  |  |
| LIN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.72 / Mom: +0.76 / Rank: 6/11] XLB IMPROVING | RS 98.72 Mom 0.76 Rank 6/11 | PASS |  |  |
| LIN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| LIN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LIN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $502.83 · Nov 20 | $502.83 · Nov 20 | PASS |  |  |
| LLY | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.6 / Mom: +1.28 / Rank: 2/11] XLV LEADING | RS 105.6 Mom 1.28 Rank 2/11 | PASS |  |  |
| LLY | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| LLY | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LLY | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,347.11 · Nov 20 | $1,347.11 · Nov 20 | PASS |  |  |
| MDA.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| MDA.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MDA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MDA.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $36.88 · Nov 20 | $36.88 · Nov 20 | PASS |  |  |
| META | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.04 / Mom: +0.33 / Rank: 8/11] X | RS 98.04 Mom 0.33 Rank 8/11 | PASS |  |  |
| META | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| META | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| META | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $560.84 · Nov 20 | $560.84 · Nov 20 | PASS |  |  |
| METU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| METU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $17.61 · Nov 20 | $17.61 · Nov 20 | PASS |  |  |
| MRVL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| MRVL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MRVL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MRVL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $122.28 · Nov 20 | $122.28 · Nov 20 | PASS |  |  |
| MSFT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| MSFT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MSFT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $484.52 · Nov 20 | $484.52 · Nov 20 | PASS |  |  |
| MSFU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $34.23 · Nov 20 | $34.23 · Nov 20 | PASS |  |  |
| MTRX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.97 / Mom: +3.18 / Rank: 10/11] XLU IMPROVING | RS 96.97 Mom 3.18 Rank 10/11 | PASS |  |  |
| NEE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $83.45 · Nov 20 | $83.45 · Nov 20 | PASS |  |  |
| NEM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.72 / Mom: +0.76 / Rank: 6/11] XLB IMPROVING | RS 98.72 Mom 0.76 Rank 6/11 | PASS |  |  |
| NEM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $94.68 · Nov 20 | $94.68 · Nov 20 | PASS |  |  |
| NFLX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.04 / Mom: +0.33 / Rank: 8/11] X | RS 98.04 Mom 0.33 Rank 8/11 | PASS |  |  |
| NFLX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NFLX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFLX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $56.73 · Nov 20 | $56.73 · Nov 20 | PASS |  |  |
| NFXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $8.90 · Nov 20 | $8.90 · Nov 20 | PASS |  |  |
| NTR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.72 / Mom: +0.76 / Rank: 6/11] XLB IMPROVING | RS 98.72 Mom 0.76 Rank 6/11 | PASS |  |  |
| NTR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NTR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NTR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $91.71 · Nov 20 | $91.71 · Nov 20 | PASS |  |  |
| NVDA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| NVDA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| NVDA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $125.53 · Nov 20 | $125.53 · Nov 20 | PASS |  |  |
| NVDL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $10.33 · Nov 20 | $10.33 · Nov 20 | PASS |  |  |
| ONTO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| ONTO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ONTO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ONTO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $170.16 · Nov 20 | $170.16 · Nov 20 | PASS |  |  |
| ORBX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| ORCL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ORCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $101.19 · Nov 20 | $101.19 · Nov 20 | PASS |  |  |
| PG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.86 / Mom: +3.52 / Rank: 3/11] XLP LE | RS 101.86 Mom 3.52 Rank 3/11 | PASS |  |  |
| PG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| PG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $169.46 · Nov 20 | $169.46 · Nov 20 | PASS |  |  |
| PLD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.34 / Mom: +1.45 / Rank: 9/11] XLRE IMPROV | RS 97.34 Mom 1.45 Rank 9/11 | PASS |  |  |
| PLD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| PLD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PLD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $122.50 · Nov 20 | $122.50 · Nov 20 | PASS |  |  |
| PNG.V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| PNG.V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| PNG.V | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 4 days | 📅 Earnings in 4 days | PASS |  |  |
| PNG.V | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 4 days | 2026-11-24, 4 days | PASS |  |  |
| QCOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| QCOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| QCOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QCOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $149.94 · Nov 20 | $149.94 · Nov 20 | PASS |  |  |
| QPUX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QPUX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $2.47 · Nov 20 | $2.47 · Nov 20 | PASS |  |  |
| QTUM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QTUM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $111.43 · Nov 20 | $111.43 · Nov 20 | PASS |  |  |
| RBOT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| RTX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| RTX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $190.17 · Nov 20 | $190.17 · Nov 20 | PASS |  |  |
| RY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.11 / Mom: -0.36 / Rank: 4/11] XLF WEAKENIN | RS 100.11 Mom -0.36 Rank 4/11 | PASS |  |  |
| RY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| RY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $263.05 · Nov 20 | $263.05 · Nov 20 | PASS |  |  |
| SETM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SETM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $19.53 · Nov 20 | $19.53 · Nov 20 | PASS |  |  |
| SGRD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $399.51 · Nov 20 | $399.51 · Nov 20 | PASS |  |  |
| SNDK.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.97 / Mom: +3.18 / Rank: 10/11] XLU IMPROVING | RS 96.97 Mom 3.18 Rank 10/11 | PASS |  |  |
| SO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| SO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $93.13 · Nov 20 | $93.13 · Nov 20 | PASS |  |  |
| SOXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $30.88 · Nov 20 | $30.88 · Nov 20 | PASS |  |  |
| SOXL.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL.NE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $7.85 · Nov 20 | $7.85 · Nov 20 | PASS |  |  |
| SOXX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $123.40 · Nov 20 | $123.40 · Nov 20 | PASS |  |  |
| SPCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SPCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $7.25 · Nov 20 | $7.25 · Nov 20 | PASS |  |  |
| TSLA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.56 / Mom: +2.38 / Rank: 7/11] X | RS 98.56 Mom 2.38 Rank 7/11 | PASS |  |  |
| TSLA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| TSLA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $345.82 · Nov 20 | $345.82 · Nov 20 | PASS |  |  |
| TSLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $8.07 · Nov 20 | $8.07 · Nov 20 | PASS |  |  |
| TSM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 98.94 / Mom: -2.08 / Rank: 5/11] XLK LAGGING | RS 98.94 Mom -2.08 Rank 5/11 | PASS |  |  |
| TSM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| TSM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $318.71 · Nov 20 | $318.71 · Nov 20 | PASS |  |  |
| UBOT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UBOT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.74 · Nov 20 | $12.74 · Nov 20 | PASS |  |  |
| UFO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UFO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $35.87 · Nov 20 | $35.87 · Nov 20 | PASS |  |  |
| URA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $26.82 · Nov 20 | $26.82 · Nov 20 | PASS |  |  |
| URAA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URAA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $9.08 · Nov 20 | $9.08 · Nov 20 | PASS |  |  |
| V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.11 / Mom: -0.36 / Rank: 4/11] XLF WEAKENIN | RS 100.11 Mom -0.36 Rank 4/11 | PASS |  |  |
| V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| V | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| V | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $401.87 · Nov 20 | $401.87 · Nov 20 | PASS |  |  |
| VFV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VRT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.51 / Mom: -0.42 / Rank: 11/11] XLI LAGGING | RS 95.51 Mom -0.42 Rank 11/11 | PASS |  |  |
| VRT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| VRT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VRT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $166.24 · Nov 20 | $166.24 · Nov 20 | PASS |  |  |
| WDC.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WELL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.34 / Mom: +1.45 / Rank: 9/11] XLRE IMPROV | RS 97.34 Mom 1.45 Rank 9/11 | PASS |  |  |
| WELL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| WELL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WELL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $240.34 · Nov 20 | $240.34 · Nov 20 | PASS |  |  |
| WMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.86 / Mom: +3.52 / Rank: 3/11] XLP LE | RS 101.86 Mom 3.52 Rank 3/11 | PASS |  |  |
| WMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| WMT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $127.95 · Nov 20 | $127.95 · Nov 20 | PASS |  |  |
| XCHP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XDRV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XEQT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XETM.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XGD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.53 / Mom: +0.47 / Rank: 1/11] XLE LEADING | RS 106.53 Mom 0.47 Rank 1/11 | PASS |  |  |
| XOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| XOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $159.97 · Nov 20 | $159.97 · Nov 20 | PASS |  |  |
| AAPL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $360.83 | $360.83 | PASS |  |  |
| AAPL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $342.56 | $342.56 | PASS |  |  |
| AAPL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $360.83 / $242.57 | $360.83 / $242.57 | PASS |  |  |
| AAPL | PD3 | % from High | -5.1% | -5.1% | PASS |  |  |
| AAPL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $14.5B | bars: $14,781,795,187 | PASS | LOW |  |
| AAPU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $51.04 | $51.04 | PASS |  |  |
| AAPU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $45.91 | $45.91 | PASS |  |  |
| AAPU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $51.04 / $25.94 | $51.04 / $25.94 | PASS |  |  |
| AAPU | PD3 | % from High | -10.1% | -10.1% | PASS |  |  |
| ABBV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.93 | $302.93 | PASS |  |  |
| ABBV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $286.20 | $286.20 | PASS |  |  |
| ABBV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.93 / $188.25 | $302.93 / $188.25 | PASS |  |  |
| ABBV | PD3 | % from High | -5.5% | -5.5% | PASS |  |  |
| ABBV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.4B | bars: $1,446,573,384 | PASS | LOW |  |
| AIPO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $34.79 | $34.79 | PASS |  |  |
| AIPO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $20.43 | $20.43 | PASS |  |  |
| AIPO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $34.79 / $20.28 | $34.79 / $20.28 | PASS |  |  |
| AIPO | PD3 | % from High | -41.3% | -41.3% | PASS |  |  |
| AIPO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $31M | bars: $34,230,208 | PASS | LOW |  |
| ALAB | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $499.48 | $499.48 | PASS |  |  |
| ALAB | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $180.35 | $180.35 | PASS |  |  |
| ALAB | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $499.48 / $97.89 | $499.48 / $97.89 | PASS |  |  |
| ALAB | PD3 | % from High | -63.9% | -63.9% | PASS |  |  |
| ALAB | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $776M | bars: $848,648,976 | PASS | LOW |  |
| AMD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $658.52 | $658.52 | PASS |  |  |
| AMD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $424.39 | $424.39 | PASS |  |  |
| AMD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $658.52 / $188.22 | $658.52 / $188.22 | PASS |  |  |
| AMD | PD3 | % from High | -35.6% | -35.6% | PASS |  |  |
| AMD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $11.1B | bars: $12,670,396,389 | PASS | LOW |  |
| AMD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $16.97 | $16.97 | PASS |  |  |
| AMD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $10.93 | $10.93 | PASS |  |  |
| AMD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $16.97 / $4.93 | $16.97 / $4.93 | PASS |  |  |
| AMD.TO | PD3 | % from High | -35.6% | -35.6% | PASS |  |  |
| AMD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $24M | bars: $26,219,110 | PASS | LOW |  |
| AMZN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $287.20 | $287.20 | PASS |  |  |
| AMZN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $246.82 | $246.82 | PASS |  |  |
| AMZN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $287.20 / $196.00 | $287.20 / $196.00 | PASS |  |  |
| AMZN | PD3 | % from High | -14.1% | -14.1% | PASS |  |  |
| AMZN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $9.9B | bars: $10,657,653,366 | PASS | LOW |  |
| AMZU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.65 | $46.65 | PASS |  |  |
| AMZU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $32.16 | $32.16 | PASS |  |  |
| AMZU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.65 / $24.14 | $46.65 / $24.14 | PASS |  |  |
| AMZU | PD3 | % from High | -31.1% | -31.1% | PASS |  |  |
| AMZU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $61M | bars: $62,178,788 | PASS | LOW |  |
| ANET.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $29.87 | $29.87 | PASS |  |  |
| ANET.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.85 / $20.97 | $38.85 / $20.97 | PASS |  |  |
| ANET.TO | PD3 | % from High | -23.1% | -23.1% | PASS |  |  |
| ASML.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $56.75 | $56.75 | PASS |  |  |
| ASML.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $38.95 | $38.95 | PASS |  |  |
| ASML.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $56.75 / $26.65 | $56.75 / $26.65 | PASS |  |  |
| ASML.TO | PD3 | % from High | -31.4% | -31.4% | PASS |  |  |
| ASML.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,822,054 | PASS | LOW |  |
| ASTL.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $8.31 | $8.31 | PASS |  |  |
| ASTL.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $6.15 | $6.15 | PASS |  |  |
| ASTL.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $8.31 / $4.46 | $8.31 / $4.46 | PASS |  |  |
| ASTL.TO | PD3 | % from High | -26.0% | -26.0% | PASS |  |  |
| ASTL.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $3,686,007 | PASS | LOW |  |
| ATD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $94.68 | $94.68 | PASS |  |  |
| ATD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $81.72 | $81.72 | PASS |  |  |
| ATD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $94.68 / $68.15 | $94.68 / $68.15 | PASS |  |  |
| ATD.TO | PD3 | % from High | -13.7% | -13.7% | PASS |  |  |
| ATD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $114M | bars: $108,289,810 | PASS | LOW |  |
| AVGC | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $14.15 | $14.15 | PASS |  |  |
| AVGC | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.79 / $13.71 | $31.79 / $13.71 | PASS |  |  |
| AVGC | PD3 | % from High | -55.5% | -55.5% | PASS |  |  |
| AVGO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $495.00 | $495.00 | PASS |  |  |
| AVGO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $304.41 | $304.41 | PASS |  |  |
| AVGO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $495.00 / $289.77 | $495.00 / $289.77 | PASS |  |  |
| AVGO | PD3 | % from High | -38.5% | -38.5% | PASS |  |  |
| AVGO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $7.7B | bars: $7,901,198,271 | PASS | LOW |  |
| AVGO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $11.53 | $11.53 | PASS |  |  |
| AVGO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $18.88 / $11.00 | $18.88 / $11.00 | PASS |  |  |
| AVGO.TO | PD3 | % from High | -38.9% | -38.9% | PASS |  |  |
| AVGO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $13M | bars: $14,384,556 | PASS | LOW |  |
| BDT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $69.45 | $69.45 | PASS |  |  |
| BDT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $86.42 / $24.37 | $86.42 / $24.37 | PASS |  |  |
| BDT.TO | PD3 | % from High | -19.6% | -19.6% | PASS |  |  |
| BDT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $27M | bars: $29,254,725 | PASS | LOW |  |
| BOTZ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $41.69 | $41.69 | PASS |  |  |
| BOTZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $27.34 | $27.34 | PASS |  |  |
| BOTZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $41.69 / $27.20 | $41.69 / $27.20 | PASS |  |  |
| BOTZ | PD3 | % from High | -34.4% | -34.4% | PASS |  |  |
| BOTZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $20M | bars: $20,836,933 | PASS | LOW |  |
| BRK-B | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $596.92 | $596.92 | PASS |  |  |
| BRK-B | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $570.00 | $570.00 | PASS |  |  |
| BRK-B | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $596.92 / $464.01 | $596.92 / $464.01 | PASS |  |  |
| BRK-B | PD3 | % from High | -4.5% | -4.5% | PASS |  |  |
| BRK-B | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.7B | bars: $2,820,904,555 | PASS | LOW |  |
| BRKU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $31.20 | $31.20 | PASS |  |  |
| BRKU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $28.45 | $28.45 | PASS |  |  |
| BRKU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.20 / $20.05 | $31.20 / $20.05 | PASS |  |  |
| BRKU | PD3 | % from High | -8.8% | -8.8% | PASS |  |  |
| CAMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $215.99 | $215.99 | PASS |  |  |
| CAMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $89.20 | $89.20 | PASS |  |  |
| CAMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $215.99 / $87.59 | $215.99 / $87.59 | PASS |  |  |
| CAMT | PD3 | % from High | -58.7% | -58.7% | PASS |  |  |
| CAMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $43M | bars: $46,836,112 | PASS | LOW |  |
| CARS.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.16 | $38.16 | PASS |  |  |
| CARS.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $18.07 | $18.07 | PASS |  |  |
| CARS.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.16 / $18.07 | $38.16 / $18.07 | PASS |  |  |
| CARS.TO | PD3 | % from High | -52.6% | -52.6% | PASS |  |  |
| CARS.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| CAT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,068.94 | $1,068.94 | PASS |  |  |
| CAT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $510.63 | $510.63 | PASS |  |  |
| CAT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,068.94 / $508.11 | $1,068.94 / $508.11 | PASS |  |  |
| CAT | PD3 | % from High | -52.2% | -52.2% | PASS |  |  |
| CAT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.5B | bars: $1,675,575,859 | PASS | LOW |  |
| CCO.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $182.72 | $182.72 | PASS |  |  |
| CCO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $83.11 | $83.11 | PASS |  |  |
| CCO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $182.72 / $83.06 | $182.72 / $83.06 | PASS |  |  |
| CCO.TO | PD3 | % from High | -54.5% | -54.5% | PASS |  |  |
| CCO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $98M | bars: $107,729,933 | PASS | LOW |  |
| CEG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $378.52 | $378.52 | PASS |  |  |
| CEG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $237.41 | $237.41 | PASS |  |  |
| CEG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $378.52 / $227.93 | $378.52 / $227.93 | PASS |  |  |
| CEG | PD3 | % from High | -37.3% | -37.3% | PASS |  |  |
| CEG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $839M | bars: $925,918,415 | PASS | LOW |  |
| CGY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $78.75 | $78.75 | PASS |  |  |
| CGY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $95.15 / $44.20 | $95.15 / $44.20 | PASS |  |  |
| CGY.TO | PD3 | % from High | -17.2% | -17.2% | PASS |  |  |
| CGY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,428,178 | PASS | LOW |  |
| CNQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $78.60 | $78.60 | PASS |  |  |
| CNQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $63.74 | $63.74 | PASS |  |  |
| CNQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $78.60 / $40.51 | $78.60 / $40.51 | PASS |  |  |
| CNQ.TO | PD3 | % from High | -18.9% | -18.9% | PASS |  |  |
| CNQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $875M | bars: $763,522,437 | PASS | LOW |  |
| CNR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $184.26 | $184.26 | PASS |  |  |
| CNR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $175.38 | $175.38 | PASS |  |  |
| CNR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $184.26 / $125.06 | $184.26 / $125.06 | PASS |  |  |
| CNR.TO | PD3 | % from High | -4.8% | -4.8% | PASS |  |  |
| CNR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $222M | bars: $212,552,706 | PASS | LOW |  |
| COP | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $153.27 | $153.27 | PASS |  |  |
| COP | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $136.12 | $136.12 | PASS |  |  |
| COP | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $153.27 / $83.30 | $153.27 / $83.30 | PASS |  |  |
| COP | PD3 | % from High | -11.2% | -11.2% | PASS |  |  |
| COP | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $915M | bars: $944,648,274 | PASS | LOW |  |
| COPP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $70.54 | $70.54 | PASS |  |  |
| COPP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.49 | $39.49 | PASS |  |  |
| COPP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $70.54 / $39.49 | $70.54 / $39.49 | PASS |  |  |
| COPP.TO | PD3 | % from High | -44.0% | -44.0% | PASS |  |  |
| COPX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $99.65 | $99.65 | PASS |  |  |
| COPX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $56.33 | $56.33 | PASS |  |  |
| COPX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $99.65 / $55.44 | $99.65 / $55.44 | PASS |  |  |
| COPX | PD3 | % from High | -43.5% | -43.5% | PASS |  |  |
| COPX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $174M | bars: $171,241,840 | PASS | LOW |  |
| COPZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $6.33 | $6.33 | PASS |  |  |
| COPZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $26.40 / $6.33 | $26.40 / $6.33 | PASS |  |  |
| COPZ | PD3 | % from High | -76.0% | -76.0% | PASS |  |  |
| COST | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,123.67 | $1,123.67 | PASS |  |  |
| COST | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,102.15 | $1,102.15 | PASS |  |  |
| COST | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,123.67 / $844.06 | $1,123.67 / $844.06 | PASS |  |  |
| COST | PD3 | % from High | -1.9% | -1.9% | PASS |  |  |
| COST | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.5B | bars: $2,660,938,291 | PASS | LOW |  |
| COTG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $17.80 | $17.80 | PASS |  |  |
| COTG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $16.69 | $16.69 | PASS |  |  |
| COTG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $17.80 / $10.95 | $17.80 / $10.95 | PASS |  |  |
| COTG | PD3 | % from High | -6.3% | -6.2% | PASS |  |  |
| COTG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,728,615 | PASS | LOW |  |
| CSU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $3,565.00 | $3,565.00 | PASS |  |  |
| CSU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3,096.00 | $3,096.00 | PASS |  |  |
| CSU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $3,565.00 / $2,192.51 | $3,565.00 / $2,192.51 | PASS |  |  |
| CSU.TO | PD3 | % from High | -13.2% | -13.2% | PASS |  |  |
| CSU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $187M | bars: $192,855,475 | PASS | LOW |  |
| CVX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $234.53 | $234.53 | PASS |  |  |
| CVX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $208.37 | $208.37 | PASS |  |  |
| CVX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $234.53 / $141.34 | $234.53 / $141.34 | PASS |  |  |
| CVX | PD3 | % from High | -11.2% | -11.2% | PASS |  |  |
| CVX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.8B | bars: $1,843,728,264 | PASS | LOW |  |
| DRAL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3.01 | $3.01 | PASS |  |  |
| DRAL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $25.52 / $2.95 | $25.52 / $2.95 | PASS |  |  |
| DRAL | PD3 | % from High | -88.2% | -88.2% | PASS |  |  |
| DRAM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $33.36 | $33.36 | PASS |  |  |
| DRAM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $81.34 / $26.14 | $81.34 / $26.14 | PASS |  |  |
| DRAM | PD3 | % from High | -59.0% | -59.0% | PASS |  |  |
| DRAM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.1B | bars: $1,199,564,033 | PASS | LOW |  |
| DRIV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $42.67 | $42.67 | PASS |  |  |
| DRIV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $24.59 | $24.59 | PASS |  |  |
| DRIV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $42.67 / $24.57 | $42.67 / $24.57 | PASS |  |  |
| DRIV | PD3 | % from High | -42.4% | -42.4% | PASS |  |  |
| DUK | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.87 | $131.87 | PASS |  |  |
| DUK | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $129.78 | $129.78 | PASS |  |  |
| DUK | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.87 / $110.06 | $131.87 / $110.06 | PASS |  |  |
| DUK | PD3 | % from High | -1.6% | -1.6% | PASS |  |  |
| DUK | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $553M | bars: $590,959,667 | PASS | LOW |  |
| ELIL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.56 | $43.56 | PASS |  |  |
| ELIL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $36.41 | $36.41 | PASS |  |  |
| ELIL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.56 / $16.21 | $43.56 / $16.21 | PASS |  |  |
| ELIL | PD3 | % from High | -16.4% | -16.4% | PASS |  |  |
| ELIL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $2,222,163 | PASS | LOW |  |
| EQIX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,112.65 | $1,112.65 | PASS |  |  |
| EQIX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $968.44 | $968.44 | PASS |  |  |
| EQIX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,112.65 / $706.18 | $1,112.65 / $706.18 | PASS |  |  |
| EQIX | PD3 | % from High | -13.0% | -13.0% | PASS |  |  |
| EQIX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $561M | bars: $609,056,565 | PASS | LOW |  |
| ETN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $478.00 | $478.00 | PASS |  |  |
| ETN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $311.33 | $311.33 | PASS |  |  |
| ETN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $478.00 / $308.22 | $478.00 / $308.22 | PASS |  |  |
| ETN | PD3 | % from High | -34.9% | -34.9% | PASS |  |  |
| ETN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $774M | bars: $856,905,396 | PASS | LOW |  |
| FCX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.07 | $80.07 | PASS |  |  |
| FCX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $45.99 | $45.99 | PASS |  |  |
| FCX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.07 / $38.49 | $80.07 / $38.49 | PASS |  |  |
| FCX | PD3 | % from High | -42.6% | -42.6% | PASS |  |  |
| FCX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $602M | bars: $582,577,712 | PASS | LOW |  |
| FINN.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $35.83 | $35.83 | PASS |  |  |
| FINN.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.38 | $30.38 | PASS |  |  |
| FINN.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $35.83 / $21.66 | $35.83 / $21.66 | PASS |  |  |
| FINN.NE | PD3 | % from High | -15.2% | -15.2% | PASS |  |  |
| FINN.NE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $9M | bars: $9,405,866 | PASS | LOW |  |
| GDX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $117.18 | $117.18 | PASS |  |  |
| GDX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $68.40 | $68.40 | PASS |  |  |
| GDX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $117.18 / $68.03 | $117.18 / $68.03 | PASS |  |  |
| GDX | PD3 | % from High | -41.6% | -41.6% | PASS |  |  |
| GDX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.5B | bars: $1,563,406,928 | PASS | LOW |  |
| GDXU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $65.00 | $65.00 | PASS |  |  |
| GDXU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $18.20 | $18.20 | PASS |  |  |
| GDXU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $65.00 / $18.09 | $65.00 / $18.09 | PASS |  |  |
| GDXU.TO | PD3 | % from High | -72.0% | -72.0% | PASS |  |  |
| GDXU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $4,767,844 | PASS | LOW |  |
| GE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $388.84 | $388.84 | PASS |  |  |
| GE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $309.62 | $309.62 | PASS |  |  |
| GE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $388.84 / $268.91 | $388.84 / $268.91 | PASS |  |  |
| GE | PD3 | % from High | -20.4% | -20.4% | PASS |  |  |
| GE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.4B | bars: $1,524,420,752 | PASS | LOW |  |
| GEV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,195.94 | $1,195.94 | PASS |  |  |
| GEV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $699.33 | $699.33 | PASS |  |  |
| GEV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,195.94 / $530.16 | $1,195.94 / $530.16 | PASS |  |  |
| GEV | PD3 | % from High | -41.5% | -41.5% | PASS |  |  |
| GEV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.1B | bars: $2,313,104,537 | PASS | LOW |  |
| GEV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $46.48 | $46.48 | PASS |  |  |
| GEV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.44 / $42.23 | $80.44 / $42.23 | PASS |  |  |
| GEV.TO | PD3 | % from High | -42.2% | -42.2% | PASS |  |  |
| GEV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,740,938 | PASS | LOW |  |
| GGLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $153.00 | $153.00 | PASS |  |  |
| GGLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $56.59 | $56.59 | PASS |  |  |
| GGLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $153.00 / $56.00 | $153.00 / $56.00 | PASS |  |  |
| GGLL | PD3 | % from High | -63.0% | -63.0% | PASS |  |  |
| GGLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $99M | bars: $110,663,380 | PASS | LOW |  |
| GIB-A.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.27 | $131.27 | PASS |  |  |
| GIB-A.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $113.76 | $113.76 | PASS |  |  |
| GIB-A.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.27 / $83.04 | $131.27 / $83.04 | PASS |  |  |
| GIB-A.TO | PD3 | % from High | -13.3% | -13.3% | PASS |  |  |
| GIB-A.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $68M | bars: $70,705,296 | PASS | LOW |  |
| GOOGL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $408.10 | $408.10 | PASS |  |  |
| GOOGL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $265.29 | $265.29 | PASS |  |  |
| GOOGL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $408.10 / $264.22 | $408.10 / $264.22 | PASS |  |  |
| GOOGL | PD3 | % from High | -35.0% | -35.0% | PASS |  |  |
| GOOGL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.2B | bars: $8,825,281,192 | PASS | LOW |  |
| GRID | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $198.80 | $198.80 | PASS |  |  |
| GRID | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $145.44 | $145.44 | PASS |  |  |
| GRID | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $198.80 / $143.36 | $198.80 / $143.36 | PASS |  |  |
| GRID | PD3 | % from High | -26.8% | -26.8% | PASS |  |  |
| GRID | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $85M | bars: $91,866,795 | PASS | LOW |  |
| HD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $389.24 | $389.24 | PASS |  |  |
| HD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $339.10 | $339.10 | PASS |  |  |
| HD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.24 / $277.15 | $389.24 / $277.15 | PASS |  |  |
| HD | PD3 | % from High | -12.9% | -12.9% | PASS |  |  |
| HD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,812,706,931 | PASS | LOW |  |
| HURA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $73.95 | $73.95 | PASS |  |  |
| HURA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $33.89 | $33.89 | PASS |  |  |
| HURA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $73.95 / $33.84 | $73.95 / $33.84 | PASS |  |  |
| HURA.TO | PD3 | % from High | -54.2% | -54.2% | PASS |  |  |
| HXQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $103.40 | $103.40 | PASS |  |  |
| HXQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $128.37 / $91.48 | $128.37 / $91.48 | PASS |  |  |
| HXQ.TO | PD3 | % from High | -19.5% | -19.5% | PASS |  |  |
| HXQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,801,915 | PASS | LOW |  |
| JNJ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $290.25 | $290.25 | PASS |  |  |
| JNJ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $270.47 | $270.47 | PASS |  |  |
| JNJ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $290.25 / $196.75 | $290.25 / $196.75 | PASS |  |  |
| JNJ | PD3 | % from High | -6.8% | -6.8% | PASS |  |  |
| JNJ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.9B | bars: $2,057,855,237 | PASS | LOW |  |
| JPM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $364.68 | $364.68 | PASS |  |  |
| JPM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $310.53 | $310.53 | PASS |  |  |
| JPM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $364.68 / $275.06 | $364.68 / $275.06 | PASS |  |  |
| JPM | PD3 | % from High | -14.8% | -14.8% | PASS |  |  |
| JPM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,425,038,412 | PASS | LOW |  |
| KEYS | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $389.93 | $389.93 | PASS |  |  |
| KEYS | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $261.51 | $261.51 | PASS |  |  |
| KEYS | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.93 / $167.23 | $389.93 / $167.23 | PASS |  |  |
| KEYS | PD3 | % from High | -32.9% | -32.9% | PASS |  |  |
| KEYS | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $339M | bars: $368,798,536 | PASS | LOW |  |
| LIN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $546.40 | $546.40 | PASS |  |  |
| LIN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $502.83 | $502.83 | PASS |  |  |
| LIN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $546.40 / $384.00 | $546.40 / $384.00 | PASS |  |  |
| LIN | PD3 | % from High | -8.0% | -8.0% | PASS |  |  |
| LIN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.0B | bars: $1,067,507,748 | PASS | LOW |  |
| LLY | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,475.25 | $1,475.25 | PASS |  |  |
| LLY | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,347.11 | $1,347.11 | PASS |  |  |
| LLY | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,475.25 / $846.81 | $1,475.25 / $846.81 | PASS |  |  |
| LLY | PD3 | % from High | -8.7% | -8.7% | PASS |  |  |
| LLY | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.5B | bars: $3,584,880,178 | PASS | LOW |  |
| MDA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $67.90 | $67.90 | PASS |  |  |
| MDA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $36.88 | $36.88 | PASS |  |  |
| MDA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $67.90 / $22.13 | $67.90 / $22.13 | PASS |  |  |
| MDA.TO | PD3 | % from High | -45.7% | -45.7% | PASS |  |  |
| MDA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $57M | bars: $57,972,503 | PASS | LOW |  |
| META | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $779.82 | $779.82 | PASS |  |  |
| META | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $560.84 | $560.84 | PASS |  |  |
| META | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $779.82 / $519.37 | $779.82 / $519.37 | PASS |  |  |
| META | PD3 | % from High | -28.1% | -28.1% | PASS |  |  |
| META | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $11.7B | bars: $12,184,404,398 | PASS | LOW |  |
| METU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.96 | $38.96 | PASS |  |  |
| METU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.61 | $17.61 | PASS |  |  |
| METU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.96 / $16.76 | $38.96 / $16.76 | PASS |  |  |
| METU | PD3 | % from High | -54.8% | -54.8% | PASS |  |  |
| METU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $92M | bars: $82,121,928 | PASS | LOW |  |
| MRVL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $329.73 | $329.73 | PASS |  |  |
| MRVL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $122.28 | $122.28 | PASS |  |  |
| MRVL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $329.73 / $70.62 | $329.73 / $70.62 | PASS |  |  |
| MRVL | PD3 | % from High | -62.9% | -62.9% | PASS |  |  |
| MRVL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.0B | bars: $3,041,379,703 | PASS | LOW |  |
| MSFT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $558.07 | $558.07 | PASS |  |  |
| MSFT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $484.52 | $484.52 | PASS |  |  |
| MSFT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $558.07 / $347.87 | $558.07 / $347.87 | PASS |  |  |
| MSFT | PD3 | % from High | -13.2% | -13.2% | PASS |  |  |
| MSFT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $11.4B | bars: $12,044,457,805 | PASS | LOW |  |
| MSFU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $45.88 | $45.88 | PASS |  |  |
| MSFU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $34.23 | $34.23 | PASS |  |  |
| MSFU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $45.88 / $19.32 | $45.88 / $19.32 | PASS |  |  |
| MSFU | PD3 | % from High | -25.4% | -25.4% | PASS |  |  |
| MSFU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $85M | bars: $84,943,294 | PASS | LOW |  |
| MTRX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $28.17 | $28.17 | PASS |  |  |
| MTRX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $39.30 / $28.00 | $39.30 / $28.00 | PASS |  |  |
| MTRX.TO | PD3 | % from High | -28.3% | -28.3% | PASS |  |  |
| MU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $55.28 | $55.28 | PASS |  |  |
| MU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $25.97 | $25.97 | PASS |  |  |
| MU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $55.28 / $8.62 | $55.28 / $8.62 | PASS |  |  |
| MU.TO | PD3 | % from High | -53.0% | -53.0% | PASS |  |  |
| MU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $46M | bars: $51,227,189 | PASS | LOW |  |
| NEE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $97.30 | $97.30 | PASS |  |  |
| NEE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $83.45 | $83.45 | PASS |  |  |
| NEE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $97.30 / $74.41 | $97.30 / $74.41 | PASS |  |  |
| NEE | PD3 | % from High | -14.2% | -14.2% | PASS |  |  |
| NEE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.0B | bars: $1,061,630,179 | PASS | LOW |  |
| NEM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $135.01 | $135.01 | PASS |  |  |
| NEM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $94.68 | $94.68 | PASS |  |  |
| NEM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $135.01 / $80.58 | $135.01 / $80.58 | PASS |  |  |
| NEM | PD3 | % from High | -29.9% | -29.9% | PASS |  |  |
| NEM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $656M | bars: $634,527,132 | PASS | LOW |  |
| NFLX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $111.10 | $111.10 | PASS |  |  |
| NFLX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $56.73 | $56.73 | PASS |  |  |
| NFLX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $111.10 / $56.56 | $111.10 / $56.56 | PASS |  |  |
| NFLX | PD3 | % from High | -48.9% | -48.9% | PASS |  |  |
| NFLX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.1B | bars: $2,326,809,173 | PASS | LOW |  |
| NFXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.37 | $43.37 | PASS |  |  |
| NFXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $8.90 | $8.90 | PASS |  |  |
| NFXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.37 / $8.84 | $43.37 / $8.84 | PASS |  |  |
| NFXL | PD3 | % from High | -79.5% | -79.5% | PASS |  |  |
| NFXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $13M | bars: $15,162,829 | PASS | LOW |  |
| NTR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $114.19 | $114.19 | PASS |  |  |
| NTR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $91.71 | $91.71 | PASS |  |  |
| NTR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $114.19 / $74.44 | $114.19 / $74.44 | PASS |  |  |
| NTR.TO | PD3 | % from High | -19.7% | -19.7% | PASS |  |  |
| NTR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $165M | bars: $172,686,634 | PASS | LOW |  |
| NVDA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $243.37 | $243.37 | PASS |  |  |
| NVDA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $125.53 | $125.53 | PASS |  |  |
| NVDA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $243.37 / $124.50 | $243.37 / $124.50 | PASS |  |  |
| NVDA | PD3 | % from High | -48.4% | -48.4% | PASS |  |  |
| NVDA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $20.4B | bars: $22,387,253,593 | PASS | LOW |  |
| NVDL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.27 | $43.27 | PASS |  |  |
| NVDL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $10.33 | $10.33 | PASS |  |  |
| NVDL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.27 / $10.05 | $43.27 / $10.05 | PASS |  |  |
| NVDL | PD3 | % from High | -76.1% | -76.1% | PASS |  |  |
| NVDL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $198M | bars: $218,095,645 | PASS | LOW |  |
| ONTO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $386.46 | $386.46 | PASS |  |  |
| ONTO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $170.16 | $170.16 | PASS |  |  |
| ONTO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $386.46 / $121.57 | $386.46 / $121.57 | PASS |  |  |
| ONTO | PD3 | % from High | -56.0% | -56.0% | PASS |  |  |
| ONTO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $171M | bars: $180,794,673 | PASS | LOW |  |
| ORBX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $14.39 | $14.39 | PASS |  |  |
| ORBX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.62 / $12.81 | $31.62 / $12.81 | PASS |  |  |
| ORBX.TO | PD3 | % from High | -54.5% | -54.5% | PASS |  |  |
| ORCL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $248.46 | $248.46 | PASS |  |  |
| ORCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $101.19 | $101.19 | PASS |  |  |
| ORCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $248.46 / $100.25 | $248.46 / $100.25 | PASS |  |  |
| ORCL | PD3 | % from High | -59.3% | -59.3% | PASS |  |  |
| ORCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.4B | bars: $3,564,780,028 | PASS | LOW |  |
| PG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $173.59 | $173.59 | PASS |  |  |
| PG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $169.46 | $169.46 | PASS |  |  |
| PG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $173.59 / $133.77 | $173.59 / $133.77 | PASS |  |  |
| PG | PD3 | % from High | -2.4% | -2.4% | PASS |  |  |
| PG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,631,952,424 | PASS | LOW |  |
| PLD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $152.14 | $152.14 | PASS |  |  |
| PLD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $122.50 | $122.50 | PASS |  |  |
| PLD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $152.14 / $118.88 | $152.14 / $118.88 | PASS |  |  |
| PLD | PD3 | % from High | -19.5% | -19.5% | PASS |  |  |
| PLD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $453M | bars: $481,488,303 | PASS | LOW |  |
| PNG.V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $10.72 | $10.72 | PASS |  |  |
| PNG.V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $2.79 | $2.79 | PASS |  |  |
| PNG.V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $10.72 / $2.70 | $10.72 / $2.70 | PASS |  |  |
| PNG.V | PD3 | % from High | -74.0% | -74.0% | PASS |  |  |
| PNG.V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $3,537,427 | PASS | LOW |  |
| QCOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $257.56 | $257.56 | PASS |  |  |
| QCOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $149.94 | $149.94 | PASS |  |  |
| QCOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $257.56 / $120.88 | $257.56 / $120.88 | PASS |  |  |
| QCOM | PD3 | % from High | -41.8% | -41.8% | PASS |  |  |
| QCOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.9B | bars: $2,006,257,491 | PASS | LOW |  |
| QPUX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.28 | $80.28 | PASS |  |  |
| QPUX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $2.47 | $2.47 | PASS |  |  |
| QPUX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.28 / $2.42 | $80.28 / $2.42 | PASS |  |  |
| QPUX | PD3 | % from High | -96.9% | -96.9% | PASS |  |  |
| QTUM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $169.21 | $169.21 | PASS |  |  |
| QTUM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $111.43 | $111.43 | PASS |  |  |
| QTUM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $169.21 / $97.17 | $169.21 / $97.17 | PASS |  |  |
| QTUM | PD3 | % from High | -34.1% | -34.1% | PASS |  |  |
| QTUM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $36M | bars: $39,164,895 | PASS | LOW |  |
| RBOT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.15 | $38.15 | PASS |  |  |
| RBOT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $25.00 | $25.00 | PASS |  |  |
| RBOT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.15 / $25.00 | $38.15 / $25.00 | PASS |  |  |
| RBOT.TO | PD3 | % from High | -34.5% | -34.5% | PASS |  |  |
| RTX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $226.41 | $226.41 | PASS |  |  |
| RTX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $190.17 | $190.17 | PASS |  |  |
| RTX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $226.41 / $164.95 | $226.41 / $164.95 | PASS |  |  |
| RTX | PD3 | % from High | -16.0% | -16.0% | PASS |  |  |
| RTX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $881M | bars: $941,863,110 | PASS | LOW |  |
| RY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.65 | $302.65 | PASS |  |  |
| RY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $263.05 | $263.05 | PASS |  |  |
| RY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.65 / $201.71 | $302.65 / $201.71 | PASS |  |  |
| RY.TO | PD3 | % from High | -13.1% | -13.1% | PASS |  |  |
| RY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $843M | bars: $892,417,659 | PASS | LOW |  |
| SETM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $40.55 | $40.55 | PASS |  |  |
| SETM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $19.53 | $19.53 | PASS |  |  |
| SETM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $40.55 / $19.46 | $40.55 / $19.46 | PASS |  |  |
| SETM | PD3 | % from High | -51.8% | -51.8% | PASS |  |  |
| SETM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,537,267 | PASS | LOW |  |
| SGRD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $16.81 | $16.81 | PASS |  |  |
| SGRD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $22.49 / $16.81 | $22.49 / $16.81 | PASS |  |  |
| SGRD.TO | PD3 | % from High | -25.2% | -25.3% | PASS |  |  |
| SMH | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $671.83 | $671.83 | PASS |  |  |
| SMH | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $399.51 | $399.51 | PASS |  |  |
| SMH | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $671.83 / $314.08 | $671.83 / $314.08 | PASS |  |  |
| SMH | PD3 | % from High | -40.5% | -40.5% | PASS |  |  |
| SMH | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.5B | bars: $4,225,597,886 | PASS | LOW |  |
| SNDK.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $15.27 | $15.27 | PASS |  |  |
| SNDK.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $57.55 / $15.16 | $57.55 / $15.16 | PASS |  |  |
| SNDK.TO | PD3 | % from High | -73.5% | -73.5% | PASS |  |  |
| SNDK.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $19M | bars: $20,305,261 | PASS | LOW |  |
| SO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $97.65 | $97.65 | PASS |  |  |
| SO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $93.13 | $93.13 | PASS |  |  |
| SO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $97.65 / $81.03 | $97.65 / $81.03 | PASS |  |  |
| SO | PD3 | % from High | -4.6% | -4.6% | PASS |  |  |
| SO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $653M | bars: $681,790,189 | PASS | LOW |  |
| SOXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $301.80 | $301.80 | PASS |  |  |
| SOXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.88 | $30.88 | PASS |  |  |
| SOXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $301.80 / $28.10 | $301.80 / $28.10 | PASS |  |  |
| SOXL | PD3 | % from High | -89.8% | -89.8% | PASS |  |  |
| SOXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.5B | bars: $4,270,894,450 | PASS | LOW |  |
| SOXL.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $74.21 | $74.21 | PASS |  |  |
| SOXL.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $7.85 | $7.85 | PASS |  |  |
| SOXL.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $74.21 / $7.55 | $74.21 / $7.55 | PASS |  |  |
| SOXL.NE | PD3 | % from High | -89.4% | -89.4% | PASS |  |  |
| SOXL.NE | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| SOXX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $218.51 | $218.51 | PASS |  |  |
| SOXX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $123.40 | $123.40 | PASS |  |  |
| SOXX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $218.51 / $86.54 | $218.51 / $86.54 | PASS |  |  |
| SOXX | PD3 | % from High | -43.5% | -43.5% | PASS |  |  |
| SOXX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.5B | bars: $3,940,770,752 | PASS | LOW |  |
| SPCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $7.25 | $7.25 | PASS |  |  |
| SPCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $83.85 / $7.16 | $83.85 / $7.16 | PASS |  |  |
| SPCL | PD3 | % from High | -91.4% | -91.4% | PASS |  |  |
| TSLA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $498.83 | $498.83 | PASS |  |  |
| TSLA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $345.82 | $345.82 | PASS |  |  |
| TSLA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $498.83 / $297.38 | $498.83 / $297.38 | PASS |  |  |
| TSLA | PD3 | % from High | -30.7% | -30.7% | PASS |  |  |
| TSLA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $12.9B | bars: $12,559,340,148 | PASS | LOW |  |
| TSLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $23.10 | $23.10 | PASS |  |  |
| TSLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $8.07 | $8.07 | PASS |  |  |
| TSLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $23.10 / $6.65 | $23.10 / $6.65 | PASS |  |  |
| TSLL | PD3 | % from High | -65.1% | -65.1% | PASS |  |  |
| TSLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $511M | bars: $435,669,380 | PASS | LOW |  |
| TSM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $487.47 | $487.47 | PASS |  |  |
| TSM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $318.71 | $318.71 | PASS |  |  |
| TSM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $487.47 / $266.82 | $487.47 / $266.82 | PASS |  |  |
| TSM | PD3 | % from High | -34.6% | -34.6% | PASS |  |  |
| TSM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.8B | bars: $4,296,437,607 | PASS | LOW |  |
| UBOT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $32.08 | $32.08 | PASS |  |  |
| UBOT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.74 | $12.74 | PASS |  |  |
| UBOT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $32.08 / $12.57 | $32.08 / $12.57 | PASS |  |  |
| UBOT | PD3 | % from High | -60.3% | -60.3% | PASS |  |  |
| UFO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $68.12 | $68.12 | PASS |  |  |
| UFO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $35.87 | $35.87 | PASS |  |  |
| UFO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $68.12 / $30.78 | $68.12 / $30.78 | PASS |  |  |
| UFO | PD3 | % from High | -47.3% | -47.3% | PASS |  |  |
| UFO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $9M | bars: $9,353,877 | PASS | LOW |  |
| URA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $62.28 | $62.28 | PASS |  |  |
| URA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $26.82 | $26.82 | PASS |  |  |
| URA | PD3 | % from High | -56.9% | -56.9% | PASS |  |  |
| URA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $108M | bars: $121,009,748 | PASS | LOW |  |
| URAA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $62.21 | $62.21 | PASS |  |  |
| URAA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $9.08 | $9.08 | PASS |  |  |
| URAA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $62.21 / $9.00 | $62.21 / $9.00 | PASS |  |  |
| URAA | PD3 | % from High | -85.4% | -85.4% | PASS |  |  |
| V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $441.41 | $441.41 | PASS |  |  |
| V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $401.87 | $401.87 | PASS |  |  |
| V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $441.41 / $292.20 | $441.41 / $292.20 | PASS |  |  |
| V | PD3 | % from High | -9.0% | -9.0% | PASS |  |  |
| V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.6B | bars: $2,717,080,773 | PASS | LOW |  |
| VFV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $176.29 | $176.29 | PASS |  |  |
| VFV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $197.83 / $155.29 | $197.83 / $155.29 | PASS |  |  |
| VFV.TO | PD3 | % from High | -10.9% | -10.9% | PASS |  |  |
| VFV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $53M | bars: $60,007,769 | PASS | LOW |  |
| VRT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $379.76 | $379.76 | PASS |  |  |
| VRT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $166.24 | $166.24 | PASS |  |  |
| VRT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $379.76 / $147.72 | $379.76 / $147.72 | PASS |  |  |
| VRT | PD3 | % from High | -56.2% | -56.2% | PASS |  |  |
| VRT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.0B | bars: $1,128,493,279 | PASS | LOW |  |
| WDC.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $15.83 | $15.83 | PASS |  |  |
| WDC.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $48.85 / $15.57 | $48.85 / $15.57 | PASS |  |  |
| WDC.TO | PD3 | % from High | -67.6% | -67.6% | PASS |  |  |
| WELL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $253.37 | $253.37 | PASS |  |  |
| WELL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $240.34 | $240.34 | PASS |  |  |
| WELL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $253.37 / $178.92 | $253.37 / $178.92 | PASS |  |  |
| WELL | PD3 | % from High | -5.1% | -5.1% | PASS |  |  |
| WELL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $672M | bars: $693,678,840 | PASS | LOW |  |
| WMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $134.84 | $134.84 | PASS |  |  |
| WMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $127.95 | $127.95 | PASS |  |  |
| WMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $134.84 / $101.82 | $134.84 / $101.82 | PASS |  |  |
| WMT | PD3 | % from High | -5.1% | -5.1% | PASS |  |  |
| WMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.0B | bars: $2,901,466,412 | PASS | LOW |  |
| XCHP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $161.26 | $161.26 | PASS |  |  |
| XCHP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $91.94 | $91.94 | PASS |  |  |
| XCHP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $161.26 / $64.67 | $161.26 / $64.67 | PASS |  |  |
| XCHP.TO | PD3 | % from High | -43.0% | -43.0% | PASS |  |  |
| XCHP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $5,068,310 | PASS | LOW |  |
| XDRV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $61.36 | $61.36 | PASS |  |  |
| XDRV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $36.31 | $36.31 | PASS |  |  |
| XDRV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $61.36 / $36.31 | $61.36 / $36.31 | PASS |  |  |
| XDRV.TO | PD3 | % from High | -40.8% | -40.8% | PASS |  |  |
| XDRV.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| XEQT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $41.97 | $41.97 | PASS |  |  |
| XEQT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.38 / $37.96 | $46.38 / $37.96 | PASS |  |  |
| XEQT.TO | PD3 | % from High | -9.5% | -9.5% | PASS |  |  |
| XEQT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $36M | bars: $41,377,314 | PASS | LOW |  |
| XETM.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $53.16 | $53.16 | PASS |  |  |
| XETM.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $93.94 / $53.11 | $93.94 / $53.11 | PASS |  |  |
| XETM.TO | PD3 | % from High | -43.4% | -43.4% | PASS |  |  |
| XGD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $69.54 | $69.54 | PASS |  |  |
| XGD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $44.38 | $44.38 | PASS |  |  |
| XGD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $69.54 / $43.30 | $69.54 / $43.30 | PASS |  |  |
| XGD.TO | PD3 | % from High | -36.2% | -36.2% | PASS |  |  |
| XGD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $21M | bars: $21,183,012 | PASS | LOW |  |
| XOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $187.33 | $187.33 | PASS |  |  |
| XOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $159.97 | $159.97 | PASS |  |  |
| XOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $187.33 / $111.26 | $187.33 / $111.26 | PASS |  |  |
| XOM | PD3 | % from High | -14.6% | -14.6% | PASS |  |  |
| XOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,266,973,202 | PASS | LOW |  |
| AAPL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $342.56 / RS 1.21 | $342.56 / RS 1.21 | PASS |  |  |
| AAPL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.21 | 1.21 | PASS |  |  |
| AAPL | RS2 | Stock 52W Return and S&P 52W Return | +29.1% / +7.0% | +29.1% / +7.0% | PASS |  |  |
| AAPL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market | Ahead of the market | PASS |  |  |
| AAPL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.1% clears | +29.1% clears | PASS |  |  |
| AAPU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $45.91 / RS 1.34 | $45.91 / RS 1.34 | PASS |  |  |
| AAPU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.34 | 1.34 | PASS |  |  |
| AAPU | RS2 | Stock 52W Return and S&P 52W Return | +43.0% / +7.0% | +43.0% / +7.0% | PASS |  |  |
| AAPU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 77 | 77 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market | Well ahead of the market | PASS |  |  |
| AAPU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +43.0% clears | +43.0% clears | PASS |  |  |
| ABBV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $286.20 / RS 1.20 | $286.20 / RS 1.20 | PASS |  |  |
| ABBV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.20 | 1.20 | PASS |  |  |
| ABBV | RS2 | Stock 52W Return and S&P 52W Return | +28.5% / +7.0% | +28.5% / +7.0% | PASS |  |  |
| ABBV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ABBV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 66 | 66 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ABBV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market | Ahead of the market | PASS |  |  |
| ABBV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.5% clears | +28.5% clears | PASS |  |  |
| AIPO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $20.43 / RS 0.89 | $20.43 / RS 0.88 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| AIPO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.88 | PASS |  |  |
| AIPO | RS2 | Stock 52W Return and S&P 52W Return | -5.3% / +7.0% | -5.3% / +7.0% | PASS |  |  |
| AIPO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AIPO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AIPO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| AIPO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.3% negative | -5.3% negative | PASS |  |  |
| ALAB | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $180.35 / RS 1.21 | $180.35 / RS 1.21 | PASS |  |  |
| ALAB | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.21 | 1.21 | PASS |  |  |
| ALAB | RS2 | Stock 52W Return and S&P 52W Return | +29.5% / +7.0% | +29.5% / +7.0% | PASS |  |  |
| ALAB | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ALAB | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ALAB | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| ALAB | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.5% clears | +29.5% clears | PASS |  |  |
| AMD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $424.39 / RS 1.93 | $424.39 / RS 1.92 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| AMD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.93 | 1.92 | PASS |  |  |
| AMD | RS2 | Stock 52W Return and S&P 52W Return | +106.0% / +7.0% | +106.0% / +7.0% | PASS |  |  |
| AMD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +106.0% clears | +106.0% clears | PASS |  |  |
| AMD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $10.93 / RS 1.87 | $10.93 / RS 1.87 | PASS |  |  |
| AMD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.87 | 1.87 | PASS |  |  |
| AMD.TO | RS2 | Stock 52W Return and S&P 52W Return | +100.5% / +7.0% | +100.6% / +7.0% | PASS |  |  |
| AMD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +100.5% clears | +100.6% clears | PASS |  |  |
| AMZN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $246.82 / RS 1.06 | $246.82 / RS 1.06 | PASS |  |  |
| AMZN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.06 | 1.06 | PASS |  |  |
| AMZN | RS2 | Stock 52W Return and S&P 52W Return | +13.7% / +7.0% | +13.7% / +7.0% | PASS |  |  |
| AMZN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| AMZN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +13.7% clears | +13.7% clears | PASS |  |  |
| AMZU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $32.16 / RS 0.97 | $32.16 / RS 0.97 | PASS |  |  |
| AMZU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.97 | 0.97 | PASS |  |  |
| AMZU | RS2 | Stock 52W Return and S&P 52W Return | +4.0% / +7.0% | +4.0% / +7.0% | PASS |  |  |
| AMZU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 48 | 48 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| AMZU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.0% under | +4.0% under | PASS |  |  |
| ANET.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $29.87 / RS 1.17 | $29.87 / RS 1.17 | PASS |  |  |
| ANET.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.17 | 1.17 | PASS |  |  |
| ANET.TO | RS2 | Stock 52W Return and S&P 52W Return | +25.3% / +7.0% | +25.3% / +7.0% | PASS |  |  |
| ANET.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ANET.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| ANET.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.3% clears | +25.3% clears | PASS |  |  |
| ASML.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $38.95 / RS 1.32 | $38.95 / RS 1.32 | PASS |  |  |
| ASML.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.32 | 1.32 | PASS |  |  |
| ASML.TO | RS2 | Stock 52W Return and S&P 52W Return | +41.7% / +7.0% | +41.7% / +7.0% | PASS |  |  |
| ASML.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASML.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 76 | 76 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASML.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ASML.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +41.7% clears | +41.7% clears | PASS |  |  |
| ASTL.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $6.15 / RS 1.24 | $6.15 / RS 1.24 | PASS |  |  |
| ASTL.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.24 | 1.24 | PASS |  |  |
| ASTL.TO | RS2 | Stock 52W Return and S&P 52W Return | +33.1% / +7.0% | +33.1% / +7.0% | PASS |  |  |
| ASTL.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASTL.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASTL.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market | Ahead of the market | PASS |  |  |
| ASTL.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +33.1% clears | +33.1% clears | PASS |  |  |
| ATD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $81.72 / RS 1.10 | $81.72 / RS 1.10 | PASS |  |  |
| ATD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.10 | 1.10 | PASS |  |  |
| ATD.TO | RS2 | Stock 52W Return and S&P 52W Return | +18.0% / +7.0% | +18.0% / +7.0% | PASS |  |  |
| ATD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ATD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ATD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| ATD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +18.0% clears | +18.0% clears | PASS |  |  |
| AVGO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $304.41 / RS 0.82 | $304.41 / RS 0.82 | PASS |  |  |
| AVGO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.82 | 0.82 | PASS |  |  |
| AVGO | RS2 | Stock 52W Return and S&P 52W Return | -12.2% / +7.0% | -12.2% / +7.0% | PASS |  |  |
| AVGO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AVGO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 36 | 36 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| AVGO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -12.2% negative | -12.2% negative | PASS |  |  |
| AVGO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $11.53 / RS 0.82 | $11.53 / RS 0.82 | PASS |  |  |
| AVGO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.82 | 0.82 | PASS |  |  |
| AVGO.TO | RS2 | Stock 52W Return and S&P 52W Return | -12.5% / +7.0% | -12.5% / +7.0% | PASS |  |  |
| AVGO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 35 | 35 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| AVGO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -12.5% negative | -12.5% negative | PASS |  |  |
| BDT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $69.45 / RS 2.62 | $69.45 / RS 2.62 | PASS |  |  |
| BDT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.62 | 2.62 | PASS |  |  |
| BDT.TO | RS2 | Stock 52W Return and S&P 52W Return | +180.2% / +7.0% | +180.2% / +7.0% | PASS |  |  |
| BDT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BDT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BDT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| BDT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +180.2% clears | +180.2% clears | PASS |  |  |
| BOTZ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $27.34 / RS 0.78 | $27.34 / RS 0.78 | PASS |  |  |
| BOTZ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.78 | 0.78 | PASS |  |  |
| BOTZ | RS2 | Stock 52W Return and S&P 52W Return | -16.9% / +7.0% | -17.0% / +7.0% | PASS |  |  |
| BOTZ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BOTZ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 32 | 32 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BOTZ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| BOTZ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -16.9% negative | -17.0% negative | PASS |  |  |
| BRK-B | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $570.00 / RS 1.06 | $570.00 / RS 1.06 | PASS |  |  |
| BRK-B | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.06 | 1.06 | PASS |  |  |
| BRK-B | RS2 | Stock 52W Return and S&P 52W Return | +13.8% / +7.0% | +13.7% / +7.0% | PASS |  |  |
| BRK-B | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRK-B | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRK-B | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRK-B | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +13.8% clears | +13.7% clears | PASS |  |  |
| BRKU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $28.45 / RS 1.08 | $28.45 / RS 1.08 | PASS |  |  |
| BRKU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.08 | 1.08 | PASS |  |  |
| BRKU | RS2 | Stock 52W Return and S&P 52W Return | +15.2% / +7.0% | +15.2% / +7.0% | PASS |  |  |
| BRKU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRKU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRKU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRKU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +15.2% clears | +15.2% clears | PASS |  |  |
| CAMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $89.20 / RS 0.88 | $89.20 / RS 0.88 | PASS |  |  |
| CAMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| CAMT | RS2 | Stock 52W Return and S&P 52W Return | -5.7% / +7.0% | -5.7% / +7.0% | PASS |  |  |
| CAMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| CAMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.7% negative | -5.7% negative | PASS |  |  |
| CARS.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $18.07 / RS 0.68 | $18.07 / RS 0.68 | PASS |  |  |
| CARS.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.68 | 0.68 | PASS |  |  |
| CARS.TO | RS2 | Stock 52W Return and S&P 52W Return | -27.3% / +7.0% | -27.3% / +7.0% | PASS |  |  |
| CARS.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CARS.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 24 | 24 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CARS.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CARS.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -27.3% negative | -27.3% negative | PASS |  |  |
| CAT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $510.63 / RS 0.88 | $510.63 / RS 0.88 | PASS |  |  |
| CAT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| CAT | RS2 | Stock 52W Return and S&P 52W Return | -5.7% / +7.0% | -5.7% / +7.0% | PASS |  |  |
| CAT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| CAT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.7% negative | -5.7% negative | PASS |  |  |
| CCO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $83.11 / RS 0.67 | $83.11 / RS 0.67 | PASS |  |  |
| CCO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.67 | 0.67 | PASS |  |  |
| CCO.TO | RS2 | Stock 52W Return and S&P 52W Return | -28.0% / +7.0% | -28.0% / +7.0% | PASS |  |  |
| CCO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CCO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 24 | 24 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CCO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| CCO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -28.0% negative | -28.0% negative | PASS |  |  |
| CEG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $237.41 / RS 0.65 | $237.41 / RS 0.65 | PASS |  |  |
| CEG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.65 | PASS |  |  |
| CEG | RS2 | Stock 52W Return and S&P 52W Return | -30.9% / +7.0% | -30.9% / +7.0% | PASS |  |  |
| CEG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CEG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CEG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CEG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -30.9% negative | -30.9% negative | PASS |  |  |
| CGY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $78.75 / RS 1.60 | $78.75 / RS 1.60 | PASS |  |  |
| CGY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.60 | 1.60 | PASS |  |  |
| CGY.TO | RS2 | Stock 52W Return and S&P 52W Return | +70.8% / +7.0% | +70.8% / +7.0% | PASS |  |  |
| CGY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CGY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 98 | 98 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CGY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CGY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +70.8% clears | +70.8% clears | PASS |  |  |
| CNQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $63.74 / RS 1.30 | $63.74 / RS 1.30 | PASS |  |  |
| CNQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.30 | 1.30 | PASS |  |  |
| CNQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +38.7% / +7.0% | +38.7% / +7.0% | PASS |  |  |
| CNQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CNQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +38.7% clears | +38.7% clears | PASS |  |  |
| CNR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $175.38 / RS 1.29 | $175.38 / RS 1.29 | PASS |  |  |
| CNR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.29 | 1.29 | PASS |  |  |
| CNR.TO | RS2 | Stock 52W Return and S&P 52W Return | +38.3% / +7.0% | +38.3% / +7.0% | PASS |  |  |
| CNR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 73 | 73 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CNR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +38.3% clears | +38.3% clears | PASS |  |  |
| COP | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $136.12 / RS 1.50 | $136.12 / RS 1.50 | PASS |  |  |
| COP | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.50 | 1.50 | PASS |  |  |
| COP | RS2 | Stock 52W Return and S&P 52W Return | +60.1% / +7.0% | +60.1% / +7.0% | PASS |  |  |
| COP | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COP | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 90 | 90 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COP | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| COP | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +60.1% clears | +60.1% clears | PASS |  |  |
| COPP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.49 / RS 0.88 | $39.49 / RS 0.87 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| COPP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.87 | PASS |  |  |
| COPP.TO | RS2 | Stock 52W Return and S&P 52W Return | -6.4% / +7.0% | -6.4% / +7.0% | PASS |  |  |
| COPP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| COPP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -6.4% negative | -6.4% negative | PASS |  |  |
| COPX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $56.33 / RS 0.94 | $56.33 / RS 0.94 | PASS |  |  |
| COPX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| COPX | RS2 | Stock 52W Return and S&P 52W Return | +0.7% / +7.0% | +0.7% / +7.0% | PASS |  |  |
| COPX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| COPX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.7% under | +0.7% under | PASS |  |  |
| COST | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,102.15 / RS 1.15 | $1,102.15 / RS 1.15 | PASS |  |  |
| COST | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| COST | RS2 | Stock 52W Return and S&P 52W Return | +23.4% / +7.0% | +23.4% / +7.0% | PASS |  |  |
| COST | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COST | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COST | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| COST | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +23.4% clears | +23.4% clears | PASS |  |  |
| COTG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $16.69 / RS 1.24 | $16.69 / RS 1.24 | PASS |  |  |
| COTG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.24 | 1.24 | PASS |  |  |
| COTG | RS2 | Stock 52W Return and S&P 52W Return | +32.6% / +7.0% | +32.6% / +7.0% | PASS |  |  |
| COTG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COTG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 69 | 69 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COTG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum accelerating) | Ahead of the market (momentum accelerating) | PASS |  |  |
| COTG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +32.6% clears | +32.6% clears | PASS |  |  |
| CSU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3,096.00 / RS 0.90 | $3,096.00 / RS 0.90 | PASS |  |  |
| CSU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| CSU.TO | RS2 | Stock 52W Return and S&P 52W Return | -3.7% / +7.0% | -3.7% / +7.0% | PASS |  |  |
| CSU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CSU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CSU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -3.7% negative | -3.7% negative | PASS |  |  |
| CVX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $208.37 / RS 1.34 | $208.37 / RS 1.34 | PASS |  |  |
| CVX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.34 | 1.34 | PASS |  |  |
| CVX | RS2 | Stock 52W Return and S&P 52W Return | +43.7% / +7.0% | +43.7% / +7.0% | PASS |  |  |
| CVX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CVX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 77 | 77 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CVX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CVX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +43.7% clears | +43.7% clears | PASS |  |  |
| DRIV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $24.59 / RS 0.84 | $24.59 / RS 0.84 | PASS |  |  |
| DRIV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.84 | 0.84 | PASS |  |  |
| DRIV | RS2 | Stock 52W Return and S&P 52W Return | -10.3% / +7.0% | -10.3% / +7.0% | PASS |  |  |
| DRIV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DRIV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 37 | 37 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DRIV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| DRIV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -10.3% negative | -10.3% negative | PASS |  |  |
| DUK | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $129.78 / RS 1.02 | $129.78 / RS 1.02 | PASS |  |  |
| DUK | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.02 | 1.02 | PASS |  |  |
| DUK | RS2 | Stock 52W Return and S&P 52W Return | +9.6% / +7.0% | +9.6% / +7.0% | PASS |  |  |
| DUK | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DUK | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DUK | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| DUK | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +9.6% clears | +9.6% clears | PASS |  |  |
| ELIL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $36.41 / RS 1.27 | $36.41 / RS 1.27 | PASS |  |  |
| ELIL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.27 | 1.27 | PASS |  |  |
| ELIL | RS2 | Stock 52W Return and S&P 52W Return | +35.9% / +7.0% | +35.9% / +7.0% | PASS |  |  |
| ELIL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ELIL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ELIL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market | Ahead of the market | PASS |  |  |
| ELIL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +35.9% clears | +35.9% clears | PASS |  |  |
| EQIX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $968.44 / RS 1.23 | $968.44 / RS 1.23 | PASS |  |  |
| EQIX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.23 | 1.23 | PASS |  |  |
| EQIX | RS2 | Stock 52W Return and S&P 52W Return | +31.3% / +7.0% | +31.3% / +7.0% | PASS |  |  |
| EQIX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| EQIX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 68 | 68 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| EQIX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| EQIX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +31.3% clears | +31.3% clears | PASS |  |  |
| ETN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $311.33 / RS 0.89 | $311.33 / RS 0.89 | PASS |  |  |
| ETN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| ETN | RS2 | Stock 52W Return and S&P 52W Return | -5.1% / +7.0% | -5.1% / +7.0% | PASS |  |  |
| ETN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ETN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ETN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| ETN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.1% negative | -5.1% negative | PASS |  |  |
| FCX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $45.99 / RS 1.09 | $45.99 / RS 1.09 | PASS |  |  |
| FCX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| FCX | RS2 | Stock 52W Return and S&P 52W Return | +17.1% / +7.0% | +17.1% / +7.0% | PASS |  |  |
| FCX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FCX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FCX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| FCX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +17.1% clears | +17.1% clears | PASS |  |  |
| FINN.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.38 / RS 1.29 | $30.38 / RS 1.29 | PASS |  |  |
| FINN.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.29 | 1.29 | PASS |  |  |
| FINN.NE | RS2 | Stock 52W Return and S&P 52W Return | +38.2% / +7.0% | +38.2% / +7.0% | PASS |  |  |
| FINN.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FINN.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 73 | 73 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FINN.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| FINN.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +38.2% clears | +38.2% clears | PASS |  |  |
| GDX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $68.40 / RS 0.88 | $68.40 / RS 0.88 | PASS |  |  |
| GDX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| GDX | RS2 | Stock 52W Return and S&P 52W Return | -5.6% / +7.0% | -5.6% / +7.0% | PASS |  |  |
| GDX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| GDX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.6% negative | -5.6% negative | PASS |  |  |
| GDXU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $18.20 / RS 0.61 | $18.20 / RS 0.61 | PASS |  |  |
| GDXU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.61 | 0.61 | PASS |  |  |
| GDXU.TO | RS2 | Stock 52W Return and S&P 52W Return | -34.5% / +7.0% | -34.5% / +7.0% | PASS |  |  |
| GDXU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDXU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 19 | 19 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDXU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| GDXU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -34.5% negative | -34.5% negative | PASS |  |  |
| GE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $309.62 / RS 0.99 | $309.62 / RS 1.00 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| GE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.99 | 1.00 | PASS |  |  |
| GE | RS2 | Stock 52W Return and S&P 52W Return | +6.5% / +7.0% | +6.5% / +7.0% | PASS |  |  |
| GE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.5% clears | +6.5% clears | PASS |  |  |
| GEV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $699.33 / RS 1.17 | $699.33 / RS 1.17 | PASS |  |  |
| GEV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.17 | 1.17 | PASS |  |  |
| GEV | RS2 | Stock 52W Return and S&P 52W Return | +25.3% / +7.0% | +25.3% / +7.0% | PASS |  |  |
| GEV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GEV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| GEV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.3% clears | +25.3% clears | PASS |  |  |
| GEV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $46.48 / RS 0.96 | $46.48 / RS 0.97 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| GEV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.97 | PASS |  |  |
| GEV.TO | RS2 | Stock 52W Return and S&P 52W Return | +3.3% / +7.0% | +3.3% / +7.0% | PASS |  |  |
| GEV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| GEV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.3% under | +3.3% under | PASS |  |  |
| GGLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $56.59 / RS 0.61 | $56.59 / RS 0.61 | PASS |  |  |
| GGLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.61 | 0.61 | PASS |  |  |
| GGLL | RS2 | Stock 52W Return and S&P 52W Return | -35.1% / +7.0% | -35.1% / +7.0% | PASS |  |  |
| GGLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GGLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 18 | 18 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GGLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| GGLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -35.1% negative | -35.1% negative | PASS |  |  |
| GIB-A.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $113.76 / RS 0.88 | $113.76 / RS 0.88 | PASS |  |  |
| GIB-A.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| GIB-A.TO | RS2 | Stock 52W Return and S&P 52W Return | -5.6% / +7.0% | -5.6% / +7.0% | PASS |  |  |
| GIB-A.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GIB-A.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GIB-A.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| GIB-A.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.6% negative | -5.6% negative | PASS |  |  |
| GOOGL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $265.29 / RS 0.86 | $265.29 / RS 0.86 | PASS |  |  |
| GOOGL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.86 | 0.86 | PASS |  |  |
| GOOGL | RS2 | Stock 52W Return and S&P 52W Return | -8.1% / +7.0% | -8.1% / +7.0% | PASS |  |  |
| GOOGL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GOOGL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 39 | 39 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GOOGL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| GOOGL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -8.1% negative | -8.1% negative | PASS |  |  |
| GRID | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $145.44 / RS 0.94 | $145.44 / RS 0.94 | PASS |  |  |
| GRID | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| GRID | RS2 | Stock 52W Return and S&P 52W Return | +0.1% / +7.0% | +0.1% / +7.0% | PASS |  |  |
| GRID | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GRID | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GRID | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GRID | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.1% under | +0.1% under | PASS |  |  |
| HD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $339.10 / RS 0.98 | $339.10 / RS 0.98 | PASS |  |  |
| HD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.98 | 0.98 | PASS |  |  |
| HD | RS2 | Stock 52W Return and S&P 52W Return | +4.9% / +7.0% | +4.9% / +7.0% | PASS |  |  |
| HD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 48 | 48 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| HD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.9% under | +4.9% under | PASS |  |  |
| HURA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $33.89 / RS 0.64 | $33.89 / RS 0.64 | PASS |  |  |
| HURA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.64 | 0.64 | PASS |  |  |
| HURA.TO | RS2 | Stock 52W Return and S&P 52W Return | -31.9% / +7.0% | -31.9% / +7.0% | PASS |  |  |
| HURA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HURA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 21 | 21 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HURA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| HURA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -31.9% negative | -31.9% negative | PASS |  |  |
| HXQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $103.40 / RS 0.99 | $103.40 / RS 0.99 | PASS |  |  |
| HXQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.99 | 0.99 | PASS |  |  |
| HXQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +6.1% / +7.0% | +6.1% / +7.0% | PASS |  |  |
| HXQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HXQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 49 | 49 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HXQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| HXQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.1% clears | +6.1% clears | PASS |  |  |
| JNJ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $270.47 / RS 1.27 | $270.47 / RS 1.27 | PASS |  |  |
| JNJ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.27 | 1.27 | PASS |  |  |
| JNJ | RS2 | Stock 52W Return and S&P 52W Return | +36.2% / +7.0% | +36.2% / +7.0% | PASS |  |  |
| JNJ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JNJ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JNJ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| JNJ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +36.2% clears | +36.2% clears | PASS |  |  |
| JPM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $310.53 / RS 0.99 | $310.53 / RS 0.99 | PASS |  |  |
| JPM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.99 | 0.99 | PASS |  |  |
| JPM | RS2 | Stock 52W Return and S&P 52W Return | +6.1% / +7.0% | +6.1% / +7.0% | PASS |  |  |
| JPM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JPM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 49 | 49 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JPM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| JPM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.1% clears | +6.1% clears | PASS |  |  |
| KEYS | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $261.51 / RS 1.44 | $261.51 / RS 1.44 | PASS |  |  |
| KEYS | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.44 | 1.44 | PASS |  |  |
| KEYS | RS2 | Stock 52W Return and S&P 52W Return | +54.1% / +7.0% | +54.1% / +7.0% | PASS |  |  |
| KEYS | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| KEYS | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 85 | 85 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| KEYS | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| KEYS | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +54.1% clears | +54.1% clears | PASS |  |  |
| LIN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $502.83 / RS 1.17 | $502.83 / RS 1.17 | PASS |  |  |
| LIN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.17 | 1.17 | PASS |  |  |
| LIN | RS2 | Stock 52W Return and S&P 52W Return | +24.8% / +7.0% | +24.8% / +7.0% | PASS |  |  |
| LIN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LIN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 63 | 63 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LIN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| LIN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +24.8% clears | +24.8% clears | PASS |  |  |
| LLY | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,347.11 / RS 1.21 | $1,347.11 / RS 1.21 | PASS |  |  |
| LLY | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.21 | 1.21 | PASS |  |  |
| LLY | RS2 | Stock 52W Return and S&P 52W Return | +29.9% / +7.0% | +29.9% / +7.0% | PASS |  |  |
| LLY | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LLY | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LLY | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market | Ahead of the market | PASS |  |  |
| LLY | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.9% clears | +29.9% clears | PASS |  |  |
| MDA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $36.88 / RS 1.50 | $36.88 / RS 1.50 | PASS |  |  |
| MDA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.50 | 1.50 | PASS |  |  |
| MDA.TO | RS2 | Stock 52W Return and S&P 52W Return | +61.0% / +7.0% | +61.0% / +7.0% | PASS |  |  |
| MDA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MDA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 90 | 90 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MDA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MDA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +61.0% clears | +61.0% clears | PASS |  |  |
| META | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $560.84 / RS 0.89 | $560.84 / RS 0.89 | PASS |  |  |
| META | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| META | RS2 | Stock 52W Return and S&P 52W Return | -4.5% / +7.0% | -4.5% / +7.0% | PASS |  |  |
| META | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| META | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| META | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| META | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.5% negative | -4.5% negative | PASS |  |  |
| METU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $17.61 / RS 0.65 | $17.61 / RS 0.64 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| METU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.64 | PASS |  |  |
| METU | RS2 | Stock 52W Return and S&P 52W Return | -31.0% / +7.0% | -31.0% / +7.0% | PASS |  |  |
| METU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| METU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| METU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| METU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -31.0% negative | -31.0% negative | PASS |  |  |
| MRVL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $122.28 / RS 1.49 | $122.28 / RS 1.49 | PASS |  |  |
| MRVL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.49 | 1.49 | PASS |  |  |
| MRVL | RS2 | Stock 52W Return and S&P 52W Return | +59.7% / +7.0% | +59.7% / +7.0% | PASS |  |  |
| MRVL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MRVL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 89 | 89 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MRVL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MRVL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +59.7% clears | +59.7% clears | PASS |  |  |
| MSFT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $484.52 / RS 0.95 | $484.52 / RS 0.95 | PASS |  |  |
| MSFT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.95 | PASS |  |  |
| MSFT | RS2 | Stock 52W Return and S&P 52W Return | +2.1% / +7.0% | +2.1% / +7.0% | PASS |  |  |
| MSFT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| MSFT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.1% under | +2.1% under | PASS |  |  |
| MSFU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $34.23 / RS 0.79 | $34.23 / RS 0.79 | PASS |  |  |
| MSFU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.79 | 0.79 | PASS |  |  |
| MSFU | RS2 | Stock 52W Return and S&P 52W Return | -15.5% / +7.0% | -15.5% / +7.0% | PASS |  |  |
| MSFU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| MSFU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -15.5% negative | -15.5% negative | PASS |  |  |
| MTRX.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $28.17 / RS 0.89 | $28.17 / RS 0.88 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| MTRX.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.88 | PASS |  |  |
| MTRX.TO | RS2 | Stock 52W Return and S&P 52W Return | -5.3% / +7.0% | -5.3% / +7.0% | PASS |  |  |
| MTRX.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MTRX.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| MTRX.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.3% negative | -5.3% negative | PASS |  |  |
| MU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $25.97 / RS 2.69 | $25.97 / RS 2.69 | PASS |  |  |
| MU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.69 | 2.69 | PASS |  |  |
| MU.TO | RS2 | Stock 52W Return and S&P 52W Return | +188.2% / +7.0% | +188.2% / +7.0% | PASS |  |  |
| MU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +188.2% clears | +188.2% clears | PASS |  |  |
| NEE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $83.45 / RS 0.95 | $83.45 / RS 0.95 | PASS |  |  |
| NEE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.95 | PASS |  |  |
| NEE | RS2 | Stock 52W Return and S&P 52W Return | +1.8% / +7.0% | +1.8% / +7.0% | PASS |  |  |
| NEE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| NEE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +1.8% under | +1.8% under | PASS |  |  |
| NEM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $94.68 / RS 1.09 | $94.68 / RS 1.09 | PASS |  |  |
| NEM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| NEM | RS2 | Stock 52W Return and S&P 52W Return | +16.5% / +7.0% | +16.5% / +7.0% | PASS |  |  |
| NEM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| NEM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +16.5% clears | +16.5% clears | PASS |  |  |
| NFLX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $56.73 / RS 0.50 | $56.73 / RS 0.50 | PASS |  |  |
| NFLX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.50 | 0.50 | PASS |  |  |
| NFLX | RS2 | Stock 52W Return and S&P 52W Return | -46.3% / +7.0% | -46.3% / +7.0% | PASS |  |  |
| NFLX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFLX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 10 | 10 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFLX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFLX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -46.3% negative | -46.3% negative | PASS |  |  |
| NFXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $8.90 / RS 0.21 | $8.90 / RS 0.21 | PASS |  |  |
| NFXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.21 | 0.21 | PASS |  |  |
| NFXL | RS2 | Stock 52W Return and S&P 52W Return | -77.3% / +7.0% | -77.3% / +7.0% | PASS |  |  |
| NFXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -77.3% negative | -77.3% negative | PASS |  |  |
| NTR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $91.71 / RS 1.14 | $91.71 / RS 1.14 | PASS |  |  |
| NTR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.14 | 1.14 | PASS |  |  |
| NTR.TO | RS2 | Stock 52W Return and S&P 52W Return | +22.1% / +7.0% | +22.1% / +7.0% | PASS |  |  |
| NTR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NTR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 61 | 61 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NTR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| NTR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +22.1% clears | +22.1% clears | PASS |  |  |
| NVDA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $125.53 / RS 0.65 | $125.53 / RS 0.65 | PASS |  |  |
| NVDA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.65 | PASS |  |  |
| NVDA | RS2 | Stock 52W Return and S&P 52W Return | -30.5% / +7.0% | -30.5% / +7.0% | PASS |  |  |
| NVDA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -30.5% negative | -30.5% negative | PASS |  |  |
| NVDL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $10.33 / RS 0.34 | $10.33 / RS 0.34 | PASS |  |  |
| NVDL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.34 | 0.34 | PASS |  |  |
| NVDL | RS2 | Stock 52W Return and S&P 52W Return | -63.4% / +7.0% | -63.4% / +7.0% | PASS |  |  |
| NVDL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -63.4% negative | -63.4% negative | PASS |  |  |
| ONTO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $170.16 / RS 1.27 | $170.16 / RS 1.27 | PASS |  |  |
| ONTO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.27 | 1.27 | PASS |  |  |
| ONTO | RS2 | Stock 52W Return and S&P 52W Return | +35.8% / +7.0% | +35.8% / +7.0% | PASS |  |  |
| ONTO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ONTO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ONTO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| ONTO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +35.8% clears | +35.8% clears | PASS |  |  |
| ORCL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $101.19 / RS 0.46 | $101.19 / RS 0.45 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| ORCL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.46 | 0.45 | PASS |  |  |
| ORCL | RS2 | Stock 52W Return and S&P 52W Return | -51.3% / +7.0% | -51.3% / +7.0% | PASS |  |  |
| ORCL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ORCL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 6 | 6 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ORCL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| ORCL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -51.3% negative | -51.3% negative | PASS |  |  |
| PG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $169.46 / RS 1.10 | $169.46 / RS 1.10 | PASS |  |  |
| PG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.10 | 1.10 | PASS |  |  |
| PG | RS2 | Stock 52W Return and S&P 52W Return | +17.6% / +7.0% | +17.6% / +7.0% | PASS |  |  |
| PG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| PG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +17.6% clears | +17.6% clears | PASS |  |  |
| PLD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $122.50 / RS 0.96 | $122.50 / RS 0.96 | PASS |  |  |
| PLD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.96 | PASS |  |  |
| PLD | RS2 | Stock 52W Return and S&P 52W Return | +2.6% / +7.0% | +2.6% / +7.0% | PASS |  |  |
| PLD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PLD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PLD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| PLD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.6% under | +2.6% under | PASS |  |  |
| PNG.V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $2.79 / RS 0.50 | $2.79 / RS 0.50 | PASS |  |  |
| PNG.V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.50 | 0.50 | PASS |  |  |
| PNG.V | RS2 | Stock 52W Return and S&P 52W Return | -46.5% / +7.0% | -46.4% / +7.0% | PASS |  |  |
| PNG.V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PNG.V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 10 | 10 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PNG.V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| PNG.V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -46.5% negative | -46.4% negative | PASS |  |  |
| QCOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $149.94 / RS 0.90 | $149.94 / RS 0.90 | PASS |  |  |
| QCOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| QCOM | RS2 | Stock 52W Return and S&P 52W Return | -4.1% / +7.0% | -4.1% / +7.0% | PASS |  |  |
| QCOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QCOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QCOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| QCOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.1% negative | -4.1% negative | PASS |  |  |
| QPUX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $2.47 / RS 0.05 | $2.47 / RS 0.05 | PASS |  |  |
| QPUX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.05 | 0.05 | PASS |  |  |
| QPUX | RS2 | Stock 52W Return and S&P 52W Return | -94.7% / +7.0% | -94.7% / +7.0% | PASS |  |  |
| QPUX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QPUX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QPUX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| QPUX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -94.7% negative | -94.7% negative | PASS |  |  |
| QTUM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $111.43 / RS 1.05 | $111.43 / RS 1.05 | PASS |  |  |
| QTUM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.05 | 1.05 | PASS |  |  |
| QTUM | RS2 | Stock 52W Return and S&P 52W Return | +12.2% / +7.0% | +12.2% / +7.0% | PASS |  |  |
| QTUM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QTUM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 54 | 54 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QTUM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| QTUM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +12.2% clears | +12.2% clears | PASS |  |  |
| RBOT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $25.00 / RS 0.76 | $25.00 / RS 0.76 | PASS |  |  |
| RBOT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.76 | 0.76 | PASS |  |  |
| RBOT.TO | RS2 | Stock 52W Return and S&P 52W Return | -18.4% / +7.0% | -18.4% / +7.0% | PASS |  |  |
| RBOT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RBOT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 31 | 31 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RBOT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| RBOT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -18.4% negative | -18.4% negative | PASS |  |  |
| RTX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $190.17 / RS 1.04 | $190.17 / RS 1.04 | PASS |  |  |
| RTX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.04 | 1.04 | PASS |  |  |
| RTX | RS2 | Stock 52W Return and S&P 52W Return | +11.7% / +7.0% | +11.7% / +7.0% | PASS |  |  |
| RTX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RTX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 54 | 54 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RTX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| RTX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +11.7% clears | +11.7% clears | PASS |  |  |
| RY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $263.05 / RS 1.21 | $263.05 / RS 1.21 | PASS |  |  |
| RY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.21 | 1.21 | PASS |  |  |
| RY.TO | RS2 | Stock 52W Return and S&P 52W Return | +29.8% / +7.0% | +29.8% / +7.0% | PASS |  |  |
| RY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| RY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.8% clears | +29.8% clears | PASS |  |  |
| SETM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $19.53 / RS 0.73 | $19.53 / RS 0.73 | PASS |  |  |
| SETM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.73 | 0.73 | PASS |  |  |
| SETM | RS2 | Stock 52W Return and S&P 52W Return | -21.9% / +7.0% | -21.9% / +7.0% | PASS |  |  |
| SETM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SETM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 28 | 28 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SETM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| SETM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -21.9% negative | -21.9% negative | PASS |  |  |
| SMH | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $399.51 / RS 1.15 | $399.51 / RS 1.15 | PASS |  |  |
| SMH | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| SMH | RS2 | Stock 52W Return and S&P 52W Return | +23.3% / +7.0% | +23.3% / +7.0% | PASS |  |  |
| SMH | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SMH | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SMH | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SMH | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +23.3% clears | +23.3% clears | PASS |  |  |
| SO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $93.13 / RS 1.01 | $93.13 / RS 1.01 | PASS |  |  |
| SO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.01 | PASS |  |  |
| SO | RS2 | Stock 52W Return and S&P 52W Return | +8.6% / +7.0% | +8.6% / +7.0% | PASS |  |  |
| SO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| SO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +8.6% clears | +8.6% clears | PASS |  |  |
| SOXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.88 / RS 0.94 | $30.88 / RS 0.94 | PASS |  |  |
| SOXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| SOXL | RS2 | Stock 52W Return and S&P 52W Return | +0.3% / +7.0% | +0.3% / +7.0% | PASS |  |  |
| SOXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| SOXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.3% under | +0.3% under | PASS |  |  |
| SOXL.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $7.85 / RS 0.79 | $7.85 / RS 0.79 | PASS |  |  |
| SOXL.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.79 | 0.79 | PASS |  |  |
| SOXL.NE | RS2 | Stock 52W Return and S&P 52W Return | -15.2% / +7.0% | -15.2% / +7.0% | PASS |  |  |
| SOXL.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| SOXL.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -15.2% negative | -15.2% negative | PASS |  |  |
| SOXX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $123.40 / RS 1.29 | $123.40 / RS 1.29 | PASS |  |  |
| SOXX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.29 | 1.29 | PASS |  |  |
| SOXX | RS2 | Stock 52W Return and S&P 52W Return | +38.5% / +7.0% | +38.5% / +7.0% | PASS |  |  |
| SOXX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| SOXX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +38.5% clears | +38.5% clears | PASS |  |  |
| TSLA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $345.82 / RS 0.82 | $345.82 / RS 0.82 | PASS |  |  |
| TSLA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.82 | 0.82 | PASS |  |  |
| TSLA | RS2 | Stock 52W Return and S&P 52W Return | -12.5% / +7.0% | -12.5% / +7.0% | PASS |  |  |
| TSLA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 35 | 35 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| TSLA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -12.5% negative | -12.5% negative | PASS |  |  |
| TSLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $8.07 / RS 0.51 | $8.07 / RS 0.51 | PASS |  |  |
| TSLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.51 | 0.51 | PASS |  |  |
| TSLL | RS2 | Stock 52W Return and S&P 52W Return | -45.8% / +7.0% | -45.8% / +7.0% | PASS |  |  |
| TSLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 11 | 11 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| TSLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -45.8% negative | -45.8% negative | PASS |  |  |
| TSM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $318.71 / RS 1.07 | $318.71 / RS 1.07 | PASS |  |  |
| TSM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.07 | 1.07 | PASS |  |  |
| TSM | RS2 | Stock 52W Return and S&P 52W Return | +14.8% / +7.0% | +14.9% / +7.0% | PASS |  |  |
| TSM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| TSM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.8% clears | +14.9% clears | PASS |  |  |
| UBOT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.74 / RS 0.56 | $12.74 / RS 0.56 | PASS |  |  |
| UBOT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.56 | 0.56 | PASS |  |  |
| UBOT | RS2 | Stock 52W Return and S&P 52W Return | -40.6% / +7.0% | -40.6% / +7.0% | PASS |  |  |
| UBOT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UBOT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 14 | 14 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UBOT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| UBOT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -40.6% negative | -40.6% negative | PASS |  |  |
| UFO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $35.87 / RS 1.07 | $35.87 / RS 1.07 | PASS |  |  |
| UFO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.07 | 1.07 | PASS |  |  |
| UFO | RS2 | Stock 52W Return and S&P 52W Return | +14.5% / +7.0% | +14.5% / +7.0% | PASS |  |  |
| UFO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UFO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UFO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| UFO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.5% clears | +14.5% clears | PASS |  |  |
| URA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $26.82 / RS 0.62 | $26.82 / RS 0.62 | PASS |  |  |
| URA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.62 | 0.62 | PASS |  |  |
| URA | RS2 | Stock 52W Return and S&P 52W Return | -33.4% / +7.0% | -33.4% / +7.0% | PASS |  |  |
| URA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| URA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 20 | 20 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| URA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| URA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -33.4% negative | -33.4% negative | PASS |  |  |
| URAA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $9.08 / RS 0.30 | $9.08 / RS 0.30 | PASS |  |  |
| URAA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.30 | 0.30 | PASS |  |  |
| URAA | RS2 | Stock 52W Return and S&P 52W Return | -67.9% / +7.0% | -67.9% / +7.0% | PASS |  |  |
| URAA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| URAA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| URAA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| URAA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -67.9% negative | -67.9% negative | PASS |  |  |
| V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $401.87 / RS 1.17 | $401.87 / RS 1.17 | PASS |  |  |
| V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.17 | 1.17 | PASS |  |  |
| V | RS2 | Stock 52W Return and S&P 52W Return | +25.1% / +7.0% | +25.1% / +7.0% | PASS |  |  |
| V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.1% clears | +25.1% clears | PASS |  |  |
| VFV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $176.29 / RS 1.01 | $176.29 / RS 1.02 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| VFV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.02 | PASS |  |  |
| VFV.TO | RS2 | Stock 52W Return and S&P 52W Return | +8.7% / +7.0% | +8.7% / +7.0% | PASS |  |  |
| VFV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VFV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VFV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| VFV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +8.7% clears | +8.7% clears | PASS |  |  |
| VRT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $166.24 / RS 0.97 | $166.24 / RS 0.97 | PASS |  |  |
| VRT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.97 | 0.97 | PASS |  |  |
| VRT | RS2 | Stock 52W Return and S&P 52W Return | +4.3% / +7.0% | +4.3% / +7.0% | PASS |  |  |
| VRT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VRT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 48 | 48 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VRT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| VRT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.3% under | +4.3% under | PASS |  |  |
| WELL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $240.34 / RS 1.15 | $240.34 / RS 1.15 | PASS |  |  |
| WELL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| WELL | RS2 | Stock 52W Return and S&P 52W Return | +23.4% / +7.0% | +23.4% / +7.0% | PASS |  |  |
| WELL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WELL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WELL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| WELL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +23.4% clears | +23.4% clears | PASS |  |  |
| WMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $127.95 / RS 1.13 | $127.95 / RS 1.13 | PASS |  |  |
| WMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.13 | 1.13 | PASS |  |  |
| WMT | RS2 | Stock 52W Return and S&P 52W Return | +20.5% / +7.0% | +20.5% / +7.0% | PASS |  |  |
| WMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| WMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +20.5% clears | +20.5% clears | PASS |  |  |
| XCHP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $91.94 / RS 1.31 | $91.94 / RS 1.31 | PASS |  |  |
| XCHP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.31 | 1.31 | PASS |  |  |
| XCHP.TO | RS2 | Stock 52W Return and S&P 52W Return | +40.3% / +7.0% | +40.3% / +7.0% | PASS |  |  |
| XCHP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XCHP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 75 | 75 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XCHP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| XCHP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +40.3% clears | +40.3% clears | PASS |  |  |
| XDRV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $36.31 / RS 0.85 | $36.31 / RS 0.85 | PASS |  |  |
| XDRV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| XDRV.TO | RS2 | Stock 52W Return and S&P 52W Return | -9.4% / +7.0% | -9.4% / +7.0% | PASS |  |  |
| XDRV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XDRV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XDRV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| XDRV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -9.4% negative | -9.4% negative | PASS |  |  |
| XEQT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $41.97 / RS 1.03 | $41.97 / RS 1.03 | PASS |  |  |
| XEQT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| XEQT.TO | RS2 | Stock 52W Return and S&P 52W Return | +10.5% / +7.0% | +10.5% / +7.0% | PASS |  |  |
| XEQT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XEQT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 53 | 53 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XEQT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| XEQT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +10.5% clears | +10.5% clears | PASS |  |  |
| XETM.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $53.16 / RS 0.59 | $53.16 / RS 0.59 | PASS |  |  |
| XETM.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.59 | 0.59 | PASS |  |  |
| XETM.TO | RS2 | Stock 52W Return and S&P 52W Return | -36.9% / +7.0% | -36.9% / +7.0% | PASS |  |  |
| XETM.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 17 | 17 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XETM.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| XETM.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -36.9% negative | -36.9% negative | PASS |  |  |
| XGD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $44.38 / RS 0.94 | $44.38 / RS 0.94 | PASS |  |  |
| XGD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| XGD.TO | RS2 | Stock 52W Return and S&P 52W Return | +0.4% / +7.0% | +0.4% / +7.0% | PASS |  |  |
| XGD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XGD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XGD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| XGD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.4% under | +0.4% under | PASS |  |  |
| XOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $159.97 / RS 1.31 | $159.97 / RS 1.31 | PASS |  |  |
| XOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.31 | 1.31 | PASS |  |  |
| XOM | RS2 | Stock 52W Return and S&P 52W Return | +40.3% / +7.0% | +40.3% / +7.0% | PASS |  |  |
| XOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 75 | 75 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| XOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +40.3% clears | +40.3% clears | PASS |  |  |
| AAPL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $344.01 – $351.46 · 0.4% above · turned here 4× | $344.01 – $351.46 · 0.4% · 4× | PASS |  |  |
| AAPL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AAPL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $334.45 – $338.44 · 1.2% below · turned here 2× | $334.45 – $338.44 · 1.2% · 2× | PASS |  |  |
| AAPL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.1741 | 8.1739 | PASS |  |  |
| AAPL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AAPL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| AAPL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| AAPL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $338.44 | $338.44 | PASS |  |  |
| AAPL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 338.44, nearest zone high 338.44 | equal | PASS |  |  |
| AAPL | TS1c | S5: the Buy on the bar = the Buy in the box | $338.44 | $338.44 | PASS |  |  |
| AAPL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| AAPL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $322.09 -4.8% | $322.09 -4.8% | PASS |  |  |
| AAPL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPL | TS4 | Target = nearest resistance edge and its % from the buy | $344.01 +1.6% | $344.01 +1.6% | PASS |  |  |
| AAPL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| AAPL | TS6 | Risk $ (and reward $ per share) | Risk $16.35 to make $5.57 a share | Risk $16.35 to make $5.57 | PASS |  |  |
| AAPU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $47.65 – $48.94 · 3.8% above · turned here 4× | $47.65 – $48.94 · 3.8% · 4× | PASS |  |  |
| AAPU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AAPU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $45.45 – $46.21 · price is inside this zone · turned here 2× | $45.45 – $46.21 · 0.0% · 2× | PASS |  |  |
| AAPU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1361 | 2.1362 | PASS |  |  |
| AAPU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AAPU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| AAPU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| AAPU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $45.91 | $45.91 | PASS |  |  |
| AAPU | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 45.91, zone 45.45-46.21 | inside the zone | PASS |  |  |
| AAPU | TS1c | S5: the Buy on the bar = the Buy in the box | $45.91 | $45.91 | PASS |  |  |
| AAPU | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 45.91 vs last close 45.91 | Buy <= last close | PASS |  |  |
| AAPU | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AAPU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $41.64 -9.3% | $41.64 -9.3% | PASS |  |  |
| AAPU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPU | TS4 | Target = nearest resistance edge and its % from the buy | $47.65 +3.8% | $47.65 +3.8% | PASS |  |  |
| AAPU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| AAPU | TS6 | Risk $ (and reward $ per share) | Risk $4.27 to make $1.74 a share | Risk $4.27 to make $1.74 | PASS |  |  |
| ABBV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $291.40 · 1.8% above · turned here 1× | $291.40 · 1.8% · 1× | PASS |  |  |
| ABBV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ABBV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $278.01 – $281.07 · 1.8% below · turned here 2× | $278.01 – $281.07 · 1.8% · 2× | PASS |  |  |
| ABBV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.7085 | 6.7085 | PASS |  |  |
| ABBV | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ABBV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| ABBV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| ABBV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $281.07 | $281.07 | PASS |  |  |
| ABBV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 281.07, nearest zone high 281.07 | equal | PASS |  |  |
| ABBV | TS1c | S5: the Buy on the bar = the Buy in the box | $281.07 | $281.07 | PASS |  |  |
| ABBV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% below | 1.8% below | PASS |  |  |
| ABBV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $267.65 -4.8% | $267.65 -4.8% | PASS |  |  |
| ABBV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ABBV | TS4 | Target = nearest resistance edge and its % from the buy | $291.40 +3.7% | $291.40 +3.7% | PASS |  |  |
| ABBV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| ABBV | TS6 | Risk $ (and reward $ per share) | Risk $13.42 to make $10.33 a share | Risk $13.42 to make $10.33 | PASS |  |  |
| AIPO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.65 – $21.23 · 1.1% above · turned here 3× | $20.65 – $21.23 · 1.1% · 3× | PASS |  |  |
| AIPO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| AIPO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| AIPO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.1556 | 1.1558 | PASS |  |  |
| AIPO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| AIPO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| AIPO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| ALAB | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $214.24 · 18.8% above · turned here 1× | $214.24 · 18.8% · 1× | PASS |  |  |
| ALAB | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ALAB | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $177.61 – $192.86 · price is inside this zone · turned here 7× | $177.61 – $192.86 · 0.0% · 7× | PASS |  |  |
| ALAB | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 24.1332 | 24.1328 | PASS |  |  |
| ALAB | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| ALAB | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| ALAB | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| ALAB | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $180.35 | $180.35 | PASS |  |  |
| ALAB | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 180.35, zone 177.61-192.86 | inside the zone | PASS |  |  |
| ALAB | TS1c | S5: the Buy on the bar = the Buy in the box | $180.35 | $180.35 | PASS |  |  |
| ALAB | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 180.35 vs last close 180.35 | Buy <= last close | PASS |  |  |
| ALAB | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| ALAB | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $132.08 -26.8% | $132.08 -26.8% | PASS |  |  |
| ALAB | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ALAB | TS4 | Target = nearest resistance edge and its % from the buy | $214.24 +18.8% | $214.24 +18.8% | PASS |  |  |
| ALAB | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| ALAB | TS6 | Risk $ (and reward $ per share) | Risk $48.27 to make $33.89 a share | Risk $48.27 to make $33.89 | PASS |  |  |
| AMD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $440.50 – $469.22 · 3.8% above · turned here 5× | $440.50 – $469.22 · 3.8% · 5× | PASS |  |  |
| AMD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $393.36 – $437.23 · price is inside this zone · turned here 4× | $393.36 – $437.23 · 0.0% · 4× | PASS |  |  |
| AMD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 45.4074 | 45.4074 | PASS |  |  |
| AMD | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AMD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| AMD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| AMD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $424.39 | $424.39 | PASS |  |  |
| AMD | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 424.39, zone 393.36-437.23 | inside the zone | PASS |  |  |
| AMD | TS1c | S5: the Buy on the bar = the Buy in the box | $424.39 | $424.39 | PASS |  |  |
| AMD | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 424.39 vs last close 424.39 | Buy <= last close | PASS |  |  |
| AMD | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AMD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $333.58 -21.4% | $333.58 -21.4% | PASS |  |  |
| AMD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD | TS4 | Target = nearest resistance edge and its % from the buy | $440.50 +3.8% | $440.50 +3.8% | PASS |  |  |
| AMD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AMD | TS6 | Risk $ (and reward $ per share) | Risk $90.81 to make $16.11 a share | Risk $90.81 to make $16.11 | PASS |  |  |
| AMD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $10.99 – $11.98 · 0.5% above · turned here 6× | $10.99 – $11.98 · 0.5% · 6× | PASS |  |  |
| AMD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $10.23 – $10.37 · 5.1% below · turned here 2× | $10.23 – $10.37 · 5.1% · 2× | PASS |  |  |
| AMD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.1481 | 1.1481 | PASS |  |  |
| AMD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AMD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| AMD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| AMD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $10.37 | $10.37 | PASS |  |  |
| AMD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 10.37, nearest zone high 10.37 | equal | PASS |  |  |
| AMD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $10.37 | $10.37 | PASS |  |  |
| AMD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.1% below | 5.1% below | PASS |  |  |
| AMD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $8.07 -22.1% | $8.07 -22.1% | PASS |  |  |
| AMD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $10.99 +6.0% | $10.99 +6.0% | PASS |  |  |
| AMD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| AMD.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.30 to make $0.62 a share | Risk $2.30 to make $0.62 | PASS |  |  |
| AMZN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $255.19 – $259.49 · 3.4% above · turned here 3× | $255.19 – $259.49 · 3.4% · 3× | PASS |  |  |
| AMZN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $244.30 – $249.71 · price is inside this zone · turned here 5× | $244.30 – $249.71 · 0.0% · 5× | PASS |  |  |
| AMZN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.9688 | 9.9689 | PASS |  |  |
| AMZN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AMZN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| AMZN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| AMZN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $246.82 | $246.82 | PASS |  |  |
| AMZN | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 246.82, zone 244.3-249.71 | inside the zone | PASS |  |  |
| AMZN | TS1c | S5: the Buy on the bar = the Buy in the box | $246.82 | $246.82 | PASS |  |  |
| AMZN | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 246.82 vs last close 246.82 | Buy <= last close | PASS |  |  |
| AMZN | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AMZN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $226.88 -8.1% | $226.88 -8.1% | PASS |  |  |
| AMZN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZN | TS4 | Target = nearest resistance edge and its % from the buy | $255.19 +3.4% | $255.19 +3.4% | PASS |  |  |
| AMZN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| AMZN | TS6 | Risk $ (and reward $ per share) | Risk $19.94 to make $8.37 a share | Risk $19.94 to make $8.37 | PASS |  |  |
| AMZU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.01 – $39.73 · 15.1% above · turned here 9× | $37.01 – $39.73 · 15.1% · 9× | PASS |  |  |
| AMZU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.74 – $32.89 · price is inside this zone · turned here 5× | $31.74 – $32.89 · 0.0% · 5× | PASS |  |  |
| AMZU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.7414 | 2.7407 | PASS |  |  |
| AMZU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AMZU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| AMZU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| AMZU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $32.16 | $32.16 | PASS |  |  |
| AMZU | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 32.16, zone 31.74-32.89 | inside the zone | PASS |  |  |
| AMZU | TS1c | S5: the Buy on the bar = the Buy in the box | $32.16 | $32.16 | PASS |  |  |
| AMZU | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 32.16 vs last close 32.16 | Buy <= last close | PASS |  |  |
| AMZU | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AMZU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $26.68 -17.0% | $26.68 -17.0% | PASS |  |  |
| AMZU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZU | TS4 | Target = nearest resistance edge and its % from the buy | $37.01 +15.1% | $37.01 +15.1% | PASS |  |  |
| AMZU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| AMZU | TS6 | Risk $ (and reward $ per share) | Risk $5.48 to make $4.85 a share | Risk $5.48 to make $4.85 | PASS |  |  |
| ANET.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $31.45 – $33.38 · 5.3% above · turned here 8× | $31.45 – $33.38 · 5.3% · 8× | PASS |  |  |
| ANET.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $29.30 · 1.9% below · turned here 1× | $29.30 · 1.9% · 1× | PASS |  |  |
| ANET.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1514 | 2.1514 | PASS |  |  |
| ANET.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ANET.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ANET.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ANET.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $29.30 | $29.30 | PASS |  |  |
| ANET.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 29.3, nearest zone high 29.3 | equal | PASS |  |  |
| ANET.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $29.30 | $29.30 | PASS |  |  |
| ANET.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.9% below | 1.9% below | PASS |  |  |
| ANET.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $25.00 -14.7% | $25.00 -14.7% | PASS |  |  |
| ANET.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ANET.TO | TS4 | Target = nearest resistance edge and its % from the buy | $31.45 +7.3% | $31.45 +7.3% | PASS |  |  |
| ANET.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| ANET.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.30 to make $2.15 a share | Risk $4.30 to make $2.15 | PASS |  |  |
| ASML.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $40.17 – $40.74 · 3.1% above · turned here 3× | $40.17 – $40.74 · 3.1% · 3× | PASS |  |  |
| ASML.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ASML.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $37.75 – $39.31 · price is inside this zone · turned here 5× | $37.75 – $39.31 · 0.0% · 5× | PASS |  |  |
| ASML.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0163 | 2.0164 | PASS |  |  |
| ASML.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| ASML.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| ASML.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.95 | $38.95 | PASS |  |  |
| ASML.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 38.95, zone 37.75-39.31 | inside the zone | PASS |  |  |
| ASML.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $38.95 | $38.95 | PASS |  |  |
| ASML.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 38.95 vs last close 38.95 | Buy <= last close | PASS |  |  |
| ASML.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| ASML.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $34.92 -10.4% | $34.92 -10.4% | PASS |  |  |
| ASML.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASML.TO | TS4 | Target = nearest resistance edge and its % from the buy | $40.17 +3.1% | $40.17 +3.1% | PASS |  |  |
| ASML.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ASML.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.03 to make $1.22 a share | Risk $4.03 to make $1.22 | PASS |  |  |
| ASTL.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $6.31 – $6.62 · 2.6% above · turned here 11× | $6.31 – $6.62 · 2.6% · 11× | PASS |  |  |
| ASTL.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ASTL.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $5.96 – $6.03 · 2.0% below · turned here 2× | $5.96 – $6.03 · 2.0% · 2× | PASS |  |  |
| ASTL.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4451 | 0.4454 | PASS |  |  |
| ASTL.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ASTL.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ASTL.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ASTL.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $6.03 | $6.03 | PASS |  |  |
| ASTL.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 6.03, nearest zone high 6.03 | equal | PASS |  |  |
| ASTL.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $6.03 | $6.03 | PASS |  |  |
| ASTL.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| ASTL.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $5.14 -14.8% | $5.14 -14.8% | PASS |  |  |
| ASTL.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASTL.TO | TS4 | Target = nearest resistance edge and its % from the buy | $6.31 +4.6% | $6.31 +4.6% | PASS |  |  |
| ASTL.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ASTL.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.89 to make $0.28 a share | Risk $0.89 to make $0.28 | PASS |  |  |
| ATD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $84.02 – $85.29 · 2.8% above · turned here 4× | $84.02 – $85.29 · 2.8% · 4× | PASS |  |  |
| ATD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ATD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $80.76 – $81.40 · 0.4% below · turned here 4× | $80.76 – $81.40 · 0.4% · 4× | PASS |  |  |
| ATD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.8583 | 1.8583 | PASS |  |  |
| ATD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ATD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| ATD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| ATD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $81.40 | $81.40 | PASS |  |  |
| ATD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 81.4, nearest zone high 81.4 | equal | PASS |  |  |
| ATD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $81.40 | $81.40 | PASS |  |  |
| ATD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| ATD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $77.68 -4.6% | $77.68 -4.6% | PASS |  |  |
| ATD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ATD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $84.02 +3.2% | $84.02 +3.2% | PASS |  |  |
| ATD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| ATD.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.72 to make $2.62 a share | Risk $3.72 to make $2.62 | PASS |  |  |
| AVGC | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $16.52 · 16.7% above · turned here 1× | $16.52 · 16.7% · 1× | PASS |  |  |
| AVGC | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $13.71 · 3.1% below · turned here 1× | $13.71 · 3.1% · 1× | PASS |  |  |
| AVGC | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9272 | 1.9272 | PASS |  |  |
| AVGC | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AVGC | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| AVGC | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| AVGC | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $13.71 | $13.71 | PASS |  |  |
| AVGC | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 13.71, nearest zone high 13.71 | equal | PASS |  |  |
| AVGC | TS1c | S5: the Buy on the bar = the Buy in the box | $13.71 | $13.71 | PASS |  |  |
| AVGC | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.1% below | 3.1% below | PASS |  |  |
| AVGC | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $9.86 -28.1% | $9.86 -28.1% | PASS |  |  |
| AVGC | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGC | TS4 | Target = nearest resistance edge and its % from the buy | $16.52 +20.5% | $16.52 +20.5% | PASS |  |  |
| AVGC | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| AVGC | TS6 | Risk $ (and reward $ per share) | Risk $3.85 to make $2.81 a share | Risk $3.85 to make $2.81 | PASS |  |  |
| AVGO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $307.20 – $321.42 · 0.9% above · turned here 4× | $307.20 – $321.42 · 0.9% · 4× | PASS |  |  |
| AVGO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AVGO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $289.77 – $295.30 · 3.0% below · turned here 3× | $289.77 – $295.30 · 3.0% · 3× | PASS |  |  |
| AVGO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 20.0187 | 20.0186 | PASS |  |  |
| AVGO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AVGO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AVGO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AVGO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $295.30 | $295.30 | PASS |  |  |
| AVGO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 295.3, nearest zone high 295.3 | equal | PASS |  |  |
| AVGO | TS1c | S5: the Buy on the bar = the Buy in the box | $295.30 | $295.30 | PASS |  |  |
| AVGO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.0% below | 3.0% below | PASS |  |  |
| AVGO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $255.26 -13.6% | $255.26 -13.6% | PASS |  |  |
| AVGO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO | TS4 | Target = nearest resistance edge and its % from the buy | $307.20 +4.0% | $307.20 +4.0% | PASS |  |  |
| AVGO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| AVGO | TS6 | Risk $ (and reward $ per share) | Risk $40.04 to make $11.90 a share | Risk $40.04 to make $11.90 | PASS |  |  |
| AVGO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $11.77 – $12.11 · 2.1% above · turned here 3× | $11.77 – $12.11 · 2.1% · 3× | PASS |  |  |
| AVGO.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $11.00 – $11.36 · 1.5% below · turned here 3× | $11.00 – $11.36 · 1.5% · 3× | PASS |  |  |
| AVGO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7382 | 0.7381 | PASS |  |  |
| AVGO.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AVGO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AVGO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AVGO.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $11.36 | $11.36 | PASS |  |  |
| AVGO.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 11.36, nearest zone high 11.36 | equal | PASS |  |  |
| AVGO.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $11.36 | $11.36 | PASS |  |  |
| AVGO.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| AVGO.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $9.88 -13.0% | $9.88 -13.0% | PASS |  |  |
| AVGO.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO.TO | TS4 | Target = nearest resistance edge and its % from the buy | $11.77 +3.6% | $11.77 +3.6% | PASS |  |  |
| AVGO.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| AVGO.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.48 to make $0.41 a share | Risk $1.48 to make $0.41 | PASS |  |  |
| BDT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $71.25 · 2.6% above · turned here 1× | $71.25 · 2.6% · 1× | PASS |  |  |
| BDT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| BDT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $66.95 – $67.00 · 3.5% below · turned here 2× | $66.95 – $67.00 · 3.5% · 2× | PASS |  |  |
| BDT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.9754 | 3.9755 | PASS |  |  |
| BDT.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BDT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| BDT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| BDT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $67.00 | $67.00 | PASS |  |  |
| BDT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 67, nearest zone high 67 | equal | PASS |  |  |
| BDT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $67.00 | $67.00 | PASS |  |  |
| BDT.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.5% below | 3.5% below | PASS |  |  |
| BDT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $59.05 -11.9% | $59.05 -11.9% | PASS |  |  |
| BDT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BDT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $71.25 +6.3% | $71.25 +6.3% | PASS |  |  |
| BDT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| BDT.TO | TS6 | Risk $ (and reward $ per share) | Risk $7.95 to make $4.25 a share | Risk $7.95 to make $4.25 | PASS |  |  |
| BOTZ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.53 · 11.7% above · turned here 1× | $30.53 · 11.7% · 1× | PASS |  |  |
| BOTZ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| BOTZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| BOTZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8689 | 0.8690 | PASS |  |  |
| BOTZ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| BOTZ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| BOTZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| BRK-B | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $596.92 · 4.7% above · turned here 1× | $596.92 · 4.7% · 1× | PASS |  |  |
| BRK-B | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Uptrend — between levels | Uptrend — between levels | PASS |  |  |
| BRK-B | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $549.96 · 3.5% below · turned here 1× | $549.96 · 3.5% · 1× | PASS |  |  |
| BRK-B | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.6499 | 9.6499 | PASS |  |  |
| BRK-B | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BRK-B | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| BRK-B | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| BRK-B | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 549.96, nearest zone high 549.96 | equal | PASS |  |  |
| BRK-B | TS1c | S5: the Buy on the bar = the Buy in the box | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.5% below | 3.5% below | PASS |  |  |
| BRK-B | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $530.66 -3.5% | $530.66 -3.5% | PASS |  |  |
| BRK-B | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRK-B | TS4 | Target = nearest resistance edge and its % from the buy | $596.92 +8.5% | $596.92 +8.5% | PASS |  |  |
| BRK-B | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.4 : 1 | 2.4 : 1 | PASS |  |  |
| BRK-B | TS6 | Risk $ (and reward $ per share) | Risk $19.30 to make $46.96 a share | Risk $19.30 to make $46.96 | PASS |  |  |
| BRKU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $31.20 · 9.7% above · turned here 1× | $31.20 · 9.7% · 1× | PASS |  |  |
| BRKU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Uptrend pulling back to support | Uptrend pulling back to support | PASS |  |  |
| BRKU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $26.69 · 6.2% below · turned here 1× | $26.69 · 6.2% · 1× | PASS |  |  |
| BRKU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9237 | 0.9237 | PASS |  |  |
| BRKU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BRKU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| BRKU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| BRKU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $26.69 | $26.69 | PASS |  |  |
| BRKU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 26.69, nearest zone high 26.69 | equal | PASS |  |  |
| BRKU | TS1c | S5: the Buy on the bar = the Buy in the box | $26.69 | $26.69 | PASS |  |  |
| BRKU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.2% below | 6.2% below | PASS |  |  |
| BRKU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $24.84 -6.9% | $24.84 -6.9% | PASS |  |  |
| BRKU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRKU | TS4 | Target = nearest resistance edge and its % from the buy | $31.20 +16.9% | $31.20 +16.9% | PASS |  |  |
| BRKU | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.4 : 1 | 2.4 : 1 | PASS |  |  |
| BRKU | TS6 | Risk $ (and reward $ per share) | Risk $1.85 to make $4.51 a share | Risk $1.85 to make $4.51 | PASS |  |  |
| CAMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $101.39 · 13.7% above · turned here 1× | $101.39 · 13.7% · 1× | PASS |  |  |
| CAMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CAMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $89.13 – $91.91 · price is inside this zone · turned here 2× | $89.13 – $91.91 · 0.0% · 2× | PASS |  |  |
| CAMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.1575 | 8.1575 | PASS |  |  |
| CAMT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| CAMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| CAMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| CAMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $89.20 | $89.20 | PASS |  |  |
| CAMT | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 89.2, zone 89.13-91.91 | inside the zone | PASS |  |  |
| CAMT | TS1c | S5: the Buy on the bar = the Buy in the box | $89.20 | $89.20 | PASS |  |  |
| CAMT | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 89.2 vs last close 89.2 | Buy <= last close | PASS |  |  |
| CAMT | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| CAMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $72.89 -18.3% | $72.89 -18.3% | PASS |  |  |
| CAMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CAMT | TS4 | Target = nearest resistance edge and its % from the buy | $101.39 +13.7% | $101.39 +13.7% | PASS |  |  |
| CAMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| CAMT | TS6 | Risk $ (and reward $ per share) | Risk $16.31 to make $12.19 a share | Risk $16.31 to make $12.19 | PASS |  |  |
| CARS.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.90 · 15.7% above · turned here 1× | $20.90 · 15.7% · 1× | PASS |  |  |
| CARS.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CARS.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CARS.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5436 | 0.5426 | PASS |  |  |
| CARS.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| CARS.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| CARS.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CAT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $532.56 · 4.3% above · turned here 1× | $532.56 · 4.3% · 1× | PASS |  |  |
| CAT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CAT | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CAT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 28.927 | 28.9273 | PASS |  |  |
| CAT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CAT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CAT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CCO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $92.52 · 11.3% above · turned here 1× | $92.52 · 11.3% · 1× | PASS |  |  |
| CCO.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CCO.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CCO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.8345 | 4.8345 | PASS |  |  |
| CCO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| CCO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| CCO.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CEG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $239.77 – $250.17 · 1.0% above · turned here 6× | $239.77 – $250.17 · 1.0% · 6× | PASS |  |  |
| CEG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CEG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $227.93 – $230.95 · 2.7% below · turned here 2× | $227.93 – $230.95 · 2.7% · 2× | PASS |  |  |
| CEG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 13.3014 | 13.3014 | PASS |  |  |
| CEG | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CEG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| CEG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| CEG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $230.95 | $230.95 | PASS |  |  |
| CEG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 230.95, nearest zone high 230.95 | equal | PASS |  |  |
| CEG | TS1c | S5: the Buy on the bar = the Buy in the box | $230.95 | $230.95 | PASS |  |  |
| CEG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| CEG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $204.35 -11.5% | $204.35 -11.5% | PASS |  |  |
| CEG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CEG | TS4 | Target = nearest resistance edge and its % from the buy | $239.77 +3.8% | $239.77 +3.8% | PASS |  |  |
| CEG | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CEG | TS6 | Risk $ (and reward $ per share) | Risk $26.60 to make $8.82 a share | Risk $26.60 to make $8.82 | PASS |  |  |
| CGY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $79.68 · 1.2% above · turned here 1× | $79.68 · 1.2% · 1× | PASS |  |  |
| CGY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CGY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $77.86 · 1.1% below · turned here 1× | $77.86 · 1.1% · 1× | PASS |  |  |
| CGY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5821 | 2.5822 | PASS |  |  |
| CGY.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CGY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CGY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CGY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $77.86 | $77.86 | PASS |  |  |
| CGY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 77.86, nearest zone high 77.86 | equal | PASS |  |  |
| CGY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $77.86 | $77.86 | PASS |  |  |
| CGY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| CGY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $72.70 -6.6% | $72.70 -6.6% | PASS |  |  |
| CGY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CGY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $79.68 +2.3% | $79.68 +2.3% | PASS |  |  |
| CGY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| CGY.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.16 to make $1.82 a share | Risk $5.16 to make $1.82 | PASS |  |  |
| CNQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $64.61 · 1.4% above · turned here 1× | $64.61 · 1.4% · 1× | PASS |  |  |
| CNQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $63.39 · 0.5% below · turned here 1× | $63.39 · 0.5% · 1× | PASS |  |  |
| CNQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0241 | 2.0241 | PASS |  |  |
| CNQ.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CNQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CNQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CNQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $63.39 | $63.39 | PASS |  |  |
| CNQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 63.39, nearest zone high 63.39 | equal | PASS |  |  |
| CNQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $63.39 | $63.39 | PASS |  |  |
| CNQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.5% below | 0.5% below | PASS |  |  |
| CNQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $59.34 -6.4% | $59.34 -6.4% | PASS |  |  |
| CNQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $64.61 +1.9% | $64.61 +1.9% | PASS |  |  |
| CNQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CNQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.05 to make $1.22 a share | Risk $4.05 to make $1.22 | PASS |  |  |
| CNR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $178.49 · 1.8% above · turned here 1× | $178.49 · 1.8% · 1× | PASS |  |  |
| CNR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $172.43 – $172.91 · 1.4% below · turned here 2× | $172.43 – $172.91 · 1.4% · 2× | PASS |  |  |
| CNR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.2638 | 3.2638 | PASS |  |  |
| CNR.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CNR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| CNR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| CNR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $172.91 | $172.91 | PASS |  |  |
| CNR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 172.91, nearest zone high 172.91 | equal | PASS |  |  |
| CNR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $172.91 | $172.91 | PASS |  |  |
| CNR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.4% below | 1.4% below | PASS |  |  |
| CNR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $166.38 -3.8% | $166.38 -3.8% | PASS |  |  |
| CNR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $178.49 +3.2% | $178.49 +3.2% | PASS |  |  |
| CNR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| CNR.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.53 to make $5.58 a share | Risk $6.53 to make $5.58 | PASS |  |  |
| COP | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $140.69 · 3.4% above · turned here 1× | $140.69 · 3.4% · 1× | PASS |  |  |
| COP | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COP | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $133.10 – $134.99 · 0.8% below · turned here 2× | $133.10 – $134.99 · 0.8% · 2× | PASS |  |  |
| COP | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.8716 | 3.8736 | PASS |  |  |
| COP | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COP | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| COP | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| COP | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $134.99 | $134.99 | PASS |  |  |
| COP | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 134.99, nearest zone high 134.99 | equal | PASS |  |  |
| COP | TS1c | S5: the Buy on the bar = the Buy in the box | $134.99 | $134.99 | PASS |  |  |
| COP | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| COP | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $127.25 -5.7% | $127.25 -5.7% | PASS |  |  |
| COP | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COP | TS4 | Target = nearest resistance edge and its % from the buy | $140.69 +4.2% | $140.69 +4.2% | PASS |  |  |
| COP | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| COP | TS6 | Risk $ (and reward $ per share) | Risk $7.74 to make $5.70 a share | Risk $7.74 to make $5.70 | PASS |  |  |
| COPP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $42.17 · 6.8% above · turned here 1× | $42.17 · 6.8% · 1× | PASS |  |  |
| COPP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| COPP.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| COPP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1938 | 2.1937 | PASS |  |  |
| COPP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| COPP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| COPP.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| COPX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $68.26 · 21.2% above · turned here 1× | $68.26 · 21.2% · 1× | PASS |  |  |
| COPX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 0 of 8 trend checks pass · ADX 30.9 | 0 of 8 trend checks pass · ADX 30.9 | PASS |  |  |
| COPX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $55.44 · 1.6% below · turned here 1× | $55.44 · 1.6% · 1× | PASS |  |  |
| COPX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.9315 | 2.9313 | PASS |  |  |
| COPX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COPX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| COPX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| COPX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $55.44 | $55.44 | PASS |  |  |
| COPX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 55.44, nearest zone high 55.44 | equal | PASS |  |  |
| COPX | TS1c | S5: the Buy on the bar = the Buy in the box | $55.44 | $55.44 | PASS |  |  |
| COPX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.6% below | 1.6% below | PASS |  |  |
| COPX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $49.58 -10.6% | $49.58 -10.6% | PASS |  |  |
| COPX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COPX | TS4 | Target = nearest resistance edge and its % from the buy | $68.26 +23.1% | $68.26 +23.1% | PASS |  |  |
| COPX | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.2 : 1 | 2.2 : 1 | PASS |  |  |
| COPX | TS6 | Risk $ (and reward $ per share) | Risk $5.86 to make $12.82 a share | Risk $5.86 to make $12.82 | PASS |  |  |
| COPZ | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| COPZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| COPZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8045 | 0.8051 | PASS |  |  |
| COPZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| COST | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 1.9% below $1,123.67 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| COST | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| COST | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 7 of 8 trend checks pass | No resistance within 30% above · 7 of 8 trend checks pass | PASS |  |  |
| COST | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,096.50 · 0.5% below · turned here 1× | $1,096.50 · 0.5% · 1× | PASS |  |  |
| COST | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 19.0753 | 19.0752 | PASS |  |  |
| COST | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COST | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| COST | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| COST | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,096.50 | $1,096.50 | PASS |  |  |
| COST | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1096.5, nearest zone high 1096.5 | equal | PASS |  |  |
| COST | TS1c | S5: the Buy on the bar = the Buy in the box | $1,096.50 | $1,096.50 | PASS |  |  |
| COST | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.5% below | 0.5% below | PASS |  |  |
| COST | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $1,058.35 -3.5% | $1,058.35 -3.5% | PASS |  |  |
| COST | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COST | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 1.9% below the high $1,123.67 | PASS |  |  |
| COST | TS6 | Risk $ (and reward $ per share) | Risk $38.15 a share | Risk $38.15 | PASS |  |  |
| COTG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $17.80 · 6.7% above · turned here 1× | $17.80 · 6.7% · 1× | PASS |  |  |
| COTG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Weakening trend — testing support | Weakening trend — testing support | PASS |  |  |
| COTG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.07 – $16.11 · 3.5% below · turned here 2× | $16.07 – $16.11 · 3.5% · 2× | PASS |  |  |
| COTG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5268 | 0.5267 | PASS |  |  |
| COTG | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COTG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| COTG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| COTG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $16.11 | $16.11 | PASS |  |  |
| COTG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 16.11, nearest zone high 16.11 | equal | PASS |  |  |
| COTG | TS1c | S5: the Buy on the bar = the Buy in the box | $16.11 | $16.11 | PASS |  |  |
| COTG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.5% below | 3.5% below | PASS |  |  |
| COTG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $15.06 -6.5% | $15.06 -6.5% | PASS |  |  |
| COTG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COTG | TS4 | Target = nearest resistance edge and its % from the buy | $17.80 +10.5% | $17.80 +10.5% | PASS |  |  |
| COTG | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.6 : 1 | 1.6 : 1 | PASS |  |  |
| COTG | TS6 | Risk $ (and reward $ per share) | Risk $1.05 to make $1.69 a share | Risk $1.05 to make $1.69 | PASS |  |  |
| CSU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3,118.74 – $3,227.61 · 0.7% above · turned here 6× | $3,118.74 – $3,227.61 · 0.7% · 6× | PASS |  |  |
| CSU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CSU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $2,943.64 – $3,036.94 · 1.9% below · turned here 4× | $2,943.64 – $3,036.94 · 1.9% · 4× | PASS |  |  |
| CSU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 126.0881 | 126.0881 | PASS |  |  |
| CSU.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CSU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| CSU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| CSU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $3,036.94 | $3,036.94 | PASS |  |  |
| CSU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 3036.94, nearest zone high 3036.94 | equal | PASS |  |  |
| CSU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $3,036.94 | $3,036.94 | PASS |  |  |
| CSU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.9% below | 1.9% below | PASS |  |  |
| CSU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $2,784.76 -8.3% | $2,784.76 -8.3% | PASS |  |  |
| CSU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CSU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $3,118.74 +2.7% | $3,118.74 +2.7% | PASS |  |  |
| CSU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CSU.TO | TS6 | Risk $ (and reward $ per share) | Risk $252.18 to make $81.80 a share | Risk $252.18 to make $81.80 | PASS |  |  |
| CVX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $215.99 · 3.7% above · turned here 1× | $215.99 · 3.7% · 1× | PASS |  |  |
| CVX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CVX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $207.26 – $209.18 · price is inside this zone · turned here 2× | $207.26 – $209.18 · 0.0% · 2× | PASS |  |  |
| CVX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.8593 | 4.8592 | PASS |  |  |
| CVX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| CVX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| CVX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| CVX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $208.37 | $208.37 | PASS |  |  |
| CVX | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 208.37, zone 207.26-209.18 | inside the zone | PASS |  |  |
| CVX | TS1c | S5: the Buy on the bar = the Buy in the box | $208.37 | $208.37 | PASS |  |  |
| CVX | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 208.37 vs last close 208.37 | Buy <= last close | PASS |  |  |
| CVX | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| CVX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $198.65 -4.7% | $198.65 -4.7% | PASS |  |  |
| CVX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CVX | TS4 | Target = nearest resistance edge and its % from the buy | $215.99 +3.7% | $215.99 +3.7% | PASS |  |  |
| CVX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| CVX | TS6 | Risk $ (and reward $ per share) | Risk $9.72 to make $7.62 a share | Risk $9.72 to make $7.62 | PASS |  |  |
| DRAL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| DRAL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| DRAL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7887 | 0.7890 | PASS |  |  |
| DRAL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| DRAM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.01 · 10.9% above · turned here 1× | $37.01 · 10.9% · 1× | PASS |  |  |
| DRAM | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| DRAM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.1995 | 3.1995 | PASS |  |  |
| DRAM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| DRAM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| DRAM | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| DRIV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $26.87 · 9.3% above · turned here 1× | $26.87 · 9.3% · 1× | PASS |  |  |
| DRIV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| DRIV | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| DRIV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8466 | 0.8471 | PASS |  |  |
| DRIV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| DRIV | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| DUK | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $130.38 – $131.87 · 0.5% above · turned here 4× | $130.38 – $131.87 · 0.5% · 4× | PASS |  |  |
| DUK | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| DUK | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $129.28 · 0.4% below · turned here 1× | $129.28 · 0.4% · 1× | PASS |  |  |
| DUK | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1903 | 2.1899 | PASS |  |  |
| DUK | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| DUK | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| DUK | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| DUK | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $129.28 | $129.28 | PASS |  |  |
| DUK | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 129.28, nearest zone high 129.28 | equal | PASS |  |  |
| DUK | TS1c | S5: the Buy on the bar = the Buy in the box | $129.28 | $129.28 | PASS |  |  |
| DUK | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| DUK | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $124.90 -3.4% | $124.90 -3.4% | PASS |  |  |
| DUK | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DUK | TS4 | Target = nearest resistance edge and its % from the buy | $130.38 +0.9% | $130.38 +0.9% | PASS |  |  |
| DUK | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| DUK | TS6 | Risk $ (and reward $ per share) | Risk $4.38 to make $1.10 a share | Risk $4.38 to make $1.10 | PASS |  |  |
| ELIL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| ELIL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| ELIL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.02 – $35.86 · 1.5% below · turned here 2× | $35.02 – $35.86 · 1.5% · 2× | PASS |  |  |
| ELIL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1514 | 2.1520 | PASS |  |  |
| ELIL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ELIL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| ELIL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| ELIL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 35.86, nearest zone high 35.86 | equal | PASS |  |  |
| ELIL | TS1c | S5: the Buy on the bar = the Buy in the box | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| ELIL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.56 -12.0% | $31.56 -12.0% | PASS |  |  |
| ELIL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ELIL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| ELIL | TS6 | Risk $ (and reward $ per share) | Risk $4.30 a share | Risk $4.30 | PASS |  |  |
| EQIX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $1,021.66 – $1,048.61 · 5.5% above · turned here 7× | $1,021.66 – $1,048.61 · 5.5% · 7× | PASS |  |  |
| EQIX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| EQIX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $962.94 – $997.14 · price is inside this zone · turned here 9× | $962.94 – $997.14 · 0.0% · 9× | PASS |  |  |
| EQIX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 34.4721 | 34.4723 | PASS |  |  |
| EQIX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| EQIX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| EQIX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| EQIX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $968.44 | $968.44 | PASS |  |  |
| EQIX | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 968.44, zone 962.94-997.14 | inside the zone | PASS |  |  |
| EQIX | TS1c | S5: the Buy on the bar = the Buy in the box | $968.44 | $968.44 | PASS |  |  |
| EQIX | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 968.44 vs last close 968.44 | Buy <= last close | PASS |  |  |
| EQIX | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| EQIX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $899.50 -7.1% | $899.50 -7.1% | PASS |  |  |
| EQIX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| EQIX | TS4 | Target = nearest resistance edge and its % from the buy | $1,021.66 +5.5% | $1,021.66 +5.5% | PASS |  |  |
| EQIX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| EQIX | TS6 | Risk $ (and reward $ per share) | Risk $68.94 to make $53.22 a share | Risk $68.94 to make $53.22 | PASS |  |  |
| ETN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $311.92 – $327.50 · 0.2% above · turned here 6× | $311.92 – $327.50 · 0.2% · 6× | PASS |  |  |
| ETN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| ETN | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| ETN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.8361 | 17.8363 | PASS |  |  |
| ETN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| ETN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| ETN | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| FCX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $50.19 – $50.45 · 9.1% above · turned here 2× | $50.19 – $50.45 · 9.1% · 2× | PASS |  |  |
| FCX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 32.5 | 3 of 8 trend checks pass · ADX 32.5 | PASS |  |  |
| FCX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.49 · 16.3% below · turned here 1× | $38.49 · 16.3% · 1× | PASS |  |  |
| FCX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.0515 | 3.0512 | PASS |  |  |
| FCX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| FCX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| FCX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| FCX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.49 | $38.49 | PASS |  |  |
| FCX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 38.49, nearest zone high 38.49 | equal | PASS |  |  |
| FCX | TS1c | S5: the Buy on the bar = the Buy in the box | $38.49 | $38.49 | PASS |  |  |
| FCX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 16.3% below | 16.3% below | PASS |  |  |
| FCX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $32.39 -15.9% | $32.39 -15.9% | PASS |  |  |
| FCX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FCX | TS4 | Target = nearest resistance edge and its % from the buy | $50.19 +30.4% | $50.19 +30.4% | PASS |  |  |
| FCX | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.9 : 1 | 1.9 : 1 | PASS |  |  |
| FCX | TS6 | Risk $ (and reward $ per share) | Risk $6.10 to make $11.70 a share | Risk $6.10 to make $11.70 | PASS |  |  |
| FINN.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.41 – $30.55 · 0.1% above · turned here 2× | $30.41 – $30.55 · 0.1% · 2× | PASS |  |  |
| FINN.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| FINN.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $29.56 · 2.7% below · turned here 1× | $29.56 · 2.7% · 1× | PASS |  |  |
| FINN.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7673 | 0.7673 | PASS |  |  |
| FINN.NE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| FINN.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| FINN.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| FINN.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $29.56 | $29.56 | PASS |  |  |
| FINN.NE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 29.56, nearest zone high 29.56 | equal | PASS |  |  |
| FINN.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $29.56 | $29.56 | PASS |  |  |
| FINN.NE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| FINN.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $28.03 -5.2% | $28.03 -5.2% | PASS |  |  |
| FINN.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FINN.NE | TS4 | Target = nearest resistance edge and its % from the buy | $30.41 +2.9% | $30.41 +2.9% | PASS |  |  |
| FINN.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| FINN.NE | TS6 | Risk $ (and reward $ per share) | Risk $1.53 to make $0.85 a share | Risk $1.53 to make $0.85 | PASS |  |  |
| GDX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $69.74 · 2.0% above · turned here 1× | $69.74 · 2.0% · 1× | PASS |  |  |
| GDX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| GDX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| GDX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.5995 | 3.5991 | PASS |  |  |
| GDX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| GDX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| GDX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| GDXU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.83 · 14.5% above · turned here 1× | $20.83 · 14.5% · 1× | PASS |  |  |
| GDXU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| GDXU.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| GDXU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.3747 | 2.3747 | PASS |  |  |
| GDXU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| GDXU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| GDXU.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| GE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $319.14 – $321.17 · 3.1% above · turned here 2× | $319.14 – $321.17 · 3.1% · 2× | PASS |  |  |
| GE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $306.80 – $311.00 · price is inside this zone · turned here 4× | $306.80 – $311.00 · 0.0% · 4× | PASS |  |  |
| GE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 10.4736 | 10.4732 | PASS |  |  |
| GE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| GE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| GE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| GE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $309.62 | $309.62 | PASS |  |  |
| GE | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 309.62, zone 306.8-311 | inside the zone | PASS |  |  |
| GE | TS1c | S5: the Buy on the bar = the Buy in the box | $309.62 | $309.62 | PASS |  |  |
| GE | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 309.62 vs last close 309.62 | Buy <= last close | PASS |  |  |
| GE | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| GE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $288.67 -6.8% | $288.67 -6.8% | PASS |  |  |
| GE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GE | TS4 | Target = nearest resistance edge and its % from the buy | $319.14 +3.1% | $319.14 +3.1% | PASS |  |  |
| GE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| GE | TS6 | Risk $ (and reward $ per share) | Risk $20.95 to make $9.52 a share | Risk $20.95 to make $9.52 | PASS |  |  |
| GEV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $731.00 – $747.00 · 4.5% above · turned here 2× | $731.00 – $747.00 · 4.5% · 2× | PASS |  |  |
| GEV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GEV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $698.74 – $701.00 · price is inside this zone · turned here 2× | $698.74 – $701.00 · 0.0% · 2× | PASS |  |  |
| GEV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 54.3479 | 54.3483 | PASS |  |  |
| GEV | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| GEV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| GEV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| GEV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $699.33 | $699.33 | PASS |  |  |
| GEV | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 699.33, zone 698.74-701 | inside the zone | PASS |  |  |
| GEV | TS1c | S5: the Buy on the bar = the Buy in the box | $699.33 | $699.33 | PASS |  |  |
| GEV | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 699.33 vs last close 699.33 | Buy <= last close | PASS |  |  |
| GEV | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| GEV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $590.63 -15.5% | $590.63 -15.5% | PASS |  |  |
| GEV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV | TS4 | Target = nearest resistance edge and its % from the buy | $731.00 +4.5% | $731.00 +4.5% | PASS |  |  |
| GEV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GEV | TS6 | Risk $ (and reward $ per share) | Risk $108.70 to make $31.67 a share | Risk $108.70 to make $31.67 | PASS |  |  |
| GEV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $47.12 · 1.4% above · turned here 1× | $47.12 · 1.4% · 1× | PASS |  |  |
| GEV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $42.23 · 9.1% below · turned here 1× | $42.23 · 9.1% · 1× | PASS |  |  |
| GEV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.5309 | 3.5305 | PASS |  |  |
| GEV.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GEV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| GEV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $42.23 | $42.23 | PASS |  |  |
| GEV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 42.23, nearest zone high 42.23 | equal | PASS |  |  |
| GEV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $42.23 | $42.23 | PASS |  |  |
| GEV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 9.1% below | 9.1% below | PASS |  |  |
| GEV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $35.17 -16.7% | $35.17 -16.7% | PASS |  |  |
| GEV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $47.12 +11.6% | $47.12 +11.6% | PASS |  |  |
| GEV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| GEV.TO | TS6 | Risk $ (and reward $ per share) | Risk $7.06 to make $4.89 a share | Risk $7.06 to make $4.89 | PASS |  |  |
| GGLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $62.13 · 9.8% above · turned here 1× | $62.13 · 9.8% · 1× | PASS |  |  |
| GGLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| GGLL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| GGLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.5082 | 5.5086 | PASS |  |  |
| GGLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| GGLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| GGLL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| GIB-A.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $119.30 · 4.9% above · turned here 1× | $119.30 · 4.9% · 1× | PASS |  |  |
| GIB-A.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Weakening trend — testing support | Weakening trend — testing support | PASS |  |  |
| GIB-A.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.35 · 3.9% below · turned here 1× | $109.35 · 3.9% · 1× | PASS |  |  |
| GIB-A.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.7334 | 2.7334 | PASS |  |  |
| GIB-A.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GIB-A.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| GIB-A.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| GIB-A.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.35, nearest zone high 109.35 | equal | PASS |  |  |
| GIB-A.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.9% below | 3.9% below | PASS |  |  |
| GIB-A.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $103.88 -5.0% | $103.88 -5.0% | PASS |  |  |
| GIB-A.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GIB-A.TO | TS4 | Target = nearest resistance edge and its % from the buy | $119.30 +9.1% | $119.30 +9.1% | PASS |  |  |
| GIB-A.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.8 : 1 | 1.8 : 1 | PASS |  |  |
| GIB-A.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.47 to make $9.95 a share | Risk $5.47 to make $9.95 | PASS |  |  |
| GOOGL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $271.77 – $276.92 · 2.4% above · turned here 2× | $271.77 – $276.92 · 2.4% · 2× | PASS |  |  |
| GOOGL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| GOOGL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| GOOGL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 11.314 | 11.3141 | PASS |  |  |
| GOOGL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| GOOGL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| GOOGL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| GRID | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $148.79 · 2.3% above · turned here 1× | $148.79 · 2.3% · 1× | PASS |  |  |
| GRID | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GRID | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $143.36 · 1.4% below · turned here 1× | $143.36 · 1.4% · 1× | PASS |  |  |
| GRID | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.4379 | 4.4379 | PASS |  |  |
| GRID | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GRID | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| GRID | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| GRID | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $143.36 | $143.36 | PASS |  |  |
| GRID | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 143.36, nearest zone high 143.36 | equal | PASS |  |  |
| GRID | TS1c | S5: the Buy on the bar = the Buy in the box | $143.36 | $143.36 | PASS |  |  |
| GRID | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.4% below | 1.4% below | PASS |  |  |
| GRID | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $134.48 -6.2% | $134.48 -6.2% | PASS |  |  |
| GRID | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GRID | TS4 | Target = nearest resistance edge and its % from the buy | $148.79 +3.8% | $148.79 +3.8% | PASS |  |  |
| GRID | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| GRID | TS6 | Risk $ (and reward $ per share) | Risk $8.88 to make $5.43 a share | Risk $8.88 to make $5.43 | PASS |  |  |
| HD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $348.39 – $356.24 · 2.7% above · turned here 5× | $348.39 – $356.24 · 2.7% · 5× | PASS |  |  |
| HD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $328.26 – $336.74 · 0.7% below · turned here 5× | $328.26 – $336.74 · 0.7% · 5× | PASS |  |  |
| HD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.0712 | 9.0712 | PASS |  |  |
| HD | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| HD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| HD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| HD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $336.74 | $336.74 | PASS |  |  |
| HD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 336.74, nearest zone high 336.74 | equal | PASS |  |  |
| HD | TS1c | S5: the Buy on the bar = the Buy in the box | $336.74 | $336.74 | PASS |  |  |
| HD | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| HD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $318.60 -5.4% | $318.60 -5.4% | PASS |  |  |
| HD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HD | TS4 | Target = nearest resistance edge and its % from the buy | $348.39 +3.5% | $348.39 +3.5% | PASS |  |  |
| HD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| HD | TS6 | Risk $ (and reward $ per share) | Risk $18.14 to make $11.65 a share | Risk $18.14 to make $11.65 | PASS |  |  |
| HURA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $36.76 · 8.5% above · turned here 1× | $36.76 · 8.5% · 1× | PASS |  |  |
| HURA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| HURA.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| HURA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.3748 | 1.3748 | PASS |  |  |
| HURA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| HURA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| HURA.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| HXQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $107.31 · 3.8% above · turned here 1× | $107.31 · 3.8% · 1× | PASS |  |  |
| HXQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HXQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $102.93 – $103.13 · 0.3% below · turned here 2× | $102.93 – $103.13 · 0.3% · 2× | PASS |  |  |
| HXQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.0253 | 3.0253 | PASS |  |  |
| HXQ.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| HXQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| HXQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| HXQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $103.13 | $103.13 | PASS |  |  |
| HXQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 103.13, nearest zone high 103.13 | equal | PASS |  |  |
| HXQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $103.13 | $103.13 | PASS |  |  |
| HXQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| HXQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $97.08 -5.9% | $97.08 -5.9% | PASS |  |  |
| HXQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HXQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $107.31 +4.1% | $107.31 +4.1% | PASS |  |  |
| HXQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| HXQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.05 to make $4.18 a share | Risk $6.05 to make $4.18 | PASS |  |  |
| JNJ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $273.55 – $275.23 · 1.1% above · turned here 3× | $273.55 – $275.23 · 1.1% · 3× | PASS |  |  |
| JNJ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JNJ | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $268.11 · 0.9% below · turned here 1× | $268.11 · 0.9% · 1× | PASS |  |  |
| JNJ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.7018 | 6.7018 | PASS |  |  |
| JNJ | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| JNJ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| JNJ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| JNJ | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $268.11 | $268.11 | PASS |  |  |
| JNJ | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 268.11, nearest zone high 268.11 | equal | PASS |  |  |
| JNJ | TS1c | S5: the Buy on the bar = the Buy in the box | $268.11 | $268.11 | PASS |  |  |
| JNJ | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| JNJ | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $254.71 -5.0% | $254.71 -5.0% | PASS |  |  |
| JNJ | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JNJ | TS4 | Target = nearest resistance edge and its % from the buy | $273.55 +2.0% | $273.55 +2.0% | PASS |  |  |
| JNJ | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| JNJ | TS6 | Risk $ (and reward $ per share) | Risk $13.40 to make $5.44 a share | Risk $13.40 to make $5.44 | PASS |  |  |
| JPM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $313.32 – $317.22 · 0.9% above · turned here 3× | $313.32 – $317.22 · 0.9% · 3× | PASS |  |  |
| JPM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JPM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $307.01 · 1.1% below · turned here 1× | $307.01 · 1.1% · 1× | PASS |  |  |
| JPM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.9181 | 7.9181 | PASS |  |  |
| JPM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| JPM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| JPM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| JPM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $307.01 | $307.01 | PASS |  |  |
| JPM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 307.01, nearest zone high 307.01 | equal | PASS |  |  |
| JPM | TS1c | S5: the Buy on the bar = the Buy in the box | $307.01 | $307.01 | PASS |  |  |
| JPM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| JPM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $291.17 -5.2% | $291.17 -5.2% | PASS |  |  |
| JPM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JPM | TS4 | Target = nearest resistance edge and its % from the buy | $313.32 +2.1% | $313.32 +2.1% | PASS |  |  |
| JPM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| JPM | TS6 | Risk $ (and reward $ per share) | Risk $15.84 to make $6.31 a share | Risk $15.84 to make $6.31 | PASS |  |  |
| KEYS | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $275.27 · 5.3% above · turned here 1× | $275.27 · 5.3% · 1× | PASS |  |  |
| KEYS | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| KEYS | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $257.93 – $266.47 · price is inside this zone · turned here 3× | $257.93 – $266.47 · 0.0% · 3× | PASS |  |  |
| KEYS | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.259 | 16.2591 | PASS |  |  |
| KEYS | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| KEYS | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| KEYS | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| KEYS | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $261.51 | $261.51 | PASS |  |  |
| KEYS | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 261.51, zone 257.93-266.47 | inside the zone | PASS |  |  |
| KEYS | TS1c | S5: the Buy on the bar = the Buy in the box | $261.51 | $261.51 | PASS |  |  |
| KEYS | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 261.51 vs last close 261.51 | Buy <= last close | PASS |  |  |
| KEYS | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| KEYS | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $228.99 -12.4% | $228.99 -12.4% | PASS |  |  |
| KEYS | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| KEYS | TS4 | Target = nearest resistance edge and its % from the buy | $275.27 +5.3% | $275.27 +5.3% | PASS |  |  |
| KEYS | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| KEYS | TS6 | Risk $ (and reward $ per share) | Risk $32.52 to make $13.76 a share | Risk $32.52 to make $13.76 | PASS |  |  |
| LIN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $505.12 – $505.96 · 0.5% above · turned here 3× | $505.12 – $505.96 · 0.5% · 3× | PASS |  |  |
| LIN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| LIN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $491.98 – $500.45 · 0.5% below · turned here 5× | $491.98 – $500.45 · 0.5% · 5× | PASS |  |  |
| LIN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.249 | 9.2487 | PASS |  |  |
| LIN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| LIN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| LIN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| LIN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $500.45 | $500.45 | PASS |  |  |
| LIN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 500.45, nearest zone high 500.45 | equal | PASS |  |  |
| LIN | TS1c | S5: the Buy on the bar = the Buy in the box | $500.45 | $500.45 | PASS |  |  |
| LIN | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.5% below | 0.5% below | PASS |  |  |
| LIN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $481.95 -3.7% | $481.95 -3.7% | PASS |  |  |
| LIN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LIN | TS4 | Target = nearest resistance edge and its % from the buy | $505.12 +0.9% | $505.12 +0.9% | PASS |  |  |
| LIN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| LIN | TS6 | Risk $ (and reward $ per share) | Risk $18.50 to make $4.67 a share | Risk $18.50 to make $4.67 | PASS |  |  |
| LLY | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| LLY | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| LLY | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,331.60 · 1.2% below · turned here 1× | $1,331.60 · 1.2% · 1× | PASS |  |  |
| LLY | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 42.3904 | 42.3907 | PASS |  |  |
| LLY | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| LLY | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| LLY | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| LLY | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,331.60 | $1,331.60 | PASS |  |  |
| LLY | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1331.6, nearest zone high 1331.6 | equal | PASS |  |  |
| LLY | TS1c | S5: the Buy on the bar = the Buy in the box | $1,331.60 | $1,331.60 | PASS |  |  |
| LLY | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| LLY | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $1,246.82 -6.4% | $1,246.82 -6.4% | PASS |  |  |
| LLY | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LLY | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| LLY | TS6 | Risk $ (and reward $ per share) | Risk $84.78 a share | Risk $84.78 | PASS |  |  |
| MDA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $38.15 · 3.4% above · turned here 1× | $38.15 · 3.4% · 1× | PASS |  |  |
| MDA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MDA.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.79 – $36.26 · 1.7% below · turned here 2× | $35.79 – $36.26 · 1.7% · 2× | PASS |  |  |
| MDA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2057 | 2.2058 | PASS |  |  |
| MDA.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MDA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| MDA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| MDA.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $36.26 | $36.26 | PASS |  |  |
| MDA.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 36.26, nearest zone high 36.26 | equal | PASS |  |  |
| MDA.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $36.26 | $36.26 | PASS |  |  |
| MDA.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.7% below | 1.7% below | PASS |  |  |
| MDA.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.85 -12.2% | $31.85 -12.2% | PASS |  |  |
| MDA.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MDA.TO | TS4 | Target = nearest resistance edge and its % from the buy | $38.15 +5.2% | $38.15 +5.2% | PASS |  |  |
| MDA.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| MDA.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.41 to make $1.89 a share | Risk $4.41 to make $1.89 | PASS |  |  |
| META | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $576.61 – $598.46 · 2.8% above · turned here 5× | $576.61 – $598.46 · 2.8% · 5× | PASS |  |  |
| META | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| META | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $555.66 – $556.06 · 0.9% below · turned here 2× | $555.66 – $556.06 · 0.9% · 2× | PASS |  |  |
| META | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 23.2728 | 23.2728 | PASS |  |  |
| META | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| META | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| META | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| META | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $556.06 | $556.06 | PASS |  |  |
| META | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 556.06, nearest zone high 556.06 | equal | PASS |  |  |
| META | TS1c | S5: the Buy on the bar = the Buy in the box | $556.06 | $556.06 | PASS |  |  |
| META | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| META | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $509.51 -8.4% | $509.51 -8.4% | PASS |  |  |
| META | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| META | TS4 | Target = nearest resistance edge and its % from the buy | $576.61 +3.7% | $576.61 +3.7% | PASS |  |  |
| META | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| META | TS6 | Risk $ (and reward $ per share) | Risk $46.55 to make $20.55 a share | Risk $46.55 to make $20.55 | PASS |  |  |
| METU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $18.39 – $19.94 · 4.4% above · turned here 5× | $18.39 – $19.94 · 4.4% · 5× | PASS |  |  |
| METU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| METU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.76 – $17.41 · 1.1% below · turned here 2× | $16.76 – $17.41 · 1.1% · 2× | PASS |  |  |
| METU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6882 | 1.6885 | PASS |  |  |
| METU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| METU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| METU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| METU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $17.41 | $17.41 | PASS |  |  |
| METU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 17.41, nearest zone high 17.41 | equal | PASS |  |  |
| METU | TS1c | S5: the Buy on the bar = the Buy in the box | $17.41 | $17.41 | PASS |  |  |
| METU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| METU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $14.03 -19.4% | $14.03 -19.4% | PASS |  |  |
| METU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| METU | TS4 | Target = nearest resistance edge and its % from the buy | $18.39 +5.6% | $18.39 +5.6% | PASS |  |  |
| METU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| METU | TS6 | Risk $ (and reward $ per share) | Risk $3.38 to make $0.98 a share | Risk $3.38 to make $0.98 | PASS |  |  |
| MRVL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $132.54 · 8.4% above · turned here 1× | $132.54 · 8.4% · 1× | PASS |  |  |
| MRVL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MRVL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $94.04 – $102.60 · 16.1% below · turned here 3× | $94.04 – $102.60 · 16.1% · 3× | PASS |  |  |
| MRVL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.0574 | 16.0576 | PASS |  |  |
| MRVL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MRVL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| MRVL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| MRVL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $102.60 | $102.60 | PASS |  |  |
| MRVL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 102.6, nearest zone high 102.6 | equal | PASS |  |  |
| MRVL | TS1c | S5: the Buy on the bar = the Buy in the box | $102.60 | $102.60 | PASS |  |  |
| MRVL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 16.1% below | 16.1% below | PASS |  |  |
| MRVL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $70.49 -31.3% | $70.49 -31.3% | PASS |  |  |
| MRVL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MRVL | TS4 | Target = nearest resistance edge and its % from the buy | $132.54 +29.2% | $132.54 +29.2% | PASS |  |  |
| MRVL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| MRVL | TS6 | Risk $ (and reward $ per share) | Risk $32.11 to make $29.94 a share | Risk $32.11 to make $29.94 | PASS |  |  |
| MSFT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $503.99 – $516.78 · 4.0% above · turned here 3× | $503.99 – $516.78 · 4.0% · 3× | PASS |  |  |
| MSFT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MSFT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $475.34 – $489.44 · price is inside this zone · turned here 6× | $475.34 – $489.44 · 0.0% · 6× | PASS |  |  |
| MSFT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.3819 | 16.3819 | PASS |  |  |
| MSFT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| MSFT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| MSFT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| MSFT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $484.52 | $484.52 | PASS |  |  |
| MSFT | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 484.52, zone 475.34-489.44 | inside the zone | PASS |  |  |
| MSFT | TS1c | S5: the Buy on the bar = the Buy in the box | $484.52 | $484.52 | PASS |  |  |
| MSFT | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 484.52 vs last close 484.52 | Buy <= last close | PASS |  |  |
| MSFT | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| MSFT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $451.76 -6.8% | $451.76 -6.8% | PASS |  |  |
| MSFT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFT | TS4 | Target = nearest resistance edge and its % from the buy | $503.99 +4.0% | $503.99 +4.0% | PASS |  |  |
| MSFT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| MSFT | TS6 | Risk $ (and reward $ per share) | Risk $32.76 to make $19.47 a share | Risk $32.76 to make $19.47 | PASS |  |  |
| MSFU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $34.44 – $36.15 · 0.6% above · turned here 4× | $34.44 – $36.15 · 0.6% · 4× | PASS |  |  |
| MSFU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MSFU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $33.18 · 3.1% below · turned here 1× | $33.18 · 3.1% · 1× | PASS |  |  |
| MSFU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4769 | 2.4770 | PASS |  |  |
| MSFU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MSFU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| MSFU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| MSFU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $33.18 | $33.18 | PASS |  |  |
| MSFU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 33.18, nearest zone high 33.18 | equal | PASS |  |  |
| MSFU | TS1c | S5: the Buy on the bar = the Buy in the box | $33.18 | $33.18 | PASS |  |  |
| MSFU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.1% below | 3.1% below | PASS |  |  |
| MSFU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $28.23 -14.9% | $28.23 -14.9% | PASS |  |  |
| MSFU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFU | TS4 | Target = nearest resistance edge and its % from the buy | $34.44 +3.8% | $34.44 +3.8% | PASS |  |  |
| MSFU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MSFU | TS6 | Risk $ (and reward $ per share) | Risk $4.95 to make $1.26 a share | Risk $4.95 to make $1.26 | PASS |  |  |
| MTRX.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $29.09 – $29.56 · 3.3% above · turned here 4× | $29.09 – $29.56 · 3.3% · 4× | PASS |  |  |
| MTRX.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $28.00 · 0.6% below · turned here 1× | $28.00 · 0.6% · 1× | PASS |  |  |
| MTRX.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9578 | 0.9579 | PASS |  |  |
| MTRX.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MTRX.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| MTRX.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| MTRX.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $28.00 | $28.00 | PASS |  |  |
| MTRX.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 28, nearest zone high 28 | equal | PASS |  |  |
| MTRX.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $28.00 | $28.00 | PASS |  |  |
| MTRX.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.6% below | 0.6% below | PASS |  |  |
| MTRX.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $26.08 -6.8% | $26.08 -6.8% | PASS |  |  |
| MTRX.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MTRX.TO | TS4 | Target = nearest resistance edge and its % from the buy | $29.09 +3.9% | $29.09 +3.9% | PASS |  |  |
| MTRX.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| MTRX.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.92 to make $1.09 a share | Risk $1.92 to make $1.09 | PASS |  |  |
| MU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $28.57 – $28.78 · 10.0% above · turned here 2× | $28.57 – $28.78 · 10.0% · 2× | PASS |  |  |
| MU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $19.41 – $20.92 · 19.4% below · turned here 4× | $19.41 – $20.92 · 19.4% · 4× | PASS |  |  |
| MU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.6694 | 2.6694 | PASS |  |  |
| MU.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| MU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| MU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $20.92 | $20.92 | PASS |  |  |
| MU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 20.92, nearest zone high 20.92 | equal | PASS |  |  |
| MU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $20.92 | $20.92 | PASS |  |  |
| MU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 19.4% below | 19.4% below | PASS |  |  |
| MU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $15.58 -25.5% | $15.58 -25.5% | PASS |  |  |
| MU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $28.57 +36.6% | $28.57 +36.6% | PASS |  |  |
| MU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.4 : 1 | 1.4 : 1 | PASS |  |  |
| MU.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.34 to make $7.65 a share | Risk $5.34 to make $7.65 | PASS |  |  |
| NEE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $84.38 – $85.68 · 1.1% above · turned here 4× | $84.38 – $85.68 · 1.1% · 4× | PASS |  |  |
| NEE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $82.34 – $82.87 · 0.7% below · turned here 3× | $82.34 – $82.87 · 0.7% · 3× | PASS |  |  |
| NEE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6423 | 1.6423 | PASS |  |  |
| NEE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| NEE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| NEE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| NEE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $82.87 | $82.87 | PASS |  |  |
| NEE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 82.87, nearest zone high 82.87 | equal | PASS |  |  |
| NEE | TS1c | S5: the Buy on the bar = the Buy in the box | $82.87 | $82.87 | PASS |  |  |
| NEE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| NEE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $79.59 -4.0% | $79.59 -4.0% | PASS |  |  |
| NEE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEE | TS4 | Target = nearest resistance edge and its % from the buy | $84.38 +1.8% | $84.38 +1.8% | PASS |  |  |
| NEE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| NEE | TS6 | Risk $ (and reward $ per share) | Risk $3.28 to make $1.51 a share | Risk $3.28 to make $1.51 | PASS |  |  |
| NEM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $96.74 – $98.72 · 2.2% above · turned here 4× | $96.74 – $98.72 · 2.2% · 4× | PASS |  |  |
| NEM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $93.92 · 0.8% below · turned here 1× | $93.92 · 0.8% · 1× | PASS |  |  |
| NEM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.9293 | 4.9292 | PASS |  |  |
| NEM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| NEM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| NEM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| NEM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $93.92 | $93.92 | PASS |  |  |
| NEM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 93.92, nearest zone high 93.92 | equal | PASS |  |  |
| NEM | TS1c | S5: the Buy on the bar = the Buy in the box | $93.92 | $93.92 | PASS |  |  |
| NEM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| NEM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $84.06 -10.5% | $84.06 -10.5% | PASS |  |  |
| NEM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEM | TS4 | Target = nearest resistance edge and its % from the buy | $96.74 +3.0% | $96.74 +3.0% | PASS |  |  |
| NEM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| NEM | TS6 | Risk $ (and reward $ per share) | Risk $9.86 to make $2.82 a share | Risk $9.86 to make $2.82 | PASS |  |  |
| NFLX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $61.39 · 8.2% above · turned here 1× | $61.39 · 8.2% · 1× | PASS |  |  |
| NFLX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFLX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFLX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9754 | 1.9752 | PASS |  |  |
| NFLX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| NFLX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| NFLX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NFXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $10.57 · 18.8% above · turned here 1× | $10.57 · 18.8% · 1× | PASS |  |  |
| NFXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFXL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7032 | 0.7034 | PASS |  |  |
| NFXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| NFXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| NFXL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NTR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $94.12 · 2.6% above · turned here 1× | $94.12 · 2.6% · 1× | PASS |  |  |
| NTR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NTR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $90.45 – $93.21 · price is inside this zone · turned here 4× | $90.45 – $93.21 · 0.0% · 4× | PASS |  |  |
| NTR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8844 | 2.8847 | PASS |  |  |
| NTR.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| NTR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| NTR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| NTR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $91.71 | $91.71 | PASS |  |  |
| NTR.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 91.71, zone 90.45-93.21 | inside the zone | PASS |  |  |
| NTR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $91.71 | $91.71 | PASS |  |  |
| NTR.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 91.71 vs last close 91.71 | Buy <= last close | PASS |  |  |
| NTR.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| NTR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $85.94 -6.3% | $85.94 -6.3% | PASS |  |  |
| NTR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NTR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $94.12 +2.6% | $94.12 +2.6% | PASS |  |  |
| NTR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| NTR.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.77 to make $2.41 a share | Risk $5.77 to make $2.41 | PASS |  |  |
| NVDA | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| NVDA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Insufficient data | Insufficient data | PASS |  |  |
| NVDA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 10.7055 | 10.7058 | PASS |  |  |
| NVDA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NVDL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| NVDL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Insufficient data | Insufficient data | PASS |  |  |
| NVDL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5897 | 2.5904 | PASS |  |  |
| NVDL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| ONTO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $171.32 – $188.28 · 0.7% above · turned here 4× | $171.32 – $188.28 · 0.7% · 4× | PASS |  |  |
| ONTO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ONTO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $146.79 – $156.99 · 7.7% below · turned here 3× | $146.79 – $156.99 · 7.7% · 3× | PASS |  |  |
| ONTO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.8006 | 17.8004 | PASS |  |  |
| ONTO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ONTO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| ONTO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| ONTO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $156.99 | $156.99 | PASS |  |  |
| ONTO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 156.99, nearest zone high 156.99 | equal | PASS |  |  |
| ONTO | TS1c | S5: the Buy on the bar = the Buy in the box | $156.99 | $156.99 | PASS |  |  |
| ONTO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.7% below | 7.7% below | PASS |  |  |
| ONTO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $121.39 -22.7% | $121.39 -22.7% | PASS |  |  |
| ONTO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ONTO | TS4 | Target = nearest resistance edge and its % from the buy | $171.32 +9.1% | $171.32 +9.1% | PASS |  |  |
| ONTO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| ONTO | TS6 | Risk $ (and reward $ per share) | Risk $35.60 to make $14.33 a share | Risk $35.60 to make $14.33 | PASS |  |  |
| ORBX.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $15.45 – $15.71 · 7.4% above · turned here 2× | $15.45 – $15.71 · 7.4% · 2× | PASS |  |  |
| ORBX.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $14.29 · 0.7% below · turned here 1× | $14.29 · 0.7% · 1× | PASS |  |  |
| ORBX.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6491 | 0.6491 | PASS |  |  |
| ORBX.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ORBX.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ORBX.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ORBX.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $14.29 | $14.29 | PASS |  |  |
| ORBX.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 14.29, nearest zone high 14.29 | equal | PASS |  |  |
| ORBX.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $14.29 | $14.29 | PASS |  |  |
| ORBX.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| ORBX.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.99 -9.1% | $12.99 -9.1% | PASS |  |  |
| ORBX.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ORBX.TO | TS4 | Target = nearest resistance edge and its % from the buy | $15.45 +8.1% | $15.45 +8.1% | PASS |  |  |
| ORBX.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| ORBX.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.30 to make $1.16 a share | Risk $1.30 to make $1.16 | PASS |  |  |
| ORCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $109.21 · 7.9% above · turned here 1× | $109.21 · 7.9% · 1× | PASS |  |  |
| ORCL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| ORCL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| ORCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.9361 | 7.9362 | PASS |  |  |
| ORCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| ORCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| ORCL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| PG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $170.52 · 0.6% above · turned here 1× | $170.52 · 0.6% · 1× | PASS |  |  |
| PG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| PG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $165.76 · 2.2% below · turned here 1× | $165.76 · 2.2% · 1× | PASS |  |  |
| PG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.2012 | 3.2009 | PASS |  |  |
| PG | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| PG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| PG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| PG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $165.76 | $165.76 | PASS |  |  |
| PG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 165.76, nearest zone high 165.76 | equal | PASS |  |  |
| PG | TS1c | S5: the Buy on the bar = the Buy in the box | $165.76 | $165.76 | PASS |  |  |
| PG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.2% below | 2.2% below | PASS |  |  |
| PG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $159.36 -3.9% | $159.36 -3.9% | PASS |  |  |
| PG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PG | TS4 | Target = nearest resistance edge and its % from the buy | $170.52 +2.9% | $170.52 +2.9% | PASS |  |  |
| PG | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| PG | TS6 | Risk $ (and reward $ per share) | Risk $6.40 to make $4.76 a share | Risk $6.40 to make $4.76 | PASS |  |  |
| PLD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $122.60 – $124.69 · 0.1% above · turned here 6× | $122.60 – $124.69 · 0.1% · 6× | PASS |  |  |
| PLD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| PLD | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| PLD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.515 | 2.5154 | PASS |  |  |
| PLD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| PLD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| PLD | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| PNG.V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3.30 · 18.3% above · turned here 1× | $3.30 · 18.3% · 1× | PASS |  |  |
| PNG.V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| PNG.V | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| PNG.V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.2205 | 0.2208 | PASS |  |  |
| PNG.V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| PNG.V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| PNG.V | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QCOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $155.38 – $155.61 · 3.6% above · turned here 2× | $155.38 – $155.61 · 3.6% · 2× | PASS |  |  |
| QCOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QCOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $142.12 – $148.25 · 1.1% below · turned here 3× | $142.12 – $148.25 · 1.1% · 3× | PASS |  |  |
| QCOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.3414 | 9.3414 | PASS |  |  |
| QCOM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| QCOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| QCOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| QCOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $148.25 | $148.25 | PASS |  |  |
| QCOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 148.25, nearest zone high 148.25 | equal | PASS |  |  |
| QCOM | TS1c | S5: the Buy on the bar = the Buy in the box | $148.25 | $148.25 | PASS |  |  |
| QCOM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| QCOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $129.57 -12.6% | $129.57 -12.6% | PASS |  |  |
| QCOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QCOM | TS4 | Target = nearest resistance edge and its % from the buy | $155.38 +4.8% | $155.38 +4.8% | PASS |  |  |
| QCOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| QCOM | TS6 | Risk $ (and reward $ per share) | Risk $18.68 to make $7.13 a share | Risk $18.68 to make $7.13 | PASS |  |  |
| QPUX | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| QPUX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Insufficient data | Insufficient data | PASS |  |  |
| QPUX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| QPUX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8079 | 0.8081 | PASS |  |  |
| QPUX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QTUM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $111.94 – $115.02 · 0.5% above · turned here 5× | $111.94 – $115.02 · 0.5% · 5× | PASS |  |  |
| QTUM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QTUM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $105.91 – $108.95 · 2.2% below · turned here 4× | $105.91 – $108.95 · 2.2% · 4× | PASS |  |  |
| QTUM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.0875 | 5.0872 | PASS |  |  |
| QTUM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| QTUM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| QTUM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| QTUM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $108.95 | $108.95 | PASS |  |  |
| QTUM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 108.95, nearest zone high 108.95 | equal | PASS |  |  |
| QTUM | TS1c | S5: the Buy on the bar = the Buy in the box | $108.95 | $108.95 | PASS |  |  |
| QTUM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.2% below | 2.2% below | PASS |  |  |
| QTUM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $98.78 -9.3% | $98.78 -9.3% | PASS |  |  |
| QTUM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QTUM | TS4 | Target = nearest resistance edge and its % from the buy | $111.94 +2.7% | $111.94 +2.7% | PASS |  |  |
| QTUM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| QTUM | TS6 | Risk $ (and reward $ per share) | Risk $10.17 to make $2.99 a share | Risk $10.17 to make $2.99 | PASS |  |  |
| RBOT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $28.00 · 12.0% above · turned here 1× | $28.00 · 12.0% · 1× | PASS |  |  |
| RBOT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| RBOT.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| RBOT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.662 | 0.6616 | PASS |  |  |
| RBOT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| RBOT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| RBOT.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| RTX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $191.01 – $193.53 · 0.4% above · turned here 5× | $191.01 – $193.53 · 0.4% · 5× | PASS |  |  |
| RTX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RTX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $184.19 – $189.39 · 0.4% below · turned here 4× | $184.19 – $189.39 · 0.4% · 4× | PASS |  |  |
| RTX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.3749 | 5.3745 | PASS |  |  |
| RTX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| RTX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| RTX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| RTX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $189.39 | $189.39 | PASS |  |  |
| RTX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 189.39, nearest zone high 189.39 | equal | PASS |  |  |
| RTX | TS1c | S5: the Buy on the bar = the Buy in the box | $189.39 | $189.39 | PASS |  |  |
| RTX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| RTX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $178.64 -5.7% | $178.64 -5.7% | PASS |  |  |
| RTX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RTX | TS4 | Target = nearest resistance edge and its % from the buy | $191.01 +0.9% | $191.01 +0.9% | PASS |  |  |
| RTX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| RTX | TS6 | Risk $ (and reward $ per share) | Risk $10.75 to make $1.62 a share | Risk $10.75 to make $1.62 | PASS |  |  |
| RY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $267.28 · 1.6% above · turned here 1× | $267.28 · 1.6% · 1× | PASS |  |  |
| RY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $261.87 · 0.4% below · turned here 1× | $261.87 · 0.4% · 1× | PASS |  |  |
| RY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.1854 | 5.1853 | PASS |  |  |
| RY.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| RY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| RY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| RY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $261.87 | $261.87 | PASS |  |  |
| RY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 261.87, nearest zone high 261.87 | equal | PASS |  |  |
| RY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $261.87 | $261.87 | PASS |  |  |
| RY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| RY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $251.50 -4.0% | $251.50 -4.0% | PASS |  |  |
| RY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $267.28 +2.1% | $267.28 +2.1% | PASS |  |  |
| RY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| RY.TO | TS6 | Risk $ (and reward $ per share) | Risk $10.37 to make $5.41 a share | Risk $10.37 to make $5.41 | PASS |  |  |
| SETM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $23.68 – $23.88 · 21.2% above · turned here 2× | $23.68 – $23.88 · 21.2% · 2× | PASS |  |  |
| SETM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| SETM | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SETM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.0059 | 1.0058 | PASS |  |  |
| SETM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| SETM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| SETM | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SGRD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $17.20 · 2.3% above · turned here 1× | $17.20 · 2.3% · 1× | PASS |  |  |
| SGRD.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SGRD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4131 | 0.4131 | PASS |  |  |
| SGRD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| SGRD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| SGRD.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SMH | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $402.50 – $404.39 · 0.7% above · turned here 2× | $402.50 – $404.39 · 0.7% · 2× | PASS |  |  |
| SMH | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SMH | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $374.16 – $374.43 · 6.3% below · turned here 3× | $374.16 – $374.43 · 6.3% · 3× | PASS |  |  |
| SMH | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 26.1267 | 26.1267 | PASS |  |  |
| SMH | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SMH | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| SMH | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| SMH | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $374.43 | $374.43 | PASS |  |  |
| SMH | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 374.43, nearest zone high 374.43 | equal | PASS |  |  |
| SMH | TS1c | S5: the Buy on the bar = the Buy in the box | $374.43 | $374.43 | PASS |  |  |
| SMH | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.3% below | 6.3% below | PASS |  |  |
| SMH | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $322.18 -14.0% | $322.18 -14.0% | PASS |  |  |
| SMH | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SMH | TS4 | Target = nearest resistance edge and its % from the buy | $402.50 +7.5% | $402.50 +7.5% | PASS |  |  |
| SMH | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| SMH | TS6 | Risk $ (and reward $ per share) | Risk $52.25 to make $28.07 a share | Risk $52.25 to make $28.07 | PASS |  |  |
| SNDK.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $19.52 · 27.8% above · turned here 1× | $19.52 · 27.8% · 1× | PASS |  |  |
| SNDK.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SNDK.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.441 | 2.4410 | PASS |  |  |
| SNDK.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| SNDK.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| SNDK.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $94.94 – $96.09 · 1.9% above · turned here 4× | $94.94 – $96.09 · 1.9% · 4× | PASS |  |  |
| SO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $92.72 – $93.41 · price is inside this zone · turned here 3× | $92.72 – $93.41 · 0.0% · 3× | PASS |  |  |
| SO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.7679 | 1.7689 | PASS |  |  |
| SO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| SO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| SO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| SO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $93.13 | $93.13 | PASS |  |  |
| SO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 93.13, zone 92.72-93.41 | inside the zone | PASS |  |  |
| SO | TS1c | S5: the Buy on the bar = the Buy in the box | $93.13 | $93.13 | PASS |  |  |
| SO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 93.13 vs last close 93.13 | Buy <= last close | PASS |  |  |
| SO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| SO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $89.59 -3.8% | $89.59 -3.8% | PASS |  |  |
| SO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SO | TS4 | Target = nearest resistance edge and its % from the buy | $94.94 +1.9% | $94.94 +1.9% | PASS |  |  |
| SO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| SO | TS6 | Risk $ (and reward $ per share) | Risk $3.54 to make $1.81 a share | Risk $3.54 to make $1.81 | PASS |  |  |
| SOXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $35.68 – $44.50 · 15.5% above · turned here 5× | $35.68 – $44.50 · 15.5% · 5× | PASS |  |  |
| SOXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $28.10 · 9.0% below · turned here 1× | $28.10 · 9.0% · 1× | PASS |  |  |
| SOXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 11.9904 | 11.9904 | PASS |  |  |
| SOXL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SOXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| SOXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| SOXL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $28.10 | $28.10 | PASS |  |  |
| SOXL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 28.1, nearest zone high 28.1 | equal | PASS |  |  |
| SOXL | TS1c | S5: the Buy on the bar = the Buy in the box | $28.10 | $28.10 | PASS |  |  |
| SOXL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 9.0% below | 9.0% below | PASS |  |  |
| SOXL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $4.12 -85.3% | $4.12 -85.3% | PASS |  |  |
| SOXL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL | TS4 | Target = nearest resistance edge and its % from the buy | $35.68 +27.0% | $35.68 +27.0% | PASS |  |  |
| SOXL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| SOXL | TS6 | Risk $ (and reward $ per share) | Risk $23.98 to make $7.58 a share | Risk $23.98 to make $7.58 | PASS |  |  |
| SOXL.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $7.92 · 0.9% above · turned here 1× | $7.92 · 0.9% · 1× | PASS |  |  |
| SOXL.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| SOXL.NE | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SOXL.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.8723 | 1.8722 | PASS |  |  |
| SOXL.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL.NE | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SOXX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $130.75 · 6.0% above · turned here 1× | $130.75 · 6.0% · 1× | PASS |  |  |
| SOXX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $121.06 – $122.73 · 0.5% below · turned here 3× | $121.06 – $122.73 · 0.5% · 3× | PASS |  |  |
| SOXX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.9009 | 8.9011 | PASS |  |  |
| SOXX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SOXX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| SOXX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| SOXX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $122.73 | $122.73 | PASS |  |  |
| SOXX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 122.73, nearest zone high 122.73 | equal | PASS |  |  |
| SOXX | TS1c | S5: the Buy on the bar = the Buy in the box | $122.73 | $122.73 | PASS |  |  |
| SOXX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.5% below | 0.5% below | PASS |  |  |
| SOXX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $104.93 -14.5% | $104.93 -14.5% | PASS |  |  |
| SOXX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXX | TS4 | Target = nearest resistance edge and its % from the buy | $130.75 +6.5% | $130.75 +6.5% | PASS |  |  |
| SOXX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| SOXX | TS6 | Risk $ (and reward $ per share) | Risk $17.80 to make $8.02 a share | Risk $17.80 to make $8.02 | PASS |  |  |
| SPCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $8.20 · 13.1% above · turned here 1× | $8.20 · 13.1% · 1× | PASS |  |  |
| SPCL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SPCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6789 | 1.6789 | PASS |  |  |
| SPCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| SPCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| SPCL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| TSLA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $364.02 – $368.60 · 5.3% above · turned here 3× | $364.02 – $368.60 · 5.3% · 3× | PASS |  |  |
| TSLA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLA | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $337.24 – $354.05 · price is inside this zone · turned here 5× | $337.24 – $354.05 · 0.0% · 5× | PASS |  |  |
| TSLA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.1403 | 17.1405 | PASS |  |  |
| TSLA | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| TSLA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| TSLA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| TSLA | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $345.82 | $345.82 | PASS |  |  |
| TSLA | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 345.82, zone 337.24-354.05 | inside the zone | PASS |  |  |
| TSLA | TS1c | S5: the Buy on the bar = the Buy in the box | $345.82 | $345.82 | PASS |  |  |
| TSLA | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 345.82 vs last close 345.82 | Buy <= last close | PASS |  |  |
| TSLA | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| TSLA | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $311.54 -9.9% | $311.54 -9.9% | PASS |  |  |
| TSLA | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLA | TS4 | Target = nearest resistance edge and its % from the buy | $364.02 +5.3% | $364.02 +5.3% | PASS |  |  |
| TSLA | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| TSLA | TS6 | Risk $ (and reward $ per share) | Risk $34.28 to make $18.20 a share | Risk $34.28 to make $18.20 | PASS |  |  |
| TSLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $8.56 – $9.04 · 6.1% above · turned here 3× | $8.56 – $9.04 · 6.1% · 3× | PASS |  |  |
| TSLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $7.83 · 3.0% below · turned here 1× | $7.83 · 3.0% · 1× | PASS |  |  |
| TSLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8984 | 0.8982 | PASS |  |  |
| TSLL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| TSLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| TSLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| TSLL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $7.83 | $7.83 | PASS |  |  |
| TSLL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 7.83, nearest zone high 7.83 | equal | PASS |  |  |
| TSLL | TS1c | S5: the Buy on the bar = the Buy in the box | $7.83 | $7.83 | PASS |  |  |
| TSLL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.0% below | 3.0% below | PASS |  |  |
| TSLL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $6.03 -22.9% | $6.03 -22.9% | PASS |  |  |
| TSLL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLL | TS4 | Target = nearest resistance edge and its % from the buy | $8.56 +9.3% | $8.56 +9.3% | PASS |  |  |
| TSLL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| TSLL | TS6 | Risk $ (and reward $ per share) | Risk $1.80 to make $0.73 a share | Risk $1.80 to make $0.73 | PASS |  |  |
| TSM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $350.44 – $360.55 · 10.0% above · turned here 4× | $350.44 – $360.55 · 10.0% · 4× | PASS |  |  |
| TSM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $313.80 – $331.92 · price is inside this zone · turned here 5× | $313.80 – $331.92 · 0.0% · 5× | PASS |  |  |
| TSM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 19.0571 | 19.0573 | PASS |  |  |
| TSM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| TSM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| TSM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| TSM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $318.71 | $318.71 | PASS |  |  |
| TSM | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 318.71, zone 313.8-331.92 | inside the zone | PASS |  |  |
| TSM | TS1c | S5: the Buy on the bar = the Buy in the box | $318.71 | $318.71 | PASS |  |  |
| TSM | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 318.71 vs last close 318.71 | Buy <= last close | PASS |  |  |
| TSM | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| TSM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $280.60 -12.0% | $280.60 -12.0% | PASS |  |  |
| TSM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSM | TS4 | Target = nearest resistance edge and its % from the buy | $350.44 +10.0% | $350.44 +10.0% | PASS |  |  |
| TSM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| TSM | TS6 | Risk $ (and reward $ per share) | Risk $38.11 to make $31.73 a share | Risk $38.11 to make $31.73 | PASS |  |  |
| UBOT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $16.00 · 25.6% above · turned here 1× | $16.00 · 25.6% · 1× | PASS |  |  |
| UBOT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| UBOT | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| UBOT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8858 | 0.8866 | PASS |  |  |
| UBOT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| UBOT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| UBOT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| UFO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $36.70 · 2.3% above · turned here 1× | $36.70 · 2.3% · 1× | PASS |  |  |
| UFO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| UFO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.19 · 1.9% below · turned here 1× | $35.19 · 1.9% · 1× | PASS |  |  |
| UFO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.4468 | 1.4471 | PASS |  |  |
| UFO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| UFO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| UFO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| UFO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $35.19 | $35.19 | PASS |  |  |
| UFO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 35.19, nearest zone high 35.19 | equal | PASS |  |  |
| UFO | TS1c | S5: the Buy on the bar = the Buy in the box | $35.19 | $35.19 | PASS |  |  |
| UFO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.9% below | 1.9% below | PASS |  |  |
| UFO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $32.30 -8.2% | $32.30 -8.2% | PASS |  |  |
| UFO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| UFO | TS4 | Target = nearest resistance edge and its % from the buy | $36.70 +4.3% | $36.70 +4.3% | PASS |  |  |
| UFO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| UFO | TS6 | Risk $ (and reward $ per share) | Risk $2.89 to make $1.51 a share | Risk $2.89 to make $1.51 | PASS |  |  |
| URA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.40 · 13.3% above · turned here 1× | $30.40 · 13.3% · 1× | PASS |  |  |
| URA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| URA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| URA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.437 | 1.4373 | PASS |  |  |
| URA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| URA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| URA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| URAA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $11.65 · 28.3% above · turned here 1× | $11.65 · 28.3% · 1× | PASS |  |  |
| URAA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| URAA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| URAA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.1389 | 1.1392 | PASS |  |  |
| URAA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| URAA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| URAA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $413.83 · 3.0% above · turned here 1× | $413.83 · 3.0% · 1× | PASS |  |  |
| V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| V | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $393.27 · 2.1% below · turned here 1× | $393.27 · 2.1% · 1× | PASS |  |  |
| V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.9308 | 8.9297 | PASS |  |  |
| V | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| V | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $393.27 | $393.27 | PASS |  |  |
| V | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 393.27, nearest zone high 393.27 | equal | PASS |  |  |
| V | TS1c | S5: the Buy on the bar = the Buy in the box | $393.27 | $393.27 | PASS |  |  |
| V | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| V | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $375.41 -4.5% | $375.41 -4.5% | PASS |  |  |
| V | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| V | TS4 | Target = nearest resistance edge and its % from the buy | $413.83 +5.2% | $413.83 +5.2% | PASS |  |  |
| V | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| V | TS6 | Risk $ (and reward $ per share) | Risk $17.86 to make $20.56 a share | Risk $17.86 to make $20.56 | PASS |  |  |
| VFV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $178.84 · 1.4% above · turned here 1× | $178.84 · 1.4% · 1× | PASS |  |  |
| VFV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VFV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $171.00 · 3.0% below · turned here 1× | $171.00 · 3.0% · 1× | PASS |  |  |
| VFV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.338 | 3.3379 | PASS |  |  |
| VFV.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| VFV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| VFV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| VFV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $171.00 | $171.00 | PASS |  |  |
| VFV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 171, nearest zone high 171 | equal | PASS |  |  |
| VFV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $171.00 | $171.00 | PASS |  |  |
| VFV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.0% below | 3.0% below | PASS |  |  |
| VFV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $164.32 -3.9% | $164.32 -3.9% | PASS |  |  |
| VFV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VFV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $178.84 +4.6% | $178.84 +4.6% | PASS |  |  |
| VFV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| VFV.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.68 to make $7.84 a share | Risk $6.68 to make $7.84 | PASS |  |  |
| VRT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $170.80 – $172.23 · 2.7% above · turned here 2× | $170.80 – $172.23 · 2.7% · 2× | PASS |  |  |
| VRT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VRT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $158.66 · 4.6% below · turned here 1× | $158.66 · 4.6% · 1× | PASS |  |  |
| VRT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.7749 | 16.7750 | PASS |  |  |
| VRT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| VRT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| VRT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| VRT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $158.66 | $158.66 | PASS |  |  |
| VRT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 158.66, nearest zone high 158.66 | equal | PASS |  |  |
| VRT | TS1c | S5: the Buy on the bar = the Buy in the box | $158.66 | $158.66 | PASS |  |  |
| VRT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.6% below | 4.6% below | PASS |  |  |
| VRT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $125.11 -21.1% | $125.11 -21.1% | PASS |  |  |
| VRT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VRT | TS4 | Target = nearest resistance edge and its % from the buy | $170.80 +7.7% | $170.80 +7.7% | PASS |  |  |
| VRT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| VRT | TS6 | Risk $ (and reward $ per share) | Risk $33.55 to make $12.14 a share | Risk $33.55 to make $12.14 | PASS |  |  |
| WDC.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.20 · 27.6% above · turned here 1× | $20.20 · 27.6% · 1× | PASS |  |  |
| WDC.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $15.70 · 0.8% below · turned here 1× | $15.70 · 0.8% · 1× | PASS |  |  |
| WDC.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.5513 | 1.5513 | PASS |  |  |
| WDC.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| WDC.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| WDC.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| WDC.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 15.7, nearest zone high 15.7 | equal | PASS |  |  |
| WDC.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| WDC.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.60 -19.8% | $12.60 -19.8% | PASS |  |  |
| WDC.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WDC.TO | TS4 | Target = nearest resistance edge and its % from the buy | $20.20 +28.7% | $20.20 +28.7% | PASS |  |  |
| WDC.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.5 : 1 | 1.5 : 1 | PASS |  |  |
| WDC.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.10 to make $4.50 a share | Risk $3.10 to make $4.50 | PASS |  |  |
| WELL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $249.75 · 3.9% above · turned here 1× | $249.75 · 3.9% · 1× | PASS |  |  |
| WELL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WELL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $240.11 – $242.20 · price is inside this zone · turned here 2× | $240.11 – $242.20 · 0.0% · 2× | PASS |  |  |
| WELL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.3611 | 5.3610 | PASS |  |  |
| WELL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| WELL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| WELL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| WELL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $240.34 | $240.34 | PASS |  |  |
| WELL | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 240.34, zone 240.11-242.2 | inside the zone | PASS |  |  |
| WELL | TS1c | S5: the Buy on the bar = the Buy in the box | $240.34 | $240.34 | PASS |  |  |
| WELL | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 240.34 vs last close 240.34 | Buy <= last close | PASS |  |  |
| WELL | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| WELL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $229.62 -4.5% | $229.62 -4.5% | PASS |  |  |
| WELL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WELL | TS4 | Target = nearest resistance edge and its % from the buy | $249.75 +3.9% | $249.75 +3.9% | PASS |  |  |
| WELL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| WELL | TS6 | Risk $ (and reward $ per share) | Risk $10.72 to make $9.41 a share | Risk $10.72 to make $9.41 | PASS |  |  |
| WMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $131.82 – $133.84 · 3.0% above · turned here 4× | $131.82 – $133.84 · 3.0% · 4× | PASS |  |  |
| WMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $127.94 – $129.13 · price is inside this zone · turned here 2× | $127.94 – $129.13 · 0.0% · 2× | PASS |  |  |
| WMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8951 | 2.8951 | PASS |  |  |
| WMT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| WMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| WMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| WMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $127.95 | $127.95 | PASS |  |  |
| WMT | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 127.95, zone 127.94-129.13 | inside the zone | PASS |  |  |
| WMT | TS1c | S5: the Buy on the bar = the Buy in the box | $127.95 | $127.95 | PASS |  |  |
| WMT | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 127.95 vs last close 127.95 | Buy <= last close | PASS |  |  |
| WMT | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| WMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $122.16 -4.5% | $122.16 -4.5% | PASS |  |  |
| WMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WMT | TS4 | Target = nearest resistance edge and its % from the buy | $131.82 +3.0% | $131.82 +3.0% | PASS |  |  |
| WMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| WMT | TS6 | Risk $ (and reward $ per share) | Risk $5.79 to make $3.87 a share | Risk $5.79 to make $3.87 | PASS |  |  |
| XCHP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $95.50 · 3.9% above · turned here 1× | $95.50 · 3.9% · 1× | PASS |  |  |
| XCHP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XCHP.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $81.39 – $87.56 · 4.8% below · turned here 5× | $81.39 – $87.56 · 4.8% · 5× | PASS |  |  |
| XCHP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.5605 | 6.5605 | PASS |  |  |
| XCHP.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XCHP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| XCHP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| XCHP.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $87.56 | $87.56 | PASS |  |  |
| XCHP.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 87.56, nearest zone high 87.56 | equal | PASS |  |  |
| XCHP.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $87.56 | $87.56 | PASS |  |  |
| XCHP.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.8% below | 4.8% below | PASS |  |  |
| XCHP.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $74.44 -15.0% | $74.44 -15.0% | PASS |  |  |
| XCHP.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XCHP.TO | TS4 | Target = nearest resistance edge and its % from the buy | $95.50 +9.1% | $95.50 +9.1% | PASS |  |  |
| XCHP.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| XCHP.TO | TS6 | Risk $ (and reward $ per share) | Risk $13.12 to make $7.94 a share | Risk $13.12 to make $7.94 | PASS |  |  |
| XDRV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $38.62 – $38.88 · 6.4% above · turned here 2× | $38.62 – $38.88 · 6.4% · 2× | PASS |  |  |
| XDRV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| XDRV.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| XDRV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9734 | 0.9734 | PASS |  |  |
| XDRV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| XDRV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| XDRV.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| XEQT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $42.44 – $42.51 · 1.1% above · turned here 2× | $42.44 – $42.51 · 1.1% · 2× | PASS |  |  |
| XEQT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XEQT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $41.87 · 0.2% below · turned here 1× | $41.87 · 0.2% · 1× | PASS |  |  |
| XEQT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6649 | 0.6646 | PASS |  |  |
| XEQT.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XEQT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| XEQT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| XEQT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $41.87 | $41.87 | PASS |  |  |
| XEQT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 41.87, nearest zone high 41.87 | equal | PASS |  |  |
| XEQT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $41.87 | $41.87 | PASS |  |  |
| XEQT.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.2% below | 0.2% below | PASS |  |  |
| XEQT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $40.54 -3.2% | $40.54 -3.2% | PASS |  |  |
| XEQT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XEQT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $42.44 +1.4% | $42.44 +1.4% | PASS |  |  |
| XEQT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| XEQT.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.33 to make $0.57 a share | Risk $1.33 to make $0.57 | PASS |  |  |
| XETM.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $64.70 · 21.7% above · turned here 1× | $64.70 · 21.7% · 1× | PASS |  |  |
| XETM.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| XETM.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5399 | 2.5399 | PASS |  |  |
| XETM.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| XETM.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| XETM.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| XGD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $45.90 – $47.23 · 3.4% above · turned here 4× | $45.90 – $47.23 · 3.4% · 4× | PASS |  |  |
| XGD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XGD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $43.30 – $44.80 · price is inside this zone · turned here 3× | $43.30 – $44.80 · 0.0% · 3× | PASS |  |  |
| XGD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1761 | 2.1761 | PASS |  |  |
| XGD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| XGD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| XGD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| XGD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $44.38 | $44.38 | PASS |  |  |
| XGD.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 44.38, zone 43.3-44.8 | inside the zone | PASS |  |  |
| XGD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $44.38 | $44.38 | PASS |  |  |
| XGD.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 44.38 vs last close 44.38 | Buy <= last close | PASS |  |  |
| XGD.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| XGD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $40.03 -9.8% | $40.03 -9.8% | PASS |  |  |
| XGD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XGD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $45.90 +3.4% | $45.90 +3.4% | PASS |  |  |
| XGD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| XGD.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.35 to make $1.52 a share | Risk $4.35 to make $1.52 | PASS |  |  |
| XOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $161.62 · 1.0% above · turned here 1× | $161.62 · 1.0% · 1× | PASS |  |  |
| XOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $157.07 – $159.11 · 0.5% below · turned here 2× | $157.07 – $159.11 · 0.5% · 2× | PASS |  |  |
| XOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.1934 | 4.1933 | PASS |  |  |
| XOM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| XOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| XOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $159.11 | $159.11 | PASS |  |  |
| XOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 159.11, nearest zone high 159.11 | equal | PASS |  |  |
| XOM | TS1c | S5: the Buy on the bar = the Buy in the box | $159.11 | $159.11 | PASS |  |  |
| XOM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.5% below | 0.5% below | PASS |  |  |
| XOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $150.72 -5.3% | $150.72 -5.3% | PASS |  |  |
| XOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XOM | TS4 | Target = nearest resistance edge and its % from the buy | $161.62 +1.6% | $161.62 +1.6% | PASS |  |  |
| XOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| XOM | TS6 | Risk $ (and reward $ per share) | Risk $8.39 to make $2.51 a share | Risk $8.39 to make $2.51 | PASS |  |  |
