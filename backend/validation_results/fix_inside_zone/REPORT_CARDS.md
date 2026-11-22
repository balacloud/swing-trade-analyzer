# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)

Run: 2026-11-18T10:14 · dumps: AAPL, AMD, META, PLD, QCOM

Verdicts: PASS 191 · WRONG 0 (CRITICAL) · MISLEADING 0 (HIGH/LOW per row) · UNVERIFIED 0 (INFO)

## Coverage (honest)
| Card | statements claimed (spans) | number tokens left unclaimed |
|---|---|---|
| card-breakout | 5 | 0 |
| card-price-data | 10 | 0 |
| card-relative-strength | 20 | 0 |
| card-trade-setup | 44 | 0 |

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
| AMD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $658.52 | $658.52 | PASS |  |  |
| AMD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -23.55% | -23.55% | PASS |  |  |
| AMD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| AMD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| AMD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| AMD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $658.52 · close 23.55% below · Nov 17 close | payload values | PASS |  |  |
| AMD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| META | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $779.82 | $779.82 | PASS |  |  |
| META | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -20.64% | -20.64% | PASS |  |  |
| META | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| META | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| META | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| META | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $779.82 · close 20.64% below · Nov 17 close | payload values | PASS |  |  |
| META | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| PLD | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $142.69 | $142.69 | PASS |  |  |
| PLD | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -12% | -12.01% | PASS |  |  |
| PLD | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| PLD | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| PLD | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| PLD | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $142.69 · close 12.00% below · Nov 17 close | payload values | PASS |  |  |
| PLD | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| QCOM | BO1 | 60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection) | $205.85 | $205.85 | PASS |  |  |
| QCOM | BO2 | close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars) | -19.03% | -19.03% | PASS |  |  |
| QCOM | BO3 | breakout day = first close above the 60-day high within the last 10 bars | None | None | PASS |  |  |
| QCOM | BO4 | volume on the breakout day / mean of the 50 bars before it (that day excluded) | None | None | PASS |  |  |
| QCOM | BO5 | status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch) | NOT_READY | NOT_READY | PASS |  |  |
| QCOM | BO6 | card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format | 60-day high $205.85 · close 19.03% below · Nov 17 close | payload values | PASS |  |  |
| QCOM | BO7 | copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber | honest copy | matches breakout_detection.py b = first close above in t-9..t | PASS |  |  |
| AAPL | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AAPL | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AAPL | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AAPL | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $351.91 · Nov 17 | $351.91 · Nov 17 | PASS |  |  |
| AMD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| AMD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| AMD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| AMD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $503.41 · Nov 17 | $503.41 · Nov 17 | PASS |  |  |
| META | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Communication Services (XLC) — RS: 97.99 / Mom: +0.28 / Rank: 8/11] X | RS 97.99 Mom 0.28 Rank 8/11 | PASS |  |  |
| META | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| META | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| META | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $618.87 · Nov 17 | $618.87 · Nov 17 | PASS |  |  |
| PLD | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Real Estate (XLRE) — RS: 97.12 / Mom: +1.22 / Rank: 9/11] XLRE IMPROV | RS 97.12 Mom 1.22 Rank 9/11 | PASS |  |  |
| PLD | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | IMPROVING | IMPROVING | PASS |  |  |
| PLD | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| PLD | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $125.56 · Nov 17 | $125.56 · Nov 17 | PASS |  |  |
| QCOM | HB1 | sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11) | [Technology (XLK) — RS: 99.11 / Mom: -1.91 / Rank: 5/11] XLK LAGGING | RS 99.11 Mom -1.91 Rank 5/11 | PASS |  |  |
| QCOM | HB2 | S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0) | LAGGING | LAGGING | PASS |  |  |
| QCOM | HB3 | no earnings badge when none is upcoming | none | none | PASS |  |  |
| QCOM | HB4 | header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan) | Last close $166.67 · Nov 17 | $166.67 · Nov 17 | PASS |  |  |
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
| META | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $779.82 | $779.82 | PASS |  |  |
| META | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $618.87 | $618.87 | PASS |  |  |
| META | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $779.82 / $519.37 | $779.82 / $519.37 | PASS |  |  |
| META | PD3 | % from High | -20.6% | -20.6% | PASS |  |  |
| META | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $13.0B | bars: $13,727,393,933 | PASS | LOW |  |
| PLD | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $152.14 | $152.14 | PASS |  |  |
| PLD | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $125.56 | $125.56 | PASS |  |  |
| PLD | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $152.14 / $117.70 | $152.14 / $117.70 | PASS |  |  |
| PLD | PD3 | % from High | -17.5% | -17.5% | PASS |  |  |
| PLD | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $462M | bars: $484,416,291 | PASS | LOW |  |
| QCOM | PD-S5 | S5: Price Data 52-week high = the Technical Read's 1-year high | $257.56 | $257.56 | PASS |  |  |
| QCOM | PD1 | "Last close" = the last COMPLETED close (the header's live "Now" is separate; S5 with the header and the plan) | $166.67 | $166.67 | PASS |  |  |
| QCOM | PD2 | 52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read) | $257.56 / $120.88 | $257.56 / $120.88 | PASS |  |  |
| QCOM | PD3 | % from High | -35.3% | -35.3% | PASS |  |  |
| QCOM | PD4 | Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band) | $2.1B | bars: $2,220,263,808 | PASS | LOW |  |
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
| META | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $618.87 / RS 0.93 | $618.87 / RS 0.93 | PASS |  |  |
| META | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.93 | 0.93 | PASS |  |  |
| META | RS2 | Stock 52W Return and S&P 52W Return | +3.1% / +11.2% | +3.2% / +11.2% | PASS |  |  |
| META | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| META | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 44 | 44 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| META | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| META | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +3.1% under | +3.2% under | PASS |  |  |
| PLD | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $125.56 / RS 0.94 | $125.56 / RS 0.94 | PASS |  |  |
| PLD | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.94 | 0.94 | PASS |  |  |
| PLD | RS2 | Stock 52W Return and S&P 52W Return | +4.8% / +11.2% | +4.8% / +11.2% | PASS |  |  |
| PLD | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| PLD | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 45 | 45 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| PLD | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market | Slightly behind the market | PASS |  |  |
| PLD | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +4.8% under | +4.8% under | PASS |  |  |
| QCOM | RS-toggle | S5: the collapsed line "$price / RS x" = the cards | $166.67 / RS 0.92 | $166.67 / RS 0.92 | PASS |  |  |
| QCOM | RS1 | RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js) | 0.92 | 0.92 | PASS |  |  |
| QCOM | RS2 | Stock 52W Return and S&P 52W Return | +2.0% / +11.2% | +2.0% / +11.2% | PASS |  |  |
| QCOM | RS3w | S3: both returns cover the same period ("52 weeks") | stock 251 bars, SPY 251 bars | equal | PASS |  |  |
| QCOM | RS4 | RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99) | 43 | 43 | PASS |  | tolerance 1: the page rounds the 3-dp RS |
| QCOM | RS5 | interpretation sentence = the band of RS (+ 13-week vs 52-week trend) | Slightly behind the market (momentum accelerating) | Slightly behind the market (momentum accelerating) | PASS |  |  |
| QCOM | RS6 | absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it) | +2.0% under | +2.0% under | PASS |  |  |
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
| PLD | KL-resistance | Resistance row: zone range, % away, turned-here count (S1 meta.zones nearest resistance) | Resistance $131.85 – $132.60 · 5.0% above · turned here 3× | $131.85 – $132.60 · 5.0% · 3× | PASS |  |  |
| PLD | KL-state | one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR) | 3 of 8 trend checks pass · ADX 16.5 | 3 of 8 trend checks pass · ADX 16.5 | PASS |  |  |
| PLD | KL-support | Support row: zone range, % away, turned-here count (S1 meta.zones nearest support) | Support $125.38 – $127.82 · price is inside this zone · turned here 6× | $125.38 – $127.82 · 0.0% · 6× | PASS |  |  |
| PLD | TS-atr | ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly) | 2.5068 | 2.5068 | PASS |  |  |
| PLD | TS-inv | structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone) | 11 zones | all hold | PASS |  |  |
| PLD | TS-ref | zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using payload ATR) | 11 zones match | match | PASS |  |  |
| PLD | TS1 | Buy = the nearest support edge (S1 /api/sr support, max) | $127.82 | $127.82 | PASS |  |  |
| PLD | TS1b | S5: the Buy equals the edge of the zone flagged nearest (Support row) | buy 127.82, nearest zone high 127.82 | equal | PASS |  |  |
| PLD | TS1c | S5: the Buy on the bar = the Buy in the box | $127.82 | $127.82 | PASS |  |  |
| PLD | TS2 | "price is inside it" = a nearest support zone with insideZone | inside wording | insideZone=True | PASS |  |  |
| PLD | TS3 | Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy | $122.81 -3.9% | $122.81 -3.9% | PASS |  |  |
| PLD | TS3w | words "2 ATR below" vs "floored" | 2 ATR below | 2 ATR below | PASS |  |  |
| PLD | TS4 | Target = nearest resistance edge and its % from the buy | $131.85 +3.2% | $131.85 +3.2% | PASS |  |  |
| PLD | TS5 | reward : risk = (target - buy) / (buy - stop) | 0.8 : 1 | 0.8 : 1 | PASS |  |  |
| PLD | TS6 | Risk $ (and reward $ per share) | Risk $5.01 to make $4.03 a share | Risk $5.01 to make $4.03 | PASS |  |  |
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
