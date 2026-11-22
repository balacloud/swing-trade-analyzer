# Statement Audit report

Run: 2026-11-18T10:01 · dumps: AAPL, NVDA · ET at first dump: 11/18/2026, 10:01:48 AM

Verdicts: PASS 81 · WRONG 0 (CRITICAL) · MISLEADING 0 (HIGH) · UNVERIFIED 4 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AAPL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $355.57 | $355.57 | PASS |  |  |
| AAPL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $347.14 | $347.14 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPL | E3 | percent from the 21-day average | 2.4% above | 2.4% above | PASS |  |  |
| AAPL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AAPL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.87 | $7.87 (sr=7.8729) | PASS |  | Wilder ATR14 |
| AAPL | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves above |
| AAPL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.8 | -5.8 | PASS |  |  |
| AAPL | L-ema21 | ladder row ema21: price and gap = price vs average | $347.14, 2.4% | $347.14, 2.4% | PASS |  |  |
| AAPL | L-note | "Last close $X · date" note = last completed bar | Last close $351.91 · Nov 17 | $351.91 · Nov 17 | PASS |  |  |
| AAPL | L-now | ladder price row = compared price; name = the basis label | $355.57 "Now" | $355.57 "now" | PASS |  |  |
| AAPL | L-sma200 | ladder row sma200: price and gap = price vs average | $301.66, 17.9% | $301.66, 17.9% | PASS |  |  |
| AAPL | L-sma50 | ladder row sma50: price and gap = price vs average | $340.17, 4.5% | $340.17, 4.5% | PASS |  |  |
| AAPL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $355.57 / entry $355.57 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| NVDA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $154.40 | $154.40 | PASS |  |  |
| NVDA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $187.5 | $187.50 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDA | E3 | percent from the 21-day average | 17.7% below | 17.7% below | PASS |  |  |
| NVDA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NVDA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.71 | $9.71 (sr=9.7101) | PASS |  | Wilder ATR14 |
| NVDA | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| NVDA | L-ema21 | ladder row ema21: price and gap = price vs average | $187.5, -17.7% | $187.50, -17.7% | PASS |  |  |
| NVDA | L-note | "Last close $X · date" note = last completed bar | Last close $155.46 · Nov 17 | $155.46 · Nov 17 | PASS |  |  |
| NVDA | L-now | ladder price row = compared price; name = the basis label | $154.4 "Now" | $154.40 "now" | PASS |  |  |
| NVDA | L-sma200 | ladder row sma200: price and gap = price vs average | $203.6, -24.2% | $203.60, -24.2% | PASS |  |  |
| NVDA | L-sma50 | ladder row sma50: price and gap = price vs average | $211.75, -27.1% | $211.75, -27.1% | PASS |  |  |
| NVDA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $154.40 / entry $154.40 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.5 | 22.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -16.5% vs +11.2% | -16.5% vs 11.2% | PASS |  |  |
| NVDA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDA | T4 | ADX 14 (S1 /api/sr meta.adx) | 45.4 | 45.4 | PASS |  | Wilder, completed bars |
| NVDA | T4w | words "20 or more / below 20" | 20 or more | ADX 45.4 | PASS |  |  |
| NVDA | T5 | "counted at the last close ($X, date)" = last completed bar | $155.46, Nov 17 | $155.46, Nov 17 | PASS |  |  |
| NVDA | T6 | price vs 200-day average (S1 pattern sma values) | $155.46 vs $203.60 · -23.6% | $155.46 vs $203.60 · -23.6% | PASS |  |  |
| NVDA | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDA | T7 | price vs 50-day average (S1 pattern sma values) | $155.46 vs $211.75 · -26.6% | $155.46 vs $211.75 · -26.6% | PASS |  |  |
| NVDA | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| NVDA | T8r | word "rising" | still rising | rising | PASS |  |  |
| NVDA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.1% below $243.37 | 36.1% below $243.37 | PASS |  | closing high would be 239.24 |
| NVDA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.1% below | PASS |  |  |
| NVDA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $243.37 | $243.3699951171875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.44%, close location 0.65, OBV falling |
| NVDA | V2 | day change of the last completed bar | down 0.4% | -0.44% | PASS |  |  |
| NVDA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDA | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 2.4× from 2026-11-17 | 2.35× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| NVDA | V6 | Volume detail: last session date and RVOL | 2026-11-17 2.35× | 2026-11-17 2.35× | PASS |  |  |
| NVDA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.35× / 0.07× | 2.35× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 370067900) | 20 bars, last ('2026-11-17', 370067900) | PASS |  |  |
| NVDA | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.35, OBV falling | condition true | PASS |  |  |
