# Statement Audit phase 3a report (Market backdrop, Fundamentals, Mean-Reversion Read)

Run: 2026-11-18T10:01 · dumps: AAPL, NVDA

Verdicts: PASS 70 · WRONG 0 (CRITICAL) · MISLEADING 0 (per-row severity) · UNVERIFIED 2 (INFO)

Recomputed from bars: MR RSI(2), % above the 200-day, dollar volume, the four rule marks, the blocker sentence; S&P 500 200/50-day and the 10-session drop (the app's own 260 bars); QQQ and "largest since" from an independent Yahoo history (S4).
Provider fields (sales growth, ROE, debt/equity) are arithmetic and flag logic only: no recompute is possible (UNVERIFIED as to truth). NOT YET COVERED: the Data Sources tab (phase 3b), other tabs; branches these tickers do not reach (signal true, VIX band edges, no-down-day, unavailable backdrop, negative equity) are exercised by planted tests only.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AAPL | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| NVDA | MB-vixts | S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked | (latest quote) | a quote time | UNVERIFIED | INFO | the /api/market/vix payload carries no quote time |
| AAPL | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +11.7% | +11.7% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| AAPL | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 127.6% | 127.6% flag=False | PASS |  |  |
| AAPL | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.71 | 0.71 flag=False | PASS |  |  |
| AAPL | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| AAPL | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| AAPL | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-02 (16 days ago); no upcoming date listed. | 2026-11-02 days_until=-16 | PASS |  |  |
| NVDA | FU2 | Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field) | ✓ Sales +105.8% | +105.8% flag=False | PASS |  | a provider field: recompute is not possible (S4 below) |
| NVDA | FU3 | ROE: value (1 dp) and the flag at < 0% | ✓ Return on equity ROE 110.1% | 110.1% flag=False | PASS |  |  |
| NVDA | FU4 | Debt/equity: value (2 dp) and the flag at > 2.0 | ✓ Debt D/E 0.15 | 0.15 flag=False | PASS |  |  |
| NVDA | FU5 | headline = the number of tripped flags | No red flags | 0 flag(s) | PASS |  |  |
| NVDA | FU6 | S1: the providers named on the card = the per-field sources in the payload | Alpha Vantage (sales) · Finnhub (ROE, debt) | Alpha Vantage, Finnhub | PASS |  |  |
| NVDA | FU8 | earnings row: date and calendar days (S5 with the header badge / /api/earnings) | Last date in the feed: 2026-11-17 (1 day ago); no upcoming date listed. | 2026-11-17 days_until=-1 | PASS |  |  |
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
