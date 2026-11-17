# Statement Audit report

Run: 2026-11-17T14:39 · dumps: AAPL, F, NVDA, RIVN, SMCI, SMH, SOXL.NE · ET at first dump: 11/17/2026, 2:37:43 PM

Verdicts: PASS 264 · WRONG 0 (CRITICAL) · MISLEADING 3 (HIGH) · UNVERIFIED 12 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| F | T4w | words "20 or more / below 20" | 20 or more | ADX 20.0 | MISLEADING | LOW | display rounding at the 20 line: ADX is 19.97, the backend rounds it to 1 decimal before the card compares it |
| SMCI | L-note | "Last close $X · date" note = last completed bar | Last close $25.02 · Nov 16 | $25.03 · Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close |
| SMCI | T5 | "counted at the last close ($X, date)" = last completed bar | $25.02, Nov 16 | $25.03, Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close (e.g. Twelve Data 25.025 vs Yahoo 25.03); the header/quote path and the price bars can read different providers |
| AAPL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| F | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| F | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RIVN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RIVN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMCI | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMCI | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $350.51 | $350.51 | PASS |  |  |
| AAPL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $346.86 | $346.86 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPL | E3 | percent from the 21-day average | 1.1% above | 1.1% above | PASS |  |  |
| AAPL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AAPL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.05 | $8.05 (sr=8.0462) | PASS |  | Wilder ATR14 |
| AAPL | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| AAPL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.6 | -5.6 | PASS |  |  |
| AAPL | L-ema21 | ladder row ema21: price and gap = price vs average | $346.86, 1.1% | $346.86, 1.1% | PASS |  |  |
| AAPL | L-note | "Last close $X · date" note = last completed bar | Last close $352.78 · Nov 16 | $352.78 · Nov 16 | PASS |  |  |
| AAPL | L-now | ladder price row = compared price; name = the basis label | $350.51 "Now" | $350.51 "now" | PASS |  |  |
| AAPL | L-sma200 | ladder row sma200: price and gap = price vs average | $301.72, 16.2% | $301.72, 16.2% | PASS |  |  |
| AAPL | L-sma50 | ladder row sma50: price and gap = price vs average | $339.69, 3.2% | $339.69, 3.2% | PASS |  |  |
| AAPL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $350.51 / entry $350.51 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 57.0 | 57.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +29.5% vs +10.1% | 29.5% vs 10.1% | PASS |  |  |
| AAPL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPL | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.6 | 18.6 | PASS |  | Wilder, completed bars |
| AAPL | T4w | words "20 or more / below 20" | below 20 | ADX 18.6 | PASS |  |  |
| AAPL | T5 | "counted at the last close ($X, date)" = last completed bar | $352.78, Nov 16 | $352.78, Nov 16 | PASS |  |  |
| AAPL | T6 | price vs 200-day average (S1 pattern sma values) | $352.78 vs $301.72 · +16.9% | $352.78 vs $301.72 · 16.9% | PASS |  |  |
| AAPL | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPL | T7 | price vs 50-day average (S1 pattern sma values) | $352.78 vs $339.69 · +3.9% | $352.78 vs $339.69 · 3.9% | PASS |  |  |
| AAPL | T7w | word "Above" | Above | Above | PASS |  |  |
| AAPL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.2% over 30 td | +4.2% over 30 td | PASS |  |  |
| AAPL | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.2% below $360.83 | 2.2% below $360.83 | PASS |  | closing high would be 356.27 |
| AAPL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.2% below | PASS |  |  |
| AAPL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $360.83 | $360.82999 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.98%, close location 0.25, OBV falling |
| AAPL | V2 | day change of the last completed bar | down 1.0% | -0.98% | PASS |  |  |
| AAPL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.05× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| AAPL | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.05× | 2026-11-16 1.05× | PASS |  |  |
| AAPL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.05× / 0.43× | 1.05× / 0.43× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 45945500) | 20 bars, last ('2026-11-16', 45945500) | PASS |  |  |
| F | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $11.33 | $11.33 | PASS |  |  |
| F | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $12.18 | $12.18 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| F | E3 | percent from the 21-day average | 7.0% below | 7.0% below | PASS |  |  |
| F | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| F | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.34 | $0.34 (sr=0.3429) | PASS |  | Wilder ATR14 |
| F | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| F | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.2 | +3.2 | PASS |  |  |
| F | L-ema21 | ladder row ema21: price and gap = price vs average | $12.18, -7.0% | $12.18, -7.0% | PASS |  |  |
| F | L-note | "Last close $X · date" note = last completed bar | Last close $11.57 · Nov 16 | $11.57 · Nov 16 | PASS |  |  |
| F | L-now | ladder price row = compared price; name = the basis label | $11.33 "Now" | $11.33 "now" | PASS |  |  |
| F | L-sma200 | ladder row sma200: price and gap = price vs average | $13.26, -14.6% | $13.26, -14.6% | PASS |  |  |
| F | L-sma50 | ladder row sma50: price and gap = price vs average | $12.5, -9.3% | $12.50, -9.3% | PASS |  |  |
| F | S5-price | S5: the same live price reads the same on the header and the Entry block | header $11.33 / entry $11.33 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| F | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| F | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.5 | 36.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| F | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -12.3% vs +10.1% | -12.3% vs 10.1% | PASS |  |  |
| F | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| F | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.0 | 20.0 | PASS |  | Wilder, completed bars |
| F | T5 | "counted at the last close ($X, date)" = last completed bar | $11.57, Nov 16 | $11.57, Nov 16 | PASS |  |  |
| F | T6 | price vs 200-day average (S1 pattern sma values) | $11.57 vs $13.26 · -12.7% | $11.57 vs $13.26 · -12.8% | PASS |  |  |
| F | T6w | word "Below" | Below | Below | PASS |  |  |
| F | T7 | price vs 50-day average (S1 pattern sma values) | $11.57 vs $12.50 · -7.4% | $11.57 vs $12.50 · -7.4% | PASS |  |  |
| F | T7w | word "Below" | Below | Below | PASS |  |  |
| F | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.7% over 30 td | -1.6% over 30 td | PASS |  |  |
| F | T8r | word "rising" | not rising | not rising | PASS |  |  |
| F | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| F | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.9% below $17.78 | 34.9% below $17.78 | PASS |  | closing high would be 17.44 |
| F | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.9% below | PASS |  |  |
| F | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $17.78 | $17.78 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| F | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.85%, close location 0.20, OBV falling |
| F | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| F | V2 | day change of the last completed bar | down 2.9% | -2.85% | PASS |  |  |
| F | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.20 (raw 0.2045) | PASS |  |  |
| F | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| F | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 0.99× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| F | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.99× | 2026-11-16 0.99× | PASS |  |  |
| F | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 0.96× | 0.99× / 0.96× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| F | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 43936700) | 20 bars, last ('2026-11-16', 43936700) | PASS |  |  |
| NVDA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $153.57 | $153.57 | PASS |  |  |
| NVDA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $190.71 | $190.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDA | E3 | percent from the 21-day average | 19.5% below | 19.5% below | PASS |  |  |
| NVDA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NVDA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.85 | $9.85 (sr=9.8532) | PASS |  | Wilder ATR14 |
| NVDA | E5 | distance in normal day-moves | 3.8 | 3.8 | PASS |  | gauge dot note uses the same number:  · 3.8 day-moves below |
| NVDA | L-ema21 | ladder row ema21: price and gap = price vs average | $190.71, -19.5% | $190.71, -19.5% | PASS |  |  |
| NVDA | L-note | "Last close $X · date" note = last completed bar | Last close $156.14 · Nov 16 | $156.14 · Nov 16 | PASS |  |  |
| NVDA | L-now | ladder price row = compared price; name = the basis label | $153.57 "Now" | $153.56 "now" | PASS |  |  |
| NVDA | L-sma200 | ladder row sma200: price and gap = price vs average | $204.02, -24.7% | $204.02, -24.7% | PASS |  |  |
| NVDA | L-sma50 | ladder row sma50: price and gap = price vs average | $213.16, -28.0% | $213.16, -28.0% | PASS |  |  |
| NVDA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $153.57 / entry $153.57 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.7 | 22.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -17.9% vs +10.1% | -17.9% vs 10.1% | PASS |  |  |
| NVDA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDA | T4 | ADX 14 (S1 /api/sr meta.adx) | 43.5 | 43.5 | PASS |  | Wilder, completed bars |
| NVDA | T4w | words "20 or more / below 20" | 20 or more | ADX 43.5 | PASS |  |  |
| NVDA | T5 | "counted at the last close ($X, date)" = last completed bar | $156.14, Nov 16 | $156.14, Nov 16 | PASS |  |  |
| NVDA | T6 | price vs 200-day average (S1 pattern sma values) | $156.14 vs $204.02 · -23.5% | $156.14 vs $204.02 · -23.5% | PASS |  |  |
| NVDA | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDA | T7 | price vs 50-day average (S1 pattern sma values) | $156.14 vs $213.16 · -26.7% | $156.14 vs $213.16 · -26.8% | PASS |  |  |
| NVDA | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| NVDA | T8r | word "rising" | still rising | rising | PASS |  |  |
| NVDA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.8% below $243.37 | 35.8% below $243.37 | PASS |  | closing high would be 239.24 |
| NVDA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.8% below | PASS |  |  |
| NVDA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $243.37 | $243.37 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.12%, close location 0.14, OBV falling |
| NVDA | V2 | day change of the last completed bar | down 4.1% | -4.12% | PASS |  |  |
| NVDA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1380) | PASS |  |  |
| NVDA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDA | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 2.2× from 2026-11-16 | 2.18× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| NVDA | V6 | Volume detail: last session date and RVOL | 2026-11-16 2.18× | 2026-11-16 2.18× | PASS |  |  |
| NVDA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.18× / 0.65× | 2.18× / 0.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 331405000) | 20 bars, last ('2026-11-16', 331405000) | PASS |  |  |
| NVDA | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.18, OBV falling | condition true | PASS |  |  |
| RIVN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $11.99 | $11.99 | PASS |  |  |
| RIVN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.01 | $13.01 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RIVN | E3 | percent from the 21-day average | 7.8% below | 7.8% below | PASS |  |  |
| RIVN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| RIVN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.65 | $0.65 (sr=0.6486) | PASS |  | Wilder ATR14 |
| RIVN | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| RIVN | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.6 | +3.6 | PASS |  |  |
| RIVN | L-ema21 | ladder row ema21: price and gap = price vs average | $13.01, -7.8% | $13.01, -7.8% | PASS |  |  |
| RIVN | L-note | "Last close $X · date" note = last completed bar | Last close $12.10 · Nov 16 | $12.10 · Nov 16 | PASS |  |  |
| RIVN | L-now | ladder price row = compared price; name = the basis label | $11.99 "Now" | $11.99 "now" | PASS |  |  |
| RIVN | L-sma200 | ladder row sma200: price and gap = price vs average | $15.32, -21.7% | $15.32, -21.7% | PASS |  |  |
| RIVN | L-sma50 | ladder row sma50: price and gap = price vs average | $13.88, -13.6% | $13.88, -13.6% | PASS |  |  |
| RIVN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $11.99 / entry $11.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RIVN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RIVN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.6 | 39.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RIVN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -19.9% vs +10.1% | -19.9% vs 10.1% | PASS |  |  |
| RIVN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RIVN | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.9 | 25.9 | PASS |  | Wilder, completed bars |
| RIVN | T4w | words "20 or more / below 20" | 20 or more | ADX 25.9 | PASS |  |  |
| RIVN | T5 | "counted at the last close ($X, date)" = last completed bar | $12.10, Nov 16 | $12.10, Nov 16 | PASS |  |  |
| RIVN | T6 | price vs 200-day average (S1 pattern sma values) | $12.10 vs $15.32 · -21.0% | $12.10 vs $15.32 · -21.0% | PASS |  |  |
| RIVN | T6w | word "Below" | Below | Below | PASS |  |  |
| RIVN | T7 | price vs 50-day average (S1 pattern sma values) | $12.10 vs $13.88 · -12.8% | $12.10 vs $13.88 · -12.8% | PASS |  |  |
| RIVN | T7w | word "Below" | Below | Below | PASS |  |  |
| RIVN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.1% over 30 td | -5.1% over 30 td | PASS |  |  |
| RIVN | T8r | word "rising" | not rising | not rising | PASS |  |  |
| RIVN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RIVN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 46.7% below $22.69 | 46.7% below $22.69 | PASS |  | closing high would be 22.45 |
| RIVN | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 46.7% below | PASS |  |  |
| RIVN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $22.69 | $22.690000534057617 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RIVN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.66%, close location 0.33, OBV falling |
| RIVN | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| RIVN | V2 | day change of the last completed bar | down 0.7% | -0.66% | PASS |  |  |
| RIVN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RIVN | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-16 | 1.28× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| RIVN | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.28× | 2026-11-16 1.28× | PASS |  |  |
| RIVN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.28× / 0.12× | 1.28× / 0.12× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RIVN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 35068400) | 20 bars, last ('2026-11-16', 35068400) | PASS |  |  |
| SMCI | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $24.02 | $24.02 | PASS |  |  |
| SMCI | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $30.82 | $30.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SMCI | E3 | percent from the 21-day average | 22.1% below | 22.1% below | PASS |  |  |
| SMCI | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| SMCI | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.58 | $2.58 (sr=2.5785) | PASS |  | Wilder ATR14 |
| SMCI | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| SMCI | L-ema21 | ladder row ema21: price and gap = price vs average | $30.82, -22.1% | $30.82, -22.1% | PASS |  |  |
| SMCI | L-now | ladder price row = compared price; name = the basis label | $24.02 "Now" | $24.02 "now" | PASS |  |  |
| SMCI | L-sma200 | ladder row sma200: price and gap = price vs average | $32.52, -26.2% | $32.52, -26.2% | PASS |  |  |
| SMCI | L-sma50 | ladder row sma50: price and gap = price vs average | $36.25, -33.7% | $36.25, -33.7% | PASS |  |  |
| SMCI | S5-price | S5: the same live price reads the same on the header and the Entry block | header $24.02 / entry $24.02 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SMCI | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SMCI | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.1 | 33.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SMCI | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -31.3% vs +10.1% | -31.3% vs 10.1% | PASS |  |  |
| SMCI | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SMCI | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.5 | 27.5 | PASS |  | Wilder, completed bars |
| SMCI | T4w | words "20 or more / below 20" | 20 or more | ADX 27.5 | PASS |  |  |
| SMCI | T6 | price vs 200-day average (S1 pattern sma values) | $25.03 vs $32.52 · -23.0% | $25.03 vs $32.52 · -23.0% | PASS |  |  |
| SMCI | T6w | word "Below" | Below | Below | PASS |  |  |
| SMCI | T7 | price vs 50-day average (S1 pattern sma values) | $25.03 vs $36.25 · -31.0% | $25.03 vs $36.25 · -30.9% | PASS |  |  |
| SMCI | T7w | word "Below" | Below | Below | PASS |  |  |
| SMCI | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.4% over 30 td | +1.4% over 30 td | PASS |  |  |
| SMCI | T8r | word "rising" | still rising | rising | PASS |  |  |
| SMCI | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SMCI | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 51.3% below $51.40 | 51.3% below $51.40 | PASS |  | closing high would be 50.17 |
| SMCI | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 51.3% below | PASS |  |  |
| SMCI | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $51.40 | $51.400001525878906 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SMCI | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.85%, close location 0.11, OBV falling |
| SMCI | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SMCI | V2 | day change of the last completed bar | down 6.8% | -6.85% | PASS |  |  |
| SMCI | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1064) | PASS |  |  |
| SMCI | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SMCI | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.84× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SMCI | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.84× | 2026-11-16 0.84× | PASS |  |  |
| SMCI | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.84× / 0.66× | 0.84× / 0.66× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SMCI | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 34333000) | 20 bars, last ('2026-11-16', 34333000) | PASS |  |  |
| SMH | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $454.16 | $454.16 | PASS |  |  |
| SMH | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $512.91 | $512.91 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SMH | E3 | percent from the 21-day average | 11.5% below | 11.5% below | PASS |  |  |
| SMH | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| SMH | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $24.35 | $24.35 (sr=24.3514) | PASS |  | Wilder ATR14 |
| SMH | E5 | distance in normal day-moves | 2.4 | 2.4 | PASS |  | gauge dot note uses the same number:  · 2.4 day-moves below |
| SMH | L-ema21 | ladder row ema21: price and gap = price vs average | $512.91, -11.5% | $512.91, -11.5% | PASS |  |  |
| SMH | L-note | "Last close $X · date" note = last completed bar | Last close $461.90 · Nov 16 | $461.90 · Nov 16 | PASS |  |  |
| SMH | L-now | ladder price row = compared price; name = the basis label | $454.16 "Now" | $454.16 "now" | PASS |  |  |
| SMH | L-sma200 | ladder row sma200: price and gap = price vs average | $524.18, -13.4% | $524.18, -13.4% | PASS |  |  |
| SMH | L-sma50 | ladder row sma50: price and gap = price vs average | $557.7, -18.6% | $557.70, -18.6% | PASS |  |  |
| SMH | S5-price | S5: the same live price reads the same on the header and the Entry block | header $454.16 / entry $454.16 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SMH | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SMH | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.6 | 35.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SMH | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +34.3% vs +10.1% | 34.3% vs 10.1% | PASS |  |  |
| SMH | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SMH | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.1 | 34.1 | PASS |  | Wilder, completed bars |
| SMH | T4w | words "20 or more / below 20" | 20 or more | ADX 34.1 | PASS |  |  |
| SMH | T5 | "counted at the last close ($X, date)" = last completed bar | $461.90, Nov 16 | $461.90, Nov 16 | PASS |  |  |
| SMH | T6 | price vs 200-day average (S1 pattern sma values) | $461.90 vs $524.18 · -11.9% | $461.90 vs $524.18 · -11.9% | PASS |  |  |
| SMH | T6w | word "Below" | Below | Below | PASS |  |  |
| SMH | T7 | price vs 50-day average (S1 pattern sma values) | $461.90 vs $557.70 · -17.2% | $461.90 vs $557.70 · -17.2% | PASS |  |  |
| SMH | T7w | word "Below" | Below | Below | PASS |  |  |
| SMH | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.6% over 30 td | +4.6% over 30 td | PASS |  |  |
| SMH | T8r | word "rising" | still rising | rising | PASS |  |  |
| SMH | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SMH | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 31.2% below $671.83 | 31.2% below $671.83 | PASS |  | closing high would be 668.91 |
| SMH | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 31.2% below | PASS |  |  |
| SMH | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $671.83 | $671.8300170898438 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SMH | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.11%, close location 0.10, OBV falling |
| SMH | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SMH | V2 | day change of the last completed bar | down 5.1% | -5.11% | PASS |  |  |
| SMH | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.0993) | PASS |  |  |
| SMH | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SMH | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.10× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SMH | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.10× | 2026-11-16 1.10× | PASS |  |  |
| SMH | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.10× / 0.97× | 1.10× / 0.97× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SMH | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 10038300) | 20 bars, last ('2026-11-16', 10038300) | PASS |  |  |
| SOXL.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $11.81 | $11.81 | PASS |  |  |
| SOXL.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.96 | $18.96 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL.NE | E3 | percent from the 21-day average | 37.7% below | 37.7% below | PASS |  |  |
| SOXL.NE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| SOXL.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.04 | $2.04 (sr=2.042) | PASS |  | Wilder ATR14 |
| SOXL.NE | E5 | distance in normal day-moves | 3.5 | 3.5 | PASS |  | gauge dot note uses the same number:  · 3.5 day-moves below |
| SOXL.NE | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.0 | +4.0 | PASS |  |  |
| SOXL.NE | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.8 | +5.8 | PASS |  |  |
| SOXL.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $18.96, -37.7% | $18.96, -37.7% | PASS |  |  |
| SOXL.NE | L-note | "Last close $X · date" note = last completed bar | Last close $12.30 · Nov 16 | $12.30 · Nov 16 | PASS |  |  |
| SOXL.NE | L-now | ladder price row = compared price; name = the basis label | $11.81 "Now" | $11.81 "now" | PASS |  |  |
| SOXL.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.88, -61.8% | $30.88, -61.8% | PASS |  |  |
| SOXL.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $27.08, -56.4% | $27.08, -56.4% | PASS |  |  |
| SOXL.NE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $11.81 / entry $11.81 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXL.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.5 | 34.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +21.7% vs +10.1% | 21.7% vs 10.1% | PASS |  |  |
| SOXL.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.6 | 26.6 | PASS |  | Wilder, completed bars |
| SOXL.NE | T4w | words "20 or more / below 20" | 20 or more | ADX 26.6 | PASS |  |  |
| SOXL.NE | T5 | "counted at the last close ($X, date)" = last completed bar | $12.30, Nov 16 | $12.30, Nov 16 | PASS |  |  |
| SOXL.NE | T6 | price vs 200-day average (S1 pattern sma values) | $12.30 vs $30.88 · -60.2% | $12.30 vs $30.88 · -60.2% | PASS |  |  |
| SOXL.NE | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T7 | price vs 50-day average (S1 pattern sma values) | $12.30 vs $27.08 · -54.6% | $12.30 vs $27.08 · -54.6% | PASS |  |  |
| SOXL.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.0% over 30 td | +5.0% over 30 td | PASS |  |  |
| SOXL.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 83.4% below $74.21 | 83.4% below $74.21 | PASS |  | closing high would be 74.21 |
| SOXL.NE | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 83.4% below | PASS |  |  |
| SOXL.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $74.21 | $74.21369934082031 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL.NE | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 50 of 50 days empty | 50 of 50 days empty | PASS |  |  |
