# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-18T10:01 · dumps: AAPL, NVDA

Verdicts: PASS 69 · WRONG 0 (CRITICAL) · MISLEADING 0 (HIGH/LOW per row) · UNVERIFIED 0 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 2 | 0 |
| card-price-data | 4 | 0 |
| card-relative-strength | 8 | 0 |
| card-trade-setup | 11 | 0 |

Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).
Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).
NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AAPL | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $351.46 | $351.46 | PASS |  |  |
| AAPL | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | 0.13% | 0.13% | PASS |  |  |
| AAPL | BO3 | breakout day = first close above the 60-day high within the last 10 bars | 2026-11-11 | 2026-11-11 | PASS |  |  |
| AAPL | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | 0.79 | 0.79 | PASS |  |  |
| AAPL | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | RETEST_ENTRY | RETEST_ENTRY | PASS |  |  |
| AAPL | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $351.46 · close 0.13% above · broke out Nov 11 on 0.79× its prior 50-day average volume · Nov 17 close | payload values | PASS |  |  |
| AAPL | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | BO8 | the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded) | named window | prior 50 bars | PASS |  |  |
| NVDA | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $243.37 | $243.37 | PASS |  |  |
| NVDA | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -36.12% | -36.12% | PASS |  |  |
| NVDA | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| NVDA | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| NVDA | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| NVDA | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $243.37 · close 36.12% below · Nov 17 close | payload values | PASS |  |  |
| NVDA | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $351.91 · Nov 17 | $351.91 · Nov 17 | PASS |  |  |
| NVDA | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| NVDA | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| NVDA | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| NVDA | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $155.46 · Nov 17 | $155.46 · Nov 17 | PASS |  |  |
| AAPL | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $360.83 | $360.83 | PASS |  |  |
| AAPL | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $351.91 | $351.91 | PASS |  |  |
| AAPL | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $360.83 / $242.57 | $360.83 / $242.57 | PASS |  |  |
| AAPL | PD3 | % from High | -2.5% | -2.5% | PASS |  |  |
| AAPL | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $15.0B | bars: $15,393,891,469 | PASS | LOW |  |
| NVDA | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $243.37 | $243.37 | PASS |  |  |
| NVDA | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $155.46 | $155.46 | PASS |  |  |
| NVDA | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $243.37 / $148.80 | $243.37 / $148.80 | PASS |  |  |
| NVDA | PD3 | % from High | -36.1% | -36.1% | PASS |  |  |
| NVDA | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $24.0B | bars: $24,430,752,602 | PASS | LOW |  |
| AAPL | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $351.91 / RS 1.19 | $351.91 / RS 1.19 | PASS |  |  |
| AAPL | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 1.19 | 1.19 | PASS |  |  |
| AAPL | RS2 | Stock 52W Return and S&P 52W Return | +32.0% / +11.2% | +32.0% / +11.2% | PASS |  |  |
| AAPL | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| AAPL | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 65 | 65 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| AAPL | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Somewhat ahead of the market | Somewhat ahead of the market | PASS |  |  |
| AAPL | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +32.0% clears | +32.0% clears | PASS |  |  |
| NVDA | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $155.46 / RS 0.75 | $155.46 / RS 0.75 | PASS |  |  |
| NVDA | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.75 | 0.75 | PASS |  |  |
| NVDA | RS2 | Stock 52W Return and S&P 52W Return | -16.5% / +11.2% | -16.5% / +11.2% | PASS |  |  |
| NVDA | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| NVDA | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 30 | 30 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| NVDA | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Well behind the market | Well behind the market | PASS |  |  |
| NVDA | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | -16.5% negative | -16.5% negative | PASS |  |  |
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
| NVDA | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $163.90 · 5.4% above · turned here 1× | $163.90 · 5.4% · 1× | PASS |  |  |
| NVDA | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | No support within 20% below | No support within 20% below | PASS |  |  |
| NVDA | KL-support | Support row: none in the window, and the payload has no nearest support zone | Support None within 20% below. | no zone | PASS |  |  |
| NVDA | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 9.7101 | 9.7101 | PASS |  |  |
| NVDA | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 4 zones | all hold | PASS |  |  |
| NVDA | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 4 zones match | match | PASS |  |  |
| NVDA | TS1 | no support level: the card says there is no plan | says so | says so | PASS |  |  |
