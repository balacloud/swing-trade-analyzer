# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-18T10:28 · dumps: AAPL, AMD, DUK, ETN, FCX, NVDA, PLD, SOXL.NE

Verdicts: PASS 308 · WRONG 0 (CRITICAL) · MISLEADING 0 (HIGH/LOW per row) · UNVERIFIED 1 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 8 | 1 |
| card-price-data | 16 | 0 |
| card-relative-strength | 32 | 0 |
| card-trade-setup | 65 | 0 |

Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).
Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).
NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| DUK | U-BO | numbers on the card no statement claimed (exhaustive scan) | 1.5 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AAPL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $351.46 | $351.46 | PASS |  |  |
| AAPL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.13% | 0.13% | PASS |  |  |
| AAPL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| AAPL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| AAPL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $351.46 · close 0.13% above · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| AAPL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| AMD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $658.52 | $658.52 | PASS |  |  |
| AMD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.55% | -23.55% | PASS |  |  |
| AMD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $658.52 · close 23.55% below · Nov 17 close | payload values | PASS |  |  |
| AMD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $127.67 | $127.67 | PASS |  |  |
| DUK | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 1.7% | 1.70% | PASS |  |  |
| DUK | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-04 | 2026-11-04 | PASS |  |  |
| DUK | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 1.82 | 1.82 | PASS |  |  |
| DUK | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | BREAKOUT_CONFIRMED | BREAKOUT_CONFIRMED | PASS |  |  |
| DUK | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $127.67 · close 1.70% above · broke out Nov 4 on 1.82× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| DUK | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| DUK | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
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
| NVDA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.37 | $243.37 | PASS |  |  |
| NVDA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.12% | -36.12% | PASS |  |  |
| NVDA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.37 · close 36.12% below · Nov 17 close | payload values | PASS |  |  |
| NVDA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PLD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $142.69 | $142.69 | PASS |  |  |
| PLD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12% | -12.01% | PASS |  |  |
| PLD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PLD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PLD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PLD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $142.69 · close 12.00% below · Nov 17 close | payload values | PASS |  |  |
| PLD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| SOXL.NE | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $40.79 | $40.79 | PASS |  |  |
| SOXL.NE | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -69.7% | -69.70% | PASS |  |  |
| SOXL.NE | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| SOXL.NE | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| SOXL.NE | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| SOXL.NE | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $40.79 · close 69.70% below · Nov 17 close | payload values | PASS |  |  |
| SOXL.NE | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $351.91 · Nov 17 | $351.91 · Nov 17 | PASS |  |  |
| AMD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AMD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $503.41 · Nov 17 | $503.41 · Nov 17 | PASS |  |  |
| DUK | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Utilities (XLU) — RS: 96.68 / Mom: +2.87 / Rank: 10/11] XLU IMPROVING | RS 96.68 Mom 2.87 Rank 10/11 | PASS |  |  |
| DUK | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| DUK | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| DUK | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $129.84 · Nov 17 | $129.84 · Nov 17 | PASS |  |  |
| ETN | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Industrials (XLI) — RS: 95.46 / Mom: -0.47 / Rank: 11/11] XLI LAGGING | RS 95.46 Mom -0.47 Rank 11/11 | PASS |  |  |
| ETN | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| ETN | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| ETN | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $337.11 · Nov 17 | $337.11 · Nov 17 | PASS |  |  |
| FCX | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Materials (XLB) — RS: 98.66 / Mom: +0.7 / Rank: 6/11] XLB IMPROVING | RS 98.66 Mom 0.7 Rank 6/11 | PASS |  |  |
| FCX | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| FCX | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| FCX | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $55.30 · Nov 17 | $55.30 · Nov 17 | PASS |  |  |
| NVDA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| NVDA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| NVDA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $155.46 · Nov 17 | $155.46 · Nov 17 | PASS |  |  |
| PLD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.12 / Mom: +1.22 / Rank: 9/11] XLRE IMPROV | RS 97.12 Mom 1.22 Rank 9/11 | PASS |  |  |
| PLD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| PLD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PLD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $125.56 · Nov 17 | $125.56 · Nov 17 | PASS |  |  |
| SOXL.NE | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| SOXL.NE | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $12.36 · Nov 17 | $12.36 · Nov 17 | PASS |  |  |
| AAPL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $360.83 | $360.83 | PASS |  |  |
| AAPL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $351.91 | $351.91 | PASS |  |  |
| AAPL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $360.83 / $242.57 | $360.83 / $242.57 | PASS |  |  |
| AAPL | PD3 | % from High | -2.5% | -2.5% | PASS |  |  |
| AAPL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15.0B | bars: $15,393,891,469 | PASS | LOW |  |
| AMD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $658.52 | $658.52 | PASS |  |  |
| AMD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $503.41 | $503.41 | PASS |  |  |
| AMD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $658.52 / $188.22 | $658.52 / $188.22 | PASS |  |  |
| AMD | PD3 | % from High | -23.6% | -23.6% | PASS |  |  |
| AMD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $12.6B | bars: $13,823,305,403 | PASS | LOW |  |
| DUK | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $131.87 | $131.87 | PASS |  |  |
| DUK | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $129.84 | $129.84 | PASS |  |  |
| DUK | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $131.87 / $110.06 | $131.87 / $110.06 | PASS |  |  |
| DUK | PD3 | % from High | -1.5% | -1.5% | PASS |  |  |
| DUK | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $544M | bars: $569,831,002 | PASS | LOW |  |
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
| NVDA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $243.37 | $243.37 | PASS |  |  |
| NVDA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $155.46 | $155.46 | PASS |  |  |
| NVDA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $243.37 / $148.80 | $243.37 / $148.80 | PASS |  |  |
| NVDA | PD3 | % from High | -36.1% | -36.1% | PASS |  |  |
| NVDA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $24.0B | bars: $24,430,752,602 | PASS | LOW |  |
| PLD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $152.14 | $152.14 | PASS |  |  |
| PLD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $125.56 | $125.56 | PASS |  |  |
| PLD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $152.14 / $117.70 | $152.14 / $117.70 | PASS |  |  |
| PLD | PD3 | % from High | -17.5% | -17.5% | PASS |  |  |
| PLD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $462M | bars: $484,416,291 | PASS | LOW |  |
| SOXL.NE | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $74.21 | $74.21 | PASS |  |  |
| SOXL.NE | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $12.36 | $12.36 | PASS |  |  |
| SOXL.NE | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $74.21 / $7.92 | $74.21 / $7.92 | PASS |  |  |
| SOXL.NE | PD3 | % from High | -83.3% | -83.3% | PASS |  |  |
| SOXL.NE | PD4 | S5: liquidity when the bars have no volume (the Technical Read says so) | N/A (no volume data) | N/A | PASS |  | a Yahoo avgVolume figure would contradict the "No volume data" line |
| AAPL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $351.91 / RS 1.19 | $351.91 / RS 1.19 | PASS |  |  |
| AAPL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.19 | 1.19 | PASS |  |  |
| AAPL | RS2 | Stock 52W Return and S&P 52W Return | +32.0% / +11.2% | +32.0% / +11.2% | PASS |  |  |
| AAPL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 65 | 65 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| AAPL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +32.0% clears | +32.0% clears | PASS |  |  |
| AMD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $503.41 / RS 1.88 | $503.41 / RS 1.88 | PASS |  |  |
| AMD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.88 | 1.88 | PASS |  |  |
| AMD | RS2 | Stock 52W Return and S&P 52W Return | +109.3% / +11.2% | +109.3% / +11.2% | PASS |  |  |
| AMD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AMD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 99 | 99 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AMD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well ahead of the market (momentum fading) | Well ahead of the market (momentum fading) | PASS |  |  |
| AMD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +109.3% clears | +109.3% clears | PASS |  |  |
| DUK | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $129.84 / RS 0.96 | $129.84 / RS 0.97 | PASS |  | RS is rounded to 3 dp and then 2 dp by the page |
| DUK | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.96 | 0.97 | PASS |  |  |
| DUK | RS2 | Stock 52W Return and S&P 52W Return | +7.3% / +11.2% | +7.3% / +11.2% | PASS |  |  |
| DUK | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| DUK | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 47 | 47 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| DUK | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| DUK | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +7.3% clears | +7.3% clears | PASS |  |  |
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
| NVDA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $155.46 / RS 0.75 | $155.46 / RS 0.75 | PASS |  |  |
| NVDA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.75 | 0.75 | PASS |  |  |
| NVDA | RS2 | Stock 52W Return and S&P 52W Return | -16.5% / +11.2% | -16.5% / +11.2% | PASS |  |  |
| NVDA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 30 | 30 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -16.5% negative | -16.5% negative | PASS |  |  |
| PLD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $125.56 / RS 0.94 | $125.56 / RS 0.94 | PASS |  |  |
| PLD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| PLD | RS2 | Stock 52W Return and S&P 52W Return | +4.8% / +11.2% | +4.8% / +11.2% | PASS |  |  |
| PLD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PLD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PLD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| PLD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.8% under | +4.8% under | PASS |  |  |
| SOXL.NE | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $12.36 / RS 1.11 | $12.36 / RS 1.11 | PASS |  |  |
| SOXL.NE | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.11 | 1.11 | PASS |  |  |
| SOXL.NE | RS2 | Stock 52W Return and S&P 52W Return | +23.6% / +11.2% | +23.6% / +11.2% | PASS |  |  |
| SOXL.NE | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| SOXL.NE | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 59 | 59 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| SOXL.NE | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market (momentum fading) | Somewhat ahead of the market (momentum fading) | PASS |  |  |
| SOXL.NE | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +23.6% clears | +23.6% clears | PASS |  |  |
| AAPL | KL-high | "The stock is near its 52-week high (within 3%)." vs the real gap to the 252-bar high | 2.5% below $360.83 | within 1% if "at"; within 3% if "near" | PASS |  |  |
| AAPL | KL-resistance | Resistance row: none in the window, and the payload has no nearest resistance zone | Resistance None within 30% above. The stock is near its 52-week high (within 3%). | no zone | PASS |  |  |
| AAPL | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No resistance within 30% above · 8 of 8 trend checks pass | No resistance within 30% above · 8 of 8 trend checks pass | PASS |  |  |
| AAPL | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $344.01 – $351.46 · 0.1% below · turned here 4× | $344.01 – $351.46 · 0.1% · 4× | PASS |  |  |
| AAPL | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 7.8729 | 7.8727 | PASS |  |  |
| AAPL | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
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
| AMD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $546.44 – $584.73 · 8.5% above · turned here 6× | $546.44 – $584.73 · 8.5% · 6× | PASS |  |  |
| AMD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| AMD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $491.12 – $530.13 · price is inside this zone · turned here 6× | $491.12 – $530.13 · 0.0% · 6× | PASS |  |  |
| AMD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 40.5705 | 40.5706 | PASS |  |  |
| AMD | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| AMD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| AMD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| AMD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $503.41 | $503.41 | PASS |  |  |
| AMD | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 503.41, zone 491.12-530.13 | inside the zone | PASS |  |  |
| AMD | TS1c | S5: the Buy on the bar = the Buy in the box | $503.41 | $503.41 | PASS |  |  |
| AMD | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 503.41 vs last close 503.41 | Buy <= last close | PASS |  |  |
| AMD | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| AMD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $422.27 -16.1% | $422.27 -16.1% | PASS |  |  |
| AMD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| AMD | TS4 | Target = nearest resistance edge and its % from the buy | $546.44 +8.5% | $546.44 +8.5% | PASS |  |  |
| AMD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| AMD | TS6 | Risk $ (and reward $ per share) | Risk $81.14 to make $43.03 a share | Risk $81.14 to make $43.03 | PASS |  |  |
| DUK | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $130.38 – $131.87 · 0.4% above · turned here 4× | $130.38 – $131.87 · 0.4% · 4× | PASS |  |  |
| DUK | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| DUK | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $129.28 · 0.4% below · turned here 1× | $129.28 · 0.4% · 1× | PASS |  |  |
| DUK | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.1475 | 2.1470 | PASS |  |  |
| DUK | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | zone_high | zone_high | PASS |  |  |
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
| ETN | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $355.76 – $373.79 · 5.5% above · turned here 7× | $355.76 – $373.79 · 5.5% · 7× | PASS |  |  |
| ETN | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| ETN | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $334.42 – $350.35 · price is inside this zone · turned here 4× | $334.42 – $350.35 · 0.0% · 4× | PASS |  |  |
| ETN | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 18.0454 | 18.0459 | PASS |  |  |
| ETN | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| ETN | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| ETN | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| ETN | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $337.11 | $337.11 | PASS |  |  |
| ETN | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 337.11, zone 334.42-350.35 | inside the zone | PASS |  |  |
| ETN | TS1c | S5: the Buy on the bar = the Buy in the box | $337.11 | $337.11 | PASS |  |  |
| ETN | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 337.11 vs last close 337.11 | Buy <= last close | PASS |  |  |
| ETN | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| ETN | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $301.02 -10.7% | $301.02 -10.7% | PASS |  |  |
| ETN | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| ETN | TS4 | Target = nearest resistance edge and its % from the buy | $355.76 +5.5% | $355.76 +5.5% | PASS |  |  |
| ETN | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| ETN | TS6 | Risk $ (and reward $ per share) | Risk $36.09 to make $18.65 a share | Risk $36.09 to make $18.65 | PASS |  |  |
| FCX | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $58.03 – $58.80 · 4.9% above · turned here 3× | $58.03 – $58.80 · 4.9% · 3× | PASS |  |  |
| FCX | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| FCX | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $55.12 – $57.84 · price is inside this zone · turned here 6× | $55.12 – $57.84 · 0.0% · 6× | PASS |  |  |
| FCX | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.8226 | 2.8222 | PASS |  |  |
| FCX | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| FCX | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 7 zones | all hold | PASS |  |  |
| FCX | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 7 zones match | match | PASS |  |  |
| FCX | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $55.30 | $55.30 | PASS |  |  |
| FCX | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 55.3, zone 55.12-57.84 | inside the zone | PASS |  |  |
| FCX | TS1c | S5: the Buy on the bar = the Buy in the box | $55.30 | $55.30 | PASS |  |  |
| FCX | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 55.3 vs last close 55.3 | Buy <= last close | PASS |  |  |
| FCX | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| FCX | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $49.65 -10.2% | $49.65 -10.2% | PASS |  |  |
| FCX | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| FCX | TS4 | Target = nearest resistance edge and its % from the buy | $58.03 +4.9% | $58.03 +4.9% | PASS |  |  |
| FCX | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| FCX | TS6 | Risk $ (and reward $ per share) | Risk $5.65 to make $2.73 a share | Risk $5.65 to make $2.73 | PASS |  |  |
| NVDA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $163.90 · 5.4% above · turned here 1× | $163.90 · 5.4% · 1× | PASS |  |  |
| NVDA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NVDA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.7101 | 9.7101 | PASS |  |  |
| NVDA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| NVDA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| NVDA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
| PLD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $131.85 – $132.60 · 5.0% above · turned here 3× | $131.85 – $132.60 · 5.0% · 3× | PASS |  |  |
| PLD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 16.5 | 3 of 8 trend checks pass · ADX 16.5 | PASS |  |  |
| PLD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $125.38 – $127.82 · price is inside this zone · turned here 6× | $125.38 – $127.82 · 0.0% · 6× | PASS |  |  |
| PLD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5068 | 2.5068 | PASS |  |  |
| PLD | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| PLD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| PLD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| PLD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $125.56 | $125.56 | PASS |  |  |
| PLD | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 125.56, zone 125.38-127.82 | inside the zone | PASS |  |  |
| PLD | TS1c | S5: the Buy on the bar = the Buy in the box | $125.56 | $125.56 | PASS |  |  |
| PLD | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 125.56 vs last close 125.56 | Buy <= last close | PASS |  |  |
| PLD | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| PLD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $120.55 -4.0% | $120.55 -4.0% | PASS |  |  |
| PLD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PLD | TS4 | Target = nearest resistance edge and its % from the buy | $131.85 +5.0% | $131.85 +5.0% | PASS |  |  |
| PLD | TS5 | reward : risk = (target - buy) / (buy - stop) | 1.3 : 1 | 1.3 : 1 | PASS |  |  |
| PLD | TS6 | Risk $ (and reward $ per share) | Risk $5.01 to make $6.29 a share | Risk $5.01 to make $6.29 | PASS |  |  |
| SOXL.NE | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $14.36 · 16.2% above · turned here 1× | $14.36 · 16.2% · 1× | PASS |  |  |
| SOXL.NE | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | Close to both support and resistance | Close to both support and resistance | PASS |  |  |
| SOXL.NE | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $12.05 – $13.46 · price is inside this zone · turned here 3× | $12.05 – $13.46 · 0.0% · 3× | PASS |  |  |
| SOXL.NE | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.0226 | 2.0229 | PASS |  |  |
| SOXL.NE | TS-basis | entryBasis in the payload = the rule re-derived from the last completed close and the nearest support zone | last_close_inside_zone | last_close_inside_zone | PASS |  |  |
| SOXL.NE | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 3 zones | all hold | PASS |  |  |
| SOXL.NE | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 3 zones match | match | PASS |  |  |
| SOXL.NE | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $12.36 | $12.36 | PASS |  |  |
| SOXL.NE | TS1b | S5: the last close is inside the nearest support zone (Support row) and the Buy is that close | buy 12.36, zone 12.05-13.46 | inside the zone | PASS |  |  |
| SOXL.NE | TS1c | S5: the Buy on the bar = the Buy in the box | $12.36 | $12.36 | PASS |  |  |
| SOXL.NE | TS1d | S3: the plan says "wait for a dip" only when the Buy is not above the last close (a Buy above the market fills at once) | buy 12.36 vs last close 12.36 | Buy <= last close | PASS |  |  |
| SOXL.NE | TS2 | "the last close, inside the support zone" = the last completed close really is inside the nearest support zone | inside wording | close inside=True | PASS |  |  |
| SOXL.NE | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $8.31 -32.7% | $8.31 -32.7% | PASS |  |  |
| SOXL.NE | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| SOXL.NE | TS4 | Target = nearest resistance edge and its % from the buy | $14.36 +16.2% | $14.36 +16.2% | PASS |  |  |
| SOXL.NE | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.5 : 1 | 0.5 : 1 | PASS |  |  |
| SOXL.NE | TS6 | Risk $ (and reward $ per share) | Risk $4.05 to make $2.00 a share | Risk $4.05 to make $2.00 | PASS |  |  |
