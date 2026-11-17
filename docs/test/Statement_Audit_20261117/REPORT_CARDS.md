# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-17T14:53 · dumps: AAPL, F, NVDA, RIVN, SMCI, SMH, SOXL.NE

Verdicts: PASS 256 · WRONG 0 (CRITICAL) · MISLEADING 0 (HIGH/LOW per row) · UNVERIFIED 5 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 7 | 0 |
| card-price-data | 14 | 0 |
| card-relative-strength | 28 | 0 |
| card-trade-setup | 56 | 0 |

Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).
Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).
NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| F | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $11.35 | last close $11.57 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| RIVN | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $11.98 | last close $12.10 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SMCI | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $23.83 | last close $25.03 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SMH | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $453.16 | last close $461.90 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| SOXL.NE | TS-live-side | levels are placed on a side of price using /api/sr currentPrice (today's live bar), the card's words use the last close | sr price $11.75 | last close $12.30 | UNVERIFIED | INFO | a zone between the two prices can sit on a different side than the words say; mid-session only (known Low) |
| AAPL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $351.73 | $351.73 | PASS |  |  |
| AAPL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.3% | 0.30% | PASS |  |  |
| AAPL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| AAPL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| AAPL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $351.73 · close 0.30% above · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 16 close | payload values | PASS |  |  |
| AAPL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| F | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $14.64 | $14.64 | PASS |  |  |
| F | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.97% | -20.97% | PASS |  |  |
| F | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| F | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| F | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| F | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $14.64 · close 20.97% below · Nov 16 close | payload values | PASS |  |  |
| F | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| NVDA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.37 | $243.37 | PASS |  |  |
| NVDA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -35.84% | -35.84% | PASS |  |  |
| NVDA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.37 · close 35.84% below · Nov 16 close | payload values | PASS |  |  |
| NVDA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| RIVN | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $17.16 | $17.16 | PASS |  |  |
| RIVN | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -29.47% | -29.49% | PASS |  |  |
| RIVN | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| RIVN | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| RIVN | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| RIVN | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $17.16 · close 29.47% below · Nov 16 close | payload values | PASS |  |  |
| RIVN | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SMCI | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $45.77 | $45.77 | PASS |  |  |
| SMCI | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -45.31% | -45.31% | PASS |  |  |
| SMCI | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SMCI | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SMCI | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SMCI | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $45.77 · close 45.31% below · Nov 16 close | payload values | PASS |  |  |
| SMCI | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SMH | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $639.47 | $639.47 | PASS |  |  |
| SMH | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -27.77% | -27.77% | PASS |  |  |
| SMH | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SMH | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SMH | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SMH | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $639.47 · close 27.77% below · Nov 16 close | payload values | PASS |  |  |
| SMH | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $40.79 | $40.79 | PASS |  |  |
| SOXL.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -69.85% | -69.85% | PASS |  |  |
| SOXL.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $40.79 · close 69.85% below · Nov 16 close | payload values | PASS |  |  |
| SOXL.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $352.78 · Nov 16 | $352.78 · Nov 16 | PASS |  |  |
| F | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.24 / Rank: 7/11] X | RS 98.43 Mom 2.24 Rank 7/11 | PASS |  |  |
| F | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| F | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| F | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $11.57 · Nov 16 | $11.57 · Nov 16 | PASS |  |  |
| NVDA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| NVDA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| NVDA | HB3 | earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming | ⚠️ EARNINGS TODAY | ⚠️ EARNINGS TODAY | PASS |  |  |
| NVDA | HB3d | earnings badge tooltip: date and calendar days until | 2026-11-17, 0 days | 2026-11-17, 0 days | PASS |  |  |
| NVDA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $156.14 · Nov 16 | $156.14 · Nov 16 | PASS |  |  |
| RIVN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Consumer Discretionary (XLY) — RS: 98.43 / Mom: +2.24 / Rank: 7/11] X | RS 98.43 Mom 2.24 Rank 7/11 | PASS |  |  |
| RIVN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| RIVN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| RIVN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.10 · Nov 16 | $12.10 · Nov 16 | PASS |  |  |
| SMCI | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| SMCI | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| SMCI | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMCI | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $25.03 · Nov 16 | $25.03 · Nov 16 | PASS |  |  |
| SMH | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SMH | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $461.90 · Nov 16 | $461.90 · Nov 16 | PASS |  |  |
| SOXL.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL.NE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.30 · Nov 16 | $12.30 · Nov 16 | PASS |  |  |
| AAPL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $360.83 | $360.83 | PASS |  |  |
| AAPL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $352.78 | $352.78 | PASS |  |  |
| AAPL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $360.83 / $243.42 | $360.83 / $243.42 | PASS |  |  |
| AAPL | PD3 | % from High | -2.2% | -2.2% | PASS |  |  |
| AAPL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15.1B | bars: $15,395,834,259 | PASS | LOW |  |
| F | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $17.78 | $17.78 | PASS |  |  |
| F | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $11.57 | $11.57 | PASS |  |  |
| F | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $17.78 / $11.11 | $17.78 / $11.11 | PASS |  |  |
| F | PD3 | % from High | -34.9% | -34.9% | PASS |  |  |
| F | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $507M | bars: $512,503,146 | PASS | LOW |  |
| NVDA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $243.37 | $243.37 | PASS |  |  |
| NVDA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $156.14 | $156.14 | PASS |  |  |
| NVDA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $243.37 / $148.80 | $243.37 / $148.80 | PASS |  |  |
| NVDA | PD3 | % from High | -35.8% | -35.8% | PASS |  |  |
| NVDA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $23.4B | bars: $23,758,416,354 | PASS | LOW |  |
| RIVN | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $22.69 | $22.69 | PASS |  |  |
| RIVN | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.10 | $12.10 | PASS |  |  |
| RIVN | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $22.69 / $11.38 | $22.69 / $11.38 | PASS |  |  |
| RIVN | PD3 | % from High | -46.7% | -46.7% | PASS |  |  |
| RIVN | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $314M | bars: $330,623,352 | PASS | LOW |  |
| SMCI | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $51.40 | $51.40 | PASS |  |  |
| SMCI | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $25.03 | $25.03 | PASS |  |  |
| SMCI | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $51.40 / $19.48 | $51.40 / $19.48 | PASS |  |  |
| SMCI | PD3 | % from High | -51.3% | -51.3% | PASS |  |  |
| SMCI | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $1.0B | bars: $1,019,443,015 | PASS | LOW |  |
| SMH | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $671.83 | $671.83 | PASS |  |  |
| SMH | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $461.90 | $461.90 | PASS |  |  |
| SMH | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $671.83 / $314.07 | $671.83 / $314.07 | PASS |  |  |
| SMH | PD3 | % from High | -31.2% | -31.2% | PASS |  |  |
| SMH | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $4.0B | bars: $4,223,616,371 | PASS | LOW |  |
| SOXL.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $74.21 | $74.21 | PASS |  |  |
| SOXL.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.30 | $12.30 | PASS |  |  |
| SOXL.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $74.21 / $7.92 | $74.21 / $7.92 | PASS |  |  |
| SOXL.NE | PD3 | % from High | -83.4% | -83.4% | PASS |  |  |
| SOXL.NE | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| AAPL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $352.78 / RS 1.18 | $352.78 / RS 1.18 | PASS |  |  |
| AAPL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.18 | 1.18 | PASS |  |  |
| AAPL | RS2 | Stock 52W Return and S&P 52W Return | +29.5% / +10.1% | +29.5% / +10.1% | PASS |  |  |
| AAPL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 64 | 64 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| AAPL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +29.5% clears | +29.5% clears | PASS |  |  |
| F | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $11.57 / RS 0.80 | $11.57 / RS 0.80 | PASS |  |  |
| F | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.80 | 0.80 | PASS |  |  |
| F | RS2 | Stock 52W Return and S&P 52W Return | -12.3% / +10.1% | -12.3% / +10.1% | PASS |  |  |
| F | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| F | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 34 | 34 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| F | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| F | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -12.3% negative | -12.3% negative | PASS |  |  |
| NVDA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $156.14 / RS 0.75 | $156.14 / RS 0.75 | PASS |  |  |
| NVDA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.75 | 0.75 | PASS |  |  |
| NVDA | RS2 | Stock 52W Return and S&P 52W Return | -17.9% / +10.1% | -17.9% / +10.1% | PASS |  |  |
| NVDA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 30 | 30 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -17.9% negative | -17.9% negative | PASS |  |  |
| RIVN | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.10 / RS 0.73 | $12.10 / RS 0.73 | PASS |  |  |
| RIVN | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.73 | 0.73 | PASS |  |  |
| RIVN | RS2 | Stock 52W Return and S&P 52W Return | -19.9% / +10.1% | -19.9% / +10.1% | PASS |  |  |
| RIVN | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| RIVN | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 28 | 28 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| RIVN | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| RIVN | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -19.9% negative | -19.9% negative | PASS |  |  |
| SMCI | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $25.03 / RS 0.62 | $25.03 / RS 0.62 | PASS |  |  |
| SMCI | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.62 | 0.62 | PASS |  |  |
| SMCI | RS2 | Stock 52W Return and S&P 52W Return | -31.3% / +10.1% | -31.3% / +10.1% | PASS |  |  |
| SMCI | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SMCI | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 20 | 20 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SMCI | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market (momentum accelerating) | Well behind the market (momentum accelerating) | PASS |  |  |
| SMCI | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -31.3% negative | -31.3% negative | PASS |  |  |
| SMH | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $461.90 / RS 1.22 | $461.90 / RS 1.22 | PASS |  |  |
| SMH | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.22 | 1.22 | PASS |  |  |
| SMH | RS2 | Stock 52W Return and S&P 52W Return | +34.3% / +10.1% | +34.3% / +10.1% | PASS |  |  |
| SMH | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SMH | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 68 | 68 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SMH | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Ahead of the market (momentum fading) | Ahead of the market (momentum fading) | PASS |  |  |
| SMH | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +34.3% clears | +34.3% clears | PASS |  |  |
| SOXL.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.30 / RS 1.10 | $12.30 / RS 1.10 | PASS |  |  |
| SOXL.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.10 | 1.10 | PASS |  |  |
| SOXL.NE | RS2 | Stock 52W Return and S&P 52W Return | +21.7% / +10.1% | +21.7% / +10.1% | PASS |  |  |
| SOXL.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 58 | 58 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +21.7% clears | +21.7% clears | PASS |  |  |
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
| F | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $11.44 – $11.46 · 0.8% above · turned here 2× | $11.44 – $11.46 · 0.8% · 2× | PASS |  |  |
| F | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| F | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $11.11 · 2.1% below · turned here 1× | $11.11 · 2.1% · 1× | PASS |  |  |
| F | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.3429 | 0.3429 | PASS |  |  |
| F | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 10 zones | all hold | PASS |  |  |
| F | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 10 zones match | match | PASS |  |  |
| F | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $11.11 | $11.11 | PASS |  |  |
| F | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 11.11, nearest zone high 11.11 | equal | PASS |  |  |
| F | TS1c | S5: the Buy on the bar = the Buy in the box | $11.11 | $11.11 | PASS |  |  |
| F | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 4.0% below | 4.0% below | PASS |  |  |
| F | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $10.42 -6.2% | $10.42 -6.2% | PASS |  |  |
| F | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| F | TS4 | Target = nearest resistance edge and its % from the buy | $11.44 +3.0% | $11.44 +3.0% | PASS |  |  |
| F | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| F | TS6 | Risk $ (and reward $ per share) | Risk $0.69 to make $0.33 a share | Risk $0.69 to make $0.33 | PASS |  |  |
| NVDA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $164.27 · 5.2% above · turned here 1× | $164.27 · 5.2% · 1× | PASS |  |  |
| NVDA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NVDA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.8532 | 9.8532 | PASS |  |  |
| NVDA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| NVDA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| NVDA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| RIVN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $12.65 · 5.6% above · turned here 1× | $12.65 · 5.6% · 1× | PASS |  |  |
| RIVN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| RIVN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $11.38 · 5.0% below · turned here 1× | $11.38 · 5.0% · 1× | PASS |  |  |
| RIVN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 0.6486 | 0.6486 | PASS |  |  |
| RIVN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 6 zones | all hold | PASS |  |  |
| RIVN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 6 zones match | match | PASS |  |  |
| RIVN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $11.38 | $11.38 | PASS |  |  |
| RIVN | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 11.38, nearest zone high 11.38 | equal | PASS |  |  |
| RIVN | TS1c | S5: the Buy on the bar = the Buy in the box | $11.38 | $11.38 | PASS |  |  |
| RIVN | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.0% below | 6.0% below | PASS |  |  |
| RIVN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $10.08 -11.4% | $10.08 -11.4% | PASS |  |  |
| RIVN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| RIVN | TS4 | Target = nearest resistance edge and its % from the buy | $12.65 +11.2% | $12.65 +11.2% | PASS |  |  |
| RIVN | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.0 : 1 | 1.0 : 1 | PASS |  |  |
| RIVN | TS6 | Risk $ (and reward $ per share) | Risk $1.30 to make $1.27 a share | Risk $1.30 to make $1.27 | PASS |  |  |
| SMCI | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $25.41 – $25.68 · 6.6% above · turned here 3× | $25.41 – $25.68 · 6.6% · 3× | PASS |  |  |
| SMCI | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SMCI | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $23.38 · 1.9% below · turned here 1× | $23.38 · 1.9% · 1× | PASS |  |  |
| SMCI | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5785 | 2.5785 | PASS |  |  |
| SMCI | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 5 zones | all hold | PASS |  |  |
| SMCI | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 5 zones match | match | PASS |  |  |
| SMCI | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $23.38 | $23.38 | PASS |  |  |
| SMCI | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 23.38, nearest zone high 23.38 | equal | PASS |  |  |
| SMCI | TS1c | S5: the Buy on the bar = the Buy in the box | $23.38 | $23.38 | PASS |  |  |
| SMCI | TS2 | "x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header) | 6.6% below | 6.6% below | PASS |  |  |
| SMCI | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $18.22 -22.1% | $18.22 -22.1% | PASS |  |  |
| SMCI | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SMCI | TS4 | Target = nearest resistance edge and its % from the buy | $25.41 +8.7% | $25.41 +8.7% | PASS |  |  |
| SMCI | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.4 : 1 | 0.4 : 1 | PASS |  |  |
| SMCI | TS6 | Risk $ (and reward $ per share) | Risk $5.16 to make $2.03 a share | Risk $5.16 to make $2.03 | PASS |  |  |
| SMH | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $503.63 · 11.1% above · turned here 1× | $503.63 · 11.1% · 1× | PASS |  |  |
| SMH | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 34.1 | 3 of 8 trend checks pass · ADX 34.1 | PASS |  |  |
| SMH | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $445.59 · 1.7% below · turned here 1× | $445.59 · 1.7% · 1× | PASS |  |  |
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
| SOXL.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $12.05 – $13.46 · 2.6% above · turned here 3× | $12.05 – $13.46 · 2.6% · 3× | PASS |  |  |
| SOXL.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $9.22 – $10.73 · 8.7% below · turned here 4× | $9.22 – $10.73 · 8.7% · 4× | PASS |  |  |
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
