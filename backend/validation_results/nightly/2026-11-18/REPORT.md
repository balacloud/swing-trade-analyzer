# Statement Audit report

Run: 2026-11-19T01:13 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM · ET at first dump: 11/18/2026, 8:58:46 PM

Verdicts: PASS 2987 · WRONG 24 (CRITICAL) · MISLEADING 4 (HIGH) · UNVERIFIED 285 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| AAPL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 50292200) | 20 bars, last ('2026-11-17', 37407500) | WRONG | CRITICAL |  |
| ABBV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 5493800) | 20 bars, last ('2026-11-17', 3947400) | WRONG | CRITICAL |  |
| ALAB | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 4625700) | 20 bars, last ('2026-11-17', 5203700) | WRONG | CRITICAL |  |
| ASTL.TO | T6 | price vs 200-day average (S1 pattern sma values) | $6.94 vs $6.26 · +10.9% | $6.94 vs $6.26 · 10.8% | WRONG | CRITICAL |  |
| AVGO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 27023000) | 20 bars, last ('2026-11-17', 26184000) | WRONG | CRITICAL |  |
| BOTZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 2 signals, 0 up, 2 down, 0 flat | WRONG | CRITICAL | change 0.00%, close location 0.20, OBV falling |
| BOTZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.98× / 0.00× | 0.98× / 0.00× | WRONG | CRITICAL | ATR % uses the sr price (may be a partial bar) |
| COTG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.2% below $17.80 | 7.1% below $17.80 | WRONG | CRITICAL | closing high would be 17.70 |
| HD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 6204200) | 20 bars, last ('2026-11-17', 7288300) | WRONG | CRITICAL |  |
| KEYS | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 2208400) | 20 bars, last ('2026-11-17', 1846800) | WRONG | CRITICAL |  |
| LLY | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 3207400) | 20 bars, last ('2026-11-17', 2641400) | WRONG | CRITICAL |  |
| META | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 11577900) | 20 bars, last ('2026-11-17', 12971800) | WRONG | CRITICAL |  |
| MRVL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 23235500) | 20 bars, last ('2026-11-17', 27118700) | WRONG | CRITICAL |  |
| MSFT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 30218600) | 20 bars, last ('2026-11-17', 27992800) | WRONG | CRITICAL |  |
| NFLX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-17', 35092700) | 20 bars, last ('2026-11-18', 26767110) | WRONG | CRITICAL |  |
| NVDA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 333822100) | 20 bars, last ('2026-11-17', 406985100) | WRONG | CRITICAL |  |
| PG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 14968400) | 20 bars, last ('2026-11-17', 8984200) | WRONG | CRITICAL |  |
| PNG.V | T7 | price vs 50-day average (S1 pattern sma values) | $2.99 vs $4.12 · -27.4% | $2.99 vs $4.12 · -27.5% | WRONG | CRITICAL |  |
| RBOT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 2 signals, 0 up, 2 down, 0 flat | WRONG | CRITICAL | change 0.00%, close location 0.21, OBV falling |
| RBOT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.41× / 0.00× | 0.41× / 0.00× | WRONG | CRITICAL | ATR % uses the sr price (may be a partial bar) |
| SMH | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-17', 12251100) | 20 bars, last ('2026-11-18', 7116300) | WRONG | CRITICAL |  |
| V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 7395300) | 20 bars, last ('2026-11-17', 5696200) | WRONG | CRITICAL |  |
| VRT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 7231800) | 20 bars, last ('2026-11-17', 5846000) | WRONG | CRITICAL |  |
| WMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 19 bars, last ('2026-11-16', 17780200) | 20 bars, last ('2026-11-17', 19841300) | WRONG | CRITICAL |  |
| ASTL.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.0 | 26.2 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| AVGC | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.1 | 19.8 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| AVGC | T4w | words "20 or more / below 20" | 20 or more | ADX 19.8 | MISLEADING | HIGH |  |
| DRAL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.5 | 34.8 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| AAPL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 37,407,500 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AAPU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.3× 0.32× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AAPU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 3,947,400 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AIPO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.07× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AIPO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 5,203,700 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AMD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.21× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.98× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMZN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.68× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMZU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 228 252. 2025 -12 -22 1.1× 1.07× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| ANET.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ASML.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.72× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ASTL.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.29× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ATD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | U1 | numbers on the card no statement above claimed (exhaustive scan) | 100 252. 1.6× 1.55× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AVGC | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 26,184,000 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AVGO.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 227 252. 2025 -12 -22 | each one claimed or exempt | UNVERIFIED | INFO | 5 unclaimed number token(s): add a statement or an exempt rule |
| AVGO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.01× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BDT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.98× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BOTZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.11× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BRK-B | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.99× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BRKU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.39× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CAMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.54× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CCO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | X0 | Technical Read card | not found | card text | UNVERIFIED | INFO | card did not render |
| CGY.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.72× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CGY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.29× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CNQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.98× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CNR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.13× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COP | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.57× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.6× 3.56× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 19 252. 2.2× 2.23× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| COPZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.95× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COST | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.47× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COTG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.80× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CSU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.16× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CVX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 10 252. 2.8× 2.84× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| DRAL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 160 252. 0.8× 0.84× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| DRAM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.52× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DRIV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.73× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DUK | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.70× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ELIL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.79× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| EQIX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.97× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ETN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.3× 2.34× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| FCX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.64× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| FINN.NE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.4× 2.39× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GDX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.3× 3.32× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GDXU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.73× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.99× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GEV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 228 252. 2025 -12 -22 1.3× 1.34× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| GEV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.47× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GGLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.97× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GIB-A.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.84× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GOOGL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 7,288,300 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| HURA.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.52× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HURA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.63× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HXQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.08× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| JNJ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| JPM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 1,846,800 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| LIN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.66× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| LIN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 2,641,400 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| MDA.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.42× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MDA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 12,971,800 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| METU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.3× 0.29× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| METU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 27,118,700 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| MSFT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 27,992,800 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| MSFU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.63× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MSFU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 210 252. 2026 -01 -20 0.2× 0.23× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| MTRX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.96× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.85× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NEE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.32× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NEM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -18 26,767,110 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| NFXL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.08× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NFXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.45× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NTR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 406,985,100 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| NVDL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.0× 3.05× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NVDL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.12× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ONTO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 141 252. 0.5× 0.51× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| ORBX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.42× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ORCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 8,984,200 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| PNG.V | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.07× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PNG.V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.69× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QCOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.15× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QPUX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.83× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QTUM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.41× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RBOT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.99× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RTX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.71× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 147 252. 0.5× 0.51× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SGRD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -18 7,116,300 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SNDK.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 134 252. 1.1× 1.10× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SNDK.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.00× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.63× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SOXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.10× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SOXX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 157 252. 0.6× 0.55× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SPCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.7× 0.74× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSLA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.6× 0.60× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.94× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.75× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| UBOT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.3× 0.28× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| UFO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 5,696,200 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| VFV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.78× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| VFV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 5,846,000 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| WDC.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 134 252. 0.6× 0.62× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| WDC.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.5× 1.50× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| WELL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2026 -11 -17 19,841,300 | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| XCHP.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.91× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XCHP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.19× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XEQT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 210 252. 2026 -01 -20 1.1× 1.14× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| XETM.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.41× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XGD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.33× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 56.3 | 56.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +32.0% vs +11.8% | 32.0% vs 11.8% | PASS |  |  |
| AAPL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $48.59 | $48.59 | PASS |  |  |
| AAPU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $47.62 | $47.62 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPU | E3 | percent from the 21-day average | 2.0% above | 2.0% above | PASS |  |  |
| AAPU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AAPU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.99 | $1.99 (sr=1.99) | PASS |  | Wilder ATR14 |
| AAPU | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| AAPU | L-ema21 | ladder row ema21: price and gap = price vs average | $47.62, 2.0% | $47.62, 2.0% | PASS |  |  |
| AAPU | L-note | "Last close $X · date" note = last completed bar | Last close $48.59 · Nov 18 | $48.59 · Nov 18 | PASS |  |  |
| AAPU | L-now | ladder price row = compared price; name = the basis label | $48.59 "After hours" | $48.59 "after hours" | PASS |  |  |
| AAPU | L-sma200 | ladder row sma200: price and gap = price vs average | $38.2, 27.2% | $38.20, 27.2% | PASS |  |  |
| AAPU | L-sma50 | ladder row sma50: price and gap = price vs average | $46.16, 5.3% | $46.16, 5.3% | PASS |  |  |
| AAPU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $48.59 / entry $48.59 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.1 | 55.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.9% vs +11.8% | 49.9% vs 11.8% | PASS |  |  |
| AAPU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPU | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.7 | 17.7 | PASS |  | Wilder, completed bars |
| AAPU | T4w | words "20 or more / below 20" | below 20 | ADX 17.7 | PASS |  |  |
| AAPU | T5 | "counted at the last close ($X, date)" = last completed bar | $48.59, Nov 18 | $48.59, Nov 18 | PASS |  |  |
| AAPU | T6 | price vs 200-day average (S1 pattern sma values) | $48.59 vs $38.20 · +27.2% | $48.59 vs $38.20 · 27.2% | PASS |  |  |
| AAPU | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T7 | price vs 50-day average (S1 pattern sma values) | $48.59 vs $46.16 · +5.3% | $48.59 vs $46.16 · 5.3% | PASS |  |  |
| AAPU | T7w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.9% over 30 td | +6.9% over 30 td | PASS |  |  |
| AAPU | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.8% below $51.04 | 4.8% below $51.04 | PASS |  | closing high would be 49.81 |
| AAPU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.8% below | PASS |  |  |
| AAPU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $51.04 | $51.040000915527344 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change 0.21%, close location 0.15, OBV falling |
| AAPU | V2 | day change of the last completed bar | up 0.2% | +0.21% | PASS |  |  |
| AAPU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1450) | PASS |  |  |
| AAPU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.32× / 0.05× | 0.32× / 0.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 279600) | 20 bars, last ('2026-11-18', 279600) | PASS |  |  |
| ABBV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.1 | 59.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ABBV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.9% vs +11.8% | 28.9% vs 11.8% | PASS |  |  |
| ABBV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AIPO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $22.69 | $22.69 | PASS |  |  |
| AIPO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $24.19 | $24.19 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AIPO | E3 | percent from the 21-day average | 6.2% below | 6.2% below | PASS |  |  |
| AIPO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AIPO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.09 | $1.09 (sr=1.092) | PASS |  | Wilder ATR14 |
| AIPO | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| AIPO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.9 | +3.9 | PASS |  |  |
| AIPO | L-ema21 | ladder row ema21: price and gap = price vs average | $24.19, -6.2% | $24.19, -6.2% | PASS |  |  |
| AIPO | L-note | "Last close $X · date" note = last completed bar | Last close $22.69 · Nov 18 | $22.69 · Nov 18 | PASS |  |  |
| AIPO | L-now | ladder price row = compared price; name = the basis label | $22.69 "After hours" | $22.69 "after hours" | PASS |  |  |
| AIPO | L-sma200 | ladder row sma200: price and gap = price vs average | $28.49, -20.3% | $28.49, -20.3% | PASS |  |  |
| AIPO | L-sma50 | ladder row sma50: price and gap = price vs average | $26.43, -14.1% | $26.43, -14.1% | PASS |  |  |
| AIPO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $22.69 / entry $22.69 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AIPO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AIPO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.9 | 38.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AIPO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.6% vs +11.8% | 2.6% vs 11.8% | PASS |  |  |
| AIPO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AIPO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.1 | 32.1 | PASS |  | Wilder, completed bars |
| AIPO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.1 | PASS |  |  |
| AIPO | T5 | "counted at the last close ($X, date)" = last completed bar | $22.69, Nov 18 | $22.69, Nov 18 | PASS |  |  |
| AIPO | T6 | price vs 200-day average (S1 pattern sma values) | $22.69 vs $28.49 · -20.4% | $22.69 vs $28.49 · -20.3% | PASS |  |  |
| AIPO | T6w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T7 | price vs 50-day average (S1 pattern sma values) | $22.69 vs $26.43 · -14.2% | $22.69 vs $26.43 · -14.1% | PASS |  |  |
| AIPO | T7w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.7% over 30 td | +0.7% over 30 td | PASS |  |  |
| AIPO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AIPO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AIPO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.8% below $34.79 | 34.8% below $34.79 | PASS |  | closing high would be 34.77 |
| AIPO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.8% below | PASS |  |  |
| AIPO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $34.79 | $34.790000915527344 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AIPO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.27%, close location 0.45, OBV falling |
| AIPO | V2 | day change of the last completed bar | up 0.3% | +0.27% | PASS |  |  |
| AIPO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AIPO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.07× / 0.06× | 1.07× / 0.06× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AIPO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1725149) | 20 bars, last ('2026-11-18', 1725149) | PASS |  |  |
| ALAB | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.0 | 38.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ALAB | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.7% vs +11.8% | 49.7% vs 11.8% | PASS |  |  |
| ALAB | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $530.14 | $530.14 | PASS |  |  |
| AMD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $524.07 | $524.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD | E3 | percent from the 21-day average | 1.2% above | 1.2% above | PASS |  |  |
| AMD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $40.33 | $40.33 (sr=40.3313) | PASS |  | Wilder ATR14 |
| AMD | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| AMD | L-ema21 | ladder row ema21: price and gap = price vs average | $524.07, 1.2% | $524.07, 1.2% | PASS |  |  |
| AMD | L-note | "Last close $X · date" note = last completed bar | Last close $530.14 · Nov 18 | $530.14 · Nov 18 | PASS |  |  |
| AMD | L-now | ladder price row = compared price; name = the basis label | $530.14 "After hours" | $530.14 "after hours" | PASS |  |  |
| AMD | L-sma200 | ladder row sma200: price and gap = price vs average | $427.18, 24.1% | $427.18, 24.1% | PASS |  |  |
| AMD | L-sma50 | ladder row sma50: price and gap = price vs average | $555.22, -4.5% | $555.22, -4.5% | PASS |  |  |
| AMD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $530.14 / entry $530.14 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.3 | 50.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +130.2% vs +11.8% | 130.2% vs 11.8% | PASS |  |  |
| AMD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.6 | 17.6 | PASS |  | Wilder, completed bars |
| AMD | T4w | words "20 or more / below 20" | below 20 | ADX 17.6 | PASS |  |  |
| AMD | T5 | "counted at the last close ($X, date)" = last completed bar | $530.14, Nov 18 | $530.14, Nov 18 | PASS |  |  |
| AMD | T6 | price vs 200-day average (S1 pattern sma values) | $530.14 vs $427.18 · +24.1% | $530.14 vs $427.18 · 24.1% | PASS |  |  |
| AMD | T6w | word "Above" | Above | Above | PASS |  |  |
| AMD | T7 | price vs 50-day average (S1 pattern sma values) | $530.14 vs $555.22 · -4.5% | $530.14 vs $555.22 · -4.5% | PASS |  |  |
| AMD | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +12.0% over 30 td | +12.0% over 30 td | PASS |  |  |
| AMD | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 19.5% below $658.52 | 19.5% below $658.52 | PASS |  | closing high would be 649.42 |
| AMD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 19.5% below | PASS |  |  |
| AMD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $658.52 | $658.52002 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 5.31%, close location 0.95, OBV rising |
| AMD | V2 | day change of the last completed bar | up 5.3% | +5.31% | PASS |  |  |
| AMD | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.95 (raw 0.9451) | PASS |  |  |
| AMD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AMD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.21× / 0.70× | 1.21× / 0.70× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 33451755) | 20 bars, last ('2026-11-18', 33451755) | PASS |  |  |
| AMZN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $267.74 | $267.74 | PASS |  |  |
| AMZN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $259.74 | $259.74 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZN | E3 | percent from the 21-day average | 3.1% above | 3.1% above | PASS |  |  |
| AMZN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMZN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.02 | $9.02 (sr=9.0203) | PASS |  | Wilder ATR14 |
| AMZN | E5 | distance in normal day-moves | 0.9 | 0.9 | PASS |  | gauge dot note uses the same number:  · 0.9 day-moves above |
| AMZN | L-ema21 | ladder row ema21: price and gap = price vs average | $259.74, 3.1% | $259.74, 3.1% | PASS |  |  |
| AMZN | L-note | "Last close $X · date" note = last completed bar | Last close $267.74 · Nov 18 | $267.74 · Nov 18 | PASS |  |  |
| AMZN | L-now | ladder price row = compared price; name = the basis label | $267.74 "After hours" | $267.74 "after hours" | PASS |  |  |
| AMZN | L-sma200 | ladder row sma200: price and gap = price vs average | $244.91, 9.3% | $244.91, 9.3% | PASS |  |  |
| AMZN | L-sma50 | ladder row sma50: price and gap = price vs average | $255.12, 4.9% | $255.12, 4.9% | PASS |  |  |
| AMZN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $267.74 / entry $267.74 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 57.2 | 57.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +20.3% vs +11.8% | 20.3% vs 11.8% | PASS |  |  |
| AMZN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZN | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.4 | 11.4 | PASS |  | Wilder, completed bars |
| AMZN | T4w | words "20 or more / below 20" | below 20 | ADX 11.4 | PASS |  |  |
| AMZN | T5 | "counted at the last close ($X, date)" = last completed bar | $267.74, Nov 18 | $267.74, Nov 18 | PASS |  |  |
| AMZN | T6 | price vs 200-day average (S1 pattern sma values) | $267.74 vs $244.91 · +9.3% | $267.74 vs $244.91 · 9.3% | PASS |  |  |
| AMZN | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T7 | price vs 50-day average (S1 pattern sma values) | $267.74 vs $255.12 · +4.9% | $267.74 vs $255.12 · 4.9% | PASS |  |  |
| AMZN | T7w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| AMZN | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMZN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.8% below $287.20 | 6.8% below $287.20 | PASS |  | closing high would be 284.02 |
| AMZN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.8% below | PASS |  |  |
| AMZN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $287.20 | $287.20001 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 3.82%, close location 0.94, OBV rising |
| AMZN | V2 | day change of the last completed bar | up 3.8% | +3.82% | PASS |  |  |
| AMZN | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.94 (raw 0.9365) | PASS |  |  |
| AMZN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AMZN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.98× / 1.13× | 0.98× / 1.13× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 40845576) | 20 bars, last ('2026-11-18', 40845576) | PASS |  |  |
| AMZU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.20 | $39.20 | PASS |  |  |
| AMZU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $36.12 | $36.12 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZU | E3 | percent from the 21-day average | 8.5% above | 8.5% above | PASS |  |  |
| AMZU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMZU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.47 | $2.47 (sr=2.4747) | PASS |  | Wilder ATR14 |
| AMZU | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves above |
| AMZU | L-ema21 | ladder row ema21: price and gap = price vs average | $36.12, 8.5% | $36.12, 8.5% | PASS |  |  |
| AMZU | L-note | "Last close $X · date" note = last completed bar | Last close $37.91 · Nov 18 | $37.91 · Nov 18 | PASS |  |  |
| AMZU | L-now | ladder price row = compared price; name = the basis label | $39.2 "After hours" | $39.20 "after hours" | PASS |  |  |
| AMZU | L-sma200 | ladder row sma200: price and gap = price vs average | $34.93, 12.2% | $34.93, 12.2% | PASS |  |  |
| AMZU | L-sma50 | ladder row sma50: price and gap = price vs average | $35.32, 11.0% | $35.31, 11.0% | PASS |  |  |
| AMZU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $39.20 / entry $39.20 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.7 | 55.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +16.6% vs +11.8% | 16.6% vs 11.8% | PASS |  |  |
| AMZU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZU | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.3 | 11.3 | PASS |  | Wilder, completed bars |
| AMZU | T4w | words "20 or more / below 20" | below 20 | ADX 11.3 | PASS |  |  |
| AMZU | T5 | "counted at the last close ($X, date)" = last completed bar | $37.91, Nov 18 | $37.91, Nov 18 | PASS |  |  |
| AMZU | T6 | price vs 200-day average (S1 pattern sma values) | $37.91 vs $34.93 · +8.5% | $37.91 vs $34.93 · 8.5% | PASS |  |  |
| AMZU | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZU | T7 | price vs 50-day average (S1 pattern sma values) | $37.91 vs $35.31 · +7.4% | $37.91 vs $35.31 · 7.3% | PASS |  |  |
| AMZU | T7w | word "Above" | Above | Above | PASS |  |  |
| AMZU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.2% over 30 td | -0.2% over 30 td | PASS |  |  |
| AMZU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AMZU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 18.7% below $46.64 | 18.7% below $46.64 | PASS |  | closing high would be 45.45 |
| AMZU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 18.7% below | PASS |  |  |
| AMZU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.64 | $46.64482080439608 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 7.55%, close location 0.92, OBV falling |
| AMZU | V2 | day change of the last completed bar | up 7.5% | +7.55% | PASS |  |  |
| AMZU | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.92 (raw 0.9188) | PASS |  |  |
| AMZU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.68× / 1.16× | 0.68× / 1.16× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1294100) | 20 bars, last ('2026-11-18', 1294100) | PASS |  |  |
| ANET.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $34.66 | $34.66 | PASS |  |  |
| ANET.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $33.41 | $33.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ANET.TO | E3 | percent from the 21-day average | 3.7% above | 3.7% above | PASS |  |  |
| ANET.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ANET.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.99 | $1.99 (sr=1.9932) | PASS |  | Wilder ATR14 |
| ANET.TO | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves above |
| ANET.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $33.41, 3.7% | $33.41, 3.7% | PASS |  |  |
| ANET.TO | L-now | ladder price row = compared price; name = the basis label | $34.66 "Last close" | $34.66 "last close" | PASS |  |  |
| ANET.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $30.18, 14.8% | $30.18, 14.8% | PASS |  |  |
| ANET.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $34.41, 0.7% | $34.41, 0.7% | PASS |  |  |
| ANET.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.4 | 53.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ANET.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +45.4% vs +11.8% | 45.4% vs 11.8% | PASS |  |  |
| ANET.TO | T3w | words "past year" vs the window used | 227 / 251 bars back | 250-253 bars | PASS |  |  |
| ANET.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.5 | 17.5 | PASS |  | Wilder, completed bars |
| ANET.TO | T4w | words "20 or more / below 20" | below 20 | ADX 17.5 | PASS |  |  |
| ANET.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 4.02%, close location 0.97, OBV rising |
| ANET.TO | V2 | day change of the last completed bar | up 4.0% | +4.02% | PASS |  |  |
| ANET.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.97 (raw 0.9706) | PASS |  |  |
| ANET.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ANET.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.07× / 0.70× | 1.07× / 0.70× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ANET.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 50464) | 20 bars, last ('2026-11-18', 50464) | PASS |  |  |
| ASML.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $41.25 | $41.25 | PASS |  |  |
| ASML.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $44.26 | $44.26 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASML.TO | E3 | percent from the 21-day average | 6.8% below | 6.8% below | PASS |  |  |
| ASML.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ASML.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.91 | $1.91 (sr=1.9083) | PASS |  | Wilder ATR14 |
| ASML.TO | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| ASML.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $44.26, -6.8% | $44.26, -6.8% | PASS |  |  |
| ASML.TO | L-now | ladder price row = compared price; name = the basis label | $41.25 "Last close" | $41.25 "last close" | PASS |  |  |
| ASML.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $45.08, -8.5% | $45.08, -8.5% | PASS |  |  |
| ASML.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $47.19, -12.6% | $47.19, -12.6% | PASS |  |  |
| ASML.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ASML.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.9 | 38.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASML.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +47.6% vs +11.8% | 47.6% vs 11.8% | PASS |  |  |
| ASML.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ASML.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.0 | 27.0 | PASS |  | Wilder, completed bars |
| ASML.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.0 | PASS |  |  |
| ASML.TO | T6 | price vs 200-day average (S1 pattern sma values) | $41.25 vs $45.08 · -8.5% | $41.25 vs $45.08 · -8.5% | PASS |  |  |
| ASML.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| ASML.TO | T7 | price vs 50-day average (S1 pattern sma values) | $41.25 vs $47.19 · -12.6% | $41.25 vs $47.19 · -12.6% | PASS |  |  |
| ASML.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| ASML.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.9% over 30 td | +3.9% over 30 td | PASS |  |  |
| ASML.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ASML.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ASML.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 27.3% below $56.75 | 27.3% below $56.75 | PASS |  | closing high would be 56.67 |
| ASML.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 27.3% below | PASS |  |  |
| ASML.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $56.75 | $56.745395859548175 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ASML.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 1.10%, close location 0.84, OBV falling |
| ASML.TO | V2 | day change of the last completed bar | up 1.1% | +1.10% | PASS |  |  |
| ASML.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.84 (raw 0.8411) | PASS |  |  |
| ASML.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ASML.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 0.24× | 0.88× / 0.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASML.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 39767) | 20 bars, last ('2026-11-18', 39767) | PASS |  |  |
| ASTL.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $6.94 | $6.94 | PASS |  |  |
| ASTL.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $7.24 | $7.24 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASTL.TO | E3 | percent from the 21-day average | 4.1% below | 4.1% below | PASS |  |  |
| ASTL.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ASTL.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.42 | $0.42 (sr=0.4239) | PASS |  | Wilder ATR14 |
| ASTL.TO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| ASTL.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $7.24, -4.1% | $7.24, -4.1% | PASS |  |  |
| ASTL.TO | L-note | "Last close $X · date" note = last completed bar | Last close $6.94 · Nov 18 | $6.94 · Nov 18 | PASS |  |  |
| ASTL.TO | L-now | ladder price row = compared price; name = the basis label | $6.94 "After hours" | $6.94 "after hours" | PASS |  |  |
| ASTL.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $6.26, 10.8% | $6.26, 10.8% | PASS |  |  |
| ASTL.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $6.52, 6.4% | $6.52, 6.4% | PASS |  |  |
| ASTL.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $6.94 / entry $6.94 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ASTL.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ASTL.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 47.4 | 47.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASTL.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.6% vs +11.8% | 39.6% vs 11.8% | PASS |  |  |
| ASTL.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ASTL.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.2 | PASS |  |  |
| ASTL.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $6.94, Nov 18 | $6.94, Nov 18 | PASS |  |  |
| ASTL.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| ASTL.TO | T7 | price vs 50-day average (S1 pattern sma values) | $6.94 vs $6.52 · +6.4% | $6.94 vs $6.52 · 6.4% | PASS |  |  |
| ASTL.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| ASTL.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.3% over 30 td | PASS |  |  |
| ASTL.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ASTL.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ASTL.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 16.5% below $8.31 | 16.5% below $8.31 | PASS |  | closing high would be 8.22 |
| ASTL.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 16.5% below | PASS |  |  |
| ASTL.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $8.31 | $8.3100004196167 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ASTL.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.28%, close location 0.10, OBV falling |
| ASTL.TO | V2 | day change of the last completed bar | down 4.3% | -4.28% | PASS |  |  |
| ASTL.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1026) | PASS |  |  |
| ASTL.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ASTL.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.72× / 0.70× | 0.72× / 0.70× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASTL.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 430637) | 20 bars, last ('2026-11-18', 430637) | PASS |  |  |
| ATD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $83.00 | $83.00 | PASS |  |  |
| ATD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $82.53 | $82.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ATD.TO | E3 | percent from the 21-day average | 0.6% above | 0.6% above | PASS |  |  |
| ATD.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ATD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.67 | $1.67 (sr=1.6673) | PASS |  | Wilder ATR14 |
| ATD.TO | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| ATD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $82.53, 0.6% | $82.53, 0.6% | PASS |  |  |
| ATD.TO | L-note | "Last close $X · date" note = last completed bar | Last close $83.00 · Nov 18 | $83.00 · Nov 18 | PASS |  |  |
| ATD.TO | L-now | ladder price row = compared price; name = the basis label | $83 "After hours" | $83.00 "after hours" | PASS |  |  |
| ATD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $82.43, 0.7% | $82.43, 0.7% | PASS |  |  |
| ATD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $80.81, 2.7% | $80.81, 2.7% | PASS |  |  |
| ATD.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $83.00 / entry $83.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ATD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ATD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.1 | 53.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ATD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +20.7% vs +11.8% | 20.7% vs 11.8% | PASS |  |  |
| ATD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ATD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.7 | 15.7 | PASS |  | Wilder, completed bars |
| ATD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.7 | PASS |  |  |
| ATD.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $83.00, Nov 18 | $83.00, Nov 18 | PASS |  |  |
| ATD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $83.00 vs $82.43 · +0.7% | $83.00 vs $82.43 · 0.7% | PASS |  |  |
| ATD.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| ATD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $83.00 vs $80.81 · +2.7% | $83.00 vs $80.81 · 2.7% | PASS |  |  |
| ATD.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| ATD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.5% over 30 td | PASS |  |  |
| ATD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ATD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ATD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.3% below $94.68 | 12.3% below $94.68 | PASS |  | closing high would be 93.29 |
| ATD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.3% below | PASS |  |  |
| ATD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $94.68 | $94.67525459795411 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ATD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.78%, close location 0.24, OBV falling |
| ATD.TO | V2 | day change of the last completed bar | down 0.8% | -0.78% | PASS |  |  |
| ATD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.24 (raw 0.2357) | PASS |  |  |
| ATD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ATD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.29× / 0.39× | 1.29× / 0.39× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ATD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1699898) | 20 bars, last ('2026-11-18', 1699898) | PASS |  |  |
| AVGC | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $19.68 | $19.68 | PASS |  |  |
| AVGC | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.38 | $18.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGC | E3 | percent from the 21-day average | 7.1% above | 7.1% above | PASS |  |  |
| AVGC | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AVGC | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.67 | $1.67 (sr=1.6663) | PASS |  | Wilder ATR14 |
| AVGC | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves above |
| AVGC | L-ema21 | ladder row ema21: price and gap = price vs average | $18.38, 7.1% | $18.38, 7.1% | PASS |  |  |
| AVGC | L-now | ladder price row = compared price; name = the basis label | $19.68 "Last close" | $19.68 "last close" | PASS |  |  |
| AVGC | L-sma50 | ladder row sma50: price and gap = price vs average | $19.64, 0.2% | $19.64, 0.2% | PASS |  |  |
| AVGC | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.3 | 53.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGC | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 8.13%, close location 0.67, OBV rising |
| AVGC | V2 | day change of the last completed bar | up 8.1% | +8.13% | PASS |  |  |
| AVGC | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGC | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.55× / 0.96× | 1.55× / 0.96× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGC | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 4800) | 20 bars, last ('2026-11-18', 4800) | PASS |  |  |
| AVGO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.4 | 51.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.4% vs +11.8% | 0.4% vs 11.8% | PASS |  |  |
| AVGO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AVGO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.94 | $12.94 | PASS |  |  |
| AVGO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $12.73 | $12.73 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGO.TO | E3 | percent from the 21-day average | 1.6% above | 1.6% above | PASS |  |  |
| AVGO.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AVGO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.65 | $0.65 (sr=0.6504) | PASS |  | Wilder ATR14 |
| AVGO.TO | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| AVGO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $12.73, 1.6% | $12.73, 1.6% | PASS |  |  |
| AVGO.TO | L-now | ladder price row = compared price; name = the basis label | $12.94 "Last close" | $12.94 "last close" | PASS |  |  |
| AVGO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $14.02, -7.7% | $14.02, -7.7% | PASS |  |  |
| AVGO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $13.09, -1.1% | $13.09, -1.1% | PASS |  |  |
| AVGO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.3 | 51.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.8% vs +11.8% | -1.8% vs 11.8% | PASS |  |  |
| AVGO.TO | T3w | words "past year" vs the window used | 226 / 251 bars back | 250-253 bars | PASS |  |  |
| AVGO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.0 | 21.0 | PASS |  | Wilder, completed bars |
| AVGO.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 21.0 | PASS |  |  |
| AVGO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 2.37%, close location 1.00, OBV rising |
| AVGO.TO | V2 | day change of the last completed bar | up 2.4% | +2.37% | PASS |  |  |
| AVGO.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 1.00 (raw 1.0000) | PASS |  |  |
| AVGO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGO.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.9× from 2026-11-17 | 0.87× from 2026-11-17 | PASS |  | window "50 bars" includes the bar itself |
| AVGO.TO | V6 | Volume detail: last session date and RVOL | 2026-11-17 0.87× | 2026-11-17 0.87× | PASS |  |  |
| AVGO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.87× / 0.47× | 0.87× / 0.47× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-17', 993758) | 20 bars, last ('2026-11-17', 993758) | PASS |  |  |
| BDT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $73.05 | $73.05 | PASS |  |  |
| BDT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.9 | $73.90 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BDT.TO | E3 | percent from the 21-day average | 1.1% below | 1.1% below | PASS |  |  |
| BDT.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BDT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.06 | $4.06 (sr=4.0612) | PASS |  | Wilder ATR14 |
| BDT.TO | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| BDT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $73.9, -1.1% | $73.90, -1.1% | PASS |  |  |
| BDT.TO | L-note | "Last close $X · date" note = last completed bar | Last close $73.05 · Nov 18 | $73.05 · Nov 18 | PASS |  |  |
| BDT.TO | L-now | ladder price row = compared price; name = the basis label | $73.05 "After hours" | $73.05 "after hours" | PASS |  |  |
| BDT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.78, 24.3% | $58.78, 24.3% | PASS |  |  |
| BDT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $76.14, -4.1% | $76.14, -4.1% | PASS |  |  |
| BDT.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $73.05 / entry $73.05 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BDT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BDT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.1 | 48.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BDT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +196.8% vs +11.8% | 196.8% vs 11.8% | PASS |  |  |
| BDT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BDT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.0 | 14.1 | PASS |  | Wilder, completed bars |
| BDT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 14.1 | PASS |  |  |
| BDT.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $73.05, Nov 18 | $73.05, Nov 18 | PASS |  |  |
| BDT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $73.05 vs $58.78 · +24.3% | $73.05 vs $58.78 · 24.3% | PASS |  |  |
| BDT.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| BDT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $73.05 vs $76.14 · -4.1% | $73.05 vs $76.14 · -4.1% | PASS |  |  |
| BDT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| BDT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +13.1% over 30 td | +13.1% over 30 td | PASS |  |  |
| BDT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| BDT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BDT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 15.5% below $86.42 | 15.5% below $86.42 | PASS |  | closing high would be 85.33 |
| BDT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 15.5% below | PASS |  |  |
| BDT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $86.42 | $86.42048390957993 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BDT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 2.70%, close location 0.77, OBV falling |
| BDT.TO | V2 | day change of the last completed bar | up 2.7% | +2.70% | PASS |  |  |
| BDT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.77 (raw 0.7740) | PASS |  |  |
| BDT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BDT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.01× / 0.49× | 1.01× / 0.49× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BDT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 416995) | 20 bars, last ('2026-11-18', 416995) | PASS |  |  |
| BOTZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $29.77 | $29.77 | PASS |  |  |
| BOTZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $31.86 | $31.86 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BOTZ | E3 | percent from the 21-day average | 6.6% below | 6.6% below | PASS |  |  |
| BOTZ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BOTZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.77 | $0.77 (sr=0.7692) | PASS |  | Wilder ATR14 |
| BOTZ | E5 | distance in normal day-moves | 2.7 | 2.7 | PASS |  | gauge dot note uses the same number:  · 2.7 day-moves below |
| BOTZ | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.6 | +5.6 | PASS |  |  |
| BOTZ | L-ema21 | ladder row ema21: price and gap = price vs average | $31.86, -6.6% | $31.86, -6.6% | PASS |  |  |
| BOTZ | L-note | "Last close $X · date" note = last completed bar | Last close $29.71 · Nov 18 | $29.71 · Nov 18 | PASS |  |  |
| BOTZ | L-now | ladder price row = compared price; name = the basis label | $29.77 "After hours" | $29.77 "after hours" | PASS |  |  |
| BOTZ | L-sma200 | ladder row sma200: price and gap = price vs average | $36.16, -17.7% | $36.16, -17.7% | PASS |  |  |
| BOTZ | L-sma50 | ladder row sma50: price and gap = price vs average | $33.75, -11.8% | $33.75, -11.8% | PASS |  |  |
| BOTZ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $29.77 / entry $29.77 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BOTZ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BOTZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.4 | 31.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BOTZ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -11.4% vs +11.8% | -11.4% vs 11.8% | PASS |  |  |
| BOTZ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BOTZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.4 | 34.4 | PASS |  | Wilder, completed bars |
| BOTZ | T4w | words "20 or more / below 20" | 20 or more | ADX 34.4 | PASS |  |  |
| BOTZ | T5 | "counted at the last close ($X, date)" = last completed bar | $29.71, Nov 18 | $29.71, Nov 18 | PASS |  |  |
| BOTZ | T6 | price vs 200-day average (S1 pattern sma values) | $29.71 vs $36.16 · -17.8% | $29.71 vs $36.16 · -17.8% | PASS |  |  |
| BOTZ | T6w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T7 | price vs 50-day average (S1 pattern sma values) | $29.71 vs $33.75 · -12.0% | $29.71 vs $33.75 · -12.0% | PASS |  |  |
| BOTZ | T7w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.9% over 30 td | -1.9% over 30 td | PASS |  |  |
| BOTZ | T8r | word "rising" | not rising | not rising | PASS |  |  |
| BOTZ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BOTZ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 28.7% below $41.69 | 28.7% below $41.69 | PASS |  | closing high would be 41.61 |
| BOTZ | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 28.7% below | PASS |  |  |
| BOTZ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $41.69 | $41.689149923077814 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BOTZ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.20 (raw 0.2000) | PASS |  |  |
| BOTZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BOTZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 707900) | 20 bars, last ('2026-11-18', 707900) | PASS |  |  |
| BRK-B | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $574.03 | $574.03 | PASS |  |  |
| BRK-B | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $566.64 | $566.64 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRK-B | E3 | percent from the 21-day average | 1.3% above | 1.3% above | PASS |  |  |
| BRK-B | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BRK-B | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.64 | $9.64 (sr=9.6387) | PASS |  | Wilder ATR14 |
| BRK-B | E5 | distance in normal day-moves | 0.8 | 0.8 | PASS |  | gauge dot note uses the same number:  · 0.8 day-moves above |
| BRK-B | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -6.7 | -6.7 | PASS |  |  |
| BRK-B | L-ema21 | ladder row ema21: price and gap = price vs average | $566.64, 1.3% | $566.64, 1.3% | PASS |  |  |
| BRK-B | L-note | "Last close $X · date" note = last completed bar | Last close $574.62 · Nov 18 | $574.62 · Nov 18 | PASS |  |  |
| BRK-B | L-now | ladder price row = compared price; name = the basis label | $574.03 "After hours" | $574.03 "after hours" | PASS |  |  |
| BRK-B | L-sma200 | ladder row sma200: price and gap = price vs average | $501.9, 14.4% | $501.90, 14.4% | PASS |  |  |
| BRK-B | L-sma50 | ladder row sma50: price and gap = price vs average | $534.37, 7.4% | $534.37, 7.4% | PASS |  |  |
| BRK-B | S5-price | S5: the same live price reads the same on the header and the Entry block | header $574.03 / entry $574.03 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRK-B | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRK-B | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 60.7 | 60.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRK-B | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +13.9% vs +11.8% | 13.9% vs 11.8% | PASS |  |  |
| BRK-B | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRK-B | T4 | ADX 14 (S1 /api/sr meta.adx) | 52.1 | 52.1 | PASS |  | Wilder, completed bars |
| BRK-B | T4w | words "20 or more / below 20" | 20 or more | ADX 52.1 | PASS |  |  |
| BRK-B | T5 | "counted at the last close ($X, date)" = last completed bar | $574.62, Nov 18 | $574.62, Nov 18 | PASS |  |  |
| BRK-B | T6 | price vs 200-day average (S1 pattern sma values) | $574.62 vs $501.90 · +14.5% | $574.62 vs $501.90 · 14.5% | PASS |  |  |
| BRK-B | T6w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T7 | price vs 50-day average (S1 pattern sma values) | $574.62 vs $534.37 · +7.5% | $574.62 vs $534.37 · 7.5% | PASS |  |  |
| BRK-B | T7w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| BRK-B | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRK-B | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRK-B | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.7% below $596.92 | 3.7% below $596.92 | PASS |  | closing high would be 592.94 |
| BRK-B | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.7% below | PASS |  |  |
| BRK-B | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $596.92 | $596.9199829101562 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRK-B | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.07%, close location 0.14, OBV rising |
| BRK-B | V2 | day change of the last completed bar | down 2.1% | -2.07% | PASS |  |  |
| BRK-B | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1439) | PASS |  |  |
| BRK-B | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| BRK-B | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.11× / 1.23× | 1.11× / 1.23× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRK-B | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 5406581) | 20 bars, last ('2026-11-18', 5406581) | PASS |  |  |
| BRKU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $28.75 | $28.75 | PASS |  |  |
| BRKU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.28 | $28.28 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRKU | E3 | percent from the 21-day average | 1.7% above | 1.7% above | PASS |  |  |
| BRKU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BRKU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.92 | $0.92 (sr=0.9182) | PASS |  | Wilder ATR14 |
| BRKU | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| BRKU | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.7 | -5.7 | PASS |  |  |
| BRKU | L-ema21 | ladder row ema21: price and gap = price vs average | $28.28, 1.7% | $28.28, 1.7% | PASS |  |  |
| BRKU | L-note | "Last close $X · date" note = last completed bar | Last close $28.85 · Nov 18 | $28.85 · Nov 18 | PASS |  |  |
| BRKU | L-now | ladder price row = compared price; name = the basis label | $28.75 "After hours" | $28.75 "after hours" | PASS |  |  |
| BRKU | L-sma200 | ladder row sma200: price and gap = price vs average | $23.06, 24.7% | $23.06, 24.7% | PASS |  |  |
| BRKU | L-sma50 | ladder row sma50: price and gap = price vs average | $25.35, 13.4% | $25.35, 13.4% | PASS |  |  |
| BRKU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $28.75 / entry $28.75 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRKU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRKU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 58.7 | 58.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRKU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +15.5% vs +11.8% | 15.5% vs 11.8% | PASS |  |  |
| BRKU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRKU | T4 | ADX 14 (S1 /api/sr meta.adx) | 51.0 | 51.0 | PASS |  | Wilder, completed bars |
| BRKU | T4w | words "20 or more / below 20" | 20 or more | ADX 51.0 | PASS |  |  |
| BRKU | T5 | "counted at the last close ($X, date)" = last completed bar | $28.85, Nov 18 | $28.85, Nov 18 | PASS |  |  |
| BRKU | T6 | price vs 200-day average (S1 pattern sma values) | $28.85 vs $23.06 · +25.1% | $28.85 vs $23.06 · 25.1% | PASS |  |  |
| BRKU | T6w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T7 | price vs 50-day average (S1 pattern sma values) | $28.85 vs $25.35 · +13.8% | $28.85 vs $25.35 · 13.8% | PASS |  |  |
| BRKU | T7w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.4% over 30 td | +2.4% over 30 td | PASS |  |  |
| BRKU | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRKU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRKU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 7.5% below $31.20 | 7.5% below $31.20 | PASS |  | closing high would be 30.81 |
| BRKU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.5% below | PASS |  |  |
| BRKU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $31.20 | $31.200000762939453 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRKU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -4.44%, close location 0.14, OBV rising |
| BRKU | V2 | day change of the last completed bar | down 4.4% | -4.44% | PASS |  |  |
| BRKU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1359) | PASS |  |  |
| BRKU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| BRKU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 1.40× | 0.99× / 1.39× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRKU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 91500) | 20 bars, last ('2026-11-18', 91500) | PASS |  |  |
| CAMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $98.42 | $98.42 | PASS |  |  |
| CAMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $109.89 | $109.89 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAMT | E3 | percent from the 21-day average | 10.4% below | 10.4% below | PASS |  |  |
| CAMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CAMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.03 | $8.03 (sr=8.0305) | PASS |  | Wilder ATR14 |
| CAMT | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| CAMT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.6 | +5.6 | PASS |  |  |
| CAMT | L-ema21 | ladder row ema21: price and gap = price vs average | $109.89, -10.4% | $109.89, -10.4% | PASS |  |  |
| CAMT | L-note | "Last close $X · date" note = last completed bar | Last close $98.42 · Nov 18 | $98.42 · Nov 18 | PASS |  |  |
| CAMT | L-now | ladder price row = compared price; name = the basis label | $98.42 "After hours" | $98.42 "after hours" | PASS |  |  |
| CAMT | L-sma200 | ladder row sma200: price and gap = price vs average | $154.64, -36.4% | $154.64, -36.4% | PASS |  |  |
| CAMT | L-sma50 | ladder row sma50: price and gap = price vs average | $130.71, -24.7% | $130.71, -24.7% | PASS |  |  |
| CAMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $98.42 / entry $98.42 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.8 | 37.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.9% vs +11.8% | 3.9% vs 11.8% | PASS |  |  |
| CAMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.3 | 34.4 | PASS |  | Wilder, completed bars |
| CAMT | T4w | words "20 or more / below 20" | 20 or more | ADX 34.4 | PASS |  |  |
| CAMT | T5 | "counted at the last close ($X, date)" = last completed bar | $98.42, Nov 18 | $98.42, Nov 18 | PASS |  |  |
| CAMT | T6 | price vs 200-day average (S1 pattern sma values) | $98.42 vs $154.64 · -36.4% | $98.42 vs $154.64 · -36.4% | PASS |  |  |
| CAMT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T7 | price vs 50-day average (S1 pattern sma values) | $98.42 vs $130.71 · -24.7% | $98.42 vs $130.71 · -24.7% | PASS |  |  |
| CAMT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.2% over 30 td | -1.2% over 30 td | PASS |  |  |
| CAMT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CAMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 54.4% below $215.99 | 54.4% below $215.99 | PASS |  | closing high would be 207.46 |
| CAMT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 54.4% below | PASS |  |  |
| CAMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $215.99 | $215.99 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 3.64%, close location 0.43, OBV falling |
| CAMT | V2 | day change of the last completed bar | up 3.6% | +3.64% | PASS |  |  |
| CAMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.39× / 0.45× | 1.39× / 0.45× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 718709) | 20 bars, last ('2026-11-18', 718709) | PASS |  |  |
| CARS.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $19.88 | $19.88 | PASS |  |  |
| CARS.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $21.64 | $21.64 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CARS.TO | E3 | percent from the 21-day average | 8.1% below | 8.1% below | PASS |  |  |
| CARS.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| CARS.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.48 | $0.48 (sr=0.4773) | PASS |  | Wilder ATR14 |
| CARS.TO | E5 | distance in normal day-moves | 3.7 | 3.7 | PASS |  | gauge dot note uses the same number:  · 3.7 day-moves below |
| CARS.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.3 | +4.3 | PASS |  |  |
| CARS.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +13.2 | +13.2 | PASS |  |  |
| CARS.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $21.64, -8.1% | $21.64, -8.1% | PASS |  |  |
| CARS.TO | L-now | ladder price row = compared price; name = the basis label | $19.88 "Last close" | $19.88 "last close" | PASS |  |  |
| CARS.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $27.94, -28.8% | $27.94, -28.8% | PASS |  |  |
| CARS.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $23.67, -16.0% | $23.67, -16.0% | PASS |  |  |
| CARS.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CARS.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.0 | 31.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CARS.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -22.4% vs +11.8% | -22.4% vs 11.8% | PASS |  |  |
| CARS.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CARS.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.0 | 29.1 | PASS |  | Wilder, completed bars |
| CARS.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 29.1 | PASS |  |  |
| CARS.TO | T6 | price vs 200-day average (S1 pattern sma values) | $19.88 vs $27.94 · -28.8% | $19.88 vs $27.94 · -28.8% | PASS |  |  |
| CARS.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CARS.TO | T7 | price vs 50-day average (S1 pattern sma values) | $19.88 vs $23.67 · -16.0% | $19.88 vs $23.67 · -16.0% | PASS |  |  |
| CARS.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CARS.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.5% over 30 td | -2.5% over 30 td | PASS |  |  |
| CARS.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CARS.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CARS.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 47.9% below $38.16 | 47.9% below $38.16 | PASS |  | closing high would be 38.16 |
| CARS.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 47.9% below | PASS |  |  |
| CARS.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.16 | $38.15896987915039 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CARS.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 11 of 50 days empty | 11 of 50 days empty | PASS |  |  |
| CCO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $89.40 | $89.40 | PASS |  |  |
| CCO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $104.03 | $104.03 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CCO.TO | E3 | percent from the 21-day average | 14.1% below | 14.1% below | PASS |  |  |
| CCO.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CCO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.92 | $4.92 (sr=4.9224) | PASS |  | Wilder ATR14 |
| CCO.TO | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| CCO.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.4 | +7.4 | PASS |  |  |
| CCO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $104.03, -14.1% | $104.03, -14.1% | PASS |  |  |
| CCO.TO | L-note | "Last close $X · date" note = last completed bar | Last close $89.40 · Nov 18 | $89.40 · Nov 18 | PASS |  |  |
| CCO.TO | L-now | ladder price row = compared price; name = the basis label | $89.4 "After hours" | $89.40 "after hours" | PASS |  |  |
| CCO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $140.51, -36.4% | $140.51, -36.4% | PASS |  |  |
| CCO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $116.73, -23.4% | $116.73, -23.4% | PASS |  |  |
| CCO.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $89.40 / entry $89.40 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CCO.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CCO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.3 | 29.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CCO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -23.1% vs +11.8% | -23.1% vs 11.8% | PASS |  |  |
| CCO.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CCO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.6 | 30.6 | PASS |  | Wilder, completed bars |
| CCO.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 30.6 | PASS |  |  |
| CCO.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $89.40, Nov 18 | $89.40, Nov 18 | PASS |  |  |
| CCO.TO | T6 | price vs 200-day average (S1 pattern sma values) | $89.40 vs $140.51 · -36.4% | $89.40 vs $140.51 · -36.4% | PASS |  |  |
| CCO.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CCO.TO | T7 | price vs 50-day average (S1 pattern sma values) | $89.40 vs $116.73 · -23.4% | $89.40 vs $116.73 · -23.4% | PASS |  |  |
| CCO.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CCO.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.2% over 30 td | -4.2% over 30 td | PASS |  |  |
| CCO.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CCO.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CCO.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 51.1% below $182.72 | 51.1% below $182.72 | PASS |  | closing high would be 181.66 |
| CCO.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 51.1% below | PASS |  |  |
| CCO.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $182.72 | $182.72000122070312 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CCO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.99%, close location 0.05, OBV falling |
| CCO.TO | V2 | day change of the last completed bar | down 3.0% | -2.99% | PASS |  |  |
| CCO.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0519) | PASS |  |  |
| CCO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CCO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.54× / 0.54× | 1.54× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CCO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1938996) | 20 bars, last ('2026-11-18', 1938996) | PASS |  |  |
| CCO.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.54, OBV falling | condition true | PASS |  |  |
| CGY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $84.14 | $84.14 | PASS |  |  |
| CGY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $85.2 | $85.20 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CGY.TO | E3 | percent from the 21-day average | 1.2% below | 1.2% below | PASS |  |  |
| CGY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CGY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.51 | $2.51 (sr=2.5117) | PASS |  | Wilder ATR14 |
| CGY.TO | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| CGY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $85.2, -1.2% | $85.20, -1.2% | PASS |  |  |
| CGY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $84.14 · Nov 18 | $84.14 · Nov 18 | PASS |  |  |
| CGY.TO | L-now | ladder price row = compared price; name = the basis label | $84.14 "After hours" | $84.14 "after hours" | PASS |  |  |
| CGY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $78.92, 6.6% | $78.92, 6.6% | PASS |  |  |
| CGY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $83.49, 0.8% | $83.49, 0.8% | PASS |  |  |
| CGY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $84.14 / entry $84.14 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CGY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CGY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.0 | 48.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CGY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +71.2% vs +11.8% | 71.2% vs 11.8% | PASS |  |  |
| CGY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CGY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.0 | 15.0 | PASS |  | Wilder, completed bars |
| CGY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.0 | PASS |  |  |
| CGY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $84.14, Nov 18 | $84.14, Nov 18 | PASS |  |  |
| CGY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $84.14 vs $78.92 · +6.6% | $84.14 vs $78.92 · 6.6% | PASS |  |  |
| CGY.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CGY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $84.14 vs $83.49 · +0.8% | $84.14 vs $83.49 · 0.8% | PASS |  |  |
| CGY.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CGY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.0% over 30 td | +5.0% over 30 td | PASS |  |  |
| CGY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CGY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CGY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.6% below $95.15 | 11.6% below $95.15 | PASS |  | closing high would be 91.80 |
| CGY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.6% below | PASS |  |  |
| CGY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $95.15 | $95.15474299571112 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CGY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.19%, close location 0.47, OBV falling |
| CGY.TO | V2 | day change of the last completed bar | down 0.2% | -0.19% | PASS |  |  |
| CGY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CGY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.72× / 0.06× | 0.72× / 0.06× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CGY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 21827) | 20 bars, last ('2026-11-18', 21827) | PASS |  |  |
| CNQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $65.26 | $65.26 | PASS |  |  |
| CNQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $70.64 | $70.64 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNQ.TO | E3 | percent from the 21-day average | 7.6% below | 7.6% below | PASS |  |  |
| CNQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| CNQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.05 | $2.05 (sr=2.0544) | PASS |  | Wilder ATR14 |
| CNQ.TO | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| CNQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $70.64, -7.6% | $70.64, -7.6% | PASS |  |  |
| CNQ.TO | L-now | ladder price row = compared price; name = the basis label | $65.26 "Last close" | $65.26 "last close" | PASS |  |  |
| CNQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.22, 1.6% | $64.22, 1.6% | PASS |  |  |
| CNQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $71.06, -8.2% | $71.06, -8.2% | PASS |  |  |
| CNQ.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.2 | 32.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +43.0% vs +11.8% | 43.1% vs 11.8% | PASS |  |  |
| CNQ.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.9 | 29.9 | PASS |  | Wilder, completed bars |
| CNQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 29.9 | PASS |  |  |
| CNQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $65.26 vs $64.22 · +1.6% | $65.26 vs $64.22 · 1.6% | PASS |  |  |
| CNQ.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CNQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $65.26 vs $71.06 · -8.2% | $65.26 vs $71.06 · -8.2% | PASS |  |  |
| CNQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CNQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.8% over 30 td | +6.8% over 30 td | PASS |  |  |
| CNQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.0% below $78.60 | 17.0% below $78.60 | PASS |  | closing high would be 78.42 |
| CNQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.0% below | PASS |  |  |
| CNQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $78.60 | $78.5999984741211 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.44%, close location 0.18, OBV falling |
| CNQ.TO | V2 | day change of the last completed bar | down 4.4% | -4.44% | PASS |  |  |
| CNQ.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.18 (raw 0.1791) | PASS |  |  |
| CNQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CNQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.29× / 1.41× | 1.29× / 1.41× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 15790904) | 20 bars, last ('2026-11-18', 15790904) | PASS |  |  |
| CNR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $179.36 | $179.36 | PASS |  |  |
| CNR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $177.62 | $177.62 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNR.TO | E3 | percent from the 21-day average | 1.0% above | 1.0% above | PASS |  |  |
| CNR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CNR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.26 | $3.26 (sr=3.2642) | PASS |  | Wilder ATR14 |
| CNR.TO | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| CNR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $177.62, 1.0% | $177.62, 1.0% | PASS |  |  |
| CNR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $179.36 · Nov 18 | $179.36 · Nov 18 | PASS |  |  |
| CNR.TO | L-now | ladder price row = compared price; name = the basis label | $179.36 "After hours" | $179.36 "after hours" | PASS |  |  |
| CNR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $161.98, 10.7% | $161.98, 10.7% | PASS |  |  |
| CNR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $172.48, 4.0% | $172.48, 4.0% | PASS |  |  |
| CNR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $179.36 / entry $179.36 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CNR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.9 | 55.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.8% vs +11.8% | 39.8% vs 11.8% | PASS |  |  |
| CNR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.1 | 23.1 | PASS |  | Wilder, completed bars |
| CNR.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 23.1 | PASS |  |  |
| CNR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $179.36, Nov 18 | $179.36, Nov 18 | PASS |  |  |
| CNR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $179.36 vs $161.98 · +10.7% | $179.36 vs $161.98 · 10.7% | PASS |  |  |
| CNR.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $179.36 vs $172.48 · +4.0% | $179.36 vs $172.48 · 4.0% | PASS |  |  |
| CNR.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.9% over 30 td | +3.9% over 30 td | PASS |  |  |
| CNR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.7% below $184.26 | 2.7% below $184.26 | PASS |  | closing high would be 182.93 |
| CNR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.7% below | PASS |  |  |
| CNR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $184.26 | $184.25630798377267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -0.65%, close location 0.49, OBV flat |
| CNR.TO | V2 | day change of the last completed bar | down 0.7% | -0.65% | PASS |  |  |
| CNR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| CNR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.98× / 0.36× | 0.98× / 0.36× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1212183) | 20 bars, last ('2026-11-18', 1212183) | PASS |  |  |
| COP | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $134.40 | $134.40 | PASS |  |  |
| COP | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $139.98 | $139.98 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COP | E3 | percent from the 21-day average | 4.0% below | 4.0% below | PASS |  |  |
| COP | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COP | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.08 | $4.08 (sr=4.082) | PASS |  | Wilder ATR14 |
| COP | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| COP | L-ema21 | ladder row ema21: price and gap = price vs average | $139.98, -4.0% | $139.98, -4.0% | PASS |  |  |
| COP | L-note | "Last close $X · date" note = last completed bar | Last close $134.40 · Nov 18 | $134.40 · Nov 18 | PASS |  |  |
| COP | L-now | ladder price row = compared price; name = the basis label | $134.4 "After hours" | $134.40 "after hours" | PASS |  |  |
| COP | L-sma200 | ladder row sma200: price and gap = price vs average | $123.83, 8.5% | $123.83, 8.5% | PASS |  |  |
| COP | L-sma50 | ladder row sma50: price and gap = price vs average | $137.46, -2.2% | $137.46, -2.2% | PASS |  |  |
| COP | S5-price | S5: the same live price reads the same on the header and the Entry block | header $134.40 / entry $134.40 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COP | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COP | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.4 | 41.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COP | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +49.9% vs +11.8% | 49.9% vs 11.8% | PASS |  |  |
| COP | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COP | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.3 | 23.3 | PASS |  | Wilder, completed bars |
| COP | T4w | words "20 or more / below 20" | 20 or more | ADX 23.3 | PASS |  |  |
| COP | T5 | "counted at the last close ($X, date)" = last completed bar | $134.40, Nov 18 | $134.40, Nov 18 | PASS |  |  |
| COP | T6 | price vs 200-day average (S1 pattern sma values) | $134.40 vs $123.83 · +8.5% | $134.40 vs $123.83 · 8.5% | PASS |  |  |
| COP | T6w | word "Above" | Above | Above | PASS |  |  |
| COP | T7 | price vs 50-day average (S1 pattern sma values) | $134.40 vs $137.46 · -2.2% | $134.40 vs $137.46 · -2.2% | PASS |  |  |
| COP | T7w | word "Below" | Below | Below | PASS |  |  |
| COP | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.8% over 30 td | +5.8% over 30 td | PASS |  |  |
| COP | T8r | word "rising" | still rising | rising | PASS |  |  |
| COP | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COP | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.9% below $154.28 | 12.9% below $154.28 | PASS |  | closing high would be 154.03 |
| COP | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.9% below | PASS |  |  |
| COP | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $154.28 | $154.28 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COP | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.64%, close location 0.04, OBV falling |
| COP | V2 | day change of the last completed bar | down 3.6% | -3.64% | PASS |  |  |
| COP | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0439) | PASS |  |  |
| COP | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COP | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.13× / 1.20× | 1.13× / 1.20× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COP | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 7773798) | 20 bars, last ('2026-11-18', 7773798) | PASS |  |  |
| COPP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $43.08 | $43.08 | PASS |  |  |
| COPP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $51.26 | $51.26 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPP.TO | E3 | percent from the 21-day average | 16.0% below | 16.0% below | PASS |  |  |
| COPP.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| COPP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.18 | $2.18 (sr=2.1812) | PASS |  | Wilder ATR14 |
| COPP.TO | E5 | distance in normal day-moves | 3.8 | 3.8 | PASS |  | gauge dot note uses the same number:  · 3.8 day-moves below |
| COPP.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.3 | +3.3 | PASS |  |  |
| COPP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $51.26, -16.0% | $51.26, -16.0% | PASS |  |  |
| COPP.TO | L-now | ladder price row = compared price; name = the basis label | $43.08 "Last close" | $43.08 "last close" | PASS |  |  |
| COPP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.55, -26.4% | $58.55, -26.4% | PASS |  |  |
| COPP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $56.85, -24.2% | $56.85, -24.2% | PASS |  |  |
| COPP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 26.9 | 26.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.3% vs +11.8% | 0.3% vs 11.8% | PASS |  |  |
| COPP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.6 | 31.6 | PASS |  | Wilder, completed bars |
| COPP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 31.6 | PASS |  |  |
| COPP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $43.08 vs $58.55 · -26.4% | $43.08 vs $58.55 · -26.4% | PASS |  |  |
| COPP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $43.08 vs $56.85 · -24.2% | $43.08 vs $56.85 · -24.2% | PASS |  |  |
| COPP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.0% over 30 td | -1.0% over 30 td | PASS |  |  |
| COPP.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 38.9% below $70.54 | 38.9% below $70.54 | PASS |  | closing high would be 68.98 |
| COPP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 38.9% below | PASS |  |  |
| COPP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $70.54 | $70.54000091552734 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.20%, close location 0.24, OBV falling |
| COPP.TO | V2 | day change of the last completed bar | down 7.2% | -7.20% | PASS |  |  |
| COPP.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.24 (raw 0.2422) | PASS |  |  |
| COPP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.57× / 1.42× | 1.57× / 1.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 23163) | 20 bars, last ('2026-11-18', 23163) | PASS |  |  |
| COPP.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.57, OBV falling | condition true | PASS |  |  |
| COPX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $61.19 | $61.19 | PASS |  |  |
| COPX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $72.02 | $72.02 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPX | E3 | percent from the 21-day average | 15.0% below | 15.0% below | PASS |  |  |
| COPX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COPX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.92 | $2.92 (sr=2.9212) | PASS |  | Wilder ATR14 |
| COPX | E5 | distance in normal day-moves | 3.7 | 3.7 | PASS |  | gauge dot note uses the same number:  · 3.7 day-moves below |
| COPX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| COPX | L-ema21 | ladder row ema21: price and gap = price vs average | $72.02, -15.0% | $72.02, -15.0% | PASS |  |  |
| COPX | L-note | "Last close $X · date" note = last completed bar | Last close $61.19 · Nov 18 | $61.19 · Nov 18 | PASS |  |  |
| COPX | L-now | ladder price row = compared price; name = the basis label | $61.19 "After hours" | $61.19 "after hours" | PASS |  |  |
| COPX | L-sma200 | ladder row sma200: price and gap = price vs average | $82.26, -25.6% | $82.26, -25.6% | PASS |  |  |
| COPX | L-sma50 | ladder row sma50: price and gap = price vs average | $79.52, -23.0% | $79.52, -23.0% | PASS |  |  |
| COPX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $61.19 / entry $61.19 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 26.6 | 26.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +7.0% vs +11.8% | 7.0% vs 11.8% | PASS |  |  |
| COPX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPX | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.0 | 26.9 | PASS |  | Wilder, completed bars |
| COPX | T4w | words "20 or more / below 20" | 20 or more | ADX 26.9 | PASS |  |  |
| COPX | T5 | "counted at the last close ($X, date)" = last completed bar | $61.19, Nov 18 | $61.19, Nov 18 | PASS |  |  |
| COPX | T6 | price vs 200-day average (S1 pattern sma values) | $61.19 vs $82.26 · -25.6% | $61.19 vs $82.26 · -25.6% | PASS |  |  |
| COPX | T6w | word "Below" | Below | Below | PASS |  |  |
| COPX | T7 | price vs 50-day average (S1 pattern sma values) | $61.19 vs $79.52 · -23.1% | $61.19 vs $79.52 · -23.0% | PASS |  |  |
| COPX | T7w | word "Below" | Below | Below | PASS |  |  |
| COPX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.8% over 30 td | -0.8% over 30 td | PASS |  |  |
| COPX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 38.6% below $99.65 | 38.6% below $99.65 | PASS |  | closing high would be 96.45 |
| COPX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 38.6% below | PASS |  |  |
| COPX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $99.65 | $99.65136047369408 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -6.31%, close location 0.45, OBV falling |
| COPX | V2 | day change of the last completed bar | down 6.3% | -6.31% | PASS |  |  |
| COPX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.56× / 1.32× | 3.56× / 1.32× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 10450352) | 20 bars, last ('2026-11-18', 10450352) | PASS |  |  |
| COPX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.56, OBV falling | condition true | PASS |  |  |
| COPZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $7.53 | $7.53 | PASS |  |  |
| COPZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $10.76 | $10.76 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPZ | E3 | percent from the 21-day average | 30.0% below | 30.0% below | PASS |  |  |
| COPZ | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| COPZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.83 | $0.83 (sr=0.8283) | PASS |  | Wilder ATR14 |
| COPZ | E5 | distance in normal day-moves | 3.9 | 3.9 | PASS |  | gauge dot note uses the same number:  · 3.9 day-moves below |
| COPZ | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.2 | +3.2 | PASS |  |  |
| COPZ | L-ema21 | ladder row ema21: price and gap = price vs average | $10.76, -30.0% | $10.76, -30.0% | PASS |  |  |
| COPZ | L-now | ladder price row = compared price; name = the basis label | $7.53 "Last close" | $7.53 "last close" | PASS |  |  |
| COPZ | L-sma50 | ladder row sma50: price and gap = price vs average | $13.44, -44.0% | $13.44, -44.0% | PASS |  |  |
| COPZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 26.7 | 26.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.1 | 28.0 | PASS |  | Wilder, completed bars |
| COPZ | T4w | words "20 or more / below 20" | 20 or more | ADX 28.0 | PASS |  |  |
| COPZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -12.34%, close location 0.30, OBV falling |
| COPZ | V2 | day change of the last completed bar | down 12.3% | -12.34% | PASS |  |  |
| COPZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.23× / 1.12× | 2.23× / 1.12× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 28546) | 20 bars, last ('2026-11-18', 28546) | PASS |  |  |
| COPZ | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.23, OBV falling | condition true | PASS |  |  |
| COST | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,096.62 | $1,096.62 | PASS |  |  |
| COST | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1052.73 | $1052.73 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COST | E3 | percent from the 21-day average | 4.2% above | 4.2% above | PASS |  |  |
| COST | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COST | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $18.69 | $18.69 (sr=18.686) | PASS |  | Wilder ATR14 |
| COST | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves above |
| COST | L-ema21 | ladder row ema21: price and gap = price vs average | $1052.73, 4.2% | $1052.73, 4.2% | PASS |  |  |
| COST | L-note | "Last close $X · date" note = last completed bar | Last close $1,096.62 · Nov 18 | $1,096.62 · Nov 18 | PASS |  |  |
| COST | L-now | ladder price row = compared price; name = the basis label | $1096.62 "After hours" | $1096.62 "after hours" | PASS |  |  |
| COST | L-sma200 | ladder row sma200: price and gap = price vs average | $977.85, 12.1% | $977.85, 12.1% | PASS |  |  |
| COST | L-sma50 | ladder row sma50: price and gap = price vs average | $978.95, 12.0% | $978.95, 12.0% | PASS |  |  |
| COST | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,096.62 / entry $1,096.62 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COST | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COST | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 69.1 | 69.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COST | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +22.5% vs +11.8% | 22.5% vs 11.8% | PASS |  |  |
| COST | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COST | T4 | ADX 14 (S1 /api/sr meta.adx) | 53.3 | 53.3 | PASS |  | Wilder, completed bars |
| COST | T4w | words "20 or more / below 20" | 20 or more | ADX 53.3 | PASS |  |  |
| COST | T5 | "counted at the last close ($X, date)" = last completed bar | $1,096.62, Nov 18 | $1096.62, Nov 18 | PASS |  |  |
| COST | T6 | price vs 200-day average (S1 pattern sma values) | $1,096.62 vs $977.85 · +12.1% | $1096.62 vs $977.85 · 12.1% | PASS |  |  |
| COST | T6w | word "Above" | Above | Above | PASS |  |  |
| COST | T7 | price vs 50-day average (S1 pattern sma values) | $1,096.62 vs $978.95 · +12.0% | $1096.62 vs $978.95 · 12.0% | PASS |  |  |
| COST | T7w | word "Above" | Above | Above | PASS |  |  |
| COST | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.6% over 30 td | PASS |  |  |
| COST | T8r | word "rising" | still rising | rising | PASS |  |  |
| COST | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COST | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.4% below $1,123.67 | 2.4% below $1123.67 | PASS |  | closing high would be 1113.74 |
| COST | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.4% below | PASS |  |  |
| COST | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,123.67 | $1123.6699 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COST | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.21%, close location 0.03, OBV rising |
| COST | V2 | day change of the last completed bar | down 1.2% | -1.21% | PASS |  |  |
| COST | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0343) | PASS |  |  |
| COST | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COST | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.95× / 0.71× | 0.95× / 0.71× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COST | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 2234726) | 20 bars, last ('2026-11-18', 2234726) | PASS |  |  |
| COTG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $16.52 | $16.52 | PASS |  |  |
| COTG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $15.34 | $15.34 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COTG | E3 | percent from the 21-day average | 7.7% above | 7.7% above | PASS |  |  |
| COTG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COTG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.51 | $0.51 (sr=0.5146) | PASS |  | Wilder ATR14 |
| COTG | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves above |
| COTG | L-ema21 | ladder row ema21: price and gap = price vs average | $15.34, 7.7% | $15.34, 7.7% | PASS |  |  |
| COTG | L-note | "Last close $X · date" note = last completed bar | Last close $16.53 · Nov 18 | $16.53 · Nov 18 | PASS |  |  |
| COTG | L-now | ladder price row = compared price; name = the basis label | $16.52 "After hours" | $16.52 "after hours" | PASS |  |  |
| COTG | L-sma200 | ladder row sma200: price and gap = price vs average | $13.93, 18.7% | $13.93, 18.7% | PASS |  |  |
| COTG | L-sma50 | ladder row sma50: price and gap = price vs average | $13.39, 23.4% | $13.39, 23.4% | PASS |  |  |
| COTG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $16.52 / entry $16.52 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COTG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COTG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 67.4 | 67.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COTG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +30.6% vs +11.8% | 30.6% vs 11.8% | PASS |  |  |
| COTG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COTG | T4 | ADX 14 (S1 /api/sr meta.adx) | 52.1 | 52.0 | PASS |  | Wilder, completed bars |
| COTG | T4w | words "20 or more / below 20" | 20 or more | ADX 52.0 | PASS |  |  |
| COTG | T5 | "counted at the last close ($X, date)" = last completed bar | $16.53, Nov 18 | $16.53, Nov 18 | PASS |  |  |
| COTG | T6 | price vs 200-day average (S1 pattern sma values) | $16.53 vs $13.92 · +18.8% | $16.53 vs $13.93 · 18.7% | PASS |  |  |
| COTG | T6w | word "Above" | Above | Above | PASS |  |  |
| COTG | T7 | price vs 50-day average (S1 pattern sma values) | $16.53 vs $13.39 · +23.5% | $16.53 vs $13.39 · 23.4% | PASS |  |  |
| COTG | T7w | word "Above" | Above | Above | PASS |  |  |
| COTG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| COTG | T8r | word "rising" | still rising | rising | PASS |  |  |
| COTG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COTG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 7.1% below | PASS |  |  |
| COTG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $17.80 | $17.80299949645996 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COTG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.36%, close location 0.02, OBV rising |
| COTG | V2 | day change of the last completed bar | down 2.4% | -2.36% | PASS |  |  |
| COTG | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0192) | PASS |  |  |
| COTG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COTG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.47× / 0.76× | 0.47× / 0.76× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COTG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 49000) | 20 bars, last ('2026-11-18', 49000) | PASS |  |  |
| CSU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3,323.15 | $3,323.15 | PASS |  |  |
| CSU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3363.78 | $3363.78 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CSU.TO | E3 | percent from the 21-day average | 1.2% below | 1.2% below | PASS |  |  |
| CSU.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CSU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $118.38 | $118.38 (sr=118.3824) | PASS |  | Wilder ATR14 |
| CSU.TO | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| CSU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $3363.78, -1.2% | $3363.78, -1.2% | PASS |  |  |
| CSU.TO | L-note | "Last close $X · date" note = last completed bar | Last close $3,323.15 · Nov 18 | $3,323.15 · Nov 18 | PASS |  |  |
| CSU.TO | L-now | ladder price row = compared price; name = the basis label | $3323.15 "After hours" | $3323.15 "after hours" | PASS |  |  |
| CSU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $2817.22, 18.0% | $2817.22, 18.0% | PASS |  |  |
| CSU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $3135.44, 6.0% | $3135.44, 6.0% | PASS |  |  |
| CSU.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3,323.15 / entry $3,323.15 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CSU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CSU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.4 | 49.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CSU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.8% vs +11.8% | 2.8% vs 11.8% | PASS |  |  |
| CSU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CSU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.7 | 30.7 | PASS |  | Wilder, completed bars |
| CSU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 30.7 | PASS |  |  |
| CSU.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $3,323.15, Nov 18 | $3323.15, Nov 18 | PASS |  |  |
| CSU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $3,323.15 vs $2,817.22 · +18.0% | $3323.15 vs $2817.22 · 18.0% | PASS |  |  |
| CSU.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CSU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $3,323.15 vs $3,135.44 · +6.0% | $3323.15 vs $3135.44 · 6.0% | PASS |  |  |
| CSU.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CSU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.6% over 30 td | PASS |  |  |
| CSU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CSU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CSU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.8% below $3,565.00 | 6.8% below $3565.00 | PASS |  | closing high would be 3526.52 |
| CSU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.8% below | PASS |  |  |
| CSU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $3,565.00 | $3565 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CSU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.19%, close location 0.64, OBV rising |
| CSU.TO | V2 | day change of the last completed bar | up 0.2% | +0.19% | PASS |  |  |
| CSU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| CSU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.80× / 0.05× | 0.80× / 0.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CSU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 48573) | 20 bars, last ('2026-11-18', 48573) | PASS |  |  |
| CVX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $205.88 | $205.88 | PASS |  |  |
| CVX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $217.31 | $217.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CVX | E3 | percent from the 21-day average | 5.3% below | 5.3% below | PASS |  |  |
| CVX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CVX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.26 | $5.26 (sr=5.2568) | PASS |  | Wilder ATR14 |
| CVX | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| CVX | L-ema21 | ladder row ema21: price and gap = price vs average | $217.31, -5.3% | $217.31, -5.3% | PASS |  |  |
| CVX | L-note | "Last close $X · date" note = last completed bar | Last close $205.88 · Nov 18 | $205.88 · Nov 18 | PASS |  |  |
| CVX | L-now | ladder price row = compared price; name = the basis label | $205.88 "After hours" | $205.88 "after hours" | PASS |  |  |
| CVX | L-sma200 | ladder row sma200: price and gap = price vs average | $196.32, 4.9% | $196.32, 4.9% | PASS |  |  |
| CVX | L-sma50 | ladder row sma50: price and gap = price vs average | $215.62, -4.5% | $215.62, -4.5% | PASS |  |  |
| CVX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $205.88 / entry $205.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CVX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CVX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.4 | 36.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CVX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +34.0% vs +11.8% | 34.0% vs 11.8% | PASS |  |  |
| CVX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CVX | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.7 | 25.7 | PASS |  | Wilder, completed bars |
| CVX | T4w | words "20 or more / below 20" | 20 or more | ADX 25.7 | PASS |  |  |
| CVX | T5 | "counted at the last close ($X, date)" = last completed bar | $205.88, Nov 18 | $205.88, Nov 18 | PASS |  |  |
| CVX | T6 | price vs 200-day average (S1 pattern sma values) | $205.88 vs $196.32 · +4.9% | $205.88 vs $196.32 · 4.9% | PASS |  |  |
| CVX | T6w | word "Above" | Above | Above | PASS |  |  |
| CVX | T7 | price vs 50-day average (S1 pattern sma values) | $205.88 vs $215.62 · -4.5% | $205.88 vs $215.62 · -4.5% | PASS |  |  |
| CVX | T7w | word "Below" | Below | Below | PASS |  |  |
| CVX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.7% over 30 td | +4.7% over 30 td | PASS |  |  |
| CVX | T8r | word "rising" | still rising | rising | PASS |  |  |
| CVX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CVX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.9% below $236.48 | 12.9% below $236.48 | PASS |  | closing high would be 235.52 |
| CVX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.9% below | PASS |  |  |
| CVX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $236.48 | $236.48 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CVX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.74%, close location 0.02, OBV falling |
| CVX | V2 | day change of the last completed bar | down 4.7% | -4.74% | PASS |  |  |
| CVX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0191) | PASS |  |  |
| CVX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CVX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.16× / 1.86× | 1.16× / 1.86× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CVX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 10158197) | 20 bars, last ('2026-11-18', 10158197) | PASS |  |  |
| DRAL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $4.15 | $4.15 | PASS |  |  |
| DRAL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $5.85 | $5.85 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAL | E3 | percent from the 21-day average | 29.0% below | 29.0% below | PASS |  |  |
| DRAL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRAL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.77 | $0.77 (sr=0.7746) | PASS |  | Wilder ATR14 |
| DRAL | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| DRAL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| DRAL | L-ema21 | ladder row ema21: price and gap = price vs average | $5.85, -29.0% | $5.85, -29.0% | PASS |  |  |
| DRAL | L-note | "Last close $X · date" note = last completed bar | Last close $4.15 · Nov 18 | $4.15 · Nov 18 | PASS |  |  |
| DRAL | L-now | ladder price row = compared price; name = the basis label | $4.15 "After hours" | $4.15 "after hours" | PASS |  |  |
| DRAL | L-sma50 | ladder row sma50: price and gap = price vs average | $8.54, -51.4% | $8.54, -51.4% | PASS |  |  |
| DRAL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $4.15 / entry $4.15 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.8 | 34.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAL | T4w | words "20 or more / below 20" | 20 or more | ADX 34.8 | PASS |  |  |
| DRAL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.97%, close location 0.58, OBV falling |
| DRAL | V2 | day change of the last completed bar | up 1.0% | +0.97% | PASS |  |  |
| DRAL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.84× / 0.05× | 2.84× / 0.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 683188) | 20 bars, last ('2026-11-18', 683188) | PASS |  |  |
| DRAL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.84, OBV falling | condition true | PASS |  |  |
| DRAM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $40.02 | $40.02 | PASS |  |  |
| DRAM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $44.47 | $44.47 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAM | E3 | percent from the 21-day average | 10.0% below | 10.0% below | PASS |  |  |
| DRAM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRAM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.04 | $3.04 (sr=3.0419) | PASS |  | Wilder ATR14 |
| DRAM | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| DRAM | L-ema21 | ladder row ema21: price and gap = price vs average | $44.47, -10.0% | $44.47, -10.0% | PASS |  |  |
| DRAM | L-note | "Last close $X · date" note = last completed bar | Last close $39.15 · Nov 18 | $39.15 · Nov 18 | PASS |  |  |
| DRAM | L-now | ladder price row = compared price; name = the basis label | $40.02 "After hours" | $40.02 "after hours" | PASS |  |  |
| DRAM | L-sma50 | ladder row sma50: price and gap = price vs average | $52.01, -23.1% | $52.01, -23.1% | PASS |  |  |
| DRAM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $40.02 / entry $40.02 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.6 | 37.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAM | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.6 | 32.6 | PASS |  | Wilder, completed bars |
| DRAM | T4w | words "20 or more / below 20" | 20 or more | ADX 32.6 | PASS |  |  |
| DRAM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.57%, close location 0.53, OBV falling |
| DRAM | V2 | day change of the last completed bar | up 0.6% | +0.57% | PASS |  |  |
| DRAM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.84× / 0.07× | 0.84× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 28921300) | 20 bars, last ('2026-11-18', 28921300) | PASS |  |  |
| DRIV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $26.82 | $26.82 | PASS |  |  |
| DRIV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $29.07 | $29.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRIV | E3 | percent from the 21-day average | 7.7% below | 7.7% below | PASS |  |  |
| DRIV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRIV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.76 | $0.76 (sr=0.7591) | PASS |  | Wilder ATR14 |
| DRIV | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| DRIV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.7 | +6.7 | PASS |  |  |
| DRIV | L-ema21 | ladder row ema21: price and gap = price vs average | $29.07, -7.7% | $29.07, -7.7% | PASS |  |  |
| DRIV | L-note | "Last close $X · date" note = last completed bar | Last close $26.82 · Nov 18 | $26.82 · Nov 18 | PASS |  |  |
| DRIV | L-now | ladder price row = compared price; name = the basis label | $26.82 "After hours" | $26.82 "after hours" | PASS |  |  |
| DRIV | L-sma200 | ladder row sma200: price and gap = price vs average | $34.19, -21.6% | $34.19, -21.6% | PASS |  |  |
| DRIV | L-sma50 | ladder row sma50: price and gap = price vs average | $31.3, -14.3% | $31.30, -14.3% | PASS |  |  |
| DRIV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $26.82 / entry $26.82 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRIV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DRIV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.7 | 30.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRIV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.4% vs +11.8% | -5.4% vs 11.8% | PASS |  |  |
| DRIV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DRIV | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.1 | 38.2 | PASS |  | Wilder, completed bars |
| DRIV | T4w | words "20 or more / below 20" | 20 or more | ADX 38.2 | PASS |  |  |
| DRIV | T5 | "counted at the last close ($X, date)" = last completed bar | $26.82, Nov 18 | $26.82, Nov 18 | PASS |  |  |
| DRIV | T6 | price vs 200-day average (S1 pattern sma values) | $26.82 vs $34.19 · -21.6% | $26.82 vs $34.19 · -21.6% | PASS |  |  |
| DRIV | T6w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T7 | price vs 50-day average (S1 pattern sma values) | $26.82 vs $31.30 · -14.3% | $26.82 vs $31.30 · -14.3% | PASS |  |  |
| DRIV | T7w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.8% over 30 td | -0.8% over 30 td | PASS |  |  |
| DRIV | T8r | word "rising" | not rising | not rising | PASS |  |  |
| DRIV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DRIV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 37.2% below $42.67 | 37.1% below $42.67 | PASS |  | closing high would be 42.45 |
| DRIV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 37.1% below | PASS |  |  |
| DRIV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $42.67 | $42.67459709729379 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DRIV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.67%, close location 0.14, OBV falling |
| DRIV | V2 | day change of the last completed bar | down 0.7% | -0.67% | PASS |  |  |
| DRIV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1351) | PASS |  |  |
| DRIV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRIV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.52× / 0.24× | 0.52× / 0.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRIV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 20700) | 20 bars, last ('2026-11-18', 20700) | PASS |  |  |
| DUK | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $130.05 | $130.05 | PASS |  |  |
| DUK | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $126.27 | $126.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DUK | E3 | percent from the 21-day average | 3.0% above | 3.0% above | PASS |  |  |
| DUK | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DUK | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.13 | $2.13 (sr=2.1298) | PASS |  | Wilder ATR14 |
| DUK | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves above |
| DUK | L-ema21 | ladder row ema21: price and gap = price vs average | $126.27, 3.0% | $126.27, 3.0% | PASS |  |  |
| DUK | L-note | "Last close $X · date" note = last completed bar | Last close $130.05 · Nov 18 | $130.05 · Nov 18 | PASS |  |  |
| DUK | L-now | ladder price row = compared price; name = the basis label | $130.05 "After hours" | $130.05 "after hours" | PASS |  |  |
| DUK | L-sma200 | ladder row sma200: price and gap = price vs average | $122.8, 5.9% | $122.80, 5.9% | PASS |  |  |
| DUK | L-sma50 | ladder row sma50: price and gap = price vs average | $120.29, 8.1% | $120.29, 8.1% | PASS |  |  |
| DUK | S5-price | S5: the same live price reads the same on the header and the Entry block | header $130.05 / entry $130.05 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DUK | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DUK | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 67.0 | 67.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DUK | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +8.7% vs +11.8% | 8.7% vs 11.8% | PASS |  |  |
| DUK | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DUK | T4 | ADX 14 (S1 /api/sr meta.adx) | 47.6 | 47.6 | PASS |  | Wilder, completed bars |
| DUK | T4w | words "20 or more / below 20" | 20 or more | ADX 47.6 | PASS |  |  |
| DUK | T5 | "counted at the last close ($X, date)" = last completed bar | $130.05, Nov 18 | $130.05, Nov 18 | PASS |  |  |
| DUK | T6 | price vs 200-day average (S1 pattern sma values) | $130.05 vs $122.80 · +5.9% | $130.05 vs $122.80 · 5.9% | PASS |  |  |
| DUK | T6w | word "Above" | Above | Above | PASS |  |  |
| DUK | T7 | price vs 50-day average (S1 pattern sma values) | $130.05 vs $120.29 · +8.1% | $130.05 vs $120.29 · 8.1% | PASS |  |  |
| DUK | T7w | word "Above" | Above | Above | PASS |  |  |
| DUK | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.2% over 30 td | +1.2% over 30 td | PASS |  |  |
| DUK | T8r | word "rising" | still rising | rising | PASS |  |  |
| DUK | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DUK | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.4% below $131.87 | 1.4% below $131.87 | PASS |  | closing high would be 130.59 |
| DUK | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.4% below | PASS |  |  |
| DUK | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.87 | $131.86787171141273 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DUK | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 0.16%, close location 0.81, OBV rising |
| DUK | V2 | day change of the last completed bar | up 0.2% | +0.16% | PASS |  |  |
| DUK | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.81 (raw 0.8105) | PASS |  |  |
| DUK | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| DUK | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.73× / 0.10× | 1.73× / 0.10× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DUK | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 7725700) | 20 bars, last ('2026-11-18', 7725700) | PASS |  |  |
| ELIL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $37.92 | $37.92 | PASS |  |  |
| ELIL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $37.97 | $37.97 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ELIL | E3 | percent from the 21-day average | 0.1% below | 0.1% below | PASS |  |  |
| ELIL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ELIL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.23 | $2.23 (sr=2.2299) | PASS |  | Wilder ATR14 |
| ELIL | E5 | distance in normal day-moves | 0.0 | 0.0 | PASS |  | gauge dot note uses the same number:  · 0.0 day-moves below |
| ELIL | L-ema21 | ladder row ema21: price and gap = price vs average | $37.97, -0.1% | $37.97, -0.1% | PASS |  |  |
| ELIL | L-note | "Last close $X · date" note = last completed bar | Last close $38.28 · Nov 18 | $38.28 · Nov 18 | PASS |  |  |
| ELIL | L-now | ladder price row = compared price; name = the basis label | $37.92 "After hours" | $37.92 "after hours" | PASS |  |  |
| ELIL | L-sma200 | ladder row sma200: price and gap = price vs average | $27.08, 40.0% | $27.08, 40.0% | PASS |  |  |
| ELIL | L-sma50 | ladder row sma50: price and gap = price vs average | $32.51, 16.6% | $32.51, 16.6% | PASS |  |  |
| ELIL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $37.92 / entry $37.92 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ELIL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ELIL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.3 | 54.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ELIL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +46.1% vs +11.8% | 46.1% vs 11.8% | PASS |  |  |
| ELIL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ELIL | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.0 | 33.0 | PASS |  | Wilder, completed bars |
| ELIL | T4w | words "20 or more / below 20" | 20 or more | ADX 33.0 | PASS |  |  |
| ELIL | T5 | "counted at the last close ($X, date)" = last completed bar | $38.28, Nov 18 | $38.28, Nov 18 | PASS |  |  |
| ELIL | T6 | price vs 200-day average (S1 pattern sma values) | $38.28 vs $27.08 · +41.4% | $38.28 vs $27.08 · 41.4% | PASS |  |  |
| ELIL | T6w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T7 | price vs 50-day average (S1 pattern sma values) | $38.28 vs $32.51 · +17.7% | $38.28 vs $32.51 · 17.7% | PASS |  |  |
| ELIL | T7w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.0% over 30 td | +5.0% over 30 td | PASS |  |  |
| ELIL | T8r | word "rising" | still rising | rising | PASS |  |  |
| ELIL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ELIL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.1% below $43.56 | 12.1% below $43.56 | PASS |  | closing high would be 41.85 |
| ELIL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.1% below | PASS |  |  |
| ELIL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.56 | $43.55500030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ELIL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.89%, close location 0.06, OBV falling |
| ELIL | V2 | day change of the last completed bar | down 4.9% | -4.89% | PASS |  |  |
| ELIL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0578) | PASS |  |  |
| ELIL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ELIL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.70× / 0.84× | 0.70× / 0.84× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ELIL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 42600) | 20 bars, last ('2026-11-18', 42600) | PASS |  |  |
| EQIX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,036.50 | $1,036.50 | PASS |  |  |
| EQIX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1025.39 | $1025.39 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| EQIX | E3 | percent from the 21-day average | 1.1% above | 1.1% above | PASS |  |  |
| EQIX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| EQIX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $33.03 | $33.03 (sr=33.0268) | PASS |  | Wilder ATR14 |
| EQIX | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| EQIX | L-ema21 | ladder row ema21: price and gap = price vs average | $1025.39, 1.1% | $1025.39, 1.1% | PASS |  |  |
| EQIX | L-note | "Last close $X · date" note = last completed bar | Last close $1,036.50 · Nov 18 | $1,036.50 · Nov 18 | PASS |  |  |
| EQIX | L-now | ladder price row = compared price; name = the basis label | $1036.5 "After hours" | $1036.50 "after hours" | PASS |  |  |
| EQIX | L-sma200 | ladder row sma200: price and gap = price vs average | $1015.18, 2.1% | $1015.18, 2.1% | PASS |  |  |
| EQIX | L-sma50 | ladder row sma50: price and gap = price vs average | $1013.93, 2.2% | $1013.93, 2.2% | PASS |  |  |
| EQIX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,036.50 / entry $1,036.50 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| EQIX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| EQIX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.1 | 53.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| EQIX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +36.5% vs +11.8% | 36.5% vs 11.8% | PASS |  |  |
| EQIX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| EQIX | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.7 | 17.7 | PASS |  | Wilder, completed bars |
| EQIX | T4w | words "20 or more / below 20" | below 20 | ADX 17.7 | PASS |  |  |
| EQIX | T5 | "counted at the last close ($X, date)" = last completed bar | $1,036.50, Nov 18 | $1036.50, Nov 18 | PASS |  |  |
| EQIX | T6 | price vs 200-day average (S1 pattern sma values) | $1,036.50 vs $1,015.18 · +2.1% | $1036.50 vs $1015.18 · 2.1% | PASS |  |  |
| EQIX | T6w | word "Above" | Above | Above | PASS |  |  |
| EQIX | T7 | price vs 50-day average (S1 pattern sma values) | $1,036.50 vs $1,013.93 · +2.2% | $1036.50 vs $1013.93 · 2.2% | PASS |  |  |
| EQIX | T7w | word "Above" | Above | Above | PASS |  |  |
| EQIX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.6% over 30 td | +3.6% over 30 td | PASS |  |  |
| EQIX | T8r | word "rising" | still rising | rising | PASS |  |  |
| EQIX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| EQIX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.8% below $1,112.65 | 6.8% below $1112.65 | PASS |  | closing high would be 1104.67 |
| EQIX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.8% below | PASS |  |  |
| EQIX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,112.65 | $1112.652 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| EQIX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 0.67%, close location 0.82, OBV rising |
| EQIX | V2 | day change of the last completed bar | up 0.7% | +0.67% | PASS |  |  |
| EQIX | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.82 (raw 0.8234) | PASS |  |  |
| EQIX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| EQIX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.79× / 0.21× | 0.79× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| EQIX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 463362) | 20 bars, last ('2026-11-18', 463362) | PASS |  |  |
| ETN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $338.34 | $338.34 | PASS |  |  |
| ETN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $362.52 | $362.52 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ETN | E3 | percent from the 21-day average | 6.7% below | 6.7% below | PASS |  |  |
| ETN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ETN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.47 | $17.47 (sr=17.4723) | PASS |  | Wilder ATR14 |
| ETN | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| ETN | L-ema21 | ladder row ema21: price and gap = price vs average | $362.52, -6.7% | $362.52, -6.7% | PASS |  |  |
| ETN | L-note | "Last close $X · date" note = last completed bar | Last close $338.34 · Nov 18 | $338.34 · Nov 18 | PASS |  |  |
| ETN | L-now | ladder price row = compared price; name = the basis label | $338.34 "After hours" | $338.34 "after hours" | PASS |  |  |
| ETN | L-sma200 | ladder row sma200: price and gap = price vs average | $395.24, -14.4% | $395.24, -14.4% | PASS |  |  |
| ETN | L-sma50 | ladder row sma50: price and gap = price vs average | $395.55, -14.5% | $395.55, -14.5% | PASS |  |  |
| ETN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $338.34 / entry $338.34 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ETN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ETN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.4 | 38.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ETN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +1.2% vs +11.8% | 1.2% vs 11.8% | PASS |  |  |
| ETN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ETN | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.2 | 27.2 | PASS |  | Wilder, completed bars |
| ETN | T4w | words "20 or more / below 20" | 20 or more | ADX 27.2 | PASS |  |  |
| ETN | T5 | "counted at the last close ($X, date)" = last completed bar | $338.34, Nov 18 | $338.34, Nov 18 | PASS |  |  |
| ETN | T6 | price vs 200-day average (S1 pattern sma values) | $338.34 vs $395.24 · -14.4% | $338.34 vs $395.24 · -14.4% | PASS |  |  |
| ETN | T6w | word "Below" | Below | Below | PASS |  |  |
| ETN | T7 | price vs 50-day average (S1 pattern sma values) | $338.34 vs $395.55 · -14.5% | $338.34 vs $395.55 · -14.5% | PASS |  |  |
| ETN | T7w | word "Below" | Below | Below | PASS |  |  |
| ETN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| ETN | T8r | word "rising" | still rising | rising | PASS |  |  |
| ETN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ETN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.0% below $476.54 | 29.0% below $476.54 | PASS |  | closing high would be 458.56 |
| ETN | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.0% below | PASS |  |  |
| ETN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $476.54 | $476.54107 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ETN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.36%, close location 0.59, OBV falling |
| ETN | V2 | day change of the last completed bar | up 0.4% | +0.36% | PASS |  |  |
| ETN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ETN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.97× / 0.07× | 0.97× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ETN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 2564178) | 20 bars, last ('2026-11-18', 2564178) | PASS |  |  |
| FCX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $51.45 | $51.45 | PASS |  |  |
| FCX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $61.15 | $61.15 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FCX | E3 | percent from the 21-day average | 15.9% below | 15.9% below | PASS |  |  |
| FCX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| FCX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.97 | $2.97 (sr=2.9667) | PASS |  | Wilder ATR14 |
| FCX | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| FCX | L-ema21 | ladder row ema21: price and gap = price vs average | $61.15, -15.9% | $61.15, -15.9% | PASS |  |  |
| FCX | L-note | "Last close $X · date" note = last completed bar | Last close $51.45 · Nov 18 | $51.45 · Nov 18 | PASS |  |  |
| FCX | L-now | ladder price row = compared price; name = the basis label | $51.45 "After hours" | $51.45 "after hours" | PASS |  |  |
| FCX | L-sma200 | ladder row sma200: price and gap = price vs average | $64.84, -20.7% | $64.84, -20.7% | PASS |  |  |
| FCX | L-sma50 | ladder row sma50: price and gap = price vs average | $67.15, -23.4% | $67.15, -23.4% | PASS |  |  |
| FCX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $51.45 / entry $51.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| FCX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FCX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 26.2 | 26.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FCX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +29.8% vs +11.8% | 29.8% vs 11.8% | PASS |  |  |
| FCX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FCX | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.4 | 28.4 | PASS |  | Wilder, completed bars |
| FCX | T4w | words "20 or more / below 20" | 20 or more | ADX 28.4 | PASS |  |  |
| FCX | T5 | "counted at the last close ($X, date)" = last completed bar | $51.45, Nov 18 | $51.45, Nov 18 | PASS |  |  |
| FCX | T6 | price vs 200-day average (S1 pattern sma values) | $51.45 vs $64.84 · -20.7% | $51.45 vs $64.84 · -20.7% | PASS |  |  |
| FCX | T6w | word "Below" | Below | Below | PASS |  |  |
| FCX | T7 | price vs 50-day average (S1 pattern sma values) | $51.45 vs $67.16 · -23.4% | $51.45 vs $67.15 · -23.4% | PASS |  |  |
| FCX | T7w | word "Below" | Below | Below | PASS |  |  |
| FCX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| FCX | T8r | word "rising" | still rising | rising | PASS |  |  |
| FCX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FCX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.7% below $80.07 | 35.7% below $80.07 | PASS |  | closing high would be 79.74 |
| FCX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.7% below | PASS |  |  |
| FCX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.07 | $80.06712214676648 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FCX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -6.96%, close location 0.46, OBV falling |
| FCX | V2 | day change of the last completed bar | down 7.0% | -6.96% | PASS |  |  |
| FCX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| FCX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.34× / 1.21× | 2.34× / 1.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FCX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 28462000) | 20 bars, last ('2026-11-18', 28462000) | PASS |  |  |
| FCX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.34, OBV falling | condition true | PASS |  |  |
| FINN.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $31.97 | $31.97 | PASS |  |  |
| FINN.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $32.62 | $32.62 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FINN.NE | E3 | percent from the 21-day average | 2.0% below | 2.0% below | PASS |  |  |
| FINN.NE | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| FINN.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.67 | $0.67 (sr=0.665) | PASS |  | Wilder ATR14 |
| FINN.NE | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| FINN.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $32.62, -2.0% | $32.62, -2.0% | PASS |  |  |
| FINN.NE | L-now | ladder price row = compared price; name = the basis label | $31.97 "Last close" | $31.97 "last close" | PASS |  |  |
| FINN.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.12, 6.1% | $30.12, 6.1% | PASS |  |  |
| FINN.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $33.25, -3.9% | $33.25, -3.9% | PASS |  |  |
| FINN.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FINN.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.5 | 42.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FINN.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +42.7% vs +11.8% | 42.7% vs 11.8% | PASS |  |  |
| FINN.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FINN.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.8 | 13.8 | PASS |  | Wilder, completed bars |
| FINN.NE | T4w | words "20 or more / below 20" | below 20 | ADX 13.8 | PASS |  |  |
| FINN.NE | T6 | price vs 200-day average (S1 pattern sma values) | $31.97 vs $30.12 · +6.1% | $31.97 vs $30.12 · 6.1% | PASS |  |  |
| FINN.NE | T6w | word "Above" | Above | Above | PASS |  |  |
| FINN.NE | T7 | price vs 50-day average (S1 pattern sma values) | $31.97 vs $33.25 · -3.8% | $31.97 vs $33.25 · -3.9% | PASS |  |  |
| FINN.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| FINN.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.6% over 30 td | +4.6% over 30 td | PASS |  |  |
| FINN.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| FINN.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FINN.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.8% below $35.83 | 10.8% below $35.83 | PASS |  | closing high would be 35.43 |
| FINN.NE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.8% below | PASS |  |  |
| FINN.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $35.83 | $35.83000183105469 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FINN.NE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.66%, close location 0.81, OBV falling |
| FINN.NE | V2 | day change of the last completed bar | up 0.7% | +0.66% | PASS |  |  |
| FINN.NE | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.81 (raw 0.8056) | PASS |  |  |
| FINN.NE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| FINN.NE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.64× / 0.32× | 0.64× / 0.32× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FINN.NE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 201023) | 20 bars, last ('2026-11-18', 201023) | PASS |  |  |
| GDX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $75.28 | $75.28 | PASS |  |  |
| GDX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $82.81 | $82.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDX | E3 | percent from the 21-day average | 9.1% below | 9.1% below | PASS |  |  |
| GDX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GDX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.61 | $3.61 (sr=3.6076) | PASS |  | Wilder ATR14 |
| GDX | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| GDX | L-ema21 | ladder row ema21: price and gap = price vs average | $82.81, -9.1% | $82.81, -9.1% | PASS |  |  |
| GDX | L-note | "Last close $X · date" note = last completed bar | Last close $74.82 · Nov 18 | $74.82 · Nov 18 | PASS |  |  |
| GDX | L-now | ladder price row = compared price; name = the basis label | $75.28 "After hours" | $75.28 "after hours" | PASS |  |  |
| GDX | L-sma200 | ladder row sma200: price and gap = price vs average | $89.31, -15.7% | $89.31, -15.7% | PASS |  |  |
| GDX | L-sma50 | ladder row sma50: price and gap = price vs average | $86.99, -13.5% | $86.99, -13.5% | PASS |  |  |
| GDX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $75.28 / entry $75.28 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GDX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.1 | 36.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -0.3% vs +11.8% | -0.3% vs 11.8% | PASS |  |  |
| GDX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDX | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.7 | 18.7 | PASS |  | Wilder, completed bars |
| GDX | T4w | words "20 or more / below 20" | below 20 | ADX 18.7 | PASS |  |  |
| GDX | T5 | "counted at the last close ($X, date)" = last completed bar | $74.82, Nov 18 | $74.82, Nov 18 | PASS |  |  |
| GDX | T6 | price vs 200-day average (S1 pattern sma values) | $74.82 vs $89.31 · -16.2% | $74.82 vs $89.31 · -16.2% | PASS |  |  |
| GDX | T6w | word "Below" | Below | Below | PASS |  |  |
| GDX | T7 | price vs 50-day average (S1 pattern sma values) | $74.82 vs $86.99 · -14.0% | $74.82 vs $86.99 · -14.0% | PASS |  |  |
| GDX | T7w | word "Below" | Below | Below | PASS |  |  |
| GDX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.0% over 30 td | -2.0% over 30 td | PASS |  |  |
| GDX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.1% below $117.18 | 36.1% below $117.18 | PASS |  | closing high would be 115.84 |
| GDX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.1% below | PASS |  |  |
| GDX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $117.18 | $117.18000030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -5.97%, close location 0.43, OBV falling |
| GDX | V2 | day change of the last completed bar | down 6.0% | -5.97% | PASS |  |  |
| GDX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.39× / 1.24× | 2.39× / 1.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 52688300) | 20 bars, last ('2026-11-18', 52688300) | PASS |  |  |
| GDX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.39, OBV falling | condition true | PASS |  |  |
| GDXU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $21.83 | $21.83 | PASS |  |  |
| GDXU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $27.26 | $27.26 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDXU.TO | E3 | percent from the 21-day average | 19.9% below | 19.9% below | PASS |  |  |
| GDXU.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GDXU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.44 | $2.44 (sr=2.4407) | PASS |  | Wilder ATR14 |
| GDXU.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| GDXU.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| GDXU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $27.26, -19.9% | $27.26, -19.9% | PASS |  |  |
| GDXU.TO | L-now | ladder price row = compared price; name = the basis label | $21.83 "Last close" | $21.83 "last close" | PASS |  |  |
| GDXU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $35.78, -39.0% | $35.78, -39.0% | PASS |  |  |
| GDXU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $31.04, -29.7% | $31.04, -29.7% | PASS |  |  |
| GDXU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDXU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.7 | 35.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDXU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -27.6% vs +11.8% | -27.6% vs 11.8% | PASS |  |  |
| GDXU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDXU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.6 | 19.6 | PASS |  | Wilder, completed bars |
| GDXU.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.6 | PASS |  |  |
| GDXU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $21.83 vs $35.78 · -39.0% | $21.83 vs $35.78 · -39.0% | PASS |  |  |
| GDXU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $21.83 vs $31.04 · -29.7% | $21.83 vs $31.04 · -29.7% | PASS |  |  |
| GDXU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -6.8% over 30 td | -6.8% over 30 td | PASS |  |  |
| GDXU.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDXU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDXU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 66.4% below $65.00 | 66.4% below $65.00 | PASS |  | closing high would be 63.22 |
| GDXU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 66.4% below | PASS |  |  |
| GDXU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $65.00 | $65 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDXU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -11.26%, close location 0.48, OBV falling |
| GDXU.TO | V2 | day change of the last completed bar | down 11.3% | -11.26% | PASS |  |  |
| GDXU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDXU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.32× / 1.01× | 3.32× / 1.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDXU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 808589) | 20 bars, last ('2026-11-18', 808589) | PASS |  |  |
| GDXU.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.32, OBV falling | condition true | PASS |  |  |
| GE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $328.10 | $328.10 | PASS |  |  |
| GE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $321.82 | $321.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GE | E3 | percent from the 21-day average | 2.0% above | 2.0% above | PASS |  |  |
| GE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.98 | $9.98 (sr=9.9801) | PASS |  | Wilder ATR14 |
| GE | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves above |
| GE | L-ema21 | ladder row ema21: price and gap = price vs average | $321.82, 2.0% | $321.82, 2.0% | PASS |  |  |
| GE | L-note | "Last close $X · date" note = last completed bar | Last close $328.10 · Nov 18 | $328.10 · Nov 18 | PASS |  |  |
| GE | L-now | ladder price row = compared price; name = the basis label | $328.1 "After hours" | $328.10 "after hours" | PASS |  |  |
| GE | L-sma200 | ladder row sma200: price and gap = price vs average | $323.49, 1.4% | $323.49, 1.4% | PASS |  |  |
| GE | L-sma50 | ladder row sma50: price and gap = price vs average | $314.26, 4.4% | $314.26, 4.4% | PASS |  |  |
| GE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $328.10 / entry $328.10 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.0 | 55.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +11.4% vs +11.8% | 11.4% vs 11.8% | PASS |  |  |
| GE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GE | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.8 | 20.8 | PASS |  | Wilder, completed bars |
| GE | T4w | words "20 or more / below 20" | 20 or more | ADX 20.8 | PASS |  |  |
| GE | T5 | "counted at the last close ($X, date)" = last completed bar | $328.10, Nov 18 | $328.10, Nov 18 | PASS |  |  |
| GE | T6 | price vs 200-day average (S1 pattern sma values) | $328.10 vs $323.49 · +1.4% | $328.10 vs $323.49 · 1.4% | PASS |  |  |
| GE | T6w | word "Above" | Above | Above | PASS |  |  |
| GE | T7 | price vs 50-day average (S1 pattern sma values) | $328.10 vs $314.26 · +4.4% | $328.10 vs $314.26 · 4.4% | PASS |  |  |
| GE | T7w | word "Above" | Above | Above | PASS |  |  |
| GE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.1% over 30 td | +0.1% over 30 td | PASS |  |  |
| GE | T8r | word "rising" | still rising | rising | PASS |  |  |
| GE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 15.5% below $388.25 | 15.5% below $388.25 | PASS |  | closing high would be 380.64 |
| GE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 15.5% below | PASS |  |  |
| GE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $388.25 | $388.25052 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.52%, close location 0.46, OBV rising |
| GE | V2 | day change of the last completed bar | up 0.5% | +0.52% | PASS |  |  |
| GE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.73× / 0.17× | 0.73× / 0.17× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 3545821) | 20 bars, last ('2026-11-18', 3545821) | PASS |  |  |
| GEV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $772.22 | $772.22 | PASS |  |  |
| GEV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $831.99 | $831.99 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV | E3 | percent from the 21-day average | 7.2% below | 7.2% below | PASS |  |  |
| GEV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GEV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $53.67 | $53.67 (sr=53.6672) | PASS |  | Wilder ATR14 |
| GEV | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| GEV | L-ema21 | ladder row ema21: price and gap = price vs average | $831.99, -7.2% | $831.99, -7.2% | PASS |  |  |
| GEV | L-note | "Last close $X · date" note = last completed bar | Last close $772.22 · Nov 18 | $772.22 · Nov 18 | PASS |  |  |
| GEV | L-now | ladder price row = compared price; name = the basis label | $772.22 "After hours" | $772.22 "after hours" | PASS |  |  |
| GEV | L-sma200 | ladder row sma200: price and gap = price vs average | $952.05, -18.9% | $952.05, -18.9% | PASS |  |  |
| GEV | L-sma50 | ladder row sma50: price and gap = price vs average | $902.2, -14.4% | $902.20, -14.4% | PASS |  |  |
| GEV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $772.22 / entry $772.22 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GEV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GEV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.2 | 39.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.2% vs +11.8% | 39.2% vs 11.8% | PASS |  |  |
| GEV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GEV | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.0 | 25.0 | PASS |  | Wilder, completed bars |
| GEV | T4w | words "20 or more / below 20" | 20 or more | ADX 25.0 | PASS |  |  |
| GEV | T5 | "counted at the last close ($X, date)" = last completed bar | $772.22, Nov 18 | $772.22, Nov 18 | PASS |  |  |
| GEV | T6 | price vs 200-day average (S1 pattern sma values) | $772.22 vs $952.05 · -18.9% | $772.22 vs $952.05 · -18.9% | PASS |  |  |
| GEV | T6w | word "Below" | Below | Below | PASS |  |  |
| GEV | T7 | price vs 50-day average (S1 pattern sma values) | $772.22 vs $902.20 · -14.4% | $772.22 vs $902.20 · -14.4% | PASS |  |  |
| GEV | T7w | word "Below" | Below | Below | PASS |  |  |
| GEV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| GEV | T8r | word "rising" | still rising | rising | PASS |  |  |
| GEV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GEV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.4% below $1,195.94 | 35.4% below $1195.94 | PASS |  | closing high would be 1174.86 |
| GEV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.4% below | PASS |  |  |
| GEV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,195.94 | $1195.94 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GEV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.99%, close location 0.07, OBV falling |
| GEV | V2 | day change of the last completed bar | down 1.0% | -0.99% | PASS |  |  |
| GEV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0727) | PASS |  |  |
| GEV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 0.14× | 0.99× / 0.14× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 3142600) | 20 bars, last ('2026-11-18', 3142600) | PASS |  |  |
| GEV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $51.66 | $51.66 | PASS |  |  |
| GEV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $55.63 | $55.63 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV.TO | E3 | percent from the 21-day average | 7.1% below | 7.1% below | PASS |  |  |
| GEV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GEV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.48 | $3.48 (sr=3.4795) | PASS |  | Wilder ATR14 |
| GEV.TO | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| GEV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $55.63, -7.1% | $55.63, -7.1% | PASS |  |  |
| GEV.TO | L-now | ladder price row = compared price; name = the basis label | $51.66 "Last close" | $51.66 "last close" | PASS |  |  |
| GEV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.09, -19.4% | $64.09, -19.4% | PASS |  |  |
| GEV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $60.31, -14.3% | $60.31, -14.3% | PASS |  |  |
| GEV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.1 | 39.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.8% vs +11.8% | 14.8% vs 11.8% | PASS |  |  |
| GEV.TO | T3w | words "past year" vs the window used | 227 / 251 bars back | 250-253 bars | PASS |  |  |
| GEV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.6 | 24.6 | PASS |  | Wilder, completed bars |
| GEV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 24.6 | PASS |  |  |
| GEV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.90%, close location 0.09, OBV falling |
| GEV.TO | V2 | day change of the last completed bar | down 0.9% | -0.90% | PASS |  |  |
| GEV.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0856) | PASS |  |  |
| GEV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.34× / 0.13× | 1.34× / 0.13× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 100846) | 20 bars, last ('2026-11-18', 100846) | PASS |  |  |
| GGLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $64.16 | $64.16 | PASS |  |  |
| GGLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.07 | $73.07 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GGLL | E3 | percent from the 21-day average | 12.2% below | 12.2% below | PASS |  |  |
| GGLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GGLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.91 | $4.91 (sr=4.9061) | PASS |  | Wilder ATR14 |
| GGLL | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| GGLL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| GGLL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.9 | +5.9 | PASS |  |  |
| GGLL | L-ema21 | ladder row ema21: price and gap = price vs average | $73.07, -12.2% | $73.07, -12.2% | PASS |  |  |
| GGLL | L-note | "Last close $X · date" note = last completed bar | Last close $64.16 · Nov 18 | $64.16 · Nov 18 | PASS |  |  |
| GGLL | L-now | ladder price row = compared price; name = the basis label | $64.16 "After hours" | $64.16 "after hours" | PASS |  |  |
| GGLL | L-sma200 | ladder row sma200: price and gap = price vs average | $101.8, -37.0% | $101.80, -37.0% | PASS |  |  |
| GGLL | L-sma50 | ladder row sma50: price and gap = price vs average | $88.5, -27.5% | $88.50, -27.5% | PASS |  |  |
| GGLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $64.16 / entry $64.16 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GGLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GGLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.4 | 33.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GGLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -20.1% vs +11.8% | -20.0% vs 11.8% | PASS |  |  |
| GGLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GGLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.6 | 27.6 | PASS |  | Wilder, completed bars |
| GGLL | T4w | words "20 or more / below 20" | 20 or more | ADX 27.6 | PASS |  |  |
| GGLL | T5 | "counted at the last close ($X, date)" = last completed bar | $64.16, Nov 18 | $64.16, Nov 18 | PASS |  |  |
| GGLL | T6 | price vs 200-day average (S1 pattern sma values) | $64.16 vs $101.80 · -37.0% | $64.16 vs $101.80 · -37.0% | PASS |  |  |
| GGLL | T6w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T7 | price vs 50-day average (S1 pattern sma values) | $64.16 vs $88.50 · -27.5% | $64.16 vs $88.50 · -27.5% | PASS |  |  |
| GGLL | T7w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.1% over 30 td | -3.1% over 30 td | PASS |  |  |
| GGLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GGLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GGLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 57.6% below $151.33 | 57.6% below $151.33 | PASS |  | closing high would be 147.32 |
| GGLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 57.6% below | PASS |  |  |
| GGLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $151.33 | $151.33258699596215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GGLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 1.76%, close location 0.51, OBV falling |
| GGLL | V2 | day change of the last completed bar | up 1.8% | +1.76% | PASS |  |  |
| GGLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GGLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.47× / 0.23× | 0.47× / 0.23× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GGLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 886100) | 20 bars, last ('2026-11-18', 886100) | PASS |  |  |
| GIB-A.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $115.21 | $115.21 | PASS |  |  |
| GIB-A.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.6 | $113.60 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GIB-A.TO | E3 | percent from the 21-day average | 1.4% above | 1.4% above | PASS |  |  |
| GIB-A.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GIB-A.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.63 | $2.63 (sr=2.6293) | PASS |  | Wilder ATR14 |
| GIB-A.TO | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves above |
| GIB-A.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.3 | -5.3 | PASS |  |  |
| GIB-A.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $113.6, 1.4% | $113.60, 1.4% | PASS |  |  |
| GIB-A.TO | L-note | "Last close $X · date" note = last completed bar | Last close $115.21 · Nov 18 | $115.21 · Nov 18 | PASS |  |  |
| GIB-A.TO | L-now | ladder price row = compared price; name = the basis label | $115.21 "After hours" | $115.21 "after hours" | PASS |  |  |
| GIB-A.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $99.8, 15.4% | $99.80, 15.4% | PASS |  |  |
| GIB-A.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $106.1, 8.6% | $106.10, 8.6% | PASS |  |  |
| GIB-A.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $115.21 / entry $115.21 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GIB-A.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GIB-A.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 59.6 | 59.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GIB-A.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -3.5% vs +11.8% | -3.5% vs 11.8% | PASS |  |  |
| GIB-A.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GIB-A.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.6 | 40.6 | PASS |  | Wilder, completed bars |
| GIB-A.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 40.6 | PASS |  |  |
| GIB-A.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $115.21, Nov 18 | $115.21, Nov 18 | PASS |  |  |
| GIB-A.TO | T6 | price vs 200-day average (S1 pattern sma values) | $115.21 vs $99.80 · +15.4% | $115.21 vs $99.80 · 15.4% | PASS |  |  |
| GIB-A.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T7 | price vs 50-day average (S1 pattern sma values) | $115.21 vs $106.10 · +8.6% | $115.21 vs $106.10 · 8.6% | PASS |  |  |
| GIB-A.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.0% over 30 td | -2.0% over 30 td | PASS |  |  |
| GIB-A.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GIB-A.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GIB-A.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.2% below $131.27 | 12.2% below $131.27 | PASS |  | closing high would be 130.81 |
| GIB-A.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.2% below | PASS |  |  |
| GIB-A.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.27 | $131.26875042581284 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GIB-A.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.12%, close location 0.53, OBV rising |
| GIB-A.TO | V2 | day change of the last completed bar | up 0.1% | +0.12% | PASS |  |  |
| GIB-A.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GIB-A.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.97× / 0.05× | 0.97× / 0.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GIB-A.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 611689) | 20 bars, last ('2026-11-18', 611689) | PASS |  |  |
| GOOGL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $282.44 | $282.44 | PASS |  |  |
| GOOGL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $298.33 | $298.33 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GOOGL | E3 | percent from the 21-day average | 5.3% below | 5.3% below | PASS |  |  |
| GOOGL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GOOGL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.78 | $9.78 (sr=9.7792) | PASS |  | Wilder ATR14 |
| GOOGL | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| GOOGL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.0 | +4.0 | PASS |  |  |
| GOOGL | L-ema21 | ladder row ema21: price and gap = price vs average | $298.33, -5.3% | $298.33, -5.3% | PASS |  |  |
| GOOGL | L-note | "Last close $X · date" note = last completed bar | Last close $282.44 · Nov 18 | $282.44 · Nov 18 | PASS |  |  |
| GOOGL | L-now | ladder price row = compared price; name = the basis label | $282.44 "After hours" | $282.44 "after hours" | PASS |  |  |
| GOOGL | L-sma200 | ladder row sma200: price and gap = price vs average | $337.33, -16.3% | $337.33, -16.3% | PASS |  |  |
| GOOGL | L-sma50 | ladder row sma50: price and gap = price vs average | $324.96, -13.1% | $324.96, -13.1% | PASS |  |  |
| GOOGL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $282.44 / entry $282.44 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GOOGL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GOOGL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.9 | 34.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GOOGL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -0.4% vs +11.8% | -0.4% vs 11.8% | PASS |  |  |
| GOOGL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GOOGL | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.7 | 25.7 | PASS |  | Wilder, completed bars |
| GOOGL | T4w | words "20 or more / below 20" | 20 or more | ADX 25.7 | PASS |  |  |
| GOOGL | T5 | "counted at the last close ($X, date)" = last completed bar | $282.44, Nov 18 | $282.44, Nov 18 | PASS |  |  |
| GOOGL | T6 | price vs 200-day average (S1 pattern sma values) | $282.44 vs $337.33 · -16.3% | $282.44 vs $337.33 · -16.3% | PASS |  |  |
| GOOGL | T6w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T7 | price vs 50-day average (S1 pattern sma values) | $282.44 vs $324.96 · -13.1% | $282.44 vs $324.96 · -13.1% | PASS |  |  |
| GOOGL | T7w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.6% over 30 td | -0.6% over 30 td | PASS |  |  |
| GOOGL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GOOGL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GOOGL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 30.8% below $408.10 | 30.8% below $408.10 | PASS |  | closing high would be 402.12 |
| GOOGL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 30.8% below | PASS |  |  |
| GOOGL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $408.10 | $408.10376741205215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GOOGL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.80%, close location 0.52, OBV falling |
| GOOGL | V2 | day change of the last completed bar | up 0.8% | +0.80% | PASS |  |  |
| GOOGL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GOOGL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.84× / 0.23× | 0.84× / 0.23× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GOOGL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 27103684) | 20 bars, last ('2026-11-18', 27103684) | PASS |  |  |
| HD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.3 | 55.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -2.6% vs +11.8% | -2.6% vs 11.8% | PASS |  |  |
| HD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HURA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $36.66 | $36.66 | PASS |  |  |
| HURA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.16 | $40.16 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HURA.TO | E3 | percent from the 21-day average | 8.7% below | 8.7% below | PASS |  |  |
| HURA.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HURA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.36 | $1.36 (sr=1.3579) | PASS |  | Wilder ATR14 |
| HURA.TO | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| HURA.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +9.4 | +9.4 | PASS |  |  |
| HURA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.16, -8.7% | $40.16, -8.7% | PASS |  |  |
| HURA.TO | L-now | ladder price row = compared price; name = the basis label | $36.66 "Last close" | $36.66 "last close" | PASS |  |  |
| HURA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $52.89, -30.7% | $52.89, -30.7% | PASS |  |  |
| HURA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $43.94, -16.6% | $43.94, -16.6% | PASS |  |  |
| HURA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HURA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.5 | 33.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HURA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -27.6% vs +11.8% | -27.5% vs 11.8% | PASS |  |  |
| HURA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HURA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.3 | 30.3 | PASS |  | Wilder, completed bars |
| HURA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 30.3 | PASS |  |  |
| HURA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $36.66 vs $52.89 · -30.7% | $36.66 vs $52.89 · -30.7% | PASS |  |  |
| HURA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $36.66 vs $43.94 · -16.6% | $36.66 vs $43.94 · -16.6% | PASS |  |  |
| HURA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.3% over 30 td | -5.3% over 30 td | PASS |  |  |
| HURA.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HURA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HURA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 50.4% below $73.95 | 50.4% below $73.95 | PASS |  | closing high would be 73.19 |
| HURA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 50.4% below | PASS |  |  |
| HURA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $73.95 | $73.94999694824219 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HURA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.95%, close location 0.07, OBV falling |
| HURA.TO | V2 | day change of the last completed bar | down 1.9% | -1.95% | PASS |  |  |
| HURA.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0674) | PASS |  |  |
| HURA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HURA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.52× / 0.53× | 0.52× / 0.53× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HURA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 6235) | 20 bars, last ('2026-11-18', 6235) | PASS |  |  |
| HXQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $111.81 | $111.81 | PASS |  |  |
| HXQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $114.93 | $114.93 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HXQ.TO | E3 | percent from the 21-day average | 2.7% below | 2.7% below | PASS |  |  |
| HXQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HXQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.59 | $2.59 (sr=2.5917) | PASS |  | Wilder ATR14 |
| HXQ.TO | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| HXQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $114.93, -2.7% | $114.93, -2.7% | PASS |  |  |
| HXQ.TO | L-now | ladder price row = compared price; name = the basis label | $111.81 "Last close" | $111.81 "last close" | PASS |  |  |
| HXQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $112.29, -0.4% | $112.29, -0.4% | PASS |  |  |
| HXQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $119.09, -6.1% | $119.09, -6.1% | PASS |  |  |
| HXQ.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HXQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.5 | 41.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HXQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +13.5% vs +11.8% | 13.5% vs 11.8% | PASS |  |  |
| HXQ.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HXQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.1 | 31.1 | PASS |  | Wilder, completed bars |
| HXQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 31.1 | PASS |  |  |
| HXQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $111.81 vs $112.29 · -0.4% | $111.81 vs $112.29 · -0.4% | PASS |  |  |
| HXQ.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HXQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $111.81 vs $119.09 · -6.1% | $111.81 vs $119.09 · -6.1% | PASS |  |  |
| HXQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HXQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.2% over 30 td | PASS |  |  |
| HXQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| HXQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HXQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.9% below $128.37 | 12.9% below $128.37 | PASS |  | closing high would be 127.79 |
| HXQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.9% below | PASS |  |  |
| HXQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $128.37 | $128.3699951171875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HXQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 1.07%, close location 0.66, OBV falling |
| HXQ.TO | V2 | day change of the last completed bar | up 1.1% | +1.07% | PASS |  |  |
| HXQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HXQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.63× / 0.46× | 0.63× / 0.46× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HXQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 20533) | 20 bars, last ('2026-11-18', 20533) | PASS |  |  |
| JNJ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $272.70 | $272.70 | PASS |  |  |
| JNJ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $274.39 | $274.39 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JNJ | E3 | percent from the 21-day average | 0.6% below | 0.6% below | PASS |  |  |
| JNJ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| JNJ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.71 | $6.71 (sr=6.712) | PASS |  | Wilder ATR14 |
| JNJ | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| JNJ | L-ema21 | ladder row ema21: price and gap = price vs average | $274.39, -0.6% | $274.39, -0.6% | PASS |  |  |
| JNJ | L-note | "Last close $X · date" note = last completed bar | Last close $272.70 · Nov 18 | $272.70 · Nov 18 | PASS |  |  |
| JNJ | L-now | ladder price row = compared price; name = the basis label | $272.7 "After hours" | $272.70 "after hours" | PASS |  |  |
| JNJ | L-sma200 | ladder row sma200: price and gap = price vs average | $249.08, 9.5% | $249.08, 9.5% | PASS |  |  |
| JNJ | L-sma50 | ladder row sma50: price and gap = price vs average | $267.31, 2.0% | $267.31, 2.0% | PASS |  |  |
| JNJ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $272.70 / entry $272.70 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JNJ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JNJ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.8 | 49.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JNJ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.4% vs +11.8% | 39.4% vs 11.8% | PASS |  |  |
| JNJ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JNJ | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.1 | 25.1 | PASS |  | Wilder, completed bars |
| JNJ | T4w | words "20 or more / below 20" | 20 or more | ADX 25.1 | PASS |  |  |
| JNJ | T5 | "counted at the last close ($X, date)" = last completed bar | $272.70, Nov 18 | $272.70, Nov 18 | PASS |  |  |
| JNJ | T6 | price vs 200-day average (S1 pattern sma values) | $272.70 vs $249.08 · +9.5% | $272.70 vs $249.08 · 9.5% | PASS |  |  |
| JNJ | T6w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T7 | price vs 50-day average (S1 pattern sma values) | $272.70 vs $267.31 · +2.0% | $272.70 vs $267.31 · 2.0% | PASS |  |  |
| JNJ | T7w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.6% over 30 td | +3.6% over 30 td | PASS |  |  |
| JNJ | T8r | word "rising" | still rising | rising | PASS |  |  |
| JNJ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JNJ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.0% below $290.25 | 6.0% below $290.25 | PASS |  | closing high would be 285.75 |
| JNJ | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.0% below | PASS |  |  |
| JNJ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $290.25 | $290.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JNJ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.15%, close location 0.02, OBV falling |
| JNJ | V2 | day change of the last completed bar | down 2.1% | -2.15% | PASS |  |  |
| JNJ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0196) | PASS |  |  |
| JNJ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JNJ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.08× / 0.87× | 1.08× / 0.87× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JNJ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 7932910) | 20 bars, last ('2026-11-18', 7932910) | PASS |  |  |
| JPM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $324.11 | $324.11 | PASS |  |  |
| JPM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $337.69 | $337.69 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JPM | E3 | percent from the 21-day average | 4.0% below | 4.0% below | PASS |  |  |
| JPM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| JPM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.38 | $7.38 (sr=7.3809) | PASS |  | Wilder ATR14 |
| JPM | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| JPM | L-ema21 | ladder row ema21: price and gap = price vs average | $337.69, -4.0% | $337.69, -4.0% | PASS |  |  |
| JPM | L-note | "Last close $X · date" note = last completed bar | Last close $324.11 · Nov 18 | $324.11 · Nov 18 | PASS |  |  |
| JPM | L-now | ladder price row = compared price; name = the basis label | $324.11 "After hours" | $324.11 "after hours" | PASS |  |  |
| JPM | L-sma200 | ladder row sma200: price and gap = price vs average | $322.82, 0.4% | $322.82, 0.4% | PASS |  |  |
| JPM | L-sma50 | ladder row sma50: price and gap = price vs average | $338.32, -4.2% | $338.32, -4.2% | PASS |  |  |
| JPM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $324.11 / entry $324.11 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JPM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JPM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.2 | 38.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JPM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +10.3% vs +11.8% | 10.3% vs 11.8% | PASS |  |  |
| JPM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JPM | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.5 | 16.5 | PASS |  | Wilder, completed bars |
| JPM | T4w | words "20 or more / below 20" | below 20 | ADX 16.5 | PASS |  |  |
| JPM | T5 | "counted at the last close ($X, date)" = last completed bar | $324.11, Nov 18 | $324.11, Nov 18 | PASS |  |  |
| JPM | T6 | price vs 200-day average (S1 pattern sma values) | $324.11 vs $322.82 · +0.4% | $324.11 vs $322.82 · 0.4% | PASS |  |  |
| JPM | T6w | word "Above" | Above | Above | PASS |  |  |
| JPM | T7 | price vs 50-day average (S1 pattern sma values) | $324.11 vs $338.32 · -4.2% | $324.11 vs $338.32 · -4.2% | PASS |  |  |
| JPM | T7w | word "Below" | Below | Below | PASS |  |  |
| JPM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.2% over 30 td | +1.2% over 30 td | PASS |  |  |
| JPM | T8r | word "rising" | still rising | rising | PASS |  |  |
| JPM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JPM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.1% below $364.68 | 11.1% below $364.68 | PASS |  | closing high would be 363.37 |
| JPM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.1% below | PASS |  |  |
| JPM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $364.68 | $364.68062001340013 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JPM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.77%, close location 0.06, OBV falling |
| JPM | V2 | day change of the last completed bar | down 1.8% | -1.77% | PASS |  |  |
| JPM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0627) | PASS |  |  |
| JPM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JPM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 0.78× | 0.88× / 0.78× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JPM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 6674408) | 20 bars, last ('2026-11-18', 6674408) | PASS |  |  |
| KEYS | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.0 | 39.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| KEYS | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +62.1% vs +11.8% | 62.1% vs 11.8% | PASS |  |  |
| KEYS | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LIN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $512.16 | $512.16 | PASS |  |  |
| LIN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $513.51 | $513.51 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LIN | E3 | percent from the 21-day average | 0.3% below | 0.3% below | PASS |  |  |
| LIN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| LIN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.88 | $8.88 (sr=8.8807) | PASS |  | Wilder ATR14 |
| LIN | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| LIN | L-ema21 | ladder row ema21: price and gap = price vs average | $513.51, -0.3% | $513.51, -0.3% | PASS |  |  |
| LIN | L-note | "Last close $X · date" note = last completed bar | Last close $512.16 · Nov 18 | $512.16 · Nov 18 | PASS |  |  |
| LIN | L-now | ladder price row = compared price; name = the basis label | $512.16 "After hours" | $512.16 "after hours" | PASS |  |  |
| LIN | L-sma200 | ladder row sma200: price and gap = price vs average | $495.54, 3.4% | $495.54, 3.4% | PASS |  |  |
| LIN | L-sma50 | ladder row sma50: price and gap = price vs average | $492.96, 3.9% | $492.96, 3.9% | PASS |  |  |
| LIN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $512.16 / entry $512.16 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LIN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LIN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.4 | 51.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LIN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.1% vs +11.8% | 25.1% vs 11.8% | PASS |  |  |
| LIN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LIN | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.2 | 30.2 | PASS |  | Wilder, completed bars |
| LIN | T4w | words "20 or more / below 20" | 20 or more | ADX 30.2 | PASS |  |  |
| LIN | T5 | "counted at the last close ($X, date)" = last completed bar | $512.16, Nov 18 | $512.16, Nov 18 | PASS |  |  |
| LIN | T6 | price vs 200-day average (S1 pattern sma values) | $512.16 vs $495.54 · +3.4% | $512.16 vs $495.54 · 3.4% | PASS |  |  |
| LIN | T6w | word "Above" | Above | Above | PASS |  |  |
| LIN | T7 | price vs 50-day average (S1 pattern sma values) | $512.16 vs $492.96 · +3.9% | $512.16 vs $492.96 · 3.9% | PASS |  |  |
| LIN | T7w | word "Above" | Above | Above | PASS |  |  |
| LIN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.3% over 30 td | PASS |  |  |
| LIN | T8r | word "rising" | still rising | rising | PASS |  |  |
| LIN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LIN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.3% below $546.47 | 6.3% below $546.47 | PASS |  | closing high would be 544.91 |
| LIN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.3% below | PASS |  |  |
| LIN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $546.47 | $546.46627 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LIN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.57%, close location 0.84, OBV falling |
| LIN | V2 | day change of the last completed bar | down 0.6% | -0.57% | PASS |  |  |
| LIN | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.84 (raw 0.8387) | PASS |  |  |
| LIN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| LIN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.66× / 0.33× | 0.66× / 0.33× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LIN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1374036) | 20 bars, last ('2026-11-18', 1374036) | PASS |  |  |
| LLY | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 63.2 | 63.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LLY | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +39.4% vs +11.8% | 39.4% vs 11.8% | PASS |  |  |
| LLY | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MDA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.98 | $39.98 | PASS |  |  |
| MDA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.46 | $40.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MDA.TO | E3 | percent from the 21-day average | 1.2% below | 1.2% below | PASS |  |  |
| MDA.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MDA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.20 | $2.20 (sr=2.1959) | PASS |  | Wilder ATR14 |
| MDA.TO | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| MDA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.46, -1.2% | $40.46, -1.2% | PASS |  |  |
| MDA.TO | L-note | "Last close $X · date" note = last completed bar | Last close $39.98 · Nov 18 | $39.98 · Nov 18 | PASS |  |  |
| MDA.TO | L-now | ladder price row = compared price; name = the basis label | $39.98 "After hours" | $39.98 "after hours" | PASS |  |  |
| MDA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $44.7, -10.6% | $44.70, -10.6% | PASS |  |  |
| MDA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $40.88, -2.2% | $40.88, -2.2% | PASS |  |  |
| MDA.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $39.98 / entry $39.98 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MDA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MDA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.3 | 48.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MDA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +84.8% vs +11.8% | 84.8% vs 11.8% | PASS |  |  |
| MDA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MDA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.0 | 25.1 | PASS |  | Wilder, completed bars |
| MDA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.1 | PASS |  |  |
| MDA.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $39.98, Nov 18 | $39.98, Nov 18 | PASS |  |  |
| MDA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $39.98 vs $44.70 · -10.6% | $39.98 vs $44.70 · -10.6% | PASS |  |  |
| MDA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $39.98 vs $40.88 · -2.2% | $39.98 vs $40.88 · -2.2% | PASS |  |  |
| MDA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.8% over 30 td | +2.8% over 30 td | PASS |  |  |
| MDA.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MDA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MDA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 41.1% below $67.90 | 41.1% below $67.90 | PASS |  | closing high would be 67.13 |
| MDA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 41.1% below | PASS |  |  |
| MDA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $67.90 | $67.9000015258789 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MDA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 1.94%, close location 0.56, OBV rising |
| MDA.TO | V2 | day change of the last completed bar | up 1.9% | +1.94% | PASS |  |  |
| MDA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| MDA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.42× / 0.35× | 0.42× / 0.35× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MDA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 669103) | 20 bars, last ('2026-11-18', 669103) | PASS |  |  |
| META | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.0 | 42.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| META | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.1% vs +11.8% | 3.2% vs 11.8% | PASS |  |  |
| META | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| METU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $21.36 | $21.36 | PASS |  |  |
| METU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $23.23 | $23.23 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| METU | E3 | percent from the 21-day average | 8.1% below | 8.1% below | PASS |  |  |
| METU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| METU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.56 | $1.56 (sr=1.5644) | PASS |  | Wilder ATR14 |
| METU | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| METU | L-ema21 | ladder row ema21: price and gap = price vs average | $23.23, -8.1% | $23.23, -8.1% | PASS |  |  |
| METU | L-note | "Last close $X · date" note = last completed bar | Last close $21.36 · Nov 18 | $21.36 · Nov 18 | PASS |  |  |
| METU | L-now | ladder price row = compared price; name = the basis label | $21.36 "After hours" | $21.36 "after hours" | PASS |  |  |
| METU | L-sma200 | ladder row sma200: price and gap = price vs average | $25.17, -15.1% | $25.17, -15.1% | PASS |  |  |
| METU | L-sma50 | ladder row sma50: price and gap = price vs average | $26.84, -20.4% | $26.84, -20.4% | PASS |  |  |
| METU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $21.36 / entry $21.36 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| METU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| METU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.0 | 40.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| METU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -18.8% vs +11.8% | -18.8% vs 11.8% | PASS |  |  |
| METU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| METU | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.2 | 24.1 | PASS |  | Wilder, completed bars |
| METU | T4w | words "20 or more / below 20" | 20 or more | ADX 24.1 | PASS |  |  |
| METU | T5 | "counted at the last close ($X, date)" = last completed bar | $21.36, Nov 18 | $21.36, Nov 18 | PASS |  |  |
| METU | T6 | price vs 200-day average (S1 pattern sma values) | $21.36 vs $25.17 · -15.1% | $21.36 vs $25.17 · -15.1% | PASS |  |  |
| METU | T6w | word "Below" | Below | Below | PASS |  |  |
| METU | T7 | price vs 50-day average (S1 pattern sma values) | $21.36 vs $26.84 · -20.4% | $21.36 vs $26.84 · -20.4% | PASS |  |  |
| METU | T7w | word "Below" | Below | Below | PASS |  |  |
| METU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.6% over 30 td | -3.6% over 30 td | PASS |  |  |
| METU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| METU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| METU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 45.2% below $38.96 | 45.2% below $38.96 | PASS |  | closing high would be 38.45 |
| METU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 45.2% below | PASS |  |  |
| METU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.96 | $38.95624380685178 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| METU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.97%, close location 0.55, OBV falling |
| METU | V2 | day change of the last completed bar | down 1.0% | -0.97% | PASS |  |  |
| METU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| METU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.29× / 0.13× | 0.29× / 0.13× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| METU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1366600) | 20 bars, last ('2026-11-18', 1366600) | PASS |  |  |
| MRVL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.2 | 34.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MRVL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +78.5% vs +11.8% | 78.5% vs 11.8% | PASS |  |  |
| MRVL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.9 | 41.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.6% vs +11.8% | 0.6% vs 11.8% | PASS |  |  |
| MSFT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $37.61 | $37.61 | PASS |  |  |
| MSFU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.33 | $40.33 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFU | E3 | percent from the 21-day average | 6.8% below | 6.8% below | PASS |  |  |
| MSFU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MSFU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.28 | $2.28 (sr=2.2779) | PASS |  | Wilder ATR14 |
| MSFU | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| MSFU | L-ema21 | ladder row ema21: price and gap = price vs average | $40.33, -6.8% | $40.33, -6.8% | PASS |  |  |
| MSFU | L-note | "Last close $X · date" note = last completed bar | Last close $37.61 · Nov 18 | $37.61 · Nov 18 | PASS |  |  |
| MSFU | L-now | ladder price row = compared price; name = the basis label | $37.61 "After hours" | $37.61 "after hours" | PASS |  |  |
| MSFU | L-sma200 | ladder row sma200: price and gap = price vs average | $31.09, 21.0% | $31.09, 21.0% | PASS |  |  |
| MSFU | L-sma50 | ladder row sma50: price and gap = price vs average | $40.17, -6.4% | $40.17, -6.4% | PASS |  |  |
| MSFU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $37.61 / entry $37.61 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.7 | 41.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -12.6% vs +11.8% | -12.6% vs 11.8% | PASS |  |  |
| MSFU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFU | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.6 | 18.6 | PASS |  | Wilder, completed bars |
| MSFU | T4w | words "20 or more / below 20" | below 20 | ADX 18.6 | PASS |  |  |
| MSFU | T5 | "counted at the last close ($X, date)" = last completed bar | $37.61, Nov 18 | $37.61, Nov 18 | PASS |  |  |
| MSFU | T6 | price vs 200-day average (S1 pattern sma values) | $37.61 vs $31.09 · +21.0% | $37.61 vs $31.09 · 21.0% | PASS |  |  |
| MSFU | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFU | T7 | price vs 50-day average (S1 pattern sma values) | $37.61 vs $40.17 · -6.4% | $37.61 vs $40.17 · -6.4% | PASS |  |  |
| MSFU | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.7% over 30 td | +1.7% over 30 td | PASS |  |  |
| MSFU | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 18.0% below $45.88 | 18.0% below $45.88 | PASS |  | closing high would be 45.40 |
| MSFU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 18.0% below | PASS |  |  |
| MSFU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $45.88 | $45.880001068115234 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.72%, close location 0.78, OBV falling |
| MSFU | V2 | day change of the last completed bar | up 0.7% | +0.72% | PASS |  |  |
| MSFU | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.78 (raw 0.7761) | PASS |  |  |
| MSFU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.63× / 0.12× | 0.63× / 0.12× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1530900) | 20 bars, last ('2026-11-18', 1530900) | PASS |  |  |
| MTRX.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $28.81 | $28.81 | PASS |  |  |
| MTRX.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $30.94 | $30.94 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MTRX.TO | E3 | percent from the 21-day average | 6.9% below | 6.9% below | PASS |  |  |
| MTRX.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| MTRX.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.94 | $0.94 (sr=0.9407) | PASS |  | Wilder ATR14 |
| MTRX.TO | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| MTRX.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.6 | +3.6 | PASS |  |  |
| MTRX.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $30.94, -6.9% | $30.94, -6.9% | PASS |  |  |
| MTRX.TO | L-now | ladder price row = compared price; name = the basis label | $28.81 "Last close" | $28.81 "last close" | PASS |  |  |
| MTRX.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $34.33, -16.1% | $34.33, -16.1% | PASS |  |  |
| MTRX.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $33.39, -13.7% | $33.39, -13.7% | PASS |  |  |
| MTRX.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.4 | 36.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MTRX.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -3.2% vs +11.8% | -3.2% vs 11.8% | PASS |  |  |
| MTRX.TO | T3w | words "past year" vs the window used | 209 / 251 bars back | 250-253 bars | PASS |  |  |
| MTRX.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.2 | 28.2 | PASS |  | Wilder, completed bars |
| MTRX.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.2 | PASS |  |  |
| MTRX.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -1.10%, close location 0.73, OBV falling |
| MTRX.TO | V2 | day change of the last completed bar | down 1.1% | -1.10% | PASS |  |  |
| MTRX.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MTRX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.23× / 0.34× | 0.23× / 0.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MTRX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 2209) | 20 bars, last ('2026-11-18', 2209) | PASS |  |  |
| MU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.76 | $30.76 | PASS |  |  |
| MU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $35.17 | $35.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MU.TO | E3 | percent from the 21-day average | 12.5% below | 12.5% below | PASS |  |  |
| MU.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| MU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.48 | $2.48 (sr=2.4826) | PASS |  | Wilder ATR14 |
| MU.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| MU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $35.17, -12.5% | $35.17, -12.5% | PASS |  |  |
| MU.TO | L-now | ladder price row = compared price; name = the basis label | $30.76 "Last close" | $30.76 "last close" | PASS |  |  |
| MU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.86, -9.2% | $33.86, -9.2% | PASS |  |  |
| MU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $40.55, -24.1% | $40.55, -24.1% | PASS |  |  |
| MU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.8 | 36.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +199.8% vs +11.8% | 199.8% vs 11.8% | PASS |  |  |
| MU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.5 | 35.5 | PASS |  | Wilder, completed bars |
| MU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 35.5 | PASS |  |  |
| MU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $30.76 vs $33.86 · -9.2% | $30.76 vs $33.86 · -9.2% | PASS |  |  |
| MU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $30.76 vs $40.55 · -24.1% | $30.76 vs $40.55 · -24.1% | PASS |  |  |
| MU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +10.8% over 30 td | +10.9% over 30 td | PASS |  |  |
| MU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 44.4% below $55.28 | 44.4% below $55.28 | PASS |  | closing high would be 53.52 |
| MU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 44.4% below | PASS |  |  |
| MU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $55.28 | $55.282308204978015 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.90%, close location 0.49, OBV falling |
| MU.TO | V2 | day change of the last completed bar | down 0.9% | -0.90% | PASS |  |  |
| MU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.96× / 0.11× | 0.96× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1780012) | 20 bars, last ('2026-11-18', 1780012) | PASS |  |  |
| NEE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $84.78 | $84.78 | PASS |  |  |
| NEE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $84.14 | $84.14 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEE | E3 | percent from the 21-day average | 0.8% above | 0.8% above | PASS |  |  |
| NEE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NEE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.61 | $1.61 (sr=1.6136) | PASS |  | Wilder ATR14 |
| NEE | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves above |
| NEE | L-ema21 | ladder row ema21: price and gap = price vs average | $84.14, 0.8% | $84.14, 0.8% | PASS |  |  |
| NEE | L-note | "Last close $X · date" note = last completed bar | Last close $84.78 · Nov 18 | $84.78 · Nov 18 | PASS |  |  |
| NEE | L-now | ladder price row = compared price; name = the basis label | $84.78 "After hours" | $84.78 "after hours" | PASS |  |  |
| NEE | L-sma200 | ladder row sma200: price and gap = price vs average | $86.52, -2.0% | $86.52, -2.0% | PASS |  |  |
| NEE | L-sma50 | ladder row sma50: price and gap = price vs average | $80.9, 4.8% | $80.90, 4.8% | PASS |  |  |
| NEE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $84.78 / entry $84.78 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.6 | 55.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.0% vs +11.8% | 3.0% vs 11.8% | PASS |  |  |
| NEE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEE | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.6 | 31.6 | PASS |  | Wilder, completed bars |
| NEE | T4w | words "20 or more / below 20" | 20 or more | ADX 31.6 | PASS |  |  |
| NEE | T5 | "counted at the last close ($X, date)" = last completed bar | $84.78, Nov 18 | $84.78, Nov 18 | PASS |  |  |
| NEE | T6 | price vs 200-day average (S1 pattern sma values) | $84.78 vs $86.52 · -2.0% | $84.78 vs $86.52 · -2.0% | PASS |  |  |
| NEE | T6w | word "Below" | Below | Below | PASS |  |  |
| NEE | T7 | price vs 50-day average (S1 pattern sma values) | $84.78 vs $80.90 · +4.8% | $84.78 vs $80.90 · 4.8% | PASS |  |  |
| NEE | T7w | word "Above" | Above | Above | PASS |  |  |
| NEE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.3% over 30 td | +0.3% over 30 td | PASS |  |  |
| NEE | T8r | word "rising" | still rising | rising | PASS |  |  |
| NEE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.9% below $97.30 | 12.9% below $97.30 | PASS |  | closing high would be 96.44 |
| NEE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.9% below | PASS |  |  |
| NEE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $97.30 | $97.30028062322594 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.43%, close location 0.77, OBV falling |
| NEE | V2 | day change of the last completed bar | up 0.4% | +0.43% | PASS |  |  |
| NEE | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.77 (raw 0.7656) | PASS |  |  |
| NEE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NEE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.85× / 0.23× | 0.85× / 0.22× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 10773900) | 20 bars, last ('2026-11-18', 10773900) | PASS |  |  |
| NEM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $104.53 | $104.53 | PASS |  |  |
| NEM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.98 | $113.98 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEM | E3 | percent from the 21-day average | 8.3% below | 8.3% below | PASS |  |  |
| NEM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NEM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.83 | $4.83 (sr=4.8285) | PASS |  | Wilder ATR14 |
| NEM | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| NEM | L-ema21 | ladder row ema21: price and gap = price vs average | $113.98, -8.3% | $113.98, -8.3% | PASS |  |  |
| NEM | L-note | "Last close $X · date" note = last completed bar | Last close $104.53 · Nov 18 | $104.53 · Nov 18 | PASS |  |  |
| NEM | L-now | ladder price row = compared price; name = the basis label | $104.53 "After hours" | $104.53 "after hours" | PASS |  |  |
| NEM | L-sma200 | ladder row sma200: price and gap = price vs average | $111.77, -6.5% | $111.77, -6.5% | PASS |  |  |
| NEM | L-sma50 | ladder row sma50: price and gap = price vs average | $116.88, -10.6% | $116.88, -10.6% | PASS |  |  |
| NEM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $104.53 / entry $104.53 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.5 | 37.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +21.8% vs +11.8% | 21.8% vs 11.8% | PASS |  |  |
| NEM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEM | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.8 | 16.8 | PASS |  | Wilder, completed bars |
| NEM | T4w | words "20 or more / below 20" | below 20 | ADX 16.8 | PASS |  |  |
| NEM | T5 | "counted at the last close ($X, date)" = last completed bar | $104.53, Nov 18 | $104.53, Nov 18 | PASS |  |  |
| NEM | T6 | price vs 200-day average (S1 pattern sma values) | $104.53 vs $111.77 · -6.5% | $104.53 vs $111.77 · -6.5% | PASS |  |  |
| NEM | T6w | word "Below" | Below | Below | PASS |  |  |
| NEM | T7 | price vs 50-day average (S1 pattern sma values) | $104.53 vs $116.88 · -10.6% | $104.53 vs $116.88 · -10.6% | PASS |  |  |
| NEM | T7w | word "Below" | Below | Below | PASS |  |  |
| NEM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.4% over 30 td | +0.4% over 30 td | PASS |  |  |
| NEM | T8r | word "rising" | still rising | rising | PASS |  |  |
| NEM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 22.6% below $135.01 | 22.6% below $135.01 | PASS |  | closing high would be 134.86 |
| NEM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 22.6% below | PASS |  |  |
| NEM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $135.01 | $135.0095325 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change -6.05%, close location 0.41, OBV flat |
| NEM | V2 | day change of the last completed bar | down 6.0% | -6.05% | PASS |  |  |
| NEM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| NEM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.32× / 1.31× | 1.32× / 1.31× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 8515235) | 20 bars, last ('2026-11-18', 8515235) | PASS |  |  |
| NFLX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.6 | 33.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFLX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -47.6% vs +11.8% | -47.6% vs 11.8% | PASS |  |  |
| NFLX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $9.88 | $9.88 | PASS |  |  |
| NFXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $11.38 | $11.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFXL | E3 | percent from the 21-day average | 13.2% below | 13.2% below | PASS |  |  |
| NFXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NFXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.68 | $0.68 (sr=0.684) | PASS |  | Wilder ATR14 |
| NFXL | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| NFXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.8 | +12.8 | PASS |  |  |
| NFXL | L-ema21 | ladder row ema21: price and gap = price vs average | $11.38, -13.2% | $11.38, -13.2% | PASS |  |  |
| NFXL | L-note | "Last close $X · date" note = last completed bar | Last close $9.88 · Nov 18 | $9.88 · Nov 18 | PASS |  |  |
| NFXL | L-now | ladder price row = compared price; name = the basis label | $9.88 "After hours" | $9.88 "after hours" | PASS |  |  |
| NFXL | L-sma200 | ladder row sma200: price and gap = price vs average | $20.13, -50.9% | $20.13, -50.9% | PASS |  |  |
| NFXL | L-sma50 | ladder row sma50: price and gap = price vs average | $13.25, -25.4% | $13.25, -25.4% | PASS |  |  |
| NFXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $9.88 / entry $9.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.7 | 32.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -78.4% vs +11.8% | -78.4% vs 11.8% | PASS |  |  |
| NFXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.5 | 26.5 | PASS |  | Wilder, completed bars |
| NFXL | T4w | words "20 or more / below 20" | 20 or more | ADX 26.5 | PASS |  |  |
| NFXL | T5 | "counted at the last close ($X, date)" = last completed bar | $9.88, Nov 18 | $9.88, Nov 18 | PASS |  |  |
| NFXL | T6 | price vs 200-day average (S1 pattern sma values) | $9.88 vs $20.13 · -50.9% | $9.88 vs $20.13 · -50.9% | PASS |  |  |
| NFXL | T6w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T7 | price vs 50-day average (S1 pattern sma values) | $9.88 vs $13.25 · -25.4% | $9.88 vs $13.25 · -25.4% | PASS |  |  |
| NFXL | T7w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -10.0% over 30 td | -10.0% over 30 td | PASS |  |  |
| NFXL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 78.8% below $46.64 | 78.8% below $46.64 | PASS |  | closing high would be 45.75 |
| NFXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 78.8% below | PASS |  |  |
| NFXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.64 | $46.64217883026212 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.20%, close location 0.29, OBV falling |
| NFXL | V2 | day change of the last completed bar | up 0.2% | +0.20% | PASS |  |  |
| NFXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.08× / 0.03× | 1.08× / 0.03× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1797800) | 20 bars, last ('2026-11-18', 1797800) | PASS |  |  |
| NTR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $94.52 | $94.52 | PASS |  |  |
| NTR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $99.33 | $99.33 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NTR.TO | E3 | percent from the 21-day average | 4.8% below | 4.8% below | PASS |  |  |
| NTR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NTR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.93 | $2.93 (sr=2.9308) | PASS |  | Wilder ATR14 |
| NTR.TO | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| NTR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $99.33, -4.8% | $99.33, -4.8% | PASS |  |  |
| NTR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $94.52 · Nov 18 | $94.52 · Nov 18 | PASS |  |  |
| NTR.TO | L-now | ladder price row = compared price; name = the basis label | $94.52 "After hours" | $94.52 "after hours" | PASS |  |  |
| NTR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $97.77, -3.3% | $97.77, -3.3% | PASS |  |  |
| NTR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $101, -6.4% | $101.00, -6.4% | PASS |  |  |
| NTR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $94.52 / entry $94.52 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NTR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NTR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.2 | 36.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NTR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +21.9% vs +11.8% | 21.9% vs 11.8% | PASS |  |  |
| NTR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NTR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.8 | 19.8 | PASS |  | Wilder, completed bars |
| NTR.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.8 | PASS |  |  |
| NTR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $94.52, Nov 18 | $94.52, Nov 18 | PASS |  |  |
| NTR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $94.52 vs $97.77 · -3.3% | $94.52 vs $97.77 · -3.3% | PASS |  |  |
| NTR.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| NTR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $94.52 vs $101.00 · -6.4% | $94.52 vs $101.00 · -6.4% | PASS |  |  |
| NTR.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| NTR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| NTR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| NTR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NTR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.2% below $114.19 | 17.2% below $114.19 | PASS |  | closing high would be 111.71 |
| NTR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.2% below | PASS |  |  |
| NTR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $114.19 | $114.18839715257722 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NTR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -4.54%, close location 0.03, OBV rising |
| NTR.TO | V2 | day change of the last completed bar | down 4.5% | -4.54% | PASS |  |  |
| NTR.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0258) | PASS |  |  |
| NTR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| NTR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.45× / 1.46× | 0.45× / 1.47× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NTR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 857424) | 20 bars, last ('2026-11-18', 857424) | PASS |  |  |
| NVDA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.5 | 22.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -16.5% vs +11.8% | -16.5% vs 11.8% | PASS |  |  |
| NVDA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $15.24 | $15.24 | PASS |  |  |
| NVDL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $23.73 | $23.73 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDL | E3 | percent from the 21-day average | 35.8% below | 35.8% below | PASS |  |  |
| NVDL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NVDL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.46 | $2.46 (sr=2.4628) | PASS |  | Wilder ATR14 |
| NVDL | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| NVDL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| NVDL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| NVDL | L-ema21 | ladder row ema21: price and gap = price vs average | $23.73, -35.8% | $23.73, -35.8% | PASS |  |  |
| NVDL | L-note | "Last close $X · date" note = last completed bar | Last close $15.24 · Nov 18 | $15.24 · Nov 18 | PASS |  |  |
| NVDL | L-now | ladder price row = compared price; name = the basis label | $15.24 "After hours" | $15.24 "after hours" | PASS |  |  |
| NVDL | L-sma200 | ladder row sma200: price and gap = price vs average | $31.24, -51.2% | $31.24, -51.2% | PASS |  |  |
| NVDL | L-sma50 | ladder row sma50: price and gap = price vs average | $31.24, -51.2% | $31.24, -51.2% | PASS |  |  |
| NVDL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $15.24 / entry $15.24 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 21.5 | 21.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -46.4% vs +11.8% | -46.4% vs 11.8% | PASS |  |  |
| NVDL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDL | T4 | ADX 14 (S1 /api/sr meta.adx) | 47.4 | 47.4 | PASS |  | Wilder, completed bars |
| NVDL | T4w | words "20 or more / below 20" | 20 or more | ADX 47.4 | PASS |  |  |
| NVDL | T5 | "counted at the last close ($X, date)" = last completed bar | $15.24, Nov 18 | $15.24, Nov 18 | PASS |  |  |
| NVDL | T6 | price vs 200-day average (S1 pattern sma values) | $15.24 vs $31.24 · -51.2% | $15.24 vs $31.24 · -51.2% | PASS |  |  |
| NVDL | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T7 | price vs 50-day average (S1 pattern sma values) | $15.24 vs $31.24 · -51.2% | $15.24 vs $31.24 · -51.2% | PASS |  |  |
| NVDL | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.5% over 30 td | -0.5% over 30 td | PASS |  |  |
| NVDL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NVDL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 64.8% below $43.27 | 64.8% below $43.27 | PASS |  | closing high would be 43.02 |
| NVDL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 64.8% below | PASS |  |  |
| NVDL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.27 | $43.27333 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.04%, close location 0.05, OBV falling |
| NVDL | V2 | day change of the last completed bar | down 6.0% | -6.04% | PASS |  |  |
| NVDL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0515) | PASS |  |  |
| NVDL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.05× / 0.37× | 3.05× / 0.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 56812900) | 20 bars, last ('2026-11-18', 56812900) | PASS |  |  |
| NVDL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.05, OBV falling | condition true | PASS |  |  |
| ONTO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $201.02 | $201.02 | PASS |  |  |
| ONTO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $208.17 | $208.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ONTO | E3 | percent from the 21-day average | 3.4% below | 3.4% below | PASS |  |  |
| ONTO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ONTO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.00 | $17.00 (sr=17.0039) | PASS |  | Wilder ATR14 |
| ONTO | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| ONTO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.0 | +3.0 | PASS |  |  |
| ONTO | L-ema21 | ladder row ema21: price and gap = price vs average | $208.17, -3.4% | $208.17, -3.4% | PASS |  |  |
| ONTO | L-note | "Last close $X · date" note = last completed bar | Last close $201.02 · Nov 18 | $201.02 · Nov 18 | PASS |  |  |
| ONTO | L-now | ladder price row = compared price; name = the basis label | $201.02 "After hours" | $201.02 "after hours" | PASS |  |  |
| ONTO | L-sma200 | ladder row sma200: price and gap = price vs average | $259.96, -22.7% | $259.96, -22.7% | PASS |  |  |
| ONTO | L-sma50 | ladder row sma50: price and gap = price vs average | $243.45, -17.4% | $243.45, -17.4% | PASS |  |  |
| ONTO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $201.02 / entry $201.02 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ONTO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ONTO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.9 | 44.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ONTO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +62.0% vs +11.8% | 62.0% vs 11.8% | PASS |  |  |
| ONTO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ONTO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.8 | 26.8 | PASS |  | Wilder, completed bars |
| ONTO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.8 | PASS |  |  |
| ONTO | T5 | "counted at the last close ($X, date)" = last completed bar | $201.02, Nov 18 | $201.02, Nov 18 | PASS |  |  |
| ONTO | T6 | price vs 200-day average (S1 pattern sma values) | $201.02 vs $259.96 · -22.7% | $201.02 vs $259.96 · -22.7% | PASS |  |  |
| ONTO | T6w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T7 | price vs 50-day average (S1 pattern sma values) | $201.02 vs $243.45 · -17.4% | $201.02 vs $243.45 · -17.4% | PASS |  |  |
| ONTO | T7w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.5% over 30 td | PASS |  |  |
| ONTO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ONTO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ONTO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 48.0% below $386.46 | 48.0% below $386.46 | PASS |  | closing high would be 378.45 |
| ONTO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 48.0% below | PASS |  |  |
| ONTO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $386.46 | $386.46 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ONTO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.73%, close location 0.32, OBV rising |
| ONTO | V2 | day change of the last completed bar | up 0.7% | +0.73% | PASS |  |  |
| ONTO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| ONTO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.12× / 0.09× | 1.12× / 0.09× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ONTO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1176485) | 20 bars, last ('2026-11-18', 1176485) | PASS |  |  |
| ORBX.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $14.39 | $14.39 | PASS |  |  |
| ORBX.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $15.12 | $15.12 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ORBX.TO | E3 | percent from the 21-day average | 4.8% below | 4.8% below | PASS |  |  |
| ORBX.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ORBX.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.65 | $0.65 (sr=0.6491) | PASS |  | Wilder ATR14 |
| ORBX.TO | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves below |
| ORBX.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $15.12, -4.8% | $15.12, -4.8% | PASS |  |  |
| ORBX.TO | L-now | ladder price row = compared price; name = the basis label | $14.39 "Last close" | $14.39 "last close" | PASS |  |  |
| ORBX.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $16.09, -10.6% | $16.09, -10.6% | PASS |  |  |
| ORBX.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.4 | 42.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ORBX.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.0 | 27.0 | PASS |  | Wilder, completed bars |
| ORBX.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.0 | PASS |  |  |
| ORBX.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.48%, close location 0.00, OBV falling |
| ORBX.TO | V2 | day change of the last completed bar | down 0.5% | -0.48% | PASS |  |  |
| ORBX.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| ORBX.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ORBX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.51× / 0.11× | 0.51× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORBX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 3267) | 20 bars, last ('2026-11-18', 3267) | PASS |  |  |
| ORCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $113.89 | $113.89 | PASS |  |  |
| ORCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $124.36 | $124.36 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ORCL | E3 | percent from the 21-day average | 8.4% below | 8.4% below | PASS |  |  |
| ORCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ORCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.71 | $7.71 (sr=7.7131) | PASS |  | Wilder ATR14 |
| ORCL | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| ORCL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| ORCL | L-ema21 | ladder row ema21: price and gap = price vs average | $124.36, -8.4% | $124.36, -8.4% | PASS |  |  |
| ORCL | L-note | "Last close $X · date" note = last completed bar | Last close $113.89 · Nov 18 | $113.89 · Nov 18 | PASS |  |  |
| ORCL | L-now | ladder price row = compared price; name = the basis label | $113.89 "After hours" | $113.89 "after hours" | PASS |  |  |
| ORCL | L-sma200 | ladder row sma200: price and gap = price vs average | $152.54, -25.3% | $152.54, -25.3% | PASS |  |  |
| ORCL | L-sma50 | ladder row sma50: price and gap = price vs average | $133.75, -14.8% | $133.75, -14.8% | PASS |  |  |
| ORCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $113.89 / entry $113.89 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ORCL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ORCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.3 | 39.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ORCL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -47.7% vs +11.8% | -47.7% vs 11.8% | PASS |  |  |
| ORCL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ORCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.3 | 13.3 | PASS |  | Wilder, completed bars |
| ORCL | T4w | words "20 or more / below 20" | below 20 | ADX 13.3 | PASS |  |  |
| ORCL | T5 | "counted at the last close ($X, date)" = last completed bar | $113.89, Nov 18 | $113.89, Nov 18 | PASS |  |  |
| ORCL | T6 | price vs 200-day average (S1 pattern sma values) | $113.89 vs $152.54 · -25.3% | $113.89 vs $152.54 · -25.3% | PASS |  |  |
| ORCL | T6w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T7 | price vs 50-day average (S1 pattern sma values) | $113.89 vs $133.75 · -14.8% | $113.89 vs $133.75 · -14.8% | PASS |  |  |
| ORCL | T7w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.3% over 30 td | -5.3% over 30 td | PASS |  |  |
| ORCL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| ORCL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ORCL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 54.2% below $248.47 | 54.2% below $248.47 | PASS |  | closing high would be 246.38 |
| ORCL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 54.2% below | PASS |  |  |
| ORCL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $248.47 | $248.46982 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ORCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.97%, close location 0.15, OBV falling |
| ORCL | V2 | day change of the last completed bar | down 1.0% | -0.97% | PASS |  |  |
| ORCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1466) | PASS |  |  |
| ORCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ORCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.42× / 0.14× | 0.42× / 0.14× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 15178970) | 20 bars, last ('2026-11-18', 15178970) | PASS |  |  |
| PG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 69.3 | 69.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +21.2% vs +11.8% | 21.2% vs 11.8% | PASS |  |  |
| PG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PNG.V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $2.99 | $2.99 | PASS |  |  |
| PNG.V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3.59 | $3.59 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PNG.V | E3 | percent from the 21-day average | 16.8% below | 16.8% below | PASS |  |  |
| PNG.V | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| PNG.V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.22 | $0.22 (sr=0.2239) | PASS |  | Wilder ATR14 |
| PNG.V | E5 | distance in normal day-moves | 2.7 | 2.7 | PASS |  | gauge dot note uses the same number:  · 2.7 day-moves below |
| PNG.V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +13.3 | +13.3 | PASS |  |  |
| PNG.V | L-ema21 | ladder row ema21: price and gap = price vs average | $3.59, -16.8% | $3.59, -16.8% | PASS |  |  |
| PNG.V | L-now | ladder price row = compared price; name = the basis label | $2.99 "Last close" | $2.99 "last close" | PASS |  |  |
| PNG.V | L-sma200 | ladder row sma200: price and gap = price vs average | $6.58, -54.5% | $6.58, -54.5% | PASS |  |  |
| PNG.V | L-sma50 | ladder row sma50: price and gap = price vs average | $4.12, -27.5% | $4.12, -27.5% | PASS |  |  |
| PNG.V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PNG.V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 25.4 | 25.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PNG.V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -43.8% vs +11.8% | -43.8% vs 11.8% | PASS |  |  |
| PNG.V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PNG.V | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.6 | 38.5 | PASS |  | Wilder, completed bars |
| PNG.V | T4w | words "20 or more / below 20" | 20 or more | ADX 38.5 | PASS |  |  |
| PNG.V | T6 | price vs 200-day average (S1 pattern sma values) | $2.99 vs $6.58 · -54.6% | $2.99 vs $6.58 · -54.5% | PASS |  |  |
| PNG.V | T6w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T7w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -7.6% over 30 td | -7.7% over 30 td | PASS |  |  |
| PNG.V | T8r | word "rising" | not rising | not rising | PASS |  |  |
| PNG.V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PNG.V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 72.1% below $10.72 | 72.1% below $10.72 | PASS |  | closing high would be 10.23 |
| PNG.V | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 72.1% below | PASS |  |  |
| PNG.V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $10.72 | $10.720000267028809 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PNG.V | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.17%, close location 0.00, OBV falling |
| PNG.V | V2 | day change of the last completed bar | down 4.2% | -4.17% | PASS |  |  |
| PNG.V | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| PNG.V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PNG.V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.07× / 0.56× | 1.07× / 0.56× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PNG.V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1285155) | 20 bars, last ('2026-11-18', 1285155) | PASS |  |  |
| QCOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $159.81 | $159.81 | PASS |  |  |
| QCOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $171.24 | $171.24 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QCOM | E3 | percent from the 21-day average | 6.7% below | 6.7% below | PASS |  |  |
| QCOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QCOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.88 | $8.88 (sr=8.8798) | PASS |  | Wilder ATR14 |
| QCOM | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| QCOM | L-ema21 | ladder row ema21: price and gap = price vs average | $171.24, -6.7% | $171.24, -6.7% | PASS |  |  |
| QCOM | L-note | "Last close $X · date" note = last completed bar | Last close $159.81 · Nov 18 | $159.81 · Nov 18 | PASS |  |  |
| QCOM | L-now | ladder price row = compared price; name = the basis label | $159.81 "After hours" | $159.81 "after hours" | PASS |  |  |
| QCOM | L-sma200 | ladder row sma200: price and gap = price vs average | $169.42, -5.7% | $169.42, -5.7% | PASS |  |  |
| QCOM | L-sma50 | ladder row sma50: price and gap = price vs average | $178.25, -10.3% | $178.25, -10.3% | PASS |  |  |
| QCOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $159.81 / entry $159.81 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QCOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QCOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.1 | 40.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QCOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -1.2% vs +11.8% | -1.2% vs 11.8% | PASS |  |  |
| QCOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QCOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.2 | 11.2 | PASS |  | Wilder, completed bars |
| QCOM | T4w | words "20 or more / below 20" | below 20 | ADX 11.2 | PASS |  |  |
| QCOM | T5 | "counted at the last close ($X, date)" = last completed bar | $159.81, Nov 18 | $159.81, Nov 18 | PASS |  |  |
| QCOM | T6 | price vs 200-day average (S1 pattern sma values) | $159.81 vs $169.42 · -5.7% | $159.81 vs $169.42 · -5.7% | PASS |  |  |
| QCOM | T6w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T7 | price vs 50-day average (S1 pattern sma values) | $159.81 vs $178.25 · -10.3% | $159.81 vs $178.25 · -10.3% | PASS |  |  |
| QCOM | T7w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.9% over 30 td | +0.9% over 30 td | PASS |  |  |
| QCOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QCOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QCOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 38.0% below $257.56 | 38.0% below $257.56 | PASS |  | closing high would be 248.74 |
| QCOM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 38.0% below | PASS |  |  |
| QCOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $257.56 | $257.5617675961248 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QCOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.12%, close location 0.14, OBV falling |
| QCOM | V2 | day change of the last completed bar | down 4.1% | -4.12% | PASS |  |  |
| QCOM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1419) | PASS |  |  |
| QCOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QCOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.69× / 0.74× | 0.69× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QCOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 9158700) | 20 bars, last ('2026-11-18', 9158700) | PASS |  |  |
| QPUX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3.19 | $3.19 | PASS |  |  |
| QPUX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $5.63 | $5.63 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QPUX | E3 | percent from the 21-day average | 43.3% below | 43.3% below | PASS |  |  |
| QPUX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QPUX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.84 | $0.84 (sr=0.8436) | PASS |  | Wilder ATR14 |
| QPUX | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| QPUX | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.8 | +3.8 | PASS |  |  |
| QPUX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +17.3 | +17.3 | PASS |  |  |
| QPUX | L-ema21 | ladder row ema21: price and gap = price vs average | $5.63, -43.3% | $5.63, -43.3% | PASS |  |  |
| QPUX | L-note | "Last close $X · date" note = last completed bar | Last close $3.19 · Nov 18 | $3.19 · Nov 18 | PASS |  |  |
| QPUX | L-now | ladder price row = compared price; name = the basis label | $3.19 "After hours" | $3.19 "after hours" | PASS |  |  |
| QPUX | L-sma200 | ladder row sma200: price and gap = price vs average | $20.22, -84.2% | $20.22, -84.2% | PASS |  |  |
| QPUX | L-sma50 | ladder row sma50: price and gap = price vs average | $8.87, -64.0% | $8.87, -64.0% | PASS |  |  |
| QPUX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3.19 / entry $3.19 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QPUX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QPUX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.8 | 28.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QPUX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -95.0% vs +11.8% | -95.0% vs 11.8% | PASS |  |  |
| QPUX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QPUX | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.3 | 38.3 | PASS |  | Wilder, completed bars |
| QPUX | T4w | words "20 or more / below 20" | 20 or more | ADX 38.3 | PASS |  |  |
| QPUX | T5 | "counted at the last close ($X, date)" = last completed bar | $3.19, Nov 18 | $3.19, Nov 18 | PASS |  |  |
| QPUX | T6 | price vs 200-day average (S1 pattern sma values) | $3.19 vs $20.22 · -84.2% | $3.19 vs $20.22 · -84.2% | PASS |  |  |
| QPUX | T6w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T7 | price vs 50-day average (S1 pattern sma values) | $3.19 vs $8.87 · -64.0% | $3.19 vs $8.87 · -64.0% | PASS |  |  |
| QPUX | T7w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -25.9% over 30 td | -26.0% over 30 td | PASS |  |  |
| QPUX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| QPUX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QPUX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 96.0% below $80.28 | 96.0% below $80.28 | PASS |  | closing high would be 79.57 |
| QPUX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 96.0% below | PASS |  |  |
| QPUX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.28 | $80.27999877929688 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QPUX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.92%, close location 0.16, OBV falling |
| QPUX | V2 | day change of the last completed bar | down 3.9% | -3.92% | PASS |  |  |
| QPUX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1556) | PASS |  |  |
| QPUX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QPUX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.15× / 0.15× | 1.15× / 0.15× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QPUX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 350468) | 20 bars, last ('2026-11-18', 350468) | PASS |  |  |
| QTUM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $123.35 | $123.35 | PASS |  |  |
| QTUM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $131.84 | $131.84 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QTUM | E3 | percent from the 21-day average | 6.4% below | 6.4% below | PASS |  |  |
| QTUM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QTUM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.63 | $4.63 (sr=4.6319) | PASS |  | Wilder ATR14 |
| QTUM | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| QTUM | L-ema21 | ladder row ema21: price and gap = price vs average | $131.84, -6.4% | $131.84, -6.4% | PASS |  |  |
| QTUM | L-note | "Last close $X · date" note = last completed bar | Last close $122.95 · Nov 18 | $122.95 · Nov 18 | PASS |  |  |
| QTUM | L-now | ladder price row = compared price; name = the basis label | $123.35 "After hours" | $123.35 "after hours" | PASS |  |  |
| QTUM | L-sma200 | ladder row sma200: price and gap = price vs average | $137.99, -10.6% | $137.99, -10.6% | PASS |  |  |
| QTUM | L-sma50 | ladder row sma50: price and gap = price vs average | $141.7, -13.0% | $141.70, -13.0% | PASS |  |  |
| QTUM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $123.35 / entry $123.35 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QTUM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QTUM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.6 | 36.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QTUM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +19.5% vs +11.8% | 19.5% vs 11.8% | PASS |  |  |
| QTUM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QTUM | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.2 | 34.2 | PASS |  | Wilder, completed bars |
| QTUM | T4w | words "20 or more / below 20" | 20 or more | ADX 34.2 | PASS |  |  |
| QTUM | T5 | "counted at the last close ($X, date)" = last completed bar | $122.95, Nov 18 | $122.95, Nov 18 | PASS |  |  |
| QTUM | T6 | price vs 200-day average (S1 pattern sma values) | $122.95 vs $137.99 · -10.9% | $122.95 vs $137.99 · -10.9% | PASS |  |  |
| QTUM | T6w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T7 | price vs 50-day average (S1 pattern sma values) | $122.95 vs $141.70 · -13.2% | $122.95 vs $141.70 · -13.2% | PASS |  |  |
| QTUM | T7w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.3% over 30 td | PASS |  |  |
| QTUM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QTUM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QTUM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 27.3% below $169.21 | 27.3% below $169.21 | PASS |  | closing high would be 167.97 |
| QTUM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 27.3% below | PASS |  |  |
| QTUM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $169.21 | $169.2079473044215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QTUM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.43%, close location 0.58, OBV falling |
| QTUM | V2 | day change of the last completed bar | up 0.4% | +0.43% | PASS |  |  |
| QTUM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QTUM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.83× / 0.11× | 0.83× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QTUM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 279100) | 20 bars, last ('2026-11-18', 279100) | PASS |  |  |
| RBOT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $27.09 | $27.09 | PASS |  |  |
| RBOT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $29.11 | $29.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RBOT.TO | E3 | percent from the 21-day average | 6.9% below | 6.9% below | PASS |  |  |
| RBOT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| RBOT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.59 | $0.58 (sr=0.585) | PASS |  | Wilder ATR14 |
| RBOT.TO | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| RBOT.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.1 | +7.1 | PASS |  |  |
| RBOT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $29.11, -6.9% | $29.11, -6.9% | PASS |  |  |
| RBOT.TO | L-now | ladder price row = compared price; name = the basis label | $27.09 "Last close" | $27.09 "last close" | PASS |  |  |
| RBOT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.26, -18.5% | $33.26, -18.5% | PASS |  |  |
| RBOT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $30.82, -12.1% | $30.82, -12.1% | PASS |  |  |
| RBOT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RBOT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.1 | 31.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RBOT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -13.4% vs +11.8% | -13.5% vs 11.8% | PASS |  |  |
| RBOT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RBOT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 36.1 | 36.1 | PASS |  | Wilder, completed bars |
| RBOT.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 36.1 | PASS |  |  |
| RBOT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $27.09 vs $33.26 · -18.6% | $27.09 vs $33.26 · -18.5% | PASS |  |  |
| RBOT.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| RBOT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $27.09 vs $30.82 · -12.1% | $27.09 vs $30.82 · -12.1% | PASS |  |  |
| RBOT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| RBOT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.1% over 30 td | -2.1% over 30 td | PASS |  |  |
| RBOT.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| RBOT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RBOT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.0% below $38.15 | 29.0% below $38.15 | PASS |  | closing high would be 38.15 |
| RBOT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.0% below | PASS |  |  |
| RBOT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.15 | $38.150001525878906 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RBOT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.21 (raw 0.2069) | PASS |  |  |
| RBOT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RBOT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1285) | 20 bars, last ('2026-11-18', 1285) | PASS |  |  |
| RTX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $197.45 | $197.45 | PASS |  |  |
| RTX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $196.31 | $196.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RTX | E3 | percent from the 21-day average | 0.6% above | 0.6% above | PASS |  |  |
| RTX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| RTX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.22 | $5.22 (sr=5.2219) | PASS |  | Wilder ATR14 |
| RTX | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| RTX | L-ema21 | ladder row ema21: price and gap = price vs average | $196.31, 0.6% | $196.31, 0.6% | PASS |  |  |
| RTX | L-note | "Last close $X · date" note = last completed bar | Last close $197.45 · Nov 18 | $197.45 · Nov 18 | PASS |  |  |
| RTX | L-now | ladder price row = compared price; name = the basis label | $197.45 "After hours" | $197.45 "after hours" | PASS |  |  |
| RTX | L-sma200 | ladder row sma200: price and gap = price vs average | $194.47, 1.5% | $194.47, 1.5% | PASS |  |  |
| RTX | L-sma50 | ladder row sma50: price and gap = price vs average | $192.66, 2.5% | $192.66, 2.5% | PASS |  |  |
| RTX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $197.45 / entry $197.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RTX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RTX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 52.2 | 52.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RTX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.7% vs +11.8% | 14.7% vs 11.8% | PASS |  |  |
| RTX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RTX | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.2 | 17.2 | PASS |  | Wilder, completed bars |
| RTX | T4w | words "20 or more / below 20" | below 20 | ADX 17.2 | PASS |  |  |
| RTX | T5 | "counted at the last close ($X, date)" = last completed bar | $197.45, Nov 18 | $197.45, Nov 18 | PASS |  |  |
| RTX | T6 | price vs 200-day average (S1 pattern sma values) | $197.45 vs $194.47 · +1.5% | $197.45 vs $194.47 · 1.5% | PASS |  |  |
| RTX | T6w | word "Above" | Above | Above | PASS |  |  |
| RTX | T7 | price vs 50-day average (S1 pattern sma values) | $197.45 vs $192.66 · +2.5% | $197.45 vs $192.66 · 2.5% | PASS |  |  |
| RTX | T7w | word "Above" | Above | Above | PASS |  |  |
| RTX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.3% over 30 td | +0.3% over 30 td | PASS |  |  |
| RTX | T8r | word "rising" | still rising | rising | PASS |  |  |
| RTX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RTX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.8% below $226.41 | 12.8% below $226.41 | PASS |  | closing high would be 225.49 |
| RTX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.8% below | PASS |  |  |
| RTX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $226.41 | $226.41 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RTX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change -0.28%, close location 0.70, OBV rising |
| RTX | V2 | day change of the last completed bar | down 0.3% | -0.28% | PASS |  |  |
| RTX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| RTX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 0.11× | 0.99× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RTX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 4805758) | 20 bars, last ('2026-11-18', 4805758) | PASS |  |  |
| RY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $272.26 | $272.26 | PASS |  |  |
| RY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $283.87 | $283.87 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RY.TO | E3 | percent from the 21-day average | 4.1% below | 4.1% below | PASS |  |  |
| RY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| RY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.94 | $4.94 (sr=4.9367) | PASS |  | Wilder ATR14 |
| RY.TO | E5 | distance in normal day-moves | 2.4 | 2.4 | PASS |  | gauge dot note uses the same number:  · 2.4 day-moves below |
| RY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $283.87, -4.1% | $283.87, -4.1% | PASS |  |  |
| RY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $272.26 · Nov 18 | $272.26 · Nov 18 | PASS |  |  |
| RY.TO | L-now | ladder price row = compared price; name = the basis label | $272.26 "After hours" | $272.26 "after hours" | PASS |  |  |
| RY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $263.53, 3.3% | $263.53, 3.3% | PASS |  |  |
| RY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $281.8, -3.4% | $281.80, -3.4% | PASS |  |  |
| RY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $272.26 / entry $272.26 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.6 | 35.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +34.1% vs +11.8% | 34.1% vs 11.8% | PASS |  |  |
| RY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.2 | 15.2 | PASS |  | Wilder, completed bars |
| RY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.2 | PASS |  |  |
| RY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $272.26, Nov 18 | $272.26, Nov 18 | PASS |  |  |
| RY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $272.26 vs $263.53 · +3.3% | $272.26 vs $263.53 · 3.3% | PASS |  |  |
| RY.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| RY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $272.26 vs $281.80 · -3.4% | $272.26 vs $281.80 · -3.4% | PASS |  |  |
| RY.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| RY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| RY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| RY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.0% below $302.65 | 10.0% below $302.65 | PASS |  | closing high would be 302.02 |
| RY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.0% below | PASS |  |  |
| RY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.65 | $302.6498839841861 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.11%, close location 0.02, OBV falling |
| RY.TO | V2 | day change of the last completed bar | down 3.1% | -3.11% | PASS |  |  |
| RY.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0188) | PASS |  |  |
| RY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.71× / 1.72× | 0.71× / 1.71× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 2350092) | 20 bars, last ('2026-11-18', 2350092) | PASS |  |  |
| SGRD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.96 | $17.96 | PASS |  |  |
| SGRD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.57 | $18.57 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SGRD.TO | E3 | percent from the 21-day average | 3.3% below | 3.3% below | PASS |  |  |
| SGRD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SGRD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.37 | $0.37 (sr=0.3692) | PASS |  | Wilder ATR14 |
| SGRD.TO | E5 | distance in normal day-moves | 1.7 | 1.7 | PASS |  | gauge dot note uses the same number:  · 1.7 day-moves below |
| SGRD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $18.57, -3.3% | $18.57, -3.3% | PASS |  |  |
| SGRD.TO | L-now | ladder price row = compared price; name = the basis label | $17.96 "Last close" | $17.96 "last close" | PASS |  |  |
| SGRD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $19.48, -7.8% | $19.48, -7.8% | PASS |  |  |
| SGRD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.5 | 40.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SGRD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.3 | 27.3 | PASS |  | Wilder, completed bars |
| SGRD.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.3 | PASS |  |  |
| SGRD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change 0.06%, close location 0.29, OBV falling |
| SGRD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SGRD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.51× / 0.03× | 0.51× / 0.03× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SGRD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 4590) | 20 bars, last ('2026-11-18', 4590) | PASS |  |  |
| SMH | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.2 | 35.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SMH | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +38.3% vs +11.8% | 38.3% vs 11.8% | PASS |  |  |
| SMH | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SNDK.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $18.74 | $18.74 | PASS |  |  |
| SNDK.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $25.06 | $25.06 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SNDK.TO | E3 | percent from the 21-day average | 25.2% below | 25.2% below | PASS |  |  |
| SNDK.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SNDK.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.40 | $2.40 (sr=2.3982) | PASS |  | Wilder ATR14 |
| SNDK.TO | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| SNDK.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.6 | +3.6 | PASS |  |  |
| SNDK.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $25.06, -25.2% | $25.06, -25.2% | PASS |  |  |
| SNDK.TO | L-now | ladder price row = compared price; name = the basis label | $18.74 "Last close" | $18.74 "last close" | PASS |  |  |
| SNDK.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $33.71, -44.4% | $33.71, -44.4% | PASS |  |  |
| SNDK.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.9 | 29.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SNDK.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.1 | 40.1 | PASS |  | Wilder, completed bars |
| SNDK.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 40.1 | PASS |  |  |
| SNDK.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.80%, close location 0.38, OBV falling |
| SNDK.TO | V2 | day change of the last completed bar | down 2.8% | -2.80% | PASS |  |  |
| SNDK.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SNDK.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.10× / 0.22× | 1.10× / 0.22× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SNDK.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1387955) | 20 bars, last ('2026-11-18', 1387955) | PASS |  |  |
| SO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $94.41 | $94.41 | PASS |  |  |
| SO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $92.1 | $92.10 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SO | E3 | percent from the 21-day average | 2.5% above | 2.5% above | PASS |  |  |
| SO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.78 | $1.78 (sr=1.7759) | PASS |  | Wilder ATR14 |
| SO | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves above |
| SO | L-ema21 | ladder row ema21: price and gap = price vs average | $92.1, 2.5% | $92.10, 2.5% | PASS |  |  |
| SO | L-note | "Last close $X · date" note = last completed bar | Last close $94.41 · Nov 18 | $94.41 · Nov 18 | PASS |  |  |
| SO | L-now | ladder price row = compared price; name = the basis label | $94.41 "After hours" | $94.41 "after hours" | PASS |  |  |
| SO | L-sma200 | ladder row sma200: price and gap = price vs average | $91.2, 3.5% | $91.20, 3.5% | PASS |  |  |
| SO | L-sma50 | ladder row sma50: price and gap = price vs average | $88.35, 6.9% | $88.35, 6.9% | PASS |  |  |
| SO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $94.41 / entry $94.41 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 62.1 | 62.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +7.5% vs +11.8% | 7.5% vs 11.8% | PASS |  |  |
| SO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.7 | 27.7 | PASS |  | Wilder, completed bars |
| SO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.7 | PASS |  |  |
| SO | T5 | "counted at the last close ($X, date)" = last completed bar | $94.41, Nov 18 | $94.41, Nov 18 | PASS |  |  |
| SO | T6 | price vs 200-day average (S1 pattern sma values) | $94.41 vs $91.20 · +3.5% | $94.41 vs $91.20 · 3.5% | PASS |  |  |
| SO | T6w | word "Above" | Above | Above | PASS |  |  |
| SO | T7 | price vs 50-day average (S1 pattern sma values) | $94.41 vs $88.35 · +6.9% | $94.41 vs $88.35 · 6.9% | PASS |  |  |
| SO | T7w | word "Above" | Above | Above | PASS |  |  |
| SO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.0% over 30 td | +1.0% over 30 td | PASS |  |  |
| SO | T8r | word "rising" | still rising | rising | PASS |  |  |
| SO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 3.3% below $97.65 | 3.3% below $97.65 | PASS |  | closing high would be 96.70 |
| SO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 3.3% below | PASS |  |  |
| SO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $97.65 | $97.64764917949712 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 0.87%, close location 0.88, OBV rising |
| SO | V2 | day change of the last completed bar | up 0.9% | +0.87% | PASS |  |  |
| SO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.88 (raw 0.8767) | PASS |  |  |
| SO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| SO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.00× / 0.46× | 1.00× / 0.46× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 7230100) | 20 bars, last ('2026-11-18', 7230100) | PASS |  |  |
| SOXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $49.26 | $49.26 | PASS |  |  |
| SOXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $71.03 | $71.03 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL | E3 | percent from the 21-day average | 30.7% below | 30.7% below | PASS |  |  |
| SOXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $11.75 | $11.75 (sr=11.7451) | PASS |  | Wilder ATR14 |
| SOXL | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| SOXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.5 | +4.5 | PASS |  |  |
| SOXL | L-ema21 | ladder row ema21: price and gap = price vs average | $71.03, -30.7% | $71.03, -30.7% | PASS |  |  |
| SOXL | L-note | "Last close $X · date" note = last completed bar | Last close $49.26 · Nov 18 | $49.26 · Nov 18 | PASS |  |  |
| SOXL | L-now | ladder price row = compared price; name = the basis label | $49.26 "After hours" | $49.26 "after hours" | PASS |  |  |
| SOXL | L-sma200 | ladder row sma200: price and gap = price vs average | $123.8, -60.2% | $123.80, -60.2% | PASS |  |  |
| SOXL | L-sma50 | ladder row sma50: price and gap = price vs average | $106, -53.5% | $106.00, -53.5% | PASS |  |  |
| SOXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $49.26 / entry $49.26 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.5 | 34.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +43.5% vs +11.8% | 43.5% vs 11.8% | PASS |  |  |
| SOXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.0 | 35.0 | PASS |  | Wilder, completed bars |
| SOXL | T4w | words "20 or more / below 20" | 20 or more | ADX 35.0 | PASS |  |  |
| SOXL | T5 | "counted at the last close ($X, date)" = last completed bar | $49.26, Nov 18 | $49.26, Nov 18 | PASS |  |  |
| SOXL | T6 | price vs 200-day average (S1 pattern sma values) | $49.26 vs $123.80 · -60.2% | $49.26 vs $123.80 · -60.2% | PASS |  |  |
| SOXL | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T7 | price vs 50-day average (S1 pattern sma values) | $49.26 vs $106.00 · -53.5% | $49.26 vs $106.00 · -53.5% | PASS |  |  |
| SOXL | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.8% over 30 td | +3.8% over 30 td | PASS |  |  |
| SOXL | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 83.7% below $301.80 | 83.7% below $301.80 | PASS |  | closing high would be 300.57 |
| SOXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 83.7% below | PASS |  |  |
| SOXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $301.80 | $301.8021115035658 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.39%, close location 0.51, OBV falling |
| SOXL | V2 | day change of the last completed bar | up 0.4% | +0.39% | PASS |  |  |
| SOXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.63× / 0.02× | 1.63× / 0.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 199975002) | 20 bars, last ('2026-11-18', 199975002) | PASS |  |  |
| SOXL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.63, OBV falling | condition true | PASS |  |  |
| SOXL.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.43 | $12.43 | PASS |  |  |
| SOXL.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $17.82 | $17.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL.NE | E3 | percent from the 21-day average | 30.2% below | 30.2% below | PASS |  |  |
| SOXL.NE | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SOXL.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.86 | $1.86 (sr=1.861) | PASS |  | Wilder ATR14 |
| SOXL.NE | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| SOXL.NE | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.6 | +4.6 | PASS |  |  |
| SOXL.NE | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.0 | +7.0 | PASS |  |  |
| SOXL.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $17.82, -30.2% | $17.82, -30.2% | PASS |  |  |
| SOXL.NE | L-now | ladder price row = compared price; name = the basis label | $12.43 "Last close" | $12.43 "last close" | PASS |  |  |
| SOXL.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.85, -59.7% | $30.85, -59.7% | PASS |  |  |
| SOXL.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $26.38, -52.9% | $26.38, -52.9% | PASS |  |  |
| SOXL.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.8 | 34.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +31.1% vs +11.8% | 31.1% vs 11.8% | PASS |  |  |
| SOXL.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.9 | 26.9 | PASS |  | Wilder, completed bars |
| SOXL.NE | T4w | words "20 or more / below 20" | 20 or more | ADX 26.9 | PASS |  |  |
| SOXL.NE | T6 | price vs 200-day average (S1 pattern sma values) | $12.43 vs $30.85 · -59.7% | $12.43 vs $30.85 · -59.7% | PASS |  |  |
| SOXL.NE | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T7 | price vs 50-day average (S1 pattern sma values) | $12.43 vs $26.38 · -52.9% | $12.43 vs $26.38 · -52.9% | PASS |  |  |
| SOXL.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.8% over 30 td | +3.8% over 30 td | PASS |  |  |
| SOXL.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 83.3% below $74.21 | 83.3% below $74.21 | PASS |  | closing high would be 74.21 |
| SOXL.NE | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 83.3% below | PASS |  |  |
| SOXL.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $74.21 | $74.21369934082031 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL.NE | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 49 of 50 days empty | 49 of 50 days empty | PASS |  |  |
| SOXX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $141.85 | $141.85 | PASS |  |  |
| SOXX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $153.43 | $153.43 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXX | E3 | percent from the 21-day average | 7.5% below | 7.5% below | PASS |  |  |
| SOXX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.17 | $8.17 (sr=8.1744) | PASS |  | Wilder ATR14 |
| SOXX | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| SOXX | L-ema21 | ladder row ema21: price and gap = price vs average | $153.43, -7.5% | $153.43, -7.5% | PASS |  |  |
| SOXX | L-note | "Last close $X · date" note = last completed bar | Last close $141.85 · Nov 18 | $141.85 · Nov 18 | PASS |  |  |
| SOXX | L-now | ladder price row = compared price; name = the basis label | $141.85 "After hours" | $141.85 "after hours" | PASS |  |  |
| SOXX | L-sma200 | ladder row sma200: price and gap = price vs average | $160.65, -11.7% | $160.65, -11.7% | PASS |  |  |
| SOXX | L-sma50 | ladder row sma50: price and gap = price vs average | $169.85, -16.5% | $169.85, -16.5% | PASS |  |  |
| SOXX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $141.85 / entry $141.85 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.3 | 38.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +54.1% vs +11.8% | 54.1% vs 11.8% | PASS |  |  |
| SOXX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXX | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.1 | 32.1 | PASS |  | Wilder, completed bars |
| SOXX | T4w | words "20 or more / below 20" | 20 or more | ADX 32.1 | PASS |  |  |
| SOXX | T5 | "counted at the last close ($X, date)" = last completed bar | $141.85, Nov 18 | $141.85, Nov 18 | PASS |  |  |
| SOXX | T6 | price vs 200-day average (S1 pattern sma values) | $141.85 vs $160.65 · -11.7% | $141.85 vs $160.65 · -11.7% | PASS |  |  |
| SOXX | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T7 | price vs 50-day average (S1 pattern sma values) | $141.85 vs $169.85 · -16.5% | $141.85 vs $169.85 · -16.5% | PASS |  |  |
| SOXX | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.0% over 30 td | +5.0% over 30 td | PASS |  |  |
| SOXX | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.1% below $218.51 | 35.1% below $218.51 | PASS |  | closing high would be 218.19 |
| SOXX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.1% below | PASS |  |  |
| SOXX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $218.51 | $218.50713476135667 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.28%, close location 0.54, OBV falling |
| SOXX | V2 | day change of the last completed bar | up 0.3% | +0.28% | PASS |  |  |
| SOXX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.10× / 0.05× | 1.10× / 0.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 32974002) | 20 bars, last ('2026-11-18', 32974002) | PASS |  |  |
| SPCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $9.44 | $9.44 | PASS |  |  |
| SPCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $12.82 | $12.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SPCL | E3 | percent from the 21-day average | 26.3% below | 26.3% below | PASS |  |  |
| SPCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SPCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.66 | $1.66 (sr=1.6602) | PASS |  | Wilder ATR14 |
| SPCL | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| SPCL | L-ema21 | ladder row ema21: price and gap = price vs average | $12.82, -26.3% | $12.82, -26.3% | PASS |  |  |
| SPCL | L-note | "Last close $X · date" note = last completed bar | Last close $9.44 · Nov 18 | $9.44 · Nov 18 | PASS |  |  |
| SPCL | L-now | ladder price row = compared price; name = the basis label | $9.44 "After hours" | $9.44 "after hours" | PASS |  |  |
| SPCL | L-sma50 | ladder row sma50: price and gap = price vs average | $17.13, -44.9% | $17.13, -44.9% | PASS |  |  |
| SPCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $9.44 / entry $9.44 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SPCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.4 | 35.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SPCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.1 | 32.1 | PASS |  | Wilder, completed bars |
| SPCL | T4w | words "20 or more / below 20" | 20 or more | ADX 32.1 | PASS |  |  |
| SPCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.81%, close location 0.05, OBV falling |
| SPCL | V2 | day change of the last completed bar | down 6.8% | -6.81% | PASS |  |  |
| SPCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0521) | PASS |  |  |
| SPCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SPCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.55× / 0.39× | 0.55× / 0.39× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SPCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 20583) | 20 bars, last ('2026-11-18', 20583) | PASS |  |  |
| TSLA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $383.72 | $383.72 | PASS |  |  |
| TSLA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $382.44 | $382.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLA | E3 | percent from the 21-day average | 0.3% above | 0.3% above | PASS |  |  |
| TSLA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSLA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $15.63 | $15.63 (sr=15.6339) | PASS |  | Wilder ATR14 |
| TSLA | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| TSLA | L-ema21 | ladder row ema21: price and gap = price vs average | $382.44, 0.3% | $382.44, 0.3% | PASS |  |  |
| TSLA | L-note | "Last close $X · date" note = last completed bar | Last close $383.72 · Nov 18 | $383.72 · Nov 18 | PASS |  |  |
| TSLA | L-now | ladder price row = compared price; name = the basis label | $383.72 "After hours" | $383.72 "after hours" | PASS |  |  |
| TSLA | L-sma200 | ladder row sma200: price and gap = price vs average | $382.08, 0.4% | $382.08, 0.4% | PASS |  |  |
| TSLA | L-sma50 | ladder row sma50: price and gap = price vs average | $375.81, 2.1% | $375.81, 2.1% | PASS |  |  |
| TSLA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $383.72 / entry $383.72 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 51.1 | 51.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.4% vs +11.8% | -4.4% vs 11.8% | PASS |  |  |
| TSLA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLA | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.5 | 11.5 | PASS |  | Wilder, completed bars |
| TSLA | T4w | words "20 or more / below 20" | below 20 | ADX 11.5 | PASS |  |  |
| TSLA | T5 | "counted at the last close ($X, date)" = last completed bar | $383.72, Nov 18 | $383.72, Nov 18 | PASS |  |  |
| TSLA | T6 | price vs 200-day average (S1 pattern sma values) | $383.72 vs $382.08 · +0.4% | $383.72 vs $382.08 · 0.4% | PASS |  |  |
| TSLA | T6w | word "Above" | Above | Above | PASS |  |  |
| TSLA | T7 | price vs 50-day average (S1 pattern sma values) | $383.72 vs $375.81 · +2.1% | $383.72 vs $375.81 · 2.1% | PASS |  |  |
| TSLA | T7w | word "Above" | Above | Above | PASS |  |  |
| TSLA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.4% over 30 td | -2.4% over 30 td | PASS |  |  |
| TSLA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 23.1% below $498.83 | 23.1% below $498.83 | PASS |  | closing high would be 489.88 |
| TSLA | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 23.1% below | PASS |  |  |
| TSLA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $498.83 | $498.82999 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.95%, close location 0.49, OBV rising |
| TSLA | V2 | day change of the last completed bar | up 0.9% | +0.95% | PASS |  |  |
| TSLA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| TSLA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.74× / 0.23× | 0.74× / 0.23× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 26666127) | 20 bars, last ('2026-11-18', 26666127) | PASS |  |  |
| TSLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $10.17 | $10.17 | PASS |  |  |
| TSLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $10.11 | $10.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLL | E3 | percent from the 21-day average | 0.6% above | 0.6% above | PASS |  |  |
| TSLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.82 | $0.82 (sr=0.8245) | PASS |  | Wilder ATR14 |
| TSLL | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| TSLL | L-ema21 | ladder row ema21: price and gap = price vs average | $10.11, 0.6% | $10.11, 0.6% | PASS |  |  |
| TSLL | L-note | "Last close $X · date" note = last completed bar | Last close $10.00 · Nov 18 | $10.00 · Nov 18 | PASS |  |  |
| TSLL | L-now | ladder price row = compared price; name = the basis label | $10.17 "After hours" | $10.17 "after hours" | PASS |  |  |
| TSLL | L-sma200 | ladder row sma200: price and gap = price vs average | $11.7, -13.1% | $11.70, -13.1% | PASS |  |  |
| TSLL | L-sma50 | ladder row sma50: price and gap = price vs average | $9.97, 2.0% | $9.97, 2.0% | PASS |  |  |
| TSLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $10.17 / entry $10.17 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.2 | 49.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -35.0% vs +11.8% | -35.0% vs 11.8% | PASS |  |  |
| TSLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.2 | 11.2 | PASS |  | Wilder, completed bars |
| TSLL | T4w | words "20 or more / below 20" | below 20 | ADX 11.2 | PASS |  |  |
| TSLL | T5 | "counted at the last close ($X, date)" = last completed bar | $10.00, Nov 18 | $10.00, Nov 18 | PASS |  |  |
| TSLL | T6 | price vs 200-day average (S1 pattern sma values) | $10.00 vs $11.70 · -14.5% | $10.00 vs $11.70 · -14.5% | PASS |  |  |
| TSLL | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T7 | price vs 50-day average (S1 pattern sma values) | $10.00 vs $9.97 · +0.3% | $10.00 vs $9.97 · 0.3% | PASS |  |  |
| TSLL | T7w | word "Above" | Above | Above | PASS |  |  |
| TSLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -9.4% over 30 td | -9.4% over 30 td | PASS |  |  |
| TSLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 56.7% below $23.10 | 56.7% below $23.10 | PASS |  | closing high would be 22.41 |
| TSLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 56.7% below | PASS |  |  |
| TSLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $23.10 | $23.098129965756442 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 1.94%, close location 0.48, OBV rising |
| TSLL | V2 | day change of the last completed bar | up 1.9% | +1.94% | PASS |  |  |
| TSLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| TSLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.60× / 0.24× | 0.60× / 0.23× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 32737700) | 20 bars, last ('2026-11-18', 32737700) | PASS |  |  |
| TSM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $362.62 | $362.62 | PASS |  |  |
| TSM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $397.99 | $397.99 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSM | E3 | percent from the 21-day average | 8.9% below | 8.9% below | PASS |  |  |
| TSM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.50 | $17.50 (sr=17.4992) | PASS |  | Wilder ATR14 |
| TSM | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| TSM | L-ema21 | ladder row ema21: price and gap = price vs average | $397.99, -8.9% | $397.99, -8.9% | PASS |  |  |
| TSM | L-note | "Last close $X · date" note = last completed bar | Last close $362.62 · Nov 18 | $362.62 · Nov 18 | PASS |  |  |
| TSM | L-now | ladder price row = compared price; name = the basis label | $362.62 "After hours" | $362.62 "after hours" | PASS |  |  |
| TSM | L-sma200 | ladder row sma200: price and gap = price vs average | $402.15, -9.8% | $402.15, -9.8% | PASS |  |  |
| TSM | L-sma50 | ladder row sma50: price and gap = price vs average | $425.87, -14.9% | $425.87, -14.9% | PASS |  |  |
| TSM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $362.62 / entry $362.62 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.8 | 36.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +31.9% vs +11.8% | 31.9% vs 11.8% | PASS |  |  |
| TSM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSM | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.1 | 32.1 | PASS |  | Wilder, completed bars |
| TSM | T4w | words "20 or more / below 20" | 20 or more | ADX 32.1 | PASS |  |  |
| TSM | T5 | "counted at the last close ($X, date)" = last completed bar | $362.62, Nov 18 | $362.62, Nov 18 | PASS |  |  |
| TSM | T6 | price vs 200-day average (S1 pattern sma values) | $362.62 vs $402.15 · -9.8% | $362.62 vs $402.15 · -9.8% | PASS |  |  |
| TSM | T6w | word "Below" | Below | Below | PASS |  |  |
| TSM | T7 | price vs 50-day average (S1 pattern sma values) | $362.62 vs $425.87 · -14.9% | $362.62 vs $425.87 · -14.9% | PASS |  |  |
| TSM | T7w | word "Below" | Below | Below | PASS |  |  |
| TSM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.5% over 30 td | +3.5% over 30 td | PASS |  |  |
| TSM | T8r | word "rising" | still rising | rising | PASS |  |  |
| TSM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 25.6% below $487.47 | 25.6% below $487.47 | PASS |  | closing high would be 485.80 |
| TSM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 25.6% below | PASS |  |  |
| TSM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $487.47 | $487.47 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.81%, close location 0.48, OBV falling |
| TSM | V2 | day change of the last completed bar | up 0.8% | +0.81% | PASS |  |  |
| TSM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.94× / 0.17× | 0.94× / 0.17× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 11982497) | 20 bars, last ('2026-11-18', 11982497) | PASS |  |  |
| UBOT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $15.07 | $15.07 | PASS |  |  |
| UBOT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $17.52 | $17.52 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UBOT | E3 | percent from the 21-day average | 14.0% below | 14.0% below | PASS |  |  |
| UBOT | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| UBOT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.80 | $0.80 (sr=0.7964) | PASS |  | Wilder ATR14 |
| UBOT | E5 | distance in normal day-moves | 3.1 | 3.1 | PASS |  | gauge dot note uses the same number:  · 3.1 day-moves below |
| UBOT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.9 | +7.9 | PASS |  |  |
| UBOT | L-ema21 | ladder row ema21: price and gap = price vs average | $17.52, -14.0% | $17.52, -14.0% | PASS |  |  |
| UBOT | L-now | ladder price row = compared price; name = the basis label | $15.07 "Last close" | $15.07 "last close" | PASS |  |  |
| UBOT | L-sma200 | ladder row sma200: price and gap = price vs average | $23.8, -36.7% | $23.80, -36.7% | PASS |  |  |
| UBOT | L-sma50 | ladder row sma50: price and gap = price vs average | $19.85, -24.1% | $19.85, -24.1% | PASS |  |  |
| UBOT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UBOT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.1 | 31.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UBOT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -31.7% vs +11.8% | -31.7% vs 11.8% | PASS |  |  |
| UBOT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UBOT | T4 | ADX 14 (S1 /api/sr meta.adx) | 39.1 | 39.1 | PASS |  | Wilder, completed bars |
| UBOT | T4w | words "20 or more / below 20" | 20 or more | ADX 39.1 | PASS |  |  |
| UBOT | T6 | price vs 200-day average (S1 pattern sma values) | $15.07 vs $23.80 · -36.7% | $15.07 vs $23.80 · -36.7% | PASS |  |  |
| UBOT | T6w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T7 | price vs 50-day average (S1 pattern sma values) | $15.07 vs $19.85 · -24.1% | $15.07 vs $19.85 · -24.1% | PASS |  |  |
| UBOT | T7w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.1% over 30 td | -5.1% over 30 td | PASS |  |  |
| UBOT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UBOT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UBOT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 52.8% below $31.91 | 52.8% below $31.91 | PASS |  | closing high would be 31.87 |
| UBOT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 52.8% below | PASS |  |  |
| UBOT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $31.91 | $31.90624 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UBOT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change 0.20%, close location 0.13, OBV falling |
| UBOT | V2 | day change of the last completed bar | up 0.2% | +0.20% | PASS |  |  |
| UBOT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.13 (raw 0.1250) | PASS |  |  |
| UBOT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UBOT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.75× / 0.04× | 0.75× / 0.04× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UBOT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 11987) | 20 bars, last ('2026-11-18', 11987) | PASS |  |  |
| UFO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $38.81 | $38.81 | PASS |  |  |
| UFO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.39 | $40.39 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UFO | E3 | percent from the 21-day average | 3.9% below | 3.9% below | PASS |  |  |
| UFO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| UFO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.33 | $1.33 (sr=1.3286) | PASS |  | Wilder ATR14 |
| UFO | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| UFO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.0 | +5.0 | PASS |  |  |
| UFO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.39, -3.9% | $40.39, -3.9% | PASS |  |  |
| UFO | L-note | "Last close $X · date" note = last completed bar | Last close $39.09 · Nov 18 | $39.09 · Nov 18 | PASS |  |  |
| UFO | L-now | ladder price row = compared price; name = the basis label | $38.81 "After hours" | $38.81 "after hours" | PASS |  |  |
| UFO | L-sma200 | ladder row sma200: price and gap = price vs average | $46.96, -17.4% | $46.96, -17.4% | PASS |  |  |
| UFO | L-sma50 | ladder row sma50: price and gap = price vs average | $41.48, -6.4% | $41.48, -6.4% | PASS |  |  |
| UFO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $38.81 / entry $38.81 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| UFO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UFO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.6 | 42.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UFO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +20.1% vs +11.8% | 20.1% vs 11.8% | PASS |  |  |
| UFO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UFO | T4 | ADX 14 (S1 /api/sr meta.adx) | 24.8 | 24.8 | PASS |  | Wilder, completed bars |
| UFO | T4w | words "20 or more / below 20" | 20 or more | ADX 24.8 | PASS |  |  |
| UFO | T5 | "counted at the last close ($X, date)" = last completed bar | $39.09, Nov 18 | $39.09, Nov 18 | PASS |  |  |
| UFO | T6 | price vs 200-day average (S1 pattern sma values) | $39.09 vs $46.96 · -16.8% | $39.09 vs $46.96 · -16.8% | PASS |  |  |
| UFO | T6w | word "Below" | Below | Below | PASS |  |  |
| UFO | T7 | price vs 50-day average (S1 pattern sma values) | $39.09 vs $41.48 · -5.8% | $39.09 vs $41.48 · -5.8% | PASS |  |  |
| UFO | T7w | word "Below" | Below | Below | PASS |  |  |
| UFO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.0% over 30 td | -1.0% over 30 td | PASS |  |  |
| UFO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UFO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UFO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 42.6% below $68.12 | 42.6% below $68.12 | PASS |  | closing high would be 67.71 |
| UFO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 42.6% below | PASS |  |  |
| UFO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $68.12 | $68.11999548611959 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UFO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.53%, close location 0.21, OBV falling |
| UFO | V2 | day change of the last completed bar | down 0.5% | -0.53% | PASS |  |  |
| UFO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.21 (raw 0.2073) | PASS |  |  |
| UFO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UFO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.28× / 0.16× | 0.28× / 0.16× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UFO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 70500) | 20 bars, last ('2026-11-18', 70500) | PASS |  |  |
| V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 54.8 | 54.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.9% vs +11.8% | 28.9% vs 11.8% | PASS |  |  |
| V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VFV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $186.20 | $186.20 | PASS |  |  |
| VFV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $189.48 | $189.48 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VFV.TO | E3 | percent from the 21-day average | 1.7% below | 1.7% below | PASS |  |  |
| VFV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| VFV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.80 | $2.80 (sr=2.8036) | PASS |  | Wilder ATR14 |
| VFV.TO | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| VFV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $189.48, -1.7% | $189.48, -1.7% | PASS |  |  |
| VFV.TO | L-now | ladder price row = compared price; name = the basis label | $186.2 "Last close" | $186.20 "last close" | PASS |  |  |
| VFV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $180.78, 3.0% | $180.78, 3.0% | PASS |  |  |
| VFV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $191.21, -2.6% | $191.21, -2.6% | PASS |  |  |
| VFV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VFV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.0 | 42.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VFV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.4% vs +11.8% | 14.4% vs 11.8% | PASS |  |  |
| VFV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VFV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.6 | 19.6 | PASS |  | Wilder, completed bars |
| VFV.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.6 | PASS |  |  |
| VFV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $186.20 vs $180.78 · +3.0% | $186.20 vs $180.78 · 3.0% | PASS |  |  |
| VFV.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| VFV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $186.20 vs $191.21 · -2.6% | $186.20 vs $191.21 · -2.6% | PASS |  |  |
| VFV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| VFV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.0% over 30 td | +2.0% over 30 td | PASS |  |  |
| VFV.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| VFV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VFV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.9% below $197.83 | 5.9% below $197.83 | PASS |  | closing high would be 197.56 |
| VFV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.9% below | PASS |  |  |
| VFV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $197.83 | $197.8300018310547 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VFV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 1 down, 2 flat | 3 signals, 0 up, 1 down, 2 flat | PASS |  | change 0.03%, close location 0.44, OBV falling |
| VFV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| VFV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.78× / 0.02× | 0.78× / 0.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VFV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 246940) | 20 bars, last ('2026-11-18', 246940) | PASS |  |  |
| VRT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.7 | 41.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VRT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.4% vs +11.8% | 14.4% vs 11.8% | PASS |  |  |
| VRT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WDC.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.44 | $17.44 | PASS |  |  |
| WDC.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $19.51 | $19.51 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WDC.TO | E3 | percent from the 21-day average | 10.6% below | 10.6% below | PASS |  |  |
| WDC.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| WDC.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.47 | $1.47 (sr=1.471) | PASS |  | Wilder ATR14 |
| WDC.TO | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| WDC.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $19.51, -10.6% | $19.51, -10.6% | PASS |  |  |
| WDC.TO | L-now | ladder price row = compared price; name = the basis label | $17.44 "Last close" | $17.44 "last close" | PASS |  |  |
| WDC.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $23.21, -24.9% | $23.21, -24.9% | PASS |  |  |
| WDC.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.0 | 38.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WDC.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.2 | 34.1 | PASS |  | Wilder, completed bars |
| WDC.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 34.1 | PASS |  |  |
| WDC.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 1.81%, close location 0.60, OBV falling |
| WDC.TO | V2 | day change of the last completed bar | up 1.8% | +1.81% | PASS |  |  |
| WDC.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| WDC.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.62× / 0.21× | 0.62× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WDC.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 99828) | 20 bars, last ('2026-11-18', 99828) | PASS |  |  |
| WELL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $247.25 | $247.25 | PASS |  |  |
| WELL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $241.38 | $241.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WELL | E3 | percent from the 21-day average | 2.4% above | 2.4% above | PASS |  |  |
| WELL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| WELL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.33 | $5.33 (sr=5.3296) | PASS |  | Wilder ATR14 |
| WELL | E5 | distance in normal day-moves | 1.1 | 1.1 | PASS |  | gauge dot note uses the same number:  · 1.1 day-moves above |
| WELL | L-ema21 | ladder row ema21: price and gap = price vs average | $241.38, 2.4% | $241.38, 2.4% | PASS |  |  |
| WELL | L-note | "Last close $X · date" note = last completed bar | Last close $247.25 · Nov 18 | $247.25 · Nov 18 | PASS |  |  |
| WELL | L-now | ladder price row = compared price; name = the basis label | $247.25 "After hours" | $247.25 "after hours" | PASS |  |  |
| WELL | L-sma200 | ladder row sma200: price and gap = price vs average | $220.78, 12.0% | $220.78, 12.0% | PASS |  |  |
| WELL | L-sma50 | ladder row sma50: price and gap = price vs average | $234.41, 5.5% | $234.41, 5.5% | PASS |  |  |
| WELL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $247.25 / entry $247.25 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| WELL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WELL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 62.5 | 62.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WELL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +26.5% vs +11.8% | 26.5% vs 11.8% | PASS |  |  |
| WELL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WELL | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.2 | 14.2 | PASS |  | Wilder, completed bars |
| WELL | T4w | words "20 or more / below 20" | below 20 | ADX 14.2 | PASS |  |  |
| WELL | T5 | "counted at the last close ($X, date)" = last completed bar | $247.25, Nov 18 | $247.25, Nov 18 | PASS |  |  |
| WELL | T6 | price vs 200-day average (S1 pattern sma values) | $247.25 vs $220.78 · +12.0% | $247.25 vs $220.78 · 12.0% | PASS |  |  |
| WELL | T6w | word "Above" | Above | Above | PASS |  |  |
| WELL | T7 | price vs 50-day average (S1 pattern sma values) | $247.25 vs $234.41 · +5.5% | $247.25 vs $234.41 · 5.5% | PASS |  |  |
| WELL | T7w | word "Above" | Above | Above | PASS |  |  |
| WELL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.8% over 30 td | +3.8% over 30 td | PASS |  |  |
| WELL | T8r | word "rising" | still rising | rising | PASS |  |  |
| WELL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WELL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.4% below $253.37 | 2.4% below $253.37 | PASS |  | closing high would be 250.26 |
| WELL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.4% below | PASS |  |  |
| WELL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $253.37 | $253.36654979575871 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WELL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 3 up, 0 down, 0 flat | 3 signals, 3 up, 0 down, 0 flat | PASS |  | change 0.61%, close location 0.84, OBV rising |
| WELL | V2 | day change of the last completed bar | up 0.6% | +0.61% | PASS |  |  |
| WELL | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.84 (raw 0.8352) | PASS |  |  |
| WELL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| WELL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.50× / 0.28× | 1.50× / 0.28× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WELL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 4275000) | 20 bars, last ('2026-11-18', 4275000) | PASS |  |  |
| WMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 65.2 | 65.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +24.9% vs +11.8% | 24.9% vs 11.8% | PASS |  |  |
| WMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XCHP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $105.84 | $105.84 | PASS |  |  |
| XCHP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.22 | $113.22 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XCHP.TO | E3 | percent from the 21-day average | 6.5% below | 6.5% below | PASS |  |  |
| XCHP.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XCHP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.06 | $6.06 (sr=6.0564) | PASS |  | Wilder ATR14 |
| XCHP.TO | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| XCHP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $113.22, -6.5% | $113.22, -6.5% | PASS |  |  |
| XCHP.TO | L-now | ladder price row = compared price; name = the basis label | $105.84 "Last close" | $105.84 "last close" | PASS |  |  |
| XCHP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $116.69, -9.3% | $116.69, -9.3% | PASS |  |  |
| XCHP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $124.76, -15.2% | $124.76, -15.2% | PASS |  |  |
| XCHP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XCHP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.1 | 40.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XCHP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +57.4% vs +11.8% | 57.4% vs 11.8% | PASS |  |  |
| XCHP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XCHP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.7 | 32.7 | PASS |  | Wilder, completed bars |
| XCHP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.7 | PASS |  |  |
| XCHP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $105.84 vs $116.69 · -9.3% | $105.84 vs $116.69 · -9.3% | PASS |  |  |
| XCHP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $105.84 vs $124.76 · -15.2% | $105.84 vs $124.76 · -15.2% | PASS |  |  |
| XCHP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.4% over 30 td | +5.4% over 30 td | PASS |  |  |
| XCHP.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XCHP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XCHP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.4% below $161.26 | 34.4% below $161.26 | PASS |  | closing high would be 160.97 |
| XCHP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.4% below | PASS |  |  |
| XCHP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $161.26 | $161.25523669513825 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XCHP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.42%, close location 0.55, OBV falling |
| XCHP.TO | V2 | day change of the last completed bar | up 0.4% | +0.42% | PASS |  |  |
| XCHP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XCHP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.91× / 0.07× | 0.91× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XCHP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 47224) | 20 bars, last ('2026-11-18', 47224) | PASS |  |  |
| XDRV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $38.84 | $38.84 | PASS |  |  |
| XDRV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $41.1 | $41.10 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XDRV.TO | E3 | percent from the 21-day average | 5.5% below | 5.5% below | PASS |  |  |
| XDRV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XDRV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.80 | $0.80 (sr=0.8021) | PASS |  | Wilder ATR14 |
| XDRV.TO | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| XDRV.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.1 | +8.1 | PASS |  |  |
| XDRV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $41.1, -5.5% | $41.10, -5.5% | PASS |  |  |
| XDRV.TO | L-now | ladder price row = compared price; name = the basis label | $38.84 "Last close" | $38.84 "last close" | PASS |  |  |
| XDRV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $47.61, -18.4% | $47.61, -18.4% | PASS |  |  |
| XDRV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $43.39, -10.5% | $43.39, -10.5% | PASS |  |  |
| XDRV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XDRV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.0 | 37.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XDRV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.5% vs +11.8% | -4.5% vs 11.8% | PASS |  |  |
| XDRV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XDRV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.7 | 22.7 | PASS |  | Wilder, completed bars |
| XDRV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.7 | PASS |  |  |
| XDRV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $38.84 vs $47.61 · -18.4% | $38.84 vs $47.61 · -18.4% | PASS |  |  |
| XDRV.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $38.84 vs $43.39 · -10.5% | $38.84 vs $43.39 · -10.5% | PASS |  |  |
| XDRV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.7% over 30 td | -0.7% over 30 td | PASS |  |  |
| XDRV.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XDRV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XDRV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.7% below $61.36 | 36.7% below $61.36 | PASS |  | closing high would be 61.36 |
| XDRV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.7% below | PASS |  |  |
| XDRV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $61.36 | $61.35662078857422 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XDRV.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 43 of 50 days empty | 43 of 50 days empty | PASS |  |  |
| XEQT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $44.01 | $44.01 | PASS |  |  |
| XEQT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $45.04 | $45.04 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XEQT.TO | E3 | percent from the 21-day average | 2.3% below | 2.3% below | PASS |  |  |
| XEQT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XEQT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.57 | $0.57 (sr=0.567) | PASS |  | Wilder ATR14 |
| XEQT.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| XEQT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $45.04, -2.3% | $45.04, -2.3% | PASS |  |  |
| XEQT.TO | L-now | ladder price row = compared price; name = the basis label | $44.01 "Last close" | $44.01 "last close" | PASS |  |  |
| XEQT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $43.58, 1.0% | $43.58, 1.0% | PASS |  |  |
| XEQT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $45.36, -3.0% | $45.36, -3.0% | PASS |  |  |
| XEQT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XEQT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.3 | 39.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XEQT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +15.2% vs +11.8% | 15.2% vs 11.8% | PASS |  |  |
| XEQT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XEQT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.3 | 16.3 | PASS |  | Wilder, completed bars |
| XEQT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 16.3 | PASS |  |  |
| XEQT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $44.01 vs $43.58 · +1.0% | $44.01 vs $43.58 · 1.0% | PASS |  |  |
| XEQT.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| XEQT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $44.01 vs $45.36 · -3.0% | $44.01 vs $45.36 · -3.0% | PASS |  |  |
| XEQT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XEQT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.7% over 30 td | +1.7% over 30 td | PASS |  |  |
| XEQT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XEQT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XEQT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.1% below $46.38 | 5.1% below $46.38 | PASS |  | closing high would be 46.27 |
| XEQT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.1% below | PASS |  |  |
| XEQT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.38 | $46.380001068115234 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XEQT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.74%, close location 0.25, OBV falling |
| XEQT.TO | V2 | day change of the last completed bar | down 0.7% | -0.74% | PASS |  |  |
| XEQT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.25 (raw 0.2500) | PASS |  |  |
| XEQT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XEQT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.19× / 0.57× | 1.19× / 0.58× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XEQT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 1081554) | 20 bars, last ('2026-11-18', 1081554) | PASS |  |  |
| XETM.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $57.76 | $57.76 | PASS |  |  |
| XETM.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $67.39 | $67.39 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XETM.TO | E3 | percent from the 21-day average | 14.3% below | 14.3% below | PASS |  |  |
| XETM.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XETM.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.54 | $2.54 (sr=2.5436) | PASS |  | Wilder ATR14 |
| XETM.TO | E5 | distance in normal day-moves | 3.8 | 3.8 | PASS |  | gauge dot note uses the same number:  · 3.8 day-moves below |
| XETM.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.9 | +4.9 | PASS |  |  |
| XETM.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $67.39, -14.3% | $67.39, -14.3% | PASS |  |  |
| XETM.TO | L-now | ladder price row = compared price; name = the basis label | $57.76 "Last close" | $57.76 "last close" | PASS |  |  |
| XETM.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $79.75, -27.6% | $79.75, -27.6% | PASS |  |  |
| XETM.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $74.6, -22.6% | $74.60, -22.6% | PASS |  |  |
| XETM.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.7 | 28.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XETM.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -31.4% vs +11.8% | -31.5% vs 11.8% | PASS |  |  |
| XETM.TO | T3w | words "past year" vs the window used | 209 / 251 bars back | 250-253 bars | PASS |  |  |
| XETM.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.2 | 23.2 | PASS |  | Wilder, completed bars |
| XETM.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 23.2 | PASS |  |  |
| XETM.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.57%, close location 0.22, OBV falling |
| XETM.TO | V2 | day change of the last completed bar | down 5.6% | -5.57% | PASS |  |  |
| XETM.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2239) | PASS |  |  |
| XETM.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XETM.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.14× / 1.27× | 1.14× / 1.27× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XETM.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 3559) | 20 bars, last ('2026-11-18', 3559) | PASS |  |  |
| XGD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $48.44 | $48.44 | PASS |  |  |
| XGD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $52.68 | $52.68 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XGD.TO | E3 | percent from the 21-day average | 8.1% below | 8.1% below | PASS |  |  |
| XGD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XGD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.17 | $2.17 (sr=2.1667) | PASS |  | Wilder ATR14 |
| XGD.TO | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| XGD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $52.68, -8.1% | $52.68, -8.1% | PASS |  |  |
| XGD.TO | L-now | ladder price row = compared price; name = the basis label | $48.44 "Last close" | $48.44 "last close" | PASS |  |  |
| XGD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $55.1, -12.1% | $55.10, -12.1% | PASS |  |  |
| XGD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $54.99, -11.9% | $54.99, -11.9% | PASS |  |  |
| XGD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XGD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.3 | 38.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XGD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.0% vs +11.8% | 6.0% vs 11.8% | PASS |  |  |
| XGD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XGD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.9 | 17.9 | PASS |  | Wilder, completed bars |
| XGD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 17.9 | PASS |  |  |
| XGD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $48.44 vs $55.10 · -12.1% | $48.44 vs $55.10 · -12.1% | PASS |  |  |
| XGD.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $48.44 vs $54.99 · -11.9% | $48.44 vs $54.99 · -11.9% | PASS |  |  |
| XGD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.1% over 30 td | -1.1% over 30 td | PASS |  |  |
| XGD.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XGD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XGD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 30.3% below $69.54 | 30.3% below $69.54 | PASS |  | closing high would be 68.70 |
| XGD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 30.3% below | PASS |  |  |
| XGD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $69.54 | $69.54086233267267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XGD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -5.54%, close location 0.43, OBV falling |
| XGD.TO | V2 | day change of the last completed bar | down 5.5% | -5.54% | PASS |  |  |
| XGD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XGD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.41× / 1.24× | 1.41× / 1.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XGD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 659042) | 20 bars, last ('2026-11-18', 659042) | PASS |  |  |
| XOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $160.58 | $160.58 | PASS |  |  |
| XOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $170.06 | $170.06 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XOM | E3 | percent from the 21-day average | 5.6% below | 5.6% below | PASS |  |  |
| XOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| XOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.40 | $4.40 (sr=4.3957) | PASS |  | Wilder ATR14 |
| XOM | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| XOM | L-ema21 | ladder row ema21: price and gap = price vs average | $170.06, -5.6% | $170.06, -5.6% | PASS |  |  |
| XOM | L-note | "Last close $X · date" note = last completed bar | Last close $160.58 · Nov 18 | $160.58 · Nov 18 | PASS |  |  |
| XOM | L-now | ladder price row = compared price; name = the basis label | $160.58 "After hours" | $160.58 "after hours" | PASS |  |  |
| XOM | L-sma200 | ladder row sma200: price and gap = price vs average | $156.71, 2.5% | $156.71, 2.5% | PASS |  |  |
| XOM | L-sma50 | ladder row sma50: price and gap = price vs average | $169.58, -5.3% | $169.58, -5.3% | PASS |  |  |
| XOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $160.58 / entry $160.58 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| XOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.9 | 35.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +34.9% vs +11.8% | 34.9% vs 11.8% | PASS |  |  |
| XOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.3 | 27.3 | PASS |  | Wilder, completed bars |
| XOM | T4w | words "20 or more / below 20" | 20 or more | ADX 27.3 | PASS |  |  |
| XOM | T5 | "counted at the last close ($X, date)" = last completed bar | $160.58, Nov 18 | $160.58, Nov 18 | PASS |  |  |
| XOM | T6 | price vs 200-day average (S1 pattern sma values) | $160.58 vs $156.71 · +2.5% | $160.58 vs $156.71 · 2.5% | PASS |  |  |
| XOM | T6w | word "Above" | Above | Above | PASS |  |  |
| XOM | T7 | price vs 50-day average (S1 pattern sma values) | $160.58 vs $169.58 · -5.3% | $160.58 vs $169.58 · -5.3% | PASS |  |  |
| XOM | T7w | word "Below" | Below | Below | PASS |  |  |
| XOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.6% over 30 td | +4.6% over 30 td | PASS |  |  |
| XOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| XOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.8% below $188.50 | 14.8% below $188.50 | PASS |  | closing high would be 187.25 |
| XOM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.8% below | PASS |  |  |
| XOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $188.50 | $188.5 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.97%, close location 0.00, OBV falling |
| XOM | V2 | day change of the last completed bar | down 4.0% | -3.97% | PASS |  |  |
| XOM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0047) | PASS |  |  |
| XOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.33× / 1.45× | 1.33× / 1.45× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 18122040) | 20 bars, last ('2026-11-18', 18122040) | PASS |  |  |
