# Statement Audit report

Run: 2026-11-20T19:53 · dumps: AAPL, AAPU, ABBV, AIPO, ALAB, AMD.TO, AMD, AMZN, AMZU, ANET.TO, ASML.TO, ASTL.TO, ATD.TO, AVGC, AVGO.TO, AVGO, BDT.TO, BOTZ, BRK-B, BRKU, CAMT, CARS.TO, CAT, CCO.TO, CEG, CGY.TO, CNQ.TO, CNR.TO, COP, COPP.TO, COPX, COPZ, COST, COTG, CSU.TO, CVX, DRAL, DRAM, DRIV, DUK, ELIL, EQIX, ETN, FCX, FINN.NE, GDX, GDXU.TO, GE, GEV.TO, GEV, GGLL, GIB-A.TO, GOOGL, GRID, HD, HURA.TO, HXQ.TO, JNJ, JPM, KEYS, LIN, LLY, MDA.TO, META, METU, MRVL, MSFT, MSFU, MTRX.TO, MU.TO, NEE, NEM, NFLX, NFXL, NTR.TO, NVDA, NVDL, ONTO, ORBX.TO, ORCL, PG, PLD, PNG.V, QCOM, QPUX, QTUM, RBOT.TO, RTX, RY.TO, SETM, SGRD.TO, SMH, SNDK.TO, SO, SOXL.NE, SOXL, SOXX, SPCL, TSLA, TSLL, TSM, UBOT, UFO, URA, URAA, V, VFV.TO, VRT, WDC.TO, WELL, WMT, XCHP.TO, XDRV.TO, XEQT.TO, XETM.TO, XGD.TO, XOM · ET at first dump: 11/20/2026, 6:36:42 PM

Verdicts: PASS 3939 · WRONG 0 (CRITICAL) · MISLEADING 3 (HIGH) · UNVERIFIED 343 (INFO)

Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.
S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| ASTL.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.0 | 25.2 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| AVGC | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.2 | 19.0 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| DRAL | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.9 | 35.1 | MISLEADING | LOW | within 0.6 of the Wilder ADX: the app smooths over its own longer frame, the audit over the 260 bars (a young fund seeds differently) |
| AAPL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.86× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AAPL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.80× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AAPU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AAPU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.73× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ABBV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ABBV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.65× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AIPO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AIPO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.69× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ALAB | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ALAB | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.3× 2.34× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.0× 2.04× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.72× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMZN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.79× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AMZU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AMZU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 230 252. 2025 -12 -22 3.2× 3.16× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| ANET.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ANET.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.0× 1.98× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ASML.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASML.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.99× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ASTL.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ASTL.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.58× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ATD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ATD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | U1 | numbers on the card no statement above claimed (exhaustive scan) | 102 252. 1.5× 1.52× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| AVGC | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGC | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.3× 2.30× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| AVGO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 230 252. 2025 -12 -22 3.0× 3.00× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| AVGO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| AVGO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.36× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BDT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BDT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.3× 3.26× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BOTZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BOTZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.36× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BRK-B | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRK-B | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.93× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| BRKU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| BRKU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CAMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CARS.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | $18.07 5.7 | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CAT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.7× 2.69× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CAT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CAT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.62× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CCO.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CCO.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.41× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CEG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CEG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.62× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CGY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CGY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.66× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CNQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.58× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CNR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CNR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.22× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COP | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COP | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 4.7× 4.67× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.3× 2.26× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COPX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 19 252. 3.0× 2.96× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| COPZ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COPZ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.71× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COST | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COST | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 0.97× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| COTG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| COTG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.8× 1.80× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CSU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CSU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.34× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| CVX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| CVX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 105 252. 2.7× 2.72× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| DRAL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 162 252. 1.9× 1.94× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| DRAM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRAM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.21× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DRIV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DRIV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.25× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| DUK | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| DUK | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.4× 0.39× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ELIL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ELIL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.7× 3.72× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| EQIX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| EQIX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.74× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ETN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ETN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.4× 2.43× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| FCX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FCX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.0× 2.01× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| FINN.NE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| FINN.NE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.2× 2.16× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GDX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.1× 3.14× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GDXU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GDXU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.11× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.87× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GEV | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 230 252. 2025 -12 -22 2.6× 2.63× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| GEV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GEV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.32× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GGLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GGLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.0× 1.02× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GIB-A.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GIB-A.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.72× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GOOGL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GOOGL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GRID | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.62× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| GRID | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| GRID | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.1× 3.07× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.8× 1.81× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HURA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HURA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 4.7× 4.71× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| HXQ.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| HXQ.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.57× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| JNJ | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JNJ | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.60× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| JPM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| JPM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.3× 2.33× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| KEYS | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| KEYS | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.65× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| LIN | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LIN | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.33× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| LLY | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| LLY | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.92× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MDA.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MDA.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.18× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| META | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| META | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.5× 0.52× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| METU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| METU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.62× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MRVL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MRVL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.90× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MSFT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.8× 1.77× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MSFU | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MSFU | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 211 252. 2026 -01 -20 | each one claimed or exempt | UNVERIFIED | INFO | 5 unclaimed number token(s): add a statement or an exempt rule |
| MTRX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MTRX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.8× 2.84× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| MU.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| MU.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.11× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NEE | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEE | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.1× 2.09× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NEM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NEM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.66× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NFLX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFLX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.4× 1.35× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NFXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NFXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.78× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NTR.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NTR.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.5× 3.52× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NVDA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 4.2× 4.23× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| NVDL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| NVDL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.15× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ONTO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ONTO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 141 252. | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ORBX.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORBX.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.34× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| ORCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| ORCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.4× 2.44× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PG | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PG | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.33× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PLD | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PLD | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.0× 2.97× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| PNG.V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| PNG.V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.7× 1.66× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QCOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QCOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.1× 2.14× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QPUX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QPUX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.0× 2.04× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| QTUM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| QTUM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | $25.00 5. 1.9× 1.92× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| RBOT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RBOT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.22× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RTX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RTX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.29× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| RY.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| RY.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SETM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.6× 1.58× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SETM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SETM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 149 252. 0.3× 0.34× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SGRD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SGRD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | U1 | numbers on the card no statement above claimed (exhaustive scan) | 6.2× 6.17× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SMH | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SMH | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 136 252. 2.4× 2.35× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SNDK.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SNDK.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.9× 0.94× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.9× 3.86× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SOXL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.7× 2.69× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| SOXX | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SOXX | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 159 252. 2.0× 1.98× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| SPCL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| SPCL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.3× 1.27× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSLA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 0.8× 0.85× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSLL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSLL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.8× 2.76× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| TSM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| TSM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.7× 2.70× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| UBOT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UBOT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.2× 2.16× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| UFO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| UFO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 4.9× 4.91× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| URA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URAA | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.2× 3.17× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| URAA | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| URAA | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.2× 1.24× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| V | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| V | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.5× 3.50× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| VFV.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VFV.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.8× 1.77× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| VRT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| VRT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 136 252. 2.0× 1.98× | each one claimed or exempt | UNVERIFIED | INFO | 4 unclaimed number token(s): add a statement or an exempt rule |
| WDC.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WDC.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.1× 1.14× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| WELL | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WELL | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | U1 | numbers on the card no statement above claimed (exhaustive scan) | 1.9× 1.88× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| WMT | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| WMT | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.6× 2.65× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XCHP.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XCHP.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.4× 3.39× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XEQT.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XEQT.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 212 252. 2026 -01 -20 3.2× 3.20× | each one claimed or exempt | UNVERIFIED | INFO | 7 unclaimed number token(s): add a statement or an exempt rule |
| XETM.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XETM.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | U1 | numbers on the card no statement above claimed (exhaustive scan) | 2.0× 2.03× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XGD.TO | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XGD.TO | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | U1 | numbers on the card no statement above claimed (exhaustive scan) | 3.2× 3.17× | each one claimed or exempt | UNVERIFIED | INFO | 2 unclaimed number token(s): add a statement or an exempt rule |
| XOM | V-effort | effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| XOM | V-obv20 | OBV 20-day divergence sentence (backend calculate_obv signal text) | shown | rule not mirrored in the audit yet | UNVERIFIED | INFO | sentence logic not recomputed; the numbers inside it are claimed above where possible |
| - | S3-1 | 200-day rising: UI words vs code window | UI says 30 trading days | code iloc[-31] = 30 bars back | PASS |  |  |
| - | S3-2 | REGRESSION: "a month ago" next to 30 bars back must be rejected | window_ok("a month ago", 30) | False | PASS |  |  |
| - | S3-3 | no "a month" wording left in technicalReadChecks.js next to the 30-bar window | none | none | PASS |  |  |
| - | S3-4 | "1-year high": code window | tail(252) | 250-253 bars | PASS |  |  |
| - | S3-5 | "past year" return: year-ago bar | iloc[-252] | 250-253 bars span | PASS |  |  |
| - | S3-6 | "Last 20 days" / "20-day On-Balance Volume": OBV lookback | lookback=20 | 20 bars | PASS |  |  |
| - | S3-7 | "at least 1 month" vs the 30-trading-day code | fixed | 30 trading days | PASS |  | not page text; logged for the Coherence audit |
| AAPL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $342.56 | $342.56 | PASS |  |  |
| AAPL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $347.3 | $347.30 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPL | E3 | percent from the 21-day average | 1.4% below | 1.4% below | PASS |  |  |
| AAPL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AAPL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.17 | $8.17 (sr=8.1741) | PASS |  | Wilder ATR14 |
| AAPL | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves below |
| AAPL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.4 | -5.4 | PASS |  |  |
| AAPL | L-ema21 | ladder row ema21: price and gap = price vs average | $347.3, -1.4% | $347.30, -1.4% | PASS |  |  |
| AAPL | L-note | "Last close $X · date" note = last completed bar | Last close $342.56 · Nov 20 | $342.56 · Nov 20 | PASS |  |  |
| AAPL | L-now | ladder price row = compared price; name = the basis label | $342.56 "After hours" | $342.56 "after hours" | PASS |  |  |
| AAPL | L-sma200 | ladder row sma200: price and gap = price vs average | $302.79, 13.1% | $302.79, 13.1% | PASS |  |  |
| AAPL | L-sma50 | ladder row sma50: price and gap = price vs average | $341.58, 0.3% | $341.58, 0.3% | PASS |  |  |
| AAPL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $342.56 / entry $342.56 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 46.6 | 46.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +29.1% vs +7.0% | 29.1% vs 7.0% | PASS |  |  |
| AAPL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPL | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.4 | 16.4 | PASS |  | Wilder, completed bars |
| AAPL | T4w | words "20 or more / below 20" | below 20 | ADX 16.4 | PASS |  |  |
| AAPL | T5 | "counted at the last close ($X, date)" = last completed bar | $342.56, Nov 20 | $342.56, Nov 20 | PASS |  |  |
| AAPL | T6 | price vs 200-day average (S1 pattern sma values) | $342.56 vs $302.79 · +13.1% | $342.56 vs $302.79 · 13.1% | PASS |  |  |
| AAPL | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPL | T7 | price vs 50-day average (S1 pattern sma values) | $342.56 vs $341.59 · +0.3% | $342.56 vs $341.58 · 0.3% | PASS |  |  |
| AAPL | T7w | word "Above" | Above | Above | PASS |  |  |
| AAPL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.3% over 30 td | +4.3% over 30 td | PASS |  |  |
| AAPL | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.1% below $360.83 | 5.1% below $360.83 | PASS |  | closing high would be 356.27 |
| AAPL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.1% below | PASS |  |  |
| AAPL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $360.83 | $360.8299865722656 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.90%, close location 0.15, OBV falling |
| AAPL | V2 | day change of the last completed bar | down 1.9% | -1.90% | PASS |  |  |
| AAPL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1456) | PASS |  |  |
| AAPL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.86× / 0.80× | 1.86× / 0.80× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 80450240) | 20 bars, last ('2026-11-20', 80450240) | PASS |  |  |
| AAPL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.86, OBV falling | condition true | PASS |  |  |
| AAPU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $45.91 | $45.91 | PASS |  |  |
| AAPU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $47.47 | $47.47 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AAPU | E3 | percent from the 21-day average | 3.3% below | 3.3% below | PASS |  |  |
| AAPU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AAPU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.14 | $2.14 (sr=2.1361) | PASS |  | Wilder ATR14 |
| AAPU | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| AAPU | L-ema21 | ladder row ema21: price and gap = price vs average | $47.47, -3.3% | $47.47, -3.3% | PASS |  |  |
| AAPU | L-note | "Last close $X · date" note = last completed bar | Last close $45.91 · Nov 20 | $45.91 · Nov 20 | PASS |  |  |
| AAPU | L-now | ladder price row = compared price; name = the basis label | $45.91 "After hours" | $45.91 "after hours" | PASS |  |  |
| AAPU | L-sma200 | ladder row sma200: price and gap = price vs average | $38.33, 19.8% | $38.33, 19.8% | PASS |  |  |
| AAPU | L-sma50 | ladder row sma50: price and gap = price vs average | $46.3, -0.8% | $46.30, -0.8% | PASS |  |  |
| AAPU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $45.91 / entry $45.91 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AAPU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AAPU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.3 | 45.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AAPU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +43.0% vs +7.0% | 43.0% vs 7.0% | PASS |  |  |
| AAPU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AAPU | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.1 | 16.1 | PASS |  | Wilder, completed bars |
| AAPU | T4w | words "20 or more / below 20" | below 20 | ADX 16.1 | PASS |  |  |
| AAPU | T5 | "counted at the last close ($X, date)" = last completed bar | $45.91, Nov 20 | $45.91, Nov 20 | PASS |  |  |
| AAPU | T6 | price vs 200-day average (S1 pattern sma values) | $45.91 vs $38.33 · +19.8% | $45.91 vs $38.33 · 19.8% | PASS |  |  |
| AAPU | T6w | word "Above" | Above | Above | PASS |  |  |
| AAPU | T7 | price vs 50-day average (S1 pattern sma values) | $45.91 vs $46.30 · -0.8% | $45.91 vs $46.30 · -0.8% | PASS |  |  |
| AAPU | T7w | word "Below" | Below | Below | PASS |  |  |
| AAPU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.9% over 30 td | +6.9% over 30 td | PASS |  |  |
| AAPU | T8r | word "rising" | still rising | rising | PASS |  |  |
| AAPU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AAPU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.1% below $51.04 | 10.1% below $51.04 | PASS |  | closing high would be 49.81 |
| AAPU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.1% below | PASS |  |  |
| AAPU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $51.04 | $51.040000915527344 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AAPU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.71%, close location 0.14, OBV falling |
| AAPU | V2 | day change of the last completed bar | down 3.7% | -3.71% | PASS |  |  |
| AAPU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1369) | PASS |  |  |
| AAPU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AAPU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.80× / 0.80× | 0.80× / 0.80× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AAPU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 597381) | 20 bars, last ('2026-11-20', 597381) | PASS |  |  |
| ABBV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $286.20 | $286.20 | PASS |  |  |
| ABBV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $288.19 | $288.19 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ABBV | E3 | percent from the 21-day average | 0.7% below | 0.7% below | PASS |  |  |
| ABBV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ABBV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.71 | $6.71 (sr=6.7085) | PASS |  | Wilder ATR14 |
| ABBV | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| ABBV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -7.2 | -7.2 | PASS |  |  |
| ABBV | L-ema21 | ladder row ema21: price and gap = price vs average | $288.19, -0.7% | $288.19, -0.7% | PASS |  |  |
| ABBV | L-note | "Last close $X · date" note = last completed bar | Last close $286.20 · Nov 20 | $286.20 · Nov 20 | PASS |  |  |
| ABBV | L-now | ladder price row = compared price; name = the basis label | $286.2 "After hours" | $286.20 "after hours" | PASS |  |  |
| ABBV | L-sma200 | ladder row sma200: price and gap = price vs average | $239.96, 19.3% | $239.96, 19.3% | PASS |  |  |
| ABBV | L-sma50 | ladder row sma50: price and gap = price vs average | $278.25, 2.9% | $278.25, 2.9% | PASS |  |  |
| ABBV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $286.20 / entry $286.20 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ABBV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ABBV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.5 | 49.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ABBV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +28.5% vs +7.0% | 28.5% vs 7.0% | PASS |  |  |
| ABBV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ABBV | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.8 | 25.8 | PASS |  | Wilder, completed bars |
| ABBV | T4w | words "20 or more / below 20" | 20 or more | ADX 25.8 | PASS |  |  |
| ABBV | T5 | "counted at the last close ($X, date)" = last completed bar | $286.20, Nov 20 | $286.20, Nov 20 | PASS |  |  |
| ABBV | T6 | price vs 200-day average (S1 pattern sma values) | $286.20 vs $239.96 · +19.3% | $286.20 vs $239.96 · 19.3% | PASS |  |  |
| ABBV | T6w | word "Above" | Above | Above | PASS |  |  |
| ABBV | T7 | price vs 50-day average (S1 pattern sma values) | $286.20 vs $278.25 · +2.9% | $286.20 vs $278.25 · 2.9% | PASS |  |  |
| ABBV | T7w | word "Above" | Above | Above | PASS |  |  |
| ABBV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.6% over 30 td | +4.6% over 30 td | PASS |  |  |
| ABBV | T8r | word "rising" | still rising | rising | PASS |  |  |
| ABBV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ABBV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.5% below $302.93 | 5.5% below $302.93 | PASS |  | closing high would be 295.03 |
| ABBV | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.5% below | PASS |  |  |
| ABBV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.93 | $302.92999267578125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ABBV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 1 up, 0 down, 2 flat | PASS |  | change 0.94%, close location 0.25, OBV flat |
| ABBV | V2 | day change of the last completed bar | up 0.9% | +0.94% | PASS |  |  |
| ABBV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| ABBV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.73× / 0.40× | 1.73× / 0.40× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ABBV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 8755117) | 20 bars, last ('2026-11-20', 8755117) | PASS |  |  |
| AIPO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $20.43 | $20.43 | PASS |  |  |
| AIPO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $23.68 | $23.68 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AIPO | E3 | percent from the 21-day average | 13.7% below | 13.7% below | PASS |  |  |
| AIPO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AIPO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.16 | $1.16 (sr=1.1556) | PASS |  | Wilder ATR14 |
| AIPO | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| AIPO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.1 | +4.1 | PASS |  |  |
| AIPO | L-ema21 | ladder row ema21: price and gap = price vs average | $23.68, -13.7% | $23.68, -13.7% | PASS |  |  |
| AIPO | L-note | "Last close $X · date" note = last completed bar | Last close $20.43 · Nov 20 | $20.43 · Nov 20 | PASS |  |  |
| AIPO | L-now | ladder price row = compared price; name = the basis label | $20.43 "After hours" | $20.43 "after hours" | PASS |  |  |
| AIPO | L-sma200 | ladder row sma200: price and gap = price vs average | $28.46, -28.2% | $28.46, -28.2% | PASS |  |  |
| AIPO | L-sma50 | ladder row sma50: price and gap = price vs average | $26.13, -21.8% | $26.13, -21.8% | PASS |  |  |
| AIPO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $20.43 / entry $20.43 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AIPO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AIPO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.4 | 30.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AIPO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.3% vs +7.0% | -5.3% vs 7.0% | PASS |  |  |
| AIPO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AIPO | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.9 | 33.9 | PASS |  | Wilder, completed bars |
| AIPO | T4w | words "20 or more / below 20" | 20 or more | ADX 33.9 | PASS |  |  |
| AIPO | T5 | "counted at the last close ($X, date)" = last completed bar | $20.43, Nov 20 | $20.43, Nov 20 | PASS |  |  |
| AIPO | T6 | price vs 200-day average (S1 pattern sma values) | $20.43 vs $28.46 · -28.2% | $20.43 vs $28.46 · -28.2% | PASS |  |  |
| AIPO | T6w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T7 | price vs 50-day average (S1 pattern sma values) | $20.43 vs $26.13 · -21.8% | $20.43 vs $26.13 · -21.8% | PASS |  |  |
| AIPO | T7w | word "Below" | Below | Below | PASS |  |  |
| AIPO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.4% over 30 td | +0.4% over 30 td | PASS |  |  |
| AIPO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AIPO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AIPO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 41.3% below $34.79 | 41.3% below $34.79 | PASS |  | closing high would be 34.77 |
| AIPO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 41.3% below | PASS |  |  |
| AIPO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $34.79 | $34.790000915527344 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AIPO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.47%, close location 0.10, OBV falling |
| AIPO | V2 | day change of the last completed bar | down 7.5% | -7.47% | PASS |  |  |
| AIPO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.0987) | PASS |  |  |
| AIPO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AIPO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.65× / 1.32× | 1.65× / 1.32× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AIPO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 2765371) | 20 bars, last ('2026-11-20', 2765371) | PASS |  |  |
| AIPO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.65, OBV falling | condition true | PASS |  |  |
| ALAB | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $180.35 | $180.35 | PASS |  |  |
| ALAB | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $231.24 | $231.24 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ALAB | E3 | percent from the 21-day average | 22.0% below | 22.0% below | PASS |  |  |
| ALAB | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ALAB | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $24.13 | $24.13 (sr=24.1332) | PASS |  | Wilder ATR14 |
| ALAB | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| ALAB | L-ema21 | ladder row ema21: price and gap = price vs average | $231.24, -22.0% | $231.24, -22.0% | PASS |  |  |
| ALAB | L-note | "Last close $X · date" note = last completed bar | Last close $180.35 · Nov 20 | $180.35 · Nov 20 | PASS |  |  |
| ALAB | L-now | ladder price row = compared price; name = the basis label | $180.35 "After hours" | $180.35 "after hours" | PASS |  |  |
| ALAB | L-sma200 | ladder row sma200: price and gap = price vs average | $258.83, -30.3% | $258.83, -30.3% | PASS |  |  |
| ALAB | L-sma50 | ladder row sma50: price and gap = price vs average | $285.21, -36.8% | $285.21, -36.8% | PASS |  |  |
| ALAB | S5-price | S5: the same live price reads the same on the header and the Entry block | header $180.35 / entry $180.35 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ALAB | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ALAB | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 33.0 | 33.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ALAB | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +29.5% vs +7.0% | 29.5% vs 7.0% | PASS |  |  |
| ALAB | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ALAB | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.1 | 28.1 | PASS |  | Wilder, completed bars |
| ALAB | T4w | words "20 or more / below 20" | 20 or more | ADX 28.1 | PASS |  |  |
| ALAB | T5 | "counted at the last close ($X, date)" = last completed bar | $180.35, Nov 20 | $180.35, Nov 20 | PASS |  |  |
| ALAB | T6 | price vs 200-day average (S1 pattern sma values) | $180.35 vs $258.83 · -30.3% | $180.35 vs $258.83 · -30.3% | PASS |  |  |
| ALAB | T6w | word "Below" | Below | Below | PASS |  |  |
| ALAB | T7 | price vs 50-day average (S1 pattern sma values) | $180.35 vs $285.21 · -36.8% | $180.35 vs $285.21 · -36.8% | PASS |  |  |
| ALAB | T7w | word "Below" | Below | Below | PASS |  |  |
| ALAB | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.1% over 30 td | +5.1% over 30 td | PASS |  |  |
| ALAB | T8r | word "rising" | still rising | rising | PASS |  |  |
| ALAB | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ALAB | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 63.9% below $499.48 | 63.9% below $499.48 | PASS |  | closing high would be 483.02 |
| ALAB | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 63.9% below | PASS |  |  |
| ALAB | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $499.48 | $499.47601318359375 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ALAB | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -14.77%, close location 0.12, OBV falling |
| ALAB | V2 | day change of the last completed bar | down 14.8% | -14.77% | PASS |  |  |
| ALAB | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1225) | PASS |  |  |
| ALAB | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ALAB | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.69× / 1.10× | 1.69× / 1.10× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ALAB | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 7932141) | 20 bars, last ('2026-11-20', 7932141) | PASS |  |  |
| ALAB | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.69, OBV falling | condition true | PASS |  |  |
| AMD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $424.39 | $424.39 | PASS |  |  |
| AMD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $512.12 | $512.12 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD | E3 | percent from the 21-day average | 17.1% below | 17.1% below | PASS |  |  |
| AMD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $45.41 | $45.41 (sr=45.4074) | PASS |  | Wilder ATR14 |
| AMD | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| AMD | L-ema21 | ladder row ema21: price and gap = price vs average | $512.12, -17.1% | $512.12, -17.1% | PASS |  |  |
| AMD | L-note | "Last close $X · date" note = last completed bar | Last close $424.39 · Nov 20 | $424.39 · Nov 20 | PASS |  |  |
| AMD | L-now | ladder price row = compared price; name = the basis label | $424.39 "After hours" | $424.39 "after hours" | PASS |  |  |
| AMD | L-sma200 | ladder row sma200: price and gap = price vs average | $429.79, -1.3% | $429.79, -1.3% | PASS |  |  |
| AMD | L-sma50 | ladder row sma50: price and gap = price vs average | $553.1, -23.3% | $553.10, -23.3% | PASS |  |  |
| AMD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $424.39 / entry $424.39 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.4 | 38.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +106.0% vs +7.0% | 106.0% vs 7.0% | PASS |  |  |
| AMD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.9 | 17.9 | PASS |  | Wilder, completed bars |
| AMD | T4w | words "20 or more / below 20" | below 20 | ADX 17.9 | PASS |  |  |
| AMD | T5 | "counted at the last close ($X, date)" = last completed bar | $424.39, Nov 20 | $424.39, Nov 20 | PASS |  |  |
| AMD | T6 | price vs 200-day average (S1 pattern sma values) | $424.39 vs $429.79 · -1.3% | $424.39 vs $429.79 · -1.3% | PASS |  |  |
| AMD | T6w | word "Below" | Below | Below | PASS |  |  |
| AMD | T7 | price vs 50-day average (S1 pattern sma values) | $424.39 vs $553.10 · -23.3% | $424.39 vs $553.10 · -23.3% | PASS |  |  |
| AMD | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +11.5% over 30 td | +11.5% over 30 td | PASS |  |  |
| AMD | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.6% below $658.52 | 35.6% below $658.52 | PASS |  | closing high would be 649.42 |
| AMD | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.6% below | PASS |  |  |
| AMD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $658.52 | $658.52001953125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -13.25%, close location 0.10, OBV falling |
| AMD | V2 | day change of the last completed bar | down 13.3% | -13.25% | PASS |  |  |
| AMD | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1005) | PASS |  |  |
| AMD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.34× / 1.24× | 2.34× / 1.24× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 69985844) | 20 bars, last ('2026-11-20', 69985844) | PASS |  |  |
| AMD | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.34, OBV falling | condition true | PASS |  |  |
| AMD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $10.93 | $10.93 | PASS |  |  |
| AMD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.18 | $13.18 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMD.TO | E3 | percent from the 21-day average | 17.1% below | 17.1% below | PASS |  |  |
| AMD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AMD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.15 | $1.15 (sr=1.1481) | PASS |  | Wilder ATR14 |
| AMD.TO | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| AMD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $13.18, -17.1% | $13.18, -17.1% | PASS |  |  |
| AMD.TO | L-now | ladder price row = compared price; name = the basis label | $10.93 "Last close" | $10.93 "last close" | PASS |  |  |
| AMD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $11.09, -1.5% | $11.09, -1.5% | PASS |  |  |
| AMD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $14.21, -23.1% | $14.21, -23.1% | PASS |  |  |
| AMD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 38.3 | 38.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +100.5% vs +7.0% | 100.6% vs 7.0% | PASS |  |  |
| AMD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.4 | 18.4 | PASS |  | Wilder, completed bars |
| AMD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 18.4 | PASS |  |  |
| AMD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $10.93 vs $11.09 · -1.4% | $10.93 vs $11.09 · -1.5% | PASS |  |  |
| AMD.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| AMD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $10.93 vs $14.21 · -23.1% | $10.93 vs $14.21 · -23.1% | PASS |  |  |
| AMD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| AMD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +11.2% over 30 td | +11.3% over 30 td | PASS |  |  |
| AMD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.6% below $16.97 | 35.6% below $16.97 | PASS |  | closing high would be 16.73 |
| AMD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.6% below | PASS |  |  |
| AMD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $16.97 | $16.968570709228516 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -13.19%, close location 0.09, OBV falling |
| AMD.TO | V2 | day change of the last completed bar | down 13.2% | -13.19% | PASS |  |  |
| AMD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0929) | PASS |  |  |
| AMD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.04× / 1.26× | 2.04× / 1.26× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 4890532) | 20 bars, last ('2026-11-20', 4890532) | PASS |  |  |
| AMD.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.04, OBV falling | condition true | PASS |  |  |
| AMZN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $246.82 | $246.82 | PASS |  |  |
| AMZN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $258.37 | $258.37 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZN | E3 | percent from the 21-day average | 4.5% below | 4.5% below | PASS |  |  |
| AMZN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMZN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.97 | $9.97 (sr=9.9688) | PASS |  | Wilder ATR14 |
| AMZN | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| AMZN | L-ema21 | ladder row ema21: price and gap = price vs average | $258.37, -4.5% | $258.37, -4.5% | PASS |  |  |
| AMZN | L-note | "Last close $X · date" note = last completed bar | Last close $246.82 · Nov 20 | $246.82 · Nov 20 | PASS |  |  |
| AMZN | L-now | ladder price row = compared price; name = the basis label | $246.82 "After hours" | $246.82 "after hours" | PASS |  |  |
| AMZN | L-sma200 | ladder row sma200: price and gap = price vs average | $245.15, 0.7% | $245.15, 0.7% | PASS |  |  |
| AMZN | L-sma50 | ladder row sma50: price and gap = price vs average | $255.03, -3.2% | $255.03, -3.2% | PASS |  |  |
| AMZN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $246.82 / entry $246.82 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.3 | 42.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +13.7% vs +7.0% | 13.7% vs 7.0% | PASS |  |  |
| AMZN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZN | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.0 | 11.0 | PASS |  | Wilder, completed bars |
| AMZN | T4w | words "20 or more / below 20" | below 20 | ADX 11.0 | PASS |  |  |
| AMZN | T5 | "counted at the last close ($X, date)" = last completed bar | $246.82, Nov 20 | $246.82, Nov 20 | PASS |  |  |
| AMZN | T6 | price vs 200-day average (S1 pattern sma values) | $246.82 vs $245.15 · +0.7% | $246.82 vs $245.15 · 0.7% | PASS |  |  |
| AMZN | T6w | word "Above" | Above | Above | PASS |  |  |
| AMZN | T7 | price vs 50-day average (S1 pattern sma values) | $246.82 vs $255.03 · -3.2% | $246.82 vs $255.03 · -3.2% | PASS |  |  |
| AMZN | T7w | word "Below" | Below | Below | PASS |  |  |
| AMZN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.2% over 30 td | +1.2% over 30 td | PASS |  |  |
| AMZN | T8r | word "rising" | still rising | rising | PASS |  |  |
| AMZN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.1% below $287.20 | 14.1% below $287.20 | PASS |  | closing high would be 284.02 |
| AMZN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.1% below | PASS |  |  |
| AMZN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $287.20 | $287.2 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.10%, close location 0.10, OBV falling |
| AMZN | V2 | day change of the last completed bar | down 4.1% | -4.10% | PASS |  |  |
| AMZN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1030) | PASS |  |  |
| AMZN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.72× / 1.02× | 1.72× / 1.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 74143103) | 20 bars, last ('2026-11-20', 74143103) | PASS |  |  |
| AMZN | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.72, OBV falling | condition true | PASS |  |  |
| AMZU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $32.16 | $32.16 | PASS |  |  |
| AMZU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $35.66 | $35.66 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AMZU | E3 | percent from the 21-day average | 9.8% below | 9.8% below | PASS |  |  |
| AMZU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AMZU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.74 | $2.74 (sr=2.7414) | PASS |  | Wilder ATR14 |
| AMZU | E5 | distance in normal day-moves | 1.3 | 1.3 | PASS |  | gauge dot note uses the same number:  · 1.3 day-moves below |
| AMZU | L-ema21 | ladder row ema21: price and gap = price vs average | $35.66, -9.8% | $35.66, -9.8% | PASS |  |  |
| AMZU | L-note | "Last close $X · date" note = last completed bar | Last close $32.16 · Nov 20 | $32.16 · Nov 20 | PASS |  |  |
| AMZU | L-now | ladder price row = compared price; name = the basis label | $32.16 "After hours" | $32.16 "after hours" | PASS |  |  |
| AMZU | L-sma200 | ladder row sma200: price and gap = price vs average | $34.94, -8.0% | $34.94, -8.0% | PASS |  |  |
| AMZU | L-sma50 | ladder row sma50: price and gap = price vs average | $35.23, -8.7% | $35.23, -8.7% | PASS |  |  |
| AMZU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $32.16 / entry $32.16 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AMZU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AMZU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.2 | 41.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AMZU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.0% vs +7.0% | 4.0% vs 7.0% | PASS |  |  |
| AMZU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AMZU | T4 | ADX 14 (S1 /api/sr meta.adx) | 10.9 | 10.9 | PASS |  | Wilder, completed bars |
| AMZU | T4w | words "20 or more / below 20" | below 20 | ADX 10.9 | PASS |  |  |
| AMZU | T5 | "counted at the last close ($X, date)" = last completed bar | $32.16, Nov 20 | $32.16, Nov 20 | PASS |  |  |
| AMZU | T6 | price vs 200-day average (S1 pattern sma values) | $32.16 vs $34.94 · -8.0% | $32.16 vs $34.94 · -8.0% | PASS |  |  |
| AMZU | T6w | word "Below" | Below | Below | PASS |  |  |
| AMZU | T7 | price vs 50-day average (S1 pattern sma values) | $32.16 vs $35.23 · -8.7% | $32.16 vs $35.23 · -8.7% | PASS |  |  |
| AMZU | T7w | word "Below" | Below | Below | PASS |  |  |
| AMZU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.2% over 30 td | -0.2% over 30 td | PASS |  |  |
| AMZU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AMZU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AMZU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 31.1% below $46.65 | 31.1% below $46.65 | PASS |  | closing high would be 45.45 |
| AMZU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 31.1% below | PASS |  |  |
| AMZU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.65 | $46.6467 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AMZU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.98%, close location 0.11, OBV falling |
| AMZU | V2 | day change of the last completed bar | down 8.0% | -7.98% | PASS |  |  |
| AMZU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1080) | PASS |  |  |
| AMZU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AMZU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.79× / 0.94× | 0.79× / 0.94× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AMZU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 1525802) | 20 bars, last ('2026-11-20', 1525802) | PASS |  |  |
| ANET.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $29.87 | $29.87 | PASS |  |  |
| ANET.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $33.13 | $33.13 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ANET.TO | E3 | percent from the 21-day average | 9.8% below | 9.8% below | PASS |  |  |
| ANET.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ANET.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.15 | $2.15 (sr=2.1514) | PASS |  | Wilder ATR14 |
| ANET.TO | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| ANET.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $33.13, -9.8% | $33.13, -9.8% | PASS |  |  |
| ANET.TO | L-now | ladder price row = compared price; name = the basis label | $29.87 "Last close" | $29.87 "last close" | PASS |  |  |
| ANET.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $30.25, -1.3% | $30.25, -1.3% | PASS |  |  |
| ANET.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $34.32, -13.0% | $34.32, -13.0% | PASS |  |  |
| ANET.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.3 | 41.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ANET.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.3% vs +7.0% | 25.3% vs 7.0% | PASS |  |  |
| ANET.TO | T3w | words "past year" vs the window used | 229 / 251 bars back | 250-253 bars | PASS |  |  |
| ANET.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.9 | 16.9 | PASS |  | Wilder, completed bars |
| ANET.TO | T4w | words "20 or more / below 20" | below 20 | ADX 16.9 | PASS |  |  |
| ANET.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -11.89%, close location 0.09, OBV falling |
| ANET.TO | V2 | day change of the last completed bar | down 11.9% | -11.89% | PASS |  |  |
| ANET.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0944) | PASS |  |  |
| ANET.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ANET.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.16× / 1.65× | 3.16× / 1.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ANET.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 162718) | 20 bars, last ('2026-11-20', 162718) | PASS |  |  |
| ANET.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.16, OBV falling | condition true | PASS |  |  |
| ASML.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $38.95 | $38.95 | PASS |  |  |
| ASML.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $43.43 | $43.43 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASML.TO | E3 | percent from the 21-day average | 10.3% below | 10.3% below | PASS |  |  |
| ASML.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| ASML.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.02 | $2.02 (sr=2.0163) | PASS |  | Wilder ATR14 |
| ASML.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| ASML.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $43.43, -10.3% | $43.43, -10.3% | PASS |  |  |
| ASML.TO | L-now | ladder price row = compared price; name = the basis label | $38.95 "Last close" | $38.95 "last close" | PASS |  |  |
| ASML.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $45.1, -13.6% | $45.10, -13.6% | PASS |  |  |
| ASML.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $46.86, -16.9% | $46.86, -16.9% | PASS |  |  |
| ASML.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ASML.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.0 | 34.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASML.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +41.7% vs +7.0% | 41.7% vs 7.0% | PASS |  |  |
| ASML.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ASML.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.2 | 28.2 | PASS |  | Wilder, completed bars |
| ASML.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.2 | PASS |  |  |
| ASML.TO | T6 | price vs 200-day average (S1 pattern sma values) | $38.95 vs $45.10 · -13.6% | $38.95 vs $45.10 · -13.6% | PASS |  |  |
| ASML.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| ASML.TO | T7 | price vs 50-day average (S1 pattern sma values) | $38.95 vs $46.86 · -16.9% | $38.95 vs $46.86 · -16.9% | PASS |  |  |
| ASML.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| ASML.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.4% over 30 td | +3.4% over 30 td | PASS |  |  |
| ASML.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ASML.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ASML.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 31.4% below $56.75 | 31.4% below $56.75 | PASS |  | closing high would be 56.67 |
| ASML.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 31.4% below | PASS |  |  |
| ASML.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $56.75 | $56.745395859548175 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ASML.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.80%, close location 0.84, OBV falling |
| ASML.TO | V2 | day change of the last completed bar | down 2.8% | -2.80% | PASS |  |  |
| ASML.TO | V3 | close location words (>=0.75 high, <=0.25 low) | settled near the day's high | close location 0.84 (raw 0.8389) | PASS |  |  |
| ASML.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ASML.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.98× / 0.54× | 1.98× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASML.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 92565) | 20 bars, last ('2026-11-20', 92565) | PASS |  |  |
| ASML.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.98, OBV falling | condition true | PASS |  |  |
| ASTL.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $6.15 | $6.15 | PASS |  |  |
| ASTL.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $7.11 | $7.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ASTL.TO | E3 | percent from the 21-day average | 13.5% below | 13.5% below | PASS |  |  |
| ASTL.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ASTL.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.45 | $0.45 (sr=0.4451) | PASS |  | Wilder ATR14 |
| ASTL.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| ASTL.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $7.11, -13.5% | $7.11, -13.5% | PASS |  |  |
| ASTL.TO | L-note | "Last close $X · date" note = last completed bar | Last close $6.15 · Nov 20 | $6.15 · Nov 20 | PASS |  |  |
| ASTL.TO | L-now | ladder price row = compared price; name = the basis label | $6.15 "After hours" | $6.15 "after hours" | PASS |  |  |
| ASTL.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $6.27, -1.9% | $6.27, -1.9% | PASS |  |  |
| ASTL.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $6.54, -6.0% | $6.54, -6.0% | PASS |  |  |
| ASTL.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $6.15 / entry $6.15 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ASTL.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ASTL.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.3 | 37.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ASTL.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +33.1% vs +7.0% | 33.1% vs 7.0% | PASS |  |  |
| ASTL.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ASTL.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.2 | PASS |  |  |
| ASTL.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $6.15, Nov 20 | $6.15, Nov 20 | PASS |  |  |
| ASTL.TO | T6 | price vs 200-day average (S1 pattern sma values) | $6.15 vs $6.27 · -1.9% | $6.15 vs $6.27 · -1.9% | PASS |  |  |
| ASTL.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| ASTL.TO | T7 | price vs 50-day average (S1 pattern sma values) | $6.15 vs $6.54 · -6.0% | $6.15 vs $6.54 · -6.0% | PASS |  |  |
| ASTL.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| ASTL.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.5% over 30 td | +2.4% over 30 td | PASS |  |  |
| ASTL.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ASTL.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ASTL.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.0% below $8.31 | 26.0% below $8.31 | PASS |  | closing high would be 8.22 |
| ASTL.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.0% below | PASS |  |  |
| ASTL.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $8.31 | $8.3100004196167 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ASTL.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.87%, close location 0.03, OBV falling |
| ASTL.TO | V2 | day change of the last completed bar | down 10.9% | -10.87% | PASS |  |  |
| ASTL.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0286) | PASS |  |  |
| ASTL.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ASTL.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.99× / 1.50× | 0.99× / 1.50× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ASTL.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 592039) | 20 bars, last ('2026-11-20', 592039) | PASS |  |  |
| ATD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $81.72 | $81.72 | PASS |  |  |
| ATD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $82.26 | $82.26 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ATD.TO | E3 | percent from the 21-day average | 0.7% below | 0.7% below | PASS |  |  |
| ATD.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ATD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.86 | $1.86 (sr=1.8583) | PASS |  | Wilder ATR14 |
| ATD.TO | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves below |
| ATD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $82.26, -0.7% | $82.26, -0.7% | PASS |  |  |
| ATD.TO | L-note | "Last close $X · date" note = last completed bar | Last close $81.72 · Nov 20 | $81.72 · Nov 20 | PASS |  |  |
| ATD.TO | L-now | ladder price row = compared price; name = the basis label | $81.72 "After hours" | $81.72 "after hours" | PASS |  |  |
| ATD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $82.47, -0.9% | $82.47, -0.9% | PASS |  |  |
| ATD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $80.86, 1.1% | $80.86, 1.1% | PASS |  |  |
| ATD.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $81.72 / entry $81.72 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ATD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ATD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.3 | 48.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ATD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +18.0% vs +7.0% | 18.0% vs 7.0% | PASS |  |  |
| ATD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ATD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.1 | 15.1 | PASS |  | Wilder, completed bars |
| ATD.TO | T4w | words "20 or more / below 20" | below 20 | ADX 15.1 | PASS |  |  |
| ATD.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $81.72, Nov 20 | $81.72, Nov 20 | PASS |  |  |
| ATD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $81.72 vs $82.47 · -0.9% | $81.72 vs $82.47 · -0.9% | PASS |  |  |
| ATD.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| ATD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $81.72 vs $80.86 · +1.1% | $81.72 vs $80.86 · 1.1% | PASS |  |  |
| ATD.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| ATD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.5% over 30 td | PASS |  |  |
| ATD.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ATD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ATD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.7% below $94.68 | 13.7% below $94.68 | PASS |  | closing high would be 93.29 |
| ATD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.7% below | PASS |  |  |
| ATD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $94.68 | $94.67526234045502 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ATD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 1 up, 0 down, 2 flat | PASS |  | change 1.97%, close location 0.50, OBV flat |
| ATD.TO | V2 | day change of the last completed bar | up 2.0% | +1.97% | PASS |  |  |
| ATD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| ATD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.58× / 0.87× | 1.58× / 0.87× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ATD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 2099514) | 20 bars, last ('2026-11-20', 2099514) | PASS |  |  |
| AVGC | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $14.16 | $14.16 | PASS |  |  |
| AVGC | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.04 | $18.04 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGC | E3 | percent from the 21-day average | 21.5% below | 21.5% below | PASS |  |  |
| AVGC | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AVGC | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.93 | $1.93 (sr=1.9272) | PASS |  | Wilder ATR14 |
| AVGC | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| AVGC | L-ema21 | ladder row ema21: price and gap = price vs average | $18.04, -21.5% | $18.04, -21.5% | PASS |  |  |
| AVGC | L-note | "Last close $X · date" note = last completed bar | Last close $14.15 · Nov 20 | $14.15 · Nov 20 | PASS |  |  |
| AVGC | L-now | ladder price row = compared price; name = the basis label | $14.16 "After hours" | $14.15 "after hours" | PASS |  |  |
| AVGC | L-sma50 | ladder row sma50: price and gap = price vs average | $19.41, -27.1% | $19.41, -27.1% | PASS |  |  |
| AVGC | S5-price | S5: the same live price reads the same on the header and the Entry block | header $14.16 / entry $14.16 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AVGC | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 39.1 | 39.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGC | T4w | words "20 or more / below 20" | below 20 | ADX 19.0 | PASS |  |  |
| AVGC | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -25.05%, close location 0.00, OBV falling |
| AVGC | V2 | day change of the last completed bar | down 25.0% | -25.05% | PASS |  |  |
| AVGC | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| AVGC | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AVGC | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.52× / 1.84× | 1.52× / 1.84× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGC | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 4881) | 20 bars, last ('2026-11-20', 4881) | PASS |  |  |
| AVGC | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.52, OBV falling | condition true | PASS |  |  |
| AVGO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $304.41 | $304.41 | PASS |  |  |
| AVGO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $335.25 | $335.25 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGO | E3 | percent from the 21-day average | 9.2% below | 9.2% below | PASS |  |  |
| AVGO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| AVGO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $20.02 | $20.02 (sr=20.0187) | PASS |  | Wilder ATR14 |
| AVGO | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| AVGO | L-ema21 | ladder row ema21: price and gap = price vs average | $335.25, -9.2% | $335.25, -9.2% | PASS |  |  |
| AVGO | L-note | "Last close $X · date" note = last completed bar | Last close $304.41 · Nov 20 | $304.41 · Nov 20 | PASS |  |  |
| AVGO | L-now | ladder price row = compared price; name = the basis label | $304.41 "After hours" | $304.41 "after hours" | PASS |  |  |
| AVGO | L-sma200 | ladder row sma200: price and gap = price vs average | $367.82, -17.2% | $367.82, -17.2% | PASS |  |  |
| AVGO | L-sma50 | ladder row sma50: price and gap = price vs average | $342.71, -11.2% | $342.71, -11.2% | PASS |  |  |
| AVGO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $304.41 / entry $304.41 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| AVGO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| AVGO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.8 | 40.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -12.2% vs +7.0% | -12.2% vs 7.0% | PASS |  |  |
| AVGO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| AVGO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.0 | 19.0 | PASS |  | Wilder, completed bars |
| AVGO | T4w | words "20 or more / below 20" | below 20 | ADX 19.0 | PASS |  |  |
| AVGO | T5 | "counted at the last close ($X, date)" = last completed bar | $304.41, Nov 20 | $304.41, Nov 20 | PASS |  |  |
| AVGO | T6 | price vs 200-day average (S1 pattern sma values) | $304.41 vs $367.82 · -17.2% | $304.41 vs $367.82 · -17.2% | PASS |  |  |
| AVGO | T6w | word "Below" | Below | Below | PASS |  |  |
| AVGO | T7 | price vs 50-day average (S1 pattern sma values) | $304.41 vs $342.71 · -11.2% | $304.41 vs $342.71 · -11.2% | PASS |  |  |
| AVGO | T7w | word "Below" | Below | Below | PASS |  |  |
| AVGO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.1% over 30 td | -0.1% over 30 td | PASS |  |  |
| AVGO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| AVGO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| AVGO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 38.5% below $495.00 | 38.5% below $495.00 | PASS |  | closing high would be 481.57 |
| AVGO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 38.5% below | PASS |  |  |
| AVGO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $495.00 | $495 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| AVGO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -12.19%, close location 0.08, OBV falling |
| AVGO | V2 | day change of the last completed bar | down 12.2% | -12.19% | PASS |  |  |
| AVGO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0807) | PASS |  |  |
| AVGO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| AVGO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.30× / 1.85× | 2.30× / 1.85× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 59622727) | 20 bars, last ('2026-11-20', 59622727) | PASS |  |  |
| AVGO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.30, OBV falling | condition true | PASS |  |  |
| AVGO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $11.53 | $11.53 | PASS |  |  |
| AVGO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $12.71 | $12.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| AVGO.TO | E3 | percent from the 21-day average | 9.3% below | 9.3% below | PASS |  |  |
| AVGO.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| AVGO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.74 | $0.74 (sr=0.7382) | PASS |  | Wilder ATR14 |
| AVGO.TO | E5 | distance in normal day-moves | 1.6 | 1.6 | PASS |  | gauge dot note uses the same number:  · 1.6 day-moves below |
| AVGO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $12.71, -9.3% | $12.71, -9.3% | PASS |  |  |
| AVGO.TO | L-now | ladder price row = compared price; name = the basis label | $11.53 "Last close" | $11.53 "last close" | PASS |  |  |
| AVGO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $14.02, -17.8% | $14.02, -17.8% | PASS |  |  |
| AVGO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $13.02, -11.4% | $13.02, -11.4% | PASS |  |  |
| AVGO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.6 | 40.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| AVGO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -12.5% vs +7.0% | -12.5% vs 7.0% | PASS |  |  |
| AVGO.TO | T3w | words "past year" vs the window used | 229 / 251 bars back | 250-253 bars | PASS |  |  |
| AVGO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.2 | 19.1 | PASS |  | Wilder, completed bars |
| AVGO.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.1 | PASS |  |  |
| AVGO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -12.19%, close location 0.07, OBV rising |
| AVGO.TO | V2 | day change of the last completed bar | down 12.2% | -12.19% | PASS |  |  |
| AVGO.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0654) | PASS |  |  |
| AVGO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| AVGO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.00× / 1.90× | 3.00× / 1.90× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| AVGO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3743221) | 20 bars, last ('2026-11-20', 3743221) | PASS |  |  |
| BDT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $69.45 | $69.45 | PASS |  |  |
| BDT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $73.29 | $73.29 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BDT.TO | E3 | percent from the 21-day average | 5.2% below | 5.2% below | PASS |  |  |
| BDT.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BDT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.98 | $3.98 (sr=3.9754) | PASS |  | Wilder ATR14 |
| BDT.TO | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| BDT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $73.29, -5.2% | $73.29, -5.2% | PASS |  |  |
| BDT.TO | L-note | "Last close $X · date" note = last completed bar | Last close $69.45 · Nov 20 | $69.45 · Nov 20 | PASS |  |  |
| BDT.TO | L-now | ladder price row = compared price; name = the basis label | $69.45 "After hours" | $69.45 "after hours" | PASS |  |  |
| BDT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $59.17, 17.4% | $59.17, 17.4% | PASS |  |  |
| BDT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $76.12, -8.8% | $76.12, -8.8% | PASS |  |  |
| BDT.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $69.45 / entry $69.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BDT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BDT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 42.5 | 42.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BDT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +180.2% vs +7.0% | 180.2% vs 7.0% | PASS |  |  |
| BDT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BDT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.0 | 13.0 | PASS |  | Wilder, completed bars |
| BDT.TO | T4w | words "20 or more / below 20" | below 20 | ADX 13.0 | PASS |  |  |
| BDT.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $69.45, Nov 20 | $69.45, Nov 20 | PASS |  |  |
| BDT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $69.45 vs $59.17 · +17.4% | $69.45 vs $59.17 · 17.4% | PASS |  |  |
| BDT.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| BDT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $69.45 vs $76.12 · -8.8% | $69.45 vs $76.12 · -8.8% | PASS |  |  |
| BDT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| BDT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +12.7% over 30 td | +12.7% over 30 td | PASS |  |  |
| BDT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| BDT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BDT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 19.6% below $86.42 | 19.6% below $86.42 | PASS |  | closing high would be 85.33 |
| BDT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 19.6% below | PASS |  |  |
| BDT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $86.42 | $86.42048390957993 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BDT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -2.76%, close location 0.50, OBV falling |
| BDT.TO | V2 | day change of the last completed bar | down 2.8% | -2.76% | PASS |  |  |
| BDT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BDT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.36× / 0.48× | 1.36× / 0.48× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BDT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 573117) | 20 bars, last ('2026-11-20', 573117) | PASS |  |  |
| BOTZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $27.34 | $27.34 | PASS |  |  |
| BOTZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $31.21 | $31.21 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BOTZ | E3 | percent from the 21-day average | 12.4% below | 12.4% below | PASS |  |  |
| BOTZ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BOTZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.87 | $0.87 (sr=0.8689) | PASS |  | Wilder ATR14 |
| BOTZ | E5 | distance in normal day-moves | 4.5 | 4.5 | PASS |  | gauge dot note uses the same number:  · 4.5 day-moves below |
| BOTZ | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.6 | +5.6 | PASS |  |  |
| BOTZ | L-ema21 | ladder row ema21: price and gap = price vs average | $31.21, -12.4% | $31.21, -12.4% | PASS |  |  |
| BOTZ | L-note | "Last close $X · date" note = last completed bar | Last close $27.34 · Nov 20 | $27.34 · Nov 20 | PASS |  |  |
| BOTZ | L-now | ladder price row = compared price; name = the basis label | $27.34 "After hours" | $27.34 "after hours" | PASS |  |  |
| BOTZ | L-sma200 | ladder row sma200: price and gap = price vs average | $36.08, -24.2% | $36.08, -24.2% | PASS |  |  |
| BOTZ | L-sma50 | ladder row sma50: price and gap = price vs average | $33.48, -18.3% | $33.48, -18.3% | PASS |  |  |
| BOTZ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $27.34 / entry $27.34 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BOTZ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BOTZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 23.0 | 23.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BOTZ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -16.9% vs +7.0% | -17.0% vs 7.0% | PASS |  |  |
| BOTZ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BOTZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 37.4 | 37.3 | PASS |  | Wilder, completed bars |
| BOTZ | T4w | words "20 or more / below 20" | 20 or more | ADX 37.3 | PASS |  |  |
| BOTZ | T5 | "counted at the last close ($X, date)" = last completed bar | $27.34, Nov 20 | $27.34, Nov 20 | PASS |  |  |
| BOTZ | T6 | price vs 200-day average (S1 pattern sma values) | $27.34 vs $36.08 · -24.2% | $27.34 vs $36.08 · -24.2% | PASS |  |  |
| BOTZ | T6w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T7 | price vs 50-day average (S1 pattern sma values) | $27.34 vs $33.48 · -18.3% | $27.34 vs $33.48 · -18.3% | PASS |  |  |
| BOTZ | T7w | word "Below" | Below | Below | PASS |  |  |
| BOTZ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.1% over 30 td | -2.1% over 30 td | PASS |  |  |
| BOTZ | T8r | word "rising" | not rising | not rising | PASS |  |  |
| BOTZ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BOTZ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.4% below $41.69 | 34.4% below $41.69 | PASS |  | closing high would be 41.61 |
| BOTZ | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.4% below | PASS |  |  |
| BOTZ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $41.69 | $41.689149923077814 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BOTZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.72%, close location 0.10, OBV falling |
| BOTZ | V2 | day change of the last completed bar | down 5.7% | -5.72% | PASS |  |  |
| BOTZ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1007) | PASS |  |  |
| BOTZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BOTZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.26× / 1.80× | 3.26× / 1.80× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BOTZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 2482146) | 20 bars, last ('2026-11-20', 2482146) | PASS |  |  |
| BOTZ | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.26, OBV falling | condition true | PASS |  |  |
| BRK-B | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $569.59 | $569.59 | PASS |  |  |
| BRK-B | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $567.39 | $567.39 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRK-B | E3 | percent from the 21-day average | 0.4% above | 0.4% above | PASS |  |  |
| BRK-B | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BRK-B | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.65 | $9.65 (sr=9.6499) | PASS |  | Wilder ATR14 |
| BRK-B | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves above |
| BRK-B | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -6.7 | -6.7 | PASS |  |  |
| BRK-B | L-ema21 | ladder row ema21: price and gap = price vs average | $567.39, 0.4% | $567.39, 0.4% | PASS |  |  |
| BRK-B | L-note | "Last close $X · date" note = last completed bar | Last close $570.00 · Nov 20 | $570.00 · Nov 20 | PASS |  |  |
| BRK-B | L-now | ladder price row = compared price; name = the basis label | $569.59 "After hours" | $569.59 "after hours" | PASS |  |  |
| BRK-B | L-sma200 | ladder row sma200: price and gap = price vs average | $502.57, 13.3% | $502.57, 13.3% | PASS |  |  |
| BRK-B | L-sma50 | ladder row sma50: price and gap = price vs average | $536.86, 6.1% | $536.86, 6.1% | PASS |  |  |
| BRK-B | S5-price | S5: the same live price reads the same on the header and the Entry block | header $569.59 / entry $569.59 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRK-B | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRK-B | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 56.6 | 56.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRK-B | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +13.8% vs +7.0% | 13.7% vs 7.0% | PASS |  |  |
| BRK-B | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRK-B | T4 | ADX 14 (S1 /api/sr meta.adx) | 46.9 | 46.9 | PASS |  | Wilder, completed bars |
| BRK-B | T4w | words "20 or more / below 20" | 20 or more | ADX 46.9 | PASS |  |  |
| BRK-B | T5 | "counted at the last close ($X, date)" = last completed bar | $570.00, Nov 20 | $570.00, Nov 20 | PASS |  |  |
| BRK-B | T6 | price vs 200-day average (S1 pattern sma values) | $570.00 vs $502.57 · +13.4% | $570.00 vs $502.57 · 13.4% | PASS |  |  |
| BRK-B | T6w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T7 | price vs 50-day average (S1 pattern sma values) | $570.00 vs $536.86 · +6.2% | $570.00 vs $536.86 · 6.2% | PASS |  |  |
| BRK-B | T7w | word "Above" | Above | Above | PASS |  |  |
| BRK-B | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.9% over 30 td | +1.9% over 30 td | PASS |  |  |
| BRK-B | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRK-B | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRK-B | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.5% below $596.92 | 4.5% below $596.92 | PASS |  | closing high would be 592.94 |
| BRK-B | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.5% below | PASS |  |  |
| BRK-B | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $596.92 | $596.9199829101562 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRK-B | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.36%, close location 0.34, OBV falling |
| BRK-B | V2 | day change of the last completed bar | down 0.4% | -0.36% | PASS |  |  |
| BRK-B | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BRK-B | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.36× / 0.21× | 1.36× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRK-B | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 6712368) | 20 bars, last ('2026-11-20', 6712368) | PASS |  |  |
| BRKU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $28.45 | $28.45 | PASS |  |  |
| BRKU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.32 | $28.32 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| BRKU | E3 | percent from the 21-day average | 0.5% above | 0.5% above | PASS |  |  |
| BRKU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| BRKU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.92 | $0.92 (sr=0.9237) | PASS |  | Wilder ATR14 |
| BRKU | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| BRKU | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.6 | -5.6 | PASS |  |  |
| BRKU | L-ema21 | ladder row ema21: price and gap = price vs average | $28.32, 0.5% | $28.32, 0.5% | PASS |  |  |
| BRKU | L-note | "Last close $X · date" note = last completed bar | Last close $28.45 · Nov 20 | $28.45 · Nov 20 | PASS |  |  |
| BRKU | L-now | ladder price row = compared price; name = the basis label | $28.45 "After hours" | $28.45 "after hours" | PASS |  |  |
| BRKU | L-sma200 | ladder row sma200: price and gap = price vs average | $23.1, 23.2% | $23.10, 23.2% | PASS |  |  |
| BRKU | L-sma50 | ladder row sma50: price and gap = price vs average | $25.56, 11.3% | $25.56, 11.3% | PASS |  |  |
| BRKU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $28.45 / entry $28.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| BRKU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| BRKU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.2 | 55.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| BRKU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +15.2% vs +7.0% | 15.2% vs 7.0% | PASS |  |  |
| BRKU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| BRKU | T4 | ADX 14 (S1 /api/sr meta.adx) | 45.7 | 45.7 | PASS |  | Wilder, completed bars |
| BRKU | T4w | words "20 or more / below 20" | 20 or more | ADX 45.7 | PASS |  |  |
| BRKU | T5 | "counted at the last close ($X, date)" = last completed bar | $28.45, Nov 20 | $28.45, Nov 20 | PASS |  |  |
| BRKU | T6 | price vs 200-day average (S1 pattern sma values) | $28.45 vs $23.10 · +23.2% | $28.45 vs $23.10 · 23.2% | PASS |  |  |
| BRKU | T6w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T7 | price vs 50-day average (S1 pattern sma values) | $28.45 vs $25.56 · +11.3% | $28.45 vs $25.56 · 11.3% | PASS |  |  |
| BRKU | T7w | word "Above" | Above | Above | PASS |  |  |
| BRKU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.6% over 30 td | +2.6% over 30 td | PASS |  |  |
| BRKU | T8r | word "rising" | still rising | rising | PASS |  |  |
| BRKU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| BRKU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.8% below $31.20 | 8.8% below $31.20 | PASS |  | closing high would be 30.81 |
| BRKU | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.8% below | PASS |  |  |
| BRKU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $31.20 | $31.200000762939453 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| BRKU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.35%, close location 0.39, OBV falling |
| BRKU | V2 | day change of the last completed bar | down 0.3% | -0.35% | PASS |  |  |
| BRKU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| BRKU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.93× / 0.11× | 0.93× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| BRKU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 87657) | 20 bars, last ('2026-11-20', 87657) | PASS |  |  |
| CAMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $89.20 | $89.20 | PASS |  |  |
| CAMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $107.01 | $107.01 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAMT | E3 | percent from the 21-day average | 16.6% below | 16.6% below | PASS |  |  |
| CAMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CAMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.16 | $8.16 (sr=8.1575) | PASS |  | Wilder ATR14 |
| CAMT | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| CAMT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.8 | +5.8 | PASS |  |  |
| CAMT | L-ema21 | ladder row ema21: price and gap = price vs average | $107.01, -16.6% | $107.01, -16.6% | PASS |  |  |
| CAMT | L-note | "Last close $X · date" note = last completed bar | Last close $89.20 · Nov 20 | $89.20 · Nov 20 | PASS |  |  |
| CAMT | L-now | ladder price row = compared price; name = the basis label | $89.2 "After hours" | $89.20 "after hours" | PASS |  |  |
| CAMT | L-sma200 | ladder row sma200: price and gap = price vs average | $154.21, -42.2% | $154.21, -42.2% | PASS |  |  |
| CAMT | L-sma50 | ladder row sma50: price and gap = price vs average | $128.61, -30.6% | $128.61, -30.6% | PASS |  |  |
| CAMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $89.20 / entry $89.20 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.7 | 32.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.7% vs +7.0% | -5.7% vs 7.0% | PASS |  |  |
| CAMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.3 | 34.3 | PASS |  | Wilder, completed bars |
| CAMT | T4w | words "20 or more / below 20" | 20 or more | ADX 34.3 | PASS |  |  |
| CAMT | T5 | "counted at the last close ($X, date)" = last completed bar | $89.20, Nov 20 | $89.20, Nov 20 | PASS |  |  |
| CAMT | T6 | price vs 200-day average (S1 pattern sma values) | $89.20 vs $154.21 · -42.2% | $89.20 vs $154.21 · -42.2% | PASS |  |  |
| CAMT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T7 | price vs 50-day average (S1 pattern sma values) | $89.20 vs $128.61 · -30.6% | $89.20 vs $128.61 · -30.6% | PASS |  |  |
| CAMT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.7% over 30 td | -1.7% over 30 td | PASS |  |  |
| CAMT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CAMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 58.7% below $215.99 | 58.7% below $215.99 | PASS |  | closing high would be 207.46 |
| CAMT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 58.7% below | PASS |  |  |
| CAMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $215.99 | $215.99000549316406 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -8.77%, close location 0.19, OBV falling |
| CAMT | V2 | day change of the last completed bar | down 8.8% | -8.77% | PASS |  |  |
| CAMT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.19 (raw 0.1917) | PASS |  |  |
| CAMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.88× / 0.96× | 0.88× / 0.96× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 463426) | 20 bars, last ('2026-11-20', 463426) | PASS |  |  |
| CARS.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $18.07 | $18.07 | PASS |  |  |
| CARS.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $21.17 | $21.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CARS.TO | E3 | percent from the 21-day average | 14.6% below | 14.6% below | PASS |  |  |
| CARS.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| CARS.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.54 | $0.54 (sr=0.5436) | PASS |  | Wilder ATR14 |
| CARS.TO | E5 | distance in normal day-moves | 5.7 | 5.7 | PASS |  | gauge dot note uses the same number:  ◂ · 5.7 day-moves below |
| CARS.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.1 | +4.1 | PASS |  |  |
| CARS.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.3 | +12.3 | PASS |  |  |
| CARS.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $21.17, -14.6% | $21.17, -14.6% | PASS |  |  |
| CARS.TO | L-now | ladder price row = compared price; name = the basis label | $18.07 "Last close" | $18.07 "last close" | PASS |  |  |
| CARS.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $27.86, -35.1% | $27.86, -35.1% | PASS |  |  |
| CARS.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $23.39, -22.7% | $23.39, -22.7% | PASS |  |  |
| CARS.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CARS.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 23.2 | 23.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CARS.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -27.3% vs +7.0% | -27.3% vs 7.0% | PASS |  |  |
| CARS.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CARS.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.2 | 31.3 | PASS |  | Wilder, completed bars |
| CARS.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 31.3 | PASS |  |  |
| CARS.TO | T6 | price vs 200-day average (S1 pattern sma values) | $18.07 vs $27.86 · -35.1% | $18.07 vs $27.86 · -35.1% | PASS |  |  |
| CARS.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CARS.TO | T7 | price vs 50-day average (S1 pattern sma values) | $18.07 vs $23.38 · -22.7% | $18.07 vs $23.39 · -22.7% | PASS |  |  |
| CARS.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CARS.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.8% over 30 td | -2.7% over 30 td | PASS |  |  |
| CARS.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CARS.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CARS.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 52.6% below $38.16 | 52.6% below $38.16 | PASS |  | closing high would be 38.16 |
| CARS.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 52.6% below | PASS |  |  |
| CARS.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.16 | $38.158966064453125 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CARS.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 11 of 50 days empty | 11 of 50 days empty | PASS |  |  |
| CAT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $510.45 | $510.45 | PASS |  |  |
| CAT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $608.01 | $608.01 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CAT | E3 | percent from the 21-day average | 16.0% below | 16.0% below | PASS |  |  |
| CAT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CAT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $28.93 | $28.93 (sr=28.927) | PASS |  | Wilder ATR14 |
| CAT | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| CAT | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.6 | +3.6 | PASS |  |  |
| CAT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.7 | +6.7 | PASS |  |  |
| CAT | L-ema21 | ladder row ema21: price and gap = price vs average | $608.01, -16.0% | $608.01, -16.0% | PASS |  |  |
| CAT | L-note | "Last close $X · date" note = last completed bar | Last close $510.63 · Nov 20 | $510.63 · Nov 20 | PASS |  |  |
| CAT | L-now | ladder price row = compared price; name = the basis label | $510.45 "After hours" | $510.45 "after hours" | PASS |  |  |
| CAT | L-sma200 | ladder row sma200: price and gap = price vs average | $801.11, -36.3% | $801.11, -36.3% | PASS |  |  |
| CAT | L-sma50 | ladder row sma50: price and gap = price vs average | $713.1, -28.4% | $713.10, -28.4% | PASS |  |  |
| CAT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $510.45 / entry $510.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CAT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CAT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 24.2 | 24.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CAT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.7% vs +7.0% | -5.7% vs 7.0% | PASS |  |  |
| CAT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CAT | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.8 | 40.8 | PASS |  | Wilder, completed bars |
| CAT | T4w | words "20 or more / below 20" | 20 or more | ADX 40.8 | PASS |  |  |
| CAT | T5 | "counted at the last close ($X, date)" = last completed bar | $510.63, Nov 20 | $510.63, Nov 20 | PASS |  |  |
| CAT | T6 | price vs 200-day average (S1 pattern sma values) | $510.63 vs $801.11 · -36.3% | $510.63 vs $801.11 · -36.3% | PASS |  |  |
| CAT | T6w | word "Below" | Below | Below | PASS |  |  |
| CAT | T7 | price vs 50-day average (S1 pattern sma values) | $510.63 vs $713.10 · -28.4% | $510.63 vs $713.10 · -28.4% | PASS |  |  |
| CAT | T7w | word "Below" | Below | Below | PASS |  |  |
| CAT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.4% over 30 td | +0.4% over 30 td | PASS |  |  |
| CAT | T8r | word "rising" | still rising | rising | PASS |  |  |
| CAT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CAT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 52.2% below $1,068.94 | 52.2% below $1068.94 | PASS |  | closing high would be 1060.42 |
| CAT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 52.2% below | PASS |  |  |
| CAT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,068.94 | $1068.93972 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CAT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.98%, close location 0.08, OBV falling |
| CAT | V2 | day change of the last completed bar | down 5.0% | -4.98% | PASS |  |  |
| CAT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0804) | PASS |  |  |
| CAT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CAT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.69× / 0.88× | 2.69× / 0.88× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CAT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 8840769) | 20 bars, last ('2026-11-20', 8840769) | PASS |  |  |
| CAT | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.69, OBV falling | condition true | PASS |  |  |
| CCO.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $83.11 | $83.11 | PASS |  |  |
| CCO.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $100.81 | $100.81 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CCO.TO | E3 | percent from the 21-day average | 17.6% below | 17.6% below | PASS |  |  |
| CCO.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CCO.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.83 | $4.83 (sr=4.8345) | PASS |  | Wilder ATR14 |
| CCO.TO | E5 | distance in normal day-moves | 3.7 | 3.7 | PASS |  | gauge dot note uses the same number:  · 3.7 day-moves below |
| CCO.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.0 | +8.0 | PASS |  |  |
| CCO.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $100.81, -17.6% | $100.81, -17.6% | PASS |  |  |
| CCO.TO | L-note | "Last close $X · date" note = last completed bar | Last close $83.11 · Nov 20 | $83.11 · Nov 20 | PASS |  |  |
| CCO.TO | L-now | ladder price row = compared price; name = the basis label | $83.11 "After hours" | $83.11 "after hours" | PASS |  |  |
| CCO.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $139.73, -40.5% | $139.73, -40.5% | PASS |  |  |
| CCO.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $114.68, -27.5% | $114.68, -27.5% | PASS |  |  |
| CCO.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $83.11 / entry $83.11 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CCO.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CCO.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 25.2 | 25.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CCO.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -28.0% vs +7.0% | -28.0% vs 7.0% | PASS |  |  |
| CCO.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CCO.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.7 | 33.7 | PASS |  | Wilder, completed bars |
| CCO.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 33.7 | PASS |  |  |
| CCO.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $83.11, Nov 20 | $83.11, Nov 20 | PASS |  |  |
| CCO.TO | T6 | price vs 200-day average (S1 pattern sma values) | $83.11 vs $139.73 · -40.5% | $83.11 vs $139.73 · -40.5% | PASS |  |  |
| CCO.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CCO.TO | T7 | price vs 50-day average (S1 pattern sma values) | $83.11 vs $114.68 · -27.5% | $83.11 vs $114.68 · -27.5% | PASS |  |  |
| CCO.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CCO.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.7% over 30 td | -4.7% over 30 td | PASS |  |  |
| CCO.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CCO.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CCO.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 54.5% below $182.72 | 54.5% below $182.72 | PASS |  | closing high would be 181.66 |
| CCO.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 54.5% below | PASS |  |  |
| CCO.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $182.72 | $182.72000122070312 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CCO.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.72%, close location 0.01, OBV falling |
| CCO.TO | V2 | day change of the last completed bar | down 5.7% | -5.72% | PASS |  |  |
| CCO.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0097) | PASS |  |  |
| CCO.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CCO.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.62× / 0.98× | 1.62× / 0.98× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CCO.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 2101355) | 20 bars, last ('2026-11-20', 2101355) | PASS |  |  |
| CCO.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.62, OBV falling | condition true | PASS |  |  |
| CEG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $237.41 | $237.41 | PASS |  |  |
| CEG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $263.04 | $263.04 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CEG | E3 | percent from the 21-day average | 9.7% below | 9.7% below | PASS |  |  |
| CEG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CEG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $13.30 | $13.30 (sr=13.3014) | PASS |  | Wilder ATR14 |
| CEG | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| CEG | L-ema21 | ladder row ema21: price and gap = price vs average | $263.04, -9.7% | $263.04, -9.7% | PASS |  |  |
| CEG | L-note | "Last close $X · date" note = last completed bar | Last close $237.41 · Nov 20 | $237.41 · Nov 20 | PASS |  |  |
| CEG | L-now | ladder price row = compared price; name = the basis label | $237.41 "After hours" | $237.41 "after hours" | PASS |  |  |
| CEG | L-sma200 | ladder row sma200: price and gap = price vs average | $277.41, -14.4% | $277.41, -14.4% | PASS |  |  |
| CEG | L-sma50 | ladder row sma50: price and gap = price vs average | $265.85, -10.7% | $265.85, -10.7% | PASS |  |  |
| CEG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $237.41 / entry $237.41 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CEG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CEG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.5 | 37.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CEG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -30.9% vs +7.0% | -30.9% vs 7.0% | PASS |  |  |
| CEG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CEG | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.8 | 13.8 | PASS |  | Wilder, completed bars |
| CEG | T4w | words "20 or more / below 20" | below 20 | ADX 13.8 | PASS |  |  |
| CEG | T5 | "counted at the last close ($X, date)" = last completed bar | $237.41, Nov 20 | $237.41, Nov 20 | PASS |  |  |
| CEG | T6 | price vs 200-day average (S1 pattern sma values) | $237.41 vs $277.41 · -14.4% | $237.41 vs $277.41 · -14.4% | PASS |  |  |
| CEG | T6w | word "Below" | Below | Below | PASS |  |  |
| CEG | T7 | price vs 50-day average (S1 pattern sma values) | $237.41 vs $265.85 · -10.7% | $237.41 vs $265.85 · -10.7% | PASS |  |  |
| CEG | T7w | word "Below" | Below | Below | PASS |  |  |
| CEG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.7% over 30 td | -2.7% over 30 td | PASS |  |  |
| CEG | T8r | word "rising" | not rising | not rising | PASS |  |  |
| CEG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CEG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 37.3% below $378.52 | 37.3% below $378.52 | PASS |  | closing high would be 376.35 |
| CEG | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 37.3% below | PASS |  |  |
| CEG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $378.52 | $378.52001655537043 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CEG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.80%, close location 0.05, OBV falling |
| CEG | V2 | day change of the last completed bar | down 5.8% | -5.80% | PASS |  |  |
| CEG | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0463) | PASS |  |  |
| CEG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CEG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.41× / 1.04× | 1.41× / 1.04× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CEG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 5488389) | 20 bars, last ('2026-11-20', 5488389) | PASS |  |  |
| CGY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $78.75 | $78.75 | PASS |  |  |
| CGY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $84.31 | $84.31 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CGY.TO | E3 | percent from the 21-day average | 6.6% below | 6.6% below | PASS |  |  |
| CGY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CGY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.58 | $2.58 (sr=2.5821) | PASS |  | Wilder ATR14 |
| CGY.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| CGY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $84.31, -6.6% | $84.31, -6.6% | PASS |  |  |
| CGY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $78.75 · Nov 20 | $78.75 · Nov 20 | PASS |  |  |
| CGY.TO | L-now | ladder price row = compared price; name = the basis label | $78.75 "After hours" | $78.75 "after hours" | PASS |  |  |
| CGY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $79.07, -0.4% | $79.07, -0.4% | PASS |  |  |
| CGY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $83.52, -5.7% | $83.52, -5.7% | PASS |  |  |
| CGY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $78.75 / entry $78.75 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CGY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CGY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.6 | 36.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CGY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +70.8% vs +7.0% | 70.8% vs 7.0% | PASS |  |  |
| CGY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CGY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.1 | 16.1 | PASS |  | Wilder, completed bars |
| CGY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 16.1 | PASS |  |  |
| CGY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $78.75, Nov 20 | $78.75, Nov 20 | PASS |  |  |
| CGY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $78.75 vs $79.07 · -0.4% | $78.75 vs $79.07 · -0.4% | PASS |  |  |
| CGY.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CGY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $78.75 vs $83.52 · -5.7% | $78.75 vs $83.52 · -5.7% | PASS |  |  |
| CGY.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CGY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.9% over 30 td | +4.9% over 30 td | PASS |  |  |
| CGY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CGY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CGY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 17.2% below $95.15 | 17.2% below $95.15 | PASS |  | closing high would be 91.80 |
| CGY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 17.2% below | PASS |  |  |
| CGY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $95.15 | $95.15474299571112 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CGY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.45%, close location 0.18, OBV falling |
| CGY.TO | V2 | day change of the last completed bar | down 3.5% | -3.45% | PASS |  |  |
| CGY.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.18 (raw 0.1827) | PASS |  |  |
| CGY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CGY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.62× / 1.05× | 1.62× / 1.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CGY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 50000) | 20 bars, last ('2026-11-20', 50000) | PASS |  |  |
| CGY.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.62, OBV falling | condition true | PASS |  |  |
| CNQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $63.74 | $63.74 | PASS |  |  |
| CNQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $69.48 | $69.48 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNQ.TO | E3 | percent from the 21-day average | 8.3% below | 8.3% below | PASS |  |  |
| CNQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| CNQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.02 | $2.02 (sr=2.0241) | PASS |  | Wilder ATR14 |
| CNQ.TO | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| CNQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $69.48, -8.3% | $69.48, -8.3% | PASS |  |  |
| CNQ.TO | L-now | ladder price row = compared price; name = the basis label | $63.74 "Last close" | $63.74 "last close" | PASS |  |  |
| CNQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.35, -1.0% | $64.35, -1.0% | PASS |  |  |
| CNQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $70.82, -10.0% | $70.82, -10.0% | PASS |  |  |
| CNQ.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.4 | 29.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +38.7% vs +7.0% | 38.7% vs 7.0% | PASS |  |  |
| CNQ.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.4 | 32.4 | PASS |  | Wilder, completed bars |
| CNQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.4 | PASS |  |  |
| CNQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $63.74 vs $64.35 · -0.9% | $63.74 vs $64.35 · -1.0% | PASS |  |  |
| CNQ.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| CNQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $63.74 vs $70.82 · -10.0% | $63.74 vs $70.82 · -10.0% | PASS |  |  |
| CNQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CNQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.5% over 30 td | +6.5% over 30 td | PASS |  |  |
| CNQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 18.9% below $78.60 | 18.9% below $78.60 | PASS |  | closing high would be 78.42 |
| CNQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 18.9% below | PASS |  |  |
| CNQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $78.60 | $78.5999984741211 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.56%, close location 0.32, OBV falling |
| CNQ.TO | V2 | day change of the last completed bar | down 0.6% | -0.56% | PASS |  |  |
| CNQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CNQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.66× / 0.18× | 1.66× / 0.18× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 19860578) | 20 bars, last ('2026-11-20', 19860578) | PASS |  |  |
| CNQ.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.66, OBV falling | condition true | PASS |  |  |
| CNR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $175.38 | $175.38 | PASS |  |  |
| CNR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $177.5 | $177.50 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CNR.TO | E3 | percent from the 21-day average | 1.2% below | 1.2% below | PASS |  |  |
| CNR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CNR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.26 | $3.26 (sr=3.2638) | PASS |  | Wilder ATR14 |
| CNR.TO | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| CNR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $177.5, -1.2% | $177.50, -1.2% | PASS |  |  |
| CNR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $175.38 · Nov 20 | $175.38 · Nov 20 | PASS |  |  |
| CNR.TO | L-now | ladder price row = compared price; name = the basis label | $175.38 "After hours" | $175.38 "after hours" | PASS |  |  |
| CNR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $162.44, 8.0% | $162.44, 8.0% | PASS |  |  |
| CNR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $172.84, 1.5% | $172.84, 1.5% | PASS |  |  |
| CNR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $175.38 / entry $175.38 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CNR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CNR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 47.1 | 47.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CNR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +38.3% vs +7.0% | 38.3% vs 7.0% | PASS |  |  |
| CNR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CNR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.6 | 20.6 | PASS |  | Wilder, completed bars |
| CNR.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 20.6 | PASS |  |  |
| CNR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $175.38, Nov 20 | $175.38, Nov 20 | PASS |  |  |
| CNR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $175.38 vs $162.44 · +8.0% | $175.38 vs $162.44 · 8.0% | PASS |  |  |
| CNR.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $175.38 vs $172.84 · +1.5% | $175.38 vs $172.84 · 1.5% | PASS |  |  |
| CNR.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| CNR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.0% over 30 td | +4.0% over 30 td | PASS |  |  |
| CNR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CNR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CNR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.8% below $184.26 | 4.8% below $184.26 | PASS |  | closing high would be 182.93 |
| CNR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.8% below | PASS |  |  |
| CNR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $184.26 | $184.25630798377267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CNR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.84%, close location 0.01, OBV falling |
| CNR.TO | V2 | day change of the last completed bar | down 1.8% | -1.84% | PASS |  |  |
| CNR.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0095) | PASS |  |  |
| CNR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CNR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.58× / 0.99× | 1.58× / 0.99× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CNR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 1920561) | 20 bars, last ('2026-11-20', 1920561) | PASS |  |  |
| CNR.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.58, OBV falling | condition true | PASS |  |  |
| COP | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $136.12 | $136.12 | PASS |  |  |
| COP | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $138.64 | $138.64 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COP | E3 | percent from the 21-day average | 1.8% below | 1.8% below | PASS |  |  |
| COP | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COP | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.87 | $3.87 (sr=3.8716) | PASS |  | Wilder ATR14 |
| COP | E5 | distance in normal day-moves | 0.7 | 0.7 | PASS |  | gauge dot note uses the same number:  · 0.7 day-moves below |
| COP | L-ema21 | ladder row ema21: price and gap = price vs average | $138.64, -1.8% | $138.64, -1.8% | PASS |  |  |
| COP | L-note | "Last close $X · date" note = last completed bar | Last close $136.12 · Nov 20 | $136.12 · Nov 20 | PASS |  |  |
| COP | L-now | ladder price row = compared price; name = the basis label | $136.12 "After hours" | $136.12 "after hours" | PASS |  |  |
| COP | L-sma200 | ladder row sma200: price and gap = price vs average | $122.53, 11.1% | $122.53, 11.1% | PASS |  |  |
| COP | L-sma50 | ladder row sma50: price and gap = price vs average | $136.59, -0.3% | $136.59, -0.3% | PASS |  |  |
| COP | S5-price | S5: the same live price reads the same on the header and the Entry block | header $136.12 / entry $136.12 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COP | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COP | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 45.6 | 45.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COP | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +60.1% vs +7.0% | 60.1% vs 7.0% | PASS |  |  |
| COP | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COP | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.8 | 21.8 | PASS |  | Wilder, completed bars |
| COP | T4w | words "20 or more / below 20" | 20 or more | ADX 21.8 | PASS |  |  |
| COP | T5 | "counted at the last close ($X, date)" = last completed bar | $136.12, Nov 20 | $136.12, Nov 20 | PASS |  |  |
| COP | T6 | price vs 200-day average (S1 pattern sma values) | $136.12 vs $122.53 · +11.1% | $136.12 vs $122.53 · 11.1% | PASS |  |  |
| COP | T6w | word "Above" | Above | Above | PASS |  |  |
| COP | T7 | price vs 50-day average (S1 pattern sma values) | $136.12 vs $136.59 · -0.3% | $136.12 vs $136.59 · -0.3% | PASS |  |  |
| COP | T7w | word "Below" | Below | Below | PASS |  |  |
| COP | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +6.0% over 30 td | +6.0% over 30 td | PASS |  |  |
| COP | T8r | word "rising" | still rising | rising | PASS |  |  |
| COP | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COP | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.2% below $153.27 | 11.2% below $153.27 | PASS |  | closing high would be 153.02 |
| COP | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.2% below | PASS |  |  |
| COP | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $153.27 | $153.2715592533114 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COP | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 0.84%, close location 0.52, OBV falling |
| COP | V2 | day change of the last completed bar | up 0.8% | +0.84% | PASS |  |  |
| COP | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COP | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.22× / 0.30× | 1.22× / 0.29× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COP | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 8467491) | 20 bars, last ('2026-11-20', 8467491) | PASS |  |  |
| COPP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $39.49 | $39.49 | PASS |  |  |
| COPP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $49.41 | $49.41 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPP.TO | E3 | percent from the 21-day average | 20.1% below | 20.1% below | PASS |  |  |
| COPP.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| COPP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.19 | $2.19 (sr=2.1938) | PASS |  | Wilder ATR14 |
| COPP.TO | E5 | distance in normal day-moves | 4.5 | 4.5 | PASS |  | gauge dot note uses the same number:  · 4.5 day-moves below |
| COPP.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.1 | +4.1 | PASS |  |  |
| COPP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $49.41, -20.1% | $49.41, -20.1% | PASS |  |  |
| COPP.TO | L-now | ladder price row = compared price; name = the basis label | $39.49 "Last close" | $39.49 "last close" | PASS |  |  |
| COPP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $58.32, -32.3% | $58.32, -32.3% | PASS |  |  |
| COPP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $55.92, -29.4% | $55.92, -29.4% | PASS |  |  |
| COPP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.6 | 22.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -6.4% vs +7.0% | -6.4% vs 7.0% | PASS |  |  |
| COPP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.3 | 35.3 | PASS |  | Wilder, completed bars |
| COPP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 35.3 | PASS |  |  |
| COPP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $39.49 vs $58.32 · -32.3% | $39.49 vs $58.32 · -32.3% | PASS |  |  |
| COPP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $39.49 vs $55.92 · -29.4% | $39.49 vs $55.92 · -29.4% | PASS |  |  |
| COPP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| COPP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.5% over 30 td | -1.5% over 30 td | PASS |  |  |
| COPP.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 44.0% below $70.54 | 44.0% below $70.54 | PASS |  | closing high would be 68.98 |
| COPP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 44.0% below | PASS |  |  |
| COPP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $70.54 | $70.54000091552734 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.59%, close location 0.00, OBV falling |
| COPP.TO | V2 | day change of the last completed bar | down 5.6% | -5.59% | PASS |  |  |
| COPP.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| COPP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 4.67× / 1.01× | 4.67× / 1.01× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 70695) | 20 bars, last ('2026-11-20', 70695) | PASS |  |  |
| COPP.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 4.67, OBV falling | condition true | PASS |  |  |
| COPX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $56.33 | $56.33 | PASS |  |  |
| COPX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $69.54 | $69.54 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPX | E3 | percent from the 21-day average | 19.0% below | 19.0% below | PASS |  |  |
| COPX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COPX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.93 | $2.93 (sr=2.9315) | PASS |  | Wilder ATR14 |
| COPX | E5 | distance in normal day-moves | 4.5 | 4.5 | PASS |  | gauge dot note uses the same number:  · 4.5 day-moves below |
| COPX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.3 | +4.3 | PASS |  |  |
| COPX | L-ema21 | ladder row ema21: price and gap = price vs average | $69.54, -19.0% | $69.54, -19.0% | PASS |  |  |
| COPX | L-note | "Last close $X · date" note = last completed bar | Last close $56.33 · Nov 20 | $56.33 · Nov 20 | PASS |  |  |
| COPX | L-now | ladder price row = compared price; name = the basis label | $56.33 "After hours" | $56.33 "after hours" | PASS |  |  |
| COPX | L-sma200 | ladder row sma200: price and gap = price vs average | $82.01, -31.3% | $82.01, -31.3% | PASS |  |  |
| COPX | L-sma50 | ladder row sma50: price and gap = price vs average | $78.29, -28.0% | $78.29, -28.0% | PASS |  |  |
| COPX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $56.33 / entry $56.33 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COPX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.3 | 22.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.7% vs +7.0% | 0.7% vs 7.0% | PASS |  |  |
| COPX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COPX | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.9 | 30.8 | PASS |  | Wilder, completed bars |
| COPX | T4w | words "20 or more / below 20" | 20 or more | ADX 30.8 | PASS |  |  |
| COPX | T5 | "counted at the last close ($X, date)" = last completed bar | $56.33, Nov 20 | $56.33, Nov 20 | PASS |  |  |
| COPX | T6 | price vs 200-day average (S1 pattern sma values) | $56.33 vs $82.01 · -31.3% | $56.33 vs $82.01 · -31.3% | PASS |  |  |
| COPX | T6w | word "Below" | Below | Below | PASS |  |  |
| COPX | T7 | price vs 50-day average (S1 pattern sma values) | $56.33 vs $78.29 · -28.0% | $56.33 vs $78.29 · -28.0% | PASS |  |  |
| COPX | T7w | word "Below" | Below | Below | PASS |  |  |
| COPX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.3% over 30 td | -1.3% over 30 td | PASS |  |  |
| COPX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| COPX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COPX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 43.5% below $99.65 | 43.5% below $99.65 | PASS |  | closing high would be 96.45 |
| COPX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 43.5% below | PASS |  |  |
| COPX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $99.65 | $99.65136047369408 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COPX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.98%, close location 0.06, OBV falling |
| COPX | V2 | day change of the last completed bar | down 5.0% | -4.98% | PASS |  |  |
| COPX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0588) | PASS |  |  |
| COPX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.26× / 0.96× | 2.26× / 0.96× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 6871593) | 20 bars, last ('2026-11-20', 6871593) | PASS |  |  |
| COPX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.26, OBV falling | condition true | PASS |  |  |
| COPZ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $6.33 | $6.33 | PASS |  |  |
| COPZ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $10.05 | $10.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COPZ | E3 | percent from the 21-day average | 37.0% below | 37.0% below | PASS |  |  |
| COPZ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COPZ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.80 | $0.81 (sr=0.8045) | PASS |  | Wilder ATR14 |
| COPZ | E5 | distance in normal day-moves | 4.6 | 4.6 | PASS |  | gauge dot note uses the same number:  · 4.6 day-moves below |
| COPZ | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| COPZ | L-ema21 | ladder row ema21: price and gap = price vs average | $10.05, -37.0% | $10.05, -37.0% | PASS |  |  |
| COPZ | L-note | "Last close $X · date" note = last completed bar | Last close $6.33 · Nov 20 | $6.33 · Nov 20 | PASS |  |  |
| COPZ | L-now | ladder price row = compared price; name = the basis label | $6.33 "After hours" | $6.33 "after hours" | PASS |  |  |
| COPZ | L-sma50 | ladder row sma50: price and gap = price vs average | $13.03, -51.4% | $13.03, -51.4% | PASS |  |  |
| COPZ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $6.33 / entry $6.33 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COPZ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 23.1 | 23.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COPZ | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.4 | 31.4 | PASS |  | Wilder, completed bars |
| COPZ | T4w | words "20 or more / below 20" | 20 or more | ADX 31.4 | PASS |  |  |
| COPZ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.34%, close location 0.00, OBV falling |
| COPZ | V2 | day change of the last completed bar | down 10.3% | -10.34% | PASS |  |  |
| COPZ | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| COPZ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| COPZ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.96× / 0.81× | 2.96× / 0.81× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COPZ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 36946) | 20 bars, last ('2026-11-20', 36946) | PASS |  |  |
| COPZ | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.96, OBV falling | condition true | PASS |  |  |
| COST | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,102.15 | $1,102.15 | PASS |  |  |
| COST | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1060.62 | $1060.62 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COST | E3 | percent from the 21-day average | 3.9% above | 3.9% above | PASS |  |  |
| COST | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COST | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $19.08 | $19.08 (sr=19.0753) | PASS |  | Wilder ATR14 |
| COST | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves above |
| COST | L-ema21 | ladder row ema21: price and gap = price vs average | $1060.62, 3.9% | $1060.62, 3.9% | PASS |  |  |
| COST | L-note | "Last close $X · date" note = last completed bar | Last close $1,102.15 · Nov 20 | $1,102.15 · Nov 20 | PASS |  |  |
| COST | L-now | ladder price row = compared price; name = the basis label | $1102.15 "After hours" | $1102.15 "after hours" | PASS |  |  |
| COST | L-sma200 | ladder row sma200: price and gap = price vs average | $979, 12.6% | $979.00, 12.6% | PASS |  |  |
| COST | L-sma50 | ladder row sma50: price and gap = price vs average | $986.73, 11.7% | $986.73, 11.7% | PASS |  |  |
| COST | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,102.15 / entry $1,102.15 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COST | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COST | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 69.6 | 69.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COST | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +23.4% vs +7.0% | 23.4% vs 7.0% | PASS |  |  |
| COST | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COST | T4 | ADX 14 (S1 /api/sr meta.adx) | 52.3 | 52.3 | PASS |  | Wilder, completed bars |
| COST | T4w | words "20 or more / below 20" | 20 or more | ADX 52.3 | PASS |  |  |
| COST | T5 | "counted at the last close ($X, date)" = last completed bar | $1,102.15, Nov 20 | $1102.15, Nov 20 | PASS |  |  |
| COST | T6 | price vs 200-day average (S1 pattern sma values) | $1,102.15 vs $979.00 · +12.6% | $1102.15 vs $979.00 · 12.6% | PASS |  |  |
| COST | T6w | word "Above" | Above | Above | PASS |  |  |
| COST | T7 | price vs 50-day average (S1 pattern sma values) | $1,102.15 vs $986.73 · +11.7% | $1102.15 vs $986.73 · 11.7% | PASS |  |  |
| COST | T7w | word "Above" | Above | Above | PASS |  |  |
| COST | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.6% over 30 td | PASS |  |  |
| COST | T8r | word "rising" | still rising | rising | PASS |  |  |
| COST | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COST | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.9% below $1,123.67 | 1.9% below $1123.67 | PASS |  | closing high would be 1113.74 |
| COST | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.9% below | PASS |  |  |
| COST | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,123.67 | $1123.6699 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COST | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.76%, close location 0.15, OBV rising |
| COST | V2 | day change of the last completed bar | up 0.8% | +0.76% | PASS |  |  |
| COST | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1498) | PASS |  |  |
| COST | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COST | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.71× / 0.44× | 1.71× / 0.44× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COST | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 4133482) | 20 bars, last ('2026-11-20', 4133482) | PASS |  |  |
| COTG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $16.69 | $16.69 | PASS |  |  |
| COTG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $15.56 | $15.56 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| COTG | E3 | percent from the 21-day average | 7.3% above | 7.3% above | PASS |  |  |
| COTG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| COTG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.53 | $0.53 (sr=0.5268) | PASS |  | Wilder ATR14 |
| COTG | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves above |
| COTG | L-ema21 | ladder row ema21: price and gap = price vs average | $15.56, 7.3% | $15.56, 7.3% | PASS |  |  |
| COTG | L-note | "Last close $X · date" note = last completed bar | Last close $16.69 · Nov 20 | $16.69 · Nov 20 | PASS |  |  |
| COTG | L-now | ladder price row = compared price; name = the basis label | $16.69 "After hours" | $16.69 "after hours" | PASS |  |  |
| COTG | L-sma200 | ladder row sma200: price and gap = price vs average | $13.94, 19.7% | $13.94, 19.7% | PASS |  |  |
| COTG | L-sma50 | ladder row sma50: price and gap = price vs average | $13.59, 22.8% | $13.59, 22.8% | PASS |  |  |
| COTG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $16.69 / entry $16.69 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| COTG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| COTG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 68.0 | 68.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| COTG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +32.6% vs +7.0% | 32.6% vs 7.0% | PASS |  |  |
| COTG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| COTG | T4 | ADX 14 (S1 /api/sr meta.adx) | 50.9 | 50.8 | PASS |  | Wilder, completed bars |
| COTG | T4w | words "20 or more / below 20" | 20 or more | ADX 50.8 | PASS |  |  |
| COTG | T5 | "counted at the last close ($X, date)" = last completed bar | $16.69, Nov 20 | $16.69, Nov 20 | PASS |  |  |
| COTG | T6 | price vs 200-day average (S1 pattern sma values) | $16.69 vs $13.94 · +19.7% | $16.69 vs $13.94 · 19.7% | PASS |  |  |
| COTG | T6w | word "Above" | Above | Above | PASS |  |  |
| COTG | T7 | price vs 50-day average (S1 pattern sma values) | $16.69 vs $13.59 · +22.8% | $16.69 vs $13.59 · 22.8% | PASS |  |  |
| COTG | T7w | word "Above" | Above | Above | PASS |  |  |
| COTG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.5% over 30 td | +1.6% over 30 td | PASS |  |  |
| COTG | T8r | word "rising" | still rising | rising | PASS |  |  |
| COTG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| COTG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.2% below $17.80 | 6.2% below $17.80 | PASS |  | closing high would be 17.70 |
| COTG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.2% below | PASS |  |  |
| COTG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $17.80 | $17.80299949645996 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| COTG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 1.46%, close location 0.12, OBV rising |
| COTG | V2 | day change of the last completed bar | up 1.5% | +1.46% | PASS |  |  |
| COTG | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1194) | PASS |  |  |
| COTG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| COTG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.97× / 0.47× | 0.97× / 0.46× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| COTG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 100894) | 20 bars, last ('2026-11-20', 100894) | PASS |  |  |
| CSU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3,096.00 | $3,096.00 | PASS |  |  |
| CSU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3324.25 | $3324.25 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CSU.TO | E3 | percent from the 21-day average | 6.9% below | 6.9% below | PASS |  |  |
| CSU.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CSU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $126.09 | $126.09 (sr=126.0881) | PASS |  | Wilder ATR14 |
| CSU.TO | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| CSU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $3324.25, -6.9% | $3324.25, -6.9% | PASS |  |  |
| CSU.TO | L-note | "Last close $X · date" note = last completed bar | Last close $3,096.00 · Nov 20 | $3,096.00 · Nov 20 | PASS |  |  |
| CSU.TO | L-now | ladder price row = compared price; name = the basis label | $3096 "After hours" | $3096.00 "after hours" | PASS |  |  |
| CSU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $2824.78, 9.6% | $2824.78, 9.6% | PASS |  |  |
| CSU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $3149.79, -1.7% | $3149.79, -1.7% | PASS |  |  |
| CSU.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3,096.00 / entry $3,096.00 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CSU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CSU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.8 | 35.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CSU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -3.7% vs +7.0% | -3.7% vs 7.0% | PASS |  |  |
| CSU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CSU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.4 | 30.4 | PASS |  | Wilder, completed bars |
| CSU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 30.4 | PASS |  |  |
| CSU.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $3,096.00, Nov 20 | $3096.00, Nov 20 | PASS |  |  |
| CSU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $3,096.00 vs $2,824.78 · +9.6% | $3096.00 vs $2824.78 · 9.6% | PASS |  |  |
| CSU.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| CSU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $3,096.00 vs $3,149.79 · -1.7% | $3096.00 vs $3149.79 · -1.7% | PASS |  |  |
| CSU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| CSU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.0% over 30 td | +2.0% over 30 td | PASS |  |  |
| CSU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| CSU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CSU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.2% below $3,565.00 | 13.2% below $3565.00 | PASS |  | closing high would be 3526.52 |
| CSU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.2% below | PASS |  |  |
| CSU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $3,565.00 | $3565 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CSU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.64%, close location 0.21, OBV falling |
| CSU.TO | V2 | day change of the last completed bar | down 2.6% | -2.64% | PASS |  |  |
| CSU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.21 (raw 0.2089) | PASS |  |  |
| CSU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| CSU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.80× / 0.65× | 1.80× / 0.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CSU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 112091) | 20 bars, last ('2026-11-20', 112091) | PASS |  |  |
| CSU.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.80, OBV falling | condition true | PASS |  |  |
| CVX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $208.37 | $208.37 | PASS |  |  |
| CVX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $214.25 | $214.25 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| CVX | E3 | percent from the 21-day average | 2.7% below | 2.7% below | PASS |  |  |
| CVX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| CVX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.86 | $4.86 (sr=4.8593) | PASS |  | Wilder ATR14 |
| CVX | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| CVX | L-ema21 | ladder row ema21: price and gap = price vs average | $214.25, -2.7% | $214.25, -2.7% | PASS |  |  |
| CVX | L-note | "Last close $X · date" note = last completed bar | Last close $208.37 · Nov 20 | $208.37 · Nov 20 | PASS |  |  |
| CVX | L-now | ladder price row = compared price; name = the basis label | $208.37 "After hours" | $208.37 "after hours" | PASS |  |  |
| CVX | L-sma200 | ladder row sma200: price and gap = price vs average | $193.3, 7.8% | $193.30, 7.8% | PASS |  |  |
| CVX | L-sma50 | ladder row sma50: price and gap = price vs average | $213.71, -2.5% | $213.71, -2.5% | PASS |  |  |
| CVX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $208.37 / entry $208.37 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| CVX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| CVX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 41.7 | 41.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| CVX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +43.7% vs +7.0% | 43.7% vs 7.0% | PASS |  |  |
| CVX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| CVX | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.6 | 25.6 | PASS |  | Wilder, completed bars |
| CVX | T4w | words "20 or more / below 20" | 20 or more | ADX 25.6 | PASS |  |  |
| CVX | T5 | "counted at the last close ($X, date)" = last completed bar | $208.37, Nov 20 | $208.37, Nov 20 | PASS |  |  |
| CVX | T6 | price vs 200-day average (S1 pattern sma values) | $208.37 vs $193.30 · +7.8% | $208.37 vs $193.30 · 7.8% | PASS |  |  |
| CVX | T6w | word "Above" | Above | Above | PASS |  |  |
| CVX | T7 | price vs 50-day average (S1 pattern sma values) | $208.37 vs $213.71 · -2.5% | $208.37 vs $213.71 · -2.5% | PASS |  |  |
| CVX | T7w | word "Below" | Below | Below | PASS |  |  |
| CVX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.9% over 30 td | +4.9% over 30 td | PASS |  |  |
| CVX | T8r | word "rising" | still rising | rising | PASS |  |  |
| CVX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| CVX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 11.2% below $234.53 | 11.2% below $234.53 | PASS |  | closing high would be 233.58 |
| CVX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 11.2% below | PASS |  |  |
| CVX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $234.53 | $234.5323921577078 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| CVX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 0 down, 2 flat | 3 signals, 1 up, 0 down, 2 flat | PASS |  | change 0.91%, close location 0.58, OBV flat |
| CVX | V2 | day change of the last completed bar | up 0.9% | +0.91% | PASS |  |  |
| CVX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | flat | flat (sr says flat) | PASS |  |  |
| CVX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.34× / 0.39× | 1.34× / 0.39× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| CVX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 11887718) | 20 bars, last ('2026-11-20', 11887718) | PASS |  |  |
| DRAL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $3.01 | $3.01 | PASS |  |  |
| DRAL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $5.44 | $5.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAL | E3 | percent from the 21-day average | 44.6% below | 44.6% below | PASS |  |  |
| DRAL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRAL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.79 | $0.79 (sr=0.7887) | PASS |  | Wilder ATR14 |
| DRAL | E5 | distance in normal day-moves | 3.1 | 3.1 | PASS |  | gauge dot note uses the same number:  · 3.1 day-moves below |
| DRAL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.5 | +3.5 | PASS |  |  |
| DRAL | L-ema21 | ladder row ema21: price and gap = price vs average | $5.44, -44.6% | $5.44, -44.6% | PASS |  |  |
| DRAL | L-note | "Last close $X · date" note = last completed bar | Last close $3.01 · Nov 20 | $3.01 · Nov 20 | PASS |  |  |
| DRAL | L-now | ladder price row = compared price; name = the basis label | $3.01 "After hours" | $3.01 "after hours" | PASS |  |  |
| DRAL | L-sma50 | ladder row sma50: price and gap = price vs average | $8.23, -63.4% | $8.23, -63.4% | PASS |  |  |
| DRAL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $3.01 / entry $3.01 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.8 | 29.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAL | T4w | words "20 or more / below 20" | 20 or more | ADX 35.1 | PASS |  |  |
| DRAL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -24.56%, close location 0.07, OBV falling |
| DRAL | V2 | day change of the last completed bar | down 24.6% | -24.56% | PASS |  |  |
| DRAL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0750) | PASS |  |  |
| DRAL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.72× / 0.94× | 2.72× / 0.94× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 749183) | 20 bars, last ('2026-11-20', 749183) | PASS |  |  |
| DRAL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.72, OBV falling | condition true | PASS |  |  |
| DRAM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $33.36 | $33.36 | PASS |  |  |
| DRAM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $42.96 | $42.96 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRAM | E3 | percent from the 21-day average | 22.4% below | 22.4% below | PASS |  |  |
| DRAM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRAM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.20 | $3.20 (sr=3.1995) | PASS |  | Wilder ATR14 |
| DRAM | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| DRAM | L-ema21 | ladder row ema21: price and gap = price vs average | $42.96, -22.4% | $42.96, -22.4% | PASS |  |  |
| DRAM | L-note | "Last close $X · date" note = last completed bar | Last close $33.36 · Nov 20 | $33.36 · Nov 20 | PASS |  |  |
| DRAM | L-now | ladder price row = compared price; name = the basis label | $33.36 "After hours" | $33.36 "after hours" | PASS |  |  |
| DRAM | L-sma50 | ladder row sma50: price and gap = price vs average | $51.09, -34.7% | $51.09, -34.7% | PASS |  |  |
| DRAM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $33.36 / entry $33.36 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRAM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.6 | 30.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRAM | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.9 | 32.9 | PASS |  | Wilder, completed bars |
| DRAM | T4w | words "20 or more / below 20" | 20 or more | ADX 32.9 | PASS |  |  |
| DRAM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -13.19%, close location 0.01, OBV falling |
| DRAM | V2 | day change of the last completed bar | down 13.2% | -13.19% | PASS |  |  |
| DRAM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0100) | PASS |  |  |
| DRAM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRAM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.94× / 1.38× | 1.94× / 1.38× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRAM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 69876924) | 20 bars, last ('2026-11-20', 69876924) | PASS |  |  |
| DRAM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.94, OBV falling | condition true | PASS |  |  |
| DRIV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $24.59 | $24.59 | PASS |  |  |
| DRIV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.43 | $28.43 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DRIV | E3 | percent from the 21-day average | 13.5% below | 13.5% below | PASS |  |  |
| DRIV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DRIV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.85 | $0.85 (sr=0.8466) | PASS |  | Wilder ATR14 |
| DRIV | E5 | distance in normal day-moves | 4.5 | 4.5 | PASS |  | gauge dot note uses the same number:  · 4.5 day-moves below |
| DRIV | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +6.7 | +6.7 | PASS |  |  |
| DRIV | L-ema21 | ladder row ema21: price and gap = price vs average | $28.43, -13.5% | $28.43, -13.5% | PASS |  |  |
| DRIV | L-note | "Last close $X · date" note = last completed bar | Last close $24.59 · Nov 20 | $24.59 · Nov 20 | PASS |  |  |
| DRIV | L-now | ladder price row = compared price; name = the basis label | $24.59 "After hours" | $24.59 "after hours" | PASS |  |  |
| DRIV | L-sma200 | ladder row sma200: price and gap = price vs average | $34.13, -27.9% | $34.13, -27.9% | PASS |  |  |
| DRIV | L-sma50 | ladder row sma50: price and gap = price vs average | $30.96, -20.6% | $30.96, -20.6% | PASS |  |  |
| DRIV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $24.59 / entry $24.59 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DRIV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DRIV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.9 | 22.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DRIV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -10.3% vs +7.0% | -10.3% vs 7.0% | PASS |  |  |
| DRIV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DRIV | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.4 | 40.5 | PASS |  | Wilder, completed bars |
| DRIV | T4w | words "20 or more / below 20" | 20 or more | ADX 40.5 | PASS |  |  |
| DRIV | T5 | "counted at the last close ($X, date)" = last completed bar | $24.59, Nov 20 | $24.59, Nov 20 | PASS |  |  |
| DRIV | T6 | price vs 200-day average (S1 pattern sma values) | $24.59 vs $34.13 · -28.0% | $24.59 vs $34.13 · -27.9% | PASS |  |  |
| DRIV | T6w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T7 | price vs 50-day average (S1 pattern sma values) | $24.59 vs $30.96 · -20.6% | $24.59 vs $30.96 · -20.6% | PASS |  |  |
| DRIV | T7w | word "Below" | Below | Below | PASS |  |  |
| DRIV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.0% over 30 td | -1.1% over 30 td | PASS |  |  |
| DRIV | T8r | word "rising" | not rising | not rising | PASS |  |  |
| DRIV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DRIV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 42.4% below $42.67 | 42.4% below $42.67 | PASS |  | closing high would be 42.45 |
| DRIV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 42.4% below | PASS |  |  |
| DRIV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $42.67 | $42.67459709729379 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DRIV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.36%, close location 0.01, OBV falling |
| DRIV | V2 | day change of the last completed bar | down 6.3% | -6.36% | PASS |  |  |
| DRIV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0145) | PASS |  |  |
| DRIV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| DRIV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.21× / 1.84× | 1.21× / 1.85× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DRIV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 48648) | 20 bars, last ('2026-11-20', 48648) | PASS |  |  |
| DUK | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $129.78 | $129.78 | PASS |  |  |
| DUK | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $126.8 | $126.80 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| DUK | E3 | percent from the 21-day average | 2.3% above | 2.3% above | PASS |  |  |
| DUK | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| DUK | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.19 | $2.19 (sr=2.1903) | PASS |  | Wilder ATR14 |
| DUK | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves above |
| DUK | L-ema21 | ladder row ema21: price and gap = price vs average | $126.8, 2.3% | $126.80, 2.3% | PASS |  |  |
| DUK | L-note | "Last close $X · date" note = last completed bar | Last close $129.78 · Nov 20 | $129.78 · Nov 20 | PASS |  |  |
| DUK | L-now | ladder price row = compared price; name = the basis label | $129.78 "After hours" | $129.78 "after hours" | PASS |  |  |
| DUK | L-sma200 | ladder row sma200: price and gap = price vs average | $122.9, 5.6% | $122.90, 5.6% | PASS |  |  |
| DUK | L-sma50 | ladder row sma50: price and gap = price vs average | $120.73, 7.5% | $120.73, 7.5% | PASS |  |  |
| DUK | S5-price | S5: the same live price reads the same on the header and the Entry block | header $129.78 / entry $129.78 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| DUK | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| DUK | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 64.1 | 64.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| DUK | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +9.6% vs +7.0% | 9.6% vs 7.0% | PASS |  |  |
| DUK | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| DUK | T4 | ADX 14 (S1 /api/sr meta.adx) | 45.8 | 45.8 | PASS |  | Wilder, completed bars |
| DUK | T4w | words "20 or more / below 20" | 20 or more | ADX 45.8 | PASS |  |  |
| DUK | T5 | "counted at the last close ($X, date)" = last completed bar | $129.78, Nov 20 | $129.78, Nov 20 | PASS |  |  |
| DUK | T6 | price vs 200-day average (S1 pattern sma values) | $129.78 vs $122.90 · +5.6% | $129.78 vs $122.90 · 5.6% | PASS |  |  |
| DUK | T6w | word "Above" | Above | Above | PASS |  |  |
| DUK | T7 | price vs 50-day average (S1 pattern sma values) | $129.78 vs $120.73 · +7.5% | $129.78 vs $120.73 · 7.5% | PASS |  |  |
| DUK | T7w | word "Above" | Above | Above | PASS |  |  |
| DUK | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| DUK | T8r | word "rising" | still rising | rising | PASS |  |  |
| DUK | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| DUK | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 1.6% below $131.87 | 1.6% below $131.87 | PASS |  | closing high would be 130.59 |
| DUK | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 1.6% below | PASS |  |  |
| DUK | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.87 | $131.86787171141273 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| DUK | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.71%, close location 0.15, OBV rising |
| DUK | V2 | day change of the last completed bar | up 0.7% | +0.71% | PASS |  |  |
| DUK | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1534) | PASS |  |  |
| DUK | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| DUK | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.25× / 0.42× | 1.25× / 0.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| DUK | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 5678480) | 20 bars, last ('2026-11-20', 5678480) | PASS |  |  |
| ELIL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $36.41 | $36.41 | PASS |  |  |
| ELIL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $37.71 | $37.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ELIL | E3 | percent from the 21-day average | 3.5% below | 3.5% below | PASS |  |  |
| ELIL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ELIL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.15 | $2.15 (sr=2.1514) | PASS |  | Wilder ATR14 |
| ELIL | E5 | distance in normal day-moves | 0.6 | 0.6 | PASS |  | gauge dot note uses the same number:  · 0.6 day-moves below |
| ELIL | L-ema21 | ladder row ema21: price and gap = price vs average | $37.71, -3.5% | $37.71, -3.5% | PASS |  |  |
| ELIL | L-note | "Last close $X · date" note = last completed bar | Last close $36.41 · Nov 20 | $36.41 · Nov 20 | PASS |  |  |
| ELIL | L-now | ladder price row = compared price; name = the basis label | $36.41 "After hours" | $36.41 "after hours" | PASS |  |  |
| ELIL | L-sma200 | ladder row sma200: price and gap = price vs average | $27.17, 34.0% | $27.17, 34.0% | PASS |  |  |
| ELIL | L-sma50 | ladder row sma50: price and gap = price vs average | $32.93, 10.6% | $32.93, 10.6% | PASS |  |  |
| ELIL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $36.41 / entry $36.41 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ELIL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ELIL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.1 | 48.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ELIL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +35.9% vs +7.0% | 35.9% vs 7.0% | PASS |  |  |
| ELIL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ELIL | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.3 | 29.3 | PASS |  | Wilder, completed bars |
| ELIL | T4w | words "20 or more / below 20" | 20 or more | ADX 29.3 | PASS |  |  |
| ELIL | T5 | "counted at the last close ($X, date)" = last completed bar | $36.41, Nov 20 | $36.41, Nov 20 | PASS |  |  |
| ELIL | T6 | price vs 200-day average (S1 pattern sma values) | $36.41 vs $27.17 · +34.0% | $36.41 vs $27.17 · 34.0% | PASS |  |  |
| ELIL | T6w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T7 | price vs 50-day average (S1 pattern sma values) | $36.41 vs $32.93 · +10.6% | $36.41 vs $32.93 · 10.6% | PASS |  |  |
| ELIL | T7w | word "Above" | Above | Above | PASS |  |  |
| ELIL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +5.4% over 30 td | +5.4% over 30 td | PASS |  |  |
| ELIL | T8r | word "rising" | still rising | rising | PASS |  |  |
| ELIL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ELIL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 16.4% below $43.56 | 16.4% below $43.56 | PASS |  | closing high would be 41.85 |
| ELIL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 16.4% below | PASS |  |  |
| ELIL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.56 | $43.55500030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ELIL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.44%, close location 0.22, OBV falling |
| ELIL | V2 | day change of the last completed bar | down 0.4% | -0.44% | PASS |  |  |
| ELIL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2230) | PASS |  |  |
| ELIL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ELIL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.39× / 0.07× | 0.39× / 0.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ELIL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 23984) | 20 bars, last ('2026-11-20', 23984) | PASS |  |  |
| EQIX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $968.22 | $968.22 | PASS |  |  |
| EQIX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1019.6 | $1019.60 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| EQIX | E3 | percent from the 21-day average | 5.0% below | 5.0% below | PASS |  |  |
| EQIX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| EQIX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $34.47 | $34.47 (sr=34.4721) | PASS |  | Wilder ATR14 |
| EQIX | E5 | distance in normal day-moves | 1.5 | 1.5 | PASS |  | gauge dot note uses the same number:  · 1.5 day-moves below |
| EQIX | L-ema21 | ladder row ema21: price and gap = price vs average | $1019.6, -5.0% | $1019.60, -5.0% | PASS |  |  |
| EQIX | L-note | "Last close $X · date" note = last completed bar | Last close $968.44 · Nov 20 | $968.44 · Nov 20 | PASS |  |  |
| EQIX | L-now | ladder price row = compared price; name = the basis label | $968.22 "After hours" | $968.22 "after hours" | PASS |  |  |
| EQIX | L-sma200 | ladder row sma200: price and gap = price vs average | $1017.23, -4.8% | $1017.23, -4.8% | PASS |  |  |
| EQIX | L-sma50 | ladder row sma50: price and gap = price vs average | $1012.64, -4.4% | $1012.64, -4.4% | PASS |  |  |
| EQIX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $968.22 / entry $968.22 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| EQIX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| EQIX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.1 | 40.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| EQIX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +31.3% vs +7.0% | 31.3% vs 7.0% | PASS |  |  |
| EQIX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| EQIX | T4 | ADX 14 (S1 /api/sr meta.adx) | 17.0 | 17.0 | PASS |  | Wilder, completed bars |
| EQIX | T4w | words "20 or more / below 20" | below 20 | ADX 17.0 | PASS |  |  |
| EQIX | T5 | "counted at the last close ($X, date)" = last completed bar | $968.44, Nov 20 | $968.44, Nov 20 | PASS |  |  |
| EQIX | T6 | price vs 200-day average (S1 pattern sma values) | $968.44 vs $1,017.23 · -4.8% | $968.44 vs $1017.23 · -4.8% | PASS |  |  |
| EQIX | T6w | word "Below" | Below | Below | PASS |  |  |
| EQIX | T7 | price vs 50-day average (S1 pattern sma values) | $968.44 vs $1,012.64 · -4.4% | $968.44 vs $1012.64 · -4.4% | PASS |  |  |
| EQIX | T7w | word "Below" | Below | Below | PASS |  |  |
| EQIX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.6% over 30 td | +3.6% over 30 td | PASS |  |  |
| EQIX | T8r | word "rising" | still rising | rising | PASS |  |  |
| EQIX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| EQIX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.0% below $1,112.65 | 13.0% below $1112.65 | PASS |  | closing high would be 1104.67 |
| EQIX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.0% below | PASS |  |  |
| EQIX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,112.65 | $1112.652 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| EQIX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.87%, close location 0.08, OBV falling |
| EQIX | V2 | day change of the last completed bar | down 4.9% | -4.87% | PASS |  |  |
| EQIX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0818) | PASS |  |  |
| EQIX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| EQIX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.72× / 1.37× | 3.72× / 1.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| EQIX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 2341640) | 20 bars, last ('2026-11-20', 2341640) | PASS |  |  |
| EQIX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.72, OBV falling | condition true | PASS |  |  |
| ETN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $311.33 | $311.33 | PASS |  |  |
| ETN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $355.72 | $355.72 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ETN | E3 | percent from the 21-day average | 12.5% below | 12.5% below | PASS |  |  |
| ETN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ETN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.84 | $17.84 (sr=17.8361) | PASS |  | Wilder ATR14 |
| ETN | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| ETN | L-ema21 | ladder row ema21: price and gap = price vs average | $355.72, -12.5% | $355.72, -12.5% | PASS |  |  |
| ETN | L-note | "Last close $X · date" note = last completed bar | Last close $311.33 · Nov 20 | $311.33 · Nov 20 | PASS |  |  |
| ETN | L-now | ladder price row = compared price; name = the basis label | $311.33 "After hours" | $311.33 "after hours" | PASS |  |  |
| ETN | L-sma200 | ladder row sma200: price and gap = price vs average | $397.09, -21.6% | $397.09, -21.6% | PASS |  |  |
| ETN | L-sma50 | ladder row sma50: price and gap = price vs average | $392.76, -20.7% | $392.76, -20.7% | PASS |  |  |
| ETN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $311.33 / entry $311.33 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ETN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ETN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.4 | 31.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ETN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.1% vs +7.0% | -5.1% vs 7.0% | PASS |  |  |
| ETN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ETN | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.3 | 28.3 | PASS |  | Wilder, completed bars |
| ETN | T4w | words "20 or more / below 20" | 20 or more | ADX 28.3 | PASS |  |  |
| ETN | T5 | "counted at the last close ($X, date)" = last completed bar | $311.33, Nov 20 | $311.33, Nov 20 | PASS |  |  |
| ETN | T6 | price vs 200-day average (S1 pattern sma values) | $311.33 vs $397.09 · -21.6% | $311.33 vs $397.09 · -21.6% | PASS |  |  |
| ETN | T6w | word "Below" | Below | Below | PASS |  |  |
| ETN | T7 | price vs 50-day average (S1 pattern sma values) | $311.33 vs $392.76 · -20.7% | $311.33 vs $392.76 · -20.7% | PASS |  |  |
| ETN | T7w | word "Below" | Below | Below | PASS |  |  |
| ETN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| ETN | T8r | word "rising" | still rising | rising | PASS |  |  |
| ETN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ETN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.9% below $478.00 | 34.9% below $478.00 | PASS |  | closing high would be 459.96 |
| ETN | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.9% below | PASS |  |  |
| ETN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $478.00 | $478 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ETN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.82%, close location 0.16, OBV falling |
| ETN | V2 | day change of the last completed bar | down 5.8% | -5.82% | PASS |  |  |
| ETN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1573) | PASS |  |  |
| ETN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ETN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.74× / 1.02× | 1.74× / 1.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ETN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 4783085) | 20 bars, last ('2026-11-20', 4783085) | PASS |  |  |
| ETN | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.74, OBV falling | condition true | PASS |  |  |
| FCX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $45.99 | $45.99 | PASS |  |  |
| FCX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $58.77 | $58.77 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FCX | E3 | percent from the 21-day average | 21.8% below | 21.8% below | PASS |  |  |
| FCX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| FCX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.05 | $3.05 (sr=3.0515) | PASS |  | Wilder ATR14 |
| FCX | E5 | distance in normal day-moves | 4.2 | 4.2 | PASS |  | gauge dot note uses the same number:  · 4.2 day-moves below |
| FCX | L-ema21 | ladder row ema21: price and gap = price vs average | $58.77, -21.8% | $58.77, -21.8% | PASS |  |  |
| FCX | L-note | "Last close $X · date" note = last completed bar | Last close $45.99 · Nov 20 | $45.99 · Nov 20 | PASS |  |  |
| FCX | L-now | ladder price row = compared price; name = the basis label | $45.99 "After hours" | $45.99 "after hours" | PASS |  |  |
| FCX | L-sma200 | ladder row sma200: price and gap = price vs average | $64.72, -28.9% | $64.72, -28.9% | PASS |  |  |
| FCX | L-sma50 | ladder row sma50: price and gap = price vs average | $66.22, -30.5% | $66.22, -30.5% | PASS |  |  |
| FCX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $45.99 / entry $45.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| FCX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FCX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 21.0 | 21.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FCX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +17.1% vs +7.0% | 17.1% vs 7.0% | PASS |  |  |
| FCX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FCX | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.5 | 32.5 | PASS |  | Wilder, completed bars |
| FCX | T4w | words "20 or more / below 20" | 20 or more | ADX 32.5 | PASS |  |  |
| FCX | T5 | "counted at the last close ($X, date)" = last completed bar | $45.99, Nov 20 | $45.99, Nov 20 | PASS |  |  |
| FCX | T6 | price vs 200-day average (S1 pattern sma values) | $45.99 vs $64.72 · -28.9% | $45.99 vs $64.72 · -28.9% | PASS |  |  |
| FCX | T6w | word "Below" | Below | Below | PASS |  |  |
| FCX | T7 | price vs 50-day average (S1 pattern sma values) | $45.99 vs $66.22 · -30.5% | $45.99 vs $66.22 · -30.5% | PASS |  |  |
| FCX | T7w | word "Below" | Below | Below | PASS |  |  |
| FCX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.3% over 30 td | +1.3% over 30 td | PASS |  |  |
| FCX | T8r | word "rising" | still rising | rising | PASS |  |  |
| FCX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FCX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 42.6% below $80.07 | 42.6% below $80.07 | PASS |  | closing high would be 79.74 |
| FCX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 42.6% below | PASS |  |  |
| FCX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.07 | $80.06712214676648 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FCX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.37%, close location 0.13, OBV falling |
| FCX | V2 | day change of the last completed bar | down 6.4% | -6.37% | PASS |  |  |
| FCX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.13 (raw 0.1331) | PASS |  |  |
| FCX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| FCX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.43× / 0.96× | 2.43× / 0.96× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FCX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 30769534) | 20 bars, last ('2026-11-20', 30769534) | PASS |  |  |
| FCX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.43, OBV falling | condition true | PASS |  |  |
| FINN.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.38 | $30.38 | PASS |  |  |
| FINN.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $32.36 | $32.36 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| FINN.NE | E3 | percent from the 21-day average | 6.1% below | 6.1% below | PASS |  |  |
| FINN.NE | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| FINN.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.77 | $0.77 (sr=0.7673) | PASS |  | Wilder ATR14 |
| FINN.NE | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| FINN.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $32.36, -6.1% | $32.36, -6.1% | PASS |  |  |
| FINN.NE | L-now | ladder price row = compared price; name = the basis label | $30.38 "Last close" | $30.38 "last close" | PASS |  |  |
| FINN.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.19, 0.6% | $30.19, 0.6% | PASS |  |  |
| FINN.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $33.22, -8.5% | $33.22, -8.5% | PASS |  |  |
| FINN.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| FINN.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.7 | 31.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| FINN.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +38.2% vs +7.0% | 38.2% vs 7.0% | PASS |  |  |
| FINN.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| FINN.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 14.2 | 14.2 | PASS |  | Wilder, completed bars |
| FINN.NE | T4w | words "20 or more / below 20" | below 20 | ADX 14.2 | PASS |  |  |
| FINN.NE | T6 | price vs 200-day average (S1 pattern sma values) | $30.38 vs $30.19 · +0.6% | $30.38 vs $30.19 · 0.6% | PASS |  |  |
| FINN.NE | T6w | word "Above" | Above | Above | PASS |  |  |
| FINN.NE | T7 | price vs 50-day average (S1 pattern sma values) | $30.38 vs $33.22 · -8.5% | $30.38 vs $33.22 · -8.5% | PASS |  |  |
| FINN.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| FINN.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.4% over 30 td | +4.4% over 30 td | PASS |  |  |
| FINN.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| FINN.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| FINN.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 15.2% below $35.83 | 15.2% below $35.83 | PASS |  | closing high would be 35.43 |
| FINN.NE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 15.2% below | PASS |  |  |
| FINN.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $35.83 | $35.83000183105469 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| FINN.NE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.97%, close location 0.14, OBV falling |
| FINN.NE | V2 | day change of the last completed bar | down 5.0% | -4.97% | PASS |  |  |
| FINN.NE | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1429) | PASS |  |  |
| FINN.NE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| FINN.NE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.01× / 1.97× | 2.01× / 1.97× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| FINN.NE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 621767) | 20 bars, last ('2026-11-20', 621767) | PASS |  |  |
| FINN.NE | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.01, OBV falling | condition true | PASS |  |  |
| GDX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $68.40 | $68.40 | PASS |  |  |
| GDX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $80.6 | $80.60 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDX | E3 | percent from the 21-day average | 15.1% below | 15.1% below | PASS |  |  |
| GDX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GDX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.60 | $3.60 (sr=3.5995) | PASS |  | Wilder ATR14 |
| GDX | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| GDX | L-ema21 | ladder row ema21: price and gap = price vs average | $80.6, -15.1% | $80.60, -15.1% | PASS |  |  |
| GDX | L-note | "Last close $X · date" note = last completed bar | Last close $68.40 · Nov 20 | $68.40 · Nov 20 | PASS |  |  |
| GDX | L-now | ladder price row = compared price; name = the basis label | $68.4 "After hours" | $68.40 "after hours" | PASS |  |  |
| GDX | L-sma200 | ladder row sma200: price and gap = price vs average | $89.06, -23.2% | $89.06, -23.2% | PASS |  |  |
| GDX | L-sma50 | ladder row sma50: price and gap = price vs average | $85.93, -20.4% | $85.93, -20.4% | PASS |  |  |
| GDX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $68.40 / entry $68.40 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GDX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.8 | 29.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.6% vs +7.0% | -5.6% vs 7.0% | PASS |  |  |
| GDX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDX | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.6 | 21.6 | PASS |  | Wilder, completed bars |
| GDX | T4w | words "20 or more / below 20" | 20 or more | ADX 21.6 | PASS |  |  |
| GDX | T5 | "counted at the last close ($X, date)" = last completed bar | $68.40, Nov 20 | $68.40, Nov 20 | PASS |  |  |
| GDX | T6 | price vs 200-day average (S1 pattern sma values) | $68.40 vs $89.06 · -23.2% | $68.40 vs $89.06 · -23.2% | PASS |  |  |
| GDX | T6w | word "Below" | Below | Below | PASS |  |  |
| GDX | T7 | price vs 50-day average (S1 pattern sma values) | $68.40 vs $85.93 · -20.4% | $68.40 vs $85.93 · -20.4% | PASS |  |  |
| GDX | T7w | word "Below" | Below | Below | PASS |  |  |
| GDX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.2% over 30 td | -2.2% over 30 td | PASS |  |  |
| GDX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 41.6% below $117.18 | 41.6% below $117.18 | PASS |  | closing high would be 115.84 |
| GDX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 41.6% below | PASS |  |  |
| GDX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $117.18 | $117.18000030517578 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.00%, close location 0.10, OBV falling |
| GDX | V2 | day change of the last completed bar | down 5.0% | -5.00% | PASS |  |  |
| GDX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.0989) | PASS |  |  |
| GDX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.16× / 0.95× | 2.16× / 0.95× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 49310822) | 20 bars, last ('2026-11-20', 49310822) | PASS |  |  |
| GDX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.16, OBV falling | condition true | PASS |  |  |
| GDXU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $18.20 | $18.20 | PASS |  |  |
| GDXU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $25.86 | $25.86 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GDXU.TO | E3 | percent from the 21-day average | 29.6% below | 29.6% below | PASS |  |  |
| GDXU.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GDXU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.37 | $2.37 (sr=2.3747) | PASS |  | Wilder ATR14 |
| GDXU.TO | E5 | distance in normal day-moves | 3.2 | 3.2 | PASS |  | gauge dot note uses the same number:  · 3.2 day-moves below |
| GDXU.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.1 | +4.1 | PASS |  |  |
| GDXU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $25.86, -29.6% | $25.86, -29.6% | PASS |  |  |
| GDXU.TO | L-now | ladder price row = compared price; name = the basis label | $18.2 "Last close" | $18.20 "last close" | PASS |  |  |
| GDXU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $35.52, -48.8% | $35.52, -48.8% | PASS |  |  |
| GDXU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $30.29, -39.9% | $30.29, -39.9% | PASS |  |  |
| GDXU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GDXU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.3 | 30.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GDXU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -34.5% vs +7.0% | -34.5% vs 7.0% | PASS |  |  |
| GDXU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GDXU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.3 | 22.3 | PASS |  | Wilder, completed bars |
| GDXU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.3 | PASS |  |  |
| GDXU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $18.20 vs $35.52 · -48.8% | $18.20 vs $35.52 · -48.8% | PASS |  |  |
| GDXU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $18.20 vs $30.29 · -39.9% | $18.20 vs $30.29 · -39.9% | PASS |  |  |
| GDXU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| GDXU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -7.3% over 30 td | -7.3% over 30 td | PASS |  |  |
| GDXU.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GDXU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GDXU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 72.0% below $65.00 | 72.0% below $65.00 | PASS |  | closing high would be 63.22 |
| GDXU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 72.0% below | PASS |  |  |
| GDXU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $65.00 | $65 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GDXU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.57%, close location 0.06, OBV falling |
| GDXU.TO | V2 | day change of the last completed bar | down 10.6% | -10.57% | PASS |  |  |
| GDXU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0576) | PASS |  |  |
| GDXU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GDXU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.14× / 0.81× | 3.14× / 0.81× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GDXU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 823673) | 20 bars, last ('2026-11-20', 823673) | PASS |  |  |
| GDXU.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.14, OBV falling | condition true | PASS |  |  |
| GE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $309.62 | $309.62 | PASS |  |  |
| GE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $320.49 | $320.49 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GE | E3 | percent from the 21-day average | 3.4% below | 3.4% below | PASS |  |  |
| GE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $10.47 | $10.47 (sr=10.4736) | PASS |  | Wilder ATR14 |
| GE | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| GE | L-ema21 | ladder row ema21: price and gap = price vs average | $320.49, -3.4% | $320.49, -3.4% | PASS |  |  |
| GE | L-note | "Last close $X · date" note = last completed bar | Last close $309.62 · Nov 20 | $309.62 · Nov 20 | PASS |  |  |
| GE | L-now | ladder price row = compared price; name = the basis label | $309.62 "After hours" | $309.62 "after hours" | PASS |  |  |
| GE | L-sma200 | ladder row sma200: price and gap = price vs average | $324.22, -4.5% | $324.22, -4.5% | PASS |  |  |
| GE | L-sma50 | ladder row sma50: price and gap = price vs average | $314.03, -1.4% | $314.03, -1.4% | PASS |  |  |
| GE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $309.62 / entry $309.62 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.9 | 43.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.5% vs +7.0% | 6.5% vs 7.0% | PASS |  |  |
| GE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GE | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.0 | 19.0 | PASS |  | Wilder, completed bars |
| GE | T4w | words "20 or more / below 20" | below 20 | ADX 19.0 | PASS |  |  |
| GE | T5 | "counted at the last close ($X, date)" = last completed bar | $309.62, Nov 20 | $309.62, Nov 20 | PASS |  |  |
| GE | T6 | price vs 200-day average (S1 pattern sma values) | $309.62 vs $324.22 · -4.5% | $309.62 vs $324.22 · -4.5% | PASS |  |  |
| GE | T6w | word "Below" | Below | Below | PASS |  |  |
| GE | T7 | price vs 50-day average (S1 pattern sma values) | $309.62 vs $314.03 · -1.4% | $309.62 vs $314.03 · -1.4% | PASS |  |  |
| GE | T7w | word "Below" | Below | Below | PASS |  |  |
| GE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.1% over 30 td | +0.1% over 30 td | PASS |  |  |
| GE | T8r | word "rising" | still rising | rising | PASS |  |  |
| GE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 20.4% below $388.84 | 20.4% below $388.84 | PASS |  | closing high would be 381.22 |
| GE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 20.4% below | PASS |  |  |
| GE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $388.84 | $388.84 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -2.90%, close location 0.16, OBV rising |
| GE | V2 | day change of the last completed bar | down 2.9% | -2.90% | PASS |  |  |
| GE | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1558) | PASS |  |  |
| GE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.11× / 0.86× | 1.11× / 0.86× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 5483050) | 20 bars, last ('2026-11-20', 5483050) | PASS |  |  |
| GEV | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $699.33 | $699.33 | PASS |  |  |
| GEV | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $813.67 | $813.67 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV | E3 | percent from the 21-day average | 14.1% below | 14.1% below | PASS |  |  |
| GEV | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GEV | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $54.35 | $54.35 (sr=54.3479) | PASS |  | Wilder ATR14 |
| GEV | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| GEV | L-ema21 | ladder row ema21: price and gap = price vs average | $813.67, -14.1% | $813.67, -14.1% | PASS |  |  |
| GEV | L-note | "Last close $X · date" note = last completed bar | Last close $699.33 · Nov 20 | $699.33 · Nov 20 | PASS |  |  |
| GEV | L-now | ladder price row = compared price; name = the basis label | $699.33 "After hours" | $699.33 "after hours" | PASS |  |  |
| GEV | L-sma200 | ladder row sma200: price and gap = price vs average | $951.91, -26.5% | $951.91, -26.5% | PASS |  |  |
| GEV | L-sma50 | ladder row sma50: price and gap = price vs average | $893.69, -21.7% | $893.69, -21.7% | PASS |  |  |
| GEV | S5-price | S5: the same live price reads the same on the header and the Entry block | header $699.33 / entry $699.33 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GEV | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GEV | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.0 | 32.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.3% vs +7.0% | 25.3% vs 7.0% | PASS |  |  |
| GEV | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GEV | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.0 | 27.0 | PASS |  | Wilder, completed bars |
| GEV | T4w | words "20 or more / below 20" | 20 or more | ADX 27.0 | PASS |  |  |
| GEV | T5 | "counted at the last close ($X, date)" = last completed bar | $699.33, Nov 20 | $699.33, Nov 20 | PASS |  |  |
| GEV | T6 | price vs 200-day average (S1 pattern sma values) | $699.33 vs $951.91 · -26.5% | $699.33 vs $951.91 · -26.5% | PASS |  |  |
| GEV | T6w | word "Below" | Below | Below | PASS |  |  |
| GEV | T7 | price vs 50-day average (S1 pattern sma values) | $699.33 vs $893.69 · -21.7% | $699.33 vs $893.69 · -21.7% | PASS |  |  |
| GEV | T7w | word "Below" | Below | Below | PASS |  |  |
| GEV | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.8% over 30 td | +2.8% over 30 td | PASS |  |  |
| GEV | T8r | word "rising" | still rising | rising | PASS |  |  |
| GEV | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GEV | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 41.5% below $1,195.94 | 41.5% below $1195.94 | PASS |  | closing high would be 1174.86 |
| GEV | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 41.5% below | PASS |  |  |
| GEV | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,195.94 | $1195.94 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GEV | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.53%, close location 0.14, OBV falling |
| GEV | V2 | day change of the last completed bar | down 7.5% | -7.53% | PASS |  |  |
| GEV | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1418) | PASS |  |  |
| GEV | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.87× / 0.97× | 1.87× / 0.97× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 6197244) | 20 bars, last ('2026-11-20', 6197244) | PASS |  |  |
| GEV | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.87, OBV falling | condition true | PASS |  |  |
| GEV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $46.48 | $46.48 | PASS |  |  |
| GEV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $54.39 | $54.39 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GEV.TO | E3 | percent from the 21-day average | 14.5% below | 14.5% below | PASS |  |  |
| GEV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| GEV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.53 | $3.53 (sr=3.5309) | PASS |  | Wilder ATR14 |
| GEV.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| GEV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $54.39, -14.5% | $54.39, -14.5% | PASS |  |  |
| GEV.TO | L-now | ladder price row = compared price; name = the basis label | $46.48 "Last close" | $46.48 "last close" | PASS |  |  |
| GEV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $64.06, -27.4% | $64.06, -27.4% | PASS |  |  |
| GEV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $59.74, -22.2% | $59.74, -22.2% | PASS |  |  |
| GEV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.5 | 31.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GEV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +3.3% vs +7.0% | 3.3% vs 7.0% | PASS |  |  |
| GEV.TO | T3w | words "past year" vs the window used | 229 / 251 bars back | 250-253 bars | PASS |  |  |
| GEV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.8 | 26.8 | PASS |  | Wilder, completed bars |
| GEV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.8 | PASS |  |  |
| GEV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -8.14%, close location 0.05, OBV falling |
| GEV.TO | V2 | day change of the last completed bar | down 8.1% | -8.14% | PASS |  |  |
| GEV.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0525) | PASS |  |  |
| GEV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GEV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.63× / 1.07× | 2.63× / 1.07× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GEV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 211845) | 20 bars, last ('2026-11-20', 211845) | PASS |  |  |
| GEV.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.63, OBV falling | condition true | PASS |  |  |
| GGLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $56.59 | $56.59 | PASS |  |  |
| GGLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $70.48 | $70.48 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GGLL | E3 | percent from the 21-day average | 19.7% below | 19.7% below | PASS |  |  |
| GGLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GGLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.51 | $5.51 (sr=5.5082) | PASS |  | Wilder ATR14 |
| GGLL | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| GGLL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.0 | +3.0 | PASS |  |  |
| GGLL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.8 | +5.8 | PASS |  |  |
| GGLL | L-ema21 | ladder row ema21: price and gap = price vs average | $70.48, -19.7% | $70.48, -19.7% | PASS |  |  |
| GGLL | L-note | "Last close $X · date" note = last completed bar | Last close $56.59 · Nov 20 | $56.59 · Nov 20 | PASS |  |  |
| GGLL | L-now | ladder price row = compared price; name = the basis label | $56.59 "After hours" | $56.59 "after hours" | PASS |  |  |
| GGLL | L-sma200 | ladder row sma200: price and gap = price vs average | $102.16, -44.6% | $102.16, -44.6% | PASS |  |  |
| GGLL | L-sma50 | ladder row sma50: price and gap = price vs average | $87.08, -35.0% | $87.08, -35.0% | PASS |  |  |
| GGLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $56.59 / entry $56.59 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GGLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GGLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.4 | 27.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GGLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -35.1% vs +7.0% | -35.1% vs 7.0% | PASS |  |  |
| GGLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GGLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.9 | 25.9 | PASS |  | Wilder, completed bars |
| GGLL | T4w | words "20 or more / below 20" | 20 or more | ADX 25.9 | PASS |  |  |
| GGLL | T5 | "counted at the last close ($X, date)" = last completed bar | $56.59, Nov 20 | $56.59, Nov 20 | PASS |  |  |
| GGLL | T6 | price vs 200-day average (S1 pattern sma values) | $56.59 vs $102.16 · -44.6% | $56.59 vs $102.16 · -44.6% | PASS |  |  |
| GGLL | T6w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T7 | price vs 50-day average (S1 pattern sma values) | $56.59 vs $87.08 · -35.0% | $56.59 vs $87.08 · -35.0% | PASS |  |  |
| GGLL | T7w | word "Below" | Below | Below | PASS |  |  |
| GGLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -3.9% over 30 td | -3.9% over 30 td | PASS |  |  |
| GGLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GGLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GGLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 63.0% below $153.00 | 63.0% below $153.00 | PASS |  | closing high would be 148.94 |
| GGLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 63.0% below | PASS |  |  |
| GGLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $153.00 | $153 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GGLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.27%, close location 0.07, OBV falling |
| GGLL | V2 | day change of the last completed bar | down 5.3% | -5.27% | PASS |  |  |
| GGLL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0715) | PASS |  |  |
| GGLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GGLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.32× / 0.54× | 1.32× / 0.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GGLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 2588106) | 20 bars, last ('2026-11-20', 2588106) | PASS |  |  |
| GIB-A.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $113.76 | $113.76 | PASS |  |  |
| GIB-A.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.52 | $113.52 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GIB-A.TO | E3 | percent from the 21-day average | 0.2% above | 0.2% above | PASS |  |  |
| GIB-A.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GIB-A.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.73 | $2.73 (sr=2.7334) | PASS |  | Wilder ATR14 |
| GIB-A.TO | E5 | distance in normal day-moves | 0.1 | 0.1 | PASS |  | gauge dot note uses the same number:  · 0.1 day-moves above |
| GIB-A.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.0 | -5.0 | PASS |  |  |
| GIB-A.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $113.52, 0.2% | $113.52, 0.2% | PASS |  |  |
| GIB-A.TO | L-note | "Last close $X · date" note = last completed bar | Last close $113.76 · Nov 20 | $113.76 · Nov 20 | PASS |  |  |
| GIB-A.TO | L-now | ladder price row = compared price; name = the basis label | $113.76 "After hours" | $113.76 "after hours" | PASS |  |  |
| GIB-A.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $99.83, 14.0% | $99.83, 14.0% | PASS |  |  |
| GIB-A.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $106.8, 6.5% | $106.80, 6.5% | PASS |  |  |
| GIB-A.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $113.76 / entry $113.76 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GIB-A.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GIB-A.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 53.9 | 53.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GIB-A.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.6% vs +7.0% | -5.6% vs 7.0% | PASS |  |  |
| GIB-A.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GIB-A.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 36.4 | 36.4 | PASS |  | Wilder, completed bars |
| GIB-A.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 36.4 | PASS |  |  |
| GIB-A.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $113.76, Nov 20 | $113.76, Nov 20 | PASS |  |  |
| GIB-A.TO | T6 | price vs 200-day average (S1 pattern sma values) | $113.76 vs $99.83 · +14.0% | $113.76 vs $99.83 · 14.0% | PASS |  |  |
| GIB-A.TO | T6w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T7 | price vs 50-day average (S1 pattern sma values) | $113.76 vs $106.80 · +6.5% | $113.76 vs $106.80 · 6.5% | PASS |  |  |
| GIB-A.TO | T7w | word "Above" | Above | Above | PASS |  |  |
| GIB-A.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.7% over 30 td | -1.7% over 30 td | PASS |  |  |
| GIB-A.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GIB-A.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GIB-A.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.3% below $131.27 | 13.3% below $131.27 | PASS |  | closing high would be 130.81 |
| GIB-A.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.3% below | PASS |  |  |
| GIB-A.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $131.27 | $131.26876580580614 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GIB-A.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 1.20%, close location 0.48, OBV rising |
| GIB-A.TO | V2 | day change of the last completed bar | up 1.2% | +1.20% | PASS |  |  |
| GIB-A.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| GIB-A.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.02× / 0.50× | 1.02× / 0.50× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GIB-A.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 633319) | 20 bars, last ('2026-11-20', 633319) | PASS |  |  |
| GOOGL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $265.29 | $265.29 | PASS |  |  |
| GOOGL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $293.2 | $293.20 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GOOGL | E3 | percent from the 21-day average | 9.5% below | 9.5% below | PASS |  |  |
| GOOGL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GOOGL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $11.31 | $11.31 (sr=11.314) | PASS |  | Wilder ATR14 |
| GOOGL | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| GOOGL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.8 | +3.8 | PASS |  |  |
| GOOGL | L-ema21 | ladder row ema21: price and gap = price vs average | $293.2, -9.5% | $293.20, -9.5% | PASS |  |  |
| GOOGL | L-note | "Last close $X · date" note = last completed bar | Last close $265.29 · Nov 20 | $265.29 · Nov 20 | PASS |  |  |
| GOOGL | L-now | ladder price row = compared price; name = the basis label | $265.29 "After hours" | $265.29 "after hours" | PASS |  |  |
| GOOGL | L-sma200 | ladder row sma200: price and gap = price vs average | $336.71, -21.2% | $336.71, -21.2% | PASS |  |  |
| GOOGL | L-sma50 | ladder row sma50: price and gap = price vs average | $322.3, -17.7% | $322.30, -17.7% | PASS |  |  |
| GOOGL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $265.29 / entry $265.29 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GOOGL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GOOGL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.8 | 27.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GOOGL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -8.1% vs +7.0% | -8.1% vs 7.0% | PASS |  |  |
| GOOGL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GOOGL | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.7 | 23.7 | PASS |  | Wilder, completed bars |
| GOOGL | T4w | words "20 or more / below 20" | 20 or more | ADX 23.7 | PASS |  |  |
| GOOGL | T5 | "counted at the last close ($X, date)" = last completed bar | $265.29, Nov 20 | $265.29, Nov 20 | PASS |  |  |
| GOOGL | T6 | price vs 200-day average (S1 pattern sma values) | $265.29 vs $336.71 · -21.2% | $265.29 vs $336.71 · -21.2% | PASS |  |  |
| GOOGL | T6w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T7 | price vs 50-day average (S1 pattern sma values) | $265.29 vs $322.30 · -17.7% | $265.29 vs $322.30 · -17.7% | PASS |  |  |
| GOOGL | T7w | word "Below" | Below | Below | PASS |  |  |
| GOOGL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.9% over 30 td | -0.9% over 30 td | PASS |  |  |
| GOOGL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| GOOGL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GOOGL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 35.0% below $408.10 | 35.0% below $408.10 | PASS |  | closing high would be 402.12 |
| GOOGL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 35.0% below | PASS |  |  |
| GOOGL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $408.10 | $408.10376741205215 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GOOGL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.70%, close location 0.06, OBV falling |
| GOOGL | V2 | day change of the last completed bar | down 2.7% | -2.70% | PASS |  |  |
| GOOGL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0566) | PASS |  |  |
| GOOGL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GOOGL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.72× / 0.63× | 1.72× / 0.63× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GOOGL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 57134050) | 20 bars, last ('2026-11-20', 57134050) | PASS |  |  |
| GOOGL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.72, OBV falling | condition true | PASS |  |  |
| GRID | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $145.44 | $145.44 | PASS |  |  |
| GRID | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $159.86 | $159.86 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| GRID | E3 | percent from the 21-day average | 9.0% below | 9.0% below | PASS |  |  |
| GRID | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| GRID | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.44 | $4.44 (sr=4.4379) | PASS |  | Wilder ATR14 |
| GRID | E5 | distance in normal day-moves | 3.2 | 3.2 | PASS |  | gauge dot note uses the same number:  · 3.2 day-moves below |
| GRID | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.0 | +4.0 | PASS |  |  |
| GRID | L-ema21 | ladder row ema21: price and gap = price vs average | $159.86, -9.0% | $159.86, -9.0% | PASS |  |  |
| GRID | L-note | "Last close $X · date" note = last completed bar | Last close $145.44 · Nov 20 | $145.44 · Nov 20 | PASS |  |  |
| GRID | L-now | ladder price row = compared price; name = the basis label | $145.44 "After hours" | $145.44 "after hours" | PASS |  |  |
| GRID | L-sma200 | ladder row sma200: price and gap = price vs average | $177.73, -18.2% | $177.73, -18.2% | PASS |  |  |
| GRID | L-sma50 | ladder row sma50: price and gap = price vs average | $169.69, -14.3% | $169.69, -14.3% | PASS |  |  |
| GRID | S5-price | S5: the same live price reads the same on the header and the Entry block | header $145.44 / entry $145.44 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| GRID | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| GRID | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.8 | 28.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| GRID | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.1% vs +7.0% | 0.1% vs 7.0% | PASS |  |  |
| GRID | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| GRID | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.2 | 32.2 | PASS |  | Wilder, completed bars |
| GRID | T4w | words "20 or more / below 20" | 20 or more | ADX 32.2 | PASS |  |  |
| GRID | T5 | "counted at the last close ($X, date)" = last completed bar | $145.44, Nov 20 | $145.44, Nov 20 | PASS |  |  |
| GRID | T6 | price vs 200-day average (S1 pattern sma values) | $145.44 vs $177.73 · -18.2% | $145.44 vs $177.73 · -18.2% | PASS |  |  |
| GRID | T6w | word "Below" | Below | Below | PASS |  |  |
| GRID | T7 | price vs 50-day average (S1 pattern sma values) | $145.44 vs $169.69 · -14.3% | $145.44 vs $169.69 · -14.3% | PASS |  |  |
| GRID | T7w | word "Below" | Below | Below | PASS |  |  |
| GRID | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.5% over 30 td | +0.5% over 30 td | PASS |  |  |
| GRID | T8r | word "rising" | still rising | rising | PASS |  |  |
| GRID | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| GRID | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 26.8% below $198.80 | 26.8% below $198.80 | PASS |  | closing high would be 198.61 |
| GRID | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 26.8% below | PASS |  |  |
| GRID | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $198.80 | $198.79897 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| GRID | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.58%, close location 0.11, OBV falling |
| GRID | V2 | day change of the last completed bar | down 4.6% | -4.58% | PASS |  |  |
| GRID | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1149) | PASS |  |  |
| GRID | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| GRID | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.62× / 1.50× | 1.62× / 1.50× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| GRID | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 1024269) | 20 bars, last ('2026-11-20', 1024269) | PASS |  |  |
| GRID | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.62, OBV falling | condition true | PASS |  |  |
| HD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $339.04 | $339.04 | PASS |  |  |
| HD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $336.35 | $336.35 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HD | E3 | percent from the 21-day average | 0.8% above | 0.8% above | PASS |  |  |
| HD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| HD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.07 | $9.07 (sr=9.0712) | PASS |  | Wilder ATR14 |
| HD | E5 | distance in normal day-moves | 0.3 | 0.3 | PASS |  | gauge dot note uses the same number:  · 0.3 day-moves above |
| HD | L-ema21 | ladder row ema21: price and gap = price vs average | $336.35, 0.8% | $336.35, 0.8% | PASS |  |  |
| HD | L-note | "Last close $X · date" note = last completed bar | Last close $339.10 · Nov 20 | $339.10 · Nov 20 | PASS |  |  |
| HD | L-now | ladder price row = compared price; name = the basis label | $339.04 "After hours" | $339.04 "after hours" | PASS |  |  |
| HD | L-sma200 | ladder row sma200: price and gap = price vs average | $328.62, 3.2% | $328.62, 3.2% | PASS |  |  |
| HD | L-sma50 | ladder row sma50: price and gap = price vs average | $314.96, 7.6% | $314.96, 7.6% | PASS |  |  |
| HD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $339.04 / entry $339.04 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| HD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 55.2 | 55.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.9% vs +7.0% | 4.9% vs 7.0% | PASS |  |  |
| HD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HD | T4 | ADX 14 (S1 /api/sr meta.adx) | 37.2 | 37.2 | PASS |  | Wilder, completed bars |
| HD | T4w | words "20 or more / below 20" | 20 or more | ADX 37.2 | PASS |  |  |
| HD | T5 | "counted at the last close ($X, date)" = last completed bar | $339.10, Nov 20 | $339.10, Nov 20 | PASS |  |  |
| HD | T6 | price vs 200-day average (S1 pattern sma values) | $339.10 vs $328.62 · +3.2% | $339.10 vs $328.62 · 3.2% | PASS |  |  |
| HD | T6w | word "Above" | Above | Above | PASS |  |  |
| HD | T7 | price vs 50-day average (S1 pattern sma values) | $339.10 vs $314.96 · +7.7% | $339.10 vs $314.96 · 7.7% | PASS |  |  |
| HD | T7w | word "Above" | Above | Above | PASS |  |  |
| HD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.4% over 30 td | -1.4% over 30 td | PASS |  |  |
| HD | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 12.9% below $389.24 | 12.9% below $389.24 | PASS |  | closing high would be 382.80 |
| HD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 12.9% below | PASS |  |  |
| HD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $389.24 | $389.24026 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change 0.72%, close location 0.10, OBV falling |
| HD | V2 | day change of the last completed bar | up 0.7% | +0.72% | PASS |  |  |
| HD | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1032) | PASS |  |  |
| HD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.07× / 0.27× | 3.07× / 0.27× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 16426660) | 20 bars, last ('2026-11-20', 16426660) | PASS |  |  |
| HD | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.07, OBV falling | condition true | PASS |  |  |
| HURA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $33.89 | $33.89 | PASS |  |  |
| HURA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $39.23 | $39.23 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HURA.TO | E3 | percent from the 21-day average | 13.6% below | 13.6% below | PASS |  |  |
| HURA.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HURA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.37 | $1.37 (sr=1.3748) | PASS |  | Wilder ATR14 |
| HURA.TO | E5 | distance in normal day-moves | 3.9 | 3.9 | PASS |  | gauge dot note uses the same number:  · 3.9 day-moves below |
| HURA.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +9.7 | +9.7 | PASS |  |  |
| HURA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $39.23, -13.6% | $39.23, -13.6% | PASS |  |  |
| HURA.TO | L-now | ladder price row = compared price; name = the basis label | $33.89 "Last close" | $33.89 "last close" | PASS |  |  |
| HURA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $52.59, -35.6% | $52.59, -35.6% | PASS |  |  |
| HURA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $43.26, -21.7% | $43.26, -21.7% | PASS |  |  |
| HURA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HURA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.3 | 27.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HURA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -31.9% vs +7.0% | -31.9% vs 7.0% | PASS |  |  |
| HURA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HURA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.8 | 32.8 | PASS |  | Wilder, completed bars |
| HURA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.8 | PASS |  |  |
| HURA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $33.89 vs $52.59 · -35.6% | $33.89 vs $52.59 · -35.6% | PASS |  |  |
| HURA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $33.89 vs $43.26 · -21.7% | $33.89 vs $43.26 · -21.7% | PASS |  |  |
| HURA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HURA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.8% over 30 td | -5.8% over 30 td | PASS |  |  |
| HURA.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| HURA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HURA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 54.2% below $73.95 | 54.2% below $73.95 | PASS |  | closing high would be 73.19 |
| HURA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 54.2% below | PASS |  |  |
| HURA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $73.95 | $73.94999694824219 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HURA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.47%, close location 0.04, OBV falling |
| HURA.TO | V2 | day change of the last completed bar | down 5.5% | -5.47% | PASS |  |  |
| HURA.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0355) | PASS |  |  |
| HURA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HURA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.81× / 1.35× | 1.81× / 1.35× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HURA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 21856) | 20 bars, last ('2026-11-20', 21856) | PASS |  |  |
| HURA.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.81, OBV falling | condition true | PASS |  |  |
| HXQ.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $103.40 | $103.40 | PASS |  |  |
| HXQ.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $113.44 | $113.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| HXQ.TO | E3 | percent from the 21-day average | 8.9% below | 8.9% below | PASS |  |  |
| HXQ.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| HXQ.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.03 | $3.03 (sr=3.0253) | PASS |  | Wilder ATR14 |
| HXQ.TO | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| HXQ.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $113.44, -8.9% | $113.44, -8.9% | PASS |  |  |
| HXQ.TO | L-now | ladder price row = compared price; name = the basis label | $103.4 "Last close" | $103.40 "last close" | PASS |  |  |
| HXQ.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $112.37, -8.0% | $112.37, -8.0% | PASS |  |  |
| HXQ.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $118.69, -12.9% | $118.69, -12.9% | PASS |  |  |
| HXQ.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| HXQ.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.9 | 29.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| HXQ.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.1% vs +7.0% | 6.1% vs 7.0% | PASS |  |  |
| HXQ.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| HXQ.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.2 | 31.2 | PASS |  | Wilder, completed bars |
| HXQ.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 31.2 | PASS |  |  |
| HXQ.TO | T6 | price vs 200-day average (S1 pattern sma values) | $103.40 vs $112.37 · -8.0% | $103.40 vs $112.37 · -8.0% | PASS |  |  |
| HXQ.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| HXQ.TO | T7 | price vs 50-day average (S1 pattern sma values) | $103.40 vs $118.69 · -12.9% | $103.40 vs $118.69 · -12.9% | PASS |  |  |
| HXQ.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| HXQ.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| HXQ.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| HXQ.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| HXQ.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 19.5% below $128.37 | 19.5% below $128.37 | PASS |  | closing high would be 127.79 |
| HXQ.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 19.5% below | PASS |  |  |
| HXQ.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $128.37 | $128.3699951171875 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| HXQ.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.67%, close location 0.07, OBV falling |
| HXQ.TO | V2 | day change of the last completed bar | down 5.7% | -5.67% | PASS |  |  |
| HXQ.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0745) | PASS |  |  |
| HXQ.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| HXQ.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 4.71× / 1.94× | 4.71× / 1.94× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| HXQ.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 173150) | 20 bars, last ('2026-11-20', 173150) | PASS |  |  |
| HXQ.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 4.71, OBV falling | condition true | PASS |  |  |
| JNJ | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $270.47 | $270.47 | PASS |  |  |
| JNJ | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $273.44 | $273.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JNJ | E3 | percent from the 21-day average | 1.1% below | 1.1% below | PASS |  |  |
| JNJ | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| JNJ | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.70 | $6.70 (sr=6.7018) | PASS |  | Wilder ATR14 |
| JNJ | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| JNJ | L-ema21 | ladder row ema21: price and gap = price vs average | $273.44, -1.1% | $273.44, -1.1% | PASS |  |  |
| JNJ | L-note | "Last close $X · date" note = last completed bar | Last close $270.47 · Nov 20 | $270.47 · Nov 20 | PASS |  |  |
| JNJ | L-now | ladder price row = compared price; name = the basis label | $270.47 "After hours" | $270.47 "after hours" | PASS |  |  |
| JNJ | L-sma200 | ladder row sma200: price and gap = price vs average | $249.44, 8.4% | $249.44, 8.4% | PASS |  |  |
| JNJ | L-sma50 | ladder row sma50: price and gap = price vs average | $267.43, 1.1% | $267.43, 1.1% | PASS |  |  |
| JNJ | S5-price | S5: the same live price reads the same on the header and the Entry block | header $270.47 / entry $270.47 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JNJ | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JNJ | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 48.1 | 48.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JNJ | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +36.2% vs +7.0% | 36.2% vs 7.0% | PASS |  |  |
| JNJ | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JNJ | T4 | ADX 14 (S1 /api/sr meta.adx) | 21.8 | 21.8 | PASS |  | Wilder, completed bars |
| JNJ | T4w | words "20 or more / below 20" | 20 or more | ADX 21.8 | PASS |  |  |
| JNJ | T5 | "counted at the last close ($X, date)" = last completed bar | $270.47, Nov 20 | $270.47, Nov 20 | PASS |  |  |
| JNJ | T6 | price vs 200-day average (S1 pattern sma values) | $270.47 vs $249.44 · +8.4% | $270.47 vs $249.44 · 8.4% | PASS |  |  |
| JNJ | T6w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T7 | price vs 50-day average (S1 pattern sma values) | $270.47 vs $267.43 · +1.1% | $270.47 vs $267.43 · 1.1% | PASS |  |  |
| JNJ | T7w | word "Above" | Above | Above | PASS |  |  |
| JNJ | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.5% over 30 td | +3.5% over 30 td | PASS |  |  |
| JNJ | T8r | word "rising" | still rising | rising | PASS |  |  |
| JNJ | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JNJ | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 6.8% below $290.25 | 6.8% below $290.25 | PASS |  | closing high would be 285.75 |
| JNJ | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 6.8% below | PASS |  |  |
| JNJ | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $290.25 | $290.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JNJ | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 1 down, 1 flat | 3 signals, 1 up, 1 down, 1 flat | PASS |  | change 1.25%, close location 0.33, OBV falling |
| JNJ | V2 | day change of the last completed bar | up 1.3% | +1.25% | PASS |  |  |
| JNJ | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JNJ | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.57× / 0.50× | 1.57× / 0.50× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JNJ | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 11918787) | 20 bars, last ('2026-11-20', 11918787) | PASS |  |  |
| JNJ | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.57, OBV falling | condition true | PASS |  |  |
| JPM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $310.53 | $310.53 | PASS |  |  |
| JPM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $333.78 | $333.78 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| JPM | E3 | percent from the 21-day average | 7.0% below | 7.0% below | PASS |  |  |
| JPM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| JPM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.92 | $7.92 (sr=7.9181) | PASS |  | Wilder ATR14 |
| JPM | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| JPM | L-ema21 | ladder row ema21: price and gap = price vs average | $333.78, -7.0% | $333.78, -7.0% | PASS |  |  |
| JPM | L-note | "Last close $X · date" note = last completed bar | Last close $310.53 · Nov 20 | $310.53 · Nov 20 | PASS |  |  |
| JPM | L-now | ladder price row = compared price; name = the basis label | $310.53 "After hours" | $310.53 "after hours" | PASS |  |  |
| JPM | L-sma200 | ladder row sma200: price and gap = price vs average | $322.88, -3.8% | $322.88, -3.8% | PASS |  |  |
| JPM | L-sma50 | ladder row sma50: price and gap = price vs average | $336.81, -7.8% | $336.81, -7.8% | PASS |  |  |
| JPM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $310.53 / entry $310.53 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| JPM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| JPM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.8 | 30.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| JPM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +6.1% vs +7.0% | 6.1% vs 7.0% | PASS |  |  |
| JPM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| JPM | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.6 | 18.6 | PASS |  | Wilder, completed bars |
| JPM | T4w | words "20 or more / below 20" | below 20 | ADX 18.6 | PASS |  |  |
| JPM | T5 | "counted at the last close ($X, date)" = last completed bar | $310.53, Nov 20 | $310.53, Nov 20 | PASS |  |  |
| JPM | T6 | price vs 200-day average (S1 pattern sma values) | $310.53 vs $322.88 · -3.8% | $310.53 vs $322.88 · -3.8% | PASS |  |  |
| JPM | T6w | word "Below" | Below | Below | PASS |  |  |
| JPM | T7 | price vs 50-day average (S1 pattern sma values) | $310.53 vs $336.81 · -7.8% | $310.53 vs $336.81 · -7.8% | PASS |  |  |
| JPM | T7w | word "Below" | Below | Below | PASS |  |  |
| JPM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.2% over 30 td | +1.2% over 30 td | PASS |  |  |
| JPM | T8r | word "rising" | still rising | rising | PASS |  |  |
| JPM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| JPM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.8% below $364.68 | 14.8% below $364.68 | PASS |  | closing high would be 363.37 |
| JPM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.8% below | PASS |  |  |
| JPM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $364.68 | $364.68062001340013 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| JPM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.03%, close location 0.11, OBV falling |
| JPM | V2 | day change of the last completed bar | down 3.0% | -3.03% | PASS |  |  |
| JPM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1146) | PASS |  |  |
| JPM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| JPM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.60× / 1.19× | 1.60× / 1.19× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| JPM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 12504254) | 20 bars, last ('2026-11-20', 12504254) | PASS |  |  |
| JPM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.60, OBV falling | condition true | PASS |  |  |
| KEYS | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $261.51 | $261.51 | PASS |  |  |
| KEYS | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $298.26 | $298.26 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| KEYS | E3 | percent from the 21-day average | 12.3% below | 12.3% below | PASS |  |  |
| KEYS | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| KEYS | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.26 | $16.26 (sr=16.259) | PASS |  | Wilder ATR14 |
| KEYS | E5 | distance in normal day-moves | 2.3 | 2.3 | PASS |  | gauge dot note uses the same number:  · 2.3 day-moves below |
| KEYS | L-ema21 | ladder row ema21: price and gap = price vs average | $298.26, -12.3% | $298.26, -12.3% | PASS |  |  |
| KEYS | L-note | "Last close $X · date" note = last completed bar | Last close $261.51 · Nov 20 | $261.51 · Nov 20 | PASS |  |  |
| KEYS | L-now | ladder price row = compared price; name = the basis label | $261.51 "After hours" | $261.51 "after hours" | PASS |  |  |
| KEYS | L-sma200 | ladder row sma200: price and gap = price vs average | $321.92, -18.8% | $321.92, -18.8% | PASS |  |  |
| KEYS | L-sma50 | ladder row sma50: price and gap = price vs average | $329.89, -20.7% | $329.89, -20.7% | PASS |  |  |
| KEYS | S5-price | S5: the same live price reads the same on the header and the Entry block | header $261.51 / entry $261.51 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| KEYS | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| KEYS | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.5 | 32.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| KEYS | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +54.1% vs +7.0% | 54.1% vs 7.0% | PASS |  |  |
| KEYS | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| KEYS | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.6 | 33.6 | PASS |  | Wilder, completed bars |
| KEYS | T4w | words "20 or more / below 20" | 20 or more | ADX 33.6 | PASS |  |  |
| KEYS | T5 | "counted at the last close ($X, date)" = last completed bar | $261.51, Nov 20 | $261.51, Nov 20 | PASS |  |  |
| KEYS | T6 | price vs 200-day average (S1 pattern sma values) | $261.51 vs $321.92 · -18.8% | $261.51 vs $321.92 · -18.8% | PASS |  |  |
| KEYS | T6w | word "Below" | Below | Below | PASS |  |  |
| KEYS | T7 | price vs 50-day average (S1 pattern sma values) | $261.51 vs $329.89 · -20.7% | $261.51 vs $329.89 · -20.7% | PASS |  |  |
| KEYS | T7w | word "Below" | Below | Below | PASS |  |  |
| KEYS | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.8% over 30 td | +4.8% over 30 td | PASS |  |  |
| KEYS | T8r | word "rising" | still rising | rising | PASS |  |  |
| KEYS | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| KEYS | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 32.9% below $389.93 | 32.9% below $389.93 | PASS |  | closing high would be 388.03 |
| KEYS | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 32.9% below | PASS |  |  |
| KEYS | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $389.93 | $389.93 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| KEYS | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.07%, close location 0.04, OBV falling |
| KEYS | V2 | day change of the last completed bar | down 7.1% | -7.07% | PASS |  |  |
| KEYS | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0438) | PASS |  |  |
| KEYS | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| KEYS | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.33× / 1.14× | 2.33× / 1.14× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| KEYS | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3291322) | 20 bars, last ('2026-11-20', 3291322) | PASS |  |  |
| KEYS | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.33, OBV falling | condition true | PASS |  |  |
| LIN | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $502.83 | $502.83 | PASS |  |  |
| LIN | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $512.27 | $512.27 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LIN | E3 | percent from the 21-day average | 1.8% below | 1.8% below | PASS |  |  |
| LIN | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| LIN | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.25 | $9.25 (sr=9.249) | PASS |  | Wilder ATR14 |
| LIN | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| LIN | L-ema21 | ladder row ema21: price and gap = price vs average | $512.27, -1.8% | $512.27, -1.8% | PASS |  |  |
| LIN | L-note | "Last close $X · date" note = last completed bar | Last close $502.83 · Nov 20 | $502.83 · Nov 20 | PASS |  |  |
| LIN | L-now | ladder price row = compared price; name = the basis label | $502.83 "After hours" | $502.83 "after hours" | PASS |  |  |
| LIN | L-sma200 | ladder row sma200: price and gap = price vs average | $495.93, 1.4% | $495.93, 1.4% | PASS |  |  |
| LIN | L-sma50 | ladder row sma50: price and gap = price vs average | $494.67, 1.7% | $494.67, 1.7% | PASS |  |  |
| LIN | S5-price | S5: the same live price reads the same on the header and the Entry block | header $502.83 / entry $502.83 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LIN | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LIN | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 44.1 | 44.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LIN | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +24.8% vs +7.0% | 24.8% vs 7.0% | PASS |  |  |
| LIN | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LIN | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.2 | 27.2 | PASS |  | Wilder, completed bars |
| LIN | T4w | words "20 or more / below 20" | 20 or more | ADX 27.2 | PASS |  |  |
| LIN | T5 | "counted at the last close ($X, date)" = last completed bar | $502.83, Nov 20 | $502.83, Nov 20 | PASS |  |  |
| LIN | T6 | price vs 200-day average (S1 pattern sma values) | $502.83 vs $495.93 · +1.4% | $502.83 vs $495.93 · 1.4% | PASS |  |  |
| LIN | T6w | word "Above" | Above | Above | PASS |  |  |
| LIN | T7 | price vs 50-day average (S1 pattern sma values) | $502.83 vs $494.67 · +1.6% | $502.83 vs $494.67 · 1.7% | PASS |  |  |
| LIN | T7w | word "Above" | Above | Above | PASS |  |  |
| LIN | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.2% over 30 td | +2.2% over 30 td | PASS |  |  |
| LIN | T8r | word "rising" | still rising | rising | PASS |  |  |
| LIN | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LIN | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.0% below $546.40 | 8.0% below $546.40 | PASS |  | closing high would be 544.85 |
| LIN | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.0% below | PASS |  |  |
| LIN | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $546.40 | $546.4006244123242 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LIN | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.45%, close location 0.16, OBV falling |
| LIN | V2 | day change of the last completed bar | down 1.4% | -1.45% | PASS |  |  |
| LIN | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1590) | PASS |  |  |
| LIN | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| LIN | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.65× / 0.79× | 1.65× / 0.79× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LIN | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3511266) | 20 bars, last ('2026-11-20', 3511266) | PASS |  |  |
| LIN | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.65, OBV falling | condition true | PASS |  |  |
| LLY | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $1,347.11 | $1,347.11 | PASS |  |  |
| LLY | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $1365.0 | $1365.00 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| LLY | E3 | percent from the 21-day average | 1.3% below | 1.3% below | PASS |  |  |
| LLY | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| LLY | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $42.39 | $42.39 (sr=42.3904) | PASS |  | Wilder ATR14 |
| LLY | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| LLY | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.9 | -5.9 | PASS |  |  |
| LLY | L-ema21 | ladder row ema21: price and gap = price vs average | $1365, -1.3% | $1365.00, -1.3% | PASS |  |  |
| LLY | L-note | "Last close $X · date" note = last completed bar | Last close $1,347.11 · Nov 20 | $1,347.11 · Nov 20 | PASS |  |  |
| LLY | L-now | ladder price row = compared price; name = the basis label | $1347.11 "After hours" | $1347.11 "after hours" | PASS |  |  |
| LLY | L-sma200 | ladder row sma200: price and gap = price vs average | $1115.02, 20.8% | $1115.02, 20.8% | PASS |  |  |
| LLY | L-sma50 | ladder row sma50: price and gap = price vs average | $1265.59, 6.4% | $1265.59, 6.4% | PASS |  |  |
| LLY | S5-price | S5: the same live price reads the same on the header and the Entry block | header $1,347.11 / entry $1,347.11 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| LLY | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| LLY | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.7 | 49.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| LLY | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +29.9% vs +7.0% | 29.9% vs 7.0% | PASS |  |  |
| LLY | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| LLY | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.0 | 33.0 | PASS |  | Wilder, completed bars |
| LLY | T4w | words "20 or more / below 20" | 20 or more | ADX 33.0 | PASS |  |  |
| LLY | T5 | "counted at the last close ($X, date)" = last completed bar | $1,347.11, Nov 20 | $1347.11, Nov 20 | PASS |  |  |
| LLY | T6 | price vs 200-day average (S1 pattern sma values) | $1,347.11 vs $1,115.02 · +20.8% | $1347.11 vs $1115.02 · 20.8% | PASS |  |  |
| LLY | T6w | word "Above" | Above | Above | PASS |  |  |
| LLY | T7 | price vs 50-day average (S1 pattern sma values) | $1,347.11 vs $1,265.59 · +6.4% | $1347.11 vs $1265.59 · 6.4% | PASS |  |  |
| LLY | T7w | word "Above" | Above | Above | PASS |  |  |
| LLY | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.9% over 30 td | +3.9% over 30 td | PASS |  |  |
| LLY | T8r | word "rising" | still rising | rising | PASS |  |  |
| LLY | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| LLY | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 8.7% below $1,475.25 | 8.7% below $1475.25 | PASS |  | closing high would be 1443.50 |
| LLY | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 8.7% below | PASS |  |  |
| LLY | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $1,475.25 | $1475.25 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| LLY | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.30%, close location 0.18, OBV falling |
| LLY | V2 | day change of the last completed bar | down 0.3% | -0.30% | PASS |  |  |
| LLY | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.18 (raw 0.1764) | PASS |  |  |
| LLY | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| LLY | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.33× / 0.10× | 1.33× / 0.09× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| LLY | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3540083) | 20 bars, last ('2026-11-20', 3540083) | PASS |  |  |
| MDA.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $36.88 | $36.88 | PASS |  |  |
| MDA.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $39.96 | $39.96 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MDA.TO | E3 | percent from the 21-day average | 7.7% below | 7.7% below | PASS |  |  |
| MDA.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MDA.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.21 | $2.21 (sr=2.2057) | PASS |  | Wilder ATR14 |
| MDA.TO | E5 | distance in normal day-moves | 1.4 | 1.4 | PASS |  | gauge dot note uses the same number:  · 1.4 day-moves below |
| MDA.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $39.96, -7.7% | $39.96, -7.7% | PASS |  |  |
| MDA.TO | L-note | "Last close $X · date" note = last completed bar | Last close $36.88 · Nov 20 | $36.88 · Nov 20 | PASS |  |  |
| MDA.TO | L-now | ladder price row = compared price; name = the basis label | $36.88 "After hours" | $36.88 "after hours" | PASS |  |  |
| MDA.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $44.7, -17.5% | $44.70, -17.5% | PASS |  |  |
| MDA.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $40.8, -9.6% | $40.80, -9.6% | PASS |  |  |
| MDA.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $36.88 / entry $36.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MDA.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MDA.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 40.2 | 40.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MDA.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +61.0% vs +7.0% | 61.0% vs 7.0% | PASS |  |  |
| MDA.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MDA.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.3 | 26.3 | PASS |  | Wilder, completed bars |
| MDA.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.3 | PASS |  |  |
| MDA.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $36.88, Nov 20 | $36.88, Nov 20 | PASS |  |  |
| MDA.TO | T6 | price vs 200-day average (S1 pattern sma values) | $36.88 vs $44.70 · -17.5% | $36.88 vs $44.70 · -17.5% | PASS |  |  |
| MDA.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T7 | price vs 50-day average (S1 pattern sma values) | $36.88 vs $40.80 · -9.6% | $36.88 vs $40.80 · -9.6% | PASS |  |  |
| MDA.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MDA.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.5% over 30 td | +2.4% over 30 td | PASS |  |  |
| MDA.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MDA.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MDA.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 45.7% below $67.90 | 45.7% below $67.90 | PASS |  | closing high would be 67.13 |
| MDA.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 45.7% below | PASS |  |  |
| MDA.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $67.90 | $67.9000015258789 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MDA.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.06%, close location 0.17, OBV falling |
| MDA.TO | V2 | day change of the last completed bar | down 4.1% | -4.06% | PASS |  |  |
| MDA.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1689) | PASS |  |  |
| MDA.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MDA.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.92× / 0.68× | 0.92× / 0.68× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MDA.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 1445926) | 20 bars, last ('2026-11-20', 1445926) | PASS |  |  |
| META | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $560.84 | $560.84 | PASS |  |  |
| META | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $627.54 | $627.54 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| META | E3 | percent from the 21-day average | 10.6% below | 10.6% below | PASS |  |  |
| META | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| META | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $23.27 | $23.27 (sr=23.2728) | PASS |  | Wilder ATR14 |
| META | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| META | L-ema21 | ladder row ema21: price and gap = price vs average | $627.54, -10.6% | $627.54, -10.6% | PASS |  |  |
| META | L-note | "Last close $X · date" note = last completed bar | Last close $560.84 · Nov 20 | $560.84 · Nov 20 | PASS |  |  |
| META | L-now | ladder price row = compared price; name = the basis label | $560.84 "After hours" | $560.84 "after hours" | PASS |  |  |
| META | L-sma200 | ladder row sma200: price and gap = price vs average | $627.89, -10.7% | $627.89, -10.7% | PASS |  |  |
| META | L-sma50 | ladder row sma50: price and gap = price vs average | $676.6, -17.1% | $676.60, -17.1% | PASS |  |  |
| META | S5-price | S5: the same live price reads the same on the header and the Entry block | header $560.84 / entry $560.84 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| META | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| META | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.3 | 30.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| META | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.5% vs +7.0% | -4.5% vs 7.0% | PASS |  |  |
| META | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| META | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.0 | 25.0 | PASS |  | Wilder, completed bars |
| META | T4w | words "20 or more / below 20" | 20 or more | ADX 25.0 | PASS |  |  |
| META | T5 | "counted at the last close ($X, date)" = last completed bar | $560.84, Nov 20 | $560.84, Nov 20 | PASS |  |  |
| META | T6 | price vs 200-day average (S1 pattern sma values) | $560.84 vs $627.89 · -10.7% | $560.84 vs $627.89 · -10.7% | PASS |  |  |
| META | T6w | word "Below" | Below | Below | PASS |  |  |
| META | T7 | price vs 50-day average (S1 pattern sma values) | $560.84 vs $676.60 · -17.1% | $560.84 vs $676.60 · -17.1% | PASS |  |  |
| META | T7w | word "Below" | Below | Below | PASS |  |  |
| META | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.2% over 30 td | -0.2% over 30 td | PASS |  |  |
| META | T8r | word "rising" | not rising | not rising | PASS |  |  |
| META | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| META | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 28.1% below $779.82 | 28.1% below $779.82 | PASS |  | closing high would be 777.59 |
| META | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 28.1% below | PASS |  |  |
| META | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $779.82 | $779.8200073242188 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| META | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.93%, close location 0.07, OBV falling |
| META | V2 | day change of the last completed bar | down 5.9% | -5.93% | PASS |  |  |
| META | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0720) | PASS |  |  |
| META | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| META | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.18× / 1.43× | 1.18× / 1.43× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| META | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 25589154) | 20 bars, last ('2026-11-20', 25589154) | PASS |  |  |
| METU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $17.61 | $17.61 | PASS |  |  |
| METU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $22.46 | $22.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| METU | E3 | percent from the 21-day average | 21.6% below | 21.6% below | PASS |  |  |
| METU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| METU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.69 | $1.69 (sr=1.6882) | PASS |  | Wilder ATR14 |
| METU | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| METU | L-ema21 | ladder row ema21: price and gap = price vs average | $22.46, -21.6% | $22.46, -21.6% | PASS |  |  |
| METU | L-note | "Last close $X · date" note = last completed bar | Last close $17.61 · Nov 20 | $17.61 · Nov 20 | PASS |  |  |
| METU | L-now | ladder price row = compared price; name = the basis label | $17.61 "After hours" | $17.61 "after hours" | PASS |  |  |
| METU | L-sma200 | ladder row sma200: price and gap = price vs average | $25.04, -29.7% | $25.04, -29.7% | PASS |  |  |
| METU | L-sma50 | ladder row sma50: price and gap = price vs average | $26.6, -33.8% | $26.60, -33.8% | PASS |  |  |
| METU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $17.61 / entry $17.61 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| METU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| METU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.0 | 30.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| METU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -31.0% vs +7.0% | -31.0% vs 7.0% | PASS |  |  |
| METU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| METU | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.0 | 26.0 | PASS |  | Wilder, completed bars |
| METU | T4w | words "20 or more / below 20" | 20 or more | ADX 26.0 | PASS |  |  |
| METU | T5 | "counted at the last close ($X, date)" = last completed bar | $17.61, Nov 20 | $17.61, Nov 20 | PASS |  |  |
| METU | T6 | price vs 200-day average (S1 pattern sma values) | $17.61 vs $25.04 · -29.7% | $17.61 vs $25.04 · -29.7% | PASS |  |  |
| METU | T6w | word "Below" | Below | Below | PASS |  |  |
| METU | T7 | price vs 50-day average (S1 pattern sma values) | $17.61 vs $26.60 · -33.8% | $17.61 vs $26.60 · -33.8% | PASS |  |  |
| METU | T7w | word "Below" | Below | Below | PASS |  |  |
| METU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.0% over 30 td | -4.0% over 30 td | PASS |  |  |
| METU | T8r | word "rising" | not rising | not rising | PASS |  |  |
| METU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| METU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 54.8% below $38.96 | 54.8% below $38.96 | PASS |  | closing high would be 38.45 |
| METU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 54.8% below | PASS |  |  |
| METU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.96 | $38.95624380685178 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| METU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -11.99%, close location 0.08, OBV falling |
| METU | V2 | day change of the last completed bar | down 12.0% | -11.99% | PASS |  |  |
| METU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0758) | PASS |  |  |
| METU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| METU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.52× / 1.25× | 0.52× / 1.25× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| METU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 2404249) | 20 bars, last ('2026-11-20', 2404249) | PASS |  |  |
| MRVL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $122.28 | $122.28 | PASS |  |  |
| MRVL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $170.18 | $170.18 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MRVL | E3 | percent from the 21-day average | 28.1% below | 28.1% below | PASS |  |  |
| MRVL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MRVL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.06 | $16.06 (sr=16.0574) | PASS |  | Wilder ATR14 |
| MRVL | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| MRVL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| MRVL | L-ema21 | ladder row ema21: price and gap = price vs average | $170.18, -28.1% | $170.18, -28.1% | PASS |  |  |
| MRVL | L-note | "Last close $X · date" note = last completed bar | Last close $122.28 · Nov 20 | $122.28 · Nov 20 | PASS |  |  |
| MRVL | L-now | ladder price row = compared price; name = the basis label | $122.28 "After hours" | $122.28 "after hours" | PASS |  |  |
| MRVL | L-sma200 | ladder row sma200: price and gap = price vs average | $188.53, -35.1% | $188.53, -35.1% | PASS |  |  |
| MRVL | L-sma50 | ladder row sma50: price and gap = price vs average | $220.25, -44.5% | $220.25, -44.5% | PASS |  |  |
| MRVL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $122.28 / entry $122.28 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MRVL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MRVL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.9 | 27.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MRVL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +59.7% vs +7.0% | 59.7% vs 7.0% | PASS |  |  |
| MRVL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MRVL | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.8 | 33.8 | PASS |  | Wilder, completed bars |
| MRVL | T4w | words "20 or more / below 20" | 20 or more | ADX 33.8 | PASS |  |  |
| MRVL | T5 | "counted at the last close ($X, date)" = last completed bar | $122.28, Nov 20 | $122.28, Nov 20 | PASS |  |  |
| MRVL | T6 | price vs 200-day average (S1 pattern sma values) | $122.28 vs $188.53 · -35.1% | $122.28 vs $188.53 · -35.1% | PASS |  |  |
| MRVL | T6w | word "Below" | Below | Below | PASS |  |  |
| MRVL | T7 | price vs 50-day average (S1 pattern sma values) | $122.28 vs $220.25 · -44.5% | $122.28 vs $220.25 · -44.5% | PASS |  |  |
| MRVL | T7w | word "Below" | Below | Below | PASS |  |  |
| MRVL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +9.8% over 30 td | +9.8% over 30 td | PASS |  |  |
| MRVL | T8r | word "rising" | still rising | rising | PASS |  |  |
| MRVL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MRVL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 62.9% below $329.73 | 62.9% below $329.73 | PASS |  | closing high would be 316.28 |
| MRVL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 62.9% below | PASS |  |  |
| MRVL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $329.73 | $329.72658943397715 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MRVL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -11.69%, close location 0.13, OBV falling |
| MRVL | V2 | day change of the last completed bar | down 11.7% | -11.69% | PASS |  |  |
| MRVL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.13 (raw 0.1263) | PASS |  |  |
| MRVL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MRVL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.62× / 0.89× | 1.62× / 0.89× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MRVL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 40299998) | 20 bars, last ('2026-11-20', 40299998) | PASS |  |  |
| MRVL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.62, OBV falling | condition true | PASS |  |  |
| MSFT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $484.52 | $484.52 | PASS |  |  |
| MSFT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $517.23 | $517.23 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFT | E3 | percent from the 21-day average | 6.3% below | 6.3% below | PASS |  |  |
| MSFT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MSFT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.38 | $16.38 (sr=16.3819) | PASS |  | Wilder ATR14 |
| MSFT | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| MSFT | L-ema21 | ladder row ema21: price and gap = price vs average | $517.23, -6.3% | $517.23, -6.3% | PASS |  |  |
| MSFT | L-note | "Last close $X · date" note = last completed bar | Last close $484.52 · Nov 20 | $484.52 · Nov 20 | PASS |  |  |
| MSFT | L-now | ladder price row = compared price; name = the basis label | $484.52 "After hours" | $484.52 "after hours" | PASS |  |  |
| MSFT | L-sma200 | ladder row sma200: price and gap = price vs average | $441.93, 9.6% | $441.93, 9.6% | PASS |  |  |
| MSFT | L-sma50 | ladder row sma50: price and gap = price vs average | $518.87, -6.6% | $518.87, -6.6% | PASS |  |  |
| MSFT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $484.52 / entry $484.52 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.0 | 35.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.1% vs +7.0% | 2.1% vs 7.0% | PASS |  |  |
| MSFT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFT | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.2 | 18.2 | PASS |  | Wilder, completed bars |
| MSFT | T4w | words "20 or more / below 20" | below 20 | ADX 18.2 | PASS |  |  |
| MSFT | T5 | "counted at the last close ($X, date)" = last completed bar | $484.52, Nov 20 | $484.52, Nov 20 | PASS |  |  |
| MSFT | T6 | price vs 200-day average (S1 pattern sma values) | $484.52 vs $441.93 · +9.6% | $484.52 vs $441.93 · 9.6% | PASS |  |  |
| MSFT | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFT | T7 | price vs 50-day average (S1 pattern sma values) | $484.52 vs $518.87 · -6.6% | $484.52 vs $518.87 · -6.6% | PASS |  |  |
| MSFT | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.3% over 30 td | +2.3% over 30 td | PASS |  |  |
| MSFT | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.2% below $558.07 | 13.2% below $558.07 | PASS |  | closing high would be 554.73 |
| MSFT | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.2% below | PASS |  |  |
| MSFT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $558.07 | $558.0719712336797 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.77%, close location 0.15, OBV falling |
| MSFT | V2 | day change of the last completed bar | down 2.8% | -2.77% | PASS |  |  |
| MSFT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1533) | PASS |  |  |
| MSFT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.90× / 0.82× | 1.90× / 0.82× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 47123194) | 20 bars, last ('2026-11-20', 47123194) | PASS |  |  |
| MSFT | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.90, OBV falling | condition true | PASS |  |  |
| MSFU | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $34.23 | $34.23 | PASS |  |  |
| MSFU | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $39.44 | $39.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MSFU | E3 | percent from the 21-day average | 13.2% below | 13.2% below | PASS |  |  |
| MSFU | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| MSFU | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.48 | $2.48 (sr=2.4769) | PASS |  | Wilder ATR14 |
| MSFU | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| MSFU | L-ema21 | ladder row ema21: price and gap = price vs average | $39.44, -13.2% | $39.44, -13.2% | PASS |  |  |
| MSFU | L-note | "Last close $X · date" note = last completed bar | Last close $34.23 · Nov 20 | $34.23 · Nov 20 | PASS |  |  |
| MSFU | L-now | ladder price row = compared price; name = the basis label | $34.23 "After hours" | $34.23 "after hours" | PASS |  |  |
| MSFU | L-sma200 | ladder row sma200: price and gap = price vs average | $31.17, 9.8% | $31.17, 9.8% | PASS |  |  |
| MSFU | L-sma50 | ladder row sma50: price and gap = price vs average | $40.11, -14.7% | $40.11, -14.7% | PASS |  |  |
| MSFU | S5-price | S5: the same live price reads the same on the header and the Entry block | header $34.23 / entry $34.23 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| MSFU | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MSFU | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.4 | 34.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MSFU | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -15.5% vs +7.0% | -15.5% vs 7.0% | PASS |  |  |
| MSFU | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MSFU | T4 | ADX 14 (S1 /api/sr meta.adx) | 18.5 | 18.5 | PASS |  | Wilder, completed bars |
| MSFU | T4w | words "20 or more / below 20" | below 20 | ADX 18.5 | PASS |  |  |
| MSFU | T5 | "counted at the last close ($X, date)" = last completed bar | $34.23, Nov 20 | $34.23, Nov 20 | PASS |  |  |
| MSFU | T6 | price vs 200-day average (S1 pattern sma values) | $34.23 vs $31.17 · +9.8% | $34.23 vs $31.17 · 9.8% | PASS |  |  |
| MSFU | T6w | word "Above" | Above | Above | PASS |  |  |
| MSFU | T7 | price vs 50-day average (S1 pattern sma values) | $34.23 vs $40.11 · -14.7% | $34.23 vs $40.11 · -14.7% | PASS |  |  |
| MSFU | T7w | word "Below" | Below | Below | PASS |  |  |
| MSFU | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.9% over 30 td | +1.9% over 30 td | PASS |  |  |
| MSFU | T8r | word "rising" | still rising | rising | PASS |  |  |
| MSFU | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MSFU | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 25.4% below $45.88 | 25.4% below $45.88 | PASS |  | closing high would be 45.40 |
| MSFU | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 25.4% below | PASS |  |  |
| MSFU | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $45.88 | $45.880001068115234 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MSFU | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.68%, close location 0.15, OBV falling |
| MSFU | V2 | day change of the last completed bar | down 5.7% | -5.68% | PASS |  |  |
| MSFU | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1515) | PASS |  |  |
| MSFU | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MSFU | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.77× / 0.78× | 1.77× / 0.78× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MSFU | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 4386363) | 20 bars, last ('2026-11-20', 4386363) | PASS |  |  |
| MSFU | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.77, OBV falling | condition true | PASS |  |  |
| MTRX.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $28.17 | $28.17 | PASS |  |  |
| MTRX.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $30.69 | $30.69 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MTRX.TO | E3 | percent from the 21-day average | 8.2% below | 8.2% below | PASS |  |  |
| MTRX.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| MTRX.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.96 | $0.96 (sr=0.9578) | PASS |  | Wilder ATR14 |
| MTRX.TO | E5 | distance in normal day-moves | 2.6 | 2.6 | PASS |  | gauge dot note uses the same number:  · 2.6 day-moves below |
| MTRX.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.8 | +3.8 | PASS |  |  |
| MTRX.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $30.69, -8.2% | $30.69, -8.2% | PASS |  |  |
| MTRX.TO | L-now | ladder price row = compared price; name = the basis label | $28.17 "Last close" | $28.17 "last close" | PASS |  |  |
| MTRX.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $34.31, -17.9% | $34.31, -17.9% | PASS |  |  |
| MTRX.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $33.23, -15.2% | $33.23, -15.2% | PASS |  |  |
| MTRX.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.1 | 34.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MTRX.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -5.3% vs +7.0% | -5.3% vs 7.0% | PASS |  |  |
| MTRX.TO | T3w | words "past year" vs the window used | 210 / 251 bars back | 250-253 bars | PASS |  |  |
| MTRX.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.9 | 28.9 | PASS |  | Wilder, completed bars |
| MTRX.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 28.9 | PASS |  |  |
| MTRX.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.22%, close location 0.03, OBV falling |
| MTRX.TO | V2 | day change of the last completed bar | down 2.2% | -2.22% | PASS |  |  |
| MTRX.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.03 (raw 0.0254) | PASS |  |  |
| MTRX.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MTRX.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 1.0× from 2026-11-19 | 1.02× from 2026-11-19 | PASS |  | window "50 bars" includes the bar itself |
| MTRX.TO | V6 | Volume detail: last session date and RVOL | 2026-11-19 1.02× | 2026-11-19 1.02× | PASS |  |  |
| MTRX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.02× / 0.65× | 1.02× / 0.65× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MTRX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-19', 9740) | 20 bars, last ('2026-11-19', 9740) | PASS |  |  |
| MU.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $25.97 | $25.97 | PASS |  |  |
| MU.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $33.92 | $33.92 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| MU.TO | E3 | percent from the 21-day average | 23.4% below | 23.4% below | PASS |  |  |
| MU.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| MU.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.67 | $2.67 (sr=2.6694) | PASS |  | Wilder ATR14 |
| MU.TO | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| MU.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $33.92, -23.4% | $33.92, -23.4% | PASS |  |  |
| MU.TO | L-now | ladder price row = compared price; name = the basis label | $25.97 "Last close" | $25.97 "last close" | PASS |  |  |
| MU.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.96, -23.5% | $33.96, -23.5% | PASS |  |  |
| MU.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $39.91, -34.9% | $39.91, -34.9% | PASS |  |  |
| MU.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| MU.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.4 | 29.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| MU.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +188.2% vs +7.0% | 188.2% vs 7.0% | PASS |  |  |
| MU.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| MU.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.7 | 35.7 | PASS |  | Wilder, completed bars |
| MU.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 35.7 | PASS |  |  |
| MU.TO | T6 | price vs 200-day average (S1 pattern sma values) | $25.97 vs $33.96 · -23.5% | $25.97 vs $33.96 · -23.5% | PASS |  |  |
| MU.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T7 | price vs 50-day average (S1 pattern sma values) | $25.97 vs $39.92 · -34.9% | $25.97 vs $39.91 · -34.9% | PASS |  |  |
| MU.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| MU.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +9.9% over 30 td | +9.9% over 30 td | PASS |  |  |
| MU.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| MU.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| MU.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 53.0% below $55.28 | 53.0% below $55.28 | PASS |  | closing high would be 53.52 |
| MU.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 53.0% below | PASS |  |  |
| MU.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $55.28 | $55.282308204978015 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| MU.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -13.81%, close location 0.12, OBV falling |
| MU.TO | V2 | day change of the last completed bar | down 13.8% | -13.81% | PASS |  |  |
| MU.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1163) | PASS |  |  |
| MU.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| MU.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.84× / 1.34× | 2.84× / 1.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| MU.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 5604127) | 20 bars, last ('2026-11-20', 5604127) | PASS |  |  |
| MU.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.84, OBV falling | condition true | PASS |  |  |
| NEE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $83.45 | $83.45 | PASS |  |  |
| NEE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $84.05 | $84.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEE | E3 | percent from the 21-day average | 0.7% below | 0.7% below | PASS |  |  |
| NEE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NEE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.64 | $1.64 (sr=1.6423) | PASS |  | Wilder ATR14 |
| NEE | E5 | distance in normal day-moves | 0.4 | 0.4 | PASS |  | gauge dot note uses the same number:  · 0.4 day-moves below |
| NEE | L-ema21 | ladder row ema21: price and gap = price vs average | $84.05, -0.7% | $84.05, -0.7% | PASS |  |  |
| NEE | L-note | "Last close $X · date" note = last completed bar | Last close $83.45 · Nov 20 | $83.45 · Nov 20 | PASS |  |  |
| NEE | L-now | ladder price row = compared price; name = the basis label | $83.45 "After hours" | $83.45 "after hours" | PASS |  |  |
| NEE | L-sma200 | ladder row sma200: price and gap = price vs average | $86.48, -3.5% | $86.48, -3.5% | PASS |  |  |
| NEE | L-sma50 | ladder row sma50: price and gap = price vs average | $80.95, 3.1% | $80.95, 3.1% | PASS |  |  |
| NEE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $83.45 / entry $83.45 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 49.1 | 49.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +1.8% vs +7.0% | 1.8% vs 7.0% | PASS |  |  |
| NEE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEE | T4 | ADX 14 (S1 /api/sr meta.adx) | 30.0 | 30.0 | PASS |  | Wilder, completed bars |
| NEE | T4w | words "20 or more / below 20" | 20 or more | ADX 30.0 | PASS |  |  |
| NEE | T5 | "counted at the last close ($X, date)" = last completed bar | $83.45, Nov 20 | $83.45, Nov 20 | PASS |  |  |
| NEE | T6 | price vs 200-day average (S1 pattern sma values) | $83.45 vs $86.48 · -3.5% | $83.45 vs $86.48 · -3.5% | PASS |  |  |
| NEE | T6w | word "Below" | Below | Below | PASS |  |  |
| NEE | T7 | price vs 50-day average (S1 pattern sma values) | $83.45 vs $80.95 · +3.1% | $83.45 vs $80.95 · 3.1% | PASS |  |  |
| NEE | T7w | word "Above" | Above | Above | PASS |  |  |
| NEE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.2% over 30 td | +0.2% over 30 td | PASS |  |  |
| NEE | T8r | word "rising" | still rising | rising | PASS |  |  |
| NEE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.2% below $97.30 | 14.2% below $97.30 | PASS |  | closing high would be 96.44 |
| NEE | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.2% below | PASS |  |  |
| NEE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $97.30 | $97.30028062322594 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEE | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.41%, close location 0.09, OBV falling |
| NEE | V2 | day change of the last completed bar | down 0.4% | -0.41% | PASS |  |  |
| NEE | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0950) | PASS |  |  |
| NEE | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NEE | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.11× / 0.21× | 1.11× / 0.21× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEE | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 14141085) | 20 bars, last ('2026-11-20', 14141085) | PASS |  |  |
| NEM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $94.68 | $94.68 | PASS |  |  |
| NEM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $111.08 | $111.08 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NEM | E3 | percent from the 21-day average | 14.8% below | 14.8% below | PASS |  |  |
| NEM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NEM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.93 | $4.93 (sr=4.9293) | PASS |  | Wilder ATR14 |
| NEM | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| NEM | L-ema21 | ladder row ema21: price and gap = price vs average | $111.08, -14.8% | $111.08, -14.8% | PASS |  |  |
| NEM | L-note | "Last close $X · date" note = last completed bar | Last close $94.68 · Nov 20 | $94.68 · Nov 20 | PASS |  |  |
| NEM | L-now | ladder price row = compared price; name = the basis label | $94.68 "After hours" | $94.68 "after hours" | PASS |  |  |
| NEM | L-sma200 | ladder row sma200: price and gap = price vs average | $111.63, -15.2% | $111.63, -15.2% | PASS |  |  |
| NEM | L-sma50 | ladder row sma50: price and gap = price vs average | $115.72, -18.2% | $115.72, -18.2% | PASS |  |  |
| NEM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $94.68 / entry $94.68 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NEM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NEM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.7 | 29.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NEM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +16.5% vs +7.0% | 16.5% vs 7.0% | PASS |  |  |
| NEM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NEM | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.7 | 19.7 | PASS |  | Wilder, completed bars |
| NEM | T4w | words "20 or more / below 20" | below 20 | ADX 19.7 | PASS |  |  |
| NEM | T5 | "counted at the last close ($X, date)" = last completed bar | $94.68, Nov 20 | $94.68, Nov 20 | PASS |  |  |
| NEM | T6 | price vs 200-day average (S1 pattern sma values) | $94.68 vs $111.63 · -15.2% | $94.68 vs $111.63 · -15.2% | PASS |  |  |
| NEM | T6w | word "Below" | Below | Below | PASS |  |  |
| NEM | T7 | price vs 50-day average (S1 pattern sma values) | $94.68 vs $115.72 · -18.2% | $94.68 vs $115.72 · -18.2% | PASS |  |  |
| NEM | T7w | word "Below" | Below | Below | PASS |  |  |
| NEM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.1% over 30 td | +0.1% over 30 td | PASS |  |  |
| NEM | T8r | word "rising" | still rising | rising | PASS |  |  |
| NEM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NEM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 29.9% below $135.01 | 29.9% below $135.01 | PASS |  | closing high would be 134.86 |
| NEM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 29.9% below | PASS |  |  |
| NEM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $135.01 | $135.0089504972229 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NEM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.37%, close location 0.13, OBV falling |
| NEM | V2 | day change of the last completed bar | down 5.4% | -5.37% | PASS |  |  |
| NEM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.13 (raw 0.1344) | PASS |  |  |
| NEM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NEM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.09× / 1.03× | 2.09× / 1.03× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NEM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 14034974) | 20 bars, last ('2026-11-20', 14034974) | PASS |  |  |
| NEM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.09, OBV falling | condition true | PASS |  |  |
| NFLX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $56.73 | $56.73 | PASS |  |  |
| NFLX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $62.65 | $62.65 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFLX | E3 | percent from the 21-day average | 9.4% below | 9.4% below | PASS |  |  |
| NFLX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NFLX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.98 | $1.98 (sr=1.9754) | PASS |  | Wilder ATR14 |
| NFLX | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| NFLX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.8 | +8.8 | PASS |  |  |
| NFLX | L-ema21 | ladder row ema21: price and gap = price vs average | $62.65, -9.4% | $62.65, -9.4% | PASS |  |  |
| NFLX | L-note | "Last close $X · date" note = last completed bar | Last close $56.73 · Nov 20 | $56.73 · Nov 20 | PASS |  |  |
| NFLX | L-now | ladder price row = compared price; name = the basis label | $56.73 "After hours" | $56.73 "after hours" | PASS |  |  |
| NFLX | L-sma200 | ladder row sma200: price and gap = price vs average | $79.94, -29.0% | $79.94, -29.0% | PASS |  |  |
| NFLX | L-sma50 | ladder row sma50: price and gap = price vs average | $67.4, -15.8% | $67.40, -15.8% | PASS |  |  |
| NFLX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $56.73 / entry $56.73 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFLX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFLX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.5 | 27.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFLX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -46.3% vs +7.0% | -46.3% vs 7.0% | PASS |  |  |
| NFLX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFLX | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.0 | 27.0 | PASS |  | Wilder, completed bars |
| NFLX | T4w | words "20 or more / below 20" | 20 or more | ADX 27.0 | PASS |  |  |
| NFLX | T5 | "counted at the last close ($X, date)" = last completed bar | $56.73, Nov 20 | $56.73, Nov 20 | PASS |  |  |
| NFLX | T6 | price vs 200-day average (S1 pattern sma values) | $56.73 vs $79.94 · -29.0% | $56.73 vs $79.94 · -29.0% | PASS |  |  |
| NFLX | T6w | word "Below" | Below | Below | PASS |  |  |
| NFLX | T7 | price vs 50-day average (S1 pattern sma values) | $56.73 vs $67.40 · -15.8% | $56.73 vs $67.40 · -15.8% | PASS |  |  |
| NFLX | T7w | word "Below" | Below | Below | PASS |  |  |
| NFLX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.2% over 30 td | -4.2% over 30 td | PASS |  |  |
| NFLX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFLX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFLX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 48.9% below $111.10 | 48.9% below $111.10 | PASS |  | closing high would be 109.35 |
| NFLX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 48.9% below | PASS |  |  |
| NFLX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $111.10 | $111.1 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFLX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.96%, close location 0.06, OBV falling |
| NFLX | V2 | day change of the last completed bar | down 3.0% | -2.96% | PASS |  |  |
| NFLX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0609) | PASS |  |  |
| NFLX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFLX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.66× / 0.85× | 1.66× / 0.85× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFLX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 68034055) | 20 bars, last ('2026-11-20', 68034055) | PASS |  |  |
| NFLX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.66, OBV falling | condition true | PASS |  |  |
| NFXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $8.90 | $8.90 | PASS |  |  |
| NFXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $11.0 | $11.00 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NFXL | E3 | percent from the 21-day average | 19.1% below | 19.1% below | PASS |  |  |
| NFXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NFXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.70 | $0.70 (sr=0.7032) | PASS |  | Wilder ATR14 |
| NFXL | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| NFXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +12.8 | +12.8 | PASS |  |  |
| NFXL | L-ema21 | ladder row ema21: price and gap = price vs average | $11, -19.1% | $11.00, -19.1% | PASS |  |  |
| NFXL | L-note | "Last close $X · date" note = last completed bar | Last close $8.90 · Nov 20 | $8.90 · Nov 20 | PASS |  |  |
| NFXL | L-now | ladder price row = compared price; name = the basis label | $8.9 "After hours" | $8.90 "after hours" | PASS |  |  |
| NFXL | L-sma200 | ladder row sma200: price and gap = price vs average | $20.01, -55.5% | $20.01, -55.5% | PASS |  |  |
| NFXL | L-sma50 | ladder row sma50: price and gap = price vs average | $12.93, -31.2% | $12.93, -31.2% | PASS |  |  |
| NFXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $8.90 / entry $8.90 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NFXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NFXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.5 | 27.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NFXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -77.3% vs +7.0% | -77.3% vs 7.0% | PASS |  |  |
| NFXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NFXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.5 | 28.5 | PASS |  | Wilder, completed bars |
| NFXL | T4w | words "20 or more / below 20" | 20 or more | ADX 28.5 | PASS |  |  |
| NFXL | T5 | "counted at the last close ($X, date)" = last completed bar | $8.90, Nov 20 | $8.90, Nov 20 | PASS |  |  |
| NFXL | T6 | price vs 200-day average (S1 pattern sma values) | $8.90 vs $20.01 · -55.5% | $8.90 vs $20.01 · -55.5% | PASS |  |  |
| NFXL | T6w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T7 | price vs 50-day average (S1 pattern sma values) | $8.90 vs $12.93 · -31.2% | $8.90 vs $12.93 · -31.2% | PASS |  |  |
| NFXL | T7w | word "Below" | Below | Below | PASS |  |  |
| NFXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -9.9% over 30 td | -9.9% over 30 td | PASS |  |  |
| NFXL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NFXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NFXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 79.5% below $43.37 | 79.5% below $43.37 | PASS |  | closing high would be 41.83 |
| NFXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 79.5% below | PASS |  |  |
| NFXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.37 | $43.36974 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NFXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.82%, close location 0.07, OBV falling |
| NFXL | V2 | day change of the last completed bar | down 5.8% | -5.82% | PASS |  |  |
| NFXL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0674) | PASS |  |  |
| NFXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NFXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.35× / 0.74× | 1.35× / 0.74× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NFXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 2302134) | 20 bars, last ('2026-11-20', 2302134) | PASS |  |  |
| NTR.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $91.71 | $91.71 | PASS |  |  |
| NTR.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $98.19 | $98.19 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NTR.TO | E3 | percent from the 21-day average | 6.6% below | 6.6% below | PASS |  |  |
| NTR.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NTR.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.88 | $2.88 (sr=2.8844) | PASS |  | Wilder ATR14 |
| NTR.TO | E5 | distance in normal day-moves | 2.2 | 2.2 | PASS |  | gauge dot note uses the same number:  · 2.2 day-moves below |
| NTR.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $98.19, -6.6% | $98.19, -6.6% | PASS |  |  |
| NTR.TO | L-note | "Last close $X · date" note = last completed bar | Last close $91.71 · Nov 20 | $91.71 · Nov 20 | PASS |  |  |
| NTR.TO | L-now | ladder price row = compared price; name = the basis label | $91.71 "After hours" | $91.71 "after hours" | PASS |  |  |
| NTR.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $97.76, -6.2% | $97.76, -6.2% | PASS |  |  |
| NTR.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $100.33, -8.6% | $100.33, -8.6% | PASS |  |  |
| NTR.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $91.71 / entry $91.71 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NTR.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NTR.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.0 | 31.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NTR.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +22.1% vs +7.0% | 22.1% vs 7.0% | PASS |  |  |
| NTR.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NTR.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.1 | 23.1 | PASS |  | Wilder, completed bars |
| NTR.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 23.1 | PASS |  |  |
| NTR.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $91.71, Nov 20 | $91.71, Nov 20 | PASS |  |  |
| NTR.TO | T6 | price vs 200-day average (S1 pattern sma values) | $91.71 vs $97.76 · -6.2% | $91.71 vs $97.76 · -6.2% | PASS |  |  |
| NTR.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| NTR.TO | T7 | price vs 50-day average (S1 pattern sma values) | $91.71 vs $100.33 · -8.6% | $91.71 vs $100.33 · -8.6% | PASS |  |  |
| NTR.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| NTR.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.6% over 30 td | PASS |  |  |
| NTR.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| NTR.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NTR.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 19.7% below $114.19 | 19.7% below $114.19 | PASS |  | closing high would be 111.71 |
| NTR.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 19.7% below | PASS |  |  |
| NTR.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $114.19 | $114.18839715257722 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NTR.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.44%, close location 0.04, OBV falling |
| NTR.TO | V2 | day change of the last completed bar | down 2.4% | -2.44% | PASS |  |  |
| NTR.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.04 (raw 0.0391) | PASS |  |  |
| NTR.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NTR.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.78× / 0.78× | 0.78× / 0.77× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NTR.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 1469303) | 20 bars, last ('2026-11-20', 1469303) | PASS |  |  |
| NVDA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $125.53 | $125.53 | PASS |  |  |
| NVDA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $175.69 | $175.69 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDA | E3 | percent from the 21-day average | 28.6% below | 28.6% below | PASS |  |  |
| NVDA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NVDA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $10.71 | $10.71 (sr=10.7055) | PASS |  | Wilder ATR14 |
| NVDA | E5 | distance in normal day-moves | 4.7 | 4.7 | PASS |  | gauge dot note uses the same number:  · 4.7 day-moves below |
| NVDA | L-ema21 | ladder row ema21: price and gap = price vs average | $175.69, -28.6% | $175.69, -28.6% | PASS |  |  |
| NVDA | L-note | "Last close $X · date" note = last completed bar | Last close $125.53 · Nov 20 | $125.53 · Nov 20 | PASS |  |  |
| NVDA | L-now | ladder price row = compared price; name = the basis label | $125.53 "After hours" | $125.53 "after hours" | PASS |  |  |
| NVDA | L-sma200 | ladder row sma200: price and gap = price vs average | $203.35, -38.3% | $203.35, -38.3% | PASS |  |  |
| NVDA | L-sma50 | ladder row sma50: price and gap = price vs average | $207, -39.4% | $207.00, -39.4% | PASS |  |  |
| NVDA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $125.53 / entry $125.53 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 15.1 | 15.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -30.5% vs +7.0% | -30.5% vs 7.0% | PASS |  |  |
| NVDA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDA | T4 | ADX 14 (S1 /api/sr meta.adx) | 50.6 | 50.6 | PASS |  | Wilder, completed bars |
| NVDA | T4w | words "20 or more / below 20" | 20 or more | ADX 50.6 | PASS |  |  |
| NVDA | T5 | "counted at the last close ($X, date)" = last completed bar | $125.53, Nov 20 | $125.53, Nov 20 | PASS |  |  |
| NVDA | T6 | price vs 200-day average (S1 pattern sma values) | $125.53 vs $203.35 · -38.3% | $125.53 vs $203.35 · -38.3% | PASS |  |  |
| NVDA | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDA | T7 | price vs 50-day average (S1 pattern sma values) | $125.53 vs $207.00 · -39.4% | $125.53 vs $207.00 · -39.4% | PASS |  |  |
| NVDA | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.6% over 30 td | +0.6% over 30 td | PASS |  |  |
| NVDA | T8r | word "rising" | still rising | rising | PASS |  |  |
| NVDA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 48.4% below $243.37 | 48.4% below $243.37 | PASS |  | closing high would be 239.24 |
| NVDA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 48.4% below | PASS |  |  |
| NVDA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $243.37 | $243.37 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -14.01%, close location 0.05, OBV falling |
| NVDA | V2 | day change of the last completed bar | down 14.0% | -14.01% | PASS |  |  |
| NVDA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0536) | PASS |  |  |
| NVDA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.52× / 1.64× | 3.52× / 1.64× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 627659345) | 20 bars, last ('2026-11-20', 627659345) | PASS |  |  |
| NVDA | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.52, OBV falling | condition true | PASS |  |  |
| NVDL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $10.33 | $10.33 | PASS |  |  |
| NVDL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $21.73 | $21.73 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| NVDL | E3 | percent from the 21-day average | 52.5% below | 52.5% below | PASS |  |  |
| NVDL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| NVDL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.59 | $2.59 (sr=2.5897) | PASS |  | Wilder ATR14 |
| NVDL | E5 | distance in normal day-moves | 4.4 | 4.4 | PASS |  | gauge dot note uses the same number:  · 4.4 day-moves below |
| NVDL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.3 | +3.3 | PASS |  |  |
| NVDL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.6 | +3.6 | PASS |  |  |
| NVDL | L-ema21 | ladder row ema21: price and gap = price vs average | $21.73, -52.5% | $21.73, -52.5% | PASS |  |  |
| NVDL | L-note | "Last close $X · date" note = last completed bar | Last close $10.33 · Nov 20 | $10.33 · Nov 20 | PASS |  |  |
| NVDL | L-now | ladder price row = compared price; name = the basis label | $10.33 "After hours" | $10.33 "after hours" | PASS |  |  |
| NVDL | L-sma200 | ladder row sma200: price and gap = price vs average | $31.12, -66.8% | $31.12, -66.8% | PASS |  |  |
| NVDL | L-sma50 | ladder row sma50: price and gap = price vs average | $30.38, -66.0% | $30.38, -66.0% | PASS |  |  |
| NVDL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $10.33 / entry $10.33 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| NVDL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| NVDL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 16.6 | 16.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| NVDL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -63.4% vs +7.0% | -63.4% vs 7.0% | PASS |  |  |
| NVDL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| NVDL | T4 | ADX 14 (S1 /api/sr meta.adx) | 50.7 | 50.7 | PASS |  | Wilder, completed bars |
| NVDL | T4w | words "20 or more / below 20" | 20 or more | ADX 50.7 | PASS |  |  |
| NVDL | T5 | "counted at the last close ($X, date)" = last completed bar | $10.33, Nov 20 | $10.33, Nov 20 | PASS |  |  |
| NVDL | T6 | price vs 200-day average (S1 pattern sma values) | $10.33 vs $31.12 · -66.8% | $10.33 vs $31.12 · -66.8% | PASS |  |  |
| NVDL | T6w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T7 | price vs 50-day average (S1 pattern sma values) | $10.33 vs $30.38 · -66.0% | $10.33 vs $30.38 · -66.0% | PASS |  |  |
| NVDL | T7w | word "Below" | Below | Below | PASS |  |  |
| NVDL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.2% over 30 td | -1.2% over 30 td | PASS |  |  |
| NVDL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| NVDL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| NVDL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 76.1% below $43.27 | 76.1% below $43.27 | PASS |  | closing high would be 43.02 |
| NVDL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 76.1% below | PASS |  |  |
| NVDL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $43.27 | $43.27333450317383 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| NVDL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -27.51%, close location 0.08, OBV falling |
| NVDL | V2 | day change of the last completed bar | down 27.5% | -27.51% | PASS |  |  |
| NVDL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0751) | PASS |  |  |
| NVDL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| NVDL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 4.23× / 1.10× | 4.23× / 1.10× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| NVDL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 89405436) | 20 bars, last ('2026-11-20', 89405436) | PASS |  |  |
| NVDL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 4.23, OBV falling | condition true | PASS |  |  |
| ONTO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $170.16 | $170.16 | PASS |  |  |
| ONTO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $203.71 | $203.71 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ONTO | E3 | percent from the 21-day average | 16.5% below | 16.5% below | PASS |  |  |
| ONTO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ONTO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.80 | $17.80 (sr=17.8006) | PASS |  | Wilder ATR14 |
| ONTO | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| ONTO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.2 | +3.2 | PASS |  |  |
| ONTO | L-ema21 | ladder row ema21: price and gap = price vs average | $203.71, -16.5% | $203.71, -16.5% | PASS |  |  |
| ONTO | L-note | "Last close $X · date" note = last completed bar | Last close $170.16 · Nov 20 | $170.16 · Nov 20 | PASS |  |  |
| ONTO | L-now | ladder price row = compared price; name = the basis label | $170.16 "After hours" | $170.16 "after hours" | PASS |  |  |
| ONTO | L-sma200 | ladder row sma200: price and gap = price vs average | $259.91, -34.5% | $259.91, -34.5% | PASS |  |  |
| ONTO | L-sma50 | ladder row sma50: price and gap = price vs average | $239.77, -29.0% | $239.77, -29.0% | PASS |  |  |
| ONTO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $170.16 / entry $170.16 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ONTO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ONTO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.8 | 35.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ONTO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +35.8% vs +7.0% | 35.8% vs 7.0% | PASS |  |  |
| ONTO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ONTO | T4 | ADX 14 (S1 /api/sr meta.adx) | 25.8 | 25.8 | PASS |  | Wilder, completed bars |
| ONTO | T4w | words "20 or more / below 20" | 20 or more | ADX 25.8 | PASS |  |  |
| ONTO | T5 | "counted at the last close ($X, date)" = last completed bar | $170.16, Nov 20 | $170.16, Nov 20 | PASS |  |  |
| ONTO | T6 | price vs 200-day average (S1 pattern sma values) | $170.16 vs $259.91 · -34.5% | $170.16 vs $259.91 · -34.5% | PASS |  |  |
| ONTO | T6w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T7 | price vs 50-day average (S1 pattern sma values) | $170.16 vs $239.77 · -29.0% | $170.16 vs $239.77 · -29.0% | PASS |  |  |
| ONTO | T7w | word "Below" | Below | Below | PASS |  |  |
| ONTO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.0% over 30 td | +1.0% over 30 td | PASS |  |  |
| ONTO | T8r | word "rising" | still rising | rising | PASS |  |  |
| ONTO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ONTO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 56.0% below $386.46 | 56.0% below $386.46 | PASS |  | closing high would be 378.45 |
| ONTO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 56.0% below | PASS |  |  |
| ONTO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $386.46 | $386.4599914550781 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ONTO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -13.15%, close location 0.17, OBV falling |
| ONTO | V2 | day change of the last completed bar | down 13.2% | -13.15% | PASS |  |  |
| ONTO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.17 (raw 0.1683) | PASS |  |  |
| ONTO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ONTO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.15× / 1.26× | 1.15× / 1.26× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ONTO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 1223904) | 20 bars, last ('2026-11-20', 1223904) | PASS |  |  |
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
| ORBX.TO | V5 | relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol) | 0.5× from 2026-11-18 | 0.51× from 2026-11-18 | PASS |  | window "50 bars" includes the bar itself |
| ORBX.TO | V6 | Volume detail: last session date and RVOL | 2026-11-18 0.51× | 2026-11-18 0.51× | PASS |  |  |
| ORBX.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.51× / 0.11× | 0.51× / 0.11× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORBX.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-18', 3267) | 20 bars, last ('2026-11-18', 3267) | PASS |  |  |
| ORCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $101.19 | $101.19 | PASS |  |  |
| ORCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $121.12 | $121.12 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| ORCL | E3 | percent from the 21-day average | 16.5% below | 16.5% below | PASS |  |  |
| ORCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| ORCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $7.94 | $7.94 (sr=7.9361) | PASS |  | Wilder ATR14 |
| ORCL | E5 | distance in normal day-moves | 2.5 | 2.5 | PASS |  | gauge dot note uses the same number:  · 2.5 day-moves below |
| ORCL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.9 | +3.9 | PASS |  |  |
| ORCL | L-ema21 | ladder row ema21: price and gap = price vs average | $121.12, -16.5% | $121.12, -16.5% | PASS |  |  |
| ORCL | L-note | "Last close $X · date" note = last completed bar | Last close $101.19 · Nov 20 | $101.19 · Nov 20 | PASS |  |  |
| ORCL | L-now | ladder price row = compared price; name = the basis label | $101.19 "After hours" | $101.19 "after hours" | PASS |  |  |
| ORCL | L-sma200 | ladder row sma200: price and gap = price vs average | $152.19, -33.5% | $152.19, -33.5% | PASS |  |  |
| ORCL | L-sma50 | ladder row sma50: price and gap = price vs average | $131.94, -23.3% | $131.94, -23.3% | PASS |  |  |
| ORCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $101.19 / entry $101.19 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| ORCL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| ORCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.9 | 31.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| ORCL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -51.3% vs +7.0% | -51.3% vs 7.0% | PASS |  |  |
| ORCL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| ORCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 15.9 | 15.9 | PASS |  | Wilder, completed bars |
| ORCL | T4w | words "20 or more / below 20" | below 20 | ADX 15.9 | PASS |  |  |
| ORCL | T5 | "counted at the last close ($X, date)" = last completed bar | $101.19, Nov 20 | $101.19, Nov 20 | PASS |  |  |
| ORCL | T6 | price vs 200-day average (S1 pattern sma values) | $101.19 vs $152.19 · -33.5% | $101.19 vs $152.19 · -33.5% | PASS |  |  |
| ORCL | T6w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T7 | price vs 50-day average (S1 pattern sma values) | $101.19 vs $131.94 · -23.3% | $101.19 vs $131.94 · -23.3% | PASS |  |  |
| ORCL | T7w | word "Below" | Below | Below | PASS |  |  |
| ORCL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.2% over 30 td | -5.2% over 30 td | PASS |  |  |
| ORCL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| ORCL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| ORCL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 59.3% below $248.46 | 59.3% below $248.46 | PASS |  | closing high would be 246.38 |
| ORCL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 59.3% below | PASS |  |  |
| ORCL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $248.46 | $248.4634626242363 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| ORCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -8.48%, close location 0.11, OBV falling |
| ORCL | V2 | day change of the last completed bar | down 8.5% | -8.48% | PASS |  |  |
| ORCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1076) | PASS |  |  |
| ORCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| ORCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.34× / 1.08× | 1.34× / 1.08× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| ORCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 47255609) | 20 bars, last ('2026-11-20', 47255609) | PASS |  |  |
| PG | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $169.37 | $169.37 | PASS |  |  |
| PG | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $165.69 | $165.69 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PG | E3 | percent from the 21-day average | 2.2% above | 2.2% above | PASS |  |  |
| PG | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| PG | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.20 | $3.20 (sr=3.2012) | PASS |  | Wilder ATR14 |
| PG | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves above |
| PG | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -5.4 | -5.4 | PASS |  |  |
| PG | L-ema21 | ladder row ema21: price and gap = price vs average | $165.69, 2.2% | $165.69, 2.2% | PASS |  |  |
| PG | L-note | "Last close $X · date" note = last completed bar | Last close $169.46 · Nov 20 | $169.46 · Nov 20 | PASS |  |  |
| PG | L-now | ladder price row = compared price; name = the basis label | $169.37 "After hours" | $169.37 "after hours" | PASS |  |  |
| PG | L-sma200 | ladder row sma200: price and gap = price vs average | $148.47, 14.1% | $148.47, 14.1% | PASS |  |  |
| PG | L-sma50 | ladder row sma50: price and gap = price vs average | $156.28, 8.4% | $156.28, 8.4% | PASS |  |  |
| PG | S5-price | S5: the same live price reads the same on the header and the Entry block | header $169.37 / entry $169.37 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PG | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PG | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 61.7 | 61.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PG | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +17.6% vs +7.0% | 17.6% vs 7.0% | PASS |  |  |
| PG | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PG | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.2 | 40.2 | PASS |  | Wilder, completed bars |
| PG | T4w | words "20 or more / below 20" | 20 or more | ADX 40.2 | PASS |  |  |
| PG | T5 | "counted at the last close ($X, date)" = last completed bar | $169.46, Nov 20 | $169.46, Nov 20 | PASS |  |  |
| PG | T6 | price vs 200-day average (S1 pattern sma values) | $169.46 vs $148.47 · +14.1% | $169.46 vs $148.47 · 14.1% | PASS |  |  |
| PG | T6w | word "Above" | Above | Above | PASS |  |  |
| PG | T7 | price vs 50-day average (S1 pattern sma values) | $169.46 vs $156.28 · +8.4% | $169.46 vs $156.28 · 8.4% | PASS |  |  |
| PG | T7w | word "Above" | Above | Above | PASS |  |  |
| PG | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| PG | T8r | word "rising" | still rising | rising | PASS |  |  |
| PG | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PG | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 2.4% below $173.59 | 2.4% below $173.59 | PASS |  | closing high would be 173.02 |
| PG | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 2.4% below | PASS |  |  |
| PG | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $173.59 | $173.59 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PG | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 0.96%, close location 0.16, OBV rising |
| PG | V2 | day change of the last completed bar | up 1.0% | +0.96% | PASS |  |  |
| PG | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.16 (raw 0.1602) | PASS |  |  |
| PG | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| PG | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.44× / 0.51× | 2.44× / 0.51× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PG | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 23502527) | 20 bars, last ('2026-11-20', 23502527) | PASS |  |  |
| PLD | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $122.50 | $122.50 | PASS |  |  |
| PLD | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $127.29 | $127.29 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PLD | E3 | percent from the 21-day average | 3.8% below | 3.8% below | PASS |  |  |
| PLD | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| PLD | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.52 | $2.52 (sr=2.515) | PASS |  | Wilder ATR14 |
| PLD | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| PLD | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +3.6 | +3.6 | PASS |  |  |
| PLD | L-ema21 | ladder row ema21: price and gap = price vs average | $127.29, -3.8% | $127.29, -3.8% | PASS |  |  |
| PLD | L-note | "Last close $X · date" note = last completed bar | Last close $122.50 · Nov 20 | $122.50 · Nov 20 | PASS |  |  |
| PLD | L-now | ladder price row = compared price; name = the basis label | $122.5 "After hours" | $122.50 "after hours" | PASS |  |  |
| PLD | L-sma200 | ladder row sma200: price and gap = price vs average | $136.23, -10.1% | $136.23, -10.1% | PASS |  |  |
| PLD | L-sma50 | ladder row sma50: price and gap = price vs average | $129.46, -5.4% | $129.46, -5.4% | PASS |  |  |
| PLD | S5-price | S5: the same live price reads the same on the header and the Entry block | header $122.50 / entry $122.50 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| PLD | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PLD | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.0 | 34.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PLD | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +2.6% vs +7.0% | 2.6% vs 7.0% | PASS |  |  |
| PLD | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PLD | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.6 | 16.6 | PASS |  | Wilder, completed bars |
| PLD | T4w | words "20 or more / below 20" | below 20 | ADX 16.6 | PASS |  |  |
| PLD | T5 | "counted at the last close ($X, date)" = last completed bar | $122.50, Nov 20 | $122.50, Nov 20 | PASS |  |  |
| PLD | T6 | price vs 200-day average (S1 pattern sma values) | $122.50 vs $136.23 · -10.1% | $122.50 vs $136.23 · -10.1% | PASS |  |  |
| PLD | T6w | word "Below" | Below | Below | PASS |  |  |
| PLD | T7 | price vs 50-day average (S1 pattern sma values) | $122.50 vs $129.46 · -5.4% | $122.50 vs $129.46 · -5.4% | PASS |  |  |
| PLD | T7w | word "Below" | Below | Below | PASS |  |  |
| PLD | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.1% over 30 td | +0.1% over 30 td | PASS |  |  |
| PLD | T8r | word "rising" | still rising | rising | PASS |  |  |
| PLD | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PLD | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 19.5% below $152.14 | 19.5% below $152.14 | PASS |  | closing high would be 148.88 |
| PLD | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 19.5% below | PASS |  |  |
| PLD | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $152.14 | $152.14207825389113 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PLD | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -0.70%, close location 0.09, OBV falling |
| PLD | V2 | day change of the last completed bar | down 0.7% | -0.70% | PASS |  |  |
| PLD | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0889) | PASS |  |  |
| PLD | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PLD | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.33× / 0.34× | 1.33× / 0.34× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PLD | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 5216938) | 20 bars, last ('2026-11-20', 5216938) | PASS |  |  |
| PNG.V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $2.79 | $2.79 | PASS |  |  |
| PNG.V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $3.46 | $3.46 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| PNG.V | E3 | percent from the 21-day average | 19.4% below | 19.4% below | PASS |  |  |
| PNG.V | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| PNG.V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.22 | $0.22 (sr=0.2205) | PASS |  | Wilder ATR14 |
| PNG.V | E5 | distance in normal day-moves | 3.0 | 3.0 | PASS |  | gauge dot note uses the same number:  · 3.0 day-moves below |
| PNG.V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +13.9 | +13.9 | PASS |  |  |
| PNG.V | L-ema21 | ladder row ema21: price and gap = price vs average | $3.46, -19.4% | $3.46, -19.4% | PASS |  |  |
| PNG.V | L-now | ladder price row = compared price; name = the basis label | $2.79 "Last close" | $2.79 "last close" | PASS |  |  |
| PNG.V | L-sma200 | ladder row sma200: price and gap = price vs average | $6.53, -57.3% | $6.53, -57.3% | PASS |  |  |
| PNG.V | L-sma50 | ladder row sma50: price and gap = price vs average | $4.04, -31.0% | $4.04, -31.0% | PASS |  |  |
| PNG.V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| PNG.V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 22.3 | 22.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| PNG.V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -46.5% vs +7.0% | -46.4% vs 7.0% | PASS |  |  |
| PNG.V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| PNG.V | T4 | ADX 14 (S1 /api/sr meta.adx) | 41.9 | 41.8 | PASS |  | Wilder, completed bars |
| PNG.V | T4w | words "20 or more / below 20" | 20 or more | ADX 41.8 | PASS |  |  |
| PNG.V | T6 | price vs 200-day average (S1 pattern sma values) | $2.79 vs $6.53 · -57.3% | $2.79 vs $6.53 · -57.3% | PASS |  |  |
| PNG.V | T6w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T7 | price vs 50-day average (S1 pattern sma values) | $2.79 vs $4.04 · -30.9% | $2.79 vs $4.04 · -31.0% | PASS |  |  |
| PNG.V | T7w | word "Below" | Below | Below | PASS |  |  |
| PNG.V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -8.2% over 30 td | -8.2% over 30 td | PASS |  |  |
| PNG.V | T8r | word "rising" | not rising | not rising | PASS |  |  |
| PNG.V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| PNG.V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 74.0% below $10.72 | 74.0% below $10.72 | PASS |  | closing high would be 10.23 |
| PNG.V | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 74.0% below | PASS |  |  |
| PNG.V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $10.72 | $10.720000267028809 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| PNG.V | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -3.12%, close location 0.56, OBV falling |
| PNG.V | V2 | day change of the last completed bar | down 3.1% | -3.12% | PASS |  |  |
| PNG.V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| PNG.V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.97× / 0.40× | 2.97× / 0.40× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| PNG.V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3766453) | 20 bars, last ('2026-11-20', 3766453) | PASS |  |  |
| PNG.V | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.97, OBV falling | condition true | PASS |  |  |
| QCOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $149.94 | $149.94 | PASS |  |  |
| QCOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $168.54 | $168.54 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QCOM | E3 | percent from the 21-day average | 11.0% below | 11.0% below | PASS |  |  |
| QCOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QCOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $9.34 | $9.34 (sr=9.3414) | PASS |  | Wilder ATR14 |
| QCOM | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| QCOM | L-ema21 | ladder row ema21: price and gap = price vs average | $168.54, -11.0% | $168.54, -11.0% | PASS |  |  |
| QCOM | L-note | "Last close $X · date" note = last completed bar | Last close $149.94 · Nov 20 | $149.94 · Nov 20 | PASS |  |  |
| QCOM | L-now | ladder price row = compared price; name = the basis label | $149.94 "After hours" | $149.94 "after hours" | PASS |  |  |
| QCOM | L-sma200 | ladder row sma200: price and gap = price vs average | $169.58, -11.6% | $169.58, -11.6% | PASS |  |  |
| QCOM | L-sma50 | ladder row sma50: price and gap = price vs average | $177.31, -15.4% | $177.31, -15.4% | PASS |  |  |
| QCOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $149.94 / entry $149.94 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QCOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QCOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.1 | 35.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QCOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -4.1% vs +7.0% | -4.1% vs 7.0% | PASS |  |  |
| QCOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QCOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.7 | 11.7 | PASS |  | Wilder, completed bars |
| QCOM | T4w | words "20 or more / below 20" | below 20 | ADX 11.7 | PASS |  |  |
| QCOM | T5 | "counted at the last close ($X, date)" = last completed bar | $149.94, Nov 20 | $149.94, Nov 20 | PASS |  |  |
| QCOM | T6 | price vs 200-day average (S1 pattern sma values) | $149.94 vs $169.58 · -11.6% | $149.94 vs $169.58 · -11.6% | PASS |  |  |
| QCOM | T6w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T7 | price vs 50-day average (S1 pattern sma values) | $149.94 vs $177.31 · -15.4% | $149.94 vs $177.31 · -15.4% | PASS |  |  |
| QCOM | T7w | word "Below" | Below | Below | PASS |  |  |
| QCOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.9% over 30 td | +0.9% over 30 td | PASS |  |  |
| QCOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QCOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QCOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 41.8% below $257.56 | 41.8% below $257.56 | PASS |  | closing high would be 248.74 |
| QCOM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 41.8% below | PASS |  |  |
| QCOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $257.56 | $257.5617517963296 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QCOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.45%, close location 0.06, OBV falling |
| QCOM | V2 | day change of the last completed bar | down 7.5% | -7.45% | PASS |  |  |
| QCOM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0604) | PASS |  |  |
| QCOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QCOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.66× / 1.20× | 1.66× / 1.20× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QCOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 22220705) | 20 bars, last ('2026-11-20', 22220705) | PASS |  |  |
| QCOM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.66, OBV falling | condition true | PASS |  |  |
| QPUX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $2.47 | $2.47 | PASS |  |  |
| QPUX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $5.11 | $5.11 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QPUX | E3 | percent from the 21-day average | 51.7% below | 51.7% below | PASS |  |  |
| QPUX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QPUX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.81 | $0.81 (sr=0.8079) | PASS |  | Wilder ATR14 |
| QPUX | E5 | distance in normal day-moves | 3.3 | 3.3 | PASS |  | gauge dot note uses the same number:  · 3.3 day-moves below |
| QPUX | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.2 | +4.2 | PASS |  |  |
| QPUX | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +18.4 | +18.4 | PASS |  |  |
| QPUX | L-ema21 | ladder row ema21: price and gap = price vs average | $5.11, -51.7% | $5.11, -51.7% | PASS |  |  |
| QPUX | L-note | "Last close $X · date" note = last completed bar | Last close $2.47 · Nov 20 | $2.47 · Nov 20 | PASS |  |  |
| QPUX | L-now | ladder price row = compared price; name = the basis label | $2.47 "After hours" | $2.47 "after hours" | PASS |  |  |
| QPUX | L-sma200 | ladder row sma200: price and gap = price vs average | $19.99, -87.6% | $19.99, -87.6% | PASS |  |  |
| QPUX | L-sma50 | ladder row sma50: price and gap = price vs average | $8.47, -70.9% | $8.47, -70.9% | PASS |  |  |
| QPUX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $2.47 / entry $2.47 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QPUX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QPUX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 26.1 | 26.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QPUX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -94.7% vs +7.0% | -94.7% vs 7.0% | PASS |  |  |
| QPUX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QPUX | T4 | ADX 14 (S1 /api/sr meta.adx) | 40.7 | 40.7 | PASS |  | Wilder, completed bars |
| QPUX | T4w | words "20 or more / below 20" | 20 or more | ADX 40.7 | PASS |  |  |
| QPUX | T5 | "counted at the last close ($X, date)" = last completed bar | $2.47, Nov 20 | $2.47, Nov 20 | PASS |  |  |
| QPUX | T6 | price vs 200-day average (S1 pattern sma values) | $2.47 vs $19.99 · -87.6% | $2.47 vs $19.99 · -87.6% | PASS |  |  |
| QPUX | T6w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T7 | price vs 50-day average (S1 pattern sma values) | $2.47 vs $8.47 · -70.8% | $2.47 vs $8.47 · -70.9% | PASS |  |  |
| QPUX | T7w | word "Below" | Below | Below | PASS |  |  |
| QPUX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -25.3% over 30 td | -25.3% over 30 td | PASS |  |  |
| QPUX | T8r | word "rising" | not rising | not rising | PASS |  |  |
| QPUX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QPUX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 96.9% below $80.28 | 96.9% below $80.28 | PASS |  | closing high would be 79.57 |
| QPUX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 96.9% below | PASS |  |  |
| QPUX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $80.28 | $80.27999877929688 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QPUX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -13.64%, close location 0.12, OBV falling |
| QPUX | V2 | day change of the last completed bar | down 13.6% | -13.64% | PASS |  |  |
| QPUX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1163) | PASS |  |  |
| QPUX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QPUX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.14× / 0.42× | 2.14× / 0.42× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QPUX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 680124) | 20 bars, last ('2026-11-20', 680124) | PASS |  |  |
| QPUX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.14, OBV falling | condition true | PASS |  |  |
| QTUM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $111.43 | $111.43 | PASS |  |  |
| QTUM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $128.98 | $128.98 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| QTUM | E3 | percent from the 21-day average | 13.6% below | 13.6% below | PASS |  |  |
| QTUM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| QTUM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.09 | $5.09 (sr=5.0875) | PASS |  | Wilder ATR14 |
| QTUM | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| QTUM | L-ema21 | ladder row ema21: price and gap = price vs average | $128.98, -13.6% | $128.98, -13.6% | PASS |  |  |
| QTUM | L-note | "Last close $X · date" note = last completed bar | Last close $111.43 · Nov 20 | $111.43 · Nov 20 | PASS |  |  |
| QTUM | L-now | ladder price row = compared price; name = the basis label | $111.43 "After hours" | $111.43 "after hours" | PASS |  |  |
| QTUM | L-sma200 | ladder row sma200: price and gap = price vs average | $138.05, -19.3% | $138.05, -19.3% | PASS |  |  |
| QTUM | L-sma50 | ladder row sma50: price and gap = price vs average | $140.48, -20.7% | $140.48, -20.7% | PASS |  |  |
| QTUM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $111.43 / entry $111.43 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| QTUM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| QTUM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.1 | 28.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| QTUM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +12.2% vs +7.0% | 12.2% vs 7.0% | PASS |  |  |
| QTUM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| QTUM | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.9 | 34.9 | PASS |  | Wilder, completed bars |
| QTUM | T4w | words "20 or more / below 20" | 20 or more | ADX 34.9 | PASS |  |  |
| QTUM | T5 | "counted at the last close ($X, date)" = last completed bar | $111.43, Nov 20 | $111.43, Nov 20 | PASS |  |  |
| QTUM | T6 | price vs 200-day average (S1 pattern sma values) | $111.43 vs $138.05 · -19.3% | $111.43 vs $138.05 · -19.3% | PASS |  |  |
| QTUM | T6w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T7 | price vs 50-day average (S1 pattern sma values) | $111.43 vs $140.48 · -20.7% | $111.43 vs $140.48 · -20.7% | PASS |  |  |
| QTUM | T7w | word "Below" | Below | Below | PASS |  |  |
| QTUM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.1% over 30 td | +2.1% over 30 td | PASS |  |  |
| QTUM | T8r | word "rising" | still rising | rising | PASS |  |  |
| QTUM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| QTUM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.1% below $169.21 | 34.1% below $169.21 | PASS |  | closing high would be 167.98 |
| QTUM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.1% below | PASS |  |  |
| QTUM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $169.21 | $169.21042 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| QTUM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.92%, close location 0.10, OBV falling |
| QTUM | V2 | day change of the last completed bar | down 6.9% | -6.92% | PASS |  |  |
| QTUM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.0997) | PASS |  |  |
| QTUM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| QTUM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.04× / 1.52× | 2.04× / 1.51× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| QTUM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 716466) | 20 bars, last ('2026-11-20', 716466) | PASS |  |  |
| QTUM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.04, OBV falling | condition true | PASS |  |  |
| RBOT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $25.00 | $25.00 | PASS |  |  |
| RBOT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $28.53 | $28.53 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RBOT.TO | E3 | percent from the 21-day average | 12.4% below | 12.4% below | PASS |  |  |
| RBOT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| RBOT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.66 | $0.66 (sr=0.662) | PASS |  | Wilder ATR14 |
| RBOT.TO | E5 | distance in normal day-moves | 5.3 | 5.3 | PASS |  | gauge dot note uses the same number:  ◂ · 5.3 day-moves below |
| RBOT.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| RBOT.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.0 | +7.0 | PASS |  |  |
| RBOT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $28.53, -12.4% | $28.53, -12.4% | PASS |  |  |
| RBOT.TO | L-now | ladder price row = compared price; name = the basis label | $25 "Last close" | $25.00 "last close" | PASS |  |  |
| RBOT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $33.17, -24.6% | $33.17, -24.6% | PASS |  |  |
| RBOT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $30.57, -18.2% | $30.57, -18.2% | PASS |  |  |
| RBOT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RBOT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 23.0 | 23.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RBOT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -18.4% vs +7.0% | -18.4% vs 7.0% | PASS |  |  |
| RBOT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RBOT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 39.5 | 39.5 | PASS |  | Wilder, completed bars |
| RBOT.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 39.5 | PASS |  |  |
| RBOT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $25.00 vs $33.17 · -24.6% | $25.00 vs $33.17 · -24.6% | PASS |  |  |
| RBOT.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| RBOT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $25.00 vs $30.57 · -18.2% | $25.00 vs $30.57 · -18.2% | PASS |  |  |
| RBOT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| RBOT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.4% over 30 td | -2.3% over 30 td | PASS |  |  |
| RBOT.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| RBOT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RBOT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.5% below $38.15 | 34.5% below $38.15 | PASS |  | closing high would be 38.15 |
| RBOT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.5% below | PASS |  |  |
| RBOT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $38.15 | $38.150001525878906 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RBOT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.12%, close location 0.00, OBV falling |
| RBOT.TO | V2 | day change of the last completed bar | down 6.1% | -6.12% | PASS |  |  |
| RBOT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| RBOT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RBOT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.92× / 2.31× | 1.92× / 2.31× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RBOT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 6310) | 20 bars, last ('2026-11-20', 6310) | PASS |  |  |
| RBOT.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.92, OBV falling | condition true | PASS |  |  |
| RTX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $190.17 | $190.17 | PASS |  |  |
| RTX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $195.52 | $195.52 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RTX | E3 | percent from the 21-day average | 2.7% below | 2.7% below | PASS |  |  |
| RTX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| RTX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.37 | $5.37 (sr=5.3749) | PASS |  | Wilder ATR14 |
| RTX | E5 | distance in normal day-moves | 1.0 | 1.0 | PASS |  | gauge dot note uses the same number:  · 1.0 day-moves below |
| RTX | L-ema21 | ladder row ema21: price and gap = price vs average | $195.52, -2.7% | $195.52, -2.7% | PASS |  |  |
| RTX | L-note | "Last close $X · date" note = last completed bar | Last close $190.17 · Nov 20 | $190.17 · Nov 20 | PASS |  |  |
| RTX | L-now | ladder price row = compared price; name = the basis label | $190.17 "After hours" | $190.17 "after hours" | PASS |  |  |
| RTX | L-sma200 | ladder row sma200: price and gap = price vs average | $194.44, -2.2% | $194.44, -2.2% | PASS |  |  |
| RTX | L-sma50 | ladder row sma50: price and gap = price vs average | $192.42, -1.2% | $192.42, -1.2% | PASS |  |  |
| RTX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $190.17 / entry $190.17 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RTX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RTX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.0 | 43.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RTX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +11.7% vs +7.0% | 11.7% vs 7.0% | PASS |  |  |
| RTX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RTX | T4 | ADX 14 (S1 /api/sr meta.adx) | 16.0 | 16.0 | PASS |  | Wilder, completed bars |
| RTX | T4w | words "20 or more / below 20" | below 20 | ADX 16.0 | PASS |  |  |
| RTX | T5 | "counted at the last close ($X, date)" = last completed bar | $190.17, Nov 20 | $190.17, Nov 20 | PASS |  |  |
| RTX | T6 | price vs 200-day average (S1 pattern sma values) | $190.17 vs $194.44 · -2.2% | $190.17 vs $194.44 · -2.2% | PASS |  |  |
| RTX | T6w | word "Below" | Below | Below | PASS |  |  |
| RTX | T7 | price vs 50-day average (S1 pattern sma values) | $190.17 vs $192.42 · -1.2% | $190.17 vs $192.42 · -1.2% | PASS |  |  |
| RTX | T7w | word "Below" | Below | Below | PASS |  |  |
| RTX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.3% over 30 td | +0.3% over 30 td | PASS |  |  |
| RTX | T8r | word "rising" | still rising | rising | PASS |  |  |
| RTX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RTX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 16.0% below $226.41 | 16.0% below $226.41 | PASS |  | closing high would be 225.49 |
| RTX | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 16.0% below | PASS |  |  |
| RTX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $226.41 | $226.41000366210938 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RTX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -1.69%, close location 0.08, OBV falling |
| RTX | V2 | day change of the last completed bar | down 1.7% | -1.69% | PASS |  |  |
| RTX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0821) | PASS |  |  |
| RTX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RTX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.22× / 0.60× | 1.22× / 0.60× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RTX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 6037843) | 20 bars, last ('2026-11-20', 6037843) | PASS |  |  |
| RY.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $263.05 | $263.05 | PASS |  |  |
| RY.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $280.78 | $280.78 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| RY.TO | E3 | percent from the 21-day average | 6.3% below | 6.3% below | PASS |  |  |
| RY.TO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| RY.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.19 | $5.19 (sr=5.1854) | PASS |  | Wilder ATR14 |
| RY.TO | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| RY.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $280.78, -6.3% | $280.78, -6.3% | PASS |  |  |
| RY.TO | L-note | "Last close $X · date" note = last completed bar | Last close $263.05 · Nov 20 | $263.05 · Nov 20 | PASS |  |  |
| RY.TO | L-now | ladder price row = compared price; name = the basis label | $263.05 "After hours" | $263.05 "after hours" | PASS |  |  |
| RY.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $263.91, -0.3% | $263.91, -0.3% | PASS |  |  |
| RY.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $281.11, -6.4% | $281.11, -6.4% | PASS |  |  |
| RY.TO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $263.05 / entry $263.05 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| RY.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| RY.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.6 | 28.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| RY.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +29.8% vs +7.0% | 29.8% vs 7.0% | PASS |  |  |
| RY.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| RY.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 19.0 | 19.0 | PASS |  | Wilder, completed bars |
| RY.TO | T4w | words "20 or more / below 20" | below 20 | ADX 19.0 | PASS |  |  |
| RY.TO | T5 | "counted at the last close ($X, date)" = last completed bar | $263.05, Nov 20 | $263.05, Nov 20 | PASS |  |  |
| RY.TO | T6 | price vs 200-day average (S1 pattern sma values) | $263.05 vs $263.91 · -0.3% | $263.05 vs $263.91 · -0.3% | PASS |  |  |
| RY.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| RY.TO | T7 | price vs 50-day average (S1 pattern sma values) | $263.05 vs $281.11 · -6.4% | $263.05 vs $281.11 · -6.4% | PASS |  |  |
| RY.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| RY.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.2% over 30 td | +3.2% over 30 td | PASS |  |  |
| RY.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| RY.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| RY.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 13.1% below $302.65 | 13.1% below $302.65 | PASS |  | closing high would be 302.02 |
| RY.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 13.1% below | PASS |  |  |
| RY.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $302.65 | $302.6498839841861 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| RY.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -2.38%, close location 0.00, OBV falling |
| RY.TO | V2 | day change of the last completed bar | down 2.4% | -2.38% | PASS |  |  |
| RY.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| RY.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| RY.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.29× / 1.21× | 1.29× / 1.20× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| RY.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 4377003) | 20 bars, last ('2026-11-20', 4377003) | PASS |  |  |
| SETM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $19.53 | $19.53 | PASS |  |  |
| SETM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $23.78 | $23.78 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SETM | E3 | percent from the 21-day average | 17.9% below | 17.9% below | PASS |  |  |
| SETM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SETM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.01 | $1.01 (sr=1.0059) | PASS |  | Wilder ATR14 |
| SETM | E5 | distance in normal day-moves | 4.2 | 4.2 | PASS |  | gauge dot note uses the same number:  · 4.2 day-moves below |
| SETM | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| SETM | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +8.4 | +8.4 | PASS |  |  |
| SETM | L-ema21 | ladder row ema21: price and gap = price vs average | $23.78, -17.9% | $23.78, -17.9% | PASS |  |  |
| SETM | L-note | "Last close $X · date" note = last completed bar | Last close $19.53 · Nov 20 | $19.53 · Nov 20 | PASS |  |  |
| SETM | L-now | ladder price row = compared price; name = the basis label | $19.53 "After hours" | $19.53 "after hours" | PASS |  |  |
| SETM | L-sma200 | ladder row sma200: price and gap = price vs average | $32.19, -39.3% | $32.19, -39.3% | PASS |  |  |
| SETM | L-sma50 | ladder row sma50: price and gap = price vs average | $26.87, -27.3% | $26.87, -27.3% | PASS |  |  |
| SETM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $19.53 / entry $19.53 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SETM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SETM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 23.9 | 23.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SETM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -21.9% vs +7.0% | -21.9% vs 7.0% | PASS |  |  |
| SETM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SETM | T4 | ADX 14 (S1 /api/sr meta.adx) | 38.0 | 38.0 | PASS |  | Wilder, completed bars |
| SETM | T4w | words "20 or more / below 20" | 20 or more | ADX 38.0 | PASS |  |  |
| SETM | T5 | "counted at the last close ($X, date)" = last completed bar | $19.53, Nov 20 | $19.53, Nov 20 | PASS |  |  |
| SETM | T6 | price vs 200-day average (S1 pattern sma values) | $19.53 vs $32.19 · -39.3% | $19.53 vs $32.19 · -39.3% | PASS |  |  |
| SETM | T6w | word "Below" | Below | Below | PASS |  |  |
| SETM | T7 | price vs 50-day average (S1 pattern sma values) | $19.53 vs $26.87 · -27.3% | $19.53 vs $26.87 · -27.3% | PASS |  |  |
| SETM | T7w | word "Below" | Below | Below | PASS |  |  |
| SETM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -4.1% over 30 td | -4.1% over 30 td | PASS |  |  |
| SETM | T8r | word "rising" | not rising | not rising | PASS |  |  |
| SETM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SETM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 51.8% below $40.55 | 51.8% below $40.55 | PASS |  | closing high would be 39.73 |
| SETM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 51.8% below | PASS |  |  |
| SETM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $40.55 | $40.54999923706055 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SETM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.38%, close location 0.06, OBV falling |
| SETM | V2 | day change of the last completed bar | down 5.4% | -5.38% | PASS |  |  |
| SETM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0560) | PASS |  |  |
| SETM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SETM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.58× / 1.04× | 1.58× / 1.04× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SETM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 286282) | 20 bars, last ('2026-11-20', 286282) | PASS |  |  |
| SETM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.58, OBV falling | condition true | PASS |  |  |
| SGRD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $16.81 | $16.81 | PASS |  |  |
| SGRD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $18.34 | $18.34 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SGRD.TO | E3 | percent from the 21-day average | 8.3% below | 8.3% below | PASS |  |  |
| SGRD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SGRD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.41 | $0.41 (sr=0.4131) | PASS |  | Wilder ATR14 |
| SGRD.TO | E5 | distance in normal day-moves | 3.7 | 3.7 | PASS |  | gauge dot note uses the same number:  · 3.7 day-moves below |
| SGRD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $18.34, -8.3% | $18.34, -8.3% | PASS |  |  |
| SGRD.TO | L-now | ladder price row = compared price; name = the basis label | $16.81 "Last close" | $16.81 "last close" | PASS |  |  |
| SGRD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $19.37, -13.2% | $19.37, -13.2% | PASS |  |  |
| SGRD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.2 | 31.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SGRD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 29.2 | 29.2 | PASS |  | Wilder, completed bars |
| SGRD.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 29.2 | PASS |  |  |
| SGRD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -4.97%, close location 0.00, OBV falling |
| SGRD.TO | V2 | day change of the last completed bar | down 5.0% | -4.97% | PASS |  |  |
| SGRD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.00 (raw 0.0000) | PASS |  |  |
| SGRD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SGRD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.34× / 2.02× | 0.34× / 2.02× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SGRD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3020) | 20 bars, last ('2026-11-20', 3020) | PASS |  |  |
| SMH | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $400.06 | $400.06 | PASS |  |  |
| SMH | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $489.58 | $489.58 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SMH | E3 | percent from the 21-day average | 18.3% below | 18.3% below | PASS |  |  |
| SMH | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SMH | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $26.13 | $26.13 (sr=26.1267) | PASS |  | Wilder ATR14 |
| SMH | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| SMH | L-ema21 | ladder row ema21: price and gap = price vs average | $489.58, -18.3% | $489.58, -18.3% | PASS |  |  |
| SMH | L-note | "Last close $X · date" note = last completed bar | Last close $399.51 · Nov 20 | $399.51 · Nov 20 | PASS |  |  |
| SMH | L-now | ladder price row = compared price; name = the basis label | $400.06 "After hours" | $400.06 "after hours" | PASS |  |  |
| SMH | L-sma200 | ladder row sma200: price and gap = price vs average | $525.17, -23.8% | $525.17, -23.8% | PASS |  |  |
| SMH | L-sma50 | ladder row sma50: price and gap = price vs average | $547.5, -26.9% | $547.50, -26.9% | PASS |  |  |
| SMH | S5-price | S5: the same live price reads the same on the header and the Entry block | header $400.06 / entry $400.06 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SMH | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SMH | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 26.1 | 26.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SMH | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +23.3% vs +7.0% | 23.3% vs 7.0% | PASS |  |  |
| SMH | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SMH | T4 | ADX 14 (S1 /api/sr meta.adx) | 36.3 | 36.3 | PASS |  | Wilder, completed bars |
| SMH | T4w | words "20 or more / below 20" | 20 or more | ADX 36.3 | PASS |  |  |
| SMH | T5 | "counted at the last close ($X, date)" = last completed bar | $399.51, Nov 20 | $399.51, Nov 20 | PASS |  |  |
| SMH | T6 | price vs 200-day average (S1 pattern sma values) | $399.51 vs $525.17 · -23.9% | $399.51 vs $525.17 · -23.9% | PASS |  |  |
| SMH | T6w | word "Below" | Below | Below | PASS |  |  |
| SMH | T7 | price vs 50-day average (S1 pattern sma values) | $399.51 vs $547.50 · -27.0% | $399.51 vs $547.50 · -27.0% | PASS |  |  |
| SMH | T7w | word "Below" | Below | Below | PASS |  |  |
| SMH | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.7% over 30 td | +3.7% over 30 td | PASS |  |  |
| SMH | T8r | word "rising" | still rising | rising | PASS |  |  |
| SMH | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SMH | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 40.5% below $671.83 | 40.5% below $671.83 | PASS |  | closing high would be 668.91 |
| SMH | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 40.5% below | PASS |  |  |
| SMH | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $671.83 | $671.83002 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SMH | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.72%, close location 0.06, OBV falling |
| SMH | V2 | day change of the last completed bar | down 10.7% | -10.72% | PASS |  |  |
| SMH | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0640) | PASS |  |  |
| SMH | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SMH | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 6.17× / 1.64× | 6.17× / 1.64× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SMH | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 65215874) | 20 bars, last ('2026-11-20', 65215874) | PASS |  |  |
| SMH | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 6.17, OBV falling | condition true | PASS |  |  |
| SNDK.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $15.27 | $15.27 | PASS |  |  |
| SNDK.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $23.61 | $23.61 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SNDK.TO | E3 | percent from the 21-day average | 35.3% below | 35.3% below | PASS |  |  |
| SNDK.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| SNDK.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.44 | $2.44 (sr=2.441) | PASS |  | Wilder ATR14 |
| SNDK.TO | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| SNDK.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.7 | +3.7 | PASS |  |  |
| SNDK.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $23.61, -35.3% | $23.61, -35.3% | PASS |  |  |
| SNDK.TO | L-now | ladder price row = compared price; name = the basis label | $15.27 "Last close" | $15.27 "last close" | PASS |  |  |
| SNDK.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $32.7, -53.3% | $32.70, -53.3% | PASS |  |  |
| SNDK.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 25.1 | 25.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SNDK.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 41.3 | 41.3 | PASS |  | Wilder, completed bars |
| SNDK.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 41.3 | PASS |  |  |
| SNDK.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -16.78%, close location 0.05, OBV falling |
| SNDK.TO | V2 | day change of the last completed bar | down 16.8% | -16.78% | PASS |  |  |
| SNDK.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0464) | PASS |  |  |
| SNDK.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SNDK.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.35× / 1.05× | 2.35× / 1.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SNDK.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3119828) | 20 bars, last ('2026-11-20', 3119828) | PASS |  |  |
| SNDK.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.35, OBV falling | condition true | PASS |  |  |
| SO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $93.13 | $93.13 | PASS |  |  |
| SO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $92.29 | $92.29 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SO | E3 | percent from the 21-day average | 0.9% above | 0.9% above | PASS |  |  |
| SO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.77 | $1.77 (sr=1.7679) | PASS |  | Wilder ATR14 |
| SO | E5 | distance in normal day-moves | 0.5 | 0.5 | PASS |  | gauge dot note uses the same number:  · 0.5 day-moves above |
| SO | L-ema21 | ladder row ema21: price and gap = price vs average | $92.29, 0.9% | $92.29, 0.9% | PASS |  |  |
| SO | L-note | "Last close $X · date" note = last completed bar | Last close $93.13 · Nov 20 | $93.13 · Nov 20 | PASS |  |  |
| SO | L-now | ladder price row = compared price; name = the basis label | $93.13 "After hours" | $93.13 "after hours" | PASS |  |  |
| SO | L-sma200 | ladder row sma200: price and gap = price vs average | $91.26, 2.1% | $91.26, 2.1% | PASS |  |  |
| SO | L-sma50 | ladder row sma50: price and gap = price vs average | $88.61, 5.1% | $88.61, 5.1% | PASS |  |  |
| SO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $93.13 / entry $93.13 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 5 / 8 | 5 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 56.0 | 56.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +8.6% vs +7.0% | 8.6% vs 7.0% | PASS |  |  |
| SO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.1 | 26.1 | PASS |  | Wilder, completed bars |
| SO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.1 | PASS |  |  |
| SO | T5 | "counted at the last close ($X, date)" = last completed bar | $93.13, Nov 20 | $93.13, Nov 20 | PASS |  |  |
| SO | T6 | price vs 200-day average (S1 pattern sma values) | $93.13 vs $91.26 · +2.0% | $93.13 vs $91.26 · 2.1% | PASS |  |  |
| SO | T6w | word "Above" | Above | Above | PASS |  |  |
| SO | T7 | price vs 50-day average (S1 pattern sma values) | $93.13 vs $88.61 · +5.1% | $93.13 vs $88.61 · 5.1% | PASS |  |  |
| SO | T7w | word "Above" | Above | Above | PASS |  |  |
| SO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.1% over 30 td | +1.1% over 30 td | PASS |  |  |
| SO | T8r | word "rising" | still rising | rising | PASS |  |  |
| SO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 4.6% below $97.65 | 4.6% below $97.65 | PASS |  | closing high would be 96.70 |
| SO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 4.6% below | PASS |  |  |
| SO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $97.65 | $97.64764917949712 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -0.17%, close location 0.08, OBV rising |
| SO | V2 | day change of the last completed bar | down 0.2% | -0.17% | PASS |  |  |
| SO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0811) | PASS |  |  |
| SO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| SO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.94× / 0.09× | 0.94× / 0.09× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 6873193) | 20 bars, last ('2026-11-20', 6873193) | PASS |  |  |
| SOXL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $30.88 | $30.88 | PASS |  |  |
| SOXL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $65.26 | $65.26 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL | E3 | percent from the 21-day average | 52.7% below | 52.7% below | PASS |  |  |
| SOXL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $11.99 | $11.99 (sr=11.9904) | PASS |  | Wilder ATR14 |
| SOXL | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| SOXL | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| SOXL | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.9 | +4.9 | PASS |  |  |
| SOXL | L-ema21 | ladder row ema21: price and gap = price vs average | $65.26, -52.7% | $65.26, -52.7% | PASS |  |  |
| SOXL | L-note | "Last close $X · date" note = last completed bar | Last close $30.88 · Nov 20 | $30.88 · Nov 20 | PASS |  |  |
| SOXL | L-now | ladder price row = compared price; name = the basis label | $30.88 "After hours" | $30.88 "after hours" | PASS |  |  |
| SOXL | L-sma200 | ladder row sma200: price and gap = price vs average | $123.65, -75.0% | $123.65, -75.0% | PASS |  |  |
| SOXL | L-sma50 | ladder row sma50: price and gap = price vs average | $102.78, -70.0% | $102.78, -70.0% | PASS |  |  |
| SOXL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $30.88 / entry $30.88 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.5 | 28.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.3% vs +7.0% | 0.3% vs 7.0% | PASS |  |  |
| SOXL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL | T4 | ADX 14 (S1 /api/sr meta.adx) | 35.2 | 35.2 | PASS |  | Wilder, completed bars |
| SOXL | T4w | words "20 or more / below 20" | 20 or more | ADX 35.2 | PASS |  |  |
| SOXL | T5 | "counted at the last close ($X, date)" = last completed bar | $30.88, Nov 20 | $30.88, Nov 20 | PASS |  |  |
| SOXL | T6 | price vs 200-day average (S1 pattern sma values) | $30.88 vs $123.65 · -75.0% | $30.88 vs $123.65 · -75.0% | PASS |  |  |
| SOXL | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T7 | price vs 50-day average (S1 pattern sma values) | $30.88 vs $102.78 · -70.0% | $30.88 vs $102.78 · -70.0% | PASS |  |  |
| SOXL | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.8% over 30 td | +2.8% over 30 td | PASS |  |  |
| SOXL | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 89.8% below $301.80 | 89.8% below $301.80 | PASS |  | closing high would be 300.57 |
| SOXL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 89.8% below | PASS |  |  |
| SOXL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $301.80 | $301.8021115035658 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -31.83%, close location 0.08, OBV falling |
| SOXL | V2 | day change of the last completed bar | down 31.8% | -31.83% | PASS |  |  |
| SOXL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.08 (raw 0.0831) | PASS |  |  |
| SOXL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.86× / 0.82× | 3.86× / 0.82× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 533762471) | 20 bars, last ('2026-11-20', 533762471) | PASS |  |  |
| SOXL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.86, OBV falling | condition true | PASS |  |  |
| SOXL.NE | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $7.85 | $7.85 | PASS |  |  |
| SOXL.NE | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $16.38 | $16.38 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXL.NE | E3 | percent from the 21-day average | 52.1% below | 52.1% below | PASS |  |  |
| SOXL.NE | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXL.NE | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.87 | $1.87 (sr=1.8723) | PASS |  | Wilder ATR14 |
| SOXL.NE | E5 | distance in normal day-moves | 4.6 | 4.6 | PASS |  | gauge dot note uses the same number:  · 4.6 day-moves below |
| SOXL.NE | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +4.9 | +4.9 | PASS |  |  |
| SOXL.NE | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.7 | +7.7 | PASS |  |  |
| SOXL.NE | L-ema21 | ladder row ema21: price and gap = price vs average | $16.38, -52.1% | $16.38, -52.1% | PASS |  |  |
| SOXL.NE | L-note | "Last close $X · date" note = last completed bar | Last close $7.85 · Nov 20 | $7.85 · Nov 20 | PASS |  |  |
| SOXL.NE | L-now | ladder price row = compared price; name = the basis label | $7.85 "After hours" | $7.85 "after hours" | PASS |  |  |
| SOXL.NE | L-sma200 | ladder row sma200: price and gap = price vs average | $30.8, -74.5% | $30.80, -74.5% | PASS |  |  |
| SOXL.NE | L-sma50 | ladder row sma50: price and gap = price vs average | $25.56, -69.3% | $25.56, -69.3% | PASS |  |  |
| SOXL.NE | S5-price | S5: the same live price reads the same on the header and the Entry block | header $7.85 / entry $7.85 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXL.NE | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXL.NE | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.8 | 28.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXL.NE | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -15.2% vs +7.0% | -15.2% vs 7.0% | PASS |  |  |
| SOXL.NE | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXL.NE | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.7 | 28.7 | PASS |  | Wilder, completed bars |
| SOXL.NE | T4w | words "20 or more / below 20" | 20 or more | ADX 28.7 | PASS |  |  |
| SOXL.NE | T5 | "counted at the last close ($X, date)" = last completed bar | $7.85, Nov 20 | $7.85, Nov 20 | PASS |  |  |
| SOXL.NE | T6 | price vs 200-day average (S1 pattern sma values) | $7.85 vs $30.80 · -74.5% | $7.85 vs $30.80 · -74.5% | PASS |  |  |
| SOXL.NE | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T7 | price vs 50-day average (S1 pattern sma values) | $7.85 vs $25.56 · -69.3% | $7.85 vs $25.56 · -69.3% | PASS |  |  |
| SOXL.NE | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXL.NE | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +2.7% over 30 td | +2.7% over 30 td | PASS |  |  |
| SOXL.NE | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXL.NE | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXL.NE | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 89.4% below $74.21 | 89.4% below $74.21 | PASS |  | closing high would be 74.21 |
| SOXL.NE | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 89.4% below | PASS |  |  |
| SOXL.NE | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $74.21 | $74.21369934082031 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXL.NE | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 49 of 50 days empty | 49 of 50 days empty | PASS |  |  |
| SOXX | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $123.40 | $123.40 | PASS |  |  |
| SOXX | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $149.42 | $149.42 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SOXX | E3 | percent from the 21-day average | 17.4% below | 17.4% below | PASS |  |  |
| SOXX | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SOXX | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.90 | $8.90 (sr=8.9009) | PASS |  | Wilder ATR14 |
| SOXX | E5 | distance in normal day-moves | 2.9 | 2.9 | PASS |  | gauge dot note uses the same number:  · 2.9 day-moves below |
| SOXX | L-ema21 | ladder row ema21: price and gap = price vs average | $149.42, -17.4% | $149.42, -17.4% | PASS |  |  |
| SOXX | L-note | "Last close $X · date" note = last completed bar | Last close $123.40 · Nov 20 | $123.40 · Nov 20 | PASS |  |  |
| SOXX | L-now | ladder price row = compared price; name = the basis label | $123.4 "After hours" | $123.40 "after hours" | PASS |  |  |
| SOXX | L-sma200 | ladder row sma200: price and gap = price vs average | $160.86, -23.3% | $160.86, -23.3% | PASS |  |  |
| SOXX | L-sma50 | ladder row sma50: price and gap = price vs average | $168.11, -26.6% | $168.11, -26.6% | PASS |  |  |
| SOXX | S5-price | S5: the same live price reads the same on the header and the Entry block | header $123.40 / entry $123.40 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SOXX | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| SOXX | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 29.1 | 29.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SOXX | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +38.5% vs +7.0% | 38.5% vs 7.0% | PASS |  |  |
| SOXX | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| SOXX | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.2 | 32.2 | PASS |  | Wilder, completed bars |
| SOXX | T4w | words "20 or more / below 20" | 20 or more | ADX 32.2 | PASS |  |  |
| SOXX | T5 | "counted at the last close ($X, date)" = last completed bar | $123.40, Nov 20 | $123.40, Nov 20 | PASS |  |  |
| SOXX | T6 | price vs 200-day average (S1 pattern sma values) | $123.40 vs $160.86 · -23.3% | $123.40 vs $160.86 · -23.3% | PASS |  |  |
| SOXX | T6w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T7 | price vs 50-day average (S1 pattern sma values) | $123.40 vs $168.11 · -26.6% | $123.40 vs $168.11 · -26.6% | PASS |  |  |
| SOXX | T7w | word "Below" | Below | Below | PASS |  |  |
| SOXX | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.5% over 30 td | +4.5% over 30 td | PASS |  |  |
| SOXX | T8r | word "rising" | still rising | rising | PASS |  |  |
| SOXX | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| SOXX | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 43.5% below $218.51 | 43.5% below $218.51 | PASS |  | closing high would be 218.19 |
| SOXX | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 43.5% below | PASS |  |  |
| SOXX | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $218.51 | $218.50713476135667 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| SOXX | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.55%, close location 0.09, OBV falling |
| SOXX | V2 | day change of the last completed bar | down 10.6% | -10.55% | PASS |  |  |
| SOXX | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0916) | PASS |  |  |
| SOXX | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SOXX | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.69× / 1.46× | 2.69× / 1.46× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SOXX | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 85807658) | 20 bars, last ('2026-11-20', 85807658) | PASS |  |  |
| SOXX | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.69, OBV falling | condition true | PASS |  |  |
| SPCL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $7.25 | $7.25 | PASS |  |  |
| SPCL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $11.99 | $11.99 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| SPCL | E3 | percent from the 21-day average | 39.5% below | 39.5% below | PASS |  |  |
| SPCL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| SPCL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.68 | $1.68 (sr=1.6789) | PASS |  | Wilder ATR14 |
| SPCL | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| SPCL | L-ema21 | ladder row ema21: price and gap = price vs average | $11.99, -39.5% | $11.99, -39.5% | PASS |  |  |
| SPCL | L-note | "Last close $X · date" note = last completed bar | Last close $7.25 · Nov 20 | $7.25 · Nov 20 | PASS |  |  |
| SPCL | L-now | ladder price row = compared price; name = the basis label | $7.25 "After hours" | $7.25 "after hours" | PASS |  |  |
| SPCL | L-sma50 | ladder row sma50: price and gap = price vs average | $16.62, -56.4% | $16.62, -56.4% | PASS |  |  |
| SPCL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $7.25 / entry $7.25 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| SPCL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.4 | 30.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| SPCL | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.7 | 33.7 | PASS |  | Wilder, completed bars |
| SPCL | T4w | words "20 or more / below 20" | 20 or more | ADX 33.7 | PASS |  |  |
| SPCL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -18.63%, close location 0.06, OBV falling |
| SPCL | V2 | day change of the last completed bar | down 18.6% | -18.63% | PASS |  |  |
| SPCL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0592) | PASS |  |  |
| SPCL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| SPCL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.98× / 0.80× | 1.98× / 0.80× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| SPCL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 75602) | 20 bars, last ('2026-11-20', 75602) | PASS |  |  |
| SPCL | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.98, OBV falling | condition true | PASS |  |  |
| TSLA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $345.82 | $345.82 | PASS |  |  |
| TSLA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $378.44 | $378.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLA | E3 | percent from the 21-day average | 8.6% below | 8.6% below | PASS |  |  |
| TSLA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSLA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $17.14 | $17.14 (sr=17.1403) | PASS |  | Wilder ATR14 |
| TSLA | E5 | distance in normal day-moves | 1.9 | 1.9 | PASS |  | gauge dot note uses the same number:  · 1.9 day-moves below |
| TSLA | L-ema21 | ladder row ema21: price and gap = price vs average | $378.44, -8.6% | $378.44, -8.6% | PASS |  |  |
| TSLA | L-note | "Last close $X · date" note = last completed bar | Last close $345.82 · Nov 20 | $345.82 · Nov 20 | PASS |  |  |
| TSLA | L-now | ladder price row = compared price; name = the basis label | $345.82 "After hours" | $345.82 "after hours" | PASS |  |  |
| TSLA | L-sma200 | ladder row sma200: price and gap = price vs average | $381.66, -9.4% | $381.66, -9.4% | PASS |  |  |
| TSLA | L-sma50 | ladder row sma50: price and gap = price vs average | $375.64, -7.9% | $375.64, -7.9% | PASS |  |  |
| TSLA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $345.82 / entry $345.82 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.8 | 37.8 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -12.5% vs +7.0% | -12.5% vs 7.0% | PASS |  |  |
| TSLA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLA | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.7 | 11.7 | PASS |  | Wilder, completed bars |
| TSLA | T4w | words "20 or more / below 20" | below 20 | ADX 11.7 | PASS |  |  |
| TSLA | T5 | "counted at the last close ($X, date)" = last completed bar | $345.82, Nov 20 | $345.82, Nov 20 | PASS |  |  |
| TSLA | T6 | price vs 200-day average (S1 pattern sma values) | $345.82 vs $381.66 · -9.4% | $345.82 vs $381.66 · -9.4% | PASS |  |  |
| TSLA | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLA | T7 | price vs 50-day average (S1 pattern sma values) | $345.82 vs $375.64 · -7.9% | $345.82 vs $375.64 · -7.9% | PASS |  |  |
| TSLA | T7w | word "Below" | Below | Below | PASS |  |  |
| TSLA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -2.3% over 30 td | -2.3% over 30 td | PASS |  |  |
| TSLA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 30.7% below $498.83 | 30.7% below $498.83 | PASS |  | closing high would be 489.88 |
| TSLA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 30.7% below | PASS |  |  |
| TSLA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $498.83 | $498.83 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -7.64%, close location 0.05, OBV falling |
| TSLA | V2 | day change of the last completed bar | down 7.6% | -7.64% | PASS |  |  |
| TSLA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0504) | PASS |  |  |
| TSLA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSLA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.27× / 1.54× | 1.27× / 1.54× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 46048760) | 20 bars, last ('2026-11-20', 46048760) | PASS |  |  |
| TSLL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $8.07 | $8.07 | PASS |  |  |
| TSLL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $9.88 | $9.88 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSLL | E3 | percent from the 21-day average | 18.3% below | 18.3% below | PASS |  |  |
| TSLL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSLL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.90 | $0.90 (sr=0.8984) | PASS |  | Wilder ATR14 |
| TSLL | E5 | distance in normal day-moves | 2.0 | 2.0 | PASS |  | gauge dot note uses the same number:  · 2.0 day-moves below |
| TSLL | L-ema21 | ladder row ema21: price and gap = price vs average | $9.88, -18.3% | $9.88, -18.3% | PASS |  |  |
| TSLL | L-note | "Last close $X · date" note = last completed bar | Last close $8.07 · Nov 20 | $8.07 · Nov 20 | PASS |  |  |
| TSLL | L-now | ladder price row = compared price; name = the basis label | $8.07 "After hours" | $8.07 "after hours" | PASS |  |  |
| TSLL | L-sma200 | ladder row sma200: price and gap = price vs average | $11.64, -30.7% | $11.64, -30.7% | PASS |  |  |
| TSLL | L-sma50 | ladder row sma50: price and gap = price vs average | $9.94, -18.8% | $9.94, -18.8% | PASS |  |  |
| TSLL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $8.07 / entry $8.07 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSLL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSLL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 36.7 | 36.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSLL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -45.8% vs +7.0% | -45.8% vs 7.0% | PASS |  |  |
| TSLL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSLL | T4 | ADX 14 (S1 /api/sr meta.adx) | 11.7 | 11.7 | PASS |  | Wilder, completed bars |
| TSLL | T4w | words "20 or more / below 20" | below 20 | ADX 11.7 | PASS |  |  |
| TSLL | T5 | "counted at the last close ($X, date)" = last completed bar | $8.07, Nov 20 | $8.07, Nov 20 | PASS |  |  |
| TSLL | T6 | price vs 200-day average (S1 pattern sma values) | $8.07 vs $11.64 · -30.7% | $8.07 vs $11.64 · -30.7% | PASS |  |  |
| TSLL | T6w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T7 | price vs 50-day average (S1 pattern sma values) | $8.07 vs $9.94 · -18.8% | $8.07 vs $9.94 · -18.8% | PASS |  |  |
| TSLL | T7w | word "Below" | Below | Below | PASS |  |  |
| TSLL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -9.0% over 30 td | -9.0% over 30 td | PASS |  |  |
| TSLL | T8r | word "rising" | not rising | not rising | PASS |  |  |
| TSLL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSLL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 65.1% below $23.10 | 65.1% below $23.10 | PASS |  | closing high would be 22.41 |
| TSLL | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 65.1% below | PASS |  |  |
| TSLL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $23.10 | $23.09813194913166 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSLL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -15.32%, close location 0.05, OBV falling |
| TSLL | V2 | day change of the last completed bar | down 15.3% | -15.32% | PASS |  |  |
| TSLL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0470) | PASS |  |  |
| TSLL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSLL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 0.85× / 1.38× | 0.85× / 1.38× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSLL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 45847321) | 20 bars, last ('2026-11-20', 45847321) | PASS |  |  |
| TSM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $318.71 | $318.71 | PASS |  |  |
| TSM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $387.0 | $387.00 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| TSM | E3 | percent from the 21-day average | 17.6% below | 17.6% below | PASS |  |  |
| TSM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| TSM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $19.06 | $19.06 (sr=19.0571) | PASS |  | Wilder ATR14 |
| TSM | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  · 3.6 day-moves below |
| TSM | L-ema21 | ladder row ema21: price and gap = price vs average | $387, -17.6% | $387.00, -17.6% | PASS |  |  |
| TSM | L-note | "Last close $X · date" note = last completed bar | Last close $318.71 · Nov 20 | $318.71 · Nov 20 | PASS |  |  |
| TSM | L-now | ladder price row = compared price; name = the basis label | $318.71 "After hours" | $318.71 "after hours" | PASS |  |  |
| TSM | L-sma200 | ladder row sma200: price and gap = price vs average | $403.55, -21.0% | $403.55, -21.0% | PASS |  |  |
| TSM | L-sma50 | ladder row sma50: price and gap = price vs average | $422.13, -24.5% | $422.13, -24.5% | PASS |  |  |
| TSM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $318.71 / entry $318.71 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| TSM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| TSM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.3 | 28.3 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| TSM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.8% vs +7.0% | 14.9% vs 7.0% | PASS |  |  |
| TSM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| TSM | T4 | ADX 14 (S1 /api/sr meta.adx) | 34.0 | 34.0 | PASS |  | Wilder, completed bars |
| TSM | T4w | words "20 or more / below 20" | 20 or more | ADX 34.0 | PASS |  |  |
| TSM | T5 | "counted at the last close ($X, date)" = last completed bar | $318.71, Nov 20 | $318.71, Nov 20 | PASS |  |  |
| TSM | T6 | price vs 200-day average (S1 pattern sma values) | $318.71 vs $403.55 · -21.0% | $318.71 vs $403.55 · -21.0% | PASS |  |  |
| TSM | T6w | word "Below" | Below | Below | PASS |  |  |
| TSM | T7 | price vs 50-day average (S1 pattern sma values) | $318.71 vs $422.13 · -24.5% | $318.71 vs $422.13 · -24.5% | PASS |  |  |
| TSM | T7w | word "Below" | Below | Below | PASS |  |  |
| TSM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.0% over 30 td | +3.0% over 30 td | PASS |  |  |
| TSM | T8r | word "rising" | still rising | rising | PASS |  |  |
| TSM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| TSM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 34.6% below $487.47 | 34.6% below $487.47 | PASS |  | closing high would be 485.80 |
| TSM | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 34.6% below | PASS |  |  |
| TSM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $487.47 | $487.47 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| TSM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -9.48%, close location 0.01, OBV falling |
| TSM | V2 | day change of the last completed bar | down 9.5% | -9.48% | PASS |  |  |
| TSM | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.01 (raw 0.0091) | PASS |  |  |
| TSM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| TSM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.76× / 1.59× | 2.76× / 1.59× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| TSM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 37176060) | 20 bars, last ('2026-11-20', 37176060) | PASS |  |  |
| TSM | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.76, OBV falling | condition true | PASS |  |  |
| UBOT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $12.74 | $12.74 | PASS |  |  |
| UBOT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $16.82 | $16.82 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UBOT | E3 | percent from the 21-day average | 24.3% below | 24.3% below | PASS |  |  |
| UBOT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| UBOT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.89 | $0.89 (sr=0.8858) | PASS |  | Wilder ATR14 |
| UBOT | E5 | distance in normal day-moves | 4.6 | 4.6 | PASS |  | gauge dot note uses the same number:  · 4.6 day-moves below |
| UBOT | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| UBOT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.9 | +7.9 | PASS |  |  |
| UBOT | L-ema21 | ladder row ema21: price and gap = price vs average | $16.82, -24.3% | $16.82, -24.3% | PASS |  |  |
| UBOT | L-note | "Last close $X · date" note = last completed bar | Last close $12.74 · Nov 20 | $12.74 · Nov 20 | PASS |  |  |
| UBOT | L-now | ladder price row = compared price; name = the basis label | $12.74 "After hours" | $12.74 "after hours" | PASS |  |  |
| UBOT | L-sma200 | ladder row sma200: price and gap = price vs average | $23.78, -46.4% | $23.78, -46.4% | PASS |  |  |
| UBOT | L-sma50 | ladder row sma50: price and gap = price vs average | $19.54, -34.8% | $19.54, -34.8% | PASS |  |  |
| UBOT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $12.74 / entry $12.74 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| UBOT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UBOT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 23.6 | 23.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UBOT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -40.6% vs +7.0% | -40.6% vs 7.0% | PASS |  |  |
| UBOT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UBOT | T4 | ADX 14 (S1 /api/sr meta.adx) | 41.9 | 41.9 | PASS |  | Wilder, completed bars |
| UBOT | T4w | words "20 or more / below 20" | 20 or more | ADX 41.9 | PASS |  |  |
| UBOT | T5 | "counted at the last close ($X, date)" = last completed bar | $12.74, Nov 20 | $12.74, Nov 20 | PASS |  |  |
| UBOT | T6 | price vs 200-day average (S1 pattern sma values) | $12.74 vs $23.79 · -46.4% | $12.74 vs $23.78 · -46.4% | PASS |  |  |
| UBOT | T6w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T7 | price vs 50-day average (S1 pattern sma values) | $12.74 vs $19.54 · -34.8% | $12.74 vs $19.54 · -34.8% | PASS |  |  |
| UBOT | T7w | word "Below" | Below | Below | PASS |  |  |
| UBOT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.4% over 30 td | -5.5% over 30 td | PASS |  |  |
| UBOT | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UBOT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UBOT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 60.3% below $32.08 | 60.3% below $32.08 | PASS |  | closing high would be 32.04 |
| UBOT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 60.3% below | PASS |  |  |
| UBOT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $32.08 | $32.08 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UBOT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -11.16%, close location 0.13, OBV falling |
| UBOT | V2 | day change of the last completed bar | down 11.2% | -11.16% | PASS |  |  |
| UBOT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.13 (raw 0.1308) | PASS |  |  |
| UBOT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UBOT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.70× / 1.61× | 2.70× / 1.60× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UBOT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 44820) | 20 bars, last ('2026-11-20', 44820) | PASS |  |  |
| UBOT | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.70, OBV falling | condition true | PASS |  |  |
| UFO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $35.87 | $35.87 | PASS |  |  |
| UFO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $39.78 | $39.78 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| UFO | E3 | percent from the 21-day average | 9.8% below | 9.8% below | PASS |  |  |
| UFO | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| UFO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.45 | $1.45 (sr=1.4468) | PASS |  | Wilder ATR14 |
| UFO | E5 | distance in normal day-moves | 2.7 | 2.7 | PASS |  | gauge dot note uses the same number:  · 2.7 day-moves below |
| UFO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.9 | +4.9 | PASS |  |  |
| UFO | L-ema21 | ladder row ema21: price and gap = price vs average | $39.78, -9.8% | $39.78, -9.8% | PASS |  |  |
| UFO | L-note | "Last close $X · date" note = last completed bar | Last close $35.87 · Nov 20 | $35.87 · Nov 20 | PASS |  |  |
| UFO | L-now | ladder price row = compared price; name = the basis label | $35.87 "After hours" | $35.87 "after hours" | PASS |  |  |
| UFO | L-sma200 | ladder row sma200: price and gap = price vs average | $46.91, -23.5% | $46.91, -23.5% | PASS |  |  |
| UFO | L-sma50 | ladder row sma50: price and gap = price vs average | $41.24, -13.0% | $41.24, -13.0% | PASS |  |  |
| UFO | S5-price | S5: the same live price reads the same on the header and the Entry block | header $35.87 / entry $35.87 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| UFO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| UFO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 32.0 | 32.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| UFO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +14.5% vs +7.0% | 14.5% vs 7.0% | PASS |  |  |
| UFO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| UFO | T4 | ADX 14 (S1 /api/sr meta.adx) | 27.0 | 27.1 | PASS |  | Wilder, completed bars |
| UFO | T4w | words "20 or more / below 20" | 20 or more | ADX 27.1 | PASS |  |  |
| UFO | T5 | "counted at the last close ($X, date)" = last completed bar | $35.87, Nov 20 | $35.87, Nov 20 | PASS |  |  |
| UFO | T6 | price vs 200-day average (S1 pattern sma values) | $35.87 vs $46.90 · -23.5% | $35.87 vs $46.91 · -23.5% | PASS |  |  |
| UFO | T6w | word "Below" | Below | Below | PASS |  |  |
| UFO | T7 | price vs 50-day average (S1 pattern sma values) | $35.87 vs $41.24 · -13.0% | $35.87 vs $41.24 · -13.0% | PASS |  |  |
| UFO | T7w | word "Below" | Below | Below | PASS |  |  |
| UFO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.2% over 30 td | -1.2% over 30 td | PASS |  |  |
| UFO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| UFO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| UFO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 47.3% below $68.12 | 47.3% below $68.12 | PASS |  | closing high would be 67.71 |
| UFO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 47.3% below | PASS |  |  |
| UFO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $68.12 | $68.11999548611959 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| UFO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.53%, close location 0.10, OBV falling |
| UFO | V2 | day change of the last completed bar | down 5.5% | -5.53% | PASS |  |  |
| UFO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.10 (raw 0.1040) | PASS |  |  |
| UFO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| UFO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.16× / 1.37× | 2.16× / 1.37× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| UFO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 562279) | 20 bars, last ('2026-11-20', 562279) | PASS |  |  |
| UFO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.16, OBV falling | condition true | PASS |  |  |
| URA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $26.79 | $26.79 | PASS |  |  |
| URA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $32.23 | $32.23 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| URA | E3 | percent from the 21-day average | 16.9% below | 16.9% below | PASS |  |  |
| URA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| URA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.44 | $1.44 (sr=1.437) | PASS |  | Wilder ATR14 |
| URA | E5 | distance in normal day-moves | 3.8 | 3.8 | PASS |  | gauge dot note uses the same number:  · 3.8 day-moves below |
| URA | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +9.1 | +9.1 | PASS |  |  |
| URA | L-ema21 | ladder row ema21: price and gap = price vs average | $32.23, -16.9% | $32.23, -16.9% | PASS |  |  |
| URA | L-note | "Last close $X · date" note = last completed bar | Last close $26.82 · Nov 20 | $26.82 · Nov 20 | PASS |  |  |
| URA | L-now | ladder price row = compared price; name = the basis label | $26.79 "After hours" | $26.79 "after hours" | PASS |  |  |
| URA | L-sma200 | ladder row sma200: price and gap = price vs average | $45.32, -40.9% | $45.32, -40.9% | PASS |  |  |
| URA | L-sma50 | ladder row sma50: price and gap = price vs average | $36.48, -26.6% | $36.48, -26.6% | PASS |  |  |
| URA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $26.79 / entry $26.79 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| URA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| URA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 24.9 | 24.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| URA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -33.4% vs +7.0% | -33.4% vs 7.0% | PASS |  |  |
| URA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| URA | T4 | ADX 14 (S1 /api/sr meta.adx) | 36.7 | 36.7 | PASS |  | Wilder, completed bars |
| URA | T4w | words "20 or more / below 20" | 20 or more | ADX 36.7 | PASS |  |  |
| URA | T5 | "counted at the last close ($X, date)" = last completed bar | $26.82, Nov 20 | $26.82, Nov 20 | PASS |  |  |
| URA | T6 | price vs 200-day average (S1 pattern sma values) | $26.82 vs $45.32 · -40.8% | $26.82 vs $45.32 · -40.8% | PASS |  |  |
| URA | T6w | word "Below" | Below | Below | PASS |  |  |
| URA | T7 | price vs 50-day average (S1 pattern sma values) | $26.82 vs $36.49 · -26.5% | $26.82 vs $36.48 · -26.5% | PASS |  |  |
| URA | T7w | word "Below" | Below | Below | PASS |  |  |
| URA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -5.6% over 30 td | -5.6% over 30 td | PASS |  |  |
| URA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| URA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| URA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 56.9% below $62.28 | 56.9% below $62.28 | PASS |  | closing high would be 61.81 |
| URA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 56.9% below | PASS |  |  |
| URA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $62.28 | $62.28 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| URA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -6.45%, close location 0.06, OBV falling |
| URA | V2 | day change of the last completed bar | down 6.5% | -6.45% | PASS |  |  |
| URA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0598) | PASS |  |  |
| URA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| URA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 4.91× / 1.20× | 4.91× / 1.20× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| URA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 22153699) | 20 bars, last ('2026-11-20', 22153699) | PASS |  |  |
| URA | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 4.91, OBV falling | condition true | PASS |  |  |
| URAA | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $9.08 | $9.08 | PASS |  |  |
| URAA | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $13.15 | $13.15 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| URAA | E3 | percent from the 21-day average | 31.0% below | 31.0% below | PASS |  |  |
| URAA | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| URAA | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.14 | $1.14 (sr=1.1389) | PASS |  | Wilder ATR14 |
| URAA | E5 | distance in normal day-moves | 3.6 | 3.6 | PASS |  | gauge dot note uses the same number:  · 3.6 day-moves below |
| URAA | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.1 | +3.1 | PASS |  |  |
| URAA | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +13.9 | +13.8 | PASS |  |  |
| URAA | L-ema21 | ladder row ema21: price and gap = price vs average | $13.15, -31.0% | $13.15, -31.0% | PASS |  |  |
| URAA | L-note | "Last close $X · date" note = last completed bar | Last close $9.08 · Nov 20 | $9.08 · Nov 20 | PASS |  |  |
| URAA | L-now | ladder price row = compared price; name = the basis label | $9.08 "After hours" | $9.08 "after hours" | PASS |  |  |
| URAA | L-sma200 | ladder row sma200: price and gap = price vs average | $28.93, -68.6% | $28.93, -68.6% | PASS |  |  |
| URAA | L-sma50 | ladder row sma50: price and gap = price vs average | $16.68, -45.6% | $16.68, -45.6% | PASS |  |  |
| URAA | S5-price | S5: the same live price reads the same on the header and the Entry block | header $9.08 / entry $9.08 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| URAA | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 0 / 8 | 0 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| URAA | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 26.4 | 26.4 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| URAA | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -67.9% vs +7.0% | -67.9% vs 7.0% | PASS |  |  |
| URAA | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| URAA | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.9 | 34.0 | PASS |  | Wilder, completed bars |
| URAA | T4w | words "20 or more / below 20" | 20 or more | ADX 34.0 | PASS |  |  |
| URAA | T5 | "counted at the last close ($X, date)" = last completed bar | $9.08, Nov 20 | $9.08, Nov 20 | PASS |  |  |
| URAA | T6 | price vs 200-day average (S1 pattern sma values) | $9.08 vs $28.93 · -68.6% | $9.08 vs $28.93 · -68.6% | PASS |  |  |
| URAA | T6w | word "Below" | Below | Below | PASS |  |  |
| URAA | T7 | price vs 50-day average (S1 pattern sma values) | $9.08 vs $16.68 · -45.6% | $9.08 vs $16.68 · -45.6% | PASS |  |  |
| URAA | T7w | word "Below" | Below | Below | PASS |  |  |
| URAA | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -13.2% over 30 td | -13.2% over 30 td | PASS |  |  |
| URAA | T8r | word "rising" | not rising | not rising | PASS |  |  |
| URAA | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| URAA | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 85.4% below $62.21 | 85.4% below $62.21 | PASS |  | closing high would be 61.16 |
| URAA | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 85.4% below | PASS |  |  |
| URAA | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $62.21 | $62.21386524011286 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| URAA | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -12.44%, close location 0.07, OBV falling |
| URAA | V2 | day change of the last completed bar | down 12.4% | -12.44% | PASS |  |  |
| URAA | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.07 (raw 0.0702) | PASS |  |  |
| URAA | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| URAA | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.17× / 0.99× | 3.17× / 0.99× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| URAA | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 246364) | 20 bars, last ('2026-11-20', 246364) | PASS |  |  |
| URAA | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.17, OBV falling | condition true | PASS |  |  |
| V | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $401.87 | $401.87 | PASS |  |  |
| V | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $412.43 | $412.43 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| V | E3 | percent from the 21-day average | 2.6% below | 2.6% below | PASS |  |  |
| V | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| V | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $8.93 | $8.93 (sr=8.9308) | PASS |  | Wilder ATR14 |
| V | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves below |
| V | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | -7.2 | -7.2 | PASS |  |  |
| V | L-ema21 | ladder row ema21: price and gap = price vs average | $412.43, -2.6% | $412.43, -2.6% | PASS |  |  |
| V | L-note | "Last close $X · date" note = last completed bar | Last close $401.87 · Nov 20 | $401.87 · Nov 20 | PASS |  |  |
| V | L-now | ladder price row = compared price; name = the basis label | $401.87 "After hours" | $401.87 "after hours" | PASS |  |  |
| V | L-sma200 | ladder row sma200: price and gap = price vs average | $347.95, 15.5% | $347.95, 15.5% | PASS |  |  |
| V | L-sma50 | ladder row sma50: price and gap = price vs average | $394.05, 2.0% | $394.05, 2.0% | PASS |  |  |
| V | S5-price | S5: the same live price reads the same on the header and the Entry block | header $401.87 / entry $401.87 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| V | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| V | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 43.9 | 43.9 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| V | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +25.1% vs +7.0% | 25.1% vs 7.0% | PASS |  |  |
| V | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| V | T4 | ADX 14 (S1 /api/sr meta.adx) | 31.9 | 31.8 | PASS |  | Wilder, completed bars |
| V | T4w | words "20 or more / below 20" | 20 or more | ADX 31.8 | PASS |  |  |
| V | T5 | "counted at the last close ($X, date)" = last completed bar | $401.87, Nov 20 | $401.87, Nov 20 | PASS |  |  |
| V | T6 | price vs 200-day average (S1 pattern sma values) | $401.87 vs $347.95 · +15.5% | $401.87 vs $347.95 · 15.5% | PASS |  |  |
| V | T6w | word "Above" | Above | Above | PASS |  |  |
| V | T7 | price vs 50-day average (S1 pattern sma values) | $401.87 vs $394.05 · +2.0% | $401.87 vs $394.05 · 2.0% | PASS |  |  |
| V | T7w | word "Above" | Above | Above | PASS |  |  |
| V | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.4% over 30 td | +3.4% over 30 td | PASS |  |  |
| V | T8r | word "rising" | still rising | rising | PASS |  |  |
| V | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| V | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 9.0% below $441.41 | 9.0% below $441.41 | PASS |  | closing high would be 435.76 |
| V | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 9.0% below | PASS |  |  |
| V | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $441.41 | $441.4129311637065 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| V | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 2 down, 1 flat | 3 signals, 0 up, 2 down, 1 flat | PASS |  | change -0.09%, close location 0.09, OBV falling |
| V | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0878) | PASS |  |  |
| V | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| V | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.24× / 0.04× | 1.24× / 0.04× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| V | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 8407291) | 20 bars, last ('2026-11-20', 8407291) | PASS |  |  |
| VFV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $176.29 | $176.29 | PASS |  |  |
| VFV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $187.74 | $187.74 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VFV.TO | E3 | percent from the 21-day average | 6.1% below | 6.1% below | PASS |  |  |
| VFV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| VFV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $3.34 | $3.34 (sr=3.338) | PASS |  | Wilder ATR14 |
| VFV.TO | E5 | distance in normal day-moves | 3.4 | 3.4 | PASS |  | gauge dot note uses the same number:  · 3.4 day-moves below |
| VFV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $187.74, -6.1% | $187.74, -6.1% | PASS |  |  |
| VFV.TO | L-now | ladder price row = compared price; name = the basis label | $176.29 "Last close" | $176.29 "last close" | PASS |  |  |
| VFV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $180.92, -2.6% | $180.92, -2.6% | PASS |  |  |
| VFV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $190.94, -7.7% | $190.94, -7.7% | PASS |  |  |
| VFV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VFV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 28.7 | 28.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VFV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +8.7% vs +7.0% | 8.7% vs 7.0% | PASS |  |  |
| VFV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VFV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.6 | 22.6 | PASS |  | Wilder, completed bars |
| VFV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 22.6 | PASS |  |  |
| VFV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $176.29 vs $180.92 · -2.6% | $176.29 vs $180.92 · -2.6% | PASS |  |  |
| VFV.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| VFV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $176.29 vs $190.94 · -7.7% | $176.29 vs $190.94 · -7.7% | PASS |  |  |
| VFV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| VFV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.9% over 30 td | +1.9% over 30 td | PASS |  |  |
| VFV.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| VFV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VFV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 10.9% below $197.83 | 10.9% below $197.83 | PASS |  | closing high would be 197.56 |
| VFV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 10.9% below | PASS |  |  |
| VFV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $197.83 | $197.8300018310547 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VFV.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.64%, close location 0.12, OBV falling |
| VFV.TO | V2 | day change of the last completed bar | down 3.6% | -3.64% | PASS |  |  |
| VFV.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.12 (raw 0.1224) | PASS |  |  |
| VFV.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| VFV.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.50× / 1.92× | 3.50× / 1.92× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VFV.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 1190018) | 20 bars, last ('2026-11-20', 1190018) | PASS |  |  |
| VFV.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.50, OBV falling | condition true | PASS |  |  |
| VRT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $166.24 | $166.24 | PASS |  |  |
| VRT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $201.22 | $201.22 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| VRT | E3 | percent from the 21-day average | 17.4% below | 17.4% below | PASS |  |  |
| VRT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| VRT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $16.77 | $16.78 (sr=16.7749) | PASS |  | Wilder ATR14 |
| VRT | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| VRT | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +4.2 | +4.2 | PASS |  |  |
| VRT | L-ema21 | ladder row ema21: price and gap = price vs average | $201.22, -17.4% | $201.22, -17.4% | PASS |  |  |
| VRT | L-note | "Last close $X · date" note = last completed bar | Last close $166.24 · Nov 20 | $166.24 · Nov 20 | PASS |  |  |
| VRT | L-now | ladder price row = compared price; name = the basis label | $166.24 "After hours" | $166.24 "after hours" | PASS |  |  |
| VRT | L-sma200 | ladder row sma200: price and gap = price vs average | $271.48, -38.8% | $271.48, -38.8% | PASS |  |  |
| VRT | L-sma50 | ladder row sma50: price and gap = price vs average | $223.02, -25.5% | $223.02, -25.5% | PASS |  |  |
| VRT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $166.24 / entry $166.24 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| VRT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 2 / 8 | 2 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| VRT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 35.1 | 35.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| VRT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +4.3% vs +7.0% | 4.3% vs 7.0% | PASS |  |  |
| VRT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| VRT | T4 | ADX 14 (S1 /api/sr meta.adx) | 22.7 | 22.7 | PASS |  | Wilder, completed bars |
| VRT | T4w | words "20 or more / below 20" | 20 or more | ADX 22.7 | PASS |  |  |
| VRT | T5 | "counted at the last close ($X, date)" = last completed bar | $166.24, Nov 20 | $166.24, Nov 20 | PASS |  |  |
| VRT | T6 | price vs 200-day average (S1 pattern sma values) | $166.24 vs $271.48 · -38.8% | $166.24 vs $271.48 · -38.8% | PASS |  |  |
| VRT | T6w | word "Below" | Below | Below | PASS |  |  |
| VRT | T7 | price vs 50-day average (S1 pattern sma values) | $166.24 vs $223.02 · -25.5% | $166.24 vs $223.02 · -25.5% | PASS |  |  |
| VRT | T7w | word "Below" | Below | Below | PASS |  |  |
| VRT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.8% over 30 td | +1.8% over 30 td | PASS |  |  |
| VRT | T8r | word "rising" | still rising | rising | PASS |  |  |
| VRT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| VRT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 56.2% below $379.76 | 56.2% below $379.76 | PASS |  | closing high would be 376.06 |
| VRT | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 56.2% below | PASS |  |  |
| VRT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $379.76 | $379.76284762424655 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| VRT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.14%, close location 0.15, OBV falling |
| VRT | V2 | day change of the last completed bar | down 10.1% | -10.14% | PASS |  |  |
| VRT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.15 (raw 0.1465) | PASS |  |  |
| VRT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| VRT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.77× / 1.00× | 1.77× / 1.00× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| VRT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 11987891) | 20 bars, last ('2026-11-20', 11987891) | PASS |  |  |
| VRT | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.77, OBV falling | condition true | PASS |  |  |
| WDC.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $15.83 | $15.83 | PASS |  |  |
| WDC.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $19.05 | $19.05 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WDC.TO | E3 | percent from the 21-day average | 16.9% below | 16.9% below | PASS |  |  |
| WDC.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| WDC.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $1.55 | $1.55 (sr=1.5513) | PASS |  | Wilder ATR14 |
| WDC.TO | E5 | distance in normal day-moves | 2.1 | 2.1 | PASS |  | gauge dot note uses the same number:  · 2.1 day-moves below |
| WDC.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $19.05, -16.9% | $19.05, -16.9% | PASS |  |  |
| WDC.TO | L-now | ladder price row = compared price; name = the basis label | $15.83 "Last close" | $15.83 "last close" | PASS |  |  |
| WDC.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $22.74, -30.4% | $22.74, -30.4% | PASS |  |  |
| WDC.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 34.2 | 34.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WDC.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 33.2 | 33.2 | PASS |  | Wilder, completed bars |
| WDC.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 33.2 | PASS |  |  |
| WDC.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -11.96%, close location 0.14, OBV falling |
| WDC.TO | V2 | day change of the last completed bar | down 12.0% | -11.96% | PASS |  |  |
| WDC.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.14 (raw 0.1436) | PASS |  |  |
| WDC.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| WDC.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.98× / 1.22× | 1.98× / 1.22× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WDC.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 336953) | 20 bars, last ('2026-11-20', 336953) | PASS |  |  |
| WDC.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 1.98, OBV falling | condition true | PASS |  |  |
| WELL | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $240.34 | $240.34 | PASS |  |  |
| WELL | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $241.44 | $241.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WELL | E3 | percent from the 21-day average | 0.5% below | 0.5% below | PASS |  |  |
| WELL | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| WELL | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $5.36 | $5.36 (sr=5.3611) | PASS |  | Wilder ATR14 |
| WELL | E5 | distance in normal day-moves | 0.2 | 0.2 | PASS |  | gauge dot note uses the same number:  · 0.2 day-moves below |
| WELL | L-ema21 | ladder row ema21: price and gap = price vs average | $241.44, -0.5% | $241.44, -0.5% | PASS |  |  |
| WELL | L-note | "Last close $X · date" note = last completed bar | Last close $240.34 · Nov 20 | $240.34 · Nov 20 | PASS |  |  |
| WELL | L-now | ladder price row = compared price; name = the basis label | $240.34 "After hours" | $240.34 "after hours" | PASS |  |  |
| WELL | L-sma200 | ladder row sma200: price and gap = price vs average | $221.34, 8.6% | $221.34, 8.6% | PASS |  |  |
| WELL | L-sma50 | ladder row sma50: price and gap = price vs average | $234.69, 2.4% | $234.69, 2.4% | PASS |  |  |
| WELL | S5-price | S5: the same live price reads the same on the header and the Entry block | header $240.34 / entry $240.34 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| WELL | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 8 / 8 | 8 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WELL | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 50.1 | 50.1 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WELL | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +23.4% vs +7.0% | 23.4% vs 7.0% | PASS |  |  |
| WELL | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WELL | T4 | ADX 14 (S1 /api/sr meta.adx) | 13.2 | 13.2 | PASS |  | Wilder, completed bars |
| WELL | T4w | words "20 or more / below 20" | below 20 | ADX 13.2 | PASS |  |  |
| WELL | T5 | "counted at the last close ($X, date)" = last completed bar | $240.34, Nov 20 | $240.34, Nov 20 | PASS |  |  |
| WELL | T6 | price vs 200-day average (S1 pattern sma values) | $240.34 vs $221.34 · +8.6% | $240.34 vs $221.34 · 8.6% | PASS |  |  |
| WELL | T6w | word "Above" | Above | Above | PASS |  |  |
| WELL | T7 | price vs 50-day average (S1 pattern sma values) | $240.34 vs $234.69 · +2.4% | $240.34 vs $234.69 · 2.4% | PASS |  |  |
| WELL | T7w | word "Above" | Above | Above | PASS |  |  |
| WELL | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +3.8% over 30 td | +3.8% over 30 td | PASS |  |  |
| WELL | T8r | word "rising" | still rising | rising | PASS |  |  |
| WELL | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WELL | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.1% below $253.37 | 5.1% below $253.37 | PASS |  | closing high would be 250.26 |
| WELL | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.1% below | PASS |  |  |
| WELL | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $253.37 | $253.36653380839243 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WELL | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 1 up, 2 down, 0 flat | 3 signals, 1 up, 2 down, 0 flat | PASS |  | change -1.17%, close location 0.06, OBV rising |
| WELL | V2 | day change of the last completed bar | down 1.2% | -1.17% | PASS |  |  |
| WELL | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.06 (raw 0.0574) | PASS |  |  |
| WELL | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| WELL | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.14× / 0.52× | 1.14× / 0.53× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WELL | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3293883) | 20 bars, last ('2026-11-20', 3293883) | PASS |  |  |
| WMT | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $127.95 | $127.95 | PASS |  |  |
| WMT | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $124.5 | $124.50 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| WMT | E3 | percent from the 21-day average | 2.8% above | 2.8% above | PASS |  |  |
| WMT | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| WMT | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.90 | $2.90 (sr=2.8951) | PASS |  | Wilder ATR14 |
| WMT | E5 | distance in normal day-moves | 1.2 | 1.2 | PASS |  | gauge dot note uses the same number:  · 1.2 day-moves above |
| WMT | L-ema21 | ladder row ema21: price and gap = price vs average | $124.5, 2.8% | $124.50, 2.8% | PASS |  |  |
| WMT | L-note | "Last close $X · date" note = last completed bar | Last close $127.95 · Nov 20 | $127.95 · Nov 20 | PASS |  |  |
| WMT | L-now | ladder price row = compared price; name = the basis label | $127.95 "After hours" | $127.95 "after hours" | PASS |  |  |
| WMT | L-sma200 | ladder row sma200: price and gap = price vs average | $118.68, 7.8% | $118.68, 7.8% | PASS |  |  |
| WMT | L-sma50 | ladder row sma50: price and gap = price vs average | $116.65, 9.7% | $116.65, 9.7% | PASS |  |  |
| WMT | S5-price | S5: the same live price reads the same on the header and the Entry block | header $127.95 / entry $127.95 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| WMT | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 6 / 8 | 6 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| WMT | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 64.0 | 64.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| WMT | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +20.5% vs +7.0% | 20.5% vs 7.0% | PASS |  |  |
| WMT | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| WMT | T4 | ADX 14 (S1 /api/sr meta.adx) | 42.8 | 42.8 | PASS |  | Wilder, completed bars |
| WMT | T4w | words "20 or more / below 20" | 20 or more | ADX 42.8 | PASS |  |  |
| WMT | T5 | "counted at the last close ($X, date)" = last completed bar | $127.95, Nov 20 | $127.95, Nov 20 | PASS |  |  |
| WMT | T6 | price vs 200-day average (S1 pattern sma values) | $127.95 vs $118.68 · +7.8% | $127.95 vs $118.68 · 7.8% | PASS |  |  |
| WMT | T6w | word "Above" | Above | Above | PASS |  |  |
| WMT | T7 | price vs 50-day average (S1 pattern sma values) | $127.95 vs $116.65 · +9.7% | $127.95 vs $116.65 · 9.7% | PASS |  |  |
| WMT | T7w | word "Above" | Above | Above | PASS |  |  |
| WMT | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +0.8% over 30 td | +0.8% over 30 td | PASS |  |  |
| WMT | T8r | word "rising" | still rising | rising | PASS |  |  |
| WMT | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| WMT | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 5.1% below $134.84 | 5.1% below $134.84 | PASS |  | closing high would be 133.88 |
| WMT | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 5.1% below | PASS |  |  |
| WMT | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $134.84 | $134.83720000658067 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| WMT | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 1 down, 0 flat | 3 signals, 2 up, 1 down, 0 flat | PASS |  | change 1.52%, close location 0.22, OBV rising |
| WMT | V2 | day change of the last completed bar | up 1.5% | +1.52% | PASS |  |  |
| WMT | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.22 (raw 0.2212) | PASS |  |  |
| WMT | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| WMT | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 1.88× / 0.67× | 1.88× / 0.67× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| WMT | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 42631719) | 20 bars, last ('2026-11-20', 42631719) | PASS |  |  |
| XCHP.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $91.94 | $91.94 | PASS |  |  |
| XCHP.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $110.45 | $110.45 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XCHP.TO | E3 | percent from the 21-day average | 16.8% below | 16.8% below | PASS |  |  |
| XCHP.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XCHP.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $6.56 | $6.56 (sr=6.5605) | PASS |  | Wilder ATR14 |
| XCHP.TO | E5 | distance in normal day-moves | 2.8 | 2.8 | PASS |  | gauge dot note uses the same number:  · 2.8 day-moves below |
| XCHP.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $110.45, -16.8% | $110.45, -16.8% | PASS |  |  |
| XCHP.TO | L-now | ladder price row = compared price; name = the basis label | $91.94 "Last close" | $91.94 "last close" | PASS |  |  |
| XCHP.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $116.86, -21.3% | $116.86, -21.3% | PASS |  |  |
| XCHP.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $123.63, -25.6% | $123.63, -25.6% | PASS |  |  |
| XCHP.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 3 / 8 | 3 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XCHP.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 30.6 | 30.6 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XCHP.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +40.3% vs +7.0% | 40.3% vs 7.0% | PASS |  |  |
| XCHP.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XCHP.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 32.5 | 32.5 | PASS |  | Wilder, completed bars |
| XCHP.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 32.5 | PASS |  |  |
| XCHP.TO | T6 | price vs 200-day average (S1 pattern sma values) | $91.94 vs $116.86 · -21.3% | $91.94 vs $116.86 · -21.3% | PASS |  |  |
| XCHP.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T7 | price vs 50-day average (S1 pattern sma values) | $91.94 vs $123.63 · -25.6% | $91.94 vs $123.63 · -25.6% | PASS |  |  |
| XCHP.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XCHP.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.9% over 30 td | +4.9% over 30 td | PASS |  |  |
| XCHP.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XCHP.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XCHP.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 43.0% below $161.26 | 43.0% below $161.26 | PASS |  | closing high would be 160.97 |
| XCHP.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 43.0% below | PASS |  |  |
| XCHP.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $161.26 | $161.25523669513825 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XCHP.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -10.90%, close location 0.05, OBV falling |
| XCHP.TO | V2 | day change of the last completed bar | down 10.9% | -10.90% | PASS |  |  |
| XCHP.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.05 (raw 0.0482) | PASS |  |  |
| XCHP.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XCHP.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.65× / 1.53× | 2.65× / 1.53× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XCHP.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 146214) | 20 bars, last ('2026-11-20', 146214) | PASS |  |  |
| XCHP.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.65, OBV falling | condition true | PASS |  |  |
| XDRV.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $36.31 | $36.31 | PASS |  |  |
| XDRV.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $40.54 | $40.54 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XDRV.TO | E3 | percent from the 21-day average | 10.4% below | 10.4% below | PASS |  |  |
| XDRV.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XDRV.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.97 | $0.97 (sr=0.9734) | PASS |  | Wilder ATR14 |
| XDRV.TO | E5 | distance in normal day-moves | 4.3 | 4.3 | PASS |  | gauge dot note uses the same number:  · 4.3 day-moves below |
| XDRV.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +7.2 | +7.2 | PASS |  |  |
| XDRV.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $40.54, -10.4% | $40.54, -10.4% | PASS |  |  |
| XDRV.TO | L-now | ladder price row = compared price; name = the basis label | $36.31 "Last close" | $36.31 "last close" | PASS |  |  |
| XDRV.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $47.56, -23.7% | $47.56, -23.7% | PASS |  |  |
| XDRV.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $43.1, -15.8% | $43.10, -15.8% | PASS |  |  |
| XDRV.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XDRV.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.2 | 31.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XDRV.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -9.4% vs +7.0% | -9.4% vs 7.0% | PASS |  |  |
| XDRV.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XDRV.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 23.4 | 23.4 | PASS |  | Wilder, completed bars |
| XDRV.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 23.4 | PASS |  |  |
| XDRV.TO | T6 | price vs 200-day average (S1 pattern sma values) | $36.31 vs $47.56 · -23.7% | $36.31 vs $47.56 · -23.7% | PASS |  |  |
| XDRV.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T7 | price vs 50-day average (S1 pattern sma values) | $36.31 vs $43.10 · -15.8% | $36.31 vs $43.10 · -15.8% | PASS |  |  |
| XDRV.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XDRV.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -0.9% over 30 td | -0.9% over 30 td | PASS |  |  |
| XDRV.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XDRV.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XDRV.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 40.8% below $61.36 | 40.8% below $61.36 | PASS |  | closing high would be 61.36 |
| XDRV.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 40.8% below | PASS |  |  |
| XDRV.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $61.36 | $61.35662078857422 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XDRV.TO | Z1 | no volume data: the card says so (and the count of empty days is right) and shows no volume numbers | 41 of 50 days empty | 41 of 50 days empty | PASS |  |  |
| XEQT.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $41.97 | $41.97 | PASS |  |  |
| XEQT.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $44.62 | $44.62 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XEQT.TO | E3 | percent from the 21-day average | 5.9% below | 5.9% below | PASS |  |  |
| XEQT.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XEQT.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $0.66 | $0.66 (sr=0.6649) | PASS |  | Wilder ATR14 |
| XEQT.TO | E5 | distance in normal day-moves | 4.0 | 4.0 | PASS |  | gauge dot note uses the same number:  · 4.0 day-moves below |
| XEQT.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $44.62, -5.9% | $44.62, -5.9% | PASS |  |  |
| XEQT.TO | L-now | ladder price row = compared price; name = the basis label | $41.97 "Last close" | $41.97 "last close" | PASS |  |  |
| XEQT.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $43.61, -3.8% | $43.61, -3.8% | PASS |  |  |
| XEQT.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $45.27, -7.3% | $45.27, -7.3% | PASS |  |  |
| XEQT.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 4 / 8 | 4 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XEQT.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 27.7 | 27.7 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XEQT.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +10.5% vs +7.0% | 10.5% vs 7.0% | PASS |  |  |
| XEQT.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XEQT.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.1 | 20.1 | PASS |  | Wilder, completed bars |
| XEQT.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 20.1 | PASS |  |  |
| XEQT.TO | T6 | price vs 200-day average (S1 pattern sma values) | $41.97 vs $43.61 · -3.8% | $41.97 vs $43.61 · -3.8% | PASS |  |  |
| XEQT.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XEQT.TO | T7 | price vs 50-day average (S1 pattern sma values) | $41.97 vs $45.27 · -7.3% | $41.97 vs $45.27 · -7.3% | PASS |  |  |
| XEQT.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XEQT.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +1.6% over 30 td | +1.6% over 30 td | PASS |  |  |
| XEQT.TO | T8r | word "rising" | still rising | rising | PASS |  |  |
| XEQT.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XEQT.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 9.5% below $46.38 | 9.5% below $46.38 | PASS |  | closing high would be 46.27 |
| XEQT.TO | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 9.5% below | PASS |  |  |
| XEQT.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $46.38 | $46.380001068115234 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XEQT.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -3.03%, close location 0.11, OBV falling |
| XEQT.TO | V2 | day change of the last completed bar | down 3.0% | -3.03% | PASS |  |  |
| XEQT.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.11 (raw 0.1135) | PASS |  |  |
| XEQT.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XEQT.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.39× / 1.91× | 3.39× / 1.91× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XEQT.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 3347017) | 20 bars, last ('2026-11-20', 3347017) | PASS |  |  |
| XEQT.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.39, OBV falling | condition true | PASS |  |  |
| XETM.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $53.16 | $53.16 | PASS |  |  |
| XETM.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $65.17 | $65.17 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XETM.TO | E3 | percent from the 21-day average | 18.4% below | 18.4% below | PASS |  |  |
| XETM.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XETM.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.54 | $2.54 (sr=2.5399) | PASS |  | Wilder ATR14 |
| XETM.TO | E5 | distance in normal day-moves | 4.7 | 4.7 | PASS |  | gauge dot note uses the same number:  · 4.7 day-moves below |
| XETM.TO | E6 | off-scale gauge label 50d: real distance in day-moves from the 21-day average | +3.2 | +3.2 | PASS |  |  |
| XETM.TO | E6 | off-scale gauge label 200d: real distance in day-moves from the 21-day average | +5.6 | +5.6 | PASS |  |  |
| XETM.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $65.17, -18.4% | $65.17, -18.4% | PASS |  |  |
| XETM.TO | L-now | ladder price row = compared price; name = the basis label | $53.16 "Last close" | $53.16 "last close" | PASS |  |  |
| XETM.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $79.44, -33.1% | $79.44, -33.1% | PASS |  |  |
| XETM.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $73.35, -27.5% | $73.35, -27.5% | PASS |  |  |
| XETM.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 24.2 | 24.2 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XETM.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | -36.9% vs +7.0% | -36.9% vs 7.0% | PASS |  |  |
| XETM.TO | T3w | words "past year" vs the window used | 211 / 251 bars back | 250-253 bars | PASS |  |  |
| XETM.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 26.8 | 26.8 | PASS |  | Wilder, completed bars |
| XETM.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 26.8 | PASS |  |  |
| XETM.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.39%, close location 0.02, OBV falling |
| XETM.TO | V2 | day change of the last completed bar | down 5.4% | -5.39% | PASS |  |  |
| XETM.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.02 (raw 0.0198) | PASS |  |  |
| XETM.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XETM.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.20× / 1.13× | 3.20× / 1.13× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XETM.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 10644) | 20 bars, last ('2026-11-20', 10644) | PASS |  |  |
| XETM.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 3.20, OBV falling | condition true | PASS |  |  |
| XGD.TO | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $44.38 | $44.38 | PASS |  |  |
| XGD.TO | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $51.44 | $51.44 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XGD.TO | E3 | percent from the 21-day average | 13.7% below | 13.7% below | PASS |  |  |
| XGD.TO | E3w | basis label when no usable live price | (last close) | (last close) | PASS |  |  |
| XGD.TO | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $2.18 | $2.18 (sr=2.1761) | PASS |  | Wilder ATR14 |
| XGD.TO | E5 | distance in normal day-moves | 3.2 | 3.2 | PASS |  | gauge dot note uses the same number:  · 3.2 day-moves below |
| XGD.TO | L-ema21 | ladder row ema21: price and gap = price vs average | $51.44, -13.7% | $51.44, -13.7% | PASS |  |  |
| XGD.TO | L-now | ladder price row = compared price; name = the basis label | $44.38 "Last close" | $44.38 "last close" | PASS |  |  |
| XGD.TO | L-sma200 | ladder row sma200: price and gap = price vs average | $54.97, -19.3% | $54.97, -19.3% | PASS |  |  |
| XGD.TO | L-sma50 | ladder row sma50: price and gap = price vs average | $54.41, -18.4% | $54.41, -18.4% | PASS |  |  |
| XGD.TO | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 1 / 8 | 1 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XGD.TO | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 31.5 | 31.5 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XGD.TO | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +0.4% vs +7.0% | 0.4% vs 7.0% | PASS |  |  |
| XGD.TO | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XGD.TO | T4 | ADX 14 (S1 /api/sr meta.adx) | 20.4 | 20.4 | PASS |  | Wilder, completed bars |
| XGD.TO | T4w | words "20 or more / below 20" | 20 or more | ADX 20.4 | PASS |  |  |
| XGD.TO | T6 | price vs 200-day average (S1 pattern sma values) | $44.38 vs $54.97 · -19.3% | $44.38 vs $54.97 · -19.3% | PASS |  |  |
| XGD.TO | T6w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T7 | price vs 50-day average (S1 pattern sma values) | $44.38 vs $54.41 · -18.4% | $44.38 vs $54.41 · -18.4% | PASS |  |  |
| XGD.TO | T7w | word "Below" | Below | Below | PASS |  |  |
| XGD.TO | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | -1.3% over 30 td | -1.3% over 30 td | PASS |  |  |
| XGD.TO | T8r | word "rising" | not rising | not rising | PASS |  |  |
| XGD.TO | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XGD.TO | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 36.2% below $69.54 | 36.2% below $69.54 | PASS |  | closing high would be 68.70 |
| XGD.TO | T9w | words "Within 25% / More than 25%" vs the real gap | More than 25% below | 36.2% below | PASS |  |  |
| XGD.TO | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $69.54 | $69.54086233267267 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XGD.TO | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 0 up, 3 down, 0 flat | 3 signals, 0 up, 3 down, 0 flat | PASS |  | change -5.15%, close location 0.09, OBV falling |
| XGD.TO | V2 | day change of the last completed bar | down 5.2% | -5.15% | PASS |  |  |
| XGD.TO | V3 | close location words (>=0.75 high, <=0.25 low) | near the day's low | close location 0.09 (raw 0.0925) | PASS |  |  |
| XGD.TO | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | falling | falling (sr says falling) | PASS |  |  |
| XGD.TO | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 2.03× / 1.05× | 2.03× / 1.05× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XGD.TO | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 966794) | 20 bars, last ('2026-11-20', 966794) | PASS |  |  |
| XGD.TO | V9 | caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling | shown, RVOL 2.03, OBV falling | condition true | PASS |  |  |
| XOM | E1 | compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format | $159.99 | $159.99 | PASS |  |  |
| XOM | E2 | 21-day average (EMA span 21 over closes; S1 frontend calculateEMA) | $167.56 | $167.56 | PASS |  | an EMA, so "21-day" is its span, not a 21-bar window |
| XOM | E3 | percent from the 21-day average | 4.5% below | 4.5% below | PASS |  |  |
| XOM | E3w | basis label for a live price (now / pre-market / after hours / last trade ...) | (after hours) | session=post | PASS |  |  |
| XOM | E4 | ATR ("a normal day's move"): Wilder 14 (S1 api.sr.meta.atr) | $4.19 | $4.19 (sr=4.1934) | PASS |  | Wilder ATR14 |
| XOM | E5 | distance in normal day-moves | 1.8 | 1.8 | PASS |  | gauge dot note uses the same number:  · 1.8 day-moves below |
| XOM | L-ema21 | ladder row ema21: price and gap = price vs average | $167.56, -4.5% | $167.56, -4.5% | PASS |  |  |
| XOM | L-note | "Last close $X · date" note = last completed bar | Last close $159.97 · Nov 20 | $159.97 · Nov 20 | PASS |  |  |
| XOM | L-now | ladder price row = compared price; name = the basis label | $159.99 "After hours" | $159.99 "after hours" | PASS |  |  |
| XOM | L-sma200 | ladder row sma200: price and gap = price vs average | $154.9, 3.3% | $154.90, 3.3% | PASS |  |  |
| XOM | L-sma50 | ladder row sma50: price and gap = price vs average | $168.38, -5.0% | $168.38, -5.0% | PASS |  |  |
| XOM | S5-price | S5: the same live price reads the same on the header and the Entry block | header $159.99 / entry $159.99 | identical text | PASS |  | two money formats used to disagree on half-cent prices |
| XOM | T1 | Trend checks N / 8 (S1 pattern_detection.check_trend_template) | 7 / 8 | 7 / 8 | PASS |  | recomputed all 8 criteria from the bars |
| XOM | T2 | RSI 14 (S1 frontend technicalIndicators RSI) | 37.0 | 37.0 | PASS |  | Wilder 14 from closes (tolerance 0.3: 2-decimal closes) |
| XOM | T3 | Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy) | +40.3% vs +7.0% | 40.3% vs 7.0% | PASS |  |  |
| XOM | T3w | words "past year" vs the window used | 251 / 251 bars back | 250-253 bars | PASS |  |  |
| XOM | T4 | ADX 14 (S1 /api/sr meta.adx) | 28.2 | 28.2 | PASS |  | Wilder, completed bars |
| XOM | T4w | words "20 or more / below 20" | 20 or more | ADX 28.2 | PASS |  |  |
| XOM | T5 | "counted at the last close ($X, date)" = last completed bar | $159.97, Nov 20 | $159.97, Nov 20 | PASS |  |  |
| XOM | T6 | price vs 200-day average (S1 pattern sma values) | $159.97 vs $154.90 · +3.3% | $159.97 vs $154.90 · 3.3% | PASS |  |  |
| XOM | T6w | word "Above" | Above | Above | PASS |  |  |
| XOM | T7 | price vs 50-day average (S1 pattern sma values) | $159.97 vs $168.38 · -5.0% | $159.97 vs $168.38 · -5.0% | PASS |  |  |
| XOM | T7w | word "Below" | Below | Below | PASS |  |  |
| XOM | T8 | 200-day average change over N trading days (S1 pattern sma_200_30d_ago) | +4.6% over 30 td | +4.6% over 30 td | PASS |  |  |
| XOM | T8r | word "rising" | still rising | rising | PASS |  |  |
| XOM | T8w | words "N trading days" vs the bars back the code uses | 30 | 30 | PASS |  |  |
| XOM | T9 | 1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w) | 14.6% below $187.33 | 14.6% below $187.33 | PASS |  | closing high would be 186.08 |
| XOM | T9w | words "Within 25% / More than 25%" vs the real gap | Within 25% of | 14.6% below | PASS |  |  |
| XOM | T9x | S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh) | $187.33 | $187.32503 | PASS |  | two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38) |
| XOM | V1 | volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead) | 3 signals, 2 up, 0 down, 1 flat | 3 signals, 2 up, 0 down, 1 flat | PASS |  | change 0.65%, close location 0.47, OBV rising |
| XOM | V2 | day change of the last completed bar | up 0.7% | +0.65% | PASS |  |  |
| XOM | V4 | OBV direction (20-bar OBV vs its average, +/-2% band) | rising | rising (sr says rising) | PASS |  |  |
| XOM | V7 | effort vs result: RVOL and /day change/ / (ATR / price) | 3.17× / 0.25× | 3.17× / 0.25× | PASS |  | ATR % uses the sr price (may be a partial bar) |
| XOM | V8 | "Last 20 days" volume bars = the last 20 completed bars (dates and volumes) | 20 bars, last ('2026-11-20', 44958781) | 20 bars, last ('2026-11-20', 44958781) | PASS |  |  |
