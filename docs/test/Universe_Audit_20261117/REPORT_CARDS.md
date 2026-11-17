# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-17T16:00 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM

Verdicts: PASS 3996 · WRONG 58 (CRITICAL) · MISLEADING 38 (HIGH/LOW per row) · UNVERIFIED 131 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 117 | 8 |
| card-price-data | 234 | 0 |
| card-relative-strength | 432 | 0 |
| card-trade-setup | 928 | 0 |

Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).
Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).
NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| DUK | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $128.76 | $127.67 | WRONG | CRITICAL |  |
| DUK | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 1.42% | 2.29% | WRONG | CRITICAL |  |
| DUK | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | BREAKOUT_CONFIRMED | WRONG | CRITICAL |  |
| EQIX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1109.22 | $1,103.95 | WRONG | CRITICAL |  |
| EQIX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -5.96% | -5.52% | WRONG | CRITICAL |  |
| GE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $375.58 | $375.01 | WRONG | CRITICAL |  |
| GE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.42% | -13.29% | WRONG | CRITICAL |  |
| GEV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1099.66 | $1,099.02 | WRONG | CRITICAL |  |
| HD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $355.74 | $358.36 | WRONG | CRITICAL |  |
| HD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.31% | -3.03% | WRONG | CRITICAL |  |
| HD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | NOT_READY | WRONG | CRITICAL |  |
| NEE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $87.52 | $86.87 | WRONG | CRITICAL |  |
| NEE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.49% | -1.76% | WRONG | CRITICAL |  |
| NEM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $135.01 | $135.29 | WRONG | CRITICAL |  |
| NEM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.29% | -18.46% | WRONG | CRITICAL |  |
| PG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $166.85 | $165.75 | WRONG | CRITICAL |  |
| PG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 3.7% | 4.39% | WRONG | CRITICAL |  |
| PLD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $142.69 | $143.82 | WRONG | CRITICAL |  |
| PLD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.57% | -11.28% | WRONG | CRITICAL |  |
| SO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $94.08 | $94.85 | WRONG | CRITICAL |  |
| SO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.6% | -0.22% | WRONG | CRITICAL |  |
| SO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-16 | None | WRONG | CRITICAL |  |
| SO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.86 | None | WRONG | CRITICAL |  |
| SO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_WATCH | WRONG | CRITICAL |  |
| UBOT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $25.62 | $25.70 | WRONG | CRITICAL |  |
| UBOT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39.47% | -39.65% | WRONG | CRITICAL |  |
| URAA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.5 | $31.45 | WRONG | CRITICAL |  |
| URAA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -62.83% | -62.77% | WRONG | CRITICAL |  |
| V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $425.99 | $426.78 | WRONG | CRITICAL |  |
| V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.11% | -0.07% | WRONG | CRITICAL |  |
| V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | FAILED_BREAKOUT | WRONG | CRITICAL |  |
| XOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $188.5 | $187.32 | WRONG | CRITICAL |  |
| XOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -11.47% | -10.92% | WRONG | CRITICAL |  |
| AMD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.97 · Nov 16 | $13.76 · Nov 13 | WRONG | CRITICAL |  |
| BRKU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $30.76 · Nov 16 | $30.81 · Nov 16 | WRONG | CRITICAL |  |
| VFV.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $188.17 · Nov 16 | $191.40 · Nov 13 | WRONG | CRITICAL |  |
| AMD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $504.28 / RS 1.85 | $504.28 / RS 1.86 | WRONG | CRITICAL |  |
| ASML.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $41.62 / RS 1.35 | $41.62 / RS 1.36 | WRONG | CRITICAL |  |
| ATD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $83.90 / RS 1.09 | $83.90 / RS 1.10 | WRONG | CRITICAL |  |
| AVGC | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| CEG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $277.82 / RS 0.74 | $277.82 / RS 0.75 | WRONG | CRITICAL |  |
| COPP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $46.48 / RS 0.94 | $46.48 / RS 0.95 | WRONG | CRITICAL |  |
| COPZ | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| DRAL | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| DRAM | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| GOOGL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $283.72 / RS 0.94 | $283.72 / RS 0.93 | WRONG | CRITICAL |  |
| ORBX.TO | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| ORCL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $119.09 / RS 0.48 | $119.09 / RS 0.49 | WRONG | CRITICAL |  |
| SGRD.TO | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| SNDK.TO | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| SO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $94.64 / RS 0.95 | $94.64 / RS 0.96 | WRONG | CRITICAL |  |
| SPCL | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| URAA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $11.71 / RS 0.34 | $11.71 / RS 0.33 | WRONG | CRITICAL |  |
| VFV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $191.40 / RS 1.04 | $191.40 / RS 1.05 | WRONG | CRITICAL |  |
| WDC.TO | RS1 | Relative Strength lines found | not found | present | WRONG | CRITICAL |  |
| AMD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 530.13, nearest zone high 469.21 | equal | WRONG | CRITICAL | the Buy and the Support row disagree (inside-zone + width-cap split) |
| META | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 643, nearest zone high 612.43 | equal | WRONG | CRITICAL | the Buy and the Support row disagree (inside-zone + width-cap split) |
| QCOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 172.12, nearest zone high 158.85 | equal | WRONG | CRITICAL | the Buy and the Support row disagree (inside-zone + width-cap split) |
| COTG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $17.05 · Nov 16 | $17.04 · Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close (header/quote path vs price bars) |
| ANET.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1M | bars: $1,571,272 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| AVGC | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $54,362.8 | bars: $53,699 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| BOTZ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $41.69 | $41.71 | MISLEADING | HIGH |  |
| CAT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,073.46 | $1,068.93 | MISLEADING | HIGH |  |
| COP | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $154.28 | $153.27 | MISLEADING | HIGH |  |
| COPP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $615,302.24 | bars: $667,081 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| COPZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $163,800.28 | bars: $111,295 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| DRAL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $955,747.8 | bars: $953,938 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| GE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $388.25 | $388.84 | MISLEADING | HIGH |  |
| GEV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,195.24 | $1,195.94 | MISLEADING | HIGH |  |
| HURA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $455,585.44 | bars: $451,081 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| LIN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $546.40 | $548.20 | MISLEADING | HIGH |  |
| MTRX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $253,715.48 | bars: $275,382 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| NEE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $97.30 | $98.75 | MISLEADING | HIGH |  |
| ORBX.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $88,680.4 | bars: $94,900 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| QPUX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.28 | $240.84 | MISLEADING | HIGH |  |
| QPUX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $999,890.39 | bars: $1,077,876 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| QTUM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $169.21 | $170.00 | MISLEADING | HIGH |  |
| RBOT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $73,697.81 | bars: $81,544 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| RTX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $226.41 | $226.88 | MISLEADING | HIGH |  |
| SGRD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $224,960.31 | bars: $168,004 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| SPCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $387,428.4 | bars: $407,661 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| UBOT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $239,738.07 | bars: $244,438 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| UFO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $68.12 | $68.21 | MISLEADING | HIGH |  |
| URAA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $860,884.07 | bars: $831,785 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| XETM.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $174,427.81 | bars: $186,311 | MISLEADING | LOW | the Yahoo figure and the price bars disagree; the label states no window |
| ANET.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 225 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| ASTL.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 250 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| AVGO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 225 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| CNQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 250 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| CSU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 250 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| GEV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 225 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| HXQ.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 250 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| MTRX.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 207 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| NTR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 250 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| RBOT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 250 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| XETM.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 207 bars, SPY 251 bars | equal | MISLEADING | HIGH | short history: the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods |
| ABBV | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| CNR.TO | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| ELIL | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| GIB-A.TO | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| HD | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| LLY | U-BO | numbers on the card no statement claimed (exhaustive scan) | 3% | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| PG | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| SO | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AAPU | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $48.30 | last close $48.77 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ABBV | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $292.29 | last close $294.55 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AIPO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $22.50 | last close $22.69 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AIPO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 3 of 7 differ: 23.12-24.26 x5, 20.65-21.23 x3, 24.68-24.68 x1 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| ALAB | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $207.34 | last close $202.34 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AMD | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $493.61 | last close $504.28 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AMZN | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $256.51 | last close $257.75 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AMZU | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $35.16 | last close $35.27 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ANET.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $33.06 | last close $33.41 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ASML.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $40.34 | last close $41.62 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ASTL.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $7.32 | last close $7.67 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ATD.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $83.44 | last close $83.90 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AVGC | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $17.70 | last close $17.48 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AVGO.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $12.87 | last close $12.64 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| BDT.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $70.90 | last close $75.18 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| BOTZ | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $29.69 | last close $30.12 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| BOTZ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 6 of 10 differ: 32.52-32.73 x2, 35-35.73 x4, 35.8-36.35 x7 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| BRK-B | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $589.10 | last close $592.85 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| BRKU | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $30.14 | last close $30.81 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CAMT | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $94.99 | last close $93.25 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CARS.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $19.88 | last close $20.19 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CAT | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $568.74 | last close $570.49 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CCO.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $91.98 | last close $94.40 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CEG | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $267.78 | last close $277.82 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CGY.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $84.10 | last close $86.08 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CNQ.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $68.29 | last close $68.96 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CNQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 2 of 12 differ: 57.41-57.41 x1, 56.44-56.44 x1 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| CNR.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $180.66 | last close $182.77 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| COP | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $139.42 | last close $140.52 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| COPP.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $46.32 | last close $46.48 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| COPX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $65.17 | last close $65.51 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| COPZ | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $8.61 | last close $8.68 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| COTG | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $16.95 | last close $17.04 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CSU.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $3,335.67 | last close $3,436.53 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CVX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $216.19 | last close $217.14 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| CVX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 6 of 8 differ: 214.71-214.71 x1, 208.98-208.98 x1, 197.55-201.96 x6 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| DRAL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $4.08 | last close $4.20 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| DRAM | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $38.93 | last close $39.27 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| DRIV | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $26.96 | last close $27.35 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| DRIV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 5 of 9 differ: 26.87-26.87 x1, 28.93-29.51 x5, 30.49-30.49 x1 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| DUK | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $129.88 | last close $130.59 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ELIL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $39.93 | last close $41.12 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ELIL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 3 of 3 differ: 35.86-35.86 x1, 33.58-35.13 x3, 30.31-32.35 x5 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| EQIX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $1,033.02 | last close $1,043.06 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| EQIX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 6 differ: 967.92-1002.24 x9 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| ETN | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $334.87 | last close $336.88 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| FCX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $55.16 | last close $55.19 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| FINN.NE | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $31.68 | last close $32.10 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| GDX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $79.57 | last close $78.95 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| GDXU.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $24.45 | last close $24.30 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| GE | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $325.25 | last close $325.18 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| GE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 11 of 12 differ: 329.17-336.53 x3, 319.14-321.17 x2, 306.8-311 x4 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| GEV | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $773.50 | last close $763.57 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| GEV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 7 of 7 differ: 777-807 x3, 731-731 x1, 846-897.68 x6 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| GEV.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $51.80 | last close $51.03 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| GEV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 7 differ: 47.12-47.12 x1 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| GGLL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $63.09 | last close $64.83 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| GOOGL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $279.84 | last close $283.72 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| GRID | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $154.71 | last close $156.14 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| HD | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $338.89 | last close $347.51 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| HURA.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $37.25 | last close $37.54 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| HXQ.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $110.47 | last close $111.87 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| JNJ | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $278.93 | last close $282.55 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| JNJ | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 7 of 9 differ: 274.9-276.47 x3, 269.43-269.43 x1, 245.17-251.71 x6 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| KEYS | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $282.45 | last close $285.63 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| LIN | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $515.14 | last close $523.46 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| LIN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 12 of 14 differ: 506.78-510.65 x3, 521.23-525.87 x4, 498.35-502.1 x3 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| LLY | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $1,411.40 | last close $1,431.67 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| MDA.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $39.10 | last close $40.08 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| METU | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $21.52 | last close $22.15 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| MRVL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $146.56 | last close $145.36 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| MSFU | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $37.23 | last close $39.17 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| MTRX.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $29.13 | last close $29.24 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| MU.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $30.59 | last close $31.43 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| NEE | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $84.44 | last close $85.34 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| NEM | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $110.78 | last close $110.31 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| NFLX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $59.56 | last close $60.75 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| NFXL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $9.84 | last close $10.22 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| NTR.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $99.27 | last close $98.62 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| NVDL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $15.91 | last close $16.35 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ONTO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $198.55 | last close $196.77 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ORBX.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $14.46 | last close $14.60 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| ORCL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $114.64 | last close $119.09 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| PG | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $171.72 | last close $173.02 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| PG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 7 of 8 differ: 166.85-167.25 x2, 163.13-163.13 x1, 155.77-155.77 x1 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| PLD | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $125.22 | last close $127.60 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| PNG.V | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $3.12 | last close $3.22 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| QCOM | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $165.41 | last close $168.52 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| QPUX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $3.28 | last close $3.59 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| QTUM | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $122.49 | last close $124.47 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| QTUM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 13 of 13 differ: 119.01-121.34 x4, 127.52-127.52 x1, 112.62-115.9 x5 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| RBOT.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $27.03 | last close $27.53 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| RBOT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 10 differ: 30.61-30.65 x2 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| RTX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $197.49 | last close $194.89 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| RTX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 9 of 9 differ: 192.59-194.17 x5, 203.03-206.73 x6, 185.57-190.02 x4 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| RY.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $280.40 | last close $285.69 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SETM | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $22.11 | last close $22.41 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SETM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 1 of 4 differ: 28.74-29.18 x3 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| SGRD.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $17.95 | last close $18.03 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SMH | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $460.10 | last close $461.90 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SNDK.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $19.22 | last close $19.60 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $93.63 | last close $94.64 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SOXL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $46.94 | last close $48.76 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SOXL.NE | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $11.80 | last close $12.30 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SOXX | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $139.79 | last close $141.22 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SPCL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $10.10 | last close $10.44 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| TSLL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $9.81 | last close $9.80 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| TSM | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $358.94 | last close $373.45 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| UBOT | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $14.92 | last close $15.51 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| UFO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $39.35 | last close $39.54 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| UFO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules | 9 of 10 differ: 38.31-39.5 x3, 40.68-40.68 x1, 41.86-42.65 x6 | match | UNVERIFIED | INFO | borderline: the audit frame is /api/stock's 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting. |
| URA | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $30.00 | last close $30.44 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| URAA | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $11.31 | last close $11.71 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| V | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $417.03 | last close $426.46 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| VRT | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $188.16 | last close $188.67 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| WELL | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $245.10 | last close $244.65 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| WMT | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $127.61 | last close $128.41 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| XCHP.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $103.82 | last close $105.33 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| XDRV.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $39.25 | last close $39.69 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| XEQT.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $44.24 | last close $44.86 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| XETM.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $61.17 | last close $61.57 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| XGD.TO | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $51.32 | last close $50.80 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| XOM | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $166.98 | last close $166.87 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AAPL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $351.73 | $351.73 | PASS |  |  |
| AAPL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.3% | 0.30% | PASS |  |  |
| AAPL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| AAPL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| AAPL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $351.73 · close 0.30% above · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| AAPL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| AAPU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $48.94 | $48.94 | PASS |  |  |
| AAPU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -0.35% | -0.35% | PASS |  |  |
| AAPU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.35 | 0.35 | PASS |  |  |
| AAPU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| AAPU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $48.94 · close 0.35% below · broke out Nov 11 on 0.35× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| AAPU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ABBV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $298.74 | $298.74 | PASS |  |  |
| ABBV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.4% | -1.40% | PASS |  |  |
| ABBV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ABBV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ABBV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| ABBV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $298.74 · close 1.40% below · Nov 16 close | payload values | PASS |  |  |
| ABBV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AIPO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.38 | $31.38 | PASS |  |  |
| AIPO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.68% | -27.69% | PASS |  |  |
| AIPO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AIPO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AIPO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AIPO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.38 · close 27.68% below · Nov 16 close | payload values | PASS |  |  |
| AIPO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ALAB | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $401.74 | $401.74 | PASS |  |  |
| ALAB | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -49.63% | -49.63% | PASS |  |  |
| ALAB | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ALAB | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ALAB | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ALAB | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $401.74 · close 49.63% below · Nov 16 close | payload values | PASS |  |  |
| ALAB | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $658.52 | $658.52 | PASS |  |  |
| AMD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.42% | -23.42% | PASS |  |  |
| AMD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $658.52 · close 23.42% below · Nov 16 close | payload values | PASS |  |  |
| AMD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.97 | $16.97 | PASS |  |  |
| AMD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.91% | -18.92% | PASS |  |  |
| AMD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.97 · close 18.91% below · Nov 13 close | payload values | PASS |  |  |
| AMD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $280.14 | $280.14 | PASS |  |  |
| AMZN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.99% | -7.99% | PASS |  |  |
| AMZN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $280.14 · close 7.99% below · Nov 16 close | payload values | PASS |  |  |
| AMZN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AMZU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $44.19 | $44.19 | PASS |  |  |
| AMZU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.18% | -20.19% | PASS |  |  |
| AMZU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMZU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMZU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMZU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $44.19 · close 20.18% below · Nov 16 close | payload values | PASS |  |  |
| AMZU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ANET.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.85 | $38.85 | PASS |  |  |
| ANET.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -14% | -14.00% | PASS |  |  |
| ANET.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ANET.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ANET.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ANET.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.85 · close 14.00% below · Nov 16 close | payload values | PASS |  |  |
| ANET.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASML.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $53.94 | $53.94 | PASS |  |  |
| ASML.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.84% | -22.84% | PASS |  |  |
| ASML.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ASML.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ASML.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ASML.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $53.94 · close 22.84% below · Nov 16 close | payload values | PASS |  |  |
| ASML.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $7.21 | $7.21 | PASS |  |  |
| ASTL.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 6.38% | 6.38% | PASS |  |  |
| ASTL.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-03 | 2026-11-03 | PASS |  |  |
| ASTL.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.07 | 2.07 | PASS |  |  |
| ASTL.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| ASTL.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $7.21 · close 6.38% above · broke out Nov 3 on 2.07× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| ASTL.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ASTL.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ATD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $93.43 | $93.43 | PASS |  |  |
| ATD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.2% | -10.20% | PASS |  |  |
| ATD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ATD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ATD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ATD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $93.43 · close 10.20% below · Nov 16 close | payload values | PASS |  |  |
| ATD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGC | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $31.24 | $31.24 | PASS |  |  |
| AVGC | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -44.06% | -44.05% | PASS |  |  |
| AVGC | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGC | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGC | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGC | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.24 · close 44.06% below · Nov 16 close | payload values | PASS |  |  |
| AVGC | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $432.73 | $432.73 | PASS |  |  |
| AVGO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.95% | -22.95% | PASS |  |  |
| AVGO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $432.73 · close 22.95% below · Nov 16 close | payload values | PASS |  |  |
| AVGO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AVGO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $16.45 | $16.45 | PASS |  |  |
| AVGO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.16% | -23.16% | PASS |  |  |
| AVGO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AVGO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AVGO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AVGO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $16.45 · close 23.16% below · Nov 16 close | payload values | PASS |  |  |
| AVGO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BDT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.01% | -13.01% | PASS |  |  |
| BDT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BDT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BDT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BDT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $86.42 · close 13.01% below · Nov 16 close | payload values | PASS |  |  |
| BDT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BOTZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $38.15 | $38.15 | PASS |  |  |
| BOTZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -21.05% | -21.05% | PASS |  |  |
| BOTZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| BOTZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| BOTZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| BOTZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $38.15 · close 21.05% below · Nov 16 close | payload values | PASS |  |  |
| BOTZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $557.59 | $557.59 | PASS |  |  |
| BRK-B | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 6.32% | 6.32% | PASS |  |  |
| BRK-B | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| BRK-B | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.51 | 1.51 | PASS |  |  |
| BRK-B | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| BRK-B | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $557.59 · close 6.32% above · broke out Nov 4 on 1.51× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| BRK-B | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRK-B | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| BRKU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $27.32 | $27.32 | PASS |  |  |
| BRKU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 12.77% | 12.77% | PASS |  |  |
| BRKU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| BRKU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.1 | 2.1 | PASS |  |  |
| BRKU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| BRKU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $27.32 · close 12.77% above · broke out Nov 4 on 2.10× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| BRKU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| BRKU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CAMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $178.02 | $178.02 | PASS |  |  |
| CAMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -47.62% | -47.62% | PASS |  |  |
| CAMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $178.02 · close 47.62% below · Nov 16 close | payload values | PASS |  |  |
| CAMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CARS.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $28.41 | $28.41 | PASS |  |  |
| CARS.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.94% | -28.93% | PASS |  |  |
| CARS.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CARS.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CARS.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CARS.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $28.41 · close 28.94% below · Nov 16 close | payload values | PASS |  |  |
| CARS.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CAT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $887.91 | $887.91 | PASS |  |  |
| CAT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.75% | -35.75% | PASS |  |  |
| CAT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CAT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CAT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CAT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $887.91 · close 35.75% below · Nov 16 close | payload values | PASS |  |  |
| CAT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CCO.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $154.65 | $154.65 | PASS |  |  |
| CCO.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -38.96% | -38.96% | PASS |  |  |
| CCO.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CCO.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CCO.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CCO.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $154.65 · close 38.96% below · Nov 16 close | payload values | PASS |  |  |
| CCO.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CEG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $309.8 | $309.80 | PASS |  |  |
| CEG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.32% | -10.32% | PASS |  |  |
| CEG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CEG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CEG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CEG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $309.80 · close 10.32% below · Nov 16 close | payload values | PASS |  |  |
| CEG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CGY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -9.54% | -9.53% | PASS |  |  |
| CGY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CGY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CGY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CGY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $95.15 · close 9.54% below · Nov 16 close | payload values | PASS |  |  |
| CGY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $78.6 | $78.60 | PASS |  |  |
| CNQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.26% | -12.26% | PASS |  |  |
| CNQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CNQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CNQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CNQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $78.60 · close 12.26% below · Nov 16 close | payload values | PASS |  |  |
| CNQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $178.77 | $178.77 | PASS |  |  |
| CNR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 2.24% | 2.24% | PASS |  |  |
| CNR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| CNR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.8 | 1.8 | PASS |  |  |
| CNR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| CNR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $178.77 · close 2.24% above · broke out Nov 4 on 1.80× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| CNR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CNR.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COP | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $154.28 | $154.28 | PASS |  |  |
| COP | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -8.92% | -8.92% | PASS |  |  |
| COP | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COP | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COP | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COP | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $154.28 · close 8.92% below · Nov 16 close | payload values | PASS |  |  |
| COP | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $69.02 | $69.02 | PASS |  |  |
| COPP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.66% | -32.66% | PASS |  |  |
| COPP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $69.02 · close 32.66% below · Nov 16 close | payload values | PASS |  |  |
| COPP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $97.59 | $97.59 | PASS |  |  |
| COPX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.87% | -32.87% | PASS |  |  |
| COPX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $97.59 · close 32.87% below · Nov 16 close | payload values | PASS |  |  |
| COPX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COPZ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.84 | $20.84 | PASS |  |  |
| COPZ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -58.37% | -58.35% | PASS |  |  |
| COPZ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| COPZ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| COPZ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| COPZ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.84 · close 58.37% below · Nov 16 close | payload values | PASS |  |  |
| COPZ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1042.57 | $1,042.57 | PASS |  |  |
| COST | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 6.83% | 6.83% | PASS |  |  |
| COST | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| COST | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.17 | 1.17 | PASS |  |  |
| COST | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| COST | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,042.57 · close 6.83% above · broke out Nov 4 on 1.17× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| COST | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COST | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| COTG | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $15.03 | $15.03 | PASS |  |  |
| COTG | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 13.41% | 13.37% | PASS |  |  |
| COTG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| COTG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.92 | 0.92 | PASS |  |  |
| COTG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | EXTENDED_CHASE_RISK | EXTENDED_CHASE_RISK | PASS |  |  |
| COTG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $15.03 · close 13.41% above · broke out Nov 4 on 0.92× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| COTG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| COTG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CSU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $3480.23 | $3,480.23 | PASS |  |  |
| CSU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.26% | -1.26% | PASS |  |  |
| CSU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-05 | 2026-11-05 | PASS |  |  |
| CSU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.08 | 1.08 | PASS |  |  |
| CSU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| CSU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $3,480.23 · close 1.26% below · broke out Nov 5 on 1.08× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| CSU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| CSU.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| CVX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $236.48 | $236.48 | PASS |  |  |
| CVX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -8.18% | -8.18% | PASS |  |  |
| CVX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| CVX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| CVX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| CVX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $236.48 · close 8.18% below · Nov 16 close | payload values | PASS |  |  |
| CVX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $13 | $13.00 | PASS |  |  |
| DRAL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -67.69% | -67.69% | PASS |  |  |
| DRAL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $13.00 · close 67.69% below · Nov 16 close | payload values | PASS |  |  |
| DRAL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRAM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $63.82 | $63.82 | PASS |  |  |
| DRAM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -38.47% | -38.47% | PASS |  |  |
| DRAM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRAM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRAM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRAM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $63.82 · close 38.47% below · Nov 16 close | payload values | PASS |  |  |
| DRAM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DRIV | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.47 | $36.47 | PASS |  |  |
| DRIV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25% | -25.01% | PASS |  |  |
| DRIV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| DRIV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| DRIV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| DRIV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.47 · close 25.00% below · Nov 16 close | payload values | PASS |  |  |
| DRIV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| DUK | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.82 | 1.82 | PASS |  |  |
| DUK | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $128.76 · close 1.42% above · broke out Nov 4 on 1.82× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| DUK | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| ELIL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $42.23 | $42.23 | PASS |  |  |
| ELIL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -2.64% | -2.63% | PASS |  |  |
| ELIL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ELIL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ELIL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| ELIL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $42.23 · close 2.64% below · Nov 16 close | payload values | PASS |  |  |
| ELIL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| EQIX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| EQIX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| EQIX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| EQIX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,109.22 · close 5.96% below · Nov 16 close | payload values | PASS |  |  |
| EQIX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ETN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $478 | $478.00 | PASS |  |  |
| ETN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.52% | -29.52% | PASS |  |  |
| ETN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ETN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ETN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ETN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $478.00 · close 29.52% below · Nov 16 close | payload values | PASS |  |  |
| ETN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FCX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $80.24 | $80.24 | PASS |  |  |
| FCX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -31.22% | -31.22% | PASS |  |  |
| FCX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FCX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FCX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FCX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $80.24 · close 31.22% below · Nov 16 close | payload values | PASS |  |  |
| FCX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| FINN.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.83 | $35.83 | PASS |  |  |
| FINN.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -10.41% | -10.41% | PASS |  |  |
| FINN.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| FINN.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| FINN.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| FINN.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.83 · close 10.41% below · Nov 16 close | payload values | PASS |  |  |
| FINN.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $105.67 | $105.67 | PASS |  |  |
| GDX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.29% | -25.29% | PASS |  |  |
| GDX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $105.67 · close 25.29% below · Nov 16 close | payload values | PASS |  |  |
| GDX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GDXU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.45 | $46.45 | PASS |  |  |
| GDXU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -47.69% | -47.69% | PASS |  |  |
| GDXU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GDXU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GDXU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GDXU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.45 · close 47.69% below · Nov 16 close | payload values | PASS |  |  |
| GDXU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $375.58 · close 13.42% below · Nov 16 close | payload values | PASS |  |  |
| GE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.56% | -30.52% | PASS |  |  |
| GEV | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,099.66 · close 30.56% below · Nov 16 close | payload values | PASS |  |  |
| GEV | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GEV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $73.78 | $73.78 | PASS |  |  |
| GEV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.83% | -30.83% | PASS |  |  |
| GEV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GEV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GEV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GEV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $73.78 · close 30.83% below · Nov 16 close | payload values | PASS |  |  |
| GEV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GGLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $111.95 | $111.95 | PASS |  |  |
| GGLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -42.09% | -42.09% | PASS |  |  |
| GGLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GGLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GGLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GGLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $111.95 · close 42.09% below · Nov 16 close | payload values | PASS |  |  |
| GGLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $115.5 | $115.50 | PASS |  |  |
| GIB-A.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 1.99% | 1.99% | PASS |  |  |
| GIB-A.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-05 | 2026-11-05 | PASS |  |  |
| GIB-A.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.52 | 1.52 | PASS |  |  |
| GIB-A.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| GIB-A.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $115.50 · close 1.99% above · broke out Nov 5 on 1.52× its prior 50-day average volume · Nov 13 close | payload values | PASS |  |  |
| GIB-A.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GIB-A.TO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| GOOGL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $364.17 | $364.17 | PASS |  |  |
| GOOGL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.09% | -22.09% | PASS |  |  |
| GOOGL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GOOGL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GOOGL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GOOGL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $364.17 · close 22.09% below · Nov 16 close | payload values | PASS |  |  |
| GOOGL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| GRID | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $191.52 | $191.52 | PASS |  |  |
| GRID | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.47% | -18.47% | PASS |  |  |
| GRID | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| GRID | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| GRID | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| GRID | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $191.52 · close 18.47% below · Nov 16 close | payload values | PASS |  |  |
| GRID | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $355.74 · close 2.31% below · Nov 16 close | payload values | PASS |  |  |
| HD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HURA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $56.75 | $56.75 | PASS |  |  |
| HURA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -33.85% | -33.85% | PASS |  |  |
| HURA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HURA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HURA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HURA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $56.75 · close 33.85% below · Nov 16 close | payload values | PASS |  |  |
| HURA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| HXQ.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $128.37 | $128.37 | PASS |  |  |
| HXQ.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.85% | -12.85% | PASS |  |  |
| HXQ.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| HXQ.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| HXQ.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| HXQ.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $128.37 · close 12.85% below · Nov 16 close | payload values | PASS |  |  |
| HXQ.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $282.01 | $282.02 | PASS |  |  |
| JNJ | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.19% | 0.19% | PASS |  |  |
| JNJ | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-09 | 2026-11-09 | PASS |  |  |
| JNJ | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.96 | 0.96 | PASS |  |  |
| JNJ | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| JNJ | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $282.01 · close 0.19% above · broke out Nov 9 on 0.96× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| JNJ | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| JNJ | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| JPM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $366.5 | $366.50 | PASS |  |  |
| JPM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -7.72% | -7.72% | PASS |  |  |
| JPM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| JPM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| JPM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| JPM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $366.50 · close 7.72% below · Nov 16 close | payload values | PASS |  |  |
| JPM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| KEYS | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $389.93 | $389.93 | PASS |  |  |
| KEYS | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -26.75% | -26.75% | PASS |  |  |
| KEYS | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| KEYS | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| KEYS | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| KEYS | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $389.93 · close 26.75% below · Nov 16 close | payload values | PASS |  |  |
| KEYS | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LIN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $522.93 | $522.93 | PASS |  |  |
| LIN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.1% | 0.10% | PASS |  |  |
| LIN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| LIN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.14 | 1.14 | PASS |  |  |
| LIN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| LIN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $522.93 · close 0.10% above · broke out Nov 4 on 1.14× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| LIN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| LIN | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| LLY | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $1449.68 | $1,449.68 | PASS |  |  |
| LLY | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -1.24% | -1.24% | PASS |  |  |
| LLY | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| LLY | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| LLY | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_WATCH | BREAKOUT_WATCH | PASS |  |  |
| LLY | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $1,449.68 · close 1.24% below · Nov 16 close | payload values | PASS |  |  |
| LLY | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MDA.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $51.34 | $51.34 | PASS |  |  |
| MDA.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -21.93% | -21.93% | PASS |  |  |
| MDA.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MDA.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MDA.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MDA.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $51.34 · close 21.93% below · Nov 16 close | payload values | PASS |  |  |
| MDA.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| META | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $779.82 | $779.82 | PASS |  |  |
| META | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.67% | -19.67% | PASS |  |  |
| META | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| META | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| META | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| META | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $779.82 · close 19.67% below · Nov 16 close | payload values | PASS |  |  |
| META | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| METU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $35.6 | $35.60 | PASS |  |  |
| METU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.78% | -37.78% | PASS |  |  |
| METU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| METU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| METU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| METU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $35.60 · close 37.78% below · Nov 16 close | payload values | PASS |  |  |
| METU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MRVL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $301.27 | $301.27 | PASS |  |  |
| MRVL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -51.75% | -51.75% | PASS |  |  |
| MRVL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MRVL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MRVL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MRVL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $301.27 · close 51.75% below · Nov 16 close | payload values | PASS |  |  |
| MRVL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $551.15 | $551.15 | PASS |  |  |
| MSFT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -6.02% | -6.02% | PASS |  |  |
| MSFT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| MSFT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.3 | 2.3 | PASS |  |  |
| MSFT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| MSFT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $551.15 · close 6.02% below · broke out Nov 4 on 2.30× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| MSFT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFT | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| MSFU | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $45.17 | $45.17 | PASS |  |  |
| MSFU | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.29% | -13.28% | PASS |  |  |
| MSFU | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| MSFU | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.32 | 1.32 | PASS |  |  |
| MSFU | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| MSFU | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $45.17 · close 13.29% below · broke out Nov 4 on 1.32× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| MSFU | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MSFU | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| MTRX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $37.54 | $37.54 | PASS |  |  |
| MTRX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.11% | -22.11% | PASS |  |  |
| MTRX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MTRX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MTRX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MTRX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $37.54 · close 22.11% below · Nov 16 close | payload values | PASS |  |  |
| MTRX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| MU.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $48.54 | $48.54 | PASS |  |  |
| MU.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.25% | -35.25% | PASS |  |  |
| MU.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| MU.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| MU.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| MU.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $48.54 · close 35.25% below · Nov 16 close | payload values | PASS |  |  |
| MU.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| NEE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 2.29 | 2.29 | PASS |  |  |
| NEE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | FAILED_BREAKOUT | FAILED_BREAKOUT | PASS |  |  |
| NEE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $87.52 · close 2.49% below · broke out Nov 4 on 2.29× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| NEE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NEE | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| NEM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NEM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NEM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NEM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $135.01 · close 18.29% below · Nov 16 close | payload values | PASS |  |  |
| NEM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFLX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $83.6 | $83.60 | PASS |  |  |
| NFLX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.33% | -27.33% | PASS |  |  |
| NFLX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFLX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFLX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFLX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $83.60 · close 27.33% below · Nov 16 close | payload values | PASS |  |  |
| NFLX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NFXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $20.49 | $20.49 | PASS |  |  |
| NFXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -50.12% | -50.12% | PASS |  |  |
| NFXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NFXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NFXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NFXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $20.49 · close 50.12% below · Nov 16 close | payload values | PASS |  |  |
| NFXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NTR.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $112.9 | $112.90 | PASS |  |  |
| NTR.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12.65% | -12.65% | PASS |  |  |
| NTR.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NTR.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NTR.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NTR.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $112.90 · close 12.65% below · Nov 16 close | payload values | PASS |  |  |
| NTR.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.37 | $243.37 | PASS |  |  |
| NVDA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.84% | -35.84% | PASS |  |  |
| NVDA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.37 · close 35.84% below · Nov 16 close | payload values | PASS |  |  |
| NVDA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $41.59 | $41.59 | PASS |  |  |
| NVDL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -60.69% | -60.69% | PASS |  |  |
| NVDL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $41.59 · close 60.69% below · Nov 16 close | payload values | PASS |  |  |
| NVDL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ONTO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $353.84 | $353.84 | PASS |  |  |
| ONTO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -44.39% | -44.39% | PASS |  |  |
| ONTO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ONTO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ONTO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ONTO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $353.84 · close 44.39% below · Nov 16 close | payload values | PASS |  |  |
| ONTO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORBX.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $19.64 | $19.64 | PASS |  |  |
| ORBX.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -25.66% | -25.66% | PASS |  |  |
| ORBX.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORBX.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORBX.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORBX.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $19.64 · close 25.66% below · Nov 16 close | payload values | PASS |  |  |
| ORBX.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| ORCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $170.7 | $170.70 | PASS |  |  |
| ORCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -30.23% | -30.23% | PASS |  |  |
| ORCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| ORCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| ORCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| ORCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $170.70 · close 30.23% below · Nov 16 close | payload values | PASS |  |  |
| ORCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| PG | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.55 | 1.55 | PASS |  |  |
| PG | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| PG | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $166.85 · close 3.70% above · broke out Nov 4 on 1.55× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| PG | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PG | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| PLD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PLD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PLD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PLD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $142.69 · close 10.57% below · Nov 16 close | payload values | PASS |  |  |
| PLD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PNG.V | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $6.8 | $6.80 | PASS |  |  |
| PNG.V | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -52.65% | -52.65% | PASS |  |  |
| PNG.V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PNG.V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PNG.V | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PNG.V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $6.80 · close 52.65% below · Nov 16 close | payload values | PASS |  |  |
| PNG.V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QCOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $205.85 | $205.85 | PASS |  |  |
| QCOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.14% | -18.13% | PASS |  |  |
| QCOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QCOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QCOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QCOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $205.85 · close 18.14% below · Nov 16 close | payload values | PASS |  |  |
| QCOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QPUX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $22.2 | $22.20 | PASS |  |  |
| QPUX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -83.83% | -83.83% | PASS |  |  |
| QPUX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QPUX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QPUX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QPUX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $22.20 · close 83.83% below · Nov 16 close | payload values | PASS |  |  |
| QPUX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QTUM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $159.25 | $159.25 | PASS |  |  |
| QTUM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -21.84% | -21.84% | PASS |  |  |
| QTUM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QTUM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QTUM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QTUM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $159.25 · close 21.84% below · Nov 16 close | payload values | PASS |  |  |
| QTUM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RBOT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $34.84 | $34.84 | PASS |  |  |
| RBOT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.98% | -20.98% | PASS |  |  |
| RBOT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RBOT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RBOT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RBOT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $34.84 · close 20.98% below · Nov 16 close | payload values | PASS |  |  |
| RBOT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RTX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $226.41 | $226.41 | PASS |  |  |
| RTX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -13.92% | -13.92% | PASS |  |  |
| RTX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RTX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RTX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RTX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $226.41 · close 13.92% below · Nov 16 close | payload values | PASS |  |  |
| RTX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RY.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.46 | $300.46 | PASS |  |  |
| RY.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -4.92% | -4.92% | PASS |  |  |
| RY.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RY.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RY.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RY.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.46 · close 4.92% below · Nov 16 close | payload values | PASS |  |  |
| RY.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SETM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $36.24 | $36.24 | PASS |  |  |
| SETM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -38.16% | -38.16% | PASS |  |  |
| SETM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SETM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SETM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SETM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $36.24 · close 38.16% below · Nov 16 close | payload values | PASS |  |  |
| SETM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SGRD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $21.32 | $21.32 | PASS |  |  |
| SGRD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -15.42% | -15.43% | PASS |  |  |
| SGRD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SGRD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SGRD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SGRD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $21.32 · close 15.42% below · Nov 16 close | payload values | PASS |  |  |
| SGRD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SMH | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $639.47 | $639.47 | PASS |  |  |
| SMH | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.77% | -27.77% | PASS |  |  |
| SMH | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SMH | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SMH | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SMH | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $639.47 · close 27.77% below · Nov 16 close | payload values | PASS |  |  |
| SMH | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SNDK.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.35 | $46.35 | PASS |  |  |
| SNDK.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -57.71% | -57.71% | PASS |  |  |
| SNDK.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SNDK.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SNDK.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SNDK.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.35 · close 57.71% below · Nov 16 close | payload values | PASS |  |  |
| SNDK.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $94.08 · close 0.60% above · broke out Nov 16 on 1.86× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| SO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SO | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| SOXL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $169.83 | $169.83 | PASS |  |  |
| SOXL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -71.29% | -71.29% | PASS |  |  |
| SOXL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $169.83 · close 71.29% below · Nov 16 close | payload values | PASS |  |  |
| SOXL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $40.79 | $40.79 | PASS |  |  |
| SOXL.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -69.85% | -69.85% | PASS |  |  |
| SOXL.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $40.79 · close 69.85% below · Nov 16 close | payload values | PASS |  |  |
| SOXL.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXX | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $198.81 | $198.81 | PASS |  |  |
| SOXX | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.97% | -28.97% | PASS |  |  |
| SOXX | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXX | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXX | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXX | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $198.81 · close 28.97% below · Nov 16 close | payload values | PASS |  |  |
| SOXX | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SPCL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.54 | $33.54 | PASS |  |  |
| SPCL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -68.87% | -68.87% | PASS |  |  |
| SPCL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SPCL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SPCL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SPCL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.54 · close 68.87% below · Nov 16 close | payload values | PASS |  |  |
| SPCL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $414.23 | $414.23 | PASS |  |  |
| TSLA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -8.33% | -8.33% | PASS |  |  |
| TSLA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $414.23 · close 8.33% below · Nov 16 close | payload values | PASS |  |  |
| TSLA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSLL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $11.98 | $11.98 | PASS |  |  |
| TSLL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -18.2% | -18.20% | PASS |  |  |
| TSLL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSLL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSLL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSLL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $11.98 · close 18.20% below · Nov 16 close | payload values | PASS |  |  |
| TSLL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| TSM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $487.47 | $487.47 | PASS |  |  |
| TSM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.39% | -23.39% | PASS |  |  |
| TSM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| TSM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| TSM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| TSM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $487.47 · close 23.39% below · Nov 16 close | payload values | PASS |  |  |
| TSM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UBOT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UBOT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UBOT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UBOT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $25.62 · close 39.47% below · Nov 16 close | payload values | PASS |  |  |
| UBOT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| UFO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.29 | $49.29 | PASS |  |  |
| UFO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.77% | -19.78% | PASS |  |  |
| UFO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| UFO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| UFO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| UFO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.29 · close 19.77% below · Nov 16 close | payload values | PASS |  |  |
| UFO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| URA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $50.09 | $50.09 | PASS |  |  |
| URA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -39.23% | -39.23% | PASS |  |  |
| URA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| URA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| URA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| URA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $50.09 · close 39.23% below · Nov 16 close | payload values | PASS |  |  |
| URA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| URAA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| URAA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| URAA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| URAA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $31.50 · close 62.83% below · Nov 16 close | payload values | PASS |  |  |
| URAA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| V | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| V | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.57 | 1.57 | PASS |  |  |
| V | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $425.99 · close 0.11% above · broke out Nov 4 on 1.57× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| V | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| V | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| VFV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.25% | -3.25% | PASS |  |  |
| VFV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VFV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VFV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VFV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $197.83 · close 3.25% below · Nov 13 close | payload values | PASS |  |  |
| VFV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| VRT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $300.3 | $300.30 | PASS |  |  |
| VRT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -37.17% | -37.17% | PASS |  |  |
| VRT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| VRT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| VRT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| VRT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $300.30 · close 37.17% below · Nov 16 close | payload values | PASS |  |  |
| VRT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WDC.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $33.32 | $33.32 | PASS |  |  |
| WDC.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -46.31% | -46.31% | PASS |  |  |
| WDC.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| WDC.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| WDC.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| WDC.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $33.32 · close 46.31% below · Nov 13 close | payload values | PASS |  |  |
| WDC.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WELL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.04 | $243.04 | PASS |  |  |
| WELL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.66% | 0.66% | PASS |  |  |
| WELL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| WELL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.46 | 1.46 | PASS |  |  |
| WELL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| WELL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.04 · close 0.66% above · broke out Nov 4 on 1.46× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| WELL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WELL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| WMT | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $127.94 | $127.94 | PASS |  |  |
| WMT | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.37% | 0.37% | PASS |  |  |
| WMT | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| WMT | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.32 | 1.32 | PASS |  |  |
| WMT | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| WMT | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $127.94 · close 0.37% above · broke out Nov 4 on 1.32× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| WMT | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| WMT | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| XCHP.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $147.5 | $147.50 | PASS |  |  |
| XCHP.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -28.59% | -28.59% | PASS |  |  |
| XCHP.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XCHP.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XCHP.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XCHP.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $147.50 · close 28.59% below · Nov 16 close | payload values | PASS |  |  |
| XCHP.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XDRV.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $49.26 | $49.26 | PASS |  |  |
| XDRV.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.43% | -19.43% | PASS |  |  |
| XDRV.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XDRV.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XDRV.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XDRV.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $49.26 · close 19.43% below · Nov 16 close | payload values | PASS |  |  |
| XDRV.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XEQT.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -3.28% | -3.28% | PASS |  |  |
| XEQT.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XEQT.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XEQT.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XEQT.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $46.38 · close 3.28% below · Nov 16 close | payload values | PASS |  |  |
| XEQT.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XETM.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $91.8 | $91.80 | PASS |  |  |
| XETM.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -32.93% | -32.93% | PASS |  |  |
| XETM.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XETM.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XETM.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XETM.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $91.80 · close 32.93% below · Nov 16 close | payload values | PASS |  |  |
| XETM.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XGD.TO | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $65.29 | $65.29 | PASS |  |  |
| XGD.TO | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -22.19% | -22.19% | PASS |  |  |
| XGD.TO | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XGD.TO | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XGD.TO | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XGD.TO | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $65.29 · close 22.19% below · Nov 16 close | payload values | PASS |  |  |
| XGD.TO | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| XOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| XOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| XOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| XOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $188.50 · close 11.47% below · Nov 16 close | payload values | PASS |  |  |
| XOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $352.78 · Nov 16 | $352.78 · Nov 16 | PASS |  |  |
| AAPU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $48.77 · Nov 16 | $48.77 · Nov 16 | PASS |  |  |
| ABBV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.52 / Mom: +1.21 / Rank: 2/11] XLV LEADING | RS 105.52 Mom 1.21 Rank 2/11 | PASS |  |  |
| ABBV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| ABBV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ABBV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $294.55 · Nov 16 | $294.55 · Nov 16 | PASS |  |  |
| AIPO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AIPO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $22.69 · Nov 16 | $22.69 · Nov 16 | PASS |  |  |
| ALAB | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| ALAB | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ALAB | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ALAB | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $202.34 · Nov 16 | $202.34 · Nov 16 | PASS |  |  |
| AMD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AMD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $504.28 · Nov 16 | $504.28 · Nov 16 | PASS |  |  |
| AMD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AMD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.24 / Rank: 7/11] X | RS 98.43 Mom 2.24 Rank 7/11 | PASS |  |  |
| AMZN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| AMZN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $257.75 · Nov 16 | $257.75 · Nov 16 | PASS |  |  |
| AMZU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMZU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $35.27 · Nov 16 | $35.27 · Nov 16 | PASS |  |  |
| ANET.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASML.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.68 / Mom: +0.71 / Rank: 6/11] XLB IMPROVING | RS 98.68 Mom 0.71 Rank 6/11 | PASS |  |  |
| ASTL.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ASTL.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ASTL.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $7.67 · Nov 16 | $7.67 · Nov 16 | PASS |  |  |
| ATD.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.24 / Rank: 7/11] X | RS 98.43 Mom 2.24 Rank 7/11 | PASS |  |  |
| ATD.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| ATD.TO | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 7 days | 📅 Earnings in 7 days | PASS |  |  |
| ATD.TO | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 7 days | 2026-11-24, 7 days | PASS |  |  |
| ATD.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $83.90 · Nov 16 | $83.90 · Nov 16 | PASS |  |  |
| AVGC | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AVGO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AVGO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AVGO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $333.40 · Nov 16 | $333.40 · Nov 16 | PASS |  |  |
| AVGO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BDT.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| BDT.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| BDT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BOTZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BOTZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $30.12 · Nov 16 | $30.12 · Nov 16 | PASS |  |  |
| BRK-B | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.07 / Mom: -0.4 / Rank: 4/11] XLF WEAKENING | RS 100.07 Mom -0.4 Rank 4/11 | PASS |  |  |
| BRK-B | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| BRK-B | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| BRK-B | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $592.85 · Nov 16 | $592.85 · Nov 16 | PASS |  |  |
| BRKU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| CAMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAMT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $93.25 · Nov 16 | $93.25 · Nov 16 | PASS |  |  |
| CARS.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CARS.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $20.19 · Nov 16 | $20.19 · Nov 16 | PASS |  |  |
| CAT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| CAT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CAT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CAT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $570.49 · Nov 16 | $570.49 · Nov 16 | PASS |  |  |
| CCO.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.41 / Mom: +0.35 / Rank: 1/11] XLE LEADING | RS 106.41 Mom 0.35 Rank 1/11 | PASS |  |  |
| CCO.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CCO.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CEG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.72 / Mom: +2.91 / Rank: 10/11] XLU IMPROVING | RS 96.72 Mom 2.91 Rank 10/11 | PASS |  |  |
| CEG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| CEG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CEG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $277.82 · Nov 16 | $277.82 · Nov 16 | PASS |  |  |
| CGY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| CGY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CGY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CGY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $86.08 · Nov 16 | $86.08 · Nov 16 | PASS |  |  |
| CNQ.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.41 / Mom: +0.35 / Rank: 1/11] XLE LEADING | RS 106.41 Mom 0.35 Rank 1/11 | PASS |  |  |
| CNQ.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CNQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNQ.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $68.96 · Nov 16 | $68.96 · Nov 16 | PASS |  |  |
| CNR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| CNR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CNR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CNR.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $182.77 · Nov 16 | $182.77 · Nov 16 | PASS |  |  |
| COP | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.41 / Mom: +0.35 / Rank: 1/11] XLE LEADING | RS 106.41 Mom 0.35 Rank 1/11 | PASS |  |  |
| COP | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COP | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COP | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $140.52 · Nov 16 | $140.52 · Nov 16 | PASS |  |  |
| COPP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPP.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $46.48 · Nov 16 | $46.48 · Nov 16 | PASS |  |  |
| COPX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $65.51 · Nov 16 | $65.51 · Nov 16 | PASS |  |  |
| COPZ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COPZ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $8.68 · Nov 16 | $8.68 · Nov 16 | PASS |  |  |
| COST | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.54 / Mom: +3.19 / Rank: 3/11] XLP LE | RS 101.54 Mom 3.19 Rank 3/11 | PASS |  |  |
| COST | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| COST | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| COST | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,113.74 · Nov 16 | $1,113.74 · Nov 16 | PASS |  |  |
| COTG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CSU.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| CSU.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| CSU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CSU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3,436.53 · Nov 16 | $3,436.53 · Nov 16 | PASS |  |  |
| CVX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.41 / Mom: +0.35 / Rank: 1/11] XLE LEADING | RS 106.41 Mom 0.35 Rank 1/11 | PASS |  |  |
| CVX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| CVX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| CVX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $217.14 · Nov 16 | $217.14 · Nov 16 | PASS |  |  |
| DRAL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $4.20 · Nov 16 | $4.20 · Nov 16 | PASS |  |  |
| DRAM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRAM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $39.27 · Nov 16 | $39.27 · Nov 16 | PASS |  |  |
| DRIV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DRIV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $27.35 · Nov 16 | $27.35 · Nov 16 | PASS |  |  |
| DUK | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.72 / Mom: +2.91 / Rank: 10/11] XLU IMPROVING | RS 96.72 Mom 2.91 Rank 10/11 | PASS |  |  |
| DUK | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| DUK | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DUK | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $130.59 · Nov 16 | $130.59 · Nov 16 | PASS |  |  |
| ELIL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ELIL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $41.12 · Nov 16 | $41.12 · Nov 16 | PASS |  |  |
| EQIX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.15 / Mom: +1.25 / Rank: 9/11] XLRE IMPROV | RS 97.15 Mom 1.25 Rank 9/11 | PASS |  |  |
| EQIX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| EQIX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| EQIX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,043.06 · Nov 16 | $1,043.06 · Nov 16 | PASS |  |  |
| ETN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| ETN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ETN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ETN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $336.88 · Nov 16 | $336.88 · Nov 16 | PASS |  |  |
| FCX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.68 / Mom: +0.71 / Rank: 6/11] XLB IMPROVING | RS 98.68 Mom 0.71 Rank 6/11 | PASS |  |  |
| FCX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| FCX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| FCX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $55.19 · Nov 16 | $55.19 · Nov 16 | PASS |  |  |
| FINN.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $78.95 · Nov 16 | $78.95 · Nov 16 | PASS |  |  |
| GDXU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GDXU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $24.30 · Nov 16 | $24.30 · Nov 16 | PASS |  |  |
| GE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| GE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $325.18 · Nov 16 | $325.18 · Nov 16 | PASS |  |  |
| GEV | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| GEV | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GEV | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GEV | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $763.57 · Nov 16 | $763.57 · Nov 16 | PASS |  |  |
| GEV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GGLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $64.83 · Nov 16 | $64.83 · Nov 16 | PASS |  |  |
| GIB-A.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| GIB-A.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| GIB-A.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GOOGL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.01 / Mom: +0.3 / Rank: 8/11] XL | RS 98.01 Mom 0.3 Rank 8/11 | PASS |  |  |
| GOOGL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| GOOGL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GOOGL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $283.72 · Nov 16 | $283.72 · Nov 16 | PASS |  |  |
| GRID | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| GRID | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $156.14 · Nov 16 | $156.14 · Nov 16 | PASS |  |  |
| HD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.24 / Rank: 7/11] X | RS 98.43 Mom 2.24 Rank 7/11 | PASS |  |  |
| HD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| HD | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ EARNINGS TODAY | ⚠️ EARNINGS TODAY | PASS |  |  |
| HD | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-17, 0 days | 2026-11-17, 0 days | PASS |  |  |
| HD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $347.51 · Nov 16 | $347.51 · Nov 16 | PASS |  |  |
| HURA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| HXQ.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.52 / Mom: +1.21 / Rank: 2/11] XLV LEADING | RS 105.52 Mom 1.21 Rank 2/11 | PASS |  |  |
| JNJ | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| JNJ | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JNJ | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $282.55 · Nov 16 | $282.55 · Nov 16 | PASS |  |  |
| JPM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.07 / Mom: -0.4 / Rank: 4/11] XLF WEAKENING | RS 100.07 Mom -0.4 Rank 4/11 | PASS |  |  |
| JPM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| JPM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| JPM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $338.21 · Nov 16 | $338.21 · Nov 16 | PASS |  |  |
| KEYS | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| KEYS | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| KEYS | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ Earnings in 2 days | ⚠️ Earnings in 2 days | PASS |  |  |
| KEYS | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-19, 2 days | 2026-11-19, 2 days | PASS |  |  |
| KEYS | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $285.63 · Nov 16 | $285.63 · Nov 16 | PASS |  |  |
| LIN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.68 / Mom: +0.71 / Rank: 6/11] XLB IMPROVING | RS 98.68 Mom 0.71 Rank 6/11 | PASS |  |  |
| LIN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| LIN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LIN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $523.46 · Nov 16 | $523.46 · Nov 16 | PASS |  |  |
| LLY | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Health Care (XLV) — RS: 105.52 / Mom: +1.21 / Rank: 2/11] XLV LEADING | RS 105.52 Mom 1.21 Rank 2/11 | PASS |  |  |
| LLY | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| LLY | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| LLY | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $1,431.67 · Nov 16 | $1,431.67 · Nov 16 | PASS |  |  |
| MDA.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| MDA.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MDA.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MDA.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $40.08 · Nov 16 | $40.08 · Nov 16 | PASS |  |  |
| META | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.01 / Mom: +0.3 / Rank: 8/11] XL | RS 98.01 Mom 0.3 Rank 8/11 | PASS |  |  |
| META | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| META | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| META | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $626.41 · Nov 16 | $626.41 · Nov 16 | PASS |  |  |
| METU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| METU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $22.15 · Nov 16 | $22.15 · Nov 16 | PASS |  |  |
| MRVL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| MRVL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MRVL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MRVL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $145.36 · Nov 16 | $145.36 · Nov 16 | PASS |  |  |
| MSFT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| MSFT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| MSFT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $517.99 · Nov 16 | $517.99 · Nov 16 | PASS |  |  |
| MSFU | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MSFU | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $39.17 · Nov 16 | $39.17 · Nov 16 | PASS |  |  |
| MTRX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MTRX.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $29.24 · Nov 16 | $29.24 · Nov 16 | PASS |  |  |
| MU.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| MU.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $31.43 · Nov 16 | $31.43 · Nov 16 | PASS |  |  |
| NEE | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.72 / Mom: +2.91 / Rank: 10/11] XLU IMPROVING | RS 96.72 Mom 2.91 Rank 10/11 | PASS |  |  |
| NEE | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $85.34 · Nov 16 | $85.34 · Nov 16 | PASS |  |  |
| NEM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.68 / Mom: +0.71 / Rank: 6/11] XLB IMPROVING | RS 98.68 Mom 0.71 Rank 6/11 | PASS |  |  |
| NEM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NEM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NEM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $110.31 · Nov 16 | $110.31 · Nov 16 | PASS |  |  |
| NFLX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 98.01 / Mom: +0.3 / Rank: 8/11] XL | RS 98.01 Mom 0.3 Rank 8/11 | PASS |  |  |
| NFLX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NFLX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFLX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $60.75 · Nov 16 | $60.75 · Nov 16 | PASS |  |  |
| NFXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NFXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $10.22 · Nov 16 | $10.22 · Nov 16 | PASS |  |  |
| NTR.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.68 / Mom: +0.71 / Rank: 6/11] XLB IMPROVING | RS 98.68 Mom 0.71 Rank 6/11 | PASS |  |  |
| NTR.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| NTR.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| NVDA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| NVDA | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ EARNINGS TODAY | ⚠️ EARNINGS TODAY | PASS |  |  |
| NVDA | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-17, 0 days | 2026-11-17, 0 days | PASS |  |  |
| NVDA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $156.14 · Nov 16 | $156.14 · Nov 16 | PASS |  |  |
| NVDL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $16.35 · Nov 16 | $16.35 · Nov 16 | PASS |  |  |
| ONTO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| ONTO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ONTO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ONTO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $196.77 · Nov 16 | $196.77 · Nov 16 | PASS |  |  |
| ORBX.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| ORCL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ORCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ORCL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $119.09 · Nov 16 | $119.09 · Nov 16 | PASS |  |  |
| PG | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.54 / Mom: +3.19 / Rank: 3/11] XLP LE | RS 101.54 Mom 3.19 Rank 3/11 | PASS |  |  |
| PG | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| PG | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PG | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $173.02 · Nov 16 | $173.02 · Nov 16 | PASS |  |  |
| PLD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.15 / Mom: +1.25 / Rank: 9/11] XLRE IMPROV | RS 97.15 Mom 1.25 Rank 9/11 | PASS |  |  |
| PLD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| PLD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PLD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $127.60 · Nov 16 | $127.60 · Nov 16 | PASS |  |  |
| PNG.V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| PNG.V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| PNG.V | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | 📅 Earnings in 7 days | 📅 Earnings in 7 days | PASS |  |  |
| PNG.V | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-24, 7 days | 2026-11-24, 7 days | PASS |  |  |
| PNG.V | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3.22 · Nov 16 | $3.22 · Nov 16 | PASS |  |  |
| QCOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| QCOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| QCOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QCOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $168.52 · Nov 16 | $168.52 · Nov 16 | PASS |  |  |
| QPUX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QPUX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $3.59 · Nov 16 | $3.59 · Nov 16 | PASS |  |  |
| QTUM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QTUM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $124.47 · Nov 16 | $124.47 · Nov 16 | PASS |  |  |
| RBOT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| RTX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| RTX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RTX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $194.89 · Nov 16 | $194.89 · Nov 16 | PASS |  |  |
| RY.TO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.07 / Mom: -0.4 / Rank: 4/11] XLF WEAKENING | RS 100.07 Mom -0.4 Rank 4/11 | PASS |  |  |
| RY.TO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| RY.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RY.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $285.69 · Nov 16 | $285.69 · Nov 16 | PASS |  |  |
| SETM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SETM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $22.41 · Nov 16 | $22.41 · Nov 16 | PASS |  |  |
| SGRD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $461.90 · Nov 16 | $461.90 · Nov 16 | PASS |  |  |
| SNDK.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.72 / Mom: +2.91 / Rank: 10/11] XLU IMPROVING | RS 96.72 Mom 2.91 Rank 10/11 | PASS |  |  |
| SO | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| SO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $94.64 · Nov 16 | $94.64 · Nov 16 | PASS |  |  |
| SOXL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $48.76 · Nov 16 | $48.76 · Nov 16 | PASS |  |  |
| SOXL.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL.NE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.30 · Nov 16 | $12.30 · Nov 16 | PASS |  |  |
| SOXX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $141.22 · Nov 16 | $141.22 · Nov 16 | PASS |  |  |
| SPCL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.24 / Rank: 7/11] X | RS 98.43 Mom 2.24 Rank 7/11 | PASS |  |  |
| TSLA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| TSLA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $379.74 · Nov 16 | $379.74 · Nov 16 | PASS |  |  |
| TSLL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSLL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $9.80 · Nov 16 | $9.80 · Nov 16 | PASS |  |  |
| TSM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| TSM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| TSM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| TSM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $373.45 · Nov 16 | $373.45 · Nov 16 | PASS |  |  |
| UBOT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| UBOT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $15.51 · Nov 16 | $15.51 · Nov 16 | PASS |  |  |
| UFO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $30.44 · Nov 16 | $30.44 · Nov 16 | PASS |  |  |
| URAA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| URAA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $11.71 · Nov 16 | $11.71 · Nov 16 | PASS |  |  |
| V | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Financials (XLF) — RS: 100.07 / Mom: -0.4 / Rank: 4/11] XLF WEAKENING | RS 100.07 Mom -0.4 Rank 4/11 | PASS |  |  |
| V | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | WEAKENING | WEAKENING | PASS |  |  |
| V | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| V | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $426.46 · Nov 16 | $426.46 · Nov 16 | PASS |  |  |
| VFV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VRT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.43 / Mom: -0.5 / Rank: 11/11] XLI LAGGING | RS 95.43 Mom -0.5 Rank 11/11 | PASS |  |  |
| VRT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| VRT | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| VRT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $188.67 · Nov 16 | $188.67 · Nov 16 | PASS |  |  |
| WDC.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WELL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.15 / Mom: +1.25 / Rank: 9/11] XLRE IMPROV | RS 97.15 Mom 1.25 Rank 9/11 | PASS |  |  |
| WELL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| WELL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| WMT | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Staples (XLP) — RS: 101.54 / Mom: +3.19 / Rank: 3/11] XLP LE | RS 101.54 Mom 3.19 Rank 3/11 | PASS |  |  |
| WMT | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| WMT | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ Earnings in 2 days | ⚠️ Earnings in 2 days | PASS |  |  |
| WMT | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-19, 2 days | 2026-11-19, 2 days | PASS |  |  |
| WMT | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $128.41 · Nov 16 | $128.41 · Nov 16 | PASS |  |  |
| XCHP.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XCHP.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $105.33 · Nov 16 | $105.33 · Nov 16 | PASS |  |  |
| XDRV.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XEQT.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XEQT.TO | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $44.86 · Nov 16 | $44.86 · Nov 16 | PASS |  |  |
| XETM.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XGD.TO | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Energy (XLE) — RS: 106.41 / Mom: +0.35 / Rank: 1/11] XLE LEADING | RS 106.41 Mom 0.35 Rank 1/11 | PASS |  |  |
| XOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LEADING | LEADING | PASS |  |  |
| XOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| XOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $166.87 · Nov 16 | $166.87 · Nov 16 | PASS |  |  |
| AAPL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $360.83 | $360.83 | PASS |  |  |
| AAPL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $352.78 | $352.78 | PASS |  |  |
| AAPL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $360.83 / $243.42 | $360.83 / $243.42 | PASS |  |  |
| AAPL | PD3 | % from High | -2.2% | -2.2% | PASS |  |  |
| AAPL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15.1B | bars: $15,395,834,259 | PASS | LOW |  |
| AAPU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $51.04 | $51.04 | PASS |  |  |
| AAPU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $48.77 | $48.77 | PASS |  |  |
| AAPU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $51.04 / $26.20 | $51.04 / $26.20 | PASS |  |  |
| AAPU | PD3 | % from High | -4.4% | -4.4% | PASS |  |  |
| AAPU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $52M | bars: $47,550,848 | PASS | LOW |  |
| ABBV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.93 | $302.93 | PASS |  |  |
| ABBV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $294.55 | $294.55 | PASS |  |  |
| ABBV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.93 / $190.75 | $302.93 / $190.75 | PASS |  |  |
| ABBV | PD3 | % from High | -2.8% | -2.8% | PASS |  |  |
| ABBV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.4B | bars: $1,463,069,750 | PASS | LOW |  |
| AIPO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $34.79 | $34.79 | PASS |  |  |
| AIPO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $22.69 | $22.69 | PASS |  |  |
| AIPO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $34.79 / $20.65 | $34.79 / $20.65 | PASS |  |  |
| AIPO | PD3 | % from High | -34.8% | -34.8% | PASS |  |  |
| AIPO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $34M | bars: $36,869,790 | PASS | LOW |  |
| ALAB | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $499.48 | $499.48 | PASS |  |  |
| ALAB | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $202.34 | $202.34 | PASS |  |  |
| ALAB | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $499.48 / $97.89 | $499.48 / $97.89 | PASS |  |  |
| ALAB | PD3 | % from High | -59.5% | -59.5% | PASS |  |  |
| ALAB | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $862M | bars: $918,330,207 | PASS | LOW |  |
| AMD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $658.52 | $658.52 | PASS |  |  |
| AMD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $504.28 | $504.28 | PASS |  |  |
| AMD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $658.52 / $188.22 | $658.52 / $188.22 | PASS |  |  |
| AMD | PD3 | % from High | -23.4% | -23.4% | PASS |  |  |
| AMD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $12.6B | bars: $13,766,165,239 | PASS | LOW |  |
| AMD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $16.97 | $16.97 | PASS |  |  |
| AMD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $13.76 | $13.76 | PASS |  |  |
| AMD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $16.97 / $4.93 | $16.97 / $4.93 | PASS |  |  |
| AMD.TO | PD3 | % from High | -18.9% | -18.9% | PASS |  |  |
| AMD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $29M | bars: $31,334,134 | PASS | LOW |  |
| AMZN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $287.20 | $287.20 | PASS |  |  |
| AMZN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $257.75 | $257.75 | PASS |  |  |
| AMZN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $287.20 / $196.00 | $287.20 / $196.00 | PASS |  |  |
| AMZN | PD3 | % from High | -10.3% | -10.3% | PASS |  |  |
| AMZN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $10.1B | bars: $10,652,393,899 | PASS | LOW |  |
| AMZU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $47.14 | $47.14 | PASS |  |  |
| AMZU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $35.27 | $35.27 | PASS |  |  |
| AMZU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $47.14 / $24.54 | $47.14 / $24.54 | PASS |  |  |
| AMZU | PD3 | % from High | -25.2% | -25.2% | PASS |  |  |
| AMZU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $67M | bars: $68,223,170 | PASS | LOW |  |
| ANET.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $33.41 | $33.41 | PASS |  |  |
| ANET.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.85 / $20.97 | $38.85 / $20.97 | PASS |  |  |
| ANET.TO | PD3 | % from High | -14.0% | -14.0% | PASS |  |  |
| ASML.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $56.75 | $56.75 | PASS |  |  |
| ASML.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $41.62 | $41.62 | PASS |  |  |
| ASML.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $56.75 / $26.65 | $56.75 / $26.65 | PASS |  |  |
| ASML.TO | PD3 | % from High | -26.7% | -26.7% | PASS |  |  |
| ASML.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,848,844 | PASS | LOW |  |
| ASTL.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $7.67 | $7.67 | PASS |  |  |
| ASTL.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $8.31 / $4.46 | $8.31 / $4.46 | PASS |  |  |
| ASTL.TO | PD3 | % from High | -7.7% | -7.7% | PASS |  |  |
| ASTL.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5M | bars: $4,565,721 | PASS | LOW |  |
| ATD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $94.68 | $94.68 | PASS |  |  |
| ATD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $83.90 | $83.90 | PASS |  |  |
| ATD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $94.68 / $67.83 | $94.68 / $67.83 | PASS |  |  |
| ATD.TO | PD3 | % from High | -11.4% | -11.4% | PASS |  |  |
| ATD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $115M | bars: $109,299,886 | PASS | LOW |  |
| AVGC | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.48 | $17.48 | PASS |  |  |
| AVGC | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.79 / $13.71 | $31.79 / $13.71 | PASS |  |  |
| AVGC | PD3 | % from High | -45.0% | -45.0% | PASS |  |  |
| AVGO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $495.00 | $495.00 | PASS |  |  |
| AVGO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $333.40 | $333.40 | PASS |  |  |
| AVGO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $495.00 / $289.77 | $495.00 / $289.77 | PASS |  |  |
| AVGO | PD3 | % from High | -32.6% | -32.6% | PASS |  |  |
| AVGO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.5B | bars: $8,404,157,162 | PASS | LOW |  |
| AVGO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.64 | $12.64 | PASS |  |  |
| AVGO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $18.88 / $11.00 | $18.88 / $11.00 | PASS |  |  |
| AVGO.TO | PD3 | % from High | -33.0% | -33.1% | PASS |  |  |
| AVGO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $14M | bars: $14,603,927 | PASS | LOW |  |
| BDT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $86.42 | $86.42 | PASS |  |  |
| BDT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $75.18 | $75.18 | PASS |  |  |
| BDT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $86.42 / $23.93 | $86.42 / $23.93 | PASS |  |  |
| BDT.TO | PD3 | % from High | -13.0% | -13.0% | PASS |  |  |
| BDT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $29M | bars: $29,868,112 | PASS | LOW |  |
| BOTZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.12 | $30.12 | PASS |  |  |
| BOTZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $41.69 / $30.08 | $41.69 / $30.08 | PASS |  |  |
| BOTZ | PD3 | % from High | -27.8% | -27.8% | PASS |  |  |
| BOTZ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $21M | bars: $21,258,274 | PASS | LOW |  |
| BRK-B | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $596.92 | $596.92 | PASS |  |  |
| BRK-B | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $592.85 | $592.85 | PASS |  |  |
| BRK-B | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $596.92 / $464.01 | $596.92 / $464.01 | PASS |  |  |
| BRK-B | PD3 | % from High | -0.7% | -0.7% | PASS |  |  |
| BRK-B | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.7B | bars: $2,842,510,624 | PASS | LOW |  |
| BRKU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $31.20 | $31.20 | PASS |  |  |
| BRKU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.81 | $30.81 | PASS |  |  |
| BRKU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.20 / $20.25 | $31.20 / $20.25 | PASS |  |  |
| BRKU | PD3 | % from High | -1.3% | -1.3% | PASS |  |  |
| BRKU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,751,514 | PASS | LOW |  |
| CAMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $215.99 | $215.99 | PASS |  |  |
| CAMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $93.25 | $93.25 | PASS |  |  |
| CAMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $215.99 / $89.13 | $215.99 / $89.13 | PASS |  |  |
| CAMT | PD3 | % from High | -56.8% | -56.8% | PASS |  |  |
| CAMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $44M | bars: $47,949,150 | PASS | LOW |  |
| CARS.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $38.16 | $38.16 | PASS |  |  |
| CARS.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $20.19 | $20.19 | PASS |  |  |
| CARS.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.16 / $20.11 | $38.16 / $20.11 | PASS |  |  |
| CARS.TO | PD3 | % from High | -47.1% | -47.1% | PASS |  |  |
| CARS.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| CAT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $570.49 | $570.49 | PASS |  |  |
| CAT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,073.46 / $537.08 | $1,073.46 / $537.08 | PASS |  |  |
| CAT | PD3 | % from High | -46.9% | -46.9% | PASS |  |  |
| CAT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.7B | bars: $1,742,027,726 | PASS | LOW |  |
| CCO.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $182.72 | $182.72 | PASS |  |  |
| CCO.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $94.40 | $94.40 | PASS |  |  |
| CCO.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $182.72 / $92.52 | $182.72 / $92.52 | PASS |  |  |
| CCO.TO | PD3 | % from High | -48.3% | -48.3% | PASS |  |  |
| CCO.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $107M | bars: $114,174,723 | PASS | LOW |  |
| CEG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $380.78 | $380.78 | PASS |  |  |
| CEG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $277.82 | $277.82 | PASS |  |  |
| CEG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $380.78 / $228.63 | $380.78 / $228.63 | PASS |  |  |
| CEG | PD3 | % from High | -27.0% | -27.0% | PASS |  |  |
| CEG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $979M | bars: $1,059,261,828 | PASS | LOW |  |
| CGY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $95.15 | $95.15 | PASS |  |  |
| CGY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $86.08 | $86.08 | PASS |  |  |
| CGY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $95.15 / $44.20 | $95.15 / $44.20 | PASS |  |  |
| CGY.TO | PD3 | % from High | -9.5% | -9.5% | PASS |  |  |
| CGY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,620,447 | PASS | LOW |  |
| CNQ.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $78.60 | $78.60 | PASS |  |  |
| CNQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $68.96 | $68.96 | PASS |  |  |
| CNQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $78.60 / $40.51 | $78.60 / $40.51 | PASS |  |  |
| CNQ.TO | PD3 | % from High | -12.3% | -12.3% | PASS |  |  |
| CNQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $921M | bars: $889,851,841 | PASS | LOW |  |
| CNR.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $184.26 | $184.26 | PASS |  |  |
| CNR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $182.77 | $182.77 | PASS |  |  |
| CNR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $184.26 / $125.06 | $184.26 / $125.06 | PASS |  |  |
| CNR.TO | PD3 | % from High | -0.8% | -0.8% | PASS |  |  |
| CNR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $233M | bars: $227,330,788 | PASS | LOW |  |
| COP | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $140.52 | $140.52 | PASS |  |  |
| COP | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $154.28 / $85.70 | $154.28 / $85.70 | PASS |  |  |
| COP | PD3 | % from High | -8.9% | -8.9% | PASS |  |  |
| COP | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $949M | bars: $954,984,881 | PASS | LOW |  |
| COPP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $70.54 | $70.54 | PASS |  |  |
| COPP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $46.48 | $46.48 | PASS |  |  |
| COPP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $70.54 / $42.17 | $70.54 / $42.17 | PASS |  |  |
| COPP.TO | PD3 | % from High | -34.1% | -34.1% | PASS |  |  |
| COPX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $99.99 | $99.99 | PASS |  |  |
| COPX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $65.51 | $65.51 | PASS |  |  |
| COPX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $99.99 / $56.93 | $99.99 / $56.93 | PASS |  |  |
| COPX | PD3 | % from High | -34.5% | -34.5% | PASS |  |  |
| COPX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $188M | bars: $180,925,572 | PASS | LOW |  |
| COPZ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $8.68 | $8.68 | PASS |  |  |
| COPZ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $26.40 / $8.68 | $26.40 / $8.68 | PASS |  |  |
| COPZ | PD3 | % from High | -67.1% | -67.1% | PASS |  |  |
| COST | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,117.00 | $1,117.00 | PASS |  |  |
| COST | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,113.74 | $1,113.74 | PASS |  |  |
| COST | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,117.00 / $844.06 | $1,117.00 / $844.06 | PASS |  |  |
| COST | PD3 | % from High | -0.3% | -0.3% | PASS |  |  |
| COST | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.5B | bars: $2,604,120,138 | PASS | LOW |  |
| COTG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $17.80 | $17.80 | PASS |  |  |
| COTG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.04 | $17.04 | PASS |  |  |
| COTG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $17.80 / $10.95 | $17.80 / $10.95 | PASS |  |  |
| COTG | PD3 | % from High | -4.3% | -4.3% | PASS |  |  |
| COTG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2M | bars: $1,858,904 | PASS | LOW |  |
| CSU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3,436.53 | $3,436.53 | PASS |  |  |
| CSU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $3,565.00 / $2,192.51 | $3,565.00 / $2,192.51 | PASS |  |  |
| CSU.TO | PD3 | % from High | -3.6% | -3.6% | PASS |  |  |
| CSU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $204M | bars: $210,226,286 | PASS | LOW |  |
| CVX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $236.48 | $236.48 | PASS |  |  |
| CVX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $217.14 | $217.14 | PASS |  |  |
| CVX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $236.48 / $142.51 | $236.48 / $142.51 | PASS |  |  |
| CVX | PD3 | % from High | -8.2% | -8.2% | PASS |  |  |
| CVX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.8B | bars: $1,892,055,036 | PASS | LOW |  |
| DRAL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $4.20 | $4.20 | PASS |  |  |
| DRAL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $25.52 / $4.06 | $25.52 / $4.06 | PASS |  |  |
| DRAL | PD3 | % from High | -83.5% | -83.5% | PASS |  |  |
| DRAM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.27 | $39.27 | PASS |  |  |
| DRAM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $81.34 / $26.14 | $81.34 / $26.14 | PASS |  |  |
| DRAM | PD3 | % from High | -51.7% | -51.7% | PASS |  |  |
| DRAM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.3B | bars: $1,354,088,584 | PASS | LOW |  |
| DRIV | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $42.76 | $42.76 | PASS |  |  |
| DRIV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $27.35 | $27.35 | PASS |  |  |
| DRIV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $42.76 / $27.05 | $42.76 / $27.05 | PASS |  |  |
| DRIV | PD3 | % from High | -36.0% | -36.0% | PASS |  |  |
| DRIV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1M | bars: $1,124,218 | PASS | LOW |  |
| DUK | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.87 | $131.87 | PASS |  |  |
| DUK | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $130.59 | $130.59 | PASS |  |  |
| DUK | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.87 / $110.06 | $131.87 / $110.06 | PASS |  |  |
| DUK | PD3 | % from High | -1.0% | -1.0% | PASS |  |  |
| DUK | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $543M | bars: $564,552,584 | PASS | LOW |  |
| ELIL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $43.56 | $43.56 | PASS |  |  |
| ELIL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $41.12 | $41.12 | PASS |  |  |
| ELIL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $43.56 / $16.21 | $43.56 / $16.21 | PASS |  |  |
| ELIL | PD3 | % from High | -5.6% | -5.6% | PASS |  |  |
| ELIL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,611,942 | PASS | LOW |  |
| EQIX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,118.65 | $1,118.65 | PASS |  |  |
| EQIX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,043.06 | $1,043.06 | PASS |  |  |
| EQIX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,118.65 / $709.79 | $1,118.65 / $709.79 | PASS |  |  |
| EQIX | PD3 | % from High | -6.8% | -6.8% | PASS |  |  |
| EQIX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $593M | bars: $607,405,130 | PASS | LOW |  |
| ETN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $478.00 | $478.00 | PASS |  |  |
| ETN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $336.88 | $336.88 | PASS |  |  |
| ETN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $478.00 / $311.92 | $478.00 / $311.92 | PASS |  |  |
| ETN | PD3 | % from High | -29.5% | -29.5% | PASS |  |  |
| ETN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $817M | bars: $879,217,628 | PASS | LOW |  |
| FCX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $80.24 | $80.24 | PASS |  |  |
| FCX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $55.19 | $55.19 | PASS |  |  |
| FCX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.24 / $38.85 | $80.24 / $38.85 | PASS |  |  |
| FCX | PD3 | % from High | -31.2% | -31.2% | PASS |  |  |
| FCX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $700M | bars: $654,032,768 | PASS | LOW |  |
| FINN.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $35.83 | $35.83 | PASS |  |  |
| FINN.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $32.10 | $32.10 | PASS |  |  |
| FINN.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $35.83 / $21.66 | $35.83 / $21.66 | PASS |  |  |
| FINN.NE | PD3 | % from High | -10.4% | -10.4% | PASS |  |  |
| FINN.NE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $9M | bars: $9,478,994 | PASS | LOW |  |
| GDX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $117.18 | $117.18 | PASS |  |  |
| GDX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $78.95 | $78.95 | PASS |  |  |
| GDX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $117.18 / $69.74 | $117.18 / $69.74 | PASS |  |  |
| GDX | PD3 | % from High | -32.6% | -32.6% | PASS |  |  |
| GDX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.8B | bars: $1,664,207,893 | PASS | LOW |  |
| GDXU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $65.00 | $65.00 | PASS |  |  |
| GDXU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $24.30 | $24.30 | PASS |  |  |
| GDXU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $65.00 / $20.83 | $65.00 / $20.83 | PASS |  |  |
| GDXU.TO | PD3 | % from High | -62.6% | -62.6% | PASS |  |  |
| GDXU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $6M | bars: $5,502,152 | PASS | LOW |  |
| GE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $325.18 | $325.18 | PASS |  |  |
| GE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $388.25 / $268.17 | $388.25 / $268.17 | PASS |  |  |
| GE | PD3 | % from High | -16.2% | -16.2% | PASS |  |  |
| GE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.5B | bars: $1,575,709,117 | PASS | LOW |  |
| GEV | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $763.57 | $763.57 | PASS |  |  |
| GEV | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,195.24 / $528.87 | $1,195.24 / $528.87 | PASS |  |  |
| GEV | PD3 | % from High | -36.1% | -36.1% | PASS |  |  |
| GEV | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,344,033,147 | PASS | LOW |  |
| GEV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $51.03 | $51.03 | PASS |  |  |
| GEV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.44 / $42.23 | $80.44 / $42.23 | PASS |  |  |
| GEV.TO | PD3 | % from High | -36.6% | -36.6% | PASS |  |  |
| GEV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,694,674 | PASS | LOW |  |
| GGLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $153.00 | $153.00 | PASS |  |  |
| GGLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $64.83 | $64.83 | PASS |  |  |
| GGLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $153.00 / $62.13 | $153.00 / $62.13 | PASS |  |  |
| GGLL | PD3 | % from High | -57.6% | -57.6% | PASS |  |  |
| GGLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $111M | bars: $125,460,442 | PASS | LOW |  |
| GIB-A.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.27 | $131.27 | PASS |  |  |
| GIB-A.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $117.80 | $117.80 | PASS |  |  |
| GIB-A.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.27 / $83.04 | $131.27 / $83.04 | PASS |  |  |
| GIB-A.TO | PD3 | % from High | -10.3% | -10.3% | PASS |  |  |
| GIB-A.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $71M | bars: $72,902,163 | PASS | LOW |  |
| GOOGL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $408.10 | $408.10 | PASS |  |  |
| GOOGL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $283.72 | $283.72 | PASS |  |  |
| GOOGL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $408.10 / $270.00 | $408.10 / $270.00 | PASS |  |  |
| GOOGL | PD3 | % from High | -30.5% | -30.5% | PASS |  |  |
| GOOGL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $8.5B | bars: $9,086,020,647 | PASS | LOW |  |
| GRID | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $199.99 | $199.99 | PASS |  |  |
| GRID | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $156.14 | $156.14 | PASS |  |  |
| GRID | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $199.99 / $144.62 | $199.99 / $144.62 | PASS |  |  |
| GRID | PD3 | % from High | -21.9% | -21.9% | PASS |  |  |
| GRID | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $88M | bars: $91,217,300 | PASS | LOW |  |
| HD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $397.63 | $397.63 | PASS |  |  |
| HD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $347.51 | $347.51 | PASS |  |  |
| HD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $397.63 / $277.15 | $397.63 / $277.15 | PASS |  |  |
| HD | PD3 | % from High | -12.6% | -12.6% | PASS |  |  |
| HD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,743,199,553 | PASS | LOW |  |
| HURA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $73.95 | $73.95 | PASS |  |  |
| HURA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $37.54 | $37.54 | PASS |  |  |
| HURA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $73.95 / $36.76 | $73.95 / $36.76 | PASS |  |  |
| HURA.TO | PD3 | % from High | -49.2% | -49.2% | PASS |  |  |
| HXQ.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $111.87 | $111.87 | PASS |  |  |
| HXQ.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $128.37 / $91.48 | $128.37 / $91.48 | PASS |  |  |
| HXQ.TO | PD3 | % from High | -12.9% | -12.9% | PASS |  |  |
| HXQ.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,659,491 | PASS | LOW |  |
| JNJ | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $290.25 | $290.25 | PASS |  |  |
| JNJ | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $282.55 | $282.55 | PASS |  |  |
| JNJ | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $290.25 / $189.28 | $290.25 / $189.28 | PASS |  |  |
| JNJ | PD3 | % from High | -2.7% | -2.7% | PASS |  |  |
| JNJ | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.0B | bars: $2,065,996,558 | PASS | LOW |  |
| JPM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $366.50 | $366.50 | PASS |  |  |
| JPM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $338.21 | $338.21 | PASS |  |  |
| JPM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $366.50 / $279.10 | $366.50 / $279.10 | PASS |  |  |
| JPM | PD3 | % from High | -7.7% | -7.7% | PASS |  |  |
| JPM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.4B | bars: $2,553,309,631 | PASS | LOW |  |
| KEYS | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $389.93 | $389.93 | PASS |  |  |
| KEYS | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $285.63 | $285.63 | PASS |  |  |
| KEYS | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $389.93 / $167.23 | $389.93 / $167.23 | PASS |  |  |
| KEYS | PD3 | % from High | -26.7% | -26.7% | PASS |  |  |
| KEYS | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $387M | bars: $369,176,775 | PASS | LOW |  |
| LIN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $523.46 | $523.46 | PASS |  |  |
| LIN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $546.40 / $384.00 | $546.40 / $384.00 | PASS |  |  |
| LIN | PD3 | % from High | -4.2% | -4.2% | PASS |  |  |
| LIN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.1B | bars: $1,097,433,890 | PASS | LOW |  |
| LLY | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $1,475.25 | $1,475.25 | PASS |  |  |
| LLY | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $1,431.67 | $1,431.67 | PASS |  |  |
| LLY | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $1,475.25 / $850.51 | $1,475.25 / $850.51 | PASS |  |  |
| LLY | PD3 | % from High | -3.0% | -3.0% | PASS |  |  |
| LLY | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.7B | bars: $3,699,845,940 | PASS | LOW |  |
| MDA.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $67.90 | $67.90 | PASS |  |  |
| MDA.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $40.08 | $40.08 | PASS |  |  |
| MDA.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $67.90 / $20.85 | $67.90 / $20.85 | PASS |  |  |
| MDA.TO | PD3 | % from High | -41.0% | -41.0% | PASS |  |  |
| MDA.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $63M | bars: $65,676,130 | PASS | LOW |  |
| META | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $779.82 | $779.82 | PASS |  |  |
| META | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $626.41 | $626.41 | PASS |  |  |
| META | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $779.82 / $520.26 | $779.82 / $520.26 | PASS |  |  |
| META | PD3 | % from High | -19.7% | -19.7% | PASS |  |  |
| META | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $13.3B | bars: $13,970,779,634 | PASS | LOW |  |
| METU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $39.74 | $39.74 | PASS |  |  |
| METU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $22.15 | $22.15 | PASS |  |  |
| METU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $39.74 / $16.85 | $39.74 / $16.85 | PASS |  |  |
| METU | PD3 | % from High | -44.3% | -44.3% | PASS |  |  |
| METU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $120M | bars: $112,109,963 | PASS | LOW |  |
| MRVL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $329.88 | $329.88 | PASS |  |  |
| MRVL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $145.36 | $145.36 | PASS |  |  |
| MRVL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $329.88 / $70.69 | $329.88 / $70.69 | PASS |  |  |
| MRVL | PD3 | % from High | -55.9% | -55.9% | PASS |  |  |
| MRVL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.6B | bars: $3,492,937,153 | PASS | LOW |  |
| MSFT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $559.15 | $559.15 | PASS |  |  |
| MSFT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $517.99 | $517.99 | PASS |  |  |
| MSFT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $559.15 / $349.20 | $559.15 / $349.20 | PASS |  |  |
| MSFT | PD3 | % from High | -7.4% | -7.4% | PASS |  |  |
| MSFT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $12.0B | bars: $12,211,215,398 | PASS | LOW |  |
| MSFU | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $50.05 | $50.05 | PASS |  |  |
| MSFU | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.17 | $39.17 | PASS |  |  |
| MSFU | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $50.05 / $19.47 | $50.05 / $19.47 | PASS |  |  |
| MSFU | PD3 | % from High | -21.7% | -21.7% | PASS |  |  |
| MSFU | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $98M | bars: $95,206,809 | PASS | LOW |  |
| MTRX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $29.24 | $29.24 | PASS |  |  |
| MTRX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $39.30 / $28.00 | $39.30 / $28.00 | PASS |  |  |
| MTRX.TO | PD3 | % from High | -25.6% | -25.6% | PASS |  |  |
| MU.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $55.28 | $55.28 | PASS |  |  |
| MU.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $31.43 | $31.43 | PASS |  |  |
| MU.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $55.28 / $8.62 | $55.28 / $8.62 | PASS |  |  |
| MU.TO | PD3 | % from High | -43.1% | -43.1% | PASS |  |  |
| MU.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $55M | bars: $58,275,432 | PASS | LOW |  |
| NEE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $85.34 | $85.34 | PASS |  |  |
| NEE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $97.30 / $74.41 | $97.30 / $74.41 | PASS |  |  |
| NEE | PD3 | % from High | -12.3% | -12.3% | PASS |  |  |
| NEE | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.1B | bars: $1,076,481,662 | PASS | LOW |  |
| NEM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $135.29 | $135.29 | PASS |  |  |
| NEM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $110.31 | $110.31 | PASS |  |  |
| NEM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $135.29 / $81.34 | $135.29 / $81.34 | PASS |  |  |
| NEM | PD3 | % from High | -18.5% | -18.5% | PASS |  |  |
| NEM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $764M | bars: $715,053,573 | PASS | LOW |  |
| NFLX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $115.25 | $115.25 | PASS |  |  |
| NFLX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $60.75 | $60.75 | PASS |  |  |
| NFLX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $115.25 / $60.48 | $115.25 / $60.48 | PASS |  |  |
| NFLX | PD3 | % from High | -47.3% | -47.3% | PASS |  |  |
| NFLX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,407,673,524 | PASS | LOW |  |
| NFXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $49.78 | $49.78 | PASS |  |  |
| NFXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $10.22 | $10.22 | PASS |  |  |
| NFXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $49.78 / $10.13 | $49.78 / $10.13 | PASS |  |  |
| NFXL | PD3 | % from High | -79.5% | -79.5% | PASS |  |  |
| NFXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15M | bars: $16,734,704 | PASS | LOW |  |
| NTR.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $98.62 | $98.62 | PASS |  |  |
| NTR.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $114.19 / $74.44 | $114.19 / $74.44 | PASS |  |  |
| NTR.TO | PD3 | % from High | -13.6% | -13.6% | PASS |  |  |
| NTR.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $178M | bars: $190,697,155 | PASS | LOW |  |
| NVDA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $243.37 | $243.37 | PASS |  |  |
| NVDA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $156.14 | $156.14 | PASS |  |  |
| NVDA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $243.37 / $148.80 | $243.37 / $148.80 | PASS |  |  |
| NVDA | PD3 | % from High | -35.8% | -35.8% | PASS |  |  |
| NVDA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $23.4B | bars: $23,758,416,354 | PASS | LOW |  |
| NVDL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $41.59 | $41.59 | PASS |  |  |
| NVDL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $16.35 | $16.35 | PASS |  |  |
| NVDL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $41.59 / $7.18 | $41.59 / $7.18 | PASS |  |  |
| NVDL | PD3 | % from High | -60.7% | -60.7% | PASS |  |  |
| NVDL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $275M | bars: $270,510,708 | PASS | LOW |  |
| ONTO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $386.46 | $386.46 | PASS |  |  |
| ONTO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $196.77 | $196.77 | PASS |  |  |
| ONTO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $386.46 / $121.58 | $386.46 / $121.58 | PASS |  |  |
| ONTO | PD3 | % from High | -49.1% | -49.1% | PASS |  |  |
| ONTO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $197M | bars: $205,049,822 | PASS | LOW |  |
| ORBX.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $14.60 | $14.60 | PASS |  |  |
| ORBX.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $31.62 / $12.81 | $31.62 / $12.81 | PASS |  |  |
| ORBX.TO | PD3 | % from High | -53.8% | -53.8% | PASS |  |  |
| ORCL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $250.25 | $250.25 | PASS |  |  |
| ORCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $119.09 | $119.09 | PASS |  |  |
| ORCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $250.25 / $109.21 | $250.25 / $109.21 | PASS |  |  |
| ORCL | PD3 | % from High | -52.4% | -52.4% | PASS |  |  |
| ORCL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.0B | bars: $4,400,319,797 | PASS | LOW |  |
| PG | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $173.57 | $173.57 | PASS |  |  |
| PG | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $173.02 | $173.02 | PASS |  |  |
| PG | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $173.57 / $133.74 | $173.57 / $133.74 | PASS |  |  |
| PG | PD3 | % from High | -0.3% | -0.3% | PASS |  |  |
| PG | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.6B | bars: $1,629,103,376 | PASS | LOW |  |
| PLD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $153.35 | $153.35 | PASS |  |  |
| PLD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $127.60 | $127.60 | PASS |  |  |
| PLD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $153.35 / $121.40 | $153.35 / $121.40 | PASS |  |  |
| PLD | PD3 | % from High | -16.8% | -16.8% | PASS |  |  |
| PLD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $468M | bars: $490,283,059 | PASS | LOW |  |
| PNG.V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $10.72 | $10.72 | PASS |  |  |
| PNG.V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3.22 | $3.22 | PASS |  |  |
| PNG.V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $10.72 / $3.16 | $10.72 / $3.16 | PASS |  |  |
| PNG.V | PD3 | % from High | -70.0% | -70.0% | PASS |  |  |
| PNG.V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4M | bars: $3,821,985 | PASS | LOW |  |
| QCOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $259.92 | $259.92 | PASS |  |  |
| QCOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $168.52 | $168.52 | PASS |  |  |
| QCOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $259.92 / $121.99 | $259.92 / $121.99 | PASS |  |  |
| QCOM | PD3 | % from High | -35.2% | -35.2% | PASS |  |  |
| QCOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.2B | bars: $2,296,344,642 | PASS | LOW |  |
| QPUX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $3.59 | $3.59 | PASS |  |  |
| QPUX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $80.28 / $3.54 | $80.28 / $3.54 | PASS |  |  |
| QPUX | PD3 | % from High | -95.5% | -95.5% | PASS |  |  |
| QTUM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $124.47 | $124.47 | PASS |  |  |
| QTUM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $169.21 / $97.17 | $169.21 / $97.17 | PASS |  |  |
| QTUM | PD3 | % from High | -26.4% | -26.4% | PASS |  |  |
| QTUM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $41M | bars: $41,488,091 | PASS | LOW |  |
| RBOT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $27.53 | $27.53 | PASS |  |  |
| RBOT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $38.15 / $27.49 | $38.15 / $27.49 | PASS |  |  |
| RBOT.TO | PD3 | % from High | -27.8% | -27.8% | PASS |  |  |
| RTX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $194.89 | $194.89 | PASS |  |  |
| RTX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $226.41 / $164.95 | $226.41 / $164.95 | PASS |  |  |
| RTX | PD3 | % from High | -13.9% | -13.9% | PASS |  |  |
| RTX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $910M | bars: $936,012,235 | PASS | LOW |  |
| RY.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.65 | $302.65 | PASS |  |  |
| RY.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $285.69 | $285.69 | PASS |  |  |
| RY.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.65 / $197.56 | $302.65 / $197.56 | PASS |  |  |
| RY.TO | PD3 | % from High | -5.6% | -5.6% | PASS |  |  |
| RY.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $919M | bars: $935,080,511 | PASS | LOW |  |
| SETM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $40.55 | $40.55 | PASS |  |  |
| SETM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $22.41 | $22.41 | PASS |  |  |
| SETM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $40.55 / $22.36 | $40.55 / $22.36 | PASS |  |  |
| SETM | PD3 | % from High | -44.7% | -44.7% | PASS |  |  |
| SETM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $3,623,159 | PASS | LOW |  |
| SGRD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $18.03 | $18.03 | PASS |  |  |
| SGRD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $22.49 / $17.20 | $22.49 / $17.20 | PASS |  |  |
| SGRD.TO | PD3 | % from High | -19.8% | -19.8% | PASS |  |  |
| SMH | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $671.83 | $671.83 | PASS |  |  |
| SMH | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $461.90 | $461.90 | PASS |  |  |
| SMH | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $671.83 / $314.07 | $671.83 / $314.07 | PASS |  |  |
| SMH | PD3 | % from High | -31.2% | -31.2% | PASS |  |  |
| SMH | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.0B | bars: $4,223,616,371 | PASS | LOW |  |
| SNDK.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $19.60 | $19.60 | PASS |  |  |
| SNDK.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $57.55 / $19.37 | $57.55 / $19.37 | PASS |  |  |
| SNDK.TO | PD3 | % from High | -65.9% | -65.9% | PASS |  |  |
| SNDK.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $24M | bars: $24,497,570 | PASS | LOW |  |
| SO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $99.58 | $99.58 | PASS |  |  |
| SO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $94.64 | $94.64 | PASS |  |  |
| SO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $99.58 / $81.69 | $99.58 / $81.69 | PASS |  |  |
| SO | PD3 | % from High | -5.0% | -5.0% | PASS |  |  |
| SO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $653M | bars: $677,800,274 | PASS | LOW |  |
| SOXL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $302.00 | $302.00 | PASS |  |  |
| SOXL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $48.76 | $48.76 | PASS |  |  |
| SOXL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $302.00 / $28.12 | $302.00 / $28.12 | PASS |  |  |
| SOXL | PD3 | % from High | -83.9% | -83.9% | PASS |  |  |
| SOXL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5.0B | bars: $5,632,505,425 | PASS | LOW |  |
| SOXL.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $74.21 | $74.21 | PASS |  |  |
| SOXL.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.30 | $12.30 | PASS |  |  |
| SOXL.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $74.21 / $7.92 | $74.21 / $7.92 | PASS |  |  |
| SOXL.NE | PD3 | % from High | -83.4% | -83.4% | PASS |  |  |
| SOXL.NE | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| SOXX | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $218.65 | $218.65 | PASS |  |  |
| SOXX | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $141.22 | $141.22 | PASS |  |  |
| SOXX | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $218.65 / $86.81 | $218.65 / $86.81 | PASS |  |  |
| SOXX | PD3 | % from High | -35.4% | -35.4% | PASS |  |  |
| SOXX | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.9B | bars: $4,178,037,168 | PASS | LOW |  |
| SPCL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $10.44 | $10.44 | PASS |  |  |
| SPCL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $83.85 / $8.20 | $83.85 / $8.20 | PASS |  |  |
| SPCL | PD3 | % from High | -87.5% | -87.5% | PASS |  |  |
| TSLA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $498.83 | $498.83 | PASS |  |  |
| TSLA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $379.74 | $379.74 | PASS |  |  |
| TSLA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $498.83 / $297.38 | $498.83 / $297.38 | PASS |  |  |
| TSLA | PD3 | % from High | -23.9% | -23.9% | PASS |  |  |
| TSLA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $14.3B | bars: $13,955,402,469 | PASS | LOW |  |
| TSLL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $23.74 | $23.74 | PASS |  |  |
| TSLL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $9.80 | $9.80 | PASS |  |  |
| TSLL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $23.74 / $6.70 | $23.74 / $6.70 | PASS |  |  |
| TSLL | PD3 | % from High | -58.7% | -58.7% | PASS |  |  |
| TSLL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $659M | bars: $547,684,463 | PASS | LOW |  |
| TSM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $487.47 | $487.47 | PASS |  |  |
| TSM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $373.45 | $373.45 | PASS |  |  |
| TSM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $487.47 / $266.82 | $487.47 / $266.82 | PASS |  |  |
| TSM | PD3 | % from High | -23.4% | -23.4% | PASS |  |  |
| TSM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.4B | bars: $4,638,761,597 | PASS | LOW |  |
| UBOT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $32.08 | $32.08 | PASS |  |  |
| UBOT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $15.51 | $15.51 | PASS |  |  |
| UBOT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $32.08 / $15.46 | $32.08 / $15.46 | PASS |  |  |
| UBOT | PD3 | % from High | -51.7% | -51.7% | PASS |  |  |
| UFO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.54 | $39.54 | PASS |  |  |
| UFO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $68.12 / $30.78 | $68.12 / $30.78 | PASS |  |  |
| UFO | PD3 | % from High | -42.0% | -42.0% | PASS |  |  |
| UFO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $10M | bars: $10,150,472 | PASS | LOW |  |
| URA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $62.28 | $62.28 | PASS |  |  |
| URA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $30.44 | $30.44 | PASS |  |  |
| URA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $62.28 / $30.30 | $62.28 / $30.30 | PASS |  |  |
| URA | PD3 | % from High | -51.1% | -51.1% | PASS |  |  |
| URA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $118M | bars: $120,397,932 | PASS | LOW |  |
| URAA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $62.21 | $62.21 | PASS |  |  |
| URAA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $11.71 | $11.71 | PASS |  |  |
| URAA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $62.21 / $11.50 | $62.21 / $11.50 | PASS |  |  |
| URAA | PD3 | % from High | -81.2% | -81.2% | PASS |  |  |
| V | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $442.23 | $442.23 | PASS |  |  |
| V | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $426.46 | $426.46 | PASS |  |  |
| V | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $442.23 / $293.89 | $442.23 / $293.89 | PASS |  |  |
| V | PD3 | % from High | -3.6% | -3.6% | PASS |  |  |
| V | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.7B | bars: $2,774,881,006 | PASS | LOW |  |
| VFV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $197.83 | $197.83 | PASS |  |  |
| VFV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $191.40 | $191.40 | PASS |  |  |
| VFV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $197.83 / $155.29 | $197.83 / $155.29 | PASS |  |  |
| VFV.TO | PD3 | % from High | -3.3% | -3.3% | PASS |  |  |
| VFV.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $56M | bars: $59,109,296 | PASS | LOW |  |
| VRT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $379.94 | $379.94 | PASS |  |  |
| VRT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $188.67 | $188.67 | PASS |  |  |
| VRT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $379.94 / $147.82 | $379.94 / $147.82 | PASS |  |  |
| VRT | PD3 | % from High | -50.3% | -50.3% | PASS |  |  |
| VRT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.2B | bars: $1,280,441,361 | PASS | LOW |  |
| WDC.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $17.89 | $17.89 | PASS |  |  |
| WDC.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $48.85 / $15.70 | $48.85 / $15.70 | PASS |  |  |
| WDC.TO | PD3 | % from High | -63.4% | -63.4% | PASS |  |  |
| WDC.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3M | bars: $2,868,161 | PASS | LOW |  |
| WELL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $255.20 | $255.20 | PASS |  |  |
| WELL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $244.65 | $244.65 | PASS |  |  |
| WELL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $255.20 / $181.47 | $255.20 / $181.47 | PASS |  |  |
| WELL | PD3 | % from High | -4.1% | -4.1% | PASS |  |  |
| WELL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $669M | bars: $681,156,605 | PASS | LOW |  |
| WMT | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $135.16 | $135.16 | PASS |  |  |
| WMT | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $128.41 | $128.41 | PASS |  |  |
| WMT | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $135.16 / $98.88 | $135.16 / $98.88 | PASS |  |  |
| WMT | PD3 | % from High | -5.0% | -5.0% | PASS |  |  |
| WMT | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $3.1B | bars: $2,782,777,671 | PASS | LOW |  |
| XCHP.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $161.26 | $161.26 | PASS |  |  |
| XCHP.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $105.33 | $105.33 | PASS |  |  |
| XCHP.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $161.26 / $64.67 | $161.26 / $64.67 | PASS |  |  |
| XCHP.TO | PD3 | % from High | -34.7% | -34.7% | PASS |  |  |
| XCHP.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $5M | bars: $5,237,218 | PASS | LOW |  |
| XDRV.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $61.36 | $61.36 | PASS |  |  |
| XDRV.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $39.69 | $39.69 | PASS |  |  |
| XDRV.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $61.36 / $38.62 | $61.36 / $38.62 | PASS |  |  |
| XDRV.TO | PD3 | % from High | -35.3% | -35.3% | PASS |  |  |
| XDRV.TO | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| XEQT.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $46.38 | $46.38 | PASS |  |  |
| XEQT.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $44.86 | $44.86 | PASS |  |  |
| XEQT.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $46.38 / $37.96 | $46.38 / $37.96 | PASS |  |  |
| XEQT.TO | PD3 | % from High | -3.3% | -3.3% | PASS |  |  |
| XEQT.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $37M | bars: $39,831,732 | PASS | LOW |  |
| XETM.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $61.57 | $61.57 | PASS |  |  |
| XETM.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $93.94 / $61.54 | $93.94 / $61.54 | PASS |  |  |
| XETM.TO | PD3 | % from High | -34.5% | -34.5% | PASS |  |  |
| XGD.TO | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $69.54 | $69.54 | PASS |  |  |
| XGD.TO | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $50.80 | $50.80 | PASS |  |  |
| XGD.TO | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $69.54 / $43.30 | $69.54 / $43.30 | PASS |  |  |
| XGD.TO | PD3 | % from High | -26.9% | -26.9% | PASS |  |  |
| XGD.TO | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $26M | bars: $23,446,029 | PASS | LOW |  |
| XOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $187.32 | $187.32 | PASS |  |  |
| XOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $166.87 | $166.87 | PASS |  |  |
| XOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $187.32 / $111.24 | $187.32 / $111.24 | PASS |  |  |
| XOM | PD3 | % from High | -10.9% | -10.9% | PASS |  |  |
| XOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.3B | bars: $2,252,651,219 | PASS | LOW |  |
| AAPL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $352.78 / RS 1.18 | $352.78 / RS 1.18 | PASS |  |  |
| AAPL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.18 | 1.18 | PASS |  |  |
| AAPL | RS2 | Stock 52W Return and S&P 52W Return | +29.5% / +10.1% | +29.5% / +10.1% | PASS |  |  |
| AAPL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| AAPL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.5% clears | +29.5% clears | PASS |  |  |
| AAPU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $48.77 / RS 1.21 | $48.77 / RS 1.21 | PASS |  |  |
| AAPU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.21 | 1.21 | PASS |  |  |
| AAPU | RS2 | Stock 52W Return and S&P 52W Return | +33.5% / +10.1% | +33.5% / +10.1% | PASS |  |  |
| AAPU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 67 | 67 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market | Ahead of the market | PASS |  |  |
| AAPU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +33.5% clears | +33.5% clears | PASS |  |  |
| ABBV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $294.55 / RS 1.15 | $294.55 / RS 1.15 | PASS |  |  |
| ABBV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| ABBV | RS2 | Stock 52W Return and S&P 52W Return | +26.8% / +10.1% | +26.8% / +10.1% | PASS |  |  |
| ABBV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ABBV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ABBV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| ABBV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +26.8% clears | +26.8% clears | PASS |  |  |
| AIPO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $22.69 / RS 0.91 | $22.69 / RS 0.91 | PASS |  |  |
| AIPO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.91 | 0.91 | PASS |  |  |
| AIPO | RS2 | Stock 52W Return and S&P 52W Return | +0.3% / +10.1% | +0.3% / +10.1% | PASS |  |  |
| AIPO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AIPO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AIPO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| AIPO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +0.3% under | +0.3% under | PASS |  |  |
| ALAB | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $202.34 / RS 1.27 | $202.34 / RS 1.27 | PASS |  |  |
| ALAB | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.27 | 1.27 | PASS |  |  |
| ALAB | RS2 | Stock 52W Return and S&P 52W Return | +40.2% / +10.1% | +40.2% / +10.1% | PASS |  |  |
| ALAB | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ALAB | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ALAB | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| ALAB | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +40.2% clears | +40.2% clears | PASS |  |  |
| AMD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.85 | 1.86 | PASS |  |  |
| AMD | RS2 | Stock 52W Return and S&P 52W Return | +104.3% / +10.1% | +104.3% / +10.1% | PASS |  |  |
| AMD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +104.3% clears | +104.3% clears | PASS |  |  |
| AMD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $13.76 / RS 1.90 | $13.76 / RS 1.90 | PASS |  |  |
| AMD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.90 | 1.90 | PASS |  |  |
| AMD.TO | RS2 | Stock 52W Return and S&P 52W Return | +109.4% / +10.1% | +109.4% / +10.1% | PASS |  |  |
| AMD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +109.4% clears | +109.4% clears | PASS |  |  |
| AMZN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $257.75 / RS 1.00 | $257.75 / RS 1.00 | PASS |  |  |
| AMZN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.00 | 1.00 | PASS |  |  |
| AMZN | RS2 | Stock 52W Return and S&P 52W Return | +9.8% / +10.1% | +9.8% / +10.1% | PASS |  |  |
| AMZN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| AMZN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +9.8% clears | +9.8% clears | PASS |  |  |
| AMZU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $35.27 / RS 0.83 | $35.27 / RS 0.83 | PASS |  |  |
| AMZU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.83 | 0.83 | PASS |  |  |
| AMZU | RS2 | Stock 52W Return and S&P 52W Return | -8.2% / +10.1% | -8.2% / +10.1% | PASS |  |  |
| AMZU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMZU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 37 | 37 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMZU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| AMZU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -8.2% negative | -8.2% negative | PASS |  |  |
| ANET.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $33.41 / RS 1.27 | $33.41 / RS 1.27 | PASS |  |  |
| ANET.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.27 | 1.27 | PASS |  |  |
| ANET.TO | RS2 | Stock 52W Return and S&P 52W Return | +40.1% / +10.1% | +40.1% / +10.1% | PASS |  |  |
| ANET.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ANET.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| ANET.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +40.1% clears | +40.1% clears | PASS |  |  |
| ASML.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.35 | 1.36 | PASS |  |  |
| ASML.TO | RS2 | Stock 52W Return and S&P 52W Return | +49.2% / +10.1% | +49.2% / +10.1% | PASS |  |  |
| ASML.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ASML.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 78 | 78 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASML.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ASML.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.2% clears | +49.2% clears | PASS |  |  |
| ASTL.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $7.67 / RS 1.42 | $7.67 / RS 1.42 | PASS |  |  |
| ASTL.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.42 | 1.42 | PASS |  |  |
| ASTL.TO | RS2 | Stock 52W Return and S&P 52W Return | +56.2% / +10.1% | +56.2% / +10.1% | PASS |  |  |
| ASTL.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 83 | 83 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ASTL.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market | Well ahead of the market | PASS |  |  |
| ASTL.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +56.2% clears | +56.2% clears | PASS |  |  |
| ATD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.10 | PASS |  |  |
| ATD.TO | RS2 | Stock 52W Return and S&P 52W Return | +20.6% / +10.1% | +20.6% / +10.1% | PASS |  |  |
| ATD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ATD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ATD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| ATD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +20.6% clears | +20.6% clears | PASS |  |  |
| AVGO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $333.40 / RS 0.88 | $333.40 / RS 0.88 | PASS |  |  |
| AVGO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| AVGO | RS2 | Stock 52W Return and S&P 52W Return | -2.6% / +10.1% | -2.6% / +10.1% | PASS |  |  |
| AVGO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AVGO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| AVGO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -2.6% negative | -2.6% negative | PASS |  |  |
| AVGO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.64 / RS 0.87 | $12.64 / RS 0.87 | PASS |  |  |
| AVGO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.87 | 0.87 | PASS |  |  |
| AVGO.TO | RS2 | Stock 52W Return and S&P 52W Return | -4.1% / +10.1% | -4.1% / +10.1% | PASS |  |  |
| AVGO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AVGO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| AVGO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.1% negative | -4.1% negative | PASS |  |  |
| BDT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $75.18 / RS 2.72 | $75.18 / RS 2.72 | PASS |  |  |
| BDT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.72 | 2.72 | PASS |  |  |
| BDT.TO | RS2 | Stock 52W Return and S&P 52W Return | +199.4% / +10.1% | +199.4% / +10.1% | PASS |  |  |
| BDT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BDT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BDT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| BDT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +199.4% clears | +199.4% clears | PASS |  |  |
| BOTZ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.12 / RS 0.78 | $30.12 / RS 0.78 | PASS |  |  |
| BOTZ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.78 | 0.78 | PASS |  |  |
| BOTZ | RS2 | Stock 52W Return and S&P 52W Return | -13.9% / +10.1% | -13.9% / +10.1% | PASS |  |  |
| BOTZ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BOTZ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BOTZ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| BOTZ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -13.9% negative | -13.9% negative | PASS |  |  |
| BRK-B | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $592.85 / RS 1.06 | $592.85 / RS 1.06 | PASS |  |  |
| BRK-B | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.06 | 1.06 | PASS |  |  |
| BRK-B | RS2 | Stock 52W Return and S&P 52W Return | +16.5% / +10.1% | +16.5% / +10.1% | PASS |  |  |
| BRK-B | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRK-B | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRK-B | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRK-B | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +16.5% clears | +16.5% clears | PASS |  |  |
| BRKU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.81 / RS 1.07 | $30.81 / RS 1.07 | PASS |  |  |
| BRKU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.07 | 1.07 | PASS |  |  |
| BRKU | RS2 | Stock 52W Return and S&P 52W Return | +18.3% / +10.1% | +18.3% / +10.1% | PASS |  |  |
| BRKU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| BRKU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| BRKU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| BRKU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +18.3% clears | +18.3% clears | PASS |  |  |
| CAMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $93.25 / RS 0.88 | $93.25 / RS 0.88 | PASS |  |  |
| CAMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| CAMT | RS2 | Stock 52W Return and S&P 52W Return | -3.1% / +10.1% | -3.1% / +10.1% | PASS |  |  |
| CAMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| CAMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -3.1% negative | -3.1% negative | PASS |  |  |
| CARS.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $20.19 / RS 0.68 | $20.19 / RS 0.68 | PASS |  |  |
| CARS.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.68 | 0.68 | PASS |  |  |
| CARS.TO | RS2 | Stock 52W Return and S&P 52W Return | -24.7% / +10.1% | -24.7% / +10.1% | PASS |  |  |
| CARS.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CARS.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 25 | 25 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CARS.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CARS.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -24.7% negative | -24.7% negative | PASS |  |  |
| CAT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $570.49 / RS 0.94 | $570.49 / RS 0.94 | PASS |  |  |
| CAT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| CAT | RS2 | Stock 52W Return and S&P 52W Return | +3.0% / +10.1% | +3.0% / +10.1% | PASS |  |  |
| CAT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CAT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CAT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| CAT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.0% under | +3.0% under | PASS |  |  |
| CCO.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $94.40 / RS 0.72 | $94.40 / RS 0.72 | PASS |  |  |
| CCO.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.72 | 0.72 | PASS |  |  |
| CCO.TO | RS2 | Stock 52W Return and S&P 52W Return | -20.4% / +10.1% | -20.4% / +10.1% | PASS |  |  |
| CCO.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CCO.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 28 | 28 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CCO.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| CCO.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -20.4% negative | -20.4% negative | PASS |  |  |
| CEG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.74 | 0.75 | PASS |  |  |
| CEG | RS2 | Stock 52W Return and S&P 52W Return | -17.9% / +10.1% | -17.9% / +10.1% | PASS |  |  |
| CEG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CEG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 30 | 30 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CEG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| CEG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -17.9% negative | -17.9% negative | PASS |  |  |
| CGY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $86.08 / RS 1.54 | $86.08 / RS 1.54 | PASS |  |  |
| CGY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.54 | 1.54 | PASS |  |  |
| CGY.TO | RS2 | Stock 52W Return and S&P 52W Return | +69.8% / +10.1% | +69.7% / +10.1% | PASS |  |  |
| CGY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CGY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 93 | 93 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CGY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CGY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +69.8% clears | +69.7% clears | PASS |  |  |
| CNQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $68.96 / RS 1.39 | $68.96 / RS 1.39 | PASS |  |  |
| CNQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.39 | 1.39 | PASS |  |  |
| CNQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +53.4% / +10.1% | +53.4% / +10.1% | PASS |  |  |
| CNQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 81 | 81 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CNQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +53.4% clears | +53.4% clears | PASS |  |  |
| CNR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $182.77 / RS 1.26 | $182.77 / RS 1.26 | PASS |  |  |
| CNR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.26 | 1.26 | PASS |  |  |
| CNR.TO | RS2 | Stock 52W Return and S&P 52W Return | +38.8% / +10.1% | +38.8% / +10.1% | PASS |  |  |
| CNR.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CNR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 71 | 71 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CNR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| CNR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +38.8% clears | +38.8% clears | PASS |  |  |
| COP | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $140.52 / RS 1.40 | $140.52 / RS 1.40 | PASS |  |  |
| COP | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.40 | 1.40 | PASS |  |  |
| COP | RS2 | Stock 52W Return and S&P 52W Return | +53.8% / +10.1% | +53.8% / +10.1% | PASS |  |  |
| COP | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COP | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 82 | 82 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COP | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| COP | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +53.8% clears | +53.8% clears | PASS |  |  |
| COPP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.95 | PASS |  |  |
| COPP.TO | RS2 | Stock 52W Return and S&P 52W Return | +4.1% / +10.1% | +4.1% / +10.1% | PASS |  |  |
| COPP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| COPP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.1% under | +4.1% under | PASS |  |  |
| COPX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $65.51 / RS 0.97 | $65.51 / RS 0.97 | PASS |  |  |
| COPX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.97 | 0.97 | PASS |  |  |
| COPX | RS2 | Stock 52W Return and S&P 52W Return | +7.1% / +10.1% | +7.1% / +10.1% | PASS |  |  |
| COPX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COPX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 48 | 48 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COPX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| COPX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +7.1% clears | +7.1% clears | PASS |  |  |
| COST | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,113.74 / RS 1.10 | $1,113.74 / RS 1.10 | PASS |  |  |
| COST | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.10 | 1.10 | PASS |  |  |
| COST | RS2 | Stock 52W Return and S&P 52W Return | +20.7% / +10.1% | +20.7% / +10.1% | PASS |  |  |
| COST | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COST | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COST | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| COST | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +20.7% clears | +20.7% clears | PASS |  |  |
| COTG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $17.04 / RS 1.15 | $17.04 / RS 1.15 | PASS |  |  |
| COTG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| COTG | RS2 | Stock 52W Return and S&P 52W Return | +26.1% / +10.1% | +26.1% / +10.1% | PASS |  |  |
| COTG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| COTG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| COTG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum accelerating) | Somewhat ahead of the market (momentum accelerating) | PASS |  |  |
| COTG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +26.1% clears | +26.1% clears | PASS |  |  |
| CSU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3,436.53 / RS 0.96 | $3,436.53 / RS 0.96 | PASS |  |  |
| CSU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.96 | PASS |  |  |
| CSU.TO | RS2 | Stock 52W Return and S&P 52W Return | +6.1% / +10.1% | +6.1% / +10.1% | PASS |  |  |
| CSU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CSU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| CSU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +6.1% clears | +6.1% clears | PASS |  |  |
| CVX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $217.14 / RS 1.30 | $217.14 / RS 1.30 | PASS |  |  |
| CVX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.30 | 1.30 | PASS |  |  |
| CVX | RS2 | Stock 52W Return and S&P 52W Return | +43.2% / +10.1% | +43.2% / +10.1% | PASS |  |  |
| CVX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| CVX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| CVX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| CVX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +43.2% clears | +43.2% clears | PASS |  |  |
| DRIV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $27.35 / RS 0.85 | $27.35 / RS 0.85 | PASS |  |  |
| DRIV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| DRIV | RS2 | Stock 52W Return and S&P 52W Return | -6.7% / +10.1% | -6.7% / +10.1% | PASS |  |  |
| DRIV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DRIV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DRIV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| DRIV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -6.7% negative | -6.7% negative | PASS |  |  |
| DUK | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $130.59 / RS 1.00 | $130.59 / RS 1.00 | PASS |  |  |
| DUK | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.00 | 1.00 | PASS |  |  |
| DUK | RS2 | Stock 52W Return and S&P 52W Return | +10.1% / +10.1% | +10.1% / +10.1% | PASS |  |  |
| DUK | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DUK | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DUK | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| DUK | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +10.1% clears | +10.1% clears | PASS |  |  |
| ELIL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $41.12 / RS 1.44 | $41.12 / RS 1.44 | PASS |  |  |
| ELIL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.44 | 1.44 | PASS |  |  |
| ELIL | RS2 | Stock 52W Return and S&P 52W Return | +58.6% / +10.1% | +58.6% / +10.1% | PASS |  |  |
| ELIL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ELIL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 85 | 85 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ELIL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ELIL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +58.6% clears | +58.6% clears | PASS |  |  |
| EQIX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,043.06 / RS 1.23 | $1,043.06 / RS 1.23 | PASS |  |  |
| EQIX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.23 | 1.23 | PASS |  |  |
| EQIX | RS2 | Stock 52W Return and S&P 52W Return | +35.6% / +10.1% | +35.6% / +10.1% | PASS |  |  |
| EQIX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| EQIX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 69 | 69 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| EQIX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| EQIX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +35.6% clears | +35.6% clears | PASS |  |  |
| ETN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $336.88 / RS 0.87 | $336.88 / RS 0.87 | PASS |  |  |
| ETN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.87 | 0.87 | PASS |  |  |
| ETN | RS2 | Stock 52W Return and S&P 52W Return | -4.4% / +10.1% | -4.4% / +10.1% | PASS |  |  |
| ETN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ETN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 39 | 39 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ETN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| ETN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.4% negative | -4.4% negative | PASS |  |  |
| FCX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $55.19 / RS 1.25 | $55.19 / RS 1.25 | PASS |  |  |
| FCX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.25 | 1.25 | PASS |  |  |
| FCX | RS2 | Stock 52W Return and S&P 52W Return | +37.4% / +10.1% | +37.4% / +10.1% | PASS |  |  |
| FCX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FCX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 70 | 70 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FCX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| FCX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +37.4% clears | +37.4% clears | PASS |  |  |
| FINN.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $32.10 / RS 1.27 | $32.10 / RS 1.27 | PASS |  |  |
| FINN.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.27 | 1.27 | PASS |  |  |
| FINN.NE | RS2 | Stock 52W Return and S&P 52W Return | +40.0% / +10.1% | +40.1% / +10.1% | PASS |  |  |
| FINN.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| FINN.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 72 | 72 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| FINN.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| FINN.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +40.0% clears | +40.1% clears | PASS |  |  |
| GDX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $78.95 / RS 0.95 | $78.95 / RS 0.95 | PASS |  |  |
| GDX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.95 | PASS |  |  |
| GDX | RS2 | Stock 52W Return and S&P 52W Return | +4.4% / +10.1% | +4.4% / +10.1% | PASS |  |  |
| GDX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| GDX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.4% under | +4.4% under | PASS |  |  |
| GDXU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $24.30 / RS 0.73 | $24.30 / RS 0.73 | PASS |  |  |
| GDXU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.73 | 0.73 | PASS |  |  |
| GDXU.TO | RS2 | Stock 52W Return and S&P 52W Return | -19.8% / +10.1% | -19.8% / +10.1% | PASS |  |  |
| GDXU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GDXU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 28 | 28 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GDXU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| GDXU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -19.8% negative | -19.8% negative | PASS |  |  |
| GE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $325.18 / RS 0.97 | $325.18 / RS 0.97 | PASS |  |  |
| GE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.97 | 0.97 | PASS |  |  |
| GE | RS2 | Stock 52W Return and S&P 52W Return | +7.3% / +10.1% | +7.3% / +10.1% | PASS |  |  |
| GE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 48 | 48 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +7.3% clears | +7.3% clears | PASS |  |  |
| GEV | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $763.57 / RS 1.20 | $763.57 / RS 1.20 | PASS |  |  |
| GEV | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.20 | 1.20 | PASS |  |  |
| GEV | RS2 | Stock 52W Return and S&P 52W Return | +32.4% / +10.1% | +32.4% / +10.1% | PASS |  |  |
| GEV | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GEV | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 66 | 66 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| GEV | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +32.4% clears | +32.4% clears | PASS |  |  |
| GEV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $51.03 / RS 1.03 | $51.03 / RS 1.03 | PASS |  |  |
| GEV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.03 | 1.03 | PASS |  |  |
| GEV.TO | RS2 | Stock 52W Return and S&P 52W Return | +13.4% / +10.1% | +13.4% / +10.1% | PASS |  |  |
| GEV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GEV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| GEV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +13.4% clears | +13.4% clears | PASS |  |  |
| GGLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $64.83 / RS 0.74 | $64.83 / RS 0.74 | PASS |  |  |
| GGLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.74 | 0.74 | PASS |  |  |
| GGLL | RS2 | Stock 52W Return and S&P 52W Return | -18.7% / +10.1% | -18.7% / +10.1% | PASS |  |  |
| GGLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GGLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 29 | 29 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GGLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| GGLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -18.7% negative | -18.7% negative | PASS |  |  |
| GIB-A.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $117.80 / RS 0.88 | $117.80 / RS 0.88 | PASS |  |  |
| GIB-A.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| GIB-A.TO | RS2 | Stock 52W Return and S&P 52W Return | -3.6% / +10.1% | -3.6% / +10.1% | PASS |  |  |
| GIB-A.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GIB-A.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GIB-A.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| GIB-A.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -3.6% negative | -3.6% negative | PASS |  |  |
| GOOGL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.93 | PASS |  |  |
| GOOGL | RS2 | Stock 52W Return and S&P 52W Return | +2.9% / +10.1% | +2.9% / +10.1% | PASS |  |  |
| GOOGL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GOOGL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GOOGL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum fading) | Slightly behind the market (momentum fading) | PASS |  |  |
| GOOGL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.9% under | +2.9% under | PASS |  |  |
| GRID | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $156.14 / RS 0.93 | $156.14 / RS 0.93 | PASS |  |  |
| GRID | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.93 | 0.93 | PASS |  |  |
| GRID | RS2 | Stock 52W Return and S&P 52W Return | +2.3% / +10.1% | +2.2% / +10.1% | PASS |  |  |
| GRID | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| GRID | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| GRID | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| GRID | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.3% under | +2.2% under | PASS |  |  |
| HD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $347.51 / RS 0.87 | $347.51 / RS 0.87 | PASS |  |  |
| HD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.87 | 0.87 | PASS |  |  |
| HD | RS2 | Stock 52W Return and S&P 52W Return | -4.1% / +10.1% | -4.1% / +10.1% | PASS |  |  |
| HD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| HD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -4.1% negative | -4.1% negative | PASS |  |  |
| HURA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $37.54 / RS 0.66 | $37.54 / RS 0.66 | PASS |  |  |
| HURA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.66 | 0.66 | PASS |  |  |
| HURA.TO | RS2 | Stock 52W Return and S&P 52W Return | -27.5% / +10.1% | -27.5% / +10.1% | PASS |  |  |
| HURA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| HURA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 23 | 23 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HURA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| HURA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -27.5% negative | -27.5% negative | PASS |  |  |
| HXQ.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $111.87 / RS 1.02 | $111.87 / RS 1.02 | PASS |  |  |
| HXQ.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.02 | 1.02 | PASS |  |  |
| HXQ.TO | RS2 | Stock 52W Return and S&P 52W Return | +11.9% / +10.1% | +11.9% / +10.1% | PASS |  |  |
| HXQ.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| HXQ.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| HXQ.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +11.9% clears | +11.9% clears | PASS |  |  |
| JNJ | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $282.55 / RS 1.34 | $282.55 / RS 1.34 | PASS |  |  |
| JNJ | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.34 | 1.34 | PASS |  |  |
| JNJ | RS2 | Stock 52W Return and S&P 52W Return | +47.5% / +10.1% | +47.5% / +10.1% | PASS |  |  |
| JNJ | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JNJ | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 77 | 77 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JNJ | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| JNJ | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +47.5% clears | +47.5% clears | PASS |  |  |
| JPM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $338.21 / RS 1.01 | $338.21 / RS 1.01 | PASS |  |  |
| JPM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.01 | 1.01 | PASS |  |  |
| JPM | RS2 | Stock 52W Return and S&P 52W Return | +11.4% / +10.1% | +11.4% / +10.1% | PASS |  |  |
| JPM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| JPM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 51 | 51 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| JPM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| JPM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +11.4% clears | +11.4% clears | PASS |  |  |
| KEYS | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $285.63 / RS 1.45 | $285.63 / RS 1.45 | PASS |  |  |
| KEYS | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.45 | 1.45 | PASS |  |  |
| KEYS | RS2 | Stock 52W Return and S&P 52W Return | +59.5% / +10.1% | +59.5% / +10.1% | PASS |  |  |
| KEYS | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| KEYS | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 86 | 86 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| KEYS | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| KEYS | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +59.5% clears | +59.5% clears | PASS |  |  |
| LIN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $523.46 / RS 1.14 | $523.46 / RS 1.14 | PASS |  |  |
| LIN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.14 | 1.14 | PASS |  |  |
| LIN | RS2 | Stock 52W Return and S&P 52W Return | +25.3% / +10.1% | +25.3% / +10.1% | PASS |  |  |
| LIN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LIN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 61 | 61 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LIN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| LIN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.3% clears | +25.3% clears | PASS |  |  |
| LLY | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $1,431.67 / RS 1.27 | $1,431.67 / RS 1.27 | PASS |  |  |
| LLY | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.27 | 1.27 | PASS |  |  |
| LLY | RS2 | Stock 52W Return and S&P 52W Return | +39.6% / +10.1% | +39.6% / +10.1% | PASS |  |  |
| LLY | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| LLY | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 71 | 71 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| LLY | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| LLY | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +39.6% clears | +39.6% clears | PASS |  |  |
| MDA.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $40.08 / RS 1.64 | $40.08 / RS 1.64 | PASS |  |  |
| MDA.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.64 | 1.64 | PASS |  |  |
| MDA.TO | RS2 | Stock 52W Return and S&P 52W Return | +80.0% / +10.1% | +80.1% / +10.1% | PASS |  |  |
| MDA.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MDA.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MDA.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MDA.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +80.0% clears | +80.1% clears | PASS |  |  |
| META | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $626.41 / RS 0.93 | $626.41 / RS 0.93 | PASS |  |  |
| META | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.93 | 0.93 | PASS |  |  |
| META | RS2 | Stock 52W Return and S&P 52W Return | +2.8% / +10.1% | +2.8% / +10.1% | PASS |  |  |
| META | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| META | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| META | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| META | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.8% under | +2.8% under | PASS |  |  |
| METU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $22.15 / RS 0.71 | $22.15 / RS 0.71 | PASS |  |  |
| METU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.71 | 0.71 | PASS |  |  |
| METU | RS2 | Stock 52W Return and S&P 52W Return | -21.6% / +10.1% | -21.6% / +10.1% | PASS |  |  |
| METU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| METU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 27 | 27 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| METU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| METU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -21.6% negative | -21.6% negative | PASS |  |  |
| MRVL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $145.36 / RS 1.53 | $145.36 / RS 1.53 | PASS |  |  |
| MRVL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.53 | 1.53 | PASS |  |  |
| MRVL | RS2 | Stock 52W Return and S&P 52W Return | +68.1% / +10.1% | +68.1% / +10.1% | PASS |  |  |
| MRVL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MRVL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 92 | 92 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MRVL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MRVL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +68.1% clears | +68.1% clears | PASS |  |  |
| MSFT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $517.99 / RS 0.92 | $517.99 / RS 0.92 | PASS |  |  |
| MSFT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| MSFT | RS2 | Stock 52W Return and S&P 52W Return | +1.5% / +10.1% | +1.5% / +10.1% | PASS |  |  |
| MSFT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| MSFT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +1.5% under | +1.5% under | PASS |  |  |
| MSFU | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.17 / RS 0.72 | $39.17 / RS 0.72 | PASS |  |  |
| MSFU | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.72 | 0.72 | PASS |  |  |
| MSFU | RS2 | Stock 52W Return and S&P 52W Return | -21.2% / +10.1% | -21.2% / +10.1% | PASS |  |  |
| MSFU | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MSFU | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 27 | 27 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MSFU | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| MSFU | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -21.2% negative | -21.2% negative | PASS |  |  |
| MTRX.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $29.24 / RS 0.89 | $29.24 / RS 0.89 | PASS |  |  |
| MTRX.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.89 | 0.89 | PASS |  |  |
| MTRX.TO | RS2 | Stock 52W Return and S&P 52W Return | -1.7% / +10.1% | -1.7% / +10.1% | PASS |  |  |
| MTRX.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 41 | 41 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MTRX.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum fading) | Behind the market (momentum fading) | PASS |  |  |
| MTRX.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -1.7% negative | -1.7% negative | PASS |  |  |
| MU.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $31.43 / RS 2.58 | $31.43 / RS 2.58 | PASS |  |  |
| MU.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 2.58 | 2.58 | PASS |  |  |
| MU.TO | RS2 | Stock 52W Return and S&P 52W Return | +184.2% / +10.1% | +184.2% / +10.1% | PASS |  |  |
| MU.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| MU.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| MU.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| MU.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +184.2% clears | +184.2% clears | PASS |  |  |
| NEE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $85.34 / RS 0.95 | $85.34 / RS 0.95 | PASS |  |  |
| NEE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.95 | PASS |  |  |
| NEE | RS2 | Stock 52W Return and S&P 52W Return | +4.7% / +10.1% | +4.7% / +10.1% | PASS |  |  |
| NEE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| NEE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.7% under | +4.7% under | PASS |  |  |
| NEM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $110.31 / RS 1.14 | $110.31 / RS 1.14 | PASS |  |  |
| NEM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.14 | 1.14 | PASS |  |  |
| NEM | RS2 | Stock 52W Return and S&P 52W Return | +25.6% / +10.1% | +25.6% / +10.1% | PASS |  |  |
| NEM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NEM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 61 | 61 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NEM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| NEM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.6% clears | +25.6% clears | PASS |  |  |
| NFLX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $60.75 / RS 0.50 | $60.75 / RS 0.50 | PASS |  |  |
| NFLX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.50 | 0.50 | PASS |  |  |
| NFLX | RS2 | Stock 52W Return and S&P 52W Return | -45.4% / +10.1% | -45.4% / +10.1% | PASS |  |  |
| NFLX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFLX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 10 | 10 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFLX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFLX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -45.4% negative | -45.4% negative | PASS |  |  |
| NFXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $10.22 / RS 0.20 | $10.22 / RS 0.20 | PASS |  |  |
| NFXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.20 | 0.20 | PASS |  |  |
| NFXL | RS2 | Stock 52W Return and S&P 52W Return | -78.1% / +10.1% | -78.1% / +10.1% | PASS |  |  |
| NFXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NFXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NFXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| NFXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -78.1% negative | -78.1% negative | PASS |  |  |
| NTR.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $98.62 / RS 1.16 | $98.62 / RS 1.16 | PASS |  |  |
| NTR.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.16 | 1.16 | PASS |  |  |
| NTR.TO | RS2 | Stock 52W Return and S&P 52W Return | +27.2% / +10.1% | +27.2% / +10.1% | PASS |  |  |
| NTR.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NTR.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| NTR.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +27.2% clears | +27.2% clears | PASS |  |  |
| NVDA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $156.14 / RS 0.75 | $156.14 / RS 0.75 | PASS |  |  |
| NVDA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.75 | 0.75 | PASS |  |  |
| NVDA | RS2 | Stock 52W Return and S&P 52W Return | -17.9% / +10.1% | -17.9% / +10.1% | PASS |  |  |
| NVDA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 30 | 30 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -17.9% negative | -17.9% negative | PASS |  |  |
| NVDL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $16.35 / RS 1.42 | $16.35 / RS 1.42 | PASS |  |  |
| NVDL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.42 | 1.42 | PASS |  |  |
| NVDL | RS2 | Stock 52W Return and S&P 52W Return | +56.6% / +10.1% | +56.6% / +10.1% | PASS |  |  |
| NVDL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 84 | 84 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| NVDL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +56.6% clears | +56.6% clears | PASS |  |  |
| ONTO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $196.77 / RS 1.40 | $196.77 / RS 1.40 | PASS |  |  |
| ONTO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.40 | 1.40 | PASS |  |  |
| ONTO | RS2 | Stock 52W Return and S&P 52W Return | +53.8% / +10.1% | +53.8% / +10.1% | PASS |  |  |
| ONTO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ONTO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 82 | 82 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ONTO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| ONTO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +53.8% clears | +53.8% clears | PASS |  |  |
| ORCL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.48 | 0.49 | PASS |  |  |
| ORCL | RS2 | Stock 52W Return and S&P 52W Return | -46.6% / +10.1% | -46.6% / +10.1% | PASS |  |  |
| ORCL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| ORCL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 9 | 9 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| ORCL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| ORCL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -46.6% negative | -46.6% negative | PASS |  |  |
| PG | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $173.02 / RS 1.09 | $173.02 / RS 1.09 | PASS |  |  |
| PG | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.09 | 1.09 | PASS |  |  |
| PG | RS2 | Stock 52W Return and S&P 52W Return | +20.6% / +10.1% | +20.6% / +10.1% | PASS |  |  |
| PG | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PG | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PG | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum accelerating) | Slightly ahead of the market (momentum accelerating) | PASS |  |  |
| PG | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +20.6% clears | +20.6% clears | PASS |  |  |
| PLD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $127.60 / RS 0.94 | $127.60 / RS 0.94 | PASS |  |  |
| PLD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| PLD | RS2 | Stock 52W Return and S&P 52W Return | +3.9% / +10.1% | +3.9% / +10.1% | PASS |  |  |
| PLD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PLD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PLD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| PLD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.9% under | +3.9% under | PASS |  |  |
| PNG.V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3.22 / RS 0.57 | $3.22 / RS 0.57 | PASS |  |  |
| PNG.V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.57 | 0.57 | PASS |  |  |
| PNG.V | RS2 | Stock 52W Return and S&P 52W Return | -37.6% / +10.1% | -37.6% / +10.1% | PASS |  |  |
| PNG.V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PNG.V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 15 | 15 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PNG.V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| PNG.V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -37.6% negative | -37.6% negative | PASS |  |  |
| QCOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $168.52 / RS 0.88 | $168.52 / RS 0.88 | PASS |  |  |
| QCOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.88 | 0.88 | PASS |  |  |
| QCOM | RS2 | Stock 52W Return and S&P 52W Return | -3.1% / +10.1% | -3.1% / +10.1% | PASS |  |  |
| QCOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QCOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 40 | 40 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QCOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| QCOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -3.1% negative | -3.1% negative | PASS |  |  |
| QPUX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $3.59 / RS 0.06 | $3.59 / RS 0.06 | PASS |  |  |
| QPUX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.06 | 0.06 | PASS |  |  |
| QPUX | RS2 | Stock 52W Return and S&P 52W Return | -93.9% / +10.1% | -93.9% / +10.1% | PASS |  |  |
| QPUX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QPUX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QPUX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| QPUX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -93.9% negative | -93.9% negative | PASS |  |  |
| QTUM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $124.47 / RS 1.07 | $124.47 / RS 1.07 | PASS |  |  |
| QTUM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.07 | 1.07 | PASS |  |  |
| QTUM | RS2 | Stock 52W Return and S&P 52W Return | +17.7% / +10.1% | +17.7% / +10.1% | PASS |  |  |
| QTUM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QTUM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 55 | 55 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QTUM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| QTUM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +17.7% clears | +17.7% clears | PASS |  |  |
| RBOT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $27.53 / RS 0.79 | $27.53 / RS 0.79 | PASS |  |  |
| RBOT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.79 | 0.79 | PASS |  |  |
| RBOT.TO | RS2 | Stock 52W Return and S&P 52W Return | -13.5% / +10.1% | -13.5% / +10.1% | PASS |  |  |
| RBOT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RBOT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| RBOT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -13.5% negative | -13.5% negative | PASS |  |  |
| RTX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $194.89 / RS 1.02 | $194.89 / RS 1.02 | PASS |  |  |
| RTX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.02 | 1.02 | PASS |  |  |
| RTX | RS2 | Stock 52W Return and S&P 52W Return | +12.7% / +10.1% | +12.7% / +10.1% | PASS |  |  |
| RTX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RTX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 52 | 52 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RTX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| RTX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +12.7% clears | +12.7% clears | PASS |  |  |
| RY.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $285.69 / RS 1.30 | $285.69 / RS 1.30 | PASS |  |  |
| RY.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.30 | 1.30 | PASS |  |  |
| RY.TO | RS2 | Stock 52W Return and S&P 52W Return | +42.7% / +10.1% | +42.7% / +10.1% | PASS |  |  |
| RY.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RY.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RY.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| RY.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +42.7% clears | +42.7% clears | PASS |  |  |
| SETM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $22.41 / RS 0.79 | $22.41 / RS 0.79 | PASS |  |  |
| SETM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.79 | 0.79 | PASS |  |  |
| SETM | RS2 | Stock 52W Return and S&P 52W Return | -12.9% / +10.1% | -12.9% / +10.1% | PASS |  |  |
| SETM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SETM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 33 | 33 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SETM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum fading) | Well behind the market (momentum fading) | PASS |  |  |
| SETM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -12.9% negative | -12.9% negative | PASS |  |  |
| SMH | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $461.90 / RS 1.22 | $461.90 / RS 1.22 | PASS |  |  |
| SMH | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.22 | 1.22 | PASS |  |  |
| SMH | RS2 | Stock 52W Return and S&P 52W Return | +34.3% / +10.1% | +34.3% / +10.1% | PASS |  |  |
| SMH | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SMH | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 68 | 68 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SMH | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| SMH | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +34.3% clears | +34.3% clears | PASS |  |  |
| SO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.95 | 0.96 | PASS |  |  |
| SO | RS2 | Stock 52W Return and S&P 52W Return | +5.2% / +10.1% | +5.2% / +10.1% | PASS |  |  |
| SO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 46 | 46 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| SO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +5.2% clears | +5.2% clears | PASS |  |  |
| SOXL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $48.76 / RS 1.14 | $48.76 / RS 1.14 | PASS |  |  |
| SOXL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.14 | 1.14 | PASS |  |  |
| SOXL | RS2 | Stock 52W Return and S&P 52W Return | +25.5% / +10.1% | +25.5% / +10.1% | PASS |  |  |
| SOXL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 61 | 61 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.5% clears | +25.5% clears | PASS |  |  |
| SOXL.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.30 / RS 1.10 | $12.30 / RS 1.10 | PASS |  |  |
| SOXL.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.10 | 1.10 | PASS |  |  |
| SOXL.NE | RS2 | Stock 52W Return and S&P 52W Return | +21.7% / +10.1% | +21.7% / +10.1% | PASS |  |  |
| SOXL.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +21.7% clears | +21.7% clears | PASS |  |  |
| SOXX | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $141.22 / RS 1.33 | $141.22 / RS 1.33 | PASS |  |  |
| SOXX | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.33 | 1.33 | PASS |  |  |
| SOXX | RS2 | Stock 52W Return and S&P 52W Return | +46.8% / +10.1% | +46.8% / +10.1% | PASS |  |  |
| SOXX | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXX | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 77 | 77 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXX | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| SOXX | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +46.8% clears | +46.8% clears | PASS |  |  |
| TSLA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $379.74 / RS 0.85 | $379.74 / RS 0.85 | PASS |  |  |
| TSLA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.85 | 0.85 | PASS |  |  |
| TSLA | RS2 | Stock 52W Return and S&P 52W Return | -6.1% / +10.1% | -6.1% / +10.1% | PASS |  |  |
| TSLA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 38 | 38 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market (momentum accelerating) | Behind the market (momentum accelerating) | PASS |  |  |
| TSLA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -6.1% negative | -6.1% negative | PASS |  |  |
| TSLL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $9.80 / RS 0.54 | $9.80 / RS 0.54 | PASS |  |  |
| TSLL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.54 | 0.54 | PASS |  |  |
| TSLL | RS2 | Stock 52W Return and S&P 52W Return | -40.9% / +10.1% | -40.9% / +10.1% | PASS |  |  |
| TSLL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSLL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 13 | 13 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSLL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| TSLL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -40.9% negative | -40.9% negative | PASS |  |  |
| TSM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $373.45 / RS 1.19 | $373.45 / RS 1.19 | PASS |  |  |
| TSM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.19 | 1.19 | PASS |  |  |
| TSM | RS2 | Stock 52W Return and S&P 52W Return | +31.1% / +10.1% | +31.1% / +10.1% | PASS |  |  |
| TSM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| TSM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 65 | 65 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| TSM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| TSM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +31.1% clears | +31.1% clears | PASS |  |  |
| UBOT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $15.51 / RS 0.58 | $15.51 / RS 0.58 | PASS |  |  |
| UBOT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.58 | 0.58 | PASS |  |  |
| UBOT | RS2 | Stock 52W Return and S&P 52W Return | -35.8% / +10.1% | -35.8% / +10.1% | PASS |  |  |
| UBOT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UBOT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 17 | 17 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UBOT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| UBOT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -35.8% negative | -35.8% negative | PASS |  |  |
| UFO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.54 / RS 1.08 | $39.54 / RS 1.08 | PASS |  |  |
| UFO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.08 | 1.08 | PASS |  |  |
| UFO | RS2 | Stock 52W Return and S&P 52W Return | +18.6% / +10.1% | +18.6% / +10.1% | PASS |  |  |
| UFO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| UFO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 56 | 56 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| UFO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| UFO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +18.6% clears | +18.6% clears | PASS |  |  |
| URA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $30.44 / RS 0.65 | $30.44 / RS 0.65 | PASS |  |  |
| URA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.65 | 0.65 | PASS |  |  |
| URA | RS2 | Stock 52W Return and S&P 52W Return | -28.7% / +10.1% | -28.7% / +10.1% | PASS |  |  |
| URA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| URA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 22 | 22 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| URA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| URA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -28.7% negative | -28.7% negative | PASS |  |  |
| URAA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.34 | 0.33 | PASS |  |  |
| URAA | RS2 | Stock 52W Return and S&P 52W Return | -63.1% / +10.1% | -63.2% / +10.1% | PASS |  |  |
| URAA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| URAA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 1 | 1 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| URAA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| URAA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -63.1% negative | -63.2% negative | PASS |  |  |
| V | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $426.46 / RS 1.17 | $426.46 / RS 1.17 | PASS |  |  |
| V | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.17 | 1.17 | PASS |  |  |
| V | RS2 | Stock 52W Return and S&P 52W Return | +29.2% / +10.1% | +29.2% / +10.1% | PASS |  |  |
| V | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| V | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| V | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| V | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.2% clears | +29.2% clears | PASS |  |  |
| VFV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.04 | 1.05 | PASS |  |  |
| VFV.TO | RS2 | Stock 52W Return and S&P 52W Return | +15.1% / +10.1% | +15.1% / +10.1% | PASS |  |  |
| VFV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VFV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 54 | 54 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VFV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| VFV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +15.1% clears | +15.1% clears | PASS |  |  |
| VRT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $188.67 / RS 1.00 | $188.67 / RS 1.00 | PASS |  |  |
| VRT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.00 | 1.00 | PASS |  |  |
| VRT | RS2 | Stock 52W Return and S&P 52W Return | +10.3% / +10.1% | +10.4% / +10.1% | PASS |  |  |
| VRT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| VRT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| VRT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market (momentum fading) | Slightly ahead of the market (momentum fading) | PASS |  |  |
| VRT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +10.3% clears | +10.4% clears | PASS |  |  |
| WELL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $244.65 / RS 1.15 | $244.65 / RS 1.15 | PASS |  |  |
| WELL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.15 | 1.15 | PASS |  |  |
| WELL | RS2 | Stock 52W Return and S&P 52W Return | +26.2% / +10.1% | +26.2% / +10.1% | PASS |  |  |
| WELL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WELL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 62 | 62 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WELL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| WELL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +26.2% clears | +26.2% clears | PASS |  |  |
| WMT | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $128.41 / RS 1.14 | $128.41 / RS 1.14 | PASS |  |  |
| WMT | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.14 | 1.14 | PASS |  |  |
| WMT | RS2 | Stock 52W Return and S&P 52W Return | +25.3% / +10.1% | +25.3% / +10.1% | PASS |  |  |
| WMT | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| WMT | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 61 | 61 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| WMT | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| WMT | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +25.3% clears | +25.3% clears | PASS |  |  |
| XCHP.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $105.33 / RS 1.36 | $105.33 / RS 1.36 | PASS |  |  |
| XCHP.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.36 | 1.36 | PASS |  |  |
| XCHP.TO | RS2 | Stock 52W Return and S&P 52W Return | +49.5% / +10.1% | +49.5% / +10.1% | PASS |  |  |
| XCHP.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XCHP.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 79 | 79 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XCHP.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| XCHP.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +49.5% clears | +49.5% clears | PASS |  |  |
| XDRV.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $39.69 / RS 0.86 | $39.69 / RS 0.86 | PASS |  |  |
| XDRV.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.86 | 0.86 | PASS |  |  |
| XDRV.TO | RS2 | Stock 52W Return and S&P 52W Return | -5.5% / +10.1% | -5.5% / +10.1% | PASS |  |  |
| XDRV.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XDRV.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 39 | 39 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XDRV.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Behind the market | Behind the market | PASS |  |  |
| XDRV.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -5.5% negative | -5.5% negative | PASS |  |  |
| XEQT.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $44.86 / RS 1.05 | $44.86 / RS 1.05 | PASS |  |  |
| XEQT.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.05 | 1.05 | PASS |  |  |
| XEQT.TO | RS2 | Stock 52W Return and S&P 52W Return | +15.2% / +10.1% | +15.2% / +10.1% | PASS |  |  |
| XEQT.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XEQT.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 54 | 54 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XEQT.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| XEQT.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +15.2% clears | +15.2% clears | PASS |  |  |
| XETM.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $61.57 / RS 0.66 | $61.57 / RS 0.66 | PASS |  |  |
| XETM.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.66 | 0.66 | PASS |  |  |
| XETM.TO | RS2 | Stock 52W Return and S&P 52W Return | -26.9% / +10.1% | -26.9% / +10.1% | PASS |  |  |
| XETM.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 23 | 23 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XETM.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| XETM.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -26.9% negative | -26.9% negative | PASS |  |  |
| XGD.TO | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $50.80 / RS 1.00 | $50.80 / RS 1.00 | PASS |  |  |
| XGD.TO | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.00 | 1.00 | PASS |  |  |
| XGD.TO | RS2 | Stock 52W Return and S&P 52W Return | +10.2% / +10.1% | +10.1% / +10.1% | PASS |  |  |
| XGD.TO | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XGD.TO | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 50 | 50 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XGD.TO | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly ahead of the market | Slightly ahead of the market | PASS |  |  |
| XGD.TO | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +10.2% clears | +10.1% clears | PASS |  |  |
| XOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $166.87 / RS 1.30 | $166.87 / RS 1.30 | PASS |  |  |
| XOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.30 | 1.30 | PASS |  |  |
| XOM | RS2 | Stock 52W Return and S&P 52W Return | +43.6% / +10.1% | +43.6% / +10.1% | PASS |  |  |
| XOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| XOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 74 | 74 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| XOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| XOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +43.6% clears | +43.6% clears | PASS |  |  |
| AAPL | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 2.2% below $360.83 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| AAPL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| AAPL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| AAPL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $344.57 – $351.73 · 0.3% below · turned here 4× | $344.57 – $351.73 · 0.3% · 4× | PASS |  |  |
| AAPL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.0462 | 8.0462 | PASS |  |  |
| AAPL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| AAPL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| AAPL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $351.73 | $351.73 | PASS |  |  |
| AAPL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 351.73, nearest zone high 351.73 | equal | PASS |  |  |
| AAPL | TS1c | S5: the Buy on the bar = the Buy in the box | $351.73 | $351.73 | PASS |  |  |
| AAPL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| AAPL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $335.64 -4.6% | $335.64 -4.6% | PASS |  |  |
| AAPL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPL | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 2.2% below the high $360.83 | PASS |  |  |
| AAPL | TS6 | Risk $ (and reward $ per share) | Risk $16.09 a share | Risk $16.09 | PASS |  |  |
| AAPU | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| AAPU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| AAPU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $47.65 – $48.94 · price is inside this zone · turned here 4× | $47.65 – $48.94 · 0.0% · 4× | PASS |  |  |
| AAPU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0849 | 2.0853 | PASS |  |  |
| AAPU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AAPU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AAPU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $48.94 | $48.94 | PASS |  |  |
| AAPU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 48.94, nearest zone high 48.94 | equal | PASS |  |  |
| AAPU | TS1c | S5: the Buy on the bar = the Buy in the box | $48.94 | $48.94 | PASS |  |  |
| AAPU | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AAPU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $44.77 -8.5% | $44.77 -8.5% | PASS |  |  |
| AAPU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AAPU | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| AAPU | TS6 | Risk $ (and reward $ per share) | Risk $4.17 a share | Risk $4.17 | PASS |  |  |
| ABBV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $302.93 · 3.6% above · turned here 1× | $302.93 · 3.6% · 1× | PASS |  |  |
| ABBV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ABBV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $291.40 · 0.3% below · turned here 1× | $291.40 · 0.3% · 1× | PASS |  |  |
| ABBV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.9093 | 6.9088 | PASS |  |  |
| ABBV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| ABBV | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| ABBV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $291.40 | $291.40 | PASS |  |  |
| ABBV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 291.4, nearest zone high 291.4 | equal | PASS |  |  |
| ABBV | TS1c | S5: the Buy on the bar = the Buy in the box | $291.40 | $291.40 | PASS |  |  |
| ABBV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| ABBV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $277.58 -4.7% | $277.58 -4.7% | PASS |  |  |
| ABBV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ABBV | TS4 | Target = nearest resistance edge and its % from the buy | $302.93 +4.0% | $302.93 +4.0% | PASS |  |  |
| ABBV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| ABBV | TS6 | Risk $ (and reward $ per share) | Risk $13.82 to make $11.53 a share | Risk $13.82 to make $11.53 | PASS |  |  |
| AIPO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $23.12 – $24.26 · 2.8% above · turned here 5× | $23.12 – $24.26 · 2.8% · 5× | PASS |  |  |
| AIPO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AIPO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $22.08 · 1.9% below · turned here 1× | $22.08 · 1.9% · 1× | PASS |  |  |
| AIPO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.1392 | 1.1391 | PASS |  |  |
| AIPO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| AIPO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $22.08 | $22.08 | PASS |  |  |
| AIPO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 22.08, nearest zone high 22.08 | equal | PASS |  |  |
| AIPO | TS1c | S5: the Buy on the bar = the Buy in the box | $22.08 | $22.08 | PASS |  |  |
| AIPO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| AIPO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $19.80 -10.3% | $19.80 -10.3% | PASS |  |  |
| AIPO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AIPO | TS4 | Target = nearest resistance edge and its % from the buy | $23.12 +4.7% | $23.12 +4.7% | PASS |  |  |
| AIPO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| AIPO | TS6 | Risk $ (and reward $ per share) | Risk $2.28 to make $1.04 a share | Risk $2.28 to make $1.04 | PASS |  |  |
| ALAB | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $214.24 · 3.3% above · turned here 1× | $214.24 · 3.3% · 1× | PASS |  |  |
| ALAB | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ALAB | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $177.61 – $192.86 · 7.0% below · turned here 7× | $177.61 – $192.86 · 7.0% · 7× | PASS |  |  |
| ALAB | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 23.8519 | 23.8514 | PASS |  |  |
| ALAB | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| ALAB | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| ALAB | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $192.86 | $192.86 | PASS |  |  |
| ALAB | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 192.86, nearest zone high 192.86 | equal | PASS |  |  |
| ALAB | TS1c | S5: the Buy on the bar = the Buy in the box | $192.86 | $192.86 | PASS |  |  |
| ALAB | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.7% below | 4.7% below | PASS |  |  |
| ALAB | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $145.16 -24.7% | $145.16 -24.7% | PASS |  |  |
| ALAB | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ALAB | TS4 | Target = nearest resistance edge and its % from the buy | $214.24 +11.1% | $214.24 +11.1% | PASS |  |  |
| ALAB | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| ALAB | TS6 | Risk $ (and reward $ per share) | Risk $47.70 to make $21.38 a share | Risk $47.70 to make $21.38 | PASS |  |  |
| AMD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $546.44 – $584.73 · 10.7% above · turned here 6× | $546.44 – $584.73 · 10.7% · 6× | PASS |  |  |
| AMD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $469.21 · 4.9% below · turned here 1× | $469.21 · 4.9% · 1× | PASS |  |  |
| AMD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 41.2793 | 41.2798 | PASS |  |  |
| AMD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AMD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AMD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $530.13 | $530.13 | PASS |  |  |
| AMD | TS1c | S5: the Buy on the bar = the Buy in the box | $530.13 | $530.13 | PASS |  |  |
| AMD | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.1% above | 5.1% above | PASS |  |  |
| AMD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $447.57 -15.6% | $447.57 -15.6% | PASS |  |  |
| AMD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD | TS4 | Target = nearest resistance edge and its % from the buy | $546.44 +3.1% | $546.44 +3.1% | PASS |  |  |
| AMD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AMD | TS6 | Risk $ (and reward $ per share) | Risk $82.56 to make $16.31 a share | Risk $82.56 to make $16.31 | PASS |  |  |
| AMD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $14.54 – $15.15 · 5.7% above · turned here 5× | $14.54 – $15.15 · 5.7% · 5× | PASS |  |  |
| AMD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $13.37 – $14.18 · price is inside this zone · turned here 3× | $13.37 – $14.18 · 0.0% · 3× | PASS |  |  |
| AMD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.0591 | 1.0591 | PASS |  |  |
| AMD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| AMD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| AMD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $14.18 | $14.18 | PASS |  |  |
| AMD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 14.18, nearest zone high 14.18 | equal | PASS |  |  |
| AMD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $14.18 | $14.18 | PASS |  |  |
| AMD.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AMD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.06 -14.9% | $12.06 -14.9% | PASS |  |  |
| AMD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $14.54 +2.5% | $14.54 +2.5% | PASS |  |  |
| AMD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AMD.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.12 to make $0.36 a share | Risk $2.12 to make $0.36 | PASS |  |  |
| AMZN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $265.34 – $267.56 · 3.4% above · turned here 2× | $265.34 – $267.56 · 3.4% · 2× | PASS |  |  |
| AMZN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $255.19 – $259.49 · price is inside this zone · turned here 3× | $255.19 – $259.49 · 0.0% · 3× | PASS |  |  |
| AMZN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.1458 | 9.1459 | PASS |  |  |
| AMZN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AMZN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AMZN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $259.49 | $259.49 | PASS |  |  |
| AMZN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 259.49, nearest zone high 259.49 | equal | PASS |  |  |
| AMZN | TS1c | S5: the Buy on the bar = the Buy in the box | $259.49 | $259.49 | PASS |  |  |
| AMZN | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AMZN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $241.20 -7.0% | $241.20 -7.0% | PASS |  |  |
| AMZN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZN | TS4 | Target = nearest resistance edge and its % from the buy | $265.34 +2.3% | $265.34 +2.3% | PASS |  |  |
| AMZN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| AMZN | TS6 | Risk $ (and reward $ per share) | Risk $18.29 to make $5.85 a share | Risk $18.29 to make $5.85 | PASS |  |  |
| AMZU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.20 – $39.71 · 5.8% above · turned here 7× | $37.20 – $39.71 · 5.8% · 7× | PASS |  |  |
| AMZU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMZU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $32.13 – $33.43 · 4.9% below · turned here 6× | $32.13 – $33.43 · 4.9% · 6× | PASS |  |  |
| AMZU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5128 | 2.5117 | PASS |  |  |
| AMZU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| AMZU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| AMZU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $33.43 | $33.43 | PASS |  |  |
| AMZU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 33.43, nearest zone high 33.43 | equal | PASS |  |  |
| AMZU | TS1c | S5: the Buy on the bar = the Buy in the box | $33.43 | $33.43 | PASS |  |  |
| AMZU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.2% below | 5.2% below | PASS |  |  |
| AMZU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $28.40 -15.0% | $28.40 -15.0% | PASS |  |  |
| AMZU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMZU | TS4 | Target = nearest resistance edge and its % from the buy | $37.20 +11.3% | $37.20 +11.3% | PASS |  |  |
| AMZU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| AMZU | TS6 | Risk $ (and reward $ per share) | Risk $5.03 to make $3.77 a share | Risk $5.03 to make $3.77 | PASS |  |  |
| ANET.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $34.01 – $34.05 · 2.9% above · turned here 2× | $34.01 – $34.05 · 2.9% · 2× | PASS |  |  |
| ANET.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.45 – $33.38 · price is inside this zone · turned here 8× | $31.45 – $33.38 · 0.0% · 8× | PASS |  |  |
| ANET.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0488 | 2.0488 | PASS |  |  |
| ANET.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ANET.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ANET.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $33.38 | $33.38 | PASS |  |  |
| ANET.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 33.38, nearest zone high 33.38 | equal | PASS |  |  |
| ANET.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $33.38 | $33.38 | PASS |  |  |
| ANET.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| ANET.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $29.28 -12.3% | $29.28 -12.3% | PASS |  |  |
| ANET.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ANET.TO | TS4 | Target = nearest resistance edge and its % from the buy | $34.01 +1.9% | $34.01 +1.9% | PASS |  |  |
| ANET.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| ANET.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.10 to make $0.63 a share | Risk $4.10 to make $0.63 | PASS |  |  |
| ASML.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $42.01 – $42.36 · 4.1% above · turned here 2× | $42.01 – $42.36 · 4.1% · 2× | PASS |  |  |
| ASML.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ASML.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $40.17 – $40.74 · price is inside this zone · turned here 3× | $40.17 – $40.74 · 0.0% · 3× | PASS |  |  |
| ASML.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.8776 | 1.8777 | PASS |  |  |
| ASML.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ASML.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ASML.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $40.74 | $40.74 | PASS |  |  |
| ASML.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 40.74, nearest zone high 40.74 | equal | PASS |  |  |
| ASML.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $40.74 | $40.74 | PASS |  |  |
| ASML.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| ASML.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $36.98 -9.2% | $36.98 -9.2% | PASS |  |  |
| ASML.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASML.TO | TS4 | Target = nearest resistance edge and its % from the buy | $42.01 +3.1% | $42.01 +3.1% | PASS |  |  |
| ASML.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ASML.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.76 to make $1.27 a share | Risk $3.76 to make $1.27 | PASS |  |  |
| ASTL.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $8.16 · 11.5% above · turned here 1× | $8.16 · 11.5% · 1× | PASS |  |  |
| ASTL.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $7.25 – $7.44 · price is inside this zone · turned here 3× | $7.25 – $7.44 · 0.0% · 3× | PASS |  |  |
| ASTL.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4186 | 0.4191 | PASS |  |  |
| ASTL.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| ASTL.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| ASTL.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $7.44 | $7.44 | PASS |  |  |
| ASTL.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 7.44, nearest zone high 7.44 | equal | PASS |  |  |
| ASTL.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $7.44 | $7.44 | PASS |  |  |
| ASTL.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| ASTL.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $6.60 -11.3% | $6.60 -11.3% | PASS |  |  |
| ASTL.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ASTL.TO | TS4 | Target = nearest resistance edge and its % from the buy | $8.16 +9.7% | $8.16 +9.7% | PASS |  |  |
| ASTL.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| ASTL.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.84 to make $0.72 a share | Risk $0.84 to make $0.72 | PASS |  |  |
| ATD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $84.02 · 0.7% above · turned here 1× | $84.02 · 0.7% · 1× | PASS |  |  |
| ATD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ATD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $80.76 – $81.40 · 2.4% below · turned here 3× | $80.76 – $81.40 · 2.4% · 3× | PASS |  |  |
| ATD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6951 | 1.6951 | PASS |  |  |
| ATD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| ATD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| ATD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $81.40 | $81.40 | PASS |  |  |
| ATD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 81.4, nearest zone high 81.4 | equal | PASS |  |  |
| ATD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $81.40 | $81.40 | PASS |  |  |
| ATD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.0% below | 3.0% below | PASS |  |  |
| ATD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $78.01 -4.2% | $78.01 -4.2% | PASS |  |  |
| ATD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ATD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $84.02 +3.2% | $84.02 +3.2% | PASS |  |  |
| ATD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| ATD.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.39 to make $2.62 a share | Risk $3.39 to make $2.62 | PASS |  |  |
| AVGC | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $19.34 – $20.42 · 9.3% above · turned here 4× | $19.34 – $20.42 · 9.3% · 4× | PASS |  |  |
| AVGC | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.52 · 6.7% below · turned here 1× | $16.52 · 6.7% · 1× | PASS |  |  |
| AVGC | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.7117 | 1.7114 | PASS |  |  |
| AVGC | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| AVGC | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| AVGC | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $16.52 | $16.52 | PASS |  |  |
| AVGC | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 16.52, nearest zone high 16.52 | equal | PASS |  |  |
| AVGC | TS1c | S5: the Buy on the bar = the Buy in the box | $16.52 | $16.52 | PASS |  |  |
| AVGC | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.5% below | 5.5% below | PASS |  |  |
| AVGC | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $13.10 -20.7% | $13.10 -20.7% | PASS |  |  |
| AVGC | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGC | TS4 | Target = nearest resistance edge and its % from the buy | $19.34 +17.1% | $19.34 +17.1% | PASS |  |  |
| AVGC | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| AVGC | TS6 | Risk $ (and reward $ per share) | Risk $3.42 to make $2.82 a share | Risk $3.42 to make $2.82 | PASS |  |  |
| AVGO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $350.06 – $366.55 · 5.0% above · turned here 9× | $350.06 – $366.55 · 5.0% · 9× | PASS |  |  |
| AVGO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AVGO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $329.06 – $343.29 · price is inside this zone · turned here 6× | $329.06 – $343.29 · 0.0% · 6× | PASS |  |  |
| AVGO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.9357 | 17.9357 | PASS |  |  |
| AVGO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| AVGO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| AVGO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $343.29 | $343.29 | PASS |  |  |
| AVGO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 343.29, nearest zone high 343.29 | equal | PASS |  |  |
| AVGO | TS1c | S5: the Buy on the bar = the Buy in the box | $343.29 | $343.29 | PASS |  |  |
| AVGO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AVGO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $307.42 -10.4% | $307.42 -10.4% | PASS |  |  |
| AVGO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO | TS4 | Target = nearest resistance edge and its % from the buy | $350.06 +2.0% | $350.06 +2.0% | PASS |  |  |
| AVGO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| AVGO | TS6 | Risk $ (and reward $ per share) | Risk $35.87 to make $6.77 a share | Risk $35.87 to make $6.77 | PASS |  |  |
| AVGO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $13.51 – $14.10 · 5.0% above · turned here 9× | $13.51 – $14.10 · 5.0% · 9× | PASS |  |  |
| AVGO.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.72 – $13.34 · price is inside this zone · turned here 7× | $12.72 – $13.34 · 0.0% · 7× | PASS |  |  |
| AVGO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6674 | 0.6673 | PASS |  |  |
| AVGO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| AVGO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| AVGO.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $13.34 | $13.34 | PASS |  |  |
| AVGO.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 13.34, nearest zone high 13.34 | equal | PASS |  |  |
| AVGO.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $13.34 | $13.34 | PASS |  |  |
| AVGO.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| AVGO.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.01 -10.0% | $12.01 -10.0% | PASS |  |  |
| AVGO.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AVGO.TO | TS4 | Target = nearest resistance edge and its % from the buy | $13.51 +1.3% | $13.51 +1.3% | PASS |  |  |
| AVGO.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| AVGO.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.33 to make $0.17 a share | Risk $1.33 to make $0.17 | PASS |  |  |
| BDT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $71.25 · 0.5% above · turned here 1× | $71.25 · 0.5% · 1× | PASS |  |  |
| BDT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| BDT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $66.95 – $67.00 · 5.5% below · turned here 2× | $66.95 – $67.00 · 5.5% · 2× | PASS |  |  |
| BDT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.9737 | 3.9738 | PASS |  |  |
| BDT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| BDT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| BDT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $67.00 | $67.00 | PASS |  |  |
| BDT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 67, nearest zone high 67 | equal | PASS |  |  |
| BDT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $67.00 | $67.00 | PASS |  |  |
| BDT.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 10.9% below | 10.9% below | PASS |  |  |
| BDT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $59.05 -11.9% | $59.05 -11.9% | PASS |  |  |
| BDT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BDT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $71.25 +6.3% | $71.25 +6.3% | PASS |  |  |
| BDT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| BDT.TO | TS6 | Risk $ (and reward $ per share) | Risk $7.95 to make $4.25 a share | Risk $7.95 to make $4.25 | PASS |  |  |
| BOTZ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.54 · 2.9% above · turned here 1× | $30.54 · 2.9% · 1× | PASS |  |  |
| BOTZ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| BOTZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| BOTZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7967 | 0.7967 | PASS |  |  |
| BOTZ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| BOTZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| BRK-B | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 0.7% below $596.92 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| BRK-B | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| BRK-B | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 7 of 8 trend checks pass | No resistance within 30% above · 7 of 8 trend checks pass | PASS |  |  |
| BRK-B | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $549.96 · 6.6% below · turned here 1× | $549.96 · 6.6% · 1× | PASS |  |  |
| BRK-B | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.5224 | 9.5224 | PASS |  |  |
| BRK-B | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| BRK-B | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| BRK-B | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 549.96, nearest zone high 549.96 | equal | PASS |  |  |
| BRK-B | TS1c | S5: the Buy on the bar = the Buy in the box | $549.96 | $549.96 | PASS |  |  |
| BRK-B | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.2% below | 7.2% below | PASS |  |  |
| BRK-B | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $530.92 -3.5% | $530.92 -3.5% | PASS |  |  |
| BRK-B | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRK-B | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 0.7% below the high $596.92 | PASS |  |  |
| BRK-B | TS6 | Risk $ (and reward $ per share) | Risk $19.04 a share | Risk $19.04 | PASS |  |  |
| BRKU | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| BRKU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| BRKU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $26.69 – $26.80 · 11.1% below · turned here 3× | $26.69 – $26.80 · 11.1% · 3× | PASS |  |  |
| BRKU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.884 | 0.8840 | PASS |  |  |
| BRKU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| BRKU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| BRKU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $26.80 | $26.80 | PASS |  |  |
| BRKU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 26.8, nearest zone high 26.8 | equal | PASS |  |  |
| BRKU | TS1c | S5: the Buy on the bar = the Buy in the box | $26.80 | $26.80 | PASS |  |  |
| BRKU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 13.0% below | 13.0% below | PASS |  |  |
| BRKU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $25.03 -6.6% | $25.03 -6.6% | PASS |  |  |
| BRKU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| BRKU | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| BRKU | TS6 | Risk $ (and reward $ per share) | Risk $1.77 a share | Risk $1.77 | PASS |  |  |
| CAMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $101.39 · 6.7% above · turned here 1× | $101.39 · 6.7% · 1× | PASS |  |  |
| CAMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CAMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $89.13 – $91.91 · 3.2% below · turned here 2× | $89.13 – $91.91 · 3.2% · 2× | PASS |  |  |
| CAMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.4392 | 8.4396 | PASS |  |  |
| CAMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| CAMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| CAMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $91.91 | $91.91 | PASS |  |  |
| CAMT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 91.91, nearest zone high 91.91 | equal | PASS |  |  |
| CAMT | TS1c | S5: the Buy on the bar = the Buy in the box | $91.91 | $91.91 | PASS |  |  |
| CAMT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.4% below | 1.4% below | PASS |  |  |
| CAMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $75.03 -18.4% | $75.03 -18.4% | PASS |  |  |
| CAMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CAMT | TS4 | Target = nearest resistance edge and its % from the buy | $101.39 +10.3% | $101.39 +10.3% | PASS |  |  |
| CAMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| CAMT | TS6 | Risk $ (and reward $ per share) | Risk $16.88 to make $9.48 a share | Risk $16.88 to make $9.48 | PASS |  |  |
| CARS.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.90 · 5.1% above · turned here 1× | $20.90 · 5.1% · 1× | PASS |  |  |
| CARS.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CARS.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CARS.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5215 | 0.5201 | PASS |  |  |
| CARS.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| CARS.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| CARS.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CAT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $572.05 · 0.6% above · turned here 1× | $572.05 · 0.6% · 1× | PASS |  |  |
| CAT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CAT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $537.08 – $557.46 · 2.0% below · turned here 3× | $537.08 – $557.46 · 2.0% · 3× | PASS |  |  |
| CAT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 29.3033 | 29.3033 | PASS |  |  |
| CAT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| CAT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| CAT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $557.46 | $557.46 | PASS |  |  |
| CAT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 557.46, nearest zone high 557.46 | equal | PASS |  |  |
| CAT | TS1c | S5: the Buy on the bar = the Buy in the box | $557.46 | $557.46 | PASS |  |  |
| CAT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.3% below | 2.3% below | PASS |  |  |
| CAT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $498.85 -10.5% | $498.85 -10.5% | PASS |  |  |
| CAT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CAT | TS4 | Target = nearest resistance edge and its % from the buy | $572.05 +2.6% | $572.05 +2.6% | PASS |  |  |
| CAT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| CAT | TS6 | Risk $ (and reward $ per share) | Risk $58.61 to make $14.59 a share | Risk $58.61 to make $14.59 | PASS |  |  |
| CCO.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $92.52 · 0.6% above · turned here 1× | $92.52 · 0.6% · 1× | PASS |  |  |
| CCO.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| CCO.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| CCO.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.116 | 5.1160 | PASS |  |  |
| CCO.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| CCO.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| CCO.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| CEG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $276.84 – $287.00 · 3.4% above · turned here 5× | $276.84 – $287.00 · 3.4% · 5× | PASS |  |  |
| CEG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CEG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $256.10 – $268.00 · price is inside this zone · turned here 7× | $256.10 – $268.00 · 0.0% · 7× | PASS |  |  |
| CEG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 13.0458 | 13.0455 | PASS |  |  |
| CEG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| CEG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| CEG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $268.00 | $268.00 | PASS |  |  |
| CEG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 268, nearest zone high 268 | equal | PASS |  |  |
| CEG | TS1c | S5: the Buy on the bar = the Buy in the box | $268.00 | $268.00 | PASS |  |  |
| CEG | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| CEG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $241.91 -9.7% | $241.91 -9.7% | PASS |  |  |
| CEG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CEG | TS4 | Target = nearest resistance edge and its % from the buy | $276.84 +3.3% | $276.84 +3.3% | PASS |  |  |
| CEG | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CEG | TS6 | Risk $ (and reward $ per share) | Risk $26.09 to make $8.84 a share | Risk $26.09 to make $8.84 | PASS |  |  |
| CGY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $84.58 – $87.00 · 0.6% above · turned here 6× | $84.58 – $87.00 · 0.6% · 6× | PASS |  |  |
| CGY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CGY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $83.01 · 1.3% below · turned here 1× | $83.01 · 1.3% · 1× | PASS |  |  |
| CGY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5511 | 2.5511 | PASS |  |  |
| CGY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| CGY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| CGY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $83.01 | $83.01 | PASS |  |  |
| CGY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 83.01, nearest zone high 83.01 | equal | PASS |  |  |
| CGY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $83.01 | $83.01 | PASS |  |  |
| CGY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.6% below | 3.6% below | PASS |  |  |
| CGY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $77.91 -6.1% | $77.91 -6.1% | PASS |  |  |
| CGY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CGY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $84.58 +1.9% | $84.58 +1.9% | PASS |  |  |
| CGY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CGY.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.10 to make $1.57 a share | Risk $5.10 to make $1.57 | PASS |  |  |
| CNQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $68.42 – $68.45 · 0.2% above · turned here 2× | $68.42 – $68.45 · 0.2% · 2× | PASS |  |  |
| CNQ.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $65.78 – $67.12 · 1.7% below · turned here 5× | $65.78 – $67.12 · 1.7% · 5× | PASS |  |  |
| CNQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9481 | 1.9481 | PASS |  |  |
| CNQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| CNQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $67.12 | $67.12 | PASS |  |  |
| CNQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 67.12, nearest zone high 67.12 | equal | PASS |  |  |
| CNQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $67.12 | $67.12 | PASS |  |  |
| CNQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.7% below | 2.7% below | PASS |  |  |
| CNQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $63.22 -5.8% | $63.22 -5.8% | PASS |  |  |
| CNQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $68.42 +1.9% | $68.42 +1.9% | PASS |  |  |
| CNQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CNQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.90 to make $1.30 a share | Risk $3.90 to make $1.30 | PASS |  |  |
| CNR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $184.26 · 2.0% above · turned here 1× | $184.26 · 2.0% · 1× | PASS |  |  |
| CNR.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CNR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $178.49 · 1.2% below · turned here 1× | $178.49 · 1.2% · 1× | PASS |  |  |
| CNR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.3694 | 3.3695 | PASS |  |  |
| CNR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| CNR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| CNR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $178.49 | $178.49 | PASS |  |  |
| CNR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 178.49, nearest zone high 178.49 | equal | PASS |  |  |
| CNR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $178.49 | $178.49 | PASS |  |  |
| CNR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.3% below | 2.3% below | PASS |  |  |
| CNR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $171.75 -3.8% | $171.75 -3.8% | PASS |  |  |
| CNR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CNR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $184.26 +3.2% | $184.26 +3.2% | PASS |  |  |
| CNR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| CNR.TO | TS6 | Risk $ (and reward $ per share) | Risk $6.74 to make $5.77 a share | Risk $6.74 to make $5.77 | PASS |  |  |
| COP | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $141.62 · 1.6% above · turned here 1× | $141.62 · 1.6% · 1× | PASS |  |  |
| COP | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COP | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $135.87 – $135.88 · 2.5% below · turned here 2× | $135.87 – $135.88 · 2.5% · 2× | PASS |  |  |
| COP | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.9297 | 3.9300 | PASS |  |  |
| COP | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| COP | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| COP | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $135.88 | $135.88 | PASS |  |  |
| COP | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 135.88, nearest zone high 135.88 | equal | PASS |  |  |
| COP | TS1c | S5: the Buy on the bar = the Buy in the box | $135.88 | $135.88 | PASS |  |  |
| COP | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.3% below | 3.3% below | PASS |  |  |
| COP | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $128.02 -5.8% | $128.02 -5.8% | PASS |  |  |
| COP | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COP | TS4 | Target = nearest resistance edge and its % from the buy | $141.62 +4.2% | $141.62 +4.2% | PASS |  |  |
| COP | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| COP | TS6 | Risk $ (and reward $ per share) | Risk $7.86 to make $5.74 a share | Risk $7.86 to make $5.74 | PASS |  |  |
| COPP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $46.40 · 0.2% above · turned here 1× | $46.40 · 0.2% · 1× | PASS |  |  |
| COPP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COPP.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $42.17 · 9.0% below · turned here 1× | $42.17 · 9.0% · 1× | PASS |  |  |
| COPP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0921 | 2.0920 | PASS |  |  |
| COPP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| COPP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| COPP.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $42.17 | $42.17 | PASS |  |  |
| COPP.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 42.17, nearest zone high 42.17 | equal | PASS |  |  |
| COPP.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $42.17 | $42.17 | PASS |  |  |
| COPP.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 9.3% below | 9.3% below | PASS |  |  |
| COPP.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $37.99 -9.9% | $37.99 -9.9% | PASS |  |  |
| COPP.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COPP.TO | TS4 | Target = nearest resistance edge and its % from the buy | $46.40 +10.0% | $46.40 +10.0% | PASS |  |  |
| COPP.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.0 : 1 | 1.0 : 1 | PASS |  |  |
| COPP.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.18 to make $4.23 a share | Risk $4.18 to make $4.23 | PASS |  |  |
| COPX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $68.49 · 5.1% above · turned here 1× | $68.49 · 5.1% · 1× | PASS |  |  |
| COPX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 0 of 8 trend checks pass · ADX 24.0 | 0 of 8 trend checks pass · ADX 24.0 | PASS |  |  |
| COPX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $56.93 · 12.6% below · turned here 1× | $56.93 · 12.6% · 1× | PASS |  |  |
| COPX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8171 | 2.8168 | PASS |  |  |
| COPX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| COPX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| COPX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $56.93 | $56.93 | PASS |  |  |
| COPX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 56.93, nearest zone high 56.93 | equal | PASS |  |  |
| COPX | TS1c | S5: the Buy on the bar = the Buy in the box | $56.93 | $56.93 | PASS |  |  |
| COPX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 13.1% below | 13.1% below | PASS |  |  |
| COPX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $51.30 -9.9% | $51.30 -9.9% | PASS |  |  |
| COPX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COPX | TS4 | Target = nearest resistance edge and its % from the buy | $68.49 +20.3% | $68.49 +20.3% | PASS |  |  |
| COPX | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.1 : 1 | 2.1 : 1 | PASS |  |  |
| COPX | TS6 | Risk $ (and reward $ per share) | Risk $5.63 to make $11.56 a share | Risk $5.63 to make $11.56 | PASS |  |  |
| COPZ | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| COPZ | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| COPZ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.82 | 0.8208 | PASS |  |  |
| COPZ | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| COST | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 0.3% below $1,117.00 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| COST | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| COST | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 7 of 8 trend checks pass | No resistance within 30% above · 7 of 8 trend checks pass | PASS |  |  |
| COST | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,096.50 · 1.5% below · turned here 1× | $1,096.50 · 1.5% · 1× | PASS |  |  |
| COST | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 19.0434 | 19.0434 | PASS |  |  |
| COST | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| COST | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| COST | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,096.50 | $1,096.50 | PASS |  |  |
| COST | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1096.5, nearest zone high 1096.5 | equal | PASS |  |  |
| COST | TS1c | S5: the Buy on the bar = the Buy in the box | $1,096.50 | $1,096.50 | PASS |  |  |
| COST | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.5% below | 1.5% below | PASS |  |  |
| COST | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $1,058.41 -3.5% | $1,058.41 -3.5% | PASS |  |  |
| COST | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COST | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 0.3% below the high $1,117.00 | PASS |  |  |
| COST | TS6 | Risk $ (and reward $ per share) | Risk $38.09 a share | Risk $38.09 | PASS |  |  |
| COTG | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $17.80 · 5.0% above · turned here 1× | $17.80 · 5.0% · 1× | PASS |  |  |
| COTG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| COTG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $16.07 – $16.11 · 5.0% below · turned here 2× | $16.07 – $16.11 · 5.0% · 2× | PASS |  |  |
| COTG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5237 | 0.5237 | PASS |  |  |
| COTG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| COTG | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| COTG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $16.11 | $16.11 | PASS |  |  |
| COTG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 16.11, nearest zone high 16.11 | equal | PASS |  |  |
| COTG | TS1c | S5: the Buy on the bar = the Buy in the box | $16.11 | $16.11 | PASS |  |  |
| COTG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.5% below | 5.5% below | PASS |  |  |
| COTG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $15.06 -6.5% | $15.06 -6.5% | PASS |  |  |
| COTG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| COTG | TS4 | Target = nearest resistance edge and its % from the buy | $17.80 +10.5% | $17.80 +10.5% | PASS |  |  |
| COTG | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.6 : 1 | 1.6 : 1 | PASS |  |  |
| COTG | TS6 | Risk $ (and reward $ per share) | Risk $1.05 to make $1.69 a share | Risk $1.05 to make $1.69 | PASS |  |  |
| CSU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3,341.06 – $3,430.89 · 0.2% above · turned here 5× | $3,341.06 – $3,430.89 · 0.2% · 5× | PASS |  |  |
| CSU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $3,118.74 – $3,227.61 · 3.2% below · turned here 5× | $3,118.74 – $3,227.61 · 3.2% · 5× | PASS |  |  |
| CSU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 119.2161 | 119.2161 | PASS |  |  |
| CSU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| CSU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| CSU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $3,227.61 | $3,227.61 | PASS |  |  |
| CSU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 3227.61, nearest zone high 3227.61 | equal | PASS |  |  |
| CSU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $3,227.61 | $3,227.61 | PASS |  |  |
| CSU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.1% below | 6.1% below | PASS |  |  |
| CSU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $2,989.18 -7.4% | $2,989.18 -7.4% | PASS |  |  |
| CSU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CSU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $3,341.06 +3.5% | $3,341.06 +3.5% | PASS |  |  |
| CSU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| CSU.TO | TS6 | Risk $ (and reward $ per share) | Risk $238.43 to make $113.45 a share | Risk $238.43 to make $113.45 | PASS |  |  |
| CVX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $217.78 · 0.7% above · turned here 1× | $217.78 · 0.7% · 1× | PASS |  |  |
| CVX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| CVX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $214.71 · 0.7% below · turned here 1× | $214.71 · 0.7% · 1× | PASS |  |  |
| CVX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.9077 | 4.9081 | PASS |  |  |
| CVX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| CVX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $214.71 | $214.71 | PASS |  |  |
| CVX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 214.71, nearest zone high 214.71 | equal | PASS |  |  |
| CVX | TS1c | S5: the Buy on the bar = the Buy in the box | $214.71 | $214.71 | PASS |  |  |
| CVX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.1% below | 1.1% below | PASS |  |  |
| CVX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $204.89 -4.6% | $204.89 -4.6% | PASS |  |  |
| CVX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| CVX | TS4 | Target = nearest resistance edge and its % from the buy | $217.78 +1.4% | $217.78 +1.4% | PASS |  |  |
| CVX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| CVX | TS6 | Risk $ (and reward $ per share) | Risk $9.82 to make $3.07 a share | Risk $9.82 to make $3.07 | PASS |  |  |
| DRAL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| DRAL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $4.06 · 0.5% below · turned here 1× | $4.06 · 0.5% · 1× | PASS |  |  |
| DRAL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8373 | 0.8371 | PASS |  |  |
| DRAL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| DRAL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| DRAL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $4.06 | $4.06 | PASS |  |  |
| DRAL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 4.06, nearest zone high 4.06 | equal | PASS |  |  |
| DRAL | TS1c | S5: the Buy on the bar = the Buy in the box | $4.06 | $4.06 | PASS |  |  |
| DRAL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.3% below | 3.3% below | PASS |  |  |
| DRAL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $2.39 -41.2% | $2.39 -41.2% | PASS |  |  |
| DRAL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRAL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| DRAL | TS6 | Risk $ (and reward $ per share) | Risk $1.67 a share | Risk $1.67 | PASS |  |  |
| DRAM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $44.40 – $46.43 · 14.1% above · turned here 3× | $44.40 – $46.43 · 14.1% · 3× | PASS |  |  |
| DRAM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $37.01 · 4.9% below · turned here 1× | $37.01 · 4.9% · 1× | PASS |  |  |
| DRAM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.2111 | 3.2109 | PASS |  |  |
| DRAM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| DRAM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| DRAM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $37.01 | $37.01 | PASS |  |  |
| DRAM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 37.01, nearest zone high 37.01 | equal | PASS |  |  |
| DRAM | TS1c | S5: the Buy on the bar = the Buy in the box | $37.01 | $37.01 | PASS |  |  |
| DRAM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.8% below | 5.8% below | PASS |  |  |
| DRAM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $30.59 -17.4% | $30.59 -17.4% | PASS |  |  |
| DRAM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRAM | TS4 | Target = nearest resistance edge and its % from the buy | $44.40 +20.0% | $44.40 +20.0% | PASS |  |  |
| DRAM | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| DRAM | TS6 | Risk $ (and reward $ per share) | Risk $6.42 to make $7.39 a share | Risk $6.42 to make $7.39 | PASS |  |  |
| DRIV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $27.77 · 3.0% above · turned here 1× | $27.77 · 3.0% · 1× | PASS |  |  |
| DRIV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| DRIV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $26.87 · 0.3% below · turned here 1× | $26.87 · 0.3% · 1× | PASS |  |  |
| DRIV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8068 | 0.8078 | PASS |  |  |
| DRIV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| DRIV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $26.87 | $26.87 | PASS |  |  |
| DRIV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 26.87, nearest zone high 26.87 | equal | PASS |  |  |
| DRIV | TS1c | S5: the Buy on the bar = the Buy in the box | $26.87 | $26.87 | PASS |  |  |
| DRIV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% below | 1.8% below | PASS |  |  |
| DRIV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $25.26 -6.0% | $25.26 -6.0% | PASS |  |  |
| DRIV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DRIV | TS4 | Target = nearest resistance edge and its % from the buy | $27.77 +3.3% | $27.77 +3.3% | PASS |  |  |
| DRIV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| DRIV | TS6 | Risk $ (and reward $ per share) | Risk $1.61 to make $0.90 a share | Risk $1.61 to make $0.90 | PASS |  |  |
| DUK | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $130.38 – $131.87 · 0.4% above · turned here 4× | $130.38 – $131.87 · 0.4% · 4× | PASS |  |  |
| DUK | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| DUK | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $129.28 · 0.5% below · turned here 1× | $129.28 · 0.5% · 1× | PASS |  |  |
| DUK | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1596 | 2.1590 | PASS |  |  |
| DUK | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| DUK | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| DUK | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $129.28 | $129.28 | PASS |  |  |
| DUK | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 129.28, nearest zone high 129.28 | equal | PASS |  |  |
| DUK | TS1c | S5: the Buy on the bar = the Buy in the box | $129.28 | $129.28 | PASS |  |  |
| DUK | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.0% below | 1.0% below | PASS |  |  |
| DUK | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $124.96 -3.3% | $124.96 -3.3% | PASS |  |  |
| DUK | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| DUK | TS4 | Target = nearest resistance edge and its % from the buy | $130.38 +0.9% | $130.38 +0.9% | PASS |  |  |
| DUK | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| DUK | TS6 | Risk $ (and reward $ per share) | Risk $4.32 to make $1.10 a share | Risk $4.32 to make $1.10 | PASS |  |  |
| ELIL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| ELIL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| ELIL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.86 · 10.2% below · turned here 1× | $35.86 · 10.2% · 1× | PASS |  |  |
| ELIL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2689 | 2.2692 | PASS |  |  |
| ELIL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| ELIL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 35.86, nearest zone high 35.86 | equal | PASS |  |  |
| ELIL | TS1c | S5: the Buy on the bar = the Buy in the box | $35.86 | $35.86 | PASS |  |  |
| ELIL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 12.8% below | 12.8% below | PASS |  |  |
| ELIL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.32 -12.7% | $31.32 -12.7% | PASS |  |  |
| ELIL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ELIL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| ELIL | TS6 | Risk $ (and reward $ per share) | Risk $4.54 a share | Risk $4.54 | PASS |  |  |
| EQIX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $1,066.51 – $1,100.66 · 3.2% above · turned here 6× | $1,066.51 – $1,100.66 · 3.2% · 6× | PASS |  |  |
| EQIX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| EQIX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,027.17 – $1,053.97 · price is inside this zone · turned here 7× | $1,027.17 – $1,053.97 · 0.0% · 7× | PASS |  |  |
| EQIX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 34.3155 | 34.3155 | PASS |  |  |
| EQIX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| EQIX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,053.97 | $1,053.97 | PASS |  |  |
| EQIX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1053.97, nearest zone high 1053.97 | equal | PASS |  |  |
| EQIX | TS1c | S5: the Buy on the bar = the Buy in the box | $1,053.97 | $1,053.97 | PASS |  |  |
| EQIX | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| EQIX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $985.34 -6.5% | $985.34 -6.5% | PASS |  |  |
| EQIX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| EQIX | TS4 | Target = nearest resistance edge and its % from the buy | $1,066.51 +1.2% | $1,066.51 +1.2% | PASS |  |  |
| EQIX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| EQIX | TS6 | Risk $ (and reward $ per share) | Risk $68.63 to make $12.54 a share | Risk $68.63 to make $12.54 | PASS |  |  |
| ETN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $338.25 – $354.37 · 1.0% above · turned here 4× | $338.25 – $354.37 · 1.0% · 4× | PASS |  |  |
| ETN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ETN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $311.92 – $327.50 · 2.2% below · turned here 6× | $311.92 – $327.50 · 2.2% · 6× | PASS |  |  |
| ETN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 18.412 | 18.4123 | PASS |  |  |
| ETN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ETN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ETN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $327.50 | $327.50 | PASS |  |  |
| ETN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 327.5, nearest zone high 327.5 | equal | PASS |  |  |
| ETN | TS1c | S5: the Buy on the bar = the Buy in the box | $327.50 | $327.50 | PASS |  |  |
| ETN | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.8% below | 2.8% below | PASS |  |  |
| ETN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $290.68 -11.2% | $290.68 -11.2% | PASS |  |  |
| ETN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ETN | TS4 | Target = nearest resistance edge and its % from the buy | $338.25 +3.3% | $338.25 +3.3% | PASS |  |  |
| ETN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ETN | TS6 | Risk $ (and reward $ per share) | Risk $36.82 to make $10.75 a share | Risk $36.82 to make $10.75 | PASS |  |  |
| FCX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $55.49 – $56.75 · 0.6% above · turned here 4× | $55.49 – $56.75 · 0.6% · 4× | PASS |  |  |
| FCX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| FCX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $50.66 – $51.51 · 6.6% below · turned here 2× | $50.66 – $51.51 · 6.6% · 2× | PASS |  |  |
| FCX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8595 | 2.8598 | PASS |  |  |
| FCX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| FCX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| FCX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $51.51 | $51.51 | PASS |  |  |
| FCX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 51.51, nearest zone high 51.51 | equal | PASS |  |  |
| FCX | TS1c | S5: the Buy on the bar = the Buy in the box | $51.51 | $51.51 | PASS |  |  |
| FCX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.7% below | 6.7% below | PASS |  |  |
| FCX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $45.79 -11.1% | $45.79 -11.1% | PASS |  |  |
| FCX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FCX | TS4 | Target = nearest resistance edge and its % from the buy | $55.49 +7.7% | $55.49 +7.7% | PASS |  |  |
| FCX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| FCX | TS6 | Risk $ (and reward $ per share) | Risk $5.72 to make $3.98 a share | Risk $5.72 to make $3.98 | PASS |  |  |
| FINN.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $32.88 · 3.8% above · turned here 1× | $32.88 · 3.8% · 1× | PASS |  |  |
| FINN.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| FINN.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $31.50 – $31.65 · 0.1% below · turned here 5× | $31.50 – $31.65 · 0.1% · 5× | PASS |  |  |
| FINN.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6776 | 0.6776 | PASS |  |  |
| FINN.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| FINN.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| FINN.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $31.65 | $31.65 | PASS |  |  |
| FINN.NE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 31.65, nearest zone high 31.65 | equal | PASS |  |  |
| FINN.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $31.65 | $31.65 | PASS |  |  |
| FINN.NE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.4% below | 1.4% below | PASS |  |  |
| FINN.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $30.29 -4.3% | $30.29 -4.3% | PASS |  |  |
| FINN.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FINN.NE | TS4 | Target = nearest resistance edge and its % from the buy | $32.88 +3.9% | $32.88 +3.9% | PASS |  |  |
| FINN.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| FINN.NE | TS6 | Risk $ (and reward $ per share) | Risk $1.36 to make $1.23 a share | Risk $1.36 to make $1.23 | PASS |  |  |
| GDX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $82.46 – $83.42 · 3.6% above · turned here 5× | $82.46 – $83.42 · 3.6% · 5× | PASS |  |  |
| GDX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GDX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $77.99 – $80.18 · price is inside this zone · turned here 4× | $77.99 – $80.18 · 0.0% · 4× | PASS |  |  |
| GDX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.477 | 3.4770 | PASS |  |  |
| GDX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| GDX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| GDX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $80.18 | $80.18 | PASS |  |  |
| GDX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 80.18, nearest zone high 80.18 | equal | PASS |  |  |
| GDX | TS1c | S5: the Buy on the bar = the Buy in the box | $80.18 | $80.18 | PASS |  |  |
| GDX | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| GDX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $73.23 -8.7% | $73.23 -8.7% | PASS |  |  |
| GDX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GDX | TS4 | Target = nearest resistance edge and its % from the buy | $82.46 +2.8% | $82.46 +2.8% | PASS |  |  |
| GDX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GDX | TS6 | Risk $ (and reward $ per share) | Risk $6.95 to make $2.28 a share | Risk $6.95 to make $2.28 | PASS |  |  |
| GDXU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $24.76 – $24.90 · 1.3% above · turned here 2× | $24.76 – $24.90 · 1.3% · 2× | PASS |  |  |
| GDXU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GDXU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $22.26 – $22.62 · 7.5% below · turned here 2× | $22.26 – $22.62 · 7.5% · 2× | PASS |  |  |
| GDXU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.406 | 2.4060 | PASS |  |  |
| GDXU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| GDXU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| GDXU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $22.62 | $22.62 | PASS |  |  |
| GDXU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 22.62, nearest zone high 22.62 | equal | PASS |  |  |
| GDXU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $22.62 | $22.62 | PASS |  |  |
| GDXU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.9% below | 6.9% below | PASS |  |  |
| GDXU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $17.81 -21.3% | $17.81 -21.3% | PASS |  |  |
| GDXU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GDXU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $24.76 +9.5% | $24.76 +9.5% | PASS |  |  |
| GDXU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| GDXU.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.81 to make $2.14 a share | Risk $4.81 to make $2.14 | PASS |  |  |
| GE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $329.17 – $336.53 · 1.2% above · turned here 3× | $329.17 – $336.53 · 1.2% · 3× | PASS |  |  |
| GE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $319.14 – $321.17 · 1.3% below · turned here 2× | $319.14 – $321.17 · 1.3% · 2× | PASS |  |  |
| GE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 10.4662 | 10.4652 | PASS |  |  |
| GE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| GE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $321.17 | $321.17 | PASS |  |  |
| GE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 321.17, nearest zone high 321.17 | equal | PASS |  |  |
| GE | TS1c | S5: the Buy on the bar = the Buy in the box | $321.17 | $321.17 | PASS |  |  |
| GE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| GE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $300.24 -6.5% | $300.24 -6.5% | PASS |  |  |
| GE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GE | TS4 | Target = nearest resistance edge and its % from the buy | $329.17 +2.5% | $329.17 +2.5% | PASS |  |  |
| GE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| GE | TS6 | Risk $ (and reward $ per share) | Risk $20.93 to make $8.00 a share | Risk $20.93 to make $8.00 | PASS |  |  |
| GEV | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $777.00 – $807.00 · 0.5% above · turned here 3× | $777.00 – $807.00 · 0.5% · 3× | PASS |  |  |
| GEV | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GEV | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $731.00 · 5.5% below · turned here 1× | $731.00 · 5.5% · 1× | PASS |  |  |
| GEV | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 56.2705 | 56.2617 | PASS |  |  |
| GEV | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GEV | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $731.00 | $731.00 | PASS |  |  |
| GEV | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 731, nearest zone high 731 | equal | PASS |  |  |
| GEV | TS1c | S5: the Buy on the bar = the Buy in the box | $731.00 | $731.00 | PASS |  |  |
| GEV | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.3% below | 4.3% below | PASS |  |  |
| GEV | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $618.46 -15.4% | $618.46 -15.4% | PASS |  |  |
| GEV | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV | TS4 | Target = nearest resistance edge and its % from the buy | $777.00 +6.3% | $777.00 +6.3% | PASS |  |  |
| GEV | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| GEV | TS6 | Risk $ (and reward $ per share) | Risk $112.54 to make $46.00 a share | Risk $112.54 to make $46.00 | PASS |  |  |
| GEV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $52.71 – $54.63 · 1.8% above · turned here 3× | $52.71 – $54.63 · 1.8% · 3× | PASS |  |  |
| GEV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $50.19 · 3.1% below · turned here 1× | $50.19 · 3.1% · 1× | PASS |  |  |
| GEV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.6559 | 3.6554 | PASS |  |  |
| GEV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| GEV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $50.19 | $50.19 | PASS |  |  |
| GEV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 50.19, nearest zone high 50.19 | equal | PASS |  |  |
| GEV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $50.19 | $50.19 | PASS |  |  |
| GEV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.6% below | 1.6% below | PASS |  |  |
| GEV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $42.88 -14.6% | $42.88 -14.6% | PASS |  |  |
| GEV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GEV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $52.71 +5.0% | $52.71 +5.0% | PASS |  |  |
| GEV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GEV.TO | TS6 | Risk $ (and reward $ per share) | Risk $7.31 to make $2.52 a share | Risk $7.31 to make $2.52 | PASS |  |  |
| GGLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $70.15 · 11.2% above · turned here 1× | $70.15 · 11.2% · 1× | PASS |  |  |
| GGLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GGLL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $62.13 · 1.5% below · turned here 1× | $62.13 · 1.5% · 1× | PASS |  |  |
| GGLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.2963 | 5.2965 | PASS |  |  |
| GGLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| GGLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| GGLL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $62.13 | $62.13 | PASS |  |  |
| GGLL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 62.13, nearest zone high 62.13 | equal | PASS |  |  |
| GGLL | TS1c | S5: the Buy on the bar = the Buy in the box | $62.13 | $62.13 | PASS |  |  |
| GGLL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.2% below | 4.2% below | PASS |  |  |
| GGLL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $51.54 -17.0% | $51.54 -17.0% | PASS |  |  |
| GGLL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GGLL | TS4 | Target = nearest resistance edge and its % from the buy | $70.15 +12.9% | $70.15 +12.9% | PASS |  |  |
| GGLL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| GGLL | TS6 | Risk $ (and reward $ per share) | Risk $10.59 to make $8.02 a share | Risk $10.59 to make $8.02 | PASS |  |  |
| GIB-A.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $121.13 – $122.37 · 2.8% above · turned here 2× | $121.13 – $122.37 · 2.8% · 2× | PASS |  |  |
| GIB-A.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Transitioning — testing resistance | Transitioning — testing resistance | PASS |  |  |
| GIB-A.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.35 · 7.2% below · turned here 1× | $109.35 · 7.2% · 1× | PASS |  |  |
| GIB-A.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.75 | 2.7500 | PASS |  |  |
| GIB-A.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| GIB-A.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| GIB-A.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.35, nearest zone high 109.35 | equal | PASS |  |  |
| GIB-A.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $109.35 | $109.35 | PASS |  |  |
| GIB-A.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.2% below | 7.2% below | PASS |  |  |
| GIB-A.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $103.85 -5.0% | $103.85 -5.0% | PASS |  |  |
| GIB-A.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GIB-A.TO | TS4 | Target = nearest resistance edge and its % from the buy | $121.13 +10.8% | $121.13 +10.8% | PASS |  |  |
| GIB-A.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 2.1 : 1 | 2.1 : 1 | PASS |  |  |
| GIB-A.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.50 to make $11.78 a share | Risk $5.50 to make $11.78 | PASS |  |  |
| GOOGL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $293.72 – $295.67 · 5.0% above · turned here 3× | $293.72 – $295.67 · 5.0% · 3× | PASS |  |  |
| GOOGL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GOOGL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $270.00 – $276.92 · 1.0% below · turned here 3× | $270.00 – $276.92 · 1.0% · 3× | PASS |  |  |
| GOOGL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 10.4716 | 10.4717 | PASS |  |  |
| GOOGL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| GOOGL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| GOOGL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $276.92 | $276.92 | PASS |  |  |
| GOOGL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 276.92, nearest zone high 276.92 | equal | PASS |  |  |
| GOOGL | TS1c | S5: the Buy on the bar = the Buy in the box | $276.92 | $276.92 | PASS |  |  |
| GOOGL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.4% below | 2.4% below | PASS |  |  |
| GOOGL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $255.98 -7.6% | $255.98 -7.6% | PASS |  |  |
| GOOGL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GOOGL | TS4 | Target = nearest resistance edge and its % from the buy | $293.72 +6.1% | $293.72 +6.1% | PASS |  |  |
| GOOGL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| GOOGL | TS6 | Risk $ (and reward $ per share) | Risk $20.94 to make $16.80 a share | Risk $20.94 to make $16.80 | PASS |  |  |
| GRID | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $155.76 – $158.09 · 0.7% above · turned here 3× | $155.76 – $158.09 · 0.7% · 3× | PASS |  |  |
| GRID | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| GRID | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $149.77 – $152.95 · 1.1% below · turned here 3× | $149.77 – $152.95 · 1.1% · 3× | PASS |  |  |
| GRID | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.3086 | 4.3086 | PASS |  |  |
| GRID | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| GRID | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| GRID | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $152.95 | $152.95 | PASS |  |  |
| GRID | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 152.95, nearest zone high 152.95 | equal | PASS |  |  |
| GRID | TS1c | S5: the Buy on the bar = the Buy in the box | $152.95 | $152.95 | PASS |  |  |
| GRID | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| GRID | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $144.33 -5.6% | $144.33 -5.6% | PASS |  |  |
| GRID | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| GRID | TS4 | Target = nearest resistance edge and its % from the buy | $155.76 +1.8% | $155.76 +1.8% | PASS |  |  |
| GRID | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| GRID | TS6 | Risk $ (and reward $ per share) | Risk $8.62 to make $2.81 a share | Risk $8.62 to make $2.81 | PASS |  |  |
| HD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $353.55 – $353.98 · 4.3% above · turned here 2× | $353.55 – $353.98 · 4.3% · 2× | PASS |  |  |
| HD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $337.71 – $344.00 · price is inside this zone · turned here 3× | $337.71 – $344.00 · 0.0% · 3× | PASS |  |  |
| HD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.6008 | 8.6009 | PASS |  |  |
| HD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| HD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| HD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $344.00 | $344.00 | PASS |  |  |
| HD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 344, nearest zone high 344 | equal | PASS |  |  |
| HD | TS1c | S5: the Buy on the bar = the Buy in the box | $344.00 | $344.00 | PASS |  |  |
| HD | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| HD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $326.80 -5.0% | $326.80 -5.0% | PASS |  |  |
| HD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HD | TS4 | Target = nearest resistance edge and its % from the buy | $353.55 +2.8% | $353.55 +2.8% | PASS |  |  |
| HD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| HD | TS6 | Risk $ (and reward $ per share) | Risk $17.20 to make $9.55 a share | Risk $17.20 to make $9.55 | PASS |  |  |
| HURA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $39.48 · 6.0% above · turned here 1× | $39.48 · 6.0% · 1× | PASS |  |  |
| HURA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| HURA.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $36.76 · 1.3% below · turned here 1× | $36.76 · 1.3% · 1× | PASS |  |  |
| HURA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.4596 | 1.4596 | PASS |  |  |
| HURA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| HURA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| HURA.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $36.76 | $36.76 | PASS |  |  |
| HURA.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 36.76, nearest zone high 36.76 | equal | PASS |  |  |
| HURA.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $36.76 | $36.76 | PASS |  |  |
| HURA.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| HURA.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $33.84 -7.9% | $33.84 -7.9% | PASS |  |  |
| HURA.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HURA.TO | TS4 | Target = nearest resistance edge and its % from the buy | $39.48 +7.4% | $39.48 +7.4% | PASS |  |  |
| HURA.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| HURA.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.92 to make $2.72 a share | Risk $2.92 to make $2.72 | PASS |  |  |
| HXQ.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $113.28 · 2.5% above · turned here 1× | $113.28 · 2.5% · 1× | PASS |  |  |
| HXQ.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.90 · 0.5% below · turned here 1× | $109.90 · 0.5% · 1× | PASS |  |  |
| HXQ.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.6506 | 2.6506 | PASS |  |  |
| HXQ.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| HXQ.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| HXQ.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $109.90 | $109.90 | PASS |  |  |
| HXQ.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 109.9, nearest zone high 109.9 | equal | PASS |  |  |
| HXQ.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $109.90 | $109.90 | PASS |  |  |
| HXQ.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% below | 1.8% below | PASS |  |  |
| HXQ.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $104.60 -4.8% | $104.60 -4.8% | PASS |  |  |
| HXQ.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| HXQ.TO | TS4 | Target = nearest resistance edge and its % from the buy | $113.28 +3.1% | $113.28 +3.1% | PASS |  |  |
| HXQ.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| HXQ.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.30 to make $3.38 a share | Risk $5.30 to make $3.38 | PASS |  |  |
| JNJ | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $281.07 – $282.01 · 0.8% above · turned here 2× | $281.07 – $282.01 · 0.8% · 2× | PASS |  |  |
| JNJ | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JNJ | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $274.90 – $276.47 · 0.9% below · turned here 3× | $274.90 – $276.47 · 0.9% · 3× | PASS |  |  |
| JNJ | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.8937 | 6.8933 | PASS |  |  |
| JNJ | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| JNJ | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $276.47 | $276.47 | PASS |  |  |
| JNJ | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 276.47, nearest zone high 276.47 | equal | PASS |  |  |
| JNJ | TS1c | S5: the Buy on the bar = the Buy in the box | $276.47 | $276.47 | PASS |  |  |
| JNJ | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.2% below | 2.2% below | PASS |  |  |
| JNJ | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $262.68 -5.0% | $262.68 -5.0% | PASS |  |  |
| JNJ | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JNJ | TS4 | Target = nearest resistance edge and its % from the buy | $281.07 +1.7% | $281.07 +1.7% | PASS |  |  |
| JNJ | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| JNJ | TS6 | Risk $ (and reward $ per share) | Risk $13.79 to make $4.60 a share | Risk $13.79 to make $4.60 | PASS |  |  |
| JPM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $343.45 – $344.40 · 1.5% above · turned here 3× | $343.45 – $344.40 · 1.5% · 3× | PASS |  |  |
| JPM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| JPM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $337.25 · 0.3% below · turned here 1× | $337.25 · 0.3% · 1× | PASS |  |  |
| JPM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.3048 | 7.3048 | PASS |  |  |
| JPM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| JPM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| JPM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $337.25 | $337.25 | PASS |  |  |
| JPM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 337.25, nearest zone high 337.25 | equal | PASS |  |  |
| JPM | TS1c | S5: the Buy on the bar = the Buy in the box | $337.25 | $337.25 | PASS |  |  |
| JPM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.3% below | 0.3% below | PASS |  |  |
| JPM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $322.64 -4.3% | $322.64 -4.3% | PASS |  |  |
| JPM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| JPM | TS4 | Target = nearest resistance edge and its % from the buy | $343.45 +1.8% | $343.45 +1.8% | PASS |  |  |
| JPM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| JPM | TS6 | Risk $ (and reward $ per share) | Risk $14.61 to make $6.20 a share | Risk $14.61 to make $6.20 | PASS |  |  |
| KEYS | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $293.55 – $306.85 · 3.9% above · turned here 5× | $293.55 – $306.85 · 3.9% · 5× | PASS |  |  |
| KEYS | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| KEYS | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $275.27 · 2.5% below · turned here 1× | $275.27 · 2.5% · 1× | PASS |  |  |
| KEYS | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.1621 | 16.1622 | PASS |  |  |
| KEYS | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| KEYS | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| KEYS | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $275.27 | $275.27 | PASS |  |  |
| KEYS | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 275.27, nearest zone high 275.27 | equal | PASS |  |  |
| KEYS | TS1c | S5: the Buy on the bar = the Buy in the box | $275.27 | $275.27 | PASS |  |  |
| KEYS | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.6% below | 3.6% below | PASS |  |  |
| KEYS | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $242.95 -11.7% | $242.95 -11.7% | PASS |  |  |
| KEYS | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| KEYS | TS4 | Target = nearest resistance edge and its % from the buy | $293.55 +6.6% | $293.55 +6.6% | PASS |  |  |
| KEYS | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| KEYS | TS6 | Risk $ (and reward $ per share) | Risk $32.32 to make $18.28 a share | Risk $32.32 to make $18.28 | PASS |  |  |
| LIN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $521.23 – $525.87 · 1.2% above · turned here 4× | $521.23 – $525.87 · 1.2% · 4× | PASS |  |  |
| LIN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| LIN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $506.78 – $510.65 · 0.9% below · turned here 3× | $506.78 – $510.65 · 0.9% · 3× | PASS |  |  |
| LIN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.8671 | 8.8674 | PASS |  |  |
| LIN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| LIN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $510.65 | $510.65 | PASS |  |  |
| LIN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 510.65, nearest zone high 510.65 | equal | PASS |  |  |
| LIN | TS1c | S5: the Buy on the bar = the Buy in the box | $510.65 | $510.65 | PASS |  |  |
| LIN | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.4% below | 2.4% below | PASS |  |  |
| LIN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $492.92 -3.5% | $492.92 -3.5% | PASS |  |  |
| LIN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LIN | TS4 | Target = nearest resistance edge and its % from the buy | $521.23 +2.1% | $521.23 +2.1% | PASS |  |  |
| LIN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| LIN | TS6 | Risk $ (and reward $ per share) | Risk $17.73 to make $10.58 a share | Risk $17.73 to make $10.58 | PASS |  |  |
| LLY | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| LLY | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| LLY | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $1,333.22 · 5.5% below · turned here 1× | $1,333.22 · 5.5% · 1× | PASS |  |  |
| LLY | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 44.5458 | 44.5460 | PASS |  |  |
| LLY | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| LLY | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| LLY | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $1,333.22 | $1,333.22 | PASS |  |  |
| LLY | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 1333.22, nearest zone high 1333.22 | equal | PASS |  |  |
| LLY | TS1c | S5: the Buy on the bar = the Buy in the box | $1,333.22 | $1,333.22 | PASS |  |  |
| LLY | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.9% below | 6.9% below | PASS |  |  |
| LLY | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $1,244.13 -6.7% | $1,244.13 -6.7% | PASS |  |  |
| LLY | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| LLY | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| LLY | TS6 | Risk $ (and reward $ per share) | Risk $89.09 a share | Risk $89.09 | PASS |  |  |
| MDA.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $39.61 – $41.67 · 1.3% above · turned here 6× | $39.61 – $41.67 · 1.3% · 6× | PASS |  |  |
| MDA.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MDA.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.15 · 2.4% below · turned here 1× | $38.15 · 2.4% · 1× | PASS |  |  |
| MDA.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2804 | 2.2806 | PASS |  |  |
| MDA.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| MDA.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| MDA.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.15 | $38.15 | PASS |  |  |
| MDA.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 38.15, nearest zone high 38.15 | equal | PASS |  |  |
| MDA.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $38.15 | $38.15 | PASS |  |  |
| MDA.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.8% below | 4.8% below | PASS |  |  |
| MDA.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $33.59 -12.0% | $33.59 -12.0% | PASS |  |  |
| MDA.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MDA.TO | TS4 | Target = nearest resistance edge and its % from the buy | $39.61 +3.8% | $39.61 +3.8% | PASS |  |  |
| MDA.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MDA.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.56 to make $1.46 a share | Risk $4.56 to make $1.46 | PASS |  |  |
| META | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $672.77 – $673.58 · 7.4% above · turned here 2× | $672.77 – $673.58 · 7.4% · 2× | PASS |  |  |
| META | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 23.5 | 3 of 8 trend checks pass · ADX 23.5 | PASS |  |  |
| META | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $600.00 – $612.43 · 2.2% below · turned here 3× | $600.00 – $612.43 · 2.2% · 3× | PASS |  |  |
| META | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 22.6918 | 22.6918 | PASS |  |  |
| META | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| META | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| META | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $643.00 | $643.00 | PASS |  |  |
| META | TS1c | S5: the Buy on the bar = the Buy in the box | $643.00 | $643.00 | PASS |  |  |
| META | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.6% above | 2.6% above | PASS |  |  |
| META | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $597.62 -7.1% | $597.62 -7.1% | PASS |  |  |
| META | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| META | TS4 | Target = nearest resistance edge and its % from the buy | $672.77 +4.6% | $672.77 +4.6% | PASS |  |  |
| META | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| META | TS6 | Risk $ (and reward $ per share) | Risk $45.38 to make $29.77 a share | Risk $45.38 to make $29.77 | PASS |  |  |
| METU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $22.90 – $23.84 · 6.4% above · turned here 4× | $22.90 – $23.84 · 6.4% · 4× | PASS |  |  |
| METU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| METU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $20.19 – $20.95 · 2.6% below · turned here 2× | $20.19 – $20.95 · 2.6% · 2× | PASS |  |  |
| METU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6813 | 1.6814 | PASS |  |  |
| METU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| METU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| METU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $20.95 | $20.95 | PASS |  |  |
| METU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 20.95, nearest zone high 20.95 | equal | PASS |  |  |
| METU | TS1c | S5: the Buy on the bar = the Buy in the box | $20.95 | $20.95 | PASS |  |  |
| METU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.4% below | 5.4% below | PASS |  |  |
| METU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $17.59 -16.1% | $17.59 -16.1% | PASS |  |  |
| METU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| METU | TS4 | Target = nearest resistance edge and its % from the buy | $22.90 +9.3% | $22.90 +9.3% | PASS |  |  |
| METU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| METU | TS6 | Risk $ (and reward $ per share) | Risk $3.36 to make $1.95 a share | Risk $3.36 to make $1.95 | PASS |  |  |
| MRVL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $146.85 · 0.2% above · turned here 1× | $146.85 · 0.2% · 1× | PASS |  |  |
| MRVL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MRVL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $132.54 · 9.6% below · turned here 1× | $132.54 · 9.6% · 1× | PASS |  |  |
| MRVL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.8536 | 16.8537 | PASS |  |  |
| MRVL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| MRVL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| MRVL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $132.54 | $132.54 | PASS |  |  |
| MRVL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 132.54, nearest zone high 132.54 | equal | PASS |  |  |
| MRVL | TS1c | S5: the Buy on the bar = the Buy in the box | $132.54 | $132.54 | PASS |  |  |
| MRVL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 8.8% below | 8.8% below | PASS |  |  |
| MRVL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $98.83 -25.4% | $98.83 -25.4% | PASS |  |  |
| MRVL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MRVL | TS4 | Target = nearest resistance edge and its % from the buy | $146.85 +10.8% | $146.85 +10.8% | PASS |  |  |
| MRVL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| MRVL | TS6 | Risk $ (and reward $ per share) | Risk $33.71 to make $14.31 a share | Risk $33.71 to make $14.31 | PASS |  |  |
| MSFT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $551.15 · 6.4% above · turned here 1× | $551.15 · 6.4% · 1× | PASS |  |  |
| MSFT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Uptrend pulling back to support | Uptrend pulling back to support | PASS |  |  |
| MSFT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $513.73 – $517.78 · 0.0% below · turned here 2× | $513.73 – $517.78 · 0.0% · 2× | PASS |  |  |
| MSFT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 14.9256 | 14.9256 | PASS |  |  |
| MSFT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| MSFT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| MSFT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $517.78 | $517.78 | PASS |  |  |
| MSFT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 517.78, nearest zone high 517.78 | equal | PASS |  |  |
| MSFT | TS1c | S5: the Buy on the bar = the Buy in the box | $517.78 | $517.78 | PASS |  |  |
| MSFT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.0% below | 0.0% below | PASS |  |  |
| MSFT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $487.93 -5.8% | $487.93 -5.8% | PASS |  |  |
| MSFT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFT | TS4 | Target = nearest resistance edge and its % from the buy | $551.15 +6.4% | $551.15 +6.4% | PASS |  |  |
| MSFT | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.1 : 1 | 1.1 : 1 | PASS |  |  |
| MSFT | TS6 | Risk $ (and reward $ per share) | Risk $29.85 to make $33.37 a share | Risk $29.85 to make $33.37 | PASS |  |  |
| MSFU | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $37.64 · 1.1% above · turned here 1× | $37.64 · 1.1% · 1× | PASS |  |  |
| MSFU | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MSFU | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $36.15 · 2.9% below · turned here 1× | $36.15 · 2.9% · 1× | PASS |  |  |
| MSFU | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.2799 | 2.2800 | PASS |  |  |
| MSFU | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| MSFU | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| MSFU | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $36.15 | $36.15 | PASS |  |  |
| MSFU | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 36.15, nearest zone high 36.15 | equal | PASS |  |  |
| MSFU | TS1c | S5: the Buy on the bar = the Buy in the box | $36.15 | $36.15 | PASS |  |  |
| MSFU | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.7% below | 7.7% below | PASS |  |  |
| MSFU | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $31.59 -12.6% | $31.59 -12.6% | PASS |  |  |
| MSFU | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MSFU | TS4 | Target = nearest resistance edge and its % from the buy | $37.64 +4.1% | $37.64 +4.1% | PASS |  |  |
| MSFU | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MSFU | TS6 | Risk $ (and reward $ per share) | Risk $4.56 to make $1.49 a share | Risk $4.56 to make $1.49 | PASS |  |  |
| MTRX.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.20 · 3.7% above · turned here 1× | $30.20 · 3.7% · 1× | PASS |  |  |
| MTRX.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $29.09 – $29.56 · price is inside this zone · turned here 4× | $29.09 – $29.56 · 0.0% · 4× | PASS |  |  |
| MTRX.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.0223 | 1.0225 | PASS |  |  |
| MTRX.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| MTRX.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| MTRX.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $29.56 | $29.56 | PASS |  |  |
| MTRX.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 29.56, nearest zone high 29.56 | equal | PASS |  |  |
| MTRX.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $29.56 | $29.56 | PASS |  |  |
| MTRX.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| MTRX.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $27.52 -6.9% | $27.52 -6.9% | PASS |  |  |
| MTRX.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MTRX.TO | TS4 | Target = nearest resistance edge and its % from the buy | $30.20 +2.2% | $30.20 +2.2% | PASS |  |  |
| MTRX.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| MTRX.TO | TS6 | Risk $ (and reward $ per share) | Risk $2.04 to make $0.64 a share | Risk $2.04 to make $0.64 | PASS |  |  |
| MU.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $32.56 · 6.4% above · turned here 1× | $32.56 · 6.4% · 1× | PASS |  |  |
| MU.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| MU.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $28.57 – $28.78 · 5.9% below · turned here 2× | $28.57 – $28.78 · 5.9% · 2× | PASS |  |  |
| MU.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.554 | 2.5540 | PASS |  |  |
| MU.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| MU.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| MU.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $28.78 | $28.78 | PASS |  |  |
| MU.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 28.78, nearest zone high 28.78 | equal | PASS |  |  |
| MU.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $28.78 | $28.78 | PASS |  |  |
| MU.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 8.4% below | 8.4% below | PASS |  |  |
| MU.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $23.67 -17.7% | $23.67 -17.7% | PASS |  |  |
| MU.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| MU.TO | TS4 | Target = nearest resistance edge and its % from the buy | $32.56 +13.1% | $32.56 +13.1% | PASS |  |  |
| MU.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.7 : 1 | 0.7 : 1 | PASS |  |  |
| MU.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.11 to make $3.78 a share | Risk $5.11 to make $3.78 | PASS |  |  |
| NEE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $86.80 – $86.87 · 2.8% above · turned here 2× | $86.80 – $86.87 · 2.8% · 2× | PASS |  |  |
| NEE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| NEE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $84.27 – $85.68 · price is inside this zone · turned here 5× | $84.27 – $85.68 · 0.0% · 5× | PASS |  |  |
| NEE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.6785 | 1.6785 | PASS |  |  |
| NEE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| NEE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 13 zones match | match | PASS |  |  |
| NEE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $85.68 | $85.68 | PASS |  |  |
| NEE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 85.68, nearest zone high 85.68 | equal | PASS |  |  |
| NEE | TS1c | S5: the Buy on the bar = the Buy in the box | $85.68 | $85.68 | PASS |  |  |
| NEE | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| NEE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $82.32 -3.9% | $82.32 -3.9% | PASS |  |  |
| NEE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEE | TS4 | Target = nearest resistance edge and its % from the buy | $86.80 +1.3% | $86.80 +1.3% | PASS |  |  |
| NEE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| NEE | TS6 | Risk $ (and reward $ per share) | Risk $3.36 to make $1.12 a share | Risk $3.36 to make $1.12 | PASS |  |  |
| NEM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $120.00 – $122.00 · 8.3% above · turned here 6× | $120.00 – $122.00 · 8.3% · 6× | PASS |  |  |
| NEM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Weakening trend — testing support | Weakening trend — testing support | PASS |  |  |
| NEM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $109.83 – $112.18 · price is inside this zone · turned here 3× | $109.83 – $112.18 · 0.0% · 3× | PASS |  |  |
| NEM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.5356 | 4.5357 | PASS |  |  |
| NEM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| NEM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| NEM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $112.18 | $112.18 | PASS |  |  |
| NEM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 112.18, nearest zone high 112.18 | equal | PASS |  |  |
| NEM | TS1c | S5: the Buy on the bar = the Buy in the box | $112.18 | $112.18 | PASS |  |  |
| NEM | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| NEM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $103.11 -8.1% | $103.11 -8.1% | PASS |  |  |
| NEM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NEM | TS4 | Target = nearest resistance edge and its % from the buy | $120.00 +7.0% | $120.00 +7.0% | PASS |  |  |
| NEM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| NEM | TS6 | Risk $ (and reward $ per share) | Risk $9.07 to make $7.82 a share | Risk $9.07 to make $7.82 | PASS |  |  |
| NFLX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $61.39 · 3.1% above · turned here 1× | $61.39 · 3.1% · 1× | PASS |  |  |
| NFLX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFLX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFLX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.9739 | 1.9737 | PASS |  |  |
| NFLX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| NFLX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| NFLX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NFXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $10.57 · 7.4% above · turned here 1× | $10.57 · 7.4% · 1× | PASS |  |  |
| NFXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NFXL | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NFXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.7243 | 0.7257 | PASS |  |  |
| NFXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| NFXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| NFXL | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NTR.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $103.59 – $104.15 · 4.4% above · turned here 3× | $103.59 – $104.15 · 4.4% · 3× | PASS |  |  |
| NTR.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $98.61 · 0.7% below · turned here 1× | $98.61 · 0.7% · 1× | PASS |  |  |
| NTR.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8588 | 2.8593 | PASS |  |  |
| NTR.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| NTR.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| NTR.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $98.61 | $98.61 | PASS |  |  |
| NTR.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 98.61, nearest zone high 98.61 | equal | PASS |  |  |
| NTR.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $98.61 | $98.61 | PASS |  |  |
| NTR.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.0% below | 0.0% below | PASS |  |  |
| NTR.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $92.89 -5.8% | $92.89 -5.8% | PASS |  |  |
| NTR.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NTR.TO | TS4 | Target = nearest resistance edge and its % from the buy | $103.59 +5.1% | $103.59 +5.1% | PASS |  |  |
| NTR.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| NTR.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.72 to make $4.98 a share | Risk $5.72 to make $4.98 | PASS |  |  |
| NVDA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $164.27 · 5.2% above · turned here 1× | $164.27 · 5.2% · 1× | PASS |  |  |
| NVDA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NVDA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.8532 | 9.8532 | PASS |  |  |
| NVDA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| NVDA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| NVDA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| NVDL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. | no zone | PASS |  |  |
| NVDL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 4 of 8 trend checks pass | No resistance within 30% above · 4 of 8 trend checks pass | PASS |  |  |
| NVDL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $13.72 – $14.42 · 9.4% below · turned here 2× | $13.72 – $14.42 · 9.4% · 2× | PASS |  |  |
| NVDL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5809 | 2.5803 | PASS |  |  |
| NVDL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| NVDL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| NVDL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $14.42 | $14.42 | PASS |  |  |
| NVDL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 14.42, nearest zone high 14.42 | equal | PASS |  |  |
| NVDL | TS1c | S5: the Buy on the bar = the Buy in the box | $14.42 | $14.42 | PASS |  |  |
| NVDL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 11.8% below | 11.8% below | PASS |  |  |
| NVDL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $9.26 -35.8% | $9.26 -35.8% | PASS |  |  |
| NVDL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| NVDL | TS4 | "no resistance within N% above" vs the proximity filter | 30% | 30% | PASS |  |  |
| NVDL | TS6 | Risk $ (and reward $ per share) | Risk $5.16 a share | Risk $5.16 | PASS |  |  |
| ONTO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $215.07 – $232.49 · 8.3% above · turned here 6× | $215.07 – $232.49 · 8.3% · 6× | PASS |  |  |
| ONTO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ONTO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $195.19 – $204.07 · price is inside this zone · turned here 2× | $195.19 – $204.07 · 0.0% · 2× | PASS |  |  |
| ONTO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.968 | 17.9680 | PASS |  |  |
| ONTO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| ONTO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| ONTO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $204.07 | $204.07 | PASS |  |  |
| ONTO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 204.07, nearest zone high 204.07 | equal | PASS |  |  |
| ONTO | TS1c | S5: the Buy on the bar = the Buy in the box | $204.07 | $204.07 | PASS |  |  |
| ONTO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| ONTO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $168.13 -17.6% | $168.13 -17.6% | PASS |  |  |
| ONTO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ONTO | TS4 | Target = nearest resistance edge and its % from the buy | $215.07 +5.4% | $215.07 +5.4% | PASS |  |  |
| ONTO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| ONTO | TS6 | Risk $ (and reward $ per share) | Risk $35.94 to make $11.00 a share | Risk $35.94 to make $11.00 | PASS |  |  |
| ORBX.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $15.45 – $15.71 · 6.8% above · turned here 2× | $15.45 – $15.71 · 6.8% · 2× | PASS |  |  |
| ORBX.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $14.29 · 1.2% below · turned here 1× | $14.29 · 1.2% · 1× | PASS |  |  |
| ORBX.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6946 | 0.6946 | PASS |  |  |
| ORBX.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ORBX.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ORBX.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $14.29 | $14.29 | PASS |  |  |
| ORBX.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 14.29, nearest zone high 14.29 | equal | PASS |  |  |
| ORBX.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $14.29 | $14.29 | PASS |  |  |
| ORBX.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% below | 2.1% below | PASS |  |  |
| ORBX.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.90 -9.7% | $12.90 -9.7% | PASS |  |  |
| ORBX.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ORBX.TO | TS4 | Target = nearest resistance edge and its % from the buy | $15.45 +8.1% | $15.45 +8.1% | PASS |  |  |
| ORBX.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| ORBX.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.39 to make $1.16 a share | Risk $1.39 to make $1.16 | PASS |  |  |
| ORCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $122.76 · 7.1% above · turned here 1× | $122.76 · 7.1% · 1× | PASS |  |  |
| ORCL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ORCL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $114.50 · 0.1% below · turned here 1× | $114.50 · 0.1% · 1× | PASS |  |  |
| ORCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.999 | 7.9990 | PASS |  |  |
| ORCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| ORCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| ORCL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $114.50 | $114.50 | PASS |  |  |
| ORCL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 114.5, nearest zone high 114.5 | equal | PASS |  |  |
| ORCL | TS1c | S5: the Buy on the bar = the Buy in the box | $114.50 | $114.50 | PASS |  |  |
| ORCL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.9% below | 3.9% below | PASS |  |  |
| ORCL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $98.50 -14.0% | $98.50 -14.0% | PASS |  |  |
| ORCL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ORCL | TS4 | Target = nearest resistance edge and its % from the buy | $122.76 +7.2% | $122.76 +7.2% | PASS |  |  |
| ORCL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| ORCL | TS6 | Risk $ (and reward $ per share) | Risk $16.00 to make $8.26 a share | Risk $16.00 to make $8.26 | PASS |  |  |
| PG | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 0.3% below $173.57 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| PG | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| PG | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 6 of 8 trend checks pass | No resistance within 30% above · 6 of 8 trend checks pass | PASS |  |  |
| PG | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $170.52 · 0.7% below · turned here 1× | $170.52 · 0.7% · 1× | PASS |  |  |
| PG | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 3.2747 | 3.2695 | PASS |  |  |
| PG | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| PG | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $170.52 | $170.52 | PASS |  |  |
| PG | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 170.52, nearest zone high 170.52 | equal | PASS |  |  |
| PG | TS1c | S5: the Buy on the bar = the Buy in the box | $170.52 | $170.52 | PASS |  |  |
| PG | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.4% below | 1.4% below | PASS |  |  |
| PG | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $163.97 -3.8% | $163.97 -3.8% | PASS |  |  |
| PG | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PG | TS4w | words "at/near its 52-week high" vs the real gap to the 252-bar high | near, within 3% | 0.3% below the high $173.57 | PASS |  |  |
| PG | TS6 | Risk $ (and reward $ per share) | Risk $6.55 a share | Risk $6.55 | PASS |  |  |
| PLD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $127.29 – $128.11 · 1.7% above · turned here 2× | $127.29 – $128.11 · 1.7% · 2× | PASS |  |  |
| PLD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| PLD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $124.69 – $126.92 · price is inside this zone · turned here 6× | $124.69 – $126.92 · 0.0% · 6× | PASS |  |  |
| PLD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.506 | 2.5054 | PASS |  |  |
| PLD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 15 zones | all hold | PASS |  |  |
| PLD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 15 zones match | match | PASS |  |  |
| PLD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $126.92 | $126.92 | PASS |  |  |
| PLD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 126.92, nearest zone high 126.92 | equal | PASS |  |  |
| PLD | TS1c | S5: the Buy on the bar = the Buy in the box | $126.92 | $126.92 | PASS |  |  |
| PLD | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| PLD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $121.91 -3.9% | $121.91 -3.9% | PASS |  |  |
| PLD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PLD | TS4 | Target = nearest resistance edge and its % from the buy | $127.29 +0.3% | $127.29 +0.3% | PASS |  |  |
| PLD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| PLD | TS6 | Risk $ (and reward $ per share) | Risk $5.01 to make $0.37 a share | Risk $5.01 to make $0.37 | PASS |  |  |
| PNG.V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3.30 · 5.8% above · turned here 1× | $3.30 · 5.8% · 1× | PASS |  |  |
| PNG.V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| PNG.V | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| PNG.V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.2319 | 0.2323 | PASS |  |  |
| PNG.V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| PNG.V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| PNG.V | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QCOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $183.44 – $185.59 · 10.9% above · turned here 3× | $183.44 – $185.59 · 10.9% · 3× | PASS |  |  |
| QCOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 11.2, under 15 | 3 of 8 trend checks pass · ADX 11.2, under 15 | PASS |  |  |
| QCOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $156.22 – $158.85 · 4.0% below · turned here 2× | $156.22 – $158.85 · 4.0% · 2× | PASS |  |  |
| QCOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.9181 | 8.9178 | PASS |  |  |
| QCOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| QCOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| QCOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $172.12 | $172.12 | PASS |  |  |
| QCOM | TS1c | S5: the Buy on the bar = the Buy in the box | $172.12 | $172.12 | PASS |  |  |
| QCOM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.1% above | 2.1% above | PASS |  |  |
| QCOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $154.28 -10.4% | $154.28 -10.4% | PASS |  |  |
| QCOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QCOM | TS4 | Target = nearest resistance edge and its % from the buy | $183.44 +6.6% | $183.44 +6.6% | PASS |  |  |
| QCOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| QCOM | TS6 | Risk $ (and reward $ per share) | Risk $17.84 to make $11.32 a share | Risk $17.84 to make $11.32 | PASS |  |  |
| QPUX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $3.90 · 18.9% above · turned here 1× | $3.90 · 18.9% · 1× | PASS |  |  |
| QPUX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| QPUX | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| QPUX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.9026 | 0.9029 | PASS |  |  |
| QPUX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 1 zones | all hold | PASS |  |  |
| QPUX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 1 zones match | match | PASS |  |  |
| QPUX | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| QTUM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $127.52 · 4.1% above · turned here 1× | $127.52 · 4.1% · 1× | PASS |  |  |
| QTUM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| QTUM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $119.01 – $121.34 · 0.9% below · turned here 4× | $119.01 – $121.34 · 0.9% · 4× | PASS |  |  |
| QTUM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.8191 | 4.8185 | PASS |  |  |
| QTUM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 13 zones | all hold | PASS |  |  |
| QTUM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $121.34 | $121.34 | PASS |  |  |
| QTUM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 121.34, nearest zone high 121.34 | equal | PASS |  |  |
| QTUM | TS1c | S5: the Buy on the bar = the Buy in the box | $121.34 | $121.34 | PASS |  |  |
| QTUM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.5% below | 2.5% below | PASS |  |  |
| QTUM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $111.70 -7.9% | $111.70 -7.9% | PASS |  |  |
| QTUM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| QTUM | TS4 | Target = nearest resistance edge and its % from the buy | $127.52 +5.1% | $127.52 +5.1% | PASS |  |  |
| QTUM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.6 : 1 | 0.6 : 1 | PASS |  |  |
| QTUM | TS6 | Risk $ (and reward $ per share) | Risk $9.64 to make $6.18 a share | Risk $9.64 to make $6.18 | PASS |  |  |
| RBOT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $28.00 · 3.6% above · turned here 1× | $28.00 · 3.6% · 1× | PASS |  |  |
| RBOT.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| RBOT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6137 | 0.6132 | PASS |  |  |
| RBOT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| RBOT.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| RTX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $203.03 – $206.73 · 2.8% above · turned here 6× | $203.03 – $206.73 · 2.8% · 6× | PASS |  |  |
| RTX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RTX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $192.59 – $194.17 · 1.7% below · turned here 5× | $192.59 – $194.17 · 1.7% · 5× | PASS |  |  |
| RTX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.301 | 5.3011 | PASS |  |  |
| RTX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| RTX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $194.17 | $194.17 | PASS |  |  |
| RTX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 194.17, nearest zone high 194.17 | equal | PASS |  |  |
| RTX | TS1c | S5: the Buy on the bar = the Buy in the box | $194.17 | $194.17 | PASS |  |  |
| RTX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.4% below | 0.4% below | PASS |  |  |
| RTX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $183.57 -5.5% | $183.57 -5.5% | PASS |  |  |
| RTX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RTX | TS4 | Target = nearest resistance edge and its % from the buy | $203.03 +4.6% | $203.03 +4.6% | PASS |  |  |
| RTX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| RTX | TS6 | Risk $ (and reward $ per share) | Risk $10.60 to make $8.86 a share | Risk $10.60 to make $8.86 | PASS |  |  |
| RY.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $287.36 – $288.75 · 2.5% above · turned here 2× | $287.36 – $288.75 · 2.5% · 2× | PASS |  |  |
| RY.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RY.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $279.07 · 0.5% below · turned here 1× | $279.07 · 0.5% · 1× | PASS |  |  |
| RY.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.4813 | 4.4812 | PASS |  |  |
| RY.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| RY.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| RY.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $279.07 | $279.07 | PASS |  |  |
| RY.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 279.07, nearest zone high 279.07 | equal | PASS |  |  |
| RY.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $279.07 | $279.07 | PASS |  |  |
| RY.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.3% below | 2.3% below | PASS |  |  |
| RY.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $270.11 -3.2% | $270.11 -3.2% | PASS |  |  |
| RY.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RY.TO | TS4 | Target = nearest resistance edge and its % from the buy | $287.36 +3.0% | $287.36 +3.0% | PASS |  |  |
| RY.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.9 : 1 | 0.9 : 1 | PASS |  |  |
| RY.TO | TS6 | Risk $ (and reward $ per share) | Risk $8.96 to make $8.29 a share | Risk $8.96 to make $8.29 | PASS |  |  |
| SETM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $23.68 – $23.88 · 7.1% above · turned here 2× | $23.68 – $23.88 · 7.1% · 2× | PASS |  |  |
| SETM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| SETM | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SETM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.0038 | 1.0037 | PASS |  |  |
| SETM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| SETM | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SGRD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $18.27 · 1.8% above · turned here 1× | $18.27 · 1.8% · 1× | PASS |  |  |
| SGRD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $17.20 · 4.2% below · turned here 1× | $17.20 · 4.2% · 1× | PASS |  |  |
| SGRD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.4036 | 0.4036 | PASS |  |  |
| SGRD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| SGRD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| SGRD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $17.20 | $17.20 | PASS |  |  |
| SGRD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 17.2, nearest zone high 17.2 | equal | PASS |  |  |
| SGRD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $17.20 | $17.20 | PASS |  |  |
| SGRD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.6% below | 4.6% below | PASS |  |  |
| SGRD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $16.39 -4.7% | $16.39 -4.7% | PASS |  |  |
| SGRD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SGRD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $18.27 +6.2% | $18.27 +6.2% | PASS |  |  |
| SGRD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.3 : 1 | 1.3 : 1 | PASS |  |  |
| SGRD.TO | TS6 | Risk $ (and reward $ per share) | Risk $0.81 to make $1.07 a share | Risk $0.81 to make $1.07 | PASS |  |  |
| SMH | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $503.63 · 9.5% above · turned here 1× | $503.63 · 9.5% · 1× | PASS |  |  |
| SMH | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SMH | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $445.59 · 3.2% below · turned here 1× | $445.59 · 3.2% · 1× | PASS |  |  |
| SMH | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 24.3517 | 24.3517 | PASS |  |  |
| SMH | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 8 zones | all hold | PASS |  |  |
| SMH | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 8 zones match | match | PASS |  |  |
| SMH | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $445.59 | $445.59 | PASS |  |  |
| SMH | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 445.59, nearest zone high 445.59 | equal | PASS |  |  |
| SMH | TS1c | S5: the Buy on the bar = the Buy in the box | $445.59 | $445.59 | PASS |  |  |
| SMH | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 3.5% below | 3.5% below | PASS |  |  |
| SMH | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $396.89 -10.9% | $396.89 -10.9% | PASS |  |  |
| SMH | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SMH | TS4 | Target = nearest resistance edge and its % from the buy | $503.63 +13.0% | $503.63 +13.0% | PASS |  |  |
| SMH | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.2 : 1 | 1.2 : 1 | PASS |  |  |
| SMH | TS6 | Risk $ (and reward $ per share) | Risk $48.70 to make $58.04 a share | Risk $48.70 to make $58.04 | PASS |  |  |
| SNDK.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $19.52 · 1.6% above · turned here 1× | $19.52 · 1.6% · 1× | PASS |  |  |
| SNDK.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| SNDK.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5371 | 2.5371 | PASS |  |  |
| SNDK.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| SNDK.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| SNDK.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| SO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $94.95 – $95.72 · 1.4% above · turned here 3× | $94.95 – $95.72 · 1.4% · 3× | PASS |  |  |
| SO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $93.16 – $93.47 · 0.2% below · turned here 3× | $93.16 – $93.47 · 0.2% · 3× | PASS |  |  |
| SO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.8377 | 1.8382 | PASS |  |  |
| SO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| SO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| SO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $93.47 | $93.47 | PASS |  |  |
| SO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 93.47, nearest zone high 93.47 | equal | PASS |  |  |
| SO | TS1c | S5: the Buy on the bar = the Buy in the box | $93.47 | $93.47 | PASS |  |  |
| SO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.2% below | 1.2% below | PASS |  |  |
| SO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $89.79 -3.9% | $89.79 -3.9% | PASS |  |  |
| SO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SO | TS4 | Target = nearest resistance edge and its % from the buy | $94.95 +1.6% | $94.95 +1.6% | PASS |  |  |
| SO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| SO | TS6 | Risk $ (and reward $ per share) | Risk $3.68 to make $1.48 a share | Risk $3.68 to make $1.48 | PASS |  |  |
| SOXL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $48.50 – $50.09 · 3.3% above · turned here 3× | $48.50 – $50.09 · 3.3% · 3× | PASS |  |  |
| SOXL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $35.70 – $44.53 · 5.1% below · turned here 5× | $35.70 – $44.53 · 5.1% · 5× | PASS |  |  |
| SOXL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 12.6338 | 12.6343 | PASS |  |  |
| SOXL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $44.53 | $44.53 | PASS |  |  |
| SOXL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 44.53, nearest zone high 44.53 | equal | PASS |  |  |
| SOXL | TS1c | S5: the Buy on the bar = the Buy in the box | $44.53 | $44.53 | PASS |  |  |
| SOXL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 8.7% below | 8.7% below | PASS |  |  |
| SOXL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $19.26 -56.7% | $19.26 -56.7% | PASS |  |  |
| SOXL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL | TS4 | Target = nearest resistance edge and its % from the buy | $48.50 +8.9% | $48.50 +8.9% | PASS |  |  |
| SOXL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| SOXL | TS6 | Risk $ (and reward $ per share) | Risk $25.27 to make $3.97 a share | Risk $25.27 to make $3.97 | PASS |  |  |
| SOXL.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $12.05 – $13.46 · 2.1% above · turned here 3× | $12.05 – $13.46 · 2.1% · 3× | PASS |  |  |
| SOXL.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $9.22 – $10.73 · 9.1% below · turned here 4× | $9.22 – $10.73 · 9.1% · 4× | PASS |  |  |
| SOXL.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.042 | 2.0424 | PASS |  |  |
| SOXL.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $10.73 | $10.73 | PASS |  |  |
| SOXL.NE | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 10.73, nearest zone high 10.73 | equal | PASS |  |  |
| SOXL.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $10.73 | $10.73 | PASS |  |  |
| SOXL.NE | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 12.8% below | 12.8% below | PASS |  |  |
| SOXL.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $6.65 -38.1% | $6.65 -38.1% | PASS |  |  |
| SOXL.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL.NE | TS4 | Target = nearest resistance edge and its % from the buy | $12.05 +12.3% | $12.05 +12.3% | PASS |  |  |
| SOXL.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| SOXL.NE | TS6 | Risk $ (and reward $ per share) | Risk $4.08 to make $1.32 a share | Risk $4.08 to make $1.32 | PASS |  |  |
| SOXX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $154.69 – $163.07 · 10.7% above · turned here 4× | $154.69 – $163.07 · 10.7% · 4× | PASS |  |  |
| SOXX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $130.75 · 6.5% below · turned here 1× | $130.75 · 6.5% · 1× | PASS |  |  |
| SOXX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.5276 | 8.5273 | PASS |  |  |
| SOXX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| SOXX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| SOXX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $130.75 | $130.75 | PASS |  |  |
| SOXX | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 130.75, nearest zone high 130.75 | equal | PASS |  |  |
| SOXX | TS1c | S5: the Buy on the bar = the Buy in the box | $130.75 | $130.75 | PASS |  |  |
| SOXX | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.4% below | 7.4% below | PASS |  |  |
| SOXX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $113.69 -13.0% | $113.69 -13.0% | PASS |  |  |
| SOXX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXX | TS4 | Target = nearest resistance edge and its % from the buy | $154.69 +18.3% | $154.69 +18.3% | PASS |  |  |
| SOXX | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.4 : 1 | 1.4 : 1 | PASS |  |  |
| SOXX | TS6 | Risk $ (and reward $ per share) | Risk $17.06 to make $23.94 a share | Risk $17.06 to make $23.94 | PASS |  |  |
| SPCL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $12.15 · 20.3% above · turned here 1× | $12.15 · 20.3% · 1× | PASS |  |  |
| SPCL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $8.20 · 18.8% below · turned here 1× | $8.20 · 18.8% · 1× | PASS |  |  |
| SPCL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.7767 | 1.7762 | PASS |  |  |
| SPCL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| SPCL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| SPCL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $8.20 | $8.20 | PASS |  |  |
| SPCL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 8.2, nearest zone high 8.2 | equal | PASS |  |  |
| SPCL | TS1c | S5: the Buy on the bar = the Buy in the box | $8.20 | $8.20 | PASS |  |  |
| SPCL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 21.5% below | 21.5% below | PASS |  |  |
| SPCL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $4.65 -43.3% | $4.65 -43.3% | PASS |  |  |
| SPCL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SPCL | TS4 | Target = nearest resistance edge and its % from the buy | $12.15 +48.2% | $12.15 +48.2% | PASS |  |  |
| SPCL | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.1 : 1 | 1.1 : 1 | PASS |  |  |
| SPCL | TS6 | Risk $ (and reward $ per share) | Risk $3.55 to make $3.95 a share | Risk $3.55 to make $3.95 | PASS |  |  |
| TSLA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $380.15 – $393.63 · 0.1% above · turned here 8× | $380.15 – $393.63 · 0.1% · 8× | PASS |  |  |
| TSLA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLA | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $364.02 – $368.60 · 2.9% below · turned here 3× | $364.02 – $368.60 · 2.9% · 3× | PASS |  |  |
| TSLA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 16.5579 | 16.5579 | PASS |  |  |
| TSLA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| TSLA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| TSLA | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $368.60 | $368.60 | PASS |  |  |
| TSLA | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 368.6, nearest zone high 368.6 | equal | PASS |  |  |
| TSLA | TS1c | S5: the Buy on the bar = the Buy in the box | $368.60 | $368.60 | PASS |  |  |
| TSLA | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.9% below | 2.9% below | PASS |  |  |
| TSLA | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $335.48 -9.0% | $335.48 -9.0% | PASS |  |  |
| TSLA | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLA | TS4 | Target = nearest resistance edge and its % from the buy | $380.15 +3.1% | $380.15 +3.1% | PASS |  |  |
| TSLA | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| TSLA | TS6 | Risk $ (and reward $ per share) | Risk $33.12 to make $11.55 a share | Risk $33.12 to make $11.55 | PASS |  |  |
| TSLL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $9.91 – $9.97 · 1.0% above · turned here 2× | $9.91 – $9.97 · 1.0% · 2× | PASS |  |  |
| TSLL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSLL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $9.10 · 7.2% below · turned here 1× | $9.10 · 7.2% · 1× | PASS |  |  |
| TSLL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8753 | 0.8752 | PASS |  |  |
| TSLL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| TSLL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| TSLL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $9.10 | $9.10 | PASS |  |  |
| TSLL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 9.1, nearest zone high 9.1 | equal | PASS |  |  |
| TSLL | TS1c | S5: the Buy on the bar = the Buy in the box | $9.10 | $9.10 | PASS |  |  |
| TSLL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 7.1% below | 7.1% below | PASS |  |  |
| TSLL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $7.35 -19.2% | $7.35 -19.2% | PASS |  |  |
| TSLL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSLL | TS4 | Target = nearest resistance edge and its % from the buy | $9.91 +8.9% | $9.91 +8.9% | PASS |  |  |
| TSLL | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| TSLL | TS6 | Risk $ (and reward $ per share) | Risk $1.75 to make $0.81 a share | Risk $1.75 to make $0.81 | PASS |  |  |
| TSM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $360.55 · 0.4% above · turned here 1× | $360.55 · 0.4% · 1× | PASS |  |  |
| TSM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| TSM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $350.44 – $351.33 · 2.1% below · turned here 3× | $350.44 – $351.33 · 2.1% · 3× | PASS |  |  |
| TSM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.7604 | 17.7605 | PASS |  |  |
| TSM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 9 zones | all hold | PASS |  |  |
| TSM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 9 zones match | match | PASS |  |  |
| TSM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $351.33 | $351.33 | PASS |  |  |
| TSM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 351.33, nearest zone high 351.33 | equal | PASS |  |  |
| TSM | TS1c | S5: the Buy on the bar = the Buy in the box | $351.33 | $351.33 | PASS |  |  |
| TSM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 5.9% below | 5.9% below | PASS |  |  |
| TSM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $315.81 -10.1% | $315.81 -10.1% | PASS |  |  |
| TSM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| TSM | TS4 | Target = nearest resistance edge and its % from the buy | $360.55 +2.6% | $360.55 +2.6% | PASS |  |  |
| TSM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| TSM | TS6 | Risk $ (and reward $ per share) | Risk $35.52 to make $9.22 a share | Risk $35.52 to make $9.22 | PASS |  |  |
| UBOT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $16.00 · 7.2% above · turned here 1× | $16.00 · 7.2% · 1× | PASS |  |  |
| UBOT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| UBOT | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| UBOT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8546 | 0.8553 | PASS |  |  |
| UBOT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| UBOT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| UBOT | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| UFO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $40.68 · 3.4% above · turned here 1× | $40.68 · 3.4% · 1× | PASS |  |  |
| UFO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| UFO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.31 – $39.50 · price is inside this zone · turned here 3× | $38.31 – $39.50 · 0.0% · 3× | PASS |  |  |
| UFO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.392 | 1.3920 | PASS |  |  |
| UFO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| UFO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $39.50 | $39.50 | PASS |  |  |
| UFO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 39.5, nearest zone high 39.5 | equal | PASS |  |  |
| UFO | TS1c | S5: the Buy on the bar = the Buy in the box | $39.50 | $39.50 | PASS |  |  |
| UFO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| UFO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $36.72 -7.0% | $36.72 -7.0% | PASS |  |  |
| UFO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| UFO | TS4 | Target = nearest resistance edge and its % from the buy | $40.68 +3.0% | $40.68 +3.0% | PASS |  |  |
| UFO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| UFO | TS6 | Risk $ (and reward $ per share) | Risk $2.78 to make $1.18 a share | Risk $2.78 to make $1.18 | PASS |  |  |
| URA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $30.40 · 1.3% above · turned here 1× | $30.40 · 1.3% · 1× | PASS |  |  |
| URA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| URA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| URA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.4673 | 1.4673 | PASS |  |  |
| URA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| URA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| URA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| URAA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $11.65 · 3.0% above · turned here 1× | $11.65 · 3.0% · 1× | PASS |  |  |
| URAA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| URAA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| URAA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.2214 | 1.2217 | PASS |  |  |
| URAA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| URAA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| URAA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| V | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $442.23 · 6.0% above · turned here 1× | $442.23 · 6.0% · 1× | PASS |  |  |
| V | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Uptrend pulling back to support | Uptrend pulling back to support | PASS |  |  |
| V | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $414.60 · 0.6% below · turned here 1× | $414.60 · 0.6% · 1× | PASS |  |  |
| V | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 8.7332 | 8.7332 | PASS |  |  |
| V | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| V | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| V | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $414.60 | $414.60 | PASS |  |  |
| V | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 414.6, nearest zone high 414.6 | equal | PASS |  |  |
| V | TS1c | S5: the Buy on the bar = the Buy in the box | $414.60 | $414.60 | PASS |  |  |
| V | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.8% below | 2.8% below | PASS |  |  |
| V | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $397.13 -4.2% | $397.13 -4.2% | PASS |  |  |
| V | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| V | TS4 | Target = nearest resistance edge and its % from the buy | $442.23 +6.7% | $442.23 +6.7% | PASS |  |  |
| V | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.6 : 1 | 1.6 : 1 | PASS |  |  |
| V | TS6 | Risk $ (and reward $ per share) | Risk $17.47 to make $27.63 a share | Risk $17.47 to make $27.63 | PASS |  |  |
| VFV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $192.95 – $193.80 · 0.8% above · turned here 2× | $192.95 – $193.80 · 0.8% · 2× | PASS |  |  |
| VFV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VFV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $188.75 – $191.22 · 0.1% below · turned here 3× | $188.75 – $191.22 · 0.1% · 3× | PASS |  |  |
| VFV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.7837 | 2.7835 | PASS |  |  |
| VFV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| VFV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| VFV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $191.22 | $191.22 | PASS |  |  |
| VFV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 191.22, nearest zone high 191.22 | equal | PASS |  |  |
| VFV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $191.22 | $191.22 | PASS |  |  |
| VFV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.1% below | 0.1% below | PASS |  |  |
| VFV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $185.65 -2.9% | $185.65 -2.9% | PASS |  |  |
| VFV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VFV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $192.95 +0.9% | $192.95 +0.9% | PASS |  |  |
| VFV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| VFV.TO | TS6 | Risk $ (and reward $ per share) | Risk $5.57 to make $1.73 a share | Risk $5.57 to make $1.73 | PASS |  |  |
| VRT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $189.66 · 0.8% above · turned here 1× | $189.66 · 0.8% · 1× | PASS |  |  |
| VRT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| VRT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $170.80 – $187.24 · 0.5% below · turned here 5× | $170.80 – $187.24 · 0.5% · 5× | PASS |  |  |
| VRT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 17.1008 | 17.0999 | PASS |  |  |
| VRT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| VRT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| VRT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $187.24 | $187.24 | PASS |  |  |
| VRT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 187.24, nearest zone high 187.24 | equal | PASS |  |  |
| VRT | TS1c | S5: the Buy on the bar = the Buy in the box | $187.24 | $187.24 | PASS |  |  |
| VRT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.8% below | 0.8% below | PASS |  |  |
| VRT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $153.04 -18.3% | $153.04 -18.3% | PASS |  |  |
| VRT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| VRT | TS4 | Target = nearest resistance edge and its % from the buy | $189.66 +1.3% | $189.66 +1.3% | PASS |  |  |
| VRT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| VRT | TS6 | Risk $ (and reward $ per share) | Risk $34.20 to make $2.42 a share | Risk $34.20 to make $2.42 | PASS |  |  |
| WDC.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $20.20 · 12.9% above · turned here 1× | $20.20 · 12.9% · 1× | PASS |  |  |
| WDC.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $15.70 · 12.2% below · turned here 1× | $15.70 · 12.2% · 1× | PASS |  |  |
| WDC.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 1.5936 | 1.5936 | PASS |  |  |
| WDC.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 2 zones | all hold | PASS |  |  |
| WDC.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 2 zones match | match | PASS |  |  |
| WDC.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 15.7, nearest zone high 15.7 | equal | PASS |  |  |
| WDC.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $15.70 | $15.70 | PASS |  |  |
| WDC.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 12.2% below | 12.2% below | PASS |  |  |
| WDC.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $12.51 -20.3% | $12.51 -20.3% | PASS |  |  |
| WDC.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WDC.TO | TS4 | Target = nearest resistance edge and its % from the buy | $20.20 +28.7% | $20.20 +28.7% | PASS |  |  |
| WDC.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.4 : 1 | 1.4 : 1 | PASS |  |  |
| WDC.TO | TS6 | Risk $ (and reward $ per share) | Risk $3.19 to make $4.50 a share | Risk $3.19 to make $4.50 | PASS |  |  |
| WELL | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $255.20 · 4.1% above · turned here 1× | $255.20 · 4.1% · 1× | PASS |  |  |
| WELL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WELL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $243.04 · 0.8% below · turned here 1× | $243.04 · 0.8% · 1× | PASS |  |  |
| WELL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 5.3272 | 5.3270 | PASS |  |  |
| WELL | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 12 zones | all hold | PASS |  |  |
| WELL | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 12 zones match | match | PASS |  |  |
| WELL | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $243.04 | $243.04 | PASS |  |  |
| WELL | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 243.04, nearest zone high 243.04 | equal | PASS |  |  |
| WELL | TS1c | S5: the Buy on the bar = the Buy in the box | $243.04 | $243.04 | PASS |  |  |
| WELL | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.7% below | 0.7% below | PASS |  |  |
| WELL | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $232.39 -4.4% | $232.39 -4.4% | PASS |  |  |
| WELL | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WELL | TS4 | Target = nearest resistance edge and its % from the buy | $255.20 +5.0% | $255.20 +5.0% | PASS |  |  |
| WELL | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.1 : 1 | 1.1 : 1 | PASS |  |  |
| WELL | TS6 | Risk $ (and reward $ per share) | Risk $10.65 to make $12.16 a share | Risk $10.65 to make $12.16 | PASS |  |  |
| WMT | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $128.75 – $129.69 · 0.9% above · turned here 2× | $128.75 – $129.69 · 0.9% · 2× | PASS |  |  |
| WMT | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| WMT | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $125.91 – $127.19 · 0.3% below · turned here 3× | $125.91 – $127.19 · 0.3% · 3× | PASS |  |  |
| WMT | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.7322 | 2.7321 | PASS |  |  |
| WMT | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| WMT | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| WMT | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $127.19 | $127.19 | PASS |  |  |
| WMT | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 127.19, nearest zone high 127.19 | equal | PASS |  |  |
| WMT | TS1c | S5: the Buy on the bar = the Buy in the box | $127.19 | $127.19 | PASS |  |  |
| WMT | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.0% below | 1.0% below | PASS |  |  |
| WMT | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $121.73 -4.3% | $121.73 -4.3% | PASS |  |  |
| WMT | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| WMT | TS4 | Target = nearest resistance edge and its % from the buy | $128.75 +1.2% | $128.75 +1.2% | PASS |  |  |
| WMT | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.3 : 1 | 0.3 : 1 | PASS |  |  |
| WMT | TS6 | Risk $ (and reward $ per share) | Risk $5.46 to make $1.56 a share | Risk $5.46 to make $1.56 | PASS |  |  |
| XCHP.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $110.04 · 6.0% above · turned here 1× | $110.04 · 6.0% · 1× | PASS |  |  |
| XCHP.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XCHP.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $95.50 · 8.0% below · turned here 1× | $95.50 · 8.0% · 1× | PASS |  |  |
| XCHP.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 6.3772 | 6.3772 | PASS |  |  |
| XCHP.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| XCHP.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| XCHP.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $95.50 | $95.50 | PASS |  |  |
| XCHP.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 95.5, nearest zone high 95.5 | equal | PASS |  |  |
| XCHP.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $95.50 | $95.50 | PASS |  |  |
| XCHP.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 9.3% below | 9.3% below | PASS |  |  |
| XCHP.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $82.75 -13.4% | $82.75 -13.4% | PASS |  |  |
| XCHP.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XCHP.TO | TS4 | Target = nearest resistance edge and its % from the buy | $110.04 +15.2% | $110.04 +15.2% | PASS |  |  |
| XCHP.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.1 : 1 | 1.1 : 1 | PASS |  |  |
| XCHP.TO | TS6 | Risk $ (and reward $ per share) | Risk $12.75 to make $14.54 a share | Risk $12.75 to make $14.54 | PASS |  |  |
| XDRV.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $40.34 · 2.8% above · turned here 1× | $40.34 · 2.8% · 1× | PASS |  |  |
| XDRV.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XDRV.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $38.62 – $38.88 · 0.9% below · turned here 2× | $38.62 – $38.88 · 0.9% · 2× | PASS |  |  |
| XDRV.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.8624 | 0.8624 | PASS |  |  |
| XDRV.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| XDRV.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| XDRV.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $38.88 | $38.88 | PASS |  |  |
| XDRV.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 38.88, nearest zone high 38.88 | equal | PASS |  |  |
| XDRV.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $38.88 | $38.88 | PASS |  |  |
| XDRV.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 2.0% below | 2.0% below | PASS |  |  |
| XDRV.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $37.16 -4.4% | $37.16 -4.4% | PASS |  |  |
| XDRV.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XDRV.TO | TS4 | Target = nearest resistance edge and its % from the buy | $40.34 +3.8% | $40.34 +3.8% | PASS |  |  |
| XDRV.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| XDRV.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.72 to make $1.46 a share | Risk $1.72 to make $1.46 | PASS |  |  |
| XEQT.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $44.58 – $44.64 · 0.8% above · turned here 3× | $44.58 – $44.64 · 0.8% · 3× | PASS |  |  |
| XEQT.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XEQT.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $43.93 – $44.41 · price is inside this zone · turned here 5× | $43.93 – $44.41 · 0.0% · 5× | PASS |  |  |
| XEQT.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.5658 | 0.5654 | PASS |  |  |
| XEQT.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 14 zones | all hold | PASS |  |  |
| XEQT.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 14 zones match | match | PASS |  |  |
| XEQT.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $44.41 | $44.41 | PASS |  |  |
| XEQT.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 44.41, nearest zone high 44.41 | equal | PASS |  |  |
| XEQT.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $44.41 | $44.41 | PASS |  |  |
| XEQT.TO | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| XEQT.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $43.28 -2.5% | $43.28 -2.5% | PASS |  |  |
| XEQT.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XEQT.TO | TS4 | Target = nearest resistance edge and its % from the buy | $44.58 +0.4% | $44.58 +0.4% | PASS |  |  |
| XEQT.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.2 : 1 | 0.2 : 1 | PASS |  |  |
| XEQT.TO | TS6 | Risk $ (and reward $ per share) | Risk $1.13 to make $0.17 a share | Risk $1.13 to make $0.17 | PASS |  |  |
| XETM.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $64.70 · 5.8% above · turned here 1× | $64.70 · 5.8% · 1× | PASS |  |  |
| XETM.TO | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| XETM.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5104 | 2.5104 | PASS |  |  |
| XETM.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| XETM.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| XETM.TO | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| XGD.TO | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $51.53 – $52.21 · 0.4% above · turned here 3× | $51.53 – $52.21 · 0.4% · 3× | PASS |  |  |
| XGD.TO | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XGD.TO | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $49.44 – $51.12 · 0.4% below · turned here 4× | $49.44 – $51.12 · 0.4% · 4× | PASS |  |  |
| XGD.TO | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0762 | 2.0762 | PASS |  |  |
| XGD.TO | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| XGD.TO | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| XGD.TO | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $51.12 | $51.12 | PASS |  |  |
| XGD.TO | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 51.12, nearest zone high 51.12 | equal | PASS |  |  |
| XGD.TO | TS1c | S5: the Buy on the bar = the Buy in the box | $51.12 | $51.12 | PASS |  |  |
| XGD.TO | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 0.6% above | 0.6% above | PASS |  |  |
| XGD.TO | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $46.97 -8.1% | $46.97 -8.1% | PASS |  |  |
| XGD.TO | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XGD.TO | TS4 | Target = nearest resistance edge and its % from the buy | $51.53 +0.8% | $51.53 +0.8% | PASS |  |  |
| XGD.TO | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.1 : 1 | 0.1 : 1 | PASS |  |  |
| XGD.TO | TS6 | Risk $ (and reward $ per share) | Risk $4.15 to make $0.41 a share | Risk $4.15 to make $0.41 | PASS |  |  |
| XOM | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $167.58 – $168.58 · 0.4% above · turned here 2× | $167.58 – $168.58 · 0.4% · 2× | PASS |  |  |
| XOM | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| XOM | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $163.88 · 1.9% below · turned here 1× | $163.88 · 1.9% · 1× | PASS |  |  |
| XOM | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 4.2479 | 4.2486 | PASS |  |  |
| XOM | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| XOM | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| XOM | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $163.88 | $163.88 | PASS |  |  |
| XOM | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 163.88, nearest zone high 163.88 | equal | PASS |  |  |
| XOM | TS1c | S5: the Buy on the bar = the Buy in the box | $163.88 | $163.88 | PASS |  |  |
| XOM | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 1.8% below | 1.8% below | PASS |  |  |
| XOM | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $155.38 -5.2% | $155.38 -5.2% | PASS |  |  |
| XOM | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| XOM | TS4 | Target = nearest resistance edge and its % from the buy | $167.58 +2.3% | $167.58 +2.3% | PASS |  |  |
| XOM | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| XOM | TS6 | Risk $ (and reward $ per share) | Risk $8.50 to make $3.70 a share | Risk $8.50 to make $3.70 | PASS |  |  |
