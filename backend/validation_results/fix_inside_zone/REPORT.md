# Statement Audit report

Run: 2026-11-18T10:14 · dumps: AAPL, AMD, META, PLD, QCOM · ET at first dump: 11/18/2026, 10:14:47 AM

Verdicts: PASS 190 · WRONG 0 (CRITICAL) · MISLEADING 0 (HIGH) · UNVERIFIED 10 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AAPL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $354.64 | $354.64 | PASS |  |  |
| AAPL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $347.14 | $347.14 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPL | E3 | percent from the 21-day average | 2.2% above | 2.2% above | PASS |  |  |
| AAPL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 10:03am ET) | session=regular | PASS |  |  |
| AAPL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.87 | $7.87 (sr=7.8729) | PASS |  | Wilder ATR14 |
| AAPL | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves above |
| AAPL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.8 | -5.8 | PASS |  |  |
| AAPL | L-ema21 | ladder row ema21: price and gap = price vs average | $347.14, 2.2% | $347.14, 2.2% | PASS |  |  |
| AAPL | L-note | "Last close $X · date" note = last completed bar | Last close $351.91 · Nov 17 | $351.91 · Nov 17 | PASS |  |  |
| AAPL | L-now | ladder price row = compared price; name = the basis label | $354.64 "Last trade 10:03am ET" | $354.64 "last trade 10:03am et" | PASS |  |  |
| AAPL | L-sma200 | ladder row sma200: price and gap = price vs average | $301.66, 17.6% | $301.66, 17.6% | PASS |  |  |
| AAPL | L-sma50 | ladder row sma50: price and gap = price vs average | $340.17, 4.3% | $340.17, 4.3% | PASS |  |  |
| AAPL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $354.64 / entry $354.64 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 56.3 | 56.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +32.0% vs +11.2% | 32.0% vs 11.2% | PASS |  |  |
| AAPL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPL | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.3 | 18.3 | PASS |  | Wilder, completed bars |
| AAPL | T4w | words "20 or more / below 20" | below 20 | ADX 18.3 | PASS |  |  |
| AAPL | T5 | "counted at the last close ($X, date)" = last completed bar | $351.91, Nov 17 | $351.91, Nov 17 | PASS |  |  |
| AAPL | T6 | price vs 200-day average (S1 pattern sma values) | $351.91 vs $301.66 · +16.7% | $351.91 vs $301.66 · 16.7% | PASS |  |  |
| AAPL | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPL | T7 | price vs 50-day average (S1 pattern sma values) | $351.91 vs $340.17 · +3.5% | $351.91 vs $340.17 · 3.5% | PASS |  |  |
| AAPL | T7w | word "Above" | Above | Above | PASS |  |  |
| AAPL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.3% over 30 td | +4.3% over 30 td | PASS |  |  |
| AAPL | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.5% below $360.83 | 2.5% below $360.83 | PASS |  | closing high would be 356.27 |
| AAPL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.5% below | PASS |  |  |
| AAPL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $360.83 | $360.8299865722656 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.25%, close location 0.39, OBV falling |
| AAPL | V2 | day change of the last completed bar | down 0.3% | -0.25% | PASS |  |  |
| AAPL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-17 | 0.83× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| AAPL | V6 | Volume detail: last session date and RVOL | 2026-11-17 0.83× | 2026-11-17 0.83× | PASS |  |  |
| AAPL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.83× / 0.11× | 0.83× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 36248936) | 20 bars, last ('2026-11-17', 36248936) | PASS |  |  |
| AMD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $513.07 | $513.07 | PASS |  |  |
| AMD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $523.46 | $523.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD | E3 | percent from the 21-day average | 2.0% below | 2.0% below | PASS |  |  |
| AMD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AMD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $40.57 | $40.57 (sr=40.5705) | PASS |  | Wilder ATR14 |
| AMD | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| AMD | L-ema21 | ladder row ema21: price and gap = price vs average | $523.46, -2.0% | $523.46, -2.0% | PASS |  |  |
| AMD | L-note | "Last close $X · date" note = last completed bar | Last close $503.41 · Nov 17 | $503.41 · Nov 17 | PASS |  |  |
| AMD | L-now | ladder price row = compared price; name = the basis label | $513.07 "Now" | $513.07 "now" | PASS |  |  |
| AMD | L-sma200 | ladder row sma200: price and gap = price vs average | $425.74, 20.5% | $425.74, 20.5% | PASS |  |  |
| AMD | L-sma50 | ladder row sma50: price and gap = price vs average | $555.04, -7.6% | $555.04, -7.6% | PASS |  |  |
| AMD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $513.07 / entry $513.07 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.6 | 46.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +109.3% vs +11.2% | 109.3% vs 11.2% | PASS |  |  |
| AMD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.4 | 18.4 | PASS |  | Wilder, completed bars |
| AMD | T4w | words "20 or more / below 20" | below 20 | ADX 18.4 | PASS |  |  |
| AMD | T5 | "counted at the last close ($X, date)" = last completed bar | $503.41, Nov 17 | $503.41, Nov 17 | PASS |  |  |
| AMD | T6 | price vs 200-day average (S1 pattern sma values) | $503.41 vs $425.74 · +18.2% | $503.41 vs $425.74 · 18.2% | PASS |  |  |
| AMD | T6w | word "Above" | Above | Above | PASS |  |  |
| AMD | T7 | price vs 50-day average (S1 pattern sma values) | $503.41 vs $555.04 · -9.3% | $503.41 vs $555.04 · -9.3% | PASS |  |  |
| AMD | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +12.3% over 30 td | +12.3% over 30 td | PASS |  |  |
| AMD | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.6% below $658.52 | 23.6% below $658.52 | PASS |  | closing high would be 649.42 |
| AMD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.6% below | PASS |  |  |
| AMD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $658.52 | $658.52001953125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.17%, close location 0.73, OBV rising |
| AMD | V2 | day change of the last completed bar | down 0.2% | -0.17% | PASS |  |  |
| AMD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AMD | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-17 | 1.27× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| AMD | V6 | Volume detail: last session date and RVOL | 2026-11-17 1.27× | 2026-11-17 1.27× | PASS |  |  |
| AMD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.27× / 0.02× | 1.27× / 0.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 34975206) | 20 bars, last ('2026-11-17', 34975206) | PASS |  |  |
| META | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $618.31 | $618.31 | PASS |  |  |
| META | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $640.17 | $640.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| META | E3 | percent from the 21-day average | 3.4% below | 3.4% below | PASS |  |  |
| META | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 10:03am ET) | session=regular | PASS |  |  |
| META | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $22.07 | $22.07 (sr=22.0699) | PASS |  | Wilder ATR14 |
| META | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| META | L-ema21 | ladder row ema21: price and gap = price vs average | $640.17, -3.4% | $640.17, -3.4% | PASS |  |  |
| META | L-note | "Last close $X · date" note = last completed bar | Last close $618.87 · Nov 17 | $618.87 · Nov 17 | PASS |  |  |
| META | L-now | ladder price row = compared price; name = the basis label | $618.31 "Last trade 10:03am ET" | $618.31 "last trade 10:03am et" | PASS |  |  |
| META | L-sma200 | ladder row sma200: price and gap = price vs average | $629.15, -1.7% | $629.15, -1.7% | PASS |  |  |
| META | L-sma50 | ladder row sma50: price and gap = price vs average | $680.02, -9.1% | $680.02, -9.1% | PASS |  |  |
| META | S5-price | S5: the same live price reads the same on the header and the Entry block | header $618.31 / entry $618.31 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| META | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| META | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.0 | 42.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| META | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.1% vs +11.2% | 3.2% vs 11.2% | PASS |  |  |
| META | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| META | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.2 | 23.2 | PASS |  | Wilder, completed bars |
| META | T4w | words "20 or more / below 20" | 20 or more | ADX 23.2 | PASS |  |  |
| META | T5 | "counted at the last close ($X, date)" = last completed bar | $618.87, Nov 17 | $618.87, Nov 17 | PASS |  |  |
| META | T6 | price vs 200-day average (S1 pattern sma values) | $618.87 vs $629.15 · -1.6% | $618.87 vs $629.15 · -1.6% | PASS |  |  |
| META | T6w | word "Below" | Below | Below | PASS |  |  |
| META | T7 | price vs 50-day average (S1 pattern sma values) | $618.87 vs $680.02 · -9.0% | $618.87 vs $680.02 · -9.0% | PASS |  |  |
| META | T7w | word "Below" | Below | Below | PASS |  |  |
| META | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.1% over 30 td | +0.1% over 30 td | PASS |  |  |
| META | T8r | word "rising" | still rising | rising | PASS |  |  |
| META | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| META | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 20.6% below $779.82 | 20.6% below $779.82 | PASS |  | closing high would be 777.59 |
| META | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 20.6% below | PASS |  |  |
| META | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $779.82 | $779.8200073242188 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| META | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.20%, close location 0.38, OBV falling |
| META | V2 | day change of the last completed bar | down 1.2% | -1.20% | PASS |  |  |
| META | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| META | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.6× from 2026-11-17 | 0.58× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| META | V6 | Volume detail: last session date and RVOL | 2026-11-17 0.58× | 2026-11-17 0.58× | PASS |  |  |
| META | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.58× / 0.34× | 0.58× / 0.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| META | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 12795966) | 20 bars, last ('2026-11-17', 12795966) | PASS |  |  |
| PLD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $125.25 | $125.25 | PASS |  |  |
| PLD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $128.51 | $128.51 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PLD | E3 | percent from the 21-day average | 2.5% below | 2.5% below | PASS |  |  |
| PLD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| PLD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.51 | $2.51 (sr=2.5068) | PASS |  | Wilder ATR14 |
| PLD | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| PLD | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| PLD | L-ema21 | ladder row ema21: price and gap = price vs average | $128.51, -2.5% | $128.51, -2.5% | PASS |  |  |
| PLD | L-note | "Last close $X · date" note = last completed bar | Last close $125.56 · Nov 17 | $125.56 · Nov 17 | PASS |  |  |
| PLD | L-now | ladder price row = compared price; name = the basis label | $125.25 "Now" | $125.25 "now" | PASS |  |  |
| PLD | L-sma200 | ladder row sma200: price and gap = price vs average | $136.34, -8.1% | $136.34, -8.1% | PASS |  |  |
| PLD | L-sma50 | ladder row sma50: price and gap = price vs average | $130.09, -3.7% | $130.09, -3.7% | PASS |  |  |
| PLD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $125.25 / entry $125.25 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PLD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PLD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.6 | 40.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PLD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.8% vs +11.2% | 4.8% vs 11.2% | PASS |  |  |
| PLD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PLD | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.5 | 16.5 | PASS |  | Wilder, completed bars |
| PLD | T4w | words "20 or more / below 20" | below 20 | ADX 16.5 | PASS |  |  |
| PLD | T5 | "counted at the last close ($X, date)" = last completed bar | $125.56, Nov 17 | $125.56, Nov 17 | PASS |  |  |
| PLD | T6 | price vs 200-day average (S1 pattern sma values) | $125.56 vs $136.34 · -7.9% | $125.56 vs $136.34 · -7.9% | PASS |  |  |
| PLD | T6w | word "Below" | Below | Below | PASS |  |  |
| PLD | T7 | price vs 50-day average (S1 pattern sma values) | $125.56 vs $130.09 · -3.5% | $125.56 vs $130.09 · -3.5% | PASS |  |  |
| PLD | T7w | word "Below" | Below | Below | PASS |  |  |
| PLD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.2% over 30 td | +0.2% over 30 td | PASS |  |  |
| PLD | T8r | word "rising" | still rising | rising | PASS |  |  |
| PLD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PLD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.5% below $152.14 | 17.5% below $152.14 | PASS |  | closing high would be 148.88 |
| PLD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.5% below | PASS |  |  |
| PLD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $152.14 | $152.14207825389113 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PLD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.60%, close location 0.23, OBV falling |
| PLD | V2 | day change of the last completed bar | down 1.6% | -1.60% | PASS |  |  |
| PLD | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.23 (raw 0.2341) | PASS |  |  |
| PLD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PLD | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-17 | 0.89× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| PLD | V6 | Volume detail: last session date and RVOL | 2026-11-17 0.89× | 2026-11-17 0.89× | PASS |  |  |
| PLD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.89× / 0.80× | 0.89× / 0.80× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PLD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3445914) | 20 bars, last ('2026-11-17', 3445914) | PASS |  |  |
| QCOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $163.34 | $163.34 | PASS |  |  |
| QCOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $172.38 | $172.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QCOM | E3 | percent from the 21-day average | 5.2% below | 5.2% below | PASS |  |  |
| QCOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| QCOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.87 | $8.87 (sr=8.866) | PASS |  | Wilder ATR14 |
| QCOM | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| QCOM | L-ema21 | ladder row ema21: price and gap = price vs average | $172.38, -5.2% | $172.38, -5.2% | PASS |  |  |
| QCOM | L-note | "Last close $X · date" note = last completed bar | Last close $166.67 · Nov 17 | $166.67 · Nov 17 | PASS |  |  |
| QCOM | L-now | ladder price row = compared price; name = the basis label | $163.34 "Now" | $163.34 "now" | PASS |  |  |
| QCOM | L-sma200 | ladder row sma200: price and gap = price vs average | $169.35, -3.6% | $169.35, -3.6% | PASS |  |  |
| QCOM | L-sma50 | ladder row sma50: price and gap = price vs average | $178.58, -8.5% | $178.58, -8.5% | PASS |  |  |
| QCOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $163.34 / entry $163.34 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QCOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QCOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.7 | 44.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QCOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.0% vs +11.2% | 2.0% vs 11.2% | PASS |  |  |
| QCOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QCOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.0 | 11.0 | PASS |  | Wilder, completed bars |
| QCOM | T4w | words "20 or more / below 20" | below 20 | ADX 11.0 | PASS |  |  |
| QCOM | T5 | "counted at the last close ($X, date)" = last completed bar | $166.67, Nov 17 | $166.67, Nov 17 | PASS |  |  |
| QCOM | T6 | price vs 200-day average (S1 pattern sma values) | $166.67 vs $169.35 · -1.6% | $166.67 vs $169.35 · -1.6% | PASS |  |  |
| QCOM | T6w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T7 | price vs 50-day average (S1 pattern sma values) | $166.67 vs $178.58 · -6.7% | $166.67 vs $178.58 · -6.7% | PASS |  |  |
| QCOM | T7w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.8% over 30 td | +0.8% over 30 td | PASS |  |  |
| QCOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QCOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QCOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.3% below $257.56 | 35.3% below $257.56 | PASS |  | closing high would be 248.74 |
| QCOM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.3% below | PASS |  |  |
| QCOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $257.56 | $257.5617517963296 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QCOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -1.10%, close location 0.51, OBV flat |
| QCOM | V2 | day change of the last completed bar | down 1.1% | -1.10% | PASS |  |  |
| QCOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| QCOM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-17 | 0.82× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| QCOM | V6 | Volume detail: last session date and RVOL | 2026-11-17 0.82× | 2026-11-17 0.82× | PASS |  |  |
| QCOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.82× / 0.21× | 0.82× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QCOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 10935821) | 20 bars, last ('2026-11-17', 10935821) | PASS |  |  |
