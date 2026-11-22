# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-19T18:07 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 4082 · WRONG 10 (CRITICAL) · MISLEADING 22 (HIGH/LOW per row) · UNVERIFIED 8 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 116 | 2 |
| card-price-data | 232 | 0 |
| card-relative-strength | 428 | 0 |
| card-trade-setup | 881 | 0 |

Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).
Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).
NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AVGC | RS1 | a history of 101 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| COPZ | RS1 | a history of 192 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| DRAL | RS1 | a history of 104 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| DRAM | RS1 | a history of 161 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| ORBX.TO | RS1 | a history of 141 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SGRD.TO | RS1 | a history of 148 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SNDK.TO | RS1 | a history of 135 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SPCL | RS1 | a history of 158 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| WDC.TO | RS1 | a history of 135 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| COP | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | last_close_inside_zone | WRONG | CRITICAL |  |
| ANET.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1M | bars: $1,641,209 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| AVGC | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $59,660.8 | bars: $59,479 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $561,149.45 | bars: $607,009 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $137,465.26 | bars: $89,754 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| DRAL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $936,425.07 | bars: $1,045,487 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| DRIV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $986,535.68 | bars: $1,041,974 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ELIL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.56 / $16.34 | $43.55 / $16.34 | MISLEADING | LOW | one-cent difference: the card rounds the high of the adjusted frame, the audit the 2-dp bars |
| HURA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $437,513.4 | bars: $428,846 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| MTRX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $237,106.89 | bars: $269,609 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ORBX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $85,145.63 | bars: $92,115 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| QPUX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $824,326.36 | bars: $886,564 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| RBOT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $78,425.55 | bars: $85,217 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SGRD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $220,435.09 | bars: $159,278 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SPCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $328,119.66 | bars: $336,848 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| UBOT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $225,955.38 | bars: $230,926 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| URAA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $773,757.55 | bars: $762,013 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| XETM.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $162,951 | bars: $185,137 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ANET.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 228 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| AVGO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 228 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| GEV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 228 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| MTRX.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 210 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| XETM.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 210 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| SO | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| WELL | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ASML.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 8 differ: 37.75-39.31 x5 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| DRIV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 8 differ: 31.32-32.04 x4 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| GEV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 7 differ: 47.12-47.12 x1 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| GRID | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 3 of 12 differ: 173.86-174.04 x2, 176.13-180.17 x6, 181.64-185.4 x6 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| NEE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 13 differ: 83.38-84.38 x4 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| FINN.NE | X1 | cards | 0 bars | at least 60 | UNVERIFIED | INFO | too short to recompute |
| AAPL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $355.11 | $355.11 | PASS |  |  |
| AAPL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.66% | -1.66% | PASS |  |  |
| AAPL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| AAPL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| AAPL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $355.11 · close 1.66% below · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| AAPL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| AAPU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.62 | $49.62 | PASS |  |  |
| AAPU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.91% | -3.91% | PASS |  |  |
| AAPU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.35 | 0.35 | PASS |  |  |
| AAPU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| AAPU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.62 · close 3.91% below · broke out Nov 11 on 0.35× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| AAPU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ABBV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $302.93 | $302.93 | PASS |  |  |
| ABBV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -6.4% | -6.40% | PASS |  |  |
| ABBV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ABBV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ABBV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ABBV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $302.93 · close 6.40% below · Nov 19 close | payload values | PASS |  |  |
| ABBV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AIPO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.38 | $31.38 | PASS |  |  |
| AIPO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.63% | -29.64% | PASS |  |  |
| AIPO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AIPO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AIPO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AIPO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.38 · close 29.63% below · Nov 19 close | payload values | PASS |  |  |
| AIPO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ALAB | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $401.74 | $401.74 | PASS |  |  |
| ALAB | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -47.33% | -47.33% | PASS |  |  |
| ALAB | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ALAB | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ALAB | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ALAB | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $401.74 · close 47.33% below · Nov 19 close | payload values | PASS |  |  |
| ALAB | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $658.52 | $658.52 | PASS |  |  |
| AMD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.71% | -25.71% | PASS |  |  |
| AMD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $658.52 · close 25.71% below · Nov 19 close | payload values | PASS |  |  |
| AMD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.97 | $16.97 | PASS |  |  |
| AMD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.8% | -25.81% | PASS |  |  |
| AMD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.97 · close 25.80% below · Nov 19 close | payload values | PASS |  |  |
| AMD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $273.23 | $273.23 | PASS |  |  |
| AMZN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.8% | -5.80% | PASS |  |  |
| AMZN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $273.23 · close 5.80% below · Nov 19 close | payload values | PASS |  |  |
| AMZN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $40.64 | $40.64 | PASS |  |  |
| AMZU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14% | -14.00% | PASS |  |  |
| AMZU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $40.64 · close 14.00% below · Nov 19 close | payload values | PASS |  |  |
| AMZU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ANET.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.85 | $38.85 | PASS |  |  |
| ANET.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.74% | -12.74% | PASS |  |  |
| ANET.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ANET.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ANET.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ANET.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.85 · close 12.74% below · Nov 19 close | payload values | PASS |  |  |
| ANET.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASML.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $53.94 | $53.94 | PASS |  |  |
| ASML.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.53% | -23.53% | PASS |  |  |
| ASML.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ASML.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ASML.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ASML.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $53.94 · close 23.53% below · Nov 18 close | payload values | PASS |  |  |
| ASML.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $7.71 | $7.71 | PASS |  |  |
| ASTL.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.51% | -10.51% | PASS |  |  |
| ASTL.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-09 | 2026-11-09 | PASS |  |  |
| ASTL.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.67 | 2.67 | PASS |  |  |
| ASTL.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| ASTL.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $7.71 · close 10.51% below · broke out Nov 9 on 2.67× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| ASTL.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ATD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $92.93 | $92.93 | PASS |  |  |
| ATD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.76% | -13.76% | PASS |  |  |
| ATD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ATD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ATD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ATD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $92.93 · close 13.76% below · Nov 19 close | payload values | PASS |  |  |
| ATD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGC | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $30.25 | $30.25 | PASS |  |  |
| AVGC | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.59% | -37.59% | PASS |  |  |
| AVGC | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGC | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGC | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGC | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $30.25 · close 37.59% below · Nov 19 close | payload values | PASS |  |  |
| AVGC | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $424.15 | $424.15 | PASS |  |  |
| AVGO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.3% | -18.30% | PASS |  |  |
| AVGO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $424.15 · close 18.30% below · Nov 19 close | payload values | PASS |  |  |
| AVGO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.22 | $16.22 | PASS |  |  |
| AVGO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.05% | -19.05% | PASS |  |  |
| AVGO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.22 · close 19.05% below · Nov 19 close | payload values | PASS |  |  |
| AVGO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BDT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -17.36% | -17.36% | PASS |  |  |
| BDT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BDT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BDT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BDT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $86.42 · close 17.36% below · Nov 19 close | payload values | PASS |  |  |
| BDT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BOTZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.02 | $38.02 | PASS |  |  |
| BOTZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.73% | -23.72% | PASS |  |  |
| BOTZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BOTZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BOTZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BOTZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.02 · close 23.73% below · Nov 19 close | payload values | PASS |  |  |
| BOTZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $586.3 | $586.30 | PASS |  |  |
| BRK-B | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.43% | -2.43% | PASS |  |  |
| BRK-B | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| BRK-B | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.09 | 1.09 | PASS |  |  |
| BRK-B | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| BRK-B | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $586.30 · close 2.43% below · broke out Nov 11 on 1.09× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| BRK-B | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| BRKU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $30.11 | $30.11 | PASS |  |  |
| BRKU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.18% | -5.18% | PASS |  |  |
| BRKU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| BRKU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.72 | 0.72 | PASS |  |  |
| BRKU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| BRKU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $30.11 · close 5.18% below · broke out Nov 11 on 0.72× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| BRKU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRKU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CAMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $178.02 | $178.02 | PASS |  |  |
| CAMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -45.07% | -45.07% | PASS |  |  |
| CAMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $178.02 · close 45.07% below · Nov 19 close | payload values | PASS |  |  |
| CAMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CARS.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $28.41 | $28.41 | PASS |  |  |
| CARS.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.04% | -30.02% | PASS |  |  |
| CARS.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CARS.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CARS.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CARS.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $28.41 · close 30.04% below · Nov 18 close | payload values | PASS |  |  |
| CARS.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CAT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $885.81 | $885.81 | PASS |  |  |
| CAT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39.35% | -39.35% | PASS |  |  |
| CAT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $885.81 · close 39.35% below · Nov 19 close | payload values | PASS |  |  |
| CAT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CCO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $154.65 | $154.65 | PASS |  |  |
| CCO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.19% | -42.19% | PASS |  |  |
| CCO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CCO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CCO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CCO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $154.65 · close 42.19% below · Nov 18 close | payload values | PASS |  |  |
| CCO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CEG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $309.8 | $309.80 | PASS |  |  |
| CEG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.65% | -18.65% | PASS |  |  |
| CEG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CEG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CEG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CEG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $309.80 · close 18.65% below · Nov 19 close | payload values | PASS |  |  |
| CEG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CGY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.29% | -14.28% | PASS |  |  |
| CGY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CGY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CGY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CGY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $95.15 · close 14.29% below · Nov 19 close | payload values | PASS |  |  |
| CGY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $78.6 | $78.60 | PASS |  |  |
| CNQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.45% | -18.45% | PASS |  |  |
| CNQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CNQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CNQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CNQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $78.60 · close 18.45% below · Nov 19 close | payload values | PASS |  |  |
| CNQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $182.06 | $182.06 | PASS |  |  |
| CNR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.87% | -1.87% | PASS |  |  |
| CNR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CNR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.18 | 1.18 | PASS |  |  |
| CNR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| CNR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $182.06 · close 1.87% below · broke out Nov 16 on 1.18× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| CNR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COP | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $153.27 | $153.27 | PASS |  |  |
| COP | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.93% | -11.93% | PASS |  |  |
| COP | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COP | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COP | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COP | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $153.27 · close 11.93% below · Nov 19 close | payload values | PASS |  |  |
| COP | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $69.02 | $69.02 | PASS |  |  |
| COPP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39.39% | -39.39% | PASS |  |  |
| COPP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $69.02 · close 39.39% below · Nov 19 close | payload values | PASS |  |  |
| COPP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $97.59 | $97.59 | PASS |  |  |
| COPX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39.26% | -39.26% | PASS |  |  |
| COPX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $97.59 · close 39.26% below · Nov 19 close | payload values | PASS |  |  |
| COPX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.84 | $20.84 | PASS |  |  |
| COPZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -66.12% | -66.12% | PASS |  |  |
| COPZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.84 · close 66.12% below · Nov 19 close | payload values | PASS |  |  |
| COPZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1081.55 | $1,081.55 | PASS |  |  |
| COST | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 1.14% | 1.14% | PASS |  |  |
| COST | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| COST | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.98 | 0.98 | PASS |  |  |
| COST | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| COST | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,081.55 · close 1.14% above · broke out Nov 11 on 0.98× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| COST | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COTG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.12 | $16.12 | PASS |  |  |
| COTG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 2.05% | 2.05% | PASS |  |  |
| COTG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| COTG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.4 | 0.4 | PASS |  |  |
| COTG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| COTG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.12 · close 2.05% above · broke out Nov 11 on 0.40× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| COTG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COTG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CSU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $3528.91 | $3,528.91 | PASS |  |  |
| CSU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.89% | -9.89% | PASS |  |  |
| CSU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CSU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CSU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CSU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $3,528.91 · close 9.89% below · Nov 19 close | payload values | PASS |  |  |
| CSU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CVX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $236.48 | $236.48 | PASS |  |  |
| CVX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.68% | -12.68% | PASS |  |  |
| CVX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CVX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CVX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CVX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $236.48 · close 12.68% below · Nov 19 close | payload values | PASS |  |  |
| CVX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $13 | $13.00 | PASS |  |  |
| DRAL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -69.31% | -69.31% | PASS |  |  |
| DRAL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $13.00 · close 69.31% below · Nov 19 close | payload values | PASS |  |  |
| DRAL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $63.82 | $63.82 | PASS |  |  |
| DRAM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39.78% | -39.78% | PASS |  |  |
| DRAM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $63.82 · close 39.78% below · Nov 19 close | payload values | PASS |  |  |
| DRAM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRIV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.47 | $36.47 | PASS |  |  |
| DRIV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28% | -28.00% | PASS |  |  |
| DRIV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRIV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRIV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRIV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.47 · close 28.00% below · Nov 19 close | payload values | PASS |  |  |
| DRIV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $132.99 | $132.99 | PASS |  |  |
| DUK | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.11% | -3.11% | PASS |  |  |
| DUK | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DUK | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DUK | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DUK | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $132.99 · close 3.11% below · Nov 19 close | payload values | PASS |  |  |
| DUK | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ELIL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $42.5 | $42.50 | PASS |  |  |
| ELIL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.95% | -13.95% | PASS |  |  |
| ELIL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ELIL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ELIL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ELIL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $42.50 · close 13.95% below · Nov 19 close | payload values | PASS |  |  |
| ELIL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| EQIX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1098.02 | $1,098.02 | PASS |  |  |
| EQIX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.25% | -7.25% | PASS |  |  |
| EQIX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| EQIX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| EQIX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| EQIX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,098.02 · close 7.25% below · Nov 19 close | payload values | PASS |  |  |
| EQIX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ETN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $459.38 | $459.38 | PASS |  |  |
| ETN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.04% | -28.04% | PASS |  |  |
| ETN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ETN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ETN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ETN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $459.38 · close 28.04% below · Nov 19 close | payload values | PASS |  |  |
| ETN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FCX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $80.24 | $80.24 | PASS |  |  |
| FCX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -38.78% | -38.78% | PASS |  |  |
| FCX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FCX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FCX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FCX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $80.24 · close 38.78% below · Nov 19 close | payload values | PASS |  |  |
| FCX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $105.67 | $105.67 | PASS |  |  |
| GDX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -31.86% | -31.86% | PASS |  |  |
| GDX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $105.67 · close 31.86% below · Nov 19 close | payload values | PASS |  |  |
| GDX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDXU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.45 | $46.45 | PASS |  |  |
| GDXU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -56.19% | -56.19% | PASS |  |  |
| GDXU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDXU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDXU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDXU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.45 · close 56.19% below · Nov 19 close | payload values | PASS |  |  |
| GDXU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $375.01 | $375.01 | PASS |  |  |
| GE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.97% | -14.97% | PASS |  |  |
| GE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $375.01 · close 14.97% below · Nov 19 close | payload values | PASS |  |  |
| GE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1099.02 | $1,099.02 | PASS |  |  |
| GEV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -31.19% | -31.19% | PASS |  |  |
| GEV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,099.02 · close 31.19% below · Nov 19 close | payload values | PASS |  |  |
| GEV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $73.78 | $73.78 | PASS |  |  |
| GEV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -31.42% | -31.42% | PASS |  |  |
| GEV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $73.78 · close 31.42% below · Nov 19 close | payload values | PASS |  |  |
| GEV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GGLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $111.95 | $111.95 | PASS |  |  |
| GGLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -46.64% | -46.64% | PASS |  |  |
| GGLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GGLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GGLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GGLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $111.95 · close 46.64% below · Nov 19 close | payload values | PASS |  |  |
| GGLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $117.04 | $117.04 | PASS |  |  |
| GIB-A.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.96% | -3.96% | PASS |  |  |
| GIB-A.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-06 | 2026-11-06 | PASS |  |  |
| GIB-A.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.52 | 1.52 | PASS |  |  |
| GIB-A.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| GIB-A.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $117.04 · close 3.96% below · broke out Nov 6 on 1.52× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| GIB-A.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| GOOGL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.17 | $364.17 | PASS |  |  |
| GOOGL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.13% | -25.13% | PASS |  |  |
| GOOGL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GOOGL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GOOGL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GOOGL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.17 · close 25.13% below · Nov 19 close | payload values | PASS |  |  |
| GOOGL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GRID | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $189.46 | $189.46 | PASS |  |  |
| GRID | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.55% | -19.55% | PASS |  |  |
| GRID | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GRID | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GRID | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GRID | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $189.46 · close 19.55% below · Nov 19 close | payload values | PASS |  |  |
| GRID | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $362.44 | $362.44 | PASS |  |  |
| HD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.11% | -7.11% | PASS |  |  |
| HD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $362.44 · close 7.11% below · Nov 19 close | payload values | PASS |  |  |
| HD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HURA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $56.75 | $56.75 | PASS |  |  |
| HURA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.83% | -36.83% | PASS |  |  |
| HURA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HURA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HURA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HURA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $56.75 · close 36.83% below · Nov 19 close | payload values | PASS |  |  |
| HURA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HXQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.61% | -14.61% | PASS |  |  |
| HXQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HXQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HXQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HXQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $128.37 · close 14.61% below · Nov 19 close | payload values | PASS |  |  |
| HXQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $282.02 | $282.02 | PASS |  |  |
| JNJ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.28% | -5.28% | PASS |  |  |
| JNJ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-09 | 2026-11-09 | PASS |  |  |
| JNJ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.96 | 0.96 | PASS |  |  |
| JNJ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| JNJ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $282.02 · close 5.28% below · broke out Nov 9 on 0.96× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| JNJ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| JPM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.68 | $364.68 | PASS |  |  |
| JPM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.19% | -12.19% | PASS |  |  |
| JPM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| JPM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| JPM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| JPM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.68 · close 12.19% below · Nov 19 close | payload values | PASS |  |  |
| JPM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| KEYS | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $389.93 | $389.93 | PASS |  |  |
| KEYS | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.83% | -27.83% | PASS |  |  |
| KEYS | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| KEYS | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| KEYS | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| KEYS | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $389.93 · close 27.83% below · Nov 19 close | payload values | PASS |  |  |
| KEYS | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LIN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $533.38 | $533.38 | PASS |  |  |
| LIN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.34% | -4.34% | PASS |  |  |
| LIN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| LIN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| LIN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| LIN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $533.38 · close 4.34% below · Nov 19 close | payload values | PASS |  |  |
| LIN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LLY | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1453 | $1,453.00 | PASS |  |  |
| LLY | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.01% | -7.01% | PASS |  |  |
| LLY | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| LLY | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| LLY | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| LLY | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,453.00 · close 7.01% below · Nov 19 close | payload values | PASS |  |  |
| LLY | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MDA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $51.34 | $51.34 | PASS |  |  |
| MDA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.13% | -25.13% | PASS |  |  |
| MDA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MDA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MDA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MDA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $51.34 · close 25.13% below · Nov 19 close | payload values | PASS |  |  |
| MDA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| META | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $779.82 | $779.82 | PASS |  |  |
| META | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.54% | -23.54% | PASS |  |  |
| META | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| META | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| META | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| META | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $779.82 · close 23.54% below · Nov 19 close | payload values | PASS |  |  |
| META | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| METU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.6 | $35.60 | PASS |  |  |
| METU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -43.79% | -43.79% | PASS |  |  |
| METU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| METU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| METU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| METU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.60 · close 43.79% below · Nov 19 close | payload values | PASS |  |  |
| METU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MRVL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $301.27 | $301.27 | PASS |  |  |
| MRVL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -54.04% | -54.04% | PASS |  |  |
| MRVL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MRVL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MRVL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MRVL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $301.27 · close 54.04% below · Nov 19 close | payload values | PASS |  |  |
| MRVL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $559.15 | $559.15 | PASS |  |  |
| MSFT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.88% | -10.88% | PASS |  |  |
| MSFT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MSFT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MSFT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MSFT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $559.15 · close 10.88% below · Nov 19 close | payload values | PASS |  |  |
| MSFT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $45.88 | $45.88 | PASS |  |  |
| MSFU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.9% | -20.90% | PASS |  |  |
| MSFU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MSFU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MSFU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MSFU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $45.88 · close 20.90% below · Nov 19 close | payload values | PASS |  |  |
| MSFU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MTRX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $37.54 | $37.54 | PASS |  |  |
| MTRX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -24.96% | -24.96% | PASS |  |  |
| MTRX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MTRX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MTRX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MTRX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $37.54 · close 24.96% below · Nov 19 close | payload values | PASS |  |  |
| MTRX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $48.54 | $48.54 | PASS |  |  |
| MU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.93% | -37.93% | PASS |  |  |
| MU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $48.54 · close 37.93% below · Nov 19 close | payload values | PASS |  |  |
| MU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $90.04 | $90.04 | PASS |  |  |
| NEE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -6.94% | -6.94% | PASS |  |  |
| NEE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NEE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NEE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NEE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $90.04 · close 6.94% below · Nov 19 close | payload values | PASS |  |  |
| NEE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $135.29 | $135.29 | PASS |  |  |
| NEM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.05% | -26.05% | PASS |  |  |
| NEM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NEM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NEM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NEM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $135.29 · close 26.05% below · Nov 19 close | payload values | PASS |  |  |
| NEM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFLX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $83.6 | $83.60 | PASS |  |  |
| NFLX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.07% | -30.07% | PASS |  |  |
| NFLX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFLX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFLX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFLX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $83.60 · close 30.07% below · Nov 19 close | payload values | PASS |  |  |
| NFLX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.33 | $20.33 | PASS |  |  |
| NFXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -53.52% | -53.52% | PASS |  |  |
| NFXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.33 · close 53.52% below · Nov 19 close | payload values | PASS |  |  |
| NFXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NTR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $112.9 | $112.90 | PASS |  |  |
| NTR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -16.74% | -16.74% | PASS |  |  |
| NTR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NTR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NTR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NTR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $112.90 · close 16.74% below · Nov 19 close | payload values | PASS |  |  |
| NTR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.37 | $243.37 | PASS |  |  |
| NVDA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -40.02% | -40.02% | PASS |  |  |
| NVDA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.37 · close 40.02% below · Nov 19 close | payload values | PASS |  |  |
| NVDA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $41.59 | $41.59 | PASS |  |  |
| NVDL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -65.74% | -65.74% | PASS |  |  |
| NVDL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $41.59 · close 65.74% below · Nov 19 close | payload values | PASS |  |  |
| NVDL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ONTO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $353.84 | $353.84 | PASS |  |  |
| ONTO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -44.63% | -44.63% | PASS |  |  |
| ONTO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ONTO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ONTO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ONTO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $353.84 · close 44.63% below · Nov 19 close | payload values | PASS |  |  |
| ONTO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORBX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $19.64 | $19.64 | PASS |  |  |
| ORBX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.73% | -26.73% | PASS |  |  |
| ORBX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORBX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORBX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORBX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $19.64 · close 26.73% below · Nov 18 close | payload values | PASS |  |  |
| ORBX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $170.07 | $170.07 | PASS |  |  |
| ORCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -34.99% | -34.99% | PASS |  |  |
| ORCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $170.07 · close 34.99% below · Nov 19 close | payload values | PASS |  |  |
| ORCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $170.52 | $170.52 | PASS |  |  |
| PG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.57% | -1.57% | PASS |  |  |
| PG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-16 | 2026-11-16 | PASS |  |  |
| PG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.62 | 1.62 | PASS |  |  |
| PG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| PG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $170.52 · close 1.57% below · broke out Nov 16 on 1.62× its prior 50-day average volume · Nov 19 close | payload values | PASS |  |  |
| PG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| PLD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $142.69 | $142.69 | PASS |  |  |
| PLD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.55% | -13.55% | PASS |  |  |
| PLD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PLD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PLD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PLD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $142.69 · close 13.55% below · Nov 19 close | payload values | PASS |  |  |
| PLD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PNG.V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $6.8 | $6.80 | PASS |  |  |
| PNG.V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -57.65% | -57.65% | PASS |  |  |
| PNG.V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PNG.V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PNG.V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PNG.V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $6.80 · close 57.65% below · Nov 19 close | payload values | PASS |  |  |
| PNG.V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QCOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $205.85 | $205.85 | PASS |  |  |
| QCOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -21.3% | -21.30% | PASS |  |  |
| QCOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QCOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QCOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QCOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $205.85 · close 21.30% below · Nov 19 close | payload values | PASS |  |  |
| QCOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QPUX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $22.2 | $22.20 | PASS |  |  |
| QPUX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -87.12% | -87.12% | PASS |  |  |
| QPUX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QPUX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QPUX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QPUX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $22.20 · close 87.12% below · Nov 19 close | payload values | PASS |  |  |
| QPUX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QTUM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $159.25 | $159.25 | PASS |  |  |
| QTUM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -24.83% | -24.83% | PASS |  |  |
| QTUM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QTUM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QTUM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QTUM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $159.25 · close 24.83% below · Nov 19 close | payload values | PASS |  |  |
| QTUM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RBOT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $34.84 | $34.84 | PASS |  |  |
| RBOT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.24% | -22.24% | PASS |  |  |
| RBOT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RBOT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RBOT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RBOT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $34.84 · close 22.24% below · Nov 18 close | payload values | PASS |  |  |
| RBOT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RTX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $226.41 | $226.41 | PASS |  |  |
| RTX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.56% | -14.56% | PASS |  |  |
| RTX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RTX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RTX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RTX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $226.41 · close 14.56% below · Nov 19 close | payload values | PASS |  |  |
| RTX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.46 | $300.46 | PASS |  |  |
| RY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.32% | -10.32% | PASS |  |  |
| RY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.46 · close 10.32% below · Nov 19 close | payload values | PASS |  |  |
| RY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SETM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.24 | $36.24 | PASS |  |  |
| SETM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -43.05% | -43.05% | PASS |  |  |
| SETM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SETM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SETM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SETM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.24 · close 43.05% below · Nov 19 close | payload values | PASS |  |  |
| SETM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SGRD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $21.32 | $21.32 | PASS |  |  |
| SGRD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -17.01% | -17.03% | PASS |  |  |
| SGRD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SGRD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SGRD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SGRD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $21.32 · close 17.01% below · Nov 19 close | payload values | PASS |  |  |
| SGRD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SMH | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $639.47 | $639.47 | PASS |  |  |
| SMH | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.02% | -30.02% | PASS |  |  |
| SMH | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SMH | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SMH | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SMH | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $639.47 · close 30.02% below · Nov 19 close | payload values | PASS |  |  |
| SMH | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SNDK.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.35 | $46.35 | PASS |  |  |
| SNDK.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -60.41% | -60.41% | PASS |  |  |
| SNDK.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SNDK.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SNDK.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SNDK.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.35 · close 60.41% below · Nov 19 close | payload values | PASS |  |  |
| SNDK.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $94.94 | $94.94 | PASS |  |  |
| SO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.74% | -1.74% | PASS |  |  |
| SO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| SO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $94.94 · close 1.74% below · Nov 19 close | payload values | PASS |  |  |
| SO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $169.83 | $169.83 | PASS |  |  |
| SOXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -73.33% | -73.33% | PASS |  |  |
| SOXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $169.83 · close 73.33% below · Nov 19 close | payload values | PASS |  |  |
| SOXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $40.79 | $40.79 | PASS |  |  |
| SOXL.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -72% | -72.00% | PASS |  |  |
| SOXL.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $40.79 · close 72.00% below · Nov 19 close | payload values | PASS |  |  |
| SOXL.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $198.81 | $198.81 | PASS |  |  |
| SOXX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.61% | -30.61% | PASS |  |  |
| SOXX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $198.81 · close 30.61% below · Nov 19 close | payload values | PASS |  |  |
| SOXX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SPCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.54 | $33.54 | PASS |  |  |
| SPCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -73.43% | -73.43% | PASS |  |  |
| SPCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SPCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SPCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SPCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.54 · close 73.43% below · Nov 19 close | payload values | PASS |  |  |
| SPCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $414.23 | $414.23 | PASS |  |  |
| TSLA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.61% | -9.61% | PASS |  |  |
| TSLA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $414.23 · close 9.61% below · Nov 19 close | payload values | PASS |  |  |
| TSLA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $11.98 | $11.98 | PASS |  |  |
| TSLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.45% | -20.45% | PASS |  |  |
| TSLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $11.98 · close 20.45% below · Nov 19 close | payload values | PASS |  |  |
| TSLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $487.47 | $487.47 | PASS |  |  |
| TSM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.77% | -27.77% | PASS |  |  |
| TSM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $487.47 · close 27.77% below · Nov 19 close | payload values | PASS |  |  |
| TSM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UBOT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $25.51 | $25.51 | PASS |  |  |
| UBOT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -43.78% | -43.79% | PASS |  |  |
| UBOT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UBOT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UBOT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UBOT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $25.51 · close 43.78% below · Nov 19 close | payload values | PASS |  |  |
| UBOT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UFO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.29 | $49.29 | PASS |  |  |
| UFO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.96% | -22.97% | PASS |  |  |
| UFO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UFO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UFO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UFO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.29 · close 22.96% below · Nov 19 close | payload values | PASS |  |  |
| UFO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| URA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $50.09 | $50.09 | PASS |  |  |
| URA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.78% | -42.78% | PASS |  |  |
| URA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| URA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| URA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| URA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $50.09 · close 42.78% below · Nov 19 close | payload values | PASS |  |  |
| URA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| URAA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.45 | $31.45 | PASS |  |  |
| URAA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -67.03% | -67.03% | PASS |  |  |
| URAA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| URAA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| URAA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| URAA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.45 · close 67.03% below · Nov 19 close | payload values | PASS |  |  |
| URAA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $442.23 | $442.23 | PASS |  |  |
| V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.04% | -9.04% | PASS |  |  |
| V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $442.23 · close 9.04% below · Nov 19 close | payload values | PASS |  |  |
| V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| VFV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.52% | -7.52% | PASS |  |  |
| VFV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VFV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VFV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VFV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $197.83 · close 7.52% below · Nov 19 close | payload values | PASS |  |  |
| VFV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| VRT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.23 | $300.23 | PASS |  |  |
| VRT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -38.38% | -38.38% | PASS |  |  |
| VRT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VRT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VRT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VRT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.23 · close 38.38% below · Nov 19 close | payload values | PASS |  |  |
| VRT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WDC.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.32 | $33.32 | PASS |  |  |
| WDC.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -46.04% | -46.04% | PASS |  |  |
| WDC.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WDC.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WDC.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| WDC.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.32 · close 46.04% below · Nov 19 close | payload values | PASS |  |  |
| WDC.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WELL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $249.12 | $249.12 | PASS |  |  |
| WELL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.38% | -2.38% | PASS |  |  |
| WELL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WELL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WELL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| WELL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $249.12 · close 2.38% below · Nov 19 close | payload values | PASS |  |  |
| WELL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $131.82 | $131.82 | PASS |  |  |
| WMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.38% | -4.38% | PASS |  |  |
| WMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| WMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $131.82 · close 4.38% below · Nov 19 close | payload values | PASS |  |  |
| WMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XCHP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $147.5 | $147.50 | PASS |  |  |
| XCHP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.04% | -30.04% | PASS |  |  |
| XCHP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XCHP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XCHP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XCHP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $147.50 · close 30.04% below · Nov 19 close | payload values | PASS |  |  |
| XCHP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XDRV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.26 | $49.26 | PASS |  |  |
| XDRV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.71% | -19.71% | PASS |  |  |
| XDRV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XDRV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XDRV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XDRV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.26 · close 19.71% below · Nov 19 close | payload values | PASS |  |  |
| XDRV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XEQT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -6.68% | -6.68% | PASS |  |  |
| XEQT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XEQT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XEQT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XEQT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.38 · close 6.68% below · Nov 19 close | payload values | PASS |  |  |
| XEQT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XETM.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $91.8 | $91.80 | PASS |  |  |
| XETM.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -38.79% | -38.79% | PASS |  |  |
| XETM.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XETM.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XETM.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XETM.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $91.80 · close 38.79% below · Nov 19 close | payload values | PASS |  |  |
| XETM.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XGD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $65.29 | $65.29 | PASS |  |  |
| XGD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.34% | -28.34% | PASS |  |  |
| XGD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XGD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XGD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XGD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $65.29 · close 28.34% below · Nov 19 close | payload values | PASS |  |  |
| XGD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $188.5 | $188.50 | PASS |  |  |
| XOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -15.69% | -15.69% | PASS |  |  |
| XOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $188.50 · close 15.69% below · Nov 19 close | payload values | PASS |  |  |
| XOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $349.21 · Nov 19 | $349.21 · Nov 19 | PASS |  |  |
| AAPU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $47.68 · Nov 19 | $47.68 · Nov 19 | PASS |  |  |
| ABBV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.36 / Mom: +1.05 / Rank: 2/11] XLV LEADING | RS 105.36 Mom 1.05 Rank 2/11 | PASS |  |  |
| ABBV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| ABBV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ABBV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $283.54 · Nov 19 | $283.54 · Nov 19 | PASS |  |  |
| AIPO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AIPO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $22.08 · Nov 19 | $22.08 · Nov 19 | PASS |  |  |
| ALAB | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| ALAB | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ALAB | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ALAB | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $211.60 · Nov 19 | $211.60 · Nov 19 | PASS |  |  |
| AMD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| AMD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $489.19 · Nov 19 | $489.19 · Nov 19 | PASS |  |  |
| AMD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| AMD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.52 / Mom: +2.33 / Rank: 7/11] X | RS 98.52 Mom 2.33 Rank 7/11 | PASS |  |  |
| AMZN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| AMZN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $257.37 · Nov 19 | $257.37 · Nov 19 | PASS |  |  |
| AMZU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $34.95 · Nov 19 | $34.95 · Nov 19 | PASS |  |  |
| ANET.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASML.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.63 / Mom: +0.66 / Rank: 6/11] XLB IMPROVING | RS 98.63 Mom 0.66 Rank 6/11 | PASS |  |  |
| ASTL.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ASTL.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $6.90 · Nov 19 | $6.90 · Nov 19 | PASS |  |  |
| ATD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.52 / Mom: +2.33 / Rank: 7/11] X | RS 98.52 Mom 2.33 Rank 7/11 | PASS |  |  |
| ATD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ATD.TO | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 5 days | 📅 Earnings in 5 days | PASS |  |  |
| ATD.TO | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 5 days | 2026-11-24, 5 days | PASS |  |  |
| ATD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $80.14 · Nov 19 | $80.14 · Nov 19 | PASS |  |  |
| AVGC | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGC | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $18.88 · Nov 19 | $18.88 · Nov 19 | PASS |  |  |
| AVGO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| AVGO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AVGO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $346.55 · Nov 19 | $346.55 · Nov 19 | PASS |  |  |
| AVGO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BDT.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| BDT.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| BDT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BDT.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $71.42 · Nov 19 | $71.42 · Nov 19 | PASS |  |  |
| BOTZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BOTZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $29.00 · Nov 19 | $29.00 · Nov 19 | PASS |  |  |
| BRK-B | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 99.98 / Mom: -0.48 / Rank: 4/11] XLF LAGGING | RS 99.98 Mom -0.48 Rank 4/11 | PASS |  |  |
| BRK-B | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| BRK-B | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRK-B | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $572.04 · Nov 19 | $572.04 · Nov 19 | PASS |  |  |
| BRKU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRKU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $28.55 · Nov 19 | $28.55 · Nov 19 | PASS |  |  |
| CAMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| CAMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAMT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $97.78 · Nov 19 | $97.78 · Nov 19 | PASS |  |  |
| CARS.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| CAT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $537.26 · Nov 19 | $537.26 · Nov 19 | PASS |  |  |
| CCO.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.33 / Mom: +0.28 / Rank: 1/11] XLE LEADING | RS 106.33 Mom 0.28 Rank 1/11 | PASS |  |  |
| CCO.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CCO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CCO.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $89.40 · Nov 18 | $89.40 · Nov 18 | PASS |  |  |
| CEG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.77 / Mom: +2.97 / Rank: 10/11] XLU IMPROVING | RS 96.77 Mom 2.97 Rank 10/11 | PASS |  |  |
| CEG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| CEG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CEG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $252.03 · Nov 19 | $252.03 · Nov 19 | PASS |  |  |
| CGY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| CGY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CGY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CGY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $81.56 · Nov 19 | $81.56 · Nov 19 | PASS |  |  |
| CNQ.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.33 / Mom: +0.28 / Rank: 1/11] XLE LEADING | RS 106.33 Mom 0.28 Rank 1/11 | PASS |  |  |
| CNQ.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CNQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| CNR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CNR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $178.66 · Nov 19 | $178.66 · Nov 19 | PASS |  |  |
| COP | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.33 / Mom: +0.28 / Rank: 1/11] XLE LEADING | RS 106.33 Mom 0.28 Rank 1/11 | PASS |  |  |
| COP | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COP | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COP | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $134.99 · Nov 19 | $134.99 · Nov 19 | PASS |  |  |
| COPP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $59.28 · Nov 19 | $59.28 · Nov 19 | PASS |  |  |
| COPZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $7.06 · Nov 19 | $7.06 · Nov 19 | PASS |  |  |
| COST | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.56 / Mom: +3.21 / Rank: 3/11] XLP LE | RS 101.56 Mom 3.21 Rank 3/11 | PASS |  |  |
| COST | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COST | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COST | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,093.83 · Nov 19 | $1,093.83 · Nov 19 | PASS |  |  |
| COTG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COTG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $16.45 · Nov 19 | $16.45 · Nov 19 | PASS |  |  |
| CSU.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| CSU.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CSU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CSU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3,180.00 · Nov 19 | $3,180.00 · Nov 19 | PASS |  |  |
| CVX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.33 / Mom: +0.28 / Rank: 1/11] XLE LEADING | RS 106.33 Mom 0.28 Rank 1/11 | PASS |  |  |
| CVX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CVX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CVX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $206.50 · Nov 19 | $206.50 · Nov 19 | PASS |  |  |
| DRAL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3.99 · Nov 19 | $3.99 · Nov 19 | PASS |  |  |
| DRAM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $38.43 · Nov 19 | $38.43 · Nov 19 | PASS |  |  |
| DRIV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRIV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $26.26 · Nov 19 | $26.26 · Nov 19 | PASS |  |  |
| DUK | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.77 / Mom: +2.97 / Rank: 10/11] XLU IMPROVING | RS 96.77 Mom 2.97 Rank 10/11 | PASS |  |  |
| DUK | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| DUK | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DUK | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $128.86 · Nov 19 | $128.86 · Nov 19 | PASS |  |  |
| ELIL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ELIL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $36.57 · Nov 19 | $36.57 · Nov 19 | PASS |  |  |
| EQIX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.16 / Mom: +1.26 / Rank: 9/11] XLRE IMPROV | RS 97.16 Mom 1.26 Rank 9/11 | PASS |  |  |
| EQIX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| EQIX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| EQIX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,018.45 · Nov 19 | $1,018.45 · Nov 19 | PASS |  |  |
| ETN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| ETN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ETN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ETN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $330.57 · Nov 19 | $330.57 · Nov 19 | PASS |  |  |
| FCX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.63 / Mom: +0.66 / Rank: 6/11] XLB IMPROVING | RS 98.63 Mom 0.66 Rank 6/11 | PASS |  |  |
| FCX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| FCX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| FCX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $49.12 · Nov 19 | $49.12 · Nov 19 | PASS |  |  |
| GDX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $72.00 · Nov 19 | $72.00 · Nov 19 | PASS |  |  |
| GDXU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| GE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $318.88 · Nov 19 | $318.88 · Nov 19 | PASS |  |  |
| GEV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| GEV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GEV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GEV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $756.28 · Nov 19 | $756.28 · Nov 19 | PASS |  |  |
| GEV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $59.74 · Nov 19 | $59.74 · Nov 19 | PASS |  |  |
| GIB-A.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| GIB-A.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GIB-A.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GIB-A.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $112.41 · Nov 19 | $112.41 · Nov 19 | PASS |  |  |
| GOOGL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 97.98 / Mom: +0.27 / Rank: 8/11] X | RS 97.98 Mom 0.27 Rank 8/11 | PASS |  |  |
| GOOGL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| GOOGL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GOOGL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $272.66 · Nov 19 | $272.66 · Nov 19 | PASS |  |  |
| GRID | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GRID | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $152.42 · Nov 19 | $152.42 · Nov 19 | PASS |  |  |
| HD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.52 / Mom: +2.33 / Rank: 7/11] X | RS 98.52 Mom 2.33 Rank 7/11 | PASS |  |  |
| HD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| HD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $336.68 · Nov 19 | $336.68 · Nov 19 | PASS |  |  |
| HURA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HXQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.36 / Mom: +1.05 / Rank: 2/11] XLV LEADING | RS 105.36 Mom 1.05 Rank 2/11 | PASS |  |  |
| JNJ | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| JNJ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $267.14 · Nov 19 | $267.14 · Nov 19 | PASS |  |  |
| JPM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 99.98 / Mom: -0.48 / Rank: 4/11] XLF LAGGING | RS 99.98 Mom -0.48 Rank 4/11 | PASS |  |  |
| JPM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| JPM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JPM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $320.22 · Nov 19 | $320.22 · Nov 19 | PASS |  |  |
| KEYS | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| KEYS | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| KEYS | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ EARNINGS TODAY | ⚠️ EARNINGS TODAY | PASS |  |  |
| KEYS | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-19, 0 days | 2026-11-19, 0 days | PASS |  |  |
| KEYS | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $281.42 · Nov 19 | $281.42 · Nov 19 | PASS |  |  |
| LIN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.63 / Mom: +0.66 / Rank: 6/11] XLB IMPROVING | RS 98.63 Mom 0.66 Rank 6/11 | PASS |  |  |
| LIN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| LIN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LIN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $510.21 · Nov 19 | $510.21 · Nov 19 | PASS |  |  |
| LLY | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.36 / Mom: +1.05 / Rank: 2/11] XLV LEADING | RS 105.36 Mom 1.05 Rank 2/11 | PASS |  |  |
| LLY | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| LLY | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LLY | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,351.12 · Nov 19 | $1,351.12 · Nov 19 | PASS |  |  |
| MDA.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| MDA.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MDA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MDA.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $38.44 · Nov 19 | $38.44 · Nov 19 | PASS |  |  |
| META | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 97.98 / Mom: +0.27 / Rank: 8/11] X | RS 97.98 Mom 0.27 Rank 8/11 | PASS |  |  |
| META | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| META | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| META | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $596.22 · Nov 19 | $596.22 · Nov 19 | PASS |  |  |
| METU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| METU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $20.01 · Nov 19 | $20.01 · Nov 19 | PASS |  |  |
| MRVL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| MRVL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MRVL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MRVL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $138.47 · Nov 19 | $138.47 · Nov 19 | PASS |  |  |
| MSFT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| MSFT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MSFT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $498.30 · Nov 19 | $498.30 · Nov 19 | PASS |  |  |
| MSFU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $36.29 · Nov 19 | $36.29 · Nov 19 | PASS |  |  |
| MTRX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.77 / Mom: +2.97 / Rank: 10/11] XLU IMPROVING | RS 96.77 Mom 2.97 Rank 10/11 | PASS |  |  |
| NEE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $83.79 · Nov 19 | $83.79 · Nov 19 | PASS |  |  |
| NEM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.63 / Mom: +0.66 / Rank: 6/11] XLB IMPROVING | RS 98.63 Mom 0.66 Rank 6/11 | PASS |  |  |
| NEM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $100.05 · Nov 19 | $100.05 · Nov 19 | PASS |  |  |
| NFLX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 97.98 / Mom: +0.27 / Rank: 8/11] X | RS 97.98 Mom 0.27 Rank 8/11 | PASS |  |  |
| NFLX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NFLX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFLX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $58.46 · Nov 19 | $58.46 · Nov 19 | PASS |  |  |
| NFXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $9.45 · Nov 19 | $9.45 · Nov 19 | PASS |  |  |
| NTR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.63 / Mom: +0.66 / Rank: 6/11] XLB IMPROVING | RS 98.63 Mom 0.66 Rank 6/11 | PASS |  |  |
| NTR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NTR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NTR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $94.00 · Nov 19 | $94.00 · Nov 19 | PASS |  |  |
| NVDA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| NVDA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| NVDA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $145.98 · Nov 19 | $145.98 · Nov 19 | PASS |  |  |
| NVDL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $14.25 · Nov 19 | $14.25 · Nov 19 | PASS |  |  |
| ONTO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| ONTO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ONTO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ONTO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $195.93 · Nov 19 | $195.93 · Nov 19 | PASS |  |  |
| ORBX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| ORCL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ORCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $110.57 · Nov 19 | $110.57 · Nov 19 | PASS |  |  |
| PG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.56 / Mom: +3.21 / Rank: 3/11] XLP LE | RS 101.56 Mom 3.21 Rank 3/11 | PASS |  |  |
| PG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| PG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $167.85 · Nov 19 | $167.85 · Nov 19 | PASS |  |  |
| PLD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.16 / Mom: +1.26 / Rank: 9/11] XLRE IMPROV | RS 97.16 Mom 1.26 Rank 9/11 | PASS |  |  |
| PLD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| PLD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PLD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $123.36 · Nov 19 | $123.36 · Nov 19 | PASS |  |  |
| PNG.V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| PNG.V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| PNG.V | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 5 days | 📅 Earnings in 5 days | PASS |  |  |
| PNG.V | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 5 days | 2026-11-24, 5 days | PASS |  |  |
| QCOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| QCOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| QCOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QCOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $162.01 · Nov 19 | $162.01 · Nov 19 | PASS |  |  |
| QPUX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QPUX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $2.86 · Nov 19 | $2.86 · Nov 19 | PASS |  |  |
| QTUM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QTUM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $119.71 · Nov 19 | $119.71 · Nov 19 | PASS |  |  |
| RBOT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| RTX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| RTX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $193.44 · Nov 19 | $193.44 · Nov 19 | PASS |  |  |
| RY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 99.98 / Mom: -0.48 / Rank: 4/11] XLF LAGGING | RS 99.98 Mom -0.48 Rank 4/11 | PASS |  |  |
| RY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| RY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $269.45 · Nov 19 | $269.45 · Nov 19 | PASS |  |  |
| SETM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SETM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $20.64 · Nov 19 | $20.64 · Nov 19 | PASS |  |  |
| SGRD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $447.48 · Nov 19 | $447.48 · Nov 19 | PASS |  |  |
| SNDK.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.77 / Mom: +2.97 / Rank: 10/11] XLU IMPROVING | RS 96.77 Mom 2.97 Rank 10/11 | PASS |  |  |
| SO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| SO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $93.29 · Nov 19 | $93.29 · Nov 19 | PASS |  |  |
| SOXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $45.30 · Nov 19 | $45.30 · Nov 19 | PASS |  |  |
| SOXL.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $137.95 · Nov 19 | $137.95 · Nov 19 | PASS |  |  |
| SPCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SPCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $8.91 · Nov 19 | $8.91 · Nov 19 | PASS |  |  |
| TSLA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.52 / Mom: +2.33 / Rank: 7/11] X | RS 98.52 Mom 2.33 Rank 7/11 | PASS |  |  |
| TSLA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| TSLA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $374.41 · Nov 19 | $374.41 · Nov 19 | PASS |  |  |
| TSLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $9.53 · Nov 19 | $9.53 · Nov 19 | PASS |  |  |
| TSM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| TSM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| TSM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $352.09 · Nov 19 | $352.09 · Nov 19 | PASS |  |  |
| UBOT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UBOT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $14.34 · Nov 19 | $14.34 · Nov 19 | PASS |  |  |
| UFO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UFO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $37.97 · Nov 19 | $37.97 · Nov 19 | PASS |  |  |
| URA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $28.66 · Nov 19 | $28.66 · Nov 19 | PASS |  |  |
| URAA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URAA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $10.37 · Nov 19 | $10.37 · Nov 19 | PASS |  |  |
| V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 99.98 / Mom: -0.48 / Rank: 4/11] XLF LAGGING | RS 99.98 Mom -0.48 Rank 4/11 | PASS |  |  |
| V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| V | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| V | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $402.25 · Nov 19 | $402.25 · Nov 19 | PASS |  |  |
| VFV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VRT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| VRT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| VRT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VRT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $184.99 · Nov 19 | $184.99 · Nov 19 | PASS |  |  |
| WDC.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WELL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.16 / Mom: +1.26 / Rank: 9/11] XLRE IMPROV | RS 97.16 Mom 1.26 Rank 9/11 | PASS |  |  |
| WELL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| WELL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WELL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $243.19 · Nov 19 | $243.19 · Nov 19 | PASS |  |  |
| WMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.56 / Mom: +3.21 / Rank: 3/11] XLP LE | RS 101.56 Mom 3.21 Rank 3/11 | PASS |  |  |
| WMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| WMT | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ EARNINGS TODAY | ⚠️ EARNINGS TODAY | PASS |  |  |
| WMT | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-19, 0 days | 2026-11-19, 0 days | PASS |  |  |
| WMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $126.04 · Nov 19 | $126.04 · Nov 19 | PASS |  |  |
| XCHP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XDRV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XEQT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XETM.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XGD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.33 / Mom: +0.28 / Rank: 1/11] XLE LEADING | RS 106.33 Mom 0.28 Rank 1/11 | PASS |  |  |
| XOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| XOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $158.93 · Nov 19 | $158.93 · Nov 19 | PASS |  |  |
| AAPL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $360.83 | $360.83 | PASS |  |  |
| AAPL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $349.21 | $349.21 | PASS |  |  |
| AAPL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $360.83 / $242.57 | $360.83 / $242.57 | PASS |  |  |
| AAPL | PD3 | % from High | -3.2% | -3.2% | PASS |  |  |
| AAPL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $14.8B | bars: $14,853,925,510 | PASS | LOW |  |
| AAPU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $51.04 | $51.04 | PASS |  |  |
| AAPU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $47.68 | $47.68 | PASS |  |  |
| AAPU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $51.04 / $25.94 | $51.04 / $25.94 | PASS |  |  |
| AAPU | PD3 | % from High | -6.6% | -6.6% | PASS |  |  |
| AAPU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $49M | bars: $36,909,252 | PASS | LOW |  |
| ABBV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.93 | $302.93 | PASS |  |  |
| ABBV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $283.54 | $283.54 | PASS |  |  |
| ABBV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.93 / $188.25 | $302.93 / $188.25 | PASS |  |  |
| ABBV | PD3 | % from High | -6.4% | -6.4% | PASS |  |  |
| ABBV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.4B | bars: $1,407,524,260 | PASS | LOW |  |
| AIPO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $34.79 | $34.79 | PASS |  |  |
| AIPO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $22.08 | $22.08 | PASS |  |  |
| AIPO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $34.79 / $20.65 | $34.79 / $20.65 | PASS |  |  |
| AIPO | PD3 | % from High | -36.5% | -36.5% | PASS |  |  |
| AIPO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $34M | bars: $36,184,515 | PASS | LOW |  |
| ALAB | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $499.48 | $499.48 | PASS |  |  |
| ALAB | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $211.60 | $211.60 | PASS |  |  |
| ALAB | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $499.48 / $97.89 | $499.48 / $97.89 | PASS |  |  |
| ALAB | PD3 | % from High | -57.6% | -57.6% | PASS |  |  |
| ALAB | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $903M | bars: $972,412,320 | PASS | LOW |  |
| AMD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $658.52 | $658.52 | PASS |  |  |
| AMD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $489.19 | $489.19 | PASS |  |  |
| AMD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $658.52 / $188.22 | $658.52 / $188.22 | PASS |  |  |
| AMD | PD3 | % from High | -25.7% | -25.7% | PASS |  |  |
| AMD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $12.4B | bars: $14,100,488,003 | PASS | LOW |  |
| AMD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $16.97 | $16.97 | PASS |  |  |
| AMD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.59 | $12.59 | PASS |  |  |
| AMD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $16.97 / $4.93 | $16.97 / $4.93 | PASS |  |  |
| AMD.TO | PD3 | % from High | -25.8% | -25.8% | PASS |  |  |
| AMD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $27M | bars: $29,307,968 | PASS | LOW |  |
| AMZN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $287.20 | $287.20 | PASS |  |  |
| AMZN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $257.37 | $257.37 | PASS |  |  |
| AMZN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $287.20 / $196.00 | $287.20 / $196.00 | PASS |  |  |
| AMZN | PD3 | % from High | -10.4% | -10.4% | PASS |  |  |
| AMZN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $10.2B | bars: $10,863,787,059 | PASS | LOW |  |
| AMZU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.64 | $46.64 | PASS |  |  |
| AMZU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $34.95 | $34.95 | PASS |  |  |
| AMZU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.64 / $24.13 | $46.64 / $24.13 | PASS |  |  |
| AMZU | PD3 | % from High | -25.1% | -25.1% | PASS |  |  |
| AMZU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $66M | bars: $67,236,507 | PASS | LOW |  |
| ANET.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $33.90 | $33.90 | PASS |  |  |
| ANET.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.85 / $20.97 | $38.85 / $20.97 | PASS |  |  |
| ANET.TO | PD3 | % from High | -12.7% | -12.7% | PASS |  |  |
| ASML.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $56.75 | $56.75 | PASS |  |  |
| ASML.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $41.25 | $41.25 | PASS |  |  |
| ASML.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $56.75 / $26.65 | $56.75 / $26.65 | PASS |  |  |
| ASML.TO | PD3 | % from High | -27.3% | -27.3% | PASS |  |  |
| ASML.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,861,668 | PASS | LOW |  |
| ASTL.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $8.31 | $8.31 | PASS |  |  |
| ASTL.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $6.90 | $6.90 | PASS |  |  |
| ASTL.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $8.31 / $4.46 | $8.31 / $4.46 | PASS |  |  |
| ASTL.TO | PD3 | % from High | -17.0% | -17.0% | PASS |  |  |
| ASTL.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $4,120,715 | PASS | LOW |  |
| ATD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $94.68 | $94.68 | PASS |  |  |
| ATD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $80.14 | $80.14 | PASS |  |  |
| ATD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $94.68 / $67.83 | $94.68 / $67.83 | PASS |  |  |
| ATD.TO | PD3 | % from High | -15.4% | -15.4% | PASS |  |  |
| ATD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $111M | bars: $105,325,085 | PASS | LOW |  |
| AVGC | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $18.88 | $18.88 | PASS |  |  |
| AVGC | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.79 / $13.71 | $31.79 / $13.71 | PASS |  |  |
| AVGC | PD3 | % from High | -40.6% | -40.6% | PASS |  |  |
| AVGO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $493.29 | $493.29 | PASS |  |  |
| AVGO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $346.55 | $346.55 | PASS |  |  |
| AVGO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $493.29 / $288.96 | $493.29 / $288.96 | PASS |  |  |
| AVGO | PD3 | % from High | -29.7% | -29.7% | PASS |  |  |
| AVGO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.8B | bars: $9,072,477,627 | PASS | LOW |  |
| AVGO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $13.13 | $13.13 | PASS |  |  |
| AVGO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $18.88 / $11.00 | $18.88 / $11.00 | PASS |  |  |
| AVGO.TO | PD3 | % from High | -30.4% | -30.5% | PASS |  |  |
| AVGO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15M | bars: $15,540,474 | PASS | LOW |  |
| BDT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $71.42 | $71.42 | PASS |  |  |
| BDT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $86.42 / $24.37 | $86.42 / $24.37 | PASS |  |  |
| BDT.TO | PD3 | % from High | -17.4% | -17.4% | PASS |  |  |
| BDT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $28M | bars: $29,725,057 | PASS | LOW |  |
| BOTZ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $41.71 | $41.71 | PASS |  |  |
| BOTZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $29.00 | $29.00 | PASS |  |  |
| BOTZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $41.71 / $28.98 | $41.71 / $28.98 | PASS |  |  |
| BOTZ | PD3 | % from High | -30.5% | -30.5% | PASS |  |  |
| BOTZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $20M | bars: $21,299,105 | PASS | LOW |  |
| BRK-B | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $596.92 | $596.92 | PASS |  |  |
| BRK-B | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $572.04 | $572.04 | PASS |  |  |
| BRK-B | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $596.92 / $464.01 | $596.92 / $464.01 | PASS |  |  |
| BRK-B | PD3 | % from High | -4.2% | -4.2% | PASS |  |  |
| BRK-B | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.7B | bars: $2,794,773,463 | PASS | LOW |  |
| BRKU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $31.20 | $31.20 | PASS |  |  |
| BRKU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $28.55 | $28.55 | PASS |  |  |
| BRKU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.20 / $20.25 | $31.20 / $20.25 | PASS |  |  |
| BRKU | PD3 | % from High | -8.5% | -8.5% | PASS |  |  |
| BRKU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,682,398 | PASS | LOW |  |
| CAMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $215.99 | $215.99 | PASS |  |  |
| CAMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $97.78 | $97.78 | PASS |  |  |
| CAMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $215.99 / $89.13 | $215.99 / $89.13 | PASS |  |  |
| CAMT | PD3 | % from High | -54.7% | -54.7% | PASS |  |  |
| CAMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $47M | bars: $50,892,180 | PASS | LOW |  |
| CARS.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.16 | $38.16 | PASS |  |  |
| CARS.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $19.88 | $19.88 | PASS |  |  |
| CARS.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.16 / $19.88 | $38.16 / $19.88 | PASS |  |  |
| CARS.TO | PD3 | % from High | -47.9% | -47.9% | PASS |  |  |
| CARS.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| CAT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,068.94 | $1,068.94 | PASS |  |  |
| CAT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $537.26 | $537.26 | PASS |  |  |
| CAT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,068.94 / $532.56 | $1,068.94 / $532.56 | PASS |  |  |
| CAT | PD3 | % from High | -49.7% | -49.7% | PASS |  |  |
| CAT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,758,165,352 | PASS | LOW |  |
| CCO.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $182.72 | $182.72 | PASS |  |  |
| CCO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $89.40 | $89.40 | PASS |  |  |
| CCO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $182.72 / $89.20 | $182.72 / $89.20 | PASS |  |  |
| CCO.TO | PD3 | % from High | -51.1% | -51.1% | PASS |  |  |
| CCO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $105M | bars: $112,560,851 | PASS | LOW |  |
| CEG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $380.78 | $380.78 | PASS |  |  |
| CEG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $252.03 | $252.03 | PASS |  |  |
| CEG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $380.78 / $228.63 | $380.78 / $228.63 | PASS |  |  |
| CEG | PD3 | % from High | -33.8% | -33.8% | PASS |  |  |
| CEG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $885M | bars: $964,740,183 | PASS | LOW |  |
| CGY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $81.56 | $81.56 | PASS |  |  |
| CGY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $95.15 / $44.20 | $95.15 / $44.20 | PASS |  |  |
| CGY.TO | PD3 | % from High | -14.3% | -14.3% | PASS |  |  |
| CGY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,463,212 | PASS | LOW |  |
| CNQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $78.60 | $78.60 | PASS |  |  |
| CNQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $64.10 | $64.10 | PASS |  |  |
| CNQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $78.60 / $40.51 | $78.60 / $40.51 | PASS |  |  |
| CNQ.TO | PD3 | % from High | -18.4% | -18.4% | PASS |  |  |
| CNQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $870M | bars: $766,775,809 | PASS | LOW |  |
| CNR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $184.26 | $184.26 | PASS |  |  |
| CNR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $178.66 | $178.66 | PASS |  |  |
| CNR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $184.26 / $125.06 | $184.26 / $125.06 | PASS |  |  |
| CNR.TO | PD3 | % from High | -3.0% | -3.0% | PASS |  |  |
| CNR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $228M | bars: $217,112,102 | PASS | LOW |  |
| COP | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $153.27 | $153.27 | PASS |  |  |
| COP | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $134.99 | $134.99 | PASS |  |  |
| COP | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $153.27 / $83.30 | $153.27 / $83.30 | PASS |  |  |
| COP | PD3 | % from High | -11.9% | -11.9% | PASS |  |  |
| COP | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $917M | bars: $928,433,847 | PASS | LOW |  |
| COPP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $70.54 | $70.54 | PASS |  |  |
| COPP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $41.83 | $41.83 | PASS |  |  |
| COPP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $70.54 / $41.80 | $70.54 / $41.80 | PASS |  |  |
| COPP.TO | PD3 | % from High | -40.7% | -40.7% | PASS |  |  |
| COPX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $99.65 | $99.65 | PASS |  |  |
| COPX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $59.28 | $59.28 | PASS |  |  |
| COPX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $99.65 / $55.44 | $99.65 / $55.44 | PASS |  |  |
| COPX | PD3 | % from High | -40.5% | -40.5% | PASS |  |  |
| COPX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $179M | bars: $175,465,378 | PASS | LOW |  |
| COPZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $7.06 | $7.06 | PASS |  |  |
| COPZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $26.40 / $7.06 | $26.40 / $7.06 | PASS |  |  |
| COPZ | PD3 | % from High | -73.3% | -73.3% | PASS |  |  |
| COST | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,123.67 | $1,123.67 | PASS |  |  |
| COST | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,093.83 | $1,093.83 | PASS |  |  |
| COST | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,123.67 / $844.06 | $1,123.67 / $844.06 | PASS |  |  |
| COST | PD3 | % from High | -2.7% | -2.7% | PASS |  |  |
| COST | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.5B | bars: $2,589,169,378 | PASS | LOW |  |
| COTG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $17.80 | $17.80 | PASS |  |  |
| COTG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $16.45 | $16.45 | PASS |  |  |
| COTG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $17.80 / $10.95 | $17.80 / $10.95 | PASS |  |  |
| COTG | PD3 | % from High | -7.6% | -7.6% | PASS |  |  |
| COTG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,725,654 | PASS | LOW |  |
| CSU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $3,565.00 | $3,565.00 | PASS |  |  |
| CSU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3,180.00 | $3,180.00 | PASS |  |  |
| CSU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $3,565.00 / $2,192.51 | $3,565.00 / $2,192.51 | PASS |  |  |
| CSU.TO | PD3 | % from High | -10.8% | -10.8% | PASS |  |  |
| CSU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $191M | bars: $195,343,457 | PASS | LOW |  |
| CVX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $236.48 | $236.48 | PASS |  |  |
| CVX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $206.50 | $206.50 | PASS |  |  |
| CVX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $236.48 / $146.49 | $236.48 / $146.49 | PASS |  |  |
| CVX | PD3 | % from High | -12.7% | -12.7% | PASS |  |  |
| CVX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.8B | bars: $1,805,968,655 | PASS | LOW |  |
| DRAL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3.99 | $3.99 | PASS |  |  |
| DRAL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $25.52 / $3.73 | $25.52 / $3.73 | PASS |  |  |
| DRAL | PD3 | % from High | -84.4% | -84.4% | PASS |  |  |
| DRAM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $38.43 | $38.43 | PASS |  |  |
| DRAM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $81.34 / $26.14 | $81.34 / $26.14 | PASS |  |  |
| DRAM | PD3 | % from High | -52.8% | -52.8% | PASS |  |  |
| DRAM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.3B | bars: $1,344,793,404 | PASS | LOW |  |
| DRIV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $42.67 | $42.67 | PASS |  |  |
| DRIV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $26.26 | $26.26 | PASS |  |  |
| DRIV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $42.67 / $26.26 | $42.67 / $26.26 | PASS |  |  |
| DRIV | PD3 | % from High | -38.5% | -38.5% | PASS |  |  |
| DUK | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $134.49 | $134.49 | PASS |  |  |
| DUK | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $128.86 | $128.86 | PASS |  |  |
| DUK | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $134.49 / $112.40 | $134.49 / $112.40 | PASS |  |  |
| DUK | PD3 | % from High | -4.2% | -4.2% | PASS |  |  |
| DUK | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $548M | bars: $580,063,916 | PASS | LOW |  |
| ELIL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.56 | $43.56 | PASS |  |  |
| ELIL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $36.57 | $36.57 | PASS |  |  |
| ELIL | PD3 | % from High | -16.0% | -16.0% | PASS |  |  |
| ELIL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $2,269,904 | PASS | LOW |  |
| EQIX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,112.65 | $1,112.65 | PASS |  |  |
| EQIX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,018.45 | $1,018.45 | PASS |  |  |
| EQIX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,112.65 / $706.18 | $1,112.65 / $706.18 | PASS |  |  |
| EQIX | PD3 | % from High | -8.5% | -8.5% | PASS |  |  |
| EQIX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $583M | bars: $612,146,237 | PASS | LOW |  |
| ETN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $478.00 | $478.00 | PASS |  |  |
| ETN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $330.57 | $330.57 | PASS |  |  |
| ETN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $478.00 / $311.92 | $478.00 / $311.92 | PASS |  |  |
| ETN | PD3 | % from High | -30.8% | -30.8% | PASS |  |  |
| ETN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $813M | bars: $889,011,382 | PASS | LOW |  |
| FCX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.24 | $80.24 | PASS |  |  |
| FCX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $49.12 | $49.12 | PASS |  |  |
| FCX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.24 / $38.85 | $80.24 / $38.85 | PASS |  |  |
| FCX | PD3 | % from High | -38.8% | -38.8% | PASS |  |  |
| FCX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $636M | bars: $602,702,736 | PASS | LOW |  |
| GDX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $117.18 | $117.18 | PASS |  |  |
| GDX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $72.00 | $72.00 | PASS |  |  |
| GDX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $117.18 / $69.74 | $117.18 / $69.74 | PASS |  |  |
| GDX | PD3 | % from High | -38.6% | -38.6% | PASS |  |  |
| GDX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,595,081,742 | PASS | LOW |  |
| GDXU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $65.00 | $65.00 | PASS |  |  |
| GDXU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $20.35 | $20.35 | PASS |  |  |
| GDXU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $65.00 / $20.31 | $65.00 / $20.31 | PASS |  |  |
| GDXU.TO | PD3 | % from High | -68.7% | -68.7% | PASS |  |  |
| GDXU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5M | bars: $5,067,454 | PASS | LOW |  |
| GE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $388.25 | $388.25 | PASS |  |  |
| GE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $318.88 | $318.88 | PASS |  |  |
| GE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $388.25 / $268.17 | $388.25 / $268.17 | PASS |  |  |
| GE | PD3 | % from High | -17.9% | -17.9% | PASS |  |  |
| GE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.4B | bars: $1,548,698,839 | PASS | LOW |  |
| GEV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,195.24 | $1,195.24 | PASS |  |  |
| GEV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $756.28 | $756.28 | PASS |  |  |
| GEV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,195.24 / $528.87 | $1,195.24 / $528.87 | PASS |  |  |
| GEV | PD3 | % from High | -36.7% | -36.7% | PASS |  |  |
| GEV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,422,845,804 | PASS | LOW |  |
| GEV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $50.60 | $50.60 | PASS |  |  |
| GEV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.44 / $42.23 | $80.44 / $42.23 | PASS |  |  |
| GEV.TO | PD3 | % from High | -37.1% | -37.1% | PASS |  |  |
| GEV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,910,025 | PASS | LOW |  |
| GGLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $151.33 | $151.33 | PASS |  |  |
| GGLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $59.74 | $59.74 | PASS |  |  |
| GGLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $151.33 / $59.64 | $151.33 / $59.64 | PASS |  |  |
| GGLL | PD3 | % from High | -60.5% | -60.5% | PASS |  |  |
| GGLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $102M | bars: $115,412,689 | PASS | LOW |  |
| GIB-A.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.27 | $131.27 | PASS |  |  |
| GIB-A.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $112.41 | $112.41 | PASS |  |  |
| GIB-A.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.27 / $83.04 | $131.27 / $83.04 | PASS |  |  |
| GIB-A.TO | PD3 | % from High | -14.4% | -14.4% | PASS |  |  |
| GIB-A.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $67M | bars: $69,923,346 | PASS | LOW |  |
| GOOGL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $408.10 | $408.10 | PASS |  |  |
| GOOGL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $272.66 | $272.66 | PASS |  |  |
| GOOGL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $408.10 / $271.77 | $408.10 / $271.77 | PASS |  |  |
| GOOGL | PD3 | % from High | -33.2% | -33.2% | PASS |  |  |
| GOOGL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.3B | bars: $8,884,812,621 | PASS | LOW |  |
| GRID | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $198.79 | $198.79 | PASS |  |  |
| GRID | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $152.42 | $152.42 | PASS |  |  |
| GRID | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $198.79 / $143.36 | $198.79 / $143.36 | PASS |  |  |
| GRID | PD3 | % from High | -23.3% | -23.3% | PASS |  |  |
| GRID | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $89M | bars: $94,041,579 | PASS | LOW |  |
| HD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $389.18 | $389.18 | PASS |  |  |
| HD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $336.68 | $336.68 | PASS |  |  |
| HD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.18 / $277.15 | $389.18 / $277.15 | PASS |  |  |
| HD | PD3 | % from High | -13.5% | -13.5% | PASS |  |  |
| HD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,711,673,949 | PASS | LOW |  |
| HURA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $73.95 | $73.95 | PASS |  |  |
| HURA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $35.85 | $35.85 | PASS |  |  |
| HURA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $73.95 / $35.75 | $73.95 / $35.75 | PASS |  |  |
| HURA.TO | PD3 | % from High | -51.5% | -51.5% | PASS |  |  |
| HXQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $109.61 | $109.61 | PASS |  |  |
| HXQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $128.37 / $91.48 | $128.37 / $91.48 | PASS |  |  |
| HXQ.TO | PD3 | % from High | -14.6% | -14.6% | PASS |  |  |
| HXQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,692,616 | PASS | LOW |  |
| JNJ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $290.25 | $290.25 | PASS |  |  |
| JNJ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $267.14 | $267.14 | PASS |  |  |
| JNJ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $290.25 / $194.99 | $290.25 / $194.99 | PASS |  |  |
| JNJ | PD3 | % from High | -8.0% | -8.0% | PASS |  |  |
| JNJ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.9B | bars: $1,993,900,283 | PASS | LOW |  |
| JPM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $364.68 | $364.68 | PASS |  |  |
| JPM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $320.22 | $320.22 | PASS |  |  |
| JPM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $364.68 / $275.06 | $364.68 / $275.06 | PASS |  |  |
| JPM | PD3 | % from High | -12.2% | -12.2% | PASS |  |  |
| JPM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.3B | bars: $2,454,548,743 | PASS | LOW |  |
| KEYS | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $389.93 | $389.93 | PASS |  |  |
| KEYS | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $281.42 | $281.42 | PASS |  |  |
| KEYS | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.93 / $167.23 | $389.93 / $167.23 | PASS |  |  |
| KEYS | PD3 | % from High | -27.8% | -27.8% | PASS |  |  |
| KEYS | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $363M | bars: $381,200,928 | PASS | LOW |  |
| LIN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $548.20 | $548.20 | PASS |  |  |
| LIN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $510.21 | $510.21 | PASS |  |  |
| LIN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $548.20 / $387.78 | $548.20 / $387.78 | PASS |  |  |
| LIN | PD3 | % from High | -6.9% | -6.9% | PASS |  |  |
| LIN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.0B | bars: $1,064,463,082 | PASS | LOW |  |
| LLY | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,475.25 | $1,475.25 | PASS |  |  |
| LLY | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,351.12 | $1,351.12 | PASS |  |  |
| LLY | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,475.25 / $850.51 | $1,475.25 / $850.51 | PASS |  |  |
| LLY | PD3 | % from High | -8.4% | -8.4% | PASS |  |  |
| LLY | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.5B | bars: $3,553,429,224 | PASS | LOW |  |
| MDA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $67.90 | $67.90 | PASS |  |  |
| MDA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $38.44 | $38.44 | PASS |  |  |
| MDA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $67.90 / $21.88 | $67.90 / $21.88 | PASS |  |  |
| MDA.TO | PD3 | % from High | -43.4% | -43.4% | PASS |  |  |
| MDA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $60M | bars: $60,960,641 | PASS | LOW |  |
| META | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $779.82 | $779.82 | PASS |  |  |
| META | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $596.22 | $596.22 | PASS |  |  |
| META | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $779.82 / $520.26 | $779.82 / $520.26 | PASS |  |  |
| META | PD3 | % from High | -23.5% | -23.5% | PASS |  |  |
| META | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $12.4B | bars: $12,848,768,088 | PASS | LOW |  |
| METU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $39.74 | $39.74 | PASS |  |  |
| METU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $20.01 | $20.01 | PASS |  |  |
| METU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $39.74 / $16.85 | $39.74 / $16.85 | PASS |  |  |
| METU | PD3 | % from High | -49.6% | -49.6% | PASS |  |  |
| METU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $105M | bars: $93,617,215 | PASS | LOW |  |
| MRVL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $329.88 | $329.88 | PASS |  |  |
| MRVL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $138.47 | $138.47 | PASS |  |  |
| MRVL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $329.88 / $70.69 | $329.88 / $70.69 | PASS |  |  |
| MRVL | PD3 | % from High | -58.0% | -58.0% | PASS |  |  |
| MRVL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.4B | bars: $3,379,885,653 | PASS | LOW |  |
| MSFT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $559.15 | $559.15 | PASS |  |  |
| MSFT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $498.30 | $498.30 | PASS |  |  |
| MSFT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $559.15 / $348.54 | $559.15 / $348.54 | PASS |  |  |
| MSFT | PD3 | % from High | -10.9% | -10.9% | PASS |  |  |
| MSFT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $11.6B | bars: $12,052,869,358 | PASS | LOW |  |
| MSFU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $45.88 | $45.88 | PASS |  |  |
| MSFU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $36.29 | $36.29 | PASS |  |  |
| MSFU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $45.88 / $19.32 | $45.88 / $19.32 | PASS |  |  |
| MSFU | PD3 | % from High | -20.9% | -20.9% | PASS |  |  |
| MSFU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $90M | bars: $88,204,282 | PASS | LOW |  |
| MTRX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $28.17 | $28.17 | PASS |  |  |
| MTRX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $39.30 / $28.00 | $39.30 / $28.00 | PASS |  |  |
| MTRX.TO | PD3 | % from High | -28.3% | -28.3% | PASS |  |  |
| MU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $55.28 | $55.28 | PASS |  |  |
| MU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.13 | $30.13 | PASS |  |  |
| MU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $55.28 / $8.62 | $55.28 / $8.62 | PASS |  |  |
| MU.TO | PD3 | % from High | -45.5% | -45.5% | PASS |  |  |
| MU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $53M | bars: $56,809,696 | PASS | LOW |  |
| NEE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $98.75 | $98.75 | PASS |  |  |
| NEE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $83.79 | $83.79 | PASS |  |  |
| NEE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $98.75 / $74.41 | $98.75 / $74.41 | PASS |  |  |
| NEE | PD3 | % from High | -15.1% | -15.1% | PASS |  |  |
| NEE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.0B | bars: $1,058,915,791 | PASS | LOW |  |
| NEM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $135.29 | $135.29 | PASS |  |  |
| NEM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $100.05 | $100.05 | PASS |  |  |
| NEM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $135.29 / $81.34 | $135.29 / $81.34 | PASS |  |  |
| NEM | PD3 | % from High | -26.0% | -26.0% | PASS |  |  |
| NEM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $694M | bars: $653,818,474 | PASS | LOW |  |
| NFLX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $113.34 | $113.34 | PASS |  |  |
| NFLX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $58.46 | $58.46 | PASS |  |  |
| NFLX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $113.34 / $58.19 | $113.34 / $58.19 | PASS |  |  |
| NFLX | PD3 | % from High | -48.4% | -48.4% | PASS |  |  |
| NFLX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,343,527,004 | PASS | LOW |  |
| NFXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $45.02 | $45.02 | PASS |  |  |
| NFXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $9.45 | $9.45 | PASS |  |  |
| NFXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $45.02 / $9.36 | $45.02 / $9.36 | PASS |  |  |
| NFXL | PD3 | % from High | -79.0% | -79.0% | PASS |  |  |
| NFXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $14M | bars: $15,835,801 | PASS | LOW |  |
| NTR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $114.19 | $114.19 | PASS |  |  |
| NTR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $94.00 | $94.00 | PASS |  |  |
| NTR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $114.19 / $74.44 | $114.19 / $74.44 | PASS |  |  |
| NTR.TO | PD3 | % from High | -17.7% | -17.7% | PASS |  |  |
| NTR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $170M | bars: $177,188,269 | PASS | LOW |  |
| NVDA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $243.37 | $243.37 | PASS |  |  |
| NVDA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $145.98 | $145.98 | PASS |  |  |
| NVDA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $243.37 / $145.71 | $243.37 / $145.71 | PASS |  |  |
| NVDA | PD3 | % from High | -40.0% | -40.0% | PASS |  |  |
| NVDA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $23.1B | bars: $24,429,325,430 | PASS | LOW |  |
| NVDL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.27 | $43.27 | PASS |  |  |
| NVDL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $14.25 | $14.25 | PASS |  |  |
| NVDL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.27 / $14.19 | $43.27 / $14.19 | PASS |  |  |
| NVDL | PD3 | % from High | -67.1% | -67.1% | PASS |  |  |
| NVDL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $263M | bars: $277,402,149 | PASS | LOW |  |
| ONTO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $386.46 | $386.46 | PASS |  |  |
| ONTO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $195.93 | $195.93 | PASS |  |  |
| ONTO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $386.46 / $121.57 | $386.46 / $121.57 | PASS |  |  |
| ONTO | PD3 | % from High | -49.3% | -49.3% | PASS |  |  |
| ONTO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $196M | bars: $205,907,716 | PASS | LOW |  |
| ORBX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $14.39 | $14.39 | PASS |  |  |
| ORBX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.62 / $12.81 | $31.62 / $12.81 | PASS |  |  |
| ORBX.TO | PD3 | % from High | -54.5% | -54.5% | PASS |  |  |
| ORCL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $248.46 | $248.46 | PASS |  |  |
| ORCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $110.57 | $110.57 | PASS |  |  |
| ORCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $248.46 / $109.21 | $248.46 / $109.21 | PASS |  |  |
| ORCL | PD3 | % from High | -55.5% | -55.5% | PASS |  |  |
| ORCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.7B | bars: $3,966,336,461 | PASS | LOW |  |
| PG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $173.59 | $173.59 | PASS |  |  |
| PG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $167.85 | $167.85 | PASS |  |  |
| PG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $173.59 / $133.74 | $173.59 / $133.74 | PASS |  |  |
| PG | PD3 | % from High | -3.3% | -3.3% | PASS |  |  |
| PG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,573,234,934 | PASS | LOW |  |
| PLD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $152.14 | $152.14 | PASS |  |  |
| PLD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $123.36 | $123.36 | PASS |  |  |
| PLD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $152.14 / $117.70 | $152.14 / $117.70 | PASS |  |  |
| PLD | PD3 | % from High | -18.9% | -18.9% | PASS |  |  |
| PLD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $455M | bars: $477,842,302 | PASS | LOW |  |
| PNG.V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $10.72 | $10.72 | PASS |  |  |
| PNG.V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $2.88 | $2.88 | PASS |  |  |
| PNG.V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $10.72 / $2.88 | $10.72 / $2.88 | PASS |  |  |
| PNG.V | PD3 | % from High | -73.1% | -73.1% | PASS |  |  |
| PNG.V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $3,483,506 | PASS | LOW |  |
| QCOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $259.92 | $259.92 | PASS |  |  |
| QCOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $162.01 | $162.01 | PASS |  |  |
| QCOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $259.92 / $121.99 | $259.92 / $121.99 | PASS |  |  |
| QCOM | PD3 | % from High | -37.7% | -37.7% | PASS |  |  |
| QCOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.1B | bars: $2,133,261,572 | PASS | LOW |  |
| QPUX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.28 | $80.28 | PASS |  |  |
| QPUX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $2.86 | $2.86 | PASS |  |  |
| QPUX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.28 / $2.86 | $80.28 / $2.86 | PASS |  |  |
| QPUX | PD3 | % from High | -96.4% | -96.4% | PASS |  |  |
| QTUM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $169.21 | $169.21 | PASS |  |  |
| QTUM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $119.71 | $119.71 | PASS |  |  |
| QTUM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $169.21 / $97.17 | $169.21 / $97.17 | PASS |  |  |
| QTUM | PD3 | % from High | -29.3% | -29.3% | PASS |  |  |
| QTUM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $39M | bars: $40,695,666 | PASS | LOW |  |
| RBOT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.15 | $38.15 | PASS |  |  |
| RBOT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $27.09 | $27.09 | PASS |  |  |
| RBOT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.15 / $27.00 | $38.15 / $27.00 | PASS |  |  |
| RBOT.TO | PD3 | % from High | -29.0% | -29.0% | PASS |  |  |
| RTX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $226.88 | $226.88 | PASS |  |  |
| RTX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $193.44 | $193.44 | PASS |  |  |
| RTX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $226.88 / $166.74 | $226.88 / $166.74 | PASS |  |  |
| RTX | PD3 | % from High | -14.7% | -14.7% | PASS |  |  |
| RTX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $898M | bars: $949,341,828 | PASS | LOW |  |
| RY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.65 | $302.65 | PASS |  |  |
| RY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $269.45 | $269.45 | PASS |  |  |
| RY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.65 / $201.71 | $302.65 / $201.71 | PASS |  |  |
| RY.TO | PD3 | % from High | -11.0% | -11.0% | PASS |  |  |
| RY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $863M | bars: $901,053,254 | PASS | LOW |  |
| SETM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $40.55 | $40.55 | PASS |  |  |
| SETM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $20.64 | $20.64 | PASS |  |  |
| SETM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $40.55 / $20.60 | $40.55 / $20.60 | PASS |  |  |
| SETM | PD3 | % from High | -49.1% | -49.1% | PASS |  |  |
| SETM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,693,557 | PASS | LOW |  |
| SGRD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.69 | $17.69 | PASS |  |  |
| SGRD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $22.49 / $17.20 | $22.49 / $17.20 | PASS |  |  |
| SGRD.TO | PD3 | % from High | -21.3% | -21.3% | PASS |  |  |
| SMH | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $671.83 | $671.83 | PASS |  |  |
| SMH | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $447.48 | $447.48 | PASS |  |  |
| SMH | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $671.83 / $314.07 | $671.83 / $314.07 | PASS |  |  |
| SMH | PD3 | % from High | -33.4% | -33.4% | PASS |  |  |
| SMH | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.9B | bars: $4,192,994,458 | PASS | LOW |  |
| SNDK.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $18.35 | $18.35 | PASS |  |  |
| SNDK.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $57.55 / $18.14 | $57.55 / $18.14 | PASS |  |  |
| SNDK.TO | PD3 | % from High | -68.1% | -68.1% | PASS |  |  |
| SNDK.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $23M | bars: $23,547,204 | PASS | LOW |  |
| SO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $97.65 | $97.65 | PASS |  |  |
| SO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $93.29 | $93.29 | PASS |  |  |
| SO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $97.65 / $81.03 | $97.65 / $81.03 | PASS |  |  |
| SO | PD3 | % from High | -4.5% | -4.5% | PASS |  |  |
| SO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $655M | bars: $679,724,648 | PASS | LOW |  |
| SOXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $301.80 | $301.80 | PASS |  |  |
| SOXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $45.30 | $45.30 | PASS |  |  |
| SOXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $301.80 / $28.10 | $301.80 / $28.10 | PASS |  |  |
| SOXL | PD3 | % from High | -85.0% | -85.0% | PASS |  |  |
| SOXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.9B | bars: $5,813,031,011 | PASS | LOW |  |
| SOXL.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $74.21 | $74.21 | PASS |  |  |
| SOXL.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $11.42 | $11.42 | PASS |  |  |
| SOXL.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $74.21 / $7.92 | $74.21 / $7.92 | PASS |  |  |
| SOXL.NE | PD3 | % from High | -84.6% | -84.6% | PASS |  |  |
| SOXL.NE | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| SOXX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $218.51 | $218.51 | PASS |  |  |
| SOXX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $137.95 | $137.95 | PASS |  |  |
| SOXX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $218.51 / $86.54 | $218.51 / $86.54 | PASS |  |  |
| SOXX | PD3 | % from High | -36.9% | -36.9% | PASS |  |  |
| SOXX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.9B | bars: $4,213,903,100 | PASS | LOW |  |
| SPCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $8.91 | $8.91 | PASS |  |  |
| SPCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $83.85 / $8.20 | $83.85 / $8.20 | PASS |  |  |
| SPCL | PD3 | % from High | -89.4% | -89.4% | PASS |  |  |
| TSLA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $498.83 | $498.83 | PASS |  |  |
| TSLA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $374.41 | $374.41 | PASS |  |  |
| TSLA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $498.83 / $297.38 | $498.83 / $297.38 | PASS |  |  |
| TSLA | PD3 | % from High | -24.9% | -24.9% | PASS |  |  |
| TSLA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $14.0B | bars: $13,477,342,034 | PASS | LOW |  |
| TSLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $23.10 | $23.10 | PASS |  |  |
| TSLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $9.53 | $9.53 | PASS |  |  |
| TSLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $23.10 / $6.65 | $23.10 / $6.65 | PASS |  |  |
| TSLL | PD3 | % from High | -58.7% | -58.7% | PASS |  |  |
| TSLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $615M | bars: $515,238,982 | PASS | LOW |  |
| TSM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $487.47 | $487.47 | PASS |  |  |
| TSM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $352.09 | $352.09 | PASS |  |  |
| TSM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $487.47 / $264.03 | $487.47 / $264.03 | PASS |  |  |
| TSM | PD3 | % from High | -27.8% | -27.8% | PASS |  |  |
| TSM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.2B | bars: $4,557,092,744 | PASS | LOW |  |
| UBOT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $31.91 | $31.91 | PASS |  |  |
| UBOT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $14.34 | $14.34 | PASS |  |  |
| UBOT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.91 / $14.33 | $31.91 / $14.33 | PASS |  |  |
| UBOT | PD3 | % from High | -55.1% | -55.1% | PASS |  |  |
| UFO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $68.12 | $68.12 | PASS |  |  |
| UFO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $37.97 | $37.97 | PASS |  |  |
| UFO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $68.12 / $30.78 | $68.12 / $30.78 | PASS |  |  |
| UFO | PD3 | % from High | -44.3% | -44.3% | PASS |  |  |
| UFO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $9M | bars: $9,572,697 | PASS | LOW |  |
| URA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $62.28 | $62.28 | PASS |  |  |
| URA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $28.66 | $28.66 | PASS |  |  |
| URA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $62.28 / $28.60 | $62.28 / $28.60 | PASS |  |  |
| URA | PD3 | % from High | -54.0% | -54.0% | PASS |  |  |
| URA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $114M | bars: $118,146,462 | PASS | LOW |  |
| URAA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $62.21 | $62.21 | PASS |  |  |
| URAA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $10.37 | $10.37 | PASS |  |  |
| URAA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $62.21 / $10.35 | $62.21 / $10.35 | PASS |  |  |
| URAA | PD3 | % from High | -83.3% | -83.3% | PASS |  |  |
| V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $442.23 | $442.23 | PASS |  |  |
| V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $402.25 | $402.25 | PASS |  |  |
| V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $442.23 / $293.89 | $442.23 / $293.89 | PASS |  |  |
| V | PD3 | % from High | -9.0% | -9.0% | PASS |  |  |
| V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.6B | bars: $2,680,874,320 | PASS | LOW |  |
| VFV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $182.95 | $182.95 | PASS |  |  |
| VFV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $197.83 / $155.29 | $197.83 / $155.29 | PASS |  |  |
| VFV.TO | PD3 | % from High | -7.5% | -7.5% | PASS |  |  |
| VFV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $55M | bars: $59,067,006 | PASS | LOW |  |
| VRT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $379.76 | $379.76 | PASS |  |  |
| VRT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $184.99 | $184.99 | PASS |  |  |
| VRT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $379.76 / $147.72 | $379.76 / $147.72 | PASS |  |  |
| VRT | PD3 | % from High | -51.3% | -51.3% | PASS |  |  |
| VRT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.1B | bars: $1,228,826,184 | PASS | LOW |  |
| WDC.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.98 | $17.98 | PASS |  |  |
| WDC.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $48.85 / $15.70 | $48.85 / $15.70 | PASS |  |  |
| WDC.TO | PD3 | % from High | -63.2% | -63.2% | PASS |  |  |
| WDC.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,966,833 | PASS | LOW |  |
| WELL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $255.20 | $255.20 | PASS |  |  |
| WELL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $243.19 | $243.19 | PASS |  |  |
| WELL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $255.20 / $181.47 | $255.20 / $181.47 | PASS |  |  |
| WELL | PD3 | % from High | -4.7% | -4.7% | PASS |  |  |
| WELL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $677M | bars: $696,261,803 | PASS | LOW |  |
| WMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $135.16 | $135.16 | PASS |  |  |
| WMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $126.04 | $126.04 | PASS |  |  |
| WMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $135.16 / $99.68 | $135.16 / $99.68 | PASS |  |  |
| WMT | PD3 | % from High | -6.7% | -6.7% | PASS |  |  |
| WMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.0B | bars: $2,793,835,494 | PASS | LOW |  |
| XCHP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $161.26 | $161.26 | PASS |  |  |
| XCHP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $103.19 | $103.19 | PASS |  |  |
| XCHP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $161.26 / $64.67 | $161.26 / $64.67 | PASS |  |  |
| XCHP.TO | PD3 | % from High | -36.0% | -36.0% | PASS |  |  |
| XCHP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5M | bars: $5,452,194 | PASS | LOW |  |
| XDRV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $61.36 | $61.36 | PASS |  |  |
| XDRV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.55 | $39.55 | PASS |  |  |
| XDRV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $61.36 / $38.62 | $61.36 / $38.62 | PASS |  |  |
| XDRV.TO | PD3 | % from High | -35.5% | -35.5% | PASS |  |  |
| XDRV.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| XEQT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $43.28 | $43.28 | PASS |  |  |
| XEQT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.38 / $37.96 | $46.38 / $37.96 | PASS |  |  |
| XEQT.TO | PD3 | % from High | -6.7% | -6.7% | PASS |  |  |
| XEQT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $37M | bars: $40,542,774 | PASS | LOW |  |
| XETM.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $56.19 | $56.19 | PASS |  |  |
| XETM.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $93.94 / $56.19 | $93.94 / $56.19 | PASS |  |  |
| XETM.TO | PD3 | % from High | -40.2% | -40.2% | PASS |  |  |
| XGD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $69.54 | $69.54 | PASS |  |  |
| XGD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $46.79 | $46.79 | PASS |  |  |
| XGD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $69.54 / $43.30 | $69.54 / $43.30 | PASS |  |  |
| XGD.TO | PD3 | % from High | -32.7% | -32.7% | PASS |  |  |
| XGD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $23M | bars: $21,874,660 | PASS | LOW |  |
| XOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $188.50 | $188.50 | PASS |  |  |
| XOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $158.93 | $158.93 | PASS |  |  |
| XOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $188.50 / $114.19 | $188.50 / $114.19 | PASS |  |  |
| XOM | PD3 | % from High | -15.7% | -15.7% | PASS |  |  |
| XOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,145,966,076 | PASS | LOW |  |
| AAPL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $349.21 / RS 1.20 | $349.21 / RS 1.20 | PASS |  |  |
| AAPL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.20 | 1.20 | PASS |  |  |
| AAPL | RS2 | Stock 52W Return and S&P 52W Return | +30.5% / +9.2% | +30.5% / +9.2% | PASS |  |  |
| AAPL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 66 | 66 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| AAPL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +30.5% clears | +30.5% clears | PASS |  |  |
| AAPU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $47.68 / RS 1.34 | $47.68 / RS 1.34 | PASS |  |  |
| AAPU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.34 | 1.34 | PASS |  |  |
| AAPU | RS2 | Stock 52W Return and S&P 52W Return | +45.9% / +9.2% | +45.9% / +9.2% | PASS |  |  |
| AAPU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 77 | 77 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market | Well ahead of the market | PASS |  |  |
| AAPU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +45.9% clears | +45.9% clears | PASS |  |  |
| ABBV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $283.54 / RS 1.15 | $283.54 / RS 1.15 | PASS |  |  |
| ABBV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| ABBV | RS2 | Stock 52W Return and S&P 52W Return | +25.4% / +9.2% | +25.4% / +9.2% | PASS |  |  |
| ABBV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ABBV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ABBV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| ABBV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.4% clears | +25.4% clears | PASS |  |  |
| AIPO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $22.08 / RS 0.90 | $22.08 / RS 0.90 | PASS |  |  |
| AIPO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| AIPO | RS2 | Stock 52W Return and S&P 52W Return | -2.2% / +9.2% | -2.2% / +9.2% | PASS |  |  |
| AIPO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AIPO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AIPO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| AIPO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -2.2% negative | -2.2% negative | PASS |  |  |
| ALAB | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $211.60 / RS 1.36 | $211.60 / RS 1.36 | PASS |  |  |
| ALAB | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.36 | 1.36 | PASS |  |  |
| ALAB | RS2 | Stock 52W Return and S&P 52W Return | +49.0% / +9.2% | +49.0% / +9.2% | PASS |  |  |
| ALAB | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ALAB | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 79 | 79 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ALAB | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ALAB | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.0% clears | +49.0% clears | PASS |  |  |
| AMD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $489.19 / RS 2.00 | $489.19 / RS 2.00 | PASS |  |  |
| AMD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.00 | 2.00 | PASS |  |  |
| AMD | RS2 | Stock 52W Return and S&P 52W Return | +118.8% / +9.2% | +118.8% / +9.2% | PASS |  |  |
| AMD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +118.8% clears | +118.8% clears | PASS |  |  |
| AMD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.59 / RS 1.95 | $12.59 / RS 1.95 | PASS |  |  |
| AMD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.95 | 1.95 | PASS |  |  |
| AMD.TO | RS2 | Stock 52W Return and S&P 52W Return | +113.4% / +9.2% | +113.4% / +9.2% | PASS |  |  |
| AMD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +113.4% clears | +113.4% clears | PASS |  |  |
| AMZN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $257.37 / RS 1.06 | $257.37 / RS 1.06 | PASS |  |  |
| AMZN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.06 | 1.06 | PASS |  |  |
| AMZN | RS2 | Stock 52W Return and S&P 52W Return | +15.6% / +9.2% | +15.6% / +9.2% | PASS |  |  |
| AMZN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| AMZN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +15.6% clears | +15.6% clears | PASS |  |  |
| AMZU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $34.95 / RS 0.98 | $34.95 / RS 0.98 | PASS |  |  |
| AMZU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.98 | 0.98 | PASS |  |  |
| AMZU | RS2 | Stock 52W Return and S&P 52W Return | +7.5% / +9.2% | +7.5% / +9.2% | PASS |  |  |
| AMZU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 49 | 49 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| AMZU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +7.5% clears | +7.5% clears | PASS |  |  |
| ANET.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $33.90 / RS 1.30 | $33.90 / RS 1.30 | PASS |  |  |
| ANET.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.30 | 1.30 | PASS |  |  |
| ANET.TO | RS2 | Stock 52W Return and S&P 52W Return | +42.2% / +9.2% | +42.2% / +9.2% | PASS |  |  |
| ANET.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ANET.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ANET.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +42.2% clears | +42.2% clears | PASS |  |  |
| ASML.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $41.25 / RS 1.35 | $41.25 / RS 1.35 | PASS |  |  |
| ASML.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.35 | 1.35 | PASS |  |  |
| ASML.TO | RS2 | Stock 52W Return and S&P 52W Return | +47.6% / +9.2% | +47.6% / +9.2% | PASS |  |  |
| ASML.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASML.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 78 | 78 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASML.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ASML.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +47.6% clears | +47.6% clears | PASS |  |  |
| ASTL.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $6.90 / RS 1.31 | $6.90 / RS 1.31 | PASS |  |  |
| ASTL.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.31 | 1.31 | PASS |  |  |
| ASTL.TO | RS2 | Stock 52W Return and S&P 52W Return | +42.6% / +9.2% | +42.6% / +9.2% | PASS |  |  |
| ASTL.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASTL.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASTL.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ASTL.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +42.6% clears | +42.6% clears | PASS |  |  |
| ATD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $80.14 / RS 1.07 | $80.14 / RS 1.07 | PASS |  |  |
| ATD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.07 | 1.07 | PASS |  |  |
| ATD.TO | RS2 | Stock 52W Return and S&P 52W Return | +17.1% / +9.2% | +17.1% / +9.2% | PASS |  |  |
| ATD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ATD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ATD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| ATD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +17.1% clears | +17.1% clears | PASS |  |  |
| AVGO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $346.55 / RS 0.90 | $346.55 / RS 0.90 | PASS |  |  |
| AVGO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| AVGO | RS2 | Stock 52W Return and S&P 52W Return | -1.5% / +9.2% | -1.5% / +9.2% | PASS |  |  |
| AVGO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AVGO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| AVGO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.5% negative | -1.5% negative | PASS |  |  |
| AVGO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $13.13 / RS 0.91 | $13.13 / RS 0.91 | PASS |  |  |
| AVGO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.91 | 0.91 | PASS |  |  |
| AVGO.TO | RS2 | Stock 52W Return and S&P 52W Return | -0.4% / +9.2% | -0.4% / +9.2% | PASS |  |  |
| AVGO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| AVGO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -0.4% negative | -0.4% negative | PASS |  |  |
| BDT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $71.42 / RS 2.57 | $71.42 / RS 2.57 | PASS |  |  |
| BDT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.57 | 2.57 | PASS |  |  |
| BDT.TO | RS2 | Stock 52W Return and S&P 52W Return | +180.2% / +9.2% | +180.2% / +9.2% | PASS |  |  |
| BDT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BDT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BDT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| BDT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +180.2% clears | +180.2% clears | PASS |  |  |
| BOTZ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $29.00 / RS 0.79 | $29.00 / RS 0.78 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| BOTZ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.79 | 0.78 | PASS |  |  |
| BOTZ | RS2 | Stock 52W Return and S&P 52W Return | -14.3% / +9.2% | -14.3% / +9.2% | PASS |  |  |
| BOTZ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BOTZ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BOTZ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| BOTZ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -14.3% negative | -14.3% negative | PASS |  |  |
| BRK-B | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $572.04 / RS 1.04 | $572.04 / RS 1.05 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| BRK-B | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.04 | 1.05 | PASS |  |  |
| BRK-B | RS2 | Stock 52W Return and S&P 52W Return | +14.1% / +9.2% | +14.1% / +9.2% | PASS |  |  |
| BRK-B | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRK-B | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 54 | 54 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRK-B | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRK-B | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.1% clears | +14.1% clears | PASS |  |  |
| BRKU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $28.55 / RS 1.03 | $28.55 / RS 1.03 | PASS |  |  |
| BRKU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| BRKU | RS2 | Stock 52W Return and S&P 52W Return | +13.0% / +9.2% | +13.0% / +9.2% | PASS |  |  |
| BRKU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRKU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 53 | 53 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRKU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRKU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +13.0% clears | +13.0% clears | PASS |  |  |
| CAMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $97.78 / RS 0.90 | $97.78 / RS 0.90 | PASS |  |  |
| CAMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| CAMT | RS2 | Stock 52W Return and S&P 52W Return | -2.3% / +9.2% | -2.3% / +9.2% | PASS |  |  |
| CAMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| CAMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -2.3% negative | -2.3% negative | PASS |  |  |
| CARS.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $19.88 / RS 0.71 | $19.88 / RS 0.71 | PASS |  |  |
| CARS.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.71 | 0.71 | PASS |  |  |
| CARS.TO | RS2 | Stock 52W Return and S&P 52W Return | -22.4% / +9.2% | -22.4% / +9.2% | PASS |  |  |
| CARS.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CARS.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 27 | 27 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CARS.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CARS.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -22.4% negative | -22.4% negative | PASS |  |  |
| CAT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $537.26 / RS 0.90 | $537.26 / RS 0.90 | PASS |  |  |
| CAT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| CAT | RS2 | Stock 52W Return and S&P 52W Return | -2.0% / +9.2% | -2.0% / +9.2% | PASS |  |  |
| CAT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| CAT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -2.0% negative | -2.0% negative | PASS |  |  |
| CCO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $89.40 / RS 0.70 | $89.40 / RS 0.70 | PASS |  |  |
| CCO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.70 | 0.70 | PASS |  |  |
| CCO.TO | RS2 | Stock 52W Return and S&P 52W Return | -23.1% / +9.2% | -23.1% / +9.2% | PASS |  |  |
| CCO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CCO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 26 | 26 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CCO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| CCO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -23.1% negative | -23.1% negative | PASS |  |  |
| CEG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $252.03 / RS 0.65 | $252.03 / RS 0.65 | PASS |  |  |
| CEG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.65 | PASS |  |  |
| CEG | RS2 | Stock 52W Return and S&P 52W Return | -29.5% / +9.2% | -29.5% / +9.2% | PASS |  |  |
| CEG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CEG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CEG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CEG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -29.5% negative | -29.5% negative | PASS |  |  |
| CGY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $81.56 / RS 1.56 | $81.56 / RS 1.56 | PASS |  |  |
| CGY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.56 | 1.56 | PASS |  |  |
| CGY.TO | RS2 | Stock 52W Return and S&P 52W Return | +70.5% / +9.2% | +70.5% / +9.2% | PASS |  |  |
| CGY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CGY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 95 | 95 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CGY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CGY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +70.5% clears | +70.5% clears | PASS |  |  |
| CNQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $64.10 / RS 1.28 | $64.10 / RS 1.28 | PASS |  |  |
| CNQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.28 | 1.28 | PASS |  |  |
| CNQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +39.8% / +9.2% | +39.8% / +9.2% | PASS |  |  |
| CNQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CNQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.8% clears | +39.8% clears | PASS |  |  |
| CNR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $178.66 / RS 1.27 | $178.66 / RS 1.27 | PASS |  |  |
| CNR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.27 | 1.27 | PASS |  |  |
| CNR.TO | RS2 | Stock 52W Return and S&P 52W Return | +39.1% / +9.2% | +39.1% / +9.2% | PASS |  |  |
| CNR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CNR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.1% clears | +39.1% clears | PASS |  |  |
| COP | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $134.99 / RS 1.45 | $134.99 / RS 1.45 | PASS |  |  |
| COP | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.45 | 1.45 | PASS |  |  |
| COP | RS2 | Stock 52W Return and S&P 52W Return | +57.9% / +9.2% | +57.8% / +9.2% | PASS |  |  |
| COP | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COP | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 86 | 86 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COP | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| COP | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +57.9% clears | +57.8% clears | PASS |  |  |
| COPP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $41.83 / RS 0.87 | $41.83 / RS 0.87 | PASS |  |  |
| COPP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.87 | 0.87 | PASS |  |  |
| COPP.TO | RS2 | Stock 52W Return and S&P 52W Return | -5.4% / +9.2% | -5.4% / +9.2% | PASS |  |  |
| COPP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 39 | 39 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| COPP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.4% negative | -5.4% negative | PASS |  |  |
| COPX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $59.28 / RS 0.93 | $59.28 / RS 0.93 | PASS |  |  |
| COPX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.93 | 0.93 | PASS |  |  |
| COPX | RS2 | Stock 52W Return and S&P 52W Return | +1.7% / +9.2% | +1.7% / +9.2% | PASS |  |  |
| COPX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| COPX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +1.7% under | +1.7% under | PASS |  |  |
| COST | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,093.83 / RS 1.13 | $1,093.83 / RS 1.12 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| COST | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.13 | 1.12 | PASS |  |  |
| COST | RS2 | Stock 52W Return and S&P 52W Return | +22.8% / +9.2% | +22.8% / +9.2% | PASS |  |  |
| COST | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COST | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COST | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| COST | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +22.8% clears | +22.8% clears | PASS |  |  |
| COTG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $16.45 / RS 1.20 | $16.45 / RS 1.20 | PASS |  |  |
| COTG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.20 | 1.20 | PASS |  |  |
| COTG | RS2 | Stock 52W Return and S&P 52W Return | +31.1% / +9.2% | +31.1% / +9.2% | PASS |  |  |
| COTG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COTG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 66 | 66 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COTG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum accelerating) | Ahead of the market (momentum accelerating) | PASS |  |  |
| COTG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +31.1% clears | +31.1% clears | PASS |  |  |
| CSU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3,180.00 / RS 0.91 | $3,180.00 / RS 0.91 | PASS |  |  |
| CSU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.91 | 0.91 | PASS |  |  |
| CSU.TO | RS2 | Stock 52W Return and S&P 52W Return | -0.5% / +9.2% | -0.5% / +9.2% | PASS |  |  |
| CSU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CSU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CSU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| CSU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -0.5% negative | -0.5% negative | PASS |  |  |
| CVX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $206.50 / RS 1.25 | $206.50 / RS 1.25 | PASS |  |  |
| CVX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.25 | PASS |  |  |
| CVX | RS2 | Stock 52W Return and S&P 52W Return | +36.1% / +9.2% | +36.1% / +9.2% | PASS |  |  |
| CVX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CVX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CVX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CVX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +36.1% clears | +36.1% clears | PASS |  |  |
| DRIV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $26.26 / RS 0.85 | $26.26 / RS 0.85 | PASS |  |  |
| DRIV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| DRIV | RS2 | Stock 52W Return and S&P 52W Return | -7.5% / +9.2% | -7.5% / +9.2% | PASS |  |  |
| DRIV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DRIV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DRIV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| DRIV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -7.5% negative | -7.5% negative | PASS |  |  |
| DUK | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $128.86 / RS 0.97 | $128.86 / RS 0.97 | PASS |  |  |
| DUK | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.97 | 0.97 | PASS |  |  |
| DUK | RS2 | Stock 52W Return and S&P 52W Return | +5.4% / +9.2% | +5.4% / +9.2% | PASS |  |  |
| DUK | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DUK | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DUK | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| DUK | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +5.4% clears | +5.4% clears | PASS |  |  |
| ELIL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $36.57 / RS 1.09 | $36.57 / RS 1.09 | PASS |  |  |
| ELIL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| ELIL | RS2 | Stock 52W Return and S&P 52W Return | +19.1% / +9.2% | +19.1% / +9.2% | PASS |  |  |
| ELIL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ELIL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ELIL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| ELIL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +19.1% clears | +19.1% clears | PASS |  |  |
| EQIX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,018.45 / RS 1.24 | $1,018.45 / RS 1.24 | PASS |  |  |
| EQIX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.24 | 1.24 | PASS |  |  |
| EQIX | RS2 | Stock 52W Return and S&P 52W Return | +35.8% / +9.2% | +35.8% / +9.2% | PASS |  |  |
| EQIX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| EQIX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| EQIX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| EQIX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +35.8% clears | +35.8% clears | PASS |  |  |
| ETN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $330.57 / RS 0.88 | $330.57 / RS 0.88 | PASS |  |  |
| ETN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| ETN | RS2 | Stock 52W Return and S&P 52W Return | -4.4% / +9.2% | -4.4% / +9.2% | PASS |  |  |
| ETN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ETN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ETN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| ETN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.4% negative | -4.4% negative | PASS |  |  |
| FCX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $49.12 / RS 1.09 | $49.12 / RS 1.09 | PASS |  |  |
| FCX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| FCX | RS2 | Stock 52W Return and S&P 52W Return | +19.1% / +9.2% | +19.1% / +9.2% | PASS |  |  |
| FCX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FCX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FCX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| FCX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +19.1% clears | +19.1% clears | PASS |  |  |
| GDX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $72.00 / RS 0.87 | $72.00 / RS 0.87 | PASS |  |  |
| GDX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.87 | 0.87 | PASS |  |  |
| GDX | RS2 | Stock 52W Return and S&P 52W Return | -5.1% / +9.2% | -5.1% / +9.2% | PASS |  |  |
| GDX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| GDX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.1% negative | -5.1% negative | PASS |  |  |
| GDXU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $20.35 / RS 0.60 | $20.35 / RS 0.60 | PASS |  |  |
| GDXU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.60 | 0.60 | PASS |  |  |
| GDXU.TO | RS2 | Stock 52W Return and S&P 52W Return | -34.1% / +9.2% | -34.1% / +9.2% | PASS |  |  |
| GDXU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDXU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 18 | 18 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDXU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| GDXU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -34.1% negative | -34.1% negative | PASS |  |  |
| GE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $318.88 / RS 0.98 | $318.88 / RS 0.98 | PASS |  |  |
| GE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.98 | 0.98 | PASS |  |  |
| GE | RS2 | Stock 52W Return and S&P 52W Return | +6.6% / +9.2% | +6.6% / +9.2% | PASS |  |  |
| GE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 48 | 48 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.6% clears | +6.6% clears | PASS |  |  |
| GEV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $756.28 / RS 1.17 | $756.28 / RS 1.17 | PASS |  |  |
| GEV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.17 | 1.17 | PASS |  |  |
| GEV | RS2 | Stock 52W Return and S&P 52W Return | +27.3% / +9.2% | +27.3% / +9.2% | PASS |  |  |
| GEV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GEV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 63 | 63 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| GEV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +27.3% clears | +27.3% clears | PASS |  |  |
| GEV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $50.60 / RS 1.03 | $50.60 / RS 1.03 | PASS |  |  |
| GEV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| GEV.TO | RS2 | Stock 52W Return and S&P 52W Return | +12.4% / +9.2% | +12.4% / +9.2% | PASS |  |  |
| GEV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| GEV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +12.4% clears | +12.4% clears | PASS |  |  |
| GGLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $59.74 / RS 0.64 | $59.74 / RS 0.64 | PASS |  |  |
| GGLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.64 | 0.64 | PASS |  |  |
| GGLL | RS2 | Stock 52W Return and S&P 52W Return | -29.8% / +9.2% | -29.8% / +9.2% | PASS |  |  |
| GGLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GGLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 21 | 21 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GGLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| GGLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -29.8% negative | -29.8% negative | PASS |  |  |
| GIB-A.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $112.41 / RS 0.85 | $112.41 / RS 0.85 | PASS |  |  |
| GIB-A.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| GIB-A.TO | RS2 | Stock 52W Return and S&P 52W Return | -7.0% / +9.2% | -7.0% / +9.2% | PASS |  |  |
| GIB-A.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GIB-A.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GIB-A.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| GIB-A.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -7.0% negative | -7.0% negative | PASS |  |  |
| GOOGL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $272.66 / RS 0.85 | $272.66 / RS 0.86 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| GOOGL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.86 | PASS |  |  |
| GOOGL | RS2 | Stock 52W Return and S&P 52W Return | -6.6% / +9.2% | -6.6% / +9.2% | PASS |  |  |
| GOOGL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GOOGL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GOOGL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| GOOGL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -6.6% negative | -6.6% negative | PASS |  |  |
| GRID | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $152.42 / RS 0.94 | $152.42 / RS 0.94 | PASS |  |  |
| GRID | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| GRID | RS2 | Stock 52W Return and S&P 52W Return | +2.9% / +9.2% | +2.9% / +9.2% | PASS |  |  |
| GRID | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GRID | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GRID | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GRID | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.9% under | +2.9% under | PASS |  |  |
| HD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $336.68 / RS 0.95 | $336.68 / RS 0.95 | PASS |  |  |
| HD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.95 | PASS |  |  |
| HD | RS2 | Stock 52W Return and S&P 52W Return | +3.5% / +9.2% | +3.5% / +9.2% | PASS |  |  |
| HD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| HD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.5% under | +3.5% under | PASS |  |  |
| HURA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $35.85 / RS 0.62 | $35.85 / RS 0.62 | PASS |  |  |
| HURA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.62 | 0.62 | PASS |  |  |
| HURA.TO | RS2 | Stock 52W Return and S&P 52W Return | -32.5% / +9.2% | -32.5% / +9.2% | PASS |  |  |
| HURA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HURA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 19 | 19 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HURA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| HURA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -32.5% negative | -32.5% negative | PASS |  |  |
| HXQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $109.61 / RS 1.01 | $109.61 / RS 1.01 | PASS |  |  |
| HXQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.01 | PASS |  |  |
| HXQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +10.1% / +9.2% | +10.1% / +9.2% | PASS |  |  |
| HXQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HXQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HXQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| HXQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +10.1% clears | +10.1% clears | PASS |  |  |
| JNJ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $267.14 / RS 1.24 | $267.14 / RS 1.24 | PASS |  |  |
| JNJ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.24 | 1.24 | PASS |  |  |
| JNJ | RS2 | Stock 52W Return and S&P 52W Return | +34.9% / +9.2% | +34.9% / +9.2% | PASS |  |  |
| JNJ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JNJ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 69 | 69 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JNJ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| JNJ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +34.9% clears | +34.9% clears | PASS |  |  |
| JPM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $320.22 / RS 0.99 | $320.22 / RS 0.99 | PASS |  |  |
| JPM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.99 | 0.99 | PASS |  |  |
| JPM | RS2 | Stock 52W Return and S&P 52W Return | +7.6% / +9.2% | +7.6% / +9.2% | PASS |  |  |
| JPM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JPM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 49 | 49 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JPM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| JPM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +7.6% clears | +7.6% clears | PASS |  |  |
| KEYS | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $281.42 / RS 1.48 | $281.42 / RS 1.48 | PASS |  |  |
| KEYS | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.48 | 1.48 | PASS |  |  |
| KEYS | RS2 | Stock 52W Return and S&P 52W Return | +61.2% / +9.2% | +61.2% / +9.2% | PASS |  |  |
| KEYS | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| KEYS | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 88 | 88 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| KEYS | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| KEYS | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +61.2% clears | +61.2% clears | PASS |  |  |
| LIN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $510.21 / RS 1.13 | $510.21 / RS 1.13 | PASS |  |  |
| LIN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.13 | 1.13 | PASS |  |  |
| LIN | RS2 | Stock 52W Return and S&P 52W Return | +23.5% / +9.2% | +23.5% / +9.2% | PASS |  |  |
| LIN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LIN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LIN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| LIN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +23.5% clears | +23.5% clears | PASS |  |  |
| LLY | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,351.12 / RS 1.18 | $1,351.12 / RS 1.18 | PASS |  |  |
| LLY | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.18 | 1.18 | PASS |  |  |
| LLY | RS2 | Stock 52W Return and S&P 52W Return | +28.7% / +9.2% | +28.7% / +9.2% | PASS |  |  |
| LLY | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LLY | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LLY | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| LLY | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.7% clears | +28.7% clears | PASS |  |  |
| MDA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $38.44 / RS 1.54 | $38.44 / RS 1.54 | PASS |  |  |
| MDA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.54 | 1.54 | PASS |  |  |
| MDA.TO | RS2 | Stock 52W Return and S&P 52W Return | +68.4% / +9.2% | +68.4% / +9.2% | PASS |  |  |
| MDA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MDA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 93 | 93 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MDA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MDA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +68.4% clears | +68.4% clears | PASS |  |  |
| META | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $596.22 / RS 0.93 | $596.22 / RS 0.93 | PASS |  |  |
| META | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.93 | 0.93 | PASS |  |  |
| META | RS2 | Stock 52W Return and S&P 52W Return | +1.0% / +9.2% | +1.0% / +9.2% | PASS |  |  |
| META | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| META | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| META | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| META | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +1.0% under | +1.0% under | PASS |  |  |
| METU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $20.01 / RS 0.69 | $20.01 / RS 0.69 | PASS |  |  |
| METU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.69 | 0.69 | PASS |  |  |
| METU | RS2 | Stock 52W Return and S&P 52W Return | -24.3% / +9.2% | -24.3% / +9.2% | PASS |  |  |
| METU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| METU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 25 | 25 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| METU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| METU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -24.3% negative | -24.3% negative | PASS |  |  |
| MRVL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $138.47 / RS 1.56 | $138.47 / RS 1.56 | PASS |  |  |
| MRVL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.56 | 1.56 | PASS |  |  |
| MRVL | RS2 | Stock 52W Return and S&P 52W Return | +70.3% / +9.2% | +70.3% / +9.2% | PASS |  |  |
| MRVL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MRVL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 95 | 95 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MRVL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MRVL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +70.3% clears | +70.3% clears | PASS |  |  |
| MSFT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $498.30 / RS 0.94 | $498.30 / RS 0.94 | PASS |  |  |
| MSFT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| MSFT | RS2 | Stock 52W Return and S&P 52W Return | +3.1% / +9.2% | +3.1% / +9.2% | PASS |  |  |
| MSFT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| MSFT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.1% under | +3.1% under | PASS |  |  |
| MSFU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $36.29 / RS 0.80 | $36.29 / RS 0.80 | PASS |  |  |
| MSFU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.80 | 0.80 | PASS |  |  |
| MSFU | RS2 | Stock 52W Return and S&P 52W Return | -13.2% / +9.2% | -13.2% / +9.2% | PASS |  |  |
| MSFU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 34 | 34 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| MSFU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -13.2% negative | -13.2% negative | PASS |  |  |
| MTRX.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $28.17 / RS 0.87 | $28.17 / RS 0.87 | PASS |  |  |
| MTRX.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.87 | 0.87 | PASS |  |  |
| MTRX.TO | RS2 | Stock 52W Return and S&P 52W Return | -5.3% / +9.2% | -5.3% / +9.2% | PASS |  |  |
| MTRX.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 39 | 39 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MTRX.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| MTRX.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.3% negative | -5.3% negative | PASS |  |  |
| MU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.13 / RS 2.73 | $30.13 / RS 2.73 | PASS |  |  |
| MU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.73 | 2.73 | PASS |  |  |
| MU.TO | RS2 | Stock 52W Return and S&P 52W Return | +197.7% / +9.2% | +197.7% / +9.2% | PASS |  |  |
| MU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +197.7% clears | +197.7% clears | PASS |  |  |
| NEE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $83.79 / RS 0.91 | $83.79 / RS 0.91 | PASS |  |  |
| NEE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.91 | 0.91 | PASS |  |  |
| NEE | RS2 | Stock 52W Return and S&P 52W Return | -0.6% / +9.2% | -0.6% / +9.2% | PASS |  |  |
| NEE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| NEE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -0.6% negative | -0.6% negative | PASS |  |  |
| NEM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $100.05 / RS 1.05 | $100.05 / RS 1.05 | PASS |  |  |
| NEM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.05 | 1.05 | PASS |  |  |
| NEM | RS2 | Stock 52W Return and S&P 52W Return | +14.3% / +9.2% | +14.3% / +9.2% | PASS |  |  |
| NEM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 54 | 54 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| NEM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.3% clears | +14.3% clears | PASS |  |  |
| NFLX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $58.46 / RS 0.49 | $58.46 / RS 0.49 | PASS |  |  |
| NFLX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.49 | 0.49 | PASS |  |  |
| NFLX | RS2 | Stock 52W Return and S&P 52W Return | -46.9% / +9.2% | -46.9% / +9.2% | PASS |  |  |
| NFLX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFLX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 9 | 9 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFLX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFLX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -46.9% negative | -46.9% negative | PASS |  |  |
| NFXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $9.45 / RS 0.20 | $9.45 / RS 0.20 | PASS |  |  |
| NFXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.20 | 0.20 | PASS |  |  |
| NFXL | RS2 | Stock 52W Return and S&P 52W Return | -77.7% / +9.2% | -77.7% / +9.2% | PASS |  |  |
| NFXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -77.7% negative | -77.7% negative | PASS |  |  |
| NTR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $94.00 / RS 1.13 | $94.00 / RS 1.13 | PASS |  |  |
| NTR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.13 | 1.13 | PASS |  |  |
| NTR.TO | RS2 | Stock 52W Return and S&P 52W Return | +23.4% / +9.2% | +23.4% / +9.2% | PASS |  |  |
| NTR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NTR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NTR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| NTR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +23.4% clears | +23.4% clears | PASS |  |  |
| NVDA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $145.98 / RS 0.72 | $145.98 / RS 0.72 | PASS |  |  |
| NVDA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.72 | 0.72 | PASS |  |  |
| NVDA | RS2 | Stock 52W Return and S&P 52W Return | -21.6% / +9.2% | -21.5% / +9.2% | PASS |  |  |
| NVDA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 27 | 27 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -21.6% negative | -21.5% negative | PASS |  |  |
| NVDL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $14.25 / RS 0.43 | $14.25 / RS 0.43 | PASS |  |  |
| NVDL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.43 | 0.43 | PASS |  |  |
| NVDL | RS2 | Stock 52W Return and S&P 52W Return | -52.7% / +9.2% | -52.7% / +9.2% | PASS |  |  |
| NVDL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 5 | 5 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NVDL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -52.7% negative | -52.7% negative | PASS |  |  |
| ONTO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $195.93 / RS 1.37 | $195.93 / RS 1.37 | PASS |  |  |
| ONTO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.37 | 1.37 | PASS |  |  |
| ONTO | RS2 | Stock 52W Return and S&P 52W Return | +49.6% / +9.2% | +49.6% / +9.2% | PASS |  |  |
| ONTO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ONTO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 80 | 80 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ONTO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ONTO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.6% clears | +49.6% clears | PASS |  |  |
| ORCL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $110.57 / RS 0.46 | $110.57 / RS 0.46 | PASS |  |  |
| ORCL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.46 | 0.46 | PASS |  |  |
| ORCL | RS2 | Stock 52W Return and S&P 52W Return | -50.3% / +9.2% | -50.3% / +9.2% | PASS |  |  |
| ORCL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ORCL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 6 | 6 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ORCL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| ORCL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -50.3% negative | -50.3% negative | PASS |  |  |
| PG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $167.85 / RS 1.08 | $167.85 / RS 1.08 | PASS |  |  |
| PG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.08 | 1.08 | PASS |  |  |
| PG | RS2 | Stock 52W Return and S&P 52W Return | +17.5% / +9.2% | +17.5% / +9.2% | PASS |  |  |
| PG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| PG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +17.5% clears | +17.5% clears | PASS |  |  |
| PLD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $123.36 / RS 0.95 | $123.36 / RS 0.95 | PASS |  |  |
| PLD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.95 | PASS |  |  |
| PLD | RS2 | Stock 52W Return and S&P 52W Return | +4.0% / +9.2% | +4.0% / +9.2% | PASS |  |  |
| PLD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PLD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PLD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| PLD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.0% under | +4.0% under | PASS |  |  |
| PNG.V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $2.88 / RS 0.50 | $2.88 / RS 0.50 | PASS |  |  |
| PNG.V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.50 | 0.50 | PASS |  |  |
| PNG.V | RS2 | Stock 52W Return and S&P 52W Return | -45.6% / +9.2% | -45.6% / +9.2% | PASS |  |  |
| PNG.V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PNG.V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 10 | 10 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PNG.V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| PNG.V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -45.6% negative | -45.6% negative | PASS |  |  |
| QCOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $162.01 / RS 0.89 | $162.01 / RS 0.89 | PASS |  |  |
| QCOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| QCOM | RS2 | Stock 52W Return and S&P 52W Return | -2.5% / +9.2% | -2.5% / +9.2% | PASS |  |  |
| QCOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QCOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QCOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| QCOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -2.5% negative | -2.5% negative | PASS |  |  |
| QPUX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $2.86 / RS 0.04 | $2.86 / RS 0.04 | PASS |  |  |
| QPUX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.04 | 0.04 | PASS |  |  |
| QPUX | RS2 | Stock 52W Return and S&P 52W Return | -95.3% / +9.2% | -95.3% / +9.2% | PASS |  |  |
| QPUX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QPUX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QPUX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| QPUX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -95.3% negative | -95.3% negative | PASS |  |  |
| QTUM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $119.71 / RS 1.06 | $119.71 / RS 1.06 | PASS |  |  |
| QTUM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.06 | 1.06 | PASS |  |  |
| QTUM | RS2 | Stock 52W Return and S&P 52W Return | +15.7% / +9.2% | +15.7% / +9.2% | PASS |  |  |
| QTUM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QTUM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QTUM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| QTUM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +15.7% clears | +15.7% clears | PASS |  |  |
| RBOT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $27.09 / RS 0.79 | $27.09 / RS 0.79 | PASS |  |  |
| RBOT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.79 | 0.79 | PASS |  |  |
| RBOT.TO | RS2 | Stock 52W Return and S&P 52W Return | -13.4% / +9.2% | -13.5% / +9.2% | PASS |  |  |
| RBOT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RBOT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RBOT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| RBOT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -13.4% negative | -13.5% negative | PASS |  |  |
| RTX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $193.44 / RS 1.02 | $193.44 / RS 1.02 | PASS |  |  |
| RTX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.02 | 1.02 | PASS |  |  |
| RTX | RS2 | Stock 52W Return and S&P 52W Return | +11.3% / +9.2% | +11.3% / +9.2% | PASS |  |  |
| RTX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RTX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RTX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| RTX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +11.3% clears | +11.3% clears | PASS |  |  |
| RY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $269.45 / RS 1.22 | $269.45 / RS 1.21 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| RY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.22 | 1.21 | PASS |  |  |
| RY.TO | RS2 | Stock 52W Return and S&P 52W Return | +32.6% / +9.2% | +32.6% / +9.2% | PASS |  |  |
| RY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| RY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +32.6% clears | +32.6% clears | PASS |  |  |
| SETM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $20.64 / RS 0.72 | $20.64 / RS 0.72 | PASS |  |  |
| SETM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.72 | 0.72 | PASS |  |  |
| SETM | RS2 | Stock 52W Return and S&P 52W Return | -21.9% / +9.2% | -21.8% / +9.2% | PASS |  |  |
| SETM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SETM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 27 | 27 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SETM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| SETM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -21.9% negative | -21.8% negative | PASS |  |  |
| SMH | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $447.48 / RS 1.21 | $447.48 / RS 1.21 | PASS |  |  |
| SMH | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.21 | 1.21 | PASS |  |  |
| SMH | RS2 | Stock 52W Return and S&P 52W Return | +32.2% / +9.2% | +32.2% / +9.2% | PASS |  |  |
| SMH | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SMH | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SMH | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| SMH | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +32.2% clears | +32.2% clears | PASS |  |  |
| SO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $93.29 / RS 0.99 | $93.29 / RS 0.99 | PASS |  |  |
| SO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.99 | 0.99 | PASS |  |  |
| SO | RS2 | Stock 52W Return and S&P 52W Return | +8.2% / +9.2% | +8.2% / +9.2% | PASS |  |  |
| SO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 49 | 49 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| SO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +8.2% clears | +8.2% clears | PASS |  |  |
| SOXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $45.30 / RS 1.15 | $45.30 / RS 1.15 | PASS |  |  |
| SOXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| SOXL | RS2 | Stock 52W Return and S&P 52W Return | +26.0% / +9.2% | +26.0% / +9.2% | PASS |  |  |
| SOXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +26.0% clears | +26.0% clears | PASS |  |  |
| SOXL.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $11.42 / RS 1.19 | $11.42 / RS 1.19 | PASS |  |  |
| SOXL.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.19 | 1.19 | PASS |  |  |
| SOXL.NE | RS2 | Stock 52W Return and S&P 52W Return | +29.5% / +9.2% | +29.5% / +9.2% | PASS |  |  |
| SOXL.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 65 | 65 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.5% clears | +29.5% clears | PASS |  |  |
| SOXX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $137.95 / RS 1.35 | $137.95 / RS 1.35 | PASS |  |  |
| SOXX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.35 | 1.35 | PASS |  |  |
| SOXX | RS2 | Stock 52W Return and S&P 52W Return | +47.4% / +9.2% | +47.4% / +9.2% | PASS |  |  |
| SOXX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 78 | 78 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| SOXX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +47.4% clears | +47.4% clears | PASS |  |  |
| TSLA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $374.41 / RS 0.85 | $374.41 / RS 0.85 | PASS |  |  |
| TSLA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| TSLA | RS2 | Stock 52W Return and S&P 52W Return | -7.3% / +9.2% | -7.3% / +9.2% | PASS |  |  |
| TSLA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| TSLA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -7.3% negative | -7.3% negative | PASS |  |  |
| TSLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $9.53 / RS 0.56 | $9.53 / RS 0.56 | PASS |  |  |
| TSLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.56 | 0.56 | PASS |  |  |
| TSLL | RS2 | Stock 52W Return and S&P 52W Return | -38.9% / +9.2% | -38.9% / +9.2% | PASS |  |  |
| TSLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 15 | 15 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| TSLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -38.9% negative | -38.9% negative | PASS |  |  |
| TSM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $352.09 / RS 1.15 | $352.09 / RS 1.15 | PASS |  |  |
| TSM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| TSM | RS2 | Stock 52W Return and S&P 52W Return | +26.0% / +9.2% | +26.0% / +9.2% | PASS |  |  |
| TSM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| TSM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +26.0% clears | +26.0% clears | PASS |  |  |
| UBOT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $14.34 / RS 0.59 | $14.34 / RS 0.59 | PASS |  |  |
| UBOT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.59 | 0.59 | PASS |  |  |
| UBOT | RS2 | Stock 52W Return and S&P 52W Return | -35.4% / +9.2% | -35.4% / +9.2% | PASS |  |  |
| UBOT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UBOT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 17 | 17 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UBOT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| UBOT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -35.4% negative | -35.4% negative | PASS |  |  |
| UFO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $37.97 / RS 1.07 | $37.97 / RS 1.07 | PASS |  |  |
| UFO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.07 | 1.07 | PASS |  |  |
| UFO | RS2 | Stock 52W Return and S&P 52W Return | +16.6% / +9.2% | +16.7% / +9.2% | PASS |  |  |
| UFO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UFO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UFO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| UFO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +16.6% clears | +16.7% clears | PASS |  |  |
| URA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $28.66 / RS 0.61 | $28.66 / RS 0.61 | PASS |  |  |
| URA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.61 | 0.61 | PASS |  |  |
| URA | RS2 | Stock 52W Return and S&P 52W Return | -33.6% / +9.2% | -33.6% / +9.2% | PASS |  |  |
| URA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| URA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 19 | 19 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| URA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| URA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -33.6% negative | -33.6% negative | PASS |  |  |
| URAA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $10.37 / RS 0.29 | $10.37 / RS 0.29 | PASS |  |  |
| URAA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.29 | 0.29 | PASS |  |  |
| URAA | RS2 | Stock 52W Return and S&P 52W Return | -67.9% / +9.2% | -67.9% / +9.2% | PASS |  |  |
| URAA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| URAA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| URAA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| URAA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -67.9% negative | -67.9% negative | PASS |  |  |
| V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $402.25 / RS 1.14 | $402.25 / RS 1.14 | PASS |  |  |
| V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.14 | 1.14 | PASS |  |  |
| V | RS2 | Stock 52W Return and S&P 52W Return | +24.1% / +9.2% | +24.1% / +9.2% | PASS |  |  |
| V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 61 | 61 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +24.1% clears | +24.1% clears | PASS |  |  |
| VFV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $182.95 / RS 1.02 | $182.95 / RS 1.02 | PASS |  |  |
| VFV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.02 | 1.02 | PASS |  |  |
| VFV.TO | RS2 | Stock 52W Return and S&P 52W Return | +11.3% / +9.2% | +11.3% / +9.2% | PASS |  |  |
| VFV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VFV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VFV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| VFV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +11.3% clears | +11.3% clears | PASS |  |  |
| VRT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $184.99 / RS 0.99 | $184.99 / RS 0.99 | PASS |  |  |
| VRT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.99 | 0.99 | PASS |  |  |
| VRT | RS2 | Stock 52W Return and S&P 52W Return | +8.5% / +9.2% | +8.5% / +9.2% | PASS |  |  |
| VRT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VRT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VRT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| VRT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +8.5% clears | +8.5% clears | PASS |  |  |
| WELL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $243.19 / RS 1.13 | $243.19 / RS 1.13 | PASS |  |  |
| WELL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.13 | 1.13 | PASS |  |  |
| WELL | RS2 | Stock 52W Return and S&P 52W Return | +23.5% / +9.2% | +23.5% / +9.2% | PASS |  |  |
| WELL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WELL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WELL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| WELL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +23.5% clears | +23.5% clears | PASS |  |  |
| WMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $126.04 / RS 1.15 | $126.04 / RS 1.15 | PASS |  |  |
| WMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| WMT | RS2 | Stock 52W Return and S&P 52W Return | +25.3% / +9.2% | +25.3% / +9.2% | PASS |  |  |
| WMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| WMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.3% clears | +25.3% clears | PASS |  |  |
| XCHP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $103.19 / RS 1.37 | $103.19 / RS 1.37 | PASS |  |  |
| XCHP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.37 | 1.37 | PASS |  |  |
| XCHP.TO | RS2 | Stock 52W Return and S&P 52W Return | +49.7% / +9.2% | +49.7% / +9.2% | PASS |  |  |
| XCHP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XCHP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 80 | 80 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XCHP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| XCHP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.7% clears | +49.7% clears | PASS |  |  |
| XDRV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.55 / RS 0.90 | $39.55 / RS 0.90 | PASS |  |  |
| XDRV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| XDRV.TO | RS2 | Stock 52W Return and S&P 52W Return | -1.4% / +9.2% | -1.4% / +9.2% | PASS |  |  |
| XDRV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XDRV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XDRV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| XDRV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.4% negative | -1.4% negative | PASS |  |  |
| XEQT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $43.28 / RS 1.03 | $43.28 / RS 1.03 | PASS |  |  |
| XEQT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| XEQT.TO | RS2 | Stock 52W Return and S&P 52W Return | +12.6% / +9.2% | +12.6% / +9.2% | PASS |  |  |
| XEQT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XEQT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XEQT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| XEQT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +12.6% clears | +12.6% clears | PASS |  |  |
| XETM.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $56.19 / RS 0.61 | $56.19 / RS 0.61 | PASS |  |  |
| XETM.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.61 | 0.61 | PASS |  |  |
| XETM.TO | RS2 | Stock 52W Return and S&P 52W Return | -33.3% / +9.2% | -33.3% / +9.2% | PASS |  |  |
| XETM.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 19 | 19 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XETM.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| XETM.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -33.3% negative | -33.3% negative | PASS |  |  |
| XGD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $46.79 / RS 0.92 | $46.79 / RS 0.92 | PASS |  |  |
| XGD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| XGD.TO | RS2 | Stock 52W Return and S&P 52W Return | +0.8% / +9.2% | +0.8% / +9.2% | PASS |  |  |
| XGD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XGD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XGD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| XGD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.8% under | +0.8% under | PASS |  |  |
| XOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $158.93 / RS 1.24 | $158.93 / RS 1.24 | PASS |  |  |
| XOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.24 | 1.24 | PASS |  |  |
| XOM | RS2 | Stock 52W Return and S&P 52W Return | +35.4% / +9.2% | +35.4% / +9.2% | PASS |  |  |
| XOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 69 | 69 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| XOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +35.4% clears | +35.4% clears | PASS |  |  |
| AAPL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| AAPL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| AAPL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $344.01 – $351.46 · price is inside this zone · turned here 4× | $344.01 – $351.46 · 0.0% · 4× | PASS |  |  |
| AAPL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.7459 | 7.7458 | PASS |  |  |
| AAPL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AAPL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| AAPL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| AAPL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $349.21 | $349.21 | PASS |  |  |
| AAPL | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 349.21, zone 344.01-351.46 | inside the zone | PASS |  |  |
| AAPL | TS1c | S5: the Buy on the bar = the Buy in the box | $349.21 | $349.21 | PASS |  |  |
| AAPL | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 349.21 vs last close 349.21 | Buy <= last close | PASS |  |  |
| AAPL | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AAPL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $333.72 -4.4% | $333.72 -4.4% | PASS |  |  |
| AAPL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| AAPL | TS6 | Risk $ (and reward $ per share) | Risk $15.49 a share | Risk $15.49 | PASS |  |  |
| AAPU | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| AAPU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| AAPU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $47.65 – $48.94 · price is inside this zone · turned here 4× | $47.65 – $48.94 · 0.0% · 4× | PASS |  |  |
| AAPU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0246 | 2.0251 | PASS |  |  |
| AAPU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AAPU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AAPU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AAPU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $47.68 | $47.68 | PASS |  |  |
| AAPU | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 47.68, zone 47.65-48.94 | inside the zone | PASS |  |  |
| AAPU | TS1c | S5: the Buy on the bar = the Buy in the box | $47.68 | $47.68 | PASS |  |  |
| AAPU | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 47.68 vs last close 47.68 | Buy <= last close | PASS |  |  |
| AAPU | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AAPU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $43.63 -8.5% | $43.63 -8.5% | PASS |  |  |
| AAPU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPU | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| AAPU | TS6 | Risk $ (and reward $ per share) | Risk $4.05 a share | Risk $4.05 | PASS |  |  |
| ABBV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $291.40 · 2.8% above · turned here 1× | $291.40 · 2.8% · 1× | PASS |  |  |
| ABBV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ABBV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $278.01 – $281.07 · 0.9% below · turned here 2× | $278.01 – $281.07 · 0.9% · 2× | PASS |  |  |
| ABBV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.7056 | 6.7057 | PASS |  |  |
| ABBV | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ABBV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| ABBV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| ABBV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $281.07 | $281.07 | PASS |  |  |
| ABBV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 281.07, nearest zone high 281.07 | equal | PASS |  |  |
| ABBV | TS1c | S5: the Buy on the bar = the Buy in the box | $281.07 | $281.07 | PASS |  |  |
| ABBV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| ABBV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $267.66 -4.8% | $267.66 -4.8% | PASS |  |  |
| ABBV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ABBV | TS4 | Target = nearest resistance edge and its % from the buy | $291.40 +3.7% | $291.40 +3.7% | PASS |  |  |
| ABBV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| ABBV | TS6 | Risk $ (and reward $ per share) | Risk $13.41 to make $10.33 a share | Risk $13.41 to make $10.33 | PASS |  |  |
| AIPO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $23.12 – $24.20 · 4.7% above · turned here 4× | $23.12 – $24.20 · 4.7% · 4× | PASS |  |  |
| AIPO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AIPO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $22.08 · price is inside this zone · turned here 1× | $22.08 · 0.0% · 1× | PASS |  |  |
| AIPO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.1057 | 1.1061 | PASS |  |  |
| AIPO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AIPO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AIPO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AIPO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $22.08 | $22.08 | PASS |  |  |
| AIPO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 22.08, zone 22.08-22.08 | inside the zone | PASS |  |  |
| AIPO | TS1c | S5: the Buy on the bar = the Buy in the box | $22.08 | $22.08 | PASS |  |  |
| AIPO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 22.08 vs last close 22.08 | Buy <= last close | PASS |  |  |
| AIPO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AIPO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $19.87 -10.0% | $19.87 -10.0% | PASS |  |  |
| AIPO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AIPO | TS4 | Target = nearest resistance edge and its % from the buy | $23.12 +4.7% | $23.12 +4.7% | PASS |  |  |
| AIPO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| AIPO | TS6 | Risk $ (and reward $ per share) | Risk $2.21 to make $1.04 a share | Risk $2.21 to make $1.04 | PASS |  |  |
| ALAB | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $214.24 · 1.2% above · turned here 1× | $214.24 · 1.2% · 1× | PASS |  |  |
| ALAB | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ALAB | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $177.61 – $192.86 · 8.9% below · turned here 7× | $177.61 – $192.86 · 8.9% · 7× | PASS |  |  |
| ALAB | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 23.3111 | 23.3106 | PASS |  |  |
| ALAB | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ALAB | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| ALAB | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| ALAB | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $192.86 | $192.86 | PASS |  |  |
| ALAB | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 192.86, nearest zone high 192.86 | equal | PASS |  |  |
| ALAB | TS1c | S5: the Buy on the bar = the Buy in the box | $192.86 | $192.86 | PASS |  |  |
| ALAB | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 8.9% below | 8.9% below | PASS |  |  |
| ALAB | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $146.24 -24.2% | $146.24 -24.2% | PASS |  |  |
| ALAB | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ALAB | TS4 | Target = nearest resistance edge and its % from the buy | $214.24 +11.1% | $214.24 +11.1% | PASS |  |  |
| ALAB | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| ALAB | TS6 | Risk $ (and reward $ per share) | Risk $46.62 to make $21.38 a share | Risk $46.62 to make $21.38 | PASS |  |  |
| AMD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $491.12 – $530.13 · 0.4% above · turned here 6× | $491.12 – $530.13 · 0.4% · 6× | PASS |  |  |
| AMD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $469.21 · 4.1% below · turned here 1× | $469.21 · 4.1% · 1× | PASS |  |  |
| AMD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 43.4822 | 43.4824 | PASS |  |  |
| AMD | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AMD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| AMD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| AMD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $469.21 | $469.21 | PASS |  |  |
| AMD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 469.21, nearest zone high 469.21 | equal | PASS |  |  |
| AMD | TS1c | S5: the Buy on the bar = the Buy in the box | $469.21 | $469.21 | PASS |  |  |
| AMD | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.1% below | 4.1% below | PASS |  |  |
| AMD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $382.25 -18.5% | $382.25 -18.5% | PASS |  |  |
| AMD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD | TS4 | Target = nearest resistance edge and its % from the buy | $491.12 +4.7% | $491.12 +4.7% | PASS |  |  |
| AMD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| AMD | TS6 | Risk $ (and reward $ per share) | Risk $86.96 to make $21.91 a share | Risk $86.96 to make $21.91 | PASS |  |  |
| AMD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $13.37 – $14.18 · 6.2% above · turned here 3× | $13.37 – $14.18 · 6.2% · 3× | PASS |  |  |
| AMD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.20 – $12.97 · price is inside this zone · turned here 5× | $12.20 – $12.97 · 0.0% · 5× | PASS |  |  |
| AMD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.0987 | 1.0987 | PASS |  |  |
| AMD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AMD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AMD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AMD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $12.59 | $12.59 | PASS |  |  |
| AMD.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 12.59, zone 12.2-12.97 | inside the zone | PASS |  |  |
| AMD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $12.59 | $12.59 | PASS |  |  |
| AMD.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 12.59 vs last close 12.59 | Buy <= last close | PASS |  |  |
| AMD.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AMD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $10.39 -17.5% | $10.39 -17.5% | PASS |  |  |
| AMD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $13.37 +6.2% | $13.37 +6.2% | PASS |  |  |
| AMD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| AMD.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.20 to make $0.78 a share | Risk $2.20 to make $0.78 | PASS |  |  |
| AMZN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $265.34 – $267.56 · 3.1% above · turned here 2× | $265.34 – $267.56 · 3.1% · 2× | PASS |  |  |
| AMZN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $255.19 – $259.49 · price is inside this zone · turned here 3× | $255.19 – $259.49 · 0.0% · 3× | PASS |  |  |
| AMZN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.6081 | 9.6081 | PASS |  |  |
| AMZN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AMZN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AMZN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AMZN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $257.37 | $257.37 | PASS |  |  |
| AMZN | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 257.37, zone 255.19-259.49 | inside the zone | PASS |  |  |
| AMZN | TS1c | S5: the Buy on the bar = the Buy in the box | $257.37 | $257.37 | PASS |  |  |
| AMZN | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 257.37 vs last close 257.37 | Buy <= last close | PASS |  |  |
| AMZN | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AMZN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $238.15 -7.5% | $238.15 -7.5% | PASS |  |  |
| AMZN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZN | TS4 | Target = nearest resistance edge and its % from the buy | $265.34 +3.1% | $265.34 +3.1% | PASS |  |  |
| AMZN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| AMZN | TS6 | Risk $ (and reward $ per share) | Risk $19.22 to make $7.97 a share | Risk $19.22 to make $7.97 | PASS |  |  |
| AMZU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.01 – $39.05 · 5.9% above · turned here 7× | $37.01 – $39.05 · 5.9% · 7× | PASS |  |  |
| AMZU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.73 – $32.89 · 5.9% below · turned here 5× | $31.73 – $32.89 · 5.9% · 5× | PASS |  |  |
| AMZU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.6462 | 2.6464 | PASS |  |  |
| AMZU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AMZU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AMZU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AMZU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $32.89 | $32.89 | PASS |  |  |
| AMZU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 32.89, nearest zone high 32.89 | equal | PASS |  |  |
| AMZU | TS1c | S5: the Buy on the bar = the Buy in the box | $32.89 | $32.89 | PASS |  |  |
| AMZU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.9% below | 5.9% below | PASS |  |  |
| AMZU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $27.60 -16.1% | $27.60 -16.1% | PASS |  |  |
| AMZU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZU | TS4 | Target = nearest resistance edge and its % from the buy | $37.01 +12.5% | $37.01 +12.5% | PASS |  |  |
| AMZU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| AMZU | TS6 | Risk $ (and reward $ per share) | Risk $5.29 to make $4.12 a share | Risk $5.29 to make $4.12 | PASS |  |  |
| ANET.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $34.01 – $34.05 · 0.3% above · turned here 2× | $34.01 – $34.05 · 0.3% · 2× | PASS |  |  |
| ANET.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.45 – $33.38 · 1.5% below · turned here 8× | $31.45 – $33.38 · 1.5% · 8× | PASS |  |  |
| ANET.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9823 | 1.9823 | PASS |  |  |
| ANET.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ANET.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ANET.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ANET.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $33.38 | $33.38 | PASS |  |  |
| ANET.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 33.38, nearest zone high 33.38 | equal | PASS |  |  |
| ANET.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $33.38 | $33.38 | PASS |  |  |
| ANET.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| ANET.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $29.42 -11.9% | $29.42 -11.9% | PASS |  |  |
| ANET.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ANET.TO | TS4 | Target = nearest resistance edge and its % from the buy | $34.01 +1.9% | $34.01 +1.9% | PASS |  |  |
| ANET.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| ANET.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.96 to make $0.63 a share | Risk $3.96 to make $0.63 | PASS |  |  |
| ASML.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $42.01 – $42.36 · 1.8% above · turned here 2× | $42.01 – $42.36 · 1.8% · 2× | PASS |  |  |
| ASML.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ASML.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $40.17 – $40.74 · 1.2% below · turned here 3× | $40.17 – $40.74 · 1.2% · 3× | PASS |  |  |
| ASML.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9083 | 1.9084 | PASS |  |  |
| ASML.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ASML.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| ASML.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $40.74 | $40.74 | PASS |  |  |
| ASML.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 40.74, nearest zone high 40.74 | equal | PASS |  |  |
| ASML.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $40.74 | $40.74 | PASS |  |  |
| ASML.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| ASML.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $36.92 -9.4% | $36.92 -9.4% | PASS |  |  |
| ASML.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASML.TO | TS4 | Target = nearest resistance edge and its % from the buy | $42.01 +3.1% | $42.01 +3.1% | PASS |  |  |
| ASML.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ASML.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.82 to make $1.27 a share | Risk $3.82 to make $1.27 | PASS |  |  |
| ASTL.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $6.99 – $7.02 · 1.3% above · turned here 3× | $6.99 – $7.02 · 1.3% · 3× | PASS |  |  |
| ASTL.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ASTL.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $6.31 – $6.62 · 4.1% below · turned here 11× | $6.31 – $6.62 · 4.1% · 11× | PASS |  |  |
| ASTL.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4201 | 0.4205 | PASS |  |  |
| ASTL.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ASTL.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ASTL.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ASTL.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $6.62 | $6.62 | PASS |  |  |
| ASTL.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 6.62, nearest zone high 6.62 | equal | PASS |  |  |
| ASTL.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $6.62 | $6.62 | PASS |  |  |
| ASTL.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.1% below | 4.1% below | PASS |  |  |
| ASTL.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $5.78 -12.7% | $5.78 -12.7% | PASS |  |  |
| ASTL.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASTL.TO | TS4 | Target = nearest resistance edge and its % from the buy | $6.99 +5.6% | $6.99 +5.6% | PASS |  |  |
| ASTL.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| ASTL.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.84 to make $0.37 a share | Risk $0.84 to make $0.37 | PASS |  |  |
| ATD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $80.76 – $81.40 · 0.8% above · turned here 4× | $80.76 – $81.40 · 0.8% · 4× | PASS |  |  |
| ATD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ATD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $78.89 – $79.96 · 0.2% below · turned here 5× | $78.89 – $79.96 · 0.2% · 5× | PASS |  |  |
| ATD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.7668 | 1.7667 | PASS |  |  |
| ATD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ATD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| ATD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| ATD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $79.96 | $79.96 | PASS |  |  |
| ATD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 79.96, nearest zone high 79.96 | equal | PASS |  |  |
| ATD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $79.96 | $79.96 | PASS |  |  |
| ATD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.2% below | 0.2% below | PASS |  |  |
| ATD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $76.43 -4.4% | $76.43 -4.4% | PASS |  |  |
| ATD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ATD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $80.76 +1.0% | $80.76 +1.0% | PASS |  |  |
| ATD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| ATD.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.53 to make $0.80 a share | Risk $3.53 to make $0.80 | PASS |  |  |
| AVGC | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $19.34 – $20.42 · 2.4% above · turned here 4× | $19.34 – $20.42 · 2.4% · 4× | PASS |  |  |
| AVGC | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.52 · 12.5% below · turned here 1× | $16.52 · 12.5% · 1× | PASS |  |  |
| AVGC | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.7114 | 1.7109 | PASS |  |  |
| AVGC | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AVGC | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| AVGC | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| AVGC | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $16.52 | $16.52 | PASS |  |  |
| AVGC | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 16.52, nearest zone high 16.52 | equal | PASS |  |  |
| AVGC | TS1c | S5: the Buy on the bar = the Buy in the box | $16.52 | $16.52 | PASS |  |  |
| AVGC | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 12.5% below | 12.5% below | PASS |  |  |
| AVGC | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $13.10 -20.7% | $13.10 -20.7% | PASS |  |  |
| AVGC | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGC | TS4 | Target = nearest resistance edge and its % from the buy | $19.34 +17.1% | $19.34 +17.1% | PASS |  |  |
| AVGC | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| AVGC | TS6 | Risk $ (and reward $ per share) | Risk $3.42 to make $2.82 a share | Risk $3.42 to make $2.82 | PASS |  |  |
| AVGO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $349.43 – $366.55 · 0.8% above · turned here 9× | $349.43 – $366.55 · 0.8% · 9× | PASS |  |  |
| AVGO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AVGO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $328.71 – $343.29 · 0.9% below · turned here 5× | $328.71 – $343.29 · 0.9% · 5× | PASS |  |  |
| AVGO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 18.0376 | 18.0376 | PASS |  |  |
| AVGO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AVGO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| AVGO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| AVGO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $343.29 | $343.29 | PASS |  |  |
| AVGO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 343.29, nearest zone high 343.29 | equal | PASS |  |  |
| AVGO | TS1c | S5: the Buy on the bar = the Buy in the box | $343.29 | $343.29 | PASS |  |  |
| AVGO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| AVGO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $307.21 -10.5% | $307.21 -10.5% | PASS |  |  |
| AVGO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO | TS4 | Target = nearest resistance edge and its % from the buy | $349.43 +1.8% | $349.43 +1.8% | PASS |  |  |
| AVGO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AVGO | TS6 | Risk $ (and reward $ per share) | Risk $36.08 to make $6.14 a share | Risk $36.08 to make $6.14 | PASS |  |  |
| AVGO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $13.51 – $14.10 · 2.9% above · turned here 10× | $13.51 – $14.10 · 2.9% · 10× | PASS |  |  |
| AVGO.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.72 – $13.34 · price is inside this zone · turned here 7× | $12.72 – $13.34 · 0.0% · 7× | PASS |  |  |
| AVGO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6642 | 0.6641 | PASS |  |  |
| AVGO.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AVGO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AVGO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AVGO.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $13.13 | $13.13 | PASS |  |  |
| AVGO.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 13.13, zone 12.72-13.34 | inside the zone | PASS |  |  |
| AVGO.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $13.13 | $13.13 | PASS |  |  |
| AVGO.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 13.13 vs last close 13.13 | Buy <= last close | PASS |  |  |
| AVGO.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AVGO.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $11.80 -10.1% | $11.80 -10.1% | PASS |  |  |
| AVGO.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO.TO | TS4 | Target = nearest resistance edge and its % from the buy | $13.51 +2.9% | $13.51 +2.9% | PASS |  |  |
| AVGO.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| AVGO.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.33 to make $0.38 a share | Risk $1.33 to make $0.38 | PASS |  |  |
| BDT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $76.69 – $79.52 · 7.4% above · turned here 4× | $76.69 – $79.52 · 7.4% · 4× | PASS |  |  |
| BDT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| BDT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $71.25 · 0.2% below · turned here 1× | $71.25 · 0.2% · 1× | PASS |  |  |
| BDT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.9797 | 3.9798 | PASS |  |  |
| BDT.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BDT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| BDT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| BDT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $71.25 | $71.25 | PASS |  |  |
| BDT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 71.25, nearest zone high 71.25 | equal | PASS |  |  |
| BDT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $71.25 | $71.25 | PASS |  |  |
| BDT.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.2% below | 0.2% below | PASS |  |  |
| BDT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $63.29 -11.2% | $63.29 -11.2% | PASS |  |  |
| BDT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BDT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $76.69 +7.6% | $76.69 +7.6% | PASS |  |  |
| BDT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| BDT.TO | TS6 | Risk $ (and reward $ per share) | Risk $7.96 to make $5.44 a share | Risk $7.96 to make $5.44 | PASS |  |  |
| BOTZ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.54 · 5.3% above · turned here 1× | $30.54 · 5.3% · 1× | PASS |  |  |
| BOTZ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| BOTZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| BOTZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7976 | 0.7975 | PASS |  |  |
| BOTZ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| BOTZ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| BOTZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| BRK-B | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $596.92 · 4.3% above · turned here 1× | $596.92 · 4.3% · 1× | PASS |  |  |
| BRK-B | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Uptrend — between levels | Uptrend — between levels | PASS |  |  |
| BRK-B | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $549.96 · 3.9% below · turned here 1× | $549.96 · 3.9% · 1× | PASS |  |  |
| BRK-B | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.5945 | 9.5945 | PASS |  |  |
| BRK-B | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BRK-B | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| BRK-B | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| BRK-B | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 549.96, nearest zone high 549.96 | equal | PASS |  |  |
| BRK-B | TS1c | S5: the Buy on the bar = the Buy in the box | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.9% below | 3.9% below | PASS |  |  |
| BRK-B | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $530.77 -3.5% | $530.77 -3.5% | PASS |  |  |
| BRK-B | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRK-B | TS4 | Target = nearest resistance edge and its % from the buy | $596.92 +8.5% | $596.92 +8.5% | PASS |  |  |
| BRK-B | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.4 : 1 | 2.4 : 1 | PASS |  |  |
| BRK-B | TS6 | Risk $ (and reward $ per share) | Risk $19.19 to make $46.96 a share | Risk $19.19 to make $46.96 | PASS |  |  |
| BRKU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $31.20 · 9.3% above · turned here 1× | $31.20 · 9.3% · 1× | PASS |  |  |
| BRKU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Uptrend pulling back to support | Uptrend pulling back to support | PASS |  |  |
| BRKU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $26.69 – $26.74 · 6.3% below · turned here 2× | $26.69 – $26.74 · 6.3% · 2× | PASS |  |  |
| BRKU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9149 | 0.9149 | PASS |  |  |
| BRKU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BRKU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| BRKU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| BRKU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $26.74 | $26.74 | PASS |  |  |
| BRKU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 26.74, nearest zone high 26.74 | equal | PASS |  |  |
| BRKU | TS1c | S5: the Buy on the bar = the Buy in the box | $26.74 | $26.74 | PASS |  |  |
| BRKU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.3% below | 6.3% below | PASS |  |  |
| BRKU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $24.91 -6.8% | $24.91 -6.8% | PASS |  |  |
| BRKU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRKU | TS4 | Target = nearest resistance edge and its % from the buy | $31.20 +16.7% | $31.20 +16.7% | PASS |  |  |
| BRKU | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.4 : 1 | 2.4 : 1 | PASS |  |  |
| BRKU | TS6 | Risk $ (and reward $ per share) | Risk $1.83 to make $4.46 a share | Risk $1.83 to make $4.46 | PASS |  |  |
| CAMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $101.39 · 3.7% above · turned here 1× | $101.39 · 3.7% · 1× | PASS |  |  |
| CAMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CAMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $89.13 – $91.91 · 6.0% below · turned here 2× | $89.13 – $91.91 · 6.0% · 2× | PASS |  |  |
| CAMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.0011 | 8.0011 | PASS |  |  |
| CAMT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CAMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CAMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CAMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $91.91 | $91.91 | PASS |  |  |
| CAMT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 91.91, nearest zone high 91.91 | equal | PASS |  |  |
| CAMT | TS1c | S5: the Buy on the bar = the Buy in the box | $91.91 | $91.91 | PASS |  |  |
| CAMT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.0% below | 6.0% below | PASS |  |  |
| CAMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $75.91 -17.4% | $75.91 -17.4% | PASS |  |  |
| CAMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CAMT | TS4 | Target = nearest resistance edge and its % from the buy | $101.39 +10.3% | $101.39 +10.3% | PASS |  |  |
| CAMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| CAMT | TS6 | Risk $ (and reward $ per share) | Risk $16.00 to make $9.48 a share | Risk $16.00 to make $9.48 | PASS |  |  |
| CARS.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.90 · 5.1% above · turned here 1× | $20.90 · 5.1% · 1× | PASS |  |  |
| CARS.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CARS.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CARS.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4773 | 0.4762 | PASS |  |  |
| CARS.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CARS.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CARS.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CAT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $550.81 – $552.77 · 2.5% above · turned here 2× | $550.81 – $552.77 · 2.5% · 2× | PASS |  |  |
| CAT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CAT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $532.56 · 0.9% below · turned here 1× | $532.56 · 0.9% · 1× | PASS |  |  |
| CAT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 28.7397 | 28.7402 | PASS |  |  |
| CAT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CAT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CAT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CAT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $532.56 | $532.56 | PASS |  |  |
| CAT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 532.56, nearest zone high 532.56 | equal | PASS |  |  |
| CAT | TS1c | S5: the Buy on the bar = the Buy in the box | $532.56 | $532.56 | PASS |  |  |
| CAT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| CAT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $475.08 -10.8% | $475.08 -10.8% | PASS |  |  |
| CAT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CAT | TS4 | Target = nearest resistance edge and its % from the buy | $550.81 +3.4% | $550.81 +3.4% | PASS |  |  |
| CAT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CAT | TS6 | Risk $ (and reward $ per share) | Risk $57.48 to make $18.25 a share | Risk $57.48 to make $18.25 | PASS |  |  |
| CCO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $92.52 · 3.5% above · turned here 1× | $92.52 · 3.5% · 1× | PASS |  |  |
| CCO.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CCO.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CCO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.9224 | 4.9224 | PASS |  |  |
| CCO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| CCO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| CCO.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CEG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $256.10 – $268.00 · 1.6% above · turned here 7× | $256.10 – $268.00 · 1.6% · 7× | PASS |  |  |
| CEG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CEG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $240.51 – $250.55 · 0.6% below · turned here 6× | $240.51 – $250.55 · 0.6% · 6× | PASS |  |  |
| CEG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 13.1699 | 13.1696 | PASS |  |  |
| CEG | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CEG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| CEG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| CEG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $250.55 | $250.55 | PASS |  |  |
| CEG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 250.55, nearest zone high 250.55 | equal | PASS |  |  |
| CEG | TS1c | S5: the Buy on the bar = the Buy in the box | $250.55 | $250.55 | PASS |  |  |
| CEG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.6% below | 0.6% below | PASS |  |  |
| CEG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $224.21 -10.5% | $224.21 -10.5% | PASS |  |  |
| CEG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CEG | TS4 | Target = nearest resistance edge and its % from the buy | $256.10 +2.2% | $256.10 +2.2% | PASS |  |  |
| CEG | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| CEG | TS6 | Risk $ (and reward $ per share) | Risk $26.34 to make $5.55 a share | Risk $26.34 to make $5.55 | PASS |  |  |
| CGY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $83.01 · 1.8% above · turned here 1× | $83.01 · 1.8% · 1× | PASS |  |  |
| CGY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CGY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $81.18 – $81.65 · price is inside this zone · turned here 2× | $81.18 – $81.65 · 0.0% · 2× | PASS |  |  |
| CGY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5223 | 2.5223 | PASS |  |  |
| CGY.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| CGY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CGY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CGY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $81.56 | $81.56 | PASS |  |  |
| CGY.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 81.56, zone 81.18-81.65 | inside the zone | PASS |  |  |
| CGY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $81.56 | $81.56 | PASS |  |  |
| CGY.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 81.56 vs last close 81.56 | Buy <= last close | PASS |  |  |
| CGY.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| CGY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $76.52 -6.2% | $76.52 -6.2% | PASS |  |  |
| CGY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CGY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $83.01 +1.8% | $83.01 +1.8% | PASS |  |  |
| CGY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CGY.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.04 to make $1.45 a share | Risk $5.04 to make $1.45 | PASS |  |  |
| CNQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $64.61 · 0.8% above · turned here 1× | $64.61 · 0.8% · 1× | PASS |  |  |
| CNQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $63.39 · 1.1% below · turned here 1× | $63.39 · 1.1% · 1× | PASS |  |  |
| CNQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0606 | 2.0605 | PASS |  |  |
| CNQ.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CNQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CNQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CNQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $63.39 | $63.39 | PASS |  |  |
| CNQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 63.39, nearest zone high 63.39 | equal | PASS |  |  |
| CNQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $63.39 | $63.39 | PASS |  |  |
| CNQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| CNQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $59.27 -6.5% | $59.27 -6.5% | PASS |  |  |
| CNQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $64.61 +1.9% | $64.61 +1.9% | PASS |  |  |
| CNQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CNQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.12 to make $1.22 a share | Risk $4.12 to make $1.22 | PASS |  |  |
| CNR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $183.80 – $184.26 · 2.9% above · turned here 2× | $183.80 – $184.26 · 2.9% · 2× | PASS |  |  |
| CNR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $178.49 · 0.1% below · turned here 1× | $178.49 · 0.1% · 1× | PASS |  |  |
| CNR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.1918 | 3.1918 | PASS |  |  |
| CNR.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CNR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| CNR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| CNR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $178.49 | $178.49 | PASS |  |  |
| CNR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 178.49, nearest zone high 178.49 | equal | PASS |  |  |
| CNR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $178.49 | $178.49 | PASS |  |  |
| CNR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.1% below | 0.1% below | PASS |  |  |
| CNR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $172.11 -3.6% | $172.11 -3.6% | PASS |  |  |
| CNR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $183.80 +3.0% | $183.80 +3.0% | PASS |  |  |
| CNR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| CNR.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.38 to make $5.31 a share | Risk $6.38 to make $5.31 | PASS |  |  |
| COP | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $140.69 · 4.2% above · turned here 1× | $140.69 · 4.2% · 1× | PASS |  |  |
| COP | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COP | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $133.10 – $134.99 · price is inside this zone · turned here 2× | $133.10 – $134.99 · 0.0% · 2× | PASS |  |  |
| COP | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.912 | 3.9133 | PASS |  |  |
| COP | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| COP | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| COP | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $134.99 | $134.99 | PASS |  |  |
| COP | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 134.99, zone 133.1-134.99 | inside the zone | PASS |  |  |
| COP | TS1c | S5: the Buy on the bar = the Buy in the box | $134.99 | $134.99 | PASS |  |  |
| COP | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 134.99 vs last close 134.99 | Buy <= last close | PASS |  |  |
| COP | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.0% below | 0.0% below | PASS |  |  |
| COP | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $127.17 -5.8% | $127.17 -5.8% | PASS |  |  |
| COP | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COP | TS4 | Target = nearest resistance edge and its % from the buy | $140.69 +4.2% | $140.69 +4.2% | PASS |  |  |
| COP | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| COP | TS6 | Risk $ (and reward $ per share) | Risk $7.82 to make $5.70 a share | Risk $7.82 to make $5.70 | PASS |  |  |
| COPP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $42.17 · 0.8% above · turned here 1× | $42.17 · 0.8% · 1× | PASS |  |  |
| COPP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| COPP.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| COPP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1825 | 2.1825 | PASS |  |  |
| COPP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| COPP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| COPP.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| COPX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $68.26 · 15.1% above · turned here 1× | $68.26 · 15.1% · 1× | PASS |  |  |
| COPX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 0 of 8 trend checks pass · ADX 28.9 | 0 of 8 trend checks pass · ADX 28.9 | PASS |  |  |
| COPX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $55.44 · 6.5% below · turned here 1× | $55.44 · 6.5% · 1× | PASS |  |  |
| COPX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.9076 | 2.9076 | PASS |  |  |
| COPX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COPX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| COPX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| COPX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $55.44 | $55.44 | PASS |  |  |
| COPX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 55.44, nearest zone high 55.44 | equal | PASS |  |  |
| COPX | TS1c | S5: the Buy on the bar = the Buy in the box | $55.44 | $55.44 | PASS |  |  |
| COPX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.5% below | 6.5% below | PASS |  |  |
| COPX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $49.62 -10.5% | $49.62 -10.5% | PASS |  |  |
| COPX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COPX | TS4 | Target = nearest resistance edge and its % from the buy | $68.26 +23.1% | $68.26 +23.1% | PASS |  |  |
| COPX | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.2 : 1 | 2.2 : 1 | PASS |  |  |
| COPX | TS6 | Risk $ (and reward $ per share) | Risk $5.82 to make $12.82 a share | Risk $5.82 to make $12.82 | PASS |  |  |
| COPZ | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| COPZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| COPZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8106 | 0.8106 | PASS |  |  |
| COPZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| COST | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $1,096.50 · 0.2% above · turned here 1× | $1,096.50 · 0.2% · 1× | PASS |  |  |
| COST | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Transitioning — testing resistance | Transitioning — testing resistance | PASS |  |  |
| COST | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,031.27 – $1,035.82 · 5.3% below · turned here 2× | $1,031.27 – $1,035.82 · 5.3% · 2× | PASS |  |  |
| COST | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 18.3134 | 18.3132 | PASS |  |  |
| COST | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COST | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| COST | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| COST | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,035.82 | $1,035.82 | PASS |  |  |
| COST | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1035.82, nearest zone high 1035.82 | equal | PASS |  |  |
| COST | TS1c | S5: the Buy on the bar = the Buy in the box | $1,035.82 | $1,035.82 | PASS |  |  |
| COST | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.3% below | 5.3% below | PASS |  |  |
| COST | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $999.19 -3.5% | $999.19 -3.5% | PASS |  |  |
| COST | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COST | TS4 | Target = nearest resistance edge and its % from the buy | $1,096.50 +5.9% | $1,096.50 +5.9% | PASS |  |  |
| COST | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.7 : 1 | 1.7 : 1 | PASS |  |  |
| COST | TS6 | Risk $ (and reward $ per share) | Risk $36.63 to make $60.68 a share | Risk $36.63 to make $60.68 | PASS |  |  |
| COTG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $17.80 · 8.2% above · turned here 1× | $17.80 · 8.2% · 1× | PASS |  |  |
| COTG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Weakening trend — testing support | Weakening trend — testing support | PASS |  |  |
| COTG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.07 – $16.11 · 2.1% below · turned here 2× | $16.07 – $16.11 · 2.1% · 2× | PASS |  |  |
| COTG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5035 | 0.5034 | PASS |  |  |
| COTG | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COTG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| COTG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| COTG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $16.11 | $16.11 | PASS |  |  |
| COTG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 16.11, nearest zone high 16.11 | equal | PASS |  |  |
| COTG | TS1c | S5: the Buy on the bar = the Buy in the box | $16.11 | $16.11 | PASS |  |  |
| COTG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| COTG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $15.10 -6.3% | $15.10 -6.3% | PASS |  |  |
| COTG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COTG | TS4 | Target = nearest resistance edge and its % from the buy | $17.80 +10.5% | $17.80 +10.5% | PASS |  |  |
| COTG | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.7 : 1 | 1.7 : 1 | PASS |  |  |
| COTG | TS6 | Risk $ (and reward $ per share) | Risk $1.01 to make $1.69 a share | Risk $1.01 to make $1.69 | PASS |  |  |
| CSU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3,341.06 – $3,430.89 · 5.1% above · turned here 5× | $3,341.06 – $3,430.89 · 5.1% · 5× | PASS |  |  |
| CSU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CSU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $3,118.74 – $3,227.61 · price is inside this zone · turned here 6× | $3,118.74 – $3,227.61 · 0.0% · 6× | PASS |  |  |
| CSU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 120.688 | 120.6880 | PASS |  |  |
| CSU.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| CSU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| CSU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| CSU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $3,180.00 | $3,180.00 | PASS |  |  |
| CSU.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 3180, zone 3118.74-3227.61 | inside the zone | PASS |  |  |
| CSU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $3,180.00 | $3,180.00 | PASS |  |  |
| CSU.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 3180 vs last close 3180 | Buy <= last close | PASS |  |  |
| CSU.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| CSU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $2,938.62 -7.6% | $2,938.62 -7.6% | PASS |  |  |
| CSU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CSU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $3,341.06 +5.1% | $3,341.06 +5.1% | PASS |  |  |
| CSU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| CSU.TO | TS6 | Risk $ (and reward $ per share) | Risk $241.38 to make $161.06 a share | Risk $241.38 to make $161.06 | PASS |  |  |
| CVX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $208.98 · 1.2% above · turned here 1× | $208.98 · 1.2% · 1× | PASS |  |  |
| CVX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CVX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $206.01 · 0.2% below · turned here 1× | $206.01 · 0.2% · 1× | PASS |  |  |
| CVX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.0626 | 5.0635 | PASS |  |  |
| CVX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CVX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CVX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CVX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $206.01 | $206.01 | PASS |  |  |
| CVX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 206.01, nearest zone high 206.01 | equal | PASS |  |  |
| CVX | TS1c | S5: the Buy on the bar = the Buy in the box | $206.01 | $206.01 | PASS |  |  |
| CVX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.2% below | 0.2% below | PASS |  |  |
| CVX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $195.88 -4.9% | $195.88 -4.9% | PASS |  |  |
| CVX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CVX | TS4 | Target = nearest resistance edge and its % from the buy | $208.98 +1.4% | $208.98 +1.4% | PASS |  |  |
| CVX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CVX | TS6 | Risk $ (and reward $ per share) | Risk $10.13 to make $2.97 a share | Risk $10.13 to make $2.97 | PASS |  |  |
| DRAL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $4.06 · 1.8% above · turned here 1× | $4.06 · 1.8% · 1× | PASS |  |  |
| DRAL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| DRAL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7697 | 0.7697 | PASS |  |  |
| DRAL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| DRAL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| DRAL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| DRAM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $44.40 – $46.43 · 15.5% above · turned here 3× | $44.40 – $46.43 · 15.5% · 3× | PASS |  |  |
| DRAM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $37.01 · 3.7% below · turned here 1× | $37.01 · 3.7% · 1× | PASS |  |  |
| DRAM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.0528 | 3.0536 | PASS |  |  |
| DRAM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| DRAM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| DRAM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| DRAM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $37.01 | $37.01 | PASS |  |  |
| DRAM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 37.01, nearest zone high 37.01 | equal | PASS |  |  |
| DRAM | TS1c | S5: the Buy on the bar = the Buy in the box | $37.01 | $37.01 | PASS |  |  |
| DRAM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.7% below | 3.7% below | PASS |  |  |
| DRAM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $30.90 -16.5% | $30.90 -16.5% | PASS |  |  |
| DRAM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRAM | TS4 | Target = nearest resistance edge and its % from the buy | $44.40 +20.0% | $44.40 +20.0% | PASS |  |  |
| DRAM | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| DRAM | TS6 | Risk $ (and reward $ per share) | Risk $6.11 to make $7.39 a share | Risk $6.11 to make $7.39 | PASS |  |  |
| DRIV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $26.87 · 2.3% above · turned here 1× | $26.87 · 2.3% · 1× | PASS |  |  |
| DRIV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| DRIV | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| DRIV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7813 | 0.7822 | PASS |  |  |
| DRIV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| DRIV | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| DUK | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $129.00 · 0.1% above · turned here 1× | $129.00 · 0.1% · 1× | PASS |  |  |
| DUK | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| DUK | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $126.77 – $126.97 · 1.5% below · turned here 2× | $126.77 – $126.97 · 1.5% · 2× | PASS |  |  |
| DUK | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1623 | 2.1624 | PASS |  |  |
| DUK | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| DUK | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| DUK | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| DUK | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $126.97 | $126.97 | PASS |  |  |
| DUK | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 126.97, nearest zone high 126.97 | equal | PASS |  |  |
| DUK | TS1c | S5: the Buy on the bar = the Buy in the box | $126.97 | $126.97 | PASS |  |  |
| DUK | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| DUK | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $122.65 -3.4% | $122.65 -3.4% | PASS |  |  |
| DUK | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DUK | TS4 | Target = nearest resistance edge and its % from the buy | $129.00 +1.6% | $129.00 +1.6% | PASS |  |  |
| DUK | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| DUK | TS6 | Risk $ (and reward $ per share) | Risk $4.32 to make $2.03 a share | Risk $4.32 to make $2.03 | PASS |  |  |
| ELIL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| ELIL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| ELIL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.86 · 1.9% below · turned here 1× | $35.86 · 1.9% · 1× | PASS |  |  |
| ELIL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2101 | 2.2098 | PASS |  |  |
| ELIL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ELIL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| ELIL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| ELIL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 35.86, nearest zone high 35.86 | equal | PASS |  |  |
| ELIL | TS1c | S5: the Buy on the bar = the Buy in the box | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.9% below | 1.9% below | PASS |  |  |
| ELIL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.44 -12.3% | $31.44 -12.3% | PASS |  |  |
| ELIL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ELIL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| ELIL | TS6 | Risk $ (and reward $ per share) | Risk $4.42 a share | Risk $4.42 | PASS |  |  |
| EQIX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $1,021.66 – $1,048.61 · 0.3% above · turned here 7× | $1,021.66 – $1,048.61 · 0.3% · 7× | PASS |  |  |
| EQIX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| EQIX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $997.14 · 2.1% below · turned here 1× | $997.14 · 2.1% · 1× | PASS |  |  |
| EQIX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 32.9877 | 32.9880 | PASS |  |  |
| EQIX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| EQIX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| EQIX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| EQIX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $997.14 | $997.14 | PASS |  |  |
| EQIX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 997.14, nearest zone high 997.14 | equal | PASS |  |  |
| EQIX | TS1c | S5: the Buy on the bar = the Buy in the box | $997.14 | $997.14 | PASS |  |  |
| EQIX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| EQIX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $931.16 -6.6% | $931.16 -6.6% | PASS |  |  |
| EQIX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| EQIX | TS4 | Target = nearest resistance edge and its % from the buy | $1,021.66 +2.5% | $1,021.66 +2.5% | PASS |  |  |
| EQIX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| EQIX | TS6 | Risk $ (and reward $ per share) | Risk $65.98 to make $24.52 a share | Risk $65.98 to make $24.52 | PASS |  |  |
| ETN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $338.25 – $354.37 · 2.3% above · turned here 4× | $338.25 – $354.37 · 2.3% · 4× | PASS |  |  |
| ETN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ETN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $311.92 – $327.50 · 0.9% below · turned here 6× | $311.92 – $327.50 · 0.9% · 6× | PASS |  |  |
| ETN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.4889 | 17.4891 | PASS |  |  |
| ETN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ETN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ETN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ETN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $327.50 | $327.50 | PASS |  |  |
| ETN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 327.5, nearest zone high 327.5 | equal | PASS |  |  |
| ETN | TS1c | S5: the Buy on the bar = the Buy in the box | $327.50 | $327.50 | PASS |  |  |
| ETN | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| ETN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $292.52 -10.7% | $292.52 -10.7% | PASS |  |  |
| ETN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ETN | TS4 | Target = nearest resistance edge and its % from the buy | $338.25 +3.3% | $338.25 +3.3% | PASS |  |  |
| ETN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ETN | TS6 | Risk $ (and reward $ per share) | Risk $34.98 to make $10.75 a share | Risk $34.98 to make $10.75 | PASS |  |  |
| FCX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $50.66 – $51.51 · 3.1% above · turned here 2× | $50.66 – $51.51 · 3.1% · 2× | PASS |  |  |
| FCX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| FCX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| FCX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.0159 | 3.0162 | PASS |  |  |
| FCX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| FCX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| FCX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| GDX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $75.83 · 5.3% above · turned here 1× | $75.83 · 5.3% · 1× | PASS |  |  |
| GDX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GDX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $71.89 – $73.70 · price is inside this zone · turned here 5× | $71.89 – $73.70 · 0.0% · 5× | PASS |  |  |
| GDX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.5688 | 3.5685 | PASS |  |  |
| GDX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| GDX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GDX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| GDX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $72.00 | $72.00 | PASS |  |  |
| GDX | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 72, zone 71.89-73.7 | inside the zone | PASS |  |  |
| GDX | TS1c | S5: the Buy on the bar = the Buy in the box | $72.00 | $72.00 | PASS |  |  |
| GDX | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 72 vs last close 72 | Buy <= last close | PASS |  |  |
| GDX | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| GDX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $64.86 -9.9% | $64.86 -9.9% | PASS |  |  |
| GDX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GDX | TS4 | Target = nearest resistance edge and its % from the buy | $75.83 +5.3% | $75.83 +5.3% | PASS |  |  |
| GDX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| GDX | TS6 | Risk $ (and reward $ per share) | Risk $7.14 to make $3.83 a share | Risk $7.14 to make $3.83 | PASS |  |  |
| GDXU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.83 · 2.4% above · turned here 1× | $20.83 · 2.4% · 1× | PASS |  |  |
| GDXU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| GDXU.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| GDXU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.3835 | 2.3835 | PASS |  |  |
| GDXU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| GDXU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| GDXU.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| GE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $328.67 – $336.02 · 3.1% above · turned here 3× | $328.67 – $336.02 · 3.1% · 3× | PASS |  |  |
| GE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $318.26 – $321.17 · price is inside this zone · turned here 2× | $318.26 – $321.17 · 0.0% · 2× | PASS |  |  |
| GE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 10.1722 | 10.1723 | PASS |  |  |
| GE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| GE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| GE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| GE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $318.88 | $318.88 | PASS |  |  |
| GE | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 318.88, zone 318.26-321.17 | inside the zone | PASS |  |  |
| GE | TS1c | S5: the Buy on the bar = the Buy in the box | $318.88 | $318.88 | PASS |  |  |
| GE | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 318.88 vs last close 318.88 | Buy <= last close | PASS |  |  |
| GE | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| GE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $298.54 -6.4% | $298.54 -6.4% | PASS |  |  |
| GE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GE | TS4 | Target = nearest resistance edge and its % from the buy | $328.67 +3.1% | $328.67 +3.1% | PASS |  |  |
| GE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| GE | TS6 | Risk $ (and reward $ per share) | Risk $20.34 to make $9.79 a share | Risk $20.34 to make $9.79 | PASS |  |  |
| GEV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $775.68 – $806.12 · 2.6% above · turned here 3× | $775.68 – $806.12 · 2.6% · 3× | PASS |  |  |
| GEV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GEV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $729.22 – $747.00 · 1.2% below · turned here 2× | $729.22 – $747.00 · 1.2% · 2× | PASS |  |  |
| GEV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 53.5552 | 53.5553 | PASS |  |  |
| GEV | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GEV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GEV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| GEV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $747.00 | $747.00 | PASS |  |  |
| GEV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 747, nearest zone high 747 | equal | PASS |  |  |
| GEV | TS1c | S5: the Buy on the bar = the Buy in the box | $747.00 | $747.00 | PASS |  |  |
| GEV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| GEV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $639.89 -14.3% | $639.89 -14.3% | PASS |  |  |
| GEV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV | TS4 | Target = nearest resistance edge and its % from the buy | $775.68 +3.8% | $775.68 +3.8% | PASS |  |  |
| GEV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GEV | TS6 | Risk $ (and reward $ per share) | Risk $107.11 to make $28.68 a share | Risk $107.11 to make $28.68 | PASS |  |  |
| GEV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $52.71 – $54.63 · 4.2% above · turned here 3× | $52.71 – $54.63 · 4.2% · 3× | PASS |  |  |
| GEV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $50.19 · 0.8% below · turned here 1× | $50.19 · 0.8% · 1× | PASS |  |  |
| GEV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.4717 | 3.4713 | PASS |  |  |
| GEV.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GEV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GEV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $50.19 | $50.19 | PASS |  |  |
| GEV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 50.19, nearest zone high 50.19 | equal | PASS |  |  |
| GEV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $50.19 | $50.19 | PASS |  |  |
| GEV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| GEV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $43.25 -13.8% | $43.25 -13.8% | PASS |  |  |
| GEV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $52.71 +5.0% | $52.71 +5.0% | PASS |  |  |
| GEV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| GEV.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.94 to make $2.52 a share | Risk $6.94 to make $2.52 | PASS |  |  |
| GGLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $62.13 · 4.0% above · turned here 1× | $62.13 · 4.0% · 1× | PASS |  |  |
| GGLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| GGLL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| GGLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.2961 | 5.2965 | PASS |  |  |
| GGLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| GGLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| GGLL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| GIB-A.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $119.30 · 6.1% above · turned here 1× | $119.30 · 6.1% · 1× | PASS |  |  |
| GIB-A.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Weakening trend — testing support | Weakening trend — testing support | PASS |  |  |
| GIB-A.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.35 · 2.7% below · turned here 1× | $109.35 · 2.7% · 1× | PASS |  |  |
| GIB-A.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.6744 | 2.6744 | PASS |  |  |
| GIB-A.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GIB-A.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| GIB-A.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| GIB-A.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.35, nearest zone high 109.35 | equal | PASS |  |  |
| GIB-A.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| GIB-A.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $104.00 -4.9% | $104.00 -4.9% | PASS |  |  |
| GIB-A.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GIB-A.TO | TS4 | Target = nearest resistance edge and its % from the buy | $119.30 +9.1% | $119.30 +9.1% | PASS |  |  |
| GIB-A.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.9 : 1 | 1.9 : 1 | PASS |  |  |
| GIB-A.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.35 to make $9.95 a share | Risk $5.35 to make $9.95 | PASS |  |  |
| GOOGL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $293.72 – $295.67 · 7.7% above · turned here 3× | $293.72 – $295.67 · 7.7% · 3× | PASS |  |  |
| GOOGL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GOOGL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $271.77 – $276.92 · price is inside this zone · turned here 2× | $271.77 – $276.92 · 0.0% · 2× | PASS |  |  |
| GOOGL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 10.729 | 10.7290 | PASS |  |  |
| GOOGL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| GOOGL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GOOGL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| GOOGL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $272.66 | $272.66 | PASS |  |  |
| GOOGL | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 272.66, zone 271.77-276.92 | inside the zone | PASS |  |  |
| GOOGL | TS1c | S5: the Buy on the bar = the Buy in the box | $272.66 | $272.66 | PASS |  |  |
| GOOGL | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 272.66 vs last close 272.66 | Buy <= last close | PASS |  |  |
| GOOGL | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| GOOGL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $251.20 -7.9% | $251.20 -7.9% | PASS |  |  |
| GOOGL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GOOGL | TS4 | Target = nearest resistance edge and its % from the buy | $293.72 +7.7% | $293.72 +7.7% | PASS |  |  |
| GOOGL | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.0 : 1 | 1.0 : 1 | PASS |  |  |
| GOOGL | TS6 | Risk $ (and reward $ per share) | Risk $21.46 to make $21.06 a share | Risk $21.46 to make $21.06 | PASS |  |  |
| GRID | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $154.73 – $157.05 · 1.5% above · turned here 3× | $154.73 – $157.05 · 1.5% · 3× | PASS |  |  |
| GRID | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GRID | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $151.79 – $151.95 · 0.3% below · turned here 2× | $151.79 – $151.95 · 0.3% · 2× | PASS |  |  |
| GRID | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.1824 | 4.1824 | PASS |  |  |
| GRID | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GRID | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| GRID | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $151.95 | $151.95 | PASS |  |  |
| GRID | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 151.95, nearest zone high 151.95 | equal | PASS |  |  |
| GRID | TS1c | S5: the Buy on the bar = the Buy in the box | $151.95 | $151.95 | PASS |  |  |
| GRID | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| GRID | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $143.59 -5.5% | $143.59 -5.5% | PASS |  |  |
| GRID | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GRID | TS4 | Target = nearest resistance edge and its % from the buy | $154.73 +1.8% | $154.73 +1.8% | PASS |  |  |
| GRID | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GRID | TS6 | Risk $ (and reward $ per share) | Risk $8.36 to make $2.78 a share | Risk $8.36 to make $2.78 | PASS |  |  |
| HD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $348.35 – $356.22 · 3.5% above · turned here 5× | $348.35 – $356.22 · 3.5% · 5× | PASS |  |  |
| HD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $328.24 – $336.69 · price is inside this zone · turned here 5× | $328.24 – $336.69 · 0.0% · 5× | PASS |  |  |
| HD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.917 | 8.9170 | PASS |  |  |
| HD | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| HD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| HD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| HD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $336.68 | $336.68 | PASS |  |  |
| HD | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 336.68, zone 328.24-336.69 | inside the zone | PASS |  |  |
| HD | TS1c | S5: the Buy on the bar = the Buy in the box | $336.68 | $336.68 | PASS |  |  |
| HD | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 336.68 vs last close 336.68 | Buy <= last close | PASS |  |  |
| HD | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| HD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $318.85 -5.3% | $318.85 -5.3% | PASS |  |  |
| HD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HD | TS4 | Target = nearest resistance edge and its % from the buy | $348.35 +3.5% | $348.35 +3.5% | PASS |  |  |
| HD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| HD | TS6 | Risk $ (and reward $ per share) | Risk $17.83 to make $11.67 a share | Risk $17.83 to make $11.67 | PASS |  |  |
| HURA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $36.76 · 2.5% above · turned here 1× | $36.76 · 2.5% · 1× | PASS |  |  |
| HURA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| HURA.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| HURA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.3259 | 1.3259 | PASS |  |  |
| HURA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| HURA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| HURA.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| HXQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $109.90 · 0.3% above · turned here 1× | $109.90 · 0.3% · 1× | PASS |  |  |
| HXQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HXQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $107.31 · 2.1% below · turned here 1× | $107.31 · 2.1% · 1× | PASS |  |  |
| HXQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.748 | 2.7480 | PASS |  |  |
| HXQ.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| HXQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| HXQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| HXQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $107.31 | $107.31 | PASS |  |  |
| HXQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 107.31, nearest zone high 107.31 | equal | PASS |  |  |
| HXQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $107.31 | $107.31 | PASS |  |  |
| HXQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| HXQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $101.81 -5.1% | $101.81 -5.1% | PASS |  |  |
| HXQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HXQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $109.90 +2.4% | $109.90 +2.4% | PASS |  |  |
| HXQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| HXQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.50 to make $2.59 a share | Risk $5.50 to make $2.59 | PASS |  |  |
| JNJ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $268.11 · 0.4% above · turned here 1× | $268.11 · 0.4% · 1× | PASS |  |  |
| JNJ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JNJ | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $260.68 – $264.39 · 1.0% below · turned here 3× | $260.68 – $264.39 · 1.0% · 3× | PASS |  |  |
| JNJ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.8066 | 6.8066 | PASS |  |  |
| JNJ | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| JNJ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| JNJ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| JNJ | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $264.39 | $264.39 | PASS |  |  |
| JNJ | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 264.39, nearest zone high 264.39 | equal | PASS |  |  |
| JNJ | TS1c | S5: the Buy on the bar = the Buy in the box | $264.39 | $264.39 | PASS |  |  |
| JNJ | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.0% below | 1.0% below | PASS |  |  |
| JNJ | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $250.78 -5.1% | $250.78 -5.1% | PASS |  |  |
| JNJ | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JNJ | TS4 | Target = nearest resistance edge and its % from the buy | $268.11 +1.4% | $268.11 +1.4% | PASS |  |  |
| JNJ | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| JNJ | TS6 | Risk $ (and reward $ per share) | Risk $13.61 to make $3.72 a share | Risk $13.61 to make $3.72 | PASS |  |  |
| JPM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $321.68 – $324.25 · 0.5% above · turned here 4× | $321.68 – $324.25 · 0.5% · 4× | PASS |  |  |
| JPM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JPM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $313.32 – $317.22 · 0.9% below · turned here 3× | $313.32 – $317.22 · 0.9% · 3× | PASS |  |  |
| JPM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.628 | 7.6279 | PASS |  |  |
| JPM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| JPM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| JPM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| JPM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $317.22 | $317.22 | PASS |  |  |
| JPM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 317.22, nearest zone high 317.22 | equal | PASS |  |  |
| JPM | TS1c | S5: the Buy on the bar = the Buy in the box | $317.22 | $317.22 | PASS |  |  |
| JPM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| JPM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $301.96 -4.8% | $301.96 -4.8% | PASS |  |  |
| JPM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JPM | TS4 | Target = nearest resistance edge and its % from the buy | $321.68 +1.4% | $321.68 +1.4% | PASS |  |  |
| JPM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| JPM | TS6 | Risk $ (and reward $ per share) | Risk $15.26 to make $4.46 a share | Risk $15.26 to make $4.46 | PASS |  |  |
| KEYS | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $293.55 – $306.85 · 4.3% above · turned here 5× | $293.55 – $306.85 · 4.3% · 5× | PASS |  |  |
| KEYS | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| KEYS | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $275.27 · 2.2% below · turned here 1× | $275.27 · 2.2% · 1× | PASS |  |  |
| KEYS | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 15.5758 | 15.5759 | PASS |  |  |
| KEYS | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| KEYS | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| KEYS | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| KEYS | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $275.27 | $275.27 | PASS |  |  |
| KEYS | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 275.27, nearest zone high 275.27 | equal | PASS |  |  |
| KEYS | TS1c | S5: the Buy on the bar = the Buy in the box | $275.27 | $275.27 | PASS |  |  |
| KEYS | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.2% below | 2.2% below | PASS |  |  |
| KEYS | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $244.12 -11.3% | $244.12 -11.3% | PASS |  |  |
| KEYS | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| KEYS | TS4 | Target = nearest resistance edge and its % from the buy | $293.55 +6.6% | $293.55 +6.6% | PASS |  |  |
| KEYS | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| KEYS | TS6 | Risk $ (and reward $ per share) | Risk $31.15 to make $18.28 a share | Risk $31.15 to make $18.28 | PASS |  |  |
| LIN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $521.23 – $525.87 · 2.2% above · turned here 4× | $521.23 – $525.87 · 2.2% · 4× | PASS |  |  |
| LIN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| LIN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $506.78 – $510.65 · price is inside this zone · turned here 3× | $506.78 – $510.65 · 0.0% · 3× | PASS |  |  |
| LIN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.7168 | 8.7169 | PASS |  |  |
| LIN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| LIN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| LIN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| LIN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $510.21 | $510.21 | PASS |  |  |
| LIN | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 510.21, zone 506.78-510.65 | inside the zone | PASS |  |  |
| LIN | TS1c | S5: the Buy on the bar = the Buy in the box | $510.21 | $510.21 | PASS |  |  |
| LIN | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 510.21 vs last close 510.21 | Buy <= last close | PASS |  |  |
| LIN | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| LIN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $492.78 -3.4% | $492.78 -3.4% | PASS |  |  |
| LIN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LIN | TS4 | Target = nearest resistance edge and its % from the buy | $521.23 +2.2% | $521.23 +2.2% | PASS |  |  |
| LIN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| LIN | TS6 | Risk $ (and reward $ per share) | Risk $17.43 to make $11.02 a share | Risk $17.43 to make $11.02 | PASS |  |  |
| LLY | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| LLY | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| LLY | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,333.22 · 1.3% below · turned here 1× | $1,333.22 · 1.3% · 1× | PASS |  |  |
| LLY | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 43.3603 | 43.3605 | PASS |  |  |
| LLY | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| LLY | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| LLY | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| LLY | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,333.22 | $1,333.22 | PASS |  |  |
| LLY | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1333.22, nearest zone high 1333.22 | equal | PASS |  |  |
| LLY | TS1c | S5: the Buy on the bar = the Buy in the box | $1,333.22 | $1,333.22 | PASS |  |  |
| LLY | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.3% below | 1.3% below | PASS |  |  |
| LLY | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $1,246.50 -6.5% | $1,246.50 -6.5% | PASS |  |  |
| LLY | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LLY | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| LLY | TS6 | Risk $ (and reward $ per share) | Risk $86.72 a share | Risk $86.72 | PASS |  |  |
| MDA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $39.61 – $41.67 · 3.0% above · turned here 6× | $39.61 – $41.67 · 3.0% · 6× | PASS |  |  |
| MDA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MDA.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.15 · 0.8% below · turned here 1× | $38.15 · 0.8% · 1× | PASS |  |  |
| MDA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2069 | 2.2070 | PASS |  |  |
| MDA.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MDA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| MDA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| MDA.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.15 | $38.15 | PASS |  |  |
| MDA.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 38.15, nearest zone high 38.15 | equal | PASS |  |  |
| MDA.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $38.15 | $38.15 | PASS |  |  |
| MDA.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| MDA.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $33.74 -11.6% | $33.74 -11.6% | PASS |  |  |
| MDA.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MDA.TO | TS4 | Target = nearest resistance edge and its % from the buy | $39.61 +3.8% | $39.61 +3.8% | PASS |  |  |
| MDA.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MDA.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.41 to make $1.46 a share | Risk $4.41 to make $1.46 | PASS |  |  |
| META | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $600.00 – $612.43 · 0.6% above · turned here 3× | $600.00 – $612.43 · 0.6% · 3× | PASS |  |  |
| META | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| META | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $577.07 – $594.81 · 0.2% below · turned here 5× | $577.07 – $594.81 · 0.2% · 5× | PASS |  |  |
| META | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 22.1742 | 22.1740 | PASS |  |  |
| META | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| META | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| META | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| META | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $594.81 | $594.81 | PASS |  |  |
| META | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 594.81, nearest zone high 594.81 | equal | PASS |  |  |
| META | TS1c | S5: the Buy on the bar = the Buy in the box | $594.81 | $594.81 | PASS |  |  |
| META | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.2% below | 0.2% below | PASS |  |  |
| META | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $550.46 -7.5% | $550.46 -7.5% | PASS |  |  |
| META | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| META | TS4 | Target = nearest resistance edge and its % from the buy | $600.00 +0.9% | $600.00 +0.9% | PASS |  |  |
| META | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| META | TS6 | Risk $ (and reward $ per share) | Risk $44.35 to make $5.19 a share | Risk $44.35 to make $5.19 | PASS |  |  |
| METU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.19 – $20.95 · 0.9% above · turned here 2× | $20.19 – $20.95 · 0.9% · 2× | PASS |  |  |
| METU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| METU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $18.62 – $19.29 · 3.6% below · turned here 4× | $18.62 – $19.29 · 3.6% · 4× | PASS |  |  |
| METU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6224 | 1.6224 | PASS |  |  |
| METU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| METU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| METU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| METU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $19.29 | $19.29 | PASS |  |  |
| METU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 19.29, nearest zone high 19.29 | equal | PASS |  |  |
| METU | TS1c | S5: the Buy on the bar = the Buy in the box | $19.29 | $19.29 | PASS |  |  |
| METU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.6% below | 3.6% below | PASS |  |  |
| METU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $16.05 -16.8% | $16.05 -16.8% | PASS |  |  |
| METU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| METU | TS4 | Target = nearest resistance edge and its % from the buy | $20.19 +4.7% | $20.19 +4.7% | PASS |  |  |
| METU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| METU | TS6 | Risk $ (and reward $ per share) | Risk $3.24 to make $0.90 a share | Risk $3.24 to make $0.90 | PASS |  |  |
| MRVL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $146.85 · 6.1% above · turned here 1× | $146.85 · 6.1% · 1× | PASS |  |  |
| MRVL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MRVL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $132.54 · 4.3% below · turned here 1× | $132.54 · 4.3% · 1× | PASS |  |  |
| MRVL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 15.9155 | 15.9152 | PASS |  |  |
| MRVL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MRVL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| MRVL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| MRVL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $132.54 | $132.54 | PASS |  |  |
| MRVL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 132.54, nearest zone high 132.54 | equal | PASS |  |  |
| MRVL | TS1c | S5: the Buy on the bar = the Buy in the box | $132.54 | $132.54 | PASS |  |  |
| MRVL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.3% below | 4.3% below | PASS |  |  |
| MRVL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $100.71 -24.0% | $100.71 -24.0% | PASS |  |  |
| MRVL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MRVL | TS4 | Target = nearest resistance edge and its % from the buy | $146.85 +10.8% | $146.85 +10.8% | PASS |  |  |
| MRVL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| MRVL | TS6 | Risk $ (and reward $ per share) | Risk $31.83 to make $14.31 a share | Risk $31.83 to make $14.31 | PASS |  |  |
| MSFT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $504.96 – $517.78 · 1.3% above · turned here 3× | $504.96 – $517.78 · 1.3% · 3× | PASS |  |  |
| MSFT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MSFT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $476.25 – $490.39 · 1.6% below · turned here 6× | $476.25 – $490.39 · 1.6% · 6× | PASS |  |  |
| MSFT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 15.9173 | 15.9173 | PASS |  |  |
| MSFT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MSFT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| MSFT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| MSFT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $490.39 | $490.39 | PASS |  |  |
| MSFT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 490.39, nearest zone high 490.39 | equal | PASS |  |  |
| MSFT | TS1c | S5: the Buy on the bar = the Buy in the box | $490.39 | $490.39 | PASS |  |  |
| MSFT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.6% below | 1.6% below | PASS |  |  |
| MSFT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $458.56 -6.5% | $458.56 -6.5% | PASS |  |  |
| MSFT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFT | TS4 | Target = nearest resistance edge and its % from the buy | $504.96 +3.0% | $504.96 +3.0% | PASS |  |  |
| MSFT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| MSFT | TS6 | Risk $ (and reward $ per share) | Risk $31.83 to make $14.57 a share | Risk $31.83 to make $14.57 | PASS |  |  |
| MSFU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.64 – $38.69 · 3.7% above · turned here 4× | $37.64 – $38.69 · 3.7% · 4× | PASS |  |  |
| MSFU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MSFU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $34.44 – $36.15 · 0.4% below · turned here 4× | $34.44 – $36.15 · 0.4% · 4× | PASS |  |  |
| MSFU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4138 | 2.4137 | PASS |  |  |
| MSFU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MSFU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| MSFU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| MSFU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $36.15 | $36.15 | PASS |  |  |
| MSFU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 36.15, nearest zone high 36.15 | equal | PASS |  |  |
| MSFU | TS1c | S5: the Buy on the bar = the Buy in the box | $36.15 | $36.15 | PASS |  |  |
| MSFU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| MSFU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.32 -13.4% | $31.32 -13.4% | PASS |  |  |
| MSFU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFU | TS4 | Target = nearest resistance edge and its % from the buy | $37.64 +4.1% | $37.64 +4.1% | PASS |  |  |
| MSFU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MSFU | TS6 | Risk $ (and reward $ per share) | Risk $4.83 to make $1.49 a share | Risk $4.83 to make $1.49 | PASS |  |  |
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
| MU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $32.56 · 8.1% above · turned here 1× | $32.56 · 8.1% · 1× | PASS |  |  |
| MU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $28.57 – $28.78 · 4.5% below · turned here 2× | $28.57 – $28.78 · 4.5% · 2× | PASS |  |  |
| MU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5224 | 2.5224 | PASS |  |  |
| MU.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| MU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| MU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $28.78 | $28.78 | PASS |  |  |
| MU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 28.78, nearest zone high 28.78 | equal | PASS |  |  |
| MU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $28.78 | $28.78 | PASS |  |  |
| MU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.5% below | 4.5% below | PASS |  |  |
| MU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $23.74 -17.5% | $23.74 -17.5% | PASS |  |  |
| MU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $32.56 +13.1% | $32.56 +13.1% | PASS |  |  |
| MU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| MU.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.04 to make $3.78 a share | Risk $5.04 to make $3.78 | PASS |  |  |
| NEE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $86.32 – $86.63 · 3.0% above · turned here 2× | $86.32 – $86.63 · 3.0% · 2× | PASS |  |  |
| NEE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $83.38 – $84.38 · price is inside this zone · turned here 4× | $83.38 – $84.38 · 0.0% · 4× | PASS |  |  |
| NEE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6153 | 1.6157 | PASS |  |  |
| NEE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| NEE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| NEE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $83.79 | $83.79 | PASS |  |  |
| NEE | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 83.79, zone 83.38-84.38 | inside the zone | PASS |  |  |
| NEE | TS1c | S5: the Buy on the bar = the Buy in the box | $83.79 | $83.79 | PASS |  |  |
| NEE | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 83.79 vs last close 83.79 | Buy <= last close | PASS |  |  |
| NEE | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| NEE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $80.56 -3.9% | $80.56 -3.9% | PASS |  |  |
| NEE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEE | TS4 | Target = nearest resistance edge and its % from the buy | $86.32 +3.0% | $86.32 +3.0% | PASS |  |  |
| NEE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| NEE | TS6 | Risk $ (and reward $ per share) | Risk $3.23 to make $2.53 a share | Risk $3.23 to make $2.53 | PASS |  |  |
| NEM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $103.62 – $108.05 · 3.6% above · turned here 6× | $103.62 – $108.05 · 3.6% · 6× | PASS |  |  |
| NEM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $96.94 – $98.93 · 1.1% below · turned here 4× | $96.94 – $98.93 · 1.1% · 4× | PASS |  |  |
| NEM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.8367 | 4.8371 | PASS |  |  |
| NEM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| NEM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| NEM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| NEM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $98.93 | $98.93 | PASS |  |  |
| NEM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 98.93, nearest zone high 98.93 | equal | PASS |  |  |
| NEM | TS1c | S5: the Buy on the bar = the Buy in the box | $98.93 | $98.93 | PASS |  |  |
| NEM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| NEM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $89.26 -9.8% | $89.26 -9.8% | PASS |  |  |
| NEM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEM | TS4 | Target = nearest resistance edge and its % from the buy | $103.62 +4.7% | $103.62 +4.7% | PASS |  |  |
| NEM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| NEM | TS6 | Risk $ (and reward $ per share) | Risk $9.67 to make $4.69 a share | Risk $9.67 to make $4.69 | PASS |  |  |
| NFLX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $61.39 · 5.0% above · turned here 1× | $61.39 · 5.0% · 1× | PASS |  |  |
| NFLX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFLX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFLX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9123 | 1.9120 | PASS |  |  |
| NFLX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| NFLX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| NFLX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NFXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $10.57 · 11.9% above · turned here 1× | $10.57 · 11.9% · 1× | PASS |  |  |
| NFXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFXL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6884 | 0.6891 | PASS |  |  |
| NFXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| NFXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| NFXL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NTR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $94.12 · 0.1% above · turned here 1× | $94.12 · 0.1% · 1× | PASS |  |  |
| NTR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NTR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $90.45 – $93.21 · 0.8% below · turned here 4× | $90.45 – $93.21 · 0.8% · 4× | PASS |  |  |
| NTR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8701 | 2.8704 | PASS |  |  |
| NTR.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| NTR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| NTR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| NTR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $93.21 | $93.21 | PASS |  |  |
| NTR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 93.21, nearest zone high 93.21 | equal | PASS |  |  |
| NTR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $93.21 | $93.21 | PASS |  |  |
| NTR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| NTR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $87.47 -6.2% | $87.47 -6.2% | PASS |  |  |
| NTR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NTR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $94.12 +1.0% | $94.12 +1.0% | PASS |  |  |
| NTR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| NTR.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.74 to make $0.91 a share | Risk $5.74 to make $0.91 | PASS |  |  |
| NVDA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $163.90 · 12.3% above · turned here 1× | $163.90 · 12.3% · 1× | PASS |  |  |
| NVDA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NVDA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.8765 | 9.8765 | PASS |  |  |
| NVDA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| NVDA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| NVDA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NVDL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| NVDL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Insufficient data | Insufficient data | PASS |  |  |
| NVDL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4655 | 2.4666 | PASS |  |  |
| NVDL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| ONTO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $204.07 · 4.2% above · turned here 1× | $204.07 · 4.2% · 1× | PASS |  |  |
| ONTO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ONTO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $188.28 – $195.19 · 0.4% below · turned here 2× | $188.28 – $195.19 · 0.4% · 2× | PASS |  |  |
| ONTO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.9022 | 16.9020 | PASS |  |  |
| ONTO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ONTO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ONTO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ONTO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $195.19 | $195.19 | PASS |  |  |
| ONTO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 195.19, nearest zone high 195.19 | equal | PASS |  |  |
| ONTO | TS1c | S5: the Buy on the bar = the Buy in the box | $195.19 | $195.19 | PASS |  |  |
| ONTO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| ONTO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $161.39 -17.3% | $161.39 -17.3% | PASS |  |  |
| ONTO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ONTO | TS4 | Target = nearest resistance edge and its % from the buy | $204.07 +4.5% | $204.07 +4.5% | PASS |  |  |
| ONTO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ONTO | TS6 | Risk $ (and reward $ per share) | Risk $33.80 to make $8.88 a share | Risk $33.80 to make $8.88 | PASS |  |  |
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
| ORCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $114.08 · 3.2% above · turned here 1× | $114.08 · 3.2% · 1× | PASS |  |  |
| ORCL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ORCL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.21 · 1.2% below · turned here 1× | $109.21 · 1.2% · 1× | PASS |  |  |
| ORCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.7528 | 7.7528 | PASS |  |  |
| ORCL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ORCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| ORCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| ORCL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.21 | $109.21 | PASS |  |  |
| ORCL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.21, nearest zone high 109.21 | equal | PASS |  |  |
| ORCL | TS1c | S5: the Buy on the bar = the Buy in the box | $109.21 | $109.21 | PASS |  |  |
| ORCL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| ORCL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $93.70 -14.2% | $93.70 -14.2% | PASS |  |  |
| ORCL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ORCL | TS4 | Target = nearest resistance edge and its % from the buy | $114.08 +4.5% | $114.08 +4.5% | PASS |  |  |
| ORCL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ORCL | TS6 | Risk $ (and reward $ per share) | Risk $15.51 to make $4.87 a share | Risk $15.51 to make $4.87 | PASS |  |  |
| PG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $170.52 · 1.6% above · turned here 1× | $170.52 · 1.6% · 1× | PASS |  |  |
| PG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| PG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $165.75 · 1.3% below · turned here 1× | $165.75 · 1.3% · 1× | PASS |  |  |
| PG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.158 | 3.1579 | PASS |  |  |
| PG | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| PG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| PG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| PG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $165.75 | $165.75 | PASS |  |  |
| PG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 165.75, nearest zone high 165.75 | equal | PASS |  |  |
| PG | TS1c | S5: the Buy on the bar = the Buy in the box | $165.75 | $165.75 | PASS |  |  |
| PG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.3% below | 1.3% below | PASS |  |  |
| PG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $159.43 -3.8% | $159.43 -3.8% | PASS |  |  |
| PG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PG | TS4 | Target = nearest resistance edge and its % from the buy | $170.52 +2.9% | $170.52 +2.9% | PASS |  |  |
| PG | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| PG | TS6 | Risk $ (and reward $ per share) | Risk $6.32 to make $4.77 a share | Risk $6.32 to make $4.77 | PASS |  |  |
| PLD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $125.38 – $127.69 · 1.6% above · turned here 5× | $125.38 – $127.69 · 1.6% · 5× | PASS |  |  |
| PLD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| PLD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $122.60 – $124.69 · price is inside this zone · turned here 6× | $122.60 – $124.69 · 0.0% · 6× | PASS |  |  |
| PLD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4319 | 2.4319 | PASS |  |  |
| PLD | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| PLD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| PLD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| PLD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $123.36 | $123.36 | PASS |  |  |
| PLD | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 123.36, zone 122.6-124.69 | inside the zone | PASS |  |  |
| PLD | TS1c | S5: the Buy on the bar = the Buy in the box | $123.36 | $123.36 | PASS |  |  |
| PLD | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 123.36 vs last close 123.36 | Buy <= last close | PASS |  |  |
| PLD | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| PLD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $118.50 -3.9% | $118.50 -3.9% | PASS |  |  |
| PLD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PLD | TS4 | Target = nearest resistance edge and its % from the buy | $125.38 +1.6% | $125.38 +1.6% | PASS |  |  |
| PLD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| PLD | TS6 | Risk $ (and reward $ per share) | Risk $4.86 to make $2.02 a share | Risk $4.86 to make $2.02 | PASS |  |  |
| PNG.V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3.30 · 14.6% above · turned here 1× | $3.30 · 14.6% · 1× | PASS |  |  |
| PNG.V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| PNG.V | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| PNG.V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.2236 | 0.2239 | PASS |  |  |
| PNG.V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| PNG.V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| PNG.V | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QCOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $164.77 – $172.12 · 1.7% above · turned here 6× | $164.77 – $172.12 · 1.7% · 6× | PASS |  |  |
| QCOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QCOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $156.22 – $158.85 · 2.0% below · turned here 2× | $156.22 – $158.85 · 2.0% · 2× | PASS |  |  |
| QCOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.0295 | 9.0293 | PASS |  |  |
| QCOM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| QCOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| QCOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| QCOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $158.85 | $158.85 | PASS |  |  |
| QCOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 158.85, nearest zone high 158.85 | equal | PASS |  |  |
| QCOM | TS1c | S5: the Buy on the bar = the Buy in the box | $158.85 | $158.85 | PASS |  |  |
| QCOM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| QCOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $140.79 -11.4% | $140.79 -11.4% | PASS |  |  |
| QCOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QCOM | TS4 | Target = nearest resistance edge and its % from the buy | $164.77 +3.7% | $164.77 +3.7% | PASS |  |  |
| QCOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| QCOM | TS6 | Risk $ (and reward $ per share) | Risk $18.06 to make $5.92 a share | Risk $18.06 to make $5.92 | PASS |  |  |
| QPUX | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| QPUX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Insufficient data | Insufficient data | PASS |  |  |
| QPUX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| QPUX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8362 | 0.8364 | PASS |  |  |
| QPUX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QTUM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $126.93 · 6.0% above · turned here 1× | $126.93 · 6.0% · 1× | PASS |  |  |
| QTUM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QTUM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $118.34 – $120.53 · price is inside this zone · turned here 4× | $118.34 – $120.53 · 0.0% · 4× | PASS |  |  |
| QTUM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.7846 | 4.7846 | PASS |  |  |
| QTUM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| QTUM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| QTUM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| QTUM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $119.71 | $119.71 | PASS |  |  |
| QTUM | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 119.71, zone 118.34-120.53 | inside the zone | PASS |  |  |
| QTUM | TS1c | S5: the Buy on the bar = the Buy in the box | $119.71 | $119.71 | PASS |  |  |
| QTUM | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 119.71 vs last close 119.71 | Buy <= last close | PASS |  |  |
| QTUM | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| QTUM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $110.14 -8.0% | $110.14 -8.0% | PASS |  |  |
| QTUM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QTUM | TS4 | Target = nearest resistance edge and its % from the buy | $126.93 +6.0% | $126.93 +6.0% | PASS |  |  |
| QTUM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| QTUM | TS6 | Risk $ (and reward $ per share) | Risk $9.57 to make $7.22 a share | Risk $9.57 to make $7.22 | PASS |  |  |
| RBOT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $28.00 · 3.4% above · turned here 1× | $28.00 · 3.4% · 1× | PASS |  |  |
| RBOT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| RBOT.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| RBOT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.585 | 0.5846 | PASS |  |  |
| RBOT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| RBOT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| RBOT.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| RTX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $203.03 – $206.73 · 5.0% above · turned here 7× | $203.03 – $206.73 · 5.0% · 7× | PASS |  |  |
| RTX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RTX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $192.59 – $194.17 · price is inside this zone · turned here 5× | $192.59 – $194.17 · 0.0% · 5× | PASS |  |  |
| RTX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.2345 | 5.2343 | PASS |  |  |
| RTX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| RTX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| RTX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| RTX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $193.44 | $193.44 | PASS |  |  |
| RTX | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 193.44, zone 192.59-194.17 | inside the zone | PASS |  |  |
| RTX | TS1c | S5: the Buy on the bar = the Buy in the box | $193.44 | $193.44 | PASS |  |  |
| RTX | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 193.44 vs last close 193.44 | Buy <= last close | PASS |  |  |
| RTX | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| RTX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $182.97 -5.4% | $182.97 -5.4% | PASS |  |  |
| RTX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RTX | TS4 | Target = nearest resistance edge and its % from the buy | $203.03 +5.0% | $203.03 +5.0% | PASS |  |  |
| RTX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| RTX | TS6 | Risk $ (and reward $ per share) | Risk $10.47 to make $9.59 a share | Risk $10.47 to make $9.59 | PASS |  |  |
| RY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $275.78 · 2.3% above · turned here 1× | $275.78 · 2.3% · 1× | PASS |  |  |
| RY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $267.28 · 0.8% below · turned here 1× | $267.28 · 0.8% · 1× | PASS |  |  |
| RY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.0919 | 5.0918 | PASS |  |  |
| RY.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| RY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| RY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| RY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $267.28 | $267.28 | PASS |  |  |
| RY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 267.28, nearest zone high 267.28 | equal | PASS |  |  |
| RY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $267.28 | $267.28 | PASS |  |  |
| RY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| RY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $257.10 -3.8% | $257.10 -3.8% | PASS |  |  |
| RY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $275.78 +3.2% | $275.78 +3.2% | PASS |  |  |
| RY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| RY.TO | TS6 | Risk $ (and reward $ per share) | Risk $10.18 to make $8.50 a share | Risk $10.18 to make $8.50 | PASS |  |  |
| SETM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $23.68 – $23.88 · 14.7% above · turned here 2× | $23.68 – $23.88 · 14.7% · 2× | PASS |  |  |
| SETM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| SETM | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SETM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9871 | 0.9870 | PASS |  |  |
| SETM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| SETM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| SETM | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SGRD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $18.27 · 3.3% above · turned here 1× | $18.27 · 3.3% · 1× | PASS |  |  |
| SGRD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $17.20 · 2.8% below · turned here 1× | $17.20 · 2.8% · 1× | PASS |  |  |
| SGRD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.3772 | 0.3772 | PASS |  |  |
| SGRD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SGRD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| SGRD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| SGRD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $17.20 | $17.20 | PASS |  |  |
| SGRD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 17.2, nearest zone high 17.2 | equal | PASS |  |  |
| SGRD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $17.20 | $17.20 | PASS |  |  |
| SGRD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.8% below | 2.8% below | PASS |  |  |
| SGRD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $16.45 -4.4% | $16.45 -4.4% | PASS |  |  |
| SGRD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SGRD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $18.27 +6.2% | $18.27 +6.2% | PASS |  |  |
| SGRD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.4 : 1 | 1.4 : 1 | PASS |  |  |
| SGRD.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.75 to make $1.07 a share | Risk $0.75 to make $1.07 | PASS |  |  |
| SMH | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $503.63 · 12.5% above · turned here 1× | $503.63 · 12.5% · 1× | PASS |  |  |
| SMH | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 35.3 | 3 of 8 trend checks pass · ADX 35.3 | PASS |  |  |
| SMH | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $445.59 · 0.4% below · turned here 1× | $445.59 · 0.4% · 1× | PASS |  |  |
| SMH | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 24.2418 | 24.2418 | PASS |  |  |
| SMH | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SMH | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| SMH | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| SMH | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $445.59 | $445.59 | PASS |  |  |
| SMH | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 445.59, nearest zone high 445.59 | equal | PASS |  |  |
| SMH | TS1c | S5: the Buy on the bar = the Buy in the box | $445.59 | $445.59 | PASS |  |  |
| SMH | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| SMH | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $397.11 -10.9% | $397.11 -10.9% | PASS |  |  |
| SMH | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SMH | TS4 | Target = nearest resistance edge and its % from the buy | $503.63 +13.0% | $503.63 +13.0% | PASS |  |  |
| SMH | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| SMH | TS6 | Risk $ (and reward $ per share) | Risk $48.48 to make $58.04 a share | Risk $48.48 to make $58.04 | PASS |  |  |
| SNDK.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $19.52 · 6.4% above · turned here 1× | $19.52 · 6.4% · 1× | PASS |  |  |
| SNDK.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SNDK.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.3834 | 2.3834 | PASS |  |  |
| SNDK.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| SNDK.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| SNDK.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $94.94 – $96.09 · 1.8% above · turned here 4× | $94.94 – $96.09 · 1.8% · 4× | PASS |  |  |
| SO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $92.72 – $93.41 · price is inside this zone · turned here 3× | $92.72 – $93.41 · 0.0% · 3× | PASS |  |  |
| SO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.7908 | 1.7911 | PASS |  |  |
| SO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| SO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| SO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| SO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $93.29 | $93.29 | PASS |  |  |
| SO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 93.29, zone 92.72-93.41 | inside the zone | PASS |  |  |
| SO | TS1c | S5: the Buy on the bar = the Buy in the box | $93.29 | $93.29 | PASS |  |  |
| SO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 93.29 vs last close 93.29 | Buy <= last close | PASS |  |  |
| SO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| SO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $89.71 -3.8% | $89.71 -3.8% | PASS |  |  |
| SO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SO | TS4 | Target = nearest resistance edge and its % from the buy | $94.94 +1.8% | $94.94 +1.8% | PASS |  |  |
| SO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| SO | TS6 | Risk $ (and reward $ per share) | Risk $3.58 to make $1.65 a share | Risk $3.58 to make $1.65 | PASS |  |  |
| SOXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $48.47 – $50.06 · 7.0% above · turned here 3× | $48.47 – $50.06 · 7.0% · 3× | PASS |  |  |
| SOXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.68 – $44.50 · 1.8% below · turned here 5× | $35.68 – $44.50 · 1.8% · 5× | PASS |  |  |
| SOXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 11.7218 | 11.7220 | PASS |  |  |
| SOXL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SOXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $44.50 | $44.50 | PASS |  |  |
| SOXL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 44.5, nearest zone high 44.5 | equal | PASS |  |  |
| SOXL | TS1c | S5: the Buy on the bar = the Buy in the box | $44.50 | $44.50 | PASS |  |  |
| SOXL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% below | 1.8% below | PASS |  |  |
| SOXL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $21.06 -52.7% | $21.06 -52.7% | PASS |  |  |
| SOXL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL | TS4 | Target = nearest resistance edge and its % from the buy | $48.47 +8.9% | $48.47 +8.9% | PASS |  |  |
| SOXL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| SOXL | TS6 | Risk $ (and reward $ per share) | Risk $23.44 to make $3.97 a share | Risk $23.44 to make $3.97 | PASS |  |  |
| SOXL.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $12.05 – $13.46 · 5.5% above · turned here 3× | $12.05 – $13.46 · 5.5% · 3× | PASS |  |  |
| SOXL.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $10.19 – $10.73 · 6.0% below · turned here 3× | $10.19 – $10.73 · 6.0% · 3× | PASS |  |  |
| SOXL.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.8485 | 1.8485 | PASS |  |  |
| SOXL.NE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SOXL.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| SOXL.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| SOXL.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $10.73 | $10.73 | PASS |  |  |
| SOXL.NE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 10.73, nearest zone high 10.73 | equal | PASS |  |  |
| SOXL.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $10.73 | $10.73 | PASS |  |  |
| SOXL.NE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.0% below | 6.0% below | PASS |  |  |
| SOXL.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $7.03 -34.5% | $7.03 -34.5% | PASS |  |  |
| SOXL.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL.NE | TS4 | Target = nearest resistance edge and its % from the buy | $12.05 +12.3% | $12.05 +12.3% | PASS |  |  |
| SOXL.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| SOXL.NE | TS6 | Risk $ (and reward $ per share) | Risk $3.70 to make $1.32 a share | Risk $3.70 to make $1.32 | PASS |  |  |
| SOXX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $154.59 – $162.96 · 12.1% above · turned here 5× | $154.59 – $162.96 · 12.1% · 5× | PASS |  |  |
| SOXX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $130.75 · 5.2% below · turned here 1× | $130.75 · 5.2% · 1× | PASS |  |  |
| SOXX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.3726 | 8.3729 | PASS |  |  |
| SOXX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SOXX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| SOXX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| SOXX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $130.75 | $130.75 | PASS |  |  |
| SOXX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 130.75, nearest zone high 130.75 | equal | PASS |  |  |
| SOXX | TS1c | S5: the Buy on the bar = the Buy in the box | $130.75 | $130.75 | PASS |  |  |
| SOXX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.2% below | 5.2% below | PASS |  |  |
| SOXX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $114.00 -12.8% | $114.00 -12.8% | PASS |  |  |
| SOXX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXX | TS4 | Target = nearest resistance edge and its % from the buy | $154.59 +18.2% | $154.59 +18.2% | PASS |  |  |
| SOXX | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.4 : 1 | 1.4 : 1 | PASS |  |  |
| SOXX | TS6 | Risk $ (and reward $ per share) | Risk $16.75 to make $23.84 a share | Risk $16.75 to make $23.84 | PASS |  |  |
| SPCL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| SPCL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $8.20 · 8.0% below · turned here 1× | $8.20 · 8.0% · 1× | PASS |  |  |
| SPCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6723 | 1.6727 | PASS |  |  |
| SPCL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SPCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| SPCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| SPCL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $8.20 | $8.20 | PASS |  |  |
| SPCL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 8.2, nearest zone high 8.2 | equal | PASS |  |  |
| SPCL | TS1c | S5: the Buy on the bar = the Buy in the box | $8.20 | $8.20 | PASS |  |  |
| SPCL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 8.0% below | 8.0% below | PASS |  |  |
| SPCL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $4.86 -40.8% | $4.86 -40.8% | PASS |  |  |
| SPCL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SPCL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| SPCL | TS6 | Risk $ (and reward $ per share) | Risk $3.34 a share | Risk $3.34 | PASS |  |  |
| TSLA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $380.15 – $393.63 · 1.5% above · turned here 7× | $380.15 – $393.63 · 1.5% · 7× | PASS |  |  |
| TSLA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLA | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $364.02 – $368.60 · 1.6% below · turned here 3× | $364.02 – $368.60 · 1.6% · 3× | PASS |  |  |
| TSLA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.145 | 16.1451 | PASS |  |  |
| TSLA | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| TSLA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| TSLA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| TSLA | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $368.60 | $368.60 | PASS |  |  |
| TSLA | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 368.6, nearest zone high 368.6 | equal | PASS |  |  |
| TSLA | TS1c | S5: the Buy on the bar = the Buy in the box | $368.60 | $368.60 | PASS |  |  |
| TSLA | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.6% below | 1.6% below | PASS |  |  |
| TSLA | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $336.31 -8.8% | $336.31 -8.8% | PASS |  |  |
| TSLA | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLA | TS4 | Target = nearest resistance edge and its % from the buy | $380.15 +3.1% | $380.15 +3.1% | PASS |  |  |
| TSLA | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| TSLA | TS6 | Risk $ (and reward $ per share) | Risk $32.29 to make $11.55 a share | Risk $32.29 to make $11.55 | PASS |  |  |
| TSLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $9.76 – $9.90 · 2.4% above · turned here 2× | $9.76 – $9.90 · 2.4% · 2× | PASS |  |  |
| TSLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $8.56 – $9.04 · 5.1% below · turned here 3× | $8.56 – $9.04 · 5.1% · 3× | PASS |  |  |
| TSLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8496 | 0.8496 | PASS |  |  |
| TSLL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| TSLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| TSLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| TSLL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $9.04 | $9.04 | PASS |  |  |
| TSLL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 9.04, nearest zone high 9.04 | equal | PASS |  |  |
| TSLL | TS1c | S5: the Buy on the bar = the Buy in the box | $9.04 | $9.04 | PASS |  |  |
| TSLL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.1% below | 5.1% below | PASS |  |  |
| TSLL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $7.34 -18.8% | $7.34 -18.8% | PASS |  |  |
| TSLL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLL | TS4 | Target = nearest resistance edge and its % from the buy | $9.76 +8.0% | $9.76 +8.0% | PASS |  |  |
| TSLL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| TSLL | TS6 | Risk $ (and reward $ per share) | Risk $1.70 to make $0.72 a share | Risk $1.70 to make $0.72 | PASS |  |  |
| TSM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $371.72 – $387.17 · 5.6% above · turned here 6× | $371.72 – $387.17 · 5.6% · 6× | PASS |  |  |
| TSM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $348.59 – $358.75 · price is inside this zone · turned here 4× | $348.59 – $358.75 · 0.0% · 4× | PASS |  |  |
| TSM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.9377 | 17.9374 | PASS |  |  |
| TSM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| TSM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| TSM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| TSM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $352.09 | $352.09 | PASS |  |  |
| TSM | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 352.09, zone 348.59-358.75 | inside the zone | PASS |  |  |
| TSM | TS1c | S5: the Buy on the bar = the Buy in the box | $352.09 | $352.09 | PASS |  |  |
| TSM | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 352.09 vs last close 352.09 | Buy <= last close | PASS |  |  |
| TSM | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| TSM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $316.21 -10.2% | $316.21 -10.2% | PASS |  |  |
| TSM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSM | TS4 | Target = nearest resistance edge and its % from the buy | $371.72 +5.6% | $371.72 +5.6% | PASS |  |  |
| TSM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| TSM | TS6 | Risk $ (and reward $ per share) | Risk $35.88 to make $19.63 a share | Risk $35.88 to make $19.63 | PASS |  |  |
| UBOT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $16.00 · 11.6% above · turned here 1× | $16.00 · 11.6% · 1× | PASS |  |  |
| UBOT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| UBOT | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| UBOT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8177 | 0.8178 | PASS |  |  |
| UBOT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| UBOT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| UBOT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| UFO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $38.31 – $39.36 · 0.9% above · turned here 3× | $38.31 – $39.36 · 0.9% · 3× | PASS |  |  |
| UFO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| UFO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $36.70 · 3.3% below · turned here 1× | $36.70 · 3.3% · 1× | PASS |  |  |
| UFO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.3804 | 1.3807 | PASS |  |  |
| UFO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| UFO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| UFO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| UFO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $36.70 | $36.70 | PASS |  |  |
| UFO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 36.7, nearest zone high 36.7 | equal | PASS |  |  |
| UFO | TS1c | S5: the Buy on the bar = the Buy in the box | $36.70 | $36.70 | PASS |  |  |
| UFO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.3% below | 3.3% below | PASS |  |  |
| UFO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $33.94 -7.5% | $33.94 -7.5% | PASS |  |  |
| UFO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| UFO | TS4 | Target = nearest resistance edge and its % from the buy | $38.31 +4.4% | $38.31 +4.4% | PASS |  |  |
| UFO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| UFO | TS6 | Risk $ (and reward $ per share) | Risk $2.76 to make $1.61 a share | Risk $2.76 to make $1.61 | PASS |  |  |
| URA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.40 · 6.1% above · turned here 1× | $30.40 · 6.1% · 1× | PASS |  |  |
| URA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| URA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| URA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.3971 | 1.3971 | PASS |  |  |
| URA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| URA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| URA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| URAA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $11.65 · 12.3% above · turned here 1× | $11.65 · 12.3% · 1× | PASS |  |  |
| URAA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| URAA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| URAA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.1204 | 1.1207 | PASS |  |  |
| URAA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| URAA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| URAA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $414.60 · 3.1% above · turned here 1× | $414.60 · 3.1% · 1× | PASS |  |  |
| V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| V | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $394.00 · 2.1% below · turned here 1× | $394.00 · 2.1% · 1× | PASS |  |  |
| V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.0485 | 9.0482 | PASS |  |  |
| V | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| V | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $394.00 | $394.00 | PASS |  |  |
| V | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 394, nearest zone high 394 | equal | PASS |  |  |
| V | TS1c | S5: the Buy on the bar = the Buy in the box | $394.00 | $394.00 | PASS |  |  |
| V | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| V | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $375.90 -4.6% | $375.90 -4.6% | PASS |  |  |
| V | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| V | TS4 | Target = nearest resistance edge and its % from the buy | $414.60 +5.2% | $414.60 +5.2% | PASS |  |  |
| V | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.1 : 1 | 1.1 : 1 | PASS |  |  |
| V | TS6 | Risk $ (and reward $ per share) | Risk $18.10 to make $20.60 a share | Risk $18.10 to make $20.60 | PASS |  |  |
| VFV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $185.71 – $186.79 · 1.5% above · turned here 4× | $185.71 – $186.79 · 1.5% · 4× | PASS |  |  |
| VFV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VFV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $181.93 – $182.97 · price is inside this zone · turned here 3× | $181.93 – $182.97 · 0.0% · 3× | PASS |  |  |
| VFV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.004 | 3.0039 | PASS |  |  |
| VFV.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| VFV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| VFV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| VFV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $182.95 | $182.95 | PASS |  |  |
| VFV.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 182.95, zone 181.93-182.97 | inside the zone | PASS |  |  |
| VFV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $182.95 | $182.95 | PASS |  |  |
| VFV.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 182.95 vs last close 182.95 | Buy <= last close | PASS |  |  |
| VFV.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| VFV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $176.94 -3.3% | $176.94 -3.3% | PASS |  |  |
| VFV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VFV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $185.71 +1.5% | $185.71 +1.5% | PASS |  |  |
| VFV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| VFV.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.01 to make $2.76 a share | Risk $6.01 to make $2.76 | PASS |  |  |
| VRT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $200.26 · 8.3% above · turned here 1× | $200.26 · 8.3% · 1× | PASS |  |  |
| VRT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VRT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $180.68 – $189.53 · price is inside this zone · turned here 4× | $180.68 – $189.53 · 0.0% · 4× | PASS |  |  |
| VRT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.418 | 16.4177 | PASS |  |  |
| VRT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| VRT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| VRT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| VRT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $184.99 | $184.99 | PASS |  |  |
| VRT | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 184.99, zone 180.68-189.53 | inside the zone | PASS |  |  |
| VRT | TS1c | S5: the Buy on the bar = the Buy in the box | $184.99 | $184.99 | PASS |  |  |
| VRT | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 184.99 vs last close 184.99 | Buy <= last close | PASS |  |  |
| VRT | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| VRT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $152.15 -17.8% | $152.15 -17.8% | PASS |  |  |
| VRT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VRT | TS4 | Target = nearest resistance edge and its % from the buy | $200.26 +8.3% | $200.26 +8.3% | PASS |  |  |
| VRT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| VRT | TS6 | Risk $ (and reward $ per share) | Risk $32.84 to make $15.27 a share | Risk $32.84 to make $15.27 | PASS |  |  |
| WDC.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.20 · 12.3% above · turned here 1× | $20.20 · 12.3% · 1× | PASS |  |  |
| WDC.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $15.70 · 12.7% below · turned here 1× | $15.70 · 12.7% · 1× | PASS |  |  |
| WDC.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.4852 | 1.4852 | PASS |  |  |
| WDC.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| WDC.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| WDC.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| WDC.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 15.7, nearest zone high 15.7 | equal | PASS |  |  |
| WDC.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 12.7% below | 12.7% below | PASS |  |  |
| WDC.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.73 -18.9% | $12.73 -18.9% | PASS |  |  |
| WDC.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WDC.TO | TS4 | Target = nearest resistance edge and its % from the buy | $20.20 +28.7% | $20.20 +28.7% | PASS |  |  |
| WDC.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.5 : 1 | 1.5 : 1 | PASS |  |  |
| WDC.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.97 to make $4.50 a share | Risk $2.97 to make $4.50 | PASS |  |  |
| WELL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $249.75 · 2.7% above · turned here 1× | $249.75 · 2.7% · 1× | PASS |  |  |
| WELL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WELL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $243.04 · 0.1% below · turned here 1× | $243.04 · 0.1% · 1× | PASS |  |  |
| WELL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.2614 | 5.2615 | PASS |  |  |
| WELL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| WELL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| WELL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| WELL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $243.04 | $243.04 | PASS |  |  |
| WELL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 243.04, nearest zone high 243.04 | equal | PASS |  |  |
| WELL | TS1c | S5: the Buy on the bar = the Buy in the box | $243.04 | $243.04 | PASS |  |  |
| WELL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.1% below | 0.1% below | PASS |  |  |
| WELL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $232.52 -4.3% | $232.52 -4.3% | PASS |  |  |
| WELL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WELL | TS4 | Target = nearest resistance edge and its % from the buy | $249.75 +2.8% | $249.75 +2.8% | PASS |  |  |
| WELL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| WELL | TS6 | Risk $ (and reward $ per share) | Risk $10.52 to make $6.71 a share | Risk $10.52 to make $6.71 | PASS |  |  |
| WMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $128.75 – $129.69 · 2.2% above · turned here 2× | $128.75 – $129.69 · 2.2% · 2× | PASS |  |  |
| WMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $125.91 – $127.19 · price is inside this zone · turned here 3× | $125.91 – $127.19 · 0.0% · 3× | PASS |  |  |
| WMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.7737 | 2.7733 | PASS |  |  |
| WMT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| WMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| WMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| WMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $126.04 | $126.04 | PASS |  |  |
| WMT | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 126.04, zone 125.91-127.19 | inside the zone | PASS |  |  |
| WMT | TS1c | S5: the Buy on the bar = the Buy in the box | $126.04 | $126.04 | PASS |  |  |
| WMT | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 126.04 vs last close 126.04 | Buy <= last close | PASS |  |  |
| WMT | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| WMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $120.49 -4.4% | $120.49 -4.4% | PASS |  |  |
| WMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WMT | TS4 | Target = nearest resistance edge and its % from the buy | $128.75 +2.2% | $128.75 +2.2% | PASS |  |  |
| WMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| WMT | TS6 | Risk $ (and reward $ per share) | Risk $5.55 to make $2.71 a share | Risk $5.55 to make $2.71 | PASS |  |  |
| XCHP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $110.04 · 6.6% above · turned here 1× | $110.04 · 6.6% · 1× | PASS |  |  |
| XCHP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XCHP.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $95.50 · 7.5% below · turned here 1× | $95.50 · 7.5% · 1× | PASS |  |  |
| XCHP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.1667 | 6.1667 | PASS |  |  |
| XCHP.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XCHP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| XCHP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| XCHP.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $95.50 | $95.50 | PASS |  |  |
| XCHP.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 95.5, nearest zone high 95.5 | equal | PASS |  |  |
| XCHP.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $95.50 | $95.50 | PASS |  |  |
| XCHP.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.5% below | 7.5% below | PASS |  |  |
| XCHP.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $83.17 -12.9% | $83.17 -12.9% | PASS |  |  |
| XCHP.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XCHP.TO | TS4 | Target = nearest resistance edge and its % from the buy | $110.04 +15.2% | $110.04 +15.2% | PASS |  |  |
| XCHP.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| XCHP.TO | TS6 | Risk $ (and reward $ per share) | Risk $12.33 to make $14.54 a share | Risk $12.33 to make $14.54 | PASS |  |  |
| XDRV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $40.34 · 2.0% above · turned here 1× | $40.34 · 2.0% · 1× | PASS |  |  |
| XDRV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XDRV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.62 – $38.88 · 1.7% below · turned here 2× | $38.62 – $38.88 · 1.7% · 2× | PASS |  |  |
| XDRV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7991 | 0.7991 | PASS |  |  |
| XDRV.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XDRV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| XDRV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| XDRV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.88 | $38.88 | PASS |  |  |
| XDRV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 38.88, nearest zone high 38.88 | equal | PASS |  |  |
| XDRV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $38.88 | $38.88 | PASS |  |  |
| XDRV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.7% below | 1.7% below | PASS |  |  |
| XDRV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $37.28 -4.1% | $37.28 -4.1% | PASS |  |  |
| XDRV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XDRV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $40.34 +3.8% | $40.34 +3.8% | PASS |  |  |
| XDRV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| XDRV.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.60 to make $1.46 a share | Risk $1.60 to make $1.46 | PASS |  |  |
| XEQT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $43.93 – $44.41 · 1.5% above · turned here 5× | $43.93 – $44.41 · 1.5% · 5× | PASS |  |  |
| XEQT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XEQT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $42.88 · 0.9% below · turned here 1× | $42.88 · 0.9% · 1× | PASS |  |  |
| XEQT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.603 | 0.6027 | PASS |  |  |
| XEQT.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XEQT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| XEQT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| XEQT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $42.88 | $42.88 | PASS |  |  |
| XEQT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 42.88, nearest zone high 42.88 | equal | PASS |  |  |
| XEQT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $42.88 | $42.88 | PASS |  |  |
| XEQT.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.9% below | 0.9% below | PASS |  |  |
| XEQT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $41.67 -2.8% | $41.67 -2.8% | PASS |  |  |
| XEQT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XEQT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $43.93 +2.4% | $43.93 +2.4% | PASS |  |  |
| XEQT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| XEQT.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.21 to make $1.05 a share | Risk $1.21 to make $1.05 | PASS |  |  |
| XETM.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $64.70 · 15.1% above · turned here 1× | $64.70 · 15.1% · 1× | PASS |  |  |
| XETM.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| XETM.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4984 | 2.4984 | PASS |  |  |
| XETM.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| XETM.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| XETM.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| XGD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $48.17 – $48.35 · 2.9% above · turned here 2× | $48.17 – $48.35 · 2.9% · 2× | PASS |  |  |
| XGD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XGD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $45.90 – $47.23 · price is inside this zone · turned here 4× | $45.90 – $47.23 · 0.0% · 4× | PASS |  |  |
| XGD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1419 | 2.1419 | PASS |  |  |
| XGD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| XGD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| XGD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| XGD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $46.79 | $46.79 | PASS |  |  |
| XGD.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 46.79, zone 45.9-47.23 | inside the zone | PASS |  |  |
| XGD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $46.79 | $46.79 | PASS |  |  |
| XGD.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 46.79 vs last close 46.79 | Buy <= last close | PASS |  |  |
| XGD.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| XGD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $42.51 -9.2% | $42.51 -9.2% | PASS |  |  |
| XGD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XGD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $48.17 +2.9% | $48.17 +2.9% | PASS |  |  |
| XGD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| XGD.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.28 to make $1.38 a share | Risk $4.28 to make $1.38 | PASS |  |  |
| XOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $159.60 – $160.11 · 0.4% above · turned here 2× | $159.60 – $160.11 · 0.4% · 2× | PASS |  |  |
| XOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $154.91 – $159.07 · price is inside this zone · turned here 6× | $154.91 – $159.07 · 0.0% · 6× | PASS |  |  |
| XOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.3295 | 4.3294 | PASS |  |  |
| XOM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| XOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| XOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| XOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $158.93 | $158.93 | PASS |  |  |
| XOM | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 158.93, zone 154.91-159.07 | inside the zone | PASS |  |  |
| XOM | TS1c | S5: the Buy on the bar = the Buy in the box | $158.93 | $158.93 | PASS |  |  |
| XOM | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 158.93 vs last close 158.93 | Buy <= last close | PASS |  |  |
| XOM | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| XOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $150.27 -5.4% | $150.27 -5.4% | PASS |  |  |
| XOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XOM | TS4 | Target = nearest resistance edge and its % from the buy | $159.60 +0.4% | $159.60 +0.4% | PASS |  |  |
| XOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| XOM | TS6 | Risk $ (and reward $ per share) | Risk $8.66 to make $0.67 a share | Risk $8.66 to make $0.67 | PASS |  |  |
