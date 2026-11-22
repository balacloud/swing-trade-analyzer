# Statement Audit phase 3a report (Market backdrop, Fundamentals, Mean-Reversion Read)

Run: 2026-11-18T10:28 · dumps: AAPL, AMD, DUK, ETN, FCX, NVDA, PLD, SOXL.NE

Verdicts: PASS 272 · WRONG 0 (CRITICAL) · MISLEADING 0 (per-row severity) · UNVERIFIED 12 (INFO)

Recomputed from bars: MR RSI(2), % above the 200-day, dollar volume, the four rule marks, the blocker sentence; S&P 500 200/50-day and the 10-session drop (the app's own 260 bars); QQQ and "largest since" from an independent Yahoo history (S4).
Provider fields (sales growth, ROE, debt/equity) are arithmetic and flag logic only: no recompute is possible (UNVERIFIED as to truth). NOT YET COVERED: the Data Sources tab (phase 3b), other tabs; branches these tickers do not reach (signal true, VIX band edges, no-down-day, unavailable backdrop, negative equity) are exercised by planted tests only.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AMD | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| DUK | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| FCX | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| PLD | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AAPL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| DUK | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| ETN | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| FCX | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NVDA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PLD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| SOXL.NE | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AAPL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.7% | +11.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AAPL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 127.6% | 127.6% flag=False | PASS |  |  |
| AAPL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| AAPL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AAPL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| AAPL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-02 (16 days ago); no upcoming date listed. | 2026-11-02 days_until=-16 | PASS |  |  |
| AMD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 11.6% | 11.6% flag=False | PASS |  |  |
| AMD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.10 | 0.10 flag=False | PASS |  |  |
| AMD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AMD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| AMD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (15 days ago); no upcoming date listed. | 2026-11-03 days_until=-15 | PASS |  |  |
| DUK | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 10.0% | 10.0% flag=False | PASS |  |  |
| DUK | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.68 | 1.68 flag=False | PASS |  |  |
| DUK | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| DUK | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| DUK | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-05 (13 days ago); no upcoming date listed. | 2026-11-05 days_until=-13 | PASS |  |  |
| ETN | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +28.0% | +28.0% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| ETN | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 19.5% | 19.5% flag=False | PASS |  |  |
| ETN | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 1.00 | 1.00 flag=False | PASS |  |  |
| ETN | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| ETN | FU6 | S1: the providers named on the card = the per-field sources in the payload | yfinance (sales, ROE, debt) | yfinance | PASS |  |  |
| ETN | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-03 (15 days ago); no upcoming date listed. | 2026-11-03 days_until=-15 | PASS |  |  |
| FCX | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 15.3% | 15.3% flag=False | PASS |  |  |
| FCX | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.49 | 0.49 flag=False | PASS |  |  |
| FCX | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| FCX | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| FCX | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-27 (22 days ago); no upcoming date listed. | 2026-10-27 days_until=-22 | PASS |  |  |
| NVDA | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +105.8% | +105.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NVDA | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 110.1% | 110.1% flag=False | PASS |  |  |
| NVDA | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| NVDA | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NVDA | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NVDA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-17 (1 day ago); no upcoming date listed. | 2026-11-17 days_until=-1 | PASS |  |  |
| PLD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 7.9% | 7.9% flag=False | PASS |  |  |
| PLD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.66 | 0.66 flag=False | PASS |  |  |
| PLD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PLD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| PLD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (34 days ago); no upcoming date listed. | 2026-10-15 days_until=-34 | PASS |  |  |
| SOXL.NE | FU1 | ETF (quoteType) -> "Not applicable" and no check tiles | Not applicable | Not applicable | PASS |  |  |
| SOXL.NE | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | No earnings date found in the feed. | None days_until=None | PASS |  |  |
| AAPL | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +16.7% | TR +16.7% | PASS | LOW | the two cards divide by different roundings of the average |
| AAPL | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AAPL | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AAPL | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AAPL | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AAPL | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 16,628,022,962 | 16,628,048,373 | PASS |  |  |
| AAPL | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AAPL | MR-price | price = the last completed close | 351.91 | 351.91 | PASS |  |  |
| AAPL | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $351.91 needs above $10 | $351.91 needs above $10 | PASS |  |  |
| AAPL | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 25.6 needs under 10 | 25.55 needs under 10 -> ✗ | PASS |  |  |
| AAPL | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 16.7% above its 200-day average | 16.7% above | PASS |  |  |
| AAPL | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $16.6B traded on an average day needs above $25M | $16,628,022,962 needs above $25,000,000 | PASS |  |  |
| AAPL | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 25.55 | 25.55 | PASS |  |  |
| AAPL | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 16.66% | 16.66% | PASS |  |  |
| AAPL | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AMD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +18.2% | TR +18.2% | PASS | LOW | the two cards divide by different roundings of the average |
| AMD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| AMD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| AMD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| AMD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| AMD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 18,509,288,047 | 18,509,288,086 | PASS |  |  |
| AMD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| AMD | MR-price | price = the last completed close | 503.41 | 503.41 | PASS |  |  |
| AMD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $503.41 needs above $10 | $503.41 needs above $10 | PASS |  |  |
| AMD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 21.5 needs under 10 | 21.49 needs under 10 -> ✗ | PASS |  |  |
| AMD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 18.2% above its 200-day average | 18.2% above | PASS |  |  |
| AMD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $18.5B traded on an average day needs above $25M | $18,509,288,047 needs above $25,000,000 | PASS |  |  |
| AMD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 21.49 | 21.49 | PASS |  |  |
| AMD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 18.24% | 18.24% | PASS |  |  |
| AMD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| DUK | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR +5.8% | TR +5.8% | PASS | LOW | the two cards divide by different roundings of the average |
| DUK | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| DUK | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher | the 2-day RSI is 10 or higher | PASS |  |  |
| DUK | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| DUK | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| DUK | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 612,423,376 | 612,423,814 | PASS |  |  |
| DUK | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| DUK | MR-price | price = the last completed close | 129.84 | 129.84 | PASS |  |  |
| DUK | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $129.84 needs above $10 | $129.84 needs above $10 | PASS |  |  |
| DUK | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 59.3 needs under 10 | 59.29 needs under 10 -> ✗ | PASS |  |  |
| DUK | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✓ 5.8% above its 200-day average | 5.8% above | PASS |  |  |
| DUK | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $612.4M traded on an average day needs above $25M | $612,423,376 needs above $25,000,000 | PASS |  |  |
| DUK | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 59.29 | 59.30 | PASS |  |  |
| DUK | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | 5.79% | 5.79% | PASS |  |  |
| DUK | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| ETN | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.7% | TR -14.7% | PASS | LOW | the two cards divide by different roundings of the average |
| ETN | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| ETN | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| ETN | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| ETN | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| ETN | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,160,203,086 | 1,160,202,187 | PASS |  |  |
| ETN | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| ETN | MR-price | price = the last completed close | 337.11 | 337.11 | PASS |  |  |
| ETN | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $337.11 needs above $10 | $337.11 needs above $10 | PASS |  |  |
| ETN | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.4 needs under 10 | 9.4 needs under 10 -> ✓ | PASS |  |  |
| ETN | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.7% below its 200-day average | 14.7% below | PASS |  |  |
| ETN | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $1.2B traded on an average day needs above $25M | $1,160,203,086 needs above $25,000,000 | PASS |  |  |
| ETN | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.4 | 9.40 | PASS |  |  |
| ETN | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.73% | -14.73% | PASS |  |  |
| ETN | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| FCX | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -14.8% | TR -14.8% | PASS | LOW | the two cards divide by different roundings of the average |
| FCX | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| FCX | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| FCX | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| FCX | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| FCX | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 789,799,320 | 789,799,321 | PASS |  |  |
| FCX | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| FCX | MR-price | price = the last completed close | 55.3 | 55.3 | PASS |  |  |
| FCX | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $55.30 needs above $10 | $55.30 needs above $10 | PASS |  |  |
| FCX | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.7 needs under 10 | 9.73 needs under 10 -> ✓ | PASS |  |  |
| FCX | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 14.8% below its 200-day average | 14.8% below | PASS |  |  |
| FCX | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $789.8M traded on an average day needs above $25M | $789,799,320 needs above $25,000,000 | PASS |  |  |
| FCX | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.73 | 9.73 | PASS |  |  |
| FCX | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -14.8% | -14.80% | PASS |  |  |
| FCX | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| NVDA | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -23.6% | TR -23.6% | PASS | LOW | the two cards divide by different roundings of the average |
| NVDA | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| NVDA | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| NVDA | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| NVDA | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| NVDA | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 42,088,882,301 | 42,088,881,875 | PASS |  |  |
| NVDA | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| NVDA | MR-price | price = the last completed close | 155.46 | 155.46 | PASS |  |  |
| NVDA | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $155.46 needs above $10 | $155.46 needs above $10 | PASS |  |  |
| NVDA | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 5.2 needs under 10 | 5.19 needs under 10 -> ✓ | PASS |  |  |
| NVDA | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 23.6% below its 200-day average | 23.6% below | PASS |  |  |
| NVDA | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $42.1B traded on an average day needs above $25M | $42,088,882,301 needs above $25,000,000 | PASS |  |  |
| NVDA | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 5.19 | 5.19 | PASS |  |  |
| NVDA | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -23.64% | -23.64% | PASS |  |  |
| NVDA | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| PLD | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -7.9% | TR -7.9% | PASS | LOW | the two cards divide by different roundings of the average |
| PLD | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| PLD | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| PLD | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| PLD | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| PLD | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 463,810,951 | 463,810,949 | PASS |  |  |
| PLD | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| PLD | MR-price | price = the last completed close | 125.56 | 125.56 | PASS |  |  |
| PLD | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $125.56 needs above $10 | $125.56 needs above $10 | PASS |  |  |
| PLD | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 3.2 needs under 10 | 3.17 needs under 10 -> ✓ | PASS |  |  |
| PLD | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 7.9% below its 200-day average | 7.9% below | PASS |  |  |
| PLD | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $463.8M traded on an average day needs above $25M | $463,810,951 needs above $25,000,000 | PASS |  |  |
| PLD | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 3.17 | 3.17 | PASS |  |  |
| PLD | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -7.91% | -7.91% | PASS |  |  |
| PLD | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| SOXL.NE | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -60.0% | TR -60.0% | PASS | LOW | the two cards divide by different roundings of the average |
| SOXL.NE | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| SOXL.NE | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | the 2-day RSI is 10 or higher; it is below its 200-day average; it does not trade enough dollars a day | PASS |  |  |
| SOXL.NE | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| SOXL.NE | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| SOXL.NE | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 1,697,226 | 1,697,226 | PASS |  |  |
| SOXL.NE | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| SOXL.NE | MR-price | price = the last completed close | 12.36 | 12.36 | PASS |  |  |
| SOXL.NE | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $12.36 needs above $10 | $12.36 needs above $10 | PASS |  |  |
| SOXL.NE | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 13.8 needs under 10 | 13.82 needs under 10 -> ✗ | PASS |  |  |
| SOXL.NE | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 60.0% below its 200-day average | 60.0% below | PASS |  |  |
| SOXL.NE | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✗ $1.7M traded on an average day needs above $25M | $1,697,226 needs above $25,000,000 | PASS |  |  |
| SOXL.NE | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 13.82 | 13.69 | PASS |  |  |
| SOXL.NE | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -59.96% | -59.96% | PASS |  |  |
| SOXL.NE | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
| AAPL | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AAPL | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AAPL | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AAPL | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AAPL | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AAPL | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AAPL | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AAPL | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AAPL | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AAPL | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AAPL | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AAPL | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| AMD | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| AMD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| AMD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| AMD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| AMD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| AMD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| AMD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| AMD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| AMD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| AMD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| AMD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| AMD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| DUK | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| DUK | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| DUK | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| DUK | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| DUK | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| DUK | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| DUK | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| DUK | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| DUK | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| DUK | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| DUK | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| DUK | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| ETN | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| ETN | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| ETN | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| ETN | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| ETN | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| ETN | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| ETN | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| ETN | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| ETN | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| ETN | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| ETN | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| ETN | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| FCX | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| FCX | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| FCX | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| FCX | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| FCX | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| FCX | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| FCX | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| FCX | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| FCX | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| FCX | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| FCX | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| FCX | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| NVDA | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| NVDA | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| NVDA | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| NVDA | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| NVDA | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| NVDA | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| NVDA | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| NVDA | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| NVDA | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| NVDA | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| NVDA | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| NVDA | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| PLD | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| PLD | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| PLD | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| PLD | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| PLD | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| PLD | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| PLD | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| PLD | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| PLD | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| PLD | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| PLD | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| PLD | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
| SOXL.NE | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| SOXL.NE | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| SOXL.NE | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| SOXL.NE | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| SOXL.NE | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| SOXL.NE | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| SOXL.NE | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| SOXL.NE | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| SOXL.NE | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| SOXL.NE | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| SOXL.NE | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| SOXL.NE | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
