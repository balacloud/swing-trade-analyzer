# Statement Audit report

Run: 2026-11-18T10:28 · dumps: AAPL, AMD, DUK, ETN, FCX, NVDA, PLD, SOXL.NE · ET at first dump: 11/18/2026, 10:27:52 AM

Verdicts: PASS 295 · WRONG 0 (CRITICAL) · MISLEADING 0 (HIGH) · UNVERIFIED 14 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AAPL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $353.24 | $353.24 | PASS |  |  |
| AAPL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $347.14 | $347.14 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPL | E3 | percent from the 21-day average | 1.8% above | 1.8% above | PASS |  |  |
| AAPL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AAPL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.87 | $7.87 (sr=7.8729) | PASS |  | Wilder ATR14 |
| AAPL | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves above |
| AAPL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.8 | -5.8 | PASS |  |  |
| AAPL | L-ema21 | ladder row ema21: price and gap = price vs average | $347.14, 1.8% | $347.14, 1.8% | PASS |  |  |
| AAPL | L-note | "Last close $X · date" note = last completed bar | Last close $351.91 · Nov 17 | $351.91 · Nov 17 | PASS |  |  |
| AAPL | L-now | ladder price row = compared price; name = the basis label | $353.24 "Now" | $353.24 "now" | PASS |  |  |
| AAPL | L-sma200 | ladder row sma200: price and gap = price vs average | $301.66, 17.1% | $301.66, 17.1% | PASS |  |  |
| AAPL | L-sma50 | ladder row sma50: price and gap = price vs average | $340.17, 3.8% | $340.17, 3.8% | PASS |  |  |
| AAPL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $353.24 / entry $353.24 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| AMD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $511.04 | $511.04 | PASS |  |  |
| AMD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $523.46 | $523.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD | E3 | percent from the 21-day average | 2.4% below | 2.4% below | PASS |  |  |
| AMD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AMD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $40.57 | $40.57 (sr=40.5705) | PASS |  | Wilder ATR14 |
| AMD | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| AMD | L-ema21 | ladder row ema21: price and gap = price vs average | $523.46, -2.4% | $523.46, -2.4% | PASS |  |  |
| AMD | L-note | "Last close $X · date" note = last completed bar | Last close $503.41 · Nov 17 | $503.41 · Nov 17 | PASS |  |  |
| AMD | L-now | ladder price row = compared price; name = the basis label | $511.04 "Now" | $511.04 "now" | PASS |  |  |
| AMD | L-sma200 | ladder row sma200: price and gap = price vs average | $425.74, 20.0% | $425.74, 20.0% | PASS |  |  |
| AMD | L-sma50 | ladder row sma50: price and gap = price vs average | $555.04, -7.9% | $555.04, -7.9% | PASS |  |  |
| AMD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $511.04 / entry $511.04 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| DUK | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $129.77 | $129.77 | PASS |  |  |
| DUK | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $125.89 | $125.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DUK | E3 | percent from the 21-day average | 3.1% above | 3.1% above | PASS |  |  |
| DUK | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| DUK | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.15 | $2.15 (sr=2.1475) | PASS |  | Wilder ATR14 |
| DUK | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves above |
| DUK | L-ema21 | ladder row ema21: price and gap = price vs average | $125.89, 3.1% | $125.89, 3.1% | PASS |  |  |
| DUK | L-note | "Last close $X · date" note = last completed bar | Last close $129.84 · Nov 17 | $129.84 · Nov 17 | PASS |  |  |
| DUK | L-now | ladder price row = compared price; name = the basis label | $129.77 "Now" | $129.77 "now" | PASS |  |  |
| DUK | L-sma200 | ladder row sma200: price and gap = price vs average | $122.74, 5.7% | $122.74, 5.7% | PASS |  |  |
| DUK | L-sma50 | ladder row sma50: price and gap = price vs average | $120.08, 8.1% | $120.08, 8.1% | PASS |  |  |
| DUK | S5-price | S5: the same live price reads the same on the header and the Entry block | header $129.77 / entry $129.77 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DUK | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DUK | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 66.5 | 66.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DUK | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +7.3% vs +11.2% | 7.3% vs 11.2% | PASS |  |  |
| DUK | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DUK | T4 | ADX 14 (S1 /api/sr meta.adx) | 48.0 | 48.0 | PASS |  | Wilder, completed bars |
| DUK | T4w | words "20 or more / below 20" | 20 or more | ADX 48.0 | PASS |  |  |
| DUK | T5 | "counted at the last close ($X, date)" = last completed bar | $129.84, Nov 17 | $129.84, Nov 17 | PASS |  |  |
| DUK | T6 | price vs 200-day average (S1 pattern sma values) | $129.84 vs $122.74 · +5.8% | $129.84 vs $122.74 · 5.8% | PASS |  |  |
| DUK | T6w | word "Above" | Above | Above | PASS |  |  |
| DUK | T7 | price vs 50-day average (S1 pattern sma values) | $129.84 vs $120.08 · +8.1% | $129.84 vs $120.08 · 8.1% | PASS |  |  |
| DUK | T7w | word "Above" | Above | Above | PASS |  |  |
| DUK | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.2% over 30 td | +1.1% over 30 td | PASS |  |  |
| DUK | T8r | word "rising" | still rising | rising | PASS |  |  |
| DUK | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DUK | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.5% below $131.87 | 1.5% below $131.87 | PASS |  | closing high would be 130.59 |
| DUK | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.5% below | PASS |  |  |
| DUK | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.87 | $131.86787171141273 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DUK | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.57%, close location 0.33, OBV rising |
| DUK | V2 | day change of the last completed bar | down 0.6% | -0.57% | PASS |  |  |
| DUK | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| DUK | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.5× from 2026-11-17 | 1.54× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| DUK | V6 | Volume detail: last session date and RVOL | 2026-11-17 1.54× | 2026-11-17 1.54× | PASS |  |  |
| DUK | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.54× / 0.34× | 1.54× / 0.35× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DUK | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 6743545) | 20 bars, last ('2026-11-17', 6743545) | PASS |  |  |
| ETN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $336.95 | $336.95 | PASS |  |  |
| ETN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $364.94 | $364.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ETN | E3 | percent from the 21-day average | 7.7% below | 7.7% below | PASS |  |  |
| ETN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| ETN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $18.05 | $18.05 (sr=18.0454) | PASS |  | Wilder ATR14 |
| ETN | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| ETN | L-ema21 | ladder row ema21: price and gap = price vs average | $364.94, -7.7% | $364.94, -7.7% | PASS |  |  |
| ETN | L-note | "Last close $X · date" note = last completed bar | Last close $337.11 · Nov 17 | $337.11 · Nov 17 | PASS |  |  |
| ETN | L-now | ladder price row = compared price; name = the basis label | $336.95 "Now" | $336.95 "now" | PASS |  |  |
| ETN | L-sma200 | ladder row sma200: price and gap = price vs average | $395.33, -14.8% | $395.33, -14.8% | PASS |  |  |
| ETN | L-sma50 | ladder row sma50: price and gap = price vs average | $397.06, -15.1% | $397.06, -15.1% | PASS |  |  |
| ETN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $336.95 / entry $336.95 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ETN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ETN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.8 | 37.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ETN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -0.5% vs +11.2% | -0.5% vs 11.2% | PASS |  |  |
| ETN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ETN | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.7 | 26.7 | PASS |  | Wilder, completed bars |
| ETN | T4w | words "20 or more / below 20" | 20 or more | ADX 26.7 | PASS |  |  |
| ETN | T5 | "counted at the last close ($X, date)" = last completed bar | $337.11, Nov 17 | $337.11, Nov 17 | PASS |  |  |
| ETN | T6 | price vs 200-day average (S1 pattern sma values) | $337.11 vs $395.33 · -14.7% | $337.11 vs $395.33 · -14.7% | PASS |  |  |
| ETN | T6w | word "Below" | Below | Below | PASS |  |  |
| ETN | T7 | price vs 50-day average (S1 pattern sma values) | $337.11 vs $397.06 · -15.1% | $337.11 vs $397.06 · -15.1% | PASS |  |  |
| ETN | T7w | word "Below" | Below | Below | PASS |  |  |
| ETN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.0% over 30 td | +2.0% over 30 td | PASS |  |  |
| ETN | T8r | word "rising" | still rising | rising | PASS |  |  |
| ETN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ETN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.3% below $476.54 | 29.3% below $476.54 | PASS |  | closing high would be 458.55 |
| ETN | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.3% below | PASS |  |  |
| ETN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $476.54 | $476.5365977066434 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ETN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change 0.07%, close location 0.42, OBV falling |
| ETN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ETN | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-17 | 1.30× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| ETN | V6 | Volume detail: last session date and RVOL | 2026-11-17 1.30× | 2026-11-17 1.30× | PASS |  |  |
| ETN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.30× / 0.01× | 1.30× / 0.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ETN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 3435048) | 20 bars, last ('2026-11-17', 3435048) | PASS |  |  |
| FCX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $51.12 | $51.12 | PASS |  |  |
| FCX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $62.12 | $62.12 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FCX | E3 | percent from the 21-day average | 17.7% below | 17.7% below | PASS |  |  |
| FCX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| FCX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.82 | $2.82 (sr=2.8226) | PASS |  | Wilder ATR14 |
| FCX | E5 | distance in normal day-moves | 3.9 | 3.9 | PASS |  | gauge dot note uses the same number:  · 3.9 day-moves below |
| FCX | L-ema21 | ladder row ema21: price and gap = price vs average | $62.12, -17.7% | $62.12, -17.7% | PASS |  |  |
| FCX | L-note | "Last close $X · date" note = last completed bar | Last close $55.30 · Nov 17 | $55.30 · Nov 17 | PASS |  |  |
| FCX | L-now | ladder price row = compared price; name = the basis label | $51.12 "Now" | $51.12 "now" | PASS |  |  |
| FCX | L-sma200 | ladder row sma200: price and gap = price vs average | $64.91, -21.2% | $64.91, -21.2% | PASS |  |  |
| FCX | L-sma50 | ladder row sma50: price and gap = price vs average | $67.65, -24.4% | $67.65, -24.4% | PASS |  |  |
| FCX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $51.12 / entry $51.12 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| FCX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FCX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.0 | 31.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FCX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +43.1% vs +11.2% | 43.1% vs 11.2% | PASS |  |  |
| FCX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FCX | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.7 | 26.7 | PASS |  | Wilder, completed bars |
| FCX | T4w | words "20 or more / below 20" | 20 or more | ADX 26.7 | PASS |  |  |
| FCX | T5 | "counted at the last close ($X, date)" = last completed bar | $55.30, Nov 17 | $55.30, Nov 17 | PASS |  |  |
| FCX | T6 | price vs 200-day average (S1 pattern sma values) | $55.30 vs $64.91 · -14.8% | $55.30 vs $64.91 · -14.8% | PASS |  |  |
| FCX | T6w | word "Below" | Below | Below | PASS |  |  |
| FCX | T7 | price vs 50-day average (S1 pattern sma values) | $55.30 vs $67.65 · -18.3% | $55.30 vs $67.65 · -18.3% | PASS |  |  |
| FCX | T7w | word "Below" | Below | Below | PASS |  |  |
| FCX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| FCX | T8r | word "rising" | still rising | rising | PASS |  |  |
| FCX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FCX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 30.9% below $80.07 | 30.9% below $80.07 | PASS |  | closing high would be 79.74 |
| FCX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 30.9% below | PASS |  |  |
| FCX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.07 | $80.06712214676648 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FCX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change 0.20%, close location 0.24, OBV falling |
| FCX | V2 | day change of the last completed bar | up 0.2% | +0.20% | PASS |  |  |
| FCX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.24 (raw 0.2426) | PASS |  |  |
| FCX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| FCX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-17 | 1.26× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| FCX | V6 | Volume detail: last session date and RVOL | 2026-11-17 1.26× | 2026-11-17 1.26× | PASS |  |  |
| FCX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.26× / 0.04× | 1.26× / 0.04× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FCX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 14934793) | 20 bars, last ('2026-11-17', 14934793) | PASS |  |  |
| NVDA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $153.02 | $153.02 | PASS |  |  |
| NVDA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $187.5 | $187.50 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDA | E3 | percent from the 21-day average | 18.4% below | 18.4% below | PASS |  |  |
| NVDA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NVDA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.71 | $9.71 (sr=9.7101) | PASS |  | Wilder ATR14 |
| NVDA | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  · 3.6 day-moves below |
| NVDA | L-ema21 | ladder row ema21: price and gap = price vs average | $187.5, -18.4% | $187.50, -18.4% | PASS |  |  |
| NVDA | L-note | "Last close $X · date" note = last completed bar | Last close $155.46 · Nov 17 | $155.46 · Nov 17 | PASS |  |  |
| NVDA | L-now | ladder price row = compared price; name = the basis label | $153.02 "Now" | $153.02 "now" | PASS |  |  |
| NVDA | L-sma200 | ladder row sma200: price and gap = price vs average | $203.6, -24.8% | $203.60, -24.8% | PASS |  |  |
| NVDA | L-sma50 | ladder row sma50: price and gap = price vs average | $211.75, -27.7% | $211.75, -27.7% | PASS |  |  |
| NVDA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $153.02 / entry $153.02 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| PLD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $125.10 | $125.10 | PASS |  |  |
| PLD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $128.51 | $128.51 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PLD | E3 | percent from the 21-day average | 2.7% below | 2.7% below | PASS |  |  |
| PLD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| PLD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.51 | $2.51 (sr=2.5068) | PASS |  | Wilder ATR14 |
| PLD | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| PLD | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| PLD | L-ema21 | ladder row ema21: price and gap = price vs average | $128.51, -2.7% | $128.51, -2.7% | PASS |  |  |
| PLD | L-note | "Last close $X · date" note = last completed bar | Last close $125.56 · Nov 17 | $125.56 · Nov 17 | PASS |  |  |
| PLD | L-now | ladder price row = compared price; name = the basis label | $125.1 "Now" | $125.10 "now" | PASS |  |  |
| PLD | L-sma200 | ladder row sma200: price and gap = price vs average | $136.34, -8.2% | $136.34, -8.2% | PASS |  |  |
| PLD | L-sma50 | ladder row sma50: price and gap = price vs average | $130.09, -3.8% | $130.09, -3.8% | PASS |  |  |
| PLD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $125.10 / entry $125.10 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| SOXL.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.50 | $12.50 | PASS |  |  |
| SOXL.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.36 | $18.36 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL.NE | E3 | percent from the 21-day average | 31.9% below | 31.9% below | PASS |  |  |
| SOXL.NE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| SOXL.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.02 | $2.02 (sr=2.0226) | PASS |  | Wilder ATR14 |
| SOXL.NE | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| SOXL.NE | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.1 | +4.1 | PASS |  |  |
| SOXL.NE | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.2 | +6.2 | PASS |  |  |
| SOXL.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $18.36, -31.9% | $18.36, -31.9% | PASS |  |  |
| SOXL.NE | L-note | "Last close $X · date" note = last completed bar | Last close $12.36 · Nov 17 | $12.36 · Nov 17 | PASS |  |  |
| SOXL.NE | L-now | ladder price row = compared price; name = the basis label | $12.5 "Now" | $12.50 "now" | PASS |  |  |
| SOXL.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.87, -59.5% | $30.87, -59.5% | PASS |  |  |
| SOXL.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $26.74, -53.3% | $26.74, -53.3% | PASS |  |  |
| SOXL.NE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $12.50 / entry $12.50 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXL.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.6 | 34.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +23.6% vs +11.2% | 23.6% vs 11.2% | PASS |  |  |
| SOXL.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.1 | 27.1 | PASS |  | Wilder, completed bars |
| SOXL.NE | T4w | words "20 or more / below 20" | 20 or more | ADX 27.1 | PASS |  |  |
| SOXL.NE | T5 | "counted at the last close ($X, date)" = last completed bar | $12.36, Nov 17 | $12.36, Nov 17 | PASS |  |  |
| SOXL.NE | T6 | price vs 200-day average (S1 pattern sma values) | $12.36 vs $30.87 · -60.0% | $12.36 vs $30.87 · -60.0% | PASS |  |  |
| SOXL.NE | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T7 | price vs 50-day average (S1 pattern sma values) | $12.36 vs $26.74 · -53.8% | $12.36 vs $26.74 · -53.8% | PASS |  |  |
| SOXL.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.4% over 30 td | +4.4% over 30 td | PASS |  |  |
| SOXL.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 83.3% below $74.21 | 83.3% below $74.21 | PASS |  | closing high would be 74.21 |
| SOXL.NE | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 83.3% below | PASS |  |  |
| SOXL.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $74.21 | $74.21369934082031 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL.NE | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 49 of 50 days empty | 49 of 50 days empty | PASS |  |  |
