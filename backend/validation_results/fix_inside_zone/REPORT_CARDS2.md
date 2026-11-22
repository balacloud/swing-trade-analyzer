# Statement Audit phase 3a report (Market backdrop, Fundamentals, Mean-Reversion Read)

Run: 2026-11-18T10:14 · dumps: AAPL, AMD, META, PLD, QCOM

Verdicts: PASS 172 · WRONG 0 (CRITICAL) · MISLEADING 0 (per-row severity) · UNVERIFIED 8 (INFO)

Recomputed from bars: MR RSI(2), % above the 200-day, dollar volume, the four rule marks, the blocker sentence; S&P 500 200/50-day and the 10-session drop (the app's own 260 bars); QQQ and "largest since" from an independent Yahoo history (S4).
Provider fields (sales growth, ROE, debt/equity) are arithmetic and flag logic only: no recompute is possible (UNVERIFIED as to truth). NOT YET COVERED: the Data Sources tab (phase 3b), other tabs; branches these tickers do not reach (signal true, VIX band edges, no-down-day, unavailable backdrop, negative equity) are exercised by planted tests only.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AMD | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| PLD | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| QCOM | U-FU | numbers on the card no statement claimed (exhaustive scan) | 2 | each one claimed or exempt | UNVERIFIED | INFO | 1 unclaimed number token(s) |
| AAPL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AMD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| META | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| PLD | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| QCOM | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
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
| META | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +26.1% | +26.1% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| META | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 30.3% | 30.3% flag=False | PASS |  |  |
| META | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.30 | 0.30 flag=False | PASS |  |  |
| META | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| META | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| META | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-21 (28 days ago); no upcoming date listed. | 2026-10-21 days_until=-28 | PASS |  |  |
| PLD | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 7.9% | 7.9% flag=False | PASS |  |  |
| PLD | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.66 | 0.66 flag=False | PASS |  |  |
| PLD | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| PLD | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| PLD | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-10-15 (34 days ago); no upcoming date listed. | 2026-10-15 days_until=-34 | PASS |  |  |
| QCOM | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 50.3% | 50.3% flag=False | PASS |  |  |
| QCOM | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.50 | 0.50 flag=False | PASS |  |  |
| QCOM | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| QCOM | FU6 | S1: the providers named on the card = the per-field sources in the payload | Finnhub (ROE, debt) | Finnhub | PASS |  |  |
| QCOM | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-04 (14 days ago); no upcoming date listed. | 2026-11-04 days_until=-14 | PASS |  |  |
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
| META | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.6% | TR -1.6% | PASS | LOW | the two cards divide by different roundings of the average |
| META | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| META | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | the 2-day RSI is 10 or higher; it is below its 200-day average | the 2-day RSI is 10 or higher; it is below its 200-day average | PASS |  |  |
| META | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| META | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| META | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| META | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 14,685,062,637 | 14,685,062,619 | PASS |  |  |
| META | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| META | MR-price | price = the last completed close | 618.87 | 618.87 | PASS |  |  |
| META | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $618.87 needs above $10 | $618.87 needs above $10 | PASS |  |  |
| META | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✗ 2-day RSI 23.3 needs under 10 | 23.31 needs under 10 -> ✗ | PASS |  |  |
| META | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.6% below its 200-day average | 1.6% below | PASS |  |  |
| META | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $14.7B traded on an average day needs above $25M | $14,685,062,637 needs above $25,000,000 | PASS |  |  |
| META | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 23.31 | 23.31 | PASS |  |  |
| META | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.63% | -1.63% | PASS |  |  |
| META | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
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
| QCOM | MR-S5 | S5: MR "% above/below its 200-day average" = the Technical Read's 200-day row (same claim, same number) | MR -1.6% | TR -1.6% | PASS | LOW | the two cards divide by different roundings of the average |
| QCOM | MR-asof | "Checked on the <date> close" = the last completed bar | 2026-11-17 | 2026-11-17 | PASS |  |  |
| QCOM | MR-block | "Blocked by:" lists exactly the failing rules (words checked against the numbers) | it is below its 200-day average | it is below its 200-day average | PASS |  |  |
| QCOM | MR-cond-above_200sma | rule "above_200sma" pass/fail from the recomputed numbers (thresholds from the payload rules) | False | False | PASS |  |  |
| QCOM | MR-cond-price_filter | rule "price_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-cond-rsi2_oversold | rule "rsi2_oversold" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-cond-volume_filter | rule "volume_filter" pass/fail from the recomputed numbers (thresholds from the payload rules) | True | True | PASS |  |  |
| QCOM | MR-dv | average dollar volume = 20-bar mean of close x volume (completed bars) | 2,384,350,444 | 2,384,350,433 | PASS |  |  |
| QCOM | MR-head | headline = all four rules must pass | No signal (payload signal=False) | all pass = False | PASS |  |  |
| QCOM | MR-price | price = the last completed close | 166.67 | 166.67 | PASS |  |  |
| QCOM | MR-row-price | Price row: price and the $10 cutoff and its mark | ✓ $166.67 needs above $10 | $166.67 needs above $10 | PASS |  |  |
| QCOM | MR-row-rsi | RSI row: 2-day RSI (1 dp) vs the cutoff and its mark | ✓ 2-day RSI 9.1 needs under 10 | 9.12 needs under 10 -> ✓ | PASS |  |  |
| QCOM | MR-row-sma | Uptrend row: % and side of the 200-day average and its mark | ✗ 1.6% below its 200-day average | 1.6% below | PASS |  |  |
| QCOM | MR-row-volume | Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark | ✓ $2.4B traded on an average day needs above $25M | $2,384,350,444 needs above $25,000,000 | PASS |  |  |
| QCOM | MR-rsi | RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars) | 9.12 | 9.12 | PASS |  |  |
| QCOM | MR-sma | % above the 200-day average = (close / 200-day SMA - 1) | -1.58% | -1.58% | PASS |  |  |
| QCOM | MR-words | S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight) | weighted mostly to the last 2 days | ewm(alpha 1/2) over the whole history | PASS |  |  |
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
| META | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| META | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| META | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| META | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| META | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| META | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| META | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| META | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| META | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| META | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| META | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| META | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
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
| QCOM | MB-QQQ-back | S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse | Nov 19, 2024 | 2024-11-19 | PASS |  | the app's frame starts at searchedFrom; a longer history may hold a larger drop (INFO) |
| QCOM | MB-QQQ-drop | Nasdaq-100 (QQQ): biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | -6.5% on Nov 5 | -6.49% on Nov 5 | PASS |  |  |
| QCOM | MB-QQQ-long | Nasdaq-100 (QQQ) 200-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -3.6% | ↓ below -3.6% | PASS |  |  |
| QCOM | MB-QQQ-short | Nasdaq-100 (QQQ) 50-day: arrow, word and % from the average (independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)) | ↓ below -8.2% | ↓ below -8.2% | PASS |  |  |
| QCOM | MB-S3 | S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW) | last 10 sessions | DROP_WINDOW = 10 | PASS |  |  |
| QCOM | MB-SPY-drop | S&P 500: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date (the app's own 260 bars) | -4.4% on Nov 5 | -4.41% on Nov 5 | PASS |  |  |
| QCOM | MB-SPY-long | S&P 500 200-day: arrow, word and % from the average (the app's own 260 bars) | ↑ above +0.4% | ↑ above +0.4% | PASS |  |  |
| QCOM | MB-SPY-short | S&P 500 50-day: arrow, word and % from the average (the app's own 260 bars) | ↓ below -4.0% | ↓ below -4.0% | PASS |  |  |
| QCOM | MB-SPY-since | S4: "largest since <date>" = the last earlier day at least as bad (independent history) | Apr 4, 2025 | 2025-04-04 | PASS |  |  |
| QCOM | MB-asof | "Index figures as of <date> close" = the last completed index bar | Index figures as of Nov 17 close | Nov 17 | PASS |  |  |
| QCOM | MB-vix | VIX value (1 decimal) from the /api/market/vix payload | 25.8 | 25.8 | PASS |  | same-dump comparison only: VIX moves between dumps |
| QCOM | MB-vixband | S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp) | high | high | PASS |  |  |
