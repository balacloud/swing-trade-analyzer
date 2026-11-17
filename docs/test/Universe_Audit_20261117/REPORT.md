# Statement Audit report

Run: 2026-11-17T16:00 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM · ET at first dump: 11/17/2026, 3:53:43 PM

Verdicts: PASS 4032 · WRONG 68 (CRITICAL) · MISLEADING 26 (HIGH) · UNVERIFIED 251 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AAPU | T6 | price vs 200-day average (S1 pattern sma values) | $48.77 vs $38.03 · +28.2% | $48.77 vs $38.28 · 27.4% | WRONG | CRITICAL |  |
| AAPU | T7 | price vs 50-day average (S1 pattern sma values) | $48.77 vs $45.83 · +6.4% | $48.77 vs $45.86 · 6.3% | WRONG | CRITICAL |  |
| AAPU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.8% over 30 td | +6.5% over 30 td | WRONG | CRITICAL |  |
| AMD | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.4× from 2026-11-16 | 1.31× from 2026-11-16 | WRONG | CRITICAL | window "50 bars" includes the bar itself |
| AMD | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.36× | 2026-11-16 1.31× | WRONG | CRITICAL |  |
| AMD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.36× / 0.68× | 1.31× / 0.68× | WRONG | CRITICAL | ATR % uses the sr price (may be a partial bar) |
| AMD.TO | L-note | "Last close $X · date" note = last completed bar | Last close $12.97 · Nov 16 | $13.76 · Nov 13 | WRONG | CRITICAL |  |
| AMD.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $12.97, Nov 16 | $13.76, Nov 13 | WRONG | CRITICAL |  |
| AVGC | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.3 | 22.0 | WRONG | CRITICAL | matches neither the completed-bar nor the forming-bar Wilder ADX |
| AVGC | V6 | Volume detail: last session date and RVOL | 2026-11-16 2.19× | 2026-11-16 2.21× | WRONG | CRITICAL |  |
| AVGC | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.19× / 0.81× | 2.21× / 0.81× | WRONG | CRITICAL | ATR % uses the sr price (may be a partial bar) |
| BOTZ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 27.8% below $41.71 | 27.8% below $41.69 | WRONG | CRITICAL | closing high would be 41.61 |
| BRK-B | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 1 up, 1 down, 1 flat | WRONG | CRITICAL | change -0.02%, close location 0.59, OBV rising |
| BRKU | L-note | "Last close $X · date" note = last completed bar | Last close $30.76 · Nov 16 | $30.81 · Nov 16 | WRONG | CRITICAL |  |
| BRKU | T5 | "counted at the last close ($X, date)" = last completed bar | $30.76, Nov 16 | $30.81, Nov 16 | WRONG | CRITICAL |  |
| BRKU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 2 up, 0 down, 1 flat | WRONG | CRITICAL | change 0.03%, close location 0.70, OBV rising |
| CARS.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.7 | 27.9 | WRONG | CRITICAL | matches neither the completed-bar nor the forming-bar Wilder ADX |
| CAT | T6 | price vs 200-day average (S1 pattern sma values) | $570.49 vs $803.95 · -29.0% | $570.49 vs $807.00 · -29.3% | WRONG | CRITICAL |  |
| CAT | T7 | price vs 50-day average (S1 pattern sma values) | $570.49 vs $734.62 · -22.3% | $570.49 vs $735.90 · -22.5% | WRONG | CRITICAL |  |
| CAT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 46.6% below $1,068.93 | 46.9% below $1073.46 | WRONG | CRITICAL | closing high would be 1064.90 |
| COP | T6 | price vs 200-day average (S1 pattern sma values) | $140.52 vs $121.84 · +15.3% | $140.52 vs $123.50 · 13.8% | WRONG | CRITICAL |  |
| COP | T7 | price vs 50-day average (S1 pattern sma values) | $140.52 vs $136.53 · +2.9% | $140.52 vs $137.41 · 2.3% | WRONG | CRITICAL |  |
| COP | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.1% over 30 td | +5.8% over 30 td | WRONG | CRITICAL |  |
| COP | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.3% below $153.27 | 8.9% below $154.28 | WRONG | CRITICAL | closing high would be 154.03 |
| CVX | T6 | price vs 200-day average (S1 pattern sma values) | $217.14 vs $195.97 · +10.8% | $217.14 vs $194.16 · 11.8% | WRONG | CRITICAL |  |
| CVX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.8% over 30 td | +5.3% over 30 td | WRONG | CRITICAL |  |
| DRAL | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.5 | 33.7 | WRONG | CRITICAL | matches neither the completed-bar nor the forming-bar Wilder ADX |
| GE | T6 | price vs 200-day average (S1 pattern sma values) | $325.18 vs $323.97 · +0.4% | $325.18 vs $323.30 · 0.6% | WRONG | CRITICAL |  |
| GE | T7 | price vs 50-day average (S1 pattern sma values) | $325.18 vs $314.53 · +3.4% | $325.18 vs $314.36 · 3.4% | WRONG | CRITICAL |  |
| GE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 16.4% below $388.84 | 16.2% below $388.25 | WRONG | CRITICAL | closing high would be 380.64 |
| GEV | T6 | price vs 200-day average (S1 pattern sma values) | $763.57 vs $951.97 · -19.8% | $763.57 vs $951.16 · -19.7% | WRONG | CRITICAL |  |
| GEV | T7 | price vs 50-day average (S1 pattern sma values) | $763.57 vs $909.60 · -16.1% | $763.57 vs $909.23 · -16.0% | WRONG | CRITICAL |  |
| GEV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.2% below $1,195.94 | 36.1% below $1195.24 | WRONG | CRITICAL | closing high would be 1174.17 |
| GGLL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.73× from 2026-11-16 | WRONG | CRITICAL | window "50 bars" includes the bar itself |
| GGLL | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.75× | 2026-11-16 0.73× | WRONG | CRITICAL |  |
| GGLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.75× / 1.00× | 0.73× / 1.00× | WRONG | CRITICAL | ATR % uses the sr price (may be a partial bar) |
| JNJ | T6 | price vs 200-day average (S1 pattern sma values) | $282.55 vs $250.04 · +13.0% | $282.55 vs $248.60 · 13.7% | WRONG | CRITICAL |  |
| JNJ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.4% over 30 td | +3.6% over 30 td | WRONG | CRITICAL |  |
| LIN | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.9 | 33.1 | WRONG | CRITICAL | matches neither the completed-bar nor the forming-bar Wilder ADX |
| LIN | T6 | price vs 200-day average (S1 pattern sma values) | $523.46 vs $497.01 · +5.3% | $523.46 vs $494.92 · 5.8% | WRONG | CRITICAL |  |
| LIN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.5% below $548.20 | 4.2% below $546.40 | WRONG | CRITICAL | closing high would be 544.85 |
| NEE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 4 / 8 | WRONG | CRITICAL | recomputed all 8 criteria from the bars |
| NEE | T6 | price vs 200-day average (S1 pattern sma values) | $85.34 vs $87.35 · -2.3% | $85.34 vs $86.53 · -1.4% | WRONG | CRITICAL |  |
| NEE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.0% over 30 td | +0.3% over 30 td | WRONG | CRITICAL |  |
| NEE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.6% below $98.75 | 12.3% below $97.30 | WRONG | CRITICAL | closing high would be 96.44 |
| PG | T4 | ADX 14 (S1 /api/sr meta.adx) | 41.2 | 42.9 | WRONG | CRITICAL | matches neither the completed-bar nor the forming-bar Wilder ADX |
| PG | T6 | price vs 200-day average (S1 pattern sma values) | $173.02 vs $149.97 · +15.4% | $173.02 vs $148.12 · 16.8% | WRONG | CRITICAL |  |
| PG | T7 | price vs 50-day average (S1 pattern sma values) | $173.02 vs $154.77 · +11.8% | $173.02 vs $154.14 · 12.2% | WRONG | CRITICAL |  |
| PG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +2.0% over 30 td | WRONG | CRITICAL |  |
| QPUX | T6 | price vs 200-day average (S1 pattern sma values) | $3.59 vs $28.55 · -87.4% | $3.59 vs $20.51 · -82.5% | WRONG | CRITICAL |  |
| QPUX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -45.2% over 30 td | -25.9% over 30 td | WRONG | CRITICAL |  |
| QPUX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 98.5% below $240.84 | 95.5% below $80.28 | WRONG | CRITICAL | closing high would be 79.57 |
| QTUM | T6 | price vs 200-day average (S1 pattern sma values) | $124.47 vs $138.40 · -10.1% | $124.47 vs $137.92 · -9.7% | WRONG | CRITICAL |  |
| QTUM | T7 | price vs 50-day average (S1 pattern sma values) | $124.47 vs $142.80 · -12.8% | $124.47 vs $142.71 · -12.8% | WRONG | CRITICAL |  |
| QTUM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.5% over 30 td | +2.7% over 30 td | WRONG | CRITICAL |  |
| QTUM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.8% below $170.00 | 26.4% below $169.21 | WRONG | CRITICAL | closing high would be 167.97 |
| RTX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 5 / 8 | WRONG | CRITICAL | recomputed all 8 criteria from the bars |
| RTX | T6 | price vs 200-day average (S1 pattern sma values) | $194.89 vs $195.26 · -0.2% | $194.89 vs $194.49 · 0.2% | WRONG | CRITICAL |  |
| RTX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.1% below $226.88 | 13.9% below $226.41 | WRONG | CRITICAL | closing high would be 225.49 |
| SPCL | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.79× | 2026-11-16 0.80× | WRONG | CRITICAL |  |
| SPCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.79× / 0.83× | 0.80× / 0.83× | WRONG | CRITICAL | ATR % uses the sr price (may be a partial bar) |
| UFO | T6 | price vs 200-day average (S1 pattern sma values) | $39.54 vs $47.06 · -16.0% | $39.54 vs $47.02 · -15.9% | WRONG | CRITICAL |  |
| UFO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 42.0% below $68.21 | 42.0% below $68.12 | WRONG | CRITICAL | closing high would be 67.71 |
| URAA | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.99× | 2026-11-16 0.98× | WRONG | CRITICAL |  |
| URAA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 0.75× | 0.98× / 0.75× | WRONG | CRITICAL | ATR % uses the sr price (may be a partial bar) |
| VFV.TO | L-note | "Last close $X · date" note = last completed bar | Last close $188.17 · Nov 16 | $191.40 · Nov 13 | WRONG | CRITICAL |  |
| VFV.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $188.17, Nov 16 | $191.40, Nov 13 | WRONG | CRITICAL |  |
| WELL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 2 up, 1 down, 0 flat | WRONG | CRITICAL | change 0.08%, close location 0.06, OBV rising |
| ANET.TO | T3w | words "past year" vs the window used | 225 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| AVGO.TO | T3w | words "past year" vs the window used | 225 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| BOTZ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $41.71 | $41.689149923077814 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,068.93 | $1073.45996 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COP | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $153.27 | $154.28 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COST | L-note | "Last close $X · date" note = last completed bar | Last close $1,113.74 · Nov 16 | $1113.74 · Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close |
| COTG | L-note | "Last close $X · date" note = last completed bar | Last close $17.05 · Nov 16 | $17.04 · Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close |
| COTG | T5 | "counted at the last close ($X, date)" = last completed bar | $17.05, Nov 16 | $17.04, Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close (e.g. Twelve Data 25.025 vs Yahoo 25.03); the header/quote path and the price bars can read different providers |
| CSU.TO | L-note | "Last close $X · date" note = last completed bar | Last close $3,436.53 · Nov 16 | $3436.53 · Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close |
| EQIX | L-note | "Last close $X · date" note = last completed bar | Last close $1,043.06 · Nov 16 | $1043.06 · Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close |
| GE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $388.84 | $388.2496041459131 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GEV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,195.94 | $1195.2406896758491 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GEV.TO | T3w | words "past year" vs the window used | 225 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| LIN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $548.20 | $546.4006244123242 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LLY | L-note | "Last close $X · date" note = last completed bar | Last close $1,431.67 · Nov 16 | $1431.67 · Nov 16 | MISLEADING | LOW | one-cent disagreement between two data providers for the same close |
| MTRX.TO | T3w | words "past year" vs the window used | 207 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| NEE | T8r | word "rising" | not rising | rising | MISLEADING | HIGH |  |
| NEE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $98.75 | $97.30028062322594 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PNG.V | V1 | volume signal tally | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 2 down, 1 flat | MISLEADING | LOW | borderline: close location 0.2500 is just above 0.25 but the app rounds it to 0.25 before comparing (display rounding at a threshold) |
| PNG.V | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.25 (raw 0.2500) | MISLEADING | LOW | display rounding at the threshold: raw value is just outside |
| QPUX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $240.84 | $80.27999877929688 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QTUM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $170.00 | $169.2079473044215 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RTX | T6w | word "Below" | Below | Above | MISLEADING | HIGH |  |
| RTX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $226.88 | $226.41000366210938 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UFO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $68.21 | $68.11999548611959 | MISLEADING | HIGH | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XETM.TO | T3w | words "past year" vs the window used | 207 / 251 bars back | 250-253 bars | MISLEADING | HIGH | history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback) |
| AAPL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 226 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ANET.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 251 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ASTL.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | U1 | numbers on the card no statement above claimed (exhaustive scan) | 98 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AVGC | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 226 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AVGO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.0 $13.05 | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CEG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | T1 | Trend checks N / 8 | 7 / 8 | needs 252 bars | UNVERIFIED | INFO | only 251 bars |
| CNQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 189 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | U1 | numbers on the card no statement above claimed (exhaustive scan) | $1,110.90 3.6 | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COST | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | U1 | numbers on the card no statement above claimed (exhaustive scan) | $16.95 3.6 | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COTG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 251 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CSU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 101 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DRAL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 158 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DRAM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 226 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GEV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GRID | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GRID | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 251 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HXQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 208 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MTRX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 251 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NTR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 139 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ORBX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 251 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RBOT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SETM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SETM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 145 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SGRD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 132 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SNDK.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 155 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SPCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URAA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URAA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 131 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| WDC.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 208 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XETM.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $351.19 | $351.19 | PASS |  |  |
| AAPL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $346.86 | $346.86 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPL | E3 | percent from the 21-day average | 1.2% above | 1.2% above | PASS |  |  |
| AAPL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AAPL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.05 | $8.05 (sr=8.0462) | PASS |  | Wilder ATR14 |
| AAPL | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| AAPL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.6 | -5.6 | PASS |  |  |
| AAPL | L-ema21 | ladder row ema21: price and gap = price vs average | $346.86, 1.2% | $346.86, 1.2% | PASS |  |  |
| AAPL | L-note | "Last close $X · date" note = last completed bar | Last close $352.78 · Nov 16 | $352.78 · Nov 16 | PASS |  |  |
| AAPL | L-now | ladder price row = compared price; name = the basis label | $351.19 "Now" | $351.19 "now" | PASS |  |  |
| AAPL | L-sma200 | ladder row sma200: price and gap = price vs average | $301.72, 16.4% | $301.72, 16.4% | PASS |  |  |
| AAPL | L-sma50 | ladder row sma50: price and gap = price vs average | $339.69, 3.4% | $339.69, 3.4% | PASS |  |  |
| AAPL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $351.19 / entry $351.19 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| AAPU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $48.30 | $48.30 | PASS |  |  |
| AAPU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $47.43 | $47.43 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPU | E3 | percent from the 21-day average | 1.8% above | 1.8% above | PASS |  |  |
| AAPU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AAPU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.08 | $2.09 (sr=2.0849) | PASS |  | Wilder ATR14 |
| AAPU | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves above |
| AAPU | L-ema21 | ladder row ema21: price and gap = price vs average | $47.43, 1.8% | $47.43, 1.8% | PASS |  |  |
| AAPU | L-note | "Last close $X · date" note = last completed bar | Last close $48.77 · Nov 16 | $48.77 · Nov 16 | PASS |  |  |
| AAPU | L-now | ladder price row = compared price; name = the basis label | $48.3 "Now" | $48.30 "now" | PASS |  |  |
| AAPU | L-sma200 | ladder row sma200: price and gap = price vs average | $38.28, 26.2% | $38.28, 26.2% | PASS |  |  |
| AAPU | L-sma50 | ladder row sma50: price and gap = price vs average | $45.86, 5.3% | $45.86, 5.3% | PASS |  |  |
| AAPU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $48.30 / entry $48.30 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.8 | 55.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +33.5% vs +10.1% | 33.5% vs 10.1% | PASS |  |  |
| AAPU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPU | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.1 | 18.1 | PASS |  | Wilder, completed bars |
| AAPU | T4w | words "20 or more / below 20" | below 20 | ADX 18.1 | PASS |  |  |
| AAPU | T5 | "counted at the last close ($X, date)" = last completed bar | $48.77, Nov 16 | $48.77, Nov 16 | PASS |  |  |
| AAPU | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T7w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.4% below $51.04 | 4.4% below $51.04 | PASS |  | closing high would be 49.81 |
| AAPU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.4% below | PASS |  |  |
| AAPU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $51.04 | $51.040001 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.09%, close location 0.23, OBV falling |
| AAPU | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AAPU | V2 | day change of the last completed bar | down 2.1% | -2.09% | PASS |  |  |
| AAPU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.23 (raw 0.2288) | PASS |  |  |
| AAPU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPU | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.3× from 2026-11-16 | 0.34× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| AAPU | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.34× | 2026-11-16 0.34× | PASS |  |  |
| AAPU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.34× / 0.49× | 0.34× / 0.49× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 329600) | 20 bars, last ('2026-11-16', 329600) | PASS |  |  |
| ABBV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $292.36 | $292.36 | PASS |  |  |
| ABBV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $288.96 | $288.96 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ABBV | E3 | percent from the 21-day average | 1.2% above | 1.2% above | PASS |  |  |
| ABBV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| ABBV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.91 | $6.91 (sr=6.9093) | PASS |  | Wilder ATR14 |
| ABBV | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| ABBV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -6.9 | -6.9 | PASS |  |  |
| ABBV | L-ema21 | ladder row ema21: price and gap = price vs average | $288.96, 1.2% | $288.96, 1.2% | PASS |  |  |
| ABBV | L-note | "Last close $X · date" note = last completed bar | Last close $294.55 · Nov 16 | $294.55 · Nov 16 | PASS |  |  |
| ABBV | L-now | ladder price row = compared price; name = the basis label | $292.36 "Now" | $292.36 "now" | PASS |  |  |
| ABBV | L-sma200 | ladder row sma200: price and gap = price vs average | $241.12, 21.3% | $241.12, 21.3% | PASS |  |  |
| ABBV | L-sma50 | ladder row sma50: price and gap = price vs average | $276.23, 5.8% | $276.23, 5.8% | PASS |  |  |
| ABBV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $292.36 / entry $292.36 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ABBV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ABBV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 61.8 | 61.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ABBV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +26.8% vs +10.1% | 26.8% vs 10.1% | PASS |  |  |
| ABBV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ABBV | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.1 | 30.1 | PASS |  | Wilder, completed bars |
| ABBV | T4w | words "20 or more / below 20" | 20 or more | ADX 30.1 | PASS |  |  |
| ABBV | T5 | "counted at the last close ($X, date)" = last completed bar | $294.55, Nov 16 | $294.55, Nov 16 | PASS |  |  |
| ABBV | T6 | price vs 200-day average (S1 pattern sma values) | $294.55 vs $241.12 · +22.2% | $294.55 vs $241.12 · 22.2% | PASS |  |  |
| ABBV | T6w | word "Above" | Above | Above | PASS |  |  |
| ABBV | T7 | price vs 50-day average (S1 pattern sma values) | $294.55 vs $276.23 · +6.6% | $294.55 vs $276.23 · 6.6% | PASS |  |  |
| ABBV | T7w | word "Above" | Above | Above | PASS |  |  |
| ABBV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.1% over 30 td | +4.1% over 30 td | PASS |  |  |
| ABBV | T8r | word "rising" | still rising | rising | PASS |  |  |
| ABBV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ABBV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.8% below $302.93 | 2.8% below $302.93 | PASS |  | closing high would be 295.03 |
| ABBV | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.8% below | PASS |  |  |
| ABBV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.93 | $302.93 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ABBV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.16%, close location 0.08, OBV rising |
| ABBV | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ABBV | V2 | day change of the last completed bar | down 0.2% | -0.16% | PASS |  |  |
| ABBV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0802) | PASS |  |  |
| ABBV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ABBV | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.11× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ABBV | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.11× | 2026-11-16 1.11× | PASS |  |  |
| ABBV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.11× / 0.07× | 1.11× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ABBV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 5493798) | 20 bars, last ('2026-11-16', 5493798) | PASS |  |  |
| AIPO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $22.50 | $22.50 | PASS |  |  |
| AIPO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $24.51 | $24.51 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AIPO | E3 | percent from the 21-day average | 8.2% below | 8.2% below | PASS |  |  |
| AIPO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AIPO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.14 | $1.14 (sr=1.1392) | PASS |  | Wilder ATR14 |
| AIPO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| AIPO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| AIPO | L-ema21 | ladder row ema21: price and gap = price vs average | $24.51, -8.2% | $24.51, -8.2% | PASS |  |  |
| AIPO | L-note | "Last close $X · date" note = last completed bar | Last close $22.69 · Nov 16 | $22.69 · Nov 16 | PASS |  |  |
| AIPO | L-now | ladder price row = compared price; name = the basis label | $22.5 "Now" | $22.50 "now" | PASS |  |  |
| AIPO | L-sma200 | ladder row sma200: price and gap = price vs average | $28.51, -21.1% | $28.51, -21.1% | PASS |  |  |
| AIPO | L-sma50 | ladder row sma50: price and gap = price vs average | $26.7, -15.7% | $26.70, -15.7% | PASS |  |  |
| AIPO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $22.50 / entry $22.50 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AIPO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AIPO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.7 | 38.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AIPO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.3% vs +10.1% | 0.3% vs 10.1% | PASS |  |  |
| AIPO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AIPO | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.4 | 31.5 | PASS |  | Wilder, completed bars |
| AIPO | T4w | words "20 or more / below 20" | 20 or more | ADX 31.5 | PASS |  |  |
| AIPO | T5 | "counted at the last close ($X, date)" = last completed bar | $22.69, Nov 16 | $22.69, Nov 16 | PASS |  |  |
| AIPO | T6 | price vs 200-day average (S1 pattern sma values) | $22.69 vs $28.51 · -20.4% | $22.69 vs $28.51 · -20.4% | PASS |  |  |
| AIPO | T6w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T7 | price vs 50-day average (S1 pattern sma values) | $22.69 vs $26.70 · -15.0% | $22.69 vs $26.70 · -15.0% | PASS |  |  |
| AIPO | T7w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.1% over 30 td | +1.1% over 30 td | PASS |  |  |
| AIPO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AIPO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AIPO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.8% below $34.79 | 34.8% below $34.79 | PASS |  | closing high would be 34.77 |
| AIPO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.8% below | PASS |  |  |
| AIPO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $34.79 | $34.7899 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AIPO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.10%, close location 0.15, OBV falling |
| AIPO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AIPO | V2 | day change of the last completed bar | down 4.1% | -4.10% | PASS |  |  |
| AIPO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1538) | PASS |  |  |
| AIPO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AIPO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 1.02× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| AIPO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.02× | 2026-11-16 1.02× | PASS |  |  |
| AIPO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.02× / 0.82× | 1.02× / 0.82× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AIPO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1661742) | 20 bars, last ('2026-11-16', 1661742) | PASS |  |  |
| ALAB | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $207.34 | $207.34 | PASS |  |  |
| ALAB | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $243.94 | $243.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ALAB | E3 | percent from the 21-day average | 15.0% below | 15.0% below | PASS |  |  |
| ALAB | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| ALAB | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $23.85 | $23.85 (sr=23.8519) | PASS |  | Wilder ATR14 |
| ALAB | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| ALAB | L-ema21 | ladder row ema21: price and gap = price vs average | $243.94, -15.0% | $243.94, -15.0% | PASS |  |  |
| ALAB | L-note | "Last close $X · date" note = last completed bar | Last close $202.34 · Nov 16 | $202.34 · Nov 16 | PASS |  |  |
| ALAB | L-now | ladder price row = compared price; name = the basis label | $207.34 "Now" | $207.34 "now" | PASS |  |  |
| ALAB | L-sma200 | ladder row sma200: price and gap = price vs average | $257.72, -19.5% | $257.72, -19.5% | PASS |  |  |
| ALAB | L-sma50 | ladder row sma50: price and gap = price vs average | $292.1, -29.0% | $292.10, -29.0% | PASS |  |  |
| ALAB | S5-price | S5: the same live price reads the same on the header and the Entry block | header $207.34 / entry $207.34 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ALAB | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ALAB | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.8 | 35.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ALAB | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +40.2% vs +10.1% | 40.2% vs 10.1% | PASS |  |  |
| ALAB | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ALAB | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.7 | 28.7 | PASS |  | Wilder, completed bars |
| ALAB | T4w | words "20 or more / below 20" | 20 or more | ADX 28.7 | PASS |  |  |
| ALAB | T5 | "counted at the last close ($X, date)" = last completed bar | $202.34, Nov 16 | $202.34, Nov 16 | PASS |  |  |
| ALAB | T6 | price vs 200-day average (S1 pattern sma values) | $202.34 vs $257.72 · -21.5% | $202.34 vs $257.72 · -21.5% | PASS |  |  |
| ALAB | T6w | word "Below" | Below | Below | PASS |  |  |
| ALAB | T7 | price vs 50-day average (S1 pattern sma values) | $202.34 vs $292.10 · -30.7% | $202.34 vs $292.10 · -30.7% | PASS |  |  |
| ALAB | T7w | word "Below" | Below | Below | PASS |  |  |
| ALAB | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.4% over 30 td | +6.4% over 30 td | PASS |  |  |
| ALAB | T8r | word "rising" | still rising | rising | PASS |  |  |
| ALAB | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ALAB | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 59.5% below $499.48 | 59.5% below $499.48 | PASS |  | closing high would be 483.02 |
| ALAB | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 59.5% below | PASS |  |  |
| ALAB | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $499.48 | $499.47601318359375 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ALAB | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -8.79%, close location 0.13, OBV falling |
| ALAB | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ALAB | V2 | day change of the last completed bar | down 8.8% | -8.79% | PASS |  |  |
| ALAB | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.13 (raw 0.1259) | PASS |  |  |
| ALAB | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ALAB | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 1.02× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ALAB | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.02× | 2026-11-16 1.02× | PASS |  |  |
| ALAB | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.02× / 0.75× | 1.02× / 0.75× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ALAB | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 4625700) | 20 bars, last ('2026-11-16', 4625700) | PASS |  |  |
| AMD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $493.79 | $493.79 | PASS |  |  |
| AMD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $525.46 | $525.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD | E3 | percent from the 21-day average | 6.0% below | 6.0% below | PASS |  |  |
| AMD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AMD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $41.28 | $41.28 (sr=41.2793) | PASS |  | Wilder ATR14 |
| AMD | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves below |
| AMD | L-ema21 | ladder row ema21: price and gap = price vs average | $525.46, -6.0% | $525.46, -6.0% | PASS |  |  |
| AMD | L-note | "Last close $X · date" note = last completed bar | Last close $504.28 · Nov 16 | $504.28 · Nov 16 | PASS |  |  |
| AMD | L-now | ladder price row = compared price; name = the basis label | $493.79 "Now" | $493.79 "now" | PASS |  |  |
| AMD | L-sma200 | ladder row sma200: price and gap = price vs average | $424.46, 16.3% | $424.46, 16.3% | PASS |  |  |
| AMD | L-sma50 | ladder row sma50: price and gap = price vs average | $555.09, -11.0% | $555.09, -11.0% | PASS |  |  |
| AMD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $493.79 / entry $493.79 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.7 | 46.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +104.3% vs +10.1% | 104.3% vs 10.1% | PASS |  |  |
| AMD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.8 | 18.8 | PASS |  | Wilder, completed bars |
| AMD | T4w | words "20 or more / below 20" | below 20 | ADX 18.8 | PASS |  |  |
| AMD | T5 | "counted at the last close ($X, date)" = last completed bar | $504.28, Nov 16 | $504.28, Nov 16 | PASS |  |  |
| AMD | T6 | price vs 200-day average (S1 pattern sma values) | $504.28 vs $424.46 · +18.8% | $504.28 vs $424.46 · 18.8% | PASS |  |  |
| AMD | T6w | word "Above" | Above | Above | PASS |  |  |
| AMD | T7 | price vs 50-day average (S1 pattern sma values) | $504.28 vs $555.09 · -9.2% | $504.28 vs $555.09 · -9.2% | PASS |  |  |
| AMD | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +12.6% over 30 td | +12.6% over 30 td | PASS |  |  |
| AMD | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.4% below $658.52 | 23.4% below $658.52 | PASS |  | closing high would be 649.42 |
| AMD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.4% below | PASS |  |  |
| AMD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $658.52 | $658.52002 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -5.58%, close location 0.12, OBV rising |
| AMD | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AMD | V2 | day change of the last completed bar | down 5.6% | -5.58% | PASS |  |  |
| AMD | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1197) | PASS |  |  |
| AMD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AMD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 35890100) | 20 bars, last ('2026-11-16', 35890100) | PASS |  |  |
| AMD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.79 | $12.79 | PASS |  |  |
| AMD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.58 | $13.58 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD.TO | E3 | percent from the 21-day average | 5.8% below | 5.8% below | PASS |  |  |
| AMD.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AMD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.06 | $1.06 (sr=1.0591) | PASS |  | Wilder ATR14 |
| AMD.TO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| AMD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $13.58, -5.8% | $13.58, -5.8% | PASS |  |  |
| AMD.TO | L-now | ladder price row = compared price; name = the basis label | $12.79 "Now" | $12.79 "now" | PASS |  |  |
| AMD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $10.93, 17.0% | $10.93, 17.0% | PASS |  |  |
| AMD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $14.22, -10.1% | $14.22, -10.1% | PASS |  |  |
| AMD.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $12.79 / entry $12.79 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.4 | 50.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +109.4% vs +10.1% | 109.4% vs 10.1% | PASS |  |  |
| AMD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.2 | 20.2 | PASS |  | Wilder, completed bars |
| AMD.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 20.2 | PASS |  |  |
| AMD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $13.76 vs $10.93 · +25.9% | $13.76 vs $10.93 · 25.9% | PASS |  |  |
| AMD.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| AMD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $13.76 vs $14.22 · -3.2% | $13.76 vs $14.22 · -3.2% | PASS |  |  |
| AMD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +12.8% over 30 td | +12.8% over 30 td | PASS |  |  |
| AMD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 18.9% below $16.97 | 18.9% below $16.97 | PASS |  | closing high would be 16.73 |
| AMD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 18.9% below | PASS |  |  |
| AMD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $16.97 | $16.968570709228516 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -8.57%, close location 0.28, OBV rising |
| AMD.TO | V2 | day change of the last completed bar | down 8.6% | -8.57% | PASS |  |  |
| AMD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AMD.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 2.1× from 2026-11-13 | 2.11× from 2026-11-13 | PASS |  | window "50 bars" includes the bar itself |
| AMD.TO | V6 | Volume detail: last session date and RVOL | 2026-11-13 2.11× | 2026-11-13 2.11× | PASS |  |  |
| AMD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.11× / 1.11× | 2.11× / 1.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-13', 4798700) | 20 bars, last ('2026-11-13', 4798700) | PASS |  |  |
| AMZN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $256.48 | $256.48 | PASS |  |  |
| AMZN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $259.05 | $259.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZN | E3 | percent from the 21-day average | 1.0% below | 1.0% below | PASS |  |  |
| AMZN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AMZN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.15 | $9.15 (sr=9.1458) | PASS |  | Wilder ATR14 |
| AMZN | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| AMZN | L-ema21 | ladder row ema21: price and gap = price vs average | $259.05, -1.0% | $259.05, -1.0% | PASS |  |  |
| AMZN | L-note | "Last close $X · date" note = last completed bar | Last close $257.75 · Nov 16 | $257.75 · Nov 16 | PASS |  |  |
| AMZN | L-now | ladder price row = compared price; name = the basis label | $256.48 "Now" | $256.48 "now" | PASS |  |  |
| AMZN | L-sma200 | ladder row sma200: price and gap = price vs average | $244.69, 4.8% | $244.69, 4.8% | PASS |  |  |
| AMZN | L-sma50 | ladder row sma50: price and gap = price vs average | $254.8, 0.7% | $254.80, 0.7% | PASS |  |  |
| AMZN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $256.48 / entry $256.48 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.6 | 49.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +9.8% vs +10.1% | 9.8% vs 10.1% | PASS |  |  |
| AMZN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZN | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.2 | 12.2 | PASS |  | Wilder, completed bars |
| AMZN | T4w | words "20 or more / below 20" | below 20 | ADX 12.2 | PASS |  |  |
| AMZN | T5 | "counted at the last close ($X, date)" = last completed bar | $257.75, Nov 16 | $257.75, Nov 16 | PASS |  |  |
| AMZN | T6 | price vs 200-day average (S1 pattern sma values) | $257.75 vs $244.69 · +5.3% | $257.75 vs $244.69 · 5.3% | PASS |  |  |
| AMZN | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T7 | price vs 50-day average (S1 pattern sma values) | $257.75 vs $254.80 · +1.2% | $257.75 vs $254.80 · 1.2% | PASS |  |  |
| AMZN | T7w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| AMZN | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMZN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.3% below $287.20 | 10.3% below $287.20 | PASS |  | closing high would be 284.02 |
| AMZN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.3% below | PASS |  |  |
| AMZN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $287.20 | $287.2 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.34%, close location 0.17, OBV falling |
| AMZN | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AMZN | V2 | day change of the last completed bar | down 3.3% | -3.34% | PASS |  |  |
| AMZN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1715) | PASS |  |  |
| AMZN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZN | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.2× from 2026-11-16 | 1.16× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| AMZN | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.16× | 2026-11-16 1.16× | PASS |  |  |
| AMZN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.16× / 0.94× | 1.16× / 0.94× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 48054227) | 20 bars, last ('2026-11-16', 48054227) | PASS |  |  |
| AMZU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $35.17 | $35.17 | PASS |  |  |
| AMZU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $36.01 | $36.01 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZU | E3 | percent from the 21-day average | 2.3% below | 2.3% below | PASS |  |  |
| AMZU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AMZU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.51 | $2.51 (sr=2.5128) | PASS |  | Wilder ATR14 |
| AMZU | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| AMZU | L-ema21 | ladder row ema21: price and gap = price vs average | $36.01, -2.3% | $36.01, -2.3% | PASS |  |  |
| AMZU | L-note | "Last close $X · date" note = last completed bar | Last close $35.27 · Nov 16 | $35.27 · Nov 16 | PASS |  |  |
| AMZU | L-now | ladder price row = compared price; name = the basis label | $35.17 "Now" | $35.17 "now" | PASS |  |  |
| AMZU | L-sma200 | ladder row sma200: price and gap = price vs average | $35.2, -0.1% | $35.20, -0.1% | PASS |  |  |
| AMZU | L-sma50 | ladder row sma50: price and gap = price vs average | $35.32, -0.4% | $35.32, -0.4% | PASS |  |  |
| AMZU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $35.17 / entry $35.17 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.2 | 48.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -8.2% vs +10.1% | -8.2% vs 10.1% | PASS |  |  |
| AMZU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZU | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.1 | 12.1 | PASS |  | Wilder, completed bars |
| AMZU | T4w | words "20 or more / below 20" | below 20 | ADX 12.1 | PASS |  |  |
| AMZU | T5 | "counted at the last close ($X, date)" = last completed bar | $35.27, Nov 16 | $35.27, Nov 16 | PASS |  |  |
| AMZU | T6 | price vs 200-day average (S1 pattern sma values) | $35.27 vs $35.20 · +0.2% | $35.27 vs $35.20 · 0.2% | PASS |  |  |
| AMZU | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZU | T7 | price vs 50-day average (S1 pattern sma values) | $35.27 vs $35.32 · -0.1% | $35.27 vs $35.32 · -0.2% | PASS |  |  |
| AMZU | T7w | word "Below" | Below | Below | PASS |  |  |
| AMZU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.3% over 30 td | -0.3% over 30 td | PASS |  |  |
| AMZU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AMZU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 25.2% below $47.14 | 25.2% below $47.14 | PASS |  | closing high would be 45.93 |
| AMZU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 25.2% below | PASS |  |  |
| AMZU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $47.14 | $47.14 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.62%, close location 0.17, OBV falling |
| AMZU | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AMZU | V2 | day change of the last completed bar | down 6.6% | -6.62% | PASS |  |  |
| AMZU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1724) | PASS |  |  |
| AMZU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZU | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.5× from 2026-11-16 | 0.45× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| AMZU | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.45× | 2026-11-16 0.45× | PASS |  |  |
| AMZU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.45× / 0.93× | 0.45× / 0.93× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 867808) | 20 bars, last ('2026-11-16', 867808) | PASS |  |  |
| ANET.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $33.41 | $33.41 | PASS |  |  |
| ANET.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $33.28 | $33.28 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ANET.TO | E3 | percent from the 21-day average | 0.4% above | 0.4% above | PASS |  |  |
| ANET.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ANET.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.05 | $2.05 (sr=2.0488) | PASS |  | Wilder ATR14 |
| ANET.TO | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| ANET.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $33.28, 0.4% | $33.28, 0.4% | PASS |  |  |
| ANET.TO | L-now | ladder price row = compared price; name = the basis label | $33.41 "Last close" | $33.41 "last close" | PASS |  |  |
| ANET.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $30.1, 11.0% | $30.10, 11.0% | PASS |  |  |
| ANET.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $34.44, -3.0% | $34.44, -3.0% | PASS |  |  |
| ANET.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.0 | 50.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ANET.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +40.1% vs +10.1% | 40.1% vs 10.1% | PASS |  |  |
| ANET.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.3 | 19.3 | PASS |  | Wilder, completed bars |
| ANET.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.3 | PASS |  |  |
| ANET.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -5.22%, close location 0.40, OBV rising |
| ANET.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ANET.TO | V2 | day change of the last completed bar | down 5.2% | -5.22% | PASS |  |  |
| ANET.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ANET.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.15× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ANET.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.15× | 2026-11-16 1.15× | PASS |  |  |
| ANET.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.15× / 0.85× | 1.15× / 0.85× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ANET.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 53900) | 20 bars, last ('2026-11-16', 53900) | PASS |  |  |
| ASML.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $41.62 | $41.62 | PASS |  |  |
| ASML.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $44.94 | $44.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASML.TO | E3 | percent from the 21-day average | 7.4% below | 7.4% below | PASS |  |  |
| ASML.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ASML.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.88 | $1.88 (sr=1.8776) | PASS |  | Wilder ATR14 |
| ASML.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| ASML.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $44.94, -7.4% | $44.94, -7.4% | PASS |  |  |
| ASML.TO | L-now | ladder price row = compared price; name = the basis label | $41.62 "Last close" | $41.62 "last close" | PASS |  |  |
| ASML.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $45.06, -7.6% | $45.06, -7.6% | PASS |  |  |
| ASML.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $47.49, -12.4% | $47.49, -12.4% | PASS |  |  |
| ASML.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ASML.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.1 | 39.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASML.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.2% vs +10.1% | 49.2% vs 10.1% | PASS |  |  |
| ASML.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ASML.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.0 | 25.0 | PASS |  | Wilder, completed bars |
| ASML.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.0 | PASS |  |  |
| ASML.TO | T6 | price vs 200-day average (S1 pattern sma values) | $41.62 vs $45.06 · -7.6% | $41.62 vs $45.06 · -7.6% | PASS |  |  |
| ASML.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| ASML.TO | T7 | price vs 50-day average (S1 pattern sma values) | $41.62 vs $47.49 · -12.4% | $41.62 vs $47.49 · -12.4% | PASS |  |  |
| ASML.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| ASML.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.5% over 30 td | +4.5% over 30 td | PASS |  |  |
| ASML.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ASML.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ASML.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.7% below $56.75 | 26.7% below $56.75 | PASS |  | closing high would be 56.67 |
| ASML.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.7% below | PASS |  |  |
| ASML.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $56.75 | $56.745395859548175 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ASML.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.05%, close location 0.03, OBV falling |
| ASML.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ASML.TO | V2 | day change of the last completed bar | down 6.0% | -6.05% | PASS |  |  |
| ASML.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0337) | PASS |  |  |
| ASML.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ASML.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.6× from 2026-11-16 | 1.60× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ASML.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.60× | 2026-11-16 1.60× | PASS |  |  |
| ASML.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.60× / 1.34× | 1.60× / 1.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASML.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 71100) | 20 bars, last ('2026-11-16', 71100) | PASS |  |  |
| ASML.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.60, OBV falling | condition true | PASS |  |  |
| ASTL.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $7.31 | $7.31 | PASS |  |  |
| ASTL.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $7.27 | $7.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASTL.TO | E3 | percent from the 21-day average | 0.6% above | 0.6% above | PASS |  |  |
| ASTL.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| ASTL.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.42 | $0.42 (sr=0.4186) | PASS |  | Wilder ATR14 |
| ASTL.TO | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| ASTL.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $7.27, 0.6% | $7.27, 0.6% | PASS |  |  |
| ASTL.TO | L-note | "Last close $X · date" note = last completed bar | Last close $7.67 · Nov 16 | $7.67 · Nov 16 | PASS |  |  |
| ASTL.TO | L-now | ladder price row = compared price; name = the basis label | $7.31 "Now" | $7.31 "now" | PASS |  |  |
| ASTL.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $6.25, 16.9% | $6.25, 16.9% | PASS |  |  |
| ASTL.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $6.49, 12.6% | $6.49, 12.6% | PASS |  |  |
| ASTL.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $7.31 / entry $7.31 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ASTL.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.9 | 59.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASTL.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +56.2% vs +10.1% | 56.2% vs 10.1% | PASS |  |  |
| ASTL.TO | T3w | words "past year" vs the window used | 250 / 251 bars back | 250-253 bars | PASS |  |  |
| ASTL.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.3 | 29.4 | PASS |  | Wilder, completed bars |
| ASTL.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 29.4 | PASS |  |  |
| ASTL.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -1.54%, close location 0.68, OBV flat |
| ASTL.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ASTL.TO | V2 | day change of the last completed bar | down 1.5% | -1.54% | PASS |  |  |
| ASTL.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| ASTL.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.75× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ASTL.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.75× | 2026-11-16 0.75× | PASS |  |  |
| ASTL.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.75× / 0.28× | 0.75× / 0.28× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASTL.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 447700) | 20 bars, last ('2026-11-16', 447700) | PASS |  |  |
| ATD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $83.41 | $83.41 | PASS |  |  |
| ATD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $82.36 | $82.36 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ATD.TO | E3 | percent from the 21-day average | 1.3% above | 1.3% above | PASS |  |  |
| ATD.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| ATD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.70 | $1.70 (sr=1.6951) | PASS |  | Wilder ATR14 |
| ATD.TO | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves above |
| ATD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $82.36, 1.3% | $82.36, 1.3% | PASS |  |  |
| ATD.TO | L-note | "Last close $X · date" note = last completed bar | Last close $83.90 · Nov 16 | $83.90 · Nov 16 | PASS |  |  |
| ATD.TO | L-now | ladder price row = compared price; name = the basis label | $83.41 "Now" | $83.41 "now" | PASS |  |  |
| ATD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $82.32, 1.3% | $82.32, 1.3% | PASS |  |  |
| ATD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $80.71, 3.3% | $80.71, 3.3% | PASS |  |  |
| ATD.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $83.41 / entry $83.41 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ATD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ATD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 57.6 | 57.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ATD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +20.6% vs +10.1% | 20.6% vs 10.1% | PASS |  |  |
| ATD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ATD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.3 | 16.3 | PASS |  | Wilder, completed bars |
| ATD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 16.3 | PASS |  |  |
| ATD.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $83.90, Nov 16 | $83.90, Nov 16 | PASS |  |  |
| ATD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $83.90 vs $82.32 · +1.9% | $83.90 vs $82.32 · 1.9% | PASS |  |  |
| ATD.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| ATD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $83.90 vs $80.71 · +4.0% | $83.90 vs $80.71 · 4.0% | PASS |  |  |
| ATD.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| ATD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| ATD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ATD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ATD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.4% below $94.68 | 11.4% below $94.68 | PASS |  | closing high would be 93.29 |
| ATD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.4% below | PASS |  |  |
| ATD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $94.68 | $94.67526234045502 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ATD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 1.27%, close location 0.99, OBV rising |
| ATD.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ATD.TO | V2 | day change of the last completed bar | up 1.3% | +1.27% | PASS |  |  |
| ATD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.99 (raw 0.9934) | PASS |  |  |
| ATD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ATD.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.76× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ATD.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.76× | 2026-11-16 0.76× | PASS |  |  |
| ATD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.76× / 0.63× | 0.76× / 0.63× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ATD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 992200) | 20 bars, last ('2026-11-16', 992200) | PASS |  |  |
| AVGC | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.48 | $17.48 | PASS |  |  |
| AVGC | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.25 | $18.25 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGC | E3 | percent from the 21-day average | 4.2% below | 4.2% below | PASS |  |  |
| AVGC | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AVGC | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.71 | $1.71 (sr=1.7117) | PASS |  | Wilder ATR14 |
| AVGC | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves below |
| AVGC | L-ema21 | ladder row ema21: price and gap = price vs average | $18.25, -4.2% | $18.25, -4.2% | PASS |  |  |
| AVGC | L-now | ladder price row = compared price; name = the basis label | $17.48 "Last close" | $17.48 "last close" | PASS |  |  |
| AVGC | L-sma50 | ladder row sma50: price and gap = price vs average | $19.79, -11.7% | $19.79, -11.7% | PASS |  |  |
| AVGC | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.8 | 46.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGC | T4w | words "20 or more / below 20" | 20 or more | ADX 22.0 | PASS |  |  |
| AVGC | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -7.90%, close location 0.64, OBV falling |
| AVGC | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AVGC | V2 | day change of the last completed bar | down 7.9% | -7.90% | PASS |  |  |
| AVGC | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AVGC | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 2.2× from 2026-11-16 | 2.21× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| AVGC | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 6800) | 20 bars, last ('2026-11-16', 6800) | PASS |  |  |
| AVGC | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.21, OBV falling | condition true | PASS |  |  |
| AVGO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $337.79 | $337.79 | PASS |  |  |
| AVGO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $335.27 | $335.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGO | E3 | percent from the 21-day average | 0.8% above | 0.8% above | PASS |  |  |
| AVGO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| AVGO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.94 | $17.94 (sr=17.9357) | PASS |  | Wilder ATR14 |
| AVGO | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| AVGO | L-ema21 | ladder row ema21: price and gap = price vs average | $335.27, 0.8% | $335.27, 0.8% | PASS |  |  |
| AVGO | L-note | "Last close $X · date" note = last completed bar | Last close $333.40 · Nov 16 | $333.40 · Nov 16 | PASS |  |  |
| AVGO | L-now | ladder price row = compared price; name = the basis label | $337.79 "Now" | $337.79 "now" | PASS |  |  |
| AVGO | L-sma200 | ladder row sma200: price and gap = price vs average | $367.43, -8.1% | $367.43, -8.1% | PASS |  |  |
| AVGO | L-sma50 | ladder row sma50: price and gap = price vs average | $344.89, -2.1% | $344.89, -2.1% | PASS |  |  |
| AVGO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $337.79 / entry $337.79 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AVGO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AVGO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.8 | 48.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -2.6% vs +10.1% | -2.6% vs 10.1% | PASS |  |  |
| AVGO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AVGO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.0 | 22.0 | PASS |  | Wilder, completed bars |
| AVGO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.0 | PASS |  |  |
| AVGO | T5 | "counted at the last close ($X, date)" = last completed bar | $333.40, Nov 16 | $333.40, Nov 16 | PASS |  |  |
| AVGO | T6 | price vs 200-day average (S1 pattern sma values) | $333.40 vs $367.43 · -9.3% | $333.40 vs $367.43 · -9.3% | PASS |  |  |
| AVGO | T6w | word "Below" | Below | Below | PASS |  |  |
| AVGO | T7 | price vs 50-day average (S1 pattern sma values) | $333.40 vs $344.89 · -3.3% | $333.40 vs $344.89 · -3.3% | PASS |  |  |
| AVGO | T7w | word "Below" | Below | Below | PASS |  |  |
| AVGO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.0% over 30 td | -0.0% over 30 td | PASS |  |  |
| AVGO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AVGO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AVGO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 32.6% below $495.00 | 32.6% below $495.00 | PASS |  | closing high would be 481.57 |
| AVGO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 32.6% below | PASS |  |  |
| AVGO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $495.00 | $495 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AVGO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -3.92%, close location 0.56, OBV rising |
| AVGO | V2 | day change of the last completed bar | down 3.9% | -3.92% | PASS |  |  |
| AVGO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 1.03× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| AVGO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.03× | 2026-11-16 1.03× | PASS |  |  |
| AVGO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.03× / 0.73× | 1.03× / 0.73× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 26056800) | 20 bars, last ('2026-11-16', 26056800) | PASS |  |  |
| AVGO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.64 | $12.64 | PASS |  |  |
| AVGO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $12.71 | $12.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGO.TO | E3 | percent from the 21-day average | 0.6% below | 0.6% below | PASS |  |  |
| AVGO.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AVGO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.67 | $0.67 (sr=0.6674) | PASS |  | Wilder ATR14 |
| AVGO.TO | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves below |
| AVGO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $12.71, -0.6% | $12.71, -0.6% | PASS |  |  |
| AVGO.TO | L-now | ladder price row = compared price; name = the basis label | $12.64 "Last close" | $12.64 "last close" | PASS |  |  |
| AVGO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $14.02, -9.8% | $14.02, -9.8% | PASS |  |  |
| AVGO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $13.1, -3.5% | $13.10, -3.5% | PASS |  |  |
| AVGO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.7 | 48.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.1% vs +10.1% | -4.1% vs 10.1% | PASS |  |  |
| AVGO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.2 | 22.1 | PASS |  | Wilder, completed bars |
| AVGO.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.1 | PASS |  |  |
| AVGO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -3.81%, close location 0.59, OBV rising |
| AVGO.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| AVGO.TO | V2 | day change of the last completed bar | down 3.8% | -3.81% | PASS |  |  |
| AVGO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGO.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.7× from 2026-11-16 | 0.65× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| AVGO.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.65× | 2026-11-16 0.65× | PASS |  |  |
| AVGO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.65× / 0.72× | 0.65× / 0.72× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 755100) | 20 bars, last ('2026-11-16', 755100) | PASS |  |  |
| BDT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $75.18 | $75.18 | PASS |  |  |
| BDT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $74.27 | $74.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BDT.TO | E3 | percent from the 21-day average | 1.2% above | 1.2% above | PASS |  |  |
| BDT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| BDT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.97 | $3.97 (sr=3.9737) | PASS |  | Wilder ATR14 |
| BDT.TO | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| BDT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $74.27, 1.2% | $74.27, 1.2% | PASS |  |  |
| BDT.TO | L-now | ladder price row = compared price; name = the basis label | $75.18 "Last close" | $75.18 "last close" | PASS |  |  |
| BDT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.36, 28.8% | $58.36, 28.8% | PASS |  |  |
| BDT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $76.12, -1.2% | $76.12, -1.2% | PASS |  |  |
| BDT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BDT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.4 | 51.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BDT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +199.4% vs +10.1% | 199.4% vs 10.1% | PASS |  |  |
| BDT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BDT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.7 | 15.7 | PASS |  | Wilder, completed bars |
| BDT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.7 | PASS |  |  |
| BDT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $75.18 vs $58.36 · +28.8% | $75.18 vs $58.36 · 28.8% | PASS |  |  |
| BDT.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| BDT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $75.18 vs $76.12 · -1.2% | $75.18 vs $76.12 · -1.2% | PASS |  |  |
| BDT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| BDT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +13.5% over 30 td | +13.4% over 30 td | PASS |  |  |
| BDT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| BDT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BDT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.0% below $86.42 | 13.0% below $86.42 | PASS |  | closing high would be 85.33 |
| BDT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.0% below | PASS |  |  |
| BDT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $86.42 | $86.42048390957993 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BDT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.97%, close location 0.72, OBV falling |
| BDT.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| BDT.TO | V2 | day change of the last completed bar | down 2.0% | -1.97% | PASS |  |  |
| BDT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BDT.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.7× from 2026-11-16 | 0.72× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| BDT.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.72× | 2026-11-16 0.72× | PASS |  |  |
| BDT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.72× / 0.37× | 0.72× / 0.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BDT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 286300) | 20 bars, last ('2026-11-16', 286300) | PASS |  |  |
| BOTZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $29.69 | $29.69 | PASS |  |  |
| BOTZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $32.31 | $32.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BOTZ | E3 | percent from the 21-day average | 8.1% below | 8.1% below | PASS |  |  |
| BOTZ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| BOTZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.80 | $0.80 (sr=0.7967) | PASS |  | Wilder ATR14 |
| BOTZ | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| BOTZ | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.9 | +4.9 | PASS |  |  |
| BOTZ | L-ema21 | ladder row ema21: price and gap = price vs average | $32.31, -8.1% | $32.31, -8.1% | PASS |  |  |
| BOTZ | L-note | "Last close $X · date" note = last completed bar | Last close $30.12 · Nov 16 | $30.12 · Nov 16 | PASS |  |  |
| BOTZ | L-now | ladder price row = compared price; name = the basis label | $29.69 "Now" | $29.69 "now" | PASS |  |  |
| BOTZ | L-sma200 | ladder row sma200: price and gap = price vs average | $36.23, -18.1% | $36.23, -18.1% | PASS |  |  |
| BOTZ | L-sma50 | ladder row sma50: price and gap = price vs average | $33.98, -12.6% | $33.98, -12.6% | PASS |  |  |
| BOTZ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $29.69 / entry $29.69 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BOTZ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BOTZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.1 | 33.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BOTZ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -13.9% vs +10.1% | -13.9% vs 10.1% | PASS |  |  |
| BOTZ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BOTZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.5 | 32.5 | PASS |  | Wilder, completed bars |
| BOTZ | T4w | words "20 or more / below 20" | 20 or more | ADX 32.5 | PASS |  |  |
| BOTZ | T5 | "counted at the last close ($X, date)" = last completed bar | $30.12, Nov 16 | $30.12, Nov 16 | PASS |  |  |
| BOTZ | T6 | price vs 200-day average (S1 pattern sma values) | $30.12 vs $36.24 · -16.9% | $30.12 vs $36.23 · -16.9% | PASS |  |  |
| BOTZ | T6w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T7 | price vs 50-day average (S1 pattern sma values) | $30.12 vs $33.98 · -11.4% | $30.12 vs $33.98 · -11.4% | PASS |  |  |
| BOTZ | T7w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.7% over 30 td | -1.7% over 30 td | PASS |  |  |
| BOTZ | T8r | word "rising" | not rising | not rising | PASS |  |  |
| BOTZ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BOTZ | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 27.8% below | PASS |  |  |
| BOTZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.55%, close location 0.07, OBV falling |
| BOTZ | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| BOTZ | V2 | day change of the last completed bar | down 3.5% | -3.55% | PASS |  |  |
| BOTZ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0727) | PASS |  |  |
| BOTZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BOTZ | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.2× from 2026-11-16 | 1.16× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| BOTZ | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.16× | 2026-11-16 1.16× | PASS |  |  |
| BOTZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.16× / 1.34× | 1.16× / 1.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BOTZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 816000) | 20 bars, last ('2026-11-16', 816000) | PASS |  |  |
| BRK-B | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $588.82 | $588.82 | PASS |  |  |
| BRK-B | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $563.75 | $563.75 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRK-B | E3 | percent from the 21-day average | 4.4% above | 4.4% above | PASS |  |  |
| BRK-B | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| BRK-B | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.52 | $9.52 (sr=9.5224) | PASS |  | Wilder ATR14 |
| BRK-B | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves above |
| BRK-B | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -6.6 | -6.6 | PASS |  |  |
| BRK-B | L-ema21 | ladder row ema21: price and gap = price vs average | $563.75, 4.4% | $563.75, 4.4% | PASS |  |  |
| BRK-B | L-note | "Last close $X · date" note = last completed bar | Last close $592.85 · Nov 16 | $592.85 · Nov 16 | PASS |  |  |
| BRK-B | L-now | ladder price row = compared price; name = the basis label | $588.82 "Now" | $588.82 "now" | PASS |  |  |
| BRK-B | L-sma200 | ladder row sma200: price and gap = price vs average | $501, 17.5% | $501.00, 17.5% | PASS |  |  |
| BRK-B | L-sma50 | ladder row sma50: price and gap = price vs average | $531.39, 10.8% | $531.39, 10.8% | PASS |  |  |
| BRK-B | S5-price | S5: the same live price reads the same on the header and the Entry block | header $588.82 / entry $588.82 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRK-B | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRK-B | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 80.8 | 80.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRK-B | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +16.5% vs +10.1% | 16.5% vs 10.1% | PASS |  |  |
| BRK-B | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRK-B | T4 | ADX 14 (S1 /api/sr meta.adx) | 54.3 | 54.3 | PASS |  | Wilder, completed bars |
| BRK-B | T4w | words "20 or more / below 20" | 20 or more | ADX 54.3 | PASS |  |  |
| BRK-B | T5 | "counted at the last close ($X, date)" = last completed bar | $592.85, Nov 16 | $592.85, Nov 16 | PASS |  |  |
| BRK-B | T6 | price vs 200-day average (S1 pattern sma values) | $592.85 vs $501.00 · +18.3% | $592.85 vs $501.00 · 18.3% | PASS |  |  |
| BRK-B | T6w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T7 | price vs 50-day average (S1 pattern sma values) | $592.85 vs $531.39 · +11.6% | $592.85 vs $531.39 · 11.6% | PASS |  |  |
| BRK-B | T7w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.7% over 30 td | +1.7% over 30 td | PASS |  |  |
| BRK-B | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRK-B | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRK-B | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 0.7% below $596.92 | 0.7% below $596.92 | PASS |  | closing high would be 592.94 |
| BRK-B | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 0.7% below | PASS |  |  |
| BRK-B | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $596.92 | $596.9199829101562 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRK-B | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| BRK-B | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| BRK-B | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.81× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| BRK-B | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.81× | 2026-11-16 0.81× | PASS |  |  |
| BRK-B | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.81× / 0.01× | 0.81× / 0.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRK-B | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3886800) | 20 bars, last ('2026-11-16', 3886800) | PASS |  |  |
| BRKU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.15 | $30.15 | PASS |  |  |
| BRKU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.03 | $28.03 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRKU | E3 | percent from the 21-day average | 7.6% above | 7.6% above | PASS |  |  |
| BRKU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| BRKU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.88 | $0.88 (sr=0.884) | PASS |  | Wilder ATR14 |
| BRKU | E5 | distance in normal day-moves | 2.4 | 2.4 | PASS |  | gauge dot note uses the same number:  · 2.4 day-moves above |
| BRKU | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.5 | -5.5 | PASS |  |  |
| BRKU | L-ema21 | ladder row ema21: price and gap = price vs average | $28.03, 7.6% | $28.03, 7.6% | PASS |  |  |
| BRKU | L-now | ladder price row = compared price; name = the basis label | $30.15 "Now" | $30.15 "now" | PASS |  |  |
| BRKU | L-sma200 | ladder row sma200: price and gap = price vs average | $23.16, 30.2% | $23.16, 30.2% | PASS |  |  |
| BRKU | L-sma50 | ladder row sma50: price and gap = price vs average | $25.11, 20.1% | $25.11, 20.1% | PASS |  |  |
| BRKU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $30.15 / entry $30.15 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRKU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRKU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 80.6 | 80.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRKU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +18.3% vs +10.1% | 18.3% vs 10.1% | PASS |  |  |
| BRKU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRKU | T4 | ADX 14 (S1 /api/sr meta.adx) | 52.7 | 52.7 | PASS |  | Wilder, completed bars |
| BRKU | T4w | words "20 or more / below 20" | 20 or more | ADX 52.7 | PASS |  |  |
| BRKU | T6 | price vs 200-day average (S1 pattern sma values) | $30.81 vs $23.16 · +33.0% | $30.81 vs $23.16 · 33.0% | PASS |  |  |
| BRKU | T6w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T7 | price vs 50-day average (S1 pattern sma values) | $30.81 vs $25.11 · +22.7% | $30.81 vs $25.11 · 22.7% | PASS |  |  |
| BRKU | T7w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.7% over 30 td | +1.7% over 30 td | PASS |  |  |
| BRKU | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRKU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRKU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.3% below $31.20 | 1.3% below $31.20 | PASS |  | closing high would be 30.81 |
| BRKU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.3% below | PASS |  |  |
| BRKU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $31.20 | $31.2 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRKU | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| BRKU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| BRKU | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.78× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| BRKU | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.78× | 2026-11-16 0.78× | PASS |  |  |
| BRKU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.78× / 0.01× | 0.78× / 0.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRKU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 69588) | 20 bars, last ('2026-11-16', 69588) | PASS |  |  |
| CAMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $94.99 | $94.99 | PASS |  |  |
| CAMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $112.65 | $112.65 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAMT | E3 | percent from the 21-day average | 15.7% below | 15.7% below | PASS |  |  |
| CAMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| CAMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.44 | $8.44 (sr=8.4392) | PASS |  | Wilder ATR14 |
| CAMT | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| CAMT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.0 | +5.0 | PASS |  |  |
| CAMT | L-ema21 | ladder row ema21: price and gap = price vs average | $112.65, -15.7% | $112.65, -15.7% | PASS |  |  |
| CAMT | L-note | "Last close $X · date" note = last completed bar | Last close $93.25 · Nov 16 | $93.25 · Nov 16 | PASS |  |  |
| CAMT | L-now | ladder price row = compared price; name = the basis label | $94.99 "Now" | $94.99 "now" | PASS |  |  |
| CAMT | L-sma200 | ladder row sma200: price and gap = price vs average | $155.09, -38.8% | $155.09, -38.8% | PASS |  |  |
| CAMT | L-sma50 | ladder row sma50: price and gap = price vs average | $132.76, -28.4% | $132.76, -28.4% | PASS |  |  |
| CAMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $94.99 / entry $94.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.8 | 32.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -3.1% vs +10.1% | -3.1% vs 10.1% | PASS |  |  |
| CAMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.5 | 33.5 | PASS |  | Wilder, completed bars |
| CAMT | T4w | words "20 or more / below 20" | 20 or more | ADX 33.5 | PASS |  |  |
| CAMT | T5 | "counted at the last close ($X, date)" = last completed bar | $93.25, Nov 16 | $93.25, Nov 16 | PASS |  |  |
| CAMT | T6 | price vs 200-day average (S1 pattern sma values) | $93.25 vs $155.09 · -39.9% | $93.25 vs $155.09 · -39.9% | PASS |  |  |
| CAMT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T7 | price vs 50-day average (S1 pattern sma values) | $93.25 vs $132.76 · -29.8% | $93.25 vs $132.76 · -29.8% | PASS |  |  |
| CAMT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.6% over 30 td | -0.5% over 30 td | PASS |  |  |
| CAMT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CAMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 56.8% below $215.99 | 56.8% below $215.99 | PASS |  | closing high would be 207.46 |
| CAMT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 56.8% below | PASS |  |  |
| CAMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $215.99 | $215.99001 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -8.34%, close location 0.20, OBV falling |
| CAMT | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CAMT | V2 | day change of the last completed bar | down 8.3% | -8.34% | PASS |  |  |
| CAMT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.20 (raw 0.2028) | PASS |  |  |
| CAMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAMT | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 1.04× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CAMT | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.04× | 2026-11-16 1.04× | PASS |  |  |
| CAMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.04× / 0.92× | 1.04× / 0.92× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 536800) | 20 bars, last ('2026-11-16', 536800) | PASS |  |  |
| CARS.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $19.88 | $19.88 | PASS |  |  |
| CARS.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $22.01 | $22.01 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CARS.TO | E3 | percent from the 21-day average | 9.7% below | 9.7% below | PASS |  |  |
| CARS.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 3:41pm ET) | session=regular | PASS |  |  |
| CARS.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.52 | $0.52 (sr=0.5215) | PASS |  | Wilder ATR14 |
| CARS.TO | E5 | distance in normal day-moves | 4.1 | 4.1 | PASS |  | gauge dot note uses the same number:  · 4.1 day-moves below |
| CARS.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| CARS.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +11.5 | +11.5 | PASS |  |  |
| CARS.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $22.01, -9.7% | $22.01, -9.7% | PASS |  |  |
| CARS.TO | L-note | "Last close $X · date" note = last completed bar | Last close $20.19 · Nov 16 | $20.19 · Nov 16 | PASS |  |  |
| CARS.TO | L-now | ladder price row = compared price; name = the basis label | $19.88 "Last trade 3:41pm ET" | $19.88 "last trade 3:41pm et" | PASS |  |  |
| CARS.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $28, -29.0% | $28.00, -29.0% | PASS |  |  |
| CARS.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $23.93, -16.9% | $23.93, -16.9% | PASS |  |  |
| CARS.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $19.88 / entry $19.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CARS.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CARS.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.5 | 32.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CARS.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -24.7% vs +10.1% | -24.7% vs 10.1% | PASS |  |  |
| CARS.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CARS.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.9 | PASS |  |  |
| CARS.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $20.19, Nov 16 | $20.19, Nov 16 | PASS |  |  |
| CARS.TO | T6 | price vs 200-day average (S1 pattern sma values) | $20.19 vs $28.00 · -27.9% | $20.19 vs $28.00 · -27.9% | PASS |  |  |
| CARS.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CARS.TO | T7 | price vs 50-day average (S1 pattern sma values) | $20.19 vs $23.93 · -15.6% | $20.19 vs $23.93 · -15.6% | PASS |  |  |
| CARS.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CARS.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.3% over 30 td | -2.3% over 30 td | PASS |  |  |
| CARS.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CARS.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CARS.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 47.1% below $38.16 | 47.1% below $38.16 | PASS |  | closing high would be 38.16 |
| CARS.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 47.1% below | PASS |  |  |
| CARS.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.16 | $38.15896987915039 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CARS.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 11 of 50 days empty | 11 of 50 days empty | PASS |  |  |
| CAT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $568.36 | $568.36 | PASS |  |  |
| CAT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $639.06 | $639.06 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAT | E3 | percent from the 21-day average | 11.1% below | 11.1% below | PASS |  |  |
| CAT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| CAT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $29.30 | $29.30 (sr=29.3033) | PASS |  | Wilder ATR14 |
| CAT | E5 | distance in normal day-moves | 2.4 | 2.4 | PASS |  | gauge dot note uses the same number:  · 2.4 day-moves below |
| CAT | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.3 | +3.3 | PASS |  |  |
| CAT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.7 | +5.7 | PASS |  |  |
| CAT | L-ema21 | ladder row ema21: price and gap = price vs average | $639.06, -11.1% | $639.06, -11.1% | PASS |  |  |
| CAT | L-note | "Last close $X · date" note = last completed bar | Last close $570.49 · Nov 16 | $570.49 · Nov 16 | PASS |  |  |
| CAT | L-now | ladder price row = compared price; name = the basis label | $568.36 "Now" | $568.36 "now" | PASS |  |  |
| CAT | L-sma200 | ladder row sma200: price and gap = price vs average | $807, -29.6% | $807.00, -29.6% | PASS |  |  |
| CAT | L-sma50 | ladder row sma50: price and gap = price vs average | $735.9, -22.8% | $735.90, -22.8% | PASS |  |  |
| CAT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $568.36 / entry $568.36 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.3 | 31.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.0% vs +10.1% | 3.0% vs 10.1% | PASS |  |  |
| CAT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAT | T4 | ADX 14 (S1 /api/sr meta.adx) | 39.4 | 39.4 | PASS |  | Wilder, completed bars |
| CAT | T4w | words "20 or more / below 20" | 20 or more | ADX 39.4 | PASS |  |  |
| CAT | T5 | "counted at the last close ($X, date)" = last completed bar | $570.49, Nov 16 | $570.49, Nov 16 | PASS |  |  |
| CAT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.4% over 30 td | +1.3% over 30 td | PASS |  |  |
| CAT | T8r | word "rising" | still rising | rising | PASS |  |  |
| CAT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 46.9% below | PASS |  |  |
| CAT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.95%, close location 0.09, OBV falling |
| CAT | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CAT | V2 | day change of the last completed bar | down 5.0% | -4.95% | PASS |  |  |
| CAT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0943) | PASS |  |  |
| CAT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAT | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.09× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CAT | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.09× | 2026-11-16 1.09× | PASS |  |  |
| CAT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.09× / 0.96× | 1.09× / 0.96× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3319300) | 20 bars, last ('2026-11-16', 3319300) | PASS |  |  |
| CCO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $94.40 | $94.40 | PASS |  |  |
| CCO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $106.82 | $106.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CCO.TO | E3 | percent from the 21-day average | 11.6% below | 11.6% below | PASS |  |  |
| CCO.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| CCO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.12 | $5.12 (sr=5.116) | PASS |  | Wilder ATR14 |
| CCO.TO | E5 | distance in normal day-moves | 2.4 | 2.4 | PASS |  | gauge dot note uses the same number:  · 2.4 day-moves below |
| CCO.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.7 | +6.7 | PASS |  |  |
| CCO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $106.82, -11.6% | $106.82, -11.6% | PASS |  |  |
| CCO.TO | L-now | ladder price row = compared price; name = the basis label | $94.4 "Last close" | $94.40 "last close" | PASS |  |  |
| CCO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $141.27, -33.2% | $141.27, -33.2% | PASS |  |  |
| CCO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $118.7, -20.5% | $118.70, -20.5% | PASS |  |  |
| CCO.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CCO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.8 | 32.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CCO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -20.4% vs +10.1% | -20.4% vs 10.1% | PASS |  |  |
| CCO.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CCO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.1 | 28.1 | PASS |  | Wilder, completed bars |
| CCO.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.1 | PASS |  |  |
| CCO.TO | T6 | price vs 200-day average (S1 pattern sma values) | $94.40 vs $141.27 · -33.2% | $94.40 vs $141.27 · -33.2% | PASS |  |  |
| CCO.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CCO.TO | T7 | price vs 50-day average (S1 pattern sma values) | $94.40 vs $118.70 · -20.5% | $94.40 vs $118.70 · -20.5% | PASS |  |  |
| CCO.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CCO.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.6% over 30 td | -3.6% over 30 td | PASS |  |  |
| CCO.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CCO.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CCO.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 48.3% below $182.72 | 48.3% below $182.72 | PASS |  | closing high would be 181.66 |
| CCO.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 48.3% below | PASS |  |  |
| CCO.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $182.72 | $182.72000122070312 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CCO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.35%, close location 0.06, OBV falling |
| CCO.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CCO.TO | V2 | day change of the last completed bar | down 6.3% | -6.35% | PASS |  |  |
| CCO.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0624) | PASS |  |  |
| CCO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CCO.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.15× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CCO.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.15× | 2026-11-16 1.15× | PASS |  |  |
| CCO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.15× / 1.17× | 1.15× / 1.17× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CCO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1393600) | 20 bars, last ('2026-11-16', 1393600) | PASS |  |  |
| CEG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $267.69 | $267.69 | PASS |  |  |
| CEG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $267.68 | $267.68 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CEG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| CEG | L-ema21 | ladder row ema21: price and gap = price vs average | $267.68, 0.0% | $267.68, 0.0% | PASS |  |  |
| CEG | L-note | "Last close $X · date" note = last completed bar | Last close $277.82 · Nov 16 | $277.82 · Nov 16 | PASS |  |  |
| CEG | L-now | ladder price row = compared price; name = the basis label | $267.69 "Now" | $267.69 "now" | PASS |  |  |
| CEG | L-sma200 | ladder row sma200: price and gap = price vs average | $278.39, -3.8% | $278.39, -3.8% | PASS |  |  |
| CEG | L-sma50 | ladder row sma50: price and gap = price vs average | $269.08, -0.5% | $269.08, -0.5% | PASS |  |  |
| CEG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $267.69 / entry $267.69 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CEG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CEG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.2 | 55.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CEG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -17.9% vs +10.1% | -17.9% vs 10.1% | PASS |  |  |
| CEG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CEG | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.5 | 14.5 | PASS |  | Wilder, completed bars |
| CEG | T4w | words "20 or more / below 20" | below 20 | ADX 14.5 | PASS |  |  |
| CEG | T5 | "counted at the last close ($X, date)" = last completed bar | $277.82, Nov 16 | $277.82, Nov 16 | PASS |  |  |
| CEG | T6 | price vs 200-day average (S1 pattern sma values) | $277.82 vs $278.39 · -0.2% | $277.82 vs $278.39 · -0.2% | PASS |  |  |
| CEG | T6w | word "Below" | Below | Below | PASS |  |  |
| CEG | T7 | price vs 50-day average (S1 pattern sma values) | $277.82 vs $269.08 · +3.2% | $277.82 vs $269.08 · 3.2% | PASS |  |  |
| CEG | T7w | word "Above" | Above | Above | PASS |  |  |
| CEG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.1% over 30 td | -3.1% over 30 td | PASS |  |  |
| CEG | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CEG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CEG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 27.0% below $380.78 | 27.0% below $380.78 | PASS |  | closing high would be 378.60 |
| CEG | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 27.0% below | PASS |  |  |
| CEG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $380.78 | $380.78 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CEG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.85%, close location 0.63, OBV falling |
| CEG | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CEG | V2 | day change of the last completed bar | down 0.8% | -0.85% | PASS |  |  |
| CEG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CEG | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-16 | 0.94× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CEG | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.94× | 2026-11-16 0.94× | PASS |  |  |
| CEG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.94× / 0.18× | 0.94× / 0.18× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CEG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3580622) | 20 bars, last ('2026-11-16', 3580622) | PASS |  |  |
| CGY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $84.10 | $84.10 | PASS |  |  |
| CGY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $85.41 | $85.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CGY.TO | E3 | percent from the 21-day average | 1.5% below | 1.5% below | PASS |  |  |
| CGY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| CGY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.55 | $2.55 (sr=2.5511) | PASS |  | Wilder ATR14 |
| CGY.TO | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves below |
| CGY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $85.41, -1.5% | $85.41, -1.5% | PASS |  |  |
| CGY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $86.08 · Nov 16 | $86.08 · Nov 16 | PASS |  |  |
| CGY.TO | L-now | ladder price row = compared price; name = the basis label | $84.1 "Now" | $84.10 "now" | PASS |  |  |
| CGY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $78.74, 6.8% | $78.74, 6.8% | PASS |  |  |
| CGY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $83.27, 1.0% | $83.27, 1.0% | PASS |  |  |
| CGY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $84.10 / entry $84.10 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CGY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CGY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.0 | 53.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CGY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +69.8% vs +10.1% | 69.7% vs 10.1% | PASS |  |  |
| CGY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CGY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.9 | 16.9 | PASS |  | Wilder, completed bars |
| CGY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 16.9 | PASS |  |  |
| CGY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $86.08, Nov 16 | $86.08, Nov 16 | PASS |  |  |
| CGY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $86.08 vs $78.74 · +9.3% | $86.08 vs $78.74 · 9.3% | PASS |  |  |
| CGY.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CGY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $86.08 vs $83.27 · +3.4% | $86.08 vs $83.27 · 3.4% | PASS |  |  |
| CGY.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CGY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.2% over 30 td | +5.2% over 30 td | PASS |  |  |
| CGY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CGY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CGY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 9.5% below $95.15 | 9.5% below $95.15 | PASS |  | closing high would be 91.80 |
| CGY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 9.5% below | PASS |  |  |
| CGY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $95.15 | $95.15474299571112 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CGY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.62%, close location 0.91, OBV falling |
| CGY.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CGY.TO | V2 | day change of the last completed bar | up 0.6% | +0.62% | PASS |  |  |
| CGY.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.91 (raw 0.9124) | PASS |  |  |
| CGY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CGY.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.7× from 2026-11-16 | 0.65× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CGY.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.65× | 2026-11-16 0.65× | PASS |  |  |
| CGY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.65× / 0.21× | 0.65× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CGY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 19900) | 20 bars, last ('2026-11-16', 19900) | PASS |  |  |
| CNQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $68.27 | $68.27 | PASS |  |  |
| CNQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $71.47 | $71.47 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNQ.TO | E3 | percent from the 21-day average | 4.5% below | 4.5% below | PASS |  |  |
| CNQ.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| CNQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.95 | $1.95 (sr=1.9481) | PASS |  | Wilder ATR14 |
| CNQ.TO | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| CNQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $71.47, -4.5% | $71.47, -4.5% | PASS |  |  |
| CNQ.TO | L-note | "Last close $X · date" note = last completed bar | Last close $68.96 · Nov 16 | $68.96 · Nov 16 | PASS |  |  |
| CNQ.TO | L-now | ladder price row = compared price; name = the basis label | $68.27 "Now" | $68.27 "now" | PASS |  |  |
| CNQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.04, 6.6% | $64.04, 6.6% | PASS |  |  |
| CNQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $71.16, -4.1% | $71.16, -4.1% | PASS |  |  |
| CNQ.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $68.27 / entry $68.27 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CNQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.0 | 41.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +53.4% vs +10.1% | 53.4% vs 10.1% | PASS |  |  |
| CNQ.TO | T3w | words "past year" vs the window used | 250 / 251 bars back | 250-253 bars | PASS |  |  |
| CNQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.7 | 28.7 | PASS |  | Wilder, completed bars |
| CNQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.7 | PASS |  |  |
| CNQ.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $68.96, Nov 16 | $68.96, Nov 16 | PASS |  |  |
| CNQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $68.96 vs $64.04 · +7.7% | $68.96 vs $64.04 · 7.7% | PASS |  |  |
| CNQ.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CNQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $68.96 vs $71.16 · -3.1% | $68.96 vs $71.16 · -3.1% | PASS |  |  |
| CNQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CNQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.9% over 30 td | +6.9% over 30 td | PASS |  |  |
| CNQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.3% below $78.60 | 12.3% below $78.60 | PASS |  | closing high would be 78.42 |
| CNQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.3% below | PASS |  |  |
| CNQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $78.60 | $78.5999984741211 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.75%, close location 0.22, OBV falling |
| CNQ.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CNQ.TO | V2 | day change of the last completed bar | down 2.8% | -2.75% | PASS |  |  |
| CNQ.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2174) | PASS |  |  |
| CNQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CNQ.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.4× from 2026-11-16 | 1.37× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CNQ.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.37× | 2026-11-16 1.37× | PASS |  |  |
| CNQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.37× / 0.97× | 1.37× / 0.97× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 17652300) | 20 bars, last ('2026-11-16', 17652300) | PASS |  |  |
| CNR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $180.62 | $180.62 | PASS |  |  |
| CNR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $177.14 | $177.14 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNR.TO | E3 | percent from the 21-day average | 2.0% above | 2.0% above | PASS |  |  |
| CNR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| CNR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.37 | $3.37 (sr=3.3694) | PASS |  | Wilder ATR14 |
| CNR.TO | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves above |
| CNR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $177.14, 2.0% | $177.14, 2.0% | PASS |  |  |
| CNR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $182.77 · Nov 16 | $182.77 · Nov 16 | PASS |  |  |
| CNR.TO | L-now | ladder price row = compared price; name = the basis label | $180.62 "Now" | $180.62 "now" | PASS |  |  |
| CNR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $161.47, 11.9% | $161.47, 11.9% | PASS |  |  |
| CNR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $172.06, 5.0% | $172.06, 5.0% | PASS |  |  |
| CNR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $180.62 / entry $180.62 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CNR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 64.5 | 64.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +38.8% vs +10.1% | 38.8% vs 10.1% | PASS |  |  |
| CNR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.9 | 23.9 | PASS |  | Wilder, completed bars |
| CNR.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 23.9 | PASS |  |  |
| CNR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $182.77, Nov 16 | $182.77, Nov 16 | PASS |  |  |
| CNR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $182.77 vs $161.47 · +13.2% | $182.77 vs $161.47 · 13.2% | PASS |  |  |
| CNR.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $182.77 vs $172.06 · +6.2% | $182.77 vs $172.06 · 6.2% | PASS |  |  |
| CNR.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.9% over 30 td | +3.9% over 30 td | PASS |  |  |
| CNR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 0.8% below $184.26 | 0.8% below $184.26 | PASS |  | closing high would be 182.93 |
| CNR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 0.8% below | PASS |  |  |
| CNR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $184.26 | $184.25630798377267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.82%, close location 0.65, OBV rising |
| CNR.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CNR.TO | V2 | day change of the last completed bar | up 0.8% | +0.82% | PASS |  |  |
| CNR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| CNR.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.2× from 2026-11-16 | 1.19× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CNR.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.19× | 2026-11-16 1.19× | PASS |  |  |
| CNR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.19× / 0.44× | 1.19× / 0.44× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1474400) | 20 bars, last ('2026-11-16', 1474400) | PASS |  |  |
| COP | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $139.46 | $139.46 | PASS |  |  |
| COP | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $140.64 | $140.64 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COP | E3 | percent from the 21-day average | 0.8% below | 0.8% below | PASS |  |  |
| COP | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| COP | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.93 | $3.93 (sr=3.9297) | PASS |  | Wilder ATR14 |
| COP | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| COP | L-ema21 | ladder row ema21: price and gap = price vs average | $140.64, -0.8% | $140.64, -0.8% | PASS |  |  |
| COP | L-note | "Last close $X · date" note = last completed bar | Last close $140.52 · Nov 16 | $140.52 · Nov 16 | PASS |  |  |
| COP | L-now | ladder price row = compared price; name = the basis label | $139.46 "Now" | $139.46 "now" | PASS |  |  |
| COP | L-sma200 | ladder row sma200: price and gap = price vs average | $123.5, 12.9% | $123.50, 12.9% | PASS |  |  |
| COP | L-sma50 | ladder row sma50: price and gap = price vs average | $137.41, 1.5% | $137.41, 1.5% | PASS |  |  |
| COP | S5-price | S5: the same live price reads the same on the header and the Entry block | header $139.46 / entry $139.46 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COP | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COP | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.5 | 50.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COP | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +53.8% vs +10.1% | 53.8% vs 10.1% | PASS |  |  |
| COP | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COP | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.5 | 25.5 | PASS |  | Wilder, completed bars |
| COP | T4w | words "20 or more / below 20" | 20 or more | ADX 25.5 | PASS |  |  |
| COP | T5 | "counted at the last close ($X, date)" = last completed bar | $140.52, Nov 16 | $140.52, Nov 16 | PASS |  |  |
| COP | T6w | word "Above" | Above | Above | PASS |  |  |
| COP | T7w | word "Above" | Above | Above | PASS |  |  |
| COP | T8r | word "rising" | still rising | rising | PASS |  |  |
| COP | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COP | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.9% below | PASS |  |  |
| COP | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.24%, close location 0.70, OBV falling |
| COP | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COP | V2 | day change of the last completed bar | down 1.2% | -1.24% | PASS |  |  |
| COP | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COP | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.4× from 2026-11-16 | 1.38× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| COP | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.38× | 2026-11-16 1.38× | PASS |  |  |
| COP | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.38× / 0.44× | 1.38× / 0.44× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COP | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 9387600) | 20 bars, last ('2026-11-16', 9387600) | PASS |  |  |
| COPP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $46.32 | $46.32 | PASS |  |  |
| COPP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $52.65 | $52.65 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPP.TO | E3 | percent from the 21-day average | 12.0% below | 12.0% below | PASS |  |  |
| COPP.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| COPP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.09 | $2.09 (sr=2.0921) | PASS |  | Wilder ATR14 |
| COPP.TO | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| COPP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $52.65, -12.0% | $52.65, -12.0% | PASS |  |  |
| COPP.TO | L-note | "Last close $X · date" note = last completed bar | Last close $46.48 · Nov 16 | $46.48 · Nov 16 | PASS |  |  |
| COPP.TO | L-now | ladder price row = compared price; name = the basis label | $46.32 "Now" | $46.32 "now" | PASS |  |  |
| COPP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.7, -21.1% | $58.70, -21.1% | PASS |  |  |
| COPP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $57.65, -19.7% | $57.65, -19.7% | PASS |  |  |
| COPP.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $46.32 / entry $46.32 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.9 | 31.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.1% vs +10.1% | 4.1% vs 10.1% | PASS |  |  |
| COPP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.8 | 28.8 | PASS |  | Wilder, completed bars |
| COPP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.8 | PASS |  |  |
| COPP.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $46.48, Nov 16 | $46.48, Nov 16 | PASS |  |  |
| COPP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $46.48 vs $58.70 · -20.8% | $46.48 vs $58.70 · -20.8% | PASS |  |  |
| COPP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $46.48 vs $57.66 · -19.4% | $46.48 vs $57.65 · -19.4% | PASS |  |  |
| COPP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.5% over 30 td | -0.5% over 30 td | PASS |  |  |
| COPP.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.1% below $70.54 | 34.1% below $70.54 | PASS |  | closing high would be 68.98 |
| COPP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.1% below | PASS |  |  |
| COPP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $70.54 | $70.54000091552734 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.14%, close location 0.03, OBV falling |
| COPP.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COPP.TO | V2 | day change of the last completed bar | down 6.1% | -6.14% | PASS |  |  |
| COPP.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0306) | PASS |  |  |
| COPP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPP.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 2.2× from 2026-11-16 | 2.22× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| COPP.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 2.22× | 2026-11-16 2.22× | PASS |  |  |
| COPP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.22× / 1.36× | 2.22× / 1.36× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 31800) | 20 bars, last ('2026-11-16', 31800) | PASS |  |  |
| COPP.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.22, OBV falling | condition true | PASS |  |  |
| COPX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $65.17 | $65.17 | PASS |  |  |
| COPX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.88 | $73.88 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPX | E3 | percent from the 21-day average | 11.8% below | 11.8% below | PASS |  |  |
| COPX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| COPX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.82 | $2.82 (sr=2.8171) | PASS |  | Wilder ATR14 |
| COPX | E5 | distance in normal day-moves | 3.1 | 3.1 | PASS |  | gauge dot note uses the same number:  · 3.1 day-moves below |
| COPX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| COPX | L-ema21 | ladder row ema21: price and gap = price vs average | $73.88, -11.8% | $73.88, -11.8% | PASS |  |  |
| COPX | L-note | "Last close $X · date" note = last completed bar | Last close $65.51 · Nov 16 | $65.51 · Nov 16 | PASS |  |  |
| COPX | L-now | ladder price row = compared price; name = the basis label | $65.17 "Now" | $65.17 "now" | PASS |  |  |
| COPX | L-sma200 | ladder row sma200: price and gap = price vs average | $82.65, -21.1% | $82.65, -21.1% | PASS |  |  |
| COPX | L-sma50 | ladder row sma50: price and gap = price vs average | $80.78, -19.3% | $80.78, -19.3% | PASS |  |  |
| COPX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $65.17 / entry $65.17 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.4 | 31.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +7.1% vs +10.1% | 7.1% vs 10.1% | PASS |  |  |
| COPX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPX | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.0 | 24.0 | PASS |  | Wilder, completed bars |
| COPX | T4w | words "20 or more / below 20" | 20 or more | ADX 24.0 | PASS |  |  |
| COPX | T5 | "counted at the last close ($X, date)" = last completed bar | $65.51, Nov 16 | $65.51, Nov 16 | PASS |  |  |
| COPX | T6 | price vs 200-day average (S1 pattern sma values) | $65.51 vs $82.65 · -20.7% | $65.51 vs $82.65 · -20.7% | PASS |  |  |
| COPX | T6w | word "Below" | Below | Below | PASS |  |  |
| COPX | T7 | price vs 50-day average (S1 pattern sma values) | $65.51 vs $80.78 · -18.9% | $65.51 vs $80.78 · -18.9% | PASS |  |  |
| COPX | T7w | word "Below" | Below | Below | PASS |  |  |
| COPX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.4% over 30 td | -0.4% over 30 td | PASS |  |  |
| COPX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.5% below $99.99 | 34.5% below $99.99 | PASS |  | closing high would be 96.45 |
| COPX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.5% below | PASS |  |  |
| COPX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $99.99 | $99.99 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.37%, close location 0.05, OBV falling |
| COPX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COPX | V2 | day change of the last completed bar | down 5.4% | -5.37% | PASS |  |  |
| COPX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0500) | PASS |  |  |
| COPX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 2.7× from 2026-11-16 | 2.69× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| COPX | V6 | Volume detail: last session date and RVOL | 2026-11-16 2.69× | 2026-11-16 2.69× | PASS |  |  |
| COPX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.69× / 1.25× | 2.69× / 1.25× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 7441396) | 20 bars, last ('2026-11-16', 7441396) | PASS |  |  |
| COPX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.69, OBV falling | condition true | PASS |  |  |
| COPZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $8.61 | $8.61 | PASS |  |  |
| COPZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $11.34 | $11.34 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPZ | E3 | percent from the 21-day average | 24.1% below | 24.1% below | PASS |  |  |
| COPZ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 3:48pm ET) | session=regular | PASS |  |  |
| COPZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.82 | $0.82 (sr=0.82) | PASS |  | Wilder ATR14 |
| COPZ | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| COPZ | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| COPZ | L-ema21 | ladder row ema21: price and gap = price vs average | $11.34, -24.1% | $11.34, -24.1% | PASS |  |  |
| COPZ | L-note | "Last close $X · date" note = last completed bar | Last close $8.68 · Nov 16 | $8.68 · Nov 16 | PASS |  |  |
| COPZ | L-now | ladder price row = compared price; name = the basis label | $8.61 "Last trade 3:48pm ET" | $8.61 "last trade 3:48pm et" | PASS |  |  |
| COPZ | L-sma50 | ladder row sma50: price and gap = price vs average | $13.9, -38.1% | $13.90, -38.1% | PASS |  |  |
| COPZ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $8.61 / entry $8.61 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.8 | 30.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.5 | 25.5 | PASS |  | Wilder, completed bars |
| COPZ | T4w | words "20 or more / below 20" | 20 or more | ADX 25.5 | PASS |  |  |
| COPZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.97%, close location 0.00, OBV falling |
| COPZ | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COPZ | V2 | day change of the last completed bar | down 11.0% | -10.97% | PASS |  |  |
| COPZ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| COPZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPZ | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.6× from 2026-11-16 | 0.63× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| COPZ | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.63× | 2026-11-16 0.63× | PASS |  |  |
| COPZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.63× / 1.16× | 0.63× / 1.16× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 8124) | 20 bars, last ('2026-11-16', 8124) | PASS |  |  |
| COST | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,110.90 | $1,110.90 | PASS |  |  |
| COST | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1042.17 | $1042.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COST | E3 | percent from the 21-day average | 6.6% above | 6.6% above | PASS |  |  |
| COST | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| COST | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $19.04 | $19.04 (sr=19.0434) | PASS |  | Wilder ATR14 |
| COST | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  ▸ · 3.6 day-moves above |
| COST | L-ema21 | ladder row ema21: price and gap = price vs average | $1042.17, 6.6% | $1042.17, 6.6% | PASS |  |  |
| COST | L-now | ladder price row = compared price; name = the basis label | $1110.9 "Now" | $1110.90 "now" | PASS |  |  |
| COST | L-sma200 | ladder row sma200: price and gap = price vs average | $976.55, 13.8% | $976.55, 13.8% | PASS |  |  |
| COST | L-sma50 | ladder row sma50: price and gap = price vs average | $971.08, 14.4% | $971.08, 14.4% | PASS |  |  |
| COST | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,110.90 / entry $1,110.90 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COST | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COST | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 77.1 | 77.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COST | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +20.7% vs +10.1% | 20.7% vs 10.1% | PASS |  |  |
| COST | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COST | T4 | ADX 14 (S1 /api/sr meta.adx) | 52.1 | 52.1 | PASS |  | Wilder, completed bars |
| COST | T4w | words "20 or more / below 20" | 20 or more | ADX 52.1 | PASS |  |  |
| COST | T5 | "counted at the last close ($X, date)" = last completed bar | $1,113.74, Nov 16 | $1113.74, Nov 16 | PASS |  |  |
| COST | T6 | price vs 200-day average (S1 pattern sma values) | $1,113.74 vs $976.55 · +14.0% | $1113.74 vs $976.55 · 14.0% | PASS |  |  |
| COST | T6w | word "Above" | Above | Above | PASS |  |  |
| COST | T7 | price vs 50-day average (S1 pattern sma values) | $1,113.74 vs $971.08 · +14.7% | $1113.74 vs $971.08 · 14.7% | PASS |  |  |
| COST | T7w | word "Above" | Above | Above | PASS |  |  |
| COST | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| COST | T8r | word "rising" | still rising | rising | PASS |  |  |
| COST | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COST | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 0.3% below $1,117.00 | 0.3% below $1117.00 | PASS |  | closing high would be 1113.74 |
| COST | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 0.3% below | PASS |  |  |
| COST | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,117.00 | $1117 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COST | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.68%, close location 0.73, OBV rising |
| COST | V2 | day change of the last completed bar | up 0.7% | +0.68% | PASS |  |  |
| COST | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COST | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-16 | 1.30× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| COST | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.30× | 2026-11-16 1.30× | PASS |  |  |
| COST | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.30× / 0.40× | 1.30× / 0.40× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COST | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3044300) | 20 bars, last ('2026-11-16', 3044300) | PASS |  |  |
| COTG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $16.95 | $16.95 | PASS |  |  |
| COTG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $15.05 | $15.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COTG | E3 | percent from the 21-day average | 12.6% above | 12.6% above | PASS |  |  |
| COTG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| COTG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.52 | $0.52 (sr=0.5237) | PASS |  | Wilder ATR14 |
| COTG | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  ▸ · 3.6 day-moves above |
| COTG | L-ema21 | ladder row ema21: price and gap = price vs average | $15.05, 12.6% | $15.05, 12.6% | PASS |  |  |
| COTG | L-now | ladder price row = compared price; name = the basis label | $16.95 "Now" | $16.95 "now" | PASS |  |  |
| COTG | L-sma200 | ladder row sma200: price and gap = price vs average | $13.9, 21.9% | $13.90, 21.9% | PASS |  |  |
| COTG | L-sma50 | ladder row sma50: price and gap = price vs average | $13.19, 28.5% | $13.19, 28.5% | PASS |  |  |
| COTG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $16.95 / entry $16.95 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COTG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COTG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 75.5 | 75.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COTG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +26.1% vs +10.1% | 26.1% vs 10.1% | PASS |  |  |
| COTG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COTG | T4 | ADX 14 (S1 /api/sr meta.adx) | 51.1 | 51.0 | PASS |  | Wilder, completed bars |
| COTG | T4w | words "20 or more / below 20" | 20 or more | ADX 51.0 | PASS |  |  |
| COTG | T6 | price vs 200-day average (S1 pattern sma values) | $17.04 vs $13.90 · +22.6% | $17.04 vs $13.90 · 22.6% | PASS |  |  |
| COTG | T6w | word "Above" | Above | Above | PASS |  |  |
| COTG | T7 | price vs 50-day average (S1 pattern sma values) | $17.04 vs $13.19 · +29.2% | $17.04 vs $13.19 · 29.2% | PASS |  |  |
| COTG | T7w | word "Above" | Above | Above | PASS |  |  |
| COTG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.4% over 30 td | +1.4% over 30 td | PASS |  |  |
| COTG | T8r | word "rising" | still rising | rising | PASS |  |  |
| COTG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COTG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.3% below $17.80 | 4.3% below $17.80 | PASS |  | closing high would be 17.70 |
| COTG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.3% below | PASS |  |  |
| COTG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $17.80 | $17.8026 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COTG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 1.19%, close location 0.82, OBV rising |
| COTG | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| COTG | V2 | day change of the last completed bar | up 1.2% | +1.19% | PASS |  |  |
| COTG | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.82 (raw 0.8214) | PASS |  |  |
| COTG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COTG | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.5× from 2026-11-16 | 0.53× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| COTG | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.52× | 2026-11-16 0.53× | PASS |  |  |
| COTG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.52× / 0.40× | 0.53× / 0.39× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COTG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 57477) | 20 bars, last ('2026-11-16', 57477) | PASS |  |  |
| CSU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3,330.81 | $3,330.81 | PASS |  |  |
| CSU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3372.93 | $3372.93 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CSU.TO | E3 | percent from the 21-day average | 1.2% below | 1.2% below | PASS |  |  |
| CSU.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| CSU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $119.22 | $119.22 (sr=119.2161) | PASS |  | Wilder ATR14 |
| CSU.TO | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| CSU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $3372.93, -1.2% | $3372.93, -1.2% | PASS |  |  |
| CSU.TO | L-now | ladder price row = compared price; name = the basis label | $3330.81 "Now" | $3330.81 "now" | PASS |  |  |
| CSU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $2808.81, 18.6% | $2808.81, 18.6% | PASS |  |  |
| CSU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $3120.14, 6.8% | $3120.14, 6.8% | PASS |  |  |
| CSU.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3,330.81 / entry $3,330.81 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CSU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 58.8 | 58.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CSU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.1% vs +10.1% | 6.1% vs 10.1% | PASS |  |  |
| CSU.TO | T3w | words "past year" vs the window used | 250 / 251 bars back | 250-253 bars | PASS |  |  |
| CSU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.1 | 34.1 | PASS |  | Wilder, completed bars |
| CSU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 34.1 | PASS |  |  |
| CSU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -1.60%, close location 0.25, OBV rising |
| CSU.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CSU.TO | V2 | day change of the last completed bar | down 1.6% | -1.60% | PASS |  |  |
| CSU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| CSU.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.77× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CSU.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.77× | 2026-11-16 0.77× | PASS |  |  |
| CSU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.77× / 0.46× | 0.77× / 0.46× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CSU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 47400) | 20 bars, last ('2026-11-16', 47400) | PASS |  |  |
| CVX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $216.24 | $216.24 | PASS |  |  |
| CVX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $218.68 | $218.68 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CVX | E3 | percent from the 21-day average | 1.1% below | 1.1% below | PASS |  |  |
| CVX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| CVX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.91 | $4.91 (sr=4.9077) | PASS |  | Wilder ATR14 |
| CVX | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves below |
| CVX | L-ema21 | ladder row ema21: price and gap = price vs average | $218.68, -1.1% | $218.68, -1.1% | PASS |  |  |
| CVX | L-note | "Last close $X · date" note = last completed bar | Last close $217.14 · Nov 16 | $217.14 · Nov 16 | PASS |  |  |
| CVX | L-now | ladder price row = compared price; name = the basis label | $216.24 "Now" | $216.24 "now" | PASS |  |  |
| CVX | L-sma200 | ladder row sma200: price and gap = price vs average | $194.16, 11.4% | $194.16, 11.4% | PASS |  |  |
| CVX | L-sma50 | ladder row sma50: price and gap = price vs average | $215.65, 0.3% | $215.65, 0.3% | PASS |  |  |
| CVX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $216.24 / entry $216.24 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CVX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CVX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.4 | 48.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CVX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +43.2% vs +10.1% | 43.2% vs 10.1% | PASS |  |  |
| CVX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CVX | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.2 | 26.2 | PASS |  | Wilder, completed bars |
| CVX | T4w | words "20 or more / below 20" | 20 or more | ADX 26.2 | PASS |  |  |
| CVX | T5 | "counted at the last close ($X, date)" = last completed bar | $217.14, Nov 16 | $217.14, Nov 16 | PASS |  |  |
| CVX | T6w | word "Above" | Above | Above | PASS |  |  |
| CVX | T7 | price vs 50-day average (S1 pattern sma values) | $217.14 vs $215.65 · +0.7% | $217.14 vs $215.65 · 0.7% | PASS |  |  |
| CVX | T7w | word "Above" | Above | Above | PASS |  |  |
| CVX | T8r | word "rising" | still rising | rising | PASS |  |  |
| CVX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CVX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.2% below $236.48 | 8.2% below $236.48 | PASS |  | closing high would be 235.52 |
| CVX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.2% below | PASS |  |  |
| CVX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $236.48 | $236.47999572753906 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CVX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.25%, close location 0.17, OBV flat |
| CVX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| CVX | V2 | day change of the last completed bar | down 1.3% | -1.25% | PASS |  |  |
| CVX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1719) | PASS |  |  |
| CVX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| CVX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.7× from 2026-11-16 | 0.71× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| CVX | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.71× | 2026-11-16 0.71× | PASS |  |  |
| CVX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.71× / 0.55× | 0.71× / 0.55× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CVX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 6147500) | 20 bars, last ('2026-11-16', 6147500) | PASS |  |  |
| DRAL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $4.08 | $4.08 | PASS |  |  |
| DRAL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $6.21 | $6.21 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAL | E3 | percent from the 21-day average | 34.4% below | 34.4% below | PASS |  |  |
| DRAL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 3:45pm ET) | session=regular | PASS |  |  |
| DRAL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.84 | $0.84 (sr=0.8373) | PASS |  | Wilder ATR14 |
| DRAL | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| DRAL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.2 | +3.2 | PASS |  |  |
| DRAL | L-ema21 | ladder row ema21: price and gap = price vs average | $6.21, -34.4% | $6.21, -34.4% | PASS |  |  |
| DRAL | L-note | "Last close $X · date" note = last completed bar | Last close $4.20 · Nov 16 | $4.20 · Nov 16 | PASS |  |  |
| DRAL | L-now | ladder price row = compared price; name = the basis label | $4.08 "Last trade 3:45pm ET" | $4.08 "last trade 3:45pm et" | PASS |  |  |
| DRAL | L-sma50 | ladder row sma50: price and gap = price vs average | $8.86, -54.0% | $8.86, -54.0% | PASS |  |  |
| DRAL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $4.08 / entry $4.08 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.8 | 34.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAL | T4w | words "20 or more / below 20" | 20 or more | ADX 33.7 | PASS |  |  |
| DRAL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -14.46%, close location 0.00, OBV falling |
| DRAL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| DRAL | V2 | day change of the last completed bar | down 14.5% | -14.46% | PASS |  |  |
| DRAL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| DRAL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.3× from 2026-11-16 | 0.31× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| DRAL | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.31× | 2026-11-16 0.31× | PASS |  |  |
| DRAL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.31× / 0.73× | 0.31× / 0.73× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 71387) | 20 bars, last ('2026-11-16', 71387) | PASS |  |  |
| DRAM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $38.95 | $38.95 | PASS |  |  |
| DRAM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $45.61 | $45.61 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAM | E3 | percent from the 21-day average | 14.6% below | 14.6% below | PASS |  |  |
| DRAM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| DRAM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.21 | $3.21 (sr=3.2111) | PASS |  | Wilder ATR14 |
| DRAM | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| DRAM | L-ema21 | ladder row ema21: price and gap = price vs average | $45.61, -14.6% | $45.61, -14.6% | PASS |  |  |
| DRAM | L-note | "Last close $X · date" note = last completed bar | Last close $39.27 · Nov 16 | $39.27 · Nov 16 | PASS |  |  |
| DRAM | L-now | ladder price row = compared price; name = the basis label | $38.95 "Now" | $38.95 "now" | PASS |  |  |
| DRAM | L-sma50 | ladder row sma50: price and gap = price vs average | $52.9, -26.4% | $52.90, -26.4% | PASS |  |  |
| DRAM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $38.95 / entry $38.95 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.5 | 37.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAM | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.6 | 31.6 | PASS |  | Wilder, completed bars |
| DRAM | T4w | words "20 or more / below 20" | 20 or more | ADX 31.6 | PASS |  |  |
| DRAM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -7.38%, close location 0.41, OBV falling |
| DRAM | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| DRAM | V2 | day change of the last completed bar | down 7.4% | -7.38% | PASS |  |  |
| DRAM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.08× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| DRAM | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.08× | 2026-11-16 1.08× | PASS |  |  |
| DRAM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.08× / 0.90× | 1.08× / 0.90× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 37358300) | 20 bars, last ('2026-11-16', 37358300) | PASS |  |  |
| DRIV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $26.99 | $26.99 | PASS |  |  |
| DRIV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $29.52 | $29.52 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRIV | E3 | percent from the 21-day average | 8.6% below | 8.6% below | PASS |  |  |
| DRIV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| DRIV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.81 | $0.81 (sr=0.8068) | PASS |  | Wilder ATR14 |
| DRIV | E5 | distance in normal day-moves | 3.1 | 3.1 | PASS |  | gauge dot note uses the same number:  · 3.1 day-moves below |
| DRIV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.9 | +5.9 | PASS |  |  |
| DRIV | L-ema21 | ladder row ema21: price and gap = price vs average | $29.52, -8.6% | $29.52, -8.6% | PASS |  |  |
| DRIV | L-note | "Last close $X · date" note = last completed bar | Last close $27.35 · Nov 16 | $27.35 · Nov 16 | PASS |  |  |
| DRIV | L-now | ladder price row = compared price; name = the basis label | $26.99 "Now" | $26.99 "now" | PASS |  |  |
| DRIV | L-sma200 | ladder row sma200: price and gap = price vs average | $34.28, -21.3% | $34.28, -21.3% | PASS |  |  |
| DRIV | L-sma50 | ladder row sma50: price and gap = price vs average | $31.61, -14.6% | $31.61, -14.6% | PASS |  |  |
| DRIV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $26.99 / entry $26.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRIV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DRIV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.9 | 32.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRIV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -6.7% vs +10.1% | -6.7% vs 10.1% | PASS |  |  |
| DRIV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DRIV | T4 | ADX 14 (S1 /api/sr meta.adx) | 37.0 | 37.0 | PASS |  | Wilder, completed bars |
| DRIV | T4w | words "20 or more / below 20" | 20 or more | ADX 37.0 | PASS |  |  |
| DRIV | T5 | "counted at the last close ($X, date)" = last completed bar | $27.35, Nov 16 | $27.35, Nov 16 | PASS |  |  |
| DRIV | T6 | price vs 200-day average (S1 pattern sma values) | $27.35 vs $34.28 · -20.2% | $27.35 vs $34.28 · -20.2% | PASS |  |  |
| DRIV | T6w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T7 | price vs 50-day average (S1 pattern sma values) | $27.35 vs $31.61 · -13.5% | $27.35 vs $31.61 · -13.5% | PASS |  |  |
| DRIV | T7w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.6% over 30 td | -0.6% over 30 td | PASS |  |  |
| DRIV | T8r | word "rising" | not rising | not rising | PASS |  |  |
| DRIV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DRIV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.0% below $42.76 | 36.0% below $42.76 | PASS |  | closing high would be 42.53 |
| DRIV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.0% below | PASS |  |  |
| DRIV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $42.76 | $42.76 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DRIV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.87%, close location 0.00, OBV falling |
| DRIV | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| DRIV | V2 | day change of the last completed bar | down 3.9% | -3.87% | PASS |  |  |
| DRIV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| DRIV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRIV | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 0.97× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| DRIV | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.97× | 2026-11-16 0.97× | PASS |  |  |
| DRIV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.97× / 1.31× | 0.97× / 1.31× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRIV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 39888) | 20 bars, last ('2026-11-16', 39888) | PASS |  |  |
| DUK | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $129.88 | $129.88 | PASS |  |  |
| DUK | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $125.5 | $125.50 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DUK | E3 | percent from the 21-day average | 3.5% above | 3.5% above | PASS |  |  |
| DUK | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| DUK | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.16 | $2.16 (sr=2.1596) | PASS |  | Wilder ATR14 |
| DUK | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves above |
| DUK | L-ema21 | ladder row ema21: price and gap = price vs average | $125.5, 3.5% | $125.50, 3.5% | PASS |  |  |
| DUK | L-note | "Last close $X · date" note = last completed bar | Last close $130.59 · Nov 16 | $130.59 · Nov 16 | PASS |  |  |
| DUK | L-now | ladder price row = compared price; name = the basis label | $129.88 "Now" | $129.88 "now" | PASS |  |  |
| DUK | L-sma200 | ladder row sma200: price and gap = price vs average | $122.66, 5.9% | $122.66, 5.9% | PASS |  |  |
| DUK | L-sma50 | ladder row sma50: price and gap = price vs average | $119.88, 8.3% | $119.88, 8.3% | PASS |  |  |
| DUK | S5-price | S5: the same live price reads the same on the header and the Entry block | header $129.88 / entry $129.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DUK | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DUK | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 69.8 | 69.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DUK | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +10.1% vs +10.1% | 10.1% vs 10.1% | PASS |  |  |
| DUK | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DUK | T4 | ADX 14 (S1 /api/sr meta.adx) | 47.9 | 47.9 | PASS |  | Wilder, completed bars |
| DUK | T4w | words "20 or more / below 20" | 20 or more | ADX 47.9 | PASS |  |  |
| DUK | T5 | "counted at the last close ($X, date)" = last completed bar | $130.59, Nov 16 | $130.59, Nov 16 | PASS |  |  |
| DUK | T6 | price vs 200-day average (S1 pattern sma values) | $130.59 vs $122.66 · +6.5% | $130.59 vs $122.66 · 6.5% | PASS |  |  |
| DUK | T6w | word "Above" | Above | Above | PASS |  |  |
| DUK | T7 | price vs 50-day average (S1 pattern sma values) | $130.59 vs $119.88 · +8.9% | $130.59 vs $119.88 · 8.9% | PASS |  |  |
| DUK | T7w | word "Above" | Above | Above | PASS |  |  |
| DUK | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.1% over 30 td | +1.1% over 30 td | PASS |  |  |
| DUK | T8r | word "rising" | still rising | rising | PASS |  |  |
| DUK | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DUK | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.0% below $131.87 | 1.0% below $131.87 | PASS |  | closing high would be 130.59 |
| DUK | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.0% below | PASS |  |  |
| DUK | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.87 | $131.86787171141273 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DUK | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 1.11%, close location 0.43, OBV rising |
| DUK | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| DUK | V2 | day change of the last completed bar | up 1.1% | +1.11% | PASS |  |  |
| DUK | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| DUK | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.5× from 2026-11-16 | 1.48× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| DUK | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.48× | 2026-11-16 1.48× | PASS |  |  |
| DUK | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.48× / 0.67× | 1.48× / 0.67× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DUK | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 6409900) | 20 bars, last ('2026-11-16', 6409900) | PASS |  |  |
| ELIL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.93 | $39.93 | PASS |  |  |
| ELIL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $37.71 | $37.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ELIL | E3 | percent from the 21-day average | 5.9% above | 5.9% above | PASS |  |  |
| ELIL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 3:51pm ET) | session=regular | PASS |  |  |
| ELIL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.27 | $2.27 (sr=2.2689) | PASS |  | Wilder ATR14 |
| ELIL | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves above |
| ELIL | L-ema21 | ladder row ema21: price and gap = price vs average | $37.71, 5.9% | $37.71, 5.9% | PASS |  |  |
| ELIL | L-note | "Last close $X · date" note = last completed bar | Last close $41.12 · Nov 16 | $41.12 · Nov 16 | PASS |  |  |
| ELIL | L-now | ladder price row = compared price; name = the basis label | $39.93 "Last trade 3:51pm ET" | $39.93 "last trade 3:51pm et" | PASS |  |  |
| ELIL | L-sma200 | ladder row sma200: price and gap = price vs average | $26.93, 48.3% | $26.93, 48.3% | PASS |  |  |
| ELIL | L-sma50 | ladder row sma50: price and gap = price vs average | $31.99, 24.8% | $31.99, 24.8% | PASS |  |  |
| ELIL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $39.93 / entry $39.93 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ELIL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ELIL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 66.0 | 66.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ELIL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +58.6% vs +10.1% | 58.6% vs 10.1% | PASS |  |  |
| ELIL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ELIL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.4 | 34.5 | PASS |  | Wilder, completed bars |
| ELIL | T4w | words "20 or more / below 20" | 20 or more | ADX 34.5 | PASS |  |  |
| ELIL | T5 | "counted at the last close ($X, date)" = last completed bar | $41.12, Nov 16 | $41.12, Nov 16 | PASS |  |  |
| ELIL | T6 | price vs 200-day average (S1 pattern sma values) | $41.12 vs $26.93 · +52.7% | $41.12 vs $26.93 · 52.7% | PASS |  |  |
| ELIL | T6w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T7 | price vs 50-day average (S1 pattern sma values) | $41.12 vs $31.99 · +28.5% | $41.12 vs $31.99 · 28.5% | PASS |  |  |
| ELIL | T7w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.5% over 30 td | +4.5% over 30 td | PASS |  |  |
| ELIL | T8r | word "rising" | still rising | rising | PASS |  |  |
| ELIL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ELIL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.6% below $43.56 | 5.6% below $43.56 | PASS |  | closing high would be 41.85 |
| ELIL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.6% below | PASS |  |  |
| ELIL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.56 | $43.55500030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ELIL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.74%, close location 0.09, OBV flat |
| ELIL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ELIL | V2 | day change of the last completed bar | down 1.8% | -1.74% | PASS |  |  |
| ELIL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0896) | PASS |  |  |
| ELIL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| ELIL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.9× from 2026-11-16 | 1.91× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ELIL | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.91× | 2026-11-16 1.91× | PASS |  |  |
| ELIL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.91× / 0.32× | 1.91× / 0.32× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ELIL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 121500) | 20 bars, last ('2026-11-16', 121500) | PASS |  |  |
| EQIX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,033.19 | $1,033.19 | PASS |  |  |
| EQIX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1028.98 | $1028.98 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| EQIX | E3 | percent from the 21-day average | 0.4% above | 0.4% above | PASS |  |  |
| EQIX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| EQIX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $34.32 | $34.32 (sr=34.3155) | PASS |  | Wilder ATR14 |
| EQIX | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| EQIX | L-ema21 | ladder row ema21: price and gap = price vs average | $1028.98, 0.4% | $1028.98, 0.4% | PASS |  |  |
| EQIX | L-now | ladder price row = compared price; name = the basis label | $1033.19 "Now" | $1033.18 "now" | PASS |  |  |
| EQIX | L-sma200 | ladder row sma200: price and gap = price vs average | $1018.04, 1.5% | $1018.04, 1.5% | PASS |  |  |
| EQIX | L-sma50 | ladder row sma50: price and gap = price vs average | $1019.26, 1.4% | $1019.26, 1.4% | PASS |  |  |
| EQIX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,033.19 / entry $1,033.19 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| EQIX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| EQIX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.5 | 53.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| EQIX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +35.6% vs +10.1% | 35.6% vs 10.1% | PASS |  |  |
| EQIX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| EQIX | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.2 | 19.2 | PASS |  | Wilder, completed bars |
| EQIX | T4w | words "20 or more / below 20" | below 20 | ADX 19.2 | PASS |  |  |
| EQIX | T5 | "counted at the last close ($X, date)" = last completed bar | $1,043.06, Nov 16 | $1043.06, Nov 16 | PASS |  |  |
| EQIX | T6 | price vs 200-day average (S1 pattern sma values) | $1,043.06 vs $1,018.04 · +2.5% | $1043.06 vs $1018.04 · 2.5% | PASS |  |  |
| EQIX | T6w | word "Above" | Above | Above | PASS |  |  |
| EQIX | T7 | price vs 50-day average (S1 pattern sma values) | $1,043.06 vs $1,019.26 · +2.3% | $1043.06 vs $1019.26 · 2.3% | PASS |  |  |
| EQIX | T7w | word "Above" | Above | Above | PASS |  |  |
| EQIX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.7% over 30 td | +3.7% over 30 td | PASS |  |  |
| EQIX | T8r | word "rising" | still rising | rising | PASS |  |  |
| EQIX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| EQIX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.8% below $1,118.65 | 6.8% below $1118.65 | PASS |  | closing high would be 1110.63 |
| EQIX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.8% below | PASS |  |  |
| EQIX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,118.65 | $1118.6549839367933 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| EQIX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.02%, close location 0.24, OBV rising |
| EQIX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| EQIX | V2 | day change of the last completed bar | down 1.0% | -1.02% | PASS |  |  |
| EQIX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.24 (raw 0.2356) | PASS |  |  |
| EQIX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| EQIX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.81× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| EQIX | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.81× | 2026-11-16 0.81× | PASS |  |  |
| EQIX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.81× / 0.31× | 0.81× / 0.31× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| EQIX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 471400) | 20 bars, last ('2026-11-16', 471400) | PASS |  |  |
| ETN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $334.98 | $334.98 | PASS |  |  |
| ETN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $368.44 | $368.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ETN | E3 | percent from the 21-day average | 9.1% below | 9.1% below | PASS |  |  |
| ETN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| ETN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $18.41 | $18.41 (sr=18.412) | PASS |  | Wilder ATR14 |
| ETN | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| ETN | L-ema21 | ladder row ema21: price and gap = price vs average | $368.44, -9.1% | $368.44, -9.1% | PASS |  |  |
| ETN | L-note | "Last close $X · date" note = last completed bar | Last close $336.88 · Nov 16 | $336.88 · Nov 16 | PASS |  |  |
| ETN | L-now | ladder price row = compared price; name = the basis label | $334.98 "Now" | $334.98 "now" | PASS |  |  |
| ETN | L-sma200 | ladder row sma200: price and gap = price vs average | $397.71, -15.8% | $397.71, -15.8% | PASS |  |  |
| ETN | L-sma50 | ladder row sma50: price and gap = price vs average | $399.85, -16.2% | $399.85, -16.2% | PASS |  |  |
| ETN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $334.98 / entry $334.98 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ETN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ETN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.6 | 37.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ETN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.4% vs +10.1% | -4.4% vs 10.1% | PASS |  |  |
| ETN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ETN | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.2 | 26.2 | PASS |  | Wilder, completed bars |
| ETN | T4w | words "20 or more / below 20" | 20 or more | ADX 26.2 | PASS |  |  |
| ETN | T5 | "counted at the last close ($X, date)" = last completed bar | $336.88, Nov 16 | $336.88, Nov 16 | PASS |  |  |
| ETN | T6 | price vs 200-day average (S1 pattern sma values) | $336.88 vs $397.71 · -15.3% | $336.88 vs $397.71 · -15.3% | PASS |  |  |
| ETN | T6w | word "Below" | Below | Below | PASS |  |  |
| ETN | T7 | price vs 50-day average (S1 pattern sma values) | $336.88 vs $399.85 · -15.7% | $336.88 vs $399.85 · -15.7% | PASS |  |  |
| ETN | T7w | word "Below" | Below | Below | PASS |  |  |
| ETN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| ETN | T8r | word "rising" | still rising | rising | PASS |  |  |
| ETN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ETN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.5% below $478.00 | 29.5% below $478.00 | PASS |  | closing high would be 459.96 |
| ETN | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.5% below | PASS |  |  |
| ETN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $478.00 | $478 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ETN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.56%, close location 0.06, OBV falling |
| ETN | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ETN | V2 | day change of the last completed bar | down 4.6% | -4.56% | PASS |  |  |
| ETN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0613) | PASS |  |  |
| ETN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ETN | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.09× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ETN | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.09× | 2026-11-16 1.09× | PASS |  |  |
| ETN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.09× / 0.83× | 1.09× / 0.83× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ETN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 2844779) | 20 bars, last ('2026-11-16', 2844779) | PASS |  |  |
| FCX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $55.17 | $55.17 | PASS |  |  |
| FCX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $62.81 | $62.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FCX | E3 | percent from the 21-day average | 12.2% below | 12.2% below | PASS |  |  |
| FCX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| FCX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.86 | $2.86 (sr=2.8595) | PASS |  | Wilder ATR14 |
| FCX | E5 | distance in normal day-moves | 2.7 | 2.7 | PASS |  | gauge dot note uses the same number:  · 2.7 day-moves below |
| FCX | L-ema21 | ladder row ema21: price and gap = price vs average | $62.81, -12.2% | $62.81, -12.2% | PASS |  |  |
| FCX | L-note | "Last close $X · date" note = last completed bar | Last close $55.19 · Nov 16 | $55.19 · Nov 16 | PASS |  |  |
| FCX | L-now | ladder price row = compared price; name = the basis label | $55.17 "Now" | $55.16 "now" | PASS |  |  |
| FCX | L-sma200 | ladder row sma200: price and gap = price vs average | $65.17, -15.4% | $65.17, -15.4% | PASS |  |  |
| FCX | L-sma50 | ladder row sma50: price and gap = price vs average | $68.15, -19.1% | $68.15, -19.1% | PASS |  |  |
| FCX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $55.17 / entry $55.17 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| FCX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FCX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.7 | 30.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FCX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +37.4% vs +10.1% | 37.4% vs 10.1% | PASS |  |  |
| FCX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FCX | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.8 | 25.8 | PASS |  | Wilder, completed bars |
| FCX | T4w | words "20 or more / below 20" | 20 or more | ADX 25.8 | PASS |  |  |
| FCX | T5 | "counted at the last close ($X, date)" = last completed bar | $55.19, Nov 16 | $55.19, Nov 16 | PASS |  |  |
| FCX | T6 | price vs 200-day average (S1 pattern sma values) | $55.19 vs $65.17 · -15.3% | $55.19 vs $65.17 · -15.3% | PASS |  |  |
| FCX | T6w | word "Below" | Below | Below | PASS |  |  |
| FCX | T7 | price vs 50-day average (S1 pattern sma values) | $55.19 vs $68.15 · -19.0% | $55.19 vs $68.15 · -19.0% | PASS |  |  |
| FCX | T7w | word "Below" | Below | Below | PASS |  |  |
| FCX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.3% over 30 td | PASS |  |  |
| FCX | T8r | word "rising" | still rising | rising | PASS |  |  |
| FCX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FCX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 31.2% below $80.24 | 31.2% below $80.24 | PASS |  | closing high would be 79.91 |
| FCX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 31.2% below | PASS |  |  |
| FCX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.24 | $80.24 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FCX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.84%, close location 0.06, OBV falling |
| FCX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| FCX | V2 | day change of the last completed bar | down 6.8% | -6.84% | PASS |  |  |
| FCX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0618) | PASS |  |  |
| FCX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| FCX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.6× from 2026-11-16 | 1.65× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| FCX | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.65× | 2026-11-16 1.65× | PASS |  |  |
| FCX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.65× / 1.32× | 1.65× / 1.32× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FCX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 19599559) | 20 bars, last ('2026-11-16', 19599559) | PASS |  |  |
| FCX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.65, OBV falling | condition true | PASS |  |  |
| FINN.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $32.10 | $32.10 | PASS |  |  |
| FINN.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $32.77 | $32.77 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FINN.NE | E3 | percent from the 21-day average | 2.0% below | 2.0% below | PASS |  |  |
| FINN.NE | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| FINN.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.68 | $0.68 (sr=0.6776) | PASS |  | Wilder ATR14 |
| FINN.NE | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| FINN.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $32.77, -2.0% | $32.77, -2.0% | PASS |  |  |
| FINN.NE | L-now | ladder price row = compared price; name = the basis label | $32.1 "Last close" | $32.10 "last close" | PASS |  |  |
| FINN.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.04, 6.8% | $30.04, 6.8% | PASS |  |  |
| FINN.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $33.27, -3.5% | $33.27, -3.5% | PASS |  |  |
| FINN.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FINN.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.8 | 42.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FINN.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +40.0% vs +10.1% | 40.1% vs 10.1% | PASS |  |  |
| FINN.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FINN.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.5 | 13.5 | PASS |  | Wilder, completed bars |
| FINN.NE | T4w | words "20 or more / below 20" | below 20 | ADX 13.5 | PASS |  |  |
| FINN.NE | T6 | price vs 200-day average (S1 pattern sma values) | $32.10 vs $30.04 · +6.9% | $32.10 vs $30.04 · 6.8% | PASS |  |  |
| FINN.NE | T6w | word "Above" | Above | Above | PASS |  |  |
| FINN.NE | T7 | price vs 50-day average (S1 pattern sma values) | $32.10 vs $33.27 · -3.5% | $32.10 vs $33.27 · -3.5% | PASS |  |  |
| FINN.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| FINN.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.8% over 30 td | +4.8% over 30 td | PASS |  |  |
| FINN.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| FINN.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FINN.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.4% below $35.83 | 10.4% below $35.83 | PASS |  | closing high would be 35.43 |
| FINN.NE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.4% below | PASS |  |  |
| FINN.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $35.83 | $35.83000183105469 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FINN.NE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.83%, close location 0.09, OBV rising |
| FINN.NE | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| FINN.NE | V2 | day change of the last completed bar | down 1.8% | -1.83% | PASS |  |  |
| FINN.NE | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0877) | PASS |  |  |
| FINN.NE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| FINN.NE | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-16 | 0.95× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| FINN.NE | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.95× | 2026-11-16 0.95× | PASS |  |  |
| FINN.NE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.95× / 0.87× | 0.95× / 0.87× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FINN.NE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 281567) | 20 bars, last ('2026-11-16', 281567) | PASS |  |  |
| GDX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $79.61 | $79.61 | PASS |  |  |
| GDX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $84.01 | $84.01 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDX | E3 | percent from the 21-day average | 5.2% below | 5.2% below | PASS |  |  |
| GDX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| GDX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.48 | $3.48 (sr=3.477) | PASS |  | Wilder ATR14 |
| GDX | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| GDX | L-ema21 | ladder row ema21: price and gap = price vs average | $84.01, -5.2% | $84.01, -5.2% | PASS |  |  |
| GDX | L-note | "Last close $X · date" note = last completed bar | Last close $78.95 · Nov 16 | $78.95 · Nov 16 | PASS |  |  |
| GDX | L-now | ladder price row = compared price; name = the basis label | $79.61 "Now" | $79.61 "now" | PASS |  |  |
| GDX | L-sma200 | ladder row sma200: price and gap = price vs average | $89.5, -11.1% | $89.50, -11.1% | PASS |  |  |
| GDX | L-sma50 | ladder row sma50: price and gap = price vs average | $87.86, -9.4% | $87.86, -9.4% | PASS |  |  |
| GDX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $79.61 / entry $79.61 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GDX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.9 | 40.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.4% vs +10.1% | 4.4% vs 10.1% | PASS |  |  |
| GDX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDX | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.5 | 17.5 | PASS |  | Wilder, completed bars |
| GDX | T4w | words "20 or more / below 20" | below 20 | ADX 17.5 | PASS |  |  |
| GDX | T5 | "counted at the last close ($X, date)" = last completed bar | $78.95, Nov 16 | $78.95, Nov 16 | PASS |  |  |
| GDX | T6 | price vs 200-day average (S1 pattern sma values) | $78.95 vs $89.50 · -11.8% | $78.95 vs $89.50 · -11.8% | PASS |  |  |
| GDX | T6w | word "Below" | Below | Below | PASS |  |  |
| GDX | T7 | price vs 50-day average (S1 pattern sma values) | $78.95 vs $87.86 · -10.1% | $78.95 vs $87.86 · -10.1% | PASS |  |  |
| GDX | T7w | word "Below" | Below | Below | PASS |  |  |
| GDX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.7% over 30 td | -1.7% over 30 td | PASS |  |  |
| GDX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 32.6% below $117.18 | 32.6% below $117.18 | PASS |  | closing high would be 115.84 |
| GDX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 32.6% below | PASS |  |  |
| GDX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $117.18 | $117.18000030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.29%, close location 0.04, OBV falling |
| GDX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GDX | V2 | day change of the last completed bar | down 3.3% | -3.29% | PASS |  |  |
| GDX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0404) | PASS |  |  |
| GDX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-16 | 1.27× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| GDX | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.27× | 2026-11-16 1.27× | PASS |  |  |
| GDX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.27× / 0.75× | 1.27× / 0.75× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 26771100) | 20 bars, last ('2026-11-16', 26771100) | PASS |  |  |
| GDXU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $24.45 | $24.45 | PASS |  |  |
| GDXU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.12 | $28.12 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDXU.TO | E3 | percent from the 21-day average | 13.1% below | 13.1% below | PASS |  |  |
| GDXU.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| GDXU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.41 | $2.41 (sr=2.406) | PASS |  | Wilder ATR14 |
| GDXU.TO | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| GDXU.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.3 | +3.3 | PASS |  |  |
| GDXU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $28.12, -13.1% | $28.12, -13.1% | PASS |  |  |
| GDXU.TO | L-note | "Last close $X · date" note = last completed bar | Last close $24.30 · Nov 16 | $24.30 · Nov 16 | PASS |  |  |
| GDXU.TO | L-now | ladder price row = compared price; name = the basis label | $24.45 "Now" | $24.45 "now" | PASS |  |  |
| GDXU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $35.96, -32.0% | $35.96, -32.0% | PASS |  |  |
| GDXU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $31.67, -22.8% | $31.67, -22.8% | PASS |  |  |
| GDXU.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $24.45 / entry $24.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GDXU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDXU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.8 | 39.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDXU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -19.8% vs +10.1% | -19.8% vs 10.1% | PASS |  |  |
| GDXU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDXU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.1 | 18.1 | PASS |  | Wilder, completed bars |
| GDXU.TO | T4w | words "20 or more / below 20" | below 20 | ADX 18.1 | PASS |  |  |
| GDXU.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $24.30, Nov 16 | $24.30, Nov 16 | PASS |  |  |
| GDXU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $24.30 vs $35.96 · -32.4% | $24.30 vs $35.96 · -32.4% | PASS |  |  |
| GDXU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $24.30 vs $31.67 · -23.3% | $24.30 vs $31.67 · -23.3% | PASS |  |  |
| GDXU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -6.4% over 30 td | -6.4% over 30 td | PASS |  |  |
| GDXU.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDXU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDXU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 62.6% below $65.00 | 62.6% below $65.00 | PASS |  | closing high would be 63.22 |
| GDXU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 62.6% below | PASS |  |  |
| GDXU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $65.00 | $65 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDXU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.72%, close location 0.03, OBV falling |
| GDXU.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GDXU.TO | V2 | day change of the last completed bar | down 6.7% | -6.72% | PASS |  |  |
| GDXU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0299) | PASS |  |  |
| GDXU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDXU.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.6× from 2026-11-16 | 1.60× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| GDXU.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.60× | 2026-11-16 1.60× | PASS |  |  |
| GDXU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.60× / 0.68× | 1.60× / 0.68× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDXU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 361400) | 20 bars, last ('2026-11-16', 361400) | PASS |  |  |
| GDXU.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.60, OBV falling | condition true | PASS |  |  |
| GE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $325.37 | $325.37 | PASS |  |  |
| GE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $320.68 | $320.68 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GE | E3 | percent from the 21-day average | 1.5% above | 1.5% above | PASS |  |  |
| GE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| GE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $10.47 | $10.47 (sr=10.4662) | PASS |  | Wilder ATR14 |
| GE | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves above |
| GE | L-ema21 | ladder row ema21: price and gap = price vs average | $320.68, 1.5% | $320.68, 1.5% | PASS |  |  |
| GE | L-note | "Last close $X · date" note = last completed bar | Last close $325.18 · Nov 16 | $325.18 · Nov 16 | PASS |  |  |
| GE | L-now | ladder price row = compared price; name = the basis label | $325.37 "Now" | $325.37 "now" | PASS |  |  |
| GE | L-sma200 | ladder row sma200: price and gap = price vs average | $323.3, 0.6% | $323.30, 0.6% | PASS |  |  |
| GE | L-sma50 | ladder row sma50: price and gap = price vs average | $314.36, 3.5% | $314.36, 3.5% | PASS |  |  |
| GE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $325.37 / entry $325.37 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.4 | 53.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +7.3% vs +10.1% | 7.3% vs 10.1% | PASS |  |  |
| GE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GE | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.2 | 22.1 | PASS |  | Wilder, completed bars |
| GE | T4w | words "20 or more / below 20" | 20 or more | ADX 22.1 | PASS |  |  |
| GE | T5 | "counted at the last close ($X, date)" = last completed bar | $325.18, Nov 16 | $325.18, Nov 16 | PASS |  |  |
| GE | T6w | word "Above" | Above | Above | PASS |  |  |
| GE | T7w | word "Above" | Above | Above | PASS |  |  |
| GE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.0% over 30 td | +0.1% over 30 td | PASS |  |  |
| GE | T8r | word "rising" | still rising | rising | PASS |  |  |
| GE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 16.2% below | PASS |  |  |
| GE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.00%, close location 0.13, OBV rising |
| GE | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GE | V2 | day change of the last completed bar | down 2.0% | -2.00% | PASS |  |  |
| GE | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.13 (raw 0.1345) | PASS |  |  |
| GE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GE | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.7× from 2026-11-16 | 0.73× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| GE | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.73× | 2026-11-16 0.73× | PASS |  |  |
| GE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.73× / 0.62× | 0.73× / 0.62× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3556800) | 20 bars, last ('2026-11-16', 3556800) | PASS |  |  |
| GEV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $773.57 | $773.57 | PASS |  |  |
| GEV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $843.65 | $843.65 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV | E3 | percent from the 21-day average | 8.3% below | 8.3% below | PASS |  |  |
| GEV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| GEV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $56.27 | $56.26 (sr=56.2705) | PASS |  | Wilder ATR14 |
| GEV | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| GEV | L-ema21 | ladder row ema21: price and gap = price vs average | $843.65, -8.3% | $843.65, -8.3% | PASS |  |  |
| GEV | L-note | "Last close $X · date" note = last completed bar | Last close $763.57 · Nov 16 | $763.57 · Nov 16 | PASS |  |  |
| GEV | L-now | ladder price row = compared price; name = the basis label | $773.57 "Now" | $773.57 "now" | PASS |  |  |
| GEV | L-sma200 | ladder row sma200: price and gap = price vs average | $951.16, -18.7% | $951.16, -18.7% | PASS |  |  |
| GEV | L-sma50 | ladder row sma50: price and gap = price vs average | $909.23, -14.9% | $909.23, -14.9% | PASS |  |  |
| GEV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $773.57 / entry $773.57 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GEV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GEV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.4 | 37.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +32.4% vs +10.1% | 32.4% vs 10.1% | PASS |  |  |
| GEV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GEV | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.0 | 23.9 | PASS |  | Wilder, completed bars |
| GEV | T4w | words "20 or more / below 20" | 20 or more | ADX 23.9 | PASS |  |  |
| GEV | T5 | "counted at the last close ($X, date)" = last completed bar | $763.57, Nov 16 | $763.57, Nov 16 | PASS |  |  |
| GEV | T6w | word "Below" | Below | Below | PASS |  |  |
| GEV | T7w | word "Below" | Below | Below | PASS |  |  |
| GEV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.6% over 30 td | +3.6% over 30 td | PASS |  |  |
| GEV | T8r | word "rising" | still rising | rising | PASS |  |  |
| GEV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GEV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.1% below | PASS |  |  |
| GEV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.93%, close location 0.09, OBV falling |
| GEV | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GEV | V2 | day change of the last completed bar | down 4.9% | -4.93% | PASS |  |  |
| GEV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0885) | PASS |  |  |
| GEV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.15× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| GEV | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.15× | 2026-11-16 1.15× | PASS |  |  |
| GEV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.15× / 0.67× | 1.15× / 0.67× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3520600) | 20 bars, last ('2026-11-16', 3520600) | PASS |  |  |
| GEV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $51.03 | $51.03 | PASS |  |  |
| GEV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $56.42 | $56.42 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV.TO | E3 | percent from the 21-day average | 9.6% below | 9.6% below | PASS |  |  |
| GEV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GEV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.66 | $3.66 (sr=3.6559) | PASS |  | Wilder ATR14 |
| GEV.TO | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| GEV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $56.42, -9.6% | $56.42, -9.6% | PASS |  |  |
| GEV.TO | L-now | ladder price row = compared price; name = the basis label | $51.03 "Last close" | $51.03 "last close" | PASS |  |  |
| GEV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.07, -20.4% | $64.07, -20.4% | PASS |  |  |
| GEV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $60.8, -16.1% | $60.80, -16.1% | PASS |  |  |
| GEV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.2 | 37.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +13.4% vs +10.1% | 13.4% vs 10.1% | PASS |  |  |
| GEV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.5 | 23.4 | PASS |  | Wilder, completed bars |
| GEV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 23.4 | PASS |  |  |
| GEV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.92%, close location 0.07, OBV falling |
| GEV.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GEV.TO | V2 | day change of the last completed bar | down 4.9% | -4.92% | PASS |  |  |
| GEV.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0695) | PASS |  |  |
| GEV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.2× from 2026-11-16 | 1.19× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| GEV.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.19× | 2026-11-16 1.19× | PASS |  |  |
| GEV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.19× / 0.69× | 1.19× / 0.69× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 86400) | 20 bars, last ('2026-11-16', 86400) | PASS |  |  |
| GGLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $63.09 | $63.09 | PASS |  |  |
| GGLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $75.06 | $75.06 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GGLL | E3 | percent from the 21-day average | 15.9% below | 15.9% below | PASS |  |  |
| GGLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| GGLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.30 | $5.30 (sr=5.2963) | PASS |  | Wilder ATR14 |
| GGLL | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| GGLL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.3 | +5.3 | PASS |  |  |
| GGLL | L-ema21 | ladder row ema21: price and gap = price vs average | $75.06, -15.9% | $75.06, -15.9% | PASS |  |  |
| GGLL | L-note | "Last close $X · date" note = last completed bar | Last close $64.83 · Nov 16 | $64.83 · Nov 16 | PASS |  |  |
| GGLL | L-now | ladder price row = compared price; name = the basis label | $63.09 "Now" | $63.09 "now" | PASS |  |  |
| GGLL | L-sma200 | ladder row sma200: price and gap = price vs average | $103.16, -38.8% | $103.16, -38.8% | PASS |  |  |
| GGLL | L-sma50 | ladder row sma50: price and gap = price vs average | $89.88, -29.8% | $89.88, -29.8% | PASS |  |  |
| GGLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $63.09 / entry $63.09 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GGLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GGLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.9 | 32.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GGLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -18.7% vs +10.1% | -18.7% vs 10.1% | PASS |  |  |
| GGLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GGLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.9 | 27.9 | PASS |  | Wilder, completed bars |
| GGLL | T4w | words "20 or more / below 20" | 20 or more | ADX 27.9 | PASS |  |  |
| GGLL | T5 | "counted at the last close ($X, date)" = last completed bar | $64.83, Nov 16 | $64.83, Nov 16 | PASS |  |  |
| GGLL | T6 | price vs 200-day average (S1 pattern sma values) | $64.83 vs $103.16 · -37.2% | $64.83 vs $103.16 · -37.2% | PASS |  |  |
| GGLL | T6w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T7 | price vs 50-day average (S1 pattern sma values) | $64.83 vs $89.88 · -27.9% | $64.83 vs $89.88 · -27.9% | PASS |  |  |
| GGLL | T7w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.7% over 30 td | -2.7% over 30 td | PASS |  |  |
| GGLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GGLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GGLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 57.6% below $153.00 | 57.6% below $153.00 | PASS |  | closing high would be 148.94 |
| GGLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 57.6% below | PASS |  |  |
| GGLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $153.00 | $153 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GGLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -8.15%, close location 0.07, OBV falling |
| GGLL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GGLL | V2 | day change of the last completed bar | down 8.2% | -8.15% | PASS |  |  |
| GGLL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0658) | PASS |  |  |
| GGLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GGLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1422300) | 20 bars, last ('2026-11-16', 1422300) | PASS |  |  |
| GIB-A.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $117.80 | $117.80 | PASS |  |  |
| GIB-A.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.06 | $113.06 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GIB-A.TO | E3 | percent from the 21-day average | 4.2% above | 4.2% above | PASS |  |  |
| GIB-A.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GIB-A.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.75 | $2.75 (sr=2.75) | PASS |  | Wilder ATR14 |
| GIB-A.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves above |
| GIB-A.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $113.06, 4.2% | $113.06, 4.2% | PASS |  |  |
| GIB-A.TO | L-now | ladder price row = compared price; name = the basis label | $117.8 "Last close" | $117.80 "last close" | PASS |  |  |
| GIB-A.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $99.81, 18.0% | $99.81, 18.0% | PASS |  |  |
| GIB-A.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $105.24, 11.9% | $105.24, 11.9% | PASS |  |  |
| GIB-A.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GIB-A.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 67.8 | 67.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GIB-A.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -3.6% vs +10.1% | -3.6% vs 10.1% | PASS |  |  |
| GIB-A.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GIB-A.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 42.1 | 42.1 | PASS |  | Wilder, completed bars |
| GIB-A.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 42.1 | PASS |  |  |
| GIB-A.TO | T6 | price vs 200-day average (S1 pattern sma values) | $117.80 vs $99.81 · +18.0% | $117.80 vs $99.81 · 18.0% | PASS |  |  |
| GIB-A.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T7 | price vs 50-day average (S1 pattern sma values) | $117.80 vs $105.24 · +11.9% | $117.80 vs $105.24 · 11.9% | PASS |  |  |
| GIB-A.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.3% over 30 td | -2.3% over 30 td | PASS |  |  |
| GIB-A.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GIB-A.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GIB-A.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.3% below $131.27 | 10.3% below $131.27 | PASS |  | closing high would be 130.81 |
| GIB-A.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.3% below | PASS |  |  |
| GIB-A.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.27 | $131.26876580580614 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GIB-A.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.85%, close location 0.71, OBV rising |
| GIB-A.TO | V2 | day change of the last completed bar | up 0.8% | +0.85% | PASS |  |  |
| GIB-A.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GIB-A.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.3× from 2026-11-13 | 0.32× from 2026-11-13 | PASS |  | window "50 bars" includes the bar itself |
| GIB-A.TO | V6 | Volume detail: last session date and RVOL | 2026-11-13 0.32× | 2026-11-13 0.32× | PASS |  |  |
| GIB-A.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.32× / 0.36× | 0.32× / 0.36× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GIB-A.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-13', 198193) | 20 bars, last ('2026-11-13', 198193) | PASS |  |  |
| GOOGL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $279.84 | $279.84 | PASS |  |  |
| GOOGL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $301.89 | $301.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GOOGL | E3 | percent from the 21-day average | 7.3% below | 7.3% below | PASS |  |  |
| GOOGL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| GOOGL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $10.47 | $10.47 (sr=10.4716) | PASS |  | Wilder ATR14 |
| GOOGL | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| GOOGL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.4 | +3.4 | PASS |  |  |
| GOOGL | L-ema21 | ladder row ema21: price and gap = price vs average | $301.89, -7.3% | $301.89, -7.3% | PASS |  |  |
| GOOGL | L-note | "Last close $X · date" note = last completed bar | Last close $283.72 · Nov 16 | $283.72 · Nov 16 | PASS |  |  |
| GOOGL | L-now | ladder price row = compared price; name = the basis label | $279.84 "Now" | $279.84 "now" | PASS |  |  |
| GOOGL | L-sma200 | ladder row sma200: price and gap = price vs average | $337.93, -17.2% | $337.93, -17.2% | PASS |  |  |
| GOOGL | L-sma50 | ladder row sma50: price and gap = price vs average | $327.09, -14.4% | $327.09, -14.4% | PASS |  |  |
| GOOGL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $279.84 / entry $279.84 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GOOGL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GOOGL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.5 | 34.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GOOGL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.9% vs +10.1% | 2.9% vs 10.1% | PASS |  |  |
| GOOGL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GOOGL | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.1 | 26.1 | PASS |  | Wilder, completed bars |
| GOOGL | T4w | words "20 or more / below 20" | 20 or more | ADX 26.1 | PASS |  |  |
| GOOGL | T5 | "counted at the last close ($X, date)" = last completed bar | $283.72, Nov 16 | $283.72, Nov 16 | PASS |  |  |
| GOOGL | T6 | price vs 200-day average (S1 pattern sma values) | $283.72 vs $337.93 · -16.0% | $283.72 vs $337.93 · -16.0% | PASS |  |  |
| GOOGL | T6w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T7 | price vs 50-day average (S1 pattern sma values) | $283.72 vs $327.09 · -13.3% | $283.72 vs $327.09 · -13.3% | PASS |  |  |
| GOOGL | T7w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.2% over 30 td | -0.2% over 30 td | PASS |  |  |
| GOOGL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GOOGL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GOOGL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 30.5% below $408.10 | 30.5% below $408.10 | PASS |  | closing high would be 402.12 |
| GOOGL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 30.5% below | PASS |  |  |
| GOOGL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $408.10 | $408.10376741205215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GOOGL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.07%, close location 0.07, OBV falling |
| GOOGL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GOOGL | V2 | day change of the last completed bar | down 4.1% | -4.07% | PASS |  |  |
| GOOGL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0680) | PASS |  |  |
| GOOGL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GOOGL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.09× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| GOOGL | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.09× | 2026-11-16 1.09× | PASS |  |  |
| GOOGL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.09× / 1.10× | 1.09× / 1.10× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GOOGL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 34747200) | 20 bars, last ('2026-11-16', 34747200) | PASS |  |  |
| GRID | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $154.65 | $154.65 | PASS |  |  |
| GRID | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $163.67 | $163.67 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GRID | E3 | percent from the 21-day average | 5.5% below | 5.5% below | PASS |  |  |
| GRID | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| GRID | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.31 | $4.31 (sr=4.3086) | PASS |  | Wilder ATR14 |
| GRID | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| GRID | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| GRID | L-ema21 | ladder row ema21: price and gap = price vs average | $163.67, -5.5% | $163.67, -5.5% | PASS |  |  |
| GRID | L-note | "Last close $X · date" note = last completed bar | Last close $156.14 · Nov 16 | $156.14 · Nov 16 | PASS |  |  |
| GRID | L-now | ladder price row = compared price; name = the basis label | $154.65 "Now" | $154.65 "now" | PASS |  |  |
| GRID | L-sma200 | ladder row sma200: price and gap = price vs average | $178.67, -13.4% | $178.67, -13.4% | PASS |  |  |
| GRID | L-sma50 | ladder row sma50: price and gap = price vs average | $171.98, -10.1% | $171.98, -10.1% | PASS |  |  |
| GRID | S5-price | S5: the same live price reads the same on the header and the Entry block | header $154.65 / entry $154.65 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GRID | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GRID | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.3 | 38.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GRID | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.3% vs +10.1% | 2.2% vs 10.1% | PASS |  |  |
| GRID | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GRID | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.5 | 29.5 | PASS |  | Wilder, completed bars |
| GRID | T4w | words "20 or more / below 20" | 20 or more | ADX 29.5 | PASS |  |  |
| GRID | T5 | "counted at the last close ($X, date)" = last completed bar | $156.14, Nov 16 | $156.14, Nov 16 | PASS |  |  |
| GRID | T6 | price vs 200-day average (S1 pattern sma values) | $156.14 vs $178.67 · -12.6% | $156.14 vs $178.67 · -12.6% | PASS |  |  |
| GRID | T6w | word "Below" | Below | Below | PASS |  |  |
| GRID | T7 | price vs 50-day average (S1 pattern sma values) | $156.14 vs $171.98 · -9.2% | $156.14 vs $171.98 · -9.2% | PASS |  |  |
| GRID | T7w | word "Below" | Below | Below | PASS |  |  |
| GRID | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.9% over 30 td | +0.9% over 30 td | PASS |  |  |
| GRID | T8r | word "rising" | still rising | rising | PASS |  |  |
| GRID | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GRID | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 21.9% below $199.99 | 21.9% below $199.99 | PASS |  | closing high would be 199.80 |
| GRID | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 21.9% below | PASS |  |  |
| GRID | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $199.99 | $199.99001 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GRID | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.59%, close location 0.16, OBV falling |
| GRID | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| GRID | V2 | day change of the last completed bar | down 2.6% | -2.59% | PASS |  |  |
| GRID | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1586) | PASS |  |  |
| GRID | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GRID | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.13× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| GRID | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.13× | 2026-11-16 1.13× | PASS |  |  |
| GRID | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.13× / 0.94× | 1.13× / 0.94× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GRID | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 659400) | 20 bars, last ('2026-11-16', 659400) | PASS |  |  |
| HD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $338.76 | $338.76 | PASS |  |  |
| HD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $335.55 | $335.55 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HD | E3 | percent from the 21-day average | 1.0% above | 1.0% above | PASS |  |  |
| HD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| HD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.60 | $8.60 (sr=8.6008) | PASS |  | Wilder ATR14 |
| HD | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves above |
| HD | L-ema21 | ladder row ema21: price and gap = price vs average | $335.55, 1.0% | $335.55, 1.0% | PASS |  |  |
| HD | L-note | "Last close $X · date" note = last completed bar | Last close $347.51 · Nov 16 | $347.51 · Nov 16 | PASS |  |  |
| HD | L-now | ladder price row = compared price; name = the basis label | $338.76 "Now" | $338.76 "now" | PASS |  |  |
| HD | L-sma200 | ladder row sma200: price and gap = price vs average | $332.52, 1.9% | $332.52, 1.9% | PASS |  |  |
| HD | L-sma50 | ladder row sma50: price and gap = price vs average | $312.68, 8.3% | $312.68, 8.3% | PASS |  |  |
| HD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $338.76 / entry $338.76 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| HD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 62.8 | 62.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.1% vs +10.1% | -4.1% vs 10.1% | PASS |  |  |
| HD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HD | T4 | ADX 14 (S1 /api/sr meta.adx) | 44.5 | 44.5 | PASS |  | Wilder, completed bars |
| HD | T4w | words "20 or more / below 20" | 20 or more | ADX 44.5 | PASS |  |  |
| HD | T5 | "counted at the last close ($X, date)" = last completed bar | $347.51, Nov 16 | $347.51, Nov 16 | PASS |  |  |
| HD | T6 | price vs 200-day average (S1 pattern sma values) | $347.51 vs $332.52 · +4.5% | $347.51 vs $332.52 · 4.5% | PASS |  |  |
| HD | T6w | word "Above" | Above | Above | PASS |  |  |
| HD | T7 | price vs 50-day average (S1 pattern sma values) | $347.51 vs $312.68 · +11.1% | $347.51 vs $312.68 · 11.1% | PASS |  |  |
| HD | T7w | word "Above" | Above | Above | PASS |  |  |
| HD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.8% over 30 td | -1.8% over 30 td | PASS |  |  |
| HD | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.6% below $397.63 | 12.6% below $397.63 | PASS |  | closing high would be 391.05 |
| HD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.6% below | PASS |  |  |
| HD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $397.63 | $397.63 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.34%, close location 0.38, OBV falling |
| HD | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| HD | V2 | day change of the last completed bar | down 0.3% | -0.34% | PASS |  |  |
| HD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HD | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.2× from 2026-11-16 | 1.24× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| HD | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.24× | 2026-11-16 1.24× | PASS |  |  |
| HD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.24× / 0.14× | 1.24× / 0.14× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 6211595) | 20 bars, last ('2026-11-16', 6211595) | PASS |  |  |
| HURA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $37.54 | $37.54 | PASS |  |  |
| HURA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.82 | $40.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HURA.TO | E3 | percent from the 21-day average | 8.0% below | 8.0% below | PASS |  |  |
| HURA.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HURA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.46 | $1.46 (sr=1.4596) | PASS |  | Wilder ATR14 |
| HURA.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| HURA.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.5 | +8.5 | PASS |  |  |
| HURA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.82, -8.0% | $40.82, -8.0% | PASS |  |  |
| HURA.TO | L-now | ladder price row = compared price; name = the basis label | $37.54 "Last close" | $37.54 "last close" | PASS |  |  |
| HURA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $53.18, -29.4% | $53.18, -29.4% | PASS |  |  |
| HURA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $44.59, -15.8% | $44.59, -15.8% | PASS |  |  |
| HURA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HURA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.8 | 35.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HURA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -27.5% vs +10.1% | -27.5% vs 10.1% | PASS |  |  |
| HURA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HURA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.9 | 28.9 | PASS |  | Wilder, completed bars |
| HURA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.9 | PASS |  |  |
| HURA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $37.54 vs $53.18 · -29.4% | $37.54 vs $53.18 · -29.4% | PASS |  |  |
| HURA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $37.54 vs $44.59 · -15.8% | $37.54 vs $44.59 · -15.8% | PASS |  |  |
| HURA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.8% over 30 td | -4.8% over 30 td | PASS |  |  |
| HURA.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HURA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HURA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.2% below $73.95 | 49.2% below $73.95 | PASS |  | closing high would be 73.19 |
| HURA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.2% below | PASS |  |  |
| HURA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $73.95 | $73.94999694824219 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HURA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.79%, close location 0.00, OBV falling |
| HURA.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| HURA.TO | V2 | day change of the last completed bar | down 3.8% | -3.79% | PASS |  |  |
| HURA.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| HURA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HURA.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.13× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| HURA.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.13× | 2026-11-16 1.13× | PASS |  |  |
| HURA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.13× / 0.97× | 1.13× / 0.98× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HURA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 13600) | 20 bars, last ('2026-11-16', 13600) | PASS |  |  |
| HXQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $111.87 | $111.87 | PASS |  |  |
| HXQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $115.7 | $115.70 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HXQ.TO | E3 | percent from the 21-day average | 3.3% below | 3.3% below | PASS |  |  |
| HXQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HXQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.65 | $2.65 (sr=2.6506) | PASS |  | Wilder ATR14 |
| HXQ.TO | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| HXQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $115.7, -3.3% | $115.70, -3.3% | PASS |  |  |
| HXQ.TO | L-now | ladder price row = compared price; name = the basis label | $111.87 "Last close" | $111.87 "last close" | PASS |  |  |
| HXQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $112.18, -0.3% | $112.18, -0.3% | PASS |  |  |
| HXQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $119.33, -6.3% | $119.33, -6.3% | PASS |  |  |
| HXQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.5 | 40.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HXQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +11.9% vs +10.1% | 11.9% vs 10.1% | PASS |  |  |
| HXQ.TO | T3w | words "past year" vs the window used | 250 / 251 bars back | 250-253 bars | PASS |  |  |
| HXQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.7 | 30.7 | PASS |  | Wilder, completed bars |
| HXQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 30.7 | PASS |  |  |
| HXQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.49%, close location 0.04, OBV falling |
| HXQ.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| HXQ.TO | V2 | day change of the last completed bar | down 2.5% | -2.49% | PASS |  |  |
| HXQ.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0412) | PASS |  |  |
| HXQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HXQ.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 0.96× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| HXQ.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.96× | 2026-11-16 0.96× | PASS |  |  |
| HXQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.96× / 1.05× | 0.96× / 1.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HXQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 31400) | 20 bars, last ('2026-11-16', 31400) | PASS |  |  |
| JNJ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $278.95 | $278.95 | PASS |  |  |
| JNJ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $274.15 | $274.15 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JNJ | E3 | percent from the 21-day average | 1.8% above | 1.8% above | PASS |  |  |
| JNJ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| JNJ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.89 | $6.89 (sr=6.8937) | PASS |  | Wilder ATR14 |
| JNJ | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves above |
| JNJ | L-ema21 | ladder row ema21: price and gap = price vs average | $274.15, 1.8% | $274.15, 1.8% | PASS |  |  |
| JNJ | L-note | "Last close $X · date" note = last completed bar | Last close $282.55 · Nov 16 | $282.55 · Nov 16 | PASS |  |  |
| JNJ | L-now | ladder price row = compared price; name = the basis label | $278.95 "Now" | $278.95 "now" | PASS |  |  |
| JNJ | L-sma200 | ladder row sma200: price and gap = price vs average | $248.6, 12.2% | $248.60, 12.2% | PASS |  |  |
| JNJ | L-sma50 | ladder row sma50: price and gap = price vs average | $267.01, 4.5% | $267.01, 4.5% | PASS |  |  |
| JNJ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $278.95 / entry $278.95 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JNJ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JNJ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 61.3 | 61.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JNJ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +47.5% vs +10.1% | 47.5% vs 10.1% | PASS |  |  |
| JNJ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JNJ | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.0 | 26.1 | PASS |  | Wilder, completed bars |
| JNJ | T4w | words "20 or more / below 20" | 20 or more | ADX 26.1 | PASS |  |  |
| JNJ | T5 | "counted at the last close ($X, date)" = last completed bar | $282.55, Nov 16 | $282.55, Nov 16 | PASS |  |  |
| JNJ | T6w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T7 | price vs 50-day average (S1 pattern sma values) | $282.55 vs $267.01 · +5.8% | $282.55 vs $267.01 · 5.8% | PASS |  |  |
| JNJ | T7w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T8r | word "rising" | still rising | rising | PASS |  |  |
| JNJ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JNJ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.7% below $290.25 | 2.7% below $290.25 | PASS |  | closing high would be 285.75 |
| JNJ | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.7% below | PASS |  |  |
| JNJ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $290.25 | $290.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JNJ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.12%, close location 0.03, OBV flat |
| JNJ | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| JNJ | V2 | day change of the last completed bar | down 1.1% | -1.12% | PASS |  |  |
| JNJ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0278) | PASS |  |  |
| JNJ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| JNJ | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.11× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| JNJ | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.11× | 2026-11-16 1.11× | PASS |  |  |
| JNJ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.11× / 0.46× | 1.11× / 0.46× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JNJ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 8101700) | 20 bars, last ('2026-11-16', 8101700) | PASS |  |  |
| JPM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $329.83 | $329.83 | PASS |  |  |
| JPM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $340.05 | $340.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JPM | E3 | percent from the 21-day average | 3.0% below | 3.0% below | PASS |  |  |
| JPM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| JPM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.30 | $7.30 (sr=7.3048) | PASS |  | Wilder ATR14 |
| JPM | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| JPM | L-ema21 | ladder row ema21: price and gap = price vs average | $340.05, -3.0% | $340.05, -3.0% | PASS |  |  |
| JPM | L-note | "Last close $X · date" note = last completed bar | Last close $338.21 · Nov 16 | $338.21 · Nov 16 | PASS |  |  |
| JPM | L-now | ladder price row = compared price; name = the basis label | $329.83 "Now" | $329.83 "now" | PASS |  |  |
| JPM | L-sma200 | ladder row sma200: price and gap = price vs average | $325.02, 1.5% | $325.02, 1.5% | PASS |  |  |
| JPM | L-sma50 | ladder row sma50: price and gap = price vs average | $340.01, -3.0% | $340.01, -3.0% | PASS |  |  |
| JPM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $329.83 / entry $329.83 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JPM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JPM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.4 | 48.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JPM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +11.4% vs +10.1% | 11.4% vs 10.1% | PASS |  |  |
| JPM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JPM | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.4 | 17.4 | PASS |  | Wilder, completed bars |
| JPM | T4w | words "20 or more / below 20" | below 20 | ADX 17.4 | PASS |  |  |
| JPM | T5 | "counted at the last close ($X, date)" = last completed bar | $338.21, Nov 16 | $338.21, Nov 16 | PASS |  |  |
| JPM | T6 | price vs 200-day average (S1 pattern sma values) | $338.21 vs $325.02 · +4.1% | $338.21 vs $325.02 · 4.1% | PASS |  |  |
| JPM | T6w | word "Above" | Above | Above | PASS |  |  |
| JPM | T7 | price vs 50-day average (S1 pattern sma values) | $338.21 vs $340.01 · -0.5% | $338.21 vs $340.01 · -0.5% | PASS |  |  |
| JPM | T7w | word "Below" | Below | Below | PASS |  |  |
| JPM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.0% over 30 td | +1.0% over 30 td | PASS |  |  |
| JPM | T8r | word "rising" | still rising | rising | PASS |  |  |
| JPM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JPM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.7% below $366.50 | 7.7% below $366.50 | PASS |  | closing high would be 365.18 |
| JPM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.7% below | PASS |  |  |
| JPM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $366.50 | $366.5 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JPM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.31%, close location 0.16, OBV falling |
| JPM | V2 | day change of the last completed bar | down 2.3% | -2.31% | PASS |  |  |
| JPM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1563) | PASS |  |  |
| JPM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JPM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 0.96× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| JPM | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.96× | 2026-11-16 0.96× | PASS |  |  |
| JPM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.96× / 1.07× | 0.96× / 1.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JPM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 7229000) | 20 bars, last ('2026-11-16', 7229000) | PASS |  |  |
| KEYS | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $282.75 | $282.75 | PASS |  |  |
| KEYS | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $307.89 | $307.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| KEYS | E3 | percent from the 21-day average | 8.2% below | 8.2% below | PASS |  |  |
| KEYS | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| KEYS | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.16 | $16.16 (sr=16.1621) | PASS |  | Wilder ATR14 |
| KEYS | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| KEYS | L-ema21 | ladder row ema21: price and gap = price vs average | $307.89, -8.2% | $307.89, -8.2% | PASS |  |  |
| KEYS | L-note | "Last close $X · date" note = last completed bar | Last close $285.63 · Nov 16 | $285.63 · Nov 16 | PASS |  |  |
| KEYS | L-now | ladder price row = compared price; name = the basis label | $282.75 "Now" | $282.75 "now" | PASS |  |  |
| KEYS | L-sma200 | ladder row sma200: price and gap = price vs average | $320.81, -11.9% | $320.81, -11.9% | PASS |  |  |
| KEYS | L-sma50 | ladder row sma50: price and gap = price vs average | $334.19, -15.4% | $334.19, -15.4% | PASS |  |  |
| KEYS | S5-price | S5: the same live price reads the same on the header and the Entry block | header $282.75 / entry $282.75 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| KEYS | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| KEYS | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.4 | 39.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| KEYS | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +59.5% vs +10.1% | 59.5% vs 10.1% | PASS |  |  |
| KEYS | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| KEYS | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.3 | 35.3 | PASS |  | Wilder, completed bars |
| KEYS | T4w | words "20 or more / below 20" | 20 or more | ADX 35.3 | PASS |  |  |
| KEYS | T5 | "counted at the last close ($X, date)" = last completed bar | $285.63, Nov 16 | $285.63, Nov 16 | PASS |  |  |
| KEYS | T6 | price vs 200-day average (S1 pattern sma values) | $285.63 vs $320.81 · -11.0% | $285.63 vs $320.81 · -11.0% | PASS |  |  |
| KEYS | T6w | word "Below" | Below | Below | PASS |  |  |
| KEYS | T7 | price vs 50-day average (S1 pattern sma values) | $285.63 vs $334.19 · -14.5% | $285.63 vs $334.19 · -14.5% | PASS |  |  |
| KEYS | T7w | word "Below" | Below | Below | PASS |  |  |
| KEYS | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.7% over 30 td | +5.7% over 30 td | PASS |  |  |
| KEYS | T8r | word "rising" | still rising | rising | PASS |  |  |
| KEYS | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| KEYS | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.7% below $389.93 | 26.7% below $389.93 | PASS |  | closing high would be 388.03 |
| KEYS | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.7% below | PASS |  |  |
| KEYS | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $389.93 | $389.92999 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| KEYS | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -4.05%, close location 0.57, OBV falling |
| KEYS | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| KEYS | V2 | day change of the last completed bar | down 4.0% | -4.05% | PASS |  |  |
| KEYS | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| KEYS | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.7× from 2026-11-16 | 1.71× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| KEYS | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.71× | 2026-11-16 1.71× | PASS |  |  |
| KEYS | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.71× / 0.72× | 1.71× / 0.72× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| KEYS | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 2208400) | 20 bars, last ('2026-11-16', 2208400) | PASS |  |  |
| KEYS | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.71, OBV falling | condition true | PASS |  |  |
| LIN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $515.09 | $515.09 | PASS |  |  |
| LIN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $513.5 | $513.50 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LIN | E3 | percent from the 21-day average | 0.3% above | 0.3% above | PASS |  |  |
| LIN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| LIN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.87 | $8.87 (sr=8.8671) | PASS |  | Wilder ATR14 |
| LIN | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| LIN | L-ema21 | ladder row ema21: price and gap = price vs average | $513.5, 0.3% | $513.50, 0.3% | PASS |  |  |
| LIN | L-note | "Last close $X · date" note = last completed bar | Last close $523.46 · Nov 16 | $523.46 · Nov 16 | PASS |  |  |
| LIN | L-now | ladder price row = compared price; name = the basis label | $515.09 "Now" | $515.09 "now" | PASS |  |  |
| LIN | L-sma200 | ladder row sma200: price and gap = price vs average | $494.92, 4.1% | $494.92, 4.1% | PASS |  |  |
| LIN | L-sma50 | ladder row sma50: price and gap = price vs average | $491.12, 4.9% | $491.12, 4.9% | PASS |  |  |
| LIN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $515.09 / entry $515.09 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LIN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LIN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 61.9 | 61.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LIN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.3% vs +10.1% | 25.3% vs 10.1% | PASS |  |  |
| LIN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LIN | T4w | words "20 or more / below 20" | 20 or more | ADX 33.1 | PASS |  |  |
| LIN | T5 | "counted at the last close ($X, date)" = last completed bar | $523.46, Nov 16 | $523.46, Nov 16 | PASS |  |  |
| LIN | T6w | word "Above" | Above | Above | PASS |  |  |
| LIN | T7 | price vs 50-day average (S1 pattern sma values) | $523.46 vs $491.12 · +6.6% | $523.46 vs $491.12 · 6.6% | PASS |  |  |
| LIN | T7w | word "Above" | Above | Above | PASS |  |  |
| LIN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.3% over 30 td | PASS |  |  |
| LIN | T8r | word "rising" | still rising | rising | PASS |  |  |
| LIN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LIN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.2% below | PASS |  |  |
| LIN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.49%, close location 0.14, OBV falling |
| LIN | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| LIN | V2 | day change of the last completed bar | down 0.5% | -0.49% | PASS |  |  |
| LIN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1377) | PASS |  |  |
| LIN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| LIN | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 0.99× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| LIN | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.99× | 2026-11-16 0.99× | PASS |  |  |
| LIN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 0.29× | 0.99× / 0.29× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LIN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 2080000) | 20 bars, last ('2026-11-16', 2080000) | PASS |  |  |
| LLY | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,411.49 | $1,411.49 | PASS |  |  |
| LLY | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1363.41 | $1363.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LLY | E3 | percent from the 21-day average | 3.5% above | 3.5% above | PASS |  |  |
| LLY | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| LLY | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $44.55 | $44.55 (sr=44.5458) | PASS |  | Wilder ATR14 |
| LLY | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves above |
| LLY | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.7 | -5.7 | PASS |  |  |
| LLY | L-ema21 | ladder row ema21: price and gap = price vs average | $1363.41, 3.5% | $1363.41, 3.5% | PASS |  |  |
| LLY | L-now | ladder price row = compared price; name = the basis label | $1411.49 "Now" | $1411.49 "now" | PASS |  |  |
| LLY | L-sma200 | ladder row sma200: price and gap = price vs average | $1111.27, 27.0% | $1111.27, 27.0% | PASS |  |  |
| LLY | L-sma50 | ladder row sma50: price and gap = price vs average | $1246.72, 13.2% | $1246.72, 13.2% | PASS |  |  |
| LLY | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,411.49 / entry $1,411.49 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LLY | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LLY | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 66.8 | 66.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LLY | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.6% vs +10.1% | 39.6% vs 10.1% | PASS |  |  |
| LLY | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LLY | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.6 | 38.6 | PASS |  | Wilder, completed bars |
| LLY | T4w | words "20 or more / below 20" | 20 or more | ADX 38.6 | PASS |  |  |
| LLY | T5 | "counted at the last close ($X, date)" = last completed bar | $1,431.67, Nov 16 | $1431.67, Nov 16 | PASS |  |  |
| LLY | T6 | price vs 200-day average (S1 pattern sma values) | $1,431.67 vs $1,111.27 · +28.8% | $1431.67 vs $1111.27 · 28.8% | PASS |  |  |
| LLY | T6w | word "Above" | Above | Above | PASS |  |  |
| LLY | T7 | price vs 50-day average (S1 pattern sma values) | $1,431.67 vs $1,246.72 · +14.8% | $1431.67 vs $1246.72 · 14.8% | PASS |  |  |
| LLY | T7w | word "Above" | Above | Above | PASS |  |  |
| LLY | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.4% over 30 td | +3.4% over 30 td | PASS |  |  |
| LLY | T8r | word "rising" | still rising | rising | PASS |  |  |
| LLY | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LLY | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.0% below $1,475.25 | 3.0% below $1475.25 | PASS |  | closing high would be 1443.50 |
| LLY | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.0% below | PASS |  |  |
| LLY | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,475.25 | $1475.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LLY | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.82%, close location 0.08, OBV rising |
| LLY | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| LLY | V2 | day change of the last completed bar | down 0.8% | -0.82% | PASS |  |  |
| LLY | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0843) | PASS |  |  |
| LLY | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| LLY | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.2× from 2026-11-16 | 1.24× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| LLY | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.24× | 2026-11-16 1.24× | PASS |  |  |
| LLY | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.24× / 0.26× | 1.24× / 0.26× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LLY | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3209223) | 20 bars, last ('2026-11-16', 3209223) | PASS |  |  |
| MDA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.10 | $39.10 | PASS |  |  |
| MDA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.63 | $40.63 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MDA.TO | E3 | percent from the 21-day average | 3.8% below | 3.8% below | PASS |  |  |
| MDA.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| MDA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.28 | $2.28 (sr=2.2804) | PASS |  | Wilder ATR14 |
| MDA.TO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| MDA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.63, -3.8% | $40.63, -3.8% | PASS |  |  |
| MDA.TO | L-note | "Last close $X · date" note = last completed bar | Last close $40.08 · Nov 16 | $40.08 · Nov 16 | PASS |  |  |
| MDA.TO | L-now | ladder price row = compared price; name = the basis label | $39.1 "Now" | $39.10 "now" | PASS |  |  |
| MDA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $44.69, -12.5% | $44.69, -12.5% | PASS |  |  |
| MDA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $40.95, -4.5% | $40.95, -4.5% | PASS |  |  |
| MDA.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $39.10 / entry $39.10 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MDA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MDA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.3 | 48.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MDA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +80.0% vs +10.1% | 80.1% vs 10.1% | PASS |  |  |
| MDA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MDA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.3 | 25.3 | PASS |  | Wilder, completed bars |
| MDA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.3 | PASS |  |  |
| MDA.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $40.08, Nov 16 | $40.08, Nov 16 | PASS |  |  |
| MDA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $40.08 vs $44.69 · -10.3% | $40.08 vs $44.69 · -10.3% | PASS |  |  |
| MDA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $40.08 vs $40.95 · -2.1% | $40.08 vs $40.95 · -2.1% | PASS |  |  |
| MDA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| MDA.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MDA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MDA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 41.0% below $67.90 | 41.0% below $67.90 | PASS |  | closing high would be 67.13 |
| MDA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 41.0% below | PASS |  |  |
| MDA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $67.90 | $67.9000015258789 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MDA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -2.84%, close location 0.48, OBV rising |
| MDA.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MDA.TO | V2 | day change of the last completed bar | down 2.8% | -2.84% | PASS |  |  |
| MDA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| MDA.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.77× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| MDA.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.77× | 2026-11-16 0.77× | PASS |  |  |
| MDA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.77× / 0.50× | 0.77× / 0.50× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MDA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1266900) | 20 bars, last ('2026-11-16', 1266900) | PASS |  |  |
| META | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $617.41 | $617.41 | PASS |  |  |
| META | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $642.31 | $642.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| META | E3 | percent from the 21-day average | 3.9% below | 3.9% below | PASS |  |  |
| META | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| META | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $22.69 | $22.69 (sr=22.6918) | PASS |  | Wilder ATR14 |
| META | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| META | L-ema21 | ladder row ema21: price and gap = price vs average | $642.31, -3.9% | $642.31, -3.9% | PASS |  |  |
| META | L-note | "Last close $X · date" note = last completed bar | Last close $626.41 · Nov 16 | $626.41 · Nov 16 | PASS |  |  |
| META | L-now | ladder price row = compared price; name = the basis label | $617.41 "Now" | $617.41 "now" | PASS |  |  |
| META | L-sma200 | ladder row sma200: price and gap = price vs average | $630.32, -2.0% | $630.32, -2.0% | PASS |  |  |
| META | L-sma50 | ladder row sma50: price and gap = price vs average | $680, -9.2% | $680.00, -9.2% | PASS |  |  |
| META | S5-price | S5: the same live price reads the same on the header and the Entry block | header $617.41 / entry $617.41 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| META | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| META | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.9 | 43.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| META | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.8% vs +10.1% | 2.8% vs 10.1% | PASS |  |  |
| META | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| META | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.5 | 23.5 | PASS |  | Wilder, completed bars |
| META | T4w | words "20 or more / below 20" | 20 or more | ADX 23.5 | PASS |  |  |
| META | T5 | "counted at the last close ($X, date)" = last completed bar | $626.41, Nov 16 | $626.41, Nov 16 | PASS |  |  |
| META | T6 | price vs 200-day average (S1 pattern sma values) | $626.41 vs $630.32 · -0.6% | $626.41 vs $630.32 · -0.6% | PASS |  |  |
| META | T6w | word "Below" | Below | Below | PASS |  |  |
| META | T7 | price vs 50-day average (S1 pattern sma values) | $626.41 vs $680.00 · -7.9% | $626.41 vs $680.00 · -7.9% | PASS |  |  |
| META | T7w | word "Below" | Below | Below | PASS |  |  |
| META | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.2% over 30 td | +0.2% over 30 td | PASS |  |  |
| META | T8r | word "rising" | still rising | rising | PASS |  |  |
| META | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| META | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 19.7% below $779.82 | 19.7% below $779.82 | PASS |  | closing high would be 777.59 |
| META | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 19.7% below | PASS |  |  |
| META | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $779.82 | $779.82001 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| META | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.38%, close location 0.30, OBV falling |
| META | V2 | day change of the last completed bar | down 2.4% | -2.38% | PASS |  |  |
| META | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| META | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.5× from 2026-11-16 | 0.52× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| META | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.52× | 2026-11-16 0.52× | PASS |  |  |
| META | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.52× / 0.66× | 0.52× / 0.66× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| META | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 11541500) | 20 bars, last ('2026-11-16', 11541500) | PASS |  |  |
| METU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $21.52 | $21.52 | PASS |  |  |
| METU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $23.61 | $23.61 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| METU | E3 | percent from the 21-day average | 8.8% below | 8.8% below | PASS |  |  |
| METU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| METU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.68 | $1.68 (sr=1.6813) | PASS |  | Wilder ATR14 |
| METU | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| METU | L-ema21 | ladder row ema21: price and gap = price vs average | $23.61, -8.8% | $23.61, -8.8% | PASS |  |  |
| METU | L-note | "Last close $X · date" note = last completed bar | Last close $22.15 · Nov 16 | $22.15 · Nov 16 | PASS |  |  |
| METU | L-now | ladder price row = compared price; name = the basis label | $21.52 "Now" | $21.52 "now" | PASS |  |  |
| METU | L-sma200 | ladder row sma200: price and gap = price vs average | $25.54, -15.7% | $25.54, -15.7% | PASS |  |  |
| METU | L-sma50 | ladder row sma50: price and gap = price vs average | $26.97, -20.2% | $26.97, -20.2% | PASS |  |  |
| METU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $21.52 / entry $21.52 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| METU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| METU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.4 | 42.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| METU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -21.6% vs +10.1% | -21.6% vs 10.1% | PASS |  |  |
| METU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| METU | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.4 | 24.4 | PASS |  | Wilder, completed bars |
| METU | T4w | words "20 or more / below 20" | 20 or more | ADX 24.4 | PASS |  |  |
| METU | T5 | "counted at the last close ($X, date)" = last completed bar | $22.15, Nov 16 | $22.15, Nov 16 | PASS |  |  |
| METU | T6 | price vs 200-day average (S1 pattern sma values) | $22.15 vs $25.54 · -13.3% | $22.15 vs $25.54 · -13.3% | PASS |  |  |
| METU | T6w | word "Below" | Below | Below | PASS |  |  |
| METU | T7 | price vs 50-day average (S1 pattern sma values) | $22.15 vs $26.97 · -17.9% | $22.15 vs $26.97 · -17.9% | PASS |  |  |
| METU | T7w | word "Below" | Below | Below | PASS |  |  |
| METU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.4% over 30 td | -3.4% over 30 td | PASS |  |  |
| METU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| METU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| METU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 44.3% below $39.74 | 44.3% below $39.74 | PASS |  | closing high would be 39.22 |
| METU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 44.3% below | PASS |  |  |
| METU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $39.74 | $39.74 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| METU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -4.65%, close location 0.33, OBV falling |
| METU | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| METU | V2 | day change of the last completed bar | down 4.7% | -4.65% | PASS |  |  |
| METU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| METU | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.3× from 2026-11-16 | 0.27× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| METU | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.27× | 2026-11-16 0.27× | PASS |  |  |
| METU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.27× / 0.61× | 0.27× / 0.61× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| METU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1376058) | 20 bars, last ('2026-11-16', 1376058) | PASS |  |  |
| MRVL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $146.50 | $146.50 | PASS |  |  |
| MRVL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $185.25 | $185.25 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MRVL | E3 | percent from the 21-day average | 20.9% below | 20.9% below | PASS |  |  |
| MRVL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| MRVL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.85 | $16.85 (sr=16.8536) | PASS |  | Wilder ATR14 |
| MRVL | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| MRVL | L-ema21 | ladder row ema21: price and gap = price vs average | $185.25, -20.9% | $185.25, -20.9% | PASS |  |  |
| MRVL | L-note | "Last close $X · date" note = last completed bar | Last close $145.36 · Nov 16 | $145.36 · Nov 16 | PASS |  |  |
| MRVL | L-now | ladder price row = compared price; name = the basis label | $146.5 "Now" | $146.50 "now" | PASS |  |  |
| MRVL | L-sma200 | ladder row sma200: price and gap = price vs average | $187.33, -21.8% | $187.33, -21.8% | PASS |  |  |
| MRVL | L-sma50 | ladder row sma50: price and gap = price vs average | $227.64, -35.6% | $227.64, -35.6% | PASS |  |  |
| MRVL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $146.50 / entry $146.50 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MRVL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MRVL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.5 | 32.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MRVL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +68.1% vs +10.1% | 68.1% vs 10.1% | PASS |  |  |
| MRVL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MRVL | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.3 | 31.3 | PASS |  | Wilder, completed bars |
| MRVL | T4w | words "20 or more / below 20" | 20 or more | ADX 31.3 | PASS |  |  |
| MRVL | T5 | "counted at the last close ($X, date)" = last completed bar | $145.36, Nov 16 | $145.36, Nov 16 | PASS |  |  |
| MRVL | T6 | price vs 200-day average (S1 pattern sma values) | $145.36 vs $187.33 · -22.4% | $145.36 vs $187.33 · -22.4% | PASS |  |  |
| MRVL | T6w | word "Below" | Below | Below | PASS |  |  |
| MRVL | T7 | price vs 50-day average (S1 pattern sma values) | $145.36 vs $227.64 · -36.1% | $145.36 vs $227.64 · -36.1% | PASS |  |  |
| MRVL | T7w | word "Below" | Below | Below | PASS |  |  |
| MRVL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +11.6% over 30 td | +11.6% over 30 td | PASS |  |  |
| MRVL | T8r | word "rising" | still rising | rising | PASS |  |  |
| MRVL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MRVL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 55.9% below $329.88 | 55.9% below $329.88 | PASS |  | closing high would be 316.43 |
| MRVL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 55.9% below | PASS |  |  |
| MRVL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $329.88 | $329.88 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MRVL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -7.27%, close location 0.26, OBV falling |
| MRVL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MRVL | V2 | day change of the last completed bar | down 7.3% | -7.27% | PASS |  |  |
| MRVL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MRVL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 0.97× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| MRVL | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.97× | 2026-11-16 0.97× | PASS |  |  |
| MRVL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.97× / 0.63× | 0.97× / 0.63× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MRVL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 23235481) | 20 bars, last ('2026-11-16', 23235481) | PASS |  |  |
| MSFT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $504.93 | $504.93 | PASS |  |  |
| MSFT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $527.18 | $527.18 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFT | E3 | percent from the 21-day average | 4.2% below | 4.2% below | PASS |  |  |
| MSFT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| MSFT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $14.93 | $14.93 (sr=14.9256) | PASS |  | Wilder ATR14 |
| MSFT | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| MSFT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.7 | -5.7 | PASS |  |  |
| MSFT | L-ema21 | ladder row ema21: price and gap = price vs average | $527.18, -4.2% | $527.18, -4.2% | PASS |  |  |
| MSFT | L-note | "Last close $X · date" note = last completed bar | Last close $517.99 · Nov 16 | $517.99 · Nov 16 | PASS |  |  |
| MSFT | L-now | ladder price row = compared price; name = the basis label | $504.93 "Now" | $504.93 "now" | PASS |  |  |
| MSFT | L-sma200 | ladder row sma200: price and gap = price vs average | $441.86, 14.3% | $441.86, 14.3% | PASS |  |  |
| MSFT | L-sma50 | ladder row sma50: price and gap = price vs average | $519.36, -2.8% | $519.36, -2.8% | PASS |  |  |
| MSFT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $504.93 / entry $504.93 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.4 | 46.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +1.5% vs +10.1% | 1.5% vs 10.1% | PASS |  |  |
| MSFT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFT | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.7 | 16.7 | PASS |  | Wilder, completed bars |
| MSFT | T4w | words "20 or more / below 20" | below 20 | ADX 16.7 | PASS |  |  |
| MSFT | T5 | "counted at the last close ($X, date)" = last completed bar | $517.99, Nov 16 | $517.99, Nov 16 | PASS |  |  |
| MSFT | T6 | price vs 200-day average (S1 pattern sma values) | $517.99 vs $441.86 · +17.2% | $517.99 vs $441.86 · 17.2% | PASS |  |  |
| MSFT | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFT | T7 | price vs 50-day average (S1 pattern sma values) | $517.99 vs $519.36 · -0.3% | $517.99 vs $519.36 · -0.3% | PASS |  |  |
| MSFT | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.0% over 30 td | +2.0% over 30 td | PASS |  |  |
| MSFT | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.4% below $559.15 | 7.4% below $559.15 | PASS |  | closing high would be 555.80 |
| MSFT | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.4% below | PASS |  |  |
| MSFT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $559.15 | $559.15002 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.12%, close location 0.11, OBV falling |
| MSFT | V2 | day change of the last completed bar | down 1.1% | -1.12% | PASS |  |  |
| MSFT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1051) | PASS |  |  |
| MSFT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFT | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-16 | 1.28× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| MSFT | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.28× | 2026-11-16 1.28× | PASS |  |  |
| MSFT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.28× / 0.39× | 1.28× / 0.39× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 30198800) | 20 bars, last ('2026-11-16', 30198800) | PASS |  |  |
| MSFU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $37.24 | $37.24 | PASS |  |  |
| MSFU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.94 | $40.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFU | E3 | percent from the 21-day average | 9.0% below | 9.0% below | PASS |  |  |
| MSFU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| MSFU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.28 | $2.28 (sr=2.2799) | PASS |  | Wilder ATR14 |
| MSFU | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| MSFU | L-ema21 | ladder row ema21: price and gap = price vs average | $40.94, -9.0% | $40.94, -9.0% | PASS |  |  |
| MSFU | L-note | "Last close $X · date" note = last completed bar | Last close $39.17 · Nov 16 | $39.17 · Nov 16 | PASS |  |  |
| MSFU | L-now | ladder price row = compared price; name = the basis label | $37.24 "Now" | $37.23 "now" | PASS |  |  |
| MSFU | L-sma200 | ladder row sma200: price and gap = price vs average | $31.31, 18.9% | $31.31, 18.9% | PASS |  |  |
| MSFU | L-sma50 | ladder row sma50: price and gap = price vs average | $40.19, -7.4% | $40.19, -7.4% | PASS |  |  |
| MSFU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $37.24 / entry $37.24 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.1 | 45.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -21.2% vs +10.1% | -21.2% vs 10.1% | PASS |  |  |
| MSFU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFU | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.5 | 16.5 | PASS |  | Wilder, completed bars |
| MSFU | T4w | words "20 or more / below 20" | below 20 | ADX 16.5 | PASS |  |  |
| MSFU | T5 | "counted at the last close ($X, date)" = last completed bar | $39.17, Nov 16 | $39.17, Nov 16 | PASS |  |  |
| MSFU | T6 | price vs 200-day average (S1 pattern sma values) | $39.17 vs $31.31 · +25.1% | $39.17 vs $31.31 · 25.1% | PASS |  |  |
| MSFU | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFU | T7 | price vs 50-day average (S1 pattern sma values) | $39.17 vs $40.19 · -2.5% | $39.17 vs $40.19 · -2.5% | PASS |  |  |
| MSFU | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.1% over 30 td | +1.1% over 30 td | PASS |  |  |
| MSFU | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 21.7% below $50.05 | 21.7% below $50.05 | PASS |  | closing high would be 49.69 |
| MSFU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 21.7% below | PASS |  |  |
| MSFU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $50.05 | $50.05 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.39%, close location 0.11, OBV falling |
| MSFU | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MSFU | V2 | day change of the last completed bar | down 2.4% | -2.39% | PASS |  |  |
| MSFU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1138) | PASS |  |  |
| MSFU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFU | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.75× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| MSFU | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.75× | 2026-11-16 0.75× | PASS |  |  |
| MSFU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.75× / 0.41× | 0.75× / 0.41× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1832527) | 20 bars, last ('2026-11-16', 1832527) | PASS |  |  |
| MTRX.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $29.13 | $29.13 | PASS |  |  |
| MTRX.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $31.36 | $31.36 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MTRX.TO | E3 | percent from the 21-day average | 7.1% below | 7.1% below | PASS |  |  |
| MTRX.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 3:56pm ET) | session=regular | PASS |  |  |
| MTRX.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.02 | $1.02 (sr=1.0223) | PASS |  | Wilder ATR14 |
| MTRX.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| MTRX.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $31.36, -7.1% | $31.36, -7.1% | PASS |  |  |
| MTRX.TO | L-note | "Last close $X · date" note = last completed bar | Last close $29.24 · Nov 16 | $29.24 · Nov 16 | PASS |  |  |
| MTRX.TO | L-now | ladder price row = compared price; name = the basis label | $29.13 "Last trade 3:56pm ET" | $29.13 "last trade 3:56pm et" | PASS |  |  |
| MTRX.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $34.35, -15.2% | $34.35, -15.2% | PASS |  |  |
| MTRX.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $33.69, -13.5% | $33.69, -13.5% | PASS |  |  |
| MTRX.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $29.13 / entry $29.13 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MTRX.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.0 | 38.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MTRX.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.7% vs +10.1% | -1.7% vs 10.1% | PASS |  |  |
| MTRX.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.5 | 27.5 | PASS |  | Wilder, completed bars |
| MTRX.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.5 | PASS |  |  |
| MTRX.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.41%, close location 0.06, OBV falling |
| MTRX.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MTRX.TO | V2 | day change of the last completed bar | down 4.4% | -4.41% | PASS |  |  |
| MTRX.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0625) | PASS |  |  |
| MTRX.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MTRX.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.4× from 2026-11-16 | 0.38× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| MTRX.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.38× | 2026-11-16 0.38× | PASS |  |  |
| MTRX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.38× / 1.26× | 0.38× / 1.26× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MTRX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3600) | 20 bars, last ('2026-11-16', 3600) | PASS |  |  |
| MU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.74 | $30.74 | PASS |  |  |
| MU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $36.07 | $36.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MU.TO | E3 | percent from the 21-day average | 14.8% below | 14.8% below | PASS |  |  |
| MU.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| MU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.55 | $2.55 (sr=2.554) | PASS |  | Wilder ATR14 |
| MU.TO | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| MU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $36.07, -14.8% | $36.07, -14.8% | PASS |  |  |
| MU.TO | L-note | "Last close $X · date" note = last completed bar | Last close $31.43 · Nov 16 | $31.43 · Nov 16 | PASS |  |  |
| MU.TO | L-now | ladder price row = compared price; name = the basis label | $30.74 "Now" | $30.74 "now" | PASS |  |  |
| MU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.74, -8.9% | $33.74, -8.9% | PASS |  |  |
| MU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $41.08, -25.2% | $41.08, -25.2% | PASS |  |  |
| MU.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $30.74 / entry $30.74 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.9 | 37.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +184.2% vs +10.1% | 184.2% vs 10.1% | PASS |  |  |
| MU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.5 | 34.5 | PASS |  | Wilder, completed bars |
| MU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 34.5 | PASS |  |  |
| MU.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $31.43, Nov 16 | $31.43, Nov 16 | PASS |  |  |
| MU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $31.43 vs $33.74 · -6.8% | $31.43 vs $33.74 · -6.8% | PASS |  |  |
| MU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $31.43 vs $41.08 · -23.5% | $31.43 vs $41.08 · -23.5% | PASS |  |  |
| MU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +11.8% over 30 td | +11.8% over 30 td | PASS |  |  |
| MU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 43.1% below $55.28 | 43.1% below $55.28 | PASS |  | closing high would be 53.52 |
| MU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 43.1% below | PASS |  |  |
| MU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $55.28 | $55.282308204978015 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.53%, close location 0.14, OBV falling |
| MU.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| MU.TO | V2 | day change of the last completed bar | down 7.5% | -7.53% | PASS |  |  |
| MU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1354) | PASS |  |  |
| MU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MU.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 0.97× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| MU.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.97× | 2026-11-16 0.97× | PASS |  |  |
| MU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.97× / 0.93× | 0.97× / 0.93× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1792600) | 20 bars, last ('2026-11-16', 1792600) | PASS |  |  |
| NEE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $84.45 | $84.45 | PASS |  |  |
| NEE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $84.05 | $84.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEE | E3 | percent from the 21-day average | 0.5% above | 0.5% above | PASS |  |  |
| NEE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NEE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.68 | $1.68 (sr=1.6785) | PASS |  | Wilder ATR14 |
| NEE | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| NEE | L-ema21 | ladder row ema21: price and gap = price vs average | $84.05, 0.5% | $84.05, 0.5% | PASS |  |  |
| NEE | L-note | "Last close $X · date" note = last completed bar | Last close $85.34 · Nov 16 | $85.34 · Nov 16 | PASS |  |  |
| NEE | L-now | ladder price row = compared price; name = the basis label | $84.45 "Now" | $84.44 "now" | PASS |  |  |
| NEE | L-sma200 | ladder row sma200: price and gap = price vs average | $86.53, -2.4% | $86.53, -2.4% | PASS |  |  |
| NEE | L-sma50 | ladder row sma50: price and gap = price vs average | $80.85, 4.5% | $80.85, 4.5% | PASS |  |  |
| NEE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $84.45 / entry $84.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 58.8 | 58.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.7% vs +10.1% | 4.7% vs 10.1% | PASS |  |  |
| NEE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEE | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.6 | 32.6 | PASS |  | Wilder, completed bars |
| NEE | T4w | words "20 or more / below 20" | 20 or more | ADX 32.6 | PASS |  |  |
| NEE | T5 | "counted at the last close ($X, date)" = last completed bar | $85.34, Nov 16 | $85.34, Nov 16 | PASS |  |  |
| NEE | T6w | word "Below" | Below | Below | PASS |  |  |
| NEE | T7 | price vs 50-day average (S1 pattern sma values) | $85.34 vs $80.85 · +5.6% | $85.34 vs $80.85 · 5.6% | PASS |  |  |
| NEE | T7w | word "Above" | Above | Above | PASS |  |  |
| NEE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.3% below | PASS |  |  |
| NEE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.26%, close location 0.56, OBV falling |
| NEE | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NEE | V2 | day change of the last completed bar | up 0.3% | +0.26% | PASS |  |  |
| NEE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NEE | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-16 | 0.94× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| NEE | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.94× | 2026-11-16 0.94× | PASS |  |  |
| NEE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.94× / 0.13× | 0.94× / 0.13× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 11825200) | 20 bars, last ('2026-11-16', 11825200) | PASS |  |  |
| NEM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $110.83 | $110.83 | PASS |  |  |
| NEM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $115.3 | $115.30 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEM | E3 | percent from the 21-day average | 3.9% below | 3.9% below | PASS |  |  |
| NEM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NEM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.54 | $4.54 (sr=4.5356) | PASS |  | Wilder ATR14 |
| NEM | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| NEM | L-ema21 | ladder row ema21: price and gap = price vs average | $115.3, -3.9% | $115.30, -3.9% | PASS |  |  |
| NEM | L-note | "Last close $X · date" note = last completed bar | Last close $110.31 · Nov 16 | $110.31 · Nov 16 | PASS |  |  |
| NEM | L-now | ladder price row = compared price; name = the basis label | $110.83 "Now" | $110.83 "now" | PASS |  |  |
| NEM | L-sma200 | ladder row sma200: price and gap = price vs average | $112.13, -1.2% | $112.13, -1.2% | PASS |  |  |
| NEM | L-sma50 | ladder row sma50: price and gap = price vs average | $117.68, -5.8% | $117.68, -5.8% | PASS |  |  |
| NEM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $110.83 / entry $110.83 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.1 | 43.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.6% vs +10.1% | 25.6% vs 10.1% | PASS |  |  |
| NEM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEM | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.2 | 16.2 | PASS |  | Wilder, completed bars |
| NEM | T4w | words "20 or more / below 20" | below 20 | ADX 16.2 | PASS |  |  |
| NEM | T5 | "counted at the last close ($X, date)" = last completed bar | $110.31, Nov 16 | $110.31, Nov 16 | PASS |  |  |
| NEM | T6 | price vs 200-day average (S1 pattern sma values) | $110.31 vs $112.13 · -1.6% | $110.31 vs $112.13 · -1.6% | PASS |  |  |
| NEM | T6w | word "Below" | Below | Below | PASS |  |  |
| NEM | T7 | price vs 50-day average (S1 pattern sma values) | $110.31 vs $117.68 · -6.3% | $110.31 vs $117.68 · -6.3% | PASS |  |  |
| NEM | T7w | word "Below" | Below | Below | PASS |  |  |
| NEM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.5% over 30 td | +0.5% over 30 td | PASS |  |  |
| NEM | T8r | word "rising" | still rising | rising | PASS |  |  |
| NEM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 18.5% below $135.29 | 18.5% below $135.29 | PASS |  | closing high would be 135.14 |
| NEM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 18.5% below | PASS |  |  |
| NEM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $135.29 | $135.29 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.50%, close location 0.04, OBV rising |
| NEM | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NEM | V2 | day change of the last completed bar | down 2.5% | -2.50% | PASS |  |  |
| NEM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0450) | PASS |  |  |
| NEM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| NEM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-16 | 0.90× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| NEM | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.90× | 2026-11-16 0.90× | PASS |  |  |
| NEM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.90× / 0.61× | 0.90× / 0.61× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 5804493) | 20 bars, last ('2026-11-16', 5804493) | PASS |  |  |
| NFLX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $59.56 | $59.56 | PASS |  |  |
| NFLX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $64.55 | $64.55 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFLX | E3 | percent from the 21-day average | 7.7% below | 7.7% below | PASS |  |  |
| NFLX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NFLX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.97 | $1.97 (sr=1.9739) | PASS |  | Wilder ATR14 |
| NFLX | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| NFLX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.0 | +8.0 | PASS |  |  |
| NFLX | L-ema21 | ladder row ema21: price and gap = price vs average | $64.55, -7.7% | $64.55, -7.7% | PASS |  |  |
| NFLX | L-note | "Last close $X · date" note = last completed bar | Last close $60.75 · Nov 16 | $60.75 · Nov 16 | PASS |  |  |
| NFLX | L-now | ladder price row = compared price; name = the basis label | $59.56 "Now" | $59.55 "now" | PASS |  |  |
| NFLX | L-sma200 | ladder row sma200: price and gap = price vs average | $80.38, -25.9% | $80.38, -25.9% | PASS |  |  |
| NFLX | L-sma50 | ladder row sma50: price and gap = price vs average | $68.83, -13.5% | $68.83, -13.5% | PASS |  |  |
| NFLX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $59.56 / entry $59.56 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFLX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFLX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.2 | 35.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFLX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -45.4% vs +10.1% | -45.4% vs 10.1% | PASS |  |  |
| NFLX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFLX | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.6 | 23.6 | PASS |  | Wilder, completed bars |
| NFLX | T4w | words "20 or more / below 20" | 20 or more | ADX 23.6 | PASS |  |  |
| NFLX | T5 | "counted at the last close ($X, date)" = last completed bar | $60.75, Nov 16 | $60.75, Nov 16 | PASS |  |  |
| NFLX | T6 | price vs 200-day average (S1 pattern sma values) | $60.75 vs $80.38 · -24.4% | $60.75 vs $80.38 · -24.4% | PASS |  |  |
| NFLX | T6w | word "Below" | Below | Below | PASS |  |  |
| NFLX | T7 | price vs 50-day average (S1 pattern sma values) | $60.75 vs $68.83 · -11.7% | $60.75 vs $68.83 · -11.7% | PASS |  |  |
| NFLX | T7w | word "Below" | Below | Below | PASS |  |  |
| NFLX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.2% over 30 td | -4.2% over 30 td | PASS |  |  |
| NFLX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFLX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFLX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 47.3% below $115.25 | 47.3% below $115.25 | PASS |  | closing high would be 114.09 |
| NFLX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 47.3% below | PASS |  |  |
| NFLX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $115.25 | $115.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFLX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.25%, close location 0.11, OBV falling |
| NFLX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NFLX | V2 | day change of the last completed bar | down 2.3% | -2.25% | PASS |  |  |
| NFLX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1080) | PASS |  |  |
| NFLX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFLX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-16 | 0.91× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| NFLX | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.91× | 2026-11-16 0.91× | PASS |  |  |
| NFLX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.91× / 0.69× | 0.91× / 0.69× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFLX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 36078360) | 20 bars, last ('2026-11-16', 36078360) | PASS |  |  |
| NFXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $9.84 | $9.84 | PASS |  |  |
| NFXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $11.7 | $11.70 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFXL | E3 | percent from the 21-day average | 15.9% below | 15.9% below | PASS |  |  |
| NFXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NFXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.72 | $0.73 (sr=0.7243) | PASS |  | Wilder ATR14 |
| NFXL | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| NFXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.1 | +12.1 | PASS |  |  |
| NFXL | L-ema21 | ladder row ema21: price and gap = price vs average | $11.7, -15.9% | $11.70, -15.9% | PASS |  |  |
| NFXL | L-note | "Last close $X · date" note = last completed bar | Last close $10.22 · Nov 16 | $10.22 · Nov 16 | PASS |  |  |
| NFXL | L-now | ladder price row = compared price; name = the basis label | $9.84 "Now" | $9.84 "now" | PASS |  |  |
| NFXL | L-sma200 | ladder row sma200: price and gap = price vs average | $20.49, -52.0% | $20.49, -52.0% | PASS |  |  |
| NFXL | L-sma50 | ladder row sma50: price and gap = price vs average | $13.55, -27.4% | $13.55, -27.4% | PASS |  |  |
| NFXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $9.84 / entry $9.84 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.4 | 34.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -78.1% vs +10.1% | -78.1% vs 10.1% | PASS |  |  |
| NFXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.8 | 25.7 | PASS |  | Wilder, completed bars |
| NFXL | T4w | words "20 or more / below 20" | 20 or more | ADX 25.7 | PASS |  |  |
| NFXL | T5 | "counted at the last close ($X, date)" = last completed bar | $10.22, Nov 16 | $10.22, Nov 16 | PASS |  |  |
| NFXL | T6 | price vs 200-day average (S1 pattern sma values) | $10.22 vs $20.49 · -50.1% | $10.22 vs $20.49 · -50.1% | PASS |  |  |
| NFXL | T6w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T7 | price vs 50-day average (S1 pattern sma values) | $10.22 vs $13.55 · -24.6% | $10.22 vs $13.55 · -24.6% | PASS |  |  |
| NFXL | T7w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -10.3% over 30 td | -10.3% over 30 td | PASS |  |  |
| NFXL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 79.5% below $49.78 | 79.5% below $49.78 | PASS |  | closing high would be 48.83 |
| NFXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 79.5% below | PASS |  |  |
| NFXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $49.78 | $49.7801 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.66%, close location 0.11, OBV falling |
| NFXL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NFXL | V2 | day change of the last completed bar | down 4.7% | -4.66% | PASS |  |  |
| NFXL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1084) | PASS |  |  |
| NFXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFXL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.5× from 2026-11-16 | 1.47× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| NFXL | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.47× | 2026-11-16 1.47× | PASS |  |  |
| NFXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.47× / 0.66× | 1.47× / 0.66× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 2404995) | 20 bars, last ('2026-11-16', 2404995) | PASS |  |  |
| NTR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $98.62 | $98.62 | PASS |  |  |
| NTR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $99.89 | $99.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NTR.TO | E3 | percent from the 21-day average | 1.3% below | 1.3% below | PASS |  |  |
| NTR.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| NTR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.86 | $2.86 (sr=2.8588) | PASS |  | Wilder ATR14 |
| NTR.TO | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| NTR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $99.89, -1.3% | $99.89, -1.3% | PASS |  |  |
| NTR.TO | L-now | ladder price row = compared price; name = the basis label | $98.62 "Last close" | $98.62 "last close" | PASS |  |  |
| NTR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $97.72, 0.9% | $97.72, 0.9% | PASS |  |  |
| NTR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $101.52, -2.9% | $101.52, -2.9% | PASS |  |  |
| NTR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.9 | 45.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NTR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +27.2% vs +10.1% | 27.2% vs 10.1% | PASS |  |  |
| NTR.TO | T3w | words "past year" vs the window used | 250 / 251 bars back | 250-253 bars | PASS |  |  |
| NTR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.5 | 18.5 | PASS |  | Wilder, completed bars |
| NTR.TO | T4w | words "20 or more / below 20" | below 20 | ADX 18.5 | PASS |  |  |
| NTR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.95%, close location 0.06, OBV rising |
| NTR.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NTR.TO | V2 | day change of the last completed bar | down 3.0% | -2.95% | PASS |  |  |
| NTR.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0594) | PASS |  |  |
| NTR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| NTR.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.4× from 2026-11-16 | 0.42× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| NTR.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.42× | 2026-11-16 0.42× | PASS |  |  |
| NTR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.42× / 1.02× | 0.42× / 1.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NTR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 813800) | 20 bars, last ('2026-11-16', 813800) | PASS |  |  |
| NVDA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $153.91 | $153.91 | PASS |  |  |
| NVDA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $190.71 | $190.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDA | E3 | percent from the 21-day average | 19.3% below | 19.3% below | PASS |  |  |
| NVDA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NVDA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.85 | $9.85 (sr=9.8532) | PASS |  | Wilder ATR14 |
| NVDA | E5 | distance in normal day-moves | 3.7 | 3.7 | PASS |  | gauge dot note uses the same number:  · 3.7 day-moves below |
| NVDA | L-ema21 | ladder row ema21: price and gap = price vs average | $190.71, -19.3% | $190.71, -19.3% | PASS |  |  |
| NVDA | L-note | "Last close $X · date" note = last completed bar | Last close $156.14 · Nov 16 | $156.14 · Nov 16 | PASS |  |  |
| NVDA | L-now | ladder price row = compared price; name = the basis label | $153.91 "Now" | $153.91 "now" | PASS |  |  |
| NVDA | L-sma200 | ladder row sma200: price and gap = price vs average | $204.02, -24.6% | $204.02, -24.6% | PASS |  |  |
| NVDA | L-sma50 | ladder row sma50: price and gap = price vs average | $213.16, -27.8% | $213.16, -27.8% | PASS |  |  |
| NVDA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $153.91 / entry $153.91 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| NVDL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $15.92 | $15.92 | PASS |  |  |
| NVDL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $25.41 | $25.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDL | E3 | percent from the 21-day average | 37.4% below | 37.4% below | PASS |  |  |
| NVDL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| NVDL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.58 | $2.58 (sr=2.5809) | PASS |  | Wilder ATR14 |
| NVDL | E5 | distance in normal day-moves | 3.7 | 3.7 | PASS |  | gauge dot note uses the same number:  · 3.7 day-moves below |
| NVDL | L-ema21 | ladder row ema21: price and gap = price vs average | $25.41, -37.4% | $25.41, -37.4% | PASS |  |  |
| NVDL | L-note | "Last close $X · date" note = last completed bar | Last close $16.35 · Nov 16 | $16.35 · Nov 16 | PASS |  |  |
| NVDL | L-now | ladder price row = compared price; name = the basis label | $15.92 "Now" | $15.92 "now" | PASS |  |  |
| NVDL | L-sma200 | ladder row sma200: price and gap = price vs average | $21.3, -25.2% | $21.30, -25.2% | PASS |  |  |
| NVDL | L-sma50 | ladder row sma50: price and gap = price vs average | $32.05, -50.3% | $32.05, -50.3% | PASS |  |  |
| NVDL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $15.92 / entry $15.92 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.8 | 22.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +56.6% vs +10.1% | 56.6% vs 10.1% | PASS |  |  |
| NVDL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDL | T4 | ADX 14 (S1 /api/sr meta.adx) | 44.1 | 44.1 | PASS |  | Wilder, completed bars |
| NVDL | T4w | words "20 or more / below 20" | 20 or more | ADX 44.1 | PASS |  |  |
| NVDL | T5 | "counted at the last close ($X, date)" = last completed bar | $16.35, Nov 16 | $16.35, Nov 16 | PASS |  |  |
| NVDL | T6 | price vs 200-day average (S1 pattern sma values) | $16.35 vs $21.30 · -23.2% | $16.35 vs $21.30 · -23.2% | PASS |  |  |
| NVDL | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T7 | price vs 50-day average (S1 pattern sma values) | $16.35 vs $32.05 · -49.0% | $16.35 vs $32.05 · -49.0% | PASS |  |  |
| NVDL | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +16.5% over 30 td | +16.4% over 30 td | PASS |  |  |
| NVDL | T8r | word "rising" | still rising | rising | PASS |  |  |
| NVDL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 60.7% below $41.59 | 60.7% below $41.59 | PASS |  | closing high would be 40.17 |
| NVDL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 60.7% below | PASS |  |  |
| NVDL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $41.59 | $41.59 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -8.30%, close location 0.15, OBV falling |
| NVDL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| NVDL | V2 | day change of the last completed bar | down 8.3% | -8.30% | PASS |  |  |
| NVDL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1455) | PASS |  |  |
| NVDL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 2.6× from 2026-11-16 | 2.61× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| NVDL | V6 | Volume detail: last session date and RVOL | 2026-11-16 2.61× | 2026-11-16 2.61× | PASS |  |  |
| NVDL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.61× / 0.53× | 2.61× / 0.53× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 43150977) | 20 bars, last ('2026-11-16', 43150977) | PASS |  |  |
| NVDL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.61, OBV falling | condition true | PASS |  |  |
| ONTO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $198.10 | $198.10 | PASS |  |  |
| ONTO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $209.82 | $209.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ONTO | E3 | percent from the 21-day average | 5.6% below | 5.6% below | PASS |  |  |
| ONTO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| ONTO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.97 | $17.97 (sr=17.968) | PASS |  | Wilder ATR14 |
| ONTO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| ONTO | L-ema21 | ladder row ema21: price and gap = price vs average | $209.82, -5.6% | $209.82, -5.6% | PASS |  |  |
| ONTO | L-note | "Last close $X · date" note = last completed bar | Last close $196.77 · Nov 16 | $196.77 · Nov 16 | PASS |  |  |
| ONTO | L-now | ladder price row = compared price; name = the basis label | $198.1 "Now" | $198.10 "now" | PASS |  |  |
| ONTO | L-sma200 | ladder row sma200: price and gap = price vs average | $259.97, -23.8% | $259.97, -23.8% | PASS |  |  |
| ONTO | L-sma50 | ladder row sma50: price and gap = price vs average | $246.63, -19.7% | $246.63, -19.7% | PASS |  |  |
| ONTO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $198.10 / entry $198.10 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ONTO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ONTO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.2 | 43.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ONTO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +53.8% vs +10.1% | 53.8% vs 10.1% | PASS |  |  |
| ONTO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ONTO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.8 | 28.8 | PASS |  | Wilder, completed bars |
| ONTO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.8 | PASS |  |  |
| ONTO | T5 | "counted at the last close ($X, date)" = last completed bar | $196.77, Nov 16 | $196.77, Nov 16 | PASS |  |  |
| ONTO | T6 | price vs 200-day average (S1 pattern sma values) | $196.77 vs $259.97 · -24.3% | $196.77 vs $259.97 · -24.3% | PASS |  |  |
| ONTO | T6w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T7 | price vs 50-day average (S1 pattern sma values) | $196.77 vs $246.63 · -20.2% | $196.77 vs $246.63 · -20.2% | PASS |  |  |
| ONTO | T7w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.2% over 30 td | PASS |  |  |
| ONTO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ONTO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ONTO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 49.1% below $386.46 | 49.1% below $386.46 | PASS |  | closing high would be 378.45 |
| ONTO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 49.1% below | PASS |  |  |
| ONTO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $386.46 | $386.46 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ONTO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -3.36%, close location 0.87, OBV flat |
| ONTO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ONTO | V2 | day change of the last completed bar | down 3.4% | -3.36% | PASS |  |  |
| ONTO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.87 (raw 0.8700) | PASS |  |  |
| ONTO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| ONTO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-16 | 1.27× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ONTO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.27× | 2026-11-16 1.27× | PASS |  |  |
| ONTO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.27× / 0.37× | 1.27× / 0.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ONTO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1327190) | 20 bars, last ('2026-11-16', 1327190) | PASS |  |  |
| ORBX.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $14.60 | $14.60 | PASS |  |  |
| ORBX.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $15.27 | $15.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ORBX.TO | E3 | percent from the 21-day average | 4.4% below | 4.4% below | PASS |  |  |
| ORBX.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ORBX.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.69 | $0.69 (sr=0.6946) | PASS |  | Wilder ATR14 |
| ORBX.TO | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| ORBX.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $15.27, -4.4% | $15.27, -4.4% | PASS |  |  |
| ORBX.TO | L-now | ladder price row = compared price; name = the basis label | $14.6 "Last close" | $14.60 "last close" | PASS |  |  |
| ORBX.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $16.2, -9.9% | $16.20, -9.9% | PASS |  |  |
| ORBX.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.8 | 43.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ORBX.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.7 | 26.6 | PASS |  | Wilder, completed bars |
| ORBX.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.6 | PASS |  |  |
| ORBX.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.70%, close location 0.00, OBV falling |
| ORBX.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ORBX.TO | V2 | day change of the last completed bar | down 4.7% | -4.70% | PASS |  |  |
| ORBX.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| ORBX.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ORBX.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.6× from 2026-11-16 | 0.62× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ORBX.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.62× | 2026-11-16 0.62× | PASS |  |  |
| ORBX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.62× / 0.99× | 0.62× / 0.99× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORBX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 4000) | 20 bars, last ('2026-11-16', 4000) | PASS |  |  |
| ORCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $114.64 | $114.64 | PASS |  |  |
| ORCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $126.49 | $126.49 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ORCL | E3 | percent from the 21-day average | 9.4% below | 9.4% below | PASS |  |  |
| ORCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| ORCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.00 | $8.00 (sr=7.999) | PASS |  | Wilder ATR14 |
| ORCL | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| ORCL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.4 | +3.4 | PASS |  |  |
| ORCL | L-ema21 | ladder row ema21: price and gap = price vs average | $126.49, -9.4% | $126.49, -9.4% | PASS |  |  |
| ORCL | L-note | "Last close $X · date" note = last completed bar | Last close $119.09 · Nov 16 | $119.09 · Nov 16 | PASS |  |  |
| ORCL | L-now | ladder price row = compared price; name = the basis label | $114.64 "Now" | $114.64 "now" | PASS |  |  |
| ORCL | L-sma200 | ladder row sma200: price and gap = price vs average | $153.88, -25.5% | $153.88, -25.5% | PASS |  |  |
| ORCL | L-sma50 | ladder row sma50: price and gap = price vs average | $135.86, -15.6% | $135.86, -15.6% | PASS |  |  |
| ORCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $114.64 / entry $114.64 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ORCL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ORCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.7 | 42.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ORCL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -46.6% vs +10.1% | -46.6% vs 10.1% | PASS |  |  |
| ORCL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ORCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.6 | 12.6 | PASS |  | Wilder, completed bars |
| ORCL | T4w | words "20 or more / below 20" | below 20 | ADX 12.6 | PASS |  |  |
| ORCL | T5 | "counted at the last close ($X, date)" = last completed bar | $119.09, Nov 16 | $119.09, Nov 16 | PASS |  |  |
| ORCL | T6 | price vs 200-day average (S1 pattern sma values) | $119.09 vs $153.88 · -22.6% | $119.09 vs $153.88 · -22.6% | PASS |  |  |
| ORCL | T6w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T7 | price vs 50-day average (S1 pattern sma values) | $119.09 vs $135.86 · -12.3% | $119.09 vs $135.86 · -12.3% | PASS |  |  |
| ORCL | T7w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.4% over 30 td | -5.4% over 30 td | PASS |  |  |
| ORCL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| ORCL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ORCL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 52.4% below $250.25 | 52.4% below $250.25 | PASS |  | closing high would be 248.15 |
| ORCL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 52.4% below | PASS |  |  |
| ORCL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $250.25 | $250.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ORCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.99%, close location 0.17, OBV falling |
| ORCL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| ORCL | V2 | day change of the last completed bar | down 5.0% | -4.99% | PASS |  |  |
| ORCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1718) | PASS |  |  |
| ORCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ORCL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.6× from 2026-11-16 | 0.55× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| ORCL | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.55× | 2026-11-16 0.55× | PASS |  |  |
| ORCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.55× / 0.74× | 0.55× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 20146223) | 20 bars, last ('2026-11-16', 20146223) | PASS |  |  |
| PG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $171.75 | $171.75 | PASS |  |  |
| PG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $163.81 | $163.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PG | E3 | percent from the 21-day average | 4.8% above | 4.8% above | PASS |  |  |
| PG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| PG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.27 | $3.27 (sr=3.2747) | PASS |  | Wilder ATR14 |
| PG | E5 | distance in normal day-moves | 2.4 | 2.4 | PASS |  | gauge dot note uses the same number:  · 2.4 day-moves above |
| PG | L-ema21 | ladder row ema21: price and gap = price vs average | $163.81, 4.8% | $163.81, 4.8% | PASS |  |  |
| PG | L-note | "Last close $X · date" note = last completed bar | Last close $173.02 · Nov 16 | $173.02 · Nov 16 | PASS |  |  |
| PG | L-now | ladder price row = compared price; name = the basis label | $171.75 "Now" | $171.75 "now" | PASS |  |  |
| PG | L-sma200 | ladder row sma200: price and gap = price vs average | $148.12, 16.0% | $148.12, 16.0% | PASS |  |  |
| PG | L-sma50 | ladder row sma50: price and gap = price vs average | $154.14, 11.4% | $154.14, 11.4% | PASS |  |  |
| PG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $171.75 / entry $171.75 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 73.1 | 73.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +20.6% vs +10.1% | 20.6% vs 10.1% | PASS |  |  |
| PG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PG | T4w | words "20 or more / below 20" | 20 or more | ADX 42.9 | PASS |  |  |
| PG | T5 | "counted at the last close ($X, date)" = last completed bar | $173.02, Nov 16 | $173.02, Nov 16 | PASS |  |  |
| PG | T6w | word "Above" | Above | Above | PASS |  |  |
| PG | T7w | word "Above" | Above | Above | PASS |  |  |
| PG | T8r | word "rising" | still rising | rising | PASS |  |  |
| PG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 0.3% below $173.57 | 0.3% below $173.57 | PASS |  | closing high would be 173.02 |
| PG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 0.3% below | PASS |  |  |
| PG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $173.57 | $173.57000732421875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 1.90%, close location 0.66, OBV rising |
| PG | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| PG | V2 | day change of the last completed bar | up 1.9% | +1.90% | PASS |  |  |
| PG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| PG | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.6× from 2026-11-16 | 1.59× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| PG | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.59× | 2026-11-16 1.59× | PASS |  |  |
| PG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.59× / 1.00× | 1.59× / 1.00× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 14968400) | 20 bars, last ('2026-11-16', 14968400) | PASS |  |  |
| PLD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $125.25 | $125.25 | PASS |  |  |
| PLD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $128.82 | $128.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PLD | E3 | percent from the 21-day average | 2.8% below | 2.8% below | PASS |  |  |
| PLD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| PLD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.51 | $2.51 (sr=2.506) | PASS |  | Wilder ATR14 |
| PLD | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| PLD | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.6 | +3.6 | PASS |  |  |
| PLD | L-ema21 | ladder row ema21: price and gap = price vs average | $128.82, -2.8% | $128.82, -2.8% | PASS |  |  |
| PLD | L-note | "Last close $X · date" note = last completed bar | Last close $127.60 · Nov 16 | $127.60 · Nov 16 | PASS |  |  |
| PLD | L-now | ladder price row = compared price; name = the basis label | $125.25 "Now" | $125.25 "now" | PASS |  |  |
| PLD | L-sma200 | ladder row sma200: price and gap = price vs average | $137.82, -9.1% | $137.82, -9.1% | PASS |  |  |
| PLD | L-sma50 | ladder row sma50: price and gap = price vs average | $130.44, -4.0% | $130.44, -4.0% | PASS |  |  |
| PLD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $125.25 / entry $125.25 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PLD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PLD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.4 | 45.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PLD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.9% vs +10.1% | 3.9% vs 10.1% | PASS |  |  |
| PLD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PLD | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.3 | 18.2 | PASS |  | Wilder, completed bars |
| PLD | T4w | words "20 or more / below 20" | below 20 | ADX 18.2 | PASS |  |  |
| PLD | T5 | "counted at the last close ($X, date)" = last completed bar | $127.60, Nov 16 | $127.60, Nov 16 | PASS |  |  |
| PLD | T6 | price vs 200-day average (S1 pattern sma values) | $127.60 vs $137.82 · -7.4% | $127.60 vs $137.82 · -7.4% | PASS |  |  |
| PLD | T6w | word "Below" | Below | Below | PASS |  |  |
| PLD | T7 | price vs 50-day average (S1 pattern sma values) | $127.60 vs $130.44 · -2.2% | $127.60 vs $130.44 · -2.2% | PASS |  |  |
| PLD | T7w | word "Below" | Below | Below | PASS |  |  |
| PLD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.1% over 30 td | -0.1% over 30 td | PASS |  |  |
| PLD | T8r | word "rising" | not rising | not rising | PASS |  |  |
| PLD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PLD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 16.8% below $153.35 | 16.8% below $153.35 | PASS |  | closing high would be 150.06 |
| PLD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 16.8% below | PASS |  |  |
| PLD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $153.35 | $153.35 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PLD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.83%, close location 0.14, OBV falling |
| PLD | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| PLD | V2 | day change of the last completed bar | down 0.8% | -0.83% | PASS |  |  |
| PLD | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1357) | PASS |  |  |
| PLD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PLD | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.80× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| PLD | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.80× | 2026-11-16 0.80× | PASS |  |  |
| PLD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.80× / 0.42× | 0.80× / 0.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PLD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3068894) | 20 bars, last ('2026-11-16', 3068894) | PASS |  |  |
| PNG.V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3.12 | $3.12 | PASS |  |  |
| PNG.V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3.71 | $3.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PNG.V | E3 | percent from the 21-day average | 15.9% below | 15.9% below | PASS |  |  |
| PNG.V | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| PNG.V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.23 | $0.23 (sr=0.2319) | PASS |  | Wilder ATR14 |
| PNG.V | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| PNG.V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.6 | +12.6 | PASS |  |  |
| PNG.V | L-ema21 | ladder row ema21: price and gap = price vs average | $3.71, -15.9% | $3.71, -15.9% | PASS |  |  |
| PNG.V | L-note | "Last close $X · date" note = last completed bar | Last close $3.22 · Nov 16 | $3.22 · Nov 16 | PASS |  |  |
| PNG.V | L-now | ladder price row = compared price; name = the basis label | $3.12 "Now" | $3.12 "now" | PASS |  |  |
| PNG.V | L-sma200 | ladder row sma200: price and gap = price vs average | $6.63, -52.9% | $6.63, -52.9% | PASS |  |  |
| PNG.V | L-sma50 | ladder row sma50: price and gap = price vs average | $4.21, -25.9% | $4.21, -25.9% | PASS |  |  |
| PNG.V | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3.12 / entry $3.12 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PNG.V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PNG.V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.6 | 29.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PNG.V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -37.6% vs +10.1% | -37.6% vs 10.1% | PASS |  |  |
| PNG.V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PNG.V | T4 | ADX 14 (S1 /api/sr meta.adx) | 36.1 | 36.0 | PASS |  | Wilder, completed bars |
| PNG.V | T4w | words "20 or more / below 20" | 20 or more | ADX 36.0 | PASS |  |  |
| PNG.V | T5 | "counted at the last close ($X, date)" = last completed bar | $3.22, Nov 16 | $3.22, Nov 16 | PASS |  |  |
| PNG.V | T6 | price vs 200-day average (S1 pattern sma values) | $3.22 vs $6.63 · -51.4% | $3.22 vs $6.63 · -51.4% | PASS |  |  |
| PNG.V | T6w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T7 | price vs 50-day average (S1 pattern sma values) | $3.22 vs $4.21 · -23.5% | $3.22 vs $4.21 · -23.6% | PASS |  |  |
| PNG.V | T7w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -7.0% over 30 td | -7.1% over 30 td | PASS |  |  |
| PNG.V | T8r | word "rising" | not rising | not rising | PASS |  |  |
| PNG.V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PNG.V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 70.0% below $10.72 | 70.0% below $10.72 | PASS |  | closing high would be 10.23 |
| PNG.V | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 70.0% below | PASS |  |  |
| PNG.V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $10.72 | $10.720000267028809 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PNG.V | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| PNG.V | V2 | day change of the last completed bar | down 5.3% | -5.29% | PASS |  |  |
| PNG.V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PNG.V | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-16 | 0.93× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| PNG.V | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.93× | 2026-11-16 0.93× | PASS |  |  |
| PNG.V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.93× / 0.73× | 0.93× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PNG.V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1108800) | 20 bars, last ('2026-11-16', 1108800) | PASS |  |  |
| QCOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $165.58 | $165.58 | PASS |  |  |
| QCOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $172.96 | $172.96 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QCOM | E3 | percent from the 21-day average | 4.3% below | 4.3% below | PASS |  |  |
| QCOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| QCOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.92 | $8.92 (sr=8.9181) | PASS |  | Wilder ATR14 |
| QCOM | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves below |
| QCOM | L-ema21 | ladder row ema21: price and gap = price vs average | $172.96, -4.3% | $172.96, -4.3% | PASS |  |  |
| QCOM | L-note | "Last close $X · date" note = last completed bar | Last close $168.52 · Nov 16 | $168.52 · Nov 16 | PASS |  |  |
| QCOM | L-now | ladder price row = compared price; name = the basis label | $165.58 "Now" | $165.58 "now" | PASS |  |  |
| QCOM | L-sma200 | ladder row sma200: price and gap = price vs average | $170.28, -2.8% | $170.28, -2.8% | PASS |  |  |
| QCOM | L-sma50 | ladder row sma50: price and gap = price vs average | $178.73, -7.4% | $178.73, -7.4% | PASS |  |  |
| QCOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $165.58 / entry $165.58 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QCOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QCOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.0 | 46.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QCOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -3.1% vs +10.1% | -3.1% vs 10.1% | PASS |  |  |
| QCOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QCOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.2 | 11.2 | PASS |  | Wilder, completed bars |
| QCOM | T4w | words "20 or more / below 20" | below 20 | ADX 11.2 | PASS |  |  |
| QCOM | T5 | "counted at the last close ($X, date)" = last completed bar | $168.52, Nov 16 | $168.52, Nov 16 | PASS |  |  |
| QCOM | T6 | price vs 200-day average (S1 pattern sma values) | $168.52 vs $170.28 · -1.0% | $168.52 vs $170.28 · -1.0% | PASS |  |  |
| QCOM | T6w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T7 | price vs 50-day average (S1 pattern sma values) | $168.52 vs $178.73 · -5.7% | $168.52 vs $178.73 · -5.7% | PASS |  |  |
| QCOM | T7w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.6% over 30 td | +0.6% over 30 td | PASS |  |  |
| QCOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QCOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QCOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.2% below $259.92 | 35.2% below $259.92 | PASS |  | closing high would be 251.02 |
| QCOM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.2% below | PASS |  |  |
| QCOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $259.92 | $259.92 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QCOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.29%, close location 0.09, OBV rising |
| QCOM | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| QCOM | V2 | day change of the last completed bar | down 2.3% | -2.29% | PASS |  |  |
| QCOM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0871) | PASS |  |  |
| QCOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| QCOM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-16 | 0.87× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| QCOM | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.87× | 2026-11-16 0.87× | PASS |  |  |
| QCOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.87× / 0.43× | 0.87× / 0.43× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QCOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 11865645) | 20 bars, last ('2026-11-16', 11865645) | PASS |  |  |
| QPUX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3.29 | $3.29 | PASS |  |  |
| QPUX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $6.13 | $6.13 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QPUX | E3 | percent from the 21-day average | 46.3% below | 46.3% below | PASS |  |  |
| QPUX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| QPUX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.90 | $0.90 (sr=0.9026) | PASS |  | Wilder ATR14 |
| QPUX | E5 | distance in normal day-moves | 3.1 | 3.1 | PASS |  | gauge dot note uses the same number:  · 3.1 day-moves below |
| QPUX | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| QPUX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +15.9 | +15.9 | PASS |  |  |
| QPUX | L-ema21 | ladder row ema21: price and gap = price vs average | $6.13, -46.3% | $6.13, -46.3% | PASS |  |  |
| QPUX | L-note | "Last close $X · date" note = last completed bar | Last close $3.59 · Nov 16 | $3.59 · Nov 16 | PASS |  |  |
| QPUX | L-now | ladder price row = compared price; name = the basis label | $3.29 "Now" | $3.29 "now" | PASS |  |  |
| QPUX | L-sma200 | ladder row sma200: price and gap = price vs average | $20.51, -84.0% | $20.51, -84.0% | PASS |  |  |
| QPUX | L-sma50 | ladder row sma50: price and gap = price vs average | $9.3, -64.6% | $9.30, -64.6% | PASS |  |  |
| QPUX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3.29 / entry $3.29 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QPUX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QPUX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.3 | 30.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QPUX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -93.9% vs +10.1% | -93.9% vs 10.1% | PASS |  |  |
| QPUX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QPUX | T4 | ADX 14 (S1 /api/sr meta.adx) | 36.2 | 36.2 | PASS |  | Wilder, completed bars |
| QPUX | T4w | words "20 or more / below 20" | 20 or more | ADX 36.2 | PASS |  |  |
| QPUX | T5 | "counted at the last close ($X, date)" = last completed bar | $3.59, Nov 16 | $3.59, Nov 16 | PASS |  |  |
| QPUX | T6w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T7 | price vs 50-day average (S1 pattern sma values) | $3.59 vs $9.30 · -61.4% | $3.59 vs $9.30 · -61.4% | PASS |  |  |
| QPUX | T7w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| QPUX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QPUX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 95.5% below | PASS |  |  |
| QPUX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -16.12%, close location 0.09, OBV falling |
| QPUX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| QPUX | V2 | day change of the last completed bar | down 16.1% | -16.12% | PASS |  |  |
| QPUX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0943) | PASS |  |  |
| QPUX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QPUX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.7× from 2026-11-16 | 1.67× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| QPUX | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.67× | 2026-11-16 1.67× | PASS |  |  |
| QPUX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.67× / 0.64× | 1.67× / 0.64× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QPUX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 501400) | 20 bars, last ('2026-11-16', 501400) | PASS |  |  |
| QPUX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.67, OBV falling | condition true | PASS |  |  |
| QTUM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $122.49 | $122.49 | PASS |  |  |
| QTUM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $133.76 | $133.76 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QTUM | E3 | percent from the 21-day average | 8.4% below | 8.4% below | PASS |  |  |
| QTUM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| QTUM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.82 | $4.82 (sr=4.8191) | PASS |  | Wilder ATR14 |
| QTUM | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| QTUM | L-ema21 | ladder row ema21: price and gap = price vs average | $133.76, -8.4% | $133.76, -8.4% | PASS |  |  |
| QTUM | L-note | "Last close $X · date" note = last completed bar | Last close $124.47 · Nov 16 | $124.47 · Nov 16 | PASS |  |  |
| QTUM | L-now | ladder price row = compared price; name = the basis label | $122.49 "Now" | $122.49 "now" | PASS |  |  |
| QTUM | L-sma200 | ladder row sma200: price and gap = price vs average | $137.92, -11.2% | $137.92, -11.2% | PASS |  |  |
| QTUM | L-sma50 | ladder row sma50: price and gap = price vs average | $142.71, -14.2% | $142.71, -14.2% | PASS |  |  |
| QTUM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $122.49 / entry $122.49 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QTUM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QTUM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.5 | 37.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QTUM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +17.7% vs +10.1% | 17.7% vs 10.1% | PASS |  |  |
| QTUM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QTUM | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.0 | 33.0 | PASS |  | Wilder, completed bars |
| QTUM | T4w | words "20 or more / below 20" | 20 or more | ADX 33.0 | PASS |  |  |
| QTUM | T5 | "counted at the last close ($X, date)" = last completed bar | $124.47, Nov 16 | $124.47, Nov 16 | PASS |  |  |
| QTUM | T6w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T7w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QTUM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QTUM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.4% below | PASS |  |  |
| QTUM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.33%, close location 0.10, OBV falling |
| QTUM | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| QTUM | V2 | day change of the last completed bar | down 4.3% | -4.33% | PASS |  |  |
| QTUM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1032) | PASS |  |  |
| QTUM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QTUM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.12× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| QTUM | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.12× | 2026-11-16 1.12× | PASS |  |  |
| QTUM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.12× / 1.12× | 1.12× / 1.12× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QTUM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 372700) | 20 bars, last ('2026-11-16', 372700) | PASS |  |  |
| RBOT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $27.53 | $27.53 | PASS |  |  |
| RBOT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $29.53 | $29.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RBOT.TO | E3 | percent from the 21-day average | 6.8% below | 6.8% below | PASS |  |  |
| RBOT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| RBOT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.61 | $0.61 (sr=0.6137) | PASS |  | Wilder ATR14 |
| RBOT.TO | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| RBOT.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.2 | +6.2 | PASS |  |  |
| RBOT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $29.53, -6.8% | $29.53, -6.8% | PASS |  |  |
| RBOT.TO | L-now | ladder price row = compared price; name = the basis label | $27.53 "Last close" | $27.53 "last close" | PASS |  |  |
| RBOT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.33, -17.4% | $33.33, -17.4% | PASS |  |  |
| RBOT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $31.04, -11.3% | $31.04, -11.3% | PASS |  |  |
| RBOT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.1 | 33.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RBOT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -13.5% vs +10.1% | -13.5% vs 10.1% | PASS |  |  |
| RBOT.TO | T3w | words "past year" vs the window used | 250 / 251 bars back | 250-253 bars | PASS |  |  |
| RBOT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.4 | 33.5 | PASS |  | Wilder, completed bars |
| RBOT.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 33.5 | PASS |  |  |
| RBOT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.71%, close location 0.07, OBV falling |
| RBOT.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| RBOT.TO | V2 | day change of the last completed bar | down 3.7% | -3.71% | PASS |  |  |
| RBOT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0690) | PASS |  |  |
| RBOT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RBOT.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 8.2× from 2026-11-16 | 8.17× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| RBOT.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 8.17× | 2026-11-16 8.17× | PASS |  |  |
| RBOT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 8.17× / 1.66× | 8.17× / 1.66× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RBOT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 24200) | 20 bars, last ('2026-11-16', 24200) | PASS |  |  |
| RBOT.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 8.17, OBV falling | condition true | PASS |  |  |
| RTX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $197.51 | $197.51 | PASS |  |  |
| RTX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $196.02 | $196.02 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RTX | E3 | percent from the 21-day average | 0.8% above | 0.8% above | PASS |  |  |
| RTX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| RTX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.30 | $5.30 (sr=5.301) | PASS |  | Wilder ATR14 |
| RTX | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| RTX | L-ema21 | ladder row ema21: price and gap = price vs average | $196.02, 0.8% | $196.02, 0.8% | PASS |  |  |
| RTX | L-note | "Last close $X · date" note = last completed bar | Last close $194.89 · Nov 16 | $194.89 · Nov 16 | PASS |  |  |
| RTX | L-now | ladder price row = compared price; name = the basis label | $197.51 "Now" | $197.50 "now" | PASS |  |  |
| RTX | L-sma200 | ladder row sma200: price and gap = price vs average | $194.49, 1.6% | $194.49, 1.6% | PASS |  |  |
| RTX | L-sma50 | ladder row sma50: price and gap = price vs average | $192.68, 2.5% | $192.68, 2.5% | PASS |  |  |
| RTX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $197.51 / entry $197.51 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RTX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.0 | 49.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RTX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +12.7% vs +10.1% | 12.7% vs 10.1% | PASS |  |  |
| RTX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RTX | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.8 | 19.8 | PASS |  | Wilder, completed bars |
| RTX | T4w | words "20 or more / below 20" | below 20 | ADX 19.8 | PASS |  |  |
| RTX | T5 | "counted at the last close ($X, date)" = last completed bar | $194.89, Nov 16 | $194.89, Nov 16 | PASS |  |  |
| RTX | T7 | price vs 50-day average (S1 pattern sma values) | $194.89 vs $192.68 · +1.1% | $194.89 vs $192.68 · 1.1% | PASS |  |  |
| RTX | T7w | word "Above" | Above | Above | PASS |  |  |
| RTX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.2% over 30 td | +0.3% over 30 td | PASS |  |  |
| RTX | T8r | word "rising" | still rising | rising | PASS |  |  |
| RTX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RTX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.9% below | PASS |  |  |
| RTX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.86%, close location 0.12, OBV rising |
| RTX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| RTX | V2 | day change of the last completed bar | down 1.9% | -1.86% | PASS |  |  |
| RTX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1174) | PASS |  |  |
| RTX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| RTX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.75× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| RTX | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.75× | 2026-11-16 0.75× | PASS |  |  |
| RTX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.75× / 0.68× | 0.75× / 0.68× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RTX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3583900) | 20 bars, last ('2026-11-16', 3583900) | PASS |  |  |
| RY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $280.58 | $280.58 | PASS |  |  |
| RY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $285.43 | $285.43 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RY.TO | E3 | percent from the 21-day average | 1.7% below | 1.7% below | PASS |  |  |
| RY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| RY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.48 | $4.48 (sr=4.4813) | PASS |  | Wilder ATR14 |
| RY.TO | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| RY.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.0 | -5.0 | PASS |  |  |
| RY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $285.43, -1.7% | $285.43, -1.7% | PASS |  |  |
| RY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $285.69 · Nov 16 | $285.69 · Nov 16 | PASS |  |  |
| RY.TO | L-now | ladder price row = compared price; name = the basis label | $280.58 "Now" | $280.58 "now" | PASS |  |  |
| RY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $263.01, 6.7% | $263.01, 6.7% | PASS |  |  |
| RY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $282.25, -0.6% | $282.25, -0.6% | PASS |  |  |
| RY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $280.58 / entry $280.58 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.4 | 51.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +42.7% vs +10.1% | 42.7% vs 10.1% | PASS |  |  |
| RY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.9 | 13.9 | PASS |  | Wilder, completed bars |
| RY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 13.9 | PASS |  |  |
| RY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $285.69, Nov 16 | $285.69, Nov 16 | PASS |  |  |
| RY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $285.69 vs $263.01 · +8.6% | $285.69 vs $263.01 · 8.6% | PASS |  |  |
| RY.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| RY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $285.69 vs $282.25 · +1.2% | $285.69 vs $282.25 · 1.2% | PASS |  |  |
| RY.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| RY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| RY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| RY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.6% below $302.65 | 5.6% below $302.65 | PASS |  | closing high would be 302.02 |
| RY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.6% below | PASS |  |  |
| RY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.65 | $302.6498839841861 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.93%, close location 0.19, OBV falling |
| RY.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| RY.TO | V2 | day change of the last completed bar | down 0.9% | -0.93% | PASS |  |  |
| RY.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.19 (raw 0.1885) | PASS |  |  |
| RY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RY.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.4× from 2026-11-16 | 1.37× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| RY.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.37× | 2026-11-16 1.37× | PASS |  |  |
| RY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.37× / 0.59× | 1.37× / 0.59× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 4479600) | 20 bars, last ('2026-11-16', 4479600) | PASS |  |  |
| SETM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $22.11 | $22.11 | PASS |  |  |
| SETM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $25.17 | $25.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SETM | E3 | percent from the 21-day average | 12.1% below | 12.1% below | PASS |  |  |
| SETM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SETM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.00 | $1.00 (sr=1.0038) | PASS |  | Wilder ATR14 |
| SETM | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| SETM | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.3 | +7.3 | PASS |  |  |
| SETM | L-ema21 | ladder row ema21: price and gap = price vs average | $25.17, -12.1% | $25.17, -12.1% | PASS |  |  |
| SETM | L-note | "Last close $X · date" note = last completed bar | Last close $22.41 · Nov 16 | $22.41 · Nov 16 | PASS |  |  |
| SETM | L-now | ladder price row = compared price; name = the basis label | $22.11 "After hours" | $22.11 "after hours" | PASS |  |  |
| SETM | L-sma200 | ladder row sma200: price and gap = price vs average | $32.47, -31.9% | $32.47, -31.9% | PASS |  |  |
| SETM | L-sma50 | ladder row sma50: price and gap = price vs average | $27.87, -20.7% | $27.87, -20.7% | PASS |  |  |
| SETM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $22.11 / entry $22.11 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SETM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SETM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.5 | 32.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SETM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -12.9% vs +10.1% | -12.9% vs 10.1% | PASS |  |  |
| SETM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SETM | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.5 | 33.5 | PASS |  | Wilder, completed bars |
| SETM | T4w | words "20 or more / below 20" | 20 or more | ADX 33.5 | PASS |  |  |
| SETM | T5 | "counted at the last close ($X, date)" = last completed bar | $22.41, Nov 16 | $22.41, Nov 16 | PASS |  |  |
| SETM | T6 | price vs 200-day average (S1 pattern sma values) | $22.41 vs $32.47 · -31.0% | $22.41 vs $32.47 · -31.0% | PASS |  |  |
| SETM | T6w | word "Below" | Below | Below | PASS |  |  |
| SETM | T7 | price vs 50-day average (S1 pattern sma values) | $22.41 vs $27.87 · -19.6% | $22.41 vs $27.87 · -19.6% | PASS |  |  |
| SETM | T7w | word "Below" | Below | Below | PASS |  |  |
| SETM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.3% over 30 td | -3.3% over 30 td | PASS |  |  |
| SETM | T8r | word "rising" | not rising | not rising | PASS |  |  |
| SETM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SETM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 44.7% below $40.55 | 44.7% below $40.55 | PASS |  | closing high would be 39.73 |
| SETM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 44.7% below | PASS |  |  |
| SETM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $40.55 | $40.54999923706055 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SETM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.44%, close location 0.05, OBV falling |
| SETM | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SETM | V2 | day change of the last completed bar | down 5.4% | -5.44% | PASS |  |  |
| SETM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0543) | PASS |  |  |
| SETM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SETM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.2× from 2026-11-16 | 1.19× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SETM | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.19× | 2026-11-16 1.19× | PASS |  |  |
| SETM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.19× / 1.21× | 1.19× / 1.22× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SETM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 192800) | 20 bars, last ('2026-11-16', 192800) | PASS |  |  |
| SGRD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $18.03 | $18.03 | PASS |  |  |
| SGRD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.7 | $18.70 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SGRD.TO | E3 | percent from the 21-day average | 3.6% below | 3.6% below | PASS |  |  |
| SGRD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SGRD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.40 | $0.40 (sr=0.4036) | PASS |  | Wilder ATR14 |
| SGRD.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| SGRD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $18.7, -3.6% | $18.70, -3.6% | PASS |  |  |
| SGRD.TO | L-now | ladder price row = compared price; name = the basis label | $18.03 "Last close" | $18.03 "last close" | PASS |  |  |
| SGRD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $19.57, -7.8% | $19.57, -7.8% | PASS |  |  |
| SGRD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.0 | 41.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SGRD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.7 | 26.7 | PASS |  | Wilder, completed bars |
| SGRD.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.7 | PASS |  |  |
| SGRD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.01%, close location 0.00, OBV falling |
| SGRD.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SGRD.TO | V2 | day change of the last completed bar | down 3.0% | -3.01% | PASS |  |  |
| SGRD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| SGRD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SGRD.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.1× from 2026-11-16 | 0.12× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SGRD.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.12× | 2026-11-16 0.12× | PASS |  |  |
| SGRD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.12× / 1.34× | 0.12× / 1.35× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SGRD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1100) | 20 bars, last ('2026-11-16', 1100) | PASS |  |  |
| SMH | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $460.10 | $460.10 | PASS |  |  |
| SMH | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $512.91 | $512.91 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SMH | E3 | percent from the 21-day average | 10.3% below | 10.3% below | PASS |  |  |
| SMH | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SMH | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $24.35 | $24.35 (sr=24.3517) | PASS |  | Wilder ATR14 |
| SMH | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| SMH | L-ema21 | ladder row ema21: price and gap = price vs average | $512.91, -10.3% | $512.91, -10.3% | PASS |  |  |
| SMH | L-note | "Last close $X · date" note = last completed bar | Last close $461.90 · Nov 16 | $461.90 · Nov 16 | PASS |  |  |
| SMH | L-now | ladder price row = compared price; name = the basis label | $460.1 "After hours" | $460.10 "after hours" | PASS |  |  |
| SMH | L-sma200 | ladder row sma200: price and gap = price vs average | $524.18, -12.2% | $524.18, -12.2% | PASS |  |  |
| SMH | L-sma50 | ladder row sma50: price and gap = price vs average | $557.7, -17.5% | $557.70, -17.5% | PASS |  |  |
| SMH | S5-price | S5: the same live price reads the same on the header and the Entry block | header $460.10 / entry $460.10 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| SNDK.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $19.60 | $19.60 | PASS |  |  |
| SNDK.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $26.33 | $26.33 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SNDK.TO | E3 | percent from the 21-day average | 25.6% below | 25.6% below | PASS |  |  |
| SNDK.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SNDK.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.54 | $2.54 (sr=2.5371) | PASS |  | Wilder ATR14 |
| SNDK.TO | E5 | distance in normal day-moves | 2.7 | 2.7 | PASS |  | gauge dot note uses the same number:  · 2.7 day-moves below |
| SNDK.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.3 | +3.3 | PASS |  |  |
| SNDK.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $26.33, -25.6% | $26.33, -25.6% | PASS |  |  |
| SNDK.TO | L-now | ladder price row = compared price; name = the basis label | $19.6 "Last close" | $19.60 "last close" | PASS |  |  |
| SNDK.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $34.64, -43.4% | $34.64, -43.4% | PASS |  |  |
| SNDK.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.1 | 31.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SNDK.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.3 | 38.3 | PASS |  | Wilder, completed bars |
| SNDK.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 38.3 | PASS |  |  |
| SNDK.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -8.45%, close location 0.26, OBV falling |
| SNDK.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SNDK.TO | V2 | day change of the last completed bar | down 8.4% | -8.45% | PASS |  |  |
| SNDK.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SNDK.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.6× from 2026-11-16 | 1.59× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SNDK.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.59× | 2026-11-16 1.59× | PASS |  |  |
| SNDK.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.59× / 0.65× | 1.59× / 0.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SNDK.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1992400) | 20 bars, last ('2026-11-16', 1992400) | PASS |  |  |
| SNDK.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.59, OBV falling | condition true | PASS |  |  |
| SO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $93.62 | $93.62 | PASS |  |  |
| SO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $92.38 | $92.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SO | E3 | percent from the 21-day average | 1.3% above | 1.3% above | PASS |  |  |
| SO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| SO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.84 | $1.84 (sr=1.8377) | PASS |  | Wilder ATR14 |
| SO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves above |
| SO | L-ema21 | ladder row ema21: price and gap = price vs average | $92.38, 1.3% | $92.38, 1.3% | PASS |  |  |
| SO | L-note | "Last close $X · date" note = last completed bar | Last close $94.64 · Nov 16 | $94.64 · Nov 16 | PASS |  |  |
| SO | L-now | ladder price row = compared price; name = the basis label | $93.62 "Now" | $93.62 "now" | PASS |  |  |
| SO | L-sma200 | ladder row sma200: price and gap = price vs average | $92.7, 1.0% | $92.70, 1.0% | PASS |  |  |
| SO | L-sma50 | ladder row sma50: price and gap = price vs average | $88.82, 5.4% | $88.82, 5.4% | PASS |  |  |
| SO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $93.62 / entry $93.62 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 62.5 | 62.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +5.2% vs +10.1% | 5.2% vs 10.1% | PASS |  |  |
| SO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.8 | 27.7 | PASS |  | Wilder, completed bars |
| SO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.7 | PASS |  |  |
| SO | T5 | "counted at the last close ($X, date)" = last completed bar | $94.64, Nov 16 | $94.64, Nov 16 | PASS |  |  |
| SO | T6 | price vs 200-day average (S1 pattern sma values) | $94.64 vs $92.70 · +2.1% | $94.64 vs $92.70 · 2.1% | PASS |  |  |
| SO | T6w | word "Above" | Above | Above | PASS |  |  |
| SO | T7 | price vs 50-day average (S1 pattern sma values) | $94.64 vs $88.82 · +6.6% | $94.64 vs $88.82 · 6.6% | PASS |  |  |
| SO | T7w | word "Above" | Above | Above | PASS |  |  |
| SO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.6% over 30 td | +0.6% over 30 td | PASS |  |  |
| SO | T8r | word "rising" | still rising | rising | PASS |  |  |
| SO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.0% below $99.58 | 5.0% below $99.58 | PASS |  | closing high would be 99.11 |
| SO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.0% below | PASS |  |  |
| SO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $99.58 | $99.58 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 1.12%, close location 0.92, OBV rising |
| SO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SO | V2 | day change of the last completed bar | up 1.1% | +1.12% | PASS |  |  |
| SO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.92 (raw 0.9198) | PASS |  |  |
| SO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| SO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.8× from 2026-11-16 | 1.83× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.83× | 2026-11-16 1.83× | PASS |  |  |
| SO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.83× / 0.58× | 1.83× / 0.58× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 13104073) | 20 bars, last ('2026-11-16', 13104073) | PASS |  |  |
| SOXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $46.91 | $46.91 | PASS |  |  |
| SOXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $75.63 | $75.63 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL | E3 | percent from the 21-day average | 38.0% below | 38.0% below | PASS |  |  |
| SOXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| SOXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $12.63 | $12.63 (sr=12.6338) | PASS |  | Wilder ATR14 |
| SOXL | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| SOXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.8 | +3.8 | PASS |  |  |
| SOXL | L-ema21 | ladder row ema21: price and gap = price vs average | $75.63, -38.0% | $75.63, -38.0% | PASS |  |  |
| SOXL | L-note | "Last close $X · date" note = last completed bar | Last close $48.76 · Nov 16 | $48.76 · Nov 16 | PASS |  |  |
| SOXL | L-now | ladder price row = compared price; name = the basis label | $46.91 "Now" | $46.91 "now" | PASS |  |  |
| SOXL | L-sma200 | ladder row sma200: price and gap = price vs average | $124.01, -62.2% | $124.01, -62.2% | PASS |  |  |
| SOXL | L-sma50 | ladder row sma50: price and gap = price vs average | $109.03, -57.0% | $109.03, -57.0% | PASS |  |  |
| SOXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $46.91 / entry $46.91 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.2 | 34.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.5% vs +10.1% | 25.5% vs 10.1% | PASS |  |  |
| SOXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.3 | 34.3 | PASS |  | Wilder, completed bars |
| SOXL | T4w | words "20 or more / below 20" | 20 or more | ADX 34.3 | PASS |  |  |
| SOXL | T5 | "counted at the last close ($X, date)" = last completed bar | $48.76, Nov 16 | $48.76, Nov 16 | PASS |  |  |
| SOXL | T6 | price vs 200-day average (S1 pattern sma values) | $48.76 vs $124.01 · -60.7% | $48.76 vs $124.01 · -60.7% | PASS |  |  |
| SOXL | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T7 | price vs 50-day average (S1 pattern sma values) | $48.76 vs $109.03 · -55.3% | $48.76 vs $109.03 · -55.3% | PASS |  |  |
| SOXL | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.0% over 30 td | +5.0% over 30 td | PASS |  |  |
| SOXL | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 83.9% below $302.00 | 83.9% below $302.00 | PASS |  | closing high would be 300.77 |
| SOXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 83.9% below | PASS |  |  |
| SOXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.00 | $302 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -16.39%, close location 0.09, OBV falling |
| SOXL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SOXL | V2 | day change of the last completed bar | down 16.4% | -16.39% | PASS |  |  |
| SOXL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0911) | PASS |  |  |
| SOXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.6× from 2026-11-16 | 1.63× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SOXL | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.63× | 2026-11-16 1.63× | PASS |  |  |
| SOXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.63× / 0.63× | 1.63× / 0.63× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 187877489) | 20 bars, last ('2026-11-16', 187877489) | PASS |  |  |
| SOXL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.63, OBV falling | condition true | PASS |  |  |
| SOXL.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $11.80 | $11.80 | PASS |  |  |
| SOXL.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.96 | $18.96 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL.NE | E3 | percent from the 21-day average | 37.8% below | 37.8% below | PASS |  |  |
| SOXL.NE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| SOXL.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.04 | $2.04 (sr=2.042) | PASS |  | Wilder ATR14 |
| SOXL.NE | E5 | distance in normal day-moves | 3.5 | 3.5 | PASS |  | gauge dot note uses the same number:  · 3.5 day-moves below |
| SOXL.NE | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.0 | +4.0 | PASS |  |  |
| SOXL.NE | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.8 | +5.8 | PASS |  |  |
| SOXL.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $18.96, -37.8% | $18.96, -37.8% | PASS |  |  |
| SOXL.NE | L-note | "Last close $X · date" note = last completed bar | Last close $12.30 · Nov 16 | $12.30 · Nov 16 | PASS |  |  |
| SOXL.NE | L-now | ladder price row = compared price; name = the basis label | $11.8 "Now" | $11.80 "now" | PASS |  |  |
| SOXL.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.88, -61.8% | $30.88, -61.8% | PASS |  |  |
| SOXL.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $27.08, -56.4% | $27.08, -56.4% | PASS |  |  |
| SOXL.NE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $11.80 / entry $11.80 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
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
| SOXX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $139.80 | $139.80 | PASS |  |  |
| SOXX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $155.9 | $155.90 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXX | E3 | percent from the 21-day average | 10.3% below | 10.3% below | PASS |  |  |
| SOXX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| SOXX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.53 | $8.53 (sr=8.5276) | PASS |  | Wilder ATR14 |
| SOXX | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| SOXX | L-ema21 | ladder row ema21: price and gap = price vs average | $155.9, -10.3% | $155.90, -10.3% | PASS |  |  |
| SOXX | L-note | "Last close $X · date" note = last completed bar | Last close $141.22 · Nov 16 | $141.22 · Nov 16 | PASS |  |  |
| SOXX | L-now | ladder price row = compared price; name = the basis label | $139.8 "Now" | $139.80 "now" | PASS |  |  |
| SOXX | L-sma200 | ladder row sma200: price and gap = price vs average | $160.52, -12.9% | $160.52, -12.9% | PASS |  |  |
| SOXX | L-sma50 | ladder row sma50: price and gap = price vs average | $171.26, -18.4% | $171.26, -18.4% | PASS |  |  |
| SOXX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $139.80 / entry $139.80 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.7 | 37.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +46.8% vs +10.1% | 46.8% vs 10.1% | PASS |  |  |
| SOXX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXX | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.7 | 31.7 | PASS |  | Wilder, completed bars |
| SOXX | T4w | words "20 or more / below 20" | 20 or more | ADX 31.7 | PASS |  |  |
| SOXX | T5 | "counted at the last close ($X, date)" = last completed bar | $141.22, Nov 16 | $141.22, Nov 16 | PASS |  |  |
| SOXX | T6 | price vs 200-day average (S1 pattern sma values) | $141.22 vs $160.52 · -12.0% | $141.22 vs $160.52 · -12.0% | PASS |  |  |
| SOXX | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T7 | price vs 50-day average (S1 pattern sma values) | $141.22 vs $171.26 · -17.5% | $141.22 vs $171.26 · -17.5% | PASS |  |  |
| SOXX | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.5% over 30 td | +5.5% over 30 td | PASS |  |  |
| SOXX | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.4% below $218.65 | 35.4% below $218.65 | PASS |  | closing high would be 218.34 |
| SOXX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.4% below | PASS |  |  |
| SOXX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $218.65 | $218.65 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.41%, close location 0.09, OBV falling |
| SOXX | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SOXX | V2 | day change of the last completed bar | down 5.4% | -5.41% | PASS |  |  |
| SOXX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0939) | PASS |  |  |
| SOXX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXX | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.3× from 2026-11-16 | 1.26× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SOXX | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.26× | 2026-11-16 1.26× | PASS |  |  |
| SOXX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.26× / 0.90× | 1.26× / 0.90× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 37178532) | 20 bars, last ('2026-11-16', 37178532) | PASS |  |  |
| SPCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $10.44 | $10.44 | PASS |  |  |
| SPCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.46 | $13.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SPCL | E3 | percent from the 21-day average | 22.4% below | 22.4% below | PASS |  |  |
| SPCL | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SPCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.78 | $1.78 (sr=1.7767) | PASS |  | Wilder ATR14 |
| SPCL | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| SPCL | L-ema21 | ladder row ema21: price and gap = price vs average | $13.46, -22.4% | $13.46, -22.4% | PASS |  |  |
| SPCL | L-now | ladder price row = compared price; name = the basis label | $10.44 "Last close" | $10.44 "last close" | PASS |  |  |
| SPCL | L-sma50 | ladder row sma50: price and gap = price vs average | $17.64, -40.8% | $17.64, -40.8% | PASS |  |  |
| SPCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.8 | 37.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SPCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.6 | 31.5 | PASS |  | Wilder, completed bars |
| SPCL | T4w | words "20 or more / below 20" | 20 or more | ADX 31.5 | PASS |  |  |
| SPCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -14.07%, close location 0.00, OBV falling |
| SPCL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| SPCL | V2 | day change of the last completed bar | down 14.1% | -14.07% | PASS |  |  |
| SPCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| SPCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SPCL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.80× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| SPCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 31300) | 20 bars, last ('2026-11-16', 31300) | PASS |  |  |
| TSLA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $378.47 | $378.47 | PASS |  |  |
| TSLA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $382.53 | $382.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLA | E3 | percent from the 21-day average | 1.1% below | 1.1% below | PASS |  |  |
| TSLA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| TSLA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.56 | $16.56 (sr=16.5579) | PASS |  | Wilder ATR14 |
| TSLA | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| TSLA | L-ema21 | ladder row ema21: price and gap = price vs average | $382.53, -1.1% | $382.53, -1.1% | PASS |  |  |
| TSLA | L-note | "Last close $X · date" note = last completed bar | Last close $379.74 · Nov 16 | $379.74 · Nov 16 | PASS |  |  |
| TSLA | L-now | ladder price row = compared price; name = the basis label | $378.47 "Now" | $378.47 "now" | PASS |  |  |
| TSLA | L-sma200 | ladder row sma200: price and gap = price vs average | $382.48, -1.0% | $382.48, -1.0% | PASS |  |  |
| TSLA | L-sma50 | ladder row sma50: price and gap = price vs average | $375.25, 0.9% | $375.25, 0.9% | PASS |  |  |
| TSLA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $378.47 / entry $378.47 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.5 | 49.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -6.1% vs +10.1% | -6.1% vs 10.1% | PASS |  |  |
| TSLA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLA | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.9 | 12.9 | PASS |  | Wilder, completed bars |
| TSLA | T4w | words "20 or more / below 20" | below 20 | ADX 12.9 | PASS |  |  |
| TSLA | T5 | "counted at the last close ($X, date)" = last completed bar | $379.74, Nov 16 | $379.74, Nov 16 | PASS |  |  |
| TSLA | T6 | price vs 200-day average (S1 pattern sma values) | $379.74 vs $382.48 · -0.7% | $379.74 vs $382.48 · -0.7% | PASS |  |  |
| TSLA | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLA | T7 | price vs 50-day average (S1 pattern sma values) | $379.74 vs $375.25 · +1.2% | $379.74 vs $375.25 · 1.2% | PASS |  |  |
| TSLA | T7w | word "Above" | Above | Above | PASS |  |  |
| TSLA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.6% over 30 td | -2.6% over 30 td | PASS |  |  |
| TSLA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.9% below $498.83 | 23.9% below $498.83 | PASS |  | closing high would be 489.88 |
| TSLA | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.9% below | PASS |  |  |
| TSLA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $498.83 | $498.82999 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.69%, close location 0.29, OBV falling |
| TSLA | V2 | day change of the last completed bar | down 2.7% | -2.69% | PASS |  |  |
| TSLA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSLA | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.82× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| TSLA | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.82× | 2026-11-16 0.82× | PASS |  |  |
| TSLA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.82× / 0.62× | 0.82× / 0.62× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 30156600) | 20 bars, last ('2026-11-16', 30156600) | PASS |  |  |
| TSLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $9.82 | $9.82 | PASS |  |  |
| TSLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $10.15 | $10.15 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLL | E3 | percent from the 21-day average | 3.3% below | 3.3% below | PASS |  |  |
| TSLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| TSLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.88 | $0.88 (sr=0.8753) | PASS |  | Wilder ATR14 |
| TSLL | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| TSLL | L-ema21 | ladder row ema21: price and gap = price vs average | $10.15, -3.3% | $10.15, -3.3% | PASS |  |  |
| TSLL | L-note | "Last close $X · date" note = last completed bar | Last close $9.80 · Nov 16 | $9.80 · Nov 16 | PASS |  |  |
| TSLL | L-now | ladder price row = compared price; name = the basis label | $9.82 "Now" | $9.81 "now" | PASS |  |  |
| TSLL | L-sma200 | ladder row sma200: price and gap = price vs average | $11.9, -17.5% | $11.90, -17.5% | PASS |  |  |
| TSLL | L-sma50 | ladder row sma50: price and gap = price vs average | $9.98, -1.6% | $9.98, -1.6% | PASS |  |  |
| TSLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $9.82 / entry $9.82 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 47.6 | 47.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -40.9% vs +10.1% | -40.9% vs 10.1% | PASS |  |  |
| TSLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.5 | 12.5 | PASS |  | Wilder, completed bars |
| TSLL | T4w | words "20 or more / below 20" | below 20 | ADX 12.5 | PASS |  |  |
| TSLL | T5 | "counted at the last close ($X, date)" = last completed bar | $9.80, Nov 16 | $9.80, Nov 16 | PASS |  |  |
| TSLL | T6 | price vs 200-day average (S1 pattern sma values) | $9.80 vs $11.90 · -17.6% | $9.80 vs $11.90 · -17.7% | PASS |  |  |
| TSLL | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T7 | price vs 50-day average (S1 pattern sma values) | $9.80 vs $9.98 · -1.8% | $9.80 vs $9.98 · -1.8% | PASS |  |  |
| TSLL | T7w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -10.0% over 30 td | -10.0% over 30 td | PASS |  |  |
| TSLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 58.7% below $23.74 | 58.7% below $23.74 | PASS |  | closing high would be 23.03 |
| TSLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 58.7% below | PASS |  |  |
| TSLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $23.74 | $23.74 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -5.50%, close location 0.27, OBV falling |
| TSLL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| TSLL | V2 | day change of the last completed bar | down 5.5% | -5.50% | PASS |  |  |
| TSLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSLL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.6× from 2026-11-16 | 0.57× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| TSLL | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.57× | 2026-11-16 0.57× | PASS |  |  |
| TSLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.57× / 0.62× | 0.57× / 0.62× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 32105689) | 20 bars, last ('2026-11-16', 32105689) | PASS |  |  |
| TSM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $358.95 | $358.95 | PASS |  |  |
| TSM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $405.73 | $405.73 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSM | E3 | percent from the 21-day average | 11.5% below | 11.5% below | PASS |  |  |
| TSM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| TSM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.76 | $17.76 (sr=17.7604) | PASS |  | Wilder ATR14 |
| TSM | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| TSM | L-ema21 | ladder row ema21: price and gap = price vs average | $405.73, -11.5% | $405.73, -11.5% | PASS |  |  |
| TSM | L-note | "Last close $X · date" note = last completed bar | Last close $373.45 · Nov 16 | $373.45 · Nov 16 | PASS |  |  |
| TSM | L-now | ladder price row = compared price; name = the basis label | $358.95 "Now" | $358.94 "now" | PASS |  |  |
| TSM | L-sma200 | ladder row sma200: price and gap = price vs average | $403.25, -11.0% | $403.25, -11.0% | PASS |  |  |
| TSM | L-sma50 | ladder row sma50: price and gap = price vs average | $428.98, -16.3% | $428.98, -16.3% | PASS |  |  |
| TSM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $358.95 / entry $358.95 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.7 | 38.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +31.1% vs +10.1% | 31.1% vs 10.1% | PASS |  |  |
| TSM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSM | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.8 | 29.8 | PASS |  | Wilder, completed bars |
| TSM | T4w | words "20 or more / below 20" | 20 or more | ADX 29.8 | PASS |  |  |
| TSM | T5 | "counted at the last close ($X, date)" = last completed bar | $373.45, Nov 16 | $373.45, Nov 16 | PASS |  |  |
| TSM | T6 | price vs 200-day average (S1 pattern sma values) | $373.45 vs $403.25 · -7.4% | $373.45 vs $403.25 · -7.4% | PASS |  |  |
| TSM | T6w | word "Below" | Below | Below | PASS |  |  |
| TSM | T7 | price vs 50-day average (S1 pattern sma values) | $373.45 vs $428.98 · -12.9% | $373.45 vs $428.98 · -12.9% | PASS |  |  |
| TSM | T7w | word "Below" | Below | Below | PASS |  |  |
| TSM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.9% over 30 td | +3.9% over 30 td | PASS |  |  |
| TSM | T8r | word "rising" | still rising | rising | PASS |  |  |
| TSM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.4% below $487.47 | 23.4% below $487.47 | PASS |  | closing high would be 485.80 |
| TSM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.4% below | PASS |  |  |
| TSM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $487.47 | $487.47 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.34%, close location 0.08, OBV falling |
| TSM | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| TSM | V2 | day change of the last completed bar | down 6.3% | -6.34% | PASS |  |  |
| TSM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0761) | PASS |  |  |
| TSM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.6× from 2026-11-16 | 1.58× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| TSM | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.58× | 2026-11-16 1.58× | PASS |  |  |
| TSM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.58× / 1.33× | 1.58× / 1.33× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 19649731) | 20 bars, last ('2026-11-16', 19649731) | PASS |  |  |
| TSM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.58, OBV falling | condition true | PASS |  |  |
| UBOT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $14.92 | $14.92 | PASS |  |  |
| UBOT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.04 | $18.04 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UBOT | E3 | percent from the 21-day average | 17.3% below | 17.3% below | PASS |  |  |
| UBOT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 3:50pm ET) | session=regular | PASS |  |  |
| UBOT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.85 | $0.86 (sr=0.8546) | PASS |  | Wilder ATR14 |
| UBOT | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  · 3.6 day-moves below |
| UBOT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.0 | +7.0 | PASS |  |  |
| UBOT | L-ema21 | ladder row ema21: price and gap = price vs average | $18.04, -17.3% | $18.04, -17.3% | PASS |  |  |
| UBOT | L-note | "Last close $X · date" note = last completed bar | Last close $15.51 · Nov 16 | $15.51 · Nov 16 | PASS |  |  |
| UBOT | L-now | ladder price row = compared price; name = the basis label | $14.92 "Last trade 3:50pm ET" | $14.92 "last trade 3:50pm et" | PASS |  |  |
| UBOT | L-sma200 | ladder row sma200: price and gap = price vs average | $24.01, -37.9% | $24.01, -37.9% | PASS |  |  |
| UBOT | L-sma50 | ladder row sma50: price and gap = price vs average | $20.14, -25.9% | $20.14, -25.9% | PASS |  |  |
| UBOT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $14.92 / entry $14.92 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| UBOT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UBOT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.5 | 32.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UBOT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -35.8% vs +10.1% | -35.8% vs 10.1% | PASS |  |  |
| UBOT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UBOT | T4 | ADX 14 (S1 /api/sr meta.adx) | 37.7 | 37.6 | PASS |  | Wilder, completed bars |
| UBOT | T4w | words "20 or more / below 20" | 20 or more | ADX 37.6 | PASS |  |  |
| UBOT | T5 | "counted at the last close ($X, date)" = last completed bar | $15.51, Nov 16 | $15.51, Nov 16 | PASS |  |  |
| UBOT | T6 | price vs 200-day average (S1 pattern sma values) | $15.51 vs $24.01 · -35.4% | $15.51 vs $24.01 · -35.4% | PASS |  |  |
| UBOT | T6w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T7 | price vs 50-day average (S1 pattern sma values) | $15.51 vs $20.14 · -23.0% | $15.51 vs $20.14 · -23.0% | PASS |  |  |
| UBOT | T7w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.8% over 30 td | -4.8% over 30 td | PASS |  |  |
| UBOT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UBOT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UBOT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 51.7% below $32.08 | 51.7% below $32.08 | PASS |  | closing high would be 32.04 |
| UBOT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 51.7% below | PASS |  |  |
| UBOT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $32.08 | $32.08 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UBOT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.01%, close location 0.08, OBV falling |
| UBOT | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| UBOT | V2 | day change of the last completed bar | down 7.0% | -7.01% | PASS |  |  |
| UBOT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0794) | PASS |  |  |
| UBOT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UBOT | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.08× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| UBOT | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.08× | 2026-11-16 1.08× | PASS |  |  |
| UBOT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.08× / 1.27× | 1.08× / 1.27× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UBOT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 17048) | 20 bars, last ('2026-11-16', 17048) | PASS |  |  |
| UFO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.54 | $39.54 | PASS |  |  |
| UFO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.64 | $40.64 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UFO | E3 | percent from the 21-day average | 2.7% below | 2.7% below | PASS |  |  |
| UFO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| UFO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.39 | $1.39 (sr=1.392) | PASS |  | Wilder ATR14 |
| UFO | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves below |
| UFO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.6 | +4.6 | PASS |  |  |
| UFO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.64, -2.7% | $40.64, -2.7% | PASS |  |  |
| UFO | L-now | ladder price row = compared price; name = the basis label | $39.54 "Last close" | $39.54 "last close" | PASS |  |  |
| UFO | L-sma200 | ladder row sma200: price and gap = price vs average | $47.02, -15.9% | $47.02, -15.9% | PASS |  |  |
| UFO | L-sma50 | ladder row sma50: price and gap = price vs average | $41.66, -5.1% | $41.66, -5.1% | PASS |  |  |
| UFO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UFO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.4 | 44.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UFO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +18.6% vs +10.1% | 18.6% vs 10.1% | PASS |  |  |
| UFO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UFO | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.5 | 24.6 | PASS |  | Wilder, completed bars |
| UFO | T4w | words "20 or more / below 20" | 20 or more | ADX 24.6 | PASS |  |  |
| UFO | T6w | word "Below" | Below | Below | PASS |  |  |
| UFO | T7 | price vs 50-day average (S1 pattern sma values) | $39.54 vs $41.66 · -5.1% | $39.54 vs $41.66 · -5.1% | PASS |  |  |
| UFO | T7w | word "Below" | Below | Below | PASS |  |  |
| UFO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.7% over 30 td | -0.7% over 30 td | PASS |  |  |
| UFO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UFO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UFO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 42.0% below | PASS |  |  |
| UFO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.83%, close location 0.19, OBV falling |
| UFO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| UFO | V2 | day change of the last completed bar | down 2.8% | -2.83% | PASS |  |  |
| UFO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.19 (raw 0.1913) | PASS |  |  |
| UFO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UFO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.5× from 2026-11-16 | 0.53× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| UFO | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.53× | 2026-11-16 0.53× | PASS |  |  |
| UFO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.53× / 0.80× | 0.53× / 0.80× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UFO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 136900) | 20 bars, last ('2026-11-16', 136900) | PASS |  |  |
| URA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.00 | $30.00 | PASS |  |  |
| URA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $33.9 | $33.90 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| URA | E3 | percent from the 21-day average | 11.5% below | 11.5% below | PASS |  |  |
| URA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| URA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.47 | $1.47 (sr=1.4673) | PASS |  | Wilder ATR14 |
| URA | E5 | distance in normal day-moves | 2.7 | 2.7 | PASS |  | gauge dot note uses the same number:  · 2.7 day-moves below |
| URA | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.1 | +8.1 | PASS |  |  |
| URA | L-ema21 | ladder row ema21: price and gap = price vs average | $33.9, -11.5% | $33.90, -11.5% | PASS |  |  |
| URA | L-note | "Last close $X · date" note = last completed bar | Last close $30.44 · Nov 16 | $30.44 · Nov 16 | PASS |  |  |
| URA | L-now | ladder price row = compared price; name = the basis label | $30 "Now" | $30.00 "now" | PASS |  |  |
| URA | L-sma200 | ladder row sma200: price and gap = price vs average | $45.8, -34.5% | $45.80, -34.5% | PASS |  |  |
| URA | L-sma50 | ladder row sma50: price and gap = price vs average | $37.84, -20.7% | $37.84, -20.7% | PASS |  |  |
| URA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $30.00 / entry $30.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| URA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| URA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.3 | 33.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| URA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -28.7% vs +10.1% | -28.7% vs 10.1% | PASS |  |  |
| URA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| URA | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.4 | 32.4 | PASS |  | Wilder, completed bars |
| URA | T4w | words "20 or more / below 20" | 20 or more | ADX 32.4 | PASS |  |  |
| URA | T5 | "counted at the last close ($X, date)" = last completed bar | $30.44, Nov 16 | $30.44, Nov 16 | PASS |  |  |
| URA | T6 | price vs 200-day average (S1 pattern sma values) | $30.44 vs $45.80 · -33.5% | $30.44 vs $45.80 · -33.5% | PASS |  |  |
| URA | T6w | word "Below" | Below | Below | PASS |  |  |
| URA | T7 | price vs 50-day average (S1 pattern sma values) | $30.44 vs $37.84 · -19.6% | $30.44 vs $37.84 · -19.6% | PASS |  |  |
| URA | T7w | word "Below" | Below | Below | PASS |  |  |
| URA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.7% over 30 td | -4.7% over 30 td | PASS |  |  |
| URA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| URA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| URA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 51.1% below $62.28 | 51.1% below $62.28 | PASS |  | closing high would be 61.81 |
| URA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 51.1% below | PASS |  |  |
| URA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $62.28 | $62.279998779296875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| URA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.40%, close location 0.11, OBV falling |
| URA | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| URA | V2 | day change of the last completed bar | down 4.4% | -4.40% | PASS |  |  |
| URA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1148) | PASS |  |  |
| URA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| URA | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 1.00× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| URA | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.00× | 2026-11-16 1.00× | PASS |  |  |
| URA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.00× / 0.91× | 1.00× / 0.91× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| URA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 3946500) | 20 bars, last ('2026-11-16', 3946500) | PASS |  |  |
| URAA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $11.31 | $11.31 | PASS |  |  |
| URAA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $14.45 | $14.45 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| URAA | E3 | percent from the 21-day average | 21.7% below | 21.7% below | PASS |  |  |
| URAA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (last trade 3:50pm ET) | session=regular | PASS |  |  |
| URAA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.22 | $1.22 (sr=1.2214) | PASS |  | Wilder ATR14 |
| URAA | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| URAA | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.4 | +12.4 | PASS |  |  |
| URAA | L-ema21 | ladder row ema21: price and gap = price vs average | $14.45, -21.7% | $14.45, -21.7% | PASS |  |  |
| URAA | L-note | "Last close $X · date" note = last completed bar | Last close $11.71 · Nov 16 | $11.71 · Nov 16 | PASS |  |  |
| URAA | L-now | ladder price row = compared price; name = the basis label | $11.31 "Last trade 3:50pm ET" | $11.31 "last trade 3:50pm et" | PASS |  |  |
| URAA | L-sma200 | ladder row sma200: price and gap = price vs average | $29.6, -61.8% | $29.60, -61.8% | PASS |  |  |
| URAA | L-sma50 | ladder row sma50: price and gap = price vs average | $17.93, -36.9% | $17.93, -36.9% | PASS |  |  |
| URAA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $11.31 / entry $11.31 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| URAA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| URAA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.0 | 34.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| URAA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -63.1% vs +10.1% | -63.2% vs 10.1% | PASS |  |  |
| URAA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| URAA | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.4 | 30.5 | PASS |  | Wilder, completed bars |
| URAA | T4w | words "20 or more / below 20" | 20 or more | ADX 30.5 | PASS |  |  |
| URAA | T5 | "counted at the last close ($X, date)" = last completed bar | $11.71, Nov 16 | $11.71, Nov 16 | PASS |  |  |
| URAA | T6 | price vs 200-day average (S1 pattern sma values) | $11.71 vs $29.60 · -60.4% | $11.71 vs $29.60 · -60.4% | PASS |  |  |
| URAA | T6w | word "Below" | Below | Below | PASS |  |  |
| URAA | T7 | price vs 50-day average (S1 pattern sma values) | $11.71 vs $17.93 · -34.7% | $11.71 vs $17.93 · -34.7% | PASS |  |  |
| URAA | T7w | word "Below" | Below | Below | PASS |  |  |
| URAA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -11.8% over 30 td | -11.8% over 30 td | PASS |  |  |
| URAA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| URAA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| URAA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 81.2% below $62.21 | 81.2% below $62.21 | PASS |  | closing high would be 61.16 |
| URAA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 81.2% below | PASS |  |  |
| URAA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $62.21 | $62.21386524011286 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| URAA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.80%, close location 0.23, OBV falling |
| URAA | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| URAA | V2 | day change of the last completed bar | down 7.8% | -7.80% | PASS |  |  |
| URAA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.23 (raw 0.2258) | PASS |  |  |
| URAA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| URAA | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 0.98× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| URAA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 69500) | 20 bars, last ('2026-11-16', 69500) | PASS |  |  |
| V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $417.08 | $417.08 | PASS |  |  |
| V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $414.8 | $414.80 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| V | E3 | percent from the 21-day average | 0.6% above | 0.6% above | PASS |  |  |
| V | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.73 | $8.73 (sr=8.7332) | PASS |  | Wilder ATR14 |
| V | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -7.7 | -7.7 | PASS |  |  |
| V | L-ema21 | ladder row ema21: price and gap = price vs average | $414.8, 0.6% | $414.80, 0.6% | PASS |  |  |
| V | L-note | "Last close $X · date" note = last completed bar | Last close $426.46 · Nov 16 | $426.46 · Nov 16 | PASS |  |  |
| V | L-now | ladder price row = compared price; name = the basis label | $417.08 "Now" | $417.08 "now" | PASS |  |  |
| V | L-sma200 | ladder row sma200: price and gap = price vs average | $347.58, 20.0% | $347.58, 20.0% | PASS |  |  |
| V | L-sma50 | ladder row sma50: price and gap = price vs average | $391.39, 6.6% | $391.39, 6.6% | PASS |  |  |
| V | S5-price | S5: the same live price reads the same on the header and the Entry block | header $417.08 / entry $417.08 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 63.3 | 63.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +29.2% vs +10.1% | 29.2% vs 10.1% | PASS |  |  |
| V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| V | T4 | ADX 14 (S1 /api/sr meta.adx) | 39.0 | 39.0 | PASS |  | Wilder, completed bars |
| V | T4w | words "20 or more / below 20" | 20 or more | ADX 39.0 | PASS |  |  |
| V | T5 | "counted at the last close ($X, date)" = last completed bar | $426.46, Nov 16 | $426.46, Nov 16 | PASS |  |  |
| V | T6 | price vs 200-day average (S1 pattern sma values) | $426.46 vs $347.58 · +22.7% | $426.46 vs $347.58 · 22.7% | PASS |  |  |
| V | T6w | word "Above" | Above | Above | PASS |  |  |
| V | T7 | price vs 50-day average (S1 pattern sma values) | $426.46 vs $391.39 · +9.0% | $426.46 vs $391.39 · 9.0% | PASS |  |  |
| V | T7w | word "Above" | Above | Above | PASS |  |  |
| V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.0% over 30 td | +3.0% over 30 td | PASS |  |  |
| V | T8r | word "rising" | still rising | rising | PASS |  |  |
| V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.6% below $442.23 | 3.6% below $442.23 | PASS |  | closing high would be 436.57 |
| V | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.6% below | PASS |  |  |
| V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $442.23 | $442.2254 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| V | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.16%, close location 0.22, OBV rising |
| V | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| V | V2 | day change of the last completed bar | up 0.2% | +0.16% | PASS |  |  |
| V | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2176) | PASS |  |  |
| V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| V | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.14× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| V | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.14× | 2026-11-16 1.14× | PASS |  |  |
| V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.14× / 0.08× | 1.14× / 0.08× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 7398910) | 20 bars, last ('2026-11-16', 7398910) | PASS |  |  |
| VFV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $185.58 | $185.58 | PASS |  |  |
| VFV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $190.38 | $190.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VFV.TO | E3 | percent from the 21-day average | 2.5% below | 2.5% below | PASS |  |  |
| VFV.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| VFV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.78 | $2.78 (sr=2.7837) | PASS |  | Wilder ATR14 |
| VFV.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| VFV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $190.38, -2.5% | $190.38, -2.5% | PASS |  |  |
| VFV.TO | L-now | ladder price row = compared price; name = the basis label | $185.58 "Now" | $185.58 "now" | PASS |  |  |
| VFV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $180.48, 2.8% | $180.48, 2.8% | PASS |  |  |
| VFV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $191.32, -3.0% | $191.32, -3.0% | PASS |  |  |
| VFV.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $185.58 / entry $185.58 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| VFV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VFV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.8 | 51.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VFV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +15.1% vs +10.1% | 15.1% vs 10.1% | PASS |  |  |
| VFV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VFV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.4 | 19.4 | PASS |  | Wilder, completed bars |
| VFV.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.4 | PASS |  |  |
| VFV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $191.40 vs $180.48 · +6.1% | $191.40 vs $180.48 · 6.1% | PASS |  |  |
| VFV.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| VFV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $191.40 vs $191.32 · +0.0% | $191.40 vs $191.32 · 0.0% | PASS |  |  |
| VFV.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| VFV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| VFV.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| VFV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VFV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.3% below $197.83 | 3.3% below $197.83 | PASS |  | closing high would be 197.56 |
| VFV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.3% below | PASS |  |  |
| VFV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $197.83 | $197.8300018310547 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VFV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -0.34%, close location 0.54, OBV flat |
| VFV.TO | V2 | day change of the last completed bar | down 0.3% | -0.34% | PASS |  |  |
| VFV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| VFV.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-13 | 0.79× from 2026-11-13 | PASS |  | window "50 bars" includes the bar itself |
| VFV.TO | V6 | Volume detail: last session date and RVOL | 2026-11-13 0.79× | 2026-11-13 0.79× | PASS |  |  |
| VFV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.79× / 0.23× | 0.79× / 0.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VFV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-13', 244200) | 20 bars, last ('2026-11-13', 244200) | PASS |  |  |
| VRT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $188.16 | $188.16 | PASS |  |  |
| VRT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $209.67 | $209.67 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VRT | E3 | percent from the 21-day average | 10.3% below | 10.3% below | PASS |  |  |
| VRT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| VRT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.10 | $17.10 (sr=17.1008) | PASS |  | Wilder ATR14 |
| VRT | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| VRT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.6 | +3.6 | PASS |  |  |
| VRT | L-ema21 | ladder row ema21: price and gap = price vs average | $209.67, -10.3% | $209.67, -10.3% | PASS |  |  |
| VRT | L-note | "Last close $X · date" note = last completed bar | Last close $188.67 · Nov 16 | $188.67 · Nov 16 | PASS |  |  |
| VRT | L-now | ladder price row = compared price; name = the basis label | $188.16 "Now" | $188.16 "now" | PASS |  |  |
| VRT | L-sma200 | ladder row sma200: price and gap = price vs average | $271.59, -30.7% | $271.59, -30.7% | PASS |  |  |
| VRT | L-sma50 | ladder row sma50: price and gap = price vs average | $229.47, -18.0% | $229.47, -18.0% | PASS |  |  |
| VRT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $188.16 / entry $188.16 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| VRT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VRT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.0 | 41.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VRT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +10.3% vs +10.1% | 10.4% vs 10.1% | PASS |  |  |
| VRT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VRT | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.0 | 22.0 | PASS |  | Wilder, completed bars |
| VRT | T4w | words "20 or more / below 20" | 20 or more | ADX 22.0 | PASS |  |  |
| VRT | T5 | "counted at the last close ($X, date)" = last completed bar | $188.67, Nov 16 | $188.67, Nov 16 | PASS |  |  |
| VRT | T6 | price vs 200-day average (S1 pattern sma values) | $188.67 vs $271.59 · -30.5% | $188.67 vs $271.59 · -30.5% | PASS |  |  |
| VRT | T6w | word "Below" | Below | Below | PASS |  |  |
| VRT | T7 | price vs 50-day average (S1 pattern sma values) | $188.67 vs $229.47 · -17.8% | $188.67 vs $229.47 · -17.8% | PASS |  |  |
| VRT | T7w | word "Below" | Below | Below | PASS |  |  |
| VRT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.5% over 30 td | +2.5% over 30 td | PASS |  |  |
| VRT | T8r | word "rising" | still rising | rising | PASS |  |  |
| VRT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VRT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 50.3% below $379.94 | 50.3% below $379.94 | PASS |  | closing high would be 376.23 |
| VRT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 50.3% below | PASS |  |  |
| VRT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $379.94 | $379.935 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VRT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -6.63%, close location 0.25, OBV falling |
| VRT | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| VRT | V2 | day change of the last completed bar | down 6.6% | -6.63% | PASS |  |  |
| VRT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| VRT | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.07× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| VRT | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.07× | 2026-11-16 1.07× | PASS |  |  |
| VRT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.07× / 0.73× | 1.07× / 0.73× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VRT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 7231785) | 20 bars, last ('2026-11-16', 7231785) | PASS |  |  |
| WDC.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.89 | $17.89 | PASS |  |  |
| WDC.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $20.27 | $20.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WDC.TO | E3 | percent from the 21-day average | 11.8% below | 11.8% below | PASS |  |  |
| WDC.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| WDC.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.59 | $1.59 (sr=1.5936) | PASS |  | Wilder ATR14 |
| WDC.TO | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| WDC.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $20.27, -11.8% | $20.27, -11.8% | PASS |  |  |
| WDC.TO | L-now | ladder price row = compared price; name = the basis label | $17.89 "Last close" | $17.89 "last close" | PASS |  |  |
| WDC.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $23.86, -25.0% | $23.86, -25.0% | PASS |  |  |
| WDC.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.2 | 38.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WDC.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.8 | 32.8 | PASS |  | Wilder, completed bars |
| WDC.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.8 | PASS |  |  |
| WDC.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -4.94%, close location 0.34, OBV falling |
| WDC.TO | V2 | day change of the last completed bar | down 4.9% | -4.94% | PASS |  |  |
| WDC.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| WDC.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-13 | 0.78× from 2026-11-13 | PASS |  | window "50 bars" includes the bar itself |
| WDC.TO | V6 | Volume detail: last session date and RVOL | 2026-11-13 0.78× | 2026-11-13 0.78× | PASS |  |  |
| WDC.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.78× / 0.55× | 0.78× / 0.55× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WDC.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-13', 124300) | 20 bars, last ('2026-11-13', 124300) | PASS |  |  |
| WELL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $244.65 | $244.65 | PASS |  |  |
| WELL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $240.81 | $240.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WELL | E3 | percent from the 21-day average | 1.6% above | 1.6% above | PASS |  |  |
| WELL | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| WELL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.33 | $5.33 (sr=5.3272) | PASS |  | Wilder ATR14 |
| WELL | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves above |
| WELL | L-ema21 | ladder row ema21: price and gap = price vs average | $240.81, 1.6% | $240.81, 1.6% | PASS |  |  |
| WELL | L-now | ladder price row = compared price; name = the basis label | $244.65 "Last close" | $244.65 "last close" | PASS |  |  |
| WELL | L-sma200 | ladder row sma200: price and gap = price vs average | $221.73, 10.3% | $221.73, 10.3% | PASS |  |  |
| WELL | L-sma50 | ladder row sma50: price and gap = price vs average | $234.71, 4.2% | $234.71, 4.2% | PASS |  |  |
| WELL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WELL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 58.4 | 58.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WELL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +26.2% vs +10.1% | 26.2% vs 10.1% | PASS |  |  |
| WELL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WELL | T4 | ADX 14 (S1 /api/sr meta.adx) | 12.7 | 12.7 | PASS |  | Wilder, completed bars |
| WELL | T4w | words "20 or more / below 20" | below 20 | ADX 12.7 | PASS |  |  |
| WELL | T6 | price vs 200-day average (S1 pattern sma values) | $244.65 vs $221.73 · +10.3% | $244.65 vs $221.73 · 10.3% | PASS |  |  |
| WELL | T6w | word "Above" | Above | Above | PASS |  |  |
| WELL | T7 | price vs 50-day average (S1 pattern sma values) | $244.65 vs $234.71 · +4.2% | $244.65 vs $234.71 · 4.2% | PASS |  |  |
| WELL | T7w | word "Above" | Above | Above | PASS |  |  |
| WELL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.5% over 30 td | +3.5% over 30 td | PASS |  |  |
| WELL | T8r | word "rising" | still rising | rising | PASS |  |  |
| WELL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WELL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.1% below $255.20 | 4.1% below $255.20 | PASS |  | closing high would be 252.07 |
| WELL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.1% below | PASS |  |  |
| WELL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $255.20 | $255.2 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WELL | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| WELL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0633) | PASS |  |  |
| WELL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| WELL | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-16 | 0.95× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| WELL | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.95× | 2026-11-16 0.95× | PASS |  |  |
| WELL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.95× / 0.04× | 0.95× / 0.04× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WELL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 2657186) | 20 bars, last ('2026-11-16', 2657186) | PASS |  |  |
| WMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $127.64 | $127.64 | PASS |  |  |
| WMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $123.23 | $123.23 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WMT | E3 | percent from the 21-day average | 3.6% above | 3.6% above | PASS |  |  |
| WMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| WMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.73 | $2.73 (sr=2.7322) | PASS |  | Wilder ATR14 |
| WMT | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves above |
| WMT | L-ema21 | ladder row ema21: price and gap = price vs average | $123.23, 3.6% | $123.23, 3.6% | PASS |  |  |
| WMT | L-note | "Last close $X · date" note = last completed bar | Last close $128.41 · Nov 16 | $128.41 · Nov 16 | PASS |  |  |
| WMT | L-now | ladder price row = compared price; name = the basis label | $127.64 "Now" | $127.64 "now" | PASS |  |  |
| WMT | L-sma200 | ladder row sma200: price and gap = price vs average | $118.98, 7.3% | $118.98, 7.3% | PASS |  |  |
| WMT | L-sma50 | ladder row sma50: price and gap = price vs average | $114.96, 11.0% | $114.96, 11.0% | PASS |  |  |
| WMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $127.64 / entry $127.64 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| WMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 68.4 | 68.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.3% vs +10.1% | 25.3% vs 10.1% | PASS |  |  |
| WMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 47.0 | 47.0 | PASS |  | Wilder, completed bars |
| WMT | T4w | words "20 or more / below 20" | 20 or more | ADX 47.0 | PASS |  |  |
| WMT | T5 | "counted at the last close ($X, date)" = last completed bar | $128.41, Nov 16 | $128.41, Nov 16 | PASS |  |  |
| WMT | T6 | price vs 200-day average (S1 pattern sma values) | $128.41 vs $118.98 · +7.9% | $128.41 vs $118.98 · 7.9% | PASS |  |  |
| WMT | T6w | word "Above" | Above | Above | PASS |  |  |
| WMT | T7 | price vs 50-day average (S1 pattern sma values) | $128.41 vs $114.96 · +11.7% | $128.41 vs $114.96 · 11.7% | PASS |  |  |
| WMT | T7w | word "Above" | Above | Above | PASS |  |  |
| WMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.6% over 30 td | +0.6% over 30 td | PASS |  |  |
| WMT | T8r | word "rising" | still rising | rising | PASS |  |  |
| WMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.0% below $135.16 | 5.0% below $135.16 | PASS |  | closing high would be 134.20 |
| WMT | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.0% below | PASS |  |  |
| WMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $135.16 | $135.155 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.25%, close location 0.27, OBV rising |
| WMT | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| WMT | V2 | day change of the last completed bar | up 0.3% | +0.25% | PASS |  |  |
| WMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| WMT | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.8× from 2026-11-16 | 0.82× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| WMT | V6 | Volume detail: last session date and RVOL | 2026-11-16 0.82× | 2026-11-16 0.82× | PASS |  |  |
| WMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.82× / 0.12× | 0.82× / 0.12× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 17780238) | 20 bars, last ('2026-11-16', 17780238) | PASS |  |  |
| XCHP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $103.82 | $103.82 | PASS |  |  |
| XCHP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $114.81 | $114.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XCHP.TO | E3 | percent from the 21-day average | 9.6% below | 9.6% below | PASS |  |  |
| XCHP.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| XCHP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.38 | $6.38 (sr=6.3772) | PASS |  | Wilder ATR14 |
| XCHP.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| XCHP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $114.81, -9.6% | $114.81, -9.6% | PASS |  |  |
| XCHP.TO | L-note | "Last close $X · date" note = last completed bar | Last close $105.33 · Nov 16 | $105.33 · Nov 16 | PASS |  |  |
| XCHP.TO | L-now | ladder price row = compared price; name = the basis label | $103.82 "Now" | $103.82 "now" | PASS |  |  |
| XCHP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $116.46, -10.9% | $116.46, -10.9% | PASS |  |  |
| XCHP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $125.56, -17.3% | $125.56, -17.3% | PASS |  |  |
| XCHP.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $103.82 / entry $103.82 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| XCHP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XCHP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.5 | 39.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XCHP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.5% vs +10.1% | 49.5% vs 10.1% | PASS |  |  |
| XCHP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XCHP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.6 | 32.6 | PASS |  | Wilder, completed bars |
| XCHP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.6 | PASS |  |  |
| XCHP.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $105.33, Nov 16 | $105.33, Nov 16 | PASS |  |  |
| XCHP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $105.33 vs $116.46 · -9.6% | $105.33 vs $116.46 · -9.6% | PASS |  |  |
| XCHP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $105.33 vs $125.56 · -16.1% | $105.33 vs $125.56 · -16.1% | PASS |  |  |
| XCHP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.9% over 30 td | +5.9% over 30 td | PASS |  |  |
| XCHP.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XCHP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XCHP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.7% below $161.26 | 34.7% below $161.26 | PASS |  | closing high would be 160.97 |
| XCHP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.7% below | PASS |  |  |
| XCHP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $161.26 | $161.25523669513825 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XCHP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -5.17%, close location 0.40, OBV falling |
| XCHP.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XCHP.TO | V2 | day change of the last completed bar | down 5.2% | -5.17% | PASS |  |  |
| XCHP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XCHP.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-16 | 1.04× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| XCHP.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.04× | 2026-11-16 1.04× | PASS |  |  |
| XCHP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.04× / 0.85× | 1.04× / 0.85× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XCHP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 51600) | 20 bars, last ('2026-11-16', 51600) | PASS |  |  |
| XDRV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.69 | $39.69 | PASS |  |  |
| XDRV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $41.54 | $41.54 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XDRV.TO | E3 | percent from the 21-day average | 4.4% below | 4.4% below | PASS |  |  |
| XDRV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XDRV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.86 | $0.86 (sr=0.8624) | PASS |  | Wilder ATR14 |
| XDRV.TO | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| XDRV.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.1 | +7.1 | PASS |  |  |
| XDRV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $41.54, -4.4% | $41.54, -4.4% | PASS |  |  |
| XDRV.TO | L-now | ladder price row = compared price; name = the basis label | $39.69 "Last close" | $39.69 "last close" | PASS |  |  |
| XDRV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $47.65, -16.7% | $47.65, -16.7% | PASS |  |  |
| XDRV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $43.66, -9.1% | $43.66, -9.1% | PASS |  |  |
| XDRV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XDRV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.9 | 39.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XDRV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.5% vs +10.1% | -5.5% vs 10.1% | PASS |  |  |
| XDRV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XDRV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.4 | 22.4 | PASS |  | Wilder, completed bars |
| XDRV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.4 | PASS |  |  |
| XDRV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $39.69 vs $47.65 · -16.7% | $39.69 vs $47.65 · -16.7% | PASS |  |  |
| XDRV.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $39.69 vs $43.66 · -9.1% | $39.69 vs $43.66 · -9.1% | PASS |  |  |
| XDRV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.5% over 30 td | -0.5% over 30 td | PASS |  |  |
| XDRV.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XDRV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XDRV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.3% below $61.36 | 35.3% below $61.36 | PASS |  | closing high would be 61.36 |
| XDRV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.3% below | PASS |  |  |
| XDRV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $61.36 | $61.35662078857422 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XDRV.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 44 of 50 days empty | 44 of 50 days empty | PASS |  |  |
| XEQT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $44.24 | $44.24 | PASS |  |  |
| XEQT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $45.22 | $45.22 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XEQT.TO | E3 | percent from the 21-day average | 2.2% below | 2.2% below | PASS |  |  |
| XEQT.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| XEQT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.57 | $0.57 (sr=0.5658) | PASS |  | Wilder ATR14 |
| XEQT.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| XEQT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $45.22, -2.2% | $45.22, -2.2% | PASS |  |  |
| XEQT.TO | L-note | "Last close $X · date" note = last completed bar | Last close $44.86 · Nov 16 | $44.86 · Nov 16 | PASS |  |  |
| XEQT.TO | L-now | ladder price row = compared price; name = the basis label | $44.24 "Now" | $44.24 "now" | PASS |  |  |
| XEQT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $43.55, 1.6% | $43.55, 1.6% | PASS |  |  |
| XEQT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $45.41, -2.6% | $45.41, -2.6% | PASS |  |  |
| XEQT.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $44.24 / entry $44.24 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| XEQT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XEQT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.1 | 46.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XEQT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +15.2% vs +10.1% | 15.2% vs 10.1% | PASS |  |  |
| XEQT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XEQT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.8 | 14.8 | PASS |  | Wilder, completed bars |
| XEQT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 14.8 | PASS |  |  |
| XEQT.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $44.86, Nov 16 | $44.86, Nov 16 | PASS |  |  |
| XEQT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $44.86 vs $43.55 · +3.0% | $44.86 vs $43.55 · 3.0% | PASS |  |  |
| XEQT.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| XEQT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $44.86 vs $45.41 · -1.2% | $44.86 vs $45.41 · -1.2% | PASS |  |  |
| XEQT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XEQT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| XEQT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XEQT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XEQT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.3% below $46.38 | 3.3% below $46.38 | PASS |  | closing high would be 46.27 |
| XEQT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.3% below | PASS |  |  |
| XEQT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.38 | $46.380001068115234 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XEQT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.45%, close location 0.11, OBV falling |
| XEQT.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XEQT.TO | V2 | day change of the last completed bar | down 1.4% | -1.45% | PASS |  |  |
| XEQT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1094) | PASS |  |  |
| XEQT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XEQT.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.5× from 2026-11-16 | 1.46× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| XEQT.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.46× | 2026-11-16 1.46× | PASS |  |  |
| XEQT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.46× / 1.15× | 1.46× / 1.15× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XEQT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 1297200) | 20 bars, last ('2026-11-16', 1297200) | PASS |  |  |
| XETM.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $61.57 | $61.57 | PASS |  |  |
| XETM.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $69.07 | $69.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XETM.TO | E3 | percent from the 21-day average | 10.9% below | 10.9% below | PASS |  |  |
| XETM.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XETM.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.51 | $2.51 (sr=2.5104) | PASS |  | Wilder ATR14 |
| XETM.TO | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| XETM.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.3 | +4.3 | PASS |  |  |
| XETM.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $69.07, -10.9% | $69.07, -10.9% | PASS |  |  |
| XETM.TO | L-now | ladder price row = compared price; name = the basis label | $61.57 "Last close" | $61.57 "last close" | PASS |  |  |
| XETM.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $79.98, -23.0% | $79.98, -23.0% | PASS |  |  |
| XETM.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $75.71, -18.7% | $75.71, -18.7% | PASS |  |  |
| XETM.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.2 | 33.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XETM.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -26.9% vs +10.1% | -26.9% vs 10.1% | PASS |  |  |
| XETM.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.9 | 20.9 | PASS |  | Wilder, completed bars |
| XETM.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 20.9 | PASS |  |  |
| XETM.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.06%, close location 0.01, OBV falling |
| XETM.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XETM.TO | V2 | day change of the last completed bar | down 6.1% | -6.06% | PASS |  |  |
| XETM.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0121) | PASS |  |  |
| XETM.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XETM.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 2.7× from 2026-11-16 | 2.74× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| XETM.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 2.74× | 2026-11-16 2.74× | PASS |  |  |
| XETM.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.74× / 1.49× | 2.74× / 1.49× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XETM.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 8300) | 20 bars, last ('2026-11-16', 8300) | PASS |  |  |
| XETM.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.74, OBV falling | condition true | PASS |  |  |
| XGD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $50.80 | $50.80 | PASS |  |  |
| XGD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $53.29 | $53.29 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XGD.TO | E3 | percent from the 21-day average | 4.7% below | 4.7% below | PASS |  |  |
| XGD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XGD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.08 | $2.08 (sr=2.0762) | PASS |  | Wilder ATR14 |
| XGD.TO | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| XGD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $53.29, -4.7% | $53.29, -4.7% | PASS |  |  |
| XGD.TO | L-now | ladder price row = compared price; name = the basis label | $50.8 "Last close" | $50.80 "last close" | PASS |  |  |
| XGD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $55.16, -7.9% | $55.16, -7.9% | PASS |  |  |
| XGD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $55.43, -8.4% | $55.43, -8.4% | PASS |  |  |
| XGD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XGD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.8 | 42.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XGD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +10.2% vs +10.1% | 10.1% vs 10.1% | PASS |  |  |
| XGD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XGD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.3 | 17.3 | PASS |  | Wilder, completed bars |
| XGD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 17.3 | PASS |  |  |
| XGD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $50.80 vs $55.16 · -7.9% | $50.80 vs $55.16 · -7.9% | PASS |  |  |
| XGD.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $50.80 vs $55.43 · -8.4% | $50.80 vs $55.43 · -8.4% | PASS |  |  |
| XGD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.9% over 30 td | -0.9% over 30 td | PASS |  |  |
| XGD.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XGD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XGD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.9% below $69.54 | 26.9% below $69.54 | PASS |  | closing high would be 68.70 |
| XGD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.9% below | PASS |  |  |
| XGD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $69.54 | $69.54086233267267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XGD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.05%, close location 0.00, OBV falling |
| XGD.TO | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XGD.TO | V2 | day change of the last completed bar | down 3.0% | -3.05% | PASS |  |  |
| XGD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| XGD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XGD.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.9× from 2026-11-16 | 1.88× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| XGD.TO | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.88× | 2026-11-16 1.88× | PASS |  |  |
| XGD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.88× / 0.75× | 1.88× / 0.75× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XGD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 867100) | 20 bars, last ('2026-11-16', 867100) | PASS |  |  |
| XGD.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.88, OBV falling | condition true | PASS |  |  |
| XOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $166.96 | $166.96 | PASS |  |  |
| XOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $170.41 | $170.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XOM | E3 | percent from the 21-day average | 2.0% below | 2.0% below | PASS |  |  |
| XOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (now) | session=regular | PASS |  |  |
| XOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.25 | $4.25 (sr=4.2479) | PASS |  | Wilder ATR14 |
| XOM | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves below |
| XOM | L-ema21 | ladder row ema21: price and gap = price vs average | $170.41, -2.0% | $170.41, -2.0% | PASS |  |  |
| XOM | L-note | "Last close $X · date" note = last completed bar | Last close $166.87 · Nov 16 | $166.87 · Nov 16 | PASS |  |  |
| XOM | L-now | ladder price row = compared price; name = the basis label | $166.96 "Now" | $166.96 "now" | PASS |  |  |
| XOM | L-sma200 | ladder row sma200: price and gap = price vs average | $154.45, 8.1% | $154.45, 8.1% | PASS |  |  |
| XOM | L-sma50 | ladder row sma50: price and gap = price vs average | $168.48, -0.9% | $168.48, -0.9% | PASS |  |  |
| XOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $166.96 / entry $166.96 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| XOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.4 | 44.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +43.6% vs +10.1% | 43.6% vs 10.1% | PASS |  |  |
| XOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.1 | 27.0 | PASS |  | Wilder, completed bars |
| XOM | T4w | words "20 or more / below 20" | 20 or more | ADX 27.0 | PASS |  |  |
| XOM | T5 | "counted at the last close ($X, date)" = last completed bar | $166.87, Nov 16 | $166.87, Nov 16 | PASS |  |  |
| XOM | T6 | price vs 200-day average (S1 pattern sma values) | $166.87 vs $154.45 · +8.0% | $166.87 vs $154.45 · 8.0% | PASS |  |  |
| XOM | T6w | word "Above" | Above | Above | PASS |  |  |
| XOM | T7 | price vs 50-day average (S1 pattern sma values) | $166.87 vs $168.48 · -1.0% | $166.87 vs $168.48 · -1.0% | PASS |  |  |
| XOM | T7w | word "Below" | Below | Below | PASS |  |  |
| XOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.1% over 30 td | +5.1% over 30 td | PASS |  |  |
| XOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| XOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.9% below $187.32 | 10.9% below $187.32 | PASS |  | closing high would be 186.08 |
| XOM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.9% below | PASS |  |  |
| XOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $187.32 | $187.31766003760222 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.56%, close location 0.11, OBV falling |
| XOM | V10 | "last completed session, <date>" = the last completed bar | 2026-11-16 | 2026-11-16 | PASS |  |  |
| XOM | V2 | day change of the last completed bar | down 1.6% | -1.56% | PASS |  |  |
| XOM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1105) | PASS |  |  |
| XOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XOM | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.1× from 2026-11-16 | 1.06× from 2026-11-16 | PASS |  | window "50 bars" includes the bar itself |
| XOM | V6 | Volume detail: last session date and RVOL | 2026-11-16 1.06× | 2026-11-16 1.06× | PASS |  |  |
| XOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.06× / 0.61× | 1.06× / 0.61× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-16', 14286200) | 20 bars, last ('2026-11-16', 14286200) | PASS |  |  |
