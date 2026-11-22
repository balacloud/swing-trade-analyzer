# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-19T01:13 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 3621 · WRONG 64 (CRITICAL) · MISLEADING 19 (HIGH/LOW per row) · UNVERIFIED 10 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 109 | 7 |
| card-price-data | 218 | 0 |
| card-relative-strength | 400 | 0 |
| card-trade-setup | 724 | 0 |

Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).
Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).
NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| CEG | BO0 | Breakout card present when /api/breakout answered | card not found | card text | WRONG | CRITICAL |  |
| CEG | PD0 | Price Data card present (Price & Relative Strength opened) | card not found | card text | WRONG | CRITICAL |  |
| AVGC | RS1 | a history of 100 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| CEG | RS0 | Relative Strength card present | card not found | card text | WRONG | CRITICAL |  |
| COPZ | RS1 | a history of 193 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| DRAL | RS1 | a history of 103 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| DRAM | RS1 | a history of 160 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| ORBX.TO | RS1 | a history of 141 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SGRD.TO | RS1 | a history of 147 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SNDK.TO | RS1 | a history of 134 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| SPCL | RS1 | a history of 157 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| WDC.TO | RS1 | a history of 134 bars (<= 200) cannot give a 52-week RS: the card says N/A, never a number | a number | N/A | WRONG | CRITICAL |  |
| AAPL | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| AAPL | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| AAPL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 7.8727 | WRONG | CRITICAL |  |
| ABBV | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| ABBV | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| ABBV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 6.6624 | WRONG | CRITICAL |  |
| ALAB | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| ALAB | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| ALAB | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 23.6677 | WRONG | CRITICAL |  |
| AVGO | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| AVGO | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| AVGO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 17.6443 | WRONG | CRITICAL |  |
| CEG | TS0 | Trade Setup card present when /api/sr answered | card not found | card text | WRONG | CRITICAL |  |
| HD | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| HD | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| HD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 8.9189 | WRONG | CRITICAL |  |
| KEYS | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| KEYS | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| KEYS | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 15.9428 | WRONG | CRITICAL |  |
| LLY | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| LLY | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| LLY | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 43.5069 | WRONG | CRITICAL |  |
| META | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| META | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| META | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 22.0700 | WRONG | CRITICAL |  |
| MRVL | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| MRVL | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| MRVL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 16.3675 | WRONG | CRITICAL |  |
| MSFT | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| MSFT | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| MSFT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 15.3934 | WRONG | CRITICAL |  |
| NFLX | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| NFLX | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| NFLX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 1.8852 | WRONG | CRITICAL |  |
| NVDA | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| NVDA | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| NVDA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 9.7101 | WRONG | CRITICAL |  |
| PG | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| PG | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| PG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 3.2038 | WRONG | CRITICAL |  |
| SMH | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| SMH | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| SMH | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 23.5866 | WRONG | CRITICAL |  |
| V | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| V | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 8.8156 | WRONG | CRITICAL |  |
| VRT | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| VRT | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| VRT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 16.8603 | WRONG | CRITICAL |  |
| WMT | KL-resistance | Resistance row matches the nearest resistance zone | row not found | none | WRONG | CRITICAL |  |
| WMT | KL-support | Support row matches the nearest support zone | row not found | none | WRONG | CRITICAL |  |
| WMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | None | 2.6697 | WRONG | CRITICAL |  |
| ANET.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1M | bars: $1,629,896 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| AVGC | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $61,401.6 | bars: $60,851 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $573,610.2 | bars: $634,537 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $144,816.96 | bars: $96,451 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| DRAL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $954,885.95 | bars: $998,199 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| HURA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $445,382.34 | bars: $436,720 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| MTRX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $245,432.39 | bars: $271,914 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ORBX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $85,778.79 | bars: $92,115 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| QPUX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $903,765.28 | bars: $973,407 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| RBOT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $77,856.66 | bars: $85,217 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SGRD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $223,781.6 | bars: $160,631 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SPCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $348,241.6 | bars: $355,790 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| UBOT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $235,770.15 | bars: $241,357 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| XETM.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $165,251.36 | bars: $179,933 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ANET.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 227 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| AVGO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 226 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| GEV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 227 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| MTRX.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 209 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| XETM.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 209 bars, SPY 251 bars | equal | MISLEADING | LOW | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods (the Technical Read tile now says "since <date>"; the RS card still labels it 52W) |
| ABBV | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AMZN | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| COST | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| LIN | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| LLY | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| PG | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| WELL | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ASML.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 8 differ: 37.75-39.31 x5 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| BDT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 2 of 6 differ: 62.75-64.68 x4, 59.9-60.72 x2 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| DRIV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 9 differ: 31.32-32.04 x4 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| AAPL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $351.46 | $351.46 | PASS |  |  |
| AAPL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.13% | 0.13% | PASS |  |  |
| AAPL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| AAPL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| AAPL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $351.46 · close 0.13% above · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| AAPL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| AAPU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.38 | $49.38 | PASS |  |  |
| AAPU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.6% | -1.60% | PASS |  |  |
| AAPU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.35 | 0.35 | PASS |  |  |
| AAPU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| AAPU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.38 · close 1.60% below · broke out Nov 11 on 0.35× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
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
| AIPO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.68% | -27.69% | PASS |  |  |
| AIPO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AIPO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AIPO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AIPO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.38 · close 27.68% below · Nov 18 close | payload values | PASS |  |  |
| AIPO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ALAB | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $401.74 | $401.74 | PASS |  |  |
| ALAB | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -47.33% | -47.33% | PASS |  |  |
| ALAB | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ALAB | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ALAB | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ALAB | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $401.74 · close 47.33% below · Nov 17 close | payload values | PASS |  |  |
| ALAB | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $658.52 | $658.52 | PASS |  |  |
| AMD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.5% | -19.50% | PASS |  |  |
| AMD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $658.52 · close 19.50% below · Nov 18 close | payload values | PASS |  |  |
| AMD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $273.46 | $273.46 | PASS |  |  |
| AMZN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.09% | -2.09% | PASS |  |  |
| AMZN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| AMZN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $273.46 · close 2.09% below · Nov 18 close | payload values | PASS |  |  |
| AMZN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $41.78 | $41.78 | PASS |  |  |
| AMZU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.27% | -9.26% | PASS |  |  |
| AMZU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $41.78 · close 9.27% below · Nov 18 close | payload values | PASS |  |  |
| AMZU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ANET.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.85 | $38.85 | PASS |  |  |
| ANET.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.79% | -10.79% | PASS |  |  |
| ANET.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ANET.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ANET.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ANET.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.85 · close 10.79% below · Nov 18 close | payload values | PASS |  |  |
| ANET.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASML.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $53.94 | $53.94 | PASS |  |  |
| ASML.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.53% | -23.53% | PASS |  |  |
| ASML.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ASML.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ASML.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ASML.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $53.94 · close 23.53% below · Nov 18 close | payload values | PASS |  |  |
| ASML.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $7.71 | $7.71 | PASS |  |  |
| ASTL.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.99% | -9.99% | PASS |  |  |
| ASTL.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-09 | 2026-11-09 | PASS |  |  |
| ASTL.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.67 | 2.67 | PASS |  |  |
| ASTL.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| ASTL.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $7.71 · close 9.99% below · broke out Nov 9 on 2.67× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| ASTL.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ATD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $93.43 | $93.43 | PASS |  |  |
| ATD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.16% | -11.16% | PASS |  |  |
| ATD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ATD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ATD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ATD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $93.43 · close 11.16% below · Nov 18 close | payload values | PASS |  |  |
| ATD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGC | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $30.25 | $30.25 | PASS |  |  |
| AVGC | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -34.94% | -34.94% | PASS |  |  |
| AVGC | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGC | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGC | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGC | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $30.25 · close 34.94% below · Nov 18 close | payload values | PASS |  |  |
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
| BDT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -15.47% | -15.47% | PASS |  |  |
| BDT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BDT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BDT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BDT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $86.42 · close 15.47% below · Nov 18 close | payload values | PASS |  |  |
| BDT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BOTZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.15 | $38.15 | PASS |  |  |
| BOTZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.12% | -22.12% | PASS |  |  |
| BOTZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BOTZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BOTZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BOTZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.15 · close 22.12% below · Nov 18 close | payload values | PASS |  |  |
| BOTZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $580.65 | $580.65 | PASS |  |  |
| BRK-B | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.04% | -1.04% | PASS |  |  |
| BRK-B | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-10 | 2026-11-10 | PASS |  |  |
| BRK-B | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.99 | 0.99 | PASS |  |  |
| BRK-B | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| BRK-B | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $580.65 · close 1.04% below · broke out Nov 10 on 0.99× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| BRK-B | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| BRKU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $29.61 | $29.61 | PASS |  |  |
| BRKU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.57% | -2.57% | PASS |  |  |
| BRKU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-10 | 2026-11-10 | PASS |  |  |
| BRKU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.67 | 0.67 | PASS |  |  |
| BRKU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| BRKU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $29.61 · close 2.57% below · broke out Nov 10 on 0.67× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| BRKU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRKU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CAMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $178.02 | $178.02 | PASS |  |  |
| CAMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -44.71% | -44.71% | PASS |  |  |
| CAMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $178.02 · close 44.71% below · Nov 18 close | payload values | PASS |  |  |
| CAMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CARS.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $28.41 | $28.41 | PASS |  |  |
| CARS.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.04% | -30.02% | PASS |  |  |
| CARS.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CARS.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CARS.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CARS.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $28.41 · close 30.04% below · Nov 18 close | payload values | PASS |  |  |
| CARS.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CCO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $154.65 | $154.65 | PASS |  |  |
| CCO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.19% | -42.19% | PASS |  |  |
| CCO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CCO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CCO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CCO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $154.65 · close 42.19% below · Nov 18 close | payload values | PASS |  |  |
| CCO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CGY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.58% | -11.57% | PASS |  |  |
| CGY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CGY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CGY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CGY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $95.15 · close 11.58% below · Nov 18 close | payload values | PASS |  |  |
| CGY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $78.6 | $78.60 | PASS |  |  |
| CNQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -16.97% | -16.97% | PASS |  |  |
| CNQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CNQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CNQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CNQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $78.60 · close 16.97% below · Nov 18 close | payload values | PASS |  |  |
| CNQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $180.55 | $180.55 | PASS |  |  |
| CNR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.66% | -0.66% | PASS |  |  |
| CNR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| CNR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| CNR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| CNR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $180.55 · close 0.66% below · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| CNR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COP | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $154.28 | $154.28 | PASS |  |  |
| COP | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.89% | -12.89% | PASS |  |  |
| COP | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COP | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COP | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COP | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $154.28 · close 12.89% below · Nov 18 close | payload values | PASS |  |  |
| COP | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $69.02 | $69.02 | PASS |  |  |
| COPP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.58% | -37.58% | PASS |  |  |
| COPP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $69.02 · close 37.58% below · Nov 18 close | payload values | PASS |  |  |
| COPP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $97.59 | $97.59 | PASS |  |  |
| COPX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.3% | -37.30% | PASS |  |  |
| COPX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $97.59 · close 37.30% below · Nov 18 close | payload values | PASS |  |  |
| COPX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.84 | $20.84 | PASS |  |  |
| COPZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -63.86% | -63.87% | PASS |  |  |
| COPZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.84 · close 63.86% below · Nov 18 close | payload values | PASS |  |  |
| COPZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1053.66 | $1,053.66 | PASS |  |  |
| COST | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 4.08% | 4.08% | PASS |  |  |
| COST | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-05 | 2026-11-05 | PASS |  |  |
| COST | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.12 | 2.12 | PASS |  |  |
| COST | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| COST | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,053.66 · close 4.08% above · broke out Nov 5 on 2.12× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| COST | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COTG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $15.33 | $15.33 | PASS |  |  |
| COTG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 7.83% | 7.83% | PASS |  |  |
| COTG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-05 | 2026-11-05 | PASS |  |  |
| COTG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.42 | 1.42 | PASS |  |  |
| COTG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| COTG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $15.33 · close 7.83% above · broke out Nov 5 on 1.42× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| COTG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COTG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CSU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $3518.6 | $3,518.60 | PASS |  |  |
| CSU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.55% | -5.55% | PASS |  |  |
| CSU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-06 | 2026-11-06 | PASS |  |  |
| CSU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.95 | 0.95 | PASS |  |  |
| CSU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| CSU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $3,518.60 · close 5.55% below · broke out Nov 6 on 0.95× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| CSU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CSU.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CVX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $236.48 | $236.48 | PASS |  |  |
| CVX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.94% | -12.94% | PASS |  |  |
| CVX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CVX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CVX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CVX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $236.48 · close 12.94% below · Nov 18 close | payload values | PASS |  |  |
| CVX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $13 | $13.00 | PASS |  |  |
| DRAL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -68.08% | -68.08% | PASS |  |  |
| DRAL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $13.00 · close 68.08% below · Nov 18 close | payload values | PASS |  |  |
| DRAL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $63.82 | $63.82 | PASS |  |  |
| DRAM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -38.66% | -38.66% | PASS |  |  |
| DRAM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $63.82 · close 38.66% below · Nov 18 close | payload values | PASS |  |  |
| DRAM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRIV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.47 | $36.47 | PASS |  |  |
| DRIV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.47% | -26.46% | PASS |  |  |
| DRIV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRIV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRIV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRIV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.47 · close 26.47% below · Nov 18 close | payload values | PASS |  |  |
| DRIV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $129.12 | $129.12 | PASS |  |  |
| DUK | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.72% | 0.72% | PASS |  |  |
| DUK | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-13 | 2026-11-13 | PASS |  |  |
| DUK | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.82 | 1.82 | PASS |  |  |
| DUK | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| DUK | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $129.12 · close 0.72% above · broke out Nov 13 on 1.82× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| DUK | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ELIL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $42.23 | $42.23 | PASS |  |  |
| ELIL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.35% | -9.35% | PASS |  |  |
| ELIL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ELIL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ELIL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ELIL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $42.23 · close 9.35% below · Nov 18 close | payload values | PASS |  |  |
| ELIL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| EQIX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1098.02 | $1,098.02 | PASS |  |  |
| EQIX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.6% | -5.60% | PASS |  |  |
| EQIX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| EQIX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| EQIX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| EQIX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,098.02 · close 5.60% below · Nov 18 close | payload values | PASS |  |  |
| EQIX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ETN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $476.54 | $476.54 | PASS |  |  |
| ETN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29% | -29.00% | PASS |  |  |
| ETN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ETN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ETN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ETN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $476.54 · close 29.00% below · Nov 18 close | payload values | PASS |  |  |
| ETN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FCX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $80.07 | $80.07 | PASS |  |  |
| FCX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.74% | -35.74% | PASS |  |  |
| FCX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FCX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FCX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FCX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $80.07 · close 35.74% below · Nov 18 close | payload values | PASS |  |  |
| FCX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FINN.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.83 | $35.83 | PASS |  |  |
| FINN.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.77% | -10.77% | PASS |  |  |
| FINN.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FINN.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FINN.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FINN.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.83 · close 10.77% below · Nov 18 close | payload values | PASS |  |  |
| FINN.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $105.67 | $105.67 | PASS |  |  |
| GDX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.19% | -29.19% | PASS |  |  |
| GDX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $105.67 · close 29.19% below · Nov 18 close | payload values | PASS |  |  |
| GDX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDXU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.45 | $46.45 | PASS |  |  |
| GDXU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -53% | -53.00% | PASS |  |  |
| GDXU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDXU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDXU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDXU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.45 · close 53.00% below · Nov 18 close | payload values | PASS |  |  |
| GDXU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $375.01 | $375.01 | PASS |  |  |
| GE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.51% | -12.51% | PASS |  |  |
| GE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $375.01 · close 12.51% below · Nov 18 close | payload values | PASS |  |  |
| GE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1099.66 | $1,099.66 | PASS |  |  |
| GEV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.78% | -29.78% | PASS |  |  |
| GEV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,099.66 · close 29.78% below · Nov 18 close | payload values | PASS |  |  |
| GEV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $73.78 | $73.78 | PASS |  |  |
| GEV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.98% | -29.98% | PASS |  |  |
| GEV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $73.78 · close 29.98% below · Nov 18 close | payload values | PASS |  |  |
| GEV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GGLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $111.95 | $111.95 | PASS |  |  |
| GGLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.69% | -42.69% | PASS |  |  |
| GGLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GGLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GGLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GGLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $111.95 · close 42.69% below · Nov 18 close | payload values | PASS |  |  |
| GGLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $117.04 | $117.04 | PASS |  |  |
| GIB-A.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.56% | -1.56% | PASS |  |  |
| GIB-A.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-06 | 2026-11-06 | PASS |  |  |
| GIB-A.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.52 | 1.52 | PASS |  |  |
| GIB-A.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| GIB-A.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $117.04 · close 1.56% below · broke out Nov 6 on 1.52× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| GIB-A.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| GOOGL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.17 | $364.17 | PASS |  |  |
| GOOGL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.44% | -22.44% | PASS |  |  |
| GOOGL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GOOGL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GOOGL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GOOGL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.17 · close 22.44% below · Nov 18 close | payload values | PASS |  |  |
| GOOGL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $355.74 | $355.74 | PASS |  |  |
| HD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.7% | -4.70% | PASS |  |  |
| HD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $355.74 · close 4.70% below · Nov 17 close | payload values | PASS |  |  |
| HD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HURA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $56.75 | $56.75 | PASS |  |  |
| HURA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.4% | -35.40% | PASS |  |  |
| HURA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HURA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HURA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HURA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $56.75 · close 35.40% below · Nov 18 close | payload values | PASS |  |  |
| HURA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HXQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.9% | -12.90% | PASS |  |  |
| HXQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HXQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HXQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HXQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $128.37 · close 12.90% below · Nov 18 close | payload values | PASS |  |  |
| HXQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $282.02 | $282.02 | PASS |  |  |
| JNJ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.3% | -3.30% | PASS |  |  |
| JNJ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-09 | 2026-11-09 | PASS |  |  |
| JNJ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.96 | 0.96 | PASS |  |  |
| JNJ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| JNJ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $282.02 · close 3.30% below · broke out Nov 9 on 0.96× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| JNJ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| JPM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.68 | $364.68 | PASS |  |  |
| JPM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.12% | -11.12% | PASS |  |  |
| JPM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| JPM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| JPM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| JPM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.68 · close 11.12% below · Nov 18 close | payload values | PASS |  |  |
| JPM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| KEYS | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $389.93 | $389.93 | PASS |  |  |
| KEYS | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.05% | -27.05% | PASS |  |  |
| KEYS | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| KEYS | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| KEYS | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| KEYS | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $389.93 · close 27.05% below · Nov 17 close | payload values | PASS |  |  |
| KEYS | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LIN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $526.56 | $526.56 | PASS |  |  |
| LIN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.73% | -2.73% | PASS |  |  |
| LIN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| LIN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| LIN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| LIN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $526.56 · close 2.73% below · Nov 18 close | payload values | PASS |  |  |
| LIN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LLY | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1447.92 | $1,447.92 | PASS |  |  |
| LLY | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.24% | -2.24% | PASS |  |  |
| LLY | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| LLY | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| LLY | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| LLY | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,447.92 · close 2.24% below · Nov 17 close | payload values | PASS |  |  |
| LLY | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MDA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $51.34 | $51.34 | PASS |  |  |
| MDA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.13% | -22.13% | PASS |  |  |
| MDA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MDA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MDA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MDA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $51.34 · close 22.13% below · Nov 18 close | payload values | PASS |  |  |
| MDA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| META | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $779.82 | $779.82 | PASS |  |  |
| META | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.64% | -20.64% | PASS |  |  |
| META | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| META | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| META | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| META | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $779.82 · close 20.64% below · Nov 17 close | payload values | PASS |  |  |
| META | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| METU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.6 | $35.60 | PASS |  |  |
| METU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -40% | -40.00% | PASS |  |  |
| METU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| METU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| METU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| METU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.60 · close 40.00% below · Nov 18 close | payload values | PASS |  |  |
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
| MSFU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $45.88 | $45.88 | PASS |  |  |
| MSFU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.03% | -18.03% | PASS |  |  |
| MSFU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MSFU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MSFU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MSFU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $45.88 · close 18.03% below · Nov 18 close | payload values | PASS |  |  |
| MSFU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MTRX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $37.54 | $37.54 | PASS |  |  |
| MTRX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.26% | -23.26% | PASS |  |  |
| MTRX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MTRX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MTRX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MTRX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $37.54 · close 23.26% below · Nov 18 close | payload values | PASS |  |  |
| MTRX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $48.54 | $48.54 | PASS |  |  |
| MU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.63% | -36.63% | PASS |  |  |
| MU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $48.54 · close 36.63% below · Nov 18 close | payload values | PASS |  |  |
| MU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $88.79 | $88.79 | PASS |  |  |
| NEE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.52% | -4.52% | PASS |  |  |
| NEE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NEE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NEE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NEE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $88.79 · close 4.52% below · Nov 18 close | payload values | PASS |  |  |
| NEE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $135.01 | $135.01 | PASS |  |  |
| NEM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.58% | -22.58% | PASS |  |  |
| NEM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NEM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NEM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NEM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $135.01 · close 22.58% below · Nov 18 close | payload values | PASS |  |  |
| NEM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFLX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $83.6 | $83.60 | PASS |  |  |
| NFLX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.45% | -28.45% | PASS |  |  |
| NFLX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFLX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFLX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFLX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $83.60 · close 28.45% below · Nov 18 close | payload values | PASS |  |  |
| NFLX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.33 | $20.33 | PASS |  |  |
| NFXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -51.41% | -51.40% | PASS |  |  |
| NFXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.33 · close 51.41% below · Nov 18 close | payload values | PASS |  |  |
| NFXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NTR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $112.9 | $112.90 | PASS |  |  |
| NTR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -16.28% | -16.28% | PASS |  |  |
| NTR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NTR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NTR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NTR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $112.90 · close 16.28% below · Nov 18 close | payload values | PASS |  |  |
| NTR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.37 | $243.37 | PASS |  |  |
| NVDA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.12% | -36.12% | PASS |  |  |
| NVDA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.37 · close 36.12% below · Nov 17 close | payload values | PASS |  |  |
| NVDA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $41.59 | $41.59 | PASS |  |  |
| NVDL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -63.36% | -63.36% | PASS |  |  |
| NVDL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $41.59 · close 63.36% below · Nov 18 close | payload values | PASS |  |  |
| NVDL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ONTO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $353.84 | $353.84 | PASS |  |  |
| ONTO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -43.19% | -43.19% | PASS |  |  |
| ONTO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ONTO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ONTO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ONTO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $353.84 · close 43.19% below · Nov 18 close | payload values | PASS |  |  |
| ONTO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORBX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $19.64 | $19.64 | PASS |  |  |
| ORBX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.73% | -26.73% | PASS |  |  |
| ORBX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORBX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORBX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORBX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $19.64 · close 26.73% below · Nov 18 close | payload values | PASS |  |  |
| ORBX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $170.07 | $170.07 | PASS |  |  |
| ORCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -33.03% | -33.03% | PASS |  |  |
| ORCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $170.07 · close 33.03% below · Nov 18 close | payload values | PASS |  |  |
| ORCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $165.75 | $165.75 | PASS |  |  |
| PG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 3.6% | 3.60% | PASS |  |  |
| PG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| PG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.55 | 1.55 | PASS |  |  |
| PG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| PG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $165.75 · close 3.60% above · broke out Nov 4 on 1.55× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| PG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| PNG.V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $6.8 | $6.80 | PASS |  |  |
| PNG.V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -56.03% | -56.03% | PASS |  |  |
| PNG.V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PNG.V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PNG.V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PNG.V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $6.80 · close 56.03% below · Nov 18 close | payload values | PASS |  |  |
| PNG.V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QCOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $205.85 | $205.85 | PASS |  |  |
| QCOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.37% | -22.37% | PASS |  |  |
| QCOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QCOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QCOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QCOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $205.85 · close 22.37% below · Nov 18 close | payload values | PASS |  |  |
| QCOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QPUX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $22.2 | $22.20 | PASS |  |  |
| QPUX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -85.63% | -85.63% | PASS |  |  |
| QPUX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QPUX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QPUX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QPUX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $22.20 · close 85.63% below · Nov 18 close | payload values | PASS |  |  |
| QPUX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QTUM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $159.25 | $159.25 | PASS |  |  |
| QTUM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.79% | -22.79% | PASS |  |  |
| QTUM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QTUM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QTUM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QTUM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $159.25 · close 22.79% below · Nov 18 close | payload values | PASS |  |  |
| QTUM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RBOT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $34.84 | $34.84 | PASS |  |  |
| RBOT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.24% | -22.24% | PASS |  |  |
| RBOT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RBOT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RBOT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RBOT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $34.84 · close 22.24% below · Nov 18 close | payload values | PASS |  |  |
| RBOT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RTX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $226.41 | $226.41 | PASS |  |  |
| RTX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.79% | -12.79% | PASS |  |  |
| RTX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RTX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RTX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RTX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $226.41 · close 12.79% below · Nov 18 close | payload values | PASS |  |  |
| RTX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.46 | $300.46 | PASS |  |  |
| RY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.39% | -9.39% | PASS |  |  |
| RY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.46 · close 9.39% below · Nov 18 close | payload values | PASS |  |  |
| RY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SGRD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $21.32 | $21.32 | PASS |  |  |
| SGRD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -15.74% | -15.76% | PASS |  |  |
| SGRD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SGRD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SGRD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SGRD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $21.32 · close 15.74% below · Nov 18 close | payload values | PASS |  |  |
| SGRD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SMH | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $639.47 | $639.47 | PASS |  |  |
| SMH | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.14% | -28.14% | PASS |  |  |
| SMH | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SMH | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SMH | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SMH | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $639.47 · close 28.14% below · Nov 18 close | payload values | PASS |  |  |
| SMH | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SNDK.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.35 | $46.35 | PASS |  |  |
| SNDK.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -59.57% | -59.57% | PASS |  |  |
| SNDK.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SNDK.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SNDK.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SNDK.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.35 · close 59.57% below · Nov 18 close | payload values | PASS |  |  |
| SNDK.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $94.08 | $94.08 | PASS |  |  |
| SO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.35% | 0.35% | PASS |  |  |
| SO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.86 | 1.86 | PASS |  |  |
| SO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| SO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $94.08 · close 0.35% above · broke out Nov 16 on 1.86× its prior 50-day average volume · Nov 18 close | payload values | PASS |  |  |
| SO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| SOXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $169.83 | $169.83 | PASS |  |  |
| SOXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -70.99% | -70.99% | PASS |  |  |
| SOXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $169.83 · close 70.99% below · Nov 18 close | payload values | PASS |  |  |
| SOXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $40.79 | $40.79 | PASS |  |  |
| SOXL.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -69.52% | -69.53% | PASS |  |  |
| SOXL.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $40.79 · close 69.52% below · Nov 18 close | payload values | PASS |  |  |
| SOXL.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $198.81 | $198.81 | PASS |  |  |
| SOXX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.65% | -28.65% | PASS |  |  |
| SOXX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $198.81 · close 28.65% below · Nov 18 close | payload values | PASS |  |  |
| SOXX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SPCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.54 | $33.54 | PASS |  |  |
| SPCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -71.85% | -71.85% | PASS |  |  |
| SPCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SPCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SPCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SPCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.54 · close 71.85% below · Nov 18 close | payload values | PASS |  |  |
| SPCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $414.23 | $414.23 | PASS |  |  |
| TSLA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.37% | -7.37% | PASS |  |  |
| TSLA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $414.23 · close 7.37% below · Nov 18 close | payload values | PASS |  |  |
| TSLA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $11.98 | $11.98 | PASS |  |  |
| TSLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -16.53% | -16.53% | PASS |  |  |
| TSLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $11.98 · close 16.53% below · Nov 18 close | payload values | PASS |  |  |
| TSLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $487.47 | $487.47 | PASS |  |  |
| TSM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.61% | -25.61% | PASS |  |  |
| TSM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $487.47 · close 25.61% below · Nov 18 close | payload values | PASS |  |  |
| TSM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UBOT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $25.62 | $25.62 | PASS |  |  |
| UBOT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -41.19% | -41.18% | PASS |  |  |
| UBOT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UBOT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UBOT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UBOT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $25.62 · close 41.19% below · Nov 18 close | payload values | PASS |  |  |
| UBOT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UFO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.29 | $49.29 | PASS |  |  |
| UFO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.69% | -20.69% | PASS |  |  |
| UFO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UFO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UFO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UFO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.29 · close 20.69% below · Nov 18 close | payload values | PASS |  |  |
| UFO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $425.99 | $425.99 | PASS |  |  |
| V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.16% | -2.16% | PASS |  |  |
| V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.57 | 1.57 | PASS |  |  |
| V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $425.99 · close 2.16% below · broke out Nov 4 on 1.57× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| V | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| VFV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.88% | -5.88% | PASS |  |  |
| VFV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VFV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VFV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VFV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $197.83 · close 5.88% below · Nov 18 close | payload values | PASS |  |  |
| VFV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| VRT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.23 | $300.23 | PASS |  |  |
| VRT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.59% | -36.59% | PASS |  |  |
| VRT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VRT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VRT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VRT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.23 · close 36.59% below · Nov 17 close | payload values | PASS |  |  |
| VRT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WDC.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.32 | $33.32 | PASS |  |  |
| WDC.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -47.66% | -47.66% | PASS |  |  |
| WDC.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WDC.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WDC.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| WDC.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.32 · close 47.66% below · Nov 18 close | payload values | PASS |  |  |
| WDC.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WELL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $247.7 | $247.70 | PASS |  |  |
| WELL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.18% | -0.18% | PASS |  |  |
| WELL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WELL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WELL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| WELL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $247.70 · close 0.18% below · Nov 18 close | payload values | PASS |  |  |
| WELL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $127.94 | $127.94 | PASS |  |  |
| WMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.33% | -0.33% | PASS |  |  |
| WMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| WMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.32 | 1.32 | PASS |  |  |
| WMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| WMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $127.94 · close 0.33% below · broke out Nov 4 on 1.32× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| WMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WMT | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| XCHP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $147.5 | $147.50 | PASS |  |  |
| XCHP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.24% | -28.24% | PASS |  |  |
| XCHP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XCHP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XCHP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XCHP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $147.50 · close 28.24% below · Nov 18 close | payload values | PASS |  |  |
| XCHP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XDRV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.26 | $49.26 | PASS |  |  |
| XDRV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -21.15% | -21.15% | PASS |  |  |
| XDRV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XDRV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XDRV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XDRV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.26 · close 21.15% below · Nov 18 close | payload values | PASS |  |  |
| XDRV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XEQT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.11% | -5.11% | PASS |  |  |
| XEQT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XEQT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XEQT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XEQT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.38 · close 5.11% below · Nov 18 close | payload values | PASS |  |  |
| XEQT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XETM.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $91.8 | $91.80 | PASS |  |  |
| XETM.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.09% | -37.08% | PASS |  |  |
| XETM.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XETM.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XETM.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XETM.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $91.80 · close 37.09% below · Nov 18 close | payload values | PASS |  |  |
| XETM.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XGD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $65.29 | $65.29 | PASS |  |  |
| XGD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.81% | -25.81% | PASS |  |  |
| XGD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XGD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XGD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XGD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $65.29 · close 25.81% below · Nov 18 close | payload values | PASS |  |  |
| XGD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $188.5 | $188.50 | PASS |  |  |
| XOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14.81% | -14.81% | PASS |  |  |
| XOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $188.50 · close 14.81% below · Nov 18 close | payload values | PASS |  |  |
| XOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $48.59 · Nov 18 | $48.59 · Nov 18 | PASS |  |  |
| ABBV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.36 / Mom: +1.06 / Rank: 2/11] XLV LEADING | RS 105.36 Mom 1.06 Rank 2/11 | PASS |  |  |
| ABBV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| ABBV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AIPO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AIPO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $22.69 · Nov 18 | $22.69 · Nov 18 | PASS |  |  |
| ALAB | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| ALAB | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ALAB | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| AMD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $530.14 · Nov 18 | $530.14 · Nov 18 | PASS |  |  |
| AMZN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.57 / Mom: +2.39 / Rank: 7/11] X | RS 98.57 Mom 2.39 Rank 7/11 | PASS |  |  |
| AMZN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| AMZN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $267.74 · Nov 18 | $267.74 · Nov 18 | PASS |  |  |
| AMZU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $37.91 · Nov 18 | $37.91 · Nov 18 | PASS |  |  |
| ANET.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASML.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.64 / Mom: +0.67 / Rank: 6/11] XLB IMPROVING | RS 98.64 Mom 0.67 Rank 6/11 | PASS |  |  |
| ASTL.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ASTL.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $6.94 · Nov 18 | $6.94 · Nov 18 | PASS |  |  |
| ATD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.57 / Mom: +2.39 / Rank: 7/11] X | RS 98.57 Mom 2.39 Rank 7/11 | PASS |  |  |
| ATD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ATD.TO | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 6 days | 📅 Earnings in 6 days | PASS |  |  |
| ATD.TO | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 6 days | 2026-11-24, 6 days | PASS |  |  |
| ATD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $83.00 · Nov 18 | $83.00 · Nov 18 | PASS |  |  |
| AVGC | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| AVGO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AVGO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BDT.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| BDT.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| BDT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BDT.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $73.05 · Nov 18 | $73.05 · Nov 18 | PASS |  |  |
| BOTZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BOTZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $29.71 · Nov 18 | $29.71 · Nov 18 | PASS |  |  |
| BRK-B | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 99.95 / Mom: -0.51 / Rank: 4/11] XLF LAGGING | RS 99.95 Mom -0.51 Rank 4/11 | PASS |  |  |
| BRK-B | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| BRK-B | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRK-B | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $574.62 · Nov 18 | $574.62 · Nov 18 | PASS |  |  |
| BRKU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRKU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $28.85 · Nov 18 | $28.85 · Nov 18 | PASS |  |  |
| CAMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| CAMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAMT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $98.42 · Nov 18 | $98.42 · Nov 18 | PASS |  |  |
| CARS.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CCO.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.25 / Mom: +0.2 / Rank: 1/11] XLE LEADING | RS 106.25 Mom 0.2 Rank 1/11 | PASS |  |  |
| CCO.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CCO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CCO.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $89.40 · Nov 18 | $89.40 · Nov 18 | PASS |  |  |
| CGY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| CGY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CGY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CGY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $84.14 · Nov 18 | $84.14 · Nov 18 | PASS |  |  |
| CNQ.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.25 / Mom: +0.2 / Rank: 1/11] XLE LEADING | RS 106.25 Mom 0.2 Rank 1/11 | PASS |  |  |
| CNQ.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CNQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| CNR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CNR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $179.36 · Nov 18 | $179.36 · Nov 18 | PASS |  |  |
| COP | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.25 / Mom: +0.2 / Rank: 1/11] XLE LEADING | RS 106.25 Mom 0.2 Rank 1/11 | PASS |  |  |
| COP | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COP | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COP | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $134.40 · Nov 18 | $134.40 · Nov 18 | PASS |  |  |
| COPP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $61.19 · Nov 18 | $61.19 · Nov 18 | PASS |  |  |
| COPZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COST | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.52 / Mom: +3.17 / Rank: 3/11] XLP LE | RS 101.52 Mom 3.17 Rank 3/11 | PASS |  |  |
| COST | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COST | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COST | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,096.62 · Nov 18 | $1,096.62 · Nov 18 | PASS |  |  |
| COTG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COTG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $16.53 · Nov 18 | $16.53 · Nov 18 | PASS |  |  |
| CSU.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| CSU.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CSU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CSU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3,323.15 · Nov 18 | $3,323.15 · Nov 18 | PASS |  |  |
| CVX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.25 / Mom: +0.2 / Rank: 1/11] XLE LEADING | RS 106.25 Mom 0.2 Rank 1/11 | PASS |  |  |
| CVX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CVX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CVX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $205.88 · Nov 18 | $205.88 · Nov 18 | PASS |  |  |
| DRAL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $4.15 · Nov 18 | $4.15 · Nov 18 | PASS |  |  |
| DRAM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $39.15 · Nov 18 | $39.15 · Nov 18 | PASS |  |  |
| DRIV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRIV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $26.82 · Nov 18 | $26.82 · Nov 18 | PASS |  |  |
| DUK | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.72 / Mom: +2.92 / Rank: 10/11] XLU IMPROVING | RS 96.72 Mom 2.92 Rank 10/11 | PASS |  |  |
| DUK | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| DUK | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DUK | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $130.05 · Nov 18 | $130.05 · Nov 18 | PASS |  |  |
| ELIL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ELIL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $38.28 · Nov 18 | $38.28 · Nov 18 | PASS |  |  |
| EQIX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.14 / Mom: +1.24 / Rank: 9/11] XLRE IMPROV | RS 97.14 Mom 1.24 Rank 9/11 | PASS |  |  |
| EQIX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| EQIX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| EQIX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,036.50 · Nov 18 | $1,036.50 · Nov 18 | PASS |  |  |
| ETN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| ETN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ETN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ETN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $338.34 · Nov 18 | $338.34 · Nov 18 | PASS |  |  |
| FCX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.64 / Mom: +0.67 / Rank: 6/11] XLB IMPROVING | RS 98.64 Mom 0.67 Rank 6/11 | PASS |  |  |
| FCX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| FCX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| FCX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $51.45 · Nov 18 | $51.45 · Nov 18 | PASS |  |  |
| FINN.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $74.82 · Nov 18 | $74.82 · Nov 18 | PASS |  |  |
| GDXU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| GE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $328.10 · Nov 18 | $328.10 · Nov 18 | PASS |  |  |
| GEV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| GEV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GEV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GEV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $772.22 · Nov 18 | $772.22 · Nov 18 | PASS |  |  |
| GEV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $64.16 · Nov 18 | $64.16 · Nov 18 | PASS |  |  |
| GIB-A.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| GIB-A.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GIB-A.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GIB-A.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $115.21 · Nov 18 | $115.21 · Nov 18 | PASS |  |  |
| GOOGL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.02 / Mom: +0.31 / Rank: 8/11] X | RS 98.02 Mom 0.31 Rank 8/11 | PASS |  |  |
| GOOGL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| GOOGL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GOOGL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $282.44 · Nov 18 | $282.44 · Nov 18 | PASS |  |  |
| HD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.57 / Mom: +2.39 / Rank: 7/11] X | RS 98.57 Mom 2.39 Rank 7/11 | PASS |  |  |
| HD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| HD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HURA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HXQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.36 / Mom: +1.06 / Rank: 2/11] XLV LEADING | RS 105.36 Mom 1.06 Rank 2/11 | PASS |  |  |
| JNJ | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| JNJ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $272.70 · Nov 18 | $272.70 · Nov 18 | PASS |  |  |
| JPM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 99.95 / Mom: -0.51 / Rank: 4/11] XLF LAGGING | RS 99.95 Mom -0.51 Rank 4/11 | PASS |  |  |
| JPM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| JPM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JPM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $324.11 · Nov 18 | $324.11 · Nov 18 | PASS |  |  |
| KEYS | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| KEYS | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| KEYS | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ Earnings in 1 day | ⚠️ Earnings in 1 day | PASS |  |  |
| KEYS | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-19, 1 days | 2026-11-19, 1 days | PASS |  |  |
| LIN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.64 / Mom: +0.67 / Rank: 6/11] XLB IMPROVING | RS 98.64 Mom 0.67 Rank 6/11 | PASS |  |  |
| LIN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| LIN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LIN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $512.16 · Nov 18 | $512.16 · Nov 18 | PASS |  |  |
| LLY | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.36 / Mom: +1.06 / Rank: 2/11] XLV LEADING | RS 105.36 Mom 1.06 Rank 2/11 | PASS |  |  |
| LLY | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| LLY | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MDA.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| MDA.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MDA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MDA.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $39.98 · Nov 18 | $39.98 · Nov 18 | PASS |  |  |
| META | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.02 / Mom: +0.31 / Rank: 8/11] X | RS 98.02 Mom 0.31 Rank 8/11 | PASS |  |  |
| META | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| META | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| METU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| METU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $21.36 · Nov 18 | $21.36 · Nov 18 | PASS |  |  |
| MRVL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| MRVL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MRVL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| MSFT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MSFT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $37.61 · Nov 18 | $37.61 · Nov 18 | PASS |  |  |
| MTRX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.72 / Mom: +2.92 / Rank: 10/11] XLU IMPROVING | RS 96.72 Mom 2.92 Rank 10/11 | PASS |  |  |
| NEE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $84.78 · Nov 18 | $84.78 · Nov 18 | PASS |  |  |
| NEM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.64 / Mom: +0.67 / Rank: 6/11] XLB IMPROVING | RS 98.64 Mom 0.67 Rank 6/11 | PASS |  |  |
| NEM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $104.53 · Nov 18 | $104.53 · Nov 18 | PASS |  |  |
| NFLX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.02 / Mom: +0.31 / Rank: 8/11] X | RS 98.02 Mom 0.31 Rank 8/11 | PASS |  |  |
| NFLX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NFLX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFLX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $59.82 · Nov 18 | $59.82 · Nov 18 | PASS |  |  |
| NFXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $9.88 · Nov 18 | $9.88 · Nov 18 | PASS |  |  |
| NTR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.64 / Mom: +0.67 / Rank: 6/11] XLB IMPROVING | RS 98.64 Mom 0.67 Rank 6/11 | PASS |  |  |
| NTR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NTR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NTR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $94.52 · Nov 18 | $94.52 · Nov 18 | PASS |  |  |
| NVDA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| NVDA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| NVDA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $15.24 · Nov 18 | $15.24 · Nov 18 | PASS |  |  |
| ONTO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| ONTO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ONTO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ONTO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $201.02 · Nov 18 | $201.02 · Nov 18 | PASS |  |  |
| ORBX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| ORCL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ORCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $113.89 · Nov 18 | $113.89 · Nov 18 | PASS |  |  |
| PG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.52 / Mom: +3.17 / Rank: 3/11] XLP LE | RS 101.52 Mom 3.17 Rank 3/11 | PASS |  |  |
| PG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| PG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PNG.V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| PNG.V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| PNG.V | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 6 days | 📅 Earnings in 6 days | PASS |  |  |
| PNG.V | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 6 days | 2026-11-24, 6 days | PASS |  |  |
| QCOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| QCOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| QCOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QCOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $159.81 · Nov 18 | $159.81 · Nov 18 | PASS |  |  |
| QPUX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QPUX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3.19 · Nov 18 | $3.19 · Nov 18 | PASS |  |  |
| QTUM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QTUM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $122.95 · Nov 18 | $122.95 · Nov 18 | PASS |  |  |
| RBOT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| RTX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| RTX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $197.45 · Nov 18 | $197.45 · Nov 18 | PASS |  |  |
| RY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 99.95 / Mom: -0.51 / Rank: 4/11] XLF LAGGING | RS 99.95 Mom -0.51 Rank 4/11 | PASS |  |  |
| RY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| RY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $272.26 · Nov 18 | $272.26 · Nov 18 | PASS |  |  |
| SGRD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $459.54 · Nov 18 | $459.54 · Nov 18 | PASS |  |  |
| SNDK.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.72 / Mom: +2.92 / Rank: 10/11] XLU IMPROVING | RS 96.72 Mom 2.92 Rank 10/11 | PASS |  |  |
| SO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| SO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $94.41 · Nov 18 | $94.41 · Nov 18 | PASS |  |  |
| SOXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $49.26 · Nov 18 | $49.26 · Nov 18 | PASS |  |  |
| SOXL.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $141.85 · Nov 18 | $141.85 · Nov 18 | PASS |  |  |
| SPCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SPCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $9.44 · Nov 18 | $9.44 · Nov 18 | PASS |  |  |
| TSLA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.57 / Mom: +2.39 / Rank: 7/11] X | RS 98.57 Mom 2.39 Rank 7/11 | PASS |  |  |
| TSLA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| TSLA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $383.72 · Nov 18 | $383.72 · Nov 18 | PASS |  |  |
| TSLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $10.00 · Nov 18 | $10.00 · Nov 18 | PASS |  |  |
| TSM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.15 / Mom: -1.87 / Rank: 5/11] XLK LAGGING | RS 99.15 Mom -1.87 Rank 5/11 | PASS |  |  |
| TSM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| TSM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $362.62 · Nov 18 | $362.62 · Nov 18 | PASS |  |  |
| UBOT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UFO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UFO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $39.09 · Nov 18 | $39.09 · Nov 18 | PASS |  |  |
| V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 99.95 / Mom: -0.51 / Rank: 4/11] XLF LAGGING | RS 99.95 Mom -0.51 Rank 4/11 | PASS |  |  |
| V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| V | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VFV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VRT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.48 / Mom: -0.45 / Rank: 11/11] XLI LAGGING | RS 95.48 Mom -0.45 Rank 11/11 | PASS |  |  |
| VRT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| VRT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WDC.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WELL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.14 / Mom: +1.24 / Rank: 9/11] XLRE IMPROV | RS 97.14 Mom 1.24 Rank 9/11 | PASS |  |  |
| WELL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| WELL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WELL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $247.25 · Nov 18 | $247.25 · Nov 18 | PASS |  |  |
| WMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.52 / Mom: +3.17 / Rank: 3/11] XLP LE | RS 101.52 Mom 3.17 Rank 3/11 | PASS |  |  |
| WMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| WMT | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ Earnings in 1 day | ⚠️ Earnings in 1 day | PASS |  |  |
| WMT | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-19, 1 days | 2026-11-19, 1 days | PASS |  |  |
| XCHP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XDRV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XEQT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XETM.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XGD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.25 / Mom: +0.2 / Rank: 1/11] XLE LEADING | RS 106.25 Mom 0.2 Rank 1/11 | PASS |  |  |
| XOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| XOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $160.58 · Nov 18 | $160.58 · Nov 18 | PASS |  |  |
| AAPL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $351.91 | $351.91 | PASS |  |  |
| AAPL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $360.83 / $242.57 | $360.83 / $242.57 | PASS |  |  |
| AAPL | PD3 | % from High | -2.5% | -2.5% | PASS |  |  |
| AAPL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15.0B | bars: $15,402,045,674 | PASS | LOW |  |
| AAPU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $51.04 | $51.04 | PASS |  |  |
| AAPU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $48.59 | $48.59 | PASS |  |  |
| AAPU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $51.04 / $25.94 | $51.04 / $25.94 | PASS |  |  |
| AAPU | PD3 | % from High | -4.8% | -4.8% | PASS |  |  |
| AAPU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $51M | bars: $42,205,371 | PASS | LOW |  |
| ABBV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $292.82 | $292.82 | PASS |  |  |
| ABBV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.93 / $188.25 | $302.93 / $188.25 | PASS |  |  |
| ABBV | PD3 | % from High | -3.3% | -3.3% | PASS |  |  |
| ABBV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.4B | bars: $1,444,493,358 | PASS | LOW |  |
| AIPO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $34.79 | $34.79 | PASS |  |  |
| AIPO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $22.69 | $22.69 | PASS |  |  |
| AIPO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $34.79 / $20.65 | $34.79 / $20.65 | PASS |  |  |
| AIPO | PD3 | % from High | -34.8% | -34.8% | PASS |  |  |
| AIPO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $35M | bars: $36,690,932 | PASS | LOW |  |
| ALAB | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $211.60 | $211.60 | PASS |  |  |
| ALAB | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $499.48 / $97.89 | $499.48 / $97.89 | PASS |  |  |
| ALAB | PD3 | % from High | -57.6% | -57.6% | PASS |  |  |
| ALAB | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $902M | bars: $958,170,506 | PASS | LOW |  |
| AMD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $658.52 | $658.52 | PASS |  |  |
| AMD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $530.14 | $530.14 | PASS |  |  |
| AMD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $658.52 / $188.22 | $658.52 / $188.22 | PASS |  |  |
| AMD | PD3 | % from High | -19.5% | -19.5% | PASS |  |  |
| AMD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $13.3B | bars: $14,691,088,643 | PASS | LOW |  |
| AMZN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $287.20 | $287.20 | PASS |  |  |
| AMZN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $267.74 | $267.74 | PASS |  |  |
| AMZN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $287.20 / $196.00 | $287.20 / $196.00 | PASS |  |  |
| AMZN | PD3 | % from High | -6.8% | -6.8% | PASS |  |  |
| AMZN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $10.6B | bars: $11,156,708,536 | PASS | LOW |  |
| AMZU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.64 | $46.64 | PASS |  |  |
| AMZU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $37.91 | $37.91 | PASS |  |  |
| AMZU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.64 / $24.13 | $46.64 / $24.13 | PASS |  |  |
| AMZU | PD3 | % from High | -18.7% | -18.7% | PASS |  |  |
| AMZU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $71M | bars: $72,371,858 | PASS | LOW |  |
| ANET.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $34.66 | $34.66 | PASS |  |  |
| ANET.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.85 / $20.97 | $38.85 / $20.97 | PASS |  |  |
| ANET.TO | PD3 | % from High | -10.8% | -10.8% | PASS |  |  |
| ASML.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $56.75 | $56.75 | PASS |  |  |
| ASML.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $41.25 | $41.25 | PASS |  |  |
| ASML.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $56.75 / $26.65 | $56.75 / $26.65 | PASS |  |  |
| ASML.TO | PD3 | % from High | -27.3% | -27.3% | PASS |  |  |
| ASML.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,861,668 | PASS | LOW |  |
| ASTL.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $8.31 | $8.31 | PASS |  |  |
| ASTL.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $6.94 | $6.94 | PASS |  |  |
| ASTL.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $8.31 / $4.46 | $8.31 / $4.46 | PASS |  |  |
| ASTL.TO | PD3 | % from High | -16.5% | -16.5% | PASS |  |  |
| ASTL.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $4,156,385 | PASS | LOW |  |
| ATD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $94.68 | $94.68 | PASS |  |  |
| ATD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $83.00 | $83.00 | PASS |  |  |
| ATD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $94.68 / $67.83 | $94.68 / $67.83 | PASS |  |  |
| ATD.TO | PD3 | % from High | -12.3% | -12.3% | PASS |  |  |
| ATD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $115M | bars: $109,388,353 | PASS | LOW |  |
| AVGC | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $19.68 | $19.68 | PASS |  |  |
| AVGC | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.79 / $13.71 | $31.79 / $13.71 | PASS |  |  |
| AVGC | PD3 | % from High | -38.1% | -38.1% | PASS |  |  |
| AVGO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $341.60 | $341.60 | PASS |  |  |
| AVGO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $493.32 / $288.98 | $493.32 / $288.98 | PASS |  |  |
| AVGO | PD3 | % from High | -30.8% | -30.8% | PASS |  |  |
| AVGO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.7B | bars: $8,588,212,058 | PASS | LOW |  |
| AVGO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.94 | $12.94 | PASS |  |  |
| AVGO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $18.88 / $11.00 | $18.88 / $11.00 | PASS |  |  |
| AVGO.TO | PD3 | % from High | -31.4% | -31.5% | PASS |  |  |
| AVGO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15M | bars: $14,841,005 | PASS | LOW |  |
| BDT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $73.05 | $73.05 | PASS |  |  |
| BDT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $86.42 / $23.93 | $86.42 / $23.93 | PASS |  |  |
| BDT.TO | PD3 | % from High | -15.5% | -15.5% | PASS |  |  |
| BDT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $29M | bars: $30,228,521 | PASS | LOW |  |
| BOTZ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $41.69 | $41.69 | PASS |  |  |
| BOTZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $29.71 | $29.71 | PASS |  |  |
| BOTZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $41.69 / $29.36 | $41.69 / $29.36 | PASS |  |  |
| BOTZ | PD3 | % from High | -28.7% | -28.7% | PASS |  |  |
| BOTZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $21M | bars: $21,531,431 | PASS | LOW |  |
| BRK-B | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $596.92 | $596.92 | PASS |  |  |
| BRK-B | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $574.62 | $574.62 | PASS |  |  |
| BRK-B | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $596.92 / $464.01 | $596.92 / $464.01 | PASS |  |  |
| BRK-B | PD3 | % from High | -3.7% | -3.7% | PASS |  |  |
| BRK-B | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.7B | bars: $2,786,857,364 | PASS | LOW |  |
| BRKU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $31.20 | $31.20 | PASS |  |  |
| BRKU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $28.85 | $28.85 | PASS |  |  |
| BRKU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.20 / $20.05 | $31.20 / $20.05 | PASS |  |  |
| BRKU | PD3 | % from High | -7.5% | -7.5% | PASS |  |  |
| BRKU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,677,222 | PASS | LOW |  |
| CAMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $215.99 | $215.99 | PASS |  |  |
| CAMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $98.42 | $98.42 | PASS |  |  |
| CAMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $215.99 / $89.13 | $215.99 / $89.13 | PASS |  |  |
| CAMT | PD3 | % from High | -54.4% | -54.4% | PASS |  |  |
| CAMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $47M | bars: $50,850,205 | PASS | LOW |  |
| CARS.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.16 | $38.16 | PASS |  |  |
| CARS.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $19.88 | $19.88 | PASS |  |  |
| CARS.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.16 / $19.88 | $38.16 / $19.88 | PASS |  |  |
| CARS.TO | PD3 | % from High | -47.9% | -47.9% | PASS |  |  |
| CARS.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| CCO.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $182.72 | $182.72 | PASS |  |  |
| CCO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $89.40 | $89.40 | PASS |  |  |
| CCO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $182.72 / $89.20 | $182.72 / $89.20 | PASS |  |  |
| CCO.TO | PD3 | % from High | -51.1% | -51.1% | PASS |  |  |
| CCO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $103M | bars: $112,560,851 | PASS | LOW |  |
| CGY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $84.14 | $84.14 | PASS |  |  |
| CGY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $95.15 / $44.20 | $95.15 / $44.20 | PASS |  |  |
| CGY.TO | PD3 | % from High | -11.6% | -11.6% | PASS |  |  |
| CGY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,550,161 | PASS | LOW |  |
| CNQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $78.60 | $78.60 | PASS |  |  |
| CNQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $65.26 | $65.26 | PASS |  |  |
| CNQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $78.60 / $40.51 | $78.60 / $40.51 | PASS |  |  |
| CNQ.TO | PD3 | % from High | -17.0% | -17.0% | PASS |  |  |
| CNQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $885M | bars: $796,948,730 | PASS | LOW |  |
| CNR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $184.26 | $184.26 | PASS |  |  |
| CNR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $179.36 | $179.36 | PASS |  |  |
| CNR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $184.26 / $125.06 | $184.26 / $125.06 | PASS |  |  |
| CNR.TO | PD3 | % from High | -2.7% | -2.7% | PASS |  |  |
| CNR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $229M | bars: $221,468,286 | PASS | LOW |  |
| COP | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $154.28 | $154.28 | PASS |  |  |
| COP | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $134.40 | $134.40 | PASS |  |  |
| COP | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $154.28 / $85.70 | $154.28 / $85.70 | PASS |  |  |
| COP | PD3 | % from High | -12.9% | -12.9% | PASS |  |  |
| COP | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $913M | bars: $926,685,930 | PASS | LOW |  |
| COPP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $70.54 | $70.54 | PASS |  |  |
| COPP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $43.08 | $43.08 | PASS |  |  |
| COPP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $70.54 / $42.17 | $70.54 / $42.17 | PASS |  |  |
| COPP.TO | PD3 | % from High | -38.9% | -38.9% | PASS |  |  |
| COPX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $99.65 | $99.65 | PASS |  |  |
| COPX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $61.19 | $61.19 | PASS |  |  |
| COPX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $99.65 / $55.44 | $99.65 / $55.44 | PASS |  |  |
| COPX | PD3 | % from High | -38.6% | -38.6% | PASS |  |  |
| COPX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $178M | bars: $179,476,208 | PASS | LOW |  |
| COPZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $7.53 | $7.53 | PASS |  |  |
| COPZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $26.40 / $7.38 | $26.40 / $7.38 | PASS |  |  |
| COPZ | PD3 | % from High | -71.5% | -71.5% | PASS |  |  |
| COST | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,123.67 | $1,123.67 | PASS |  |  |
| COST | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,096.62 | $1,096.62 | PASS |  |  |
| COST | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,123.67 / $844.06 | $1,123.67 / $844.06 | PASS |  |  |
| COST | PD3 | % from High | -2.4% | -2.4% | PASS |  |  |
| COST | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.5B | bars: $2,591,314,551 | PASS | LOW |  |
| COTG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $17.80 | $17.80 | PASS |  |  |
| COTG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $16.53 | $16.53 | PASS |  |  |
| COTG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $17.80 / $10.95 | $17.80 / $10.95 | PASS |  |  |
| COTG | PD3 | % from High | -7.2% | -7.1% | PASS |  |  |
| COTG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,739,419 | PASS | LOW |  |
| CSU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $3,565.00 | $3,565.00 | PASS |  |  |
| CSU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3,323.15 | $3,323.15 | PASS |  |  |
| CSU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $3,565.00 / $2,192.51 | $3,565.00 / $2,192.51 | PASS |  |  |
| CSU.TO | PD3 | % from High | -6.8% | -6.8% | PASS |  |  |
| CSU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $199M | bars: $202,550,844 | PASS | LOW |  |
| CVX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $236.48 | $236.48 | PASS |  |  |
| CVX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $205.88 | $205.88 | PASS |  |  |
| CVX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $236.48 / $146.49 | $236.48 / $146.49 | PASS |  |  |
| CVX | PD3 | % from High | -12.9% | -12.9% | PASS |  |  |
| CVX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.7B | bars: $1,804,862,852 | PASS | LOW |  |
| DRAL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $4.15 | $4.15 | PASS |  |  |
| DRAL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $25.52 / $3.73 | $25.52 / $3.73 | PASS |  |  |
| DRAL | PD3 | % from High | -83.7% | -83.7% | PASS |  |  |
| DRAM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.15 | $39.15 | PASS |  |  |
| DRAM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $81.34 / $26.14 | $81.34 / $26.14 | PASS |  |  |
| DRAM | PD3 | % from High | -51.9% | -51.9% | PASS |  |  |
| DRAM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.3B | bars: $1,355,190,561 | PASS | LOW |  |
| DRIV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $42.67 | $42.67 | PASS |  |  |
| DRIV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $26.82 | $26.82 | PASS |  |  |
| DRIV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $42.67 / $26.77 | $42.67 / $26.77 | PASS |  |  |
| DRIV | PD3 | % from High | -37.2% | -37.1% | PASS |  |  |
| DRIV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1M | bars: $1,069,367 | PASS | LOW |  |
| DUK | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.87 | $131.87 | PASS |  |  |
| DUK | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $130.05 | $130.05 | PASS |  |  |
| DUK | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.87 / $110.06 | $131.87 / $110.06 | PASS |  |  |
| DUK | PD3 | % from High | -1.4% | -1.4% | PASS |  |  |
| DUK | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $544M | bars: $582,146,196 | PASS | LOW |  |
| ELIL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.56 | $43.56 | PASS |  |  |
| ELIL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $38.28 | $38.28 | PASS |  |  |
| ELIL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.56 / $16.21 | $43.56 / $16.21 | PASS |  |  |
| ELIL | PD3 | % from High | -12.1% | -12.1% | PASS |  |  |
| ELIL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,345,492 | PASS | LOW |  |
| EQIX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,112.65 | $1,112.65 | PASS |  |  |
| EQIX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,036.50 | $1,036.50 | PASS |  |  |
| EQIX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,112.65 / $706.18 | $1,112.65 / $706.18 | PASS |  |  |
| EQIX | PD3 | % from High | -6.8% | -6.8% | PASS |  |  |
| EQIX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $592M | bars: $605,240,584 | PASS | LOW |  |
| ETN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $476.54 | $476.54 | PASS |  |  |
| ETN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $338.34 | $338.34 | PASS |  |  |
| ETN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $476.54 / $308.40 | $476.54 / $308.40 | PASS |  |  |
| ETN | PD3 | % from High | -29.0% | -29.0% | PASS |  |  |
| ETN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $828M | bars: $897,519,106 | PASS | LOW |  |
| FCX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.07 | $80.07 | PASS |  |  |
| FCX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $51.45 | $51.45 | PASS |  |  |
| FCX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.07 / $38.49 | $80.07 / $38.49 | PASS |  |  |
| FCX | PD3 | % from High | -35.7% | -35.7% | PASS |  |  |
| FCX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $656M | bars: $626,447,688 | PASS | LOW |  |
| FINN.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $35.83 | $35.83 | PASS |  |  |
| FINN.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $31.97 | $31.97 | PASS |  |  |
| FINN.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $35.83 / $21.66 | $35.83 / $21.66 | PASS |  |  |
| FINN.NE | PD3 | % from High | -10.8% | -10.8% | PASS |  |  |
| FINN.NE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $9M | bars: $10,037,795 | PASS | LOW |  |
| GDX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $117.18 | $117.18 | PASS |  |  |
| GDX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $74.82 | $74.82 | PASS |  |  |
| GDX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $117.18 / $69.74 | $117.18 / $69.74 | PASS |  |  |
| GDX | PD3 | % from High | -36.1% | -36.1% | PASS |  |  |
| GDX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.7B | bars: $1,646,982,283 | PASS | LOW |  |
| GDXU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $65.00 | $65.00 | PASS |  |  |
| GDXU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $21.83 | $21.83 | PASS |  |  |
| GDXU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $65.00 / $20.70 | $65.00 / $20.70 | PASS |  |  |
| GDXU.TO | PD3 | % from High | -66.4% | -66.4% | PASS |  |  |
| GDXU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5M | bars: $5,312,151 | PASS | LOW |  |
| GE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $388.25 | $388.25 | PASS |  |  |
| GE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $328.10 | $328.10 | PASS |  |  |
| GE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $388.25 / $268.17 | $388.25 / $268.17 | PASS |  |  |
| GE | PD3 | % from High | -15.5% | -15.5% | PASS |  |  |
| GE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.5B | bars: $1,584,669,329 | PASS | LOW |  |
| GEV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,195.94 | $1,195.94 | PASS |  |  |
| GEV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $772.22 | $772.22 | PASS |  |  |
| GEV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,195.94 / $530.16 | $1,195.94 / $530.16 | PASS |  |  |
| GEV | PD3 | % from High | -35.4% | -35.4% | PASS |  |  |
| GEV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,450,043,167 | PASS | LOW |  |
| GEV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $51.66 | $51.66 | PASS |  |  |
| GEV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.44 / $42.23 | $80.44 / $42.23 | PASS |  |  |
| GEV.TO | PD3 | % from High | -35.8% | -35.8% | PASS |  |  |
| GEV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,898,104 | PASS | LOW |  |
| GGLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $151.33 | $151.33 | PASS |  |  |
| GGLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $64.16 | $64.16 | PASS |  |  |
| GGLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $151.33 / $62.13 | $151.33 / $62.13 | PASS |  |  |
| GGLL | PD3 | % from High | -57.6% | -57.6% | PASS |  |  |
| GGLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $110M | bars: $122,192,207 | PASS | LOW |  |
| GIB-A.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.27 | $131.27 | PASS |  |  |
| GIB-A.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $115.21 | $115.21 | PASS |  |  |
| GIB-A.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.27 / $83.04 | $131.27 / $83.04 | PASS |  |  |
| GIB-A.TO | PD3 | % from High | -12.2% | -12.2% | PASS |  |  |
| GIB-A.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $70M | bars: $72,484,346 | PASS | LOW |  |
| GOOGL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $408.10 | $408.10 | PASS |  |  |
| GOOGL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $282.44 | $282.44 | PASS |  |  |
| GOOGL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $408.10 / $271.77 | $408.10 / $271.77 | PASS |  |  |
| GOOGL | PD3 | % from High | -30.8% | -30.8% | PASS |  |  |
| GOOGL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.5B | bars: $9,063,174,139 | PASS | LOW |  |
| HD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $339.01 | $339.01 | PASS |  |  |
| HD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.18 / $277.15 | $389.18 / $277.15 | PASS |  |  |
| HD | PD3 | % from High | -12.9% | -12.9% | PASS |  |  |
| HD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,710,677,005 | PASS | LOW |  |
| HURA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $73.95 | $73.95 | PASS |  |  |
| HURA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $36.66 | $36.66 | PASS |  |  |
| HURA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $73.95 / $36.60 | $73.95 / $36.60 | PASS |  |  |
| HURA.TO | PD3 | % from High | -50.4% | -50.4% | PASS |  |  |
| HXQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $111.81 | $111.81 | PASS |  |  |
| HXQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $128.37 / $91.48 | $128.37 / $91.48 | PASS |  |  |
| HXQ.TO | PD3 | % from High | -12.9% | -12.9% | PASS |  |  |
| HXQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,665,206 | PASS | LOW |  |
| JNJ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $290.25 | $290.25 | PASS |  |  |
| JNJ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $272.70 | $272.70 | PASS |  |  |
| JNJ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $290.25 / $194.15 | $290.25 / $194.15 | PASS |  |  |
| JNJ | PD3 | % from High | -6.0% | -6.0% | PASS |  |  |
| JNJ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.9B | bars: $2,008,683,712 | PASS | LOW |  |
| JPM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $364.68 | $364.68 | PASS |  |  |
| JPM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $324.11 | $324.11 | PASS |  |  |
| JPM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $364.68 / $275.06 | $364.68 / $275.06 | PASS |  |  |
| JPM | PD3 | % from High | -11.1% | -11.1% | PASS |  |  |
| JPM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.3B | bars: $2,466,025,343 | PASS | LOW |  |
| KEYS | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $284.45 | $284.45 | PASS |  |  |
| KEYS | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.93 / $167.23 | $389.93 / $167.23 | PASS |  |  |
| KEYS | PD3 | % from High | -27.1% | -27.1% | PASS |  |  |
| KEYS | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $378M | bars: $372,354,721 | PASS | LOW |  |
| LIN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $546.47 | $546.47 | PASS |  |  |
| LIN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $512.16 | $512.16 | PASS |  |  |
| LIN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $546.47 / $384.12 | $546.47 / $384.12 | PASS |  |  |
| LIN | PD3 | % from High | -6.3% | -6.3% | PASS |  |  |
| LIN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.1B | bars: $1,064,005,599 | PASS | LOW |  |
| LLY | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,415.55 | $1,415.55 | PASS |  |  |
| LLY | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,475.25 / $846.81 | $1,475.25 / $846.81 | PASS |  |  |
| LLY | PD3 | % from High | -4.0% | -4.0% | PASS |  |  |
| LLY | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.7B | bars: $3,661,136,054 | PASS | LOW |  |
| MDA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $67.90 | $67.90 | PASS |  |  |
| MDA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.98 | $39.98 | PASS |  |  |
| MDA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $67.90 / $20.85 | $67.90 / $20.85 | PASS |  |  |
| MDA.TO | PD3 | % from High | -41.1% | -41.1% | PASS |  |  |
| MDA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $62M | bars: $63,311,611 | PASS | LOW |  |
| META | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $618.87 | $618.87 | PASS |  |  |
| META | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $779.82 / $519.37 | $779.82 / $519.37 | PASS |  |  |
| META | PD3 | % from High | -20.6% | -20.6% | PASS |  |  |
| META | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $13.0B | bars: $13,729,570,301 | PASS | LOW |  |
| METU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.96 | $38.96 | PASS |  |  |
| METU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $21.36 | $21.36 | PASS |  |  |
| METU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.96 / $16.76 | $38.96 / $16.76 | PASS |  |  |
| METU | PD3 | % from High | -45.2% | -45.2% | PASS |  |  |
| METU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $114M | bars: $101,453,122 | PASS | LOW |  |
| MRVL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $148.74 | $148.74 | PASS |  |  |
| MRVL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $329.73 / $70.62 | $329.73 / $70.62 | PASS |  |  |
| MRVL | PD3 | % from High | -54.9% | -54.9% | PASS |  |  |
| MRVL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.7B | bars: $3,593,494,442 | PASS | LOW |  |
| MSFT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $506.24 | $506.24 | PASS |  |  |
| MSFT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $559.15 / $348.54 | $559.15 / $348.54 | PASS |  |  |
| MSFT | PD3 | % from High | -9.5% | -9.5% | PASS |  |  |
| MSFT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $11.8B | bars: $12,026,660,657 | PASS | LOW |  |
| MSFU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $45.88 | $45.88 | PASS |  |  |
| MSFU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $37.61 | $37.61 | PASS |  |  |
| MSFU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $45.88 / $19.32 | $45.88 / $19.32 | PASS |  |  |
| MSFU | PD3 | % from High | -18.0% | -18.0% | PASS |  |  |
| MSFU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $94M | bars: $91,643,234 | PASS | LOW |  |
| MTRX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $28.81 | $28.81 | PASS |  |  |
| MTRX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $39.30 / $28.00 | $39.30 / $28.00 | PASS |  |  |
| MTRX.TO | PD3 | % from High | -26.7% | -26.7% | PASS |  |  |
| MU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $55.28 | $55.28 | PASS |  |  |
| MU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.76 | $30.76 | PASS |  |  |
| MU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $55.28 / $8.62 | $55.28 / $8.62 | PASS |  |  |
| MU.TO | PD3 | % from High | -44.4% | -44.4% | PASS |  |  |
| MU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $54M | bars: $57,056,916 | PASS | LOW |  |
| NEE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $97.30 | $97.30 | PASS |  |  |
| NEE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $84.78 | $84.78 | PASS |  |  |
| NEE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $97.30 / $74.41 | $97.30 / $74.41 | PASS |  |  |
| NEE | PD3 | % from High | -12.9% | -12.9% | PASS |  |  |
| NEE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.0B | bars: $1,078,106,057 | PASS | LOW |  |
| NEM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $135.01 | $135.01 | PASS |  |  |
| NEM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $104.53 | $104.53 | PASS |  |  |
| NEM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $135.01 / $80.59 | $135.01 / $80.59 | PASS |  |  |
| NEM | PD3 | % from High | -22.6% | -22.6% | PASS |  |  |
| NEM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $725M | bars: $675,283,525 | PASS | LOW |  |
| NFLX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $59.82 | $59.82 | PASS |  |  |
| NFLX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $115.25 / $59.41 | $115.25 / $59.41 | PASS |  |  |
| NFLX | PD3 | % from High | -48.1% | -48.1% | PASS |  |  |
| NFLX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,377,054,670 | PASS | LOW |  |
| NFXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.64 | $46.64 | PASS |  |  |
| NFXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $9.88 | $9.88 | PASS |  |  |
| NFXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.64 / $9.77 | $46.64 / $9.77 | PASS |  |  |
| NFXL | PD3 | % from High | -78.8% | -78.8% | PASS |  |  |
| NFXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15M | bars: $16,387,363 | PASS | LOW |  |
| NTR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $114.19 | $114.19 | PASS |  |  |
| NTR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $94.52 | $94.52 | PASS |  |  |
| NTR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $114.19 / $74.44 | $114.19 / $74.44 | PASS |  |  |
| NTR.TO | PD3 | % from High | -17.2% | -17.2% | PASS |  |  |
| NTR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $171M | bars: $180,023,215 | PASS | LOW |  |
| NVDA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $155.46 | $155.46 | PASS |  |  |
| NVDA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $243.37 / $148.80 | $243.37 / $148.80 | PASS |  |  |
| NVDA | PD3 | % from High | -36.1% | -36.1% | PASS |  |  |
| NVDA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $24.0B | bars: $24,545,535,560 | PASS | LOW |  |
| NVDL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.27 | $43.27 | PASS |  |  |
| NVDL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $15.24 | $15.24 | PASS |  |  |
| NVDL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.27 / $14.54 | $43.27 / $14.54 | PASS |  |  |
| NVDL | PD3 | % from High | -64.8% | -64.8% | PASS |  |  |
| NVDL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $271M | bars: $284,034,647 | PASS | LOW |  |
| ONTO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $386.46 | $386.46 | PASS |  |  |
| ONTO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $201.02 | $201.02 | PASS |  |  |
| ONTO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $386.46 / $121.58 | $386.46 / $121.58 | PASS |  |  |
| ONTO | PD3 | % from High | -48.0% | -48.0% | PASS |  |  |
| ONTO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $201M | bars: $210,703,688 | PASS | LOW |  |
| ORBX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $14.39 | $14.39 | PASS |  |  |
| ORBX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.62 / $12.81 | $31.62 / $12.81 | PASS |  |  |
| ORBX.TO | PD3 | % from High | -54.5% | -54.5% | PASS |  |  |
| ORCL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $248.47 | $248.47 | PASS |  |  |
| ORCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $113.89 | $113.89 | PASS |  |  |
| ORCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $248.47 / $109.21 | $248.47 / $109.21 | PASS |  |  |
| ORCL | PD3 | % from High | -54.2% | -54.2% | PASS |  |  |
| ORCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.8B | bars: $4,153,431,108 | PASS | LOW |  |
| PG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $171.72 | $171.72 | PASS |  |  |
| PG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $173.59 / $133.74 | $173.59 / $133.74 | PASS |  |  |
| PG | PD3 | % from High | -1.1% | -1.1% | PASS |  |  |
| PG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,619,126,587 | PASS | LOW |  |
| PNG.V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $10.72 | $10.72 | PASS |  |  |
| PNG.V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $2.99 | $2.99 | PASS |  |  |
| PNG.V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $10.72 / $2.99 | $10.72 / $2.99 | PASS |  |  |
| PNG.V | PD3 | % from High | -72.1% | -72.1% | PASS |  |  |
| PNG.V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $3,597,015 | PASS | LOW |  |
| QCOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $257.56 | $257.56 | PASS |  |  |
| QCOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $159.81 | $159.81 | PASS |  |  |
| QCOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $257.56 / $120.88 | $257.56 / $120.88 | PASS |  |  |
| QCOM | PD3 | % from High | -38.0% | -38.0% | PASS |  |  |
| QCOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.0B | bars: $2,111,036,723 | PASS | LOW |  |
| QPUX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.28 | $80.28 | PASS |  |  |
| QPUX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3.19 | $3.19 | PASS |  |  |
| QPUX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.28 / $3.12 | $80.28 / $3.12 | PASS |  |  |
| QPUX | PD3 | % from High | -96.0% | -96.0% | PASS |  |  |
| QTUM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $169.21 | $169.21 | PASS |  |  |
| QTUM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $122.95 | $122.95 | PASS |  |  |
| QTUM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $169.21 / $97.17 | $169.21 / $97.17 | PASS |  |  |
| QTUM | PD3 | % from High | -27.3% | -27.3% | PASS |  |  |
| QTUM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $40M | bars: $41,485,051 | PASS | LOW |  |
| RBOT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.15 | $38.15 | PASS |  |  |
| RBOT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $27.09 | $27.09 | PASS |  |  |
| RBOT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.15 / $27.00 | $38.15 / $27.00 | PASS |  |  |
| RBOT.TO | PD3 | % from High | -29.0% | -29.0% | PASS |  |  |
| RTX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $226.41 | $226.41 | PASS |  |  |
| RTX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $197.45 | $197.45 | PASS |  |  |
| RTX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $226.41 / $164.96 | $226.41 / $164.96 | PASS |  |  |
| RTX | PD3 | % from High | -12.8% | -12.8% | PASS |  |  |
| RTX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $921M | bars: $961,613,716 | PASS | LOW |  |
| RY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.65 | $302.65 | PASS |  |  |
| RY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $272.26 | $272.26 | PASS |  |  |
| RY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.65 / $199.32 | $302.65 / $199.32 | PASS |  |  |
| RY.TO | PD3 | % from High | -10.0% | -10.0% | PASS |  |  |
| RY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $883M | bars: $906,485,270 | PASS | LOW |  |
| SGRD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.96 | $17.96 | PASS |  |  |
| SGRD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $22.49 / $17.20 | $22.49 / $17.20 | PASS |  |  |
| SGRD.TO | PD3 | % from High | -20.1% | -20.1% | PASS |  |  |
| SMH | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $459.54 | $459.54 | PASS |  |  |
| SMH | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $671.83 / $314.08 | $671.83 / $314.08 | PASS |  |  |
| SMH | PD3 | % from High | -31.6% | -31.6% | PASS |  |  |
| SMH | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.0B | bars: $4,271,967,476 | PASS | LOW |  |
| SNDK.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $18.74 | $18.74 | PASS |  |  |
| SNDK.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $57.55 / $18.14 | $57.55 / $18.14 | PASS |  |  |
| SNDK.TO | PD3 | % from High | -67.4% | -67.4% | PASS |  |  |
| SNDK.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $23M | bars: $23,544,207 | PASS | LOW |  |
| SO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $97.65 | $97.65 | PASS |  |  |
| SO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $94.41 | $94.41 | PASS |  |  |
| SO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $97.65 / $81.03 | $97.65 / $81.03 | PASS |  |  |
| SO | PD3 | % from High | -3.3% | -3.3% | PASS |  |  |
| SO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $658M | bars: $685,963,800 | PASS | LOW |  |
| SOXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $301.80 | $301.80 | PASS |  |  |
| SOXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $49.26 | $49.26 | PASS |  |  |
| SOXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $301.80 / $28.10 | $301.80 / $28.10 | PASS |  |  |
| SOXL | PD3 | % from High | -83.7% | -83.7% | PASS |  |  |
| SOXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5.2B | bars: $6,057,560,329 | PASS | LOW |  |
| SOXL.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $74.21 | $74.21 | PASS |  |  |
| SOXL.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.43 | $12.43 | PASS |  |  |
| SOXL.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $74.21 / $7.92 | $74.21 / $7.92 | PASS |  |  |
| SOXL.NE | PD3 | % from High | -83.3% | -83.3% | PASS |  |  |
| SOXL.NE | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| SOXX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $218.51 | $218.51 | PASS |  |  |
| SOXX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $141.85 | $141.85 | PASS |  |  |
| SOXX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $218.51 / $86.54 | $218.51 / $86.54 | PASS |  |  |
| SOXX | PD3 | % from High | -35.1% | -35.1% | PASS |  |  |
| SOXX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.0B | bars: $4,271,304,933 | PASS | LOW |  |
| SPCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $9.44 | $9.44 | PASS |  |  |
| SPCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $83.85 / $8.20 | $83.85 / $8.20 | PASS |  |  |
| SPCL | PD3 | % from High | -88.7% | -88.7% | PASS |  |  |
| TSLA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $498.83 | $498.83 | PASS |  |  |
| TSLA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $383.72 | $383.72 | PASS |  |  |
| TSLA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $498.83 / $297.38 | $498.83 / $297.38 | PASS |  |  |
| TSLA | PD3 | % from High | -23.1% | -23.1% | PASS |  |  |
| TSLA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $14.4B | bars: $13,836,098,456 | PASS | LOW |  |
| TSLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $23.10 | $23.10 | PASS |  |  |
| TSLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $10.00 | $10.00 | PASS |  |  |
| TSLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $23.10 / $6.65 | $23.10 / $6.65 | PASS |  |  |
| TSLL | PD3 | % from High | -56.7% | -56.7% | PASS |  |  |
| TSLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $658M | bars: $542,270,940 | PASS | LOW |  |
| TSM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $487.47 | $487.47 | PASS |  |  |
| TSM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $362.62 | $362.62 | PASS |  |  |
| TSM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $487.47 / $264.03 | $487.47 / $264.03 | PASS |  |  |
| TSM | PD3 | % from High | -25.6% | -25.6% | PASS |  |  |
| TSM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.3B | bars: $4,624,530,551 | PASS | LOW |  |
| UBOT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $31.91 | $31.91 | PASS |  |  |
| UBOT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $15.07 | $15.07 | PASS |  |  |
| UBOT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.91 / $14.87 | $31.91 / $14.87 | PASS |  |  |
| UBOT | PD3 | % from High | -52.8% | -52.8% | PASS |  |  |
| UFO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $68.12 | $68.12 | PASS |  |  |
| UFO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.09 | $39.09 | PASS |  |  |
| UFO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $68.12 / $30.78 | $68.12 / $30.78 | PASS |  |  |
| UFO | PD3 | % from High | -42.6% | -42.6% | PASS |  |  |
| UFO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $10M | bars: $9,878,434 | PASS | LOW |  |
| V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $416.77 | $416.77 | PASS |  |  |
| V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $441.41 / $292.20 | $441.41 / $292.20 | PASS |  |  |
| V | PD3 | % from High | -5.6% | -5.6% | PASS |  |  |
| V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.7B | bars: $2,717,461,263 | PASS | LOW |  |
| VFV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $186.20 | $186.20 | PASS |  |  |
| VFV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $197.83 / $155.29 | $197.83 / $155.29 | PASS |  |  |
| VFV.TO | PD3 | % from High | -5.9% | -5.9% | PASS |  |  |
| VFV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $55M | bars: $58,725,022 | PASS | LOW |  |
| VRT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $190.37 | $190.37 | PASS |  |  |
| VRT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $379.76 / $147.72 | $379.76 / $147.72 | PASS |  |  |
| VRT | PD3 | % from High | -49.9% | -49.9% | PASS |  |  |
| VRT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.2B | bars: $1,295,743,886 | PASS | LOW |  |
| WDC.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.44 | $17.44 | PASS |  |  |
| WDC.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $48.85 / $15.70 | $48.85 / $15.70 | PASS |  |  |
| WDC.TO | PD3 | % from High | -64.3% | -64.3% | PASS |  |  |
| WDC.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,828,638 | PASS | LOW |  |
| WELL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $253.37 | $253.37 | PASS |  |  |
| WELL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $247.25 | $247.25 | PASS |  |  |
| WELL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $253.37 / $178.92 | $253.37 / $178.92 | PASS |  |  |
| WELL | PD3 | % from High | -2.4% | -2.4% | PASS |  |  |
| WELL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $681M | bars: $702,334,394 | PASS | LOW |  |
| WMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $127.52 | $127.52 | PASS |  |  |
| WMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $134.84 / $98.85 | $134.84 / $98.85 | PASS |  |  |
| WMT | PD3 | % from High | -5.4% | -5.4% | PASS |  |  |
| WMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.1B | bars: $2,756,086,700 | PASS | LOW |  |
| XCHP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $161.26 | $161.26 | PASS |  |  |
| XCHP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $105.84 | $105.84 | PASS |  |  |
| XCHP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $161.26 / $64.67 | $161.26 / $64.67 | PASS |  |  |
| XCHP.TO | PD3 | % from High | -34.4% | -34.4% | PASS |  |  |
| XCHP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5M | bars: $5,481,293 | PASS | LOW |  |
| XDRV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $61.36 | $61.36 | PASS |  |  |
| XDRV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $38.84 | $38.84 | PASS |  |  |
| XDRV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $61.36 / $38.62 | $61.36 / $38.62 | PASS |  |  |
| XDRV.TO | PD3 | % from High | -36.7% | -36.7% | PASS |  |  |
| XDRV.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| XEQT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $44.01 | $44.01 | PASS |  |  |
| XEQT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.38 / $37.96 | $46.38 / $37.96 | PASS |  |  |
| XEQT.TO | PD3 | % from High | -5.1% | -5.1% | PASS |  |  |
| XEQT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $37M | bars: $40,041,754 | PASS | LOW |  |
| XETM.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $57.76 | $57.76 | PASS |  |  |
| XETM.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $93.94 / $57.46 | $93.94 / $57.46 | PASS |  |  |
| XETM.TO | PD3 | % from High | -38.5% | -38.5% | PASS |  |  |
| XGD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $69.54 | $69.54 | PASS |  |  |
| XGD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $48.44 | $48.44 | PASS |  |  |
| XGD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $69.54 / $43.30 | $69.54 / $43.30 | PASS |  |  |
| XGD.TO | PD3 | % from High | -30.3% | -30.3% | PASS |  |  |
| XGD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $24M | bars: $22,644,287 | PASS | LOW |  |
| XOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $188.50 | $188.50 | PASS |  |  |
| XOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $160.58 | $160.58 | PASS |  |  |
| XOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $188.50 / $114.19 | $188.50 / $114.19 | PASS |  |  |
| XOM | PD3 | % from High | -14.8% | -14.8% | PASS |  |  |
| XOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,182,248,600 | PASS | LOW |  |
| AAPL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $351.91 / RS 1.18 | $351.91 / RS 1.18 | PASS |  |  |
| AAPL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.18 | 1.18 | PASS |  |  |
| AAPL | RS2 | Stock 52W Return and S&P 52W Return | +32.0% / +11.8% | +32.0% / +11.8% | PASS |  |  |
| AAPL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| AAPL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +32.0% clears | +32.0% clears | PASS |  |  |
| AAPU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $48.59 / RS 1.34 | $48.59 / RS 1.34 | PASS |  |  |
| AAPU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.34 | 1.34 | PASS |  |  |
| AAPU | RS2 | Stock 52W Return and S&P 52W Return | +49.9% / +11.8% | +49.9% / +11.8% | PASS |  |  |
| AAPU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 77 | 77 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market | Well ahead of the market | PASS |  |  |
| AAPU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.9% clears | +49.9% clears | PASS |  |  |
| ABBV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $292.82 / RS 1.15 | $292.82 / RS 1.15 | PASS |  |  |
| ABBV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| ABBV | RS2 | Stock 52W Return and S&P 52W Return | +28.9% / +11.8% | +28.9% / +11.8% | PASS |  |  |
| ABBV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ABBV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ABBV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| ABBV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.9% clears | +28.9% clears | PASS |  |  |
| AIPO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $22.69 / RS 0.92 | $22.69 / RS 0.92 | PASS |  |  |
| AIPO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| AIPO | RS2 | Stock 52W Return and S&P 52W Return | +2.6% / +11.8% | +2.6% / +11.8% | PASS |  |  |
| AIPO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AIPO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AIPO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| AIPO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.6% under | +2.6% under | PASS |  |  |
| ALAB | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $211.60 / RS 1.34 | $211.60 / RS 1.34 | PASS |  |  |
| ALAB | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.34 | 1.34 | PASS |  |  |
| ALAB | RS2 | Stock 52W Return and S&P 52W Return | +49.7% / +11.8% | +49.7% / +11.8% | PASS |  |  |
| ALAB | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ALAB | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 77 | 77 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ALAB | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ALAB | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.7% clears | +49.7% clears | PASS |  |  |
| AMD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $530.14 / RS 2.06 | $530.14 / RS 2.06 | PASS |  |  |
| AMD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.06 | 2.06 | PASS |  |  |
| AMD | RS2 | Stock 52W Return and S&P 52W Return | +130.2% / +11.8% | +130.2% / +11.8% | PASS |  |  |
| AMD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +130.2% clears | +130.2% clears | PASS |  |  |
| AMZN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $267.74 / RS 1.08 | $267.74 / RS 1.08 | PASS |  |  |
| AMZN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.08 | 1.08 | PASS |  |  |
| AMZN | RS2 | Stock 52W Return and S&P 52W Return | +20.3% / +11.8% | +20.3% / +11.8% | PASS |  |  |
| AMZN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| AMZN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +20.3% clears | +20.3% clears | PASS |  |  |
| AMZU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $37.91 / RS 1.04 | $37.91 / RS 1.04 | PASS |  |  |
| AMZU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.04 | 1.04 | PASS |  |  |
| AMZU | RS2 | Stock 52W Return and S&P 52W Return | +16.6% / +11.8% | +16.6% / +11.8% | PASS |  |  |
| AMZU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 53 | 53 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| AMZU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +16.6% clears | +16.6% clears | PASS |  |  |
| ANET.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $34.66 / RS 1.30 | $34.66 / RS 1.30 | PASS |  |  |
| ANET.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.30 | 1.30 | PASS |  |  |
| ANET.TO | RS2 | Stock 52W Return and S&P 52W Return | +45.4% / +11.8% | +45.4% / +11.8% | PASS |  |  |
| ANET.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ANET.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ANET.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +45.4% clears | +45.4% clears | PASS |  |  |
| ASML.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $41.25 / RS 1.32 | $41.25 / RS 1.32 | PASS |  |  |
| ASML.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.32 | 1.32 | PASS |  |  |
| ASML.TO | RS2 | Stock 52W Return and S&P 52W Return | +47.6% / +11.8% | +47.6% / +11.8% | PASS |  |  |
| ASML.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASML.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 76 | 76 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASML.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ASML.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +47.6% clears | +47.6% clears | PASS |  |  |
| ASTL.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $6.94 / RS 1.25 | $6.94 / RS 1.25 | PASS |  |  |
| ASTL.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.25 | PASS |  |  |
| ASTL.TO | RS2 | Stock 52W Return and S&P 52W Return | +39.6% / +11.8% | +39.6% / +11.8% | PASS |  |  |
| ASTL.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASTL.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASTL.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| ASTL.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.6% clears | +39.6% clears | PASS |  |  |
| ATD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $83.00 / RS 1.08 | $83.00 / RS 1.08 | PASS |  |  |
| ATD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.08 | 1.08 | PASS |  |  |
| ATD.TO | RS2 | Stock 52W Return and S&P 52W Return | +20.7% / +11.8% | +20.7% / +11.8% | PASS |  |  |
| ATD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ATD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ATD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| ATD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +20.7% clears | +20.7% clears | PASS |  |  |
| AVGO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $341.60 / RS 0.90 | $341.60 / RS 0.90 | PASS |  |  |
| AVGO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| AVGO | RS2 | Stock 52W Return and S&P 52W Return | +0.4% / +11.8% | +0.4% / +11.8% | PASS |  |  |
| AVGO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AVGO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| AVGO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.4% under | +0.4% under | PASS |  |  |
| AVGO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.94 / RS 0.88 | $12.94 / RS 0.88 | PASS |  |  |
| AVGO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| AVGO.TO | RS2 | Stock 52W Return and S&P 52W Return | -1.8% / +11.8% | -1.8% / +11.8% | PASS |  |  |
| AVGO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| AVGO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.8% negative | -1.8% negative | PASS |  |  |
| BDT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $73.05 / RS 2.65 | $73.05 / RS 2.65 | PASS |  |  |
| BDT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.65 | 2.65 | PASS |  |  |
| BDT.TO | RS2 | Stock 52W Return and S&P 52W Return | +196.8% / +11.8% | +196.8% / +11.8% | PASS |  |  |
| BDT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BDT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BDT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| BDT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +196.8% clears | +196.8% clears | PASS |  |  |
| BOTZ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $29.71 / RS 0.79 | $29.71 / RS 0.79 | PASS |  |  |
| BOTZ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.79 | 0.79 | PASS |  |  |
| BOTZ | RS2 | Stock 52W Return and S&P 52W Return | -11.4% / +11.8% | -11.4% / +11.8% | PASS |  |  |
| BOTZ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BOTZ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BOTZ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| BOTZ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -11.4% negative | -11.4% negative | PASS |  |  |
| BRK-B | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $574.62 / RS 1.02 | $574.62 / RS 1.02 | PASS |  |  |
| BRK-B | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.02 | 1.02 | PASS |  |  |
| BRK-B | RS2 | Stock 52W Return and S&P 52W Return | +13.9% / +11.8% | +13.9% / +11.8% | PASS |  |  |
| BRK-B | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRK-B | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRK-B | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRK-B | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +13.9% clears | +13.9% clears | PASS |  |  |
| BRKU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $28.85 / RS 1.03 | $28.85 / RS 1.03 | PASS |  |  |
| BRKU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| BRKU | RS2 | Stock 52W Return and S&P 52W Return | +15.5% / +11.8% | +15.5% / +11.8% | PASS |  |  |
| BRKU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRKU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 53 | 53 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRKU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRKU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +15.5% clears | +15.5% clears | PASS |  |  |
| CAMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $98.42 / RS 0.93 | $98.42 / RS 0.93 | PASS |  |  |
| CAMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.93 | 0.93 | PASS |  |  |
| CAMT | RS2 | Stock 52W Return and S&P 52W Return | +3.9% / +11.8% | +3.9% / +11.8% | PASS |  |  |
| CAMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| CAMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.9% under | +3.9% under | PASS |  |  |
| CARS.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $19.88 / RS 0.69 | $19.88 / RS 0.69 | PASS |  |  |
| CARS.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.69 | 0.69 | PASS |  |  |
| CARS.TO | RS2 | Stock 52W Return and S&P 52W Return | -22.4% / +11.8% | -22.4% / +11.8% | PASS |  |  |
| CARS.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CARS.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 26 | 26 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CARS.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CARS.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -22.4% negative | -22.4% negative | PASS |  |  |
| CCO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $89.40 / RS 0.69 | $89.40 / RS 0.69 | PASS |  |  |
| CCO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.69 | 0.69 | PASS |  |  |
| CCO.TO | RS2 | Stock 52W Return and S&P 52W Return | -23.1% / +11.8% | -23.1% / +11.8% | PASS |  |  |
| CCO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CCO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 25 | 25 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CCO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| CCO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -23.1% negative | -23.1% negative | PASS |  |  |
| CGY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $84.14 / RS 1.53 | $84.14 / RS 1.53 | PASS |  |  |
| CGY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.53 | 1.53 | PASS |  |  |
| CGY.TO | RS2 | Stock 52W Return and S&P 52W Return | +71.2% / +11.8% | +71.2% / +11.8% | PASS |  |  |
| CGY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CGY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 92 | 92 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CGY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CGY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +71.2% clears | +71.2% clears | PASS |  |  |
| CNQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $65.26 / RS 1.28 | $65.26 / RS 1.28 | PASS |  |  |
| CNQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.28 | 1.28 | PASS |  |  |
| CNQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +43.0% / +11.8% | +43.1% / +11.8% | PASS |  |  |
| CNQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CNQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +43.0% clears | +43.1% clears | PASS |  |  |
| CNR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $179.36 / RS 1.25 | $179.36 / RS 1.25 | PASS |  |  |
| CNR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.25 | PASS |  |  |
| CNR.TO | RS2 | Stock 52W Return and S&P 52W Return | +39.8% / +11.8% | +39.8% / +11.8% | PASS |  |  |
| CNR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CNR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.8% clears | +39.8% clears | PASS |  |  |
| COP | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $134.40 / RS 1.34 | $134.40 / RS 1.34 | PASS |  |  |
| COP | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.34 | 1.34 | PASS |  |  |
| COP | RS2 | Stock 52W Return and S&P 52W Return | +49.9% / +11.8% | +49.9% / +11.8% | PASS |  |  |
| COP | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COP | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 77 | 77 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COP | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| COP | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.9% clears | +49.9% clears | PASS |  |  |
| COPP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $43.08 / RS 0.90 | $43.08 / RS 0.90 | PASS |  |  |
| COPP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| COPP.TO | RS2 | Stock 52W Return and S&P 52W Return | +0.3% / +11.8% | +0.3% / +11.8% | PASS |  |  |
| COPP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| COPP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.3% under | +0.3% under | PASS |  |  |
| COPX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $61.19 / RS 0.96 | $61.19 / RS 0.96 | PASS |  |  |
| COPX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.96 | PASS |  |  |
| COPX | RS2 | Stock 52W Return and S&P 52W Return | +7.0% / +11.8% | +7.0% / +11.8% | PASS |  |  |
| COPX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| COPX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +7.0% clears | +7.0% clears | PASS |  |  |
| COST | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,096.62 / RS 1.10 | $1,096.62 / RS 1.10 | PASS |  |  |
| COST | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.10 | 1.10 | PASS |  |  |
| COST | RS2 | Stock 52W Return and S&P 52W Return | +22.5% / +11.8% | +22.5% / +11.8% | PASS |  |  |
| COST | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COST | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COST | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| COST | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +22.5% clears | +22.5% clears | PASS |  |  |
| COTG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $16.53 / RS 1.17 | $16.53 / RS 1.17 | PASS |  |  |
| COTG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.17 | 1.17 | PASS |  |  |
| COTG | RS2 | Stock 52W Return and S&P 52W Return | +30.6% / +11.8% | +30.6% / +11.8% | PASS |  |  |
| COTG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COTG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 63 | 63 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COTG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| COTG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +30.6% clears | +30.6% clears | PASS |  |  |
| CSU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3,323.15 / RS 0.92 | $3,323.15 / RS 0.92 | PASS |  |  |
| CSU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| CSU.TO | RS2 | Stock 52W Return and S&P 52W Return | +2.8% / +11.8% | +2.8% / +11.8% | PASS |  |  |
| CSU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CSU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CSU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| CSU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.8% under | +2.8% under | PASS |  |  |
| CVX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $205.88 / RS 1.20 | $205.88 / RS 1.20 | PASS |  |  |
| CVX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.20 | 1.20 | PASS |  |  |
| CVX | RS2 | Stock 52W Return and S&P 52W Return | +34.0% / +11.8% | +34.0% / +11.8% | PASS |  |  |
| CVX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CVX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 66 | 66 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CVX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| CVX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +34.0% clears | +34.0% clears | PASS |  |  |
| DRIV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $26.82 / RS 0.85 | $26.82 / RS 0.85 | PASS |  |  |
| DRIV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| DRIV | RS2 | Stock 52W Return and S&P 52W Return | -5.4% / +11.8% | -5.4% / +11.8% | PASS |  |  |
| DRIV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DRIV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DRIV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| DRIV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.4% negative | -5.4% negative | PASS |  |  |
| DUK | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $130.05 / RS 0.97 | $130.05 / RS 0.97 | PASS |  |  |
| DUK | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.97 | 0.97 | PASS |  |  |
| DUK | RS2 | Stock 52W Return and S&P 52W Return | +8.7% / +11.8% | +8.7% / +11.8% | PASS |  |  |
| DUK | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DUK | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 48 | 48 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DUK | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| DUK | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +8.7% clears | +8.7% clears | PASS |  |  |
| ELIL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $38.28 / RS 1.31 | $38.28 / RS 1.31 | PASS |  |  |
| ELIL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.31 | 1.31 | PASS |  |  |
| ELIL | RS2 | Stock 52W Return and S&P 52W Return | +46.1% / +11.8% | +46.1% / +11.8% | PASS |  |  |
| ELIL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ELIL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 75 | 75 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ELIL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ELIL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +46.1% clears | +46.1% clears | PASS |  |  |
| EQIX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,036.50 / RS 1.22 | $1,036.50 / RS 1.22 | PASS |  |  |
| EQIX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.22 | 1.22 | PASS |  |  |
| EQIX | RS2 | Stock 52W Return and S&P 52W Return | +36.5% / +11.8% | +36.5% / +11.8% | PASS |  |  |
| EQIX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| EQIX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 68 | 68 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| EQIX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| EQIX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +36.5% clears | +36.5% clears | PASS |  |  |
| ETN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $338.34 / RS 0.91 | $338.34 / RS 0.90 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| ETN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.91 | 0.90 | PASS |  |  |
| ETN | RS2 | Stock 52W Return and S&P 52W Return | +1.2% / +11.8% | +1.2% / +11.8% | PASS |  |  |
| ETN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ETN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ETN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| ETN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +1.2% under | +1.2% under | PASS |  |  |
| FCX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $51.45 / RS 1.16 | $51.45 / RS 1.16 | PASS |  |  |
| FCX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.16 | 1.16 | PASS |  |  |
| FCX | RS2 | Stock 52W Return and S&P 52W Return | +29.8% / +11.8% | +29.8% / +11.8% | PASS |  |  |
| FCX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FCX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 63 | 63 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FCX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| FCX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.8% clears | +29.8% clears | PASS |  |  |
| FINN.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $31.97 / RS 1.28 | $31.97 / RS 1.28 | PASS |  |  |
| FINN.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.28 | 1.28 | PASS |  |  |
| FINN.NE | RS2 | Stock 52W Return and S&P 52W Return | +42.7% / +11.8% | +42.7% / +11.8% | PASS |  |  |
| FINN.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FINN.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FINN.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| FINN.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +42.7% clears | +42.7% clears | PASS |  |  |
| GDX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $74.82 / RS 0.89 | $74.82 / RS 0.89 | PASS |  |  |
| GDX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| GDX | RS2 | Stock 52W Return and S&P 52W Return | -0.3% / +11.8% | -0.3% / +11.8% | PASS |  |  |
| GDX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| GDX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -0.3% negative | -0.3% negative | PASS |  |  |
| GDXU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $21.83 / RS 0.65 | $21.83 / RS 0.65 | PASS |  |  |
| GDXU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.65 | PASS |  |  |
| GDXU.TO | RS2 | Stock 52W Return and S&P 52W Return | -27.6% / +11.8% | -27.6% / +11.8% | PASS |  |  |
| GDXU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDXU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDXU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| GDXU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -27.6% negative | -27.6% negative | PASS |  |  |
| GE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $328.10 / RS 1.00 | $328.10 / RS 1.00 | PASS |  |  |
| GE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.00 | 1.00 | PASS |  |  |
| GE | RS2 | Stock 52W Return and S&P 52W Return | +11.4% / +11.8% | +11.4% / +11.8% | PASS |  |  |
| GE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +11.4% clears | +11.4% clears | PASS |  |  |
| GEV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $772.22 / RS 1.25 | $772.22 / RS 1.24 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| GEV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.24 | PASS |  |  |
| GEV | RS2 | Stock 52W Return and S&P 52W Return | +39.2% / +11.8% | +39.2% / +11.8% | PASS |  |  |
| GEV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GEV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| GEV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.2% clears | +39.2% clears | PASS |  |  |
| GEV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $51.66 / RS 1.03 | $51.66 / RS 1.03 | PASS |  |  |
| GEV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| GEV.TO | RS2 | Stock 52W Return and S&P 52W Return | +14.8% / +11.8% | +14.8% / +11.8% | PASS |  |  |
| GEV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| GEV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.8% clears | +14.8% clears | PASS |  |  |
| GGLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $64.16 / RS 0.71 | $64.16 / RS 0.72 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| GGLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.71 | 0.72 | PASS |  |  |
| GGLL | RS2 | Stock 52W Return and S&P 52W Return | -20.1% / +11.8% | -20.0% / +11.8% | PASS |  |  |
| GGLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GGLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 27 | 27 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GGLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| GGLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -20.1% negative | -20.0% negative | PASS |  |  |
| GIB-A.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $115.21 / RS 0.86 | $115.21 / RS 0.86 | PASS |  |  |
| GIB-A.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.86 | 0.86 | PASS |  |  |
| GIB-A.TO | RS2 | Stock 52W Return and S&P 52W Return | -3.5% / +11.8% | -3.5% / +11.8% | PASS |  |  |
| GIB-A.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GIB-A.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 39 | 39 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GIB-A.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| GIB-A.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -3.5% negative | -3.5% negative | PASS |  |  |
| GOOGL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $282.44 / RS 0.89 | $282.44 / RS 0.89 | PASS |  |  |
| GOOGL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| GOOGL | RS2 | Stock 52W Return and S&P 52W Return | -0.4% / +11.8% | -0.4% / +11.8% | PASS |  |  |
| GOOGL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GOOGL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GOOGL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| GOOGL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -0.4% negative | -0.4% negative | PASS |  |  |
| HD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $339.01 / RS 0.87 | $339.01 / RS 0.87 | PASS |  |  |
| HD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.87 | 0.87 | PASS |  |  |
| HD | RS2 | Stock 52W Return and S&P 52W Return | -2.6% / +11.8% | -2.6% / +11.8% | PASS |  |  |
| HD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| HD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -2.6% negative | -2.6% negative | PASS |  |  |
| HURA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $36.66 / RS 0.65 | $36.66 / RS 0.65 | PASS |  |  |
| HURA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.65 | PASS |  |  |
| HURA.TO | RS2 | Stock 52W Return and S&P 52W Return | -27.6% / +11.8% | -27.5% / +11.8% | PASS |  |  |
| HURA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HURA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HURA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| HURA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -27.6% negative | -27.5% negative | PASS |  |  |
| HXQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $111.81 / RS 1.01 | $111.81 / RS 1.01 | PASS |  |  |
| HXQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.01 | PASS |  |  |
| HXQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +13.5% / +11.8% | +13.5% / +11.8% | PASS |  |  |
| HXQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HXQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HXQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| HXQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +13.5% clears | +13.5% clears | PASS |  |  |
| JNJ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $272.70 / RS 1.25 | $272.70 / RS 1.25 | PASS |  |  |
| JNJ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.25 | PASS |  |  |
| JNJ | RS2 | Stock 52W Return and S&P 52W Return | +39.4% / +11.8% | +39.4% / +11.8% | PASS |  |  |
| JNJ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JNJ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JNJ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| JNJ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.4% clears | +39.4% clears | PASS |  |  |
| JPM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $324.11 / RS 0.99 | $324.11 / RS 0.99 | PASS |  |  |
| JPM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.99 | 0.99 | PASS |  |  |
| JPM | RS2 | Stock 52W Return and S&P 52W Return | +10.3% / +11.8% | +10.3% / +11.8% | PASS |  |  |
| JPM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JPM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 49 | 49 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JPM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| JPM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +10.3% clears | +10.3% clears | PASS |  |  |
| KEYS | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $284.45 / RS 1.45 | $284.45 / RS 1.45 | PASS |  |  |
| KEYS | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.45 | 1.45 | PASS |  |  |
| KEYS | RS2 | Stock 52W Return and S&P 52W Return | +62.1% / +11.8% | +62.1% / +11.8% | PASS |  |  |
| KEYS | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| KEYS | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 86 | 86 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| KEYS | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| KEYS | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +62.1% clears | +62.1% clears | PASS |  |  |
| LIN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $512.16 / RS 1.12 | $512.16 / RS 1.12 | PASS |  |  |
| LIN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.12 | 1.12 | PASS |  |  |
| LIN | RS2 | Stock 52W Return and S&P 52W Return | +25.1% / +11.8% | +25.1% / +11.8% | PASS |  |  |
| LIN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LIN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LIN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| LIN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.1% clears | +25.1% clears | PASS |  |  |
| LLY | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,415.55 / RS 1.25 | $1,415.55 / RS 1.25 | PASS |  |  |
| LLY | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.25 | PASS |  |  |
| LLY | RS2 | Stock 52W Return and S&P 52W Return | +39.4% / +11.8% | +39.4% / +11.8% | PASS |  |  |
| LLY | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LLY | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LLY | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market | Ahead of the market | PASS |  |  |
| LLY | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.4% clears | +39.4% clears | PASS |  |  |
| MDA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.98 / RS 1.65 | $39.98 / RS 1.65 | PASS |  |  |
| MDA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.65 | 1.65 | PASS |  |  |
| MDA.TO | RS2 | Stock 52W Return and S&P 52W Return | +84.8% / +11.8% | +84.8% / +11.8% | PASS |  |  |
| MDA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MDA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MDA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MDA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +84.8% clears | +84.8% clears | PASS |  |  |
| META | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $618.87 / RS 0.92 | $618.87 / RS 0.92 | PASS |  |  |
| META | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| META | RS2 | Stock 52W Return and S&P 52W Return | +3.1% / +11.8% | +3.2% / +11.8% | PASS |  |  |
| META | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| META | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| META | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| META | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.1% under | +3.2% under | PASS |  |  |
| METU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $21.36 / RS 0.73 | $21.36 / RS 0.73 | PASS |  |  |
| METU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.73 | 0.73 | PASS |  |  |
| METU | RS2 | Stock 52W Return and S&P 52W Return | -18.8% / +11.8% | -18.8% / +11.8% | PASS |  |  |
| METU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| METU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 28 | 28 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| METU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| METU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -18.8% negative | -18.8% negative | PASS |  |  |
| MRVL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $148.74 / RS 1.60 | $148.74 / RS 1.60 | PASS |  |  |
| MRVL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.60 | 1.60 | PASS |  |  |
| MRVL | RS2 | Stock 52W Return and S&P 52W Return | +78.5% / +11.8% | +78.5% / +11.8% | PASS |  |  |
| MRVL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MRVL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 98 | 98 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MRVL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MRVL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +78.5% clears | +78.5% clears | PASS |  |  |
| MSFT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $506.24 / RS 0.90 | $506.24 / RS 0.90 | PASS |  |  |
| MSFT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.90 | 0.90 | PASS |  |  |
| MSFT | RS2 | Stock 52W Return and S&P 52W Return | +0.6% / +11.8% | +0.6% / +11.8% | PASS |  |  |
| MSFT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 42 | 42 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| MSFT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.6% under | +0.6% under | PASS |  |  |
| MSFU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $37.61 / RS 0.78 | $37.61 / RS 0.78 | PASS |  |  |
| MSFU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.78 | 0.78 | PASS |  |  |
| MSFU | RS2 | Stock 52W Return and S&P 52W Return | -12.6% / +11.8% | -12.6% / +11.8% | PASS |  |  |
| MSFU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| MSFU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -12.6% negative | -12.6% negative | PASS |  |  |
| MTRX.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $28.81 / RS 0.87 | $28.81 / RS 0.87 | PASS |  |  |
| MTRX.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.87 | 0.87 | PASS |  |  |
| MTRX.TO | RS2 | Stock 52W Return and S&P 52W Return | -3.2% / +11.8% | -3.2% / +11.8% | PASS |  |  |
| MTRX.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 39 | 39 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MTRX.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| MTRX.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -3.2% negative | -3.2% negative | PASS |  |  |
| MU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.76 / RS 2.68 | $30.76 / RS 2.68 | PASS |  |  |
| MU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.68 | 2.68 | PASS |  |  |
| MU.TO | RS2 | Stock 52W Return and S&P 52W Return | +199.8% / +11.8% | +199.8% / +11.8% | PASS |  |  |
| MU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +199.8% clears | +199.8% clears | PASS |  |  |
| NEE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $84.78 / RS 0.92 | $84.78 / RS 0.92 | PASS |  |  |
| NEE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| NEE | RS2 | Stock 52W Return and S&P 52W Return | +3.0% / +11.8% | +3.0% / +11.8% | PASS |  |  |
| NEE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| NEE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.0% under | +3.0% under | PASS |  |  |
| NEM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $104.53 / RS 1.09 | $104.53 / RS 1.09 | PASS |  |  |
| NEM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| NEM | RS2 | Stock 52W Return and S&P 52W Return | +21.8% / +11.8% | +21.8% / +11.8% | PASS |  |  |
| NEM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| NEM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +21.8% clears | +21.8% clears | PASS |  |  |
| NFLX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $59.82 / RS 0.47 | $59.82 / RS 0.47 | PASS |  |  |
| NFLX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.47 | 0.47 | PASS |  |  |
| NFLX | RS2 | Stock 52W Return and S&P 52W Return | -47.6% / +11.8% | -47.6% / +11.8% | PASS |  |  |
| NFLX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFLX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 8 | 8 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFLX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFLX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -47.6% negative | -47.6% negative | PASS |  |  |
| NFXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $9.88 / RS 0.19 | $9.88 / RS 0.19 | PASS |  |  |
| NFXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.19 | 0.19 | PASS |  |  |
| NFXL | RS2 | Stock 52W Return and S&P 52W Return | -78.4% / +11.8% | -78.4% / +11.8% | PASS |  |  |
| NFXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -78.4% negative | -78.4% negative | PASS |  |  |
| NTR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $94.52 / RS 1.09 | $94.52 / RS 1.09 | PASS |  |  |
| NTR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| NTR.TO | RS2 | Stock 52W Return and S&P 52W Return | +21.9% / +11.8% | +21.9% / +11.8% | PASS |  |  |
| NTR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NTR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NTR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| NTR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +21.9% clears | +21.9% clears | PASS |  |  |
| NVDA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $155.46 / RS 0.75 | $155.46 / RS 0.75 | PASS |  |  |
| NVDA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.75 | 0.75 | PASS |  |  |
| NVDA | RS2 | Stock 52W Return and S&P 52W Return | -16.5% / +11.8% | -16.5% / +11.8% | PASS |  |  |
| NVDA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 30 | 30 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -16.5% negative | -16.5% negative | PASS |  |  |
| NVDL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $15.24 / RS 0.48 | $15.24 / RS 0.48 | PASS |  |  |
| NVDL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.48 | 0.48 | PASS |  |  |
| NVDL | RS2 | Stock 52W Return and S&P 52W Return | -46.4% / +11.8% | -46.4% / +11.8% | PASS |  |  |
| NVDL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 8 | 8 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -46.4% negative | -46.4% negative | PASS |  |  |
| ONTO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $201.02 / RS 1.45 | $201.02 / RS 1.45 | PASS |  |  |
| ONTO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.45 | 1.45 | PASS |  |  |
| ONTO | RS2 | Stock 52W Return and S&P 52W Return | +62.0% / +11.8% | +62.0% / +11.8% | PASS |  |  |
| ONTO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ONTO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 86 | 86 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ONTO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ONTO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +62.0% clears | +62.0% clears | PASS |  |  |
| ORCL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $113.89 / RS 0.47 | $113.89 / RS 0.47 | PASS |  |  |
| ORCL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.47 | 0.47 | PASS |  |  |
| ORCL | RS2 | Stock 52W Return and S&P 52W Return | -47.7% / +11.8% | -47.7% / +11.8% | PASS |  |  |
| ORCL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ORCL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 7 | 7 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ORCL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| ORCL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -47.7% negative | -47.7% negative | PASS |  |  |
| PG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $171.72 / RS 1.08 | $171.72 / RS 1.08 | PASS |  |  |
| PG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.08 | 1.08 | PASS |  |  |
| PG | RS2 | Stock 52W Return and S&P 52W Return | +21.2% / +11.8% | +21.2% / +11.8% | PASS |  |  |
| PG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 57 | 57 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| PG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +21.2% clears | +21.2% clears | PASS |  |  |
| PNG.V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $2.99 / RS 0.50 | $2.99 / RS 0.50 | PASS |  |  |
| PNG.V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.50 | 0.50 | PASS |  |  |
| PNG.V | RS2 | Stock 52W Return and S&P 52W Return | -43.8% / +11.8% | -43.8% / +11.8% | PASS |  |  |
| PNG.V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PNG.V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 10 | 10 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PNG.V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| PNG.V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -43.8% negative | -43.8% negative | PASS |  |  |
| QCOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $159.81 / RS 0.88 | $159.81 / RS 0.88 | PASS |  |  |
| QCOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| QCOM | RS2 | Stock 52W Return and S&P 52W Return | -1.2% / +11.8% | -1.2% / +11.8% | PASS |  |  |
| QCOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QCOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QCOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| QCOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.2% negative | -1.2% negative | PASS |  |  |
| QPUX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3.19 / RS 0.04 | $3.19 / RS 0.04 | PASS |  |  |
| QPUX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.04 | 0.04 | PASS |  |  |
| QPUX | RS2 | Stock 52W Return and S&P 52W Return | -95.0% / +11.8% | -95.0% / +11.8% | PASS |  |  |
| QPUX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QPUX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QPUX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| QPUX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -95.0% negative | -95.0% negative | PASS |  |  |
| QTUM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $122.95 / RS 1.07 | $122.95 / RS 1.07 | PASS |  |  |
| QTUM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.07 | 1.07 | PASS |  |  |
| QTUM | RS2 | Stock 52W Return and S&P 52W Return | +19.5% / +11.8% | +19.5% / +11.8% | PASS |  |  |
| QTUM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QTUM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QTUM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| QTUM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +19.5% clears | +19.5% clears | PASS |  |  |
| RBOT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $27.09 / RS 0.77 | $27.09 / RS 0.77 | PASS |  |  |
| RBOT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.77 | 0.77 | PASS |  |  |
| RBOT.TO | RS2 | Stock 52W Return and S&P 52W Return | -13.4% / +11.8% | -13.5% / +11.8% | PASS |  |  |
| RBOT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RBOT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 32 | 32 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RBOT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| RBOT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -13.4% negative | -13.5% negative | PASS |  |  |
| RTX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $197.45 / RS 1.03 | $197.45 / RS 1.03 | PASS |  |  |
| RTX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| RTX | RS2 | Stock 52W Return and S&P 52W Return | +14.7% / +11.8% | +14.7% / +11.8% | PASS |  |  |
| RTX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RTX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RTX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| RTX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.7% clears | +14.7% clears | PASS |  |  |
| RY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $272.26 / RS 1.20 | $272.26 / RS 1.20 | PASS |  |  |
| RY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.20 | 1.20 | PASS |  |  |
| RY.TO | RS2 | Stock 52W Return and S&P 52W Return | +34.1% / +11.8% | +34.1% / +11.8% | PASS |  |  |
| RY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 66 | 66 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| RY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +34.1% clears | +34.1% clears | PASS |  |  |
| SMH | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $459.54 / RS 1.24 | $459.54 / RS 1.24 | PASS |  |  |
| SMH | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.24 | 1.24 | PASS |  |  |
| SMH | RS2 | Stock 52W Return and S&P 52W Return | +38.3% / +11.8% | +38.3% / +11.8% | PASS |  |  |
| SMH | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SMH | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 69 | 69 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SMH | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| SMH | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +38.3% clears | +38.3% clears | PASS |  |  |
| SO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $94.41 / RS 0.96 | $94.41 / RS 0.96 | PASS |  |  |
| SO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.96 | PASS |  |  |
| SO | RS2 | Stock 52W Return and S&P 52W Return | +7.5% / +11.8% | +7.5% / +11.8% | PASS |  |  |
| SO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| SO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +7.5% clears | +7.5% clears | PASS |  |  |
| SOXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $49.26 / RS 1.28 | $49.26 / RS 1.28 | PASS |  |  |
| SOXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.28 | 1.28 | PASS |  |  |
| SOXL | RS2 | Stock 52W Return and S&P 52W Return | +43.5% / +11.8% | +43.5% / +11.8% | PASS |  |  |
| SOXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 73 | 73 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| SOXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +43.5% clears | +43.5% clears | PASS |  |  |
| SOXL.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.43 / RS 1.17 | $12.43 / RS 1.17 | PASS |  |  |
| SOXL.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.17 | 1.17 | PASS |  |  |
| SOXL.NE | RS2 | Stock 52W Return and S&P 52W Return | +31.1% / +11.8% | +31.1% / +11.8% | PASS |  |  |
| SOXL.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +31.1% clears | +31.1% clears | PASS |  |  |
| SOXX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $141.85 / RS 1.38 | $141.85 / RS 1.38 | PASS |  |  |
| SOXX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.38 | 1.38 | PASS |  |  |
| SOXX | RS2 | Stock 52W Return and S&P 52W Return | +54.1% / +11.8% | +54.1% / +11.8% | PASS |  |  |
| SOXX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 80 | 80 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| SOXX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +54.1% clears | +54.1% clears | PASS |  |  |
| TSLA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $383.72 / RS 0.85 | $383.72 / RS 0.86 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| TSLA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.86 | PASS |  |  |
| TSLA | RS2 | Stock 52W Return and S&P 52W Return | -4.4% / +11.8% | -4.4% / +11.8% | PASS |  |  |
| TSLA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| TSLA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.4% negative | -4.4% negative | PASS |  |  |
| TSLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $10.00 / RS 0.58 | $10.00 / RS 0.58 | PASS |  |  |
| TSLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.58 | 0.58 | PASS |  |  |
| TSLL | RS2 | Stock 52W Return and S&P 52W Return | -35.0% / +11.8% | -35.0% / +11.8% | PASS |  |  |
| TSLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 17 | 17 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| TSLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -35.0% negative | -35.0% negative | PASS |  |  |
| TSM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $362.62 / RS 1.18 | $362.62 / RS 1.18 | PASS |  |  |
| TSM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.18 | 1.18 | PASS |  |  |
| TSM | RS2 | Stock 52W Return and S&P 52W Return | +31.9% / +11.8% | +31.9% / +11.8% | PASS |  |  |
| TSM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| TSM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +31.9% clears | +31.9% clears | PASS |  |  |
| UBOT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $15.07 / RS 0.61 | $15.07 / RS 0.61 | PASS |  |  |
| UBOT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.61 | 0.61 | PASS |  |  |
| UBOT | RS2 | Stock 52W Return and S&P 52W Return | -31.7% / +11.8% | -31.7% / +11.8% | PASS |  |  |
| UBOT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UBOT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 19 | 19 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UBOT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| UBOT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -31.7% negative | -31.7% negative | PASS |  |  |
| UFO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.09 / RS 1.07 | $39.09 / RS 1.07 | PASS |  |  |
| UFO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.07 | 1.07 | PASS |  |  |
| UFO | RS2 | Stock 52W Return and S&P 52W Return | +20.1% / +11.8% | +20.1% / +11.8% | PASS |  |  |
| UFO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UFO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UFO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| UFO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +20.1% clears | +20.1% clears | PASS |  |  |
| V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $416.77 / RS 1.15 | $416.77 / RS 1.15 | PASS |  |  |
| V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| V | RS2 | Stock 52W Return and S&P 52W Return | +28.9% / +11.8% | +28.9% / +11.8% | PASS |  |  |
| V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +28.9% clears | +28.9% clears | PASS |  |  |
| VFV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $186.20 / RS 1.02 | $186.20 / RS 1.02 | PASS |  |  |
| VFV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.02 | 1.02 | PASS |  |  |
| VFV.TO | RS2 | Stock 52W Return and S&P 52W Return | +14.4% / +11.8% | +14.4% / +11.8% | PASS |  |  |
| VFV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VFV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VFV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| VFV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.4% clears | +14.4% clears | PASS |  |  |
| VRT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $190.37 / RS 1.02 | $190.37 / RS 1.02 | PASS |  |  |
| VRT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.02 | 1.02 | PASS |  |  |
| VRT | RS2 | Stock 52W Return and S&P 52W Return | +14.4% / +11.8% | +14.4% / +11.8% | PASS |  |  |
| VRT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VRT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VRT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| VRT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +14.4% clears | +14.4% clears | PASS |  |  |
| WELL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $247.25 / RS 1.13 | $247.25 / RS 1.13 | PASS |  |  |
| WELL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.13 | 1.13 | PASS |  |  |
| WELL | RS2 | Stock 52W Return and S&P 52W Return | +26.5% / +11.8% | +26.5% / +11.8% | PASS |  |  |
| WELL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WELL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 60 | 60 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WELL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| WELL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +26.5% clears | +26.5% clears | PASS |  |  |
| WMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $127.52 / RS 1.12 | $127.52 / RS 1.12 | PASS |  |  |
| WMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.12 | 1.12 | PASS |  |  |
| WMT | RS2 | Stock 52W Return and S&P 52W Return | +24.9% / +11.8% | +24.9% / +11.8% | PASS |  |  |
| WMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 59 | 59 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| WMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +24.9% clears | +24.9% clears | PASS |  |  |
| XCHP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $105.84 / RS 1.41 | $105.84 / RS 1.41 | PASS |  |  |
| XCHP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.41 | 1.41 | PASS |  |  |
| XCHP.TO | RS2 | Stock 52W Return and S&P 52W Return | +57.4% / +11.8% | +57.4% / +11.8% | PASS |  |  |
| XCHP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XCHP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 83 | 83 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XCHP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| XCHP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +57.4% clears | +57.4% clears | PASS |  |  |
| XDRV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $38.84 / RS 0.85 | $38.84 / RS 0.85 | PASS |  |  |
| XDRV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| XDRV.TO | RS2 | Stock 52W Return and S&P 52W Return | -4.5% / +11.8% | -4.5% / +11.8% | PASS |  |  |
| XDRV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XDRV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XDRV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| XDRV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.5% negative | -4.5% negative | PASS |  |  |
| XEQT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $44.01 / RS 1.03 | $44.01 / RS 1.03 | PASS |  |  |
| XEQT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| XEQT.TO | RS2 | Stock 52W Return and S&P 52W Return | +15.2% / +11.8% | +15.2% / +11.8% | PASS |  |  |
| XEQT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XEQT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XEQT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| XEQT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +15.2% clears | +15.2% clears | PASS |  |  |
| XETM.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $57.76 / RS 0.61 | $57.76 / RS 0.61 | PASS |  |  |
| XETM.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.61 | 0.61 | PASS |  |  |
| XETM.TO | RS2 | Stock 52W Return and S&P 52W Return | -31.4% / +11.8% | -31.5% / +11.8% | PASS |  |  |
| XETM.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 19 | 19 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XETM.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| XETM.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -31.4% negative | -31.5% negative | PASS |  |  |
| XGD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $48.44 / RS 0.95 | $48.44 / RS 0.95 | PASS |  |  |
| XGD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.95 | PASS |  |  |
| XGD.TO | RS2 | Stock 52W Return and S&P 52W Return | +6.0% / +11.8% | +6.0% / +11.8% | PASS |  |  |
| XGD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XGD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XGD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| XGD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.0% clears | +6.0% clears | PASS |  |  |
| XOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $160.58 / RS 1.21 | $160.58 / RS 1.21 | PASS |  |  |
| XOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.21 | 1.21 | PASS |  |  |
| XOM | RS2 | Stock 52W Return and S&P 52W Return | +34.9% / +11.8% | +34.9% / +11.8% | PASS |  |  |
| XOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| XOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +34.9% clears | +34.9% clears | PASS |  |  |
| AAPL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| AAPU | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| AAPU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| AAPU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $47.65 – $48.94 · price is inside this zone · turned here 4× | $47.65 – $48.94 · 0.0% · 4× | PASS |  |  |
| AAPU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.99 | 1.9901 | PASS |  |  |
| AAPU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AAPU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| AAPU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| AAPU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $48.59 | $48.59 | PASS |  |  |
| AAPU | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 48.59, zone 47.65-48.94 | inside the zone | PASS |  |  |
| AAPU | TS1c | S5: the Buy on the bar = the Buy in the box | $48.59 | $48.59 | PASS |  |  |
| AAPU | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 48.59 vs last close 48.59 | Buy <= last close | PASS |  |  |
| AAPU | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AAPU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $44.61 -8.2% | $44.61 -8.2% | PASS |  |  |
| AAPU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPU | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| AAPU | TS6 | Risk $ (and reward $ per share) | Risk $3.98 a share | Risk $3.98 | PASS |  |  |
| ABBV | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| AIPO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $23.12 – $23.65 · 1.9% above · turned here 3× | $23.12 – $23.65 · 1.9% · 3× | PASS |  |  |
| AIPO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AIPO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $22.08 · 2.7% below · turned here 1× | $22.08 · 2.7% · 1× | PASS |  |  |
| AIPO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.092 | 1.0922 | PASS |  |  |
| AIPO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AIPO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| AIPO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| AIPO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $22.08 | $22.08 | PASS |  |  |
| AIPO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 22.08, nearest zone high 22.08 | equal | PASS |  |  |
| AIPO | TS1c | S5: the Buy on the bar = the Buy in the box | $22.08 | $22.08 | PASS |  |  |
| AIPO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| AIPO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $19.90 -9.9% | $19.90 -9.9% | PASS |  |  |
| AIPO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AIPO | TS4 | Target = nearest resistance edge and its % from the buy | $23.12 +4.7% | $23.12 +4.7% | PASS |  |  |
| AIPO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| AIPO | TS6 | Risk $ (and reward $ per share) | Risk $2.18 to make $1.04 a share | Risk $2.18 to make $1.04 | PASS |  |  |
| ALAB | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| AMD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $546.44 – $584.73 · 3.1% above · turned here 6× | $546.44 – $584.73 · 3.1% · 6× | PASS |  |  |
| AMD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $491.12 – $530.13 · 0.0% below · turned here 6× | $491.12 – $530.13 · 0.0% · 6× | PASS |  |  |
| AMD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 40.3313 | 40.3313 | PASS |  |  |
| AMD | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AMD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AMD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AMD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $530.13 | $530.13 | PASS |  |  |
| AMD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 530.13, nearest zone high 530.13 | equal | PASS |  |  |
| AMD | TS1c | S5: the Buy on the bar = the Buy in the box | $530.13 | $530.13 | PASS |  |  |
| AMD | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.0% below | 0.0% below | PASS |  |  |
| AMD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $449.47 -15.2% | $449.47 -15.2% | PASS |  |  |
| AMD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD | TS4 | Target = nearest resistance edge and its % from the buy | $546.44 +3.1% | $546.44 +3.1% | PASS |  |  |
| AMD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AMD | TS6 | Risk $ (and reward $ per share) | Risk $80.66 to make $16.31 a share | Risk $80.66 to make $16.31 | PASS |  |  |
| AMZN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $274.75 – $278.56 · 2.6% above · turned here 3× | $274.75 – $278.56 · 2.6% · 3× | PASS |  |  |
| AMZN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $265.34 – $267.56 · 0.1% below · turned here 2× | $265.34 – $267.56 · 0.1% · 2× | PASS |  |  |
| AMZN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.0203 | 9.0203 | PASS |  |  |
| AMZN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| AMZN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AMZN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AMZN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $267.56 | $267.56 | PASS |  |  |
| AMZN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 267.56, nearest zone high 267.56 | equal | PASS |  |  |
| AMZN | TS1c | S5: the Buy on the bar = the Buy in the box | $267.56 | $267.56 | PASS |  |  |
| AMZN | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.1% below | 0.1% below | PASS |  |  |
| AMZN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $249.52 -6.7% | $249.52 -6.7% | PASS |  |  |
| AMZN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZN | TS4 | Target = nearest resistance edge and its % from the buy | $274.75 +2.7% | $274.75 +2.7% | PASS |  |  |
| AMZN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| AMZN | TS6 | Risk $ (and reward $ per share) | Risk $18.04 to make $7.19 a share | Risk $18.04 to make $7.19 | PASS |  |  |
| AMZU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $39.72 – $40.25 · 4.8% above · turned here 3× | $39.72 – $40.25 · 4.8% · 3× | PASS |  |  |
| AMZU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $37.01 – $39.05 · price is inside this zone · turned here 7× | $37.01 – $39.05 · 0.0% · 7× | PASS |  |  |
| AMZU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4747 | 2.4746 | PASS |  |  |
| AMZU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AMZU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AMZU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AMZU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $37.91 | $37.91 | PASS |  |  |
| AMZU | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 37.91, zone 37.01-39.05 | inside the zone | PASS |  |  |
| AMZU | TS1c | S5: the Buy on the bar = the Buy in the box | $37.91 | $37.91 | PASS |  |  |
| AMZU | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 37.91 vs last close 37.91 | Buy <= last close | PASS |  |  |
| AMZU | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AMZU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $32.96 -13.1% | $32.96 -13.1% | PASS |  |  |
| AMZU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZU | TS4 | Target = nearest resistance edge and its % from the buy | $39.72 +4.8% | $39.72 +4.8% | PASS |  |  |
| AMZU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| AMZU | TS6 | Risk $ (and reward $ per share) | Risk $4.95 to make $1.81 a share | Risk $4.95 to make $1.81 | PASS |  |  |
| ANET.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $35.91 – $36.75 · 3.6% above · turned here 2× | $35.91 – $36.75 · 3.6% · 2× | PASS |  |  |
| ANET.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $34.01 – $34.05 · 1.8% below · turned here 2× | $34.01 – $34.05 · 1.8% · 2× | PASS |  |  |
| ANET.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9932 | 1.9932 | PASS |  |  |
| ANET.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ANET.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ANET.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ANET.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $34.05 | $34.05 | PASS |  |  |
| ANET.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 34.05, nearest zone high 34.05 | equal | PASS |  |  |
| ANET.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $34.05 | $34.05 | PASS |  |  |
| ANET.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% below | 1.8% below | PASS |  |  |
| ANET.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $30.06 -11.7% | $30.06 -11.7% | PASS |  |  |
| ANET.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ANET.TO | TS4 | Target = nearest resistance edge and its % from the buy | $35.91 +5.5% | $35.91 +5.5% | PASS |  |  |
| ANET.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| ANET.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.99 to make $1.86 a share | Risk $3.99 to make $1.86 | PASS |  |  |
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
| ASTL.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $6.99 – $7.02 · 0.7% above · turned here 3× | $6.99 – $7.02 · 0.7% · 3× | PASS |  |  |
| ASTL.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ASTL.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $6.31 – $6.62 · 4.6% below · turned here 11× | $6.31 – $6.62 · 4.6% · 11× | PASS |  |  |
| ASTL.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4239 | 0.4244 | PASS |  |  |
| ASTL.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ASTL.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ASTL.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ASTL.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $6.62 | $6.62 | PASS |  |  |
| ASTL.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 6.62, nearest zone high 6.62 | equal | PASS |  |  |
| ASTL.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $6.62 | $6.62 | PASS |  |  |
| ASTL.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.6% below | 4.6% below | PASS |  |  |
| ASTL.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $5.77 -12.8% | $5.77 -12.8% | PASS |  |  |
| ASTL.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASTL.TO | TS4 | Target = nearest resistance edge and its % from the buy | $6.99 +5.6% | $6.99 +5.6% | PASS |  |  |
| ASTL.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| ASTL.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.85 to make $0.37 a share | Risk $0.85 to make $0.37 | PASS |  |  |
| ATD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $84.02 · 1.2% above · turned here 1× | $84.02 · 1.2% · 1× | PASS |  |  |
| ATD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ATD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $80.76 – $81.40 · 1.9% below · turned here 4× | $80.76 – $81.40 · 1.9% · 4× | PASS |  |  |
| ATD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6673 | 1.6673 | PASS |  |  |
| ATD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ATD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| ATD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| ATD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $81.40 | $81.40 | PASS |  |  |
| ATD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 81.4, nearest zone high 81.4 | equal | PASS |  |  |
| ATD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $81.40 | $81.40 | PASS |  |  |
| ATD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.9% below | 1.9% below | PASS |  |  |
| ATD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $78.07 -4.1% | $78.07 -4.1% | PASS |  |  |
| ATD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ATD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $84.02 +3.2% | $84.02 +3.2% | PASS |  |  |
| ATD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| ATD.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.33 to make $2.62 a share | Risk $3.33 to make $2.62 | PASS |  |  |
| AVGC | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $21.22 · 7.8% above · turned here 1× | $21.22 · 7.8% · 1× | PASS |  |  |
| AVGC | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $19.34 – $20.42 · price is inside this zone · turned here 4× | $19.34 – $20.42 · 0.0% · 4× | PASS |  |  |
| AVGC | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6663 | 1.6663 | PASS |  |  |
| AVGC | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AVGC | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| AVGC | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| AVGC | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $19.68 | $19.68 | PASS |  |  |
| AVGC | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 19.68, zone 19.34-20.42 | inside the zone | PASS |  |  |
| AVGC | TS1c | S5: the Buy on the bar = the Buy in the box | $19.68 | $19.68 | PASS |  |  |
| AVGC | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 19.68 vs last close 19.68 | Buy <= last close | PASS |  |  |
| AVGC | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AVGC | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $16.35 -16.9% | $16.35 -16.9% | PASS |  |  |
| AVGC | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGC | TS4 | Target = nearest resistance edge and its % from the buy | $21.22 +7.8% | $21.22 +7.8% | PASS |  |  |
| AVGC | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| AVGC | TS6 | Risk $ (and reward $ per share) | Risk $3.33 to make $1.54 a share | Risk $3.33 to make $1.54 | PASS |  |  |
| AVGO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| AVGO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $13.51 – $14.10 · 4.4% above · turned here 9× | $13.51 – $14.10 · 4.4% · 9× | PASS |  |  |
| AVGO.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.72 – $13.34 · price is inside this zone · turned here 7× | $12.72 – $13.34 · 0.0% · 7× | PASS |  |  |
| AVGO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6504 | 0.6503 | PASS |  |  |
| AVGO.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AVGO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AVGO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AVGO.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $12.94 | $12.94 | PASS |  |  |
| AVGO.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 12.94, zone 12.72-13.34 | inside the zone | PASS |  |  |
| AVGO.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $12.94 | $12.94 | PASS |  |  |
| AVGO.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 12.94 vs last close 12.94 | Buy <= last close | PASS |  |  |
| AVGO.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AVGO.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $11.64 -10.1% | $11.64 -10.1% | PASS |  |  |
| AVGO.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO.TO | TS4 | Target = nearest resistance edge and its % from the buy | $13.51 +4.4% | $13.51 +4.4% | PASS |  |  |
| AVGO.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| AVGO.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.30 to make $0.57 a share | Risk $1.30 to make $0.57 | PASS |  |  |
| BDT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $76.69 – $78.33 · 5.0% above · turned here 3× | $76.69 – $78.33 · 5.0% · 3× | PASS |  |  |
| BDT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| BDT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $71.25 · 2.5% below · turned here 1× | $71.25 · 2.5% · 1× | PASS |  |  |
| BDT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.0612 | 4.0613 | PASS |  |  |
| BDT.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BDT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| BDT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $71.25 | $71.25 | PASS |  |  |
| BDT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 71.25, nearest zone high 71.25 | equal | PASS |  |  |
| BDT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $71.25 | $71.25 | PASS |  |  |
| BDT.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.5% below | 2.5% below | PASS |  |  |
| BDT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $63.13 -11.4% | $63.13 -11.4% | PASS |  |  |
| BDT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BDT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $76.69 +7.6% | $76.69 +7.6% | PASS |  |  |
| BDT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| BDT.TO | TS6 | Risk $ (and reward $ per share) | Risk $8.12 to make $5.44 a share | Risk $8.12 to make $5.44 | PASS |  |  |
| BOTZ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.53 · 2.8% above · turned here 1× | $30.53 · 2.8% · 1× | PASS |  |  |
| BOTZ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| BOTZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| BOTZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7692 | 0.7695 | PASS |  |  |
| BOTZ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| BOTZ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| BOTZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| BRK-B | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| BRK-B | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 7 of 8 trend checks pass | No resistance within 30% above · 7 of 8 trend checks pass | PASS |  |  |
| BRK-B | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $549.96 · 4.3% below · turned here 1× | $549.96 · 4.3% · 1× | PASS |  |  |
| BRK-B | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.6387 | 9.6387 | PASS |  |  |
| BRK-B | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BRK-B | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| BRK-B | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| BRK-B | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 549.96, nearest zone high 549.96 | equal | PASS |  |  |
| BRK-B | TS1c | S5: the Buy on the bar = the Buy in the box | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.3% below | 4.3% below | PASS |  |  |
| BRK-B | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $530.68 -3.5% | $530.68 -3.5% | PASS |  |  |
| BRK-B | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRK-B | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| BRK-B | TS6 | Risk $ (and reward $ per share) | Risk $19.28 a share | Risk $19.28 | PASS |  |  |
| BRKU | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| BRKU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| BRKU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $26.69 · 7.5% below · turned here 1× | $26.69 · 7.5% · 1× | PASS |  |  |
| BRKU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9182 | 0.9181 | PASS |  |  |
| BRKU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| BRKU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| BRKU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| BRKU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $26.69 | $26.69 | PASS |  |  |
| BRKU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 26.69, nearest zone high 26.69 | equal | PASS |  |  |
| BRKU | TS1c | S5: the Buy on the bar = the Buy in the box | $26.69 | $26.69 | PASS |  |  |
| BRKU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.5% below | 7.5% below | PASS |  |  |
| BRKU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $24.85 -6.9% | $24.85 -6.9% | PASS |  |  |
| BRKU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRKU | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| BRKU | TS6 | Risk $ (and reward $ per share) | Risk $1.84 a share | Risk $1.84 | PASS |  |  |
| CAMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $101.39 · 3.0% above · turned here 1× | $101.39 · 3.0% · 1× | PASS |  |  |
| CAMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CAMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $89.13 – $91.91 · 6.6% below · turned here 2× | $89.13 – $91.91 · 6.6% · 2× | PASS |  |  |
| CAMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.0305 | 8.0304 | PASS |  |  |
| CAMT | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CAMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CAMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CAMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $91.91 | $91.91 | PASS |  |  |
| CAMT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 91.91, nearest zone high 91.91 | equal | PASS |  |  |
| CAMT | TS1c | S5: the Buy on the bar = the Buy in the box | $91.91 | $91.91 | PASS |  |  |
| CAMT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.6% below | 6.6% below | PASS |  |  |
| CAMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $75.85 -17.5% | $75.85 -17.5% | PASS |  |  |
| CAMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CAMT | TS4 | Target = nearest resistance edge and its % from the buy | $101.39 +10.3% | $101.39 +10.3% | PASS |  |  |
| CAMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| CAMT | TS6 | Risk $ (and reward $ per share) | Risk $16.06 to make $9.48 a share | Risk $16.06 to make $9.48 | PASS |  |  |
| CARS.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.90 · 5.1% above · turned here 1× | $20.90 · 5.1% · 1× | PASS |  |  |
| CARS.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CARS.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CARS.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4773 | 0.4762 | PASS |  |  |
| CARS.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CARS.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CARS.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CCO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $92.52 · 3.5% above · turned here 1× | $92.52 · 3.5% · 1× | PASS |  |  |
| CCO.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CCO.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CCO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.9224 | 4.9224 | PASS |  |  |
| CCO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| CCO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| CCO.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CGY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $84.58 – $87.00 · 0.5% above · turned here 6× | $84.58 – $87.00 · 0.5% · 6× | PASS |  |  |
| CGY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CGY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $83.01 · 1.3% below · turned here 1× | $83.01 · 1.3% · 1× | PASS |  |  |
| CGY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5117 | 2.5117 | PASS |  |  |
| CGY.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CGY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CGY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CGY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $83.01 | $83.01 | PASS |  |  |
| CGY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 83.01, nearest zone high 83.01 | equal | PASS |  |  |
| CGY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $83.01 | $83.01 | PASS |  |  |
| CGY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.3% below | 1.3% below | PASS |  |  |
| CGY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $77.99 -6.1% | $77.99 -6.1% | PASS |  |  |
| CGY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CGY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $84.58 +1.9% | $84.58 +1.9% | PASS |  |  |
| CGY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CGY.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.02 to make $1.57 a share | Risk $5.02 to make $1.57 | PASS |  |  |
| CNQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $65.78 – $67.12 · 0.8% above · turned here 6× | $65.78 – $67.12 · 0.8% · 6× | PASS |  |  |
| CNQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $64.61 · 1.0% below · turned here 1× | $64.61 · 1.0% · 1× | PASS |  |  |
| CNQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0544 | 2.0544 | PASS |  |  |
| CNQ.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CNQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CNQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CNQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $64.61 | $64.61 | PASS |  |  |
| CNQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 64.61, nearest zone high 64.61 | equal | PASS |  |  |
| CNQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $64.61 | $64.61 | PASS |  |  |
| CNQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.0% below | 1.0% below | PASS |  |  |
| CNQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $60.50 -6.4% | $60.50 -6.4% | PASS |  |  |
| CNQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $65.78 +1.8% | $65.78 +1.8% | PASS |  |  |
| CNQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CNQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.11 to make $1.17 a share | Risk $4.11 to make $1.17 | PASS |  |  |
| CNR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $184.26 · 2.7% above · turned here 1× | $184.26 · 2.7% · 1× | PASS |  |  |
| CNR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $178.49 · 0.5% below · turned here 1× | $178.49 · 0.5% · 1× | PASS |  |  |
| CNR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.2642 | 3.2642 | PASS |  |  |
| CNR.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CNR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| CNR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| CNR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $178.49 | $178.49 | PASS |  |  |
| CNR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 178.49, nearest zone high 178.49 | equal | PASS |  |  |
| CNR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $178.49 | $178.49 | PASS |  |  |
| CNR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.5% below | 0.5% below | PASS |  |  |
| CNR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $171.96 -3.7% | $171.96 -3.7% | PASS |  |  |
| CNR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $184.26 +3.2% | $184.26 +3.2% | PASS |  |  |
| CNR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| CNR.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.53 to make $5.77 a share | Risk $6.53 to make $5.77 | PASS |  |  |
| COP | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $135.87 – $135.88 · 1.1% above · turned here 2× | $135.87 – $135.88 · 1.1% · 2× | PASS |  |  |
| COP | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COP | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $131.12 · 2.4% below · turned here 1× | $131.12 · 2.4% · 1× | PASS |  |  |
| COP | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.082 | 4.0818 | PASS |  |  |
| COP | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COP | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| COP | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| COP | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $131.12 | $131.12 | PASS |  |  |
| COP | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 131.12, nearest zone high 131.12 | equal | PASS |  |  |
| COP | TS1c | S5: the Buy on the bar = the Buy in the box | $131.12 | $131.12 | PASS |  |  |
| COP | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.4% below | 2.4% below | PASS |  |  |
| COP | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $122.96 -6.2% | $122.96 -6.2% | PASS |  |  |
| COP | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COP | TS4 | Target = nearest resistance edge and its % from the buy | $135.87 +3.6% | $135.87 +3.6% | PASS |  |  |
| COP | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| COP | TS6 | Risk $ (and reward $ per share) | Risk $8.16 to make $4.75 a share | Risk $8.16 to make $4.75 | PASS |  |  |
| COPP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $46.40 · 7.7% above · turned here 1× | $46.40 · 7.7% · 1× | PASS |  |  |
| COPP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COPP.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $42.17 · 2.1% below · turned here 1× | $42.17 · 2.1% · 1× | PASS |  |  |
| COPP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1812 | 2.1811 | PASS |  |  |
| COPP.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COPP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| COPP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| COPP.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $42.17 | $42.17 | PASS |  |  |
| COPP.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 42.17, nearest zone high 42.17 | equal | PASS |  |  |
| COPP.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $42.17 | $42.17 | PASS |  |  |
| COPP.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| COPP.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $37.81 -10.3% | $37.81 -10.3% | PASS |  |  |
| COPP.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COPP.TO | TS4 | Target = nearest resistance edge and its % from the buy | $46.40 +10.0% | $46.40 +10.0% | PASS |  |  |
| COPP.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.0 : 1 | 1.0 : 1 | PASS |  |  |
| COPP.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.36 to make $4.23 a share | Risk $4.36 to make $4.23 | PASS |  |  |
| COPX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $68.26 · 11.6% above · turned here 1× | $68.26 · 11.6% · 1× | PASS |  |  |
| COPX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 0 of 8 trend checks pass · ADX 27.0 | 0 of 8 trend checks pass · ADX 27.0 | PASS |  |  |
| COPX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $55.44 · 9.4% below · turned here 1× | $55.44 · 9.4% · 1× | PASS |  |  |
| COPX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.9212 | 2.9212 | PASS |  |  |
| COPX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COPX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| COPX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| COPX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $55.44 | $55.44 | PASS |  |  |
| COPX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 55.44, nearest zone high 55.44 | equal | PASS |  |  |
| COPX | TS1c | S5: the Buy on the bar = the Buy in the box | $55.44 | $55.44 | PASS |  |  |
| COPX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 9.4% below | 9.4% below | PASS |  |  |
| COPX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $49.60 -10.5% | $49.60 -10.5% | PASS |  |  |
| COPX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COPX | TS4 | Target = nearest resistance edge and its % from the buy | $68.26 +23.1% | $68.26 +23.1% | PASS |  |  |
| COPX | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.2 : 1 | 2.2 : 1 | PASS |  |  |
| COPX | TS6 | Risk $ (and reward $ per share) | Risk $5.84 to make $12.82 a share | Risk $5.84 to make $12.82 | PASS |  |  |
| COPZ | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| COPZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| COPZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8283 | 0.8283 | PASS |  |  |
| COPZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| COST | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 2.4% below $1,123.67 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| COST | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| COST | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 6 of 8 trend checks pass | No resistance within 30% above · 6 of 8 trend checks pass | PASS |  |  |
| COST | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,096.50 · 0.0% below · turned here 1× | $1,096.50 · 0.0% · 1× | PASS |  |  |
| COST | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 18.686 | 18.6858 | PASS |  |  |
| COST | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COST | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| COST | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| COST | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,096.50 | $1,096.50 | PASS |  |  |
| COST | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1096.5, nearest zone high 1096.5 | equal | PASS |  |  |
| COST | TS1c | S5: the Buy on the bar = the Buy in the box | $1,096.50 | $1,096.50 | PASS |  |  |
| COST | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.0% below | 0.0% below | PASS |  |  |
| COST | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $1,059.13 -3.4% | $1,059.13 -3.4% | PASS |  |  |
| COST | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COST | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 2.4% below the high $1,123.67 | PASS |  |  |
| COST | TS6 | Risk $ (and reward $ per share) | Risk $37.37 a share | Risk $37.37 | PASS |  |  |
| COTG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $17.80 · 7.7% above · turned here 1× | $17.80 · 7.7% · 1× | PASS |  |  |
| COTG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Weakening trend — testing support | Weakening trend — testing support | PASS |  |  |
| COTG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.07 – $16.11 · 2.5% below · turned here 2× | $16.07 – $16.11 · 2.5% · 2× | PASS |  |  |
| COTG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5146 | 0.5144 | PASS |  |  |
| COTG | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| COTG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| COTG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| COTG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $16.11 | $16.11 | PASS |  |  |
| COTG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 16.11, nearest zone high 16.11 | equal | PASS |  |  |
| COTG | TS1c | S5: the Buy on the bar = the Buy in the box | $16.11 | $16.11 | PASS |  |  |
| COTG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.5% below | 2.5% below | PASS |  |  |
| COTG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $15.08 -6.4% | $15.08 -6.4% | PASS |  |  |
| COTG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COTG | TS4 | Target = nearest resistance edge and its % from the buy | $17.80 +10.5% | $17.80 +10.5% | PASS |  |  |
| COTG | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.6 : 1 | 1.6 : 1 | PASS |  |  |
| COTG | TS6 | Risk $ (and reward $ per share) | Risk $1.03 to make $1.69 a share | Risk $1.03 to make $1.69 | PASS |  |  |
| CSU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3,341.06 – $3,430.89 · 0.5% above · turned here 5× | $3,341.06 – $3,430.89 · 0.5% · 5× | PASS |  |  |
| CSU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CSU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $3,118.74 – $3,227.61 · 2.9% below · turned here 6× | $3,118.74 – $3,227.61 · 2.9% · 6× | PASS |  |  |
| CSU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 118.3824 | 118.3824 | PASS |  |  |
| CSU.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CSU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| CSU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| CSU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $3,227.61 | $3,227.61 | PASS |  |  |
| CSU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 3227.61, nearest zone high 3227.61 | equal | PASS |  |  |
| CSU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $3,227.61 | $3,227.61 | PASS |  |  |
| CSU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.9% below | 2.9% below | PASS |  |  |
| CSU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $2,990.85 -7.3% | $2,990.85 -7.3% | PASS |  |  |
| CSU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CSU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $3,341.06 +3.5% | $3,341.06 +3.5% | PASS |  |  |
| CSU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| CSU.TO | TS6 | Risk $ (and reward $ per share) | Risk $236.76 to make $113.45 a share | Risk $236.76 to make $113.45 | PASS |  |  |
| CVX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $206.01 · 0.1% above · turned here 1× | $206.01 · 0.1% · 1× | PASS |  |  |
| CVX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CVX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $197.55 – $201.96 · 1.9% below · turned here 6× | $197.55 – $201.96 · 1.9% · 6× | PASS |  |  |
| CVX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.2568 | 5.2576 | PASS |  |  |
| CVX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| CVX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| CVX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| CVX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $201.96 | $201.96 | PASS |  |  |
| CVX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 201.96, nearest zone high 201.96 | equal | PASS |  |  |
| CVX | TS1c | S5: the Buy on the bar = the Buy in the box | $201.96 | $201.96 | PASS |  |  |
| CVX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.9% below | 1.9% below | PASS |  |  |
| CVX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $191.45 -5.2% | $191.45 -5.2% | PASS |  |  |
| CVX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CVX | TS4 | Target = nearest resistance edge and its % from the buy | $206.01 +2.0% | $206.01 +2.0% | PASS |  |  |
| CVX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| CVX | TS6 | Risk $ (and reward $ per share) | Risk $10.51 to make $4.05 a share | Risk $10.51 to make $4.05 | PASS |  |  |
| DRAL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| DRAL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $4.06 · 2.2% below · turned here 1× | $4.06 · 2.2% · 1× | PASS |  |  |
| DRAL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7746 | 0.7745 | PASS |  |  |
| DRAL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| DRAL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| DRAL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| DRAL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $4.06 | $4.06 | PASS |  |  |
| DRAL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 4.06, nearest zone high 4.06 | equal | PASS |  |  |
| DRAL | TS1c | S5: the Buy on the bar = the Buy in the box | $4.06 | $4.06 | PASS |  |  |
| DRAL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.2% below | 2.2% below | PASS |  |  |
| DRAL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $2.51 -38.2% | $2.51 -38.2% | PASS |  |  |
| DRAL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRAL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| DRAL | TS6 | Risk $ (and reward $ per share) | Risk $1.55 a share | Risk $1.55 | PASS |  |  |
| DRAM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $44.40 – $46.43 · 13.4% above · turned here 3× | $44.40 – $46.43 · 13.4% · 3× | PASS |  |  |
| DRAM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $37.01 · 5.5% below · turned here 1× | $37.01 · 5.5% · 1× | PASS |  |  |
| DRAM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.0419 | 3.0419 | PASS |  |  |
| DRAM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| DRAM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| DRAM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| DRAM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $37.01 | $37.01 | PASS |  |  |
| DRAM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 37.01, nearest zone high 37.01 | equal | PASS |  |  |
| DRAM | TS1c | S5: the Buy on the bar = the Buy in the box | $37.01 | $37.01 | PASS |  |  |
| DRAM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.5% below | 5.5% below | PASS |  |  |
| DRAM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $30.93 -16.4% | $30.93 -16.4% | PASS |  |  |
| DRAM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRAM | TS4 | Target = nearest resistance edge and its % from the buy | $44.40 +20.0% | $44.40 +20.0% | PASS |  |  |
| DRAM | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| DRAM | TS6 | Risk $ (and reward $ per share) | Risk $6.08 to make $7.39 a share | Risk $6.08 to make $7.39 | PASS |  |  |
| DRIV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $26.87 · 0.2% above · turned here 1× | $26.87 · 0.2% · 1× | PASS |  |  |
| DRIV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| DRIV | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| DRIV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7591 | 0.7601 | PASS |  |  |
| DRIV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| DRIV | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| DUK | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $130.38 – $131.87 · 0.3% above · turned here 4× | $130.38 – $131.87 · 0.3% · 4× | PASS |  |  |
| DUK | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| DUK | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $129.28 · 0.6% below · turned here 1× | $129.28 · 0.6% · 1× | PASS |  |  |
| DUK | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1298 | 2.1293 | PASS |  |  |
| DUK | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| DUK | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| DUK | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| DUK | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $129.28 | $129.28 | PASS |  |  |
| DUK | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 129.28, nearest zone high 129.28 | equal | PASS |  |  |
| DUK | TS1c | S5: the Buy on the bar = the Buy in the box | $129.28 | $129.28 | PASS |  |  |
| DUK | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.6% below | 0.6% below | PASS |  |  |
| DUK | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $125.02 -3.3% | $125.02 -3.3% | PASS |  |  |
| DUK | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DUK | TS4 | Target = nearest resistance edge and its % from the buy | $130.38 +0.9% | $130.38 +0.9% | PASS |  |  |
| DUK | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| DUK | TS6 | Risk $ (and reward $ per share) | Risk $4.26 to make $1.10 a share | Risk $4.26 to make $1.10 | PASS |  |  |
| ELIL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| ELIL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| ELIL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.02 – $35.86 · 6.3% below · turned here 2× | $35.02 – $35.86 · 6.3% · 2× | PASS |  |  |
| ELIL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2299 | 2.2307 | PASS |  |  |
| ELIL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ELIL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| ELIL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| ELIL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 35.86, nearest zone high 35.86 | equal | PASS |  |  |
| ELIL | TS1c | S5: the Buy on the bar = the Buy in the box | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.3% below | 6.3% below | PASS |  |  |
| ELIL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.40 -12.4% | $31.40 -12.4% | PASS |  |  |
| ELIL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ELIL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| ELIL | TS6 | Risk $ (and reward $ per share) | Risk $4.46 a share | Risk $4.46 | PASS |  |  |
| EQIX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $1,061.09 – $1,093.83 · 2.4% above · turned here 6× | $1,061.09 – $1,093.83 · 2.4% · 6× | PASS |  |  |
| EQIX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| EQIX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,021.66 – $1,048.61 · price is inside this zone · turned here 7× | $1,021.66 – $1,048.61 · 0.0% · 7× | PASS |  |  |
| EQIX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 33.0268 | 33.0267 | PASS |  |  |
| EQIX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| EQIX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| EQIX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| EQIX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,036.50 | $1,036.50 | PASS |  |  |
| EQIX | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 1036.5, zone 1021.66-1048.61 | inside the zone | PASS |  |  |
| EQIX | TS1c | S5: the Buy on the bar = the Buy in the box | $1,036.50 | $1,036.50 | PASS |  |  |
| EQIX | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 1036.5 vs last close 1036.5 | Buy <= last close | PASS |  |  |
| EQIX | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| EQIX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $970.45 -6.4% | $970.45 -6.4% | PASS |  |  |
| EQIX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| EQIX | TS4 | Target = nearest resistance edge and its % from the buy | $1,061.09 +2.4% | $1,061.09 +2.4% | PASS |  |  |
| EQIX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| EQIX | TS6 | Risk $ (and reward $ per share) | Risk $66.05 to make $24.59 a share | Risk $66.05 to make $24.59 | PASS |  |  |
| ETN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $355.77 – $372.98 · 5.2% above · turned here 6× | $355.77 – $372.98 · 5.2% · 6× | PASS |  |  |
| ETN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ETN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $334.43 – $350.37 · price is inside this zone · turned here 4× | $334.43 – $350.37 · 0.0% · 4× | PASS |  |  |
| ETN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.4723 | 17.4719 | PASS |  |  |
| ETN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| ETN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ETN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ETN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $338.34 | $338.34 | PASS |  |  |
| ETN | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 338.34, zone 334.43-350.37 | inside the zone | PASS |  |  |
| ETN | TS1c | S5: the Buy on the bar = the Buy in the box | $338.34 | $338.34 | PASS |  |  |
| ETN | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 338.34 vs last close 338.34 | Buy <= last close | PASS |  |  |
| ETN | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| ETN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $303.40 -10.3% | $303.40 -10.3% | PASS |  |  |
| ETN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ETN | TS4 | Target = nearest resistance edge and its % from the buy | $355.77 +5.2% | $355.77 +5.2% | PASS |  |  |
| ETN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| ETN | TS6 | Risk $ (and reward $ per share) | Risk $34.94 to make $17.43 a share | Risk $34.94 to make $17.43 | PASS |  |  |
| FCX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $55.12 – $58.06 · 7.1% above · turned here 8× | $55.12 – $58.06 · 7.1% · 8× | PASS |  |  |
| FCX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| FCX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $50.19 – $50.45 · 1.9% below · turned here 2× | $50.19 – $50.45 · 1.9% · 2× | PASS |  |  |
| FCX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.9667 | 2.9664 | PASS |  |  |
| FCX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| FCX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| FCX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| FCX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $50.45 | $50.45 | PASS |  |  |
| FCX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 50.45, nearest zone high 50.45 | equal | PASS |  |  |
| FCX | TS1c | S5: the Buy on the bar = the Buy in the box | $50.45 | $50.45 | PASS |  |  |
| FCX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.9% below | 1.9% below | PASS |  |  |
| FCX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $44.52 -11.8% | $44.52 -11.8% | PASS |  |  |
| FCX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FCX | TS4 | Target = nearest resistance edge and its % from the buy | $55.12 +9.3% | $55.12 +9.3% | PASS |  |  |
| FCX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| FCX | TS6 | Risk $ (and reward $ per share) | Risk $5.93 to make $4.67 a share | Risk $5.93 to make $4.67 | PASS |  |  |
| FINN.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $32.88 · 2.8% above · turned here 1× | $32.88 · 2.8% · 1× | PASS |  |  |
| FINN.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| FINN.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.50 – $31.65 · 1.0% below · turned here 5× | $31.50 – $31.65 · 1.0% · 5× | PASS |  |  |
| FINN.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.665 | 0.6650 | PASS |  |  |
| FINN.NE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| FINN.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| FINN.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| FINN.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $31.65 | $31.65 | PASS |  |  |
| FINN.NE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 31.65, nearest zone high 31.65 | equal | PASS |  |  |
| FINN.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $31.65 | $31.65 | PASS |  |  |
| FINN.NE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.0% below | 1.0% below | PASS |  |  |
| FINN.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $30.32 -4.2% | $30.32 -4.2% | PASS |  |  |
| FINN.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FINN.NE | TS4 | Target = nearest resistance edge and its % from the buy | $32.88 +3.9% | $32.88 +3.9% | PASS |  |  |
| FINN.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| FINN.NE | TS6 | Risk $ (and reward $ per share) | Risk $1.33 to make $1.23 a share | Risk $1.33 to make $1.23 | PASS |  |  |
| GDX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $75.83 · 1.3% above · turned here 1× | $75.83 · 1.3% · 1× | PASS |  |  |
| GDX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GDX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $71.89 – $73.70 · 1.5% below · turned here 5× | $71.89 – $73.70 · 1.5% · 5× | PASS |  |  |
| GDX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.6076 | 3.6076 | PASS |  |  |
| GDX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GDX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| GDX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| GDX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $73.70 | $73.70 | PASS |  |  |
| GDX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 73.7, nearest zone high 73.7 | equal | PASS |  |  |
| GDX | TS1c | S5: the Buy on the bar = the Buy in the box | $73.70 | $73.70 | PASS |  |  |
| GDX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| GDX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $66.48 -9.8% | $66.48 -9.8% | PASS |  |  |
| GDX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GDX | TS4 | Target = nearest resistance edge and its % from the buy | $75.83 +2.9% | $75.83 +2.9% | PASS |  |  |
| GDX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GDX | TS6 | Risk $ (and reward $ per share) | Risk $7.22 to make $2.13 a share | Risk $7.22 to make $2.13 | PASS |  |  |
| GDXU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $22.26 – $22.62 · 2.0% above · turned here 2× | $22.26 – $22.62 · 2.0% · 2× | PASS |  |  |
| GDXU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GDXU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $20.83 · 4.6% below · turned here 1× | $20.83 · 4.6% · 1× | PASS |  |  |
| GDXU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4407 | 2.4407 | PASS |  |  |
| GDXU.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GDXU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| GDXU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| GDXU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $20.83 | $20.83 | PASS |  |  |
| GDXU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 20.83, nearest zone high 20.83 | equal | PASS |  |  |
| GDXU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $20.83 | $20.83 | PASS |  |  |
| GDXU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.6% below | 4.6% below | PASS |  |  |
| GDXU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $15.95 -23.4% | $15.95 -23.4% | PASS |  |  |
| GDXU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GDXU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $22.26 +6.9% | $22.26 +6.9% | PASS |  |  |
| GDXU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GDXU.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.88 to make $1.43 a share | Risk $4.88 to make $1.43 | PASS |  |  |
| GE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $328.67 – $336.02 · 0.2% above · turned here 3× | $328.67 – $336.02 · 0.2% · 3× | PASS |  |  |
| GE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $318.26 – $321.17 · 2.1% below · turned here 2× | $318.26 – $321.17 · 2.1% · 2× | PASS |  |  |
| GE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.9801 | 9.9801 | PASS |  |  |
| GE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| GE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| GE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $321.17 | $321.17 | PASS |  |  |
| GE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 321.17, nearest zone high 321.17 | equal | PASS |  |  |
| GE | TS1c | S5: the Buy on the bar = the Buy in the box | $321.17 | $321.17 | PASS |  |  |
| GE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| GE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $301.21 -6.2% | $301.21 -6.2% | PASS |  |  |
| GE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GE | TS4 | Target = nearest resistance edge and its % from the buy | $328.67 +2.3% | $328.67 +2.3% | PASS |  |  |
| GE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| GE | TS6 | Risk $ (and reward $ per share) | Risk $19.96 to make $7.50 a share | Risk $19.96 to make $7.50 | PASS |  |  |
| GEV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $777.00 – $807.00 · 0.6% above · turned here 3× | $777.00 – $807.00 · 0.6% · 3× | PASS |  |  |
| GEV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GEV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $731.00 – $747.00 · 3.3% below · turned here 2× | $731.00 – $747.00 · 3.3% · 2× | PASS |  |  |
| GEV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 53.6672 | 53.6676 | PASS |  |  |
| GEV | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GEV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GEV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| GEV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $747.00 | $747.00 | PASS |  |  |
| GEV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 747, nearest zone high 747 | equal | PASS |  |  |
| GEV | TS1c | S5: the Buy on the bar = the Buy in the box | $747.00 | $747.00 | PASS |  |  |
| GEV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.3% below | 3.3% below | PASS |  |  |
| GEV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $639.67 -14.4% | $639.67 -14.4% | PASS |  |  |
| GEV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV | TS4 | Target = nearest resistance edge and its % from the buy | $777.00 +4.0% | $777.00 +4.0% | PASS |  |  |
| GEV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GEV | TS6 | Risk $ (and reward $ per share) | Risk $107.33 to make $30.00 a share | Risk $107.33 to make $30.00 | PASS |  |  |
| GEV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $52.71 – $54.63 · 2.0% above · turned here 3× | $52.71 – $54.63 · 2.0% · 3× | PASS |  |  |
| GEV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $50.19 · 2.8% below · turned here 1× | $50.19 · 2.8% · 1× | PASS |  |  |
| GEV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.4795 | 3.4791 | PASS |  |  |
| GEV.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GEV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GEV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| GEV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $50.19 | $50.19 | PASS |  |  |
| GEV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 50.19, nearest zone high 50.19 | equal | PASS |  |  |
| GEV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $50.19 | $50.19 | PASS |  |  |
| GEV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.8% below | 2.8% below | PASS |  |  |
| GEV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $43.23 -13.9% | $43.23 -13.9% | PASS |  |  |
| GEV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $52.71 +5.0% | $52.71 +5.0% | PASS |  |  |
| GEV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| GEV.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.96 to make $2.52 a share | Risk $6.96 to make $2.52 | PASS |  |  |
| GGLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $69.39 · 8.2% above · turned here 1× | $69.39 · 8.2% · 1× | PASS |  |  |
| GGLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GGLL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $62.13 · 3.2% below · turned here 1× | $62.13 · 3.2% · 1× | PASS |  |  |
| GGLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.9061 | 4.9062 | PASS |  |  |
| GGLL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GGLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| GGLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| GGLL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $62.13 | $62.13 | PASS |  |  |
| GGLL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 62.13, nearest zone high 62.13 | equal | PASS |  |  |
| GGLL | TS1c | S5: the Buy on the bar = the Buy in the box | $62.13 | $62.13 | PASS |  |  |
| GGLL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.2% below | 3.2% below | PASS |  |  |
| GGLL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $52.32 -15.8% | $52.32 -15.8% | PASS |  |  |
| GGLL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GGLL | TS4 | Target = nearest resistance edge and its % from the buy | $69.39 +11.7% | $69.39 +11.7% | PASS |  |  |
| GGLL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| GGLL | TS6 | Risk $ (and reward $ per share) | Risk $9.81 to make $7.26 a share | Risk $9.81 to make $7.26 | PASS |  |  |
| GIB-A.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $119.30 · 3.6% above · turned here 1× | $119.30 · 3.6% · 1× | PASS |  |  |
| GIB-A.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Transitioning — testing resistance | Transitioning — testing resistance | PASS |  |  |
| GIB-A.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.35 · 5.1% below · turned here 1× | $109.35 · 5.1% · 1× | PASS |  |  |
| GIB-A.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.6293 | 2.6293 | PASS |  |  |
| GIB-A.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GIB-A.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| GIB-A.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| GIB-A.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.35, nearest zone high 109.35 | equal | PASS |  |  |
| GIB-A.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.1% below | 5.1% below | PASS |  |  |
| GIB-A.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $104.09 -4.8% | $104.09 -4.8% | PASS |  |  |
| GIB-A.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GIB-A.TO | TS4 | Target = nearest resistance edge and its % from the buy | $119.30 +9.1% | $119.30 +9.1% | PASS |  |  |
| GIB-A.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.9 : 1 | 1.9 : 1 | PASS |  |  |
| GIB-A.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.26 to make $9.95 a share | Risk $5.26 to make $9.95 | PASS |  |  |
| GOOGL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $293.72 – $295.67 · 4.0% above · turned here 3× | $293.72 – $295.67 · 4.0% · 3× | PASS |  |  |
| GOOGL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GOOGL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $276.92 · 2.0% below · turned here 1× | $276.92 · 2.0% · 1× | PASS |  |  |
| GOOGL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.7792 | 9.7790 | PASS |  |  |
| GOOGL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| GOOGL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| GOOGL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| GOOGL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $276.92 | $276.92 | PASS |  |  |
| GOOGL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 276.92, nearest zone high 276.92 | equal | PASS |  |  |
| GOOGL | TS1c | S5: the Buy on the bar = the Buy in the box | $276.92 | $276.92 | PASS |  |  |
| GOOGL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| GOOGL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $257.36 -7.1% | $257.36 -7.1% | PASS |  |  |
| GOOGL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GOOGL | TS4 | Target = nearest resistance edge and its % from the buy | $293.72 +6.1% | $293.72 +6.1% | PASS |  |  |
| GOOGL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| GOOGL | TS6 | Risk $ (and reward $ per share) | Risk $19.56 to make $16.80 a share | Risk $19.56 to make $16.80 | PASS |  |  |
| HD | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| HURA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $36.76 · 0.3% above · turned here 1× | $36.76 · 0.3% · 1× | PASS |  |  |
| HURA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| HURA.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| HURA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.3579 | 1.3579 | PASS |  |  |
| HURA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| HURA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| HURA.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| HXQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $113.28 · 1.3% above · turned here 1× | $113.28 · 1.3% · 1× | PASS |  |  |
| HXQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HXQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.90 · 1.7% below · turned here 1× | $109.90 · 1.7% · 1× | PASS |  |  |
| HXQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5917 | 2.5917 | PASS |  |  |
| HXQ.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| HXQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| HXQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| HXQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.90 | $109.90 | PASS |  |  |
| HXQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.9, nearest zone high 109.9 | equal | PASS |  |  |
| HXQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $109.90 | $109.90 | PASS |  |  |
| HXQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.7% below | 1.7% below | PASS |  |  |
| HXQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $104.72 -4.7% | $104.72 -4.7% | PASS |  |  |
| HXQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HXQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $113.28 +3.1% | $113.28 +3.1% | PASS |  |  |
| HXQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| HXQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.18 to make $3.38 a share | Risk $5.18 to make $3.38 | PASS |  |  |
| JNJ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $273.55 – $275.23 · 0.3% above · turned here 3× | $273.55 – $275.23 · 0.3% · 3× | PASS |  |  |
| JNJ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JNJ | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $268.11 · 1.7% below · turned here 1× | $268.11 · 1.7% · 1× | PASS |  |  |
| JNJ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.712 | 6.7118 | PASS |  |  |
| JNJ | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| JNJ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| JNJ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| JNJ | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $268.11 | $268.11 | PASS |  |  |
| JNJ | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 268.11, nearest zone high 268.11 | equal | PASS |  |  |
| JNJ | TS1c | S5: the Buy on the bar = the Buy in the box | $268.11 | $268.11 | PASS |  |  |
| JNJ | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.7% below | 1.7% below | PASS |  |  |
| JNJ | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $254.69 -5.0% | $254.69 -5.0% | PASS |  |  |
| JNJ | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JNJ | TS4 | Target = nearest resistance edge and its % from the buy | $273.55 +2.0% | $273.55 +2.0% | PASS |  |  |
| JNJ | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| JNJ | TS6 | Risk $ (and reward $ per share) | Risk $13.42 to make $5.44 a share | Risk $13.42 to make $5.44 | PASS |  |  |
| JPM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $330.40 – $333.00 · 1.9% above · turned here 3× | $330.40 – $333.00 · 1.9% · 3× | PASS |  |  |
| JPM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JPM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $321.68 – $324.25 · price is inside this zone · turned here 4× | $321.68 – $324.25 · 0.0% · 4× | PASS |  |  |
| JPM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.3809 | 7.3809 | PASS |  |  |
| JPM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| JPM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| JPM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| JPM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $324.11 | $324.11 | PASS |  |  |
| JPM | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 324.11, zone 321.68-324.25 | inside the zone | PASS |  |  |
| JPM | TS1c | S5: the Buy on the bar = the Buy in the box | $324.11 | $324.11 | PASS |  |  |
| JPM | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 324.11 vs last close 324.11 | Buy <= last close | PASS |  |  |
| JPM | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| JPM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $309.35 -4.6% | $309.35 -4.6% | PASS |  |  |
| JPM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JPM | TS4 | Target = nearest resistance edge and its % from the buy | $330.40 +1.9% | $330.40 +1.9% | PASS |  |  |
| JPM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| JPM | TS6 | Risk $ (and reward $ per share) | Risk $14.76 to make $6.29 a share | Risk $14.76 to make $6.29 | PASS |  |  |
| KEYS | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| LIN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $517.94 – $524.21 · 1.1% above · turned here 4× | $517.94 – $524.21 · 1.1% · 4× | PASS |  |  |
| LIN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| LIN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $505.18 – $506.02 · 1.2% below · turned here 3× | $505.18 – $506.02 · 1.2% · 3× | PASS |  |  |
| LIN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.8807 | 8.8807 | PASS |  |  |
| LIN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| LIN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| LIN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| LIN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $506.02 | $506.02 | PASS |  |  |
| LIN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 506.02, nearest zone high 506.02 | equal | PASS |  |  |
| LIN | TS1c | S5: the Buy on the bar = the Buy in the box | $506.02 | $506.02 | PASS |  |  |
| LIN | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| LIN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $488.26 -3.5% | $488.26 -3.5% | PASS |  |  |
| LIN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LIN | TS4 | Target = nearest resistance edge and its % from the buy | $517.94 +2.4% | $517.94 +2.4% | PASS |  |  |
| LIN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| LIN | TS6 | Risk $ (and reward $ per share) | Risk $17.76 to make $11.92 a share | Risk $17.76 to make $11.92 | PASS |  |  |
| LLY | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| MDA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $45.19 – $46.27 · 13.0% above · turned here 3× | $45.19 – $46.27 · 13.0% · 3× | PASS |  |  |
| MDA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 25.0 | 3 of 8 trend checks pass · ADX 25.0 | PASS |  |  |
| MDA.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $39.61 – $41.67 · price is inside this zone · turned here 6× | $39.61 – $41.67 · 0.0% · 6× | PASS |  |  |
| MDA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1959 | 2.1960 | PASS |  |  |
| MDA.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| MDA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| MDA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| MDA.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $39.98 | $39.98 | PASS |  |  |
| MDA.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 39.98, zone 39.61-41.67 | inside the zone | PASS |  |  |
| MDA.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $39.98 | $39.98 | PASS |  |  |
| MDA.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 39.98 vs last close 39.98 | Buy <= last close | PASS |  |  |
| MDA.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| MDA.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $35.59 -11.0% | $35.59 -11.0% | PASS |  |  |
| MDA.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MDA.TO | TS4 | Target = nearest resistance edge and its % from the buy | $45.19 +13.0% | $45.19 +13.0% | PASS |  |  |
| MDA.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| MDA.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.39 to make $5.21 a share | Risk $4.39 to make $5.21 | PASS |  |  |
| META | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| METU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $22.78 – $23.77 · 6.6% above · turned here 5× | $22.78 – $23.77 · 6.6% · 5× | PASS |  |  |
| METU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| METU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $20.84 · 2.4% below · turned here 1× | $20.84 · 2.4% · 1× | PASS |  |  |
| METU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.5644 | 1.5647 | PASS |  |  |
| METU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| METU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| METU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| METU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $20.84 | $20.84 | PASS |  |  |
| METU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 20.84, nearest zone high 20.84 | equal | PASS |  |  |
| METU | TS1c | S5: the Buy on the bar = the Buy in the box | $20.84 | $20.84 | PASS |  |  |
| METU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.4% below | 2.4% below | PASS |  |  |
| METU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $17.71 -15.0% | $17.71 -15.0% | PASS |  |  |
| METU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| METU | TS4 | Target = nearest resistance edge and its % from the buy | $22.78 +9.3% | $22.78 +9.3% | PASS |  |  |
| METU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| METU | TS6 | Risk $ (and reward $ per share) | Risk $3.13 to make $1.94 a share | Risk $3.13 to make $1.94 | PASS |  |  |
| MRVL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| MSFT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| MSFU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.64 – $38.69 · 0.1% above · turned here 4× | $37.64 – $38.69 · 0.1% · 4× | PASS |  |  |
| MSFU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MSFU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $34.44 – $36.15 · 3.9% below · turned here 4× | $34.44 – $36.15 · 3.9% · 4× | PASS |  |  |
| MSFU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2779 | 2.2778 | PASS |  |  |
| MSFU | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MSFU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| MSFU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| MSFU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $36.15 | $36.15 | PASS |  |  |
| MSFU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 36.15, nearest zone high 36.15 | equal | PASS |  |  |
| MSFU | TS1c | S5: the Buy on the bar = the Buy in the box | $36.15 | $36.15 | PASS |  |  |
| MSFU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.9% below | 3.9% below | PASS |  |  |
| MSFU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.59 -12.6% | $31.59 -12.6% | PASS |  |  |
| MSFU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFU | TS4 | Target = nearest resistance edge and its % from the buy | $37.64 +4.1% | $37.64 +4.1% | PASS |  |  |
| MSFU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MSFU | TS6 | Risk $ (and reward $ per share) | Risk $4.56 to make $1.49 a share | Risk $4.56 to make $1.49 | PASS |  |  |
| MTRX.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $29.09 – $29.56 · 1.0% above · turned here 4× | $29.09 – $29.56 · 1.0% · 4× | PASS |  |  |
| MTRX.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $28.00 · 2.8% below · turned here 1× | $28.00 · 2.8% · 1× | PASS |  |  |
| MTRX.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9407 | 0.9409 | PASS |  |  |
| MTRX.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MTRX.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| MTRX.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| MTRX.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $28.00 | $28.00 | PASS |  |  |
| MTRX.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 28, nearest zone high 28 | equal | PASS |  |  |
| MTRX.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $28.00 | $28.00 | PASS |  |  |
| MTRX.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.8% below | 2.8% below | PASS |  |  |
| MTRX.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $26.12 -6.7% | $26.12 -6.7% | PASS |  |  |
| MTRX.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MTRX.TO | TS4 | Target = nearest resistance edge and its % from the buy | $29.09 +3.9% | $29.09 +3.9% | PASS |  |  |
| MTRX.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| MTRX.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.88 to make $1.09 a share | Risk $1.88 to make $1.09 | PASS |  |  |
| MU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $32.56 · 5.9% above · turned here 1× | $32.56 · 5.9% · 1× | PASS |  |  |
| MU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $28.57 – $28.78 · 6.4% below · turned here 2× | $28.57 – $28.78 · 6.4% · 2× | PASS |  |  |
| MU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4826 | 2.4826 | PASS |  |  |
| MU.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| MU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| MU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| MU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $28.78 | $28.78 | PASS |  |  |
| MU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 28.78, nearest zone high 28.78 | equal | PASS |  |  |
| MU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $28.78 | $28.78 | PASS |  |  |
| MU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.4% below | 6.4% below | PASS |  |  |
| MU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $23.81 -17.3% | $23.81 -17.3% | PASS |  |  |
| MU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $32.56 +13.1% | $32.56 +13.1% | PASS |  |  |
| MU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| MU.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.97 to make $3.78 a share | Risk $4.97 to make $3.78 | PASS |  |  |
| NEE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $86.80 – $86.87 · 2.4% above · turned here 2× | $86.80 – $86.87 · 2.4% · 2× | PASS |  |  |
| NEE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $84.27 – $85.68 · price is inside this zone · turned here 5× | $84.27 – $85.68 · 0.0% · 5× | PASS |  |  |
| NEE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6136 | 1.6136 | PASS |  |  |
| NEE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| NEE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| NEE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| NEE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $84.78 | $84.78 | PASS |  |  |
| NEE | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 84.78, zone 84.27-85.68 | inside the zone | PASS |  |  |
| NEE | TS1c | S5: the Buy on the bar = the Buy in the box | $84.78 | $84.78 | PASS |  |  |
| NEE | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 84.78 vs last close 84.78 | Buy <= last close | PASS |  |  |
| NEE | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| NEE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $81.55 -3.8% | $81.55 -3.8% | PASS |  |  |
| NEE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEE | TS4 | Target = nearest resistance edge and its % from the buy | $86.80 +2.4% | $86.80 +2.4% | PASS |  |  |
| NEE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| NEE | TS6 | Risk $ (and reward $ per share) | Risk $3.23 to make $2.02 a share | Risk $3.23 to make $2.02 | PASS |  |  |
| NEM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $109.84 – $111.95 · 5.1% above · turned here 3× | $109.84 – $111.95 · 5.1% · 3× | PASS |  |  |
| NEM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $103.41 – $107.36 · price is inside this zone · turned here 6× | $103.41 – $107.36 · 0.0% · 6× | PASS |  |  |
| NEM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.8285 | 4.8282 | PASS |  |  |
| NEM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| NEM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| NEM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| NEM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $104.53 | $104.53 | PASS |  |  |
| NEM | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 104.53, zone 103.41-107.36 | inside the zone | PASS |  |  |
| NEM | TS1c | S5: the Buy on the bar = the Buy in the box | $104.53 | $104.53 | PASS |  |  |
| NEM | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 104.53 vs last close 104.53 | Buy <= last close | PASS |  |  |
| NEM | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| NEM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $94.87 -9.2% | $94.87 -9.2% | PASS |  |  |
| NEM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEM | TS4 | Target = nearest resistance edge and its % from the buy | $109.84 +5.1% | $109.84 +5.1% | PASS |  |  |
| NEM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| NEM | TS6 | Risk $ (and reward $ per share) | Risk $9.66 to make $5.31 a share | Risk $9.66 to make $5.31 | PASS |  |  |
| NFLX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NFXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $10.57 · 7.0% above · turned here 1× | $10.57 · 7.0% · 1× | PASS |  |  |
| NFXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFXL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.684 | 0.6844 | PASS |  |  |
| NFXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| NFXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| NFXL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NTR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $95.79 – $96.81 · 1.3% above · turned here 6× | $95.79 – $96.81 · 1.3% · 6× | PASS |  |  |
| NTR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NTR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $94.12 · 0.4% below · turned here 1× | $94.12 · 0.4% · 1× | PASS |  |  |
| NTR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.9308 | 2.9312 | PASS |  |  |
| NTR.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| NTR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| NTR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| NTR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $94.12 | $94.12 | PASS |  |  |
| NTR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 94.12, nearest zone high 94.12 | equal | PASS |  |  |
| NTR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $94.12 | $94.12 | PASS |  |  |
| NTR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| NTR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $88.26 -6.2% | $88.26 -6.2% | PASS |  |  |
| NTR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NTR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $95.79 +1.8% | $95.79 +1.8% | PASS |  |  |
| NTR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| NTR.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.86 to make $1.67 a share | Risk $5.86 to make $1.67 | PASS |  |  |
| NVDA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NVDL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| NVDL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Insufficient data | Insufficient data | PASS |  |  |
| NVDL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.4628 | 2.4619 | PASS |  |  |
| NVDL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| ONTO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $204.07 · 1.5% above · turned here 1× | $204.07 · 1.5% · 1× | PASS |  |  |
| ONTO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ONTO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $195.19 · 2.9% below · turned here 1× | $195.19 · 2.9% · 1× | PASS |  |  |
| ONTO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.0039 | 17.0039 | PASS |  |  |
| ONTO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ONTO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ONTO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ONTO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $195.19 | $195.19 | PASS |  |  |
| ONTO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 195.19, nearest zone high 195.19 | equal | PASS |  |  |
| ONTO | TS1c | S5: the Buy on the bar = the Buy in the box | $195.19 | $195.19 | PASS |  |  |
| ONTO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.9% below | 2.9% below | PASS |  |  |
| ONTO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $161.18 -17.4% | $161.18 -17.4% | PASS |  |  |
| ONTO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ONTO | TS4 | Target = nearest resistance edge and its % from the buy | $204.07 +4.5% | $204.07 +4.5% | PASS |  |  |
| ONTO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ONTO | TS6 | Risk $ (and reward $ per share) | Risk $34.01 to make $8.88 a share | Risk $34.01 to make $8.88 | PASS |  |  |
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
| ORCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $114.08 · 0.2% above · turned here 1× | $114.08 · 0.2% · 1× | PASS |  |  |
| ORCL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ORCL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.21 · 4.1% below · turned here 1× | $109.21 · 4.1% · 1× | PASS |  |  |
| ORCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.7131 | 7.7130 | PASS |  |  |
| ORCL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| ORCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ORCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ORCL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.21 | $109.21 | PASS |  |  |
| ORCL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.21, nearest zone high 109.21 | equal | PASS |  |  |
| ORCL | TS1c | S5: the Buy on the bar = the Buy in the box | $109.21 | $109.21 | PASS |  |  |
| ORCL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.1% below | 4.1% below | PASS |  |  |
| ORCL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $93.78 -14.1% | $93.78 -14.1% | PASS |  |  |
| ORCL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ORCL | TS4 | Target = nearest resistance edge and its % from the buy | $114.08 +4.5% | $114.08 +4.5% | PASS |  |  |
| ORCL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ORCL | TS6 | Risk $ (and reward $ per share) | Risk $15.43 to make $4.87 a share | Risk $15.43 to make $4.87 | PASS |  |  |
| PG | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| PNG.V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3.30 · 10.4% above · turned here 1× | $3.30 · 10.4% · 1× | PASS |  |  |
| PNG.V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| PNG.V | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| PNG.V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.2239 | 0.2242 | PASS |  |  |
| PNG.V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| PNG.V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| PNG.V | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QCOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $163.88 – $171.19 · 2.5% above · turned here 6× | $163.88 – $171.19 · 2.5% · 6× | PASS |  |  |
| QCOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QCOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $155.38 – $155.61 · 2.6% below · turned here 2× | $155.38 – $155.61 · 2.6% · 2× | PASS |  |  |
| QCOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.8798 | 8.8799 | PASS |  |  |
| QCOM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| QCOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| QCOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| QCOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $155.61 | $155.61 | PASS |  |  |
| QCOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 155.61, nearest zone high 155.61 | equal | PASS |  |  |
| QCOM | TS1c | S5: the Buy on the bar = the Buy in the box | $155.61 | $155.61 | PASS |  |  |
| QCOM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.6% below | 2.6% below | PASS |  |  |
| QCOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $137.85 -11.4% | $137.85 -11.4% | PASS |  |  |
| QCOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QCOM | TS4 | Target = nearest resistance edge and its % from the buy | $163.88 +5.3% | $163.88 +5.3% | PASS |  |  |
| QCOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| QCOM | TS6 | Risk $ (and reward $ per share) | Risk $17.76 to make $8.27 a share | Risk $17.76 to make $8.27 | PASS |  |  |
| QPUX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3.90 · 22.3% above · turned here 1× | $3.90 · 22.3% · 1× | PASS |  |  |
| QPUX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| QPUX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| QPUX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8436 | 0.8438 | PASS |  |  |
| QPUX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| QPUX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| QPUX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QTUM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $126.93 · 3.2% above · turned here 1× | $126.93 · 3.2% · 1× | PASS |  |  |
| QTUM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QTUM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $118.34 – $120.53 · 2.0% below · turned here 4× | $118.34 – $120.53 · 2.0% · 4× | PASS |  |  |
| QTUM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.6319 | 4.6319 | PASS |  |  |
| QTUM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| QTUM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| QTUM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| QTUM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $120.53 | $120.53 | PASS |  |  |
| QTUM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 120.53, nearest zone high 120.53 | equal | PASS |  |  |
| QTUM | TS1c | S5: the Buy on the bar = the Buy in the box | $120.53 | $120.53 | PASS |  |  |
| QTUM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| QTUM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $111.27 -7.7% | $111.27 -7.7% | PASS |  |  |
| QTUM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QTUM | TS4 | Target = nearest resistance edge and its % from the buy | $126.93 +5.3% | $126.93 +5.3% | PASS |  |  |
| QTUM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| QTUM | TS6 | Risk $ (and reward $ per share) | Risk $9.26 to make $6.40 a share | Risk $9.26 to make $6.40 | PASS |  |  |
| RBOT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $28.00 · 3.4% above · turned here 1× | $28.00 · 3.4% · 1× | PASS |  |  |
| RBOT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| RBOT.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| RBOT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.585 | 0.5846 | PASS |  |  |
| RBOT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| RBOT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| RBOT.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| RTX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $200.86 – $205.62 · 1.7% above · turned here 6× | $200.86 – $205.62 · 1.7% · 6× | PASS |  |  |
| RTX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RTX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $191.02 – $193.53 · 2.0% below · turned here 5× | $191.02 – $193.53 · 2.0% · 5× | PASS |  |  |
| RTX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.2219 | 5.2215 | PASS |  |  |
| RTX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| RTX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| RTX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| RTX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $193.53 | $193.53 | PASS |  |  |
| RTX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 193.53, nearest zone high 193.53 | equal | PASS |  |  |
| RTX | TS1c | S5: the Buy on the bar = the Buy in the box | $193.53 | $193.53 | PASS |  |  |
| RTX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| RTX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $183.09 -5.4% | $183.09 -5.4% | PASS |  |  |
| RTX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RTX | TS4 | Target = nearest resistance edge and its % from the buy | $200.86 +3.8% | $200.86 +3.8% | PASS |  |  |
| RTX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| RTX | TS6 | Risk $ (and reward $ per share) | Risk $10.44 to make $7.33 a share | Risk $10.44 to make $7.33 | PASS |  |  |
| RY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $275.78 · 1.3% above · turned here 1× | $275.78 · 1.3% · 1× | PASS |  |  |
| RY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $267.28 · 1.8% below · turned here 1× | $267.28 · 1.8% · 1× | PASS |  |  |
| RY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.9367 | 4.9366 | PASS |  |  |
| RY.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| RY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| RY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| RY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $267.28 | $267.28 | PASS |  |  |
| RY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 267.28, nearest zone high 267.28 | equal | PASS |  |  |
| RY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $267.28 | $267.28 | PASS |  |  |
| RY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% below | 1.8% below | PASS |  |  |
| RY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $257.41 -3.7% | $257.41 -3.7% | PASS |  |  |
| RY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $275.78 +3.2% | $275.78 +3.2% | PASS |  |  |
| RY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| RY.TO | TS6 | Risk $ (and reward $ per share) | Risk $9.87 to make $8.50 a share | Risk $9.87 to make $8.50 | PASS |  |  |
| SGRD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $18.27 · 1.7% above · turned here 1× | $18.27 · 1.7% · 1× | PASS |  |  |
| SGRD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $17.20 · 4.2% below · turned here 1× | $17.20 · 4.2% · 1× | PASS |  |  |
| SGRD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.3692 | 0.3693 | PASS |  |  |
| SGRD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SGRD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| SGRD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| SGRD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $17.20 | $17.20 | PASS |  |  |
| SGRD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 17.2, nearest zone high 17.2 | equal | PASS |  |  |
| SGRD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $17.20 | $17.20 | PASS |  |  |
| SGRD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.2% below | 4.2% below | PASS |  |  |
| SGRD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $16.46 -4.3% | $16.46 -4.3% | PASS |  |  |
| SGRD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SGRD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $18.27 +6.2% | $18.27 +6.2% | PASS |  |  |
| SGRD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.4 : 1 | 1.4 : 1 | PASS |  |  |
| SGRD.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.74 to make $1.07 a share | Risk $0.74 to make $1.07 | PASS |  |  |
| SMH | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SNDK.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $19.52 · 4.2% above · turned here 1× | $19.52 · 4.2% · 1× | PASS |  |  |
| SNDK.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SNDK.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.3982 | 2.3982 | PASS |  |  |
| SNDK.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| SNDK.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| SNDK.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $94.94 – $96.09 · 0.6% above · turned here 4× | $94.94 – $96.09 · 0.6% · 4× | PASS |  |  |
| SO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $92.72 – $93.41 · 1.1% below · turned here 3× | $92.72 – $93.41 · 1.1% · 3× | PASS |  |  |
| SO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.7759 | 1.7766 | PASS |  |  |
| SO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| SO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| SO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $93.41 | $93.41 | PASS |  |  |
| SO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 93.41, nearest zone high 93.41 | equal | PASS |  |  |
| SO | TS1c | S5: the Buy on the bar = the Buy in the box | $93.41 | $93.41 | PASS |  |  |
| SO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| SO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $89.86 -3.8% | $89.86 -3.8% | PASS |  |  |
| SO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SO | TS4 | Target = nearest resistance edge and its % from the buy | $94.94 +1.6% | $94.94 +1.6% | PASS |  |  |
| SO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| SO | TS6 | Risk $ (and reward $ per share) | Risk $3.55 to make $1.53 a share | Risk $3.55 to make $1.53 | PASS |  |  |
| SOXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $57.74 – $58.21 · 17.2% above · turned here 2× | $57.74 – $58.21 · 17.2% · 2× | PASS |  |  |
| SOXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $48.47 – $50.06 · price is inside this zone · turned here 3× | $48.47 – $50.06 · 0.0% · 3× | PASS |  |  |
| SOXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 11.7451 | 11.7452 | PASS |  |  |
| SOXL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| SOXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $49.26 | $49.26 | PASS |  |  |
| SOXL | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 49.26, zone 48.47-50.06 | inside the zone | PASS |  |  |
| SOXL | TS1c | S5: the Buy on the bar = the Buy in the box | $49.26 | $49.26 | PASS |  |  |
| SOXL | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 49.26 vs last close 49.26 | Buy <= last close | PASS |  |  |
| SOXL | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| SOXL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $25.77 -47.7% | $25.77 -47.7% | PASS |  |  |
| SOXL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL | TS4 | Target = nearest resistance edge and its % from the buy | $57.74 +17.2% | $57.74 +17.2% | PASS |  |  |
| SOXL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| SOXL | TS6 | Risk $ (and reward $ per share) | Risk $23.49 to make $8.48 a share | Risk $23.49 to make $8.48 | PASS |  |  |
| SOXL.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $14.36 · 15.5% above · turned here 1× | $14.36 · 15.5% · 1× | PASS |  |  |
| SOXL.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.05 – $13.46 · price is inside this zone · turned here 3× | $12.05 – $13.46 · 0.0% · 3× | PASS |  |  |
| SOXL.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.861 | 1.8608 | PASS |  |  |
| SOXL.NE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| SOXL.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $12.43 | $12.43 | PASS |  |  |
| SOXL.NE | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 12.43, zone 12.05-13.46 | inside the zone | PASS |  |  |
| SOXL.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $12.43 | $12.43 | PASS |  |  |
| SOXL.NE | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 12.43 vs last close 12.43 | Buy <= last close | PASS |  |  |
| SOXL.NE | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| SOXL.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $8.71 -29.9% | $8.71 -29.9% | PASS |  |  |
| SOXL.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL.NE | TS4 | Target = nearest resistance edge and its % from the buy | $14.36 +15.5% | $14.36 +15.5% | PASS |  |  |
| SOXL.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| SOXL.NE | TS6 | Risk $ (and reward $ per share) | Risk $3.72 to make $1.93 a share | Risk $3.72 to make $1.93 | PASS |  |  |
| SOXX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $154.59 – $159.14 · 9.0% above · turned here 4× | $154.59 – $159.14 · 9.0% · 4× | PASS |  |  |
| SOXX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $130.75 · 7.8% below · turned here 1× | $130.75 · 7.8% · 1× | PASS |  |  |
| SOXX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.1744 | 8.1747 | PASS |  |  |
| SOXX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SOXX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| SOXX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| SOXX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $130.75 | $130.75 | PASS |  |  |
| SOXX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 130.75, nearest zone high 130.75 | equal | PASS |  |  |
| SOXX | TS1c | S5: the Buy on the bar = the Buy in the box | $130.75 | $130.75 | PASS |  |  |
| SOXX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.8% below | 7.8% below | PASS |  |  |
| SOXX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $114.40 -12.5% | $114.40 -12.5% | PASS |  |  |
| SOXX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXX | TS4 | Target = nearest resistance edge and its % from the buy | $154.59 +18.2% | $154.59 +18.2% | PASS |  |  |
| SOXX | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.5 : 1 | 1.5 : 1 | PASS |  |  |
| SOXX | TS6 | Risk $ (and reward $ per share) | Risk $16.35 to make $23.84 a share | Risk $16.35 to make $23.84 | PASS |  |  |
| SPCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $12.16 · 28.8% above · turned here 1× | $12.16 · 28.8% · 1× | PASS |  |  |
| SPCL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $8.20 · 13.1% below · turned here 1× | $8.20 · 13.1% · 1× | PASS |  |  |
| SPCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6602 | 1.6598 | PASS |  |  |
| SPCL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| SPCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| SPCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| SPCL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $8.20 | $8.20 | PASS |  |  |
| SPCL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 8.2, nearest zone high 8.2 | equal | PASS |  |  |
| SPCL | TS1c | S5: the Buy on the bar = the Buy in the box | $8.20 | $8.20 | PASS |  |  |
| SPCL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 13.1% below | 13.1% below | PASS |  |  |
| SPCL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $4.88 -40.5% | $4.88 -40.5% | PASS |  |  |
| SPCL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SPCL | TS4 | Target = nearest resistance edge and its % from the buy | $12.16 +48.3% | $12.16 +48.3% | PASS |  |  |
| SPCL | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| SPCL | TS6 | Risk $ (and reward $ per share) | Risk $3.32 to make $3.96 a share | Risk $3.32 to make $3.96 | PASS |  |  |
| TSLA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $409.28 – $424.37 · 6.7% above · turned here 6× | $409.28 – $424.37 · 6.7% · 6× | PASS |  |  |
| TSLA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLA | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $380.15 – $393.63 · price is inside this zone · turned here 7× | $380.15 – $393.63 · 0.0% · 7× | PASS |  |  |
| TSLA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 15.6339 | 15.6339 | PASS |  |  |
| TSLA | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| TSLA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| TSLA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| TSLA | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $383.72 | $383.72 | PASS |  |  |
| TSLA | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 383.72, zone 380.15-393.63 | inside the zone | PASS |  |  |
| TSLA | TS1c | S5: the Buy on the bar = the Buy in the box | $383.72 | $383.72 | PASS |  |  |
| TSLA | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 383.72 vs last close 383.72 | Buy <= last close | PASS |  |  |
| TSLA | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| TSLA | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $352.45 -8.1% | $352.45 -8.1% | PASS |  |  |
| TSLA | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLA | TS4 | Target = nearest resistance edge and its % from the buy | $409.28 +6.7% | $409.28 +6.7% | PASS |  |  |
| TSLA | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| TSLA | TS6 | Risk $ (and reward $ per share) | Risk $31.27 to make $25.56 a share | Risk $31.27 to make $25.56 | PASS |  |  |
| TSLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $10.71 – $11.20 · 7.1% above · turned here 5× | $10.71 – $11.20 · 7.1% · 5× | PASS |  |  |
| TSLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $9.76 – $9.90 · 1.0% below · turned here 2× | $9.76 – $9.90 · 1.0% · 2× | PASS |  |  |
| TSLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8245 | 0.8241 | PASS |  |  |
| TSLL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| TSLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| TSLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| TSLL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $9.90 | $9.90 | PASS |  |  |
| TSLL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 9.9, nearest zone high 9.9 | equal | PASS |  |  |
| TSLL | TS1c | S5: the Buy on the bar = the Buy in the box | $9.90 | $9.90 | PASS |  |  |
| TSLL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.0% below | 1.0% below | PASS |  |  |
| TSLL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $8.25 -16.7% | $8.25 -16.7% | PASS |  |  |
| TSLL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLL | TS4 | Target = nearest resistance edge and its % from the buy | $10.71 +8.2% | $10.71 +8.2% | PASS |  |  |
| TSLL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| TSLL | TS6 | Risk $ (and reward $ per share) | Risk $1.65 to make $0.81 a share | Risk $1.65 to make $0.81 | PASS |  |  |
| TSM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $371.73 – $387.17 · 2.5% above · turned here 6× | $371.73 – $387.17 · 2.5% · 6× | PASS |  |  |
| TSM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $348.60 – $358.75 · 1.1% below · turned here 4× | $348.60 – $358.75 · 1.1% · 4× | PASS |  |  |
| TSM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.4992 | 17.4994 | PASS |  |  |
| TSM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| TSM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| TSM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| TSM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $358.75 | $358.75 | PASS |  |  |
| TSM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 358.75, nearest zone high 358.75 | equal | PASS |  |  |
| TSM | TS1c | S5: the Buy on the bar = the Buy in the box | $358.75 | $358.75 | PASS |  |  |
| TSM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| TSM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $323.75 -9.8% | $323.75 -9.8% | PASS |  |  |
| TSM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSM | TS4 | Target = nearest resistance edge and its % from the buy | $371.73 +3.6% | $371.73 +3.6% | PASS |  |  |
| TSM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| TSM | TS6 | Risk $ (and reward $ per share) | Risk $35.00 to make $12.98 a share | Risk $35.00 to make $12.98 | PASS |  |  |
| UBOT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $16.00 · 6.2% above · turned here 1× | $16.00 · 6.2% · 1× | PASS |  |  |
| UBOT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| UBOT | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| UBOT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7964 | 0.7970 | PASS |  |  |
| UBOT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| UBOT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| UBOT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| UFO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $40.53 · 3.7% above · turned here 1× | $40.53 · 3.7% · 1× | PASS |  |  |
| UFO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| UFO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.31 – $39.36 · price is inside this zone · turned here 3× | $38.31 – $39.36 · 0.0% · 3× | PASS |  |  |
| UFO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.3286 | 1.3284 | PASS |  |  |
| UFO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| UFO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| UFO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| UFO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $39.09 | $39.09 | PASS |  |  |
| UFO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 39.09, zone 38.31-39.36 | inside the zone | PASS |  |  |
| UFO | TS1c | S5: the Buy on the bar = the Buy in the box | $39.09 | $39.09 | PASS |  |  |
| UFO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 39.09 vs last close 39.09 | Buy <= last close | PASS |  |  |
| UFO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| UFO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $36.43 -6.8% | $36.43 -6.8% | PASS |  |  |
| UFO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| UFO | TS4 | Target = nearest resistance edge and its % from the buy | $40.53 +3.7% | $40.53 +3.7% | PASS |  |  |
| UFO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| UFO | TS6 | Risk $ (and reward $ per share) | Risk $2.66 to make $1.44 a share | Risk $2.66 to make $1.44 | PASS |  |  |
| V | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| VFV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $188.75 – $191.22 · 1.4% above · turned here 3× | $188.75 – $191.22 · 1.4% · 3× | PASS |  |  |
| VFV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VFV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $185.71 – $186.79 · price is inside this zone · turned here 4× | $185.71 – $186.79 · 0.0% · 4× | PASS |  |  |
| VFV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8036 | 2.8034 | PASS |  |  |
| VFV.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| VFV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| VFV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| VFV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $186.20 | $186.20 | PASS |  |  |
| VFV.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 186.2, zone 185.71-186.79 | inside the zone | PASS |  |  |
| VFV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $186.20 | $186.20 | PASS |  |  |
| VFV.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 186.2 vs last close 186.2 | Buy <= last close | PASS |  |  |
| VFV.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| VFV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $180.59 -3.0% | $180.59 -3.0% | PASS |  |  |
| VFV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VFV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $188.75 +1.4% | $188.75 +1.4% | PASS |  |  |
| VFV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| VFV.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.61 to make $2.55 a share | Risk $5.61 to make $2.55 | PASS |  |  |
| VRT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| WDC.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.20 · 15.8% above · turned here 1× | $20.20 · 15.8% · 1× | PASS |  |  |
| WDC.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $15.70 · 10.0% below · turned here 1× | $15.70 · 10.0% · 1× | PASS |  |  |
| WDC.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.471 | 1.4710 | PASS |  |  |
| WDC.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| WDC.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| WDC.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| WDC.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 15.7, nearest zone high 15.7 | equal | PASS |  |  |
| WDC.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 10.0% below | 10.0% below | PASS |  |  |
| WDC.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.76 -18.7% | $12.76 -18.7% | PASS |  |  |
| WDC.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WDC.TO | TS4 | Target = nearest resistance edge and its % from the buy | $20.20 +28.7% | $20.20 +28.7% | PASS |  |  |
| WDC.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.5 : 1 | 1.5 : 1 | PASS |  |  |
| WDC.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.94 to make $4.50 a share | Risk $2.94 to make $4.50 | PASS |  |  |
| WELL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $253.37 · 2.5% above · turned here 1× | $253.37 · 2.5% · 1× | PASS |  |  |
| WELL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WELL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $240.11 – $242.20 · 2.0% below · turned here 2× | $240.11 – $242.20 · 2.0% · 2× | PASS |  |  |
| WELL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.3296 | 5.3295 | PASS |  |  |
| WELL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| WELL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| WELL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| WELL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $242.20 | $242.20 | PASS |  |  |
| WELL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 242.2, nearest zone high 242.2 | equal | PASS |  |  |
| WELL | TS1c | S5: the Buy on the bar = the Buy in the box | $242.20 | $242.20 | PASS |  |  |
| WELL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| WELL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $231.54 -4.4% | $231.54 -4.4% | PASS |  |  |
| WELL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WELL | TS4 | Target = nearest resistance edge and its % from the buy | $253.37 +4.6% | $253.37 +4.6% | PASS |  |  |
| WELL | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.0 : 1 | 1.0 : 1 | PASS |  |  |
| WELL | TS6 | Risk $ (and reward $ per share) | Risk $10.66 to make $11.17 a share | Risk $10.66 to make $11.17 | PASS |  |  |
| WMT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| XCHP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $110.04 · 4.0% above · turned here 1× | $110.04 · 4.0% · 1× | PASS |  |  |
| XCHP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XCHP.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $95.50 · 9.8% below · turned here 1× | $95.50 · 9.8% · 1× | PASS |  |  |
| XCHP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.0564 | 6.0564 | PASS |  |  |
| XCHP.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XCHP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| XCHP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| XCHP.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $95.50 | $95.50 | PASS |  |  |
| XCHP.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 95.5, nearest zone high 95.5 | equal | PASS |  |  |
| XCHP.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $95.50 | $95.50 | PASS |  |  |
| XCHP.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 9.8% below | 9.8% below | PASS |  |  |
| XCHP.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $83.39 -12.7% | $83.39 -12.7% | PASS |  |  |
| XCHP.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XCHP.TO | TS4 | Target = nearest resistance edge and its % from the buy | $110.04 +15.2% | $110.04 +15.2% | PASS |  |  |
| XCHP.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| XCHP.TO | TS6 | Risk $ (and reward $ per share) | Risk $12.11 to make $14.54 a share | Risk $12.11 to make $14.54 | PASS |  |  |
| XDRV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $40.34 · 3.9% above · turned here 1× | $40.34 · 3.9% · 1× | PASS |  |  |
| XDRV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XDRV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.62 – $38.88 · price is inside this zone · turned here 2× | $38.62 – $38.88 · 0.0% · 2× | PASS |  |  |
| XDRV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8021 | 0.8021 | PASS |  |  |
| XDRV.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| XDRV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| XDRV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| XDRV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.84 | $38.84 | PASS |  |  |
| XDRV.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 38.84, zone 38.62-38.88 | inside the zone | PASS |  |  |
| XDRV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $38.84 | $38.84 | PASS |  |  |
| XDRV.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 38.84 vs last close 38.84 | Buy <= last close | PASS |  |  |
| XDRV.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| XDRV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $37.24 -4.1% | $37.24 -4.1% | PASS |  |  |
| XDRV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XDRV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $40.34 +3.9% | $40.34 +3.9% | PASS |  |  |
| XDRV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| XDRV.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.60 to make $1.50 a share | Risk $1.60 to make $1.50 | PASS |  |  |
| XEQT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $44.58 – $44.64 · 1.3% above · turned here 3× | $44.58 – $44.64 · 1.3% · 3× | PASS |  |  |
| XEQT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XEQT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $43.93 – $44.41 · price is inside this zone · turned here 5× | $43.93 – $44.41 · 0.0% · 5× | PASS |  |  |
| XEQT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.567 | 0.5667 | PASS |  |  |
| XEQT.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| XEQT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| XEQT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| XEQT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $44.01 | $44.01 | PASS |  |  |
| XEQT.TO | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 44.01, zone 43.93-44.41 | inside the zone | PASS |  |  |
| XEQT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $44.01 | $44.01 | PASS |  |  |
| XEQT.TO | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 44.01 vs last close 44.01 | Buy <= last close | PASS |  |  |
| XEQT.TO | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| XEQT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $42.88 -2.6% | $42.88 -2.6% | PASS |  |  |
| XEQT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XEQT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $44.58 +1.3% | $44.58 +1.3% | PASS |  |  |
| XEQT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| XEQT.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.13 to make $0.57 a share | Risk $1.13 to make $0.57 | PASS |  |  |
| XETM.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $64.70 · 12.0% above · turned here 1× | $64.70 · 12.0% · 1× | PASS |  |  |
| XETM.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| XETM.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5436 | 2.5436 | PASS |  |  |
| XETM.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| XETM.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| XETM.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| XGD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $49.44 – $51.57 · 2.1% above · turned here 6× | $49.44 – $51.57 · 2.1% · 6× | PASS |  |  |
| XGD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XGD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $48.17 – $48.35 · 0.2% below · turned here 2× | $48.17 – $48.35 · 0.2% · 2× | PASS |  |  |
| XGD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1667 | 2.1667 | PASS |  |  |
| XGD.TO | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XGD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| XGD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| XGD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $48.35 | $48.35 | PASS |  |  |
| XGD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 48.35, nearest zone high 48.35 | equal | PASS |  |  |
| XGD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $48.35 | $48.35 | PASS |  |  |
| XGD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.2% below | 0.2% below | PASS |  |  |
| XGD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $44.02 -9.0% | $44.02 -9.0% | PASS |  |  |
| XGD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XGD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $49.44 +2.3% | $49.44 +2.3% | PASS |  |  |
| XGD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| XGD.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.33 to make $1.09 a share | Risk $4.33 to make $1.09 | PASS |  |  |
| XOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $163.68 – $164.91 · 1.9% above · turned here 2× | $163.68 – $164.91 · 1.9% · 2× | PASS |  |  |
| XOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $159.60 – $160.11 · 0.3% below · turned here 2× | $159.60 – $160.11 · 0.3% · 2× | PASS |  |  |
| XOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.3957 | 4.3956 | PASS |  |  |
| XOM | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
| XOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| XOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| XOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $160.11 | $160.11 | PASS |  |  |
| XOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 160.11, nearest zone high 160.11 | equal | PASS |  |  |
| XOM | TS1c | S5: the Buy on the bar = the Buy in the box | $160.11 | $160.11 | PASS |  |  |
| XOM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| XOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $151.32 -5.5% | $151.32 -5.5% | PASS |  |  |
| XOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XOM | TS4 | Target = nearest resistance edge and its % from the buy | $163.68 +2.2% | $163.68 +2.2% | PASS |  |  |
| XOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| XOM | TS6 | Risk $ (and reward $ per share) | Risk $8.79 to make $3.57 a share | Risk $8.79 to make $3.57 | PASS |  |  |
